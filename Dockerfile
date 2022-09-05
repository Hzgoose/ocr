FROM ubuntu:20.04
EXPOSE 8008
WORKDIR /python/data

## for apt to be noninteractive
ENV DEBIAN_FRONTEND noninteractive
ENV DEBCONF_NONINTERACTIVE_SEEN true

RUN apt update
RUN apt install -y python3 python3-pip libtesseract-dev tesseract-ocr libleptonica-dev wget

COPY . /python/data
RUN chmod -R 775 /python/

RUN pip3 install -r requirement.txt 

ENTRYPOINT ["sh", "deploy.sh"]