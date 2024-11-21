#!/bin/bash

# Check input parameters
if [ "$#" -ne 3 ]; then
    echo "❌ Usage: $0 <container_name> <path_to_sql_dump> <database_name>"
    exit 1
fi

# Parameters
CONTAINER_NAME=$1
DUMP_FILE=$2
DATABASE_NAME=$3

# Check if the dump file exists
if [ ! -f "$DUMP_FILE" ]; then
    echo "❌ Error: Dump file '$DUMP_FILE' does not exist."
    exit 1
fi

# Copy the dump file to the container
echo "📂 Copying dump file '$DUMP_FILE' into container '$CONTAINER_NAME'..."
docker cp "$DUMP_FILE" "$CONTAINER_NAME":/tmp/backup.sql
if [ $? -ne 0 ]; then
    echo "❌ Error copying the file into the container."
    exit 1
fi

# Check if the database exists
echo "🔍 Checking if the database '$DATABASE_NAME' exists..."
DB_EXISTS=$(docker exec -i "$CONTAINER_NAME" psql -U postgres -tAc "SELECT 1 FROM pg_database WHERE datname = '$DATABASE_NAME'")
if [ "$DB_EXISTS" != "1" ]; then
    echo "⚙️ Database '$DATABASE_NAME' does not exist. Creating it..."
    docker exec -i "$CONTAINER_NAME" psql -U postgres -c "CREATE DATABASE \"$DATABASE_NAME\";"
    if [ $? -ne 0 ]; then
        echo "❌ Error creating the database."
        exit 1
    fi
    echo "✅ Database '$DATABASE_NAME' created successfully."
else
    echo "✅ Database '$DATABASE_NAME' already exists."
fi

# Restore the database
echo "⏳ Restoring database '$DATABASE_NAME' from the dump file..."
docker exec -i "$CONTAINER_NAME" bash -c "psql -U postgres -d $DATABASE_NAME < /tmp/backup.sql"
if [ $? -ne 0 ]; then
    echo "❌ Error restoring the database."
    exit 1
fi

# Create the pgvector extension
echo "🔧 Creating pgvector extension..."
docker exec -i "$CONTAINER_NAME" psql -U postgres -d "$DATABASE_NAME" -c "CREATE EXTENSION IF NOT EXISTS vector;"
if [ $? -ne 0 ]; then
    echo "❌ Error creating pgvector extension."
    exit 1
fi
echo "✅ pgvector extension created successfully."

# Clean up: Remove the dump file from the container
echo "🧹 Cleaning up: Removing the dump file from the container..."
docker exec -i "$CONTAINER_NAME" bash -c "rm /tmp/backup.sql"
if [ $? -ne 0 ]; then
    echo "❌ Error removing the dump file from the container."
    exit 1
fi

echo "🎉 Database restoration completed successfully!"
exit 0
