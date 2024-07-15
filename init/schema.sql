CREATE TABLE users(
	id INTEGER NOT NULL PRIMARY KEY,
	username VARCHAR(100),
	date_of_birth DATE NOT NULL,
	fullname VARCHAR(100) NOT NULL,
	[password] VARCHAR(255) NOT NULL
);

CREATE TABLE Profiles(
	id INTEGER NOT NULL PRIMARY KEY,
	[user_id] INTEGER NOT NULL,
	[role] VARCHAR(14) NOT NULL,
	consensus VARCHAR(2000) NULL
	FOREIGN KEY ([user_id]) REFERENCES Users(id)
);

CREATE TABLE Disciplines(
	id INTEGER NOT NULL PRIMARY KEY,
	instructor_id INTEGER NOT NULL,
	FOREIGN KEY (instructor_id) REFERENCES Users(id)
);

CREATE TABLE StudentAvaliation(
	id INTEGER NOT NULL PRIMARY KEY,
	discipline_id INTEGER NOT NULL,
	student_id INTEGER NOT NULL,
	comment VARCHAR(2000),
	FOREIGN KEY (discipline_id) REFERENCES Disciplines(id),
	FOREIGN KEY (student_id) REFERENCES Users(id)
);