#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import sqlite3
import matplotlib.ticker as ticker

# Connect to the SQLite database
con = sqlite3.connect('BostonHousing-allyears.db')

# SQL query to calculate average price per year
query = """
SELECT year, ROUND(AVG(LV + BV)) AS average_price
FROM Assessments 
WHERE LV <> 0
AND BV <> 0 
GROUP BY year
"""

# Execute the query and read the results into a DataFrame
df = pd.read_sql_query(query, con)

# Plotting the line graph
plt.figure(figsize=(10, 6))
plt.plot(df['year'], df['average_price'], marker='o')

# Add each year on X-axis
plt.xticks(df['year'], rotation=45)

# Add currency value onto Y-axis
formatter = ticker.StrMethodFormatter('${x:,.0f}')
plt.gca().yaxis.set_major_formatter(formatter)

# Label graph 
plt.xlabel('Year')
plt.ylabel('Average Price')
plt.title('Average Boston Property Prices Since 2004')
plt.grid(True)
plt.show()


# In[ ]:




