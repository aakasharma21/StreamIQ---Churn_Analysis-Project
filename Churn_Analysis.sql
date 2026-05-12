
/* StreamIQ Analytics - Ott Users Churn Analysis | By-Aakash Sharma (Certified Data Analyst) */

/*  Dataset Link - https://www.kaggle.com/datasets/aakasharma21/project-ott-churn-dataset */


-- CREATE DATABASE Proj_Ott

use Proj_Ott

SELECT * FROM Churn_Dataset;

/**************************************** General Analysis ******************************************************************************/


-- Total Customers Vs Churned Customers

SELECT COUNT(CustomerID) AS Total_Customers, COUNT(CASE WHEN ChurnLabel=1 THEN 1 END) as Churned_Customers FROM Churn_Dataset;


-- Customers on gender basis

SELECT DISTINCT Gender FROM Churn_Dataset;

SELECT Gender, COUNT(CustomerID) AS No_of_Customers FROM Churn_Dataset
GROUP BY Gender;


-- Average Monthly Revenue Generated

SELECT FORMAT(AVG(MonthlyCharges_INR), 'C', 'en-IN') AS Avg_Monthly_Revenue  FROM Churn_Dataset;


-- TOP 3 Preferred Platforms by Users

SELECT TOP 3 Platform, COUNT(CustomerID) AS Active_Users FROM Churn_Dataset
GROUP BY Platform
ORDER BY Active_Users DESC


-- Preferred Payment Mode

SELECT PaymentMethod AS Mode_Of_Payment, COUNT(CustomerID) AS Active_Users FROM Churn_Dataset
GROUP BY PaymentMethod
ORDER BY Active_Users DESC


-- Genres Distribution

SELECT Genres_Viewed, COUNT(CustomerID) AS Active_Users FROM Churn_Dataset
GROUP BY Genres_Viewed
ORDER BY Active_Users DESC


-- Preferred Logged In Device

SELECT DeviceRegistered AS LoggedIn_Device, COUNT(CustomerID) AS Active_Users  FROM Churn_Dataset
GROUP BY DeviceRegistered
ORDER BY Active_Users DESC


-- Most Used Ott Geographically

SELECT Location AS City,COUNT(CASE WHEN Platform='Netflix' THEN 1 END) AS Netflix,
COUNT(CASE WHEN Platform='Amazon Prime' THEN 1 END) AS Prime,
COUNT(CASE WHEN Platform='JioHotstar' THEN 1 END) AS Jio_Hotstar,
COUNT(CASE WHEN Platform='SonyLiv' THEN 1 END) AS SonyLiv,
COUNT(CASE WHEN Platform='ZEE5' THEN 1 END) AS ZEE5  
FROM Churn_Dataset
GROUP BY Location


/**************************************** Churn Analysis ******************************************************************************/

-- Net Churn rate %

SELECT COUNT(CustomerID) AS Total_Customers,SUM(CASE WHEN ChurnLabel=1 THEN 1  ELSE 0 END) AS Churned_Customers,
CONCAT(CAST(SUM(CASE WHEN ChurnLabel=1 THEN 1 ELSE 0 END) * 100.0 / COUNT(CustomerID) AS DECIMAL(5,2)),' %') AS Churn_Rate_Percentage
FROM Churn_Dataset;


-- Churn by Age Group

SELECT AgeGroup, COUNT(CASE WHEN Gender='Male' THEN 1 END) as Male,
COUNT(CASE WHEN Gender='Female' THEN 1 END) as Female,
COUNT(CASE WHEN Gender='Non-Binary' THEN 1 END) as Others
FROM Churn_Dataset
WHERE ChurnLabel=1
GROUP BY AgeGroup


-- Churn Rate % by Platform

SELECT Platform, CONCAT(CAST((COUNT(CASE WHEN ChurnLabel=1 THEN 1 END)*100.0)/128 AS decimal(5,2)), ' %') AS Churn_rate FROM Churn_Dataset
GROUP BY Platform
ORDER BY Churn_rate DESC


-- Reason for Customer Attrition     

SELECT * FROM Churn_Dataset

SELECT ChurnReason AS Churned_Reason, COUNT(CASE WHEN ChurnLabel=1 THEN 1 END) as Net_Attrition FROM Churn_Dataset
GROUP BY ChurnReason
ORDER BY Net_Attrition DESC


-- Geographical Analysis

SELECT Location, COUNT(*) as Net_Attrition  FROM Churn_Dataset
WHERE ChurnLabel=1
GROUP BY Location
ORDER BY Net_Attrition DESC


-- Devices vs Churn

SELECT DeviceRegistered AS Register_Device, COUNT(CustomerID) as Net_Attrition FROM Churn_Dataset
WHERE ChurnLabel=1
GROUP BY DeviceRegistered


-- Revenue Vs Churn by Subscription 

SELECT SubscriptionType AS Subscription_Plan, AVG(MonthlyCharges_INR) AS Avg_Monthly_Revenue, SUM(ChurnLabel) AS Net_Attrition FROM Churn_Dataset
GROUP BY SubscriptionType


-- Payment Plan Vs Churn %

SELECT PaymentPlan AS Plans, CONCAT(COUNT(CustomerID), ' %') AS Net_Attrition FROM Churn_Dataset
WHERE ChurnLabel=1
GROUP BY PaymentPlan


-- Net Attrition by Platform and ChurnReason


SELECT ChurnReason AS Reason,COUNT(CASE WHEN Platform='Netflix' THEN 1 END) AS Netflix,
COUNT(CASE WHEN Platform='Amazon Prime' THEN 1 END) AS Prime,
COUNT(CASE WHEN Platform='JioHotstar' THEN 1 END) AS Jio_Hotstar,
COUNT(CASE WHEN Platform='SonyLiv' THEN 1 END) AS SonyLiv,
COUNT(CASE WHEN Platform='ZEE5' THEN 1 END) AS ZEE5
FROM Churn_Dataset
WHERE ChurnLabel=1
GROUP BY ChurnReason


/**************************************** END ******************************************************************************/