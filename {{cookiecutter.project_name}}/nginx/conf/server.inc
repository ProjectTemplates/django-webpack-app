# Logging
access_log off;
error_log /var/log/nginx/error.log warn;
# Optimization
sendfile on;
tcp_nopush on;
tcp_nodelay on;
# Encoding
add_header Vary "Accept-Encoding";
