FROM python:3.11.9-alpine3.19

ADD ./main.py .

RUN pip install fastapi uvicorn

CMD ["uvicorn", "main:app", "--port", "8000", "--host","0.0.0.0", "--reload"]
