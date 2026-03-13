# This is a placeholder Dockerfile 
# We'll customize this later for our specific services 
FROM python:3.11-slim 
 
WORKDIR /app 
 
COPY requirements.txt . 
RUN pip install --no-cache-dir -r requirements.txt 
 
COPY . . 
 
CMD ["uvicorn", "backend.api.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"] 
