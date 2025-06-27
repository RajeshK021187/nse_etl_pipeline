import pandas as pd
from typing import Tuple

def transform_data(upstox_df: pd.DataFrame, dhan_df: pd.DataFrame) -> Tuple[pd.DataFrame, pd.DataFrame]:
    print("🔧 Starting transformation...")

    # ✅ Filter Upstox: Use correct values
    upstox_filtered = upstox_df[
        (upstox_df['exchange'] == 'NSE_EQ') & (upstox_df['instrument_type'] == 'EQUITY')
    ].copy()

    # ✅ Filter Dhan as before
    dhan_filtered = dhan_df[
        (dhan_df['SEM_EXM_EXCH_ID'] == 'NSE') & (dhan_df['SEM_INSTRUMENT_NAME'] == 'EQUITY')
    ].copy()

    # Normalize trading_symbol for join
    upstox_filtered['trading_symbol'] = upstox_filtered['tradingsymbol'].str.strip().str.upper()
    dhan_filtered['trading_symbol'] = dhan_filtered['SEM_TRADING_SYMBOL'].str.strip().str.upper()

    # Final Upstox DF
    upstox_final = upstox_filtered[[
        'instrument_key', 'name', 'tradingsymbol', 'trading_symbol'
    ]].copy()
    upstox_final['exchange'] = 'NSE'
    upstox_final = upstox_final.rename(columns={'tradingsymbol': 'short_name'})
    upstox_final = upstox_final[['exchange', 'instrument_key', 'short_name', 'name', 'trading_symbol']]

    # Final Dhan DF
    dhan_final = dhan_filtered[[
        'SM_SYMBOL_NAME', 'SEM_SMST_SECURITY_ID', 'trading_symbol'
    ]].copy()
    dhan_final['exchange'] = 'NSE'
    dhan_final = dhan_final.rename(columns={
        'SM_SYMBOL_NAME': 'symbol_name',
        'SEM_SMST_SECURITY_ID': 'security_id'
    })
    dhan_final = dhan_final[['exchange', 'symbol_name', 'security_id', 'trading_symbol']]

    # Debug print
    print("📊 Sample Upstox symbols:", upstox_final['trading_symbol'].dropna().unique()[:10])
    print("📊 Sample Dhan symbols:", dhan_final['trading_symbol'].dropna().unique()[:10])
    print("✅ Transformation complete.")
    return upstox_final, dhan_final

