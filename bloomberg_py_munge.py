import pandas as pd
import numpy as np

def bool_col_unnamed(col_name):
    if col_name.lower()[:7] == "unnamed":
        return True
    return False

def from_excel(path, sheet, pivot=False):
    temp_df = None
    idx_last_valid = 0
    output = pd.DataFrame([], columns=['date', 'security'])
    xlsx = pd.ExcelFile(path)
    df = pd.read_excel(xlsx, sheet)
    # iterate through all columns
    for col_name in df.columns:
        if not bool_col_unnamed(col_name):
            temp_df = pd.DataFrame([], columns=['date', 'security'])
            # if column name doesn't start with "Unnamed", it's a date list, find first instance of NaN,
            # copy list of dates up to the NaN value, and place into results
            # copy the secID and do so as well
            sec_name = col_name
            idx_last_valid = df[col_name].last_valid_index()
            series_date = df[col_name][1:idx_last_valid+1]
            temp_df.date = series_date
            temp_df.security = sec_name
        else:
            # if it starts with Unnamed, grab the value in the 0 entry, that's the column title,
            # again for the same
            header_value = str(df[col_name][0])
            if header_value != "nan":
                # length of data as the dates, place into results, but check if the column exists, if it doesn't, add it
                # if it does, then add to existing
                series_unknown = df[col_name][1:idx_last_valid+1]
                temp_df[header_value] = series_unknown
            else:
                # if it starts with unnamed but the 0 entry is a NaN, then move onto next column
                # merge temp into result
                output = pd.concat([output, temp_df])
                temp_df = None
    if temp_df is not None:
        output = pd.concat([output, temp_df])
    return output
