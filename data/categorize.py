import pandas as pd
import numpy as np

excel_file = 'Data2018_19SY.xls'

#milk and cream, preserves
def categorize():
	food_input = pd.read_excel(excel_file)
	#only use inputs in pounds
	food_input = food_input.loc[food_input['Purchase Unit'] == 'LB']
	#reset indices
	food_input.reset_index(inplace=True)
	#only include relevant columns
	food_input = food_input[['Item Name', 'Cost Category Name', 'Purchase Unit', 'Units']]

	food_input['Carbon Category'] = ''

	food_input['Carbon Category'] = np.where((food_input['Cost Category Name'] == 'BAKERY - BREADS'), 
		'Wheat', food_input['Carbon Category'])

	food_input['Carbon Category'] = np.where((food_input['Cost Category Name'] == 'BUTTER & MARGARINE'), 
		'Butter', food_input['Carbon Category'])

	food_input['Carbon Category'] = np.where((food_input['Cost Category Name'] == 'CANNED VEGETABLES'), 
		'Vegetables', food_input['Carbon Category'])

	food_input['Carbon Category'] = np.where((food_input['Cost Category Name'] == 'FROZEN VEGETABLES'), 
		'Vegetables', food_input['Carbon Category'])

	food_input['Carbon Category'] = np.where((food_input['Cost Category Name'] == 'FRESH VEGETABLES'), 
		'Vegetables', food_input['Carbon Category'])

	food_input['Carbon Category'] = np.where((food_input['Cost Category Name'] == 'CANNED FRUIT'), 
		'Fruits', food_input['Carbon Category'])

	food_input['Carbon Category'] = np.where((food_input['Cost Category Name'] == 'FROZEN FRUIT'), 
		'Fruits', food_input['Carbon Category'])

	food_input['Carbon Category'] = np.where((food_input['Cost Category Name'] == 'FRESH FRUIT'), 
		'Fruits', food_input['Carbon Category'])

	food_input['Carbon Category'] = np.where((food_input['Cost Category Name'] == 'ICE CREAM'), 
		'Ice Cream', food_input['Carbon Category'])

	food_input['Carbon Category'] = np.where((food_input['Cost Category Name'] == 'PASTA'), 
		'Wheat', food_input['Carbon Category'])

	food_input['Carbon Category'] = np.where((food_input['Cost Category Name'] == 'POULTRY'), 
		'Poultry', food_input['Carbon Category'])

	food_input['Carbon Category'] = np.where((food_input['Cost Category Name'] == 'BUTTER & MARGARINE'), 
		'Butter', food_input['Carbon Category'])

	food_input['Carbon Category'] = np.where((food_input['Cost Category Name'] == 'EGGS'), 
		'Eggs', food_input['Carbon Category'])

	food_input['Carbon Category'] = np.where(food_input['Cost Category Name'].str.contains
			("Beer", case=False, na=False), 'Beer', food_input['Carbon Category'])

	food_input['Carbon Category'] = np.where(food_input['Cost Category Name'].str.contains
			("WINE", case=False, na=False), 'Wine', food_input['Carbon Category'])

	food_input['Carbon Category'] = np.where((food_input['Item Name'].str.contains("TOFU", case=False, na=False) 
		& (food_input['Cost Category Name'] == 'CHEESE YOGURT & TOFU')), 'Tofu', food_input['Carbon Category'])

	food_input['Carbon Category'] = np.where((food_input['Item Name'].str.contains("CHEESE", case=False, na=False)
		& (food_input['Cost Category Name'] == 'CHEESE YOGURT & TOFU')), 'Cheese', food_input['Carbon Category'])

	food_input['Carbon Category'] = np.where((food_input['Cost Category Name'] == 'FISH'), 
		'Fish', food_input['Carbon Category'])

	food_input['Carbon Category'] = np.where((food_input['Item Name'].str.contains
		("shrimp|mussel|scallop|calamari|clam|lobster|crab", case=False, na=False) 
		& (food_input['Cost Category Name'] == 'FISH')), 'Shellfish', food_input['Carbon Category'])

	food_input['Carbon Category'] = np.where((food_input['Item Name'].str.contains
		("beef|burger|veal", case=False, na=False) 
		& (food_input['Cost Category Name'] == 'MEAT')), 'Beef', food_input['Carbon Category'])

	food_input['Carbon Category'] = np.where((food_input['Item Name'].str.contains
		("pork|bacon|prosciutto|capicola|salami|pepperoni|ham|sausage|franks|linguica|pastrami|mortadella", 
		case=False, na=False) & (food_input['Cost Category Name'] == 'MEAT')), 'Pork', 
		food_input['Carbon Category'])

	food_input['Carbon Category'] = np.where((food_input['Item Name'].str.contains
		("lamb", case=False, na=False) 
		& (food_input['Cost Category Name'] == 'MEAT')), 'Lamb', food_input['Carbon Category'])
	
	food_input = food_input.loc[food_input['Carbon Category'] != '']
	#reset indices
	food_input.reset_index(inplace=True)

	return food_input