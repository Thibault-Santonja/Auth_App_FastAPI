/* Check existing databases */
SELECT datname FROM pg_database;


/* trigger update function : update timestamp */
CREATE OR REPLACE FUNCTION trigger_set_timestamp()
RETURNS TRIGGER AS $$
BEGIN
  NEW.updated_at = NOW();
  RETURN NEW;
END;
$$ LANGUAGE plpgsql;

/* ------------------ */
/* ----- Tables ----- */
/* ------------------ */
CREATE TABLE IF NOT EXISTS users (
    id          serial PRIMARY KEY,
    email       TEXT UNIQUE NOT NULL,
    username    TEXT UNIQUE NOT NULL,
    password    TEXT UNIQUE NOT NULL,
    created_at  TIMESTAMPTZ NOT NULL DEFAULT NOW(),
  updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

CREATE TRIGGER set_timestamp
BEFORE UPDATE ON users
FOR EACH ROW
EXECUTE PROCEDURE trigger_set_timestamp();

INSERT INTO public.users (id, email, username, password, created_at, updated_at) VALUES (DEFAULT, 'admin@mail.com', 'admin', 'password', DEFAULT, DEFAULT);
