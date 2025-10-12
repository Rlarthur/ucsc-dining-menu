#Scrapes UCSC dining data and updates JSON file
# Main job is to fetch menu data from UCSC dining website and save it in a structured JSON format
# This data is then served by the Flask app in app.py
# Need to implement automatic updates (e.g. via cron job) to keep data fresh