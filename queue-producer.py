import common

def insert(conn, urls):
    with conn:
        with conn.cursor() as cur:
            for url in urls:
                cur.execute("INSERT INTO entries (url) VALUES (%s);", [url])

if __name__ == "__main__":
    import sys

    conn = common.queue()
    insert(conn, sys.argv[1:])
