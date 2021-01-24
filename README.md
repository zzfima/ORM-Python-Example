# ORM-Python-Example

###After this tutorial you will be able to:
* Create Table in MySQL
* Add Data to MySQL Table
* Query table in Python in SQL manner
* Query table in Python in ORM manner

Pre-Requirements:
* Python installed
* MySQL Server installed

## Tutorial
1. Create MySql DB 'store'. In MySQL cmd: create database store
2. Set active MySql DB. In MySQL cmd: use store
3. Create a 'category' table :  
CREATE TABLE IF NOT EXISTS `category` (  
  `id` INT NOT NULL,  
  `name` VARCHAR(255) NULL,  
  PRIMARY KEY (`id`))  
ENGINE = InnoDB;  
4. Add data to 'category' table:  
INSERT INTO `category` (`id`, `name`) VALUES (1, 'Air Fresheners');  
INSERT INTO `category` (`id`, `name`) VALUES (2, 'Bath Products');  
INSERT INTO `category` (`id`, `name`) VALUES (3, 'Cakes');  
INSERT INTO `category` (`id`, `name`) VALUES (4, 'Candy');  
INSERT INTO `category` (`id`, `name`) VALUES (5, 'Dental Care');  
INSERT INTO `category` (`id`, `name`) VALUES (6, 'Health & Medicine');  
INSERT INTO `category` (`id`, `name`) VALUES (7, 'Juices');  
INSERT INTO `category` (`id`, `name`) VALUES (8, 'Snacks');  
INSERT INTO `category` (`id`, `name`) VALUES (9, 'Tea & Coffee');  
INSERT INTO `category` (`id`, `name`) VALUES (10, 'Water');  
INSERT INTO `category` (`id`, `name`) VALUES (11, 'Seasonings & Spices');  
INSERT INTO `category` (`id`, `name`) VALUES (12, 'Pasta & Noodles');  
INSERT INTO `category` (`id`, `name`) VALUES (13, 'Fruits & Vegetables');  
5. Commit all changes to MySQL DB 'store'. In MySQL cmd: COMMIT
6. Try python code.  
First part of code do query: 'SELECT * FROM category' in SQL manner.  
Second part of code do query: 'SELECT * FROM category' in ORM manner.   