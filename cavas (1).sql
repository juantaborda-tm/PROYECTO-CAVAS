-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 11-12-2025 a las 10:05:52
-- Versión del servidor: 10.4.32-MariaDB
-- Versión de PHP: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `cavas`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `bebidas`
--

CREATE TABLE `bebidas` (
  `disparador` int(11) NOT NULL,
  `id` int(11) NOT NULL,
  `nombre` varchar(128) NOT NULL,
  `categoria` varchar(10) NOT NULL,
  `cantidad` int(11) DEFAULT 0,
  `precio_compra` decimal(10,2) DEFAULT NULL,
  `precio_venta` decimal(10,2) DEFAULT NULL,
  `proveedor_cedula` varchar(18) DEFAULT NULL,
  `id_ubicacion` int(11) DEFAULT NULL,
  `fecha_ingreso` date DEFAULT curdate(),
  `id_categoria` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `bebidas`
--

INSERT INTO `bebidas` (`disparador`, `id`, `nombre`, `categoria`, `cantidad`, `precio_compra`, `precio_venta`, `proveedor_cedula`, `id_ubicacion`, `fecha_ingreso`, `id_categoria`) VALUES
(62, 0, '', 'postobon', 0, NULL, NULL, NULL, NULL, '2025-12-11', NULL),
(42, 1, 'Coca-Cola', 'Gaseosa', 50, NULL, NULL, NULL, NULL, '2025-12-10', NULL),
(43, 2, 'Pepsi', 'Gaseosa', 40, NULL, NULL, NULL, NULL, '2025-12-10', NULL),
(44, 3, 'Sprite', 'Gaseosa', 30, NULL, NULL, NULL, NULL, '2025-12-10', NULL),
(45, 4, 'Fanta Naranja', 'Gaseosa', 25, NULL, NULL, NULL, NULL, '2025-12-10', NULL),
(46, 5, 'Agua Cristal', 'Agua', 60, NULL, NULL, NULL, NULL, '2025-12-10', NULL),
(47, 6, 'Agua Evian', 'Agua', 20, NULL, NULL, NULL, NULL, '2025-12-10', NULL),
(48, 7, 'Jugo de Naranja', 'Jugo natur', 35, NULL, NULL, NULL, NULL, '2025-12-10', NULL),
(49, 8, 'Jugo de Mango', 'Jugo natur', 30, NULL, NULL, NULL, NULL, '2025-12-10', NULL),
(50, 9, 'Jugo de Piña', 'Jugo natur', 28, NULL, NULL, NULL, NULL, '2025-12-10', NULL),
(51, 10, 'Jugo de Mora', 'Jugo natur', 22, NULL, NULL, NULL, NULL, '2025-12-10', NULL),
(52, 11, 'Café Americano', 'Café', 40, NULL, NULL, NULL, NULL, '2025-12-10', NULL),
(53, 12, 'Cappuccino', 'Café', 25, NULL, NULL, NULL, NULL, '2025-12-10', NULL),
(54, 13, 'Té Verde', 'Té', 20, NULL, NULL, NULL, NULL, '2025-12-10', NULL),
(55, 14, 'Té Negro', 'Té', 18, NULL, NULL, NULL, NULL, '2025-12-10', NULL),
(56, 15, 'Cerveza Poker', 'Cerveza', 100, NULL, NULL, NULL, NULL, '2025-12-10', NULL),
(57, 16, 'Cerveza Club Colombia', 'Cerveza', 80, NULL, NULL, NULL, NULL, '2025-12-10', NULL),
(58, 17, 'Vino Tinto', 'Vino', 15, NULL, NULL, NULL, NULL, '2025-12-10', NULL),
(59, 18, 'Vino Blanco', 'Vino', 12, NULL, NULL, NULL, NULL, '2025-12-10', NULL),
(60, 19, 'Whisky', 'Licor', 10, NULL, NULL, NULL, NULL, '2025-12-10', NULL),
(61, 20, 'Ron Medellín', 'Licor', 20, NULL, NULL, NULL, NULL, '2025-12-10', NULL),
(38, 10000, 'cagasfranco', 'comemierda', 30, NULL, NULL, NULL, NULL, '2025-12-10', NULL),
(39, 119283223, 'poker', 'cerveza', 100, NULL, NULL, NULL, NULL, '2025-12-10', NULL);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `categorias`
--

CREATE TABLE `categorias` (
  `id_categoria` int(11) NOT NULL,
  `nombre_categoria` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `categorias`
--

INSERT INTO `categorias` (`id_categoria`, `nombre_categoria`) VALUES
(1, 'postobon'),
(2, 'cocacola'),
(3, 'mamahuevo'),
(4, 'siguiente'),
(5, 'juan'),
(6, 'alan'),
(7, 'mama');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `historial_productos`
--

CREATE TABLE `historial_productos` (
  `id` int(11) NOT NULL,
  `nombre_producto` varchar(255) DEFAULT NULL,
  `categoria` varchar(255) DEFAULT NULL,
  `descripcion` text DEFAULT NULL,
  `fecha` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `pedidos`
--

CREATE TABLE `pedidos` (
  `id_pedido` int(11) NOT NULL,
  `usuario_cedula` varchar(18) DEFAULT NULL,
  `proveedor_cedula` varchar(18) DEFAULT NULL,
  `juant` varchar(18) NOT NULL,
  `fecha_pedido` datetime DEFAULT current_timestamp(),
  `estado` enum('pendiente','recibido','cancelado','completado') DEFAULT 'pendiente'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `proveedores`
--

CREATE TABLE `proveedores` (
  `cedula` varchar(18) NOT NULL,
  `nit` varchar(18) NOT NULL,
  `nombre` varchar(15) NOT NULL,
  `telefono` varchar(20) DEFAULT NULL,
  `correo` varchar(40) DEFAULT NULL,
  `direccion` varchar(30) DEFAULT NULL,
  `fecha_registro` datetime DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `proveedores`
--

INSERT INTO `proveedores` (`cedula`, `nit`, `nombre`, `telefono`, `correo`, `direccion`, `fecha_registro`) VALUES
('123456789', '900123456', 'Proveedor Coca-', '3001234567', 'coca@proveedor.com', 'Calle 10 #20-30', '2025-11-01 00:00:00'),
('456789123', '901456789', 'Distribuidor Ba', '3014567890', 'bavaria@proveedor.com', 'Av. Siempre Viva 123', '2025-11-03 00:00:00'),
('987654320', '1073233792', 'Alan ', '3214567890', 'pinilla@gmail.com', 'calle 24D 18S', '2025-12-10 19:31:43'),
('987654321', '900987654', 'Proveedor Posto', '3009876543', 'postobon@proveedor.com', 'Carrera 15 #45-60', '2025-11-02 00:00:00');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `ubicaciones`
--

CREATE TABLE `ubicaciones` (
  `id_ubicacion` int(11) NOT NULL,
  `numero_estanteria` int(11) NOT NULL,
  `numero_peldano` int(11) NOT NULL,
  `descripcion` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `ubicaciones`
--

INSERT INTO `ubicaciones` (`id_ubicacion`, `numero_estanteria`, `numero_peldano`, `descripcion`) VALUES
(1, 0, 1, 'Estante A - Peldano 1: Gaseosas'),
(2, 0, 2, 'Estante A - Peldano 2: Aguas'),
(3, 0, 1, 'Estante B - Peldano 1: Cervezas'),
(4, 0, 2, 'Estante B - Peldano 2: Jugos'),
(5, 0, 1, 'Estante C - Peldano 1: Energizantes');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuarios`
--

CREATE TABLE `usuarios` (
  `num_id` varchar(18) NOT NULL,
  `nom_comple` varchar(30) DEFAULT NULL,
  `correo` varchar(40) NOT NULL,
  `contra` varchar(255) NOT NULL,
  `nom_empresa` varchar(50) NOT NULL,
  `num_tel` varchar(11) NOT NULL,
  `nit_empre` varchar(9) NOT NULL,
  `fecha_naci` date NOT NULL,
  `tipo_id` varchar(100) NOT NULL,
  `roll` varchar(3) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `usuarios`
--

INSERT INTO `usuarios` (`num_id`, `nom_comple`, `correo`, `contra`, `nom_empresa`, `num_tel`, `nit_empre`, `fecha_naci`, `tipo_id`, `roll`) VALUES
('1073233793', 'Alan ', 'alan@gmail.com', '12345678', 'inventario cava', '3217721514', '107323379', '2026-01-03', 'documento_1', '1'),
('1234567880', 'leandra', 'leandra@gmail.com', '123456789', '', '3217721654', '', '2025-12-08', 'Cedula de ciudadania', '2');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `bebidas`
--
ALTER TABLE `bebidas`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `disparador` (`disparador`),
  ADD KEY `proveedor_cedula` (`proveedor_cedula`),
  ADD KEY `id_ubicacion` (`id_ubicacion`),
  ADD KEY `nombre` (`nombre`),
  ADD KEY `categoria` (`categoria`),
  ADD KEY `fk_bebidas_categorias` (`id_categoria`);

--
-- Indices de la tabla `categorias`
--
ALTER TABLE `categorias`
  ADD PRIMARY KEY (`id_categoria`);

--
-- Indices de la tabla `historial_productos`
--
ALTER TABLE `historial_productos`
  ADD PRIMARY KEY (`id`),
  ADD KEY `nombre_producto` (`nombre_producto`);

--
-- Indices de la tabla `pedidos`
--
ALTER TABLE `pedidos`
  ADD PRIMARY KEY (`id_pedido`),
  ADD KEY `usuario_cedula` (`usuario_cedula`),
  ADD KEY `proveedor_cedula` (`proveedor_cedula`);

--
-- Indices de la tabla `proveedores`
--
ALTER TABLE `proveedores`
  ADD PRIMARY KEY (`cedula`),
  ADD UNIQUE KEY `nit` (`nit`);

--
-- Indices de la tabla `ubicaciones`
--
ALTER TABLE `ubicaciones`
  ADD PRIMARY KEY (`id_ubicacion`);

--
-- Indices de la tabla `usuarios`
--
ALTER TABLE `usuarios`
  ADD PRIMARY KEY (`num_id`),
  ADD UNIQUE KEY `correo` (`correo`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `bebidas`
--
ALTER TABLE `bebidas`
  MODIFY `disparador` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=65;

--
-- AUTO_INCREMENT de la tabla `categorias`
--
ALTER TABLE `categorias`
  MODIFY `id_categoria` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT de la tabla `historial_productos`
--
ALTER TABLE `historial_productos`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `pedidos`
--
ALTER TABLE `pedidos`
  MODIFY `id_pedido` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `ubicaciones`
--
ALTER TABLE `ubicaciones`
  MODIFY `id_ubicacion` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `bebidas`
--
ALTER TABLE `bebidas`
  ADD CONSTRAINT `bebidas_ibfk_1` FOREIGN KEY (`proveedor_cedula`) REFERENCES `proveedores` (`cedula`),
  ADD CONSTRAINT `bebidas_ibfk_2` FOREIGN KEY (`id_ubicacion`) REFERENCES `ubicaciones` (`id_ubicacion`),
  ADD CONSTRAINT `fk_bebidas_categorias` FOREIGN KEY (`id_categoria`) REFERENCES `categorias` (`id_categoria`);

--
-- Filtros para la tabla `historial_productos`
--
ALTER TABLE `historial_productos`
  ADD CONSTRAINT `historial_productos_ibfk_1` FOREIGN KEY (`nombre_producto`) REFERENCES `bebidas` (`nombre`);

--
-- Filtros para la tabla `pedidos`
--
ALTER TABLE `pedidos`
  ADD CONSTRAINT `pedidos_ibfk_1` FOREIGN KEY (`usuario_cedula`) REFERENCES `usuarios` (`num_id`),
  ADD CONSTRAINT `pedidos_ibfk_2` FOREIGN KEY (`proveedor_cedula`) REFERENCES `proveedores` (`cedula`),
  ADD CONSTRAINT `pedidos_ibfk_3` FOREIGN KEY (`juant`) REFERENCES `clientes` (`cedula`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
