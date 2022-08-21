FROM alpine:latest

RUN apk add --update curl

CMD /bin/bash