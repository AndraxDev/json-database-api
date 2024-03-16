#!/usr/bin/bash

# Uninstall docker image
echo "Stopping docker..."
docker stop $(docker ps -a -q --filter "ancestor=json-database-api:latest")
echo "Docker has been stopped."
echo "Uninstalling docker image json-database-api:latest..."
docker rmi json-database-api:latest
echo "Docker image json-database-api:latest has been uninstalled."
echo "Uninstalling virtual network papi..."
docker network rm papi
echo "Virtual network papi has been uninstalled."
