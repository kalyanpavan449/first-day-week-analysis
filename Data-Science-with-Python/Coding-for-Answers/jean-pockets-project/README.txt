
# 👖 Pocket Size Analysis in Jeans

This project analyzes pocket dimensions in men's and women's jeans using a structured dataset. It highlights gender-based disparities in pocket usability and explores how style influences pocket depth and area.

---

## 📂 Dataset Overview

- **Source**: `jean-pocket-measurements.csv`
- **Features**:
  - `gender`
  - `style`
  - `height_front`
  - `height_back`
  - `width_back`
  - *(additional pocket-related metrics)*

---

## 📊 Analysis Breakdown

### 🧵 Front Pocket Comparison
- Calculated average height difference between men's and women's front pockets.
- Conducted statistical testing (t-test) to compare pocket depth across styles (e.g., skinny vs straight).

### 🧵 Back Pocket Area
- Measured average back pocket dimensions and computed area by gender.
- Assessed percentage difference in usable space between men's and women's jeans.

---

## 🧪 Tools & Environment

- `scipy.stats` for statistical testing
- Jupyter Notebook in Visual Studio Code

---

## 📈 Sample Output

```text
Average pocket height difference: 5.20 units
Women: p-value = 0.0321
Men: p-value = 0.0874

Back pocket area is 47.85% smaller in women's jeans compared to men's.

Percentage of jeans that fit the phone in back pocket:
Women: 18.75%
Men: 92.5%
```

---

## 💡 Insights

- Women's jeans consistently have shallower and smaller pockets.
- Style (e.g., skinny vs straight) significantly affects pocket depth.
- Back pockets in women's jeans are nearly half the size of men's, limiting usability.
- Only 1 in 5 women's jeans can fit a phone in the back pocket — compared to over 90% of men's jeans.

---

