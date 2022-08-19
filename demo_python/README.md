https://github.com/sevdokimov/log-viewer

docker build -t log-viewer-java .

docker run --rm -it -v $(pwd)/logs:/my-app/logs -p 8111:8111 log-viewer-java:latest
docker run --rm -it -v $(pwd)/logs:/var/log/my-app -v $(pwd)/config:/opt/app/config -p 8111:8111 log-viewer-java:latest

docker run --rm -it -v $(pwd)/logs:/root/logs -v $(pwd)/config:/opt/app/config -p 8111:8111 log-viewer-java:latest

#https://logback.qos.ch/manual/layouts.html#conversionWord

http://127.0.0.1:8111/log?path=%2Fmy-app%2Flogs%2Ftest.log