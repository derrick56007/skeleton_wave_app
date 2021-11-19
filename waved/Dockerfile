FROM ubuntu:focal

ARG WAVE_VERSION=0.19.0

RUN apt-get update && \
    apt-get -y install wget && \
    wget https://github.com/h2oai/wave/releases/download/v${WAVE_VERSION}/wave-${WAVE_VERSION}-linux-amd64.tar.gz && \
    tar -xvf wave-${WAVE_VERSION}-linux-amd64.tar.gz && \
    mv wave-${WAVE_VERSION}-linux-amd64 /wave

WORKDIR /wave

EXPOSE 10101/tcp

ENTRYPOINT [ "./waved" ]