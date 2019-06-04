FROM debian:stretch
RUN apt-get update && apt-get upgrade -y

RUN apt-get install -y python \
                       python-opencv \
                       python-serial

RUN mkdir  /opt/face_follower
COPY *.py  /opt/face_follower/
COPY *.xml /opt/face_follower/
WORKDIR    /opt/face_follower
ENTRYPOINT ["./face_follower.py"]
