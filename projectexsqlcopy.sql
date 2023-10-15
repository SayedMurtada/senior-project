--
-- File generated with SQLiteStudio v3.2.1 on Tue Mar 31 19:05:00 2020
--
-- Text encoding used: System
--
PRAGMA foreign_keys = off;
BEGIN TRANSACTION;

-- Table: activity
CREATE TABLE activity (Sr int (11) NOT NULL PRIMARY KEY, Title varchar (255) NOT NULL, Description varchar (255) NOT NULL, created_Date datetime NOT NULL, Activity_Type int (11) NOT NULL REFERENCES activitytype (Sr), Activity_Status int (11) NOT NULL REFERENCES activitystatus (Sr), Offered_By INT (11) NOT NULL REFERENCES user (Sr), Start_Date date NOT NULL, End_Date date NOT NULL);
INSERT INTO activity (Sr, Title, Description, created_Date, Activity_Type, Activity_Status, Offered_By, Start_Date, End_Date) VALUES (1, 'a', 'a', '2019-12-11 00:00:00', 1, 3, 1, '2019-12-11', '2019-12-11');
INSERT INTO activity (Sr, Title, Description, created_Date, Activity_Type, Activity_Status, Offered_By, Start_Date, End_Date) VALUES (2, 'abs', 'bbbbb', '0000-00-00 00:00:00', 1, 2, 1, '2019-12-11', '2019-12-12');
INSERT INTO activity (Sr, Title, Description, created_Date, Activity_Type, Activity_Status, Offered_By, Start_Date, End_Date) VALUES (4, 'abs2', 'bbb', '0000-00-00 00:00:00', 1, 2, 1, '2019-12-11', '2019-12-12');
INSERT INTO activity (Sr, Title, Description, created_Date, Activity_Type, Activity_Status, Offered_By, Start_Date, End_Date) VALUES (5, 'bbbb', 'bbbbbbbbbb', '2019-12-11 00:00:00', 1, 2, 2, '2019-12-11', '2019-12-13');
INSERT INTO activity (Sr, Title, Description, created_Date, Activity_Type, Activity_Status, Offered_By, Start_Date, End_Date) VALUES (6, 'abs3', 'aaaaaaaaaaaaaa', '0000-00-00 00:00:00', 1, 1, 2, '2019-12-09', '2019-12-12');
INSERT INTO activity (Sr, Title, Description, created_Date, Activity_Type, Activity_Status, Offered_By, Start_Date, End_Date) VALUES (13, 'aaaaaaaa', 'nnnnnnnnnnnn', '0000-00-00 00:00:00', 1, 1, 1, '2019-12-12', '2019-12-12');

-- Table: activitystatus
CREATE TABLE activitystatus (Sr int (11) NOT NULL PRIMARY KEY, Status varchar (100) NOT NULL);
INSERT INTO activitystatus (Sr, Status) VALUES (2, 'accepted');
INSERT INTO activitystatus (Sr, Status) VALUES (5, 'cancled');
INSERT INTO activitystatus (Sr, Status) VALUES (4, 'ended');
INSERT INTO activitystatus (Sr, Status) VALUES (1, 'pending');
INSERT INTO activitystatus (Sr, Status) VALUES (3, 'rejected');

-- Table: activitytype
CREATE TABLE activitytype (Sr int (11) PRIMARY KEY, Name varchar (255) NOT NULL);
INSERT INTO activitytype (Sr, Name) VALUES (1, 'ESports');

-- Table: comments
CREATE TABLE comments (Sr int (11) NOT NULL PRIMARY KEY, Content varchar (255) NOT NULL, Activity_ID int (11) NOT NULL REFERENCES activity (Sr), User_ID int (11) NOT NULL REFERENCES user (Sr));

-- Table: participation
CREATE TABLE participation (Sr int (11) PRIMARY KEY, User_ID int (11) NOT NULL REFERENCES user (Sr), Activity_ID int (11) NOT NULL REFERENCES activity (Sr), Status_ID int (11) NOT NULL REFERENCES participationstatus (Sr));
INSERT INTO participation (Sr, User_ID, Activity_ID, Status_ID) VALUES (1, 2, 4, 2);
INSERT INTO participation (Sr, User_ID, Activity_ID, Status_ID) VALUES (6, 2, 1, 2);
INSERT INTO participation (Sr, User_ID, Activity_ID, Status_ID) VALUES (9, 2, 2, 1);
INSERT INTO participation (Sr, User_ID, Activity_ID, Status_ID) VALUES (10, 1, 5, 1);

-- Table: participationstatus
CREATE TABLE participationstatus (Sr int (255) NOT NULL PRIMARY KEY, Status varchar (20) NOT NULL);
INSERT INTO participationstatus (Sr, Status) VALUES (2, 'accepted');
INSERT INTO participationstatus (Sr, Status) VALUES (1, 'pending');
INSERT INTO participationstatus (Sr, Status) VALUES (3, 'rejected');

-- Table: profile
CREATE TABLE profile (Sr int (11) NOT NULL PRIMARY KEY, U_ID int (10) NOT NULL REFERENCES user (Sr), Full_Name varchar (100) DEFAULT NULL, State varchar (100) DEFAULT NULL, City varchar (100) DEFAULT NULL);
INSERT INTO profile (Sr, U_ID, Full_Name, State, City) VALUES (1, 1, 'Murtada Alawami', 'State A', 'City B');
INSERT INTO profile (Sr, U_ID, Full_Name, State, City) VALUES (2, 2, NULL, NULL, NULL);

-- Table: user
CREATE TABLE user (Sr int (11) NOT NULL PRIMARY KEY, Username varchar (50) NOT NULL, Email varchar (255) NOT NULL, Password varchar (5000) NOT NULL, created_Date datetime NOT NULL, User_Type int (11) NOT NULL REFERENCES usertype (Sr), User_Status int (11) NOT NULL REFERENCES userstatus (Sr));
INSERT INTO user (Sr, Username, Email, Password, created_Date, User_Type, User_Status) VALUES (1, 'Murtada', 'sayed@sayed', 'mmm', '2019-12-11 00:00:00', 1, 3);
INSERT INTO user (Sr, Username, Email, Password, created_Date, User_Type, User_Status) VALUES (2, 'sayed', 'sayed2@sayed', 'mmm', '2019-12-11 00:00:00', 2, 2);

-- Table: userstatus
CREATE TABLE userstatus (Sr int (11) NOT NULL PRIMARY KEY, Status varchar (100) NOT NULL);
INSERT INTO userstatus (Sr, Status) VALUES (2, 'accepted');
INSERT INTO userstatus (Sr, Status) VALUES (4, 'blocked');
INSERT INTO userstatus (Sr, Status) VALUES (5, 'deleted');
INSERT INTO userstatus (Sr, Status) VALUES (1, 'pending');
INSERT INTO userstatus (Sr, Status) VALUES (3, 'rejected');

-- Table: usertype
CREATE TABLE usertype (Sr int (11) NOT NULL PRIMARY KEY, Name varchar (100) NOT NULL);
INSERT INTO usertype (Sr, Name) VALUES (1, 'admin');
INSERT INTO usertype (Sr, Name) VALUES (2, 'Registered');

COMMIT TRANSACTION;
PRAGMA foreign_keys = on;
