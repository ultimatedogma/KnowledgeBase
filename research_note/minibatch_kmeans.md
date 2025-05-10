# Mini-batch K-means

# Theory

Thought for 4 seconds


### Intuition in one sentence

Mini‑batch $k$-means keeps the **exact same objective** as vanilla $k$-means (minimise the sum of squared distances to centroids) but **approximates every iteration** with a tiny, randomly sampled subset of points—so each update is noisy but extremely cheap.

---

## Step‑by‑step algorithm

| Step                                                                                                                                                                                                                                                                                                                                                                                                                  | What happens                                                                                                            | Why it’s fast                                 |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------- | --------------------------------------------- |
| 1. **Initialise $k$ centroids**<br>*(k‑means++ or random)*                                                                                                                                                                                                                                                                                                                                                            | Gives a reasonable starting guess                                                                                       | Done once on the full data                    |
| 2. **Draw a mini‑batch** of `batch_size` samples *without* replacement                                                                                                                                                                                                                                                                                                                                                | Reduces the working set from $n$→`batch_size`                                                                           | Memory & CPU ∝ `batch_size`, not $n$          |
| 3. **Assign the mini‑batch points** to their nearest centroids                                                                                                                                                                                                                                                                                                                                                        | Standard nearest‑neighbour step                                                                                         | Only `batch_size × k` distance checks         |
| 4. **Update the touched centroids** using a **running average**<br>For each centroid $c_j$ that received at least one point $x$:  $N_j \leftarrow N_j + 1$  $c_j \leftarrow c_j + \frac{1}{N_j}\,( \bar{x}_j - c_j )$  where $N_j$ is the *total* number of mini‑batches that have ever assigned at least one sample to $c_j$ and $\bar{x}_j$ is the mean of the samples in the current mini‑batch assigned to $c_j$. | Updates cost $O(kd)$ not $O(nd)$.  The $1/N_j$ term makes old and new data contribute **equally over time** (unbiased). |                                               |
| 5. **Repeat 2–4** for a fixed number of iterations *or* until the centroids stabilise                                                                                                                                                                                                                                                                                                                                 |                                                                                                                         | Stops once inertia or centroid shift plateaus |

*(This is essentially the algorithm described by Sculley, 2010—the basis of scikit‑learn’s `MiniBatchKMeans`.)*

---

## Key differences from full $k$-means

| Full $k$-means (Lloyd’s)                          | Mini‑batch $k$-means                                 |
| ------------------------------------------------- | ---------------------------------------------------- |
| **Whole data** at every iteration                 | Random subset (`batch_size`)                         |
| Exact centroid update (mean of whole cluster)     | **Stochastic** update (running mean)                 |
| Converges in few iterations but each is expensive | Needs many more iterations, but each is milliseconds |
| Memory ≥ $O(n + kd)$                              | Memory ≈ `batch_size × d + kd` (independent of $n$)  |

---

## Convergence behaviour

* Mini‑batch is a **stochastic approximation** to Lloyd’s algorithm.
* With diminishing learning rates $1/N_j$ it is an **unbiased estimator** of the true centroid and converges (almost surely) to a local minimum of the k‑means objective, though typically not quite as low as full $k$-means.
* In practice the loss plateaus quickly; you stop when extra mini‑batches no longer reduce inertia meaningfully.

---

## Complexity cheat‑sheet

| Symbol | Meaning                             |
| ------ | ----------------------------------- |
| $n$    | total samples                       |
| $d$    | dimensions                          |
| $k$    | clusters                            |
| $b$    | `batch_size`                        |
| $T$    | iterations (mini‑batches processed) |

*Time*: $O(T\,b\,k\,d)$ (Compare to $O(n\,k\,d)$ per iteration for full $k$-means.)
*Memory*: $O(b\,d + k\,d)$ (vs. $O(n\,d + k\,d)$.)

Because $b\ll n$, large datasets fit in RAM and iterations are fast.

---

## Practical tips

