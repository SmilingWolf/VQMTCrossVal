# http://www2.irccyn.ec-nantes.fr/ivcdb/

import pandas as pd

mosField = 'mos'
metrics = [mosField, 'DSSIM', 'SSIMULACRA', 'Butteraugli', 'Butteraugli_XL', 'Butteraugli_XL_3m', 'Butteraugli_XL_2s', 'Butteraugli_XL_3s', 'Butteraugli_XL_6s', 'Butteraugli_XL_12s']

df = pd.read_csv('IVC.VQMT.csv')

print('SROCC:')
print(df[metrics][df['dst_type'].isin(['j2000', 'jpeg', 'jpeg_lumichr'])].corr('spearman')[[mosField]].sort_values([mosField]))
print(df[metrics][df['dst_type'].isin(['j2000', 'jpeg', 'jpeg_lumichr', 'flou'])].corr('spearman')[[mosField]].sort_values([mosField]))
print(df[metrics].corr('spearman')[[mosField]].sort_values([mosField]))

print('\nKROCC:')
print(df[metrics][df['dst_type'].isin(['j2000', 'jpeg', 'jpeg_lumichr'])].corr('kendall')[[mosField]].sort_values([mosField]))
print(df[metrics][df['dst_type'].isin(['j2000', 'jpeg', 'jpeg_lumichr', 'flou'])].corr('kendall')[[mosField]].sort_values([mosField]))
print(df[metrics].corr('kendall')[[mosField]].sort_values([mosField]))
