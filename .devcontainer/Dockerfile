FROM ubuntu:focal

ENV LANG C.UTF-8

ENV DEBIAN_FRONTEND=noninteractive

ARG USERNAME=vscode
ARG USER_UID=1000
ARG USER_GID=$USER_UID

RUN apt-get update && \
	apt-get install -y sudo && \
	apt-get install -y software-properties-common --no-install-recommends && \
	add-apt-repository ppa:deadsnakes/ppa && \
	apt-get update && \
	apt-get install -y wget curl git python3.9 python3-distutils gpg-agent --no-install-recommends && \
	curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py && \
	python3 get-pip.py && \
	pip install jupyterlab pylint pycodestyle autopep8

RUN rm get-pip.py && \
	apt-get autoremove -y && \
	apt-get clean -y && \
	rm -rf /var/lib/apt/lists/* && \
	groupadd --gid $USER_GID $USERNAME && \
	useradd -s /bin/bash --uid $USER_UID --gid $USER_GID -m $USERNAME && \
	echo $USERNAME ALL=\(root\) NOPASSWD:ALL > /etc/sudoers.d/$USERNAME && \
	chmod 0440 /etc/sudoers.d/$USERNAME