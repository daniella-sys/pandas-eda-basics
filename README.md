# Store Inventory Analysis (Pandas EDA)

Practical mini-project demonstrating basic Exploratory Data Analysis (EDA) and file storage operations in CSV and Excel formats using the Pandas library.

## Project Description

The script generates a structured catalog of retail enterprise products, exports data into two independent formats (CSV and Excel), and then imports them to perform an initial review, dimension analysis, data type validation, and calculation of basic descriptive statistics.

## Technologies Used

- Python 3.x
- Pandas (DataFrame and Series data models, Data I/O subsystems)
- OpenPyXL (driver for working with XLSX format tables)

## Functionality and Software Methods

The project implements the following data processing stages:
1. **DataFrame Initialization** based on a dictionary with heterogeneous data types (string variables, integers).
2. **Data Export:**
   - `to_csv('store_inventory.csv', index=False)`
   - `to_excel('store_inventory.xlsx', index=False)`
3. **Data Import:**
   - `pd.read_csv()`
   - `pd.read_excel()`
4. **Exploratory Data Analysis (EDA):**
   - `.head(n)` — extraction of the first $n$ records of the table.
   - `.shape` — determination of matrix dimensions (number of rows and columns).
   - `.info()` — generation of a technical profile of the structure (presence of null values, data types in columns).
   - `.describe()` — calculation of summary statistical metrics for numeric fields (mean, standard deviation, minimum and maximum values, quartiles).

## Repository Structure

- `pandas_mod2_combined.py` — main script file implementing the business logic for generation and analysis.
- `store_inventory.csv` — generated data file in CSV format.
- `store_inventory.xlsx` — generated data file in Excel format.
- `README.md` — technical documentation of the repository.

## Deployment Instructions

1. Clone the repository:
   ```bash
   git clone [https://github.com/daniella-sys/pandas-store-analysis.git](https://github.com/daniella-sys/pandas-store-analysis.git)
