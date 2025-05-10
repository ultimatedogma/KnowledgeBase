# BLAST

## E-value

**BLAST E‑value (expect value)**
The E‑value is the number of alignments with a score *S* or better that you would **expect to find by chance** when searching a database of a given size.

---

### Formal definition

For an alignment that achieves raw score *S*, the expected number of high‑scoring segment pairs (HSPs) with score ≥ *S* in a random database is

$$
E = K\,m\,n \; e^{-\lambda S}
$$

| Symbol   | Meaning                                                                                                            |
| -------- | ------------------------------------------------------------------------------------------------------------------ |
| *m*      | effective length of the query (in residues or nucleotides)                                                         |
| *n*      | effective length of the database                                                                                   |
| *K*, *λ* | statistical parameters that depend on the scoring system (substitution matrix, gap costs) and sequence composition |

These parameters are estimated internally by BLAST each time it runs.

---

### How to read it

* **Smaller E‑value ⇒ less likely the match is due to chance**
  *E = 1×10⁻⁵* means you would expect 1 such hit in 100 000 random searches; *E = 0* (reported when the value is below the machine’s floating‑point precision) indicates an essentially unique match.

* **Database‑size dependent**
  If you search a larger database, *n* rises, so the E‑value for the same alignment score increases.

* **Not a probability**
  The E‑value is an **expectation count**, not a probability between 0 and 1. The related probability (*p*-value) is

  $$
  P = 1 - e^{-E}\;(\approx E \text{ when } E\ll 1)
  $$

---

### Practical thresholds

| Typical cutoff      | Interpretation                                           |
| ------------------- | -------------------------------------------------------- |
| **E ≤ 1e‑5**        | Strong evidence of homology (commonly used for proteins) |
| **1e‑5 < E ≤ 1e‑2** | Possibly homologous; inspect alignment biology           |
| **E > 1e‑2**        | Likely a chance match for large databases                |

Choose cutoffs in context: shorter queries, low‑complexity regions, or very large databases may require stricter thresholds.

---

**In short:** the BLAST E‑value tells you how many equally good or better hits you would expect to see *just by random chance*. The lower it is, the more biologically meaningful your alignment is likely to be.
