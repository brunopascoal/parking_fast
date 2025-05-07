# Parking Management System

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-4.2-brightgreen)](https://www.djangoproject.com/)
[![DRF](https://img.shields.io/badge/Django_REST_Framework-3.14-red)](https://www.django-rest-framework.org/)

## Live Preview

🔗 [Access the live application here](https://parking.brunopascoal.tech/) 
- user: demo
- password: test123@@

  
🔗 [Access the live application docs here]([https://parking.brunopascoal.tech/)




A complete parking management system with vehicle and customer integration, developed using Django REST Framework.

## Key Features

- 🚗 Parking spot management
- ⏳ Vehicle check-in/check-out
- 🔐 JWT authentication
- 📊 Admin dashboard with Jazzmin
- 📄 Auto-generated API documentation (Swagger / Redoc)

## Technologies Used

- **Backend**: Django 5.2
- **API**: Django REST Framework
- **Authentication**: Simple JWT
- **Documentation**: DRF Spectacular
- **Database**: PostgreSQL (via Docker)

## Getting Started

### Prerequisites

- Docker
- Docker Compose

### Setup Instructions (Docker)

1. Clone the repository

```bash
git clone https://github.com/brunopascoal/parking_fast.git
cd parking_fast
```

2. Start the containers

```bash
docker-compose up --build
```

3. Access the application at

```
http://localhost:8080
```

### Docker Services Overview

```yaml
services:
  web:
    build: .
    restart: always
    ports:
      - "8080:8000"
    depends_on:
      - parking_db

  parking_db:
    image: postgres:15
    ports:
      - "5432:5432"
    volumes:
      - postgres_data:/var/lib/postgresql/data
    environment:
      - POSTGRES_USER=postgres
      - POSTGRES_PASSWORD=postgres
      - POSTGRES_DB=parking_fast

volumes:
  postgres_data:
```

## API Documentation

Access the interactive documentation after starting the server:

- Swagger UI: [http://localhost:8080/api/v1/docs/](http://localhost:8080/api/v1/docs/)
- Redoc: [http://localhost:8080/api/v1/redoc/](http://localhost:8080/api/v1/redoc/)

## Project Structure

```
src/
├── authentication/   # User authentication
├── customers/        # Customer management
├── parking/          # Parking spots and records
├── vehicles/         # Vehicle management
└── core/             # Core project settings
```

## Environment Variables

| Variable     | Description             | Default Value                                                   |
| ------------ | ----------------------- | --------------------------------------------------------------- |
| SECRET_KEY   | Django secret key       | Required                                                        |
| DEBUG        | Debug mode              | False                                                           |
| DATABASE_URL | Database connection URL | postgres\://postgres\:postgres\@parking_db:5432/parking_service |

> You can configure these in a `.env` file and reference them in your `settings.py` using `python-decouple` or similar.

## Running Tests

```bash
docker-compose exec web python manage.py test
```

## License

Distributed under the GNU License. See the LICENSE file for more information.

## Contact

Bruno Pascoal - [@brunopascoal](https://github.com/brunopascoal) - [bpascoal.santos@gmail.com](mailto:bpascoal.santos@gmail.com)

Project Link: [https://github.com/brunopascoal/parking_fast](https://github.com/brunopascoal/parking_fast)
