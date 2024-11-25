import streamlit as st
import mysql.connector
import pandas as pd
from datetime import time

st.title("REDBUS")

# Database connection
db_connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="boot",
    database="redbus"
)
cursor = db_connection.cursor()

# Fetch BusDetails data
cursor.execute("SELECT * FROM BusDetails")
result = cursor.fetchall()
columns = [col[0] for col in cursor.description]
data = pd.DataFrame(result, columns=columns)

# Convert columns to numeric where necessary
data['price'] = pd.to_numeric(data['price'])
data['star_rating'] = pd.to_numeric(data['star_rating'])

# Convert `departing_time` to datetime for filtering
data['departing_time'] = pd.to_datetime(data['departing_time'], format='%H:%M').dt.time

# Sidebar Filters
states = ["All"] + list(data['state'].unique())
state_choice = st.sidebar.selectbox("Select State", states)

# Filter routes based on selected state
if state_choice == "All":
    routes = ["All"] + list(data['route_name'].unique())
else:
    filtered_routes = data[data['state'] == state_choice]
    routes = ["All"] + list(filtered_routes['route_name'].unique())

route_choice = st.sidebar.selectbox("Select Route", routes)

bus_types = ["All", "AC", "Non-AC", "Seater", "Sleeper"]
bus_type_choice = st.sidebar.selectbox("Select Bus Type", bus_types)

departing_times = ["All", "06:01 to 12:00", "12:01 to 18:00", "18:01 to 23:59", "00:01 to 06:00"]
departing_time_choice = st.sidebar.selectbox("Select Bus Timing", departing_times)

# Price Filters
fare_ranges = {
    'Below 100': (0, 100), '100-200': (100, 200), '200-400': (200, 400),
    '400-600': (400, 600), '600-800': (600, 800), '800-1000': (800, 1000),
    'Above 1000': (1001, float('inf'))
}
option_price = st.sidebar.selectbox("Select a Price", ["All"] + list(fare_ranges.keys()))
min_price, max_price = fare_ranges.get(option_price, (0, float('inf')))

# Rating Filters
min_rating, max_rating = st.sidebar.slider("Select star rating:", 0.0, 5.0, (0.0, 5.0))

# Helper function for filtering by time range
def with_range(departing_time, time_range):
    if time_range == "06:01 to 12:00":
        return time(6, 1) <= departing_time <= time(12, 0)
    elif time_range == "12:01 to 18:00":
        return time(12, 1) <= departing_time <= time(18, 0)
    elif time_range == "18:01 to 23:59":
        return time(18, 1) <= departing_time <= time(23, 59)
    elif time_range == "00:01 to 06:00":
        return time(0, 1) <= departing_time <= time(6, 0)
    return True

# Filtering logic
filtered_data = data.copy()

if state_choice != "All":
    filtered_data = filtered_data[filtered_data['state'] == state_choice]

if route_choice != "All":
    filtered_data = filtered_data[filtered_data['route_name'] == route_choice]

if bus_type_choice != "All":
    filtered_data = filtered_data[filtered_data['bus_type'].str.contains(bus_type_choice, case=False)]

if departing_time_choice != "All":
    timing = [with_range(x, departing_time_choice) for x in filtered_data['departing_time']]
    filtered_data = filtered_data[timing]

filtered_data = filtered_data[
    (filtered_data['price'] >= min_price) & (filtered_data['price'] <= max_price) &
    (filtered_data['star_rating'] >= min_rating) & (filtered_data['star_rating'] <= max_rating)
]

# Display filtered data
st.subheader("Bus Details")
st.dataframe(filtered_data)

# Close database connections
cursor.close()
db_connection.close()
