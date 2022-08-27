import unittest
from ouidxpy.ouidx import Ouidx

class TestOuidx(unittest.TestCase):

    def test_idx1(self):
        oi = Ouidx()
        claims = [{"date_of_service": "2022-06-01",
                    "cpt": ["71045"],
                    "icd10_cm": ["Z0181"], 
                    "event_setting": "op"},
                    {"date_of_service": "2022-07-01",
                    "icd10_cm": ["K00"]}]
        res = oi.get_idx(claims)
        print(res)

if __name__=="__main__":
    unittest.main()
