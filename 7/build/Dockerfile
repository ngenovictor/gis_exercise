FROM ghcr.io/osgeo/gdal:ubuntu-small-3.5.2

RUN apt-get update && apt-get install -y python3-pip

WORKDIR /app

COPY data ./data

COPY build/requirements.txt ./

RUN pip3 install -r requirements.txt
