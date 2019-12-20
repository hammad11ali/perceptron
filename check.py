import pandas as pd

col_names =  ['A', 'B', 'C']
my_df  = pd.DataFrame(columns = col_names)
my_df.loc[len(my_df)] = [2, 4, 5]
my_df.loc[len(my_df)] = [92, 54, 36]
my_df.loc[len(my_df)] = [27, 47, 35]
my_df.to_csv("result.csv",index=False)

