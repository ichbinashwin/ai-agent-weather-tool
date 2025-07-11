# Docker container
FROM python:3.10-slim

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

ENV PYTHONUNBUFFERED=1

#CMD ["python", "agent.py"]
CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "8000"]

