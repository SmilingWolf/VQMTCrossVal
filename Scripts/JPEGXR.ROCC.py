# https://www.epfl.ch/labs/mmspg/research/page-58317-en-html/page-58332-en-html/page-58333-en-html/iqa/

import pandas as pd

df = pd.read_csv('JPEGXR.VQMT.csv')

print('SROCC:')
print(df[['mos', 'DSSIM', 'SSIMULACRA', 'Butteraugli']].corr('spearman'))

print('\nKROCC:')
print(df[['mos', 'DSSIM', 'SSIMULACRA', 'Butteraugli']].corr('kendall'))
