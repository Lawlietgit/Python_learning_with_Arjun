import pandas as pd
import numpy as np

def gen_matrix(engine='random', size=(2,2), limits=(0,1)):
    """
    generate a numpy array with different ways and specified size
    :param engine: str, 'one'/'zero'/'random'/'gaussian'/'int'
    :param size: tuple, indicating the size
    :param limits: tuple, the lower and upper limit for integers,
                   only works for engine=='int'
    """
    assert engine in {'one','zero','random','gaussian','int'}, "invalid engine!"
    if engine=='random':
        return np.random.random(size)
    if engine=='one':
        return np.ones(size)
    if engine=='zero':
        return np.zeros(size)
    if engine=='random':
        return np.random.randn(*size)
    return np.random.randint(*limits, size)

def load_df(fpath):
    df = pd.read_csv(fpath)
    n, d = df.shape
    print("{} rows and {} columns read from {}".format(n, d, fpath))
    return df

def get_df_info(df):
    """
    print several info for a pandas df
    """
    null_count = df.isnull().astype('int').sum(axis=0) # number of nulls for each col
    print("-"*20 + "missing values" + "-"*20)
    for col in df.columns:
        if null_count[col] != 0:
            print(col, null_count[col])
    str_cols = []
    num_cols = []
    for col in df.columns:
        if df[col].dtype == np.dtype('O'):
            str_cols.append(col)
        elif df[col].dtype == np.dtype('float') or df[col].dtype == np.dtype('int'):
            num_cols.append(col)
    print("-"*20 + "numeric columns" + "-"*20)
    print(num_cols)
    print("-"*20 + "string columns" + "-"*20)
    print(str_cols)
    print("-"*20 + "statistics" + "-"*20)
    print(df[num_cols].describe())
