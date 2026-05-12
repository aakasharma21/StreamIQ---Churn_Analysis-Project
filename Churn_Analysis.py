# =============================================================================
#   StreamIQ Analytics — OTT Users Churn Analysis
#   Author  : Aakash Sharma (Certified Data Analyst)
#   Tool    : Python (Pandas & NumPy)
#   Dataset : OTT_Churn.xlsx
#   GitHub  : https://github.com/aakasharma21
# =============================================================================

import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings("ignore")

# ── Config ────────────────────────────────────────────────────────────────────

FILE_PATH = "OTT_Churn.xlsx"   # update path if needed
pd.set_option("display.max_columns", None)
pd.set_option("display.width", 120)
pd.set_option("display.float_format", lambda x: f"{x:.2f}")

SEP_THICK = "=" * 70
SEP_THIN  = "-" * 70

def header(title):
    print(f"\n{SEP_THICK}")
    print(f"  {title}")
    print(SEP_THICK)

def subheader(title):
    print(f"\n{SEP_THIN}")
    print(f"  -- {title}")
    print(SEP_THIN)

# ── Load Dataset ──────────────────────────────────────────────────────────────

df = pd.read_excel(FILE_PATH)
df["ChurnLabel"]  = df["ChurnLabel"].astype(int)
df["ChurnReason"] = df["ChurnReason"].fillna("N/A")

TOTAL_CHURNED = int(df["ChurnLabel"].sum())   # used in churn rate % by platform


# =============================================================================
#   SECTION 1 — GENERAL ANALYSIS
# =============================================================================

header("SECTION 1 — GENERAL ANALYSIS")


# -- Total Customers vs Churned Customers -------------------------------------

subheader("Total Customers vs Churned Customers")

total_vs_churned = pd.DataFrame({
    "Total_Customers" : [len(df)],
    "Churned_Customers": [TOTAL_CHURNED],
})
print(total_vs_churned.to_string(index=False))


# -- Customers on Gender Basis ------------------------------------------------

subheader("Customers on Gender Basis")

# Distinct genders
distinct_gender = pd.DataFrame({"Gender": df["Gender"].unique()})
print("Distinct Genders:")
print(distinct_gender.to_string(index=False))

# Count per gender
gender_count = (
    df.groupby("Gender", as_index=False)
    .agg(No_of_Customers=("CustomerID", "count"))
)
print("\nCustomer Count by Gender:")
print(gender_count.to_string(index=False))


# -- Average Monthly Revenue Generated ----------------------------------------

subheader("Average Monthly Revenue Generated")

avg_revenue = df["MonthlyCharges_INR"].mean()
print(f"  Avg_Monthly_Revenue : ₹{avg_revenue:,.2f}")


# -- Top 3 Preferred Platforms by Users ---------------------------------------

subheader("Top 3 Preferred Platforms by Users")

top3_platforms = (
    df.groupby("Platform", as_index=False)
    .agg(Active_Users=("CustomerID", "count"))
    .sort_values("Active_Users", ascending=False)
    .head(3)
    .reset_index(drop=True)
)
print(top3_platforms.to_string(index=False))


# -- Preferred Payment Mode ---------------------------------------------------

subheader("Preferred Payment Mode")

payment_mode = (
    df.groupby("PaymentMethod", as_index=False)
    .agg(Active_Users=("CustomerID", "count"))
    .rename(columns={"PaymentMethod": "Mode_Of_Payment"})
    .sort_values("Active_Users", ascending=False)
    .reset_index(drop=True)
)
print(payment_mode.to_string(index=False))


# -- Genres Distribution ------------------------------------------------------

subheader("Genres Distribution")

genres_dist = (
    df.groupby("GenresViewed", as_index=False)
    .agg(Active_Users=("CustomerID", "count"))
    .rename(columns={"GenresViewed": "Genres_Viewed"})
    .sort_values("Active_Users", ascending=False)
    .reset_index(drop=True)
)
print(genres_dist.to_string(index=False))


# -- Preferred Logged-In Device -----------------------------------------------

subheader("Preferred Logged-In Device")

device_pref = (
    df.groupby("DeviceRegistered", as_index=False)
    .agg(Active_Users=("CustomerID", "count"))
    .rename(columns={"DeviceRegistered": "LoggedIn_Device"})
    .sort_values("Active_Users", ascending=False)
    .reset_index(drop=True)
)
print(device_pref.to_string(index=False))


# -- Most Used OTT Geographically ---------------------------------------------

subheader("Most Used OTT Geographically")

geo_pivot = (
    df.groupby("Location")
    .apply(lambda g: pd.Series({
        "Netflix"     : (g["Platform"] == "Netflix").sum(),
        "Prime"       : (g["Platform"] == "Amazon Prime").sum(),
        "Jio_Hotstar" : (g["Platform"] == "JioHotstar").sum(),
        "SonyLiv"     : (g["Platform"] == "SonyLiv").sum(),
        "ZEE5"        : (g["Platform"] == "ZEE5").sum(),
    }))
    .reset_index()
    .rename(columns={"Location": "City"})
)
print(geo_pivot.to_string(index=False))


