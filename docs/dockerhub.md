# Uploading to Docker Hub

```bash
ETHEREUMETL_VERSION=1.11.0
docker build -t xdc-etl:${ETHEREUMETL_VERSION} -f Dockerfile .
docker tag xdc-etl:${ETHEREUMETL_VERSION} blockchainetl/xdc-etl:${ETHEREUMETL_VERSION}
docker push blockchainetl/xdc-etl:${ETHEREUMETL_VERSION}

docker tag xdc-etl:${ETHEREUMETL_VERSION} blockchainetl/xdc-etl:latest
docker push blockchainetl/xdc-etl:latest
```