import  pandas as pd
import numpy as np
import pickle

def save_pickle_file(df, filename):
    """ The function save the dataframe in pickle file
     df - Dataframe
     filename - filename to be saved """

    with open(filename, 'wb') as f:
      pickle.dump(df, f)

def load_pickle_file(filename):
    """ The function reads the data from pickle file and return dataframe
     filename - filename to be saved """

    with open(filename, 'rb') as f:
        df = pickle.load(f)
        return df


def aggregate_speeches(df):
    """ The function groups the data by major heading and date and returns the dataframe with aggregated speeches
     df - Dataframe """

    return df.groupby(['date','major_heading']).agg({'speech_processed': ' '.join, 'speech': ' '.join}).reset_index()

def get_speech_by_heading(df, heading):
    """ The function selects the data based on the heading and return dataframe
     df - Dataframe 
     heading - heading selected"""

    return df[df.major_heading == heading]