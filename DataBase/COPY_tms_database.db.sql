BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "Tutors_Weekdays" (
	"tutor_id"	INTEGER,
	"subject_id"	INTEGER,
	FOREIGN KEY("subject_id") REFERENCES "Subjects"("subject_id"),
	FOREIGN KEY("tutor_id") REFERENCES "Tutors"("tutor_id")
);
CREATE TABLE IF NOT EXISTS "Tutors_Subjects" (
	"tutor_id"	INTEGER,
	"subject_id"	INTEGER,
	FOREIGN KEY("tutor_id") REFERENCES "Tutors"("tutor_id"),
	FOREIGN KEY("subject_id") REFERENCES "Subjects"("subject_id")
);
CREATE TABLE IF NOT EXISTS "Tutors_Schools" (
	"tutor_id"	INTEGER,
	"school_id"	INTEGER,
	FOREIGN KEY("school_id") REFERENCES "Schools"("school_id"),
	FOREIGN KEY("tutor_id") REFERENCES "Tutors"("tutor_id")
);
CREATE TABLE IF NOT EXISTS "Tutors" (
	"tutor_id"	INTEGER NOT NULL DEFAULT 3000 PRIMARY KEY AUTOINCREMENT UNIQUE,
	"first_name"	TEXT NOT NULL,
	"last_name"	TEXT NOT NULL,
	"email"	TEXT
);
CREATE TABLE IF NOT EXISTS "Students_Schools" (
	"student_id"	INTEGER,
	"school_id"	INTEGER,
	FOREIGN KEY("student_id") REFERENCES "Students"("student_id"),
	FOREIGN KEY("school_id") REFERENCES "Schools"("school_id")
);
CREATE TABLE IF NOT EXISTS "Weekdays" (
	"weekday_id"	INTEGER NOT NULL DEFAULT 1 PRIMARY KEY AUTOINCREMENT UNIQUE,
	"weekday_name"	TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS "Schools" (
	"school_id"	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
	"school_name"	TEXT NOT NULL,
	"school_phone"	TEXT,
	"school_email"	TEXT
);
CREATE TABLE IF NOT EXISTS "Students_Weekdays" (
	"student_id"	INTEGER,
	"weekday_id"	INTEGER,
	FOREIGN KEY("student_id") REFERENCES "Students"("student_id"),
	FOREIGN KEY("weekday_id") REFERENCES "Weekdays"("weekday_id")
);
CREATE TABLE IF NOT EXISTS "Students_Subjects" (
	"student_id"	INTEGER,
	"subject_id"	INTEGER,
	FOREIGN KEY("subject_id") REFERENCES "Subjects"("subject_id"),
	FOREIGN KEY("student_id") REFERENCES "Students"("student_id")
);
CREATE TABLE IF NOT EXISTS "Guardians" (
	"guardian_id"	INTEGER NOT NULL DEFAULT 2000 PRIMARY KEY AUTOINCREMENT UNIQUE,
	"First_Name"	TEXT NOT NULL,
	"Last_Name"	TEXT NOT NULL,
	"Email"	TEXT,
	"Guardian_Type"	TEXT NOT NULL,
	"is_main_contact"	TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS "Students" (
	"student_id"	INTEGER NOT NULL DEFAULT 1000 PRIMARY KEY AUTOINCREMENT UNIQUE,
	"first_name"	TEXT NOT NULL,
	"last_name"	TEXT NOT NULL,
	"email"	TEXT,
	"grade_level"	INTEGER NOT NULL
);
CREATE TABLE IF NOT EXISTS "Subjects" (
	"subject_id"	INTEGER NOT NULL DEFAULT 100 PRIMARY KEY AUTOINCREMENT UNIQUE,
	"subject_name"	TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS "Family" (
	"student_id"	INTEGER,
	"guardian_id"	INTEGER,
	FOREIGN KEY("student_id") REFERENCES "Students"("student_id"),
	FOREIGN KEY("guardian_id") REFERENCES "Guardians"("guardian_id")
);
INSERT INTO "Guardians" VALUES (1,'John','Smith','js@gmail.com','father','no');
INSERT INTO "Guardians" VALUES (2,'Mary','Smith','ms@gmail.com','mother','yes');
INSERT INTO "Guardians" VALUES (3,'Karl','Marx','km@gmail.com','father','yes');
INSERT INTO "Guardians" VALUES (4,'Judith','Buttler','jb@gmail.com','mother','no');
INSERT INTO "Guardians" VALUES (5,'Friedrich','Engels','fe@gmail.com','father','no');
INSERT INTO "Guardians" VALUES (6,'Heleieth','Saffioti','hs@gmail.com','mother','yes');
INSERT INTO "Students" VALUES (1,'Peter','Smith','ps@gmail.com',3);
INSERT INTO "Students" VALUES (2,'Joana','Engels','je@gmail.com',6);
INSERT INTO "Students" VALUES (3,'Claire','Marx','cm@gmail.com',9);
INSERT INTO "Students" VALUES (4,'Nataly','Saffioti','ns@gmail.com',11);
INSERT INTO "Students" VALUES (6,'rafael','silva',NULL,0);
INSERT INTO "Family" VALUES (1,2);
INSERT INTO "Family" VALUES (1,1);
INSERT INTO "Family" VALUES (2,5);
INSERT INTO "Family" VALUES (3,3);
INSERT INTO "Family" VALUES (4,6);
COMMIT;
