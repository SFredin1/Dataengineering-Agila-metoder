FROM python:bookworm

RUN pip install -U setuptools

ADD index.html .

CMD ["python", "-m", "http.server"]