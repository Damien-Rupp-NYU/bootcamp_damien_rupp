## Cleaning.py

This file contains 3 helper functions :
- `fill_missing_median()`: this function takes as argument a dataframe, and a list of column names, and returns a copy of the dataframe with all the mentionned column NaNs filled with the median, if no columns are mentionned it apply the fill to all numerical columns.

- `drop_missing`: this function takes as argument a dataframe, and can take a list of column names or a threshold. If columns are provided, it returns a copy of the dataframe with all rows dropped where those columns contain NaN. If a threshold is provided, it drops rows that have fewer than *threshold * total_columns* non-NaN values. If neither is given, it simply drops all rows that contain any NaN.

- `normalize_data()`: this function takes as argument a dataframe, and optionally a list of column names and a method ('minmax' or 'standard'). It returns a copy of the dataframe where the selected columns are scaled, with 'minmax' rescaling values to the range [0,1] and 'standard' standardizing values to mean 0 and variance 1. If no columns are specified, it applies the transformation to all numerical columns.

## Justification of cleaning choices:
  - `age`: rows with missing values are dropped because age is essential and cannot be reliably imputed.
  - `income` & `score`: median imputation is robust to outliers and preserves distribution.
  - `extra_data`: dropped because it contains only one usable value.
  - Scaling: MinMax scaling for continuous values to normalize ranges.  

If dataset expands with extreme values, re-evaluate MinMax choice.
