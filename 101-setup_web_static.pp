# Install nginx server

exec { 'install':
  provider => shell,
  command  => "sudo apt-get -y update ; sudo apt-get -y install nginx ; sudo ufw allow 'Nginx HTTP' ; mkdir -p /data/web_static/shared/ ; mkdir -p /data/web_static/releases/test/ ; echo -e '<html>\n  <head>\n  </head>\n  <body>\n    Holberton School\n  </body>\n</html>' >/data/web_static/releases/test/index.html ; ln -sf /data/web_static/releases/test/ /data/web_static/current ; chown -R ubuntu /data/ ; chgrp -R ubuntu /data/ ; sudo echo -e 'server {\n    listen 80 default_server;\n	  listen [::]:80 default_server;\n    root /var/www/html;\n	  index index.html index.htm index.nginx-debian.html;\n    server_name _;\n    location /hbnb_static {\n        alias /data/web_static/current;\n    }\n    location / {\n		try_files \$uri \$uri/ =404;\n	}\n    if ( \$request_filename ~ redirect_me ) {\n        rewrite ^ https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;\n    }\n}' >/etc/nginx/sites-available/default ; service nginx restart"
}
