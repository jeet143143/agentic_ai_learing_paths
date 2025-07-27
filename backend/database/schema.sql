CREATE TABLE learners (
  id SERIAL PRIMARY KEY,
  name TEXT NOT NULL,
  email TEXT UNIQUE NOT NULL,
  goal TEXT,
  progress JSONB
);
