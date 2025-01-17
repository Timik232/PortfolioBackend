import os
import django
from pathlib import Path
import dotenv


BASE_DIR = Path(__file__).resolve().parent.parent
dotenv_file = os.path.join(BASE_DIR, os.environ.get("ENV_FILE", '.env'))
if os.path.isfile(dotenv_file):
    dotenv.load_dotenv(dotenv_file)

# Установка переменной окружения, указывающей на файл с настройками Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'PictureMe.settings')
django.setup()

from django.contrib.auth.models import User
# Функция для создания суперпользователя, если его ещё нет
def create_superuser_if_not_exists():
    username = os.environ.get('DJANGO_SUPERUSER_USERNAME', "lumpen")
    email = os.environ.get('DJANGO_SUPERUSER_EMAIL', "otrizanie@gmail.com")
    password = os.environ.get('DJANGO_SUPERUSER_PASSWORD', "not_udar")

    try:
        if not User.objects.filter(username=username).exists():
            user = User.objects.create_superuser(username, email, password)
            print(f"Superuser {user.username} created successfully!")
        else:
            print("Superuser already exists.")
    except Exception as e:
        print(f"Error creating superuser: {e}")


if __name__ == "__main__":
    create_superuser_if_not_exists()
