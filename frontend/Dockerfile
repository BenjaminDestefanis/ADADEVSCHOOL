FROM node:18-alpine
WORKDIR /app
COPY package.json yarn.lock ./
RUN yarn install                        # Instala dependencias del frontend
COPY . .                                # Copia el resto del código fuente
CMD ["yarn", "dev", "--host"]           # Inicia servidor de desarrollo accesible externamente