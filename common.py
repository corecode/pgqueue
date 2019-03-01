import psycopg2

def queue():
    conn = psycopg2.connect("dbname=pgqueue user=pgqueue host=localhost password=pgqueue")

    with conn:
        with conn.cursor() as cur:
            cur.execute("CREATE TABLE IF NOT EXISTS entries (id SERIAL PRIMARY KEY, priority INTEGER, filled BOOL NOT NULL DEFAULT 'f', url VARCHAR NOT NULL UNIQUE, score INTEGER);")

    return conn
