from etl import *

file_path = "~/basic-etl-pipeline/data/economic-indicators.csv"
save_path = "~/basic-etl-pipeline/data/clean_economic-indicators.csv"



df = extract(file_path=file_path)
df = transform(df=df)
load(df=df, save_path=save_path)