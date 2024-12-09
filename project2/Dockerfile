# Usar a imagem oficial do Python
FROM python:3.9-slim

# Definir o diretório de trabalho dentro do container
WORKDIR /app

# Copiar os arquivos de dependências para dentro do container
COPY requirements.txt /app/

# Instalar as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copiar o código da aplicação para dentro do container
COPY . /app/

# Expôr a porta em que a aplicação Flask vai rodar
EXPOSE 5000

# Comando para rodar a aplicação Flask
CMD ["flask", "run", "--host=0.0.0.0"]
