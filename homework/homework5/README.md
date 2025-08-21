# Data Storage

## Folders
- data/raw/ to store timestamped CSV exports.
- data/processed/ to store timestamped Parquet exports.

Path can be overridden in your .env file :

~~~
DATA_DIR_RAW = your storage location RAW

DATA_DIR_PROCESSED = your storage location PROCESSED
~~~

## Formats

- **CSV** for readability

    universally supported
    
- **Parquet** for efficiency 
    
    requires pyarrow or fastparquet

## How the core reads and writes

The code is aware of where we want to store our data thanks to the .env file.

### Write function

The write_df function takes a dataframe and a path (including the name of the file) and creates it or raise an error if the extension isn't CSV or Parquet.

### Read function

The read_df function takes a path, auto-parses the date column if it exists, and returns a pandas dataframe or raises an error if the path given does not lead to a CSV or a Parquet file.

## Assumptions and Validation

- The shape and dtypes should be maintained
- The price should be numeric
- The date should be of type datetime