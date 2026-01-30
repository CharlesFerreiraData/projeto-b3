# Usa uma imagem leve do Python
FROM python:3.11-slim

# Instala o Java (essencial para o PySpark) e procps para gestão de processos
RUN apt-get update && apt-get install -y default-jre procps && apt-get clean

# Define o diretório de trabalho dentro do container
WORKDIR /app

# Copia e instala as dependências primeiro (otimiza o cache do Docker)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia todo o conteúdo do projeto para dentro do container
COPY . .

# Mantém o container vivo para execução dos comandos
CMD ["tail", "-f", "/dev/null"]