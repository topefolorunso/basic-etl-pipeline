import pandas as pd
from pandas.core.frame import DataFrame

def extract(file_path: str) -> DataFrame:
    '''
    extracts csv data and converts to pandas Dataframe

    args:
        file_path (str): path to the csv file
    
    returns:
        df (DataFrame): pandas dataframe containing the csv data
    '''

    # exracts the csv data as pandas daaframe
    df = pd.read_csv(file_path)

    return df


def transform(df: DataFrame) -> DataFrame:
    '''
    cleans data

    args:
        df (DataFrame): pandas dataframe containing the raw data
    
    returns:
        df (DataFrame): pandas dataframe containing the clean data
    '''

    # drop null values
    df.dropna(inplace=True)

    # remove decimal from year column and convert to string
    df.Year = df.Year.astype('int').astype("str")
    
    return df

def load(df: DataFrame, save_path: str):
    '''
    writes pandas Dataframe to csv file

    args:
        df (DataFrame): pandas dataframe containing the clean data
        save_path (str): path to save the csv file
    
    returns:
        None
    '''

    # write dataframe to csv
    df.to_csv(save_path, index=False)
    return
