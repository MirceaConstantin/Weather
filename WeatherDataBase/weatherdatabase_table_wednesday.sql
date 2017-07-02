
-- --------------------------------------------------------

--
-- Table structure for table `wednesday`
--

CREATE TABLE `wednesday` (
  `TEMPERATURE` int(3) NOT NULL,
  `HUMIDITY` int(3) NOT NULL,
  `DATA` text NOT NULL,
  `DAY` text NOT NULL,
  `SUNRISE` text NOT NULL,
  `SUNTSET` text NOT NULL,
  `WEATHER` text NOT NULL,
  `MAX TEMPERATURE` int(3) NOT NULL,
  `MIN TEMPERATURE` int(3) NOT NULL,
  `WIND DIRECTION` text NOT NULL,
  `WIND SPEED` int(3) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
