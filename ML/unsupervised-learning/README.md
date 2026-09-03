# Unsupervised Learning Algorithms

A repository dedicated to Unsupervised Learning algorithms designed for clustering, dimensionality reduction, anomaly detection, and association pattern mining.

---

## 📌 Overview

Unsupervised Learning algorithms process **unlabeled data** ($X$ features only). Without explicit target variables, these models uncover intrinsic spatial geometry, statistical relationships, and structural patterns hidden in complex datasets.

---

## 🚀 Algorithm Directory

### 🧩 Clustering Algorithms

* **K-Means Clustering**
  * Partitions data into $K$ non-overlapping clusters by iteratively minimizing the Within-Cluster Sum of Squares ($\text{WCSS}$).
* **K-Medoids / PAM (Partitioning Around Medoids)**
  * Similar to K-Means, but uses actual data points (medoids) as centers, making it more robust to noise and outliers.
* **Hierarchical Clustering (Agglomerative & Divisive)**
  * Builds a tree-like hierarchy (Dendrogram) of merged clusters based on distance linkage criteria (Single, Complete, Average, Ward).
* **DBSCAN (Density-Based Spatial Clustering of Applications with Noise)**
  * Groups dense regions of data and identifies arbitrarily-shaped clusters while automatically classifying low-density points as noise.
* **OPTICS (Ordering Points To Identify the Clustering Structure)**
  * An extension of DBSCAN that handles clusters of varying densities by creating a reachability plot.
* **Gaussian Mixture Models (GMM)**
  * A probabilistic clustering method assuming data is generated from a mixture of finite Gaussian distributions with unknown parameters (fitted via Expectation-Maximization).

### 📉 Dimensionality Reduction Algorithms

* **Principal Component Analysis (PCA)**
  * Linear technique that projects high-dimensional data onto orthogonal axes that maximize variance.
* **t-SNE (t-Distributed Stochastic Neighbor Embedding)**
  * Non-linear technique optimized for visualizing high-dimensional data by maintaining local point similarities in 2D or 3D space.
* **UMAP (Uniform Manifold Approximation and Projection)**
  * Manifold learning technique that preserves both local and global data structures faster than t-SNE.
* **Linear Discriminant Analysis (LDA) - Unsupervised Projection**
  * Finds linear feature combinations for feature extraction and data compression.

### 🚨 Anomaly & Novelty Detection

* **Isolation Forest**
  * Detects anomalies by isolating instances using random partitioning trees (outliers require fewer splits to isolate).
* **One-Class SVM**
  * Learns a boundary around normal data points to detect novel or out-of-distribution instances.

### 🛒 Association Rule Learning

* **Apriori Algorithm**
  * Identifies frequent itemsets and generates association rules using Support, Confidence, and Lift metrics.
* **FP-Growth (Frequent Pattern Growth)**
  * Mines frequent itemsets without candidate generation by constructing an FP-Tree data structure.

---

## 🛠️ Performance Metrics

* **Clustering:** Silhouette Score, Davies-Bouldin Index, Calinski-Harabasz Index, Within-Cluster Sum of Squares (Elbow Method).
* **Dimensionality Reduction:** Explained Variance Ratio, Reconstruction Error.

---

## 📦 Project Structure

text
unsupervised-learning/
├── clustering/
│   ├── kmeans.py
│   ├── dbscan.py
│   ├── hierarchical.py
│   └── gmm.py
├── dimensionality_reduction/
│   ├── pca.py
│   ├── tsne.py
│   └── umap_model.py
├── anomaly_detection/
│   └── isolation_forest.py
├── requirements.txt
└── README.md
