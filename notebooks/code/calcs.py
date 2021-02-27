# -*- coding: utf-8 -*-
"""
This function was created for the data science challenge from Smarthelio. All
the functios here included are to be used specifically for this propose. If
additional information in needed, please contact the functions author.

@author: dguzmanr
"""


def pr(df, p_col=None, irr_col=None, temp_col=None, pnom=None,
       temp_coef=-0.42):
    """
    This function calculates PR temperature corrected from a
    DataFrame. Module temperature coef is needed and Nominal power is in W.

    Parameters
    ----------
    df : Pamdas DataFrame
        DataFrame with time series data.
    p_col : string, optional
        Power column name. The default is None.
    irr_col : String, optional
        Irradiance in POA column name. The default is None.
    temp_col : String, optional
        Module temperature column name. The default is None.
    pnom : Float, optional
        Nominal power in [Wp]. The default is None.
    temp_coef : Float, optional
        Power temperature coeficient in %/K. The default is -0.43.

    Returns
    -------
    Pandas DataFrame
        DataFrame Series with PR temperature corrected.

    """
    col_names = [p_col, irr_col, temp_col, pnom]
    if any(x is None for x in col_names):
        raise Exception("Please define 'p_col', 'irr_col', 'temp_col' and\
                        'pnom'")
    else:
        ret_df = df.copy()
        ret_df["PR_corr"] = ((ret_df[p_col]) /
                             (pnom * (ret_df[irr_col] / 1000) *
                              (1 + ((temp_coef / 100) *
                                    (ret_df[temp_col] - 25)))))
    return ret_df[["PR_corr"]]
