import csv
from collections import defaultdict
from dateutil.parser import parse
from pkg_resources import resource_filename as rscfn

class Ouidx:

    def __init__(self):
        
        cpts = defaultdict(list)
        with open(rscfn("ouidxpy", "cpt.csv"), "r") as fp:
            reader = csv.reader(fp)
            header = next(reader)
            for row in reader:
                d = {"oid": row[0].strip(),
                    "indicator": row[1].strip(),
                    "code": row[2].strip(),
                    "desc": row[3].strip()}
                cpts[d["oid"]].append(d)
        
        icd10pcs = defaultdict(list)
        with open(rscfn("ouidxpy", "icd10pcs.csv"), "r") as fp:
            reader = csv.reader(fp)
            header = next(reader)
            for row in reader:
                tokens = row[2].strip().split()
                d = {"oid": row[0].strip(),
                    "indicator": row[1].strip(),
                    "code": tokens[0],
                    "desc": " ".join(tokens[1:])}
                icd10pcs[d["oid"]].append(d)
        
        icd10cm = defaultdict(list)
        with open(rscfn("ouidxpy", "icd10cm.csv"), "r") as fp:
            reader = csv.reader(fp)
            header = next(reader)
            for row in reader:
                is_incl = row[2] == "x"
                is_excl = row[3] == "x"
                tokens = row[4].strip().split()
                codes = tokens[0].split("-")
                d = {"oid": row[0].strip(),
                    "indicator": row[1].strip(),
                    "include": is_incl,
                    "exclude": is_excl,
                    "start": codes[0].replace(".",""),
                    "end": codes[-1].replace(".",""),
                    "desc": " ".join(tokens[1:])}
                icd10cm[d["oid"]].append(d)

        defs = {}
        with open(rscfn("ouidxpy", "definitions.csv"), "r", 
                    encoding="ISO-8859-1") as fp:
            reader = csv.reader(fp)
            header = next(reader)
            for row in reader:
                defs[row[0]] = {
                        "name": row[1].strip(),
                        "motivator": row[2].strip(),
                        "description": row[3].strip(),
                        "algorithm": row[4].strip(),
                        "event_type": row[5].strip()}
        self.cpts = cpts
        self.icd10pcs = icd10pcs
        self.icd10cm = icd10cm
        self.defs = defs

    def _idx_logic(self, 
                oid, 
                event_settings,
                min_age,
                min_dos_diff,
                max_dos_diff,
                claims, 
                age):
        
        # Idx "oid"
        # Filter age
        # Match
        #   - event_setting
        #   - cpt or icd10_pcs
        #   - inclusion dx
        # Check
        #   - exclusion dx in a specified window
        # If no exclusion dx, then Over-utilized
        out = {"oid": oid,
                "name": self.defs[oid]["name"],
                "motivator": self.defs[oid]["motivator"],
                "evidence": [], "cnt": 0}

        if age < min_age:
            return out

        ref_events = []
        cpt_target = {x["code"] for x in self.cpts[oid]}
        icd10_pcs_target = {x["code"] for x in self.icd10pcs[oid]}
        dx_incl = [(x["start"], x["end"]) for x in self.icd10cm[oid]
                    if x["include"]]
        dx_excl = [(x["start"], x["end"]) for x in self.icd10cm[oid]
                        if x["exclude"]]
        
        for claim in claims:
            
            es_match = claim.get("event_setting", "") in event_settings
            
            proc_match = False 
            if oid == "5":
                proc_match = any((x in icd10_pcs_target) 
                                for x in claim.get("icd10_pcs",[]))
                if (("74150" in claim.get("cpt",[]) and 
                        "74160" in claim.get("cpt",[])) or 
                    "74170" in claim.get("cpt",[])):
                    proc_match = True
            else:
                proc_match = (any((x in cpt_target) 
                            for x in claim.get("cpt", [])) or
                        any((x in icd10_pcs_target)
                            for x in claim.get("icd10_pcs",[])))
            
            dx_match = (len(dx_incl) == 0) # if no dx_incl, then True
            for dx in claim.get("icd10_cm", []):
                if dx_match:
                    break
                for dx_range in dx_incl:
                    ndx = len(dx_range[0])
                    if dx_range[0] <= dx[:ndx] <= dx_range[1]:
                        dx_match = True
                        break
            if (es_match and proc_match and dx_match):
                ref_events.append(claim)
         
        dos0 = "1970-01-01"
        for ref_event in ref_events:
            has_exclusion = False
            dos_ref = parse(ref_event.get("date_of_service", dos0))
            for claim in claims:
                dos_claim = parse(claim.get("date_of_service", dos0))
                dos_diff = (dos_ref - dos_claim).days
                within_range = (dos_diff >= min_dos_diff and 
                                dos_diff <= max_dos_diff) 
                if not within_range:
                    continue
                dx_match = False
                for dx in claim.get("icd10_cm", []):
                    if dx_match:
                        break
                    for dx_range in dx_excl:
                        ndx = len(dx_range[0])
                        if dx_range[0] <= dx[:ndx] <= dx_range[1]:
                            dx_match = True
                            break
                if within_range and dx_match: 
                    has_exclusion = True
                    break
            
            if not has_exclusion:
                out["evidence"].append(ref_event.copy())

        out["cnt"] = len(out["evidence"])
        return out

    def get_idx(self, claims, age=65):
      
        """
        claims = [
            {"date_of_service": "YYYY-MM-DD",
            "icd10_pcs": [],
            "icd10_cm": [],
            "cpt": [],
            "event_setting": "ip" # "op", "ed", "other"
            }, ...]
        """
        out = {}
        
        # NOTE: If no min age, put 0 on the age variable.
        out["oid1"] = self._idx_logic("1", {"op"}, 0, 0, 180, claims, age)
        # NOTE: For Oid=2, exclusion dx gets applied to the claims 
        #   a day before the target event. This may create some 
        #   discrepancies with the original implementation.
        out["oid2"] = self._idx_logic("2", {"ip", "op", "ed"}, 5, 1, 30, 
                                    claims, age)
        # NOTE: If no exclusion dx, we give (0, 0) on the dos_diff pair.
        out["oid3"] = self._idx_logic("3", {"op", "ed"}, 0, 0, 0, 
                                    claims, age)
        out["oid4"] = self._idx_logic("4", {"ip", "op", "ed"}, 
                                    0, 0, 180, claims, age)
        out["oid5"] = self._idx_logic("5", {"ip", "op", "ed"}, 0, 0, 0,
                                    claims, age) 
        out["oid7"] = self._idx_logic("7", {"op", "ed"}, 0, 0, 60, 
                                    claims, age) 
        out["oid8"] = self._idx_logic("8", {"ip", "op", "ed"}, 0, 0, 0,
                                    claims, age) 
        out["oid9"] = self._idx_logic("9", {"ip", "op", "ed"}, 0, 0, 0,
                                    claims, age) 
        out["oid10"] = self._idx_logic("10", {"ip", "op", "ed"}, 0, 0, 60,
                                    claims, age) 
        out["oid11"] = self._idx_logic("11", {"ip", "op", "ed"}, 0, 0, 60,
                                    claims, age) 
        out["oid12"] = self._idx_logic("12", {"op"}, 0, 0, 180,
                                claims, age) 
        # NOTE: The SAS script doesn't address the exclusion Dx for Oid=13.
        #   We apply those with the same DoS.
        out["oid13"] = self._idx_logic("13", {"op"}, 65, 0, 0,
                                    claims, age) 
        out["oid14"] = self._idx_logic("14", {"op"}, 85, 0, 0,
                                    claims, age) 
        out["oid15"] = self._idx_logic("15", {"op"}, 80, 0, 0,
                                    claims, age) 
        out["oid16"] = self._idx_logic("16", {"op"}, 0, 0, 180,
                                    claims, age) 
        out["oid17"] = self._idx_logic("17", {"ip", "op"}, 0, 0, 0,
                                    claims, age) 
        out["oid18"] = self._idx_logic("18", {"ip"}, 0, 0, 0,
                                    claims, age) 

        oid_score = 0
        for oid in out.keys():
            oid_score += out[oid]["cnt"]

        out["score"] = oid_score
 
        return out


    

