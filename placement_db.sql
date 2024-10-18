-- phpMyAdmin SQL Dump
-- version 5.1.3
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: May 23, 2022 at 03:48 PM
-- Server version: 10.4.24-MariaDB
-- PHP Version: 7.4.28

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `placement_db`
--

-- --------------------------------------------------------

--
-- Table structure for table `admindata`
--

CREATE TABLE `admindata` (
  `id` int(11) NOT NULL,
  `Username` varchar(100) NOT NULL,
  `Password` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `admindata`
--

INSERT INTO `admindata` (`id`, `Username`, `Password`) VALUES
(1, 'admin', '123');

-- --------------------------------------------------------

--
-- Table structure for table `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL,
  `name` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can view log entry', 1, 'view_logentry'),
(5, 'Can add permission', 2, 'add_permission'),
(6, 'Can change permission', 2, 'change_permission'),
(7, 'Can delete permission', 2, 'delete_permission'),
(8, 'Can view permission', 2, 'view_permission'),
(9, 'Can add group', 3, 'add_group'),
(10, 'Can change group', 3, 'change_group'),
(11, 'Can delete group', 3, 'delete_group'),
(12, 'Can view group', 3, 'view_group'),
(13, 'Can add user', 4, 'add_user'),
(14, 'Can change user', 4, 'change_user'),
(15, 'Can delete user', 4, 'delete_user'),
(16, 'Can view user', 4, 'view_user'),
(17, 'Can add content type', 5, 'add_contenttype'),
(18, 'Can change content type', 5, 'change_contenttype'),
(19, 'Can delete content type', 5, 'delete_contenttype'),
(20, 'Can view content type', 5, 'view_contenttype'),
(21, 'Can add session', 6, 'add_session'),
(22, 'Can change session', 6, 'change_session'),
(23, 'Can delete session', 6, 'delete_session'),
(24, 'Can view session', 6, 'view_session'),
(25, 'Can add admindata', 7, 'add_admindata'),
(26, 'Can change admindata', 7, 'change_admindata'),
(27, 'Can delete admindata', 7, 'delete_admindata'),
(28, 'Can view admindata', 7, 'view_admindata'),
(29, 'Can add company details', 8, 'add_companydetails'),
(30, 'Can change company details', 8, 'change_companydetails'),
(31, 'Can delete company details', 8, 'delete_companydetails'),
(32, 'Can view company details', 8, 'view_companydetails'),
(33, 'Can add student_ details', 9, 'add_student_details'),
(34, 'Can change student_ details', 9, 'change_student_details'),
(35, 'Can delete student_ details', 9, 'delete_student_details'),
(36, 'Can view student_ details', 9, 'view_student_details'),
(37, 'Can add student_status', 10, 'add_student_status'),
(38, 'Can change student_status', 10, 'change_student_status'),
(39, 'Can delete student_status', 10, 'delete_student_status'),
(40, 'Can view student_status', 10, 'view_student_status'),
(41, 'Can add all_ information', 11, 'add_all_information'),
(42, 'Can change all_ information', 11, 'change_all_information'),
(43, 'Can delete all_ information', 11, 'delete_all_information'),
(44, 'Can view all_ information', 11, 'view_all_information'),
(45, 'Can add college login', 12, 'add_collegelogin'),
(46, 'Can change college login', 12, 'change_collegelogin'),
(47, 'Can delete college login', 12, 'delete_collegelogin'),
(48, 'Can view college login', 12, 'view_collegelogin'),
(49, 'Can add off campus placed', 13, 'add_offcampusplaced'),
(50, 'Can change off campus placed', 13, 'change_offcampusplaced'),
(51, 'Can delete off campus placed', 13, 'delete_offcampusplaced'),
(52, 'Can view off campus placed', 13, 'view_offcampusplaced');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user`
--

CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_groups`
--

CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_user_permissions`
--

CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `collegelogin`
--

CREATE TABLE `collegelogin` (
  `id` int(11) NOT NULL,
  `username` varchar(100) NOT NULL,
  `password` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `collegelogin`
--

INSERT INTO `collegelogin` (`id`, `username`, `password`) VALUES
(1, 'college', '123');

-- --------------------------------------------------------

--
-- Table structure for table `companydetails`
--

CREATE TABLE `companydetails` (
  `id` int(11) NOT NULL,
  `CompanyName` varchar(100) NOT NULL,
  `Package` varchar(100) NOT NULL,
  `File` varchar(100) NOT NULL,
  `Pre_Placement` datetime(6) NOT NULL,
  `Test_Date` datetime(6) NOT NULL,
  `Interview_Date` datetime(6) NOT NULL,
  `Additional_Information` varchar(100) NOT NULL,
  `CGPA` varchar(100) NOT NULL,
  `CSl` varchar(100) DEFAULT NULL,
  `IS` varchar(100) DEFAULT NULL,
  `ECE` varchar(100) DEFAULT NULL,
  `EEE` varchar(100) DEFAULT NULL,
  `MECH` varchar(100) DEFAULT NULL,
  `IP` varchar(100) DEFAULT NULL,
  `CIVIL` varchar(100) DEFAULT NULL,
  `ALL_BRANCHES` varchar(100) DEFAULT NULL,
  `OTHERS` varchar(100) DEFAULT NULL,
  `CATEGORY` varchar(100) DEFAULT NULL,
  `Pre_Placement_month` varchar(100) NOT NULL,
  `Test_Date_month` varchar(100) NOT NULL,
  `Interview_Date_month` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `companydetails`
--

INSERT INTO `companydetails` (`id`, `CompanyName`, `Package`, `File`, `Pre_Placement`, `Test_Date`, `Interview_Date`, `Additional_Information`, `CGPA`, `CSl`, `IS`, `ECE`, `EEE`, `MECH`, `IP`, `CIVIL`, `ALL_BRANCHES`, `OTHERS`, `CATEGORY`, `Pre_Placement_month`, `Test_Date_month`, `Interview_Date_month`) VALUES
(1, 'TCS', '7.8', 'media/Resume.pdf', '2022-05-13 00:00:00.000000', '2022-09-13 00:00:00.000000', '2022-05-13 00:00:00.000000', 'okay', '6.00', 'CSl', 'IS', 'Null', 'Null', 'Null', 'Null', 'Null', 'Null', 'arts', 'MASS', '5', '9', '5'),
(2, 'KPMG', '7.8', 'media/Resume_JPpQYza.pdf', '2022-05-11 00:00:00.000000', '2022-05-21 00:00:00.000000', '2022-06-15 00:00:00.000000', 'okay', '6.00', 'Null', 'Null', 'Null', 'Null', 'Null', 'Null', 'Null', 'Null', '', 'MASS', '5', '5', '6'),
(3, 'Nevon', '6', 'media/Resume.docx', '2022-05-01 00:00:00.000000', '2022-05-20 00:00:00.000000', '2022-07-08 00:00:00.000000', 'Software company providing services based on python android flutter .net ', '2', 'Null', 'Null', 'Null', 'Null', 'Null', 'Null', 'CIVIL', 'Null', '', 'DREAM', '5', '5', '7'),
(4, 'Pi Techniques', '7.00', 'media/Resume_1czVVrL.docx', '2022-06-02 00:00:00.000000', '2022-06-16 00:00:00.000000', '2022-07-08 00:00:00.000000', 'Private Limited', '7.5', 'Null', 'Null', 'Null', 'Null', 'MECH', 'Null', 'Null', 'Null', '', 'MASS', '6', '6', '7'),
(5, 'Amazon', '9.00', 'media/Resume_xBGKbaO.docx', '2022-05-11 00:00:00.000000', '2022-05-13 00:00:00.000000', '2022-05-16 00:00:00.000000', 'You know who we are', '7.00', 'CSl', 'Null', 'Null', 'Null', 'Null', 'Null', 'Null', 'Null', '', 'DREAM', '5', '5', '5'),
(6, 'Sankey Solutions', '6.00', 'media/Resume_WawNdTP.docx', '2022-07-04 00:00:00.000000', '2022-07-08 00:00:00.000000', '2022-07-09 00:00:00.000000', 'Come work with us', '8.00', 'Null', 'Null', 'Null', 'EEE', 'Null', 'Null', 'Null', 'Null', '', 'MASS', '7', '7', '7'),
(7, 'Yahoo', '9', 'media/Resume_wqCxLfd.docx', '2022-07-28 00:00:00.000000', '2022-07-29 00:00:00.000000', '2022-07-31 00:00:00.000000', 'yahoo', '5', 'Null', 'Null', 'ECE', 'Null', 'Null', 'Null', 'Null', 'Null', '', 'CORE', '7', '7', '7'),
(8, 'Boss', '7.8', 'media/Resume_EeJj5oo.docx', '2022-05-25 00:00:00.000000', '2022-05-26 00:00:00.000000', '2022-05-27 00:00:00.000000', 'happy to work with smart minds', '6.00', 'Null', 'Null', 'ECE', 'Null', 'Null', 'Null', 'Null', 'Null', '', 'MASS', '5', '5', '5'),
(9, 'cello', '7.00', 'media/Resume_piZZJQT.docx', '2022-06-01 00:00:00.000000', '2022-06-02 00:00:00.000000', '2022-06-03 00:00:00.000000', 'yes', '9', 'Null', 'Null', 'ECE', 'Null', 'Null', 'Null', 'Null', 'Null', '', 'MASS', '6', '6', '6'),
(11, 'Asian Paints', '10', 'media/Resume_GICA2xg.docx', '2022-05-08 00:00:00.000000', '2022-05-09 00:00:00.000000', '2022-05-10 00:00:00.000000', 'yes paint', '8', 'Null', 'Null', 'Null', 'Null', 'Null', 'Null', 'Null', 'ALL_BRANCHES', '', 'MASS', '5', '5', '5'),
(13, 'Boss', '7.8', 'media/Resume_EeJj5oo.docx', '2022-05-25 00:00:00.000000', '2022-05-26 00:00:00.000000', '2022-05-27 00:00:00.000000', 'happy to work with smart minds', '6.00', 'Null', 'Null', 'ECE', 'Null', 'Null', 'Null', 'Null', 'Null', '', 'MASS', '5', '5', '5');

-- --------------------------------------------------------

--
-- Table structure for table `django_admin_log`
--

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext DEFAULT NULL,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL CHECK (`action_flag` >= 0),
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(7, 'AppCampusPlacement', 'admindata'),
(11, 'AppCampusPlacement', 'all_information'),
(12, 'AppCampusPlacement', 'collegelogin'),
(8, 'AppCampusPlacement', 'companydetails'),
(13, 'AppCampusPlacement', 'offcampusplaced'),
(9, 'AppCampusPlacement', 'student_details'),
(10, 'AppCampusPlacement', 'student_status'),
(3, 'auth', 'group'),
(2, 'auth', 'permission'),
(4, 'auth', 'user'),
(5, 'contenttypes', 'contenttype'),
(6, 'sessions', 'session');

-- --------------------------------------------------------

--
-- Table structure for table `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'AppCampusPlacement', '0001_initial', '2022-05-13 09:54:36.306796'),
(2, 'AppCampusPlacement', '0002_companydetails', '2022-05-13 09:54:36.338050'),
(3, 'AppCampusPlacement', '0003_auto_20220510_1837', '2022-05-13 09:54:36.338050'),
(4, 'contenttypes', '0001_initial', '2022-05-13 09:54:36.385917'),
(5, 'auth', '0001_initial', '2022-05-13 09:54:36.800295'),
(6, 'admin', '0001_initial', '2022-05-13 09:54:36.894573'),
(7, 'admin', '0002_logentry_remove_auto_add', '2022-05-13 09:54:36.894573'),
(8, 'admin', '0003_logentry_add_action_flag_choices', '2022-05-13 09:54:36.910203'),
(9, 'contenttypes', '0002_remove_content_type_name', '2022-05-13 09:54:36.957076'),
(10, 'auth', '0002_alter_permission_name_max_length', '2022-05-13 09:54:36.988709'),
(11, 'auth', '0003_alter_user_email_max_length', '2022-05-13 09:54:37.004338'),
(12, 'auth', '0004_alter_user_username_opts', '2022-05-13 09:54:37.019962'),
(13, 'auth', '0005_alter_user_last_login_null', '2022-05-13 09:54:37.051208'),
(14, 'auth', '0006_require_contenttypes_0002', '2022-05-13 09:54:37.051208'),
(15, 'auth', '0007_alter_validators_add_error_messages', '2022-05-13 09:54:37.066842'),
(16, 'auth', '0008_alter_user_username_max_length', '2022-05-13 09:54:37.066842'),
(17, 'auth', '0009_alter_user_last_name_max_length', '2022-05-13 09:54:37.086981'),
(18, 'auth', '0010_alter_group_name_max_length', '2022-05-13 09:54:37.098903'),
(19, 'auth', '0011_update_proxy_permissions', '2022-05-13 09:54:37.114533'),
(20, 'auth', '0012_alter_user_first_name_max_length', '2022-05-13 09:54:37.130157'),
(21, 'sessions', '0001_initial', '2022-05-13 09:54:37.177025'),
(22, 'AppCampusPlacement', '0004_student_details', '2022-05-14 07:51:23.024137'),
(23, 'AppCampusPlacement', '0005_student_status', '2022-05-14 10:14:58.418882'),
(24, 'AppCampusPlacement', '0006_all_information', '2022-05-14 11:54:15.432682'),
(25, 'AppCampusPlacement', '0007_auto_20220516_1312', '2022-05-16 07:42:52.892182'),
(26, 'AppCampusPlacement', '0008_auto_20220517_1701', '2022-05-17 11:31:42.203760'),
(27, 'AppCampusPlacement', '0009_collegelogin', '2022-05-18 07:10:50.761151'),
(28, 'AppCampusPlacement', '0010_alter_companydetails_test_date', '2022-05-18 11:22:17.577933'),
(29, 'AppCampusPlacement', '0011_auto_20220518_1710', '2022-05-18 11:40:51.224608'),
(30, 'AppCampusPlacement', '0012_auto_20220519_1159', '2022-05-19 06:30:03.802003'),
(31, 'AppCampusPlacement', '0013_companydetails_interview_date_month', '2022-05-19 06:31:42.246484'),
(32, 'AppCampusPlacement', '0014_offcampusplaced', '2022-05-19 07:59:49.435609');

-- --------------------------------------------------------

--
-- Table structure for table `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('srcr50upzndc3kffci6rq4ivzde7zjfz', '.eJyrViqpLEiNz0xRslJyzs_JSU1PVdJRCi1OLQoBiqMI5uSnZ-YBRSJTi5VqARp7EoY:1nt0b9:QxM6Lsf7gTRpVxa6_xvSLBLWpAcRAcQf_hGyywEwPcI', '2022-06-06 05:27:19.542371');

-- --------------------------------------------------------

--
-- Table structure for table `offcampusplaced`
--

CREATE TABLE `offcampusplaced` (
  `id` int(11) NOT NULL,
  `USN` varchar(100) NOT NULL,
  `CompanyName` varchar(100) NOT NULL,
  `package` varchar(100) NOT NULL,
  `proof` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `offcampusplaced`
--

INSERT INTO `offcampusplaced` (`id`, `USN`, `CompanyName`, `package`, `proof`) VALUES
(1, '4NI18IS021', 'Dell', '6 Lakhs', 'Resume_FJf603a.pdf'),
(2, '4NI18IS022', 'TCL', '6', 'Resume_rJ3BhfK.pdf'),
(3, '4NI18IS023', 'a', '2', 'Resume_LLFD1dr.pdf'),
(4, '4NI18IS025', 'b', '5', 'Resume_ixqgtfZ.pdf');

-- --------------------------------------------------------

--
-- Table structure for table `student_details`
--

CREATE TABLE `student_details` (
  `id` int(11) NOT NULL,
  `Name` varchar(100) DEFAULT NULL,
  `USN` varchar(100) DEFAULT NULL,
  `Date_of_Birth` varchar(100) DEFAULT NULL,
  `Gender` varchar(100) DEFAULT NULL,
  `Category` varchar(100) DEFAULT NULL,
  `Mode_of_admission` varchar(100) DEFAULT NULL,
  `Engineering_branch` varchar(100) DEFAULT NULL,
  `Section` varchar(100) DEFAULT NULL,
  `Year_of_joining` varchar(100) DEFAULT NULL,
  `Year_of_passing` varchar(100) DEFAULT NULL,
  `first_sem_SGPA` varchar(100) DEFAULT NULL,
  `first_sem_percentage` varchar(100) DEFAULT NULL,
  `second_sem_SGPA` varchar(100) DEFAULT NULL,
  `second_sem_percentage` varchar(100) DEFAULT NULL,
  `third_sem_SGPA` varchar(100) DEFAULT NULL,
  `third_sem_percentage` varchar(100) DEFAULT NULL,
  `fourth_sem_SGPA` varchar(100) DEFAULT NULL,
  `fourth_sem_percentage` varchar(100) DEFAULT NULL,
  `fifth_sem_SGPA` varchar(100) DEFAULT NULL,
  `fifth_sem_percentage` varchar(100) DEFAULT NULL,
  `Total_CGPA` varchar(100) DEFAULT NULL,
  `TOTAL_CREDITS_EARNED_UPTO_5TH_SEMESTER` varchar(100) DEFAULT NULL,
  `NUMBER_OF_SUBJECTS_CLEARED_IN_MUTE` varchar(100) DEFAULT NULL,
  `CURRENT_ARREARS` varchar(100) DEFAULT NULL,
  `tenth_SSLC_percentage` varchar(100) DEFAULT NULL,
  `tenth_sslc_board` varchar(100) DEFAULT NULL,
  `Name_of_institution_studied_in_10th_sslc` varchar(100) DEFAULT NULL,
  `tenth_sslc_qualified_year` varchar(100) DEFAULT NULL,
  `twelveth_PUC_percentage` varchar(100) DEFAULT NULL,
  `twelveth_PUC_board` varchar(100) DEFAULT NULL,
  `Name_of_the_institution_studied_12th_Puc` varchar(100) DEFAULT NULL,
  `twelveth_PUC_qualified_year` varchar(100) DEFAULT NULL,
  `Diploma_percentage` varchar(100) DEFAULT NULL,
  `Diploma_CET_percentage` varchar(100) DEFAULT NULL,
  `Name_of_the_institution_studied_diploma` varchar(100) DEFAULT NULL,
  `Diploma_qualified_year` varchar(100) DEFAULT NULL,
  `contact_number` varchar(100) DEFAULT NULL,
  `LANDLINE_NUMBER` varchar(100) DEFAULT NULL,
  `PARENTS_NUMBER` varchar(100) DEFAULT NULL,
  `Alternate_contact_number` varchar(100) DEFAULT NULL,
  `EMAIL_ID` varchar(100) DEFAULT NULL,
  `College_mail` varchar(100) DEFAULT NULL,
  `CURRENT_ADDRESS` varchar(100) DEFAULT NULL,
  `PERMANENT_ADDRESS` varchar(100) DEFAULT NULL,
  `password` varchar(100) DEFAULT NULL,
  `uname` varchar(100) DEFAULT NULL,
  `Total_CGPA_per` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `student_details`
--

INSERT INTO `student_details` (`id`, `Name`, `USN`, `Date_of_Birth`, `Gender`, `Category`, `Mode_of_admission`, `Engineering_branch`, `Section`, `Year_of_joining`, `Year_of_passing`, `first_sem_SGPA`, `first_sem_percentage`, `second_sem_SGPA`, `second_sem_percentage`, `third_sem_SGPA`, `third_sem_percentage`, `fourth_sem_SGPA`, `fourth_sem_percentage`, `fifth_sem_SGPA`, `fifth_sem_percentage`, `Total_CGPA`, `TOTAL_CREDITS_EARNED_UPTO_5TH_SEMESTER`, `NUMBER_OF_SUBJECTS_CLEARED_IN_MUTE`, `CURRENT_ARREARS`, `tenth_SSLC_percentage`, `tenth_sslc_board`, `Name_of_institution_studied_in_10th_sslc`, `tenth_sslc_qualified_year`, `twelveth_PUC_percentage`, `twelveth_PUC_board`, `Name_of_the_institution_studied_12th_Puc`, `twelveth_PUC_qualified_year`, `Diploma_percentage`, `Diploma_CET_percentage`, `Name_of_the_institution_studied_diploma`, `Diploma_qualified_year`, `contact_number`, `LANDLINE_NUMBER`, `PARENTS_NUMBER`, `Alternate_contact_number`, `EMAIL_ID`, `College_mail`, `CURRENT_ADDRESS`, `PERMANENT_ADDRESS`, `password`, `uname`, `Total_CGPA_per`) VALUES
(1, 'Siddesh', '4NI18IS021', '8/7/97', 'Male', 'GENERAL', 'CET', 'CSE', 'A', '112', '112', '2', '3', '4', '5', '6', '7', '8', '9', '1', '2', '2', '1', '2', '1', '2', '2', 'eds', '1', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2asd', 'asd', 'asd', 'asd', 'asd', 'asd', '123', 'abc', NULL),
(2, 'Priya', 'asdfg', 'asdf', 'Female', 'asdf', 'asdf', 'asd', 'sdf', 'sdf', 'asdf', '6', 'sdf', 'gh', 'sdfgh', 'asdf', 'asdfg', 'asdf', 'sdfg', 'erf', 'dc', 'ssss', 'ssss', 'sssss', 'ssss', 'ssssss', 'ssss', 'ffff', 'fff', 'ffff', 'fffff', 'fffff', 'fffff', 'ffff', 'fffff', 'fffff', 'ffffff', 'ffff', 'ffff', 'fffff', 'fffff', 'fff', 'fff', 'fff', 'fff', '123', 'asd', NULL),
(3, 'Aishwarya', '1', '2022-05-12', 'Male', 'Shoes', 'comed k', 'ISE', 'A', '8', '8', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '2016', '3', '3', '3', '3', '3', '3', '3', '3', '9087765432', '23456789', '12233', '23e4r5678', 'test@gmail.com', 'test@gmail.com', 'asd', 'cotton green', '123', NULL, '3'),
(4, 'Yogesh', '2', '2022-02-18', 'Male', 'OK', 'comed k', 'CSE', 'A', '22', '22', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '9', '2', '2', '2', '2', '2', '2', '2016', '2', '2', '2', '2', '2', '2', '2', '3', '9876543210', '22222222', '9876543210', '1234567990', 'test@gmail.com', 'test@gmail.com', 'Sangharsha', 'cotten green', '789', NULL, '2');

-- --------------------------------------------------------

--
-- Table structure for table `student_status`
--

CREATE TABLE `student_status` (
  `id` int(11) NOT NULL,
  `Student_id` varchar(100) DEFAULT NULL,
  `Student_name` varchar(100) DEFAULT NULL,
  `Company_id` varchar(100) DEFAULT NULL,
  `Company_name` varchar(100) DEFAULT NULL,
  `Status` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `student_status`
--

INSERT INTO `student_status` (`id`, `Student_id`, `Student_name`, `Company_id`, `Company_name`, `Status`) VALUES
(1, '1', 'Siddesh', '1', 'TCS', 'Applied'),
(2, '2', 'Priya', '2', 'KPMG', 'Applied'),
(3, '1', 'Siddesh', '3', 'Abcd', 'Not Placed');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `admindata`
--
ALTER TABLE `admindata`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `auth_group`
--
ALTER TABLE `auth_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indexes for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  ADD KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`);

--
-- Indexes for table `auth_user`
--
ALTER TABLE `auth_user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- Indexes for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  ADD KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`);

--
-- Indexes for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  ADD KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `collegelogin`
--
ALTER TABLE `collegelogin`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `companydetails`
--
ALTER TABLE `companydetails`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  ADD KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`);

--
-- Indexes for table `django_content_type`
--
ALTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`);

--
-- Indexes for table `django_migrations`
--
ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `django_session`
--
ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_expire_date_a5c62663` (`expire_date`);

--
-- Indexes for table `offcampusplaced`
--
ALTER TABLE `offcampusplaced`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `student_details`
--
ALTER TABLE `student_details`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `student_status`
--
ALTER TABLE `student_status`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `admindata`
--
ALTER TABLE `admindata`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=53;

--
-- AUTO_INCREMENT for table `auth_user`
--
ALTER TABLE `auth_user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `collegelogin`
--
ALTER TABLE `collegelogin`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `companydetails`
--
ALTER TABLE `companydetails`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;

--
-- AUTO_INCREMENT for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;

--
-- AUTO_INCREMENT for table `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=33;

--
-- AUTO_INCREMENT for table `offcampusplaced`
--
ALTER TABLE `offcampusplaced`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `student_details`
--
ALTER TABLE `student_details`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `student_status`
--
ALTER TABLE `student_status`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Constraints for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Constraints for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
