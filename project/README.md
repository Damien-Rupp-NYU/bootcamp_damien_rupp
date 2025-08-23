# CitiBike Bike-Sharing Demand Forecasting
## **Stage:** Problem Framing & Scoping (Stage 01)


### Problem Statement
Bike-Sharing program needs to ensure that bikes are available at busy stations while avoiding overcrowding at others. Demand varies daily depending on the weather, the seasonality, the time of the week, and occasional one-off events. Without some sort of forecasting, shortages and surpluses of bikes would happen often, leading to inefficiencies and customer dissatisfaction.

This project aims to forecast daily demand per station to improve rebalancing decisions. Aiming to improve customer satisfaction.

### Stakeholder & User
- **Stakeholder**: The manager, who is responsible for system efficiency and resource allocation.
- **User**: The operator, who will rely on forecast to plan daily bike distributions.
- **Timing**: Daily, most likely at night, so bikes can be moved before the morning rush.


### Useful Answer & Decision
- **Predictive**: Forecast daile bike demand per station, focusing on identifying where shortages or surpluses are most likely.

- **Metric**: Predict the number of rades starting at each station.

- **Artifact**: A table or list showing the ideal number of bikes to place at each station before morning rush.


### Assumptions & Constraints
- **Data availability**: Trip history data from CitiBike is published monthly. Weather data is also accessible through public APIs

- **Capacity**: Each station has a fixed docking capacity.

- **Latency**: Forecasts must be ready overnight so that bikes can be rebalanced before the morning rush.

- **Compliance**: Only publicly available data will be used.

- **Stability assumption**: Patterns (weekdays / weekend and summer / winter) remain relatively consistent.

### Known Unknowns / Risks
- **Event effects**: One-off events like marathons or strikes.

- **Data quality**: Trip logs may contain missing or inconsistent entries.

- **External changes**: Policy shifts, pricing changes, or new stations.

- **Stability assumption**: Patterns (weekdays / weekend and summer / winter) remain relatively consistent.

----------------
----------------
## **Stage:**  Tooling Setup (Stage 02)

- `requirement.txt` for reproducibility
- `.env.example` for reproducibility and privacy
- `.gitignore` to have a clean git and for privacy

----------------
----------------
## **Stage**: Python Fundamentals (Stage 03)

### Utils

- `utils.py` file is located in the `src` folder, and includes the following functions:

- `clean_columns(df)`: that lowercases everything, remove useless spaces at the begining or the end of each entry, and tries to convert to int the column that can be but are strings.

- `parse_date(df, col)`: takes a df and a column and converts it to datetime if possible.

--------------
--------------

## **Stage:**  Data Acquisition (Stage 04)

- pulled from database online

- data file not pushed because is to heavy for git

----------------
----------------

## **Stage:**  Data Storage (Stage 05)

- In `data/raw` all the monthly parquet file are stored as well as the merged one

- In `data/processed` I will store a processed and probably lighter parquet file.

----------------
----------------


## **Stage:**  Processing the Data (Stage 06)

### Assumption : 
- `tag` is the same for all the the entry it just says that it is in new york, we can drop it safely

- `id`, `nuid`, and `name` are unique per station, so I decided to only keep the `name`

- I wont be using the localisation, so I will also drop `latitude` or `longitude`

- And I will also drop `extra` because it does not provide any information useful that i cant create like `total_slot` = `bikes` + `free`

----------------
----------------


## Lifecycle Mapping
- **Framing the project** → Problem Framing & Scoping (Stage 01) → **README.md** and **stakeholder memo**

- **Setup Structure and Initialize version** → Tooling Setup (Stage 02) → **README.md** and **.gitignore** and **requirement.txt**

- **Pandas, Numpy and basic cleaning functions** → Python Fundamentals (Stage 03) → **utils.py** 

- **Get the Data** → Data acquisition (Stage 04) → **Raw trip** and **merged in a single file**

- **Store the Data** → Data acquisition (Stage 05) → **data/raw** and **data/processed**

- **Clean the Data** → Data processing (Stage 06) → **Clean processed Data set** and **Assumption listed**


### Repo Plan
/data/, /src/, /notebooks/, /docs/ ; cadence for updates