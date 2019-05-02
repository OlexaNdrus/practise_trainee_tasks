# Use an official Python runtime as a parent image
FROM alpine:edge

# Install any needed packages specified in requirements.txt
RUN apk add --no-cache -y mosquitto mosquitto-clients

# Make port 80 available to the world outside this container
EXPOSE 1883

# Run app.py when the container launches
CMD mosquitto -p 1883


