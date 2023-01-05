# APIs for Financial Planning

APIs for Financial Planning activities such as pension estinamtions, asset management, income simulations and so on.

## Demo

You can execute APIs on the API document. 👉 https://unagiken.com/fpapi/docs

## Quick start

If you have container runtime environment, you can host the APIs lightning fast⚡️
You can change the port exposed to external network by modifing `-p 80:8000`.

```bash
$ docker build -t fpapi-image .
$ docker run --name fpapi-container -p 80:8000 -it fpapi-image
```

Try it out on the API document 👉 http://127.0.0.1/docs


Of course you can start as a python application without container runtime like below:

```bash
$ pip install -r requirements.txt
$ export PYTHONPATH=./src
$ uvicorn src.run:app
```

Try it out on the API document 👉 http://127.0.0.1:8000/docs
