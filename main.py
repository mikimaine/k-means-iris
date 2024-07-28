import pandas as pd
from sklearn.datasets import load_iris
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt


iris = load_iris()
X = iris.data
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)


def calculate_sse(X, k_values):
    sse = []
    for k in k_values:
        kmeans = KMeans(n_clusters=k, random_state=42)
        kmeans.fit(X)
        sse.append(kmeans.inertia_)
    return sse


# Values of k to test
k_values = [3, 4, 5, 6, 7, 8, 9, 10, 12, 15]

# Calculate SSE for each k
sse = calculate_sse(X_scaled, k_values)

# Create a dataframe to store the results
results_df = pd.DataFrame({
    'Experiment Number': range(1, len(k_values) + 1),
    'Value of k': k_values,
    'SSE Value': sse
})

# Plotting the SSE values to find the elbow point
plt.figure(figsize=(10, 6))
plt.plot(k_values, sse, marker='o')
plt.title('SSE for different values of k')
plt.xlabel('Number of clusters (k)')
plt.ylabel('Sum of Squared Error (SSE)')
plt.xticks(k_values)
plt.grid(True)
print(results_df)
plt.show()
