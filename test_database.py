import pytest
import psycopg2
from unittest.mock import MagicMock

# Parametri di connessione per il database
DB_HOST = "172.17.0.2"
DB_NAME = "KPI_database"
DB_USER = "postgres"
DB_PASSWORD = "password"


# Mock della funzione di connessione
@pytest.fixture
def mock_connection(mocker):
    mock_conn = mocker.patch("psycopg2.connect")
    mock_cursor = MagicMock()
    mock_conn.return_value.cursor.return_value = mock_cursor
    return mock_conn, mock_cursor


# Test: connessione al database
def test_database_connection(mock_connection):
    mock_conn, mock_cursor = mock_connection

    # Simula la connessione e l'esecuzione del codice
    with psycopg2.connect(
        host=DB_HOST,
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD
    ) as conn:
        with conn.cursor() as cursor:
            cursor.execute("SELECT 1;")
            cursor.fetchall()
    # Verifica che psycopg2.connect sia stato chiamato con i parametri giusti
    mock_conn.assert_called_with(
        host=DB_HOST,
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD
    )
