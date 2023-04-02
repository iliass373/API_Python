FROM ubuntu:18.04
WORKDIR /app
ARG url
ENV url=$url
# install python and pip, and delete cache
RUN apt update && apt install -y python3 python3-pip && rm -rf /var/lib/apt/lists/*

RUN pip3 install --upgrade pip

ADD . /app
# Install the dependencies
RUN pip3 install -r requirements.txt

CMD ["sh", "-c", "python3 app.py $url"]

