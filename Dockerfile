# Base docker image
FROM python:3.8-alpine

# Working directory
WORKDIR /app

# Copy files to the docker image
COPY ./app.py /app
COPY ./requirements.txt /app
COPY ./database-test.json /app

# Install dependencies
RUN pip install -r requirements.txt

# Set environment variables
ENV FLASK_APP app.py

# Run
ENTRYPOINT [ "flask" ]

# Arguments
CMD ["run", "--host", "0.0.0.0"]
