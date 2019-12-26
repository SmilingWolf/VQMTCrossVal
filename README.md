# VQMTCrossVal
Cross validation of objective quality metric measurement tools on multiple public datasets

Datasets used:
- CSIQ: http://vision.eng.shizuoka.ac.jp/mod/page/view.php?id=23
- IVC: http://www2.irccyn.ec-nantes.fr/ivcdb/
- JPEG XR: https://www.epfl.ch/labs/mmspg/research/page-58317-en-html/page-58332-en-html/page-58333-en-html/iqa/
- KADID-10k: http://database.mmsp-kn.de/kadid-10k-database.html
- LIVE2: https://live.ece.utexas.edu/research/quality/subjective.htm
- TID2013: http://www.ponomarenko.info/tid2013.htm

## Results

CSIQ:

|             |   PLCC |   SROCC |   KROCC |
|-------------|--------|---------|---------|
| DSSIM       |  **0.803** |   **0.946** |   **0.793** |
| SSIMULACRA  |  0.793 |   0.848 |   0.644 |
| Butteraugli |  0.767 |   0.902 |   0.722 |

IVC:

|             |   PLCC |   SROCC |   KROCC |
|-------------|--------|---------|---------|
| DSSIM       | -0.758 |  **-0.916** |  **-0.748** |
| SSIMULACRA  | **-0.789** |  -0.834 |  -0.64  |
| Butteraugli | -0.607 |  -0.792 |  -0.595 |

JPEG XR:

|             |   PLCC |   SROCC |   KROCC |
|-------------|--------|---------|---------|
| DSSIM       | -0.833 |  **-0.904** |  **-0.725** |
| SSIMULACRA  | **-0.849** |  -0.84  |  -0.656 |
| Butteraugli | -0.836 |  -0.878 |  -0.696 |

KADID-10k:

|             |   PLCC |   SROCC |   KROCC |
|-------------|--------|---------|---------|
| DSSIM       | **-0.639** |  **-0.856** |  **-0.67**  |
| SSIMULACRA  | -0.623 |  -0.7   |  -0.508 |
| Butteraugli | -0.605 |  -0.735 |  -0.546 |

LIVE2:

|             |   PLCC |   SROCC |   KROCC |
|-------------|--------|---------|---------|
| DSSIM       |  0.576 |   **0.955** |   **0.813** |
| SSIMULACRA  |  **0.783** |   0.914 |   0.74  |
| Butteraugli |  0.699 |   0.9   |   0.718 |

TID2013:

|             |   PLCC |   SROCC |   KROCC |
|-------------|--------|---------|---------|
| DSSIM       | **-0.773** |  **-0.861** |  **-0.678** |
| SSIMULACRA  | -0.663 |  -0.673 |  -0.485 |
| Butteraugli | -0.648 |  -0.76  |  -0.572 |
