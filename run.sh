#!/bin/bash

#docker run --network=host --env-file .env -it aiagent_weather

# === Configuration ===
IMAGE_NAME="ai-weather-agent"
TAG="latest"
CONTAINER_NAME="ai-weather-agent-container"
PORT="11434"  # optional - change if you're exposing web API
USE_DOCKER_HOST_INTERNAL=true  # change to false if not needed

# === Check & Remove existing container ===
echo "🧹 Checking for existing container: $CONTAINER_NAME"
if [ "$(docker ps -a -q -f name=^/${CONTAINER_NAME}$)" ]; then
    echo "🗑 Removing existing container: $CONTAINER_NAME"
    docker rm -f "$CONTAINER_NAME"
fi

# === Run container ===
echo "🚀 Starting new container: $CONTAINER_NAME"

if [ "$USE_DOCKER_HOST_INTERNAL" = true ]; then
    docker run -it \
        --name "$CONTAINER_NAME" \
        --network=host \
        --env-file .env \
        "$IMAGE_NAME:$TAG"
else
    docker run -it \
        --name "$CONTAINER_NAME" \
        --env-file .env \
        "$IMAGE_NAME:$TAG"
fi

echo "✅ Container $CONTAINER_NAME is running."
