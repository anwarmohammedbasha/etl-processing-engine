import pandas as pd

def extract(path='C:/Users/anwar/PycharmProjects/etl-processing-engine/data/coffee-shop-sales/sales.csv'):
    return pd.read_csv(path)

