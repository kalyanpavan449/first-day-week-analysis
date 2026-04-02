# Load the dataset containing first day of the week info
import pandas as pd
df = pd.read_csv('first-day-of-week.csv')
df.head()


df.groupby('first_day').count()

# How many people start the week on Friday, Saturday, Sunday, and Monday? Hint: This will involve a `merge`.
pop = pd.read_csv('population.csv')
merged = df.merge(pop, on='alpha3')
week_day = merged.groupby('first_day').agg({'population': 'sum'}).round(2)
print("Population grouped by first_day of week:")
print(week_day, "\n")


# How many territories show Friday, Saturday, Sunday, and Monday as the `first_day` of the week?
filtered = merged[merged['first_day'].isin(['fri', 'sat', 'sun', 'mon'])]
total_people = filtered['population'].sum().round(2)
print(f"Total_people: {total_people} million")

# Which of the `four_regions` predominantly start the week on Sunday? On Monday? Are there any regions that are more divided between Sunday and Monday? 
# Hint: This will also involve a `merge`.
region = pd.read_csv('four-regions.csv')
merged_region = merged.merge(region, on='alpha3')
region_merge = merged_region.groupby(['four_regions', 'first_day']).agg({'population': 'sum'}).round(2)
region_summary = region_merge[region_merge.index.get_level_values('first_day').isin(['sun', 'mon'])]
print("Regional population summary (only Sun & Mon):")
print(region_summary)



