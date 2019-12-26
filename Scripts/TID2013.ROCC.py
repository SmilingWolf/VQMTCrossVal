# http://www.ponomarenko.info/tid2013.htm

import pandas as pd

df = pd.read_csv('TID2013.VQMT.csv')

print('SROCC:')
print(df[['mos', 'DSSIM', 'SSIMULACRA', 'Butteraugli']][df['dst_type'].isin([10, 11])].corr('spearman'))
print(df[['mos', 'DSSIM', 'SSIMULACRA', 'Butteraugli']][df['dst_type'].isin([10, 11, 8])].corr('spearman'))
print(df[['mos', 'DSSIM', 'SSIMULACRA', 'Butteraugli']].corr('spearman'))

print('\nKROCC:')
print(df[['mos', 'DSSIM', 'SSIMULACRA', 'Butteraugli']][df['dst_type'].isin([10, 11])].corr('kendall'))
print(df[['mos', 'DSSIM', 'SSIMULACRA', 'Butteraugli']][df['dst_type'].isin([10, 11, 8])].corr('kendall'))
print(df[['mos', 'DSSIM', 'SSIMULACRA', 'Butteraugli']].corr('kendall'))
