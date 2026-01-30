Este repositório contém uma solução completa de engenharia de dados para o mercado financeiro brasileiro. 
O projeto implementa um pipeline escalável que automatiza o ciclo de vida dos dados, desde a extração via API até a entrega de indicadores refinados para análise de negócios. 
A solução foi desenhada para resolver o desafio de processar dados financeiros brutos de forma resiliente, utilizando a Arquitetura Medalhão para garantir a governança e a qualidade em cada etapa.

Na Camada Bronze, ocorre a ingestão de dados históricos utilizando Python e a biblioteca yfinance, preservando os arquivos em seu estado original para garantir a linhagem da informação.
A Camada Silver realiza o processamento e limpeza com PySpark, aplicando tipagem rigorosa e convertendo os dados para o formato Parquet para otimizar o armazenamento.
Por fim, a Camada Gold realiza agregações complexas e cálculo de indicadores como médias diárias e volatilidade, preparando o produto final para consumo por dashboards ou modelos de aprendizado de máquina.

O projeto utiliza tecnologias como Python 3.11, Apache Spark, Docker e Docker-Compose. 
O uso de contêineres garante a portabilidade absoluta do pipeline e gerencia dependências complexas como a Java Virtual Machine para o Spark.
Além do processamento de engenharia, o pipeline gera insights de ciência de dados, calculando indicadores de tendência e risco como médias móveis e volatilidade de sete dias.
Para ambientes de produção, a arquitetura prevê o uso de APIs REST para disponibilizar modelos, orquestração via GitHub Actions ou Airflow para rotinas diárias e monitoramento contínuo para garantir a saúde da operação.
