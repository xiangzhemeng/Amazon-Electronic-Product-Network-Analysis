import pandas as pd
import numpy as np
import multiprocessing
from multiprocessing import Pool

num_partitions = multiprocessing.cpu_count()
num_cores = multiprocessing.cpu_count()

df_product = pd.read_pickle('data/product_intersection.pkl')
product_asin = df_product.index.values
print("data loading finished...")

def also_viewed(x):
    if 'also_viewed' in x.keys():
        temp = []
        for asin in x['also_viewed']:
            if asin in product_asin:
                temp.append(asin)
        return temp
    else:
        return []

def also_bought(x):
    if 'also_bought' in x.keys():
        temp = []
        for asin in x['also_bought']:
            if asin in product_asin:
                temp.append(asin)
        return temp
    else:
        return []

def parallelize_dataframe(df, func):
    df_split = np.array_split(df, num_partitions)
    pool = Pool(num_cores)
    df = pd.concat(pool.map(func, df_split))
    pool.close()
    pool.join()
    return df

def multiply_columns(data):
    data['also_viewed'] = data['related'].apply(lambda x: also_viewed(x))
    data['also_bought'] = data['related'].apply(lambda x: also_bought(x))
    return data

print("start running...")
df_product = parallelize_dataframe(df_product, multiply_columns)
df_product.to_pickle('data/product_also_viewed_bought.pkl')
print("ALL DONE!")
