-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Lis 16, 2024 at 01:14 AM
-- Wersja serwera: 10.4.32-MariaDB
-- Wersja PHP: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `econsultationdb`
--

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `consult`
--

CREATE TABLE `consult` (
  `ID` int(11) NOT NULL,
  `ID_teachers` int(11) DEFAULT NULL,
  `ID_users` int(11) DEFAULT NULL,
  `Title` varchar(255) DEFAULT NULL,
  `Description` varchar(255) DEFAULT NULL,
  `C_Date` date DEFAULT NULL,
  `ID_stamp` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `days`
--

CREATE TABLE `days` (
  `ID` int(11) NOT NULL,
  `Day` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `days`
--

INSERT INTO `days` (`ID`, `Day`) VALUES
(1, 'Monday'),
(2, 'Tuesday'),
(3, 'Wednesday'),
(4, 'Thursday'),
(5, 'Friday'),
(6, 'Saturday'),
(7, 'Sunday');

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `teachers`
--

CREATE TABLE `teachers` (
  `ID` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `teachers_days_time`
--

CREATE TABLE `teachers_days_time` (
  `ID_teachers` int(11) NOT NULL,
  `ID_days` int(11) NOT NULL,
  `ID_time` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `time_stamps`
--

CREATE TABLE `time_stamps` (
  `ID` int(11) NOT NULL,
  `Stamp` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `time_stamps`
--

INSERT INTO `time_stamps` (`ID`, `Stamp`) VALUES
(1, '8:30 - 9:15'),
(2, '9:15 - 10:00'),
(3, '10:15 - 11:00'),
(4, '11:00 - 11:45'),
(5, '12:00 - 12:45'),
(6, '12:45 - 13:30'),
(7, '14:00 - 14:45'),
(8, '14:45 - 15:30'),
(9, '16:00 - 16:45'),
(10, '16:45 - 17:30'),
(11, '17:40 - 18:25'),
(12, '18:25 - 19:10'),
(13, '19:20 - 20:05'),
(14, '20:05 - 20:50');

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `users`
--

CREATE TABLE `users` (
  `ID` int(11) NOT NULL,
  `LastName` varchar(255) DEFAULT NULL,
  `FirstName` varchar(255) DEFAULT NULL,
  `Login` varchar(255) DEFAULT NULL,
  `Password` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Indeksy dla zrzutów tabel
--

--
-- Indeksy dla tabeli `consult`
--
ALTER TABLE `consult`
  ADD PRIMARY KEY (`ID`),
  ADD KEY `ID_teachers` (`ID_teachers`),
  ADD KEY `ID_users` (`ID_users`),
  ADD KEY `ID_stamp` (`ID_stamp`);

--
-- Indeksy dla tabeli `days`
--
ALTER TABLE `days`
  ADD PRIMARY KEY (`ID`);

--
-- Indeksy dla tabeli `teachers`
--
ALTER TABLE `teachers`
  ADD KEY `ID` (`ID`);

--
-- Indeksy dla tabeli `teachers_days_time`
--
ALTER TABLE `teachers_days_time`
  ADD KEY `ID_teachers` (`ID_teachers`),
  ADD KEY `ID_days` (`ID_days`),
  ADD KEY `ID_time` (`ID_time`);

--
-- Indeksy dla tabeli `time_stamps`
--
ALTER TABLE `time_stamps`
  ADD PRIMARY KEY (`ID`);

--
-- Indeksy dla tabeli `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`ID`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `consult`
--
ALTER TABLE `consult`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `days`
--
ALTER TABLE `days`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT for table `time_stamps`
--
ALTER TABLE `time_stamps`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=15;

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `consult`
--
ALTER TABLE `consult`
  ADD CONSTRAINT `consult_ibfk_1` FOREIGN KEY (`ID_teachers`) REFERENCES `teachers` (`ID`),
  ADD CONSTRAINT `consult_ibfk_2` FOREIGN KEY (`ID_users`) REFERENCES `users` (`ID`),
  ADD CONSTRAINT `consult_ibfk_3` FOREIGN KEY (`ID_stamp`) REFERENCES `time_stamps` (`ID`);

--
-- Constraints for table `teachers`
--
ALTER TABLE `teachers`
  ADD CONSTRAINT `teachers_ibfk_1` FOREIGN KEY (`ID`) REFERENCES `users` (`ID`);

--
-- Constraints for table `teachers_days_time`
--
ALTER TABLE `teachers_days_time`
  ADD CONSTRAINT `teachers_days_time_ibfk_1` FOREIGN KEY (`ID_teachers`) REFERENCES `teachers` (`ID`),
  ADD CONSTRAINT `teachers_days_time_ibfk_2` FOREIGN KEY (`ID_days`) REFERENCES `days` (`ID`),
  ADD CONSTRAINT `teachers_days_time_ibfk_3` FOREIGN KEY (`ID_time`) REFERENCES `time_stamps` (`ID`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
