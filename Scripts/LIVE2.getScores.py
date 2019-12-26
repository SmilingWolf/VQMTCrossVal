# https://live.ece.utexas.edu/research/quality/subjective.htm

import os

import pandas as pd

df = pd.read_csv('LIVE2.DMOS.csv')
df['DSSIM'] = 0
df['SSIMULACRA'] = 0
df['Butteraugli'] = 0

for i, dfRow in df.iterrows():
	orig = 'refimgs/%s.png' % (dfRow['refnames_all'])
	dist = '%s/%s.png' % (dfRow['dst_type'], dfRow['dist_img'])

	cmd = "dssim %s %s" % (orig, dist)
	proc = os.popen(cmd, "r")
	dssim = float(proc.readline().split('\t')[0])
	df.loc[i, 'DSSIM'] = dssim

	cmd = "ssimulacra %s %s" % (orig, dist)
	proc = os.popen(cmd, "r")
	dssim = float(proc.readline().split('\t')[0])
	df.loc[i, 'SSIMULACRA'] = dssim

	cmd = "butteraugli %s %s" % (orig, dist)
	proc = os.popen(cmd, "r")
	dssim = float(proc.readline().split('\t')[0])
	df.loc[i, 'Butteraugli'] = dssim

df.to_csv('LIVE2.VQMT.csv', index=False)
