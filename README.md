# 🛍️ AI Customer Segmentation System

An end-to-end Machine Learning application that segments retail customers into meaningful groups using **K-Means Clustering**. The project includes a professionally designed **Streamlit dashboard** where users can enter customer information and instantly identify the customer's segment along with detailed business insights and marketing recommendations.

## 📌 Project Overview

Customer segmentation helps businesses understand different customer groups based on their purchasing behavior. Instead of treating every customer the same, businesses can design personalized marketing campaigns, improve customer satisfaction, and increase revenue.

This project uses **unsupervised machine learning (K-Means Clustering)** to automatically identify customer segments based on:

- Age
- Annual Income
- Spending Score

The trained model is deployed through an interactive Streamlit web application.

---

# 🚀 Live Features

- Predict customer segment instantly
- Interactive Streamlit dashboard
- Professional UI
- Data preprocessing pipeline
- Feature scaling using StandardScaler
- K-Means clustering model
- Cluster visualization
- Current customer visualization
- Customer segment descriptions
- Business characteristics
- Marketing strategies
- Business recommendations

# 📊 Dataset

Dataset: **Mall Customers Dataset**
https://www.kaggle.com/datasets/vjchoudhary7/customer-segmentation-tutorial-in-python

Features used:

- Age
- Annual Income (k$)
- Spending Score (1–100)

Rows: **200**

# 🧠 Machine Learning Workflow

## 1. Data Preprocessing

- Removed unnecessary columns
- Selected relevant features
- One-Hot Encoding experiment on Gender(gender_feature_exp.ipynb)
- Feature Scaling using StandardScaler

## 2. Finding Optimal Number of Clusters

Two evaluation techniques were used:

- Elbow Method
- Silhouette Score

After comparing both methods and visual inspection, the final value selected was:

**K = 6**

## 3. Model Training

Algorithm:

- K-Means Clustering

Libraries:

- Scikit-Learn

## 4. Model Saving

The trained model and scaler are saved using **Joblib**.

Saved files:

- kmeans_model.pkl
- scaler.pkl

---

# 🎯 Customer Segments

The trained model identifies six customer groups:

| Cluster | Customer Segment |
|----------|------------------|
| 0 | Mature Balanced Customers |
| 1 | Young Moderate Customers |
| 2 | Potential Customers |
| 3 | Premium Customers |
| 4 | Young High Spenders |
| 5 | Budget Customers |

# 📈 Business Insights

The application provides:

- Customer segment prediction
- Customer characteristics
- Business interpretation
- Marketing strategy
- Personalized recommendations

This transforms raw clustering results into actionable business intelligence.

# 💻 Technologies Used

- Python
- Streamlit
- Scikit-Learn
- Pandas
- NumPy
- Matplotlib
- Joblib

# ▶️ Run Locally

Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/AI-Customer-Segmentation.git
```

Move into the project directory

```bash
cd AI-Customer-Segmentation
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
streamlit run app.py
```
This streamlit app is deployed on streamlit community cloud
## 🚀 Live Demo

Check out the deployed application here:  
👉 **[AI Customer Segmentation Dashboard](https://ai-customer-segmentation-eerzfgt6ntqzk3tsbmdn6j.streamlit.app/)**

# 📷 Application Preview

Please have a look on images in images folder

# 📚 Learning Outcomes

Through this project, I gained practical experience in:

- Unsupervised Machine Learning
- K-Means Clustering
- Feature Engineering
- Feature Scaling
- Elbow Method
- Silhouette Score
- Model Serialization
- Streamlit Application Development
- Data Visualization
- Business Intelligence
- Git & GitHub
- Machine Learning Deployment

# 👩‍💻 Author

**Safia Rasheed**

BS Computer Science

Machine Learning | Data Science | Python | Streamlit

---

## ⭐ If you found this project useful, consider giving it a star!