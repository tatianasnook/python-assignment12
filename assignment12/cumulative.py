import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# Task 2: A Line Plot with Pandas
# 1. Create a file called cumulative.py. The boss wants to see how money is rolling in .
# You use SQL to access ../db/lesson.db again.
# You create a DataFrame with the order_id and the total_price for each order.
# This requires joining several tables, GROUP BY, SUM, etc.
# 2. Add a "cumulative" column to the DataFrame.

with sqlite3.connect("db/lesson.db") as conn:
    query = """
    SELECT o.order_id, SUM(p.price * l.quantity) AS total_price
    FROM orders o
    JOIN line_items l ON o.order_id = l.order_id  
    JOIN products p ON l.product_id = p.product_id  
    GROUP BY o.order_id
    ORDER BY o.order_id;
    """
    df = pd.read_sql_query(query, conn)

df['cumulative'] = df['total_price'].cumsum()

# 3. Use Pandas plotting to create a line plot of cumulative revenue vs. order_id.
# 4. Show the Plot.

df.plot(
    x='order_id',
    y='cumulative',
    kind='line',
    title="Cumulative Revenue vs Order ID",
    legend=False
)
plt.xlabel("Order")
plt.ylabel("Revenue ($)")
plt.grid(axis='y', color='gray', linestyle='--', linewidth=0.4)
plt.tight_layout()
plt.show()