# =============================================================================
#   SECTION 2 — CHURN ANALYSIS
# =============================================================================

header("SECTION 2 — CHURN ANALYSIS")

churned_df = df[df["ChurnLabel"] == 1].copy()


# -- Net Churn Rate % ---------------------------------------------------------

subheader("Net Churn Rate %")

total_cust  = len(df)
total_churn = TOTAL_CHURNED
churn_pct   = round(total_churn * 100.0 / total_cust, 2)

net_churn = pd.DataFrame({
    "Total_Customers"    : [total_cust],
    "Churned_Customers"  : [total_churn],
    "Churn_Rate_Percentage": [f"{churn_pct} %"],
})
print(net_churn.to_string(index=False))


# -- Churn by Age Group (Gender Split) ----------------------------------------

subheader("Churn by Age Group")

churn_age = (
    churned_df.groupby("AgeGroup")
    .apply(lambda g: pd.Series({
        "Male"      : (g["Gender"] == "Male").sum(),
        "Female"    : (g["Gender"] == "Female").sum(),
        "Others"    : (g["Gender"] == "Non-Binary").sum(),
    }))
    .reset_index()
)
print(churn_age.to_string(index=False))


# -- Churn Rate % by Platform -------------------------------------------------

subheader("Churn Rate % by Platform")

churn_by_platform = (
    df.groupby("Platform", as_index=False)
    .apply(lambda g: pd.Series({
        "Churn_rate": f"{round((g['ChurnLabel'].sum() * 100.0) / TOTAL_CHURNED, 2)} %"
    }))
    .sort_values("Churn_rate", ascending=False)
    .reset_index(drop=True)
)
print(churn_by_platform.to_string(index=False))


# -- Reason for Customer Attrition --------------------------------------------

subheader("Reason for Customer Attrition")

attrition_reason = (
    df.groupby("ChurnReason", as_index=False)
    .agg(Net_Attrition=("ChurnLabel", "sum"))
    .rename(columns={"ChurnReason": "Churned_Reason"})
    .sort_values("Net_Attrition", ascending=False)
    .reset_index(drop=True)
)
print(attrition_reason.to_string(index=False))


# -- Geographical Analysis (Churn) --------------------------------------------

subheader("Geographical Analysis")

geo_churn = (
    churned_df.groupby("Location", as_index=False)
    .agg(Net_Attrition=("CustomerID", "count"))
    .sort_values("Net_Attrition", ascending=False)
    .reset_index(drop=True)
)
print(geo_churn.to_string(index=False))


# -- Devices vs Churn ---------------------------------------------------------

subheader("Devices vs Churn")

device_churn = (
    churned_df.groupby("DeviceRegistered", as_index=False)
    .agg(Net_Attrition=("CustomerID", "count"))
    .rename(columns={"DeviceRegistered": "Register_Device"})
    .reset_index(drop=True)
)
print(device_churn.to_string(index=False))


# -- Revenue vs Churn by Subscription -----------------------------------------

subheader("Revenue vs Churn by Subscription")

rev_churn_sub = (
    df.groupby("SubscriptionType", as_index=False)
    .agg(
        Avg_Monthly_Revenue=("MonthlyCharges_INR", "mean"),
        Net_Attrition      =("ChurnLabel", "sum"),
    )
    .rename(columns={"SubscriptionType": "Subscription_Plan"})
)
print(rev_churn_sub.to_string(index=False))


# -- Payment Plan vs Churn ----------------------------------------------------

subheader("Payment Plan vs Churn")

pay_plan_churn = (
    churned_df.groupby("PaymentPlan", as_index=False)
    .agg(Net_Attrition=("CustomerID", "count"))
    .rename(columns={"PaymentPlan": "Plans"})
    .reset_index(drop=True)
)
# Mirror SQL: CONCAT(COUNT, ' %') — count displayed with ' %' suffix
pay_plan_churn["Net_Attrition"] = pay_plan_churn["Net_Attrition"].astype(str) + " %"
print(pay_plan_churn.to_string(index=False))


# -- Net Attrition by Platform and ChurnReason --------------------------------

subheader("Net Attrition by Platform and ChurnReason")

attrition_pivot = (
    churned_df.groupby("ChurnReason")
    .apply(lambda g: pd.Series({
        "Netflix"     : (g["Platform"] == "Netflix").sum(),
        "Prime"       : (g["Platform"] == "Amazon Prime").sum(),
        "Jio_Hotstar" : (g["Platform"] == "JioHotstar").sum(),
        "SonyLiv"     : (g["Platform"] == "SonyLiv").sum(),
        "ZEE5"        : (g["Platform"] == "ZEE5").sum(),
    }))
    .reset_index()
    .rename(columns={"ChurnReason": "Reason"})
)
print(attrition_pivot.to_string(index=False))


# =============================================================================
#   END
# =============================================================================

print(f"\n{SEP_THICK}")
print("  StreamIQ Analytics — OTT Churn Analysis | Complete")
print(f"  By: Aakash Sharma (Certified Data Analyst)")
print(SEP_THICK)
