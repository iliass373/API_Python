## Getting started

#### Change the env file

put the url value on url.env where the picture is stored, example : 
```
url =  https://****/picture.jpg
```
#### RUN the container
```
docker-compose up -d --build 
```

### Output ( Example )

app_1  | DEBUG:urllib3.connectionpool:Starting new HTTPS connection (1): anass-test.s3.eu-west-3.amazonaws.com:443
app_1  | DEBUG:urllib3.connectionpool:https://anass-test.s3.eu-west-3.amazonaws.com:443 "GET /instantane.jpg HTTP/1.1" 200 109361
app_1  | METADATA :  {'ExifVersion': b'0230', 'FlashPixVersion': b'0100', 'DateTimeOriginal': '2023:03:27 00:55:53', 'ExifOffset': 128, 'Model': 'HP HD Webcam [Fixed]: HP HD Web', 'Software': 'cheese 3.34.0', 'DateTime': '2023:03:27 00:55:53'}
api_python_app_1 exited with code 0



##### Code :

## app.py 

is the API written in python that accept url of an image and return the metadata

## Requirements.txt

the python library that the app.py will need to do the task 

## url.env 

the env file that you contains the url variable 

## Dockerfile

used to build the app.py as a container with the url variable given from .env 

