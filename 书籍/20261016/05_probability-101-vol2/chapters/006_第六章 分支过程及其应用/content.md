# 第六章 分支过程及其应用

原始 PDF 第 149–162 页。

150

第六章 分支过程及其应用

分支过程是复杂群体随机演化的数学模型, 其重要特性是由分支结构所导致的可加性. 概率母函数是分支过程研究的基本工具. 本章讨论不带移民和带移民的分支过程及其应用, 包括基本结构、矩的表达、爆炸概率、灭绝概率、指数增长速度、平稳分布等. 作为分支过程的应用, 还研究了一维简单随机游动对不同水平的穿越次数.

## 6.1 定义和基本构造

## 6.1.1 分支过程的定义

设  $\{\xi_{n,k}:n,k=1,2,\cdots\}$  是取值于  $Z_{+}$  的独立同分布随机变量族, 且服从概率分布  $\{p(j):j\in\mathbb{Z}_{+}\}$ . 取定独立于  $\{\xi_{n,k}\}$  的  $Z_{+}$  值随机变量  $X_{0}$ , 再递推地定义

$$
X _ {n} = \sum_ {k = 1} ^ {X _ {n - 1}} \xi_ {n, k}, \quad n \geqslant 1. \tag {6.1.1}
$$

这里约定  $\sum_{k=1}^{0}\cdots=0.$  令  $(p^{*i}(j):j\in\mathbb{Z}_{+})$  为  $(p(j):i,j\in\mathbb{Z}_{+})$  的 i 重卷积. 不难看出,
对任何  $n \geqslant 1$  及  $\{i_{0}, i_{1}, \cdots, i_{n-1} = i, j\} \subseteq Z_{+}$  有

$$
\mathbf {P} (X _ {n} = j | X _ {0} = i _ {0}, X _ {1} = i _ {1}, \dots , X _ {n - 1} = i _ {n - 1}) = \mathbf {P} (X _ {n} = j | X _ {n - 1} = i) = p ^ {* i} (j).
$$

所以  $X = (X_{n} : n \geqslant 0)$  是以  $(p^{*i}(j) : i, j \in \mathbb{Z}_{+})$  为转移矩阵的马氏链.

定义 6.1.1 给定概率分布  $(p(j): j \in \mathbb{Z}_{+})$ ，我们称任何具有转移矩阵  $P = (p^{*i}(j): i, j \in \mathbb{Z}_{+})$  的马氏链为分支过程，并称  $(p(j): j \in \mathbb{Z}_{+})$  为其后代分布。

考虑具有后代分布 $(p(j):j\in \mathbb{Z}_{+})$ 的分支过程 $X$ .令 $P^n = (p_n(i,j):i,j\in \mathbb{Z}_+)$ 为$X$ 的 $n$ 步转移矩阵.

定理 6.1.1 令 g 为后代分布  $(p(j): j \in \mathbb{Z}_{+})$  的母函数, 则对任何  $i, n \geqslant 1$  有

$$
\sum_ {j = 0} ^ {\infty} p _ {n} (i, j) z ^ {j} = g _ {n} (z) ^ {i}, \quad | z | \leqslant 1, \tag {6.1.2}
$$

其中  $g_{n}(z):=g\circ g\circ\cdots\circ g(z)$  表示 n 重复合.

证明 由前面的讨论, 我们有 $p_1(i,j) = p^{*i}(j)$, 所以

$$
\sum_ {j = 0} ^ {\infty} p _ {1} (i, j) z ^ {j} = \sum_ {j = 0} ^ {\infty} p ^ {* i} (j) z ^ {j} = g (z) ^ {i}.
$$

---

6.1 定义和基本构造

151

即 (6.1.2) 式对 $n = 1$ 成立. 下设该式对某个 $n \geqslant 1$ 成立, 则

$$
\begin{array}{l} \sum_ {j = 0} ^ {\infty} p _ {n + 1} (i, j) z ^ {j} = \sum_ {j = 0} ^ {\infty} \sum_ {k = 0} ^ {\infty} p _ {1} (i, k) p _ {n} (k, j) z ^ {j} \\ = \sum_ {k = 0} ^ {\infty} p _ {1} (i, k) g _ {n} (z) ^ {k} = g _ {n + 1} (z) ^ {i}. \\ \end{array}
$$

根据数学归纳法即得欲证结论. $\square$

推论 6.1.2 分支过程的 n 步转移矩阵  $P^{n} = (p_{n}(i, j) : i, j \in \mathbb{Z}_{+})$  具有性质

$$
p _ {n} (i _ {1} + i _ {2}, \cdot) = p _ {n} (i _ {1}, \cdot) * p _ {n} (i _ {2}, \cdot), \quad i _ {1}, i _ {2} \in \mathbb {Z} _ {+}. \tag {6.1.3}
$$

推论 6.1.3 分支过程的 n 步转移矩阵  $P^{n} = (p_{n}(i, j) : i, j \in \mathbb{Z}_{+})$  具有性质

$$
p _ {n} (i, j) = \sum_ {k _ {1} + k _ {2} + \dots + k _ {i} = j} p _ {n} (1, k _ {1}) p _ {n} (1, k _ {2}) \dots p _ {n} (1, k _ {i}), \quad i, j \in \mathbb {Z} _ {+}. \tag {6.1.4}
$$

分支过程描述的是封闭环境下生物群体的演化过程, 最早由别奈梅 (Bienaymé) [2] 与高尔顿 (Galton) 和沃森 (Watson) [15] 独立地引入. 直观上, 群体中的个体均只生存一个单位时间, 且在死亡时产生一定数量的后代. 这里 $\xi_{n,i}$ 表示第 $n - 1$ 代的第 $i$ 号个体在死亡时产生的后代的个数. 性质 (6.1.3) 称为转移矩阵的分支性. 该性质导致了下面定理给出的可加性.

定理 6.1.4 设  $(X_{n}: n \geqslant 0)$  和  $(Y_{n}: n \geqslant 0)$  是独立的分支过程, 且有相同的后代概率分布  $(p(j): j \in \mathbb{Z}_{+})$ , 则  $(X_{n} + Y_{n}: n \geqslant 0)$  也是具有后代分布  $(p(j): j \in \mathbb{Z}_{+})$  的分支过程.

证明 令 $Z_{n} = X_{n} + Y_{n}$. 再对 $\{i_0, i_1, \dots, i_n = i\} \subseteq \mathbb{Z}_{+}$ 记 $G_{n} = \{Z_{0} = i_{0}, Z_{1} = i_{1}, \dots, Z_{n} = i_{n} = i\}$. 因为 $(X_{n}: n \geqslant 0)$ 与 $(Y_{n}: n \geqslant 0)$ 独立, 根据推论6.1.2有

