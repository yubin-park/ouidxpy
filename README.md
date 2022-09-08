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
{'oid1': {'cnt': 1,
          'evidence': [{'cpt': ['71045'],
                        'date_of_service': '2022-06-01',
                        'event_setting': 'op',
                        'icd10_cm': ['Z0181']}],
          'motivator': 'Motivator: this is of little clinical value and leads '
                       'to cascades of harm',
          'name': 'Preoperative chest radiography in the absence of a clinical '
                  'suspicion for intrathoracic pathology',
          'oid': '1'},
 'oid10': {'cnt': 0,
           'evidence': [],
           'motivator': 'Motivator: there are too many lumbar laminectomies '
                        'done for back pain; they largely should never happen '
                        'except for radicular pain or weakness.',
           'name': 'Laminectomy and/or spinal fusion',
           'oid': '10'},
 'oid11': {'cnt': 0,
           'evidence': [],
           'motivator': 'Motivator: partial meniscectomy or meniscus repair or '
                        'placement of an artificial meniscus have little value '
                        'in patients with DJD of the knee',
           'name': 'Meniscectomy in patients with DJD of the knee',
           'oid': '11'},
 'oid12': {'cnt': 0,
           'evidence': [],
           'motivator': 'Motivator: patients with acute sinusitis should not '
                        'be rushed to nasal endoscopy; this would only be '
                        'indicated for chronic sinusitis',
           'name': 'Nasal endoscopy for sinusitis diagnosis',
           'oid': '12'},
 'oid13': {'cnt': 0,
           'evidence': [],
           'motivator': 'Motivator: there is no reduction in morbidity and '
                        'mortality with cervical cancer screening in women at '
                        'low risk of cervical cancer',
           'name': 'Use of routine cervical cytology (Pap tests) in women over '
                   '65 years',
           'oid': '13'},
 'oid14': {'cnt': 0,
           'evidence': [],
           'motivator': 'Motivator: women over age 85 have slowly growing '
                        'cancers and do not benefit form screening given short '
                        'life expectancy',
           'name': 'Screening mammography in women 85 years and older',
           'oid': '14'},
 'oid15': {'cnt': 0,
           'evidence': [],
           'motivator': 'Motivator: patients with expected longevity of less '
                        'than 10 years do not benefit from screening for colon '
                        'cancer',
           'name': 'Screening for colorectal cancer in adults 80 years and '
                   'older',
           'oid': '15'},
 'oid16': {'cnt': 0,
           'evidence': [],
           'motivator': 'Motivator: screening asymptomatic patients has not '
                        'been demonstrated to prevent stroke',
           'name': 'Screening for asymptomatic carotid artery stenosis (CAS) '
                   'in individuals over age 80 years',
           'oid': '16'},
 'oid17': {'cnt': 0,
           'evidence': [],
           'motivator': 'Motivator: digoxin monitoring should not be done '
                        'routinely; it should only be done if there is concern '
                        'about digoxin toxicity',
           'name': 'Routine monitoring of digoxin in patients with congestive '
                   'heart failure',
           'oid': '17'},
 'oid18': {'cnt': 0,
           'evidence': [],
           'motivator': 'Motivator: this seldom yields a diagnosis of seizures '
                        'in this population',
           'name': 'EEG monitoring in individuals presenting with syncope',
           'oid': '18'},
 'oid2': {'cnt': 0,
          'evidence': [],
          'motivator': 'Motivator: Ottowa rules work very well. Where they do '
                       'not apply, plain film radiography is the first '
                       'appropriate study.',
          'name': 'Imaging in acute foot trauma',
          'oid': '2'},
 'oid3': {'cnt': 0,
          'evidence': [],
          'motivator': 'Motivator: patients with mild TBI are unlikely to have '
                       'a brain hemorrhage',
          'name': 'MRI in individuals with mild traumatic brain injury',
          'oid': '3'},
 'oid4': {'cnt': 0,
          'evidence': [],
          'motivator': 'Motivator: sinus CT adds little information that will '
                       'change management of acute sinusitis',
          'name': 'DonÕt order sinus computed tomography (CT) for '
                  'uncomplicated acute rhinosinusitis.',
          'oid': '4'},
 'oid5': {'cnt': 0,
          'evidence': [],
          'motivator': 'Motivator: If one has the results of an abdominal CT '
                       'with contrast, there is no added information on doing '
                       'and billing for one without contrast',
          'name': 'Abdomen CT use of contrast material (w and w/o)',
          'oid': '5'},
 'oid7': {'cnt': 0,
          'evidence': [],
          'motivator': 'Motivator: MRIÕs are used too early and too often for '
                       'mechanical low back pain; they are only indicated when '
                       'there are red flags or radicular symptoms where there '
                       'might be need for intervention',
          'name': 'MRI Lumbar Spine for Low Back Pain',
          'oid': '7'},
 'oid8': {'cnt': 0,
          'evidence': [],
          'motivator': 'Motivator: traction has little evidence base for low '
                       'back pain treatment.',
          'name': 'Traction for low back pain',
          'oid': '8'},
 'oid9': {'cnt': 0,
          'evidence': [],
          'motivator': 'Motivator: there are too many hysterectomies performed '
                       'for benign disease that could be managed more '
                       'conservatively',
          'name': 'Hysterectomy for benign disease',
          'oid': '9'},
 'score': 1}
```

