# -*- coding: utf-8 -*-
"""
This function was created for the data science challenge from Smarthelio. All
the functios here included are to be used specifically for this propose. If
additional information in needed, please contact the functions author.

@author: dguzmanr
"""

import pandas as pd
from os.path import join


def read_data(xls_file):
    """
    This function takes an .xls file (called Challenge1.xls), creates a
    timeseries pandas DataFrame and returns it

    Parameters
    ----------
    xls_file : String
        File name, including the complet path.

    Returns
    -------
    df_out : Pandas DataFrame
        Pandas DataFrame with measurements.

    """
    # read .xls file and returns a pandas DataFrame
    df_out = pd.read_excel(xls_file, header=1)
    # drop unused columns
    df_out = df_out.drop([0])
    # set index to Datetime, ideal to work with time series data
    df_out = df_out.set_index(pd.DatetimeIndex(df_out.curve)).drop("curve",
                                                                   axis=1)
    df_out = df_out.rename_axis("Date")
    # drop missing values specifically in the DateTime column
    df_out = df_out[df_out.index.notnull()]
    return df_out


if __name__ == "__main__":
    # Raw data import
    # reading .xls file
    file = join(
        r"D:\Users\dguzmanr\Desktop\smarthelio\data\Challenge1.xlsx")
    ch1_df = read_data(file)
    print(ch1_df)
