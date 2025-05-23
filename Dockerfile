FROM ubuntu:latest
LABEL authors="Ivan"
FROM python:3.11-slim

ENTRYPOINT ["top", "-b"]

RUN pip install -r requirements.txt

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
