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
