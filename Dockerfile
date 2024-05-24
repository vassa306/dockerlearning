from nginx:1.25.5-alpine

COPY html /usr/share/nginx/html/

EXPOSE 80

CMD ["nginx","-g","daemon off;"]