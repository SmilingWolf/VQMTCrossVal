# http://vision.eng.shizuoka.ac.jp/mod/page/view.php?id=23

import pandas as pd

df = pd.read_csv('csiq.VQMT.csv')

print('SROCC:')
print(df[['dmos', 'DSSIM', 'SSIMULACRA', 'Butteraugli']][df['dst_idx'].isin([2, 3])].corr('spearman'))
print(df[['dmos', 'DSSIM', 'SSIMULACRA', 'Butteraugli']][df['dst_idx'].isin([2, 3, 5])].corr('spearman'))
print(df[['dmos', 'DSSIM', 'SSIMULACRA', 'Butteraugli']].corr('spearman'))

print('\nKROCC:')
print(df[['dmos', 'DSSIM', 'SSIMULACRA', 'Butteraugli']][df['dst_idx'].isin([2, 3])].corr('kendall'))
print(df[['dmos', 'DSSIM', 'SSIMULACRA', 'Butteraugli']][df['dst_idx'].isin([2, 3, 5])].corr('kendall'))
print(df[['dmos', 'DSSIM', 'SSIMULACRA', 'Butteraugli']].corr('kendall'))
