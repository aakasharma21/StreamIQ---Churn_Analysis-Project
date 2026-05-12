<div align="center">

![StreamIQ Banner](StreamIQ_Churn%20Project/Dashboard_Screenshot/Home.png)

# StreamIQ Analytics — OTT Customer Churn Analysis

**End-to-end churn intelligence project | Data Cleaning → SQL Analysis → Python EDA → Looker Studio Dashboard**

![Excel](https://img.shields.io/badge/Excel-Advanced-217346?style=flat-square&logo=microsoft-excel&logoColor=white)
![SQL Server](https://img.shields.io/badge/SQL_Server-T--SQL-CC2927?style=flat-square&logo=microsoft-sql-server&logoColor=white)
![Python](https://img.shields.io/badge/Python-Pandas%20%26%20NumPy-3776AB?style=flat-square&logo=python&logoColor=white)
![Looker Studio](https://img.shields.io/badge/Looker_Studio-Dashboard-4285F4?style=flat-square&logo=google&logoColor=white)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen?style=flat-square)
[![Kaggle](https://img.shields.io/badge/Dataset-Kaggle-20BEFF?style=flat-square&logo=kaggle&logoColor=white)](https://www.kaggle.com/datasets/aakasharma21/project-ott-churn-dataset)

</div>

---

## 📋 Table of Contents

1. [Problem Statement](#-problem-statement)
2. [Project Overview & Objectives](#-project-overview--objectives)
3. [Tools & Technologies](#-tools--technologies)
4. [Dataset](#-dataset)
5. [Project Workflow](#-project-workflow)
6. [Dashboard Preview](#-dashboard-preview)
7. [KPIs](#-kpis)
8. [Key Insights](#-key-insights)
9. [SQL Analysis](#-sql-analysis)
10. [Python Analysis](#-python-analysis)
11. [Repository Structure](#-repository-structure)
12. [Getting Started](#-getting-started)
13. [Author](#-author)

---

## 🎯 Problem Statement

OTT platforms in India operate in one of the most competitive subscription markets globally — with users juggling multiple platforms and churning at the first sign of dissatisfaction. Understanding **why users leave, who leaves, and from which platform** is critical to reducing attrition and protecting revenue.

This project analyzes **1,000 OTT subscribers** across 5 platforms (Netflix, Amazon Prime, JioHotstar, SonyLiv, ZEE5), 10 cities, and multiple device and subscription types to decode the churn signals hiding in the data.

---

## 📌 Project Overview & Objectives

A full end-to-end churn analytics pipeline — from raw subscriber data to an interactive executive dashboard — covering behavioral patterns, platform-level attrition, revenue impact, and geographic spread.

**Key Questions Answered:**
- What is the overall churn rate and which platforms drive it most?
- What are the primary reasons customers cancel their subscriptions?
- Which age groups, devices, and cities are most churn-prone?
- How does subscription plan and payment method correlate with churn?
- Which platform-reason combinations create the highest attrition risk?

---

## 🛠 Tools & Technologies

| Tool | Usage |
|------|-------|
| **Advanced Excel** | Data cleaning, formatting, deduplication, preliminary EDA |
| **SQL Server (T-SQL)** | Relational database, KPI queries, churn segmentation |
| **Python (Pandas & NumPy)** | Programmatic analysis, churn computation, pivot aggregations |
| **Looker Studio (Data Studio)** | Interactive multi-page churn dashboard |

---

## 📂 Dataset

> 📦 [Project_OTT_Churn_Dataset on Kaggle](https://www.kaggle.com/datasets/aakasharma21/project-ott-churn-dataset)

**1,000 subscriber records** across a single flat table with the following key fields:

| Column | Description |
|--------|-------------|
| `CustomerID` | Unique subscriber identifier |
| `Gender`, `AgeGroup` | Demographics |
| `Location` | City (10 Indian cities) |
| `Platform` | Netflix / Amazon Prime / JioHotstar / SonyLiv / ZEE5 |
| `SubscriptionType` | Basic / Standard / Premium / Family |
| `PaymentMethod` | UPI / Credit Card / Debit Card / Net Banking / Wallet |
| `PaymentPlan` | Monthly / Quarterly / Annual |
| `MonthlyCharges_INR` | Monthly subscription charge |
| `DeviceRegistered` | Mobile / Smart TV / Laptop / Tablet / Desktop |
| `GenresViewed` | Preferred content genre |
| `ChurnLabel` | 1 = Churned, 0 = Active |
| `ChurnReason` | Price / Technical Issues / Found Alternative / Content / etc. |

---

## 🔄 Project Workflow

```
Raw Excel Data  →  Data Cleaning (Excel)  →  SQL Analysis (SQL Server)  →  Python EDA  →  Dashboard (Looker Studio)  →  Insights
```

1. **Excel** — Cleaned raw data, standardised column types, handled nulls, preliminary pivot checks
2. **SQL Server** — Imported cleaned table, wrote T-SQL across General Analysis & Churn Analysis domains
3. **Python** — Replicated and extended SQL logic using Pandas & NumPy for programmatic validation and deeper segmentation
4. **Looker Studio** — Built an interactive dashboard with churn KPIs, platform comparisons, geo maps, and reason breakdowns
5. **Insights** — Extracted business findings and retention recommendations

---

## 📊 Dashboard Preview

> 🔗 **[View Live Dashboard](https://datastudio.google.com/reporting/cee7f4c5-9132-406f-80b9-f50d3e75eec5)**

### Page 1 — Churn Overview
> Churn rate KPI · Churn by age group · Churn % by platform · Revenue vs churn by subscription

![Dashboard Overview](StreamIQ_Churn%20Project/Dashboard_Screenshot/Overview.png)

---

### Page 2 — Behavioral & Geographic Breakdown
> Churn reason breakdown · Subscription mix · Most preferred platform · Total churn by location · Device usage vs churn · Gender distribution · Payment mode · Genres distribution · Payment plan vs churn · Net attrition by platform & reason

![Dashboard Overview 2](StreamIQ_Churn%20Project/Dashboard_Screenshot/Overview2.PNG)

---

## 📈 KPIs

<div align="center">

| KPI | Value |
|-----|-------|
| 👥 Total Customers | **1,000** |
| 🚨 Total Churned | **128** |
| 📉 Churn Rate | **12.80%** |
| 💰 Avg Monthly Revenue | **₹340.44** |
| 🏆 Highest Churn Platform | **JioHotstar (29.69%)** |
| 📍 Top Churn Cities | **Delhi & Mumbai (16 each)** |
| 📱 Highest Churn Device | **Mobile (49)** |
| 🔴 Top Churn Reason | **Price (20.3%)** |
| 💳 Most Used Payment Mode | **UPI (474 transactions)** |
| 📺 Most Preferred Platform | **Netflix (26.7%)** |
| 📋 Top Subscription Plan | **Standard (35.3%)** |
| 💸 Highest Churn Plan | **Basic (44 churned)** |

</div>

---

## 💡 Key Insights

#### 📉 Churn Overview
- Overall churn rate stands at **12.80%** — with **128 of 1,000 subscribers** having left the platform
- **JioHotstar (29.69%) and Netflix (28.91%)** together account for nearly **60% of all churned users**, despite Netflix being the most preferred platform overall

#### 💸 Price is the #1 Retention Risk
- **Price sensitivity drives 20.3% of churn** — the single largest reason, followed by Technical Issues (18.8%) and Found Alternative (15.6%)
- **Basic plan subscribers churn the most (44)** despite paying the least — suggesting unmet content expectations at entry level
- Higher-paying **Premium and Family plan users churn significantly less**, indicating value perception improves with plan richness

#### 🧑‍🤝‍🧑 Demographics & Age
- The **25–34 age group** has the highest churn count — the most active streaming demographic, also the most willing to switch
- Churn is fairly distributed across genders (Male: 46.1%, Female: 51.1%, Non-Binary: 2.8%), suggesting churn is not gender-driven

#### 📱 Device & Geography
- **Mobile users churn the most (49)** — poor mobile UX or content experience is a key risk area
- **Smart TV users (33)** are the second-highest churn device — despite typically indicating more engaged, home-based viewers
- **Delhi and Mumbai lead churn geographically (16 each)** — high competition markets with multiple platform alternatives

#### 💳 Payment Behaviour
- **UPI dominates transactions (474)** — far ahead of Credit Card (198) and Debit Card (162)
- **Monthly payment plan users have the highest churn rate** — users on Annual plans are significantly more retained, reinforcing the value of locking in longer commitments

---

## 🔍 SQL Analysis

Full script: [`Churn_Analysis.sql`](Churn_Analysis.sql) — structured across 2 domains:

<details>

<summary><b>General Analysis</b> — customer overview, platforms, payments, geography</summary>

</details>


<details>

<summary><b>Churn Analysis</b> — churn rate, platform attrition, reasons, revenue impact</summary>

</details>

---

## 🐍 Python Analysis

Full script: [`Churn_Analysis.py`](Churn_Analysis.py) — mirrors and extends the SQL logic using **Pandas & NumPy**.

<details>
<summary><b>Coverage</b> — what the Python script computes</summary>

**Section 1 — General Analysis**
- Total vs churned customer count
- Gender distribution
- Average monthly revenue
- Top 3 platforms by active users
- Preferred payment modes
- Genres distribution
- Device preferences
- Geographic platform usage pivot (city × platform matrix)

**Section 2 — Churn Analysis**
- Net churn rate (%)
- Churn by age group with gender split
- Churn rate % by platform
- Reasons for attrition ranked by volume
- Geographic churn distribution
- Device vs churn breakdown
- Revenue vs churn by subscription type
- Payment plan vs churn
- Platform × ChurnReason attrition pivot matrix

</details>

---

## 📁 Repository Structure

```
StreamIQ-Churn-Analytics/
├── Ott_data.xlsx             # Raw dataset
├── Churn_Analysis.sql        # SQL queries (General + Churn Analysis)
├── Churn_Analysis.py         # Python analysis (Pandas & NumPy)
├── Home.png                  # Project banner
├── Overview.png              # Dashboard Page 1 snapshot
├── Overview2.PNG             # Dashboard Page 2 snapshot
├── Dashboard_Overview.pdf    # Full dashboard export (PDF)
└── README.md
```

---

## 🚀 Getting Started

**Prerequisites:** Excel 2016+ · SQL Server + SSMS · Python 3.8+ · Looker Studio (browser)

```bash
# Python dependencies
pip install pandas numpy openpyxl

# Run the analysis
python Churn_Analysis.py
```

```sql
-- SQL Server setup
CREATE DATABASE Proj_Ott;
USE Proj_Ott;
-- Import "Churn_Dataset.csv" as flat File(available on Kaggle) via SSMS: Tasks → Import Flat File
-- Then run Churn_Analysis.sql
```

```
-- Looker Studio Dashboard
-- Open live link: https://datastudio.google.com/reporting/cee7f4c5-9132-406f-80b9-f50d3e75eec5
-- Or import Dashboard_Overview.pdf for a static view
```

> 💡 **Dataset:** [Kaggle — Project_OTT_Churn_Dataset](https://www.kaggle.com/datasets/aakasharma21/project-ott-churn-dataset)

---

## 👨‍💻 Author

<div align="center">

**Aakash Sharma** — Certified Data Analyst

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/aakasharma21/)
[![Kaggle](https://img.shields.io/badge/Kaggle-Follow-20BEFF?style=for-the-badge&logo=kaggle&logoColor=white)](https://www.kaggle.com/aakasharma21)
[![Gmail](https://img.shields.io/badge/Gmail-Mail_Me-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:aakashs0101@gmail.com)

*Dataset is synthetic and built for portfolio & learning purposes.*

⭐ *If this project helped you, consider starring the repo!*

</div>
