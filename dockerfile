# Usa l'immagine ufficiale di PostgreSQL 16 come base
FROM postgres:16

# Installa le dipendenze necessarie per compilare TimescaleDB e pgvector
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    postgresql-server-dev-16 \
    wget \
    git \
    cmake \
    ca-certificates \
    && rm -rf /var/lib/apt/lists/*

# Scarica e installa TimescaleDB dalla sorgente
RUN wget https://github.com/timescale/timescaledb/archive/refs/tags/2.17.2.tar.gz \
    && tar -xvf 2.17.2.tar.gz \
    && cd timescaledb-2.17.2 \
    && ./bootstrap \
    && cd build && make && make install \
    && cd ../.. \
    && rm -rf timescaledb-2.17.2 2.17.2.tar.gz

# Installa pgvector
RUN git clone https://github.com/pgvector/pgvector.git \
    && cd pgvector \
    && make && make install \
    && cd .. \
    && rm -rf pgvector

# Configurazione di TimescaleDB nel file di configurazione di PostgreSQL
RUN echo "shared_preload_libraries = 'timescaledb'" >> /usr/share/postgresql/postgresql.conf.sample

# Crea la directory per i dati di PostgreSQL
RUN mkdir -p /var/lib/postgresql/data
VOLUME /var/lib/postgresql/data

# Esponi la porta predefinita di PostgreSQL
EXPOSE 5432

# Comando di avvio
CMD ["postgres"]
