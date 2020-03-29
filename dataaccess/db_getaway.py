import psycopg2 as ps


class Storage:

    def __init__(self, dbname, user, host, password):

        self.conn = ps.connect(f"dbname='{dbname}' user='{user}' host='{host}' password='{password}'")

    def save_url(self, long, short):
        cur = self.conn.cursor()
        cur.execute(f"INSERT INTO long VALUES {long};")
        cur.execute(f"""INSERT INTO short (url, long_id) VALUES ('{short}', (SELECT id FROM long WHERE long='{long}'))""")
        self.conn.commit()

        cur.close()

    def close(self):
        pass
