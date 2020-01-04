# https://www.epfl.ch/labs/mmspg/research/page-58317-en-html/page-58332-en-html/page-58333-en-html/iqa/

import pandas as pd

mosField = 'mos'
metrics = [mosField, 'DSSIM', 'SSIMULACRA', 'Butteraugli', 'Butteraugli_XL', 'Butteraugli_XL_3m', 'Butteraugli_XL_2s', 'Butteraugli_XL_3s', 'Butteraugli_XL_6s', 'Butteraugli_XL_12s']

df = pd.read_csv('JPEGXR.VQMT.csv')

print('SROCC:')
print(df[metrics].corr('spearman')[[mosField]].sort_values([mosField]))

print('\nKROCC:')
print(df[metrics].corr('kendall')[[mosField]].sort_values([mosField]))
