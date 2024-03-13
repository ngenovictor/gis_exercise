FROM ghcr.io/osgeo/gdal:alpine-small-3.8.4

WORKDIR /app

COPY data ./data

COPY build/requirements.txt /.

RUN python -m pip install -r requirements.txt
