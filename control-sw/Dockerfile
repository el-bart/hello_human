FROM debian:stretch
RUN apt-get update && apt-get upgrade -y
RUN apt-get install -y python \
                       python-opencv \
                       python-serial

RUN apt-get install -y openssh-server && \
    mkdir -p /run/sshd && \
    echo 'X11UseLocalhost no' >> /etc/ssh/sshd_config
RUN mkdir -p /root/.ssh
COPY authorized_keys /root/.ssh/
ENTRYPOINT ["/usr/sbin/sshd", "-D"]
