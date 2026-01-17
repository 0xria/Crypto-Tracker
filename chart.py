import psycopg2
import pandas as pd
import matplotlib.pyplot as plt

def create_chart():
    # Connect to the Docker DB
    conn = psycopg2.connect(host="localhost", database="crypto_tracker", 
                            user="ria_admin", password="dhPPRAJxDl4fH2hA", port=5432)
    
    # Load data into a DataFrame
    df = pd.read_sql("SELECT symbol, price, retrieved_at FROM crypto_prices", conn)
    conn.close()

    # Convert time to readable format and plot
    df['retrieved_at'] = pd.to_datetime(df['retrieved_at'])
    for coin in df['symbol'].unique():
        subset = df[df['symbol'] == coin]
        plt.plot(subset['retrieved_at'], subset['price'], label=coin)

    plt.title("Crypto Price History (from my Docker Pipeline)")
    plt.legend()
    plt.savefig("my_crypto_chart.png") # This saves the chart as an image
    print("Chart saved as my_crypto_chart.png!")

if __name__ == "__main__":
    create_chart()