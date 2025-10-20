# BlogWeb

## Overview
Blog API is a Django-based RESTful backend application built with Django REST Framework (DRF). It provides a platform for users to register, authenticate, create and manage blog posts, add comments, and categorize content. The application is fully dockerized, using PostgreSQL as the database, and includes JWT-based authentication.

## Features
- **User Authentication**:
  - User registration and login using JSON Web Tokens (JWT).
  - Custom user model with fields for bio and profile picture URL.
  - Only authenticated users can create, update, or delete their own posts/comments.
- **Blog Posts**:
  - CRUD operations for blog posts (Create, Read, Update, Delete).
  - Posts include title, content, author, category, and timestamps.
  - Filtering by title/content and ordering by creation/update time.
  - Pagination for post listings (10 posts per page).
- **Comments**:
  - CRUD operations for comments tied to specific posts.
  - Comments include content, author, and timestamps.
- **Categories**:
  - List and view categories for organizing posts.
- **Permissions**:
  - Read-only access for unauthenticated users.
  - Only post/comment authors can edit or delete their content.
- **Dockerized Setup**:
  - Uses Docker and Docker Compose for easy setup with PostgreSQL.

## Prerequisites
- **Docker**: Ensure Docker is installed ([Install Docker](https://docs.docker.com/get-docker/)).
- **Docker Compose**: Required for managing the app and database services ([Install Docker Compose](https://docs.docker.com/compose/install/)).
- A tool like Postman or curl to test API endpoints.

## Setup and Running Instructions
1. **Clone the Repository** (or copy the code into a directory named `BlogWeb`):
   ```bash
   git clone https://github.com/nomansum/BlogWeb.git
   cd BlogWeb
   ```
   If you copied the code manually, ensure the directory structure matches the one provided.

2. **Create the Directory Structure**:
   Ensure the files are organized as follows:
   ```
   blog_api/
   ├── Dockerfile
   ├── docker-compose.yml
   ├── requirements.txt
   ├── manage.py
   ├── blog_api/
   │   ├── __init__.py
   │   ├── asgi.py
   │   ├── settings.py
   │   ├── urls.py
   │   └── wsgi.py
   ├── users/
   │   ├── __init__.py
   │   ├── admin.py
   │   ├── apps.py
   │   ├── migrations/
   │   ├── models.py
   │   ├── serializers.py
   │   ├── tests.py
   │   ├── urls.py
   │   └── views.py
   └── blog/
       ├── __init__.py
       ├── admin.py
       ├── apps.py
       ├── migrations/
       ├── models.py
       ├── serializers.py
       ├── tests.py
       ├── urls.py
       └── views.py
   ```

3. **Build and Run with Docker Compose**:
   ```bash
   docker-compose up --build
   ```
   This command:
   - Builds the Docker image for the Django app.
   - Starts the PostgreSQL database and Django app containers.
   - Automatically runs migrations to set up the database.
   - Exposes the app at `http://localhost:8000`.

4. **Create a Superuser** (optional, for admin access):
   ```bash
   docker-compose exec web python manage.py createsuperuser
   ```
   Follow the prompts to create an admin user. Access the admin panel at `http://localhost:8000/admin/`.

5. **Access the API**:
   - The API is available at `http://localhost:8000/api/`.
   - Use a tool like Postman to interact with the endpoints.

6. **Stop the Application**:
   ```bash
   docker-compose down
   ```

## API Endpoints
- **Authentication**:
  - `POST /api/auth/register/` - Register a new user (username, email, password).
  - `POST /api/auth/login/` - Login to get JWT access and refresh tokens.
  - `POST /api/auth/token/refresh/` - Refresh an access token using a refresh token.
- **Categories**:
  - `GET /api/categories/` - List all categories (public).
- **Posts**:
  - `GET /api/posts/` - List all posts (supports ?search=term and ?ordering=created_at).
  - `POST /api/posts/` - Create a new post (authenticated users).
  - `GET /api/posts/<id>/` - Retrieve a post.
  - `PUT /api/posts/<id>/` - Update a post (author only).
  - `DELETE /api/posts/<id>/` - Delete a post (author only).
- **Comments**:
  - `GET /api/posts/<post_id>/comments/` - List comments for a post.
  - `POST /api/posts/<post_id>/comments/` - Create a comment (authenticated users).
  - `GET /api/comments/<id>/` - Retrieve a comment.
  - `PUT /api/comments/<id>/` - Update a comment (author only).
  - `DELETE /api/comments/<id>/` - Delete a comment (author only).

## Example API Requests
- **Register a User**:
  ```bash
  curl -X POST http://localhost:8000/api/auth/register/ \
  -H "Content-Type: application/json" \
  -d '{"username": "testuser", "email": "test@example.com", "password": "securepass123"}'
  ```
- **Login**:
  ```bash
  curl -X POST http://localhost:8000/api/auth/login/ \
  -H "Content-Type: application/json" \
  -d '{"username": "testuser", "password": "securepass123"}'
  ```
- **Create a Post** (use the access token from login):
  ```bash
  curl -X POST http://localhost:8000/api/posts/ \
  -H "Authorization: Bearer <access_token>" \
  -H "Content-Type: application/json" \
  -d '{"title": "My Post", "content": "Content here", "category": 1}'
  ```

## Notes for Production
- **Secret Key**: Replace the `SECRET_KEY` in `blog_api/settings.py` with a secure value and store it in an environment variable.
- **Environment Variables**: Use a `.env` file or Docker secrets for sensitive data (e.g., database credentials).
- **Debug Mode**: Set `DEBUG = False` in `blog_api/settings.py` for production.
- **Gunicorn**: The Dockerfile uses Gunicorn for production-ready deployment. Adjust workers as needed.
- **Database**: Ensure the PostgreSQL volume (`postgres_data`) is backed up.
- **HTTPS**: Configure a reverse proxy (e.g., Nginx) with SSL for secure connections.
- **Scaling**: Adjust Docker Compose services for scaling (e.g., multiple Gunicorn workers).

## Troubleshooting
- **Database Issues**: Ensure the PostgreSQL container is running and accessible. Check logs with `docker-compose logs db`.
- **Migrations**: If migrations fail, run `docker-compose exec web python manage.py makemigrations` manually, then `migrate`.
- **Port Conflicts**: If port 8000 is in use, modify the `ports` section in `docker-compose.yml`.

