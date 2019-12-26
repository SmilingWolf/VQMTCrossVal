# VQMTCrossVal
Cross validation for objective quality metric measurement tools on multiple public datasets

Datasets used:
- CSIQ: http://vision.eng.shizuoka.ac.jp/mod/page/view.php?id=23
- IVC: http://www2.irccyn.ec-nantes.fr/ivcdb/
- JPEG XR: https://www.epfl.ch/labs/mmspg/research/page-58317-en-html/page-58332-en-html/page-58333-en-html/iqa/
- KADID10k: http://database.mmsp-kn.de/kadid-10k-database.html
- LIVE2: https://live.ece.utexas.edu/research/quality/subjective.htm
- TID2013: http://www.ponomarenko.info/tid2013.htm

## SROCC

CSIQ:

|             |     dmos |
|-------------|----------|
| DSSIM       | **0.946151** |
| SSIMULACRA  | 0.847857 |
| Butteraugli | 0.902055 |

IVC:

|             |       mos |
|-------------|-----------|
| DSSIM       | **-0.915765** |
| SSIMULACRA  | -0.834436 |
| Butteraugli | -0.79186  |

JPEG XR:

|             |       mos |
|-------------|-----------|
| DSSIM       | **-0.9035**   |
| SSIMULACRA  | -0.840177 |
| Butteraugli | -0.87797  |

KADID10k:

|             |      dmos |
|-------------|-----------|
| DSSIM       | **-0.856177** |
| SSIMULACRA  | -0.699555 |
| Butteraugli | -0.735086 |

LIVE2:

|             |   dmos_new |
|-------------|------------|
| DSSIM       |   **0.95493**  |
| SSIMULACRA  |   0.913573 |
| Butteraugli |   0.899623 |

TID2013:

|             |       mos |
|-------------|-----------|
| DSSIM       | **-0.860908** |
| SSIMULACRA  | -0.6733   |
| Butteraugli | -0.760307 |
