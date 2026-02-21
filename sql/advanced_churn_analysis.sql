-- 
SELECT 
    COUNT(CASE WHEN churn = 'Yes' THEN 1 END) * 100.0 / COUNT(*) AS churn_rate_percentage
FROM customer_churn;

------------------------------------------------------------


SELECT 
    contract_type,
    COUNT(*) AS total_customers,
    COUNT(CASE WHEN churn = 'Yes' THEN 1 END) AS churned_customers,
    ROUND(
        COUNT(CASE WHEN churn = 'Yes' THEN 1 END) * 100.0 / COUNT(*),
        2
    ) AS churn_rate_percentage
FROM customer_churn
GROUP BY contract_type
ORDER BY churn_rate_percentage DESC;

------------------------------------------------------------

SELECT 
    SUM(monthly_charges) AS estimated_monthly_revenue_loss
FROM customer_churn
WHERE churn = 'Yes';

------------------------------------------------------------

SELECT 
    CASE 
        WHEN tenure < 12 THEN '0-12 Months'
        WHEN tenure BETWEEN 12 AND 24 THEN '12-24 Months'
        ELSE '24+ Months'
    END AS tenure_group,
    COUNT(*) AS total_customers,
    COUNT(CASE WHEN churn = 'Yes' THEN 1 END) AS churned_customers
FROM customer_churn
GROUP BY tenure_group;

------------------------------------------------------------

-- 5️⃣ High-Risk Customer Ranking (Advanced - Window Function)
SELECT 
    customer_id,
    monthly_charges,
    tenure,
    RANK() OVER (ORDER BY monthly_charges DESC) AS high_risk_rank
FROM customer_churn
WHERE churn = 'Yes';
