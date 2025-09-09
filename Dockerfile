FROM python:3.11-slim
WORKDIR /app

COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app

EXPOSE 9999
CMD ["uvicorn", "backend:app", "--host", "0.0.0.0", "--port", "9999"]
