import psycopg2
import pandas as pd

def export_to_csv():
    try:
        # Connect to the Docker DB (using localhost since it's forwarded)
        conn = psycopg2.connect(
            host="localhost",
            database="crypto_tracker",
            user="ria_admin",
            password="dhPPRAJxDl4fH2hA",
            port=5432
        )
        
        # Pull everything into a Pandas DataFrame
        query = "SELECT * FROM crypto_prices ORDER BY retrieved_at DESC"
        df = pd.read_sql(query, conn)
        
        # Save to your folder
        df.to_csv("crypto_history.csv", index=False)
        print(f"📊 Exported {len(df)} rows to crypto_history.csv!")
        
        conn.close()
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    export_to_csv()