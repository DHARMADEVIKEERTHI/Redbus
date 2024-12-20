# Redbus
## Overview
This project automates the scraping bus details from the RedBus website, stores the data in a MySQL database, and provides an interactive web interface using Streamlit for users to view and filter bus details.
## Features
### Web Scraper
*Scrapes bus route information, including route names and links.

*Extracts detailed bus data:
1. State
2. Route Name
3. Bus Name
4. Bus Type
5. Departing Time
6. Duration
7. Reaching Time
8. Star Rating
9. Price
10. Seat Availability
    
*Stores the scraped data into a MySQL database.

*Exports the data into a CSV file (.csv).

### Requirements
Python 3.7+
Required Python Libraries:
1. streamlit
2. mysql-connector-python
3. pandas

### Streamlit Web App
*Displays bus details from the database in a tabular format.

*Allows users to filter buses based on:

1. State Selection: Choose the state to filter bus routes available within it.
2. Route Selection: Filter buses based on the selected state and available routes.
3. Bus Type: Choose between AC, Non-AC, Seater, or Sleeper buses.
4. Departing Time: Filter buses based on their departure time in specific ranges (e.g., "06:01 to 12:00").
5. Price Range: Select a price range to filter buses based on ticket prices.
6. Star Rating: Filter buses based on their star ratings.

### How it Works
# Database Querying: 
The app connects to a MySQL database (redbus), fetches the bus data from the BusDetails table, and displays it on the frontend.
# Filtering: 
Users can select different filter options via the sidebar, and the app dynamically updates the bus details displayed based on these criteria. The filtering is done in real-time by applying conditions on the data from the database.
