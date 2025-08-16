--Menu
-- Wok
INSERT INTO comidas.productos (nombre, descripcion, precio, categoria, disponible, imagen_url, created_at, updated_at) VALUES
('Wok de Vegetales', 'Vegetales salteados con salsa de soja y arroz o fideos de arroz', 7000, 'Wok', TRUE, NULL, NOW(), NOW()),
('Wok de Ave', 'Vegetales salteados con pollo, salsa de soja y arroz o fideos de arroz', 7700, 'Wok', TRUE, NULL, NOW(), NOW()),
('Wok de Cerdo', 'Vegetales salteados con cerdo, salsa de soja y arroz o fideos de arroz', 8000, 'Wok', TRUE, NULL, NOW(), NOW()),
('Wok de Lomo', 'Vegetales salteados con lomo, salsa de soja y arroz o fideos de arroz', 8300, 'Wok', TRUE, NULL, NOW(), NOW()),
('Wok de Camarones', 'Vegetales salteados con camarones, salsa de soja y arroz o fideos de arroz', 9700, 'Wok', TRUE, NULL, NOW(), NOW());

-- Ensaladas
INSERT INTO comidas.productos (nombre, descripcion, precio, categoria, disponible, imagen_url, created_at, updated_at) VALUES
('Ensalada Caesar', 'Lechuga, crutons, queso parmesano, daditos de pollo, aderezo Caesar', 7800, 'Ensaladas', TRUE, NULL, NOW(), NOW()),
('Ensalada Al Dente', 'Lechuga, rúcula, tomates cherris, granos de choclo amarillos, kanikamas, huevo duro, palmitos y salsa golf', 8400, 'Ensaladas', TRUE, NULL, NOW(), NOW()),
('Ensalada Primavera', 'Pollo, choclo, lechuga, tomate, zanahoria y huevo', 7600, 'Ensaladas', TRUE, NULL, NOW(), NOW());

-- Burritos
INSERT INTO comidas.productos (nombre, descripcion, precio, categoria, disponible, imagen_url, created_at, updated_at) VALUES
('Burrito de Lomo', 'Relleno de cebolla, pimientos, zanahoria y lomo salteado acompañado de salsa de guacamole y jitomate', 8500, 'Burritos', TRUE, NULL, NOW(), NOW()),
('Burrito de Ave', 'Relleno de cebolla, pimientos, zanahoria y lomo salteado acompañado de salsa de guacamole y jitomate', 8300, 'Burritos', TRUE, NULL, NOW(), NOW()),
('Mix Mexicano', '1 unidad Burrito de lomo, 1 unidad Burrito de ave, nachos y salsas de guacamole y jitomate', 9300, 'Burritos', TRUE, NULL, NOW(), NOW());

-- Sandwiches
INSERT INTO comidas.productos (nombre, descripcion, precio, categoria, disponible, imagen_url, created_at, updated_at) VALUES
('Sandwich Lomo Al Dente', 'Lechuga, tomate, rúcula, jamón crudo, lomo, queso cheddar, panceta y huevo', 8600, 'Sandwiches', TRUE, NULL, NOW(), NOW()),
('Sandwich Mapio', 'Pan y mayonesa de la casa, milanesa a la napolitana, lechuga y huevo', 8600, 'Sandwiches', TRUE, NULL, NOW(), NOW()),
('Sandwich Vegetariano', 'Pan con semillas, lechuga, tomate, choclo, huevo y queso', 7500, 'Sandwiches', TRUE, NULL, NOW(), NOW()),
('Sandwich Pan de Ajo y Parmesano', 'Lomo desmechado, cebolla morada, lechuga, rúcula, tomate, queso cheddar, panceta, jamón crudo y huevo crudo', 8600, 'Sandwiches', TRUE, NULL, NOW(), NOW());

