# Redbus
## Overview
This project automates the scraping bus details from the RedBus website, stores the data in a MySQL database, and provides an interactive web interface using Streamlit for users to view and filter bus details.
## Features
### Web Scraper
*Scrapes bus route information, including route names and links.

*Extracts detailed bus data:
1. Route Name
2. Bus Name
3. Bus Type
4. Departing Time
5. Duration
6. Reaching Time
7. Star Rating
8. Price
9. Seat Availability
    
*Stores the scraped data into a MySQL database.

*Exports the data into a CSV file (.csv).

### Streamlit Web App
*Displays bus details from the database in a tabular format.

*Allows users to filter buses based on:

1. Route Name
2. Bus Type
3. Departing Time
