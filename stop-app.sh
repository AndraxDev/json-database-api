#!/usr/bin/bash

# Uninstall docker image
echo "Stopping docker..."
docker stop $(docker ps -a -q --filter "ancestor=json-database-api:latest")
echo "Docker has been stopped."
