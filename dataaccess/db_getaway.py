import psycopg2 as ps


class Storage:

    def __init__(self, dbname, user, host, password):

        self.conn = ps.connect(f"dbname='{dbname}' user='{user}' host='{host}' password='{password}'")

    def save_url(self, long: str, short: str):
        cur = self.conn.cursor()
        # insert only unique value long url
        cur.execute(f"""INSERT INTO long (url) 
                        SELECT ('{long}') 
                        where not exists (select * from long where url='{long}');""")
        self.conn.commit()
        cur.execute(f"INSERT INTO short (url, long_id) VALUES ('{short}', (SELECT id FROM long WHERE url='{long}'))")
        self.conn.commit()

        cur.close()

    def close(self):
        pass
