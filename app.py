import streamlit as st
import pandas as pd
import plotly.express as px


df = pd.read_csv('vehicles_us.csv')

st.header('My Web Application Dashboard')

# Number of Vehicles for each Cylinder
# working code

# Histogram using st.write
st.header("Histogram of cylinders using st.write")
fig = px.histogram(df, x='cylinders', title='Number of Vehicles for each Cylinder')
st.write(fig)

fig.show()

# Number of Vehicles for each Type
# working code

# Histogram of Engine Cylinders
fig = px.histogram(df, x='type', title='Number of Vehicles for each Type')
st.plotly_chart(fig)

fig.show()


# Vehicle Age vs Vehicle Mileage Group
# working code

# Scatter plot using st.write
st.header("Age vs. Mileage Group")
fig = px.scatter(df, x='age', y='mileage_group', title="Vehicle Age vs Vehicle Mileage Group")
st.write(fig)

fig.show()

# Engine Size Category vs Vehicle Age
# working code

# Scatter plot using st.plotly_chart
st.header("Engine Size Category vs Vehicle Age")
fig = px.scatter(df, x='engine_size_category', y='age', title="Engine Size Category vs Vehicle Age")
st.plotly_chart(fig)

fig.show()

# Scatter Plot of Fuel Type Category vs. Age
# working code

# Scatter plot using st.plotly_chart
st.header("Scatter Plot of Fuel Type Category vs. Age")
fig = px.scatter(df, x='fuel', y='age', title="Scatter Plot of Fuel Type Category vs. Age")

# Enable/disable regression line
show_regression_line = st.checkbox("Show Regression Line")

if show_regression_line:
    fig.add_trace(
        go.Scatter(
            x=df['fuel'],
            y=df['age'],
            mode='markers',
            marker=dict(color='rgba(0, 0, 0, 0.3)'),
        )
    )
    fig.add_trace(
        go.Scatter(
            x=df['fuel'],
            y=np.polyval(np.polyfit(df['fuel'], df['age'], 1), df['fuel']),
            mode='lines',
            line=dict(color='red'),
        )
    )

st.plotly_chart(fig)
fig.show()

# Histogram of price
fig = px.histogram(df, x='price', nbins=50, title='Distribution of Price of All Vehicles')
fig.show()

# Histogram of odometer
fig = px.histogram(df, x='odometer', nbins=50, title='Distribution of Mileage of All Vehicles')
fig.show()

# Scatterplot of price vs. mileage
fig = px.scatter(df, x='odometer', y='price', title='Price vs. Mileage')
fig.show()

# Scatterplot of Vehicle Price vs. age
fig = px.scatter(df, x='age', y='price', title='Vehicle Price vs. Age')
fig.show()

# Scatterplot Vehicle Price vs. Mileage by Model
fig = px.scatter(df, x='odometer', y='price', color='model', labels={'mileage': 'Mileage (miles)', 'price': 'Price (USD)'}, title='Vehicle Price vs. Mileage by Model')
fig.show()

# Box plot of price distribution by model popularity category
box_fig = px.box(
    df,
    x='model_popularity_category',
    y='price',
    title='Price Distribution by Model Popularity Category',
    labels={'model_popularity_category': 'Model Popularity Category', 'price': 'Price'}
)
box_fig.show()

# Histogram of Vehicle Age Distribution
hist_fig = px.histogram(
    df,
    x='age',
    nbins=20,
    title='Distribution of Vehicle Age',
    labels={'age': 'Vehicle Age'}
)
hist_fig.show()

# Bar chart of model counts by popularity category
# Groupping
model_counts = df.groupby('model_popularity_category').size().reset_index(name='count')

# Create
bar_fig = go.Figure(data=[go.Bar(
    x=model_counts['model_popularity_category'],
    y=model_counts['count'],
    text=model_counts['count'],
    textposition='auto',
    marker=dict(color=px.colors.qualitative.Pastel)
)])

# Update
bar_fig.update_layout(
    title='Model Counts by Popularity Category',
    xaxis_title='Model Popularity Category',
    yaxis_title='Number of Vehicles',
    showlegend=False
)
# Show
bar_fig.show()

# Box plot of mileage by fuel type
box_fig = px.box(
    df,
    x='fuel',
    y='odometer',
    title='Mileage Distribution by Fuel Type',
    labels={'fuel_type': 'Fuel Type', 'mileage': 'Mileage'}
)
box_fig.show()

# Sunburst chart of vehicle type, model popularity category, and fuel type
sunburst_fig = px.sunburst(
    df,
    path=['type', 'model_popularity_category', 'fuel'],
    title='Vehicle Type, Model Popularity, and Fuel Type Distribution',
    color_discrete_sequence=px.colors.qualitative.Pastel
)
sunburst_fig.show()

