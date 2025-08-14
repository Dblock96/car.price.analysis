![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

# Car Price Analysis

Car Price Analysis is a comprehensive data analysis tool designed to streamline data exploration, analysis, and visualization of car pricing data. The tool supports CSV data formats and provides an intuitive workflow for both novice and expert data scientists.

## Dataset Content

The dataset used for this project includes detailed information about various car models, such as make, model, year, engine size, horsepower, and price. The primary datasets are:
- `data/car_price_clean.csv`
- `data/CarPrice_Assignment.csv`

These datasets are of reasonable size and do not exceed the repository's maximum size of 100GB.

Data source: https://www.kaggle.com/datasets/hellbuoy/car-price-prediction 

## Business Requirements

- Identify key factors influencing car prices.
- Build a predictive model to estimate car prices based on features.
- Provide actionable insights for car buyers and sellers.

## Hypothesis and How to Validate

- **Hypothesis 1:** Engine size and horsepower are positively correlated with car price.
	- *Validation:* Use correlation analysis and regression plots.
- **Hypothesis 2:** Brand and model year significantly impact car price.
	- *Validation:* Use group-by analysis and ANOVA tests.

## Project Plan

- **Data Collection:** Gathered from provided CSV files.
- **Data Processing:** Cleaned and preprocessed data for analysis.
- **Analysis:** Explored data using statistical and visualization techniques.
- **Interpretation:** Derived insights and built predictive models.

The research methodologies were chosen for their effectiveness in handling tabular data and providing interpretable results.

## Mapping Business Requirements to Data Visualisations

- **Key Factors Analysis:** Bar plots and correlation heatmaps.
- **Predictive Modeling:** Regression plots and residual analysis.
- **Brand/Year Impact:** Boxplots and grouped bar charts.

## Analysis Techniques Used

- **Exploratory Data Analysis (EDA):** Descriptive statistics, missing value analysis.
- **Visualization:** Matplotlib, Seaborn, Plotly for interactive plots.
- **Predictive Modeling:** Linear regression, decision trees.
- **Limitations:** Limited by dataset size and feature availability. Alternative approaches (e.g., feature engineering) were used to address these.

**Generative AI tools** were used for ideation, code optimization, and documentation.

## Ethical Considerations

- **Data Privacy:** No personal data present.
- **Bias/Fairness:** Checked for brand/model bias in pricing.
- **Legal/Societal Issues:** Used only open-source datasets.

## Dashboard Design

- **Main Page:** Overview statistics and key insights.
- **Exploration Page:** Interactive plots (e.g., price vs. engine size).
- **Prediction Page:** Input features to predict car price.
- **Widgets:** Dropdowns for brand/model, sliders for year/engine size, image displays.

Insights were communicated using clear visualizations and concise explanations for both technical and non-technical audiences.

## Unfixed Bugs

- Occasional rendering issues with interactive plots in some browsers.
- Some rare outliers in the dataset were not fully addressed due to lack of additional data.

Knowledge gaps were addressed through peer feedback and online resources.

## Development Roadmap

- **Challenges:** Data cleaning, feature selection, model tuning.
- **Strategies:** Iterative testing, peer code reviews.
- **Next Steps:** Explore advanced ML models, deploy dashboard online.

## Main Data Analysis Libraries

- **pandas:** Data manipulation and analysis.
	```python
	import pandas as pd
	df = pd.read_csv('data/car_price_clean.csv')
	```
- **numpy:** Numerical operations.
- **matplotlib/seaborn/plotly:** Data visualization.
- **scikit-learn:** Machine learning models.

## Credits

- Parts of this project, including code, documentation, and ideation, were assisted by AI tools such as OpenAI's ChatGPT and GitHub Copilot.

### Content

- Data cleaning techniques inspired by [Kaggle tutorials](https://www.kaggle.com/).
- EDA and visualization methods adapted from various open-source repositories.
- Data source: https://www.kaggle.com/datasets/hellbuoy/car-price-prediction 

## Acknowledgements

Special thanks to peers, instructors, and the open-source community for their support and feedback throughout this project.


