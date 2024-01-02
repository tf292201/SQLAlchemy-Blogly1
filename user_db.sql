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
