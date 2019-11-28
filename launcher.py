import os
import sys


import pandas as pd
date1 = '2019-11-21'
date2 = '2019-11-27'
mydates = pd.date_range(date1, date2)

for arg in mydates:
	print(arg.strftime('%Y-%m-%d'))
	os.system("Automating_Category-Seller.py {}".format(arg.strftime('%Y-%m-%d')))
