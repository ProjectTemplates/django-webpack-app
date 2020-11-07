# GZIP Compression
gzip on;
gzip_buffers 64 8k;
gzip_comp_level 4;
gzip_min_length 500;
gzip_proxied any;
gzip_types text/plain text/javascript text/css application/xml application/x-javascript application/javascript application/json image/svg+xml;
gzip_http_version 1.0;
gzip_disable "msie6";
gzip_vary on;
gzip_static on;
