# Quantum Chemistry

Q: 解释一下量子力学中的电子密度矩阵是什么意思




**Explaining the electronic density matrix**

The user wants an explanation of the electronic density matrix in quantum mechanics. This is a concept in quantum physics and chemistry, often used to describe quantum states, especially in the context of electron density.

I’ll give a simple yet detailed answer, focusing on its physical meaning, making sure to cover the mathematical definition, its relationship with wavefunctions and density operators, and key properties like trace and idempotency, pure vs. mixed states, and how it applies to quantum chemistry, especially in one-particle density matrix form.


Thought for 8 seconds


**电子密度矩阵（density matrix）是什么？**

在量子力学里，所有可观测量都源自于“态”的信息。

* 如果体系处于一个确定的纯态 $|\Psi\rangle$，我们通常用波函数或态矢 $|\Psi\rangle$ 来描述它。
* 但更一般的情况（例如含有统计混合、退相干或仅关注部分粒子时）需要一种能同时处理“纯态”与“混合态”的统一语言——这就是**密度算符 $\hat{\rho}$**。在给定一组正交基 $\{|i\rangle\}$ 下，$\hat{\rho}$ 的矩阵元

$$
\rho_{ij}=\langle i|\hat{\rho}|j\rangle
$$

就构成了**密度矩阵**。

---

### 1. 电子密度矩阵的数学定义

对于 $N$ 电子体系，最常用的是**一阶（单粒子）约化密度矩阵**：

