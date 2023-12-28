<<<<<<< HEAD
=======
```markdown
>>>>>>> 813ea39e80c74384fd15a0e05c8912d24b558adb
# FastAPI Docker Tutorial
```markdown
This repository contains the code and configurations for a project that utilizes Docker Compose to run two APIs built with FastAPI.

## Project Structure

- **api1**: FastAPI application for numerical operations.
- **api2**: FastAPI application for text manipulation.

## Getting Started

### Prerequisites

- [Docker](https://www.docker.com/)

### Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/PabloReca/FastAPI-Docker-Tutorial.git
   ```

2. Navigate to the project directory:

   ```bash
   cd FastAPI-Docker-Tutorial
   ```

3. Run the project using Docker Compose:

   ```bash
   docker-compose up
   ```

   This will build and start the Docker containers for API 1 and API 2.

### Accessing the APIs

- **API 1**: [http://localhost:50001](http://localhost:50001)
  - Endpoints:
    - `/add`: Add two numbers.
    - `/subtract`: Subtract one number from another.
    - `/multiply`: Multiply two numbers.
    - `/divide`: Divide one number by another.

- **API 2**: [http://localhost:50002](http://localhost:50002)
  - Endpoints:
    - `/uppercase/{text}`: Convert text to uppercase.
    - `/lowercase/{text}`: Convert text to lowercase.

## API Documentation

- **API 1 documentation**: [http://localhost:50001/docs](http://localhost:50001/docs)
- **API 2 documentation**: [http://localhost:50002/docs](http://localhost:50002/docs)

## Stopping the Project

To stop the project, press `Ctrl + C` in the terminal where Docker Compose is running.

<<<<<<< HEAD
## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
```
=======
Просто выделите весь текст выше и скопируйте его. Затем вставьте в ваш файл README.md в репозитории на GitHub.
>>>>>>> 813ea39e80c74384fd15a0e05c8912d24b558adb
