# Use an official Python image as a base
FROM python:3.10-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements and application files
COPY main.py /app/
COPY requirements.txt /app/

# Install FastAPI and Uvicorn
RUN pip install fastapi uvicorn

# Expose the application port
EXPOSE 8000

# Command to run the Uvicorn server
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
