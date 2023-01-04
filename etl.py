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


    # TODO - # exracts the csv data as pandas dataframe
    df =  

    return  # TODO - # return the dataframe


def transform(df: DataFrame) -> DataFrame:
    '''
    cleans data

    args:
        df (DataFrame): pandas dataframe containing the raw data
    
    returns:
        df (DataFrame): pandas dataframe containing the clean data
    '''

    # TODO - # drop null values
    

    # TODO - # remove decimal from year column and convert to string
    
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

    # TODO - # write dataframe to csv

    return
