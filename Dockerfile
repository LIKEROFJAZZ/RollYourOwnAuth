FROM elice/python-nginx:3.9
WORKDIR /usr/src/app

COPY api/* ./
COPY requirements.txt ./

COPY web /usr/share/nginx/html
COPY nginx.conf /etc/nginx/nginx.conf
COPY reverse-proxy.conf /etc/nginx/sites-available

RUN pip3 install --no-cache-dir -r requirements.txt
CMD [ "python3", "flask_api.py" ]

