# http://www.ponomarenko.info/tid2013.htm

import pandas as pd

mosField = 'mos'
metrics = [mosField, 'DSSIM', 'SSIMULACRA', 'Butteraugli', 'Butteraugli_XL', 'Butteraugli_XL_3m', 'Butteraugli_XL_2s', 'Butteraugli_XL_3s', 'Butteraugli_XL_6s', 'Butteraugli_XL_12s']

df = pd.read_csv('TID2013.VQMT.csv')

print('SROCC:')
print(df[metrics][df['dst_type'].isin([10, 11])].corr('spearman')[[mosField]].sort_values([mosField]))
print(df[metrics][df['dst_type'].isin([10, 11, 8])].corr('spearman')[[mosField]].sort_values([mosField]))
print(df[metrics].corr('spearman')[[mosField]].sort_values([mosField]))

print('\nKROCC:')
print(df[metrics][df['dst_type'].isin([10, 11])].corr('kendall')[[mosField]].sort_values([mosField]))
print(df[metrics][df['dst_type'].isin([10, 11, 8])].corr('kendall')[[mosField]].sort_values([mosField]))
print(df[metrics].corr('kendall')[[mosField]].sort_values([mosField]))
