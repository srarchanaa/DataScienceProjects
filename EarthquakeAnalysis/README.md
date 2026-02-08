🌍 Global Earthquake Analysis & Seismic Insights
📌 Project Overview
This project analyzes global earthquake data to uncover seismic patterns, trends, and high-risk zones using a fully data-driven pipeline. Earthquake data is retrieved from the USGS Earthquake API, cleaned and enriched using Python (Pandas & Regex), stored in MySQL, and analyzed through advanced SQL queries. Insights are presented via an interactive Streamlit dashboard.
🎯 Problem Statement
Analyze and interpret global earthquake data to identify seismic patterns, trends, and risk zones
Build a scalable, data-driven system using API-based data retrieval, preprocessing, and SQL analytics for meaningful earthquake insights
🏢 Business Use Cases
Enable governments and disaster-management teams to assess earthquake risks and plan mitigation strategies
Support insurers and researchers in evaluating seismic exposure and historical trends
Facilitate data-driven policies for urban safety, infrastructure resilience, and emergency response
🔧 Technical Approach
Retrieved earthquake data from the USGS Earthquake API for a defined time range (last 5 years)
Cleaned and preprocessed data using Python (Pandas & Regex)
Converted timestamps, handled missing values, and normalized numeric and text fields
Derived analytical columns such as year, month, day, depth category, and severity flags
Stored the cleaned dataset in MySQL for efficient querying
Performed in-depth SQL analytics to extract trends and insights
Built an interactive Streamlit dashboard for visualization and exploration
🗄️ Dataset Retrieval
API Used:
https://earthquake.usgs.gov/fdsnws/event/1/query
Key Parameters:
starttime
endtime
minmagnitude
format=geojson
Process:
Loop through each month and year for the selected time range
Fetch data using API requests
Extract data from properties and geometry fields
Convert timestamps from milliseconds to datetime
Store records in a Pandas DataFrame
#	📊 Dataset Description (26 Features)
Feature	Description
1	id	Unique identifier for each earthquake
2	time	Timestamp of the earthquake event
3	updated	Last updated timestamp
4	latitude	Epicenter latitude
5	longitude	Epicenter longitude
6	depth_km	Earthquake depth in kilometers
7	mag	Earthquake magnitude
8	magType	Magnitude measurement type
9	place	Location description
10	status	Reviewed or automatic event
11	tsunami	Tsunami indicator (0/1)
12	sig	Significance score
13	net	Reporting network
14	nst	Number of stations
15	dmin	Distance to nearest station
16	rms	RMS residual
17	gap	Azimuthal gap
18	magError	Magnitude uncertainty
19	depthError	Depth uncertainty
20	magNst	Stations used for magnitude
21	locationSource	Location reporting source
22	magSource	Magnitude reporting source
23	types	Associated data types
24	ids	All associated IDs
25	sources	Reporting sources
26	type	Event type (earthquake)
🧹 Data Preparation
Objective
Clean, transform, and store earthquake API data for reliable analysis.
Steps
Convert time and updated to datetime
Normalize text fields using Regex (e.g., extract country from place)
Convert numeric columns and handle missing values
Create derived columns:
Year, Month, Day, Day of Week
Shallow vs Deep earthquakes
Strong vs Destructive earthquakes
Store the final dataset in MySQL using SQLAlchemy
📈 Analytical Tasks
Magnitude & Depth Analysis
Top strongest and deepest earthquakes
Shallow high-magnitude events
Average depth and magnitude by region
Time-Based Analysis
Year, month, and day with most earthquakes
Hourly earthquake distribution
Most active reporting networks
Event Quality & Impact
Reviewed vs automatic events
Station coverage and reliability metrics
RMS and gap-based quality analysis
Advanced Seismic Insights
Most seismically active countries and regions
Year-over-year earthquake growth trends
Shallow vs deep earthquake ratios
Tsunami vs non-tsunami magnitude comparison
Spatial and temporal proximity analysis
📊 Results & Deliverables
✔️ Clean, normalized earthquake dataset (last 5 years)
✔️ MySQL database with all 26 features and derived metrics
✔️ 30+ advanced SQL queries for deep analysis
✔️ Interactive Streamlit dashboard
✔️ Comprehensive project documentation
🧠 Tools & Technologies
Python (Pandas, Regex, Requests)
MySQL & Advanced SQL
USGS Earthquake API
Streamlit

🚀 Future Enhancements
Real-time earthquake monitoring
Predictive modeling for seismic risk
Integration with GIS mapping tools
Automated ETL scheduling
