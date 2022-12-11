# Get the Fast API image with Python version 3.8
FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8

# Create the directory for the container
WORKDIR /app
COPY requirements.txt ./requirements.txt

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

COPY ./app.py ./

# Copy the serialized model
COPY ./models/diabetes_detector_model.pkl ./models/diabetes_detector_model.pkl

# Run by specifying the host and port
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "80"]