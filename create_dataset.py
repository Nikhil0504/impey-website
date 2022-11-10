import pandas as pd

from constants import *

df = pd.DataFrame(columns=["URL", "Categories", *PEOPLE])
df.to_pickle("Datasets/links.pkl")
