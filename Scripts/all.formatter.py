import pandas as pd
import tabulate

files = ['csiq', 'IVC', 'JPEGXR', 'kadid10k', 'LIVE2', 'TID2013']
fields = ['dmos', 'mos', 'mos', 'dmos', 'dmos_new', 'mos']

for index, file in enumerate(files):
	field = fields[index]

	df = pd.read_csv('%s.VQMT.csv' % (file))

	resume = pd.DataFrame()

	resume['PLCC'] = df[[field, 'DSSIM', 'SSIMULACRA', 'Butteraugli']].corr('pearson')[field][1:].round(decimals=3)
	resume['SROCC'] = df[[field, 'DSSIM', 'SSIMULACRA', 'Butteraugli']].corr('spearman')[field][1:].round(decimals=3)
	resume['KROCC'] = df[[field, 'DSSIM', 'SSIMULACRA', 'Butteraugli']].corr('kendall')[field][1:].round(decimals=3)

	print('\n%s:\n' % (file.upper()))
	print(tabulate.tabulate(resume, headers='keys', tablefmt='github'))