$$
\begin{array}{l} \mathbf {P} (G _ {n} \cap \{Z _ {n + 1} = j \}) = \sum_ {k _ {0} = 0} ^ {i _ {0}} \dots \sum_ {k _ {n} = 0} ^ {i _ {n}} \sum_ {l = 0} ^ {j} \mathbf {P} (X _ {0} = k _ {0}, \dots , X _ {n} = k _ {n}, X _ {n + 1} = l, \\ Y _ {0} = i _ {0} - k _ {0}, \dots , Y _ {n} = i _ {n} - k _ {n}, Y _ {n + 1} = j - l) \\ = \sum_ {k _ {0} = 0} ^ {i _ {0}} \dots \sum_ {k _ {n} = 0} ^ {i _ {n}} \sum_ {l = 0} ^ {j} \mathbf {P} (X _ {0} = k _ {0}, \dots , X _ {n} = k _ {n}, X _ {n + 1} = l) \cdot \\ \mathbf {P} (Y _ {0} = i _ {0} - k _ {0}, \dots , Y _ {n} = i _ {n} - k _ {n}, Y _ {n + 1} = j - l) \\ = \sum_ {k _ {0} = 0} ^ {i _ {0}} \dots \sum_ {k _ {n} = 0} ^ {i _ {n}} \sum_ {l = 0} ^ {j} \mathbf {P} (X _ {0} = k _ {0}, \dots , X _ {n} = k _ {n}) p (k _ {n}, l) \cdot \\ \mathbf {P} (Y _ {0} = i _ {0} - k _ {0}, \dots , Y _ {n} = i _ {n} - k _ {n}) p (i _ {n} - k _ {n}, j - l) \\ = \sum_ {k _ {0} = 0} ^ {i _ {0}} \dots \sum_ {k _ {n} = 0} ^ {i _ {n}} \mathbf {P} (X _ {0} = k _ {0}, \dots , X _ {n} = k _ {n}) \cdot \\ \end{array}
$$

---

152

第六章 分支过程及其应用

$$
\begin{array}{l} \mathbf {P} (Y _ {0} = i _ {0} - k _ {0}, \dots , Y _ {n} = i _ {n} - k _ {n}) p (i _ {n}, j) \\ = \sum_ {k _ {0} = 0} ^ {i _ {0}} \dots \sum_ {k _ {n} = 0} ^ {i _ {n}} \mathbf {P} (X _ {0} = k _ {0}, \dots , X _ {n} = k _ {n}, \\ Y _ {0} = i _ {0} - k _ {0}, \dots , Y _ {n} = i _ {n} - k _ {n}) p (i, j) \\ = \mathbf {P} (G _ {n}) p (i, j). \\ \end{array}
$$

故得

$$
\mathbf {P} (Z _ {n + 1} = j | G _ {n}) = \mathbf {P} (G _ {n}) ^ {- 1} \mathbf {P} (G _ {n} \cap \{Z _ {n + 1} = j \}) = p (i, j) = p ^ {* i} (j).
$$

根据定理 4.2.2, 这就证明了  $(Z_{n}: n \geqslant 0)$  是具有后代分布  $(p(j): j \in \mathbb{Z}_{+})$  分支过程. □

## 6.1.2 临界类和矩

考虑以 $(p(j): j \in \mathbb{Z}_{+})$ 为后代分布的分支过程 $X = (X_{n}: n \geqslant 0)$. 令 $g$ 为 $(p(j): j \in \mathbb{Z}_{+})$ 的母函数. 记 $m = g'(1) \in [0, \infty]$. 若 $m = 1$, 则称 $X$ 具有临界分支; 若 $m > 1$ 或 $< 1$, 相应地称 $X$ 具有上临界的或下临界的. 为简化记号, 我们写 $\mathbf{P}_i = \mathbf{P}(\cdot | X_0 = i)$ 并分别用 $\mathbf{E}_i$ 和 $\mathbf{Var}_i$ 表示相应的数学期望和方差.

定理 6.1.5 假定  $m := g'(1) < \infty$ ，则对任何  $i, n \geqslant 1$  有

$$
\mathbf {E} _ {i} (X _ {n}) = \sum_ {j = 1} ^ {\infty} j p _ {n} (i, j) = i m ^ {n}. \tag {6.1.5}
$$

证明 由关系 $g_{n}(z) = g(g_{n - 1}(z))$ 得 $g_{n}^{\prime}(z) = g^{\prime}(g_{n - 1}(z))g_{n - 1}^{\prime}(z)$，进而有

$$
g _ {n} ^ {\prime} (1) = g ^ {\prime} (1) g _ {n - 1} ^ {\prime} (1) = m g _ {n - 1} ^ {\prime} (1).
$$

反复应用上式得 $g_{n}^{\prime}(1) = m^{n}$. 再由 (6.1.2) 式即得结论. $\square$

定理 6.1.6 假定  $m_{2} := g'(1) + g''(1) < \infty$ ，则对任何  $n \geqslant 1$  有

$$
\mathbf {E} _ {1} (X _ {n} ^ {2}) = \sigma^ {2} m ^ {n - 1} (m ^ {n - 1} + m ^ {n - 2} + \dots + 1) + m ^ {2 n} \tag {6.1.6}
$$

和

$$
\mathbf {V a r} _ {1} (X _ {n}) = \sigma^ {2} m ^ {n - 1} (m ^ {n - 1} + m ^ {n - 2} + \dots + 1). \tag {6.1.7}
$$

其中  $\sigma^{2}=m_{2}-m^{2}=\mathbf{Var}_{1}(X_{1})$ .

证明 在定理 6.1.5 证明中计算的基础上不难得到

$$
g _ {n} ^ {\prime \prime} (z) = g ^ {\prime \prime} (g _ {n - 1} (z)) g _ {n - 1} ^ {\prime} (z) ^ {2} + g ^ {\prime} (g _ {n - 1} (z)) g _ {n - 1} ^ {\prime \prime} (z).
$$

---

6.1 定义和基本构造

153

由定理 6.1.5 知  $g_{n}^{\prime}(1)=\mathbf{E}_{1}(X_{n})=m^{n}$ . 此外, 易知  $g^{\prime\prime}(1)=\sigma^{2}+m^{2}-m$ . 所以有

