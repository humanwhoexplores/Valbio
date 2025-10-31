#!/bin/bash
set -e

# --- CONFIG ---
PROJECT_NAME="strike_backend"
APP_NAME="reports"

echo "🚀 Setting up Django backend structure for $PROJECT_NAME ..."

# Create Django project
django-admin startproject $PROJECT_NAME
cd $PROJECT_NAME

# Create app
python manage.py startapp $APP_NAME

# Create management/commands directories for CSV loader
mkdir -p $APP_NAME/management/commands

# Create .env file
cat <<EOF > .env
DEBUG=1
DJANGO_SECRET_KEY=dev-secret-key
PG_DB=strike_db
PG_USER=krishchopra
PG_PASSWORD=abcdabcd
PG_HOST=valbio-postgre-server.postgres.database.azure.com
PG_PORT=5432
PG_SSLMODE=require
ALLOWED_HOSTS=*
EOF

# Create requirements.txt
cat <<EOF > requirements.txt
Django==4.2.25
djangorestframework==3.16.1
psycopg2-binary==2.9.11
python-dotenv==1.2.1
gunicorn==23.0.0
EOF

# Create startup.sh
cat <<'EOF' > startup.sh
#!/bin/bash
set -e
python manage.py collectstatic --noinput
python manage.py migrate
gunicorn strike_backend.wsgi --bind=0.0.0.0:${PORT:-8000}
EOF
chmod +x startup.sh

# Create placeholder files for your minimal structure
touch $APP_NAME/models.py \
      $APP_NAME/serializers.py \
      $APP_NAME/views.py \
      $APP_NAME/urls.py \
      $APP_NAME/management/commands/load_strikes.py

echo "✅ Basic structure created under $(pwd)"
echo
echo "Next steps:"
echo "1️⃣ Edit $PROJECT_NAME/settings.py → add 'rest_framework' and '$APP_NAME' in INSTALLED_APPS"
echo "2️⃣ Replace placeholder files with actual code snippets I gave you."
echo "3️⃣ Run: python manage.py migrate && python manage.py runserver"
