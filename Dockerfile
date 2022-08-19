# Java 8.212
FROM openjdk:8u212-jre

WORKDIR /opt/app
COPY log-viewer-1.0.3 .

CMD /bin/bash logviewer.sh
