FROM node:18-alpine                     # Imagen base ligera con Node.js v18
WORKDIR /app                            # Directorio de trabajo dentro del contenedor
COPY package.json yarn.lock ./          # Copia definiciones de dependencias
RUN yarn install --frozen-lockfile      # Instala dependencias según lockfile
COPY . .                                # Copia el resto del código fuente
CMD ["yarn", "dev"]                     # Comando por defecto al iniciar el contenedor