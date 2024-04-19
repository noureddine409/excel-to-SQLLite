import sqlite3
import pandas as pd

# Function to load XLS file into SQLite
def load_xls_to_sqlite(xls_file, table_name, conn, delimiter=','):
    try:
        cursor = conn.cursor()

        # Read XLS file into pandas DataFrame
        df = pd.read_excel(xls_file)

        # Save DataFrame to CSV with specified delimiter
        csv_file = './export.csv'
        df.to_csv(csv_file, index=False, sep=delimiter)

        # Load CSV data into SQLite table
        df.to_sql(table_name, conn, if_exists='replace', index=False, dtype='TEXT')

        print("XLS data loaded into SQLite successfully.")

    except Exception as e:
        print("Error:", e)
        conn.rollback()

    finally:
        if cursor:
            cursor.close()

# Connect to SQLite
conn = sqlite3.connect('event_logs.db')

# Load XLS file into SQLite with a different delimiter (e.g., tab)
xls_file = './export.xlsx' # change it with your excel file
table_name = 'event_logs' # choose appropriate table name

# Specify the delimiter (e.g., '\t' for tab)
load_xls_to_sqlite(xls_file, table_name, conn, delimiter='\t')

# Close the connection
conn.close()
