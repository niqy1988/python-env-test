"""test python script that imports a package and uses it"""

import pandas as pd

df = pd.DataFrame(
    {'val': [1, 2, 3, 4],
     'cat': ['a', 'a', 'b', 'b']}
)

agg_df = df.groupby('cat').sum()
print(agg_df['val'])
