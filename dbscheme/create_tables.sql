CREATE TABLE IF NOT EXISTS long (
  id serial PRIMARY KEY,
  url VARCHAR,
    UNIQUE(url)
);

CREATE TABLE IF NOT EXISTS short (
  id serial PRIMARY KEY,
  long_id INTEGER REFERENCES long(id),
  url VARCHAR(25)
);
