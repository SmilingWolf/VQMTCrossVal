# http://vision.eng.shizuoka.ac.jp/mod/page/view.php?id=23

import pandas as pd

mosField = 'dmos'
metrics = [mosField, 'DSSIM', 'SSIMULACRA', 'Butteraugli', 'Butteraugli_XL', 'Butteraugli_XL_3m', 'Butteraugli_XL_2s', 'Butteraugli_XL_3s', 'Butteraugli_XL_6s', 'Butteraugli_XL_12s']

df = pd.read_csv('csiq.VQMT.csv')

print('SROCC:')
print(df[metrics][df['dst_idx'].isin([2, 3])].corr('spearman')[[mosField]].sort_values([mosField]))
print(df[metrics][df['dst_idx'].isin([2, 3, 5])].corr('spearman')[[mosField]].sort_values([mosField]))
print(df[metrics].corr('spearman')[[mosField]].sort_values([mosField]))

print('\nKROCC:')
print(df[metrics][df['dst_idx'].isin([2, 3])].corr('kendall')[[mosField]].sort_values([mosField]))
print(df[metrics][df['dst_idx'].isin([2, 3, 5])].corr('kendall')[[mosField]].sort_values([mosField]))
print(df[metrics].corr('kendall')[[mosField]].sort_values([mosField]))
