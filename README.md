# ReviewHood 🎥

Welcome to **ReviewHood**, a Django-based REST API platform designed for managing movies, actors, genres, and reviews! The API allows you to perform CRUD operations on movies, actors, genres, and reviews, with JWT authentication for secure access.

## Table of Contents
1. [Project Overview](#project-overview)
2. [Features](#features)
3. [Installation](#installation)
4. [Endpoints](#endpoints)
5. [Authentication](#authentication)
6. [Environment Variables](#environment-variables)
7. [License](#license)

---

## Project Overview

ReviewHood is a REST API backend built with Django and Django REST Framework (DRF). It serves as a database and interface for applications needing information about movies, genres, and actors. It supports:
- CRUD operations for Movies, Actors, Genres, and Reviews.
- JWT-based authentication for secure API calls.

---

## Features

- **Movies**: Manage movies with details like name, rating, release date, associated genres, and actors.
- **Actors**: Create, retrieve, update, and delete actors.
- **Genres**: Categorize movies into genres and retrieve movies by genre.
- **Reviews**: Add and manage reviews for movies.
- **Authentication**: Secure access using JWT authentication.

---

## Installation

### Prerequisites
- Python >= 3.12
- PostgreSQL
- Virtual Environment (optional but recommended)

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/AmulyaParitosh/ReviewHood.git
   cd reviewhood
   ```

2. Install dependencies:
   ```bash
   pip install .
   ```

3. Create a `.env` file in the root directory and set up environment variables (see [Environment Variables](#environment-variables)).

4. Run migrations:
   ```bash
   python manage.py migrate
   ```

5. Create a superuser:
   ```bash
   python manage.py createsuperuser
   ```

6. Start the development server:
   ```bash
   python manage.py runserver
   ```

7. Access the API at:
   ```
   http://127.0.0.1:8000/api/
   ```

---

## Endpoints

Below is an overview of the endpoints available in **ReviewHood**.

### **Actors**
| Method | Endpoint                | Description                     |
|--------|-------------------------|---------------------------------|
| GET    | `/api/actors`           | Get all actors                 |
| GET    | `/api/actors/:id`       | Get an actor by ID             |
| POST   | `/api/actors`           | Create a new actor             |
| PUT    | `/api/actors/:id`       | Update an actor by ID          |
| DELETE | `/api/actors/:id`       | Delete an actor by ID          |

### **Movies**
| Method | Endpoint                | Description                     |
|--------|-------------------------|---------------------------------|
| GET    | `/api/movies`           | Get all movies                 |
| GET    | `/api/movies/:id`       | Get a movie by ID              |
| POST   | `/api/movies`           | Create a new movie             |
| PUT    | `/api/movies/:id`       | Update a movie by ID           |
| DELETE | `/api/movies/:id`       | Delete a movie by ID           |

### **Genres**
| Method | Endpoint                | Description                     |
|--------|-------------------------|---------------------------------|
| GET    | `/api/genres`           | Get all genres                 |
| GET    | `/api/genres/:id`       | Get a genre by ID              |
| POST   | `/api/genres`           | Create a new genre             |
| PUT    | `/api/genres/:id`       | Update a genre by ID           |
| DELETE | `/api/genres/:id`       | Delete a genre by ID           |

### **Reviews**
| Method | Endpoint                          | Description                     |
|--------|-----------------------------------|---------------------------------|
| GET    | `/api/movies/:movie_id/reviews`   | Get all reviews for a movie    |
| POST   | `/api/movies/:movie_id/reviews`   | Add a review for a movie       |
| GET    | `/api/movies/:movie_id/reviews/:id`| Get a review by ID             |
| PUT    | `/api/movies/:movie_id/reviews/:id`| Update a review by ID          |
| DELETE | `/api/movies/:movie_id/reviews/:id`| Delete a review by ID          |

### **Auth**
| Method | Endpoint         | Description         |
|--------|------------------|---------------------|
| POST   | `/api/token`     | Obtain JWT token    |

---

## Authentication

**JWT Authentication** is used for secured endpoints:
1. Obtain a JWT token via the `/api/token` endpoint.
2. Use the token in the `Authorization` header as:
   ```
   Authorization: Bearer <your-token>
   ```

---

## Environment Variables

Create a `.env` file in the root directory with the following keys:

```env
POSTGRES_DB_NAME=db-name
POSTGRES_USER=db_user_name
POSTGRES_PASSWORD=db_password
POSTGRES_HOST="127.0.0.1"
POSTGRES_PORT="5432"

```

---

## License

This project is licensed under the [MIT License](LICENSE).

---
