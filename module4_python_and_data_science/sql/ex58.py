import pandas as pd
import sqlite3

# 1NF
db_file = "euro.sqlite3"
input_file = "eurofxref-hist.csv"

df = pd.read_csv(input_file, skip_blank_lines=True)
df = df.dropna(axis=1, how="all")
df = df.head(50) # Limit to first 50 rows

# Convert from wide format (date + multiple currency columns) to long format (date, currency, rate)
df_melted = df.melt(id_vars=["Date"], var_name="currency", value_name="rate")

# Connect to db
conn = sqlite3.connect(db_file)
cur = conn.cursor()

# Create table if it doesn't exist
cur.execute("""
    CREATE TABLE IF NOT EXISTS rate (
        id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        date DATE,
        currency TEXT,
        rate REAL
    );
""")

# Insert data into the db
df_melted.to_sql('rate', conn, if_exists="append", index=False)

# Close the connection
conn.commit()
conn.close()

print(f"Data successfully inserted into {db_file} (table: rate)")

