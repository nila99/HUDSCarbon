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
	food_input['Carbon Category'] = np.where(food_input['Cost Category Name'].str.contains
			("Beer", case=False, na=False), 'Alcohol', '')

	for i in range(food_input.shape[0]):
		if (food_input['Cost Category Name'][i] == 'BAKERY - BREADS'):
			food_input['Carbon Category'][i] = 'Bread'

		if (food_input['Cost Category Name'][i] == 'BUTTER & MARGARINE'):
			food_input['Carbon Category'][i] = 'Butter'

		if (food_input['Cost Category Name'][i] == 'CANNED FRUIT'):
			food_input['Carbon Category'][i] = 'Fruit'

		if (food_input['Cost Category Name'][i] == 'CANNED VEGETABLES'):
			food_input['Carbon Category'][i] = 'Vegetables'

		


categorize()