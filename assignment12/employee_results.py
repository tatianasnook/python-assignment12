import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# Task 1: Plotting with Pandas
# 1. Create a file called employee_results.py.
# 2. Load a DataFrame called employee_results using SQL.
# Copy the db/lesson.db database from your python_homework folder to your python-assignment12 folder.
# Copy the db folder and the lesson.db file within it.
# This can be done using the cp - r command. In your assignment12 folder, connect to ../db/lesson.db.
# You use SQL to join the employees table with the orders table with the line_items table with the products table.
# You then group by employee_id, and you SELECT the last_name and revenue, where revenue is the sum of price * quantity.

with sqlite3.connect("db/lesson.db") as conn:
    query = """
    SELECT last_name, SUM(price * quantity) AS revenue 
    FROM employees e 
    JOIN orders o ON e.employee_id = o.employee_id 
    JOIN line_items l ON o.order_id = l.order_id 
    JOIN products p ON l.product_id = p.product_id 
    GROUP BY e.employee_id;
    """
    employee_results = pd.read_sql_query(query, conn)

# 3. Use the Pandas plotting functionality to create a bar chart where the x axis is the employee last name and the y axis is the revenue.
# 4. Give appropriate titles, labels, and colors.
# 5. Show the plot.

employee_results.plot(
    x='last_name',
    y='revenue',
    kind='bar',
    color='skyblue',
    legend=False,
    title="Employee Revenue"
)
plt.xlabel("Employee Last Name")
plt.ylabel("Revenue ($)")
plt.xticks(rotation=45)
plt.grid(axis='y', color='gray', linestyle='--', linewidth=0.4)
plt.tight_layout()
plt.show()
