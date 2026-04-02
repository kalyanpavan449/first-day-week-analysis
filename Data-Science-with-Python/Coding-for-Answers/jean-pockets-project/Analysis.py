# Import necessary libraries
import pandas as pd
from scipy.stats import ttest_ind

# Load the dataset
df = pd.read_csv('jean-pocket-measurements.csv')

# --- Front Pocket Height Comparison ---

# Calculate average front pocket height by gender
avg_height = df.groupby('gender')['height_front'].mean()

# Compute absolute difference in average height
height_diff = abs(avg_height['men'] - avg_height['women']).round(3)
print(f"Average pocket height difference: {height_diff:.2f} units")

# --- T-Test: Skinny vs Straight Styles ---

# Filter data by gender and style
women_skinny = df[(df['gender'] == 'women') & (df['style'] == 'skinny')]['height_front']
women_straight = df[(df['gender'] == 'women') & (df['style'] == 'straight')]['height_front']
men_skinny = df[(df['gender'] == 'men') & (df['style'] == 'skinny')]['height_front']
men_straight = df[(df['gender'] == 'men') & (df['style'] == 'straight')]['height_front']

# Perform independent t-tests
t_stat_women, p_val_women = ttest_ind(women_skinny, women_straight, equal_var=False)
t_stat_men, p_val_men = ttest_ind(men_skinny, men_straight, equal_var=False)

# Display p-values
print(f"Women: p-value = {p_val_women:.4f}")
print(f"Men: p-value = {p_val_men:.4f}")

# --- Back Pocket Area Comparison ---

# Calculate average back pocket dimensions by gender
back_pocket = df.groupby('gender')[['height_back', 'width_back']].mean()

# Compute pocket area
back_pocket['area_back'] = back_pocket['height_back'] * back_pocket['width_back']
print(back_pocket)

# Calculate area difference and percentage
area_diff = abs(back_pocket.loc['men', 'area_back'] - back_pocket.loc['women', 'area_back'])
percent_diff = (area_diff / back_pocket.loc['men', 'area_back']) * 100
print(f"\nBack pocket area is {percent_diff:.2f}% smaller in women's jeans compared to men's.")

# --- Phone Fit Analysis ---

# Define phone height in cm
phone_height = 16.0  # Example: Iqoo Neo9 Pro

# Check if phone fits in back pocket
df['phone_fits_back'] = df['height_back'] >= phone_height

# Calculate fit percentage by gender
fit_percent = df.groupby('gender')['phone_fits_back'].mean() * 100

# Display results
print("📱 Percentage of jeans that fit the phone in back pocket:")
print(f"Women: {fit_percent.get('women', 0):.2f}%")
print(f"Men: {fit_percent.get('men', 0):.2f}%")