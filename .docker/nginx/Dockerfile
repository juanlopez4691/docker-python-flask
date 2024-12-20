FROM nginx:latest

COPY nginx.conf /etc/nginx/conf.d/default.conf
COPY certs/cert.pem /etc/nginx/certs/cert.pem
COPY certs/cert-key.pem /etc/nginx/certs/cert-key.pem

EXPOSE 80 443
