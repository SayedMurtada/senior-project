--
-- File generated with SQLiteStudio v3.2.1 on Wed May 6 14:18:32 2020
--
-- Text encoding used: System
--
PRAGMA foreign_keys = off;
BEGIN TRANSACTION;

-- Table: Databases
CREATE TABLE Databases (Sr INTEGER PRIMARY KEY NOT NULL, Name VARCHAR NOT NULL, Host VARCHAR, Username VARCHAR, Password VARCHAR, Path VARCHAR);

-- Table: Designs
CREATE TABLE Designs (Sr INTEGER PRIMARY KEY AUTOINCREMENT, Name VARCHAR (255) NOT NULL, URL VARCHAR);
INSERT INTO Designs (Sr, Name, URL) VALUES (1, 'MyStyle', 'https://drive.google.com/uc?id=1VA6zA6oHJXwBgcgnUc4lTOaCrx0TH0Fp');
INSERT INTO Designs (Sr, Name, URL) VALUES (2, 'Default', NULL);

-- Table: History
CREATE TABLE History (Sr INTEGER PRIMARY KEY AUTOINCREMENT, user INTEGER REFERENCES user (Sr) ON DELETE RESTRICT ON UPDATE RESTRICT MATCH FULL NOT NULL ON CONFLICT FAIL, PageName VARCHAR (255) NOT NULL UNIQUE ON CONFLICT REPLACE, Design INTEGER REFERENCES Designs (Sr) ON DELETE RESTRICT ON UPDATE RESTRICT MATCH FULL NOT NULL);
INSERT INTO History (Sr, user, PageName, Design) VALUES (1, 1, 'MySQL_Project', 2);
INSERT INTO History (Sr, user, PageName, Design) VALUES (12, 2, 'sqlite_Project', 1);

-- Table: user
CREATE TABLE user (Sr INTEGER PRIMARY KEY AUTOINCREMENT, username VARCHAR (255) NOT NULL, Pass VARCHAR (255) NOT NULL, email VARCHAR);
INSERT INTO user (Sr, username, Pass, email) VALUES (1, 'ALI', 'mmm', NULL);
INSERT INTO user (Sr, username, Pass, email) VALUES (2, 'Mohammed', 'mmm', NULL);

COMMIT TRANSACTION;
PRAGMA foreign_keys = on;
