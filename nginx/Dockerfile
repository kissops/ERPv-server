FROM nginx:1.15.10-alpine AS base

RUN rm /etc/nginx/conf.d/default.conf
COPY nginx.conf /etc/nginx/conf.d
