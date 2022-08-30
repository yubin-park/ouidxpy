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
 
    def test_idx10(self):
        oi = Ouidx()
        # proper case
        claims = [{"date_of_service": "2022-06-01",
                    "cpt": ["22558"],
                    "icd10_cm": ["M545"],
                    "event_setting": "op"},
                    {"date_of_service": "2022-05-01",
                    "icd10_cm": ["M543"],
                    "event_setting": "op"}
                    ]
        res = oi.get_idx(claims)
        self.assertEqual(len(res["oid10"]), 0)
        
        # overuse case
        claims = [{"date_of_service": "2022-06-01",
                    "cpt": ["22558"],
                    "icd10_cm": ["M545"],
                    "event_setting": "op"}]
        res = oi.get_idx(claims)
        self.assertEqual(len(res["oid10"]), 1)
 
    def test_idx11(self):
        oi = Ouidx()
        # proper case
        claims = [{"date_of_service": "2022-06-01",
                    "cpt": ["29881"],
                    "icd10_cm": ["M17"],
                    "event_setting": "op"},
                    {"date_of_service": "2022-05-01",
                    "icd10_cm": ["VOO"],
                    "event_setting": "op"}
                    ]
        res = oi.get_idx(claims)
        self.assertEqual(len(res["oid11"]), 0)
        
        # overuse case
        claims = [{"date_of_service": "2022-06-01",
                    "cpt": ["29881"],
                    "icd10_cm": ["M17"],
                    "event_setting": "op"}]
        res = oi.get_idx(claims)
        self.assertEqual(len(res["oid11"]), 1)

    def test_idx12(self):
        oi = Ouidx()
        # proper case
        claims = [{"date_of_service": "2022-06-01",
                    "cpt": ["31231"],
                    "icd10_cm": ["J0100"],
                    "event_setting": "op"},
                    {"date_of_service": "2022-05-01",
                    "icd10_cm": ["J320"],
                    "event_setting": "op"}
                    ]
        res = oi.get_idx(claims)
        self.assertEqual(len(res["oid12"]), 0)
        
        # overuse case
        claims = [{"date_of_service": "2022-06-01",
                    "cpt": ["31231"],
                    "icd10_cm": ["J0110"],
                    "event_setting": "op"}]
        res = oi.get_idx(claims)
        self.assertEqual(len(res["oid12"]), 1)
    
    def test_idx13(self):
        oi = Ouidx()
        # proper case
        claims = [{"date_of_service": "2022-06-01",
                    "cpt": ["G0144"],
                    "icd10_cm": ["Z124"],
                    "event_setting": "op"},
                    {"date_of_service": "2022-06-01",
                    "icd10_cm": ["C53"],
                    "event_setting": "op"}
                    ]
        res = oi.get_idx(claims, 65)
        self.assertEqual(len(res["oid13"]), 0)
        
        # overuse case
        claims = [{"date_of_service": "2022-06-01",
                    "cpt": ["G0145"],
                    "icd10_cm": ["Z1151"],
                    "event_setting": "op"}]
        res = oi.get_idx(claims, 66)
        self.assertEqual(len(res["oid13"]), 1)
 
    def test_idx14(self):
        oi = Ouidx()
        # proper case
        claims = [{"date_of_service": "2022-06-01",
                    "cpt": ["G0202"],
                    "icd10_cm": ["Z1231"],
                    "event_setting": "op"}]
        res = oi.get_idx(claims, 65)
        self.assertEqual(len(res["oid14"]), 0)
        
        # overuse case
        claims = [{"date_of_service": "2022-06-01",
                    "cpt": ["G0202"],
                    "icd10_cm": ["Z1231"],
                    "event_setting": "op"}]
        res = oi.get_idx(claims, 86)
        self.assertEqual(len(res["oid14"]), 1)
 
    def test_idx15(self):
        oi = Ouidx()
        # proper case
        claims = [{"date_of_service": "2022-06-01",
                    "cpt": ["45380"],
                    "icd10_cm": ["Z1211"],
                    "event_setting": "op"}]
        res = oi.get_idx(claims, 65)
        self.assertEqual(len(res["oid15"]), 0)
        
        # overuse case
        claims = [{"date_of_service": "2022-06-01",
                    "cpt": ["45330"],
                    "icd10_cm": ["Z1211"],
                    "event_setting": "op"}]
        res = oi.get_idx(claims, 81)
        self.assertEqual(len(res["oid15"]), 1)
    
    def test_idx16(self):
        oi = Ouidx()
        # proper case
        claims = [{"date_of_service": "2022-06-01",
                    "cpt": ["93880"],
                    "event_setting": "op"},
                {"date_of_service": "2022-05-01",
                    "icd10_cm": ["I64"],
                    "event_setting": "op"}
                    ]
        res = oi.get_idx(claims, 65)
        self.assertEqual(len(res["oid16"]), 0)
        
        # overuse case
        claims = [{"date_of_service": "2022-06-01",
                    "cpt": ["3100F"],
                    "event_setting": "op"}]
        res = oi.get_idx(claims, 81)
        self.assertEqual(len(res["oid16"]), 1)
 
    def test_idx17(self):
        oi = Ouidx()
        # proper case
        claims = [{"date_of_service": "2022-06-01",
                    "cpt": ["80162"],
                    "icd10_cm": ["I50"],
                    "event_setting": "op"},
                {"date_of_service": "2022-06-01",
                    "icd10_cm": ["T460X2"],
                    "event_setting": "op"}
                    ]
        res = oi.get_idx(claims, 65)
        self.assertEqual(len(res["oid17"]), 0)
        
        # overuse case
        claims = [{"date_of_service": "2022-06-01",
                    "cpt": ["80162"],
                    "icd10_cm": ["I50"],
                    "event_setting": "op"}]
        res = oi.get_idx(claims, 81)
        self.assertEqual(len(res["oid17"]), 1)
 
    def test_idx18(self):
        oi = Ouidx()
        # proper case
        claims = [{"date_of_service": "2022-06-01",
                    "cpt": ["95816"],
                    "event_setting": "ip"}
                    ]
        res = oi.get_idx(claims, 65)
        self.assertEqual(len(res["oid17"]), 0)
        
        # overuse case
        claims = [{"date_of_service": "2022-06-01",
                    "cpt": ["95816"],
                    "icd10_cm": ["R559"],
                    "event_setting": "ip"}]
        res = oi.get_idx(claims, 81)
        self.assertEqual(len(res["oid18"]), 1)


 
if __name__=="__main__":
    unittest.main()