$$
\begin{array}{l} g _ {n} ^ {\prime \prime} (1) = g ^ {\prime \prime} (1) g _ {n - 1} ^ {\prime} (1) ^ {2} + g ^ {\prime} (1) g _ {n - 1} ^ {\prime \prime} (1) \\ = g ^ {\prime \prime} (1) m ^ {2 (n - 1)} + m g _ {n - 1} ^ {\prime \prime} (1) \\ = g ^ {\prime \prime} (1) m ^ {2 (n - 1)} + m \big [ g ^ {\prime \prime} (1) m ^ {2 (n - 1) - 2} + m g _ {n - 2} ^ {\prime \prime} (1) \big ] \\ = g ^ {\prime \prime} (1) m ^ {2 (n - 1)} + g ^ {\prime \prime} (1) m ^ {2 (n - 1) - 1} + m ^ {2} g _ {n - 2} ^ {\prime \prime} (1) \\ = \dots \\ = g ^ {\prime \prime} (1) (m ^ {2 (n - 1)} + m ^ {2 (n - 1) - 1} + \dots + m ^ {n - 1}) \\ = (\sigma^ {2} + m ^ {2} - m) m ^ {n - 1} (m ^ {n - 1} + m ^ {n - 2} + \dots + 1) \\ = \sigma^ {2} m ^ {n - 1} (m ^ {n - 1} + m ^ {n - 2} + \dots + 1) + m ^ {n} (m ^ {n} - 1). \\ \end{array}
$$

再根据二阶矩的计算公式即得欲证等式. $\square$

## 6.1.3 带移民分支过程

设  $\{\xi_{n,k}:n,k=1,2,\cdots\}$  和  $\{\eta_{n}:n=1,2,\cdots\}$  是两个独立的  $Z_{+}$  值独立同分布随机变量族，且分别服从概率分布  $(p(j):j\in\mathbb{Z}_{+})$  和概率分布  $\{\gamma(j):j\in\mathbb{Z}_{+}\}$ . 令  $Y_{0}$  是独立于  $\{\xi_{n,k}\}$  和  $\{\eta_{n}\}$  的  $Z_{+}$  值随机变量. 递推地定义

$$
Y _ {n} = \sum_ {k = 1} ^ {Y _ {n - 1}} \xi_ {n, k} + \eta_ {n}, \quad n \geqslant 1. \tag {6.1.8}
$$

不难证明, 对任何  $n \geqslant 0$  及  $\{i_{0}, i_{1}, \cdots, i_{n-1} = i, j\} \subseteq Z_{+}$  有

$$
\mathbf {P} (Y _ {n} = j | Y _ {0} = i _ {0}, Y _ {1} = i _ {1}, \dots , Y _ {n - 1} = i _ {n - 1}) = p ^ {* i} * \gamma (j).
$$

所以 $Y = (Y_{n}:n\geqslant 0)$ 是以 $P^{\gamma} = (p^{*i}*\gamma (j):i,j\in \mathbb{Z}_{+})$ 为转移矩阵的马氏链.该模型描述的是开放环境下生物群体的演化过程.在分支过程模型的基础上,这里在第 $n$ 个时间段有 $\eta_{n}$ 个新个体加入到群体中来.

定义 6.1.2 设  $(p(j): j \in \mathbb{Z}_{+})$  和  $(\gamma(j): j \in \mathbb{Z}_{+})$  为概率分布。称  $Z_{+}$ 上的离散时间马氏链  $Y = (Y_{n}: n \geqslant 0)$  为带移民的分支过程，是指其转移矩阵  $P^{\gamma} = (p^{\gamma}(i, j): i, j \in \mathbb{Z}_{+})$  有分解

$$
p ^ {\gamma} (i, \cdot) = p ^ {* i} * \gamma (\cdot), \quad i \in \mathbb {Z} _ {+}. \tag {6.1.9}
$$

此时称 $(p(j):j\in \mathbb{Z}_{+})$ 为 $Y$ 的后代分布, 而称 $(\gamma (j):j\in \mathbb{Z}_{+})$ 为其移民分布.

下面几个结果的证明与无移民的情况类似, 故这里略去.

定理 6.1.7 假定  $\{Y_{1}(n): n \geqslant 0\}$  和  $\{Y_{2}(n): n \geqslant 0\}$  是独立且具有相同后代分布  $(p(j): j \in \mathbb{Z}_{+})$  的带移民分支过程. 分别以  $(\gamma_{1}(j): j \in \mathbb{Z}_{+})$  和  $(\gamma_{2}(j): j \in \mathbb{Z}_{+})$  记它

---

154

第六章 分支过程及其应用

们的移民概率分布, 那么 $\{Y_1(n) + Y_2(n): n \geqslant 0\}$ 也是带移民分支过程, 且有后代分布 $(p(j): j \in \mathbb{Z}_+)$ 和移民分布 $(\gamma_1 * \gamma_2(j): j \in \mathbb{Z}_+)$.

定理 6.1.8 令  $P_{n}^{\gamma} = (p_{n}^{\gamma}(i, j) : i, j \in \mathbb{Z}_{+})$  是以  $(p(j) : j \in \mathbb{Z}_{+})$  为后代分布以  $(\gamma(j) : j \in \mathbb{Z}_{+})$  为移民分布的带移民分支过程的 n 步转移矩阵，则对任何  $i, n \geqslant 1$  有

$$
\sum_ {j = 0} ^ {\infty} p _ {n} ^ {\gamma} (i, j) z ^ {j} = g _ {n} (z) ^ {i} \prod_ {k = 1} ^ {n} h (g _ {k - 1} (z)), \quad | z | \leqslant 1, \tag {6.1.10}
$$

其中 h 为移民分布  $(\gamma(j): j \in \mathbb{Z}_{+})$  的母函数.

定理 6.1.9 设  $m := g'(1-) < \infty$  和  $\mu := h'(1-) < \infty$ ，则对任何  $i, n \geqslant 1$  有

$$
\mathbf {P} (Y _ {n} | Y _ {0} = i) = i m ^ {n} + \mu \sum_ {k = 1} ^ {n} m ^ {k - 1}. \tag {6.1.11}
$$

## 练习题

1. 给出定理 6.1.7, 定理 6.1.8 和定理 6.1.9 的证明.
2. 给定常数 $b \in (0,1)$ 和 $p \in (0,1)$, 令 $\mu(0) = (1 - b - p)/(1 - p)$ 和 $\mu(j) = bp^{j-1}$ ($j \geqslant 1$). 易见 $(\mu(j): j \in \mathbb{Z}_+)$ 为概率分布且

$$
g (z) := \sum_ {j = 0} ^ {\infty} \mu (j) z ^ {j} = \frac {1 - b - p}{1 - p} + \frac {b z}{1 - p z}.
$$

3. 在上题中, 若取 $b = (1 - p)^2$, 则 $g'(1) = 1$ 且

$$
g (z) = p + \frac {(1 - p) ^ {2} z}{1 - p z} = \frac {p - (2 p - 1) z}{1 - p z}.
$$

证明对任何 $n \geqslant 1$ 有

$$
g _ {n} (z) = \frac {n p - [ (n + 1) p - 1) z}{1 + (n - 1) p - n p z}.
$$

提示: 对  $n \geqslant 1$  用数学归纳法.

## 6.2 过程的长时间行为

