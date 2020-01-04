# https://live.ece.utexas.edu/research/quality/subjective.htm

import pandas as pd

mosField = 'dmos_new'
metrics = [mosField, 'DSSIM', 'SSIMULACRA', 'Butteraugli', 'Butteraugli_XL', 'Butteraugli_XL_3m', 'Butteraugli_XL_2s', 'Butteraugli_XL_3s', 'Butteraugli_XL_6s', 'Butteraugli_XL_12s']

df = pd.read_csv('LIVE2.VQMT.csv')

print('SROCC:')
print(df[metrics][df['dst_type'].isin(['jp2k', 'jpeg'])].corr('spearman')[[mosField]].sort_values([mosField]))
print(df[metrics][df['dst_type'].isin(['jp2k', 'jpeg', 'gblur'])].corr('spearman')[[mosField]].sort_values([mosField]))
print(df[metrics].corr('spearman')[[mosField]].sort_values([mosField]))

print('\nKROCC:')
print(df[metrics][df['dst_type'].isin(['jp2k', 'jpeg'])].corr('kendall')[[mosField]].sort_values([mosField]))
print(df[metrics][df['dst_type'].isin(['jp2k', 'jpeg', 'gblur'])].corr('kendall')[[mosField]].sort_values([mosField]))
print(df[metrics].corr('kendall')[[mosField]].sort_values([mosField]))