# Violin plot of price by vehicle condition
violin_fig = px.violin(
    df,
    x='condition',
    y='price',
    title='Price Distribution by Vehicle Condition',
    labels={'condition': 'Vehicle Condition', 'price': 'Price'}
)
violin_fig.show()

# Scatter plot of mileage vs. age, colored by model popularity category
scatter_fig = px.scatter(
    df,
    x='age',
    y='odometer',
    color='model_popularity_category',
    title='Mileage vs. Age',
    labels={'age': 'Vehicle Age', 'mileage': 'Mileage'},
    hover_data={'model': True, 'model_year': True, 'odometer': True, 'age': True}
)
scatter_fig.show()

# Bar Figure for Model Years with Highest Number of Vehicles
# Filtering
last_10_years = list(range(current_year - 9, current_year + 1))
filtered_df = df[df['model_year'].isin(last_10_years)]

# Counting
model_year_counts = filtered_df['model_year'].value_counts().reset_index()
model_year_counts.columns = ['Model Year', 'Number of Vehicles']

# Creating Bar Chart
bar_fig = px.bar(
    model_year_counts,
    x='Model Year',
    y='Number of Vehicles',
    title=f'Model Years with Highest Number of Vehicles (Last 10 Years)',
    labels={'Model Year': 'Model Year', 'Number of Vehicles': 'Number of Vehicles'},
    color='Number of Vehicles',
    color_continuous_scale=px.colors.sequential.Viridis,
    text='Number of Vehicles',
    text_auto='.2s'
)

# Updating
bar_fig.update_layout(
    xaxis_title='Model Year',
    yaxis_title='Number of Vehicles',
    xaxis_tickangle=-45,
    showlegend=False
)
# Showing
bar_fig.show()

# Bar Figure for Average Price by Fuel Type
# Grouping 
avg_price_by_fuel = df.groupby('fuel')['price'].mean().reset_index()

# Bar Chart
fig = go.Figure(data=[go.Bar(
    x=avg_price_by_fuel['fuel'],
    y=avg_price_by_fuel['price'],
    text=avg_price_by_fuel['price'].round(2),
    textposition='outside',
    hoverinfo='text',
    marker=dict(color='steelblue')
)])

# Updating 
fig.update_layout(
    title='Average Price by Fuel Type',
    xaxis=dict(title='Fuel Type'),
    yaxis=dict(title='Average Price')
)

# Showing the plot
fig.show()

# Pie Chart for Percentage of Vehicles by Trasmission Type
# Calculation of the percentage of vehicles by transmission type
transmission_percentage = df['transmission'].value_counts(normalize=True) * 100

# Pie Chart
fig = go.Figure(data=[go.Pie(
    labels=transmission_percentage.index,
    values=transmission_percentage.values,
    textinfo='label+percent',
    insidetextorientation='radial',
    marker=dict(colors=['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728'])
)])

# Updating
fig.update_layout(
    title='Percentage of Vehicles by Transmission Type',
    legend=dict(
        x=0.8,
        y=0.5,
        orientation='v'
    )
)

# Showing the Plot
fig.show()

# Bar Plot for Top 5 Vehicle Types
# Get the top 5 vehicle types
top_5_types = df['type'].value_counts()

# Bar Plot
plt.figure(figsize=(10, 6))
top_5_types.plot(kind='bar', color='skyblue')
plt.title('Top 5 Vehicle Types')
plt.xlabel('Vehicle Type')
plt.ylabel('Number of Vehicles')
plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
plt.grid(axis='y', linestyle='--', alpha=0.7)  # Add grid lines for y-axis

# Show Number of Vehicles
for i, v in enumerate(top_5_types):
    plt.text(i, v + 5, str(v), ha='center', va='bottom')

plt.tight_layout()  # Adjust layout to prevent clipping of labels
plt.show()

# Bar Chart for Top 5 Vehicle Models
# Top 5 vehicle models by count
top_5_models = df['model'].value_counts().head(5)

# Bar Chart
fig = go.Figure(go.Bar(
    x=top_5_models.values,
    y=top_5_models.index,
    orientation='h',
    marker=dict(color='steelblue'),
    text=top_5_models.values,
    textposition='outside',
    hoverinfo='text'
))

# Update
fig.update_layout(
    title='Top 5 Vehicle Models',
    xaxis=dict(title='Count'),
    yaxis=dict(title='Model', autorange='reversed'),
    showlegend=False
)

# Show
fig.show()