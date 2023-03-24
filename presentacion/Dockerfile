FROM node:19.0.1-alpine as build

WORKDIR /app

COPY . .
RUN npm install
RUN npm run build

FROM nginx:1.17.1-alpine
COPY --from=build /app/dist/portal /usr/share/nginx/html
COPY /server/nginx.conf /etc/nginx/conf.d/default.conf
EXPOSE 80
