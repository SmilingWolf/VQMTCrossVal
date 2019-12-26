# http://vision.eng.shizuoka.ac.jp/mod/page/view.php?id=23

import os

import pandas as pd

df = pd.read_csv('csiq.DMOS.csv', decimal=',')
df['DSSIM'] = 0
df['SSIMULACRA'] = 0

for i, dfRow in df.iterrows():
	orig = 'src/%s.png' % (dfRow['image'])
	dist = '%s/%s.%s.%d.png' % (dfRow['dst_type'], dfRow['image'], dfRow['dst_type'], dfRow['dst_lev'])
	cmd = "dssim %s %s" % (orig, dist)
	proc = os.popen(cmd, "r")
	dssim = float(proc.readline().split('\t')[0])
	df.loc[i, 'DSSIM'] = dssim

	cmd = "ssimulacra %s %s" % (orig, dist)
	proc = os.popen(cmd, "r")
	dssim = float(proc.readline().split('\t')[0])
	df.loc[i, 'SSIMULACRA'] = dssim

df.to_csv('csiq.VQMT.csv', index=False)
