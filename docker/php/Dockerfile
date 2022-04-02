FROM php:8.1.4-fpm
COPY ./docker/php/php.ini /usr/local/etc/php/

RUN apt update && \
    apt upgrade -y
RUN apt install -y \
      vim \
      unzip \
      zlib1g-dev \
      libzip-dev \
      libpq-dev && \
    docker-php-ext-install \
      zip \
      pdo_pgsql \
      pgsql

#Composer install
RUN php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');"
RUN php composer-setup.php
RUN php -r "unlink('composer-setup.php');"
RUN mv composer.phar /usr/local/bin/composer

ENV COMPOSER_ALLOW_SUPERUSER 1
ENV COMPOSER_HOME /composer
ENV PATH $PATH:/composer/vendor/bin

WORKDIR /var/www
RUN composer global require "laravel/installer"
