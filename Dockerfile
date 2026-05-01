FROM nginx:alpine
# Kendi config dosyamızı içeri atıyoruz
COPY nginx.conf /etc/nginx/conf.d/default.conf
COPY index.html /usr/share/nginx/html/index.html
EXPOSE 80
