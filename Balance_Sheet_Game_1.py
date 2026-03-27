import streamlit as st

st.title("📊 Business Scenario Simulator Game")

# -----------------------------
# Base Financial Data
# -----------------------------
sales = 50_000_000
cost_of_sales = 20_000_000
salaries = 15_000_000
rent = 1_200_000
marketing = 45_000
admin_costs = 3_480_000
tax_rate = 0.27

fixed_assets = 10_411_000
inventory = 450_000
debtors = 435_000
bank = 0

long_term_liabilities = 1_500_000
creditors = 46_000
share_capital = 2_249_250
Retained_Income = 7_500_750

# -----------------------------
# Scenario Controls
# -----------------------------
st.sidebar.header("Choose Business Decisions")

scenario1 = st.sidebar.checkbox("Move to cheaper rent (-80,000 rent)")
scenario2 = st.sidebar.checkbox("Increase marketing (+50k cost, +500k sales)")
scenario3 = st.sidebar.checkbox("Hire 2 employees (+500k salaries, +2M sales)")
scenario4 = st.sidebar.checkbox("New supplier (-500k cost of sales)")

# -----------------------------
# Apply Scenarios
# -----------------------------
cash_flow = 0

if scenario1:
    rent -= 80_000
    cash_flow += 80_000
    creditors += 22_000
        
if scenario2:
    marketing += 50_000
    sales += 500_000
    cash_flow += 450_000
    creditors += 121_500
    
if scenario3:
    salaries += 500_000
    sales += 2_000_000
    cash_flow += 1_500_000
    creditors += 405_000
    
if scenario4:
    cost_of_sales -= 500_000
    cash_flow += 500_000
    creditors += 135_000
   
# -----------------------------
# Income Statement Calculations
# -----------------------------
gross_profit = sales - cost_of_sales

expenses = salaries + rent + marketing + admin_costs
ebt = gross_profit - expenses
tax = ebt * tax_rate
net_profit = ebt - tax

# -----------------------------
# Balance Sheet Calculations
# -----------------------------
current_assets = inventory + debtors + cash_flow
total_assets = fixed_assets + current_assets

total_liabilities = long_term_liabilities + creditors
retained_income = net_profit
equity = share_capital + retained_income  # assuming no new share capital changes
total_equity_liabilities = total_liabilities + equity

# -----------------------------
# Ratios
# -----------------------------
gross_profit_ratio = gross_profit / sales
net_profit_ratio = net_profit / sales
roi = net_profit / total_equity_liabilities
current_ratio = current_assets / creditors if creditors != 0 else 0
debtors_days = (debtors / sales) * 365
debt_to_equity = total_liabilities / equity

# -----------------------------
# Display Results
# -----------------------------
st.header("📄 Income Statement")

st.write(f"Sales: {sales:,.0f}")
st.write(f"Cost of Sales: {cost_of_sales:,.0f}")
st.write(f"Gross Profit: {gross_profit:,.0f}")

st.write("### Expenses")
st.write(f"Salaries: {salaries:,.0f}")
st.write(f"Rent: {rent:,.0f}")
st.write(f"Marketing: {marketing:,.0f}")
st.write(f"Admin Costs: {admin_costs:,.0f}")

st.write(f"Earnings Before Tax: {ebt:,.0f}")
st.write(f"Tax: {tax:,.0f}")
st.write(f"Net Profit: {net_profit:,.0f}")

# -----------------------------
st.header("🏦 Balance Sheet")

st.subheader("Assets")
st.write(f"Fixed Assets: {fixed_assets:,.0f}")
st.write(f"Inventory: {inventory:,.0f}")
st.write(f"Debtors: {debtors:,.0f}")
st.write(f"Bank (Cash Flow): {cash_flow:,.0f}")
st.write(f"Total Assets: {total_assets:,.0f}")

st.subheader("Equity & Liabilities")
st.write(f"Share Capital: {share_capital:,.0f}")
st.write(f"Retained Income: {retained_income:,.0f}")
st.write(f"Total Equity: {equity:,.0f}")
st.write(f"Long-term Liabilities: {long_term_liabilities:,.0f}")
st.write(f"Creditors: {creditors:,.0f}")
st.write(f"Total Liabilities: {total_liabilities:,.0f}")
st.write(f"Total Equity + Liabilities: {total_equity_liabilities:,.0f}")

# -----------------------------
st.header("📊 Financial Ratios")

st.write(f"Gross Profit Ratio: {gross_profit_ratio:.2%}")
st.write(f"Net Profit Ratio: {net_profit_ratio:.2%}")
st.write(f"Return on Investment: {roi:.2%}")
st.write(f"Current Ratio: {current_ratio:.2f}")
st.write(f"Debtors Days: {debtors_days:.2f} days")
st.write(f"Debt to Equity Ratio: {debt_to_equity:.2f}")

# -----------------------------
st.success("✅ Try different combinations to maximize profit!")
