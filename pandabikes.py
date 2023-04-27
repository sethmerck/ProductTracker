import pandas as pd

df = pd.read_csv ('all_pages.csv')

df.Title = df.Title.str.split(expand=False)

df = df.explode('Title', ignore_index=True)

df['Counts'] = df.groupby(['Title'])['Title'].transform('count')

df = df.groupby(by=df.Title).median().sort_values('Title')

df['views/watched'] = df['Views'] / df['Watched']

df = df.sort_values('Counts', ascending=False)[:60]

print(df.sort_values('views/watched'))