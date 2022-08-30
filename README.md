# ouidxpy

Overuse Index Python version

This project is based on [Overuse-Index-Segal-et-al-Johns-Hopkins-University-ICD-10-Coding](https://github.com/susanmhutfless/Overuse-Index-Segal-et-al-Johns-Hopkins-University-ICD-10-Coding).

I made it usable as a Python library with some assumptions.

Please contact me if you want to properly use the package.

The implementation is not exactly the same as the paper. Many custom assumptions are baked in, so please use this at your discretion.

## Install

`pyproject.toml` is still in BETA

Use `setup.cfg`

`>>> from ouidxpy.ouidx import Ouidx`

## How to Use

```

from ouidxpy.ouidx import Ouidx

oi = Ouidx()

# overuse case
claims = [{"date_of_service": "2022-06-01",
                    "cpt": ["71045"],
                    "icd10_cm": ["Z0181"], 
                    "event_setting": "op"}]


res = oi.get_idx(claims)
from pprint import pprint
pprint(res) 

```
The output would be:
```
>>> pprint(res)
defaultdict(<class 'list'>,
            {'oid1': [{'cpt': ['71045'],
                       'date_of_service': '2022-06-01',
                       'event_setting': 'op',
                       'icd10_cm': ['Z0181']}],
             'oid10': [],
             'oid11': [],
             'oid12': [],
             'oid13': [],
             'oid14': [],
             'oid15': [],
             'oid16': [],
             'oid17': [],
             'oid18': [],
             'oid2': [],
             'oid3': [],
             'oid4': [],
             'oid5': [],
             'oid7': [],
             'oid8': [],
             'oid9': [],
             'score': 1})
```

