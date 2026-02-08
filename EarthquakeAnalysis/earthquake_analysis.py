import pandas as pd
import mysql.connector
import streamlit as st

# ---------------- PAGE CONFIG ----------------
st.set_page_config(page_title="Earthquake Analysis", layout="wide")

st.markdown("### Select Earthquake Analysis")

# ---------------- DROPDOWN ----------------
analysis_choice = st.selectbox(
    "Earthquake Analysis",
    (
        "",
        "Top 10 strongest earthquakes",
        "Top 10 deepest earthquakes",
        "Shallow earthquakes <50km & mag>7.5",
        "Average magnitude by type",
        "Year with most earthquakes",
        "Month with most earthquakes",
        "Day with most earthquakes",
        "Earthquakes per hour",
        "Most active network",
        "Top 5 casualties",
        "Average loss by alert",
        "Reviewed vs Automatic",
        "Count by earthquake type",
        "Count by data type",
        "High station coverage",
        "Tsunamis per year",
        "Alert level count",
        "Top avg magnitude (10 years)",
        "Year over year growth",
        "Deep focus regions"
    ),
    label_visibility="collapsed"
)

# ---------------- DB CONNECTION ----------------
def get_connection():
    return mysql.connector.connect(
        host="127.0.0.1",
        port="3306",
        user="root",
        password="12345678",
        database="EQProject"
    )

# ---------------- QUERY FUNCTIONS ----------------

def top_10_strongest():
    title = "Top 10 Strongest Earthquakes (by Magnitude)"
    query = """
        SELECT time, place, country, mag, depth_km
        FROM earthquakes
        ORDER BY mag DESC
        LIMIT 10;
    """
    return pd.read_sql(query, get_connection()), title

def top_10_deepest():
    title = "Top 10 Deepest Earthquakes"
    query = """
        SELECT time, place, country, mag, depth_km
        FROM earthquakes
        ORDER BY depth_km DESC
        LIMIT 10;
    """
    return pd.read_sql(query, get_connection()), title

def shallow_high_mag():
    title = "Shallow Earthquakes (<50 km & Magnitude > 7.5)"
    query = """
        SELECT time, place, country, mag, depth_km
        FROM earthquakes
        WHERE depth_km < 50 AND mag > 7.5
        ORDER BY mag DESC;
    """
    return pd.read_sql(query, get_connection()), title

def avg_mag_by_type():
    title = "Average Magnitude by Magnitude Type"
    query = """
        SELECT magType, AVG(mag) AS avg_magnitude
        FROM earthquakes
        GROUP BY magType;
    """
    return pd.read_sql(query, get_connection()), title

def year_most_quakes():
    title = "Year with Most Earthquakes"
    query = """
        SELECT
        year,
        COUNT(*) AS total
        FROM earthquakes
        GROUP BY year
        ORDER BY total DESC
        LIMIT 1;
    """
    return pd.read_sql(query, get_connection()), title

def month_most_quakes():
    title = "Month with Highest Number of Earthquakes"
    query = """
        SELECT
        month,
        COUNT(*) AS total
        FROM earthquakes
        GROUP BY month
        ORDER BY total DESC
        LIMIT 1;
    """
    return pd.read_sql(query, get_connection()), title

def day_most_quakes():
    title = "Day of Week with Most Earthquakes"
    query = """
        SELECT
        day_of_week AS day,
        COUNT(*) AS total
        FROM earthquakes
        GROUP BY day_of_week
        ORDER BY total DESC;
    """
    return pd.read_sql(query, get_connection()), title

def quakes_per_hour():
    title = "Earthquake Count per Hour of Day"
    query = """
        SELECT HOUR(time) AS hour, COUNT(*) AS total
        FROM earthquakes
        GROUP BY hour
        ORDER BY hour;
    """
    return pd.read_sql(query, get_connection()), title

def most_active_network():
    title = "Most Active Reporting Network"
    query = """
        SELECT net, COUNT(*) AS total
        FROM earthquakes
        GROUP BY net
        ORDER BY total DESC
        LIMIT 1;
    """
    return pd.read_sql(query, get_connection()), title

def top_5_casualties():
    title = "Top 5 Places with Highest Casualties"
    query = """
        SELECT
        place,
        SUM(sig) AS casualties
        FROM earthquakes
        GROUP BY place
        ORDER BY casualties DESC
        LIMIT 5;
    """
    return pd.read_sql(query, get_connection()), title

def avg_loss_by_alert():
    title = "Average Economic Loss by Alert Level"
    query = """
        SELECT
        impact_level,
        ROUND(AVG(sig), 2) AS avg_loss
        FROM earthquakes
        GROUP BY impact_level
        ORDER BY avg_loss DESC;
    """
    return pd.read_sql(query, get_connection()), title

def reviewed_vs_auto():
    title = "Reviewed vs Automatic Earthquakes"
    query = """
        SELECT status, COUNT(*) AS total
        FROM earthquakes
        GROUP BY status;
    """
    return pd.read_sql(query, get_connection()), title

