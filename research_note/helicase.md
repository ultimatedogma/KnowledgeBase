# Helicase

Below is a practical “field‑guide” to every *class* of enzyme known to open or otherwise unwind double‑stranded DNA.  For each class I give the main biochemical role and representative members you will meet in bacteria, eukaryotes and viruses.  (Listing every orthologue would run into the hundreds—in humans alone there are 31 different DNA helicases! ([Wikipedia][1]))

---

### 1. ATP‑dependent DNA helicases

Motor proteins that translocate along DNA, using ATP to break the hydrogen bonds between strands.

| Functional group                        | Super‑family / direction\*        | Typical examples & where they act                                                                          |
| --------------------------------------- | --------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| **Replicative “fork” helicases**        | SF4 (5′→3′ hexamer)               | **DnaB** in almost all bacteria; phage **T7 gp4**, **T4 gp41** ([Wikipedia][2])                            |
|                                         | SF6 (3′→5′ hexamer)               | **MCM2‑7/CMG** complex in eukaryotic nuclei; archaeal MCM; mitochondrial **Twinkle** ([Wikipedia][3])      |
|                                         | SF3 viral AAA⁺ (3′→5′ hexamer)    | **SV40 Large T antigen**, papillomavirus **E1**, adeno‑associated **NS1** ([Wikipedia][4])                 |
| **Fork restart & DNA‑repair helicases** | SF1A (3′→5′)                      | **UvrD**, **PcrA**, **Rep** (bacteria); **RecBCD** (bi‑directional) ([Wikipedia][1], [Wikipedia][5])       |
|                                         | SF1B (5′→3′)                      | **Upf1** (eukaryotic genome surveillance)                                                                  |
|                                         | SF2 Fe‑S family (5′→3′)           | **XPD / ERCC2**, **FANCJ/BRIP1**, **DDX11/Chl1**, **RTEL1**, **PIF1** ([Wikipedia][6])                     |
|                                         | SF2 RecQ family (3′→5′)           | **RecQ** (E. coli), human **BLM**, **WRN**, **RECQL4**, **RECQL5**—guard genome stability ([Wikipedia][7]) |
|                                         | Other repair/recombination motors | **RuvAB** branch‑migration helicase, **RecG**, **Srs2**, **FANCM**, **DNA2** (helicase‑nuclease)           |

\*Direction refers to translocation on the tracking (ssDNA) strand.

---

### 2. Helicases embedded in multiprotein machines

| Complex                       | Helicase subunits                   | Function                                                                                                            |
| ----------------------------- | ----------------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| **TFIIH (transcription/NER)** | **XPB** (3′→5′) and **XPD** (5′→3′) | Opens promoter DNA for RNA‑pol II initiation and unwinds lesions during nucleotide‑excision repair ([Wikipedia][6]) |
| **RecBCD**                    | RecB (3′→5′) + RecD (5′→3′)         | Simultaneous unwinding and resection of dsDNA ends in recombinational repair ([Wikipedia][5])                       |

---

### 3. DNA topoisomerases – “torsional unwinders”

These enzymes do not translocate like helicases; instead they make transient breaks to relieve super‑ or overwinding, thereby allowing the duplex ahead of polymerases or helicases to open smoothly.

| Type                          | What it does                                                     | Representative enzymes                                                                             |
| ----------------------------- | ---------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| Type I (single‑strand break)  | Relax positive or negative supercoils                            | Eukaryotic **Topo I**, bacterial **Topo I/III**                                                    |
| Type II (double‑strand break) | Pass one duplex through another, decatenate daughter chromosomes | Eukaryotic **Topo II α/β**, bacterial **DNA gyrase**, **Topo IV** ([Wikipedia][8], [Wikipedia][9]) |
| Type IIB                      | Specialised breakage during meiosis or archaeal replication      | **Spo11**, archaeal **Topo VI**                                                                    |

Topoisomerases do not separate the strands over long tracts, but by eliminating torsional strain they are essential “enablers” of helicase‑driven unwinding ([PubMed Central][10]).

---

### 4. Strand‑displacing DNA polymerases (auxiliary)

Certain polymerases can peel off the downstream strand while synthesising (e.g., phage Φ29 or eukaryotic Pol δ during Okazaki‑fragment maturation), but they work over short regions and are usually assisted by one of the helicases above.

---

## How to use this list

* **Replication studies** – focus on the SF4 (bacteria) or SF6 (eukaryote) helicase plus Topo I/II.
* **DNA repair/recombination** – look at RecQ, Fe‑S helicases, RecBCD/RuvAB, plus Topoisomerase II.
* **Transcription initiation/NER** – TFIIH’s XPB/XPD pair is the key unwinder.
* **Viral systems** – search the viral AAA⁺ hexamer (e.g., SV40 LT) encoded in that virus.

Together these classes cover every enzymatic strategy cells (and viruses) use to open a DNA double helix, whether by direct strand separation or by removing the torsional road‑blocks that prevent it.

[1]: https://en.wikipedia.org/wiki/Helicase "Helicase - Wikipedia"
[2]: https://en.wikipedia.org/wiki/DnaB_helicase?utm_source=chatgpt.com "DnaB helicase"
[3]: https://en.wikipedia.org/wiki/Minichromosome_maintenance?utm_source=chatgpt.com "Minichromosome maintenance"
[4]: https://en.wikipedia.org/wiki/Large_tumor_antigen?utm_source=chatgpt.com "Large tumor antigen"
[5]: https://en.wikipedia.org/wiki/RecBCD?utm_source=chatgpt.com "RecBCD"
[6]: https://en.wikipedia.org/wiki/XPB?utm_source=chatgpt.com "XPB"
[7]: https://en.wikipedia.org/wiki/RecQ_helicase?utm_source=chatgpt.com "RecQ helicase"
[8]: https://en.wikipedia.org/wiki/Topoisomerase?utm_source=chatgpt.com "Topoisomerase"
[9]: https://en.wikipedia.org/wiki/DNA_gyrase?utm_source=chatgpt.com "DNA gyrase - Wikipedia"
[10]: https://pmc.ncbi.nlm.nih.gov/articles/PMC2730144/ "
            DNA topoisomerase II and its growing repertoire of biological functions - PMC
        "
