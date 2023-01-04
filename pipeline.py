from etl import *



file_path = "~/basic-etl-pipeline/data/economic-indicators.csv"
save_path = "~/basic-etl-pipeline/data/clean_economic-indicators.csv"

def run_pipeline(file_path:str, save_path:str):

    # TODO - extract
    df = extract(file_path=file_path)

    # TODO - transform
    df = transform(df=df)

    # TODO - load
    load(df=df, save_path=save_path)

    return

print(__name__)

if __name__ == "__main__":

    run_pipeline(file_path=file_path, save_path=save_path)