$$
\gamma(\mathbf{r},\mathbf{r'})=
N\int d\mathbf{r}_2\cdots d\mathbf{r}_N\;
\Psi^*(\mathbf{r'},\mathbf{r}_2,\dots,\mathbf{r}_N)\;
\Psi(\mathbf{r},\mathbf{r}_2,\dots,\mathbf{r}_N).
$$

* **对角元** $\gamma(\mathbf{r},\mathbf{r})=\rho(\mathbf{r})$ 就是熟悉的**电子空间密度**：在 $\mathbf{r}$ 处找到电子的概率分布。
* **非对角元** $\gamma(\mathbf{r},\mathbf{r'})$ 含有相干（量子干涉）信息；它告诉我们“电子同时出现在 $\mathbf{r}$ 与 $\mathbf{r'}$ 的相位关联”，在凝聚态与量子化学中用来衡量键合、轨道占据等性质。

在轨道基 $\{\phi_\mu(\mathbf{r})\}$ 上，这一表达变为离散矩阵形式

$$
\gamma_{\mu\nu}= \sum_{\text{占据轨道 }i} C_{\mu i}C_{\nu i}^* \quad\text{(Hartree–Fock 纯态)}
$$

或更一般地

$$
\gamma_{\mu\nu}= \sum_{i} n_i\, C_{\mu i}C_{\nu i}^*,\quad 0\le n_i\le 1
$$

其中 $n_i$ 是**自然轨道占据数**，允许混合态（相关电子体系）。

---

### 2. 物理意义

| 角度         | 解释                                                                                       |
| ---------- | ---------------------------------------------------------------------------------------- |
| **统计**     | $\gamma$ 把“在哪儿有多少电子”与“它们之间的量子相关”编码到同一个对象里。                                               |
| **可观测量**   | 任何一体算符 $\hat{O}=\sum_k \hat{o}(k)$ 的期望值可写成 $\mathrm{Tr}[\gamma\,o]$，计算效率高于直接用 $N$-电子波函数。 |
| **纯/混态判据** | 若 $\gamma^2=\gamma$（幂等），体系是一体纯态（例如单行列式）。若迹仍为 $N$ 但不幂等，则包含电子相关或统计混合。                      |
| **化学键**    | 非对角元大小反映不同轨道或原子之间的电子共享，常用于键级、共价性分析（Mulliken、DM-NOCI 等）。                                  |

---

### 3. 与常见理论的联系

* **Hartree–Fock (HF)**：$\gamma$ 由占据轨道完全决定且幂等；能量表达式 $E[\gamma]$ 只依赖 $\gamma$。
* **密度泛函理论 (DFT)**：最终只需要对角密度 $\rho(\mathbf{r})$；但许多改进泛函（如依赖动量密度或严格相关电子的 Kohn–Sham 派生物）仍会用到 $\gamma$。
* **多参考/相关方法（CI, CC, DMFT 等）**：$\gamma$ 不再幂等；占据数 $n_i$ 反映电子相关强度，0–1 之间的分数为“部分占据”轨道。
* **固体物理**：布洛赫函数基下的 $\gamma_{\mathbf{k}n,\mathbf{k}'n'}$ 与 Berry 相位、拓扑不变量等相连。

---

### 4. 关键性质速览

1. **自伴 (Hermitian)**：$\gamma^\dagger=\gamma$。
2. **迹为粒子数**：$\mathrm{Tr}\,\gamma = N$。
3. **半正定**：所有本征值 $n_i\ge 0$。
4. **幂等性**：纯单体态时 $\gamma^2=\gamma$。
5. **相似变换不变**：可在任意完备轨道基表示。

---

### 5. 通俗类比

* **照片 vs. 视频**：波函数像一段全息视频，包含所有粒子全部的瞬时相位信息；密度矩阵像把视频压缩成“多维直方图”，对我们关心的粒子子集保留必要统计与相干，而忽略无关细节。
* **阴影**：高维 $N$-电子波函数对其余电子积分后，投影到单电子子空间；密度矩阵就是这种“阴影投影”的数学描述。

---

**总结**
电子密度矩阵是量子体系“可观测信息”的集中载体：它比单纯的电子密度更完整，又比全多体波函数更简洁。在量子化学、凝聚态物理乃至量子信息的实际计算中，许多能量、力以及化学键性质都可以直接从密度矩阵获得，因而成为分析电子结构和量子相关不可或缺的工具。

Q: 对于DFT方法，是不是电子密度的建模方式就不一样了？是什么样的





**Explaining DFT electron density modeling**

The user asks about the modeling of electron density in density functional theory (DFT), specifically how it's different from the electron density matrix. DFT focuses on the electron density ρ(r) as the fundamental variable, which defines the ground-state energy. This contrasts with previous methods that used the density matrix. I'll need to explain the Kohn-Sham formalism and the Hohenberg-Kohn theorems. To ensure accuracy, I'll gather up-to-date references from reliable sources. Let's proceed with a quick search!


**Explaining DFT vs density matrix modeling**

The user is asking about the difference in electron density modeling in DFT methods. In DFT, electron density ρ(r) is the central variable, and the ground-state energy is a functional of ρ, which contrasts with older methods that used the electron density matrix. The Kohn-Sham formalism is key here. To provide an accurate and detailed answer, I’ll explore the Kohn-Sham theory and the Hohenberg-Kohn theorems and ensure proper citations. Let’s get started on the explanation in Chinese with those references!


Thought for 25 seconds


### 在 DFT 里，电子“态”不再用密度矩阵，而是用 **电子空间密度 ρ(𝐫)** 作为唯一基本变量

| 传统多体方法                            | DFT 中的做法                             |
| --------------------------------- | ------------------------------------ |
| 需要完整 $N$ 电子波函数或一阶/二阶密度矩阵，维度随电子数爆炸 | 只需三维实函数 $ρ(\mathbf r)$，维度与体系大小**无关** |

---

#### 1. 为何能只看 $ρ(\mathbf r)$？——Hohenberg–Kohn 定理

1. **第一定理**：给定基态密度 $ρ_0(\mathbf r)$（满足粒子数守恒），外加势 $v_\text{ext}(\mathbf r)$ 以及相应的所有基态性质都被唯一确定。
2. **第二定理**：存在一个泛函 $E[ρ]$ 使得其最小值等于体系基态能量，最小化时得到正确的 $ρ_0$。([UCSB Chemistry People][1], [kthpanor.github.io][2])

> 这意味着只要能写出“能量 vs. 密度”的正确表达式，就无需再保留密度矩阵的非对角信息。

---

#### 2. Kohn–Sham 方案：把困难隐藏在交换‑相关泛函

直接写 $E[ρ]$ 很难，于是 Kohn 和 Sham 引入一个**非相互作用的辅助体系**，要求它产生同样的 ρ：

$$
\left[-\frac{1}{2}\nabla^2 + v_\text{eff}[ρ](\mathbf r)\right]\phi_i(\mathbf r)=\varepsilon_i\phi_i(\mathbf r),
\quad ρ(\mathbf r)=\sum_i^{\text{occ}}|\phi_i(\mathbf r)|^2
$$

* $v_\text{eff}=v_\text{ext}+v_H[ρ]+v_{xc}[ρ]$
* $v_H$ 是经典库仑势；
* **$v_{xc}[ρ]$**（交换‑相关势）把所有多体量子效应收进去。([Wikipedia][3], [Wikipedia][4])

求解步骤是自洽的 SCF 循环：

1. 猜 ρ$^\text{(0)}$→构造 $v_\text{eff}$
2. 解 K‑S 方程得 $\{\phi_i\}$→更新新 ρ
3. 迭代直到 ρ 收敛。

---

#### 3. 电子密度的常见“建模”层级

| 层级            | 泛函示例         | 依赖信息            | 适用场景       |
| ------------- | ------------ | --------------- | ---------- |
| LDA  (局域密度近似) | Dirac‑Slater | ρ               | 均匀电子气、简单固体 |
| GGA  (梯度修正)   | PBE, BLYP    | ρ, ∇ρ           | 分子化学、表面    |
| meta‑GGA      | SCAN         | ρ, ∇ρ, τ (动能密度) | 兼顾分子与固体    |
| 混合泛函          | B3LYP, PBE0  | ρ + 少量 HF 交换    | 激发能隙、反应势垒  |
| 逸电子校正         | D3, VV10     | ρ + 经验伦纳德‑琼斯    | 范德华、层状材料   |

> 不论层级多高，本质仍只需 ρ；任何额外轨道信息（动能密度 τ 等）都是从 K‑S 轨道 **后处理** 得到的辅助量，并不会恢复完整的密度矩阵相干信息。

---

#### 4. 与密度矩阵方法的差异与联系

| 观测量                       | DFT                                                                              | 密度矩阵方法                                 |
| ------------------------- | -------------------------------------------------------------------------------- | -------------------------------------- |
| 一体算符 $\hat O=\sum_k o(k)$ | $\displaystyle \langle\hat O\rangle=\int ρ(\mathbf r)\,o(\mathbf r)\,d\mathbf r$ | $\displaystyle \mathrm{Tr}[\gamma\,o]$ |
| 电子相关                      | 全部吸收进 $E_{xc}[ρ]$，用近似泛函处理                                                        | 显式出现在 $\gamma$ 非幂等或在二阶密度矩阵             |
| 计算量                       | 与电子数近线性（对每步迭代解单粒子方程）                                                             | Hartree‑Fock‑like $N^4$‑$N^5$          |
| 可得信息                      | 基态能量、力、部分激发态 (TD‑DFT)                                                            | 更丰富的相干与多体信息（可直接导出占据数、自然轨道）             |

**所以**：DFT 并不是“改造”了密度矩阵，而是从根本上**抛弃**了对非对角元的需求，用一个三维密度场加上一套近似泛函来描述所有基态性质。这种极大简化使得 DFT 成为今天最常用的电子结构方法之一。

[1]: https://people.chem.ucsb.edu/metiu/horia/OldFiles/115C/KH_Ch4.pdf?utm_source=chatgpt.com "[PDF] 4 The Hohenberg-Kohn Theorems"
[2]: https://kthpanor.github.io/echem/docs/elec_struct/hohenberg.html?utm_source=chatgpt.com "Hohenberg–Kohn theorems"
[3]: https://en.wikipedia.org/wiki/Kohn%E2%80%93Sham_equations?utm_source=chatgpt.com "Kohn–Sham equations - Wikipedia"
[4]: https://en.wikipedia.org/wiki/Density_functional_theory?utm_source=chatgpt.com "Density functional theory - Wikipedia"


Q: 再解释一下什么是泛函，包括不同的基组等等




**Explaining functionals and basis sets**

The user wants another explanation of functionals in the context of Density Functional Theory (DFT) and its application in quantum chemistry, covering basis sets too. I'll need to explain what a functional is — mapping electron density (or spin density) to energy — and mention the types of functionals like LDA, GGA, hybrid, meta-GGA, etc. I'll also touch upon basis sets, such as Gaussian, Slater, and more. Different types, like split-valence and correlation-consistent, will need a discussion of trade-offs and selection criteria.

**Exploring DFT functionals and basis sets**

The user has asked about functionals and basis sets in DFT. I'll provide an explanation of functionals and how they're used in quantum chemistry, including familiar types like LDA, GGA, hybrid functionals, and examples such as PBE and B3LYP. For basis sets, I'll discuss important families like Gaussian (e.g., Pople, Dunning), and Slater-type, as well as errors like BSSE. Additionally, I’ll look up the latest advancements in functionals and basis sets for 2024 and 2025 to provide updated information.


**Explaining functionals and basis sets**

I'm outlining a breakdown of functionals and basis sets. First, I'll clarify the math definition of functionals vs. their role in quantum chemistry. Then, I'll describe common families of exchange-correlation functionals. For basis sets, I’ll cover various types, such as Gaussian (Pople, Dunning), Slater-type, and plane-wave, and talk about concepts like split-valence and correlation-consistent sets. I'll also look into basis set errors (e.g., BSSE) and provide guidelines on selection. I need to gather sources and search updated information.


Thought for 1m 0s


下面把 **“泛函”** 和 **“基组”** 这两个常被放在一起讨论，却各司其职的核心概念一次理清。为了方便查阅，我把内容分成四大块：

---

## 1 | 什么是“泛函”（functional）

> **数学定义**：普通函数把数 → 数，
> **泛函** 把 *函数* → 数。

在密度泛函理论（DFT）里，能量就是一个 **ρ → E \[ρ]** 的泛函：给它一条三维电子密度 ρ(𝐫)，它返回一个标量——体系基态能。Hohenberg‑Kohn 定理保证这样的映射是存在且唯一的。([ACS Publications][1])

但我们不知其精确形式，只能做近似，于是出现了 **“Jacob’s Ladder”**：

| 梯级                   | 代表泛函                 | 依赖的输入         |                         |
| -------------------- | -------------------- | ------------- | ----------------------- |
| ① LDA                | SVWN                 | ρ             |                         |
| ② GGA                | PBE、BLYP             | ρ, ∇ρ         |                         |
| ③ meta‑GGA           | SCAN、r2SCAN          | ρ, ∇ρ, 动能密度 τ | ([ACS Publications][2]) |
| ④ 混合（Hybrid）         | B3LYP、PBE0、HSE06     | ③ + 少量 HF 交换  |                         |
| ⑤ 双杂化（Double‑Hybrid） | DSD‑PBEP86‑D4、revDSD | ④ + 二阶微扰相关    |                         |

> 选什么泛函＝在计算成本、精度和目标体系之间做平衡。近年热门的 **r²SCAN‑3c**、**ωB97X‑V/‑D**、**DM21** 等都属于对④/⑤梯级的改良或机器学习版本。([SCM][3], [ACS Publications][4])

---

## 2 | 什么是“基组”（basis set）

波函数或 Kohn–Sham 轨道要展开在一组已知函数 $\{\chi_\mu\}$ 上：

$$
\phi_i(\mathbf r)=\sum_\mu C_{\mu i}\,\chi_\mu(\mathbf r)
$$

* **基组大小**＝一阶近似的“分辨率”：越大越精，但耗时越高。
* 常见基函数：Gaussian、Slater（STO）、平面波 (PW)、数值原子轨道 (NAO)。

### 2.1 高斯型原子轨道（Gaussian‑type Orbitals）

1. **Pople 系列**：`STO‑3G`, `6‑31G*`, `6‑311++G**` ……

   * 语法易读，适合教学与快速估算。
2. **Dunning “cc‑pVnZ” 系列**（n=D,T,Q,5,6）：cc‑pVDZ, cc‑pVTZ …

   * **相关一致**：逐级收敛，可做 CBS 外推，量化精度高。([arXiv][5], [AIP Publishing][6])
3. **Karlsruhe def2 系列**：def2‑SVP, def2‑TZVP, def2‑QZVPP …

   * 覆盖 s–f 元素，搭配 ECP 易做重元素；与分子轨道程序 (TURBOMOLE、ORCA) 兼容好。([Google Sites][7], [arXiv][8])

**后缀约定**

* `*` / `(d)` / `P`：加极化函数（提高角动量）
* `+` 或 `aug`：加弥散函数（扩展尾部，描述弱相互作用和阴离子）([arXiv][9])

### 2.2 平面波 + 赝势

* 常用于周期体系（固体），基组由截断动量 $E_\text{cut}$ 控制。
* 与 **投影缀加波 (PAW)** 或 **超软赝势** 配合降低基组需求。

### 2.3 数值原子轨道（NAO）

* 如 FHI‑aims、SIESTA、ADF / BAND 使用；基组由 “tier1/2/3” 或 “DZP/TZ2P” 描述。

---

## 3 | 如何搭配“泛函 + 基组”？

| 目的           | 推荐组合（经验值，仅供快速决策）                                                 |
| ------------ | ---------------------------------------------------------------- |
| 有机分子几何 & 热化学 | **PBE0/def2‑TZVP**, **B3LYP/6‑31G(d,p)**                         |
| 精确相对能 / 反应屏障 | **ωB97X‑D/def2‑TZVPP**, **r²SCAN‑3c**（自带 mTZ2P 基组，含 gCP & D4 修正） |
| 弱相互作用 / 氢键   | GGA 或混合泛函 + **aug‑cc‑pVTZ** 或 **def2‑TZVPP** + `D3`/`D4` 色散      |
| 金属配合物        | **TPSSh/def2‑TZVP (ECP)**，或 **PBE0/def2‑QZVPP** (if cost allows) |

> **关键词**
>
> 1. **大小一致性**：换基组不应打乱能量差。
> 2. **BSSE**（基组重叠误差）：小基组时需做 counterpoise 校正。
> 3. **Core vs. Valence**：重元素常配有效芯势 ECP，减小基组规模但保持价层精度。

---

## 4 | 小结

* **泛函**：把 ρ(𝐫) 变成能量（E），分层次、比拼近似；越往“梯子”上走，通常越贵也越准。
* **基组**：决定波函数“像素密度”，直接影响 SCF 规模与结果精度。
* **选型思路**：先确定你要的精度，再按体系规模和预算在“泛函梯子”与“基组等级”上找平衡，必要时加色散、BSSE、相对论等修正。

掌握这两把“螺丝刀”，就能在绝大多数量子化学场景里拧出既省时又靠谱的答案。

[1]: https://pubs.acs.org/doi/10.1021/acs.jctc.0c01147?utm_source=chatgpt.com "Meta-Local Density Functionals: A New Rung on Jacob's Ladder"
[2]: https://pubs.acs.org/doi/10.1021/acs.jpca.2c02951?utm_source=chatgpt.com "Optimization of the r2SCAN-3c Composite Electronic-Structure ..."
[3]: https://www.scm.com/doc/Tutorials/StructureAndReactivity/Accurate_XC_functionals.html?utm_source=chatgpt.com "Accurate XC functionals — Tutorials 2025.1 documentation - SCM"
[4]: https://pubs.acs.org/doi/10.1021/acs.jpclett.4c01979?utm_source=chatgpt.com "A Critical Evaluation of the Hybrid KS DFT Functionals Based on the ..."
[5]: https://arxiv.org/pdf/2405.11567?utm_source=chatgpt.com "[PDF] arXiv:2405.11567v3 [physics.chem-ph] 5 Oct 2024"
[6]: https://pubs.aip.org/aip/jcp/article/160/8/084105/3266843/Correlation-consistent-basis-sets-designed-for?utm_source=chatgpt.com "Correlation consistent basis sets designed for density functional theory"
[7]: https://sites.google.com/site/orcainputlibrary/basis-sets?utm_source=chatgpt.com "Basis sets - ORCA Input Library - Google Sites"
[8]: https://arxiv.org/pdf/2308.06079?utm_source=chatgpt.com "[PDF] arXiv:2308.06079v2 [physics.chem-ph] 22 Sep 2023"
[9]: https://arxiv.org/html/2502.04631v1?utm_source=chatgpt.com "The Conundrum of Diffuse Basis Sets: A Blessing for Accuracy yet a ..."

Q: 假设我们已经知道了空间中任意一点的电子云密度，如何简单的理解能量的计算过程


**Explaining energy calculation concept**

The user is asking for an intuitive explanation of energy calculation given electron density, likely referencing DFT. I need to break it down conceptually, focusing on energy terms: kinetic energy (via Kohn-Sham orbitals), electron-nuclear attraction, electron-electron Coulomb repulsion, exchange-correlation, and nuclear-nuclear repulsion. It’s important to provide a simplified, relatable summary, maybe with analogies for each term. I’ll avoid unnecessary technical details and focus on how these terms fit together to calculate the total energy.


Thought for 17 seconds


### 如果 **电子云密度 ρ(𝐫)** 已知，能量是怎样“加总”出来的？——一幅拼图式的直观图解

> 下文把 **公式** 拆成 **看得见／想得出的五块积木**，并配上“为什么要这样算”的生活类比。忽略细节常数，只抓住“把什么跟什么做积分”这一核心。

| 积木                        | 数学表达（示意）                                              | 一句话物理解释                             | 简单类比                                        |                            |                                                          |
| ------------------------- | ----------------------------------------------------- | ----------------------------------- | ------------------------------------------- | -------------------------- | -------------------------------------------------------- |
| **1. 电子‑核吸引**             | (E\_{eN}= \displaystyle\sum\_A Z\_A\int \frac{ρ(𝐫)}{ | 𝐫-𝐑\_A                            | },d𝐫)                                      | 带负电的电子云被正电核吸住              | 把砂糖 (电子) 均匀撒在桌面，桌上若放几个吸铁石 (原子核)，吸力随距离 $1/r$ 衰减，积分就是“总吸力” |
| **2. 电子‑电子排斥（Hartree）**   | (E\_H= \tfrac12\iint \frac{ρ(𝐫),ρ(𝐫')}{             | 𝐫-𝐫'                              | },d𝐫,d𝐫')                                 | 云对云的库仑排斥；双积分避免漏掉任何两点的相互作用  | 像计算一团“带电棉花”中任意两根纤维之间的斥力，再把所有斥力相加                         |
| **3. 核‑核排斥**              | (E\_{NN}= \displaystyle\sum\_{A\<B}\frac{Z\_A Z\_B}{  | 𝐑\_A-𝐑\_B                         | })                                          | 不随电子改变，像分子骨架的常数项           | 固定的“骨架弹簧势能”，只决定核间距离                                      |
| **4. 电子动能（$T_s[ρ]$）**     | **非显式**：在 Kohn–Sham 里用轨道求 (\sum\_i ⟨φ\_i              | -\tfrac12∇^2                        | φ\_i⟩)                                      | 电子云会“扩散”——越局促越贵；这是那份“扩散代价” | 水波收得越窄，浪头越陡、能量越高；动能就是这种“陡峭度”积分                           |
| **5. 交换‑相关能 $E_{xc}[ρ]$** | **近似泛函** LDA/GGA/...                                  | 纠正在 2 & 4 中遗漏的纯量子效应：泡利排斥、短程关联、零点动能等 | 人群中既要保持社交距离 (排斥) 又可能三五成群 (关联)；这块能量把这些行为统计进去 |                            |                                                          |

把五块积木拼起来：

$$
E[ρ] = T_s[ρ] + E_{eN}[ρ] + E_H[ρ] + E_{xc}[ρ] + E_{NN}
$$

---

#### **为什么“知道 ρ 就够了”却还要拆 5 块？**

* **局部 vs. 非局部**

  * $E_{eN}$ 与 $E_H$：纯粹靠积分 ρ × 势/距离，完全“看云”就能算。
  * $T_s$ 与 $E_{xc}$：涉及量子相干，单靠 $\rho(𝐫)$ 裸数据无法直接写成简单积分，只能用 K‑S 轨道或经验泛函来“打补丁”。
* **分块好处**：

  1. **物理含义清晰**，便于改进局部缺点而不动其它部分；
  2. **数值效率高**: 1, 2 块可快速 FFT/数值积分；复杂度主要集中在动能与交换‑相关近似。

---

#### **一步步在电脑里发生什么？**——把公式落地

1. **给定 ρ** → 直接积分得 **2 + 3**。
2. **构造有效势 $v_\text{eff}[ρ]=v_{eN}+v_H+v_{xc}$**。
3. **解 Kohn–Sham 方程** 得轨道 → 计算 **动能 $T_s$**。
4. **用同一轨道再更新 ρ**，循环到自洽（SCF）。
5. **输出** $E[ρ]$ 与力常数，用于几何优化、分子动力学等。

> **关键直觉**：能量就是“把云当作带电果冻”，对它与自身、与核的相互作用以及云内的“搅动”成本分门别类地做积分；量子纠缠那块算不易，只能用半经验或轨道技巧补齐。

---

### 小结

* **电子云密度就像一张 3D 分布图**：每一点给云上了“多少电子”的数值。
* **能量计算 = 对这张图做多重积分 + 量子修正**。
* 分解成 5 块积木可同时保持直观和可计算性；动能与交换‑相关是重头戏，其余项都是“把云当经典电荷”就能算的积分。


