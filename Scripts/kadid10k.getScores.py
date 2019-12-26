# http://database.mmsp-kn.de/kadid-10k-database.html

import os

import pandas as pd

df = pd.read_csv('kadid10k.DMOS.csv')
df['DSSIM'] = 0
df['SSIMULACRA'] = 0

for i, dfRow in df.iterrows():
	orig = 'images/%s' % (dfRow['ref_img'])
	dist = 'images/%s' % (dfRow['dist_img'])
	cmd = "dssim %s %s" % (orig, dist)
	proc = os.popen(cmd, "r")
	dssim = float(proc.readline().split('\t')[0])
	df.loc[i, 'DSSIM'] = dssim

	cmd = "ssimulacra %s %s" % (orig, dist)
	proc = os.popen(cmd, "r")
	dssim = float(proc.readline().split('\t')[0])
	df.loc[i, 'SSIMULACRA'] = dssim

df.to_csv('kadid10k.VQMT.csv', index=False)
