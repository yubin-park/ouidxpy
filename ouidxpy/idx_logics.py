from dateutil.parser import parse

def idx1(claims, cpts, icd10pcs, icd10cm):
    # Idx 1
    # detect "op" and having the cpt or icd10_pcs and inclusion dx
    # go back 180 days window
    # find claims with exclusion dx => if none, then OU
    out = [] 
    oid = "1"
    ref_events = []
    cpt_target = {x["code"] for x in cpts[oid]}
    icd10_pcs_target = {x["code"] for x in icd10pcs[oid]}
    dx_incl = [(x["start"], x["end"]) for x in icd10cm[oid]
                if x["include"]]
    dx_excl = [(x["start"], x["end"]) for x in icd10cm[oid]
                    if x["exclude"]]
    
    for claim in claims:
        setting_match = claim.get("event_setting", "") == "op"
        proc_match = any(x in cpt_target for x in claim.get("cpt", []))
        proc_match = proc_match or any(x in icd10_pcs_target 
                        for x in claim.get("icd10_pcs",[]))
        dx_match = False
        for dx in claim.get("icd10_cm", []):
            if dx_match:
                break
            for dx_range in dx_incl:
                if dx_range[0] <= dx <= dx_range[1]:
                    dx_match = True
        if (setting_match and proc_match and dx_match):
            ref_events.append(claim)

    for ref_event in ref_events:
        # 180 days window before ref_event
        has_exclusion = False
        dos_ref = parse(ref_event.get("date_of_service", "1970-01-01"))
        for claim in claims:
            dos_claim = parse(claim.get("date_of_service", "1970-01-01"))
            dos_diff = (dos_ref - dos_claim).days
            within_range = (dos_diff >= 0 and dos_diff < 180) 
            if not within_range:
                continue
            dx_match = False
            for dx in claim.get("icd10_cm", []):
                if dx_match:
                    break
                for dx_range in dx_excl:
                    if dx_range[0] <= dx <= dx_range[1]:
                        dx_match = True
                        break
            if within_range and dx_match: 
                has_exclusion = True
                break
        if not has_exclusion:
            out.append(ref_event)

    return out


