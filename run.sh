set -o errexit
gunicorn portfolio.wsgi:application