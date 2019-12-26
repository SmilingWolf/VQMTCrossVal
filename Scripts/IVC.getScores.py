# http://www2.irccyn.ec-nantes.fr/ivcdb/

import os

import pandas as pd

df = pd.read_csv('IVC.MOS.csv')
df['DSSIM'] = 0
df['SSIMULACRA'] = 0
df['Butteraugli'] = 0

for i, dfRow in df.iterrows():
	orig = 'color/%s.bmp.png' % (dfRow['ref_img'])
	dist = 'color/%s.bmp.png' % (dfRow['dist_img'])

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

df.to_csv('IVC.VQMT.csv', index=False)
