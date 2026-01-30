import yfinance as yf
import os

# Ativos de exemplo da B3
tickers = ["PETR4.SA", "VALE3.SA", "ITUB4.SA", "BBDC4.SA"]

def run_ingestion():
    print("Iniciando extração de dados da B3...")
    # Cria a pasta bronze se não existir 
    os.makedirs("data/bronze", exist_ok=True)
    
    for t in tickers:
        print(f"Baixando {t}...")
        # Baixa dados históricos [cite: 70]
        df = yf.download(t, period="1y")
        
        # Limpa colunas MultiIndex [cite: 72]
        df.columns = [col[0] if isinstance(col, tuple) else col for col in df.columns]
        
        # Salva na camada Bronze [cite: 74, 75]
        output_file = f"data/bronze/{t}.csv"
        df.reset_index().to_csv(output_file, index=False)
        print(f"Arquivo {output_file} gerado.")

if __name__ == "__main__":
    run_ingestion()