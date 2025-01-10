
# PyTesseract Microservice

## Objective

The objective of this project is to create a robust and scalable microservice for Optical Character Recognition (OCR) using PyTesseract. This microservice is designed to be easily deployable using Docker, making it suitable for any cloud environment.

## Deploy

To deploy this microservice, follow these steps:

1. **Clone the Git Repository:**

   First, clone the git repository to your server:

   ```sh
   git clone https://github.com/arnabd64/PyTesseract-API.git
   cd PyTesseract-API
   ```

2. **Build and Run the Docker Container:**

   You can build the Docker container and run it using the following commands:

   ```sh
   docker build -t pytesseract:latest .
   docker run -itd --name=pytesseract -p 8000:8000 pytesseract:latest
   ```

   This will build the Docker image with the tag `pytesseract:latest` and run a container named `pytesseract` that maps port 8000 of the container to port 8000 of the host.

3. **Use Docker Compose:**

   Alternatively, you can use Docker Compose to build and run the microservice. Ensure you have Docker Compose installed, then run:

   ```sh
   docker compose up --build -d
   ```

   This command will build the Docker image and start the container in detached mode using the configurations specified in the `docker-compose.yml` file.

## Additional Information

- **Dependencies:** Ensure that Docker and Docker Compose are installed on your server.
- **Configuration:** You can customize the microservice by modifying the configuration files within the repository.
- **Scalability:** This microservice is designed to be scalable. You can deploy multiple instances behind a load balancer for high availability and performance.

For any issues or enhancements, feel free to open an issue or submit a pull request.

Happy coding!
