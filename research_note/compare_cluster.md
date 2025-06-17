# Compare clustering methods

Below is a “menu” of the metrics most often used to compare two clusterings $C$ and $C'$ that are defined on **exactly the same $n$ data points**.  I’ve grouped them by how they are computed, then given the key formula, interpretation, range, and typical pros/cons for each.

---

### 1. Pair‑counting family

All of these look at every unordered pair of points $(i,j)$ and ask whether the two clusterings agree on that pair (same cluster vs. different cluster).

| Metric                        | Core idea                                                     | Formula / range                                                                                                                       | When to use                                                              | Pros / Cons                                                               |
| ----------------------------- | ------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------ | ------------------------------------------------------------------------- |
| **Rand Index (RI)**           | Fraction of point‑pairs on which the two clusterings agree.   | $ \text{RI}= \frac{TP+TN}{\binom{n}{2}}$.  Range \[0, 1] (1 = identical).                                                             | Quick sanity check.                                                      | Easy to interpret but **inflated when $k$ is large** (many TNs).          |
| **Adjusted Rand Index (ARI)** | Rand Index corrected for chance agreement.                    | $ \text{ARI}= \frac{\text{RI}-\mathbb E[\text{RI}]}{\max(\text{RI})-\mathbb E[\text{RI}]}$.  Range \[–1, 1] (expected‑by‑chance = 0). | Most cited default in ML papers.                                         | Robust to number of clusters; can be negative for anticorrelation.        |
| **Jaccard Index (pairwise)**  | Ignore TNs; focus on the pairs both clusterings put together. | $ \text{J}= \frac{TP}{TP+FP+FN}$.  Range \[0, 1].                                                                                     | Sensitive when “similarity” = “same cluster”.                            | Penalises over‑splitting more than merging; asymmetric wrt splits/merges. |
| **Fowlkes–Mallows (FM)**      | Geometric mean of pair‑precision and pair‑recall.             | $ \text{FM}= \sqrt{\frac{TP}{TP+FP}\,\frac{TP}{TP+FN}}$.                                                                              | When you care equally about precision & recall for “same‑cluster” pairs. | Harder to interpret absolute scale.                                       |

$TP$, $FP$, $FN$, $TN$ are computed on pair labels “together/different”.

---

### 2. Information‑theoretic family

Treat each clustering as a categorical label vector and measure the information shared between them.

| Metric                            | Core idea                                                             | Formula / range                                                                                      | When to use                                                       | Pros / Cons                                                   |
| --------------------------------- | --------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------- | ------------------------------------------------------------- |
| **Mutual Information (MI)**       | Reduction in uncertainty of one clustering given the other.           | $ \text{MI}(C,C') = \sum_{i,j} \frac{n_{ij}}{n}\log\!\frac{n_{ij}\,n}{n_i\,n'_j}$.  Unbounded above. | Foundation for NMI/AMI.                                           | Raw MI increases with $k$; hard to compare across datasets.   |
| **Normalized MI (NMI)**           | Scale MI to \[0, 1].  Common variant: arithmetic mean normalisation.  | $ \text{NMI}= \frac{\text{MI}}{\bigl(H(C)+H(C')\bigr)/2}$.                                           | Popular in text/image clustering.                                 | Still biased upward when many clusters.                       |
| **Adjusted MI (AMI)**             | MI minus its expected value under random relabeling, then normalized. | $ \text{AMI}= \frac{\text{MI}-\mathbb E[\text{MI}]}{\max-\mathbb E[\text{MI}]}$.  Range \[–1, 1].    | Fair comparison across different $k$ and $n$.                     | More expensive to compute (needs hypergeometric expectation). |
| **Variation of Information (VI)** | Metric distance between clusterings (lower = more similar).           | $ \text{VI}=H(C)+H(C')-2\,\text{MI}(C,C')$. Range \[0, $\log n$].                                    | When you need a true metric to do e.g. clustering of clusterings. | Less intuitive (lower = better).                              |

$H(C) = -\sum_i \frac{n_i}{n}\log\frac{n_i}{n}$ is entropy, $n_{ij}$ is the contingency‑table count.

---

### 3. Assignment‑based family

First find the best one‑to‑one mapping between clusters (Hungarian algorithm), then score the match.

| Metric                                      | Core idea                                                                                  | Formula / range                                                   | When to use                                        | Pros / Cons                                                     |
| ------------------------------------------- | ------------------------------------------------------------------------------------------ | ----------------------------------------------------------------- | -------------------------------------------------- | --------------------------------------------------------------- |
| **Cluster Accuracy / Purity**               | Fraction of points that fall in the mapped “correct” cluster.                              | $ \text{Purity}= \frac{1}{n}\sum_j \max_i n_{ij}$. Range \[0, 1]. | When one clustering is a “ground‑truth” labeling.  | Not symmetric; ignores intra‑cluster errors in larger clusters. |
| **Hungarian‑matched F1 (a.k.a. BCubed F1)** | Compute precision & recall for each point using its mapped cluster, average, then take F1. | Defined in the BCubed paper (Amigó et al., 2009). Range \[0, 1].  | Information‑extraction / entity‑coreference tasks. | Gives each point equal weight; harder to implement.             |

---

### 4. Other notable measures

| Metric                                          | Highlights                                                                                                                                                                                                               |
| ----------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **V‑measure**                                   | Harmonic mean of *homogeneity* (each predicted cluster has only one true label) and *completeness* (all points of a true label are in one predicted cluster).  Equivalent to symmetric NMI with a particular normaliser. |
| **Silhouette overlap**                          | Not common for comparing two clusterings; mainly internal quality vs ground truth, but sometimes used to see how similar the structure implied by two clusterings is.                                                    |
| **Earth Mover’s Distance on cluster centroids** | If clusters have centroids in a metric space, treat each clustering as a weighted empirical distribution and compute Wasserstein distance.  Useful when geometric placement matters, not just membership.                |

---

## How to choose?

1. **Need chance correction?** → Use *ARI* or *AMI* when cluster counts differ or chance agreement is high.
2. **Ground‑truth vs prediction?** → *Purity*, *V‑measure*, or assignment F1.
3. **Want a true metric distance?** → *Variation of Information* (can be input to hierarchical clustering of clusterings).
4. **Pairwise interpretation appealing?** → *Jaccard* or *Fowlkes–Mallows* give precision‑recall style control.

In practice, libraries such as **`sklearn.metrics`** in Python implement ARI, NMI/AMI, Fowlkes–Mallows, mutual‑information variants, etc., so you can compute several and see which resonates with your domain’s notion of “similar”.

