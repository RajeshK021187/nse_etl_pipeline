from extraction import extract_data
from transformation import transform_data
from load import load_to_mongodb, load_to_sqlite
from comparison import compare_and_generate_outputs

def run_etl():
    print("🚀 Starting NSE ETL Pipeline...\n")

    # Step 1: Extract data from both sources
    upstox_df, dhan_df = extract_data()

    # Step 2: Transform and filter NSE Equity instruments
    upstox_final, dhan_final = transform_data(upstox_df, dhan_df)

    # Step 3: Load data into MongoDB and SQLite
    load_to_mongodb(upstox_final)      # MongoDB: market_data.upstox_nse
    load_to_sqlite(dhan_final)         # SQLite: dhan_nse table

    # Step 4: Compare datasets and write output CSVs
    compare_and_generate_outputs(upstox_final, dhan_final)

    print("\n🎉 ETL Process Completed Successfully!")

if __name__ == "__main__":
    run_etl()
