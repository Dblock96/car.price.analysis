"""
Car Price Analysis Dashboard
Streamlit application for interactive car price analysis and prediction
"""

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, r2_score
import warnings
warnings.filterwarnings('ignore')

# Page configuration
st.set_page_config(
    page_title="Car Price Analysis Dashboard",
    page_icon="🚗",
    layout="wide",
    initial_sidebar_state="expanded"
)

@st.cache_data
def load_data():
    """Load and cache the car price dataset"""
    try:
        df = pd.read_csv('data/car_price_clean.csv')
        return df
    except FileNotFoundError:
        st.error("Dataset not found. Please ensure 'data/car_price_clean.csv' exists.")
        return None

def main():
    st.title("🚗 Car Price Analysis Dashboard")
    st.subheader("Hamza Hackathon Project - Team 3")
    
    # Load data
    df = load_data()
    if df is None:
        st.stop()
    
    # Sidebar navigation
    st.sidebar.title("Navigation")
    page = st.sidebar.selectbox(
        "Choose a page:",
        ["Overview", "Data Exploration", "Price Prediction", "Team Info"]
    )
    
    if page == "Overview":
        show_overview(df)
    elif page == "Data Exploration":
        show_exploration(df)
    elif page == "Price Prediction":
        show_prediction(df)
    elif page == "Team Info":
        show_team_info()

def show_overview(df):
    """Display overview statistics and insights"""
    st.header("📊 Dataset Overview")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Total Cars", len(df))
    
    with col2:
        st.metric("Average Price", f"${df['price'].mean():,.0f}")
    
    with col3:
        st.metric("Price Range", f"${df['price'].max() - df['price'].min():,.0f}")
    
    with col4:
        st.metric("Unique Brands", df['CarName'].nunique() if 'CarName' in df.columns else "N/A")
    
    # Display sample data
    st.subheader("Sample Data")
    st.dataframe(df.head(10))
    
    # Basic statistics
    st.subheader("Statistical Summary")
    st.dataframe(df.describe())

def show_exploration(df):
    """Display data exploration visualizations"""
    st.header("🔍 Data Exploration")
    
    # Price distribution
    st.subheader("Price Distribution")
    fig, ax = plt.subplots(figsize=(10, 6))
    plt.hist(df['price'], bins=30, alpha=0.7, color='skyblue', edgecolor='black')
    plt.xlabel('Price ($)')
    plt.ylabel('Frequency')
    plt.title('Distribution of Car Prices')
    st.pyplot(fig)
    
    # Correlation heatmap
    if len(df.select_dtypes(include=[np.number]).columns) > 1:
        st.subheader("Feature Correlations")
        numeric_cols = df.select_dtypes(include=[np.number]).columns
        corr_matrix = df[numeric_cols].corr()
        
        fig, ax = plt.subplots(figsize=(12, 8))
        sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', center=0, ax=ax)
        plt.title('Feature Correlation Matrix')
        st.pyplot(fig)
    
    # Interactive scatter plot
    st.subheader("Interactive Price Analysis")
    numeric_columns = df.select_dtypes(include=[np.number]).columns.tolist()
    
    if len(numeric_columns) >= 2:
        x_axis = st.selectbox("Select X-axis:", numeric_columns, index=0)
        y_axis = st.selectbox("Select Y-axis:", numeric_columns, 
                             index=numeric_columns.index('price') if 'price' in numeric_columns else 1)
        
        fig = px.scatter(df, x=x_axis, y=y_axis, 
                        title=f'{y_axis} vs {x_axis}',
                        hover_data=['price'] if 'price' in df.columns else None)
        st.plotly_chart(fig, use_container_width=True)

