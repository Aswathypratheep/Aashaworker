-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: May 10, 2022 at 06:32 PM
-- Server version: 10.4.21-MariaDB
-- PHP Version: 8.0.11

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `babycare`
--

-- --------------------------------------------------------

--
-- Table structure for table `booking`
--

CREATE TABLE `booking` (
  `bkid` int(11) NOT NULL,
  `doctor_id` int(11) DEFAULT NULL,
  `mother_id` int(11) DEFAULT NULL,
  `booking_date` date DEFAULT NULL,
  `desc` varchar(200) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `booking`
--

INSERT INTO `booking` (`bkid`, `doctor_id`, `mother_id`, `booking_date`, `desc`) VALUES
(1, 6, 8, '2022-05-11', 'hsahj');

-- --------------------------------------------------------

--
-- Table structure for table `disease`
--

CREATE TABLE `disease` (
  `disease_id` int(100) NOT NULL,
  `wrkr_id` int(100) DEFAULT NULL,
  `doc_id` int(100) DEFAULT NULL,
  `details` varchar(200) DEFAULT NULL,
  `posted_date` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `disease`
--

INSERT INTO `disease` (`disease_id`, `wrkr_id`, `doc_id`, `details`, `posted_date`) VALUES
(1, 2, 1, 'Expert in baby care', '2019-12-12'),
(2, 3, 4, 'sfdgtrfg', '2020-02-28'),
(3, 6, 6, 'jncakjcjha', '2022-04-10');

-- --------------------------------------------------------

--
-- Table structure for table `doctor`
--

CREATE TABLE `doctor` (
  `doctor_id` int(100) NOT NULL,
  `district` varchar(50) DEFAULT NULL,
  `panchayath` varchar(50) DEFAULT NULL,
  `dname` varchar(50) DEFAULT NULL,
  `qualification` varchar(50) DEFAULT NULL,
  `address` varchar(100) DEFAULT NULL,
  `phone_no` varchar(10) DEFAULT NULL,
  `optime` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `doctor`
--

INSERT INTO `doctor` (`doctor_id`, `district`, `panchayath`, `dname`, `qualification`, `address`, `phone_no`, `optime`) VALUES
(1, 'Ernakulam', 'Karumalloor', 'Dr Manu', 'MBBS', 'Aluva', '9947394641', '15:25'),
(2, 'Ernakulam', 'Alangad', 'Dr Dilsha', 'MBBS MD', 'oolampara', '9947394641', '11:47'),
(3, 'Ernakulam', 'Karumalloor', 'Anu', 'MBBS', 'Aluva', '7845847454', '03:03'),
(4, 'Ernakulam', 'Kunnumpuram', 'Ramachandran', 'kadjn', 'ksdfj', '8891212022', '10:00'),
(5, 'Thrissur', 'chowannur', 'Sijo paul', 'MSC Medicine', 'Thrissur Road Taxi Stand, near Police Station, Kunnamkulam, Kerala 680503', '9876543210', '10:00'),
(6, 'Ernakulam', 'Pan', 'DOC Name', 'MD E', 'vvg', '9898989899', '15:30');

-- --------------------------------------------------------

--
-- Table structure for table `food`
--

CREATE TABLE `food` (
  `food_id` int(100) NOT NULL,
  `wrkr_id` int(100) DEFAULT NULL,
  `title` varchar(50) DEFAULT NULL,
  `details` varchar(100) DEFAULT NULL,
  `posted_date` date DEFAULT NULL,
  `status` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `food`
--

INSERT INTO `food` (`food_id`, `wrkr_id`, `title`, `details`, `posted_date`, `status`) VALUES
(1, 2, 'Nutrition Food', 'mango\r\nwatermelon', '2019-12-12', '1'),
(2, 6, 'x saj', 'bjhcbajh', '2022-04-10', '1');

-- --------------------------------------------------------

--
-- Table structure for table `health_tips`
--

CREATE TABLE `health_tips` (
  `tipid` int(100) NOT NULL,
  `wrkr_id` int(100) DEFAULT NULL,
  `age_grp` varchar(50) DEFAULT NULL,
  `tips` varchar(100) DEFAULT NULL,
  `posted_date` date DEFAULT NULL,
  `status` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `health_tips`
--

INSERT INTO `health_tips` (`tipid`, `wrkr_id`, `age_grp`, `tips`, `posted_date`, `status`) VALUES
(1, 2, 'upto 3 months babys', 'nutristion food', '2019-12-12', '1'),
(2, 2, '6 months', 'qwerty', '2019-12-12', '1'),
(3, 6, '1 12', 'kjacnskj', '2022-04-10', '1'),
(4, 6, '1-10', 'jnbhkj\r\n', '2022-04-10', '1');

-- --------------------------------------------------------

--
-- Table structure for table `login`
--

CREATE TABLE `login` (
  `logid` int(100) NOT NULL,
  `userid` int(100) DEFAULT NULL,
  `username` varchar(100) DEFAULT NULL,
  `password` varchar(50) DEFAULT NULL,
  `status` varchar(10) DEFAULT NULL,
  `usertype` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `login`
--

INSERT INTO `login` (`logid`, `userid`, `username`, `password`, `status`, `usertype`) VALUES
(1, 0, 'admin', 'admin', '1', 'admin'),
(2, 2, '9947394641', 'worker5462', '1', 'worker'),
(3, 2, '9947394641', 'doctor6958', '1', 'doctor'),
(5, 3, '7845847454', 'doctor8640', '1', 'doctor'),
(6, 2, '9585478545', 'mother6176', '1', 'mother'),
(7, 3, '9541023678', 'worker6962', '1', 'worker'),
(8, 4, '8891212022', 'doctor3116', '1', 'doctor'),
(9, 3, '9562301478', 'mother3038', '1', 'mother'),
(10, 4, '9876543210', 'worker2360', '1', 'worker'),
(11, 5, '9876543210', 'doctor1954', '1', 'doctor'),
(12, 5, '9539464779', 'worker1904', '1', 'worker'),
(16, 6, '9898989898', '9898989898', '1', 'worker'),
(17, 6, '9898989899', '9898989899', '1', 'doctor'),
(18, 7, '9090909090', '9090909090', '1', 'mother'),
(19, 8, '7878787878', '7878787878', '1', 'mother');

-- --------------------------------------------------------

--
-- Table structure for table `mother_reg`
--

CREATE TABLE `mother_reg` (
  `mother_id` int(100) NOT NULL,
  `wrker_id` int(100) DEFAULT NULL,
  `mother_name` varchar(50) DEFAULT NULL,
  `age` varchar(20) DEFAULT NULL,
  `address` varchar(100) DEFAULT NULL,
  `district` varchar(50) DEFAULT NULL,
  `panchayath` varchar(50) DEFAULT NULL,
  `ward_no` varchar(50) DEFAULT NULL,
  `pstatus` varchar(20) DEFAULT NULL,
  `month_count` varchar(10) DEFAULT NULL,
  `delivery_date` date DEFAULT NULL,
  `phone_number` varchar(10) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `mother_reg`
--

INSERT INTO `mother_reg` (`mother_id`, `wrker_id`, `mother_name`, `age`, `address`, `district`, `panchayath`, `ward_no`, `pstatus`, `month_count`, `delivery_date`, `phone_number`) VALUES
(2, 2, 'Ghy', '23', 'ty', 'Ernakulam', 'Karumalloor', '10', 'carrying', '8', '2019-12-29', '9585478545'),
(3, 3, 'Baby', '25', 'adjfhbk', 'Ernakulam', 'Kunnumpuram', '2', 'carrying', '8', '2020-03-27', '9562301478'),
(4, 4, 'saranya', '28', 'kallazhikunnu Nr post office House No 216', 'Thrissur', 'chowannur', '12', 'carrying', '9', '2022-01-29', '9876543210'),
(7, 6, 'Anju', '23', 'Aj\r\nAdrs', 'Ernakulam', 'Pan', '1', 'carrying', '9', '2022-04-29', '9090909090'),
(8, 6, 'Mot', '22', 'Mot \r\nAdrs', 'Ernakulam', 'Pan', '1', NULL, NULL, NULL, '7878787878');

-- --------------------------------------------------------

--
-- Table structure for table `panchayath_reg`
--

CREATE TABLE `panchayath_reg` (
  `panchayath_id` int(100) NOT NULL,
  `name` varchar(50) DEFAULT NULL,
  `district` varchar(25) DEFAULT NULL,
  `ward_count` varchar(20) DEFAULT NULL,
  `house_count` varchar(20) DEFAULT NULL,
  `president_name` varchar(25) DEFAULT NULL,
  `address` varchar(100) DEFAULT NULL,
  `email` varchar(50) DEFAULT NULL,
  `phone_number` varchar(10) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `panchayath_reg`
--

INSERT INTO `panchayath_reg` (`panchayath_id`, `name`, `district`, `ward_count`, `house_count`, `president_name`, `address`, `email`, `phone_number`) VALUES
(1, 'Alangad', 'Ernakulam', '231', '203', 'Megha', 'Alanagad po aluva', 'alangad@gmail.com', '9565478545'),
(2, 'Karumalloor', 'Ernakulam', '100', '3000', 'amritha', 'hgjkhkhk\r\noippppu', 'ammu1@gmail.com', '4534565'),
(3, 'Aluva', 'Ernakulam', '25', '4500', 'Sherin', 'Aluva', 'aluva@gmail.com', '9652301478'),
(4, 'Kunnumpuram', 'Ernakulam', '152', '4500', 'Arya', 'KLJNsda', 'kunnumpuram@gmail.com', '9623015478'),
(5, 'chowannur', 'Thrissur', '17', '345', 'Bindhu', 'Chowannur, Narimada Road, Kunnamkulam, Kerala 680107', 'chowannur@gmail.com', '9876543210'),
(6, 'Pan', 'Ernakulam', '21', '10000', 'Aji', 'Pan\r\nAdrs', 'pan@mail.com', '9090909090');

-- --------------------------------------------------------

--
-- Table structure for table `projects`
--

CREATE TABLE `projects` (
  `project_id` int(100) NOT NULL,
  `district` varchar(50) DEFAULT NULL,
  `panchayath` varchar(50) DEFAULT NULL,
  `title` varchar(100) DEFAULT NULL,
  `details` varchar(200) DEFAULT NULL,
  `posted_date` date DEFAULT NULL,
  `valid_upto` date DEFAULT NULL,
  `status` varchar(10) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `projects`
--

INSERT INTO `projects` (`project_id`, `district`, `panchayath`, `title`, `details`, `posted_date`, `valid_upto`, `status`) VALUES
(2, 'Ernakulam', 'Karumalloor', 'Meetings On Comming Monday', 'dont miss out', '2019-12-10', '2019-12-11', '1'),
(3, 'Ernakulam', 'Kunnumpuram', 'Baby Protect', 'arg', '2020-02-28', '2020-03-02', '1'),
(5, 'Thrissur', 'chowannur', 'pradhana manthiri', 'PMMVY, a maternity benefit programme is being run by the department since 01/01/2017.  The scheme is implementing in Kerala using the platform of Ankanawadi Services of Umbrella ICDS. The scheme is im', '2022-01-20', '2022-01-30', '1'),
(6, 'Thrissur', 'chowannur', 'jhujg', 'h', '2022-01-20', '2022-01-23', '1'),
(7, 'Ernakulam', 'Pan', 'KLLK', 'kjxsjhbj\r\nxksnxjka', '2022-04-10', '2022-04-20', '1');

-- --------------------------------------------------------

--
-- Table structure for table `vaccination`
--

CREATE TABLE `vaccination` (
  `vac_id` int(100) NOT NULL,
  `wrkr_id` int(100) DEFAULT NULL,
  `vac_name` varchar(50) DEFAULT NULL,
  `details` varchar(100) DEFAULT NULL,
  `time` varchar(50) DEFAULT NULL,
  `posted_date` date DEFAULT NULL,
  `vaccination_date` date DEFAULT NULL,
  `location` varchar(50) DEFAULT NULL,
  `status` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `vaccination`
--

INSERT INTO `vaccination` (`vac_id`, `wrkr_id`, `vac_name`, `details`, `time`, `posted_date`, `vaccination_date`, `location`, `status`) VALUES
(1, 2, 'Polio', 'its for the babys who are in 3 months', '23:02', '2019-12-11', '2019-12-20', 'panchayath office', '1'),
(2, 4, 'Covaxin', 'Lorem Ipsum is simply ', '09:00', '2022-01-20', '2022-01-30', 'GOV Hospital', '1'),
(3, 6, 'Covaxin', 'mnbjh', '10:10', '2022-04-10', '2022-04-11', 'GOV Hospital', '1');

-- --------------------------------------------------------

--
-- Table structure for table `worker_reg`
--

CREATE TABLE `worker_reg` (
  `wrkr_id` int(100) NOT NULL,
  `district` varchar(50) DEFAULT NULL,
  `panchayath` varchar(50) DEFAULT NULL,
  `worker_name` varchar(50) DEFAULT NULL,
  `phone_no` varchar(10) DEFAULT NULL,
  `ward_no` varchar(20) DEFAULT NULL,
  `address` varchar(100) DEFAULT NULL,
  `email` varchar(50) DEFAULT NULL,
  `qualification` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `worker_reg`
--

INSERT INTO `worker_reg` (`wrkr_id`, `district`, `panchayath`, `worker_name`, `phone_no`, `ward_no`, `address`, `email`, `qualification`) VALUES
(1, 'Ernakulam', 'Alangad', 'Megha', '9654854754', '12', 'aluva', 'megha@gmail.com', 'MCA'),
(2, 'Ernakulam', 'Karumalloor', 'meenu', '9947394641', '10', 'hgjkhkhk\r\noippppu', 'meenu@gmail.com', 'Bcom'),
(3, 'Ernakulam', 'Kunnumpuram', 'Anjana', '9541023678', '2', 'dertgh', 'anjana@gmail.com', 'BSc'),
(4, 'Thrissur', 'chowannur', 'Bindhu', '9876543210', '12', ' Chowwannur part, Kerala 680517, House No Ak47', 'bindhu@gmail.com', 'SSLC'),
(5, 'Thrissur', 'chowannur', 'vishnu', '9539464779', '29', 'guruvayur', 'v@gmail.com', 'SSLC'),
(6, 'Ernakulam', 'Pan', 'BKY', '9898989898', '1', 'BK \r\nAdrs', 'bk@mail.com', 'MA English');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `booking`
--
ALTER TABLE `booking`
  ADD PRIMARY KEY (`bkid`);

--
-- Indexes for table `disease`
--
ALTER TABLE `disease`
  ADD PRIMARY KEY (`disease_id`);

--
-- Indexes for table `doctor`
--
ALTER TABLE `doctor`
  ADD PRIMARY KEY (`doctor_id`);

--
-- Indexes for table `food`
--
ALTER TABLE `food`
  ADD PRIMARY KEY (`food_id`);

--
-- Indexes for table `health_tips`
--
ALTER TABLE `health_tips`
  ADD PRIMARY KEY (`tipid`);

--
-- Indexes for table `login`
--
ALTER TABLE `login`
  ADD PRIMARY KEY (`logid`);

--
-- Indexes for table `mother_reg`
--
ALTER TABLE `mother_reg`
  ADD PRIMARY KEY (`mother_id`);

--
-- Indexes for table `panchayath_reg`
--
ALTER TABLE `panchayath_reg`
  ADD PRIMARY KEY (`panchayath_id`);

--
-- Indexes for table `projects`
--
ALTER TABLE `projects`
  ADD PRIMARY KEY (`project_id`);

--
-- Indexes for table `vaccination`
--
ALTER TABLE `vaccination`
  ADD PRIMARY KEY (`vac_id`);

--
-- Indexes for table `worker_reg`
--
ALTER TABLE `worker_reg`
  ADD PRIMARY KEY (`wrkr_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `booking`
--
ALTER TABLE `booking`
  MODIFY `bkid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `disease`
--
ALTER TABLE `disease`
  MODIFY `disease_id` int(100) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `doctor`
--
ALTER TABLE `doctor`
  MODIFY `doctor_id` int(100) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `food`
--
ALTER TABLE `food`
  MODIFY `food_id` int(100) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `health_tips`
--
ALTER TABLE `health_tips`
  MODIFY `tipid` int(100) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `login`
--
ALTER TABLE `login`
  MODIFY `logid` int(100) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=20;

--
-- AUTO_INCREMENT for table `mother_reg`
--
ALTER TABLE `mother_reg`
  MODIFY `mother_id` int(100) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT for table `panchayath_reg`
--
ALTER TABLE `panchayath_reg`
  MODIFY `panchayath_id` int(100) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `projects`
--
ALTER TABLE `projects`
  MODIFY `project_id` int(100) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT for table `vaccination`
--
ALTER TABLE `vaccination`
  MODIFY `vac_id` int(100) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `worker_reg`
--
ALTER TABLE `worker_reg`
  MODIFY `wrkr_id` int(100) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
