import numpy as np
import pandas as pd

def clean_columns(df):
    df = df.copy()
    # Lowercase everything and remvoes the spaces
    df.columns = (df.columns.str.lower().str.replace(" ", "_"))
    for col in df.columns:
        df[col] = (df[col].astype(str).str.strip().str.lower())
    
    # Clean and convert numeric-looking columns
    for col in df.columns:
        if df[col].dtype == "object":  # only try on string/object columns
            # Remove $, %, commas, spaces
            df[col] = df[col].astype(str).str.replace(r'[\$€,%]', '', regex=True)
        
            # Try converting to numeric (if it fails, stays as string)
            df[col] = pd.to_numeric(df[col], errors="ignore")
    return df

def parse_date(df, col):
    df = df.copy()
    df[col] = pd.to_datetime(df[col], errors="coerce")
    return df