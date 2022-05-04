INSERT INTO dojos (name) VALUES('Burbank'),('San Jose'),('Online');
INSERT INTO dojos (name) VALUES('Chicago'),('Seattle'),('Tulsa');

DELETE FROM dojos WHERE id=6;

-- Query: Create 3 ninjas that belong to the first dojo
INSERT INTO ninjas (first_name, last_name, age, dojo_id)
VALUES ('Jenny', 'Sam',39, 7),('Marty', 'McCoder',29, 7),('Jesus', 'Montes',33, 7);

-- Query: Create 3 ninjas that belong to the first dojo
INSERT INTO ninjas (first_name, last_name, age, dojo_id)
VALUES ('Jenny', 'Sam',39, 8),('Marty', 'McCoder',29, 8),('Jesus', 'Montes',33, 8);

-- Query: Create 3 ninjas that belong to the first dojo
INSERT INTO ninjas (first_name, last_name, age, dojo_id)
VALUES ('Jenny', 'Sam',39, 9),('Marty', 'McCoder',29, 9),('Jesus', 'Montes',33, 9);

SELECT * from ninjas;

-- Query: Retrieve all the ninjas from the first dojo
SELECT * from ninjas WHERE dojo_id = 7;
SELECT * from ninjas WHERE dojo_id = 9;
SELECT * from dojos WHERE id = 9;dojos