import pytest
import psycopg2

# Parametri di connessione per il database
DB_HOST = "172.17.0.2"
DB_NAME = "KPI_database"
DB_USER = "postgres"
DB_PASSWORD = "password"


# Test: connessione al database
def test_database_connection():
    """
    Testing of the connection to the database.
    """
    try:
        # Connetti al database
        with psycopg2.connect(
            host=DB_HOST,
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD
        ) as conn:
            with conn.cursor() as cursor:
                # Esegui una query semplice per verificare la connessione
                cursor.execute("SELECT 1;")
                result = cursor.fetchone()
        # Verifica che il risultato della query sia valido
        assert result == (1,), \
            "La query SELECT 1 non ha restituito il valore atteso."

    except Exception as e:
        pytest.fail(f"Connessione al database fallita: {e}")


# Test: verifica che ci siano righe nella tabella machines
def test_select_machines():
    """
    Execute a simple SELECT query on the machines table
    and check that at least one row is returned.
    """
    try:
        # Connetti al database
        with psycopg2.connect(
            host=DB_HOST,
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD
        ) as conn:
            with conn.cursor() as cursor:
                cursor.execute("SELECT * FROM machines;")
                rows = cursor.fetchall()
        # Verifica che almeno una riga sia stata restituita
        assert len(rows) > 0, \
            "La tabella machines è vuota o non esiste."

    except Exception as e:
        pytest.fail(f"Errore durante l'esecuzione della query: {e}")
