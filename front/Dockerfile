FROM node:16-slim

WORKDIR /app

COPY ./front .
RUN npm install -g npm
RUN npm install

EXPOSE 8080

CMD ["npm", "run", "serve"]