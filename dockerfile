FROM postgres:16

# Install the necessary dependencies for building TimescaleDB from source, pgvector, and cron
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    postgresql-server-dev-16 \
    wget \
    git \
    cmake \
    ca-certificates \
    cron \
    && rm -rf /var/lib/apt/lists/*

# Install TimescaleDB 2.17.2 and build it from source
RUN wget https://github.com/timescale/timescaledb/archive/refs/tags/2.17.2.tar.gz \
    && tar -xvf 2.17.2.tar.gz \
    && cd timescaledb-2.17.2 \
    && ./bootstrap \
    && cd build && make && make install \
    && cd ../.. \
    && rm -rf timescaledb-2.17.2 2.17.2.tar.gz

# Install pgvector and build it from source
RUN git clone https://github.com/pgvector/pgvector.git \
    && cd pgvector \
    && make && make install \
    && cd .. \
    && rm -rf pgvector

# Add TimescaleDB to the shared_preload_libraries
RUN echo "shared_preload_libraries = 'timescaledb'" >> /usr/share/postgresql/postgresql.conf.sample

# Create the data directory for PostgreSQL and expose it as a volume
RUN mkdir -p /var/lib/postgresql/data
VOLUME /var/lib/postgresql/data

# Expose the PostgreSQL port
EXPOSE 5432

# Start PostgreSQL
CMD ["postgres"]
