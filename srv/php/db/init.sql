
DROP TABLE IF EXISTS infos;
DROP TABLE IF EXISTS users;
CREATE TABLE users(
  ID VARCHAR(50) PRIMARY KEY,
  password VARCHAR(50) NOT NULL,
  token VARCHAR(50)
);
CREATE TABLE infos(
  ID VARCHAR(50),
  date DATE  NOT NULL,
  time TIME NOT NULL,
  FOREIGN KEY(ID) REFERENCES users(ID)
);




INSERT INTO users(ID, password) VALUES('userid', 'password');
INSERT INTO infos(ID, date, time) VALUES('userid', '2022-03-20', '15:41:42'),('userid', '2022-03-21', '15:41:42');
