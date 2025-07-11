#!/bin/bash

# === Settings ===
IMAGE_NAME="ai-weather-agent"
DOCKERFILE_PATH="Dockerfile"  # or change if needed
BUILD_CONTEXT="."
TAG="latest"

# === Remove old image if it exists ===
echo "🧹 Checking for existing image: $IMAGE_NAME:$TAG"
EXISTING_IMAGE_ID=$(docker images -q "$IMAGE_NAME:$TAG")

if [ -n "$EXISTING_IMAGE_ID" ]; then
    echo "🗑 Removing old image: $EXISTING_IMAGE_ID"
    docker rmi -f "$EXISTING_IMAGE_ID"
else
    echo "✅ No existing image found."
fi

# === Build fresh image ===
echo "⚙️ Building new Docker image..."
docker build -t "$IMAGE_NAME:$TAG" -f "$DOCKERFILE_PATH" "$BUILD_CONTEXT"

# === Cleanup exited containers from this image (optional) ===
echo "🧹 Removing exited containers based on $IMAGE_NAME"
docker ps -a -q --filter ancestor="$IMAGE_NAME:$TAG" --filter status=exited | xargs -r docker rm

echo "✅ Docker image $IMAGE_NAME:$TAG built successfully!"

