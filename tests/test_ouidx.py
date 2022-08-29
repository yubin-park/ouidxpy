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
        res = oi.get_idx(claims)
        self.assertEqual(len(res["oid1"]), 0)
        
        # overuse case
        claims = [{"date_of_service": "2022-06-01",
                    "cpt": ["71045"],
                    "icd10_cm": ["Z0181"], 
                    "event_setting": "op"}]

        res = oi.get_idx(claims)
        self.assertEqual(len(res["oid1"]), 1)
    
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
        self.assertEqual(len(res["oid2"]), 0)
        
        # overuse case
        claims = [{"date_of_service": "2022-06-01",
                    "cpt": ["73700"],
                    "icd10_cm": ["S90"], 
                    "event_setting": "ed"}]
        res = oi.get_idx(claims)
        self.assertEqual(len(res["oid2"]), 1)

    def test_idx3(self):
        
        oi = Ouidx()
        # proper case
        claims = [{"date_of_service": "2022-06-01",
                    "cpt": ["70551"],
                    "icd10_cm": ["S06"], 
                    "event_setting": "ed"}]
        res = oi.get_idx(claims)
        self.assertEqual(len(res["oid3"]), 0)
        
        # overuse case
        claims = [{"date_of_service": "2022-06-01",
                    "cpt": ["70551"],
                    "icd10_cm": ["S060X0A"], 
                    "event_setting": "ed"}]
        res = oi.get_idx(claims)
        self.assertEqual(len(res["oid3"]), 1)
 
    def test_idx4(self):
        oi = Ouidx()
        # proper case
        claims = [{"date_of_service": "2022-06-01",
                    "cpt": ["70486"],
                    "icd10_cm": ["J0100"], 
                    "event_setting": "op"},
                    {"date_of_service": "2022-01-01",
                    "icd10_cm": ["J320"]}]
        res = oi.get_idx(claims)
        self.assertEqual(len(res["oid3"]), 0)
        
        # overuse case
        claims = [{"date_of_service": "2022-06-01",
                    "cpt": ["70486"],
                    "icd10_cm": ["J0100"], 
                    "event_setting": "op"}]
        res = oi.get_idx(claims)
        self.assertEqual(len(res["oid4"]), 1)
    
    def test_idx5(self):
        oi = Ouidx()
        # proper case
        claims = [{"date_of_service": "2022-06-01",
                    "cpt": ["74160"],
                    "event_setting": "op"},
                    {"date_of_service": "2022-01-01",
                    "icd10_cm": ["J320"]}]
        res = oi.get_idx(claims)
        self.assertEqual(len(res["oid5"]), 0)
        
        # overuse case
        claims = [{"date_of_service": "2022-06-01",
                    "cpt": ["74160", "74150"],
                    "icd10_cm": ["J0100"], 
                    "event_setting": "op"}]
        res = oi.get_idx(claims)
        self.assertEqual(len(res["oid5"]), 1)
        
    def test_idx7(self):
        oi = Ouidx()
        # proper case
        claims = [{"date_of_service": "2022-06-01",
                    "cpt": ["72148"],
                    "icd10_cm": ["M545"],
                    "event_setting": "op"},
                    {"date_of_service": "2022-05-01",
                    "icd10_cm": ["C45"]}]
        res = oi.get_idx(claims)
        self.assertEqual(len(res["oid7"]), 0)
        
        # overuse case
        claims = [{"date_of_service": "2022-06-01",
                    "cpt": ["72148"],
                    "icd10_cm": ["M545"],
                    "event_setting": "op"},
                    {"date_of_service": "2022-05-01",
                    "icd10_cm": ["C44"]}]
        res = oi.get_idx(claims)
        self.assertEqual(len(res["oid7"]), 1)
 
    def test_idx8(self):
        oi = Ouidx()
        # proper case
        claims = [{"date_of_service": "2022-06-01",
                    "cpt": ["97012"],
                    "event_setting": "op"}]
        res = oi.get_idx(claims)
        self.assertEqual(len(res["oid8"]), 0)
        
        # overuse case
        claims = [{"date_of_service": "2022-06-01",
                    "cpt": ["97012"],
                    "icd10_cm": ["M545"],
                    "event_setting": "op"}]
        res = oi.get_idx(claims)
        self.assertEqual(len(res["oid8"]), 1)
 
    def test_idx9(self):
        oi = Ouidx()
        # proper case
        claims = [{"date_of_service": "2022-06-01",
                    "cpt": ["58150"],
                    "icd10_cm": ["C54"],
                    "event_setting": "op"}]
        res = oi.get_idx(claims)
        self.assertEqual(len(res["oid9"]), 0)
        
        # overuse case
        claims = [{"date_of_service": "2022-06-01",
                    "cpt": ["58150"],
                    "icd10_cm": ["M545"],
                    "event_setting": "op"}]
        res = oi.get_idx(claims)
        self.assertEqual(len(res["oid9"]), 1)
 

if __name__=="__main__":
    unittest.main()
