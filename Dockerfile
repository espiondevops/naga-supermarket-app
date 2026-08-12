# 1. Base Image: Use an official lightweight Python runtime
FROM python:3.10-slim

# 2. Work Directory: Set the internal folder inside the container
WORKDIR /app

# 3. Copy files & Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4. Copy application code & Run
COPY app.py .
EXPOSE 5000
CMD ["python", "app.py"]
