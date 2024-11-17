import streamlit as st
import mysql.connector
import pandas as pd

# Set the title
st.title("Bus Route Details")

# Connect to the database
db_connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="boot",
    database="redbus"
)
cursor = db_connection.cursor()

# the database to fetch data
details = "SELECT * FROM BusDetails"
cursor.execute(details)
result = cursor.fetchall()
columns = []
for d in cursor.description:
    columns.append(d[0])
data = pd.DataFrame(result, columns=columns)

# Sidebar Filters
st.sidebar.header("Filter Buses")

# Filter by Route (Make it optional, select all by default)
routes = data['route_name'].unique()
route_choice = st.sidebar.selectbox("Select Route (All Routes by Default)", options=["All"] + list(routes))

# Filter by Bus Type (Make it optional, select all by default)
bus_types = data['bus_type'].unique()
bus_type_choice = st.sidebar.selectbox("Select Bus Type (All Types by Default)", options=["All"] + list(bus_types))

# Filter by Bus Timing (Make it optional, select all by default)
departing_time = data['departing_time'].unique()
departing_time_choice = st.sidebar.selectbox("Select Bus Type (All Timing by Default)", options=["All"] + list(departing_time))

# Apply filters (filter based on both route and bus type)
if route_choice != "All" and bus_type_choice != "All":
    filtered_data = data[(data['route_name'] == route_choice) & (data['bus_type'] == bus_type_choice) & (data['departing_time'] == departing_time)]
elif route_choice != "All":
    filtered_data = data[data['route_name'] == route_choice]
elif bus_type_choice != "All":
    filtered_data = data[data['bus_type'] == bus_type_choice]
elif departing_time_choice != "All":
    filtered_data = data[data['departing_time'] == departing_time_choice]
else:
    filtered_data = data

# Display data
st.subheader("Bus Details")
st.dataframe(filtered_data)

cursor.close()
db_connection.close()
