FROM python:latest

# Set the working directory
RUN mkdir /app
WORKDIR /app

RUN echo "print('Hello World')" > app.py

# Run the application

## Make the container to be able to -it
CMD ["python", "app.py"]