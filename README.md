# Telco Customer Churn Data Analysis

This project analyzes customer data from a telecom company to understand why customers stay or leave. It uses 8 different charts to find patterns in customer habits.

## Author
* **Md. Readul Islam**

## Key Findings from the Charts

* **Churn Rate:** About 26.5% of the customers have left the company. `[Reference: Pie Chart]`
* **Contract Type:** Most customers choose temporary month-to-month contracts. `[Reference: Bar Plot]`
* **Customer Loyalty:** Churn is very high in the first few months. If a customer stays for a long time, they rarely leave. `[Reference: Histogram & Violin Plot]`
* **Spending Habits:** Customers who leave the company usually have much higher monthly bills than customers who decide to stay. `[Reference: Box Plot]`
* **Total Revenue:** A customer's total spending is strongly tied to how many months they stay with the company. Long-term loyalty drives the most revenue. `[Reference: Line Plot & Heatmap]`

## Charts Created in this Project

1. **Line Plot:** Shows the trend of average monthly charges over customer tenure.
2. **Bar Plot:** Compares the number of customers across different contract types.
3. **Pie Chart:** Displays the percentage breakdown of customer churn status.
4. **Histogram:** Shows how customer tenure months are distributed.
5. **Scatter Plot:** Explores the customer tenure vs monthly charges.
6. **Box Plot:** Compares the monthly charges distribution between churned and active customers.
7. **Violin Plot:** Visualizes the density and spread of customer tenure by churn status.
8. **Heatmap:** Displays the correlation grid matrix among all numerical features.

## Requirements
* Python 3
* pandas
* matplotlib
* seaborn