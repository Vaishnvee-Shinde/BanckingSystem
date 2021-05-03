-- phpMyAdmin SQL Dump
-- version 5.0.4
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: May 03, 2021 at 08:29 AM
-- Server version: 10.4.17-MariaDB
-- PHP Version: 8.0.0

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
(448966, 'Vrusha', 'Veushali22@gmail.com', 14398, 'ASQ9981562', 13900),
(346578, 'Aradhya', 'Aradhyac@gmail.com', 223367, 'AS189231', 40800),
(346569, 'Zeba', 'zebarow@gmail.com', 224456, 'AS189754V', 91000),
(9045864, 'Kartik', 'kartik990@gmail.com', 349456, 'AC3475370D', 86100),
(9045236, 'Sanju', 's.sanju@gmail.com', 349756, 'AC3465890D', 91000),
(446516, 'Vaishnvee', 'vaishnvee169@gmail.com', 1431221, 'WWQ9551562', 8000),
(841652, 'Arjun', 'Arjun124@outlook.com', 3162123, 'SD9856785X', 903450),
(876815, 'Rahi', 'Rahi45v@gmial.com', 3294892, 'AS576457S', 34400),
(847543, 'Arjuna', 'j.Arjuna@outlook.com', 8962123, 'SD985675Y', 89800),
(87653, 'Abhishek', 'dev.abhishek@yahoo.com', 9569876, 'SA875436SD', 74360);

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
('Arjuna', 8962123, 'Rahi', 3294892, 200, '2021-05-02 09:40:57'),
('Abhishek', 9569876, 'Aradhya', 223367, 10000, '2021-05-02 09:53:43'),
('Abhishek', 9569876, 'Rahi', 3294892, 200, '2021-05-02 09:53:59'),
('Vaishnvee', 1431221, 'Zeba', 224456, 2000, '2021-05-02 09:58:39'),
('Vrusha', 14398, 'Kartik', 349456, 100, '2021-05-02 10:19:48'),
('Rahi', 3294892, 'Vrusha', 14398, 10000, '2021-05-02 10:23:12'),
('Vrusha', 14398, 'Sanju', 349756, 1000, '2021-05-02 10:24:29'),
('Kartik', 349456, 'Rahi', 3294892, 4000, '2021-05-02 10:31:01'),
('Vrusha', 14398, 'Abhishek', 9569876, 5000, '2021-05-03 05:36:51');

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
