-- settings.sql
CREATE DATABASE events;
CREATE USER eventsuser WITH PASSWORD 'events';
GRANT ALL PRIVILEGES ON DATABASE events TO eventsuser;