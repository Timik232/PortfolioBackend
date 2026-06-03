<div align="center">

# 📸 PictureMe

**Photographer Portfolio Backend**

A production-grade Django application for managing photographer portfolios,
photo series, client orders, and media — powered by Docker, MySQL, and Nginx.

[![Python](https://img.shields.io/badge/Python-3.12-3776AB?logo=python&logoColor=white)](https://python.org)
[![Django](https://img.shields.io/badge/Django-5.2_LTS-092E20?logo=django&logoColor=white)](https://www.djangoproject.com)
[![Docker](https://img.shields.io/badge/Docker-Compose-2496ED?logo=docker&logoColor=white)](https://www.docker.com)
[![MySQL](https://img.shields.io/badge/MySQL-9.7-4479A1?logo=mysql&logoColor=white)](https://www.mysql.com)
[![License](https://img.shields.io/badge/License-Apache_2.0-D22128?logo=apache&logoColor=white)](LICENSE)

[//]: # (<!-- Add screenshot here -->)
[//]: # (<img src="docs/screenshot.png" width="700" alt="PictureMe Screenshot">)

</div>

---

## Features

- **Album Management** — Organize photos into series and collections
- **Photo Ordering** — Clients can request photo sessions directly
- **Admin Panel** — Grappelli-powered admin with django-filer media management
- **Responsive Portfolio** — Mobile-friendly photographer showcase
- **Custom UI** — Glowing cursor effect, smooth transitions
- **VK Integration** — Social sharing via VK API
- **SEO Ready** — robots.txt, semantic URLs, meta tags
- **Monitoring** — Prometheus metrics via django-prometheus
- **Production Hardened** — SSL, reverse proxy, static CDN, health checks

## Tech Stack

| Layer | Technology | Version |
|-------|-----------|---------|
| Backend | Django | 5.2 LTS |
| Runtime | Python | 3.12 |
| WSGI | Gunicorn | 23.0 |
| Database | MySQL | 9.7 |
| Reverse Proxy | Nginx | latest |
| Media | Pillow + easy-thumbnails | 11.x / 2.10 |
| Admin UI | django-grappelli | 4.0 |
| Container | Docker Compose | — |

## Architecture

```
                    ┌─────────────────────────────────────┐
                    │         Synology Reverse Proxy       │
                    │   (SSL termination, domain routing)  │
                    └──────────────┬──────────────────────┘
                                   │
                    ┌──────────────▼──────────────────────┐
                    │         nginx-photo (:80/:443)       │
                    │   Reverse proxy + static serving     │
                    └──────┬──────────────────────┬───────┘
                           │                      │
              ┌────────────▼──────────┐  ┌───────▼────────────┐
              │  web-django (:8010)   │  │ static-server (:79) │
              │  Django + Gunicorn    │  │  Static files CDN   │
              └────────────┬──────────┘  └────────────────────┘
                           │
              ┌────────────▼──────────┐
              │   db (:3306)          │
              │   MySQL 9.7           │
              └───────────────────────┘

  Volumes: PictureMe1 (app) | db_PictureMe (MySQL) | bind mounts (media/static/templates)
```

## Getting Started

### Prerequisites

- [Docker](https://docs.docker.com/get-docker/) + [Docker Compose](https://docs.docker.com/compose/install/)
- SSL certificates for your domain

### Installation

```bash
# Clone the repository
git clone https://github.com/Timik232/PortfolioBackend.git
cd PortfolioBackend

# Create environment file
cp .envdev .env

# Add your SSL certificates
mkdir -p ssl
# Place your cert.pem and key.pem in ssl/
```

### Configuration

Edit `.env` with your settings:

| Variable | Description | Example |
|----------|-------------|---------|
| `MYSQL_DATABASE` | Database name | `portfolio` |
| `MYSQL_USER` | Database user | `dbuser` |
| `MYSQL_PASSWORD` | Database password | `changeme` |
| `MYSQL_ROOT_PASSWORD` | Root password | `changeme` |
| `MYSQL_HOST` | Database host | `127.0.0.1` |
| `MYSQL_PORT` | Database port | `3306` |
| `DJANGO_DEBUG` | Debug mode | `False` |
| `DJANGO_ALLOWED_HOSTS` | Allowed hostnames | `photo.example.com,localhost` |
| `DJANGO_ALLOWED_CSRF` | CSRF trusted origins | `https://photo.example.com` |
| `DJANGO_SUPERUSER_USERNAME` | Admin username | `admin` |
| `DJANGO_SUPERUSER_EMAIL` | Admin email | `admin@example.com` |
| `DJANGO_SUPERUSER_PASSWORD` | Admin password | `changeme` |

### Run

```bash
# Build and start all services
docker compose up -d --build

# Check status
docker compose ps

# View logs
docker compose logs -f web-django
```

The application will be available at:
- **Portfolio:** `https://photo.yourdomain.com`
- **Admin:** `https://photo.yourdomain.com/admin/`
- **Static CDN:** `https://static.yourdomain.com`

## Development

### Pre-commit Hooks

```bash
# Install hooks
pre-commit install

# Run manually on all files
pre-commit run --all-files
```

Configured hooks:
- **black** — Code formatter
- **isort** — Import sorting (black-compatible profile)
- **flake8** — Linter (with pep8-naming, flake8-bugbear)
- **Standard checks** — trailing whitespace, EOF, merge conflicts, private keys
- **Branch protection** — prevents direct commits to `main`

### Code Quality

```bash
# Format
black .

# Sort imports
isort --profile black .

# Lint
flake8 .
```

## Project Structure

```
PortfolioBackend/
├── Dockerfile                 # Multi-stage Docker build (Python 3.12 + Bookworm)
├── docker-compose.yaml        # 4-service compose configuration
├── requirements.txt           # Python dependencies
├── .pre-commit-config.yaml    # Pre-commit hooks (black, isort, flake8)
├── .flake8                    # Flake8 configuration
├── .gitignore
├── nginx/                     # Main nginx (reverse proxy + SSL)
│   ├── Dockerfile
│   ├── nginx.conf
│   └── mime.types
├── nginx-static/              # Static file server
│   ├── Dockerfile
│   └── static-nginx.conf
├── PictureMe/
│   ├── PictureMe/             # Django project
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── wsgi.py
│   ├── portfolio/             # Main application
│   │   ├── models.py          # Album, Element, Image, Order
│   │   ├── views.py
│   │   ├── admin.py           # Grappelli admin customization
│   │   ├── urls.py
│   │   ├── form.py
│   │   ├── vk_module.py       # VK social integration
│   │   ├── fixtures/          # Initial data
│   │   ├── migrations/
│   │   └── templates/
│   │       └── photoUploading/
│   │           ├── base.html
│   │           ├── index.html
│   │           ├── series.html
│   │           ├── element.html
│   │           ├── aboutme.html
│   │           ├── contacts.html
│   │           ├── photoreports.html
│   │           └── phototerm.html
│   ├── media/                 # User uploads (gitignored)
│   └── static/                # Collected static files (gitignored)
├── superuser.py               # Auto superuser creation on startup
├── wait_for_db.sh             # DB readiness check
└── prometheus.yml             # Prometheus monitoring config
```

## License

This project is licensed under the [Apache License 2.0](LICENSE).

---

<div align="center">
Built with ❤️ by <a href="https://github.com/Timik232">Timik232</a>
</div>
