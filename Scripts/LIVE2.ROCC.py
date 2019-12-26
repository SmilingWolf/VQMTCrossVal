# https://live.ece.utexas.edu/research/quality/subjective.htm

import pandas as pd

df = pd.read_csv('LIVE2.VQMT.csv')

print('SROCC:')
print(df[['dmos_new', 'DSSIM', 'SSIMULACRA', 'Butteraugli']][df['dst_type'].isin(['jp2k', 'jpeg'])].corr('spearman'))
print(df[['dmos_new', 'DSSIM', 'SSIMULACRA', 'Butteraugli']][df['dst_type'].isin(['jp2k', 'jpeg', 'gblur'])].corr('spearman'))
print(df[['dmos_new', 'DSSIM', 'SSIMULACRA', 'Butteraugli']].corr('spearman'))

print('\nKROCC:')
print(df[['dmos_new', 'DSSIM', 'SSIMULACRA', 'Butteraugli']][df['dst_type'].isin(['jp2k', 'jpeg'])].corr('kendall'))
print(df[['dmos_new', 'DSSIM', 'SSIMULACRA', 'Butteraugli']][df['dst_type'].isin(['jp2k', 'jpeg', 'gblur'])].corr('kendall'))
print(df[['dmos_new', 'DSSIM', 'SSIMULACRA', 'Butteraugli']].corr('kendall'))
