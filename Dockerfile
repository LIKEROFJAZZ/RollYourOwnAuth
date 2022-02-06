FROM nginx
COPY web /usr/share/nginx/html
# overwrite the default configuration
COPY nginx.conf /etc/nginx/nginx.conf
