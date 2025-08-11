-- PostgreSQL CREATE TABLE Statements

-- Tabla para la autenticación de usuarios y tipo de rol
CREATE TABLE IF NOT EXISTS users(
user_id UUID PRIMARY KEY,
username VARCHAR(75) UNIQUE NOT NULL,
email VARCHAR(100) UNIQUE NOT NULL,
password VARCHAR(200) NOT NULL,
is_admin BOOLEAN NOT NULL DEFAULT FALSE
)

-- Tabla para la información personal de los usuarios
CREATE TABLE IF NOT EXISTS profiles (
user_id UUID PRIMARY KEY REFERENCES users(user_id) ON DELETE CASCADE,
first_name VARCHAR(100) NOT NULL,
last_name VARCHAR(100) NOT NULL,
city VARCHAR(100) NOT NULL,
state VARCHAR(100) NOT NULL,
country VARCHAR(100) NOT NULL,
zip_code VARCHAR(15) NOT NULL,
gender VARCHAR(20) DEFAULT 'Not especified',
phone_number VARCHAR(20)
)

-- Tabla para la información de los productos
CREATE TABLE IF NOT EXISTS products (
product_id UUID PRIMARY KEY,
name VARCHAR(250) NOT NULL,
description TEXT NOT NULL,
unit_price NUMERIC(10, 2) NOT NULL
)

-- Tabla para el stock actual de cada producto (para performance)
CREATE TABLE IF NOT EXISTS products_inventory (
product_id UUID PRIMARY KEY REFERENCES products(product_id) ON DELETE CASCADE,
stock INT NOT NULL CHECK (stock >= 0)
);

-- -------------------------------------------------------------
-- Tablas de búsqueda para un diseño más flexible y escalable
-- -------------------------------------------------------------

-- Tabla de búsqueda para los estados de las órdenes
CREATE TABLE IF NOT EXISTS order_statuses (
status_id UUID PRIMARY KEY,
status_name VARCHAR(50) UNIQUE NOT NULL
);

-- Tabla de búsqueda para los métodos de pago
CREATE TABLE IF NOT EXISTS payment_methods (
method_id UUID PRIMARY KEY,
method_name VARCHAR(50) UNIQUE NOT NULL
)

-- Tabla de búsqueda para los estados de los pagos
CREATE TABLE IF NOT EXISTS payment_statuses (
status_id UUID PRIMARY KEY,
status_name VARCHAR(50) UNIQUE NOT NULL
)

-- Tabla de búsqueda para los tipos de movimientos de inventario
CREATE TABLE IF NOT EXISTS inventory_movement_types (
type_id UUID PRIMARY KEY,
type_name VARCHAR(50) UNIQUE NOT NULL
)

-- Tabla para las categorías de productos
CREATE TABLE IF NOT EXISTS categories (
category_id UUID PRIMARY KEY,
name VARCHAR(100) UNIQUE NOT NULL
)

-- -------------------------------------------------------------
-- Tablas principales, actualizadas con las nuevas claves foráneas
-- -------------------------------------------------------------

