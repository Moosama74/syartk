FROM python:3.12-slim

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PORT=7860

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Set open permissions so SQLite can write database & uploads
RUN chmod -R 777 /app

EXPOSE 7860

CMD ["python", "run.py"]
