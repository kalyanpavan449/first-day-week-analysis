First Day of Week Analysis
# What is the First Day of the Week?
- Whether the Gregorian calendar shows Sunday or Monday as the first day of the week depends on where you live.
- Do more countries start the week on Sunday or Monday? What about people? What about by continent?
- The file `first-day-of-week.csv` shows the first day of the week for each territory. The file `population.csv` shows the population in the year 2020 for each territory in millions, and the file `four-regions.csv` specifies whether each territory is in asia, europe, africa, or the americas. 

📌 Overview
This project uses Pandas to analyze global data about the first day of the week across countries, combined with population and regional information.
The script demonstrates how to:
- Load and merge multiple CSV datasets
- Perform grouping and aggregation
- Filter data based on conditions
- Summarize results by population and region

It’s designed to be beginner-friendly, with clear comments and structured outputs.
📂 Datasets
The script expects the following CSV files in the same directory:
1. first-day-of-week.csv
   - Contains country codes and the first day of the week (e.g., Sunday, Monday).
   - Key column: alpha3 (ISO country code).
2. population.csv
   - Contains population data for each country.
   - Key column: alpha3.
3. four-regions.csv
   - Maps countries to one of four global regions.
   - Key column: alpha3.
⚙️ How It Works
1. Load the datasets using pandas.read_csv().
2. Merge datasets on the common alpha3 country code.
3. Group and aggregate population data by:
   - First day of the week
   - Region + first day of the week
4. Filter results to focus on specific days (Fri, Sat, Sun, Mon).
5. Print summaries for easy interpretation.
▶️ Usage
1. Clone this repository:
   git clone https://github.com/your-username/first-day-week-analysis.git
   cd first-day-week-analysis

2. Ensure the required CSV files are present in the project folder.

3. Run the script:
   python analysis.py
📊 Example Output
- Preview of datasets
- Count of countries grouped by first day
- Total population for selected days
- Regional breakdown for Sunday and Monday
🛠️ Requirements
- Python 3.x
- Pandas library

Install dependencies:
pip install pandas
✨ Author
Developed by Pavan — transitioning from accounting to data analytics, with a focus on clear, structured, and impactful data insights.
