import pandas as pd
df = pd.read_csv("data/Mall_Customers.csv")
print(df.head())

print('\n Info')
print(df.info())

print('\n Statistics')
print(df.describe(include = 'all'))

print('\n Missing Values Count per column')
print(df.isnull().sum())
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('whitegrid')
# Histograms for numerical columns
df[['Age', 'Annual Income (k$)', 'Spending Score (1-100)']].hist(bins=20, figsize=(12, 6))
plt.show()

# Box plots to check outliers
plt.figure(figsize=(10, 5))
sns.boxplot(data=df[['Age', 'Annual Income (k$)', 'Spending Score (1-100)']])
plt.show()
plt.figure(figsize=(8,6))

sns.scatterplot(
    data=df,
    x="Annual Income (k$)",
    y="Spending Score (1-100)"
)

plt.title("Annual Income vs Spending Score")
plt.xlabel("Annual Income (k$)")
plt.ylabel("Spending Score (1-100)")

plt.show()
plt.figure(figsize=(8,6))

sns.scatterplot(
    data=df,
    x="Age",
    y="Spending Score (1-100)"
)

plt.title("Age vs Spending Score")
plt.xlabel("Age")
plt.ylabel("Spending Score")

plt.show()
df = df.drop("CustomerID", axis=1)

df.head()
numerical_features = df[["Age", "Annual Income (k$)", "Spending Score (1-100)"]]

numerical_features.head()

from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()

scaled_features = scaler.fit_transform(numerical_features)
print(scaled_features[:5])
# Elbow graph
from sklearn.cluster import KMeans
wcss = []

for k in range(1, 11):
    kmeans = KMeans(
        n_clusters=k,
        init='k-means++',
        random_state=42,
        n_init=10
    )

    kmeans.fit(scaled_features)

    wcss.append(kmeans.inertia_)

plt.figure(figsize=(8,5))
plt.plot(range(1, 11), wcss, marker='o')

plt.title("Elbow Method")
plt.xlabel("Number of Clusters (K)")
plt.ylabel("WCSS (Inertia)")

plt.show()
# silhouette_score
from sklearn.metrics import silhouette_score

silhouette_scores = []

for k in range(2, 11):   # Silhouette Score is not defined for K=1

    kmeans = KMeans(
        n_clusters=k,
        init='k-means++',
        random_state=42,
        n_init=10
    )

    labels = kmeans.fit_predict(scaled_features)

    score = silhouette_score(scaled_features, labels)

    silhouette_scores.append(score)

    print(f"K = {k}, Silhouette Score = {score:.4f}")
# Model Training
kmeans = KMeans(
    n_clusters=6,
    init='k-means++',
    random_state=42,
    n_init=10
)

clusters = kmeans.fit_predict(scaled_features)

df["Cluster"] = clusters

df.head()
# Centroids Calculations
centroids = kmeans.cluster_centers_

print(centroids)
centroids_original = scaler.inverse_transform(centroids)

print(centroids_original)
# Centroids Visualization
import matplotlib.pyplot as plt

plt.figure(figsize=(10,6))

# Customers
plt.scatter(
    df["Annual Income (k$)"],
    df["Spending Score (1-100)"],
    c=df["Cluster"],
    cmap="viridis",
    s=70,
    label="Customers"
)

# Centroids
plt.scatter(
    centroids_original[:,1],   # Income
    centroids_original[:,2],   # Spending
    c="red",
    s=300,
    marker="X",
    edgecolors="black",
    label="Centroids"
)

plt.xlabel("Annual Income (k$)")
plt.ylabel("Spending Score (1-100)")
plt.title("Customer Segments with Centroids")
plt.legend()

plt.show()
# For Business Analysis
cluster_summary = df.groupby("Cluster").agg(
    Average_Age=("Age", "mean"),
    Average_Income=("Annual Income (k$)", "mean"),
    Average_Spending=("Spending Score (1-100)", "mean"),
    Number_of_Customers=("Cluster", "size")
)

cluster_summary
# dictionary
cluster_names = {
    0: "Mature Balanced Customers",
    1: "Young Moderate Customers",
    2: "Potential Customers",
    3: "Premium Customers",
    4: "Young High Spenders",
    5: "Budget Customers"
}
df["Customer Segment"] = df["Cluster"].map(cluster_names)
df.head(10)
# Saving
import joblib

joblib.dump(kmeans, "models/kmeans_model.pkl")
joblib.dump(scaler, "models/scaler.pkl")
