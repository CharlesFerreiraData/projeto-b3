import pandas as pd
import os

def run_science():
    print("--- INICIANDO ANÁLISE DE CIÊNCIA DE DADOS ---")
    path = "data/silver/precos_limpos"
    df = pd.read_parquet(path)
    df = df.sort_values(by=["Date"])
    
    # Ciência de Dados: Tendência e Risco
    df['Media_Movel_7d'] = df['Close'].rolling(window=7).mean()
    df['Volatilidade_7d'] = df['Close'].rolling(window=7).std()
    
    print(df[['Date', 'Close', 'Media_Movel_7d', 'Volatilidade_7d']].tail(5))
    os.makedirs("data/gold/insights_ciencia", exist_ok=True)
    df.to_csv("data/gold/insights_ciencia/analise_preditiva.csv", index=False)
    print("\n--- INSIGHTS GERADOS NA CAMADA GOLD ---")

if __name__ == "__main__":
    run_science()