-- Pastas caseras
INSERT INTO comidas.productos (nombre, descripcion, precio, categoria, disponible, imagen_url, created_at, updated_at) VALUES
('Tallarines Caseros', 'Con salsa roja', 4800, 'Pastas', TRUE, NULL, NOW(), NOW()),
('Sorrentinos de Jamón y Queso', 'Con salsa roja', 6500, 'Pastas', TRUE, NULL, NOW(), NOW()),
('Sorrentinos Negros de Salmón', 'Con salsa roja', 9500, 'Pastas', TRUE, NULL, NOW(), NOW()),
('Ravioles de Verdura', 'Con salsa roja', 6300, 'Pastas', TRUE, NULL, NOW(), NOW()),
('Capelettis de Jamón Crudo, Nuez y Roquefort', 'Con salsa roja', 6900, 'Pastas', TRUE, NULL, NOW(), NOW()),
('Ñoquis de papa', 'Con salsa roja', 4800, 'Pastas', TRUE, NULL, NOW(), NOW());

-- Salsas
INSERT INTO comidas.productos (nombre, descripcion, precio, categoria, disponible, imagen_url, created_at, updated_at) VALUES
('Salsa Mixta', NULL, 3000, 'Salsas', TRUE, NULL, NOW(), NOW()),
('Salsa Blanca', NULL, 3000, 'Salsas', TRUE, NULL, NOW(), NOW()),
('Salsa Mixta con Peceto', NULL, 3900, 'Salsas', TRUE, NULL, NOW(), NOW()),
('Salsa Bolognesa', NULL, 3900, 'Salsas', TRUE, NULL, NOW(), NOW()),
('Salsa de Roquefort', NULL, 3900, 'Salsas', TRUE, NULL, NOW(), NOW()),
('Salsa Champignon', NULL, 4300, 'Salsas', TRUE, NULL, NOW(), NOW()),
('Salsa 3 Hongos', NULL, 4500, 'Salsas', TRUE, NULL, NOW(), NOW()),
('Salsa Parisienne', NULL, 4500, 'Salsas', TRUE, NULL, NOW(), NOW()),
('Salsa de Camarones', NULL, 5500, 'Salsas', TRUE, NULL, NOW(), NOW());

-- Entradas
INSERT INTO comidas.productos (nombre, descripcion, precio, categoria, disponible, imagen_url, created_at, updated_at) VALUES
('Rabas', NULL, 6500, 'Entradas', TRUE, NULL, NOW(), NOW()),
('Papas Fritas', NULL, 3500, 'Entradas', TRUE, NULL, NOW(), NOW()),
('Papas Gratinadas con Cheddar y Panceta', NULL, 5500, 'Entradas', TRUE, NULL, NOW(), NOW()),
('Picada de Mar y Tierra', 'Rabas, langostinos apanados, pollo frito, milanesa, papas y 4 salsas caseras', 12000, 'Entradas', TRUE, NULL, NOW(), NOW()),
('Pollo Frito para Compartir', 'Acompañado de papas fritas y 4 salsas caseras', 9800, 'Entradas', TRUE, NULL, NOW(), NOW());

-- Empanadas Tradicionales
INSERT INTO comidas.productos (nombre, descripcion, precio, categoria, disponible, imagen_url, created_at, updated_at) VALUES
('Empanada de Carne', NULL, 1200, 'Empanadas', TRUE, NULL, NOW(), NOW()),
('Empanada de Jamón y Queso', NULL, 1200, 'Empanadas', TRUE, NULL, NOW(), NOW()),
('Empanada de Humita', NULL, 1200, 'Empanadas', TRUE, NULL, NOW(), NOW()),
('Empanada de Queso y Cebolla', NULL, 1200, 'Empanadas', TRUE, NULL, NOW(), NOW()),
('Empanada Caprese', NULL, 1200, 'Empanadas', TRUE, NULL, NOW(), NOW()),
('Empanada de Atún', NULL, 1200, 'Empanadas', TRUE, NULL, NOW(), NOW()),
('Empanada Cordobesa', NULL, 1200, 'Empanadas', TRUE, NULL, NOW(), NOW()),
('Empanada de Carne Picante', NULL, 1200, 'Empanadas', TRUE, NULL, NOW(), NOW()),
('Empanada Árabe', NULL, 1200, 'Empanadas', TRUE, NULL, NOW(), NOW()),
('Empanada de Verdura', NULL, 1200, 'Empanadas', TRUE, NULL, NOW(), NOW());

