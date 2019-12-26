# http://www.ponomarenko.info/tid2013.htm

import os

import pandas as pd

df = pd.read_csv('TID2013.MOS.csv')
df['DSSIM'] = 0
df['SSIMULACRA'] = 0

for i, dfRow in df.iterrows():
	orig = 'reference_images/%s.png' % (dfRow['ref_img'])
	dist = 'distorted_images/%s.png' % (dfRow['dist_img'])
	cmd = "dssim %s %s" % (orig, dist)
	proc = os.popen(cmd, "r")
	dssim = float(proc.readline().split('\t')[0])
	df.loc[i, 'DSSIM'] = dssim

	cmd = "ssimulacra %s %s" % (orig, dist)
	proc = os.popen(cmd, "r")
	dssim = float(proc.readline().split('\t')[0])
	df.loc[i, 'SSIMULACRA'] = dssim

df = df[['dist_img','ref_img','dst_type','mos','var','DSSIM','SSIMULACRA']]
df.to_csv('TID2013.VQMT.csv', index=False)
