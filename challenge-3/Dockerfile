FROM docker.io/debian:unstable-slim
ADD --chmod="555" --checksum=sha256:49b2181401add9d9dee3c010d40db0d725a64bd692665879b58c8f478fb0b3ea https://github.com/hoexter/interview-homework-challenge-sre/raw/refs/heads/main/challenge-3/server.py /server.py
RUN apt -yU upgrade python3
EXPOSE 8080
ENTRYPOINT ["/server.py"]
