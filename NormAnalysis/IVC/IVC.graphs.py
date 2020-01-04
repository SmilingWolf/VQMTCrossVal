# http://www2.irccyn.ec-nantes.fr/ivcdb/

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import minmax_scale

pd.set_option('display.max_rows', 1000)
pd.set_option('display.max_columns', 1000)
pd.set_option('display.width', 1000)

df = pd.read_csv('IVC.VQMT.csv')
df['mos'] = minmax_scale(df['mos'], feature_range=(1,5), axis=0)

minMOS = df['mos'].min()
maxMOS = df['mos'].max()
series = np.linspace(maxMOS, minMOS, 20)

results = pd.DataFrame()
for i in series:
	filtered = df[['mos', 'DSSIM', 'SSIMULACRA', 'Butteraugli', 'Butteraugli_XL', 'Butteraugli_XL_3m', 'Butteraugli_XL_2s', 'Butteraugli_XL_3s', 'Butteraugli_XL_6s', 'Butteraugli_XL_12s']][df['mos'] >= i]
	results = results.append(filtered.corr('spearman')[['mos']].T.reset_index(), ignore_index=True, sort=False)

results.index = series
results = results.drop(['mos', 'index'], axis=1)
results = results.dropna(thresh=1)

print(results)

plt.figure(figsize=(1920/96, 1080/96), dpi=96)
#plt.plot(results.index, results['DSSIM'], label='DSSIM')
#plt.plot(results.index, results['SSIMULACRA'], label='SSIMULACRA')
plt.plot(results.index, results['Butteraugli_XL'], label='Butteraugli_XL')
#plt.plot(results.index, results['Butteraugli_XL_3m'], label='Butteraugli_XL_3m')
plt.plot(results.index, results['Butteraugli_XL_2s'], label='Butteraugli_XL_2s')
plt.plot(results.index, results['Butteraugli_XL_3s'], label='Butteraugli_XL_3s')
plt.plot(results.index, results['Butteraugli_XL_6s'], label='Butteraugli_XL_6s')
plt.plot(results.index, results['Butteraugli_XL_12s'], label='Butteraugli_XL_12s')
plt.legend()
plt.ylabel('SROCC')
plt.xlabel('IVC MOS')
plt.savefig('plot.png', bbox_inches='tight')
