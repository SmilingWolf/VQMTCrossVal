# https://www.epfl.ch/labs/mmspg/research/page-58317-en-html/page-58332-en-html/page-58333-en-html/iqa/

import os

import pandas as pd

df = pd.read_csv('JPEGXR.MOS.csv')
df['DSSIM'] = 0
df['SSIMULACRA'] = 0

for i, dfRow in df.iterrows():
	orig = 'Original/%s_orig.bmp.png' % (dfRow['ref_img'])
	dist = 'Dist/%s.png' % (dfRow['dist_img'])
	cmd = "dssim %s %s" % (orig, dist)
	proc = os.popen(cmd, "r")
	dssim = float(proc.readline().split('\t')[0])
	df.loc[i, 'DSSIM'] = dssim

	cmd = "ssimulacra %s %s" % (orig, dist)
	proc = os.popen(cmd, "r")
	dssim = float(proc.readline().split('\t')[0])
	df.loc[i, 'SSIMULACRA'] = dssim

df.to_csv('JPEGXR.VQMT.csv', index=False)
