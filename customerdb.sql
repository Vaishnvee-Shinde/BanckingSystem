-- phpMyAdmin SQL Dump
-- version 5.0.3
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Apr 29, 2021 at 07:26 PM
-- Server version: 10.4.14-MariaDB
-- PHP Version: 7.4.11

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `qxp`
--

-- --------------------------------------------------------

--
-- Table structure for table `customer`
--

CREATE TABLE `customer` (
  `UserID` int(11) NOT NULL,
  `Name` varchar(11) NOT NULL,
  `Email` varchar(25) NOT NULL,
  `Acc_Number` int(25) NOT NULL,
  `IFSC` varchar(20) NOT NULL,
  `Balance` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `customer`
--

INSERT INTO `customer` (`UserID`, `Name`, `Email`, `Acc_Number`, `IFSC`, `Balance`) VALUES
(446516, 'Jimmy', 'jimmy@gmail.com', 1431221, 'WWQ9551562', 17780),
(251262, 'Chloe', 'chloeroy@gmail.com', 2421522, 'AS18485151', 3155),
(132456, 'Aswin', 'ps.aswin@yahoo.com', 3421312, 'SA1651466SD', 10395),
(652841, 'Juno', 'junos@outlook.com', 6213123, 'SD1231232X', 10345),
(815626, 'Shahkeeb', 'shahke@gmial.com', 8923222, 'AS565656S', 4325);

-- --------------------------------------------------------

--
-- Table structure for table `transfer`
--

CREATE TABLE `transfer` (
  `s_name` varchar(10) NOT NULL,
  `s_acc_no` int(11) NOT NULL,
  `r_name` varchar(10) NOT NULL,
  `r_acc_no` int(11) NOT NULL,
  `amount` int(11) NOT NULL,
  `date_time` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `transfer`
--

INSERT INTO `transfer` (`s_name`, `s_acc_no`, `r_name`, `r_acc_no`, `amount`, `date_time`) VALUES
('Abhiram', 1431221, 'Mark', 2421522, 500, '2021-04-29 05:57:59'),
('Aswin', 3421312, 'Prashant', 6213123, 325, '2021-04-29 05:58:20'),
('Mark', 2421522, 'Adarsh', 8923222, 325, '2021-04-29 05:58:35'),
('Adarsh', 8923222, 'Abhiram', 1431221, 5000, '2021-04-29 05:58:48'),
('Mark', 2421522, 'Prashant', 6213123, 5020, '2021-04-29 05:59:05'),
('Abhiram', 1431221, 'Aswin', 3421312, 7543, '2021-04-29 06:00:14'),
('Jimmy', 1431221, 'Aswin', 3421312, 123, '2021-04-29 14:22:41'),
('Jimmy', 1431221, 'Aswin', 3421312, 333, '2021-04-29 15:04:54'),
('Jimmy', 1431221, 'Aswin', 3421312, 1221, '2021-04-29 16:23:36'),
('Aswin', 3421312, 'Jimmy', 1431221, 4000, '2021-04-29 16:24:15'),
('Juno', 6213123, 'Jimmy', 1431221, 10000, '2021-04-29 17:00:48');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `customer`
--
ALTER TABLE `customer`
  ADD PRIMARY KEY (`Acc_Number`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
