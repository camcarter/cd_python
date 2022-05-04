-- Forward engineer the dojos_and_ninjas_schema from the previous chapter

-- Create a .txt file where you'll save each of your queries from below

-- Query: Create 3 new dojos
INSERT INTO dojos (name) VALUES('Burbank'),('San Jose'),('Online');

-- Query: Delete the 3 dojos you just created
DELETE FROM dojos WHERE id=1;

-- Query: Create 3 more dojos
INSERT INTO dojos (name) VALUES('Chicago'),('Seattle'),('Tulsa');

-- Query: Create 3 ninjas that belong to the first dojo
INSERT INTO ninjas (first_name, last_name, age, dojo_id)
VALUES ('Jenny', 'Sam',39, 14),('Marty', 'McCoder',29, 14),('Jesus', 'Montes',33, 14);

-- Query: Create 3 ninjas that belong to the second dojo
INSERT INTO table_name (column_name1, column_name2) 
VALUES('column1_value', 'column2_value');

-- Query: Create 3 ninjas that belong to the third dojo
INSERT INTO table_name (column_name1, column_name2) 
VALUES('column1_value', 'column2_value');

-- Query: Retrieve all the ninjas from the first dojo
SELECT * from ninjas WHERE dojo_id = 7;

-- Query: Retrieve all the ninjas from the last dojo
SELECT * from ninjas WHERE dojo_id = 9;

-- Query: Retrieve the last ninja's dojo
SELECT * from ninjas WHERE id = 9;

-- Submit your .txt file that contains all the queries you ran in the shell