假定 $X = (X_{n}: n \geqslant 0)$ 是以 $(p(j): j \in \mathbb{Z}_{+})$ 为后代分布的分支过程. 令 $g$ 为 $(p(j): j \in \mathbb{Z}_{+})$ 的母函数. 本节研究 $X$ 的长时间行为. 为了避免平凡的情况, 我们假定 $p(1) < 1$.

---

6.2 过程的长时间行为

155

## 6.2.1 爆炸概率和灭绝概率

爆炸或灭绝的概率的计算是关于分支过程的基本问题, 也是最初引入该模型时的主要动机之一. 定义分支过程 $X$ 的灭绝时间 $\tau_0 = \inf \{n \geqslant 0 : X_n = 0\}$. 我们分别称

$$
A := \Big \{\lim _ {n \to \infty} X _ {n} = \infty \Big \}, \quad B := \Big \{\lim _ {n \to \infty} X _ {n} = 0 \Big \} = \{\tau_ {0} <   \infty \}
$$

为 $X$ 的爆炸事件和灭绝事件.显然 $B = \bigcup_{n=1}^{\infty} B_n$，其中 $B_n = \{\tau_0 \leqslant n\}$.以下简记 $\mathbf{P}_i = \mathbf{P}(\cdot | X_0 = i)$. 由 (6.1.1) 式和 (6.1.2) 式不难看出

$$
\mathbf {P} _ {i} (B _ {n}) = \mathbf {P} _ {i} (X _ {n} = 0) = \mathbf {P} _ {i} (X _ {n} = X _ {n + 1} = \dots = 0) = g _ {n} (0) ^ {i}.
$$

下面的命题显然成立.

命题 6.2.1 设  $m := g'(1) < 1$ ，则对  $i, n \geqslant 1$  有

$$
\mathbf {P} _ {i} (B _ {n} ^ {c}) = \mathbf {P} _ {i} (\tau_ {0} > n) = \mathbf {P} _ {i} (X _ {n} > 0) \leqslant \mathbf {E} _ {i} (X _ {n}) = i m ^ {n},
$$

进而有  $\mathbf{P}_{i}(B)=\mathbf{P}_{i}(\tau_{0}<\infty)=1.$

根据命题 6.2.1, 下临界分支过程的存活概率  $\mathbf{P}_{i}(X_{n}>0)$  至少是以指数速度衰减的, 这是对此概率的一个非常有用的上界估计.

定理 6.2.2 所有状态  $i \geqslant 1$  对于分支过程都是暂留态的.

证明 任取 $i \geqslant 1$. 当 $p(0) > 0$ 时, 我们有

$$
\mathbf {P} _ {i} (X _ {n} \neq i \text {对所有} n \geqslant 1 \text {成立})
$$

$$
\geqslant \mathbf {P} _ {i} (X _ {1} = 0) = p _ {1} (i, 0) = p (0) ^ {i} > 0.
$$

当  $p(0)=0$  时, 在非平凡假定条件  $p(1)<1$  之下有

$$
\mathbf {P} _ {i} (X _ {n} \neq i \text {对所有} n \geqslant 1 \text {成立}) \geqslant \mathbf {P} _ {i} (X _ {1} \geqslant i + 1)
$$

$$
= \mathbf {P} _ {i} \bigg (\sum_ {k = 1} ^ {i} \xi_ {1, k} \geqslant i + 1 \bigg)
$$

$$
\geqslant \mathbf {P} _ {i} (\xi_ {1, 1} \geqslant 2) = \sum_ {j = 2} ^ {\infty} p (j) > 0.
$$

因此所有状态  $i \geqslant 1$  都是暂留态. □

推论 6.2.3 对任何  $i \geqslant 0$  有

$$
\mathbf {P} _ {i} (A \cup B) = \mathbf {P} _ {i} \Big (\lim _ {n \to \infty} X _ {n} = \infty \text {或} 0 \Big) = 1. \tag {6.2.1}
$$

---

156

第六章 分支过程及其应用

证明 由定理 6.2.2, 所有状态 $k \geqslant 1$ 都是暂留态. 因此, 任何有限集合 $\{1, 2, \cdots, k\}$ 以概率 1 至多只被访问有限次. 再考虑到零点的吸收性即得欲证结果. $\square$

注意, 在非平凡假定 $p(1) < 1$ 之下, 母函数 $g$ 在区间 $[0,1]$ 上是凸增函数, 且有 $g(0) = p(0)$ 和 $g(1) = 1$. 令 $q$ 是方程 $z = g(z)$ 在 $[0,1]$ 上的最小解. 显然, 当 $m \leqslant 1$ 时有 $q = 1$; 而当 $m > 1$ 时有 $q < 1$.

引理 6.2.4 对于  $z \in [0, q]$ ，当  $n \to \infty$  时递增地  $g_{n}(z) \to q$ ; 而对于  $z \in [q, 1)$ ，当  $n \to \infty$  时递降地  $g_{n}(z) \to q$ .

证明 不难看出, 对于任何 $z \in [0, q]$ 有 $z \leqslant g(z) \leqslant g(q)$. 由于 $g$ 是增函数, 反复应用此关系得

$$
z \leqslant g _ {1} (z) \leqslant g _ {2} (z) \leqslant \dots \leqslant g _ {n} (z) \leqslant g _ {n} (q) = q.
$$

所以极限 $r := \lim_{n \to \infty} g_n(z)$ 存在. 在关系式 $g_n(z) = g(g_{n-1}(z))$ 中令 $n \to \infty$ 得 $r = g(r)$. 故必有 $r = q$. 类似地可证明 $z \in [q, 1]$ 的情况. $\square$

下面的定理说明分支过程 $X$ 的灭绝概率 $\mathbf{P}_i(B) = \mathbf{P}_1(B)^i$ 和爆炸概率 $\mathbf{P}_i(A) = 1 - \mathbf{P}_1(B)^i$ 可由后代分布的母函数简单决定.

定理 6.2.5 我们有  $\mathbf{P}_{i}(B)=\lim_{n\to\infty}\mathbf{P}_{i}(B_{n})=q^{i}$ ，其中 q 是方程  $z=g(z)$  在 [0,1] 上的最小解.

证明 由概率测度的下连续性有

$$
\mathbf {P} _ {i} (B) = \mathbf {P} _ {i} \bigg (\bigcup_ {n = 1} ^ {\infty} B _ {n} \bigg) = \lim _ {n \to \infty} \mathbf {P} _ {i} (B _ {n}) = \lim _ {n \to \infty} \mathbf {P} _ {i} (X _ {n} = 0) = \lim _ {n \to \infty} g _ {n} (0) ^ {i}.
$$

再由引理6.2.4即得结论.□

