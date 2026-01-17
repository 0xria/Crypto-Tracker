## Running the Project with Docker

This project includes a `Dockerfile` and a `docker-compose.yml` for containerized execution using Python 3.13-slim. The setup uses a virtual environment inside the container and installs dependencies from `requirements.txt` (ensure this file exists in your project root).

### Requirements
- Docker
- Docker Compose
- Python version: **3.13-slim** (as specified in the Dockerfile)
- `requirements.txt` file in the project root (required for dependency installation)

### Environment Variables
- An `.env` file is present in the project root. To use it, uncomment the `env_file: ./.env` line in `docker-compose.yml`.
- No specific environment variables are required by default, but you can define your own in `.env` as needed by your application.

### Build and Run Instructions
1. **Build and start the service:**
   ```sh
   docker compose up --build
   ```
   This will build the image and start the `python-app` service using the provided Dockerfile and Compose configuration.

2. **Stopping the service:**
   ```sh
   docker compose down
   ```

### Configuration Notes
- The application runs as a non-root user (`appuser`) inside the container for improved security.
- No ports are exposed by default, as the application does not specify any network services.
- No volumes or persistent storage are configured.
- If you need to pass environment variables, use the `.env` file and ensure the corresponding line is uncommented in `docker-compose.yml`.

### Ports
- **No ports are exposed** by default. If your application requires network access, update the `docker-compose.yml` to expose the necessary ports.

---

_This section was updated to reflect the current Docker-based setup for this project._