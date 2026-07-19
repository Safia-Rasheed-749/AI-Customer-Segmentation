import joblib
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


# -------------------------------
# Load Saved Model
# -------------------------------
def load_model():
    return joblib.load("models/kmeans_model.pkl")


# -------------------------------
# Load Saved Scaler
# -------------------------------
def load_scaler():
    return joblib.load("models/scaler.pkl")


# -------------------------------
# Predict Customer Cluster
# -------------------------------
def predict_cluster(age, income, spending):

    model = load_model()
    scaler = load_scaler()

    customer = np.array([[age, income, spending]])

    customer_scaled = scaler.transform(customer)

    cluster = model.predict(customer_scaled)[0]

    return int(cluster)


#Cluster Names

cluster_names = {

    0: "Mature Balanced Customers",

    1: "Young Moderate Customers",

    2: "Potential Customers",

    3: "Premium Customers",

    4: "Young High Spenders",

    5: "Budget Customers"

}


#Segment Details

segment_details = {

    0: {

        "title": "Mature Balanced Customers",

        "description":
        "These customers have moderate income and moderate spending behavior. They are financially stable, make planned purchases, and contribute consistent revenue over time.",

        "characteristics": [

            "Middle-aged customers",

            "Moderate annual income",

            "Moderate spending habits",

            "Stable purchasing behavior",

            "Likely to become long-term loyal customers"

        ],

        "marketing": [

            "Offer personalized promotions based on purchase history.",

            "Introduce loyalty and reward programs.",

            "Provide bundle offers to increase basket size.",

            "Send seasonal and festive promotional campaigns.",

            "Recommend complementary products through cross-selling."

        ],

        "business":
        "Focus on increasing customer lifetime value by strengthening loyalty and encouraging repeat purchases rather than aggressive discounting."

    },


    1: {

        "title": "Young Moderate Customers",

        "description":
        "Young customers with average purchasing power and moderate spending behavior. They represent an important growth segment with long-term business potential.",

        "characteristics": [

            "Young adults",

            "Moderate income",

            "Moderate spending",

            "Technology-oriented",

            "Responsive to digital marketing"

        ],

        "marketing": [

            "Run social media marketing campaigns.",

            "Offer referral and student programs where applicable.",

            "Introduce mobile app exclusive discounts.",

            "Provide limited-time promotional offers.",

            "Use personalized email and push notifications."

        ],

        "business":
        "Build long-term customer relationships early to maximize future customer lifetime value."

    },


    2: {

        "title": "Potential Customers",

        "description":
        "These customers have high income but currently spend relatively little. They have strong purchasing power and represent one of the most valuable growth opportunities.",

        "characteristics": [

            "High income",

            "Low spending",

            "High purchasing potential",

            "Low current engagement",

            "Untapped customer value"

        ],

        "marketing": [

            "Provide personalized premium product recommendations.",

            "Offer exclusive VIP invitations.",

            "Use targeted email marketing campaigns.",

            "Provide premium membership incentives.",

            "Create personalized shopping experiences."

        ],

        "business":
        "The primary objective should be converting these customers into Premium Customers by increasing engagement and purchase frequency."

    },


    3: {

        "title": "Premium Customers",

        "description":
        "These are the highest-value customers with both high income and high spending behavior. They contribute significantly to business revenue and profitability.",

        "characteristics": [

            "High annual income",

            "High spending score",

            "Frequent purchases",

            "High customer lifetime value",

            "Premium buying behavior"

        ],

        "marketing": [

            "Offer VIP membership programs.",

            "Provide exclusive access to new product launches.",

            "Deliver personalized shopping experiences.",

            "Reward loyalty with premium benefits.",

            "Assign dedicated customer support where appropriate."

        ],

        "business":
        "Customer retention should be the highest priority. Retaining premium customers is generally more profitable than acquiring new customers."

    },


    4: {

        "title": "Young High Spenders",

        "description":
        "These customers have relatively low income but spend aggressively. Their purchasing behavior suggests strong interest in shopping, trends, and new products.",

        "characteristics": [

            "Young customers",

            "Lower income",

            "High spending",

            "Trend-driven buyers",

            "Highly engaged shoppers"

        ],

        "marketing": [

            "Promote trending products.",

            "Offer influencer-based marketing campaigns.",

            "Provide installment or flexible payment options where applicable.",

            "Create limited-edition product launches.",

            "Use social media engagement campaigns."

        ],

        "business":
        "Monitor profitability carefully while maintaining engagement. Encourage repeat purchases without relying heavily on discounts."

    },


    5: {

        "title": "Budget Customers",

        "description":
        "These customers have both low income and low spending behavior. They are highly price-sensitive and typically purchase only when they perceive strong value.",

        "characteristics": [

            "Lower annual income",

            "Low spending",

            "Price-sensitive",

            "Value-conscious",

            "Selective purchasing behavior"

        ],

        "marketing": [

            "Offer discounts and promotional coupons.",

            "Create value bundles.",

            "Highlight affordable product ranges.",

            "Provide cashback and savings campaigns.",

            "Advertise budget-friendly deals."

        ],

        "business":
        "Focus on increasing purchase frequency through value-based marketing while maintaining healthy profit margins."

    }
}
#Cluster Visualization

def plot_customer_clusters(income, spending):

    df = pd.read_csv("data/Mall_Customers.csv")

    model = load_model()
    scaler = load_scaler()

    features = df[["Age", "Annual Income (k$)", "Spending Score (1-100)"]]

    scaled_features = scaler.transform(features)

    clusters = model.predict(scaled_features)

    df["Cluster"] = clusters

    colors = [
        "#1f77b4",
        "#ff7f0e",
        "#2ca02c",
        "#d62728",
        "#9467bd",
        "#8c564b"
    ]

    fig, ax = plt.subplots(figsize=(8, 6))

    for cluster in sorted(df["Cluster"].unique()):

        cluster_data = df[df["Cluster"] == cluster]

        ax.scatter(
            cluster_data["Annual Income (k$)"],
            cluster_data["Spending Score (1-100)"],
            s=60,
            color=colors[cluster],
            alpha=0.7,
            label=f"Cluster {cluster}"
        )

    ax.scatter(
        income,
        spending,
        color="black",
        marker="X",
        s=220,
        edgecolors="red",
        linewidths=2,
        label="Current Customer"
    )

    ax.set_title("Customer Location in Segments using K-Means")

    ax.set_xlabel("Annual Income (k$)")

    ax.set_ylabel("Spending Score (1-100)")

    ax.legend()

    ax.grid(alpha=0.3)
    plt.tight_layout()
    return fig