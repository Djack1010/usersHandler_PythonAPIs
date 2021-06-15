FROM python:3.8.5-alpine
EXPOSE 5000
WORKDIR /test_api
ADD . /test_api
RUN python -m pip install --upgrade pip setuptools wheel
RUN pip install -r requirements.txt
ENTRYPOINT [ "python" ]
CMD ["main.py"]
