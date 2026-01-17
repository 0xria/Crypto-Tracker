import os
import time
import requests
import psycopg2
from dotenv import load_dotenv


load_dotenv()

def fetch_db_connect():
    return psycopg2.connect(
        host='db',
        database='crypto_tracker',
        user='ria_admin',
        password='dhPPRAJxDl4fH2hA', 
        port=5432
    )

def setup_db():
    conn = None
    while True:
        try:
            conn = fetch_db_connect()
            cur = conn.cursor()
            cur.execute("""
                CREATE TABLE IF NOT EXISTS crypto_prices (
                    id SERIAL PRIMARY KEY,
                    symbol VARCHAR(10),
                    price DECIMAL,
                    retrieved_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP);
            """)
            conn.commit()
            cur.close()
            print("DB table is ready...", flush=True)
            return conn
        except Exception as e:
            print(f"DB not ready yet ({e}). Retrying...", flush=True)
            time.sleep(5)

def fetch_from_api():
    # List of coins you want to track
    coins = ['BTC-USD', 'ETH-USD', 'SOL-USD']
    
    conn = fetch_db_connect()
    cur = conn.cursor()
    
    for pair in coins:
        try:
            url = f"https://api.coinbase.com/v2/prices/{pair}/spot"
            response = requests.get(url).json()
            price = response['data']['amount']
            symbol = response['data']['base']

            cur.execute(
                "INSERT INTO crypto_prices (symbol, price) VALUES (%s, %s)",
                (symbol, price)
            )
            print(f"Captured {symbol} at ${price}", flush=True)
        except Exception as e:
            print(f"Error fetching {pair}: {e}", flush=True)
            
    conn.commit()
    cur.close()
    conn.close()

if __name__ == "__main__":
    print("Starting Crypto Tracker...", flush=True)
    setup_db()
    
    while True:
        print("Fetching data from API...", flush=True)
        try:
            fetch_from_api()
        except Exception as e:
            print(f"Error: {e}", flush=True)

        print("Waiting for next fetch...")
        time.sleep(60)