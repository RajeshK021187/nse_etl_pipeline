import sqlite3
from pymongo import MongoClient, UpdateOne

def load_to_mongodb(upstox_data, mongo_uri="mongodb://localhost:27017/", db_name="market_data"):
    print("📦 Connecting to MongoDB...")
    client = MongoClient(mongo_uri)
    db = client[db_name]
    collection = db["upstox_nse"]

    print("⬆️  Upserting data into MongoDB...")
    operations = []
    for _, row in upstox_data.iterrows():
        doc = row.to_dict()
        operations.append(UpdateOne(
            {"instrument_key": doc["instrument_key"]},
            {"$set": doc},
            upsert=True
        ))

    if operations:
        collection.bulk_write(operations)
    print("✅ MongoDB load complete.")

def load_to_sqlite(dhan_data, db_path="dhan_data.db"):
    print("📦 Connecting to SQLite DB...")
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    print("🧱 Creating dhan_nse table if not exists...")
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS dhan_nse (
            exchange TEXT,
            symbol_name TEXT,
            security_id TEXT PRIMARY KEY,
            trading_symbol TEXT
        )
    """)

    print("⬆️  Upserting Dhan data into SQLite...")
    for _, row in dhan_data.iterrows():
        cursor.execute("""
            INSERT INTO dhan_nse (exchange, symbol_name, security_id, trading_symbol)
            VALUES (?, ?, ?, ?)
            ON CONFLICT(security_id) DO UPDATE SET
                symbol_name=excluded.symbol_name,
                trading_symbol=excluded.trading_symbol
        """, (
            row["exchange"],
            row["symbol_name"],
            row["security_id"],
            row["trading_symbol"]
        ))

    conn.commit()
    conn.close()
    print("✅ SQLite load complete.")
