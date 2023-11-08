CREATE TABLE COFFEESHOP (
    ShopID INT PRIMARY KEY,
    ShopName VARCHAR(255),
    Location VARCHAR(255),
    Rating FLOAT,
    ManagerID INT
);

CREATE TABLE SUPPLIER (
    SupplierID INT PRIMARY KEY,
    SupplierName VARCHAR(255),
    SupplierLocation VARCHAR(255)
);

CREATE TABLE ITEM_CATEGORY (
    ItemCategory VARCHAR(255) PRIMARY KEY
);

-- Create the tables that reference the base tables
CREATE TABLE CONTRACT (
    ContractID INT PRIMARY KEY,
    SupplierID INT,
    ShopID INT
);

CREATE TABLE MENU_ITEM (
    ItemID INT PRIMARY KEY,
    ItemPrice DECIMAL(10, 2),
    ItemCategory VARCHAR(255)
);

CREATE TABLE EMPLOYEE (
    EmployeeID INT PRIMARY KEY,
    EmployeeName VARCHAR(255),
    ShopID INT,
    ManagerID INT
);

INSERT INTO COFFEESHOP (ManagerID)
VALUES
    (4001),
    (4002),
    (4003),
    (4004),
    (4005),
    (4006),
    (4007);

INSERT INTO EMPLOYEE (EmployeeID, EmployeeName, ShopID, ManagerID)
VALUES
    (4001, 'Chris Brown', 1001, 4001),
    (4002, 'John Frank', 1002, 4002),
    (4003, 'Fred Red', 1003, 4003),
    (4004, 'Bo Green', 1004, 4004),
    (4005, 'Mark Smart', 1005, 4005),
    (4006, 'Reed Free', 1006, 4006),
    (4007, 'Joe Bro', 1007, 4007);