如上面所指出的, 在非平凡假定条件 $p(1) < 1$ 之下, 只要 $m \leqslant 1$, 就有 $q = 1$, 进而 $\mathbf{P}_i(B) = 1$. 也就是说, 非平凡的临界或下临界分支过程几乎必然灭绝. 这个结论似乎与我们的感性经验相悖, 它说明了数学方法对于理性思维的重要意义.

## 6.2.2 几何增长率

下面定理的证明用到了上鞅收敛定理, 没有学习过鞅论的读者可以跳过证明.

定理 6.2.6 设  $m := g'(1) < \infty$ ，则对任何  $i \geqslant 1$  在概率  $P_{i}$  之下存在非负可积随机变量 W 使得 (a.s.)

$$
\lim _ {n \to \infty} m ^ {- n} X _ {n} = W. \tag {6.2.2}
$$

证明 令 $(\mathcal{F}_n)$ 为 $(X_{n})$ 的自然流. 由 (6.1.5) 式不难看出, 在 $\mathbf{P}_i$ 之下 $(m^{-n}X_n)$ 关于流 $(\mathcal{F}_n)$ 是非负鞅. 再由推论 2.4.6 知 (6.2.2) 式中的极限存在且可积. □

---

6.2 过程的长时间行为

157

根据定理 6.2.6, 当 n 很大时  $(X_{n})$  的演化趋势与随机序列  $(m^{n}W)$  近似. 这给出了马尔萨斯 (Malthus) 的人口几何增长率的随机版本. 但是, 该定理并没有提供关于极限 W 除可积性之外的其他信息. 当然, 由 (6.2.2) 式和法图定理可以得到

$$
\mathbf {E} _ {i} (W) \leqslant \operatorname * {l i m i n f} _ {n \to \infty} m ^ {- n} \mathbf {E} _ {i} (X _ {n}) = \mathbf {E} _ {i} (X _ {0}) = i.
$$

但这并没有排除 $W = 0$ (a.s.) 的情况. 若 $W = 0$ (a.s.), 则 (6.2.2) 式只不过表明这里的规范化因子 $m^{-n}$ 实在太大. 事实上, 根据前面的讨论, 只要 $p(1) < 1$ 且 $m \leqslant 1$, 就有 $\mathbf{P}_i(\tau_0 < \infty) = 1$, 故对于充分大的 $n$ 有 $X_n = 0$, 从而 $W = 0$ (a.s.). 下面的定理表明, 当 $m > 1$ 时在二阶矩条件下 (6.2.2) 式中的规范化因子 $m^{-n}$ 是合适的.

定理 6.2.7 设有  $1 < m := g'(1) < \infty$  和  $m_{2} := g'(1) + g''(1) < \infty$ ，则

$$
\mathbf {E} _ {1} (W) = 1, \quad \mathbf {P} _ {1} (W = 0) = q. \tag {6.2.3}
$$

证明 根据定理 6.1.6 易知

$$
\mathbf {E} _ {1} [ (m ^ {- n} X _ {n}) ^ {2} ] = \sigma^ {2} m ^ {- 1} (m - 1) ^ {- 1} (1 - m ^ {- n}) + 1
$$

和

$$
\sup _ {n \geqslant 1} \mathbf {E} _ {1} [ (m ^ {- n} X _ {n}) ^ {2} ] = \sigma^ {2} m ^ {- 1} (m - 1) ^ {- 1} + 1.
$$

因此 $(m^{-n}X_{n}:n\geqslant 0)$ 是一致可积的非负鞅.再由定理2.4.5有 $\mathbf{E}_1(|m^{-n}X_n - W|)\to 0$ 故 $\mathbf{E}_1(W) = 1$ .记 $r = \mathbf{P}_1(W = 0)$ .显然 $r <   1$ 根据全概率公式，

$$
r = \sum_ {j = 0} ^ {\infty} \mathbf {P} _ {1} (X _ {1} = j) \mathbf {P} _ {1} (W = 0 | X _ {1} = j) = \sum_ {j = 0} ^ {\infty} p (j) r ^ {j} = g (r),
$$

故知 r = q. □

## 6.2.3 带移民过程的极限定理

令 $P_{n}^{\gamma} = (p_{n}^{\gamma}(i,j):i,j\in \mathbb{Z}_{+})$ 是由(6.1.10)式定义的带移民分支过程的 $n$ 步转移矩阵.为避免退化的情况,这里假定 $p(0) < 1$ 和 $p(1) < 1$. 下面的定理给出了当 $n\to \infty$ 时在 $\mathbf{P}(\cdot |Y_0 = i)$ 之下 $Y_{n}$ 依分布收敛的充要条件.

定理 6.2.8 设  $m := g'(1) \leqslant 1$ ，则存在离散概率分布  $(p^{\gamma}(j): j \in \mathbb{Z}_{+})$ ，使对任何  $i, j \geqslant 0$  有  $\lim_{n \to \infty} p_{n}^{\gamma}(i, j) = p^{\gamma}(j)$  当且仅当

$$
\int_ {0} ^ {1} \frac {1 - h (z)}{g (z) - z} \mathrm{d} z <   \infty , \tag {6.2.4}
$$

---

158

第六章 分支过程及其应用

且此时有

$$
f ^ {\gamma} (z) := \sum_ {j = 0} ^ {\infty} p ^ {\gamma} (j) z ^ {j} = \prod_ {k = 1} ^ {\infty} h (g _ {k - 1} (z)), \quad | z | \leqslant 1. \tag {6.2.5}
$$

证明 根据假定, 有 $p(0) < 1$, $p(1) < 1$ 和 $m := g'(1) \leqslant 1$, 故对任何 $0 < z < 1$ 当 $n \to \infty$ 时有 $g_n(z) \uparrow 1$, 因此 $\lim_{n \to \infty} p_n(0) = 1$. 由 (6.1.10) 式有

$$
f _ {n} ^ {\gamma} (i, z) := \sum_ {j = 0} ^ {\infty} p _ {n} ^ {\gamma} (i, j) z ^ {j} = g _ {n} (z) ^ {i} \prod_ {k = 1} ^ {n} h (g _ {k - 1} (z)).
$$

显然, 当 $|z| \leqslant 1$ 时有 $\lim_{n \to \infty} f_n^\gamma(i, z) = f^\gamma(z)$. 由母函数连续性定理, 极限 $\lim_{n \to \infty} p_n^\gamma(i, j) = p^\gamma(j)$ 存在且 (6.2.5) 式成立. 注意 (6.2.5) 式右端无穷乘积中的每个因子不超过 1, 故 $f^\gamma(z) > 0$ 当且仅当

$$
\sum_ {k = 1} ^ {\infty} \ln h (g _ {k - 1} (z)) ^ {- 1} = \sum_ {k = 1} ^ {\infty} \ln \left[ 1 + \frac {1 - h (g _ {k - 1} (z))}{h (g _ {k - 1} (z))} \right] <   \infty ,
$$

或等价地，

