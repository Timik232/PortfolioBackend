#!/bin/bash
set -e

host=db
port=3306

until nc -z $host $port; do
  echo "Waiting for database to be available..."
  sleep 1
done

echo "Database is available"