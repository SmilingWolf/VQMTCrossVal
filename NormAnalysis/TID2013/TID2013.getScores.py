# http://www.ponomarenko.info/tid2013.htm

import os

import pandas as pd

df = pd.read_csv('TID2013.VQMT.csv')
df['Butteraugli_XL'] = 0
df['Butteraugli_XL_3m'] = 0
df['Butteraugli_XL_2s'] = 0
df['Butteraugli_XL_3s'] = 0
df['Butteraugli_XL_6s'] = 0
df['Butteraugli_XL_12s'] = 0

for i, dfRow in df.iterrows():
	orig = 'reference_images/%s.png' % (dfRow['ref_img'])
	dist = 'distorted_images/%s.png' % (dfRow['dist_img'])
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

df.to_csv('TID2013.VQMT.2.csv', index=False)
