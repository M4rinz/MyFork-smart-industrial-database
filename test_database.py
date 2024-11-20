import pytest
import psycopg2

# Connection parameters for the database
DB_HOST = "172.17.0.2"
DB_NAME = "KPI_database"
DB_USER = "postgres"
DB_PASSWORD = "password"


# Test: connection to the database
def test_database_connection():
    """
    Testing the connection to the database.
    """
    try:
        # Connect to the database
        with psycopg2.connect(
            host=DB_HOST,
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD
        ) as conn:
            with conn.cursor() as cursor:
                # Execute a simple query to verify the connection
                cursor.execute("SELECT 1;")
                result = cursor.fetchone()
        # Verify that the query result is valid
        assert result == (1,), \
            "The SELECT 1 query did not return the expected value."

    except Exception as e:
        pytest.fail(f"Database connection failed: {e}")


# Test: verify that there are rows in the machines table
def test_select_machines():
    """
    Execute a simple SELECT query on the machines table
    and check that at least one row is returned.
    """
    try:
        # Connect to the database
        with psycopg2.connect(
            host=DB_HOST,
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD
        ) as conn:
            with conn.cursor() as cursor:
                cursor.execute("SELECT * FROM machines;")
                rows = cursor.fetchall()
        # Verify that at least one row was returned
        assert len(rows) > 0, \
            "The machines table is empty or does not exist."

    except Exception as e:
        pytest.fail(f"Error during query execution: {e}")
