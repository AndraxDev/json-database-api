#!/usr/bin/bash

# Creating virtual network
docker network create papi

# Build docker image
echo "Building docker image json-database-api:latest..."
docker build -t json-database-api:latest .

# Run docker container
echo "Running docker container json-database-api..."
docker run -d -it --network papi --rm -p 5000:5000 json-database-api