-- Empanadas Gourmet
INSERT INTO comidas.productos (nombre, descripcion, precio, categoria, disponible, imagen_url, created_at, updated_at) VALUES
('Empanada de Cebolla, Queso y Roquefort', NULL, 1500, 'Empanadas Gourmet', TRUE, NULL, NOW(), NOW()),
('Empanada de Queso, Roquefort y Nuez', NULL, 1500, 'Empanadas Gourmet', TRUE, NULL, NOW(), NOW()),
('Empanada de Rúcula y Jamón Crudo', NULL, 1500, 'Empanadas Gourmet', TRUE, NULL, NOW(), NOW()),
('Empanada de Pollo al Champignon', NULL, 1500, 'Empanadas Gourmet', TRUE, NULL, NOW(), NOW()),
('Empanada de Matambre Cortado a Cuchillo', NULL, 1500, 'Empanadas Gourmet', TRUE, NULL, NOW(), NOW()),
('Empanada de Fugazza y Panceta', NULL, 1500, 'Empanadas Gourmet', TRUE, NULL, NOW(), NOW()),
('Empanada Napo con Ajo', NULL, 1500, 'Empanadas Gourmet', TRUE, NULL, NOW(), NOW()),
('Empanada Bacon y Cheddar', NULL, 1500, 'Empanadas Gourmet', TRUE, NULL, NOW(), NOW()),
('Empanada Criollas Fritas', NULL, 1500, 'Empanadas Gourmet', TRUE, NULL, NOW(), NOW());

-- Platos Principales
INSERT INTO comidas.productos (nombre, descripcion, precio, categoria, disponible, imagen_url, created_at, updated_at) VALUES
('Lomo Grillado con Puré', NULL, 15000, 'Platos Principales', TRUE, NULL, NOW(), NOW()),
('Bife de Chorizo a Caballo con Papas Fritas', NULL, 16500, 'Platos Principales', TRUE, NULL, NOW(), NOW()),
('Milanesa de Ternera con Puré o Papas Fritas', NULL, 9500, 'Platos Principales', TRUE, NULL, NOW(), NOW()),
('Milanesa a la Napolitana con Puré o Papas Fritas', NULL, 11800, 'Platos Principales', TRUE, NULL, NOW(), NOW()),
('Muslo Deshuesado a la Plancha con Salsa de Champignon y Puré', NULL, 10500, 'Platos Principales', TRUE, NULL, NOW(), NOW());

-- Pizzas
INSERT INTO comidas.productos (nombre, descripcion, precio, categoria, disponible, imagen_url, created_at, updated_at) VALUES
('Pizza Muzzarella', NULL, 9200, 'Pizzas', TRUE, NULL, NOW(), NOW()),
('Pizza Especial', NULL, 11000, 'Pizzas', TRUE, NULL, NOW(), NOW()),
('Pizza 3 Quesos', NULL, 11000, 'Pizzas', TRUE, NULL, NOW(), NOW()),
('Pizza Fugazzeta', NULL, 11000, 'Pizzas', TRUE, NULL, NOW(), NOW()),
('Pizza Napolitana y Ajo', NULL, 11000, 'Pizzas', TRUE, NULL, NOW(), NOW()),
('Pizza Rúcula y Jamón Crudo', NULL, 11700, 'Pizzas', TRUE, NULL, NOW(), NOW()),
('Pizza Palmitos, Salsa Golf y Jamón Crudo', NULL, 12000, 'Pizzas', TRUE, NULL, NOW(), NOW()),
('Pizza Valentín', 'Pollo, verdeo, panceta y queso provolone', 12200, 'Pizzas', TRUE, NULL, NOW(), NOW());

-- Hamburguesas
INSERT INTO comidas.productos (nombre, descripcion, precio, categoria, disponible, imagen_url, created_at, updated_at) VALUES
('Hamburguesa de Quesos', 'Lechuga, tomate, carne, queso muzza, queso tubo, queso cheddar, aros de cebolla morada, panceta, jamón cocido, huevo y papas fritas', 7500, 'Hamburguesas', TRUE, NULL, NOW(), NOW()),
('Hamburguesa Mexicana', 'Lechuga, tomate, carne, queso cheddar, aros de cebolla morada, panceta, jamón cocido, huevo, guacamole y nachos', 7500, 'Hamburguesas', TRUE, NULL, NOW(), NOW());