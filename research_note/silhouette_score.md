# Silhouette Score

Related link:

- [Wikipedia](https://en.wikipedia.org/wiki/Silhouette_(clustering))
- [Medium](https://medium.com/@hazallgultekin/what-is-silhouette-score-f428fb39bf9a)

The Silhouette score is a metric used to evaluate how good clustering results are in data clustering. This score is calculated by measuring each data point’s similarity to the cluster it belongs to and how different it is from other clusters. The Silhouette score is commonly used to assess the performance of clustering algorithms like K-Means.


When calculating the Silhouette score, the following steps are followed:

1. For each data point, the average distance ($a_i$) to other data points within the same cluster is calculated. This value represents the similarity level of the data point to others in its cluster.

2. For each data point, the average distance ($b_i$) to all other clusters it doesn’t belong to is computed. This value indicates how different the data point is from data points in other clusters.

3. The Silhouette score is calculated using the formula: 

$$
\text{Silhouette Score} = \frac{b_i — a_i}{max(a_i, b_i)}
$$

4. By taking the average of the Silhouette scores calculated for each data point, an overall Silhouette score is obtained, which measures the success of clustering results.


It ranges from -1 to +1:

- Positive values indicate that data points belong to the correct clusters, indicating good clustering results.
- A score of zero suggests overlapping clusters or data points equally close to multiple clusters.
- Negative values indicate that data points are assigned to incorrect clusters, indicating poor clustering results.



Range of SC	Interpretation, [Source](https://www.stat.berkeley.edu/users/spector/s133/Clus.html)

| Range of SC | Interpretation |
|------------|----------------|
| 0.71-1.0   | A strong structure has been found |
| 0.51-0.70  | A reasonable structure has been found |
| 0.26-0.50  | The structure is weak and could be artificial |
| < 0.25     | No substantial structure has been found |

