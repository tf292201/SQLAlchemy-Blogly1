-- Drop existing database if it exists
DROP DATABASE IF EXISTS user_db;

-- Create the 'user_db' database
CREATE DATABASE user_db;

-- Connect to the 'user_db' database
\c user_db;

-- Create the 'users' table
CREATE TABLE users (
  id SERIAL PRIMARY KEY,
  first_name VARCHAR(255) NOT NULL,
  last_name VARCHAR(255) NOT NULL,
  image_url VARCHAR(255) DEFAULT 'default_profile_image.jpg'
);
    
<<<<<<< Updated upstream
=======
CREATE TABLE posts (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255),
    content TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    user_id INTEGER REFERENCES users(id) NOT NULL
);

CREATE TABLE tags (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL UNIQUE
);

-- Create PostsTags table
CREATE TABLE posts_tags (
    post_id INTEGER REFERENCES posts(id),
    tag_id INTEGER REFERENCES tags(id),
    PRIMARY KEY (post_id, tag_id),
    FOREIGN KEY (post_id) REFERENCES posts(id),
    FOREIGN KEY (tag_id) REFERENCES tags(id)
);
>>>>>>> Stashed changes
-- Insert 10 users into the 'users' table
INSERT INTO users (first_name, last_name) VALUES
  ('John', 'Doe'),
  ('Jane', 'Smith'),
  ('Michael', 'Johnson'),
  ('Emily', 'Davis'),
  ('David', 'Wilson'),
  ('Sarah', 'Anderson'),
  ('Matthew', 'Taylor'),
  ('Olivia', 'Brown'),
  ('Daniel', 'Miller'),
  ('Sophia', 'Moore');

-- Insert 5 tags into the 'tags' table
INSERT INTO tags (name) VALUES
  ('Technology'),
  ('Travel'),
  ('Food'),
  ('Programming'),
  ('Fashion');

-- Insert 10 posts into the 'posts' table
INSERT INTO posts (title, content, user_id) VALUES
  ('First Post', 'This is my first post!', 1),
  ('Second Post', 'This is my second post!', 2),
  ('Third Post', 'This is my third post!', 3),
  ('Fourth Post', 'This is my fourth post!', 4),
  ('Fifth Post', 'This is my fifth post!', 5),
  ('Sixth Post', 'This is my sixth post!', 6),
  ('Seventh Post', 'This is my seventh post!', 7),
  ('Eighth Post', 'This is my eighth post!', 8),
  ('Ninth Post', 'This is my ninth post!', 9),
  ('Tenth Post', 'This is my tenth post!', 10);

-- Insert 5 posts-tags associations into the 'poststags' table
INSERT INTO posts_tags (post_id, tag_id) VALUES
  (1, 1), -- Post with ID 1 is associated with Tag with ID 1
  (1, 2), -- Post with ID 1 is associated with Tag with ID 2
  (2, 1), -- Post with ID 2 is associated with Tag with ID 1
  (3, 2), -- Post with ID 3 is associated with Tag with ID 2
  (3, 3); -- Post with ID 3 is associated with Tag with ID 3
