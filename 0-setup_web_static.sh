#!/usr/bin/env bash
# set up web server for deployment of web_static

apt-get -y update
apt-get -y install nginx

mkdir -p /data/web_static/shared/
mkdir -p /data/web_static/releases/test/
HTML="<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>"
echo -e "$HTML" >/data/web_static/releases/test/index.html

ln -sf /data/web_static/releases/test/ /data/web_static/current
chown -R ubuntu /data/
chgrp -R ubuntu /data/

CONFIG="server {
    listen 80 default_server;
    listen [::]:80 default_server;
    root /var/www/html;
    index index.html index.htm index.nginx-debian.html;
    server_name _;
    location /hbnb_static {
        alias /data/web_static/current;
    }
    location /redirect_me {
        return 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;
    }
    error_page 404 /404.html;
    location = /404.html {
        internal;
    }
}"
echo -e "$CONFIG" >/etc/nginx/sites-available/default
service nginx restart
