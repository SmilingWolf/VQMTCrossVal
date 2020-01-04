# http://vision.eng.shizuoka.ac.jp/mod/page/view.php?id=23

import os

import pandas as pd

df = pd.read_csv('csiq.VQMT.csv', decimal=',')
df['Butteraugli_XL'] = 0
df['Butteraugli_XL_3m'] = 0
df['Butteraugli_XL_2s'] = 0
df['Butteraugli_XL_3s'] = 0
df['Butteraugli_XL_6s'] = 0
df['Butteraugli_XL_12s'] = 0

for i, dfRow in df.iterrows():
	orig = 'src/%s.png' % (dfRow['image'])
	dist = '%s/%s.%s.%d.png' % (dfRow['dst_type'], dfRow['image'], dfRow['dst_type'], dfRow['dst_lev'])
	cmd = "butteraugli_xl.exe %s %s" % (orig, dist)
	print(cmd)
	proc = os.popen(cmd, "r")
	dssim = float(proc.readline())
	df.loc[i, 'Butteraugli_XL'] = dssim
	dssim = float(proc.readline().split(' ')[1])
	df.loc[i, 'Butteraugli_XL_3m'] = dssim

	dssim = float(proc.readline().split(' ')[1])
	df.loc[i, 'Butteraugli_XL_2s'] = dssim
	dssim = float(proc.readline().split(' ')[1])
	df.loc[i, 'Butteraugli_XL_3s'] = dssim
	dssim = float(proc.readline().split(' ')[1])
	df.loc[i, 'Butteraugli_XL_6s'] = dssim
	dssim = float(proc.readline().split(' ')[1])
	df.loc[i, 'Butteraugli_XL_12s'] = dssim

df.to_csv('csiq.VQMT.2.csv', index=False)
