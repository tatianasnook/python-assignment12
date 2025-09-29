import plotly.express as px
import plotly.data as pldata

# Task 3: Interactive Visualizations with Plotly

# 1. Load the Plotly wind dataset. Print the first and last 10 lines of the DataFrame.

df = pldata.wind(return_type='pandas')

print(df.head(10))
print(df.tail(10))

# 2. Clean the data. You need to convert the 'strength' column to a float.
# Use of str.replace() with regex is one way to do this, followed by type conversion.

df['strength'] = df['strength'].str.replace(r'^\d+-', '', regex=True).str.replace('+', '', regex=False).astype(float)

# 3. Create an interactive scatter plot of strength vs. frequency, with colors based on the direction.
# 4. Save and load the HTML file, as wind.html. Verify that the plot works correctly.

fig = px.scatter(df,
                 x='strength',
                 y='frequency',
                 color='direction',
                 title="Strength vs. Frequency",
                 hover_data=["frequency"])
fig.write_html("wind.html", auto_open=True)
