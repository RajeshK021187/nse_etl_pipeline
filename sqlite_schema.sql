📄 **File:** `sqlite_schema.sql`

```sql
-- SQLite Schema for Dhan NSE Equity Instruments

CREATE TABLE IF NOT EXISTS dhan_nse (
    exchange TEXT,
    symbol_name TEXT,
    security_id TEXT PRIMARY KEY,
    trading_symbol TEXT
);

-- Note:
-- `security_id` is used as the PRIMARY KEY for upserts.
