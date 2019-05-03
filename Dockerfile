FROM ubuntu:latest
MAINTAINER Mira Ekladious "miraekladious@gmail.com"

RUN apt-get update -y
RUN apt-get install -y python3-pip python3-dev build-essential
# RUN apt-get install python3.6

# Add source files
COPY . /app

ENV HOME=/app
WORKDIR /app

RUN pip3 install -r requirements.txt

EXPOSE 8080

ENTRYPOINT [ "python3" ]
CMD [ "app.py" ]