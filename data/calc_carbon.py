import pandas as pd
import numpy as np
from categorize import categorize
import copy

excel_file = 'CFP_Calculator.xlsx'


def calc_carbon():
	emission_factors = pd.read_excel(excel_file, sheet_name=5)
	# emission_factors = emission_factors.pivot_table(index = ['Food']) 
	food_input =  categorize()

	emission_numbers = dict((emission_factors['Food'][el],(emission_factors['Emissions'][el],
		emission_factors['Land Use'][el],emission_factors['Carbon Oppurtunity Costs'][el])) 
		for el in range(emission_factors.shape[0]))


	food_input['Carbon Emissions'] = ''
	food_input['Land Use'] = ''
	food_input['Carbon Oppurtunity Costs'] = ''

	for i in range(food_input.shape[0]):
		food_input.at[i, 'Carbon Emissions'] = (food_input.at[i, 'Units'])* \
		(emission_numbers.get(food_input.at[i, 'Carbon Category'])[0]/1000)

		food_input.at[i, 'Land Use'] = (food_input.at[i, 'Units'])* \
		(emission_numbers.get(food_input.at[i, 'Carbon Category'])[1]/10000)

		food_input.at[i, 'Carbon Oppurtunity Costs'] = (food_input.at[i, 'Units'])* \
		(emission_numbers.get(food_input.at[i, 'Carbon Category'])[2]/1000)
	
	return food_input