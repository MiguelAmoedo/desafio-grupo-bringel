# Usando a imagem oficial do Node.js
FROM node:18

# Definindo o diretório de trabalho dentro do container
WORKDIR /app

# Instalando as dependências
COPY package*.json ./
RUN npm install

# Expondo a porta que o React vai rodar (3000)
EXPOSE 3000

# Copiando o código fonte para o container (apenas o código local)
COPY . .

# Comando para iniciar o servidor do React (modo de desenvolvimento)
CMD ["npm", "start"]
