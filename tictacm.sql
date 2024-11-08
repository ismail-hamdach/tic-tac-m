-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Oct 06, 2024 at 10:21 PM
-- Server version: 5.7.31
-- PHP Version: 8.0.30

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `tictacm`
--

-- --------------------------------------------------------

--
-- Table structure for table `attendance_checks`
--

CREATE TABLE `attendance_checks` (
  `id` int(11) NOT NULL,
  `check_in` int(11) NOT NULL DEFAULT '0',
  `check_out` int(11) NOT NULL DEFAULT '0',
  `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `date` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `attendance_checks`
--

INSERT INTO `attendance_checks` (`id`, `check_in`, `check_out`, `created_at`, `updated_at`, `date`) VALUES
(1, 2, 2, '2024-08-19 18:40:47', '2024-08-19 18:51:37', '2024-08-19 00:36:30'),
(2, 5, 5, '2024-08-20 01:27:47', '2024-08-20 17:19:15', '2024-08-19 23:00:00'),
(6, 0, 1, '2024-08-22 14:32:39', '2024-08-22 14:32:39', '2024-08-21 23:00:00');

-- --------------------------------------------------------

--
-- Table structure for table `attendance_logs`
--

CREATE TABLE `attendance_logs` (
  `index` bigint(20) DEFAULT NULL,
  `user_id` bigint(20) DEFAULT NULL,
  `status` int(11) DEFAULT NULL,
  `check_in` datetime DEFAULT NULL,
  `check_out` datetime DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Dumping data for table `attendance_logs`
--

INSERT INTO `attendance_logs` (`index`, `user_id`, `status`, `check_in`, `check_out`) VALUES
(0, 1017, 0, '2024-05-29 10:00:00', '2024-05-30 18:00:00'),
(1, 1004, 0, '2024-05-30 09:00:00', '2024-05-29 04:00:00'),
(2, 1037, 0, '2024-05-31 17:00:00', '2024-05-31 00:00:00'),
(3, 1036, 1, '2024-05-30 22:00:00', '2024-05-29 09:00:00'),
(4, 1001, 1, '2024-05-28 20:00:00', '2024-06-01 12:00:00'),
(5, 1007, 0, '2024-05-28 23:00:00', '2024-06-01 09:00:00'),
(6, 1042, 1, '2024-06-01 01:00:00', '2024-05-29 00:00:00'),
(7, 1016, 1, '2024-05-29 08:00:00', '2024-05-30 01:00:00'),
(8, 1009, 1, '2024-05-28 08:00:00', '2024-05-31 02:00:00'),
(9, 1006, 1, '2024-05-29 04:00:00', '2024-05-28 16:00:00'),
(10, 1001, 1, '2024-05-28 02:00:00', '2024-05-30 06:00:00'),
(11, 1022, 0, '2024-05-28 09:00:00', '2024-06-01 03:00:00'),
(12, 1020, 0, '2024-05-28 00:00:00', '2024-05-31 15:00:00'),
(13, 1047, 1, '2024-05-29 14:00:00', '2024-05-31 21:00:00'),
(14, 1008, 1, '2024-05-31 11:00:00', '2024-05-29 11:00:00'),
(15, 1033, 1, '2024-05-29 11:00:00', '2024-05-31 04:00:00'),
(16, 1029, 1, '2024-05-30 08:00:00', '2024-05-29 10:00:00'),
(17, 1014, 1, '2024-05-30 07:00:00', '2024-05-29 13:00:00'),
(18, 1038, 1, '2024-05-28 07:00:00', '2024-05-30 04:00:00'),
(19, 1012, 1, '2024-05-28 20:00:00', '2024-05-30 17:00:00'),
(20, 1029, 1, '2024-05-29 12:00:00', '2024-05-31 13:00:00'),
(21, 1016, 0, '2024-05-29 10:00:00', '2024-06-01 00:00:00'),
(22, 1045, 0, '2024-05-28 18:00:00', '2024-05-28 12:00:00'),
(23, 1020, 0, '2024-05-30 13:00:00', '2024-06-01 07:00:00'),
(24, 1046, 0, '2024-05-28 13:00:00', '2024-05-31 03:00:00'),
(25, 1024, 0, '2024-05-31 12:00:00', '2024-05-30 10:00:00'),
(26, 1020, 0, '2024-05-31 14:00:00', '2024-06-01 07:00:00'),
(27, 1025, 1, '2024-05-30 14:00:00', '2024-05-30 23:00:00'),
(28, 1037, 0, '2024-05-28 10:00:00', '2024-05-30 22:00:00'),
(29, 1014, 0, '2024-05-31 15:00:00', '2024-06-01 06:00:00'),
(30, 1041, 0, '2024-05-28 23:00:00', '2024-05-30 03:00:00'),
(31, 1007, 1, '2024-05-31 11:00:00', '2024-05-28 13:00:00'),
(32, 1010, 1, '2024-05-28 18:00:00', '2024-06-01 03:00:00'),
(33, 1026, 0, '2024-05-28 05:00:00', '2024-05-28 13:00:00'),
(34, 1032, 0, '2024-06-01 00:00:00', '2024-06-01 06:00:00'),
(35, 1010, 1, '2024-06-01 03:00:00', '2024-05-29 23:00:00'),
(36, 1013, 1, '2024-05-31 10:00:00', '2024-05-29 00:00:00'),
(37, 1033, 1, '2024-05-30 11:00:00', '2024-05-28 10:00:00'),
(38, 1043, 0, '2024-05-28 18:00:00', '2024-05-30 02:00:00'),
(39, 1032, 1, '2024-05-29 20:00:00', '2024-05-30 08:00:00'),
(40, 1034, 0, '2024-05-28 08:00:00', '2024-05-29 09:00:00'),
(41, 1047, 1, '2024-05-30 13:00:00', '2024-05-31 12:00:00'),
(42, 1038, 0, '2024-05-30 05:00:00', '2024-05-30 21:00:00'),
(43, 1027, 0, '2024-05-28 10:00:00', '2024-06-01 03:00:00'),
(44, 1001, 0, '2024-05-30 23:00:00', '2024-05-31 08:00:00'),
(45, 1028, 0, '2024-05-28 01:00:00', '2024-05-29 20:00:00'),
(46, 1037, 1, '2024-05-31 20:00:00', '2024-05-31 13:00:00'),
(47, 1031, 1, '2024-05-30 15:00:00', '2024-06-01 12:00:00'),
(48, 1037, 0, '2024-05-29 06:00:00', '2024-05-28 22:00:00'),
(49, 1013, 1, '2024-05-31 10:00:00', '2024-05-30 19:00:00'),
(50, 1018, 1, '2024-05-30 02:00:00', '2024-05-30 03:00:00'),
(51, 1007, 1, '2024-05-31 09:00:00', '2024-06-01 09:00:00'),
(52, 1049, 1, '2024-05-30 16:00:00', '2024-05-31 22:00:00'),
(53, 1033, 1, '2024-05-30 16:00:00', '2024-06-01 00:00:00'),
(54, 1027, 0, '2024-05-28 11:00:00', '2024-05-31 13:00:00'),
(55, 1031, 0, '2024-05-28 14:00:00', '2024-05-31 17:00:00'),
(56, 1003, 0, '2024-05-28 09:00:00', '2024-05-30 04:00:00'),
(57, 1004, 0, '2024-05-29 23:00:00', '2024-05-31 08:00:00'),
(58, 1024, 0, '2024-05-30 16:00:00', '2024-05-31 21:00:00'),
(59, 1044, 0, '2024-05-31 05:00:00', '2024-05-29 19:00:00'),
(60, 1036, 1, '2024-05-28 22:00:00', '2024-05-30 17:00:00'),
(61, 1004, 1, '2024-05-31 16:00:00', '2024-05-28 13:00:00'),
(62, 1004, 1, '2024-05-30 15:00:00', '2024-05-31 07:00:00'),
(63, 1025, 0, '2024-05-30 15:00:00', '2024-05-30 00:00:00'),
(64, 1009, 0, '2024-05-29 09:00:00', '2024-06-01 04:00:00'),
(65, 1016, 0, '2024-05-30 08:00:00', '2024-05-30 07:00:00'),
(66, 1003, 1, '2024-05-31 10:00:00', '2024-05-30 01:00:00'),
(67, 1005, 1, '2024-05-28 17:00:00', '2024-05-30 22:00:00'),
(68, 1042, 0, '2024-05-31 20:00:00', '2024-05-31 02:00:00'),
(69, 1017, 1, '2024-05-29 00:00:00', '2024-05-29 12:00:00'),
(70, 1044, 0, '2024-05-31 05:00:00', '2024-05-31 00:00:00'),
(71, 1027, 1, '2024-05-28 14:00:00', '2024-05-29 18:00:00'),
(72, 1042, 1, '2024-05-31 19:00:00', '2024-05-29 23:00:00'),
(73, 1010, 1, '2024-05-31 17:00:00', '2024-06-01 04:00:00'),
(74, 1028, 1, '2024-05-28 13:00:00', '2024-05-29 10:00:00'),
(75, 1027, 1, '2024-05-31 20:00:00', '2024-05-30 13:00:00'),
(76, 1008, 1, '2024-05-31 05:00:00', '2024-05-31 20:00:00'),
(77, 1028, 0, '2024-05-29 21:00:00', '2024-05-29 15:00:00'),
(78, 1009, 0, '2024-05-28 03:00:00', '2024-05-30 13:00:00'),
(79, 1035, 0, '2024-05-31 10:00:00', '2024-06-01 02:00:00'),
(80, 1033, 1, '2024-05-30 08:00:00', '2024-05-31 22:00:00'),
(81, 1043, 1, '2024-05-29 04:00:00', '2024-05-30 00:00:00'),
(82, 1003, 1, '2024-05-29 06:00:00', '2024-06-01 04:00:00'),
(83, 1042, 0, '2024-05-29 21:00:00', '2024-05-31 19:00:00'),
(84, 1032, 0, '2024-05-31 08:00:00', '2024-05-28 10:00:00'),
(85, 1007, 0, '2024-05-28 20:00:00', '2024-05-31 22:00:00'),
(86, 1015, 0, '2024-05-30 23:00:00', '2024-05-28 16:00:00'),
(87, 1015, 1, '2024-05-30 21:00:00', '2024-05-30 01:00:00'),
(88, 1019, 1, '2024-05-29 10:00:00', '2024-05-31 10:00:00'),
(89, 1047, 0, '2024-05-29 04:00:00', '2024-05-28 23:00:00'),
(90, 1004, 1, '2024-05-29 18:00:00', '2024-05-30 20:00:00'),
(91, 1001, 0, '2024-05-30 05:00:00', '2024-05-31 22:00:00'),
(92, 1026, 1, '2024-05-31 06:00:00', '2024-05-29 08:00:00'),
(93, 1036, 0, '2024-05-31 21:00:00', '2024-05-31 11:00:00'),
(94, 1036, 1, '2024-05-31 18:00:00', '2024-05-31 09:00:00'),
(95, 1050, 0, '2024-06-01 00:00:00', '2024-05-30 06:00:00'),
(96, 1021, 0, '2024-05-30 12:00:00', '2024-05-29 08:00:00'),
(97, 1031, 1, '2024-05-30 21:00:00', '2024-06-01 02:00:00'),
(98, 1046, 1, '2024-05-29 10:00:00', '2024-05-30 05:00:00'),
(99, 1013, 1, '2024-05-30 22:00:00', '2024-05-30 05:00:00');

-- --------------------------------------------------------

--
-- Table structure for table `employees`
--

CREATE TABLE `employees` (
  `index` bigint(20) DEFAULT NULL,
  `user_id` bigint(20) DEFAULT NULL,
  `user_name` text,
  `phone_number` int(11) DEFAULT NULL,
  `privilege` text
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Dumping data for table `employees`
--

INSERT INTO `employees` (`index`, `user_id`, `user_name`, `phone_number`, `privilege`) VALUES
(0, 1001, 'Jane', 2719282, 'admin'),
(1, 1002, 'Michael', 2765156, 'manager'),
(2, 1003, 'Michael', 1247755, 'employee'),
(3, 1004, 'Emily', 2800364, 'manager'),
(4, 1005, 'John', 5340559, 'admin'),
(5, 1006, 'Jane', 1155888, 'manager'),
(6, 1007, 'John', 1168022, 'employee'),
(7, 1008, 'Jane', 2558086, 'admin'),
(8, 1009, 'John', 6088945, 'employee'),
(9, 1010, 'John', 4217344, 'admin'),
(10, 1011, 'John', 1961225, 'manager'),
(11, 1012, 'Jane', 3870854, 'admin'),
(12, 1013, 'Emily', 4364800, 'manager'),
(13, 1014, 'Michael', 2626800, 'employee'),
(14, 1015, 'Jane', 7293443, 'admin'),
(15, 1016, 'John', 4350748, 'admin'),
(16, 1017, 'Michael', 1341428, 'manager'),
(17, 1018, 'Michael', 6645719, 'admin'),
(18, 1019, 'Michael', 1586854, 'employee'),
(19, 1020, 'John', 7147236, 'manager'),
(20, 1021, 'Jane', 6157749, 'manager'),
(21, 1022, 'John', 3597539, 'admin'),
(22, 1023, 'Jane', 3383245, 'manager'),
(23, 1024, 'Michael', 6257533, 'employee'),
(24, 1025, 'Emily', 7447796, 'manager'),
(25, 1026, 'Michael', 1024145, 'manager'),
(26, 1027, 'Emily', 5412712, 'manager'),
(27, 1028, 'Emily', 6777682, 'admin'),
(28, 1029, 'John', 2820178, 'admin'),
(29, 1030, 'John', 2849737, 'admin'),
(30, 1031, 'Emily', 7576353, 'employee'),
(31, 1032, 'John', 2319614, 'employee'),
(32, 1033, 'John', 6152939, 'employee'),
(33, 1034, 'Emily', 1785610, 'admin'),
(34, 1035, 'Emily', 8497543, 'employee'),
(35, 1036, 'Jane', 2959580, 'employee'),
(36, 1037, 'Jane', 5096588, 'admin'),
(37, 1038, 'Jane', 3330858, 'manager'),
(38, 1039, 'Jane', 6700742, 'employee'),
(39, 1040, 'Jane', 2495562, 'manager'),
(40, 1041, 'Jane', 8244956, 'manager'),
(41, 1042, 'John', 4449819, 'manager'),
(42, 1043, 'Michael', 5983032, 'manager'),
(43, 1044, 'Michael', 7895657, 'manager'),
(44, 1045, 'Jane', 5548004, 'manager'),
(45, 1046, 'John', 3000714, 'employee'),
(46, 1047, 'Emily', 3275995, 'admin'),
(47, 1048, 'Jane', 8150745, 'admin'),
(48, 1049, 'Jane', 8508425, 'manager'),
(49, 1050, 'John', 6108623, 'employee');

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `user_id` int(11) NOT NULL,
  `user_name` varchar(255) NOT NULL,
  `privilege` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `attendance_checks`
--
ALTER TABLE `attendance_checks`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `attendance_logs`
--
ALTER TABLE `attendance_logs`
  ADD KEY `ix_attendance_logs_index` (`index`);

--
-- Indexes for table `employees`
--
ALTER TABLE `employees`
  ADD KEY `ix_employees_index` (`index`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`user_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `attendance_checks`
--
ALTER TABLE `attendance_checks`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `user_id` int(11) NOT NULL AUTO_INCREMENT;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;