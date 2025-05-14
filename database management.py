-- Create Categories Table
CREATE TABLE Categories (
    category_id INT AUTO_INCREMENT PRIMARY KEY,
    category_name VARCHAR(100) NOT NULL,
    description TEXT
);

-- Create Suppliers Table
CREATE TABLE Suppliers (
    supplier_id INT AUTO_INCREMENT PRIMARY KEY,
    supplier_name VARCHAR(100) NOT NULL,
    contact_email VARCHAR(100),
    contact_phone VARCHAR(15)
);

-- Create Products Table
CREATE TABLE Products (
    product_id INT AUTO_INCREMENT PRIMARY KEY,
    product_name VARCHAR(100) NOT NULL,
    category_id INT,
    price DECIMAL(10, 2) NOT NULL,
    supplier_id INT,
    stock_quantity INT NOT NULL,
    FOREIGN KEY (category_id) REFERENCES Categories(category_id),
    FOREIGN KEY (supplier_id) REFERENCES Suppliers(supplier_id)
);

-- Create Inventory Table
CREATE TABLE Inventory (
    inventory_id INT AUTO_INCREMENT PRIMARY KEY,
    product_id INT,
    quantity_received INT NOT NULL,
    received_date DATE NOT NULL,
    FOREIGN KEY (product_id) REFERENCES Products(product_id)
);

-- Insert Sample Data into Categories Table
INSERT INTO Categories (category_name, description)
VALUES 
('Electronics', 'Devices such as phones, laptops, and accessories'),
('Furniture', 'Chairs, tables, and other office furniture'),
('Stationery', 'Office supplies like paper, pens, and notebooks');

-- Insert Sample Data into Suppliers Table
INSERT INTO Suppliers (supplier_name, contact_email, contact_phone)
VALUES 
('Tech Supplies Co.', 'contact@techsupplies.com', '123-456-7890'),
('Furniture World', 'info@furnitureworld.com', '987-654-3210'),
('Stationery Hub', 'support@stationeryhub.com', '555-123-4567');

-- Insert Sample Data into Products Table
INSERT INTO Products (product_name, category_id, price, supplier_id, stock_quantity)
VALUES 
('Laptop', 1, 799.99, 1, 50),
('Office Chair', 2, 120.00, 2, 100),
('Pen', 3, 1.50, 3, 500),
('Smartphone', 1, 699.00, 1, 30);

-- Insert Sample Data into Inventory Table
INSERT INTO Inventory (product_id, quantity_received, received_date)
VALUES 
(1, 30, '2025-04-01'),
(2, 100, '2025-04-03'),
(3, 500, '2025-04-05'),
(4, 20, '2025-04-07');
