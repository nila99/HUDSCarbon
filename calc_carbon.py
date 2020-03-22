import pandas as pd
import numpy as np
from categorize import categorize

excel_file = 'CFP_Calculator.xlsx'

def calc_carbon():
	food_input =  categorize()
	print(food_input.head())


calc_carbon()
