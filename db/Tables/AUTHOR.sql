USE BKEL;

CREATE TABLE IF NOT EXISTS AUTHOR (
    AuthorId INTEGER NOT NULL AUTO_INCREMENT,
    AuthorName VARCHAR(255) NOT NULL,
    PRIMARY KEY (AuthorId)
);

LOAD DATA INFILE '/mnt/DAE242A5E242862B/Code/db/Excel/author.csv' 
INTO TABLE AUTHOR
    FIELDS TERMINATED BY ','
    LINES TERMINATED BY '\r\n'
    IGNORE 1 LINES
    (AuthorId, AuthorName);