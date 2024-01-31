CREATE DATABASE IF NOT EXISTS test;
USE test;
DROP TABLE IF EXISTS test1;
CREATE TABLE test1 (
    id INT NOT NULL AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    PRIMARY KEY (id)
) AUTO_ID_CACHE 1;

DROP TABLE IF EXISTS test2;
CREATE TABLE IF NOT EXISTS test2 (
    id INT NOT NULL AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    PRIMARY KEY (id)
) AUTO_ID_CACHE 1;

DROP TABLE IF EXISTS test3;
CREATE TABLE IF NOT EXISTS test3 (
    id INT NOT NULL AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    PRIMARY KEY (id)
);

DROP TABLE IF EXISTS test4;
CREATE TABLE IF NOT EXISTS test4 (
    id BIGINT NOT NULL AUTO_RANDOM,
    name VARCHAR(100) NOT NULL,
    PRIMARY KEY (id)
);

-- insert multiple rows into test1
INSERT INTO test1 (name) VALUES ('test1-1'), ('test1-2'), ('test1-3');
INSERT INTO test2 (name) VALUES ('test2-1'), ('test2-2'), ('test2-3'), ('test2-4');
INSERT INTO test3 (name) VALUES ('test3-1'), ('test3-2'), ('test3-3'), ('test3-4'), ('test3-5');
INSERT INTO test4 (name) VALUES ('test4-1'), ('test4-2'), ('test4-3'), ('test4-4'), ('test4-5'), ('test4-6');
