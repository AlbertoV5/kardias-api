# REST API

Web API for Kardias Project.

## AWS Lambda


### Container

Build image.

```shell
docker build -t kardias-api . 
```

Test locally.

```shell
docker run -p 9000:8080 kardias-api 
```

More: https://docs.aws.amazon.com/lambda/latest/dg/images-create.html#images-create-from-base