def show_prediction(df):
    """Display price prediction interface"""
    st.header("🎯 Car Price Prediction")
    
    # Prepare data for modeling
    numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()
    
    if 'price' not in numeric_cols:
        st.error("Price column not found in the dataset.")
        return
    
    # Feature selection
    feature_cols = [col for col in numeric_cols if col != 'price']
    
    if len(feature_cols) == 0:
        st.error("No numeric features available for prediction.")
        return
    
    # Model training
    X = df[feature_cols].fillna(df[feature_cols].median())
    y = df['price']
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Train models
    lr_model = LinearRegression()
    rf_model = RandomForestRegressor(n_estimators=100, random_state=42)
    
    lr_model.fit(X_train, y_train)
    rf_model.fit(X_train, y_train)
    
    # Model evaluation
    lr_pred = lr_model.predict(X_test)
    rf_pred = rf_model.predict(X_test)
    
    lr_mae = mean_absolute_error(y_test, lr_pred)
    rf_mae = mean_absolute_error(y_test, rf_pred)
    
    lr_r2 = r2_score(y_test, lr_pred)
    rf_r2 = r2_score(y_test, rf_pred)
    
    # Display model performance
    st.subheader("Model Performance")
    col1, col2 = st.columns(2)
    
    with col1:
        st.metric("Linear Regression MAE", f"${lr_mae:,.0f}")
        st.metric("Linear Regression R²", f"{lr_r2:.3f}")
    
    with col2:
        st.metric("Random Forest MAE", f"${rf_mae:,.0f}")
        st.metric("Random Forest R²", f"{rf_r2:.3f}")
    
    # Feature input for prediction
    st.subheader("Make a Prediction")
    st.write("Enter car features to predict the price:")
    
    input_data = {}
    cols = st.columns(min(3, len(feature_cols)))
    
    for i, feature in enumerate(feature_cols):
        with cols[i % 3]:
            min_val = float(df[feature].min())
            max_val = float(df[feature].max())
            mean_val = float(df[feature].mean())
            
            input_data[feature] = st.slider(
                f"{feature.replace('_', ' ').title()}",
                min_value=min_val,
                max_value=max_val,
                value=mean_val,
                key=f"slider_{feature}"
            )
    
    # Make prediction
    if st.button("Predict Price"):
        input_df = pd.DataFrame([input_data])
        
        lr_prediction = lr_model.predict(input_df)[0]
        rf_prediction = rf_model.predict(input_df)[0]
        
        st.success(f"**Linear Regression Prediction:** ${lr_prediction:,.0f}")
        st.success(f"**Random Forest Prediction:** ${rf_prediction:,.0f}")
        
        avg_prediction = (lr_prediction + rf_prediction) / 2
        st.info(f"**Average Prediction:** ${avg_prediction:,.0f}")

def show_team_info():
    """Display team information and collaboration details"""
    st.header("👥 Hamza Hackathon Project - Team 3")
    
    st.subheader("🎯 Project Mission")
    st.write("""
    Our team is dedicated to building a comprehensive car price analysis tool that provides
    valuable insights for car buyers, sellers, and automotive enthusiasts through data-driven
    analysis and machine learning predictions.
    """)
    
    st.subheader("👨‍💻 Team Members")
    
    # Team member information (to be updated with actual team members)
    team_members = [
        {
            "name": "Hamza",
            "role": "Team Lead & Data Scientist",
            "skills": "Python, Machine Learning, Project Management",
            "github": "hamza-username"
        },
        {
            "name": "Team Member 2",
            "role": "Frontend Developer",
            "skills": "Streamlit, UI/UX, Data Visualization",
            "github": "member2-username"
        },
        {
            "name": "Team Member 3",
            "role": "Data Engineer",
            "skills": "Data Processing, ETL, Database Management",
            "github": "member3-username"
        },
        {
            "name": "Your Name Here",
            "role": "Collaborator",
            "skills": "Add your skills",
            "github": "your-username"
        }
    ]
    
    for member in team_members:
        with st.container():
            col1, col2, col3 = st.columns([1, 2, 2])
            
            with col1:
                st.write(f"**{member['name']}**")
            
            with col2:
                st.write(f"*{member['role']}*")
            
            with col3:
                st.write(f"Skills: {member['skills']}")
                st.write(f"GitHub: @{member['github']}")
            
            st.divider()
    
    st.subheader("🚀 How to Contribute")
    st.write("""
    1. **Fork the repository** on GitHub
    2. **Clone your fork** locally
    3. **Create a feature branch** for your contribution
    4. **Make your changes** following our coding standards
    5. **Test your changes** thoroughly
    6. **Submit a pull request** with a clear description
    
    Check out our CONTRIBUTING.md file for detailed guidelines!
    """)
    
    st.subheader("📋 Current Project Status")
    
    progress_items = [
        ("Data Collection & Cleaning", 100),
        ("Exploratory Data Analysis", 90),
        ("Streamlit Dashboard", 80),
        ("Machine Learning Models", 70),
        ("Documentation", 85),
        ("Testing & Validation", 60),
        ("Deployment Setup", 75)
    ]
    
    for item, progress in progress_items:
        st.write(f"**{item}**")
        st.progress(progress / 100)
        st.write(f"{progress}% Complete")
        st.write("")

if __name__ == "__main__":
    main()