$$
\sum_ {k = 1} ^ {\infty} [ 1 - h (g _ {k - 1} (z)) ] <   \infty . \tag {6.2.6}
$$

当 (6.2.6) 式对某个 $0 < z < 1$ 不成立时, 有 $f^{\gamma}(z) = 0$, 故对一切 $j \geqslant 0$ 有 $p^{\gamma}(j) = 0$; 而当 (6.2.6) 式对某个 $0 < z < 1$ 成立时, 有

$$
\lim _ {s \to 1 -} f ^ {\gamma} (s) = \lim _ {n \to \infty} f ^ {\gamma} (g _ {n} (z)) = \lim _ {n \to \infty} \prod_ {k = n} ^ {\infty} h (g _ {k - 1} (0)) = 1,
$$

从而 $(p^{\gamma}(j):j\geqslant 0)$ 为概率分布.由母函数的凸性可知

$$
\frac {1 - h (z)}{1 - z}, \quad \frac {1 - z}{g (z) - z} = \left[ 1 - \frac {1 - g (z)}{1 - z} \right] ^ {- 1}, \quad \frac {1 - h (z)}{g (z) - z}
$$

都在区间 $(0,1)$ 内不降. 因此有

$$
\begin{array}{l} \sum_ {k = 1} ^ {\infty} [ 1 - h (g _ {k - 1} (z)) ] = \sum_ {k = 1} ^ {\infty} \frac {1 - h (g _ {k - 1} (z))}{g (g _ {k - 1} (z)) - g _ {k - 1} (z)} [ g _ {k} (z) - g _ {k - 1} (z) ] \\ \leqslant \int_ {z} ^ {1} \frac {1 - h (s)}{g (s) - s} \mathrm{d} s \\ \leqslant \sum_ {k = 1} ^ {\infty} \frac {1 - h (g _ {k} (z))}{g (g _ {k} (z)) - g _ {k} (z)} [ g _ {k} (z) - g _ {k - 1} (z) ] \\ = \sum_ {k = 1} ^ {\infty} [ 1 - h (g _ {k} (z)) ] \frac {g _ {k} (z) - g _ {k - 1} (z)}{g (g _ {k} (z)) - g (g _ {k - 1} (z))}, \\ \end{array}
$$

---

6.2 过程的长时间行为

159

其中

$$
\frac {g _ {k} (z) - g _ {k - 1} (z)}{g (g _ {k} (z)) - g (g _ {k - 1} (z))} \rightarrow \frac {1}{g ^ {\prime} (1)} \geqslant 1, \quad k \rightarrow \infty .
$$

所以 (6.2.6) 式成立当且仅当 (6.2.4) 式成立. □

推论 6.2.9 设  $m := g'(1) < 1$ . 则存在离散概率分布  $(p^{\gamma}(j): j \in \mathbb{Z}_{+})$  使对任何  $i, j \geqslant 0$  有  $\lim_{n \to \infty} p_{n}^{\gamma}(i, j) = p^{\gamma}(j)$  当且仅当

$$
\sum_ {j = 0} ^ {\infty} p (j) \ln (j + 1) <   \infty . \tag {6.2.7}
$$

证明 因为 $m := g'(1) < 1$, 当 $z \to 1-$ 时有 $(g(z) - z)/(1 - z) = (1 - m) + o(1)$. 所以 (6.2.4) 式成立的充要条件是

$$
\int_ {0} ^ {1} \frac {1 - h (z)}{1 - z} \mathrm{d} z <   \infty . \tag {6.2.8}
$$

记 $b(k) = \sum_{j=0}^{k} p(j)$. 则有

$$
\frac {1 - h (z)}{1 - z} = \sum_ {k = 0} ^ {\infty} [ 1 - b (k) ] z ^ {k} = \sum_ {k = 0} ^ {\infty} z ^ {k} \sum_ {j = k + 1} ^ {\infty} p (j).
$$

所以 (6.2.8) 式成立当且仅当

$$
\sum_ {k = 1} ^ {\infty} \frac {1}{1 + k} \sum_ {j = k + 1} ^ {\infty} p (j) = \sum_ {j = 1} ^ {\infty} p (j) \sum_ {k = 1} ^ {j - 1} \frac {1}{1 + k} <   \infty .
$$

注意

$$
\begin{array}{l} \sum_ {j = 1} ^ {\infty} p (j) \sum_ {k = 1} ^ {j - 1} \frac {1}{1 + k} \leqslant \sum_ {j = 1} ^ {\infty} p (j) \int_ {0} ^ {j - 1} \frac {1}{1 + s} \mathrm{d} s \\ = \sum_ {j = 1} ^ {\infty} p (j) \ln j \\ \end{array}
$$

和

$$
\begin{array}{l} \sum_ {j = 1} ^ {\infty} p (j) \sum_ {k = 1} ^ {j - 1} \frac {1}{1 + k} \geqslant \sum_ {j = 1} ^ {\infty} p (j) \int_ {1} ^ {j} \frac {1}{1 + s} \mathrm{d} s \\ \geqslant \sum_ {j = 1} ^ {\infty} p (j) \ln (1 + j) - \ln 2. \\ \end{array}
$$

因此 (6.2.8) 式成立当且仅当 (6.2.7) 式成立. □

---

160

第六章 分支过程及其应用

## 练习题

1. 在定理 6.1.6 的假设条件下, 对于 $k \geqslant 1$ 记 $X_{n}^{(k)} = k^{-1}X_{n}$. 证明对 $\varepsilon > 0$ 和 $i, n \geqslant 1$ 有

$$
\mathbf {P} \big (| X _ {n} ^ {(k)} - i m ^ {n} | \geqslant \varepsilon \big | X _ {0} ^ {(k)} = i \big) \to 0 \quad (k \to \infty).
$$

在分支过程的应用中, 往往考虑规模庞大的群体, 因此在计算个体数量时通常会用很大的单位 $k$ (千、万、亿等). 这样 $X_{n}^{(k)}$ 就代表第 $n$ 代个体的总数. 本题的结论说明, 当 $X_{0}^{(k)} = i$ 时 $X_{n}^{(k)}$ 与 $im^{n}$ 有较大偏差的概率很小.

提示: 利用定理 6.1.6, 并注意

$$
\mathbf {E} (X _ {n} ^ {(k)} | X _ {0} ^ {(k)} = i) = k ^ {- 1} \mathbf {P} (X _ {n} | X _ {0} = k i) = i m ^ {n}
$$

和

$$
\mathbf {E} \big (| X _ {n} ^ {(k)} - i m ^ {n} | ^ {2} \big | X _ {0} ^ {(k)} = i \big) = k ^ {- 2} \mathbf {P} \big (| X _ {n} - k i m ^ {n} | ^ {2} \big | X _ {0} = k i \big).
$$

