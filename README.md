# NSE Instruments ETL Pipeline

This project implements a Python-based ETL pipeline that:
- Extracts NSE Equity stock master data from two public sources (Upstox & Dhan)
- Filters and transforms them to retain only valid NSE Equity instruments
- Loads:
  - Filtered Upstox data as JSON into MongoDB
  - Filtered Dhan data as rows into SQLite
- Compares both datasets using `trading_symbol`
- Generates 3 output CSVs:
  - `common_stocks.csv`
  - `only_in_upstox.csv`
  - `only_in_dhan.csv`

---

## 📁 Project Structure

```
nse_etl_pipeline/
│
├── etl_pipeline.py           # Main script to run the whole pipeline
├── extraction.py             # Step 1: Download and read data
├── transformation.py         # Step 2: Filter and normalize
├── load.py                   # Step 3: Load to MongoDB & SQLite
├── comparison.py             # Step 4: Join and generate CSVs
│
├── config.py                 # 🔄 Optional: store MongoDB/SQLite configs here
├── mongodb_schema.md         # MongoDB document structure and index info
├── sqlite_schema.sql         # SQLite table creation script
├── requirements.txt          # Python dependencies
├── README.md                 # You are here 📘
│
└── output/                   # Generated CSV files
    ├── common_stocks.csv
    ├── only_in_upstox.csv
    └── only_in_dhan.csv
```

---

## 🚀 How to Run

### 1. 📦 Install Requirements

Make sure you have Python 3.7+ installed, then run:

```bash
pip install -r requirements.txt
```

### 2. 🛠️ Ensure MongoDB is running

- The project uses `localhost:27017` for MongoDB.
- Upserts into `market_data.upstox_nse`.

### 3. ▶️ Run the ETL Pipeline

```bash
python etl_pipeline.py
```

This will:

- Download both datasets
- Filter NSE Equity instruments
- Load to MongoDB and SQLite
- Generate 3 comparison CSVs in `output/`

---

## 📋 Output Files (in `/output`)

- `common_stocks.csv`: Stocks present in both sources
- `only_in_upstox.csv`: Present only in Upstox
- `only_in_dhan.csv`: Present only in Dhan

---

## 📚 Schema Files

- **MongoDB**: see `mongodb_schema.md`
- **SQLite**: run `sqlite_schema.sql` to initialize `dhan_nse` table

---

## 📝 Assumptions & Notes

- The join key is `trading_symbol`, uppercased and stripped in both datasets.
- Only NSE Equity instruments are processed.
- Upserts are used:
  - MongoDB → key: `instrument_key`
  - SQLite → key: `security_id`

---

## 💬 Contact

For queries or issues, please reach out to the project concerned resource team.
