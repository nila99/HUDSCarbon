import pandas as pd
import numpy as np
from calc_carbon import calc_carbon
import os

outname = 'totalCE.csv'
outname1 = 'totalLU.csv'
outname2 = 'totalCOC.csv'

outdir = '/Users/vaannilaannadurai/Desktop/HUDSCarbon/data/'
if not os.path.exists(outdir):
    os.mkdir(outdir)

fullname = os.path.join(outdir, outname)
fullname1 = os.path.join(outdir, outname1)
fullname2 = os.path.join(outdir, outname2)    


def get_totals():
	food_input =  calc_carbon()
	totalCE = food_input[['Carbon Category', 'Carbon Emissions']]
	totalLU = food_input[['Carbon Category', 'Land Use']]
	totalCOC = food_input[['Carbon Category', 'Carbon Oppurtunity Costs']]
	totalCE = totalCE.groupby('Carbon Category').sum()
	totalLU = totalLU.groupby('Carbon Category').sum()
	totalCOC = totalCOC.groupby('Carbon Category').sum()
	totalCE.to_csv(outname)
	totalLU.to_csv(outname1)
	totalCOC.to_csv(outname2)

get_totals()


		