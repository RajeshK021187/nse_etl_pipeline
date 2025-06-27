import pandas as pd
import requests
import gzip

# Source URLs
UPSTOX_URL = "https://assets.upstox.com/market-quote/instruments/exchange/NSE.csv.gz"
DHAN_URL = "https://images.dhan.co/api-data/api-scrip-master.csv"

def download_and_extract_upstox(url: str = UPSTOX_URL, filename: str = "upstox_nse.csv.gz") -> pd.DataFrame:
    print("🔽 Downloading Upstox data...")
    response = requests.get(url)
    with open(filename, "wb") as f:
        f.write(response.content)

    print("📂 Extracting Upstox CSV...")
    with gzip.open(filename, 'rt') as f_in:
        df_upstox = pd.read_csv(f_in)

    return df_upstox

def download_dhan_csv(url: str = DHAN_URL, filename: str = "dhan.csv") -> pd.DataFrame:
    print("🔽 Downloading Dhan data...")
    response = requests.get(url)
    with open(filename, "wb") as f:
        f.write(response.content)

    df_dhan = pd.read_csv(filename)
    print("📋 Dhan Columns:\n", df_dhan.columns.tolist())
    return df_dhan

def extract_data():
    print("🚀 Starting extraction...")
    upstox_df = download_and_extract_upstox()
    dhan_df = download_dhan_csv()
    print("✅ Extraction complete.\n")
    return upstox_df, dhan_df