def count_by_type():
    title = "Earthquake Count by Type"
    query = """
        SELECT type, COUNT(*) AS total
        FROM earthquakes
        GROUP BY type;
    """
    return pd.read_sql(query, get_connection()), title

def count_by_data_type():
    title = "Earthquake Count by Data Type"
    query = """
        SELECT types, COUNT(*) AS total
        FROM earthquakes
        GROUP BY types;
    """
    return pd.read_sql(query, get_connection()), title

def high_station_coverage():
    title = "High Station Coverage Earthquakes (nst > 100)"
    query = """
        SELECT time, place, mag, nst
        FROM earthquakes
        WHERE nst > 100
        ORDER BY nst DESC;
    """
    return pd.read_sql(query, get_connection()), title

def tsunamis_per_year():
    title = "Tsunamis Triggered per Year"
    query = """
        SELECT
        year,
        COUNT(*) AS total
        FROM earthquakes
        WHERE tsunami = 1
        GROUP BY year
        ORDER BY year;
    """
    return pd.read_sql(query, get_connection()), title

def alert_level_count():
    title = "Earthquake Count by Alert Level"
    query = """
        SELECT
        impact_level,
        COUNT(*) AS total
        FROM earthquakes
        GROUP BY impact_level
        ORDER BY total DESC;
    """
    return pd.read_sql(query, get_connection()), title

def top_avg_mag_last_10_years():
    title = "Top 5 Countries by Average Magnitude (Last 10 Years)"
    query = """
        SELECT country, AVG(mag) AS avg_mag
        FROM earthquakes
        WHERE time >= DATE_SUB(CURDATE(), INTERVAL 10 YEAR)
        GROUP BY country
        ORDER BY avg_mag DESC
        LIMIT 5;
    """
    return pd.read_sql(query, get_connection()), title

def yoy_growth():
    title = "Year-over-Year Earthquake Growth Rate"
    query = """
        SELECT
        year,
        total,
        LAG(total) OVER (ORDER BY year) AS prev_year,
        ROUND(
            (total - LAG(total) OVER (ORDER BY year)) /
            LAG(total) OVER (ORDER BY year) * 100,
            2
        ) AS growth_pct
        FROM (
        SELECT
            year,
            COUNT(*) AS total
        FROM earthquakes
        GROUP BY year
        ) t
        ORDER BY year;
    """
    return pd.read_sql(query, get_connection()), title

def deep_focus_regions():
    title = "Regions with Most Deep-Focus Earthquakes (>300 km)"
    query = """
        SELECT country, COUNT(*) AS total
        FROM earthquakes
        WHERE depth_km > 300
        GROUP BY country
        ORDER BY total DESC;
    """
    return pd.read_sql(query, get_connection()), title

# ---------------- MAIN LOGIC ----------------
if analysis_choice == "":
    st.info("Please select an analysis from the dropdown above.")
    st.stop()

elif analysis_choice == "Top 10 strongest earthquakes":
    df, title_suffix = top_10_strongest()

elif analysis_choice == "Top 10 deepest earthquakes":
    df, title_suffix = top_10_deepest()

elif analysis_choice == "Shallow earthquakes <50km & mag>7.5":
    df, title_suffix = shallow_high_mag()

elif analysis_choice == "Average magnitude by type":
    df, title_suffix = avg_mag_by_type()

elif analysis_choice == "Year with most earthquakes":
    df, title_suffix = year_most_quakes()

elif analysis_choice == "Month with most earthquakes":
    df, title_suffix = month_most_quakes()

elif analysis_choice == "Day with most earthquakes":
    df, title_suffix = day_most_quakes()

elif analysis_choice == "Earthquakes per hour":
    df, title_suffix = quakes_per_hour()

elif analysis_choice == "Most active network":
    df, title_suffix = most_active_network()

elif analysis_choice == "Top 5 casualties":
    df, title_suffix = top_5_casualties()

elif analysis_choice == "Average loss by alert":
    df, title_suffix = avg_loss_by_alert()

elif analysis_choice == "Reviewed vs Automatic":
    df, title_suffix = reviewed_vs_auto()

elif analysis_choice == "Count by earthquake type":
    df, title_suffix = count_by_type()

elif analysis_choice == "Count by data type":
    df, title_suffix = count_by_data_type()

elif analysis_choice == "High station coverage":
    df, title_suffix = high_station_coverage()

elif analysis_choice == "Tsunamis per year":
    df, title_suffix = tsunamis_per_year()

elif analysis_choice == "Alert level count":
    df, title_suffix = alert_level_count()

elif analysis_choice == "Top avg magnitude (10 years)":
    df, title_suffix = top_avg_mag_last_10_years()

elif analysis_choice == "Year over year growth":
    df, title_suffix = yoy_growth()

elif analysis_choice == "Deep focus regions":
    df, title_suffix = deep_focus_regions()

# ---------------- DISPLAY ----------------
st.title(f"🌍 {analysis_choice}")
st.dataframe(df, use_container_width=True)