import csv
from collections import defaultdict

class Ouidx:

    def __init__(self):
        
        cpts = defaultdict(list)
        with open("cpt.csv", "r") as fp:
            reader = csv.reader(fp)
            header = next(reader)
            for row in reader:
                d = {"oid": row[0].strip(),
                    "indicator": row[1].strip(),
                    "code": row[2].strip(),
                    "desc": row[3].strip()}
                cpts[d["oid"]].append(d)
        
        icd10pcs = defaultdict(list)
        with open("icd10pcs.csv", "r") as fp:
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
        with open("icd10cm.csv", "r") as fp:
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
        with open("definitions.csv", "r", encoding="ISO-8859-1") as fp:
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
        
        # Idx 1
        for claim in claims:
            # detect "op" and having the cpt or icd10_pcs and inclusion dx
            # go back 180 days window
            # find claims with exclusion dx => if none, then OU
            break

        # Idx 2

        return {}


if __name__ == "__main__":

    ouidx = Ouidx()
    

