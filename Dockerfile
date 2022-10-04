# FROM python:3.10.0-slim

# RUN apt-get update \
#     && apt-get install --no-install-recommends -y \
#     curl \
#     build-essential \
#     netcat \
#     gcc \
#     postgresql \
#     && apt-get clean