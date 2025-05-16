# Housing Data Analysis

This project performs data cleaning, outlier detection, and visualization on a housing dataset using Python.

## Features

- Handles missing values for price, parking, and bathrooms
- Identifies and displays outliers in housing prices
- Visualizes:
  - Price vs Area (line & scatter plot)
  - Parking distribution (pie chart)
  - Price distribution (histogram)

## Project Structure

```
housing-analysis/
├── data/ # CSV dataset
├── notebooks/ # Original notebook
├── src/ # Script version of the analysis
├── README.md
├── .gitignore
└── requirements.txt
```

## Setup

```bash
git clone https://github.com/yourusername/housing-analysis.git
cd housing-analysis
pip install -r requirements.txt
python src/analysis.py
```

## Dependencies

- pandas
- matplotlib
