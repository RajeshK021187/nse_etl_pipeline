import pandas as pd
import os

OUTPUT_DIR = "output"
os.makedirs(OUTPUT_DIR, exist_ok=True)

def compare_and_generate_outputs(upstox_df: pd.DataFrame, dhan_df: pd.DataFrame):
    print("🔍 Comparing datasets...")

    # Perform inner join on trading_symbol
    common = pd.merge(upstox_df, dhan_df, on="trading_symbol", how="inner")
    only_in_upstox = upstox_df[~upstox_df["trading_symbol"].isin(common["trading_symbol"])]
    only_in_dhan = dhan_df[~dhan_df["trading_symbol"].isin(common["trading_symbol"])]

    # Reorder and align columns for output
    common = common[[
        'instrument_key', 'symbol_name', 'security_id',
        'short_name', 'name', 'trading_symbol'
    ]]
    only_in_upstox = only_in_upstox[[
        'instrument_key', 'short_name', 'name', 'trading_symbol'
    ]]
    only_in_dhan = only_in_dhan[[
        'symbol_name', 'security_id', 'trading_symbol'
    ]]

    # Save CSVs
    common.to_csv(os.path.join(OUTPUT_DIR, "common_stocks.csv"), index=False)
    only_in_upstox.to_csv(os.path.join(OUTPUT_DIR, "only_in_upstox.csv"), index=False)
    only_in_dhan.to_csv(os.path.join(OUTPUT_DIR, "only_in_dhan.csv"), index=False)

    print("✅ CSVs generated: common_stocks.csv, only_in_upstox.csv, only_in_dhan.csv")
