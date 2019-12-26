# http://database.mmsp-kn.de/kadid-10k-database.html

import pandas as pd

df = pd.read_csv('kadid10k.VQMT.csv')

print('SROCC:')
print(df[['dmos', 'DSSIM', 'SSIMULACRA', 'Butteraugli']][df['dst_type'].isin([9, 10])].corr('spearman'))
print(df[['dmos', 'DSSIM', 'SSIMULACRA', 'Butteraugli']][df['dst_type'].isin([9, 10, 1])].corr('spearman'))
print(df[['dmos', 'DSSIM', 'SSIMULACRA', 'Butteraugli']].corr('spearman'))

print('\nKROCC:')
print(df[['dmos', 'DSSIM', 'SSIMULACRA', 'Butteraugli']][df['dst_type'].isin([9, 10])].corr('kendall'))
print(df[['dmos', 'DSSIM', 'SSIMULACRA', 'Butteraugli']][df['dst_type'].isin([9, 10, 1])].corr('kendall'))
print(df[['dmos', 'DSSIM', 'SSIMULACRA', 'Butteraugli']].corr('kendall'))
