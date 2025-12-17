#Python Base image
FROM python:3.10-slim

# Create a non-root user
RUN useradd -m appuser

#Working directory insider the container
WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Give permission to non-root user
RUN chown -R appuser:appuser /app

USER appuser

EXPOSE 8080

#starts python app when container launches
CMD ["python", "app.py"]
