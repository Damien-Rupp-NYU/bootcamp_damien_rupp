import numpy as np

def print_column_names(df):
    print("Names: ")
    print(*list(df.columns))

def nb_entries_and_mean(df, column):
    return {"nb_entries": len(df), "mean": float(np.mean(df[column]))}

