FROM elice/python-nginx:3.9
WORKDIR /app

COPY api/* ./
COPY requirements.txt requirements.txt

COPY web /usr/share/nginx/html
COPY nginx.conf /etc/nginx/nginx.conf
COPY reverse-proxy.conf /etc/nginx/sites-available/

COPY start-services.sh ./

RUN pip3 install --no-cache-dir -r requirements.txt

CMD ["sh", "start-services.sh"]

