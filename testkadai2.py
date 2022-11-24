import pandas as pd
import numpy as np

data = np.random.randint(10, 100,(5, 2))

idx =  ['Python', 'C++', 'SQL', 'Java', 'JavaScript']
col= ['2021', '2020']
df = pd.DataFrame(data=data, index=idx, columns=col)
print(df)
print(df['2021'].plot.pie(y='2021'))
