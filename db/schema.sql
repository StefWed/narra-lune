CREATE TABLE books (
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    author TEXT NOT NULL,
    pages INTEGER NOT NULL,
    pub_date INTEGER NOT NULL,
    blurb TEXT NOT NULL,
    genre TEXT
);

CREATE TABLE reading_challenges (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT NOT NULL
);

CREATE TABLE prompts (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  challenge_id INTEGER NOT NULL REFERENCES reading_challenges(id) ON DELETE CASCADE,
  text TEXT NOT NULL
);

CREATE TABLE challenge_books (
  prompt_id INTEGER REFERENCES prompts(id) ON DELETE CASCADE,
  book_id INTEGER REFERENCES books(id) ON DELETE CASCADE,
  PRIMARY KEY (prompt_id, book_id)
);