-- Tabla para los encabezados de las órdenes
CREATE TABLE IF NOT EXISTS orders (
order_id UUID PRIMARY KEY,
user_id UUID NOT NULL REFERENCES users(user_id) ON DELETE RESTRICT,
status_id UUID NOT NULL REFERENCES order_statuses(status_id) ON DELETE RESTRICT,
total_cost NUMERIC(10, 2) NOT NULL,
created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- Tabla para los detalles de los productos en cada orden
CREATE TABLE IF NOT EXISTS order_items (
order_id UUID NOT NULL REFERENCES orders(order_id) ON DELETE CASCADE,
product_id UUID NOT NULL REFERENCES products(product_id) ON DELETE RESTRICT,
quantity INT NOT NULL CHECK (quantity > 0),
price_at_purchase NUMERIC(10, 2) NOT NULL,
PRIMARY KEY (order_id, product_id)
);

-- Tabla para los pagos de las órdenes
CREATE TABLE IF NOT EXISTS payments (
payment_id UUID PRIMARY KEY,
order_id UUID UNIQUE NOT NULL REFERENCES orders(order_id) ON DELETE RESTRICT,
amount NUMERIC(10, 2) NOT NULL,
payment_method_id UUID NOT NULL REFERENCES payment_methods(method_id) ON DELETE RESTRICT,
status_id UUID NOT NULL REFERENCES payment_statuses(status_id) ON DELETE RESTRICT,
created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- Tabla para los carritos de compra de los usuarios
CREATE TABLE IF NOT EXISTS shopping_carts (
cart_id UUID PRIMARY KEY,
user_id UUID UNIQUE NOT NULL REFERENCES users(user_id) ON DELETE CASCADE,
created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- Tabla de unión para los productos en cada carrito
CREATE TABLE IF NOT EXISTS cart_items (
cart_id UUID NOT NULL REFERENCES shopping_carts(cart_id) ON DELETE CASCADE,
product_id UUID NOT NULL REFERENCES products(product_id) ON DELETE CASCADE,
quantity INT NOT NULL CHECK (quantity > 0),
PRIMARY KEY (cart_id, product_id)
);

-- Tabla de unión para productos y categorías (Many to Many)
CREATE TABLE IF NOT EXISTS product_categories (
product_id UUID NOT NULL REFERENCES products(product_id) ON DELETE CASCADE,
category_id UUID NOT NULL REFERENCES categories(category_id) ON DELETE CASCADE,
PRIMARY KEY (product_id, category_id)
);

-- Tabla para el historial de movimientos de inventario (auditoría)
CREATE TABLE IF NOT EXISTS inventory_movements (
movement_id UUID PRIMARY KEY,
product_id UUID NOT NULL REFERENCES products(product_id) ON DELETE RESTRICT,
movement_type_id UUID NOT NULL REFERENCES inventory_movement_types(type_id) ON DELETE RESTRICT,
quantity_change INT NOT NULL,
reference_id VARCHAR(255),
movement_date TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- -------------------------------------------------------------
-- INSERT Statements
-- -------------------------------------------------------------

-- Sample User
INSERT INTO users (user_id, username, email, password, is_admin) VALUES
('b370a256-4b9e-4b2a-a9e9-d757d54402b1', 'admin', 'admin@example.com', '123456789', TRUE);

-- Sample User Profile
-- INSERT INTO profiles (user_id, first_name, last_name, city, state, country, zip_code) VALUES
-- ('b370a256-4b9e-4b2a-a9e9-d757d54402b1', 'John', 'Doe', 'Springfield', 'IL', 'USA', '62704');

-- ------------------------------
-- Laptops (20 products)
-- ------------------------------
INSERT INTO products (product_id, name, description, unit_price) VALUES
('b30a1c8f-28c0-43f5-a8e9-d757d54402a1', 'MacBook Pro 14', 'High-performance laptop with M3 Pro chip, 18GB RAM, and 512GB SSD.', 2199.99),
('f6b8e3d0-37e4-4a4b-8a71-6c7c2514539e', 'Dell XPS 15', 'Premium laptop with OLED display, Intel Core i9, 32GB RAM, and 1TB SSD.', 2599.99),
('d4f5c9b2-9a0e-4e6f-8d2b-5e6f8d2b5e6f', 'HP Envy x360', '2-in-1 laptop with AMD Ryzen 7 processor, 15.6" touchscreen, and 16GB RAM.', 999.50),
('a2c7e0f8-1d4a-4e2b-9c6d-3f5c7b9e1a4d', 'Lenovo Yoga Slim 7', 'Ultra-thin laptop with Intel Core i7 processor, 16GB RAM, and aluminum design.', 1150.00),
('3e9a7c0d-b4e1-4c5d-8f2a-6b4e1c5d8f2a', 'ASUS ROG Strix G16', 'Gaming laptop with Intel Core i9, NVIDIA RTX 4080, and a 16" 240Hz display.', 2300.00),
('f1d2c3e4-5f6a-7b8c-9d0e-1f2a3c4d5e6f', 'Acer Nitro 5', 'Entry-level gaming laptop with AMD Ryzen 5, NVIDIA GTX 1650, and 8GB RAM.', 799.00),
('7b3c2d4e-5f1a-6d8c-9e2b-3f4a5c6d7e8f', 'Microsoft Surface Laptop Studio', 'Creators laptop with dynamic touchscreen, Intel Core i7, and RTX 3050 Ti GPU.', 1899.00),
('9d5e6f7c-8a1b-4d9e-c2f8-a1b9e2d3f4a5', 'Gigabyte Aero 16 OLED', 'Content creator laptop with 4K OLED display, Intel Core i7, and RTX 4070 GPU.', 1999.00),
('2a4b6c8d-0e1f-2a3b-4c5d-6e7f8a9b0c1d', 'Razer Blade 14', 'Ultra-compact gaming laptop with AMD Ryzen 9 CPU and NVIDIA RTX 4070.', 2499.00),
('5d8a9b0c-1e2f-3a4b-5c6d-7e8f9a0b1c2d', 'MSI Prestige 14 Evo', 'Business laptop with Intel Core i7, 16GB RAM, and a lightweight design.', 1050.00),
('e9b2c4f1-3d5a-6b8e-7c9d-8a1e2f3d4c5b', 'ASUS Zenbook Duo', 'Laptop with dual OLED touchscreens for maximum productivity.', 2599.00),
('4f1a5e9b-2c3d-6e7f-8a9b-0c1d2e3f4a5b', 'LG Gram 16', 'Ultra-light 16-inch laptop with Intel Core i5 and 16GB RAM.', 1399.00),
('b8d9c0e1-f2a3-4b5c-6d7e-8f9a0b1c2d3e', 'Dell Alienware m16', 'High-performance gaming laptop with Intel Core i9 and NVIDIA RTX 4090.', 3499.00),
('6c7c2514-539e-4a4b-8a71-f6b8e3d037e4', 'Acer Predator Helios 18', '18" gaming laptop with Intel Core i9, NVIDIA RTX 4080, and a Mini LED display.', 2999.00),
('3a4b5c6d-7e8f-9a0b-1c2d-3e4f5a6b7c8d', 'Lenovo Legion Pro 7i', 'Gaming laptop with Intel Core i9, NVIDIA RTX 4080, and advanced cooling system.', 2899.00),
('1b9e2d3f-4a5c-7d8e-8a1b-9e2d3f4a5c7d', 'Gigabyte AORUS 17H', 'Gaming laptop with Intel Core i7, NVIDIA RTX 4070, and a 17.3" 300Hz display.', 1799.00),
('9a0b1c2d-3e4f-5a6b-7c8d-9e0f1a2b3c4d', 'MSI GF63 Thin', 'Thin and affordable gaming laptop with Intel Core i5 and NVIDIA GTX 4050.', 849.00),
('5c6d7e8f-9a0b-1c2d-3e4f-5a6b7c8d9e0f', 'ASUS TUF Gaming A15', 'Durable gaming laptop with AMD Ryzen 7, NVIDIA RTX 4060, and 16GB RAM.', 1299.00),
('2d3f4a5c-6d7e-8f9a-0b1c-2d3e4f5a6b7c', 'HP Victus 16', 'Gaming laptop with Intel Core i7, NVIDIA RTX 4060, and a 16.1" display.', 1199.00),
('8a1b9e2d-3f4a-5c6d-7e8f-9a0b1c2d3e4f', 'Dell G15', 'Gaming laptop with Intel Core i7 and NVIDIA RTX 4060, a popular model.', 1199.00);

-- ------------------------------
-- Processors (15 products)
-- ------------------------------
INSERT INTO products (product_id, name, description, unit_price) VALUES
('8e7a6d5c-4b3c-2a1d-0f9e-8d7c6b5a4f3e', 'Intel Core i9-14900K', 'High-end desktop processor with 24 cores and 32 threads.', 599.00),
('c7a8d9e0-f1b2-3c4d-5e6f-7a8b9c0d1e2f', 'AMD Ryzen 9 7950X3D', 'Processor for gaming and productivity with 16 cores and 3D V-Cache technology.', 659.00),
('a1b2c3d4-e5f6-7a8b-9c0d-e1f2a3b4c5d6', 'Intel Core i7-14700K', 'High-end processor with 20 cores and excellent performance.', 429.00),
('d5e6f7a8-b9c0-d1e2-f3a4-b5c6d7e8f9a0', 'AMD Ryzen 7 7800X3D', 'The fastest gaming processor in the world with 3D V-Cache technology.', 369.00),
('2b3c4d5e-6f7a-8b9c-0d1e-2f3a4b5c6d7e', 'Intel Core i5-14600K', 'Mid-to-high-end processor with 14 cores, ideal for gaming and demanding tasks.', 319.00),
('8c9d0e1f-2a3b-4c5d-6e7f-8a9b0c1d2e3f', 'AMD Ryzen 5 7600X', 'Mid-range processor with 6 cores, ideal for 1080p and 1440p gaming.', 229.00),
('e4f5a6b7-c8d9-0e1f-2a3b-4c5d6e7f8a9b', 'Intel Core i3-14100', 'Entry-level processor with 4 cores, perfect for office or budget PCs.', 129.00),
('1f2a3b4c-5d6e-7f8a-9b0c-d1e2f3a4b5c6', 'AMD Ryzen 5 5600X', 'Older generation processor, popular for mid-range gaming PCs.', 159.00),
('9b0c1d2e-3f4a-5b6c-7d8e-9f0a1b2c3d4e', 'Intel Core i9-13900K', 'High-end processor from the previous generation, still with excellent performance.', 549.00),
('4d5e6f7a-8b9c-0d1e-2f3a-4b5c6d7e8f9a', 'AMD Ryzen 7 5700X', '8-core processor for gaming and multitasking, great value.', 179.00),
('e2f3a4b5-c6d7-e8f9-a0b1-c2d3e4f5a6b7', 'Intel Core i5-13600K', 'Popular mid-range processor for gaming.', 279.00),
('1c2d3e4f-5a6b-7c8d-9e0f-a1b2c3d4e5f6', 'AMD Ryzen 3 4100', 'Very affordable entry-level processor.', 69.00),
('7f8a9b0c-1d2e-3f4a-5b6c-7d8e9f0a1b2c', 'Intel Core i5-12400', '12th generation mid-range processor, with great performance for its price.', 179.00),
('3a4b5c6d-7e8f-9a0b-1c2d-3e4f5a6b7c8f', 'AMD Ryzen 9 5900X', '12-core processor from the 5000 series, ideal for productivity.', 309.00),
('f2a3b4c5-d6e7-f8a9-b0c1-d2e3f4a5b6c7', 'Intel Pentium Gold G6400', 'Low-power processor for basic tasks and office work.', 79.00);

-- ------------------------------
-- Graphics Cards (15 products)
-- ------------------------------
INSERT INTO products (product_id, name, description, unit_price) VALUES
('6b4e1c5d-8f2a-3e9a-7c0d-b4e1c5d8f2a6', 'NVIDIA GeForce RTX 4090', 'High-end GPU with 24GB of VRAM, ideal for 4K gaming and AI.', 1699.00),
('9d5e6f7c-8a1b-4d9e-c2f8-a1b9e2d3f4a6', 'AMD Radeon RX 7900 XTX', 'Enthusiast GPU with 24GB of GDDR6 VRAM, competes in the high-end segment.', 999.00),
('1a2b3c4d-5e6f-7a8b-9c0d-e1f2a3b4c5d7', 'NVIDIA GeForce RTX 4070 Ti', 'High-performance GPU for 1440p gaming with 12GB of VRAM.', 799.00),
('4e5f6a7b-8c9d-0e1f-2a3b-4c5d6e7f8a9c', 'AMD Radeon RX 7800 XT', 'Mid-to-high-end GPU with 16GB of VRAM, ideal for 1440p gaming.', 499.00),
('8c9d0e1f-2a3b-4c5d-6e7f-8a9b0c1d2e3d', 'NVIDIA GeForce RTX 4060', 'Mid-range GPU for 1080p gaming with 8GB of VRAM.', 329.00),
('e1f2a3b4-c5d6-e7f8-a9b0-c1d2e3f4a5b8', 'NVIDIA GeForce RTX 3060 Ti', 'Previous generation GPU, still very popular for 1440p gaming.', 399.00),
('f4e3d2c1-b0a9-8f7e-6d5c-4b3a2c1b0a9d', 'Intel Arc A770', 'Intel enthusiast GPU with 16GB of VRAM, offers excellent performance in its range.', 349.00),
('5b6c7d8e-9f0a-1b2c-3d4e-5f6a7b8c9d0e', 'ASUS TUF Gaming RTX 4080', 'Custom variant of the RTX 4080 with a robust cooling design.', 1299.00),
('6f7a8b9c-0d1e-2f3a-4b5c-6d7e8f9a0b1f', 'MSI VENTUS 3X RTX 4070 SUPER', 'Model of the RTX 4070 SUPER with three fans, excellent for heat dissipation.', 649.00),
('7c8d9e0f-1a2b-3c4d-5e6f-7a8b9c0d1e2f', 'PowerColor Hellhound RX 7900 XT', 'Model of the RX 7900 XT with triple-fan cooling.', 799.00)

INSERT INTO products (product_id, name, description, unit_price) VALUES
('e2f3a4b5-c6d7-e8f9-a0b1-c2d3e4f5a6b8', 'PNY GeForce GTX 1660 SUPER', 'Past generation GPU, ideal for entry-level 1080p gaming.', 189.00),
('2c3d4e5f-6a7b-8c9d-0e1f-2a3b4c5d6e7f', 'EVGA GeForce RTX 3080', '30 series GPU, still very powerful for 4K and ray tracing.', 699.00)
('8c9d0e1f-2a3b-4c5d-6e7f-8a9b0c1d2e3g', 'Zotac GAMING RTX 4070', 'Compact GPU, ideal for Mini-ITX cases.', 549.00),
('1b2c3d4e-5f6a-7b8c-9d0e-1f2a3b4c5d6g', 'Gigabyte Eagle RTX 4060 Ti', 'Variant of the RTX 4060 Ti with a clean design and solid performance.', 449.00)
('4d5e6f7a-8b9c-0d1e-2f3a-4b5c6d7e8f9g', 'ASRock Challenger Pro RX 7700 XT', 'Mid-range GPU with 12GB of VRAM and good 1440p performance.', 429.00),
-- ------------------------------
-- Peripherals (15 products)
-- ------------------------------
INSERT INTO products (product_id, name, description, unit_price) VALUES
('2e3f4a5b-6c7d-8e9f-0a1b-2c3d4e5f6a7b', 'Elgato Stream Deck +', 'Controller with 8 LCD buttons, 4 rotary dials, and a touchscreen.', 199.99),
('d5e6f7a8-b9c0-d1e2-f3a4-b5c6d7e8f9a1', 'HyperX QuadCast S', 'USB microphone for gaming and streaming with RGB lighting and 4 polar patterns.', 159.99),
('e4f5a6b7-c8d9-0e1f-2a3b-4c5d6e7f8a9d', 'SteelSeries QcK Heavy XXL', 'Extra large and thick gaming mousepad, optimized for optical and laser mouse sensors.', 39.99),
('6e7f8a9b-0c1d-2e3f-4a5b-6c7d8e9f0a1c', 'Elgato Facecam Pro', 'Professional 4K60 webcam, ideal for high-quality content creators and streaming.', 299.99),
('1c2d3e4f-5a6b-7c8d-9e0f-a1b2c3d4e5f7', 'Audio-Technica ATH-M50xBT2', 'Bluetooth studio headphones with great sound quality.', 199.00),
('4a5b6c7d-8e9f-0a1b-2c3d-4e5f6a7b8c9d', 'GMMK Pro 75% Keyboard', 'Customizable mechanical keyboard kit with 75% layout.', 169.99),
('a1b2c3d4-e5f6-7a8b-9c0d-e1f2a3b4c5d9', 'Logitech G915 TKL', 'Wireless mechanical keyboard with low-profile switches and a tenkeyless design.', 229.00);

-- ------------------------------
-- Components (20 products)
-- ------------------------------
-- RAM (5 products)
INSERT INTO products (product_id, name, description, unit_price) VALUES
('b9e0f1a2-c3d4-e5f6-a7b8-c9d0e1f2a3b1', 'Corsair Vengeance RGB Pro 32GB', 'DDR4 RAM kit (2x16GB) at 3600MHz with RGB lighting.', 109.99),
('8c7d6e5f-4a3b-2c1d-0e9f-8a7b6c5d4e3f', 'G.Skill Trident Z5 RGB 32GB', 'DDR5 RAM kit (2x16GB) at 6000MHz with low latency.', 159.99),
('4d5e6f7a-8b9c-0d1e-2f3a-4b5c6d7e8f9b', 'Crucial Ballistix 16GB', 'DDR4 RAM kit (2x8GB) at 3200MHz, ideal for gaming.', 69.99),
('1f2a3b4c-5d6e-7f8a-9b0c-d1e2f3a4b5c7', 'Kingston FURY Beast 32GB', 'DDR5 RAM kit (2x16GB) at 5200MHz with a low-profile design.', 129.99),
('f9a0b1c2-d3e4-f5a6-b7c8-d9e0f1a2b3c4', 'Team T-Force Delta RGB 16GB', 'DDR4 RAM kit (2x8GB) at 3200MHz with diffused RGB lighting.', 59.99);

-- SSD (5 products)
INSERT INTO products (product_id, name, description, unit_price) VALUES
('e1d2c3f4-5a6b-7c8d-9e0f-a1b2c3d4e5f1', 'Samsung 990 Pro 2TB', 'High-speed 2TB M.2 NVMe SSD for exceptional performance.', 189.99),
('f2a3c4d5-e6b7-f8a9-b0c1-d2e3f4a5b6c8', 'Western Digital Black SN850X 1TB', 'High-performance 1TB M.2 NVMe SSD for gaming.', 129.99),
('d4e5f6a7-b8c9-0d1e-2f3a-4b5c6d7e8f9e', 'Crucial P3 Plus 4TB', '4TB M.2 NVMe SSD, ideal for large amounts of data.', 299.99),
('a1b2c3d4-e5f6-7a8b-9c0d-e1f2a3b4c5f9', 'Seagate FireCuda 530 1TB', 'M.2 NVMe SSD with read speeds up to 7300 MB/s.', 149.99),
('e9b2c4f1-3d5a-6b8e-7c9d-8a1e2f3d4c5c', 'SK Hynix P41 Platinum 2TB', 'M.2 NVMe SSD with excellent performance and energy efficiency.', 179.99);

-- HDD (5 products)
INSERT INTO products (product_id, name, description, unit_price) VALUES
('b30a1c8f-28c0-43f5-a8e9-d757d54402a2', 'Seagate BarraCuda 4TB', 'Internal 3.5-inch hard drive, 5400RPM, for mass storage.', 89.99),
('d4e5f6a7-b8c9-0d1e-2f3a-4b5c6d7e8f9a', 'Western Digital Blue 1TB', 'Reliable internal 3.5-inch hard drive, 7200RPM, for desktop PCs.', 49.99),
('7b3c2d4e-5f1a-6d8c-9e2b-3f4a5c6d7e8a', 'Seagate IronWolf 8TB', '3.5-inch NAS hard drive, optimized for NAS systems.', 199.99),
('9d5e6f7c-8a1b-4d9e-c2f8-a1b9e2d3f4a7', 'Western Digital Ultrastar 12TB', 'Enterprise-grade hard drive for data centers and high-capacity storage.', 299.99);

-- NVMe M.2 (5 products)
INSERT INTO products (product_id, name, description, unit_price) VALUES
('e4f5a6b7-c8d9-0e1f-2a3b-4c5d6e7f8a9e', 'Crucial P5 Plus 2TB', '2TB NVMe M.2 SSD with read speeds up to 6600 MB/s.', 149.99),
('1f2a3b4c-5d6e-7f8a-9b0c-d1e2f3a4b5c8', 'Western Digital SN770 1TB', '1TB NVMe M.2 SSD for gaming, ideal for PCs and laptops.', 69.99),
('9d0e1f2a-3b4c-5d6e-7f8a-9b0c1d2e3f4f', 'Gigabyte AORUS Gen4 7000s 2TB', '2TB PCIe 4.0 NVMe M.2 SSD with thermal heatsink.', 199.99),
('f6b8e3d0-37e4-4a4b-8a71-6c7c2514539f', 'Corsair MP600 Pro LPX 1TB', '1TB NVMe M.2 SSD optimized for PlayStation 5 and PC.', 79.99);


-- -------------------------------------------------------------
-- Data for lookup tables
-- -------------------------------------------------------------

-- Order statuses
INSERT INTO order_statuses (status_id, status_name) VALUES
('1f2b3a4c-5d6e-4f7a-8b9c-d0e1f2a3b4c5', 'Processing'),
('2d3e4f5a-6b7c-4d8e-9f0a-b1c2d3e4f5a6', 'Shipped'),
('3c4d5e6f-7a8b-4c9d-a0b1-c2d3e4f5a6b7', 'Delivered'),
('4e5f6a7b-8c9d-4e1f-2a3b-4c5d6e7f8a9b', 'Canceled');

-- Payment methods
INSERT INTO payment_methods (method_id, method_name) VALUES
('b1a2c3d4-e5f6-4a7b-8c9d-0e1f2a3b4c5d', 'Credit Card'),
('e2f3a4b5-c6d7-4e8f-9a0b-1c2d3e4f5a6b', 'PayPal'),
('f3a4b5c6-d7e8-4f9a-0b1c-2d3e4f5a6b7c', 'Bank Transfer');

-- Payment statuses
INSERT INTO payment_statuses (status_id, status_name) VALUES
('a0b1c2d3-e4f5-4a6b-7c8d-9e0f1a2b3c4d', 'Pending'),
('b1c2d3e4-f5a6-4b7c-8d9e-0f1a2b3c4d5e', 'Completed'),
('c2d3e4f5-a6b7-4c8d-9e0f-1a2b3c4d5e6f', 'Failed');

-- Inventory movement types
INSERT INTO inventory_movement_types (type_id, type_name) VALUES
('d0e1f2a3-b4c5-4d6e-7f8a-9b0c1d2e3f4a', 'Sale'),
('e1f2a3b4-c5d6-4e7f-8a9b-0c1d2e3f4a5b', 'Restock'),
('f2a3b4c5-d6e7-4f8a-9b0c-1d2e3f4a5b6c', 'Adjustment');

-- -------------------------------------------------------------
-- Data for categories
-- -------------------------------------------------------------
INSERT INTO categories (category_id, name) VALUES
('b30a1c8f-28c0-43f5-a8e9-d757d54403c1', 'Laptops'),
('a2c7e0f8-1d4a-4e2b-9c6d-3f5c7b9e1d4c', 'Processors'),
('3e9a7c0d-b4e1-4c5d-8f2a-6b4e1c5d8f2d', 'Graphics Cards'),
('5c6d7e8f-9a0b-1c2d-3e4f-5a6b7c8d9e0f', 'Monitors'),
('e9b2c4f1-3d5a-6b8e-7c9d-8a1e2f3d4c6a', 'Cases'),
('8a1b9e2d-3f4a-5c6d-7e8f-9a0b1c2d3e5b', 'RAM'),
('f6b8e3d0-37e4-4a4b-8a71-6c7c25145888', 'SSD'),
('1b9e2d3f-4a5c-7d8e-8a1b-9e2d3f4a5c7a', 'HDD'),
('a1b2c3d4-e5f6-7a8b-9c0d-e1f2a3b4c5d8', 'Peripherals'),
('2b3c4d5e-6f7a-8b9c-0d1e-2f3a4b5c6d7e', 'NVMe M.2');

-- -------------------------------------------------------------
-- Product category assignments (product_categories)
-- -------------------------------------------------------------

-- Laptops (20 products)
INSERT INTO product_categories (product_id, category_id) VALUES
('b30a1c8f-28c0-43f5-a8e9-d757d54402a1', 'b30a1c8f-28c0-43f5-a8e9-d757d54403c1'),
('f6b8e3d0-37e4-4a4b-8a71-6c7c2514539e', 'b30a1c8f-28c0-43f5-a8e9-d757d54403c1'),
('d4f5c9b2-9a0e-4e6f-8d2b-5e6f8d2b5e6f', 'b30a1c8f-28c0-43f5-a8e9-d757d54403c1'),
('a2c7e0f8-1d4a-4e2b-9c6d-3f5c7b9e1a4d', 'b30a1c8f-28c0-43f5-a8e9-d757d54403c1'),
('3e9a7c0d-b4e1-4c5d-8f2a-6b4e1c5d8f2a', 'b30a1c8f-28c0-43f5-a8e9-d757d54403c1'),
('f1d2c3e4-5f6a-7b8c-9d0e-1f2a3c4d5e6f', 'b30a1c8f-28c0-43f5-a8e9-d757d54403c1'),
('7b3c2d4e-5f1a-6d8c-9e2b-3f4a5c6d7e8f', 'b30a1c8f-28c0-43f5-a8e9-d757d54403c1'),
('9d5e6f7c-8a1b-4d9e-c2f8-a1b9e2d3f4a5', 'b30a1c8f-28c0-43f5-a8e9-d757d54403c1'),
('2a4b6c8d-0e1f-2a3b-4c5d-6e7f8a9b0c1d', 'b30a1c8f-28c0-43f5-a8e9-d757d54403c1'),
('5d8a9b0c-1e2f-3a4b-5c6d-7e8f9a0b1c2d', 'b30a1c8f-28c0-43f5-a8e9-d757d54403c1'),
('e9b2c4f1-3d5a-6b8e-7c9d-8a1e2f3d4c5b', 'b30a1c8f-28c0-43f5-a8e9-d757d54403c1'),
('4f1a5e9b-2c3d-6e7f-8a9b-0c1d2e3f4a5b', 'b30a1c8f-28c0-43f5-a8e9-d757d54403c1'),
('b8d9c0e1-f2a3-4b5c-6d7e-8f9a0b1c2d3e', 'b30a1c8f-28c0-43f5-a8e9-d757d54403c1'),
('6c7c2514-539e-4a4b-8a71-f6b8e3d037e4', 'b30a1c8f-28c0-43f5-a8e9-d757d54403c1'),
('3a4b5c6d-7e8f-9a0b-1c2d-3e4f5a6b7c8d', 'b30a1c8f-28c0-43f5-a8e9-d757d54403c1'),
('1b9e2d3f-4a5c-7d8e-8a1b-9e2d3f4a5c7d', 'b30a1c8f-28c0-43f5-a8e9-d757d54403c1'),
('9a0b1c2d-3e4f-5a6b-7c8d-9e0f1a2b3c4d', 'b30a1c8f-28c0-43f5-a8e9-d757d54403c1'),
('5c6d7e8f-9a0b-1c2d-3e4f-5a6b7c8d9e0f', 'b30a1c8f-28c0-43f5-a8e9-d757d54403c1'),
('2d3f4a5c-6d7e-8f9a-0b1c-2d3e4f5a6b7c', 'b30a1c8f-28c0-43f5-a8e9-d757d54403c1'),
('8a1b9e2d-3f4a-5c6d-7e8f-9a0b1c2d3e4f', 'b30a1c8f-28c0-43f5-a8e9-d757d54403c1');

-- Processors (15 products)
INSERT INTO product_categories (product_id, category_id) VALUES
('8e7a6d5c-4b3c-2a1d-0f9e-8d7c6b5a4f3e', 'a2c7e0f8-1d4a-4e2b-9c6d-3f5c7b9e1d4c'),
('c7a8d9e0-f1b2-3c4d-5e6f-7a8b9c0d1e2f', 'a2c7e0f8-1d4a-4e2b-9c6d-3f5c7b9e1d4c'),
('a1b2c3d4-e5f6-7a8b-9c0d-e1f2a3b4c5d6', 'a2c7e0f8-1d4a-4e2b-9c6d-3f5c7b9e1d4c'),
('d5e6f7a8-b9c0-d1e2-f3a4-b5c6d7e8f9a0', 'a2c7e0f8-1d4a-4e2b-9c6d-3f5c7b9e1d4c'),
('2b3c4d5e-6f7a-8b9c-0d1e-2f3a4b5c6d7e', 'a2c7e0f8-1d4a-4e2b-9c6d-3f5c7b9e1d4c'),
('8c9d0e1f-2a3b-4c5d-6e7f-8a9b0c1d2e3f', 'a2c7e0f8-1d4a-4e2b-9c6d-3f5c7b9e1d4c'),
('e4f5a6b7-c8d9-0e1f-2a3b-4c5d6e7f8a9b', 'a2c7e0f8-1d4a-4e2b-9c6d-3f5c7b9e1d4c'),
('1f2a3b4c-5d6e-7f8a-9b0c-d1e2f3a4b5c6', 'a2c7e0f8-1d4a-4e2b-9c6d-3f5c7b9e1d4c'),
('9b0c1d2e-3f4a-5b6c-7d8e-9f0a1b2c3d4e', 'a2c7e0f8-1d4a-4e2b-9c6d-3f5c7b9e1d4c'),
('4d5e6f7a-8b9c-0d1e-2f3a-4b5c6d7e8f9a', 'a2c7e0f8-1d4a-4e2b-9c6d-3f5c7b9e1d4c'),
('e2f3a4b5-c6d7-e8f9-a0b1-c2d3e4f5a6b7', 'a2c7e0f8-1d4a-4e2b-9c6d-3f5c7b9e1d4c'),
('1c2d3e4f-5a6b-7c8d-9e0f-a1b2c3d4e5f6', 'a2c7e0f8-1d4a-4e2b-9c6d-3f5c7b9e1d4c'),
('7f8a9b0c-1d2e-3f4a-5b6c-7d8e9f0a1b2c', 'a2c7e0f8-1d4a-4e2b-9c6d-3f5c7b9e1d4c'),
('3a4b5c6d-7e8f-9a0b-1c2d-3e4f5a6b7c8f', 'a2c7e0f8-1d4a-4e2b-9c6d-3f5c7b9e1d4c'),
('f2a3b4c5-d6e7-f8a9-b0c1-d2e3f4a5b6c7', 'a2c7e0f8-1d4a-4e2b-9c6d-3f5c7b9e1d4c');

-- Graphics Cards (15 products)
INSERT INTO product_categories (product_id, category_id) VALUES
('6b4e1c5d-8f2a-3e9a-7c0d-b4e1c5d8f2a6', '3e9a7c0d-b4e1-4c5d-8f2a-6b4e1c5d8f2d'),
('9d5e6f7c-8a1b-4d9e-c2f8-a1b9e2d3f4a6', '3e9a7c0d-b4e1-4c5d-8f2a-6b4e1c5d8f2d'),
('1a2b3c4d-5e6f-7a8b-9c0d-e1f2a3b4c5d7', '3e9a7c0d-b4e1-4c5d-8f2a-6b4e1c5d8f2d'),
('4e5f6a7b-8c9d-0e1f-2a3b-4c5d6e7f8a9c', '3e9a7c0d-b4e1-4c5d-8f2a-6b4e1c5d8f2d'),
('8c9d0e1f-2a3b-4c5d-6e7f-8a9b0c1d2e3d', '3e9a7c0d-b4e1-4c5d-8f2a-6b4e1c5d8f2d'),
('e1f2a3b4-c5d6-e7f8-a9b0-c1d2e3f4a5b8', '3e9a7c0d-b4e1-4c5d-8f2a-6b4e1c5d8f2d'),
('f4e3d2c1-b0a9-8f7e-6d5c-4b3a2c1b0a9d', '3e9a7c0d-b4e1-4c5d-8f2a-6b4e1c5d8f2d'),
('5b6c7d8e-9f0a-1b2c-3d4e-5f6a7b8c9d0e', '3e9a7c0d-b4e1-4c5d-8f2a-6b4e1c5d8f2d'),
('6f7a8b9c-0d1e-2f3a-4b5c-6d7e8f9a0b1f', '3e9a7c0d-b4e1-4c5d-8f2a-6b4e1c5d8f2d'),
('7c8d9e0f-1a2b-3c4d-5e6f-7a8b9c0d1e2f', '3e9a7c0d-b4e1-4c5d-8f2a-6b4e1c5d8f2d'),
('e2f3a4b5-c6d7-e8f9-a0b1-c2d3e4f5a6b8', '3e9a7c0d-b4e1-4c5d-8f2a-6b4e1c5d8f2d'),
('2c3d4e5f-6a7b-8c9d-0e1f-2a3b4c5d6e7f', '3e9a7c0d-b4e1-4c5d-8f2a-6b4e1c5d8f2d');

-- Peripherals (15 products)
INSERT INTO product_categories (product_id, category_id) VALUES
('2e3f4a5b-6c7d-8e9f-0a1b-2c3d4e5f6a7b', 'a1b2c3d4-e5f6-7a8b-9c0d-e1f2a3b4c5d8'),
('d5e6f7a8-b9c0-d1e2-f3a4-b5c6d7e8f9a1', 'a1b2c3d4-e5f6-7a8b-9c0d-e1f2a3b4c5d8'),
('e4f5a6b7-c8d9-0e1f-2a3b-4c5d6e7f8a9d', 'a1b2c3d4-e5f6-7a8b-9c0d-e1f2a3b4c5d8'),
('6e7f8a9b-0c1d-2e3f-4a5b-6c7d8e9f0a1c', 'a1b2c3d4-e5f6-7a8b-9c0d-e1f2a3b4c5d8'),
('1c2d3e4f-5a6b-7c8d-9e0f-a1b2c3d4e5f7', 'a1b2c3d4-e5f6-7a8b-9c0d-e1f2a3b4c5d8'),
('4a5b6c7d-8e9f-0a1b-2c3d-4e5f6a7b8c9d', 'a1b2c3d4-e5f6-7a8b-9c0d-e1f2a3b4c5d8'),
('a1b2c3d4-e5f6-7a8b-9c0d-e1f2a3b4c5d9', 'a1b2c3d4-e5f6-7a8b-9c0d-e1f2a3b4c5d8');

-- RAM (5 products)
INSERT INTO product_categories (product_id, category_id) VALUES
('b9e0f1a2-c3d4-e5f6-a7b8-c9d0e1f2a3b1', '8a1b9e2d-3f4a-5c6d-7e8f-9a0b1c2d3e5b'),
('8c7d6e5f-4a3b-2c1d-0e9f-8a7b6c5d4e3f', '8a1b9e2d-3f4a-5c6d-7e8f-9a0b1c2d3e5b'),
('4d5e6f7a-8b9c-0d1e-2f3a-4b5c6d7e8f9b', '8a1b9e2d-3f4a-5c6d-7e8f-9a0b1c2d3e5b'),
('1f2a3b4c-5d6e-7f8a-9b0c-d1e2f3a4b5c7', '8a1b9e2d-3f4a-5c6d-7e8f-9a0b1c2d3e5b'),
('f9a0b1c2-d3e4-f5a6-b7c8-d9e0f1a2b3c4', '8a1b9e2d-3f4a-5c6d-7e8f-9a0b1c2d3e5b');

-- SSD (5 products)
INSERT INTO product_categories (product_id, category_id) VALUES
('e1d2c3f4-5a6b-7c8d-9e0f-a1b2c3d4e5f1', 'f6b8e3d0-37e4-4a4b-8a71-6c7c25145888'),
('f2a3c4d5-e6b7-f8a9-b0c1-d2e3f4a5b6c8', 'f6b8e3d0-37e4-4a4b-8a71-6c7c25145888'),
('d4e5f6a7-b8c9-0d1e-2f3a-4b5c6d7e8f9e', 'f6b8e3d0-37e4-4a4b-8a71-6c7c25145888'),
('a1b2c3d4-e5f6-7a8b-9c0d-e1f2a3b4c5f9', 'f6b8e3d0-37e4-4a4b-8a71-6c7c25145888'),
('e9b2c4f1-3d5a-6b8e-7c9d-8a1e2f3d4c5c', 'f6b8e3d0-37e4-4a4b-8a71-6c7c25145888');

-- HDD (5 products)
INSERT INTO product_categories (product_id, category_id) VALUES
('b30a1c8f-28c0-43f5-a8e9-d757d54402a2', '1b9e2d3f-4a5c-7d8e-8a1b-9e2d3f4a5c7a'),
('d4e5f6a7-b8c9-0d1e-2f3a-4b5c6d7e8f9a', '1b9e2d3f-4a5c-7d8e-8a1b-9e2d3f4a5c7a'),
('7b3c2d4e-5f1a-6d8c-9e2b-3f4a5c6d7e8a', '1b9e2d3f-4a5c-7d8e-8a1b-9e2d3f4a5c7a'),
('9d5e6f7c-8a1b-4d9e-c2f8-a1b9e2d3f4a7', '1b9e2d3f-4a5c-7d8e-8a1b-9e2d3f4a5c7a');

-- NVMe M.2 (5 products)
INSERT INTO product_categories (product_id, category_id) VALUES
('e4f5a6b7-c8d9-0e1f-2a3b-4c5d6e7f8a9e', '2b3c4d5e-6f7a-8b9c-0d1e-2f3a4b5c6d7e'),
('1f2a3b4c-5d6e-7f8a-9b0c-d1e2f3a4b5c8', '2b3c4d5e-6f7a-8b9c-0d1e-2f3a4b5c6d7e'),
('9d0e1f2a-3b4c-5d6e-7f8a-9b0c1d2e3f4f', '2b3c4d5e-6f7a-8b9c-0d1e-2f3a4b5c6d7e'),
('f6b8e3d0-37e4-4a4b-8a71-6c7c2514539f', '2b3c4d5e-6f7a-8b9c-0d1e-2f3a4b5c6d7e');

-- -------------------------------------------------------------
-- Data for product stock (products_inventory)
-- -------------------------------------------------------------
-- The stock values are random to provide variety.
-- Laptops
INSERT INTO products_inventory (product_id, stock) VALUES
('b30a1c8f-28c0-43f5-a8e9-d757d54402a1', 50),
('f6b8e3d0-37e4-4a4b-8a71-6c7c2514539e', 25),
('d4f5c9b2-9a0e-4e6f-8d2b-5e6f8d2b5e6f', 15),
('a2c7e0f8-1d4a-4e2b-9c6d-3f5c7b9e1a4d', 40),
('3e9a7c0d-b4e1-4c5d-8f2a-6b4e1c5d8f2a', 10),
('f1d2c3e4-5f6a-7b8c-9d0e-1f2a3c4d5e6f', 60),
('7b3c2d4e-5f1a-6d8c-9e2b-3f4a5c6d7e8f', 20),
('9d5e6f7c-8a1b-4d9e-c2f8-a1b9e2d3f4a5', 12),
('2a4b6c8d-0e1f-2a3b-4c5d-6e7f8a9b0c1d', 8),
('5d8a9b0c-1e2f-3a4b-5c6d-7e8f9a0b1c2d', 35),
('e9b2c4f1-3d5a-6b8e-7c9d-8a1e2f3d4c5b', 7),
('4f1a5e9b-2c3d-6e7f-8a9b-0c1d2e3f4a5b', 28),
('b8d9c0e1-f2a3-4b5c-6d7e-8f9a0b1c2d3e', 6),
('6c7c2514-539e-4a4b-8a71-f6b8e3d037e4', 11),
('3a4b5c6d-7e8f-9a0b-1c2d-3e4f5a6b7c8d', 9),
('1b9e2d3f-4a5c-7d8e-8a1b-9e2d3f4a5c7d', 14),
('9a0b1c2d-3e4f-5a6b-7c8d-9e0f1a2b3c4d', 45),
('5c6d7e8f-9a0b-1c2d-3e4f-5a6b7c8d9e0f', 55),
('2d3f4a5c-6d7e-8f9a-0b1c-2d3e4f5a6b7c', 30),
('8a1b9e2d-3f4a-5c6d-7e8f-9a0b1c2d3e4f', 22);

-- Processors
INSERT INTO products_inventory (product_id, stock) VALUES
('8e7a6d5c-4b3c-2a1d-0f9e-8d7c6b5a4f3e', 20),
('c7a8d9e0-f1b2-3c4d-5e6f-7a8b9c0d1e2f', 0),
('a1b2c3d4-e5f6-7a8b-9c0d-e1f2a3b4c5d6', 24),
('d5e6f7a8-b9c0-d1e2-f3a4-b5c6d7e8f9a0', 0),
('2b3c4d5e-6f7a-8b9c-0d1e-2f3a4b5c6d7e', 0),
('8c9d0e1f-2a3b-4c5d-6e7f-8a9b0c1d2e3f', 20),
('e4f5a6b7-c8d9-0e1f-2a3b-4c5d6e7f8a9b', 30),
('1f2a3b4c-5d6e-7f8a-9b0c-d1e2f3a4b5c6', 30),
('9b0c1d2e-3f4a-5b6c-7d8e-9f0a1b2c3d4e', 15),
('4d5e6f7a-8b9c-0d1e-2f3a-4b5c6d7e8f9a', 28),
('e2f3a4b5-c6d7-e8f9-a0b1-c2d3e4f5a6b7', 32),
('1c2d3e4f-5a6b-7c8d-9e0f-a1b2c3d4e5f6', 10),
('7f8a9b0c-1d2e-3f4a-5b6c-7d8e9f0a1b2c', 45),
('3a4b5c6d-7e8f-9a0b-1c2d-3e4f5a6b7c8f', 21),
('f2a3b4c5-d6e7-f8a9-b0c1-d2e3f4a5b6c7', 65);

-- Graphics Cards
INSERT INTO products_inventory (product_id, stock) VALUES
('6b4e1c5d-8f2a-3e9a-7c0d-b4e1c5d8f2a6', 5),
('9d5e6f7c-8a1b-4d9e-c2f8-a1b9e2d3f4a6', 8),
('1a2b3c4d-5e6f-7a8b-9c0d-e1f2a3b4c5d7', 12),
('4e5f6a7b-8c9d-0e1f-2a3b-4c5d6e7f8a9c', 20),
('8c9d0e1f-2a3b-4c5d-6e7f-8a9b0c1d2e3d', 0),
('e1f2a3b4-c5d6-e7f8-a9b0-c1d2e3f4a5b8', 0),
('f4e3d2c1-b0a9-8f7e-6d5c-4b3a2c1b0a9d', 0),
('5b6c7d8e-9f0a-1b2c-3d4e-5f6a7b8c9d0e', 0),
('6f7a8b9c-0d1e-2f3a-4b5c-6d7e8f9a0b1f', 10),
('7c8d9e0f-1a2b-3c4d-5e6f-7a8b9c0d1e2f', 11)

