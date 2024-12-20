ARG PYTHON_VERSION

FROM python:${PYTHON_VERSION:-3.10}-slim

WORKDIR /usr/src/app

COPY app/requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY app/ .

CMD ["python", "app.py"]