* **Batch size**: start with `max(10 k, 1024)` and keep ≤ 1–2 % of $n$ (details in the previous answer).
* **Shuffling** the data once and scanning sequentially often suffices; strict random sampling isn’t mandatory.
* **Reassignment**: if a centroid gets no points for many mini‑batches, re‑seed it to a random sample—prevents “empty” clusters.
* **Early stopping**: track the moving average of inertia on the processed mini‑batches; stop when relative improvement falls below (say) 1 e‑4.
* **Evaluation**: after training, compute inertia on the *full* dataset once to judge final quality.

---

### When to choose mini‑batch $k$-means

| Use it when…                                                              | Avoid if…                                                                           |
| ------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- |
| Dataset is too large to fit in memory or full $k$-means is painfully slow | You require the absolutely lowest possible inertia (e.g., sensitive downstream use) |
| You need rapid, repeated clustering during model selection                | $k$ is small and $n$ is modest (< 50 k); full $k$-means may already be fast         |

---

> **Bottom line:** Mini‑batch $k$-means trades a *bit* of clustering quality for **drastic gains** in speed and memory, making $k$-means feasible on millions of points with ordinary hardware.



# Batch size discussion

Thought for a few seconds


`batch_size` controls how many samples are pulled from your data‑set at every update step.  It is one of the few “knobs” you have when using mini‑batch $k$-means, and it drives a three‑way trade‑off:

| if `batch_size` is … | memory per step | time per step | convergence quality\*          |
| -------------------- | --------------- | ------------- | ------------------------------ |
| **small (≤ k)**      | very low        | very fast     | noisy, may stall               |
| **medium (≈ 10 k)**  | moderate        | fast          | usually best balance           |
| **large (≫ 10 k)**   | high            | slower        | smooth but diminishing returns |

\*“Quality” here means both the final inertia (within‑cluster SSE) and the stability of the centroids.

---

### Practical heuristics

1. **Start with `10 × n_clusters` (or `1024`, whichever is larger)**

   * This is the current scikit‑learn default (`batch_size=1024`) and is rarely far off for typical tabular data.

2. **Keep it at most 1–2 % of the whole data‑set**

   * Beyond that you lose the computational savings of mini‑batch and approach full K‑Means.

3. **Never use a batch smaller than `n_clusters`**

   * Otherwise some clusters will go unseen in many updates and drift.

4. **Scale with dimensionality**

   * High‑dimensional, sparse data (e.g. text TF‑IDF) benefits from slightly larger batches (2–4 × above the rule of thumb) to smooth out the noise in empty features.

5. **Profile, don’t guess**

   * Measure elapsed time vs. final inertia for a few candidate sizes (e.g. 0.5×, 1×, 2×, 4× your starting guess).  Pick the knee of the curve where inertia stops improving meaningfully per extra second of compute.

---

### Quick recipe (scikit‑learn)

```python
from sklearn.cluster import MiniBatchKMeans

n_clusters = 100
n_samples  = X.shape[0]

# Rule‑of‑thumb starting point
batch = max(10 * n_clusters, 1024)
batch = min(batch, int(0.02 * n_samples))   # cap at 2 % of data

mbk = MiniBatchKMeans(n_clusters=n_clusters,
                      batch_size=batch,
                      max_iter=100,
                      random_state=0).fit(X)
```

---

### When to increase the batch

* Inertia stops dropping after many iterations (oscillates).
* You see empty clusters frequently being re‑seeded.
* Data are very sparse or each point is extremely high‑dimensional.

### When to decrease the batch

* You hit RAM limits or swap.
* Iterations become your bottleneck rather than the number of iterations.
* Mini‑batch quickly reaches a plateau similar to full $k$-means, so extra samples provide little benefit.

---

### Bottom line

* **Batch too small →** fast but unstable; clusters may wander.
* **Batch too large →** safe but slow; might as well switch to full $k$-means.
* **Batch \~ 10 k (or \~ 1 %–2 % of data) →** sweet spot on most problems.

Treat `batch_size` like a hyper‑parameter: start with the heuristic, then tune on a small validation set for the best speed‑versus‑quality trade‑off.
