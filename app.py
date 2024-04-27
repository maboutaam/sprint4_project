import streamlit as st
import pandas as pd
import plotly.express as px
import datetime


df = pd.read_csv('vehicles_us.csv')

st.header('Vehicles US -  Data Visualization Web Page')
st.subheader("Welcome to my first Github Project ")


df= df.dropna()

df = df.fillna(0)

df['price'] = df['price'].astype('float')

# Age new column

# working code

current_year = datetime.datetime.now().year
df['age'] = current_year - df['model_year']

# Price Range new column

# working code

def price_range(price):
    if price < 10000:
        return 'Low'
    elif price < 30000:
        return 'Medium'
    else:
        return 'High'

df['price_range'] = df['price'].apply(price_range)


# Mileage Group new column

# working code

def mileage_group(odometer):
    if odometer < 50000:
        return 'Low'
    elif odometer < 100000:
        return 'Medium'
    else:
        return 'High'

df['mileage_group'] = df['odometer'].apply(mileage_group)



# Engine Size Category new column

# working code

def engine_size_category(cylinders):
    if cylinders < 4.0:
        return 'Small'
    elif cylinders < 6.0:
        return 'Medium'
    else:
        return 'Large'

df['engine_size_category'] = df['cylinders'].apply(engine_size_category)


### Data Visualization



# Number of Vehicles for each Cylinder
fig = px.histogram(df, x='cylinders', title='Number of Vehicles for each Vehicle Cylinder')
st.plotly_chart(fig)

st.text("As seen in the above histogram, Vehicle with 6 cyclinders have the highest amount with a total of 13.264k, while there is only one 12 cylinder vehicle.")


# Number of Vehicles for each Type
fig = px.histogram(df, x='type', title='Number of Vehicles for each Vehicle Type')
st.plotly_chart(fig)

st.text("We can observe from the above histogram that the highest number of vehicles are SUVs with 10.511k and the least are buses with 23.")


# Vehicle Age vs Vehicle Mileage Group

fig = px.scatter(df, x='age', y='mileage_group', title="Vehicle Age vs Vehicle Mileage Group")
st.plotly_chart(fig)

st.text("The above Scattered histogram shows the distribution of Vehicle Age between Mileage Groups. For instance, low mileage group tend to live longer than groups. One example of a vehicle aged 88 years with low mileage.")


# Engine Size Category vs Vehicle Age

fig = px.scatter(df, x='engine_size_category', y='age', title="Engine Size Category vs Vehicle Age")
st.plotly_chart(fig)
st.text("This Plotly Express histogram shows how vehicle with large engine size tend to live longer than others. One example is a vehicle aged 116 have a Large engine.")


# Scatter Plot of Fuel Type Category vs. Age

# working code

# Create checkbox
show_regression_line = st.checkbox("Show Regression Line")

# Create scatter plot using st.plotly_chart
st.header("Scatter Plot of Fuel Type Category vs. Age")
fig = px.scatter(df, x='fuel', y='age', title="Scatter Plot of Fuel Type Category vs. Age", trendline="ols" if show_regression_line else None)

st.plotly_chart(fig)

st.text("We can interpret from the above scatter plot that vehicle that run on gas tend to live longer than vehicles who run with different kind of fuel. One example is a vehicle aged 116 years that runs on gas.")