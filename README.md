# 💸 Payday Loan APR Calculator

> A simple Python tool that calculates the **Annual Percentage Rate (APR)** of payday loans — helping users uncover the hidden, often predatory costs of high-interest short-term loans.

---

## 📚 Project Overview

Millions of Americans rely on payday loans, often without realizing how steep the interest truly is. These loans frequently advertise flat fees rather than clear APRs, obscuring their actual cost. This tool helps compute the **real APR** based on either:

- The loan amount, finance charge, and repayment period
- OR a flat fee per $100 borrowed and the repayment duration

---

## 🎯 Goals

- **Promote financial literacy** by revealing the true cost of payday loans.
- Encourage **ethical computing** by applying programming to social-good problems.
- Practice real-world use of **Python conditionals, user input, and arithmetic**.

---

## 🧪 Example Usage

```text
Welcome to the payday loan APR calculator.
Please have the proposed terms of your payday loan handy so we can calculate the APR.

Select which one best fits your situation.
  (1) I know the total loan amount, the finance charge, and the repayment period (in days or months).
  (2) I know the fee in dollars for every 100 dollars borrowed and the repayment period (in days or months).

How was the information given to you? Choose (1) or (2): 1

What is the total loan amount? 350.00
What is the finance charge for the loan? 50.00
Is the length of the repayment period in days or months? Enter d or m: d
How many days is the repayment period? 14

Your 14 day loan has an APR of 372.45%.
````

---

## 🧠 APR Calculation Logic

### Scenario 1: Loan Amount, Finance Charge, Repayment Period

**Formula:**

```
APR = (finance_charge / loan_amount) × (365 / repayment_period_days) × 100
```

### Scenario 2: Fee Per \$100 Borrowed

**Formula:**

```
APR = fee × (365 / repayment_period_days)
```

If the repayment period is in **months**, the formula uses `12` instead of `365`.

---

## 🌍 Why This Matters

This project highlights the ethical responsibility of programmers to use computing to promote **transparency** and **justice** — especially in financial systems where vulnerable populations are frequently exploited.

More about payday loans:
📺 [WMC Action News - Memphis urges payday loan ban](https://www.wmcactionnews5.com/2020/09/06/memphis-city-council-urges-state-ban-all-payday-lenders/)

---