import unittest
from ouidxpy.ouidx import Ouidx

class TestOuidx(unittest.TestCase):

    def test_idx1(self):
        oi = Ouidx()
        # proper case
        claims = [{"date_of_service": "2022-06-01",
                    "cpt": ["71045"],
                    "icd10_cm": ["Z0181"], 
                    "event_setting": "op"},
                    {"date_of_service": "2022-01-01",
                    "icd10_cm": ["J00"]}]
        #res = oi.get_idx(claims)
        #print(res) 
        # overuse case
        claims = [{"date_of_service": "2022-06-01",
                    "cpt": ["71045"],
                    "icd10_cm": ["Z0181"], 
                    "event_setting": "op"}]

        #res = oi.get_idx(claims)
        #print(res)
    
    def test_idx2(self):
         
        oi = Ouidx()
        # proper case
        claims = [{"date_of_service": "2022-06-01",
                    "cpt": ["73700"],
                    "icd10_cm": ["S90"], 
                    "event_setting": "ed"},
                    {"date_of_service": "2022-05-10",
                    "icd10_cm": ["S90"]}]
        res = oi.get_idx(claims)
        print(res)
        
        # overuse case
        claims = [{"date_of_service": "2022-06-01",
                    "cpt": ["73700"],
                    "icd10_cm": ["S90"], 
                    "event_setting": "ed"}]
        res = oi.get_idx(claims)
        print(res)

if __name__=="__main__":
    unittest.main()
