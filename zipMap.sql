DROP DATABASE IF EXISTS zipMap_db;

CREATE DATABASE zipMap_db;

USE zipMap_db;

CREATE TABLE Province(
    province_id INTEGER NOT NULL UNIQUE AUTO_INCREMENT,
    province_name VARCHAR(50),
    PRIMARY KEY (province_id)
);

CREATE TABLE Zip_code(
    zip_id INTEGER NOT NULL UNIQUE AUTO_INCREMENT,
    postal_code VARCHAR(100),
    country_code VARCHAR(100) DEFAULT '041',
    latitude DECIMAL,
    longitude DECIMAL,
    city VARCHAR(50),
    province_id INTEGER,
    FOREIGN KEY (province_id) REFERENCES Province(province_id),
    PRIMARY KEY (zip_id)
);

CREATE TABLE User_profile(
    user_id INTEGER NOT NULL UNIQUE AUTO_INCREMENT,
    username VARCHAR(50) UNIQUE NOT NULL,
    password VARCHAR(400) NOT NULL,
    natural_name VARCHAR(50),
    lastname VARCHAR(50),
    email VARCHAR(100) UNIQUE NOT NULL,
    phone INTEGER DEFAULT NULL,
    recovery_email VARCHAR(100) DEFAULT NULL,
    sec_question VARCHAR(100) DEFAULT NULL,
    zip_id INTEGER,
    FOREIGN KEY (zip_id) REFERENCES Zip_code(zip_id),
    PRIMARY KEY (user_id)
);

CREATE TABLE District(
    district_id INTEGER NOT NULL UNIQUE AUTO_INCREMENT,
    district_name VARCHAR(60),
    province_id INTEGER,
    FOREIGN KEY (province_id) REFERENCES Province(province_id),
    PRIMARY KEY (district_id)
);

CREATE TABLE Village(
    village_id INTEGER NOT NULL UNIQUE AUTO_INCREMENT,
    village_name VARCHAR(60),
    district_id INTEGER,
    FOREIGN KEY (district_id) REFERENCES District(district_id),
    PRIMARY KEY (village_id)
);

CREATE TABLE Neighborhood(
    neighborhood_id INTEGER NOT NULL AUTO_INCREMENT,
    neighborhood_name VARCHAR(60),
    village_id INTEGER,
    FOREIGN KEY (village_id) REFERENCES Village(village_id),
    PRIMARY KEY (neighborhood_id)
);