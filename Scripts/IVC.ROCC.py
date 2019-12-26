# http://www2.irccyn.ec-nantes.fr/ivcdb/

import pandas as pd

df = pd.read_csv('IVC.VQMT.csv')

print('SROCC:')
print(df[['mos', 'DSSIM', 'SSIMULACRA', 'Butteraugli']][df['dst_type'].isin(['j2000', 'jpeg', 'jpeg_lumichr'])].corr('spearman'))
print(df[['mos', 'DSSIM', 'SSIMULACRA', 'Butteraugli']][df['dst_type'].isin(['j2000', 'jpeg', 'jpeg_lumichr', 'flou'])].corr('spearman'))
print(df[['mos', 'DSSIM', 'SSIMULACRA', 'Butteraugli']].corr('spearman'))

print('\nKROCC:')
print(df[['mos', 'DSSIM', 'SSIMULACRA', 'Butteraugli']][df['dst_type'].isin(['j2000', 'jpeg', 'jpeg_lumichr'])].corr('kendall'))
print(df[['mos', 'DSSIM', 'SSIMULACRA', 'Butteraugli']][df['dst_type'].isin(['j2000', 'jpeg', 'jpeg_lumichr', 'flou'])].corr('kendall'))
print(df[['mos', 'DSSIM', 'SSIMULACRA', 'Butteraugli']].corr('kendall'))
