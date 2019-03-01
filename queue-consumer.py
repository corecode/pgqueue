import common

def handle_one(conn):
    with conn:
        with conn.cursor() as cur:
            cur.execute("SELECT id, url FROM entries WHERE NOT filled ORDER BY RANDOM() FOR UPDATE SKIP LOCKED LIMIT 1;")
            result = cur.fetchone()
            if result is None:
                print("queue is empty")
                return False
            id, url = result
            print(url)
            cur.execute("UPDATE entries SET filled = 't', score = 1234 WHERE id = %s;", [id])
    return True

if __name__ == '__main__':
    import time

    conn = common.queue()
    while True:
        more = handle_one(conn)
        if not more:
            time.sleep(5)
