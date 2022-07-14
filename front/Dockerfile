FROM node:16

WORKDIR /app

COPY ./front .
RUN npm install -g npm
RUN npm install

EXPOSE 8080

CMD ["npm", "run", "serve"]