FROM httpd:2.4

RUN apt-get update && apt-get install -y \
    openssl \
    && rm -rf /var/lib/apt/lists/*

RUN sed -i \
    -e 's/^#\(LoadModule proxy_module\)/\1/' \
    -e 's/^#\(LoadModule proxy_http_module\)/\1/' \
    -e 's/^#\(LoadModule ssl_module\)/\1/' \
    -e 's/^#\(LoadModule headers_module\)/\1/' \
    -e 's/^#\(LoadModule rewrite_module\)/\1/' \
    /usr/local/apache2/conf/httpd.conf

COPY pictureme.conf /usr/local/apache2/conf/extra/
RUN echo "Include conf/extra/pictureme.conf" >> /usr/local/apache2/conf/httpd.conf

EXPOSE 8088 442