# REST API

Web API for Kardias Project.

## AWS Lambda

Install requirements.

```shell
pip install -t lib -r requirements.txt
```

Zip requirements.

```shell
cd lib && zip ../lambda_function.zip -r . && cd ..
```

Include the app folder.

```shell
zip lambda_function.zip -u -r ./app
```

Include main.py

```shell
zip lambda_function.zip -u main.py
```

https://www.youtube.com/watch?v=RGIM4JfsSk0&ab_channel=pixegami
