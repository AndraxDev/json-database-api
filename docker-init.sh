#!/usr/bin/bash

# Build docker image
echo "Building docker image json-database-api:latest..."
docker build -t json-database-api:latest .

# Run docker container
echo "Running docker container json-database-api..."
docker run -it --rm -p 5000:5000 json-database-api
