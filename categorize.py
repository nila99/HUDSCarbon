import pandas as pd
import numpy as np

excel_file = 'Data2018_19SY.xls'
categories = np.array(['Beef', 'Pork', 'Poultry', 'Fish', 'Shellfish', 'LambSheepGoat', 'Milk', 
	'Yogurt', 'Cream', 'Cheese', 'Butter', 'IceCream', 'Eggs', 'Beans', 'Peanuts', 'PeanutButter', 
	'Soybeans', 'NutsSeeds', 'NutSeedButter', 'Rice', 'Wheat', 'Corn', 'Bread', 'Pasta', 
	'OtherGrains', 'AlmondMilk', 'CoconutMilk', 'MeatSub', 'CheeseSub', 'EggSub', 'FishSub', 'Fruits',
	'Vegetables', 'Roots', 'Sugars', 'VegOils', 'TeaCoffeeSpices', 'Alcohol'])

def categorize():
	food_input = pd.read_excel(excel_file)
	#only use inputs in pounds
	food_input = food_input.loc[food_input['Purchase Unit'] == 'LB']
	#reset indices
	food_input.reset_index(inplace=True)
	#only include relevant columns
	food_input = food_input[['Item Name', 'Cost Category Name', 'Purchase Unit']]
	
	food_input['Carbon Category'] = ''

	food_input['Carbon Category'] = np.where((food_input['Cost Category Name'] == 'BAKERY - BREADS'), 
		'Bread', food_input['Carbon Category'])

	food_input['Carbon Category'] = np.where((food_input['Cost Category Name'] == 'BUTTER & MARGARINE'), 
		'Butter', food_input['Carbon Category'])

	food_input['Carbon Category'] = np.where((food_input['Cost Category Name'] == 'CANNED VEGETABLES'), 
		'Vegetables', food_input['Carbon Category'])

	food_input['Carbon Category'] = np.where((food_input['Cost Category Name'] == 'FROZEN VEGETABLES'), 
		'Vegetables', food_input['Carbon Category'])

	food_input['Carbon Category'] = np.where((food_input['Cost Category Name'] == 'FRESH VEGETABLES'), 
		'Vegetables', food_input['Carbon Category'])

	food_input['Carbon Category'] = np.where((food_input['Cost Category Name'] == 'CANNED FRUIT'), 
		'Fruit', food_input['Carbon Category'])

	food_input['Carbon Category'] = np.where((food_input['Cost Category Name'] == 'FROZEN FRUIT'), 
		'Fruit', food_input['Carbon Category'])

	food_input['Carbon Category'] = np.where((food_input['Cost Category Name'] == 'FRESH FRUIT'), 
		'Fruit', food_input['Carbon Category'])

	food_input['Carbon Category'] = np.where((food_input['Cost Category Name'] == 'ICE CREAM'), 
		'IceCream', food_input['Carbon Category'])

	food_input['Carbon Category'] = np.where((food_input['Cost Category Name'] == 'POULTRY'), 
		'Poultry', food_input['Carbon Category'])

	food_input['Carbon Category'] = np.where((food_input['Cost Category Name'] == 'BUTTER & MARGARINE'), 
		'Butter', food_input['Carbon Category'])

	food_input['Carbon Category'] = np.where(food_input['Cost Category Name'].str.contains
			("Beer", case=False, na=False), 'Alcohol', food_input['Carbon Category'])

	food_input['Carbon Category'] = np.where(food_input['Cost Category Name'].str.contains
			("WINE", case=False, na=False), 'Alcohol', food_input['Carbon Category'])

	food_input['Carbon Category'] = np.where((food_input['Item Name'].str.contains("TOFU", case=False, na=False) 
		& (food_input['Cost Category Name'] == 'CHEESE YOGURT & TOFU')), 'TOFU', food_input['Carbon Category'])

	food_input['Carbon Category'] = np.where((food_input['Item Name'].str.contains("CHEESE", case=False, na=False)
		& (food_input['Cost Category Name'] == 'CHEESE YOGURT & TOFU')), 'CHEESE', food_input['Carbon Category'])	


categorize()