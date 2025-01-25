-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema inventory
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS `inventory` ;

-- -----------------------------------------------------
-- Schema inventory
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `inventory` DEFAULT CHARACTER SET utf8 ;
USE `inventory` ;

-- -----------------------------------------------------
-- Table `inventory`.`User`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `inventory`.`User` ;

CREATE TABLE IF NOT EXISTS `inventory`.`User` (
  `Id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `Username` VARCHAR(20) NOT NULL,
  `Password` VARCHAR(100) NOT NULL,
  `CompanyName` VARCHAR(50) NOT NULL,
  PRIMARY KEY (`Id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `inventory`.`Category`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `inventory`.`Category` ;

CREATE TABLE IF NOT EXISTS `inventory`.`Category` (
  `Id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `Name` VARCHAR(50) NOT NULL,
  `Abbr` VARCHAR(10) NOT NULL,
  PRIMARY KEY (`Id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `inventory`.`Item`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `inventory`.`Item` ;

CREATE TABLE IF NOT EXISTS `inventory`.`Item` (
  `Id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `ItemId` VARCHAR(10) NOT NULL,
  `Name` VARCHAR(50) NOT NULL,
  `Quantity` FLOAT NOT NULL,
  `Price` FLOAT NOT NULL,
  `IsWeight` TINYINT NOT NULL DEFAULT 0,
  `IsPerItem` TINYINT NOT NULL DEFAULT 1,
  `UserId` INT UNSIGNED NOT NULL,
  `CategoryId` INT UNSIGNED NOT NULL,
  PRIMARY KEY (`Id`),
  INDEX `item_user_fk1_idx` (`UserId` ASC) VISIBLE,
  INDEX `item_category_fk2_idx` (`CategoryId` ASC) VISIBLE,
  CONSTRAINT `item_user_fk1`
    FOREIGN KEY (`UserId`)
    REFERENCES `inventory`.`User` (`Id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `item_category_fk2`
    FOREIGN KEY (`CategoryId`)
    REFERENCES `inventory`.`Category` (`Id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;


USE inventory;

INSERT INTO Category(Name, Abbr)
VALUES
    ('Grocery and Food','GRF')
,   ('Household Essentials', 'HHE')
,   ('Health and Wellness', 'HLW')
,   ('Electronics', 'ELE')
,   ('Apparel and Accessories', 'APP')
,   ('Home Goods and Furniture', 'HOM')
,   ('Toys and Entertainment', 'TOY')
,   ('Sporting Goods and Outdoor Equipment', 'SPO')
,   ('Automotive and Hardware', 'AUT')
,   ('Pharmacy and Wellness Services', 'PHA')
,   ('Seasonal and Holiday Items', 'SEA')
,   ('Miscellaneous', 'MISC');

INSERT INTO User(Username, Password, CompanyName)
VALUES
    ('walmart','iamwalmart123','Walmart Incorporated')
,   ('costco','iamcostco007','Costco Wholesale Corporation');

INSERT INTO Item(Name,ItemId ,IsWeight, IsPerItem,Quantity, Price, UserId, CategoryId)
VALUES
('Grapes', 'GRP001', 1, 0, 50.0, 2.52, (SELECT Id FROM User WHERE Username = 'walmart'), (SELECT Id FROM Category WHERE Abbr = 'GRF')),
    ('Freezer', 'FRZ001', 0, 1, 100.0, 1325.50, (SELECT Id FROM User WHERE Username = 'costco'), (SELECT Id FROM Category WHERE Abbr = 'ELE')),
    ('Bananas', 'BNN001', 1, 0, 200.0, 1.15, (SELECT Id FROM User WHERE Username = 'walmart'), (SELECT Id FROM Category WHERE Abbr = 'GRF')),
    ('Microwave', 'MWV123', 0, 1, 30.0, 250.75, (SELECT Id FROM User WHERE Username = 'costco'), (SELECT Id FROM Category WHERE Abbr = 'ELE')),
    ('Milk', 'MLK002', 1, 0, 500.0, 3.75, (SELECT Id FROM User WHERE Username = 'walmart'), (SELECT Id FROM Category WHERE Abbr = 'GRF')),
    ('Television', 'TV001', 0, 1, 25.0, 500.00, (SELECT Id FROM User WHERE Username = 'costco'), (SELECT Id FROM Category WHERE Abbr = 'ELE')),
    ('Laptop', 'LPT001', 0, 1, 15.0, 1200.99, (SELECT Id FROM User WHERE Username = 'walmart'), (SELECT Id FROM Category WHERE Abbr = 'ELE')),
    ('Bread', 'BRD001', 1, 0, 100.0, 1.25, (SELECT Id FROM User WHERE Username = 'walmart'), (SELECT Id FROM Category WHERE Abbr = 'GRF')),
    ('Chair', 'CHR001', 0, 1, 60.0, 45.00, (SELECT Id FROM User WHERE Username = 'costco'), (SELECT Id FROM Category WHERE Abbr = 'HOM')),
    ('Toaster', 'TST001', 0, 1, 40.0, 30.50, (SELECT Id FROM User WHERE Username = 'walmart'), (SELECT Id FROM Category WHERE Abbr = 'ELE')),
    ('Basketball', 'BKB001', 0, 1, 70.0, 25.00, (SELECT Id FROM User WHERE Username = 'costco'), (SELECT Id FROM Category WHERE Abbr = 'SPO')),
    ('Jacket', 'JCK001', 0, 1, 80.0, 75.99, (SELECT Id FROM User WHERE Username = 'walmart'), (SELECT Id FROM Category WHERE Abbr = 'APP')),
    ('Shampoo', 'SHP001', 1, 0, 120.0, 5.50, (SELECT Id FROM User WHERE Username = 'costco'), (SELECT Id FROM Category WHERE Abbr = 'HLW')),
    ('Holiday Lights', 'HLT001', 0, 1, 200.0, 12.99, (SELECT Id FROM User WHERE Username = 'walmart'), (SELECT Id FROM Category WHERE Abbr = 'SEA')),
    ('Car Oil', 'CAR001', 0, 1, 100.0, 15.75, (SELECT Id FROM User WHERE Username = 'costco'), (SELECT Id FROM Category WHERE Abbr = 'AUT'));