2. 在定理 6.2.7 的条件下, 记 $\sigma^2 = m_2 - m^2 = \mathbf{Var}_1(X_1)$. 证明

$$
\lim _ {n \to \infty} \mathbf {E} _ {1} [ (m ^ {- n} X _ {n} - W) ^ {2} ] = 0, \quad \mathbf {V a r} _ {1} (W) = \sigma^ {2} m ^ {- 1} (m - 1) ^ {- 1}.
$$

提示: 参考 [1, p.9, Theorem 2].

3. 在定理 6.2.8 的条件下, 利用母函数方法证明  $(p^{\gamma}(j): j \in \mathbb{Z}_{+})$  是转移矩阵  $P_{n}^{\gamma}$  的平稳分布, 即有

$$
\sum_ {i = 0} ^ {\infty} p ^ {\gamma} (i) p _ {n} ^ {\gamma} (i, j) = p ^ {\gamma} (j), \quad j \geqslant 0.
$$

4. 在定理 6.2.8 的条件下, 讨论  $\mathbf{E}(Y_{n}|Y_{0}=i)$  当  $n\to\infty$  时的极限行为.

## \*6.3 随机游动中的分支过程

本节中我们利用分支过程的理论研究一维简单随机游动的轨道结构, 给出其对不同水平的穿越次数的分布的刻画.

## 6.3.1 随机游动的下穿

称取值于 $\mathbb{Z}$ 的随机过程 $X = (X_{n}:n\geqslant 0)$ 在时刻 $k\geqslant 1$ 下穿水平 $a\in \mathbb{Z}$ 是指$X_{k - 1} = a + 1$ 且 $X_{k} = a,$ 称它在时刻 $k\geqslant 1$ 上穿水平 $a\in \mathbb{Z}$ 是指 $X_{k - 1} = a - 1$ 且

---

\*6.3 随机游动中的分支过程

161

$X_{k}=a.$  下穿和上穿统称为穿越.

定理 6.3.1 设  $e=\{e(n):n\geqslant0\}$  是从  $a+1$  出发在 a 停止的简单随机游动, 其转移矩阵  $P^{a}$  由 (4.4.7) 式给出, 其中  $0\leqslant p\leqslant q\leqslant1$ . 令  $\xi$  是 e 下穿水平  $a+1$  的次数, 则  $\xi$  有分布

$$
\mathbf {P} (\xi = k) = q p ^ {k}, \quad k = 0, 1, \dots . \tag {6.3.1}
$$

证明 根据随机游动的平移不变性, 我们可以假定 $a = 0$. 这样就有 $e(0) = 1$, 故 $\sigma_1 := \inf \{n \geqslant 0 : e(n) = 1\} = 0$. 欲使 $\xi = 0$ 必须且只需: $e$ 在 1 时刻下降到位置 0, 因而 $\tau_1 := \inf \{n \geqslant 1 : e(n) = 0\} = 1$, 此后 $e$ 停止运动. 否则 $e$ 在 1 时刻上升到位置 2, 因 $p \leqslant q$ 它必在之后某时刻回到位置 1, 从而导致 $\xi \geqslant 1$. 因 $\mathbf{P}(e(0) = 1) = 1$, 有

$$
\mathbf {P} (\xi = 0) = \mathbf {P} (e (1) = 0) = \mathbf {P} (e (1) = 0 | e (0) = 1) = q.
$$

欲使 $\xi = 1$ 必须且只需: $e$ 在 1 时刻上升到位置 2, 因 $p \leqslant q$ 它必在之后的时刻 $\sigma_1' := \inf \{n \geqslant 1 : e(n) = 1\}$ 回到位置 1, 接着 $e$ 在 $\sigma_1' + 1$ 时刻下降到 0, 因而 $\tau_1 := \inf \{n \geqslant \sigma_1' : e(n) = 0\} = \sigma_1' + 1$, 此后 $e$ 停止运动. 由于 $\mathbf{P}(e(0) = e(\sigma_1') = 1) = 1$, 根据强马氏性有

$$
\begin{array}{l} \mathbf {P} (\xi = 1) = \mathbf {P} (e (1) = 2, e (\sigma_ {1} ^ {\prime}) = 1, e (\sigma_ {1} ^ {\prime} + 1) = 0) \\ = \mathbf {P} (e (1) = 2, e (\sigma_ {1} ^ {\prime}) = 1) \mathbf {P} (e (\sigma_ {1} ^ {\prime} + 1) = 0 | e (1) = 2, e (\sigma_ {1} ^ {\prime}) = 1) \\ = \mathbf {P} (e (1) = 2) \mathbf {P} (e (\sigma_ {1} ^ {\prime} + 1) = 0 | e (\sigma_ {1} ^ {\prime}) = 1) = p q. \\ \end{array}
$$

与上面推导类似地可以证明 (6.3.1) 式对 $k \geqslant 2$ 成立. □

## 6.3.2 反射游动中的分支过程

考虑 $\mathbb{Z}_{+}$ 上的从 $c \geqslant 0$ 出发的反射简单随机游动 $W = (W_{n}: n \geqslant 0)$. 它的转移矩阵 $Q_{+}^{0}$ 由 (4.4.4) 式给出, 其中 $a = 0$ 而 $0 < p \leqslant q < 1$. 对于 $b \geqslant 1$ 用 $\xi_{i}(b)$ 表示 $(W_{n})$ 的第 $i$ 个由 $b$ 到 $b - 1$ 的游程 $e_{i}(b) = \{e_{i}(b, n): n \geqslant 0\}$ 下穿水平 $b$ 的次数.

定理 6.3.2 随机变量  $\xi_{i}(b), i \geqslant 1, b \geqslant 1$  独立且均服从 (6.3.1) 式给出的分布.

证明 根据定理 4.4.1, 游程 $e_i(b), i \geqslant 1$ 相互独立且等价, 所以 $\xi_i(b), i \geqslant 1$ 独立同分布. 由定理 6.3.1 知它们服从 (6.3.1) 式给出的分布. 下面考虑位置 $b > a \geqslant 1$. 根据定理 4.4.5, 利用 $(W_n)$ 的由 $a + 1$ 到 $a$ 的游程可以构造一个 $\mathbb{Z}_{a+} := \mathbb{Z} \cap [a, \infty)$ 上的反射简单游动 $(W_n^+)$, 利用 $(W_n)$ 的由 $a$ 到 $a + 1$ 的游程可以构造一个 $\mathbb{Z}_{0,a+1} := \mathbb{Z} \cap [0, a + 1]$ 上的反射简单游动 $(W_n^-)$, 且二者相互独立. 显然 $(W_n)$ 的由 $b$ 到 $b - 1$ 的第 $i$ 个游程也是 $(W_n^+)$ 的由 $b$ 到 $b - 1$ 的第 $i$ 个游程, 而 $(W_n)$ 的由 $a$ 到 $a - 1$ 的第 $i$ 个游程也是 $(W_n^-)$ 的由 $a$ 到 $a - 1$ 的第 $i$ 个游程. 所以 $\{\xi_i(b): i \geqslant 1, b \geqslant a + 1\}$ 和 $\{\xi_i(a): i \geqslant 1\}$ 独立. 由此易知 $\xi_i(b), i \geqslant 1, b \geqslant 1$ 独立. □

---

162

第六章 分支过程及其应用

由于 $W = (W_{n}:n\geqslant 0)$ 是不可约且常返的, 它无限次地下穿 $\mathbb{Z}_{+}$ 的每个水平. 取定整数 $x\geqslant 1$ 并令 $\tau$ 为 $(W_{n})$ 的第 $x$ 次下穿水平0的时刻. 用 $X_{b}$ 表示 $(W_{n\wedge \tau}:n\geqslant 0)$ 下穿水平 $b\in \mathbb{Z}_{+}$ 的次数. 注意 $X_{b}$ 也是 $(W_{n\wedge \tau}:n\geqslant 0)$ 中包含的由 $b + 1$ 到 $b$ 的游程的个数.

定理 6.3.3 在上面的假定下有:

(1) $(X_{b}:b\geqslant c-1)$ 是分支过程, 其后代分布由(6.3.1)式给出;
(2) $(X_{b}:0\leqslant b\leqslant c - 1)$ 是带移民的分支过程, 其后代分布由 (6.3.1) 式给出, 而移民分布为集中于 1 的退化分布.

证明 (1) 考虑水平 $b + 1 > b > b - 1 \geqslant c - 1$. 此时轨道 $(W_{n \wedge \tau}: n \geqslant 0)$ 的每个由 $b + 1$ 到 $b$ 的游程都属于某个由 $b$ 到 $b - 1$ 的游程, 故不难发现

$$
X _ {b} = \sum_ {i = 1} ^ {X _ {b - 1}} \xi_ {i} (b), \quad b > b - 1 \geqslant c - 1. \tag {6.3.2}
$$

由定理 6.3.2 知  $(X_{b}: b \geqslant c - 1)$  是分支过程且有 (6.3.1) 式给出的后代分布.

(2) 考虑水平 $0 \leqslant b - 1 < b < b + 1 \leqslant c$. 此时轨道 $(W_{n \wedge \tau}: n \geqslant 0)$ 在首次到达位置 $b$ 前刚好完成一个由 $b + 1$ 到 $b$ 的游程, 而它在其后的每个由 $b + 1$ 到 $b$ 的游程都属于某个由 $b$ 到 $b - 1$ 的游程, 故有

$$
X _ {b} = 1 + \sum_ {i = 1} ^ {X _ {b - 1}} \xi_ {i} (b), \quad 0 \leqslant b - 1 <   b \leqslant c - 1.
$$

再由定理 6.3.2 知  $(X_{b}:0\leqslant b\leqslant c-1)$  是带移民的分支过程, 其后代分布由 (6.3.1) 式给出, 而移民分布为集中于 1 的退化分布. □

类似定理 6.3.3 的结果有多种不同的形式, 其连续时空版本通常称为雷伊-奈特 (Ray-Knight) 型定理; 参见 [9,27]. 分支结构模型在随机复杂系统的研究中有很多重要的应用, 参见 [1,3,24,32] 及其所引文献.

## 练习题

1. 设 $S = (S_{n}: n \geqslant 0)$ 是 $\mathbb{Z}$ 上的从 $S_{0} = c \geqslant 0$ 出发的一维对称简单随机游动. 取 $k \geqslant 1$ 并用 $\tau$ 表示 $(S_{n})$ 的第 $k$ 次下穿水平 0 的时刻. 令 $X_{b}$ 为 $(S_{n \wedge \tau}: n \geqslant 0)$ 下穿水平 $b \in \mathbb{Z}$ 的次数. 证明:

(1) $(X_{b}:b\geqslant c-1)$ 是分支过程, 其后代分布由 (6.3.1) 式给出, 其中 p=q=1/2;
(2) $(X_{-a}:a\geqslant1)$ 是分支过程, 其后代分布由(6.3.1)式给出, 其中 p=q=1/2;
(3) $\{X_b : 0 \leqslant b \leqslant c - 1\}$ 为带移民的分支过程, 其后代分布由 (6.3.1) 式给出, 其中 $p = q = 1/2$, 而移民分布为集中于 1 的退化分布.

---

\*6.3 随机游动中的分支过程

163

2. 固定 $c < b \in \mathbb{Z}_{+}$. 设 $W = (W_{n}: n \geqslant 0)$ 是 $\mathbb{Z}_{0,b}$ 上的从 $W_{0} = c \geqslant 0$ 出发的一维反射简单随机游动, 其转移矩阵 $P^{0,b}$ 由 (4.4.6) 式给出, 其中 $a = 0$ 而 $p, q > 0$ 满足 $p + q = 1$ (不要求 $q \leqslant p$). 取 $k \geqslant 1$ 并用 $\tau$ 表示 $(W_{n})$ 的第 $k$ 次下穿水平 0 的时刻. 对 $0 \leqslant a \leqslant b - 1$ 令 $X_{a}$ 为 $(W_{n \wedge \tau}: n \geqslant 0)$ 下穿水平 $a$ 的次数. 证明:

(1) $(X_{b}:c-1\leqslant a\leqslant b-1)$ 是分支过程, 其后代分布由 (6.3.1) 式给出;
(2) $\{X_b: 0 \leqslant b \leqslant c - 1\}$ 为带移民的分支过程, 其后代分布由 (6.3.1) 式给出, 而移民分布为集中于 1 的退化分布.

3. 设 $W = (W_{n}: n \geqslant 0)$ 是 $\mathbb{Z}$ 上的从 $W_{0} = 0$ 出发的一维简单随机游动, 其转移矩阵 $P$ 由 (4.4.3) 式给出, 其中 $0 < p < q < 1$. 令 $X_{a}$ 为 $W$ 下穿水平 $a \in \mathbb{Z}$ 的次数. 记 $r = p / q$. 证明:

(1) $\mathbf{P}(X_0 = i) = r^i (1 - r), i \geqslant 0;$
(2) 对 $a \geqslant 0$ 有 $\mathbf{P}(X_a = 0) = 1 - r^{a + 1}$, $\mathbf{P}(X_a = i) = r^{a + i}(1 - r)$, $i \geqslant 1$.

4. 在上题假设条件下, 证明对 $a \leqslant -1$ 下穿次数 $X_{a}$ 服从几何分布 $G(1 - r)$, 即有 $\mathbf{P}(X_{a} = i) = r^{i-1}(1 - r), i \geqslant 1$.
