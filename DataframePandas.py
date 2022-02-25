#to get first 5 and last 5 elements from a datafram
# head(5) , tail(5)

import  pandas as pd
df = pd.read_csv("matches.csv")
df.head(5)