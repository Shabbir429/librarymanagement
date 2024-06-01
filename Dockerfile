FROM python:3.11-alpine

COPY . .

RUN pip install uvicorn
RUN pip install fastapi

CMD ["uvicorn", "main:app"]