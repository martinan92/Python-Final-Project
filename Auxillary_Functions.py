import numpy as np
import pandas as pd

#Imports CSV file give input path
def read_data(input_path):
    raw_data = pd.read_csv(input_path, keep_default_na=False, na_values=['_'])
    return raw_data
