#!/usr/bin/env bash
set -o errexit

# Build frontend
cd frontend/courses-platform
npm install
npm run build

# Copy build to backend
rm -rf ../../backend/frontend_build
cp -r build ../../backend/frontend_build

# Setup backend
cd ../../backend
pip install -r requirements.txt
python manage.py collectstatic --noinput
python manage.py migrate
