# Command-Line-Analytics

### What it does
Outputs the following meaningful analytics for a news website:
* Top 3 articles of all time
* Top authors of all time (ranked by aggregate article views)
* Days when the server returned an abnormal ammount of requests with error codes

### How it works
* Uses the psycopg2 python-DB package to interface between postgreSQL and python3

### How to use it
0. Requirements: Python3 and an up-to-date version of pSQL
1. Download the example database (newsdata.sql from udacity), and move it to the same folder as the rest of the code in this repo
2. Init the 'news' database and run the SQL script inside newsdata.sql
3. Run analytics.py from the command line using Python3
