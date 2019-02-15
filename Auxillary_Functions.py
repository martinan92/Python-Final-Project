import numpy as np
import pandas as pd
import yaml

#Imports YML file give input path
def read_yml(input_path):
    with open(input_path, 'r') as stream:
        try:
            print(yaml.load(stream))
        except yaml.YAMLError as exc:
            print(exc)

#Imports CSV file give input path
def read_data(input_path):
    raw_data = pd.read_csv(input_path, keep_default_na=False, na_values=['_'])
    return raw_data