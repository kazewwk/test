# 第五章 马氏链的遍历理论

原始 PDF 第 125–148 页。

124

第五章 马氏链的遍历理论

本章讨论马氏链的遍历理论, 包括平稳链、不变测度、弱遍历定理、遍历定理和转移矩阵的遍历性. 在形式上, 马氏链的遍历定理通常是指它的转移概率或轨道按时间平均的极限定理, 前者称为弱遍历定理, 后者称为强遍历定理.

## 5.1 可逆性与对称性

马氏链的不变测度就是在它的转移矩阵作用下保持不变的测度. 以不变概率测度为初始分布的马氏链是一个平稳过程, 即其有限维分布具有时间上的推移不变性. 可逆性是指过程的分布性质在时间逆转下的不变性, 即将时间反转后过程的有限维分布保持不变. 对称性是可逆性的推广. 可逆过程和对称过程具有许多特殊性质, 非常便于处理.

## 5.1.1 平稳链和可逆链

考虑定义于概率空间 $(\Omega, \mathcal{F}, \mathbf{P})$ 上的具有可数状态空间 $E$ 和转移矩阵 $P = (p_{ij}: i, j \in E)$ 的马氏链 $X = (X_n : n \geqslant 0)$.

定义 5.1.1 称 E 上的概率测度  $\pi = (\pi_{i} : i \in E)$  为 X 或 P 的平稳分布, 是指

$$
\sum_ {i \in E} \pi_ {i} p _ {i j} = \pi_ {j}, \quad j \in E. \tag {5.1.1}
$$

称  $\pi$  为 X 或 P 的可逆分布, 是指

$$
\pi_ {i} p _ {i j} = \pi_ {j} p _ {j i}, \quad i, j \in E. \tag {5.1.2}
$$

显然, 若  $\pi$  是 X 的可逆分布, 则它一定是 X 的平稳分布.

定义 5.1.2 称马氏链 X 为平稳的, 是指  $X_{n}$  的概率分布不依赖于时间  $n \geqslant 0$ . 根据 X 的马氏性, 这意味着对任意的  $n \geqslant 0$  和  $k \geqslant 0$  下面的随机向量具有相同的概率分布:

$$
(X _ {0}, X _ {1}, \dots , X _ {k}), \quad (X _ {n}, X _ {n + 1}, \dots , X _ {n + k}).
$$

命题 5.1.1 以  $\pi = (\pi_{i} : i \in E)$  为初始分布且有转移矩阵 P 的马氏链 X 是平稳的当且仅当  $\pi$  是 P 的平稳分布.

证明 设 $X$ 是以 $\pi$ 为初始分布的马氏链. 根据马氏性有

$$
\mathbf {P} (X _ {1} = j) = \sum_ {i \in E} \mathbf {P} (X _ {0} = i) \mathbf {P} (X _ {1} = j | X _ {0} = i) = \sum_ {i \in E} \pi_ {i} p _ {i j},
$$

---

5.1 可逆性与对称性

125

所以 $X_{1}$ 服从分布 $\pi$ 当且仅当 (5.1.1) 式成立.利用马氏性和数学归纳法可得命题结论.$\square$

定义 5.1.3 称马氏链 X 是可逆的, 是指对任何  $n \geqslant 0$  下面的随机向量具有相同的概率分布:

$$
(X _ {0}, X _ {1}, \dots , X _ {n - 1}, X _ {n}), \quad (X _ {n}, X _ {n - 1}, \dots , X _ {1}, X _ {0}),
$$

命题 5.1.2 以  $\pi = (\pi_{i} : i \in E)$  为初始分布且有转移矩阵 P 的马氏链 X 是可逆的当且仅当  $\pi$  是 P 的可逆分布.

证明 如果 $X$ 可逆, 那么对任意的 $i, j \in E$ 我们有

$$
\pi_ {i} p _ {i j} = \mathbf {P} (X _ {0} = i, X _ {1} = j) = \mathbf {P} (X _ {1} = i, X _ {0} = j) = \pi_ {j} p _ {j i},
$$

即 (5.1.2) 式成立. 反之, 假设 (5.1.2) 式成立. 则对  $n \geqslant 0$  和  $\{i_{0}, i_{1}, \cdots, i_{n}\} \subseteq E$  有

$$
\begin{array}{l} \mathbf {P} (X _ {0} = i _ {0}, X _ {1} = i _ {1}, \dots , X _ {n - 1} = i _ {n - 1}, X _ {n} = i _ {n}) \\ = \pi_ {i _ {0}} p _ {i _ {0} i _ {1}} p _ {i _ {1} i _ {2}} \dots p _ {i _ {n - 2} i _ {n - 1}} p _ {i _ {n - 1} i _ {n}} \\ = p _ {i _ {1} i _ {0}} \pi_ {i _ {1}} p _ {i _ {1} i _ {2}} \dots p _ {i _ {n - 2} i _ {n - 1}} p _ {i _ {n - 1} i _ {n}} \\ = p _ {i _ {1} i _ {0}} p _ {i _ {2} i _ {1}} \pi_ {i _ {2}} \dots p _ {i _ {n - 2} i _ {n - 1}} p _ {i _ {n - 1} i _ {n}} \\ = \dots \\ = p _ {i _ {1} i _ {0}} p _ {i _ {2} i _ {1}} \dots p _ {i _ {n - 1} i _ {n - 2}} p _ {i _ {n} i _ {n - 1}} \pi_ {i _ {n}} \\ = \pi_ {i _ {n}} p _ {i _ {n} i _ {n - 1}} p _ {i _ {n - 1} i _ {n - 2}} \dots p _ {i _ {2} i _ {1}} p _ {i _ {1} i _ {0}} \\ = \mathbf {P} (X _ {0} = i _ {n}, X _ {1} = i _ {n - 1}, \dots , X _ {n - 1} = i _ {1}, X _ {n} = i _ {0}). \\ \end{array}
$$

这说明 $X$ 是可逆的. $\square$

可逆马氏链必然是平稳的. 物理学中称满足 (5.1.2) 式的过程 $(X_{n}: n \geqslant 0)$ 是细致平衡的, 意为对任意一对状态 $\{i, j\} \subseteq E$, 过程从 $i$ 运动到 $j$ 的概率与从 $j$ 运动到 $i$ 的概率相同. 此时, 对给定的 $n \geqslant 1$ 令 $Y_{k} = X_{n-k}$, 则 $(Y_{k}: 0 \leqslant k \leqslant n)$ 也是以 $P$ 为转移矩阵的平稳马氏链.

定义 5.1.4 对 $n \geqslant 1$ 写 $P^n = (p_{ij}^n : i, j \in E)$. 称 $P$ 是遍历的, 是指存在 $E$ 上的概率分布 $\pi = (\pi_i : i \in E)$ 使得

$$
\lim _ {n \to \infty} p _ {i j} ^ {n} = \pi_ {j}, \quad i, j \in E. \tag {5.1.3}
$$

命题 5.1.3 若 P 是遍历转移矩阵且  $\pi$  由 (5.1.3) 式确给出, 则  $\pi$  是 P 的唯一的平稳分布.

证明 根据 (5.1.3) 式和法图定理有

$$
\pi_ {j} = \lim _ {n \to \infty} p _ {i j} ^ {n} = \lim _ {n \to \infty} \sum_ {k \in E} p _ {i k} ^ {n - 1} p _ {k j} \geqslant \sum_ {k \in E} \pi_ {k} p _ {k j}.
$$

---

126

第五章 马氏链的遍历理论

将上式对 $j \in E$ 求和, 易见两端均为 1 , 故这里只能成立等号. 所以 $\pi$ 是 $P$ 的平稳分布. 假设 $\mu = (\mu_i : i \in E)$ 也是 $P$ 的平稳分布. 根据控制收敛定理有

$$
\mu_ {j} = \lim _ {n \to \infty} \sum_ {k \in E} \mu_ {k} p _ {k j} ^ {n} = \sum_ {k \in E} \mu_ {k} \pi_ {j} = \pi_ {j}.
$$

这说明 $\pi$ 是 $P$ 的唯一的平稳分布. $\square$

## 5.1.2 对称测度

作为平稳分布和可逆分布的推广, 我们引入不变测度和对称测度的概念如下:

定义 5.1.5 称 E 上的  $\sigma$  有限测度  $\mu = (\mu_{i} : i \in E)$  是 X 或 P 的不变测度, 是指

$$
\sum_ {i \in E} \mu_ {i} p _ {i j} = \mu_ {j}, \quad j \in E. \tag {5.1.4}
$$

称  $\mu$  是 X 或 P 的对称测度, 是指

$$
\mu_ {i} p _ {i j} = \mu_ {j} p _ {j i}, \quad i, j \in E. \tag {5.1.5}
$$

命题 5.1.4 转移矩阵 P 关于测度  $\mu$  是对称的当且仅当有

$$
\mu_ {i} p _ {i j} (n) = \mu_ {j} p _ {j i} (n), \quad n \geqslant 0, i, j \in E. \tag {5.1.6}
$$

证明 若 (5.1.6) 式成立, 显然 $P$ 关于测度 $\mu$ 对称. 反之, 若 $P$ 关于 $\mu$ 是对称的, 则 (5.1.6) 式对于 $n = 1$ 成立. 假若 (5.1.6) 式对于某个 $n \geqslant 1$ 成立, 则有

$$
\begin{array}{l} \mu_ {i} p _ {i j} (n + 1) = \sum_ {k \in E} \mu_ {i} p _ {i k} (n) p _ {k j} = \sum_ {k \in E} p _ {k i} (n) \mu_ {k} p _ {k j} \\ = \sum_ {k \in E} p _ {k i} (n) p _ {j k} \mu_ {j} = \mu_ {j} p _ {j i} (n + 1). \\ \end{array}
$$

由数学归纳法知 (5.1.6) 式对于所有 $n \geqslant 1$ 成立. $\square$

例 5.1.1 对于每个  $i \in Z$  取常数  $p_{i}, q_{i} > 0$  满足  $p_{i} + q_{i} = 1$ . 定义 Z 上的转移矩阵  $P = (p_{ij} : i, j \in \mathbb{Z})$  如下:

$$
p _ {i j} = p _ {i} 1 _ {\{j = i + 1 \}} + q _ {i} 1 _ {\{j = i - 1 \}}, \quad i, j \in \mathbb {Z}.
$$

以 $P$ 为转移矩阵的马氏链也称为生灭过程. 令

$$
\mu_ {0} = 1, \quad \mu_ {i} = \prod_ {k = 0} ^ {i - 1} \frac {p _ {k}}{q _ {k + 1}} (i > 0), \quad \mu_ {i} = \prod_ {k = i + 1} ^ {0} \frac {q _ {k}}{p _ {k - 1}} (i <   0),
$$

则当 $|i - j| \geqslant 2$ 时有 $\mu_i p_{ij} = \mu_j p_{ji} = 0$. 当 $|i - j| = 1$ 时, 利用上式易证 $\mu_i p_{ij} = \mu_j p_{ji}$. 所以 $\mu$ 是 $P$ 的对称测度.

---

5.1 可逆性与对称性

127

例5.1.2 设有 $m(\geqslant 1)$ 个粒子被放置到一个容器中, 容器被挡板分为左右两侧. 每过一个时间单位从 $m$ 个粒子中等概率地随机选择一个, 将它移到容器的另外一侧. 用 $X_{n}$ 表示第 $n$ 次操作完成后容器左侧粒子的个数, 则 $X = (X_{n}: n \geqslant 0)$ 是整数区间 $E := [0, m]$ 上的马氏链, 其转移矩阵 $P = (p_{ij}: 0 \leqslant i, j \leqslant m)$ 可表示为

$$
p _ {i j} = \Big (\frac {i}{m} \Big) 1 _ {\{j = i - 1 \}} + \Big (1 - \frac {i}{m} \Big) 1 _ {\{j = i + 1 \}}.
$$

易证 $X$ 不可约, 以2为周期且有平稳分布 $\pi = (\pi_i:0\leqslant i\leqslant m)$, 其中 $\pi_j = 2^{-m}\mathrm{C}_m^i$. 此外, 对任何 $1\leqslant i\leqslant m$ 有 $\pi_{i}p_{i,i - 1} = \pi_{i - 1}p_{i - 1,i}$. 由命题5.1.2知 $\pi$ 是 $X$ 的可逆分布. 该马氏链称为埃伦菲斯特(Ehrenfest)模型, 是为研究气体分子的扩散行为而设计的简化模型.

## 5.1.3 对称测度的判别法

马氏链的对称测度一定是不变测度, 且比不变测度更容易处理. 事实上, 对称测度总可以用转移矩阵的元素给出显式表示, 而不变测度通常很难做到这点. 下面的定理属于柯尔莫哥洛夫, 它提供了一个非常有用的对称性判别法, 同时给出了对称测度的表示.

定理 5.1.5 不可约转移矩阵  $P = (p_{ij} : i, j \in E)$  有非零的对称测度当且仅当对状态空间中任意的环路  $i_{1} \rightarrow i_{2} \rightarrow \cdots \rightarrow i_{r} \rightarrow i_{1}$  有等式

$$
p _ {i _ {1} i _ {2}} p _ {i _ {2} i _ {3}} \dots p _ {i _ {r - 1} i _ {r}} p _ {i _ {r} i _ {1}} = p _ {i _ {1} i _ {r}} p _ {i _ {r} i _ {r - 1}} \dots p _ {i _ {3} i _ {2}} p _ {i _ {2} i _ {1}}. \tag {5.1.7}
$$

此时, 可以定义非零对称测度  $\mu = (\mu_{i} : i \in E)$  如下: 取状态  $i_{0} \in E$  并令  $\mu_{i_{0}} = 1$ ; 对于  $i \neq i_{0} \in E$  取  $\{i_{1}, i_{2}, \cdots, i_{n}\} \subseteq E$  满足  $p_{i_{0}i_{1}} p_{i_{1}i_{2}} \cdots p_{i_{n-1}i_{n}} p_{i_{n}i} > 0$ , 再令

$$
\mu_ {i} = \frac {p _ {i _ {0} i _ {1}} p _ {i _ {1} i _ {2}} \cdots p _ {i _ {n - 1} i _ {n}} p _ {i _ {n} i}}{p _ {i i _ {n}} p _ {i _ {n} i _ {n - 1}} \cdots p _ {i _ {2} i _ {1}} p _ {i _ {1} i _ {0}}} = \prod_ {k = 0} ^ {n} \frac {p _ {i _ {k} i _ {k + 1}}}{p _ {i _ {k + 1} i _ {k}}}, \tag {5.1.8}
$$

其中  $i_{n+1}=i$ . 上式右边的值与  $\{i_{1},i_{2},\cdots,i_{n}\}$  的选择无关, 且分子和分母均严格正.

证明 假设 $\mu$ 是 $P$ 的非零的对称测度. 由命题5.1.4, 对 $n \geqslant 0$ 和 $i, j \in E$ 有 $\mu_{i} p_{ij}(n) = \mu_{j} p_{ji}(n)$. 因 $P$ 是不可约的, 若 $\mu_{i_0} > 0$, 对 $i_0 \neq j \in E$ 可取 $n \geqslant 1$ 使得 $p_{i_0j}(n) > 0$, 从而 $\mu_{j} p_{ji_0}(n) = \mu_{i_0} p_{i_0j}(n) > 0$. 由此可见 $\mu_j > 0$ 对所有 $j \in E$ 成立. 对任意的环路 $i_1 \to i_2 \to \dots \to i_r \to i_1$ 有

$$
\begin{array}{l} \mu_ {i _ {1}} p _ {i _ {1} i _ {2}} p _ {i _ {2} i _ {3}} \dots p _ {i _ {r - 1} i _ {r}} p _ {i _ {r} i _ {1}} = p _ {i _ {2} i _ {1}} \mu_ {i _ {2}} p _ {i _ {2} i _ {3}} \dots p _ {i _ {r - 1} i _ {r}} p _ i _ {r} i _ {1} \\ = \dots = p _ {i _ {2} i _ {1}} p _ {i _ {3} i _ {2}} \dots p _ {i _ {r} i _ {r - 1}} p _ {i _ {1} i _ {r}} \mu_ i _ {1} \\ = \mu_ {i _ {1}} p _ {i _ {1} i _ {r}} p _ {i _ {r} i _ {r - 1}} \dots p _ {i _ {3} i _ {2}} p _ {i _ {2} i _ {1}}. \\ \end{array}
$$

由于  $\mu_{i_{1}}>0$ ，上式等价于 (5.1.7) 式。反之，假设 (5.1.7) 式对所有环路成立。我们证明 (5.1.8) 式定义了非零对称测度  $\mu$ 。先证该式中分子和分母均不为零。取  $\{l_{1}, l_{2}, \cdots, l_{r}\} \subseteq$

---

128

第五章 马氏链的遍历理论

E 满足  $p_{il_{1}}p_{l_{1}l_{2}}\cdots p_{l_{r-1}l_{r}}p_{l_{r}i_{0}}>0,$  则

$$
p _ {i _ {0} i _ {1}} p _ {i _ {1} i _ {2}} \dots p _ {i _ {n - 1} i _ {n}} p _ {i _ {n} i} \cdot p _ {i l _ {1}} p _ {l _ {1} l _ {2}} \dots p _ {l _ {r - 1} l _ {r}} p _ {l _ {r} i _ {0}} > 0.
$$

由 (5.1.7) 式得

$$
p _ {i _ {0} l _ {r}} p _ {l _ {r} l _ {r - 1}} \dots p _ {l _ {2} l _ {1}} p _ {l _ {1} i} \cdot p _ {i i _ {n}} p _ {i _ {n} i _ {n - 1}} \dots p _ {i _ {2} i _ {1}} p _ {i _ {1} i _ {0}} > 0.
$$

所以 (5.1.8) 式中分子和分母均不为零. 再证该式的值与  $\{i_{1}, i_{2}, \cdots, i_{n}\} \subseteq E$  的选择无关. 假定还有  $\{j_{1}, j_{2}, \cdots, j_{r}\} \subseteq E$  使  $p_{i_{0}j_{1}}p_{j_{1}j_{2}} \cdots p_{j_{r-1}j_{r}}p_{j_{r}i} > 0$ . 应用 (5.1.7) 式于环路

$$
\begin{array}{l} i _ {0} \rightarrow i _ {1} \rightarrow i _ {2} \rightarrow \dots \rightarrow i _ {n} \rightarrow i _ {n + 1} = i = j _ {r + 1} \\ \rightarrow j _ {r} \rightarrow j _ {r - 1} \rightarrow \dots \rightarrow j _ {2} \rightarrow j _ {1} \rightarrow j _ {0} = i _ {0}, \\ \end{array}
$$

得到

$$
\begin{array}{l} 1 = \frac {p _ {i _ {0} i _ {1}} p _ {i _ {1} i _ {2}} \cdots p _ {i _ {n - 1} i _ {n}} p _ {i _ {n} i} p _ {i j _ {r}} p _ {j _ {r} j _ {r - 1}} \cdots p _ {j _ {2} j _ {1}} p _ {j _ {1} i _ {0}}}{p _ {i _ {0} j _ {1}} p _ {j _ {1} j _ {2}} \cdots p _ {j _ {r - 1} j _ {r}} p _ {j _ {r} i} p _ {i i _ {n}} p _ {i _ {n} i _ {n - 1}} \cdots p _ {i _ {2} i _ {1}} p _ {i _ {1} i _ {0}}} \\ = \prod_ {k = 0} ^ {n} \frac {p _ {i _ {k} i _ {k + 1}}}{p _ {i _ {k + 1} i _ {k}}} \prod_ {k = 0} ^ {r} \frac {p _ {j _ {k + 1} j _ {k}}}{p _ {j _ {k} j _ {k + 1}}} = \prod_ {k = 0} ^ {n} \frac {p _ {i _ {k} i _ {k + 1}}}{p _ {i _ {k + 1} i _ {k}}} \left(\prod_ {k = 0} ^ {r} \frac {p _ {j _ {k} j _ {k + 1}}}{p _ {j _ {k + 1} j _ {k}}}\right) ^ {- 1}. \\ \end{array}
$$

这就证明了 (5.1.8) 式的值与  $i_{1}, i_{2}, \cdots, i_{n}$  的选取无关, 而且  $\mu_{i} > 0$ . 最后, 我们来证明由 (5.1.8) 式定义的  $\mu$  是对称测度. 对于  $i_{0} \neq j \in E$ , 由互通性必有  $\{j_{1}, j_{2}, \cdots, j_{r}\} \subseteq E$  满足

$$
p _ {i _ {0} j _ {1}} p _ {j _ {1} j _ {2}} \dots p _ {j _ {r - 1} j _ {r}} p _ {j _ {r} j} > 0.
$$

注意

$$
\mu_ {i} p _ {i j} = \frac {p _ {i _ {0} i _ {1}} p _ {i _ {1} i _ {2}} \cdots p _ {i _ {n - 1} i _ {n}} p _ {i _ {n} i} \cdot p _ {i j}}{p _ {i i _ {n}} p _ {i _ {n} i _ {n - 1}} \cdots p _ {i _ {2} i _ {1}} p _ {i _ {1} i _ {0}}}, \quad \mu_ {j} p _ {j i} = \frac {p _ {i _ {0} j _ {1}} p _ {j _ {1} j _ {2}} \cdots p _ {j _ {r - 1} j _ {r}} p _ {j _ {r} j} \cdot p _ {j i}}{p _ {j j _ {r}} p _ {j _ {r} j _ {r - 1}} \cdots p _ {j _ {2} j _ {1}} p _ {j _ {1} i _ {0}}},
$$

由 (5.1.7) 式有

$$
\begin{array}{l} p _ {i _ {0} i _ {1}} p _ {i _ {1} i _ {2}} \dots p _ {i _ {n - 1} i _ {n}} p _ {i _ {n} i} \cdot p _ {i j} \cdot p _ {j j _ {r}} p _ {j _ {r} j _ {r - 1}} \dots p _ {j _ {2} j _ {1}} p _ {j _ {1} i _ {0}} \\ = p _ {i _ {0} j _ {1}} p _ {j _ {1} j _ {2}} \dots p _ {j _ {r - 1} j _ {r}} p _ {j _ {r} j} \cdot p _ {j i} \cdot p _ {i i _ {n}} p _ {i _ {n} i _ {n - 1}} \dots p _ {i _ {2} i _ {1}} p _ {i _ {1} i _ {0}}. \\ \end{array}
$$

所以  $\mu_{i}p_{ij}=\mu_{j}p_{ji}$ ，即  $\mu$  的确是 X 的对称测度。☐

推论 5.1.6 不可约转移矩阵 P 的非零对称测度点点严格正, 而且在相差一个常数因子的意义下唯一.

---

5.1 可逆性与对称性

129

证明 前一结果由定理 5.1.5 给出.假设  $\nu = (\nu_{i} : i \in E)$  是非零对称测度且  $\nu_{i_{0}} > 0$ .令  $\mu = (\mu_{i} : i \in E)$  是由 (5.1.8) 式给出的非零对称测度.对于  $i_{0} \neq i \in E$ ，由互通性必有  $\{j_{1}, j_{2}, \cdots, j_{n}\} \subseteq E$  满足  $p_{i_{0}j_{1}}p_{j_{1}j_{2}} \cdots p_{j_{n-1}j_{n}}p_{j_{n}i} > 0$ .由  $\nu$  的对称性有  $\nu_{i}p_{ij} = \nu_{j}p_{ji}$ .反复应用此关系得到

$$
\nu_ {i _ {0}} p _ {i _ {0} j _ {1}} p _ {j _ {1} j _ {2}} \dots p _ {j _ {n - 1} j _ {n}} p _ {j _ {n} i} = \nu_ {i} p _ {i j _ {n}} p _ {j _ {n} j _ {n - 1}} \dots p _ {j _ {2} j _ {1}} p _ {j _ {1} i _ {0}}.
$$

再由(5.1.8)式可见 $\nu_{i} / \nu_{i_0} = \mu_{i} / \mu_{i_0}$. 所以 $\nu$ 和 $\mu$ 至多只相差一个常数因子. □

命题 5.1.7 设转移矩阵  $P = (p_{ij} : i, j \in E)$  以  $\mu = (\mu_i : i \in E)$  为对称测度. 对于  $E_0 \subseteq E$  令

$$
\tilde {p} _ {i j} = \left\{ \begin{array}{l l} p _ {i j}, & i \neq j \in E _ {0}, \\ p _ {i i} + \sum_ {k \notin E _ {0}} p _ {i k}, & i = j \in E _ {0}, \end{array} \right.
$$

则  $\tilde{P}=(\tilde{p}_{ij}:i,j\in E_{0})$  是一个转移矩阵, 并且以  $\tilde{\mu}=(\mu_{i}:i\in E_{0})$  为对称测度.

证明 对于 $i = j \in E_0$ 显然有 $\mu_i \tilde{p}_{ij} = \mu_j \tilde{p}_{ji}$. 对于不同的 $i, j \in E_0$ 有 $\mu_i \tilde{p}_{ij} = \mu_i p_{ij} = \mu_j p_{ji} = \mu_j \tilde{p}_{ji}$. 所以 $\tilde{\mu}$ 是 $\tilde{P}$ 的对称测度. □

上面的定理说明, 将一个马氏链 “限制在” 它的状态空间的某个子集  $E_{0}$  上, 新马氏链的对称测度就是原来马氏链的对称测度在  $E_{0}$  上的限制. 这个特点为对称马氏链的研究提供了很大的方便. 但是类似的性质对于不变测度一般并不成立.

## 练习题

1. 令 $P$ 是有限状态空间 $E$ 上的转移矩阵. 设对每个 $j \in E$ 极限 $\pi_j = \lim_{n \to \infty} p_{ij}(n)$ 存在且不依赖于 $i \in E$. 证明 $\pi = (\pi_j : j \in E)$ 是 $P$ 的平稳分布.
2. 令 $(X_{n}: n \geqslant 0)$ 是状态空间 $E$ 上的以 $P$ 为转移矩阵的马氏链。设对每个 $j \in E$ 极限 $\pi_{j} = \lim_{n \to \infty} p_{ij}(n)$ 存在且不依赖于 $i \in E$。证明对任何 $j, k \in E$ 极限 $\lim_{n \to \infty} \mathbf{P}\{(X_{n}, X_{n+1}) = (j, k)\}$ 存在。
3. 令 $P = (p_{ij}: i, j \in \mathbb{Z})$ 是 $\mathbb{Z}$ 上的简单随机游动的转移矩阵, 即有

$$
p _ {i j} = p 1 _ {\{j = i + 1 \}} + q 1 _ {\{j = i - 1 \}}, \quad i, j \in \mathbb {Z}.
$$

其中 $p, q > 0$ 满足 $p + q = 1$. 再令 $\pi$ 为 $\mathbb{Z}$ 上的计数测度. 证明 $\pi$ 是 $P$ 的不变测度, 且它是对称测度当且仅当 $p = q = 1 / 2$.

4. 考虑状态空间 $E = \{1, 2, 3\}$ 上的概率分布 $\mu = (1/3, 1/3, 1/3)$. 定义 $E$ 上的转

---

130

第五章 马氏链的遍历理论

移矩阵 P 如下:

$$
P = \left( \begin{array}{c c c} 0 & 1 / 2 & 1 / 2 \\ 1 / 2 & 0 & 1 / 2 \\ 1 / 2 & 1 / 2 & 0 \end{array} \right),
$$

证明 $\mu$ 是 $P$ 唯一的可逆分布. 由命题5.1.7可得 $P$ 在 $E_0 := \{1,2\}$ 上的限制为

$$
\tilde {P} = \left( \begin{array}{c c} 1 / 2 & 1 / 2 \\ 1 / 2 & 1 / 2 \end{array} \right).
$$

验证  $\mu$  在  $E_{0}$  上的限制  $\tilde{\mu}:=(1/3,1/3)$  是  $\tilde{P}$  的可逆分布.

5. 考虑上题中的状态空间 $E$ 和概率分布 $\mu$. 这里定义 $E$ 上的转移矩阵 $P$ 如下:

$$
P = \left( \begin{array}{c c c} 1 / 2 & 1 / 2 & 0 \\ 0 & 1 / 2 & 1 / 2 \\ 1 / 2 & 0 & 1 / 2 \end{array} \right),
$$

(1) 证明 $\mu$ 是 $P$ 的唯一平稳分布. (2) 转移矩阵 $P$ 是否有可逆分布?

## 5.2 弱遍历定理

弱遍历定理是指转移概率按时间平均的极限定理. 给定可数状态空间 $E$ 上的转移矩阵 $P = (p_{ij})_{i,j \in E}$, 可以定义其关于时间的平均

$$
L _ {n} = \frac {1}{n} \sum_ {k = 0} ^ {n - 1} P ^ {k} = \frac {1}{n} \sum_ {k = 1} ^ {n} P ^ {k - 1}, \quad n \geqslant 1. \tag {5.2.1}
$$

注意, 这里的每个 $L_{n}$ 也都是 $E$ 上的转移矩阵, 而 $P$ 的弱遍历性是指该矩阵当 $n \to \infty$ 时的收敛性质.

## 5.2.1 弱遍历性

定理 5.2.1 (弱遍历定理) 极限  $\lim_{n\to\infty}L_n=L$  存在且满足方程 PL=LP=L=L².

证明 记 $P^n = (p_{ij}(n))_{i,j \in E}$ 和 $L_n = (L_{ij}(n))_{i,j \in E}$. 对于 $i, j \in E$ 序列 $\{L_{ij}(n): n \geqslant 0\}$ 非负有界, 故存在非负整数列 $n_k(i, j) \to \infty$ 使极限 $\lim_{k \to \infty} L_{ij}(n_k(i, j)) = L_{ij}$ 存

---

5.2 弱遍历定理

131

在. 利用对角线抽取法可得到不依赖于 $(i,j)$ 的子列 $n_k \to \infty$ 使

$$
\lim _ {k \to \infty} L _ {n _ {k}} = \lim _ {k \to \infty} (L _ {i j} (n _ {k})) = (L _ {i j}) = L. \tag {5.2.2}
$$

另一方面, 由 (5.2.1) 式不难看出

$$
L _ {n} P = P L _ {n} = \frac {1}{n} \sum_ {k = 1} ^ {n} P ^ {k} = L _ {n} + \frac {1}{n} (P ^ {n} - I), \tag {5.2.3}
$$

其中 $I$ 是单位矩阵. 用1表示所有元素都为1的列向量. 我们有 $P1 = 1$. 根据(5.2.2)式和(5.2.3)式, 并利用有界收敛定理得

$$
P L = \lim _ {k \to \infty} (P L _ {n _ {k}}) = \lim _ {k \to \infty} L _ {n _ {k}} + \lim _ {k \to \infty} \frac {1}{n _ {k}} (P ^ {n _ {k}} - I) = L.
$$

类似地, 利用法图定理得

$$
L P \leqslant \lim _ {k \to \infty} (L _ {n _ {k}} P) = \lim _ {k \to \infty} L _ {n _ {k}} + \lim _ {k \to \infty} \frac {1}{n _ {k}} (P ^ {n _ {k}} - I) = L.
$$

假若上式中有严格不等号成立, 即存在  $i, j \in E$  使

$$
\sum_ {k \in E} L _ {i k} p _ {k j} <   L _ {i j},
$$

则导致矛盾的结论

$$
\sum_ {k \in E} L _ {i k} = \sum_ {l \in E} \sum_ {k \in E} L _ {i k} p _ {k l} <   \sum_ {l \in E} L _ {i l}.
$$

可见必然有 PL = LP = L. 由 (5.2.2) 式及法图定理有  $L1 \leqslant 1$ , 进而利用有界收敛定理得

$$
L = \lim _ {k \to \infty} \frac {1}{n _ {k}} \sum_ {r = 1} ^ {n _ {k}} L = \lim _ {k \to \infty} \frac {1}{n _ {k}} \sum_ {r = 1} ^ {n _ {k}} L P ^ {r - 1} = \lim _ {k \to \infty} L L _ {n _ {k}} = L L = L ^ {2}.
$$

最后我们来证明 $\lim_{n\to \infty}L_n = L$。假设有子列 $m_k\to \infty$ 使 $\lim_{k\to \infty}L_{m_k} = M$。与上式类似地可得

$$
L = \lim _ {k \to \infty} \frac {1}{m _ {k}} \sum_ {r = 1} ^ {m _ {k}} L = \lim _ {k \to \infty} \frac {1}{m _ {k}} \sum_ {r = 1} ^ {m _ {k}} L P ^ {r - 1} = \lim _ {k \to \infty} L L _ {m _ {k}} = L M.
$$

同理可知 M = ML. 再由法图定理有

$$
L = \lim _ {k \to \infty} \frac {1}{m _ {k}} \sum_ {r = 1} ^ {m _ {k}} L = \lim _ {k \to \infty} \frac {1}{m _ {k}} \sum_ {r = 1} ^ {m _ {k}} P ^ {r - 1} L = \lim _ {k \to \infty} (L _ {m _ {k}} L) \geqslant M L.
$$

同理有 $LM \leqslant M$. 于是 $M = ML \leqslant L = LM \leqslant M$. 因而有 $M = ML = LM = L$. 这就证明了 $\lim_{n \to \infty} L_n = L$. $\square$

---

132

第五章 马氏链的遍历理论

## 5.2.2 极限矩阵的表示

由定理 5.2.1 知 L 的每一行都构成转移矩阵 P 的不变测度. 下面的定理给出了极限矩阵  $L = \lim_{n \to \infty} L_n$  一种表示.

定理 5.2.2 假定  $P = (p_{ij})_{i,j \in E}$  不可约且常返. 将状态空间表示为  $E := \{i_k : k = 1, 2, \cdots\}$ . 令  $\lim_{n \to \infty} L_n = L$ . 则有:

(1) 存在一个非负行向量 $\pi = (\pi_i : i \in E)$ 使得

$$
L = \left( \begin{array}{c} \pi \\ \pi \\ \vdots \end{array} \right) = \left( \begin{array}{c c c} \pi_ {1} & \pi_ {2} & \dots \\ \pi_ {1} & \pi_ {2} & \dots \\ \vdots & \vdots \end{array} \right), \tag {5.2.4}
$$

或简写为  $L=1\pi$ ，其中 1 表示所有元素都为 1 的列向量；

(2) $\pi$ 的元素或者全为零, 或者全不为零;
(3) $P$ 有平稳分布当且仅当 $\pi$ 不为零, 这时 $\pi$ 是 $P$ 的唯一平稳分布.

证明 (1) 由 $PL = L$ 知 $L$ 的每一列都构成一个调和函数, 因而是过份函数. 再由于 $P$ 不可约, 根据定理 4.3.15 知 $L$ 的每一列都是常函数, 即 $L$ 的每行都相同. 故只需令 $\pi_i = L_{ii}, i \in E$, 就得到 (5.2.4) 式.

(2) 设有 $i \in E$ 使 $\pi_i = L_{ii} = 0$. 由于任意 $j \in E$ 与 $i$ 互通, 必存在 $m, n \geqslant 1$ 使得 $p_{ij}(m)p_{ji}(n) > 0$. 再注意 $p_{ii}(k + m + n) \geqslant p_{ij}(m)p_{jj}(k)p_{ji}(n)$, 就得到

$$
\frac {1}{l} \sum_ {k = 0} ^ {l - 1} p _ {i i} (k + m + n) \geqslant p _ {i j} (m) p _ {j i} (n) \frac {1}{l} \sum_ {k = 0} ^ {l - 1} p _ {j j} (k).
$$

令 $l \to \infty$, 就得到

$$
0 = \pi_ {i} = L _ {i i} \geqslant p _ {i j} (m) p _ {j i} (n) L _ {j j} \geqslant 0,
$$

因而  $\pi_{j}=L_{jj}=0.$

(3) 由关系 $LP = L$ 显然有 $\pi P = \pi$, 即 $\pi$ 是 $P$ 的不变测度. 设 $\pi$ 不为 0 . 再由

$$
1 \pi = L = L ^ {2} = (1 \pi) (1 \pi) = 1 \Big (\sum_ {j \in E} \pi_ {j} \Big) \pi = \Big (\sum_ {j \in E} \pi_ {j} \Big) 1 \pi ,
$$

可见 $\sum_{j\in E}\pi_j = 1$ ，于是 $\pi$ 是 $P$ 的平稳分布.假设 $\rho$ 也是 $P$ 的平稳分布.则有 $\rho = \rho P^n$ 进而 $\rho = \rho L_n$ .利用有界收敛定理得 $\rho = \rho L = \rho 1\pi = \pi ,$ 唯一性得证.另一方面，若 $P$ 有平稳分布 $\rho$ ，由上面推导有 $\rho = \pi$ ，故 $\pi \neq 0$ □

对于一般的转移矩阵 P, 由其分解 (4.3.9) 式可以导出极限矩阵 L 的如下结构.

---

5.2 弱遍历定理

133

定理 5.2.3 对于 E 上的任意转移矩阵 P, 极限矩阵  $L = \lim_{n \to \infty} L_n$  具有以下形式:

$$
\begin{array}{l} U \quad H _ {1} \quad H _ {2} \quad \dots \quad H _ {n} \quad \dots \\ L = \begin{array}{c} U \\ H _ {1} \\ H _ {2} \\ \vdots \\ H _ {n} \\ \vdots \end{array} \left( \begin{array}{c c c c c c} 0 & (f _ {i j} ^ {*} (^ {1} \pi) _ {j}) & (f _ {i j} ^ {*} (^ {2} \pi) _ {j}) & \dots & (f _ {i j} ^ {*} (^ {n} \pi) _ {j}) & \dots \\ 0 & 1 (^ {1} \pi) & 0 & \dots & 0 & \dots \\ 0 & 0 & 1 (^ {2} \pi) & \dots & 0 & \dots \\ \vdots & \vdots & \vdots & & \vdots \\ 0 & 0 & 0 & \dots & 1 (^ {n} \pi) & \dots \\ \vdots & \vdots & \vdots & & \vdots \end{array} \right), \tag {5.2.5} \\ \end{array}
$$

其中 $f_{ij}^{*} = \sum_{k=1}^{\infty} f_{ij}(k)$, 而 $(^{k}\pi)_{j}$ 表示行向量 $^{k}\pi$ 的第 $j$ 个元素. 另外, 这里每个 $^{k}\pi$ 的元素或全为零或全不为零.

证明 (1) 考虑 $i \in E$ 和 $j \in U$. 注意 $f_{ij}^{*} = \sum_{n=1}^{\infty} f_{ij}(n) \leqslant 1$. 根据推论 4.3.5, 我们有

$$
p _ {j j} ^ {*} = \sum_ {n = 0} ^ {\infty} p _ {j j} (n) <   \infty ,
$$

故 $\lim_{n\to \infty}p_{jj}(n) = 0.$ 再由(4.3.2)式并利用有界收敛定理得

$$
\lim _ {n \to \infty} p _ {i j} (n) = \lim _ {n \to \infty} \sum_ {k = 0} ^ {\infty} f _ {i j} (k) 1 _ {\{k \leqslant n \}} p _ {j j} (n - k) = 0.
$$

显然上式蕴涵

$$
L _ {i j} = \lim _ {n \to \infty} \frac {1}{n} \sum_ {m = 0} ^ {n - 1} p _ {i j} (m) = 0.
$$

(2) 考虑 $i, j \in H_k$. 我们可以将 $P$ 限制在 $H_k$ 上得到转移矩阵 $^k P$. 对此应用定理 5.2.1 和定理 5.2.2 得到行向量 $^k \pi$ 使

$$
L _ {i j} = \lim _ {n \to \infty} \frac {1}{n} \sum_ {m = 0} ^ {n - 1} p _ {i j} (m) = (^ {k} \pi) _ {j}.
$$

(3) 考虑 $i \in H_k$ 及 $j \in H_l$, 其中 $k \neq l$. 此时, 对任何 $n \geqslant 1$ 有 $p_{ij}(n) = 0$, 故得 $L_{ij} = 0$.

(4) 考虑 $i \in U$ 和 $j \in H_k$. 回忆 (4.3.2) 式, 我们有

$$
\frac {1}{n} \sum_ {m = 1} ^ {n - 1} p _ {i j} (m) = \frac {1}{n} \sum_ {m = 1} ^ {n - 1} \sum_ {r = 1} ^ {m} f _ {i j} (r) p _ {j j} (m - r)
$$

---

134

第五章 马氏链的遍历理论

$$
\begin{array}{l} = \frac {1}{n} \sum_ {r = 1} ^ {n - 1} f _ {i j} (r) \sum_ {m = r} ^ {n - 1} p _ {j j} (m - r) \\ = \sum_ {r = 1} ^ {\infty} f _ {i j} (r) 1 _ {\{r \leqslant n - 1 \}} \frac {1}{n} \sum_ {m = 0} ^ {n - r - 1} p _ {j j} (m). \\ \end{array}
$$

利用有界收敛定理得

$$
L _ {i j} = \lim _ {n \to \infty} \frac {1}{n} \sum_ {m = 0} ^ {n - 1} p _ {i j} (m) = \sum_ {r = 1} ^ {\infty} f _ {i j} (r) (^ {k} \pi) _ {j} = f _ {i j} ^ {*} (^ {k} \pi) _ {j}.
$$

故知预证结论成立. □

## 5.2.3 平均回访时间

考虑定义于概率空间 $(\Omega, \mathcal{F}, \mathbf{P})$ 上的以 $P = (p_{ij} : i, j \in E)$ 为转移矩阵马氏链 $X = (X_n : n \geqslant 0)$. 对于状态 $i \in E$ 记 $\mathbf{P}_i = \mathbf{P}(\cdot | X_0 = i)$. 再令 $T_i = \min \{n \geqslant 1 : X_n = i\}$, 并定义 $X$ 对 $i$ 的平均回访时间 $\mu_i = \mathbf{P}_i(T_i)$. 根据前面定义的概念, 当 $\mu_i < \infty$ 时, 状态 $i$ 是正常返的. 对于 $n \geqslant 1$ 记

$$
r _ {i i} (n) = \sum_ {k = n} ^ {\infty} f _ {i i} (k), \quad \alpha_ {i i} (n) = \sum_ {k = 1} ^ {n} r _ {i i} (k) p _ {i i} (n - k), \tag {5.2.6}
$$

则有

$$
\mu_ {i} = \sum_ {k = 1} ^ {\infty} k f _ {i i} (k) = \sum_ {k = 1} ^ {\infty} \sum_ {n = 1} ^ {k} f _ {i i} (k) = \sum_ {n = 1} ^ {\infty} r _ {i i} (n). \tag {5.2.7}
$$

另外, 不难看出对  $k \geqslant 1$  有

$$
\pi_ {i} = \lim _ {n \to \infty} \frac {1}{n} \sum_ {m = 0} ^ {n - 1} p _ {i i} (m) = \lim _ {n \to \infty} \frac {1}{n} \sum_ {m = 0} ^ {n - k} p _ {i i} (m). \tag {5.2.8}
$$

定理 5.2.4 状态  $i \in E$  正常返当且仅当  $\pi_{i} > 0$ . 而且, 此时有  $\mu_{i} = \mathbf{P}_{i}(T_{i}) = 1/\pi_{i}$ .

证明 首先, 考虑一般常返态 $i \in E$. 此时 $f_{ii}^{*} = 1$. 由 (4.3.2) 式有

$$
\begin{array}{l} p _ {i i} (n - 1) = \sum_ {k = 1} ^ {n - 1} f _ {i i} (k) p _ {i i} (n - 1 - k) \\ = \sum_ {k = 1} ^ {n - 1} [ r _ {i i} (k) - r _ {i i} (k + 1) ] p _ {i i} (n - 1 - k) \\ \end{array}
$$

---

5.2 弱遍历定理

135

$$
\begin{array}{l} = \alpha_ {i i} (n - 1) - \sum_ {k = 1} ^ {n - 1} r _ {i i} (k + 1) p _ {i i} (n - 1 - k) \\ = \alpha_ {i i} (n - 1) - \sum_ {k = 2} ^ {n} r _ {i i} (k) p _ {i i} (n - k). \\ \end{array}
$$

注意 $r_{ii}(1) = f_{ii}^{*} = 1$ ，故由上式有 $\alpha_{ii}(n) = \alpha_{ii}(n - 1)$ .于是得

$$
\alpha_ {i i} (n) = \alpha_ {i i} (n - 1) = \dots = \alpha_ {i i} (1) = r _ {i i} (1) p _ {i i} (0) = 1.
$$

这样, 我们有

$$
\begin{array}{l} 1 = \frac {1}{n} \sum_ {m = 1} ^ {n} \alpha_ {i i} (m) = \frac {1}{n} \sum_ {m = 1} ^ {n} \sum_ {k = 1} ^ {m} r _ {i i} (k) p _ {i i} (m - k) \\ = \frac {1}{n} \sum_ {k = 1} ^ {n} r _ {i i} (k) \sum_ {m = k} ^ {n} p _ {i i} (m - k) = \sum_ {k = 1} ^ {\infty} r _ {i i} (k) \frac {1}{n} \sum_ {m = 0} ^ {n - k} p _ {i i} (m) 1 _ {\{k \leqslant n \}}. \tag {5.2.9} \\ \end{array}
$$

现假设 $i \in E$ 正常返, 即 $\mu_i < \infty$. 基于 (5.2.7) 式和 (5.2.8) 式, 在 (5.2.9) 式中令 $n \to \infty$, 并应用有界收敛定理得

$$
1 = \sum_ {k = 1} ^ {\infty} r _ {i i} (k) \pi_ {i} = \mu_ {i} \pi_ {i},
$$

故 $\pi_{i} = 1 / \mu_{i} > 0$. 反之, 若 $\pi_{i} > 0$, 由定理5.2.3知 $i$ 是常返态, 故(5.2.9)式成立. 再由(5.2.7)式和(5.2.8)式, 令 $n \to \infty$ 并应用法图定理得

$$
1 \geqslant \sum_ {k = 1} ^ {\infty} r _ {i i} (k) \pi_ {i} = \mu_ {i} \pi_ {i}.
$$

因而 $\mu_{i} < \infty$ ，即 $i$ 正常返.再由前面的推导知 $\pi_i = 1 / \mu_i$ □

推论 5.2.5 若  $i \in E$  相对于 P 是正常返的, 则它所在的常返互通类  $H_{k}$  中全部状态都是正常返的, 即正常返性是互通类的性质.

证明 根据定理 5.2.3, 每个行向量 $k\pi$ 的元素全为零或全非零. 再由定理 5.2.4 立得结论. $\square$

根据定理 5.2.4 和推论 5.2.5, 正常返互通类  $H_{k}$  在分解 (5.2.5) 中对应的  $^{k}\pi$  的元素全非零. 再由定理 5.2.2 和定理 5.2.3 的证明知这样的  $^{k}\pi$  是集中在  $H_{k}$  上的唯一平稳分布.

推论 5.2.6 转移矩阵 P 有平稳分布当且仅当在其分解 (4.3.9) 中至少有一个正常返类。在这种情况下，它的任一平稳分布必是所有这些正常返类在分解 (5.2.5) 中对应的平稳分布  $k\pi$  ( $k=1,2,\cdots$ ) 的凸线性组合。

---

136

第五章 马氏链的遍历理论

证明 假定 $P$ 至少有一个正常返类 $H_{k}$. 则相应的 $^{k}\pi$ 就是 $P$ 的平稳分布. 反之, 假定 $P$ 有平稳分布 $\mu$. 令 $L$ 由定理 5.2.3 给出. 则有 $\mu P^{n} = \mu$ 和 $\mu L_{n} = \mu$. 利用控制收敛定理得 $\mu L = \mu$. 根据定理 5.2.4, 若 $j \in E$ 属于非常返类 $U$ 或某个零常返类, 则 $L$ 的第 $j$ 列全为 0, 从而

$$
\mu_ {j} = \sum_ {i \in E} \mu_ {i} L _ {i j} = 0.
$$

可见若 P 无正常返状态, 则对任何  $j \in E$  有  $\mu_{j} = 0$ , 这与  $\mu$  是概率测度矛盾. 因而 P 至少有一个正常返类. 如上所述, 当  $i \in U$  时有  $\mu_{i} = 0$ . 由 (5.2.5) 式可见 L 在  $H_{1} \cup H_{2} \cup \cdots$  上具有块状对角线结构. 这样, 当  $j \in E$  属于某个正常返类  $H_{k}$  时有

$$
\begin{array}{l} \mu_ {j} = \sum_ {i \in U} \mu_ {i} L _ {i j} + \sum_ {i \in H _ {k}} \mu_ {i} L _ {i j} + \sum_ {l \neq k} \sum_ {i \in H _ {l}} \mu_ {i} L _ {i j} \\ = \sum_ {i \in H _ {k}} \mu_ {i} L _ {i j} = \Big (\sum_ {i \in H _ {k}} \mu_ {i} \Big) (^ {k} \pi) _ {j}. \\ \end{array}
$$

所以只需取  $\sum_{i\in H_{k}}\mu_{i}$  为  $^{k}\pi$  的系数, 即知  $\mu$  是  $^{k}\pi$  的凸线性组合. □

推论 5.2.7 不可约的转移矩阵 P 是正常返的当且仅当它有唯一平稳分布  $\pi$ . 而且, 此时对任何  $i \in E$  有  $\pi_{i} = 1/\mu_{i} = 1/\mathbf{P}_{i}(T_{i})$ .

## 练习题

1. 证明: 若对 $i \in E$ 极限 $\lim_{n \to \infty} p_{ii}(n)$ 存在, 则该极限为 $1 / \mu_i = 1 / \mathbf{P}_i(T_i)$.

提示: 应用定理 5.2.2 和定理 5.2.4.

2. 设 P 是  $Z_{+}$ 上的转移矩阵, 首行为概率分布列  $\{0, a_{1}, a_{2}, \cdots\}$ , 对  $i \geqslant 1$  有  $p_{i,i-1} = 1$ , 而对其他  $i, j \in Z_{+}$  有  $p_{i,j} = 0$ . 讨论该转移矩阵的不可约性、点 0 的常返性和周期性.

提示: 注意 P 是不可约的当且仅当序列  $\{a_{1}, a_{2}, \cdots\}$  中有无穷多个元素非零.

3. 假定上题的序列  $\{a_{0}, a_{1}, a_{2}, \cdots\}$  中有无穷多个元素非零. 讨论转移矩阵 P 的正常返性和平稳分布的存在性.

提示: 此时 $P$ 是不可约的. 注意 $\mathbf{P}_0(T_0) < \infty$ 当且仅当 $\sum_{k=1}^{\infty} k a_k < \infty$. 在这种情况下 $P$ 是正常返的. 再应用推论 5.2.7.

4. 对于上面两题中讨论的马氏链, 记 $m = \inf \{i \geqslant 1 : a_i > 0\}$ 和 $T_m = \inf \{n \geqslant 1 : X_n = m\}$. 给出 $T_m$ 在 $\mathbf{P}_m$ 之下的分布并求期望 $\mathbf{E}_m(T_m) < \infty$.

---

5.3 强遍历定理

137

## 5.3 强遍历定理

考虑定义于概率空间 $(\Omega, \mathcal{F}, \mathbf{P})$ 上的具有状态空间 $E$ 的马氏链 $X = (X_n : n \geqslant 0)$, 其转移矩阵为 $P = (p_{ij})_{i,j \in E}$. 令 $\pi = (\pi_i : i \in E)$ 由定理5.2.2给出. 根据推论5.2.7, 若 $P$ 是不可约且正常返的, 则 $\pi$ 是它的唯一平稳分布. 强遍历性指的是 $X$ 的轨道的规范化经验测度收敛到 $\pi$ 的性质.

## 5.3.1 强遍历性

取定 $i \in E$. 令 $S_0 = 0$, 并对 $k \geqslant 1$ 递归地定义 $S_k = \min \{n > S_{k-1}: X_n = i\}$. 则 $\{S_1, S_2, \cdots\}$ 是递增的有限停时列. 直观上 $S_k$ 是 $X$ 第 $k$ 次到达状态 $i$ 的时间. 再对 $k \geqslant 0$ 令 $\eta_k = S_{k+1} - S_k$, 则有

$$
S _ {n + 1} = \sum_ {k = 0} ^ {n} \eta_ {k}, \quad n \geqslant 0.
$$

对  $n=1,2,\cdots$ ，令  $\rho_{i}(n)$  为 X 在时刻 n-1 或之前访问状态 i 的次数，即

$$
\rho_ {i} (n) = \sum_ {k = 0} ^ {n - 1} 1 _ {\{X _ {k} = i \}}. \tag {5.3.1}
$$

称每个  $\rho(n)=(\rho_{i}(n):i\in E)$  为 X 的经验测度或占位时测度.

定理 5.3.1 (强遍历定理) 设 X 为不可约的正常返马氏链, 则对任何  $i \in E$  当  $n \to \infty$  时几乎必然有  $\rho_{i}(n)/n \to \pi_{i}$ .

证明 根据强马氏性, 在条件概率 $\mathbf{P}(\cdot|S_1 < \infty) = \mathbf{P}(\cdot|S_1 < \infty, X_{S_1} = i)$ 之下 $(X_{n \wedge S_1}: n \geqslant 0)$ 和 $(X_{S_1+n}: n \geqslant 0)$ 独立, 且后者也是从 $i$ 出发以 $P$ 为转移矩阵的马氏链. 因为 $\mathbf{P}(S_1 < \infty) = \mathbf{P}(S_1 < \infty, X_{S_1} = i) = 1$, 所以在原概率 $\mathbf{P}$ 之下 $(X_{n \wedge S_1}: n \geqslant 0)$ 和 $(X_{S_1+n}: n \geqslant 0)$ 独立, 且后者是以 $P$ 为转移矩阵的马氏链. 注意 $\eta_0 = S_1$ 是 $(X_{n \wedge S_1}: n \geqslant 0)$ 对 $i$ 的首中时, 而当 $k \geqslant 2$ 时 $S_k - S_1$ 是 $(X_{S_1+n}: n \geqslant 0)$ 对 $i$ 的第 $k$ 次击中时. 因此 $\eta_0$ 和 $\eta_1, \eta_2, \cdots$ 独立. 再由定理4.3.3知 $\eta_1, \eta_2, \cdots$ 独立同分布, 其共同分布就是 $\eta_0 = S_1$ 在 $\mathbf{P}_i = \mathbf{P}(\cdot|X_0 = i)$ 之下的分布. 所以 $\mu_i := \mathbf{E}(\eta_1) = \mathbf{E}_i(S_1)$ 就是 $X$ 对 $i$ 的平均回访时间. 因为 $\mathbf{P}(\eta_0 < \infty) = 1$, 由强大数律几乎必然有

$$
\lim _ {n \to \infty} \frac {1}{n} \sum_ {k = 0} ^ {n} \eta_ {k} = \lim _ {n \to \infty} \frac {1}{n} \sum_ {k = 1} ^ {n} \eta_ {k} = \mu_ {i}.
$$

---

138

第五章 马氏链的遍历理论

再由常返性知当 $n\to \infty$ 时有 $\rho_i(n)\to \infty$ .根据上式有

$$
\lim _ {n \to \infty} \frac {\rho_ {i} (n)}{S _ {\rho_ {i} (n) + 1}} = \lim _ {n \to \infty} \frac {\rho_ {i} (n)}{\sum_ {k = 0} ^ {\rho_ {i} (n)} \eta_ {k}} = \frac {1}{\mu_ {i}} = \pi_ {i} \tag {5.3.2}
$$

和

$$
\lim _ {n \to \infty} \frac {\rho_ {i} (n)}{S _ {\rho_ {i} (n)}} = \lim _ {n \to \infty} \frac {\rho_ {i} (n) - 1}{\sum_ {k = 0} ^ {\rho_ {i} (n) - 1} \eta_ {k}} = \frac {1}{\mu_ {i}} = \pi_ {i}. \tag {5.3.3}
$$

注意 $\rho_{i}(n)$ 是 $X$ 在时刻 $n - 1$ 或之前访问状态 $i$ 的次数, 故 $S_{\rho_i(n)}$ 是 $X$ 在时刻 $n - 1$ 或之前最后一次访问状态 $i$ 的时刻, 而 $S_{\rho_i(n) + 1}$ 是 $X$ 此后再次访问状态 $i$ 的时刻. 所以有 $S_{\rho_i(n)} \leqslant n - 1 < S_{\rho_i(n) + 1}$. 因此

$$
\frac {\rho_ {i} (n)}{S _ {\rho_ {i} (n) + 1}} <   \frac {\rho_ {i} (n)}{n - 1} = \frac {1}{n - 1} \sum_ {k = 0} ^ {n - 1} 1 _ {\{X _ {k} = i \}} \leqslant \frac {\rho_ {i} (n)}{S _ {\rho_ {i} (n)}}.
$$

由 (5.3.2) 式和 (5.3.3) 式即得欲证结论. $\square$

引理 5.3.2 设  $\mu = (\mu_{i} : i \in E)$  和  $\mu(n) = (\mu_{i}(n) : i \in E)$ ,  $n = 1, 2, \cdots$  为 E 上的概率测度. 若对于每个  $i \in E$  都有  $\lim_{n \to \infty} \mu_{i}(n) = \mu_{i}$ ，则对 E 上的任何有界函数 g 有

$$
\lim _ {n \to \infty} \sum_ {i \in E} g (i) \mu_ {i} (n) = \sum_ {i \in E} g (i) \mu_ {i}. \tag {5.3.4}
$$

证明 若 E 为有限集, 预证结论显然, 故只考虑 E 无限的情况. 记  $E = \{i_{1}, i_{2}, \cdots\}$ . 对于任何  $\varepsilon > 0$  取  $m \geqslant 1$  充分大使  $\sum_{k=m+1}^{\infty} \mu_{i_{k}} < \varepsilon$ , 故  $\sum_{k=1}^{m} \mu_{i_{k}} > 1 - \varepsilon$ . 由假设存在  $N \geqslant 1$  使当  $n \geqslant N$  时有  $\sum_{k=1}^{m} \mu_{i_{k}}(n) > 1 - \varepsilon$ , 故  $\sum_{k=m+1}^{\infty} \mu_{i_{k}}(n) < \varepsilon$ . 这样, 我们有

$$
\begin{array}{l} \left| \sum_ {i \in E} g (i) \mu_ {i} (n) - \sum_ {i \in E} g (i) \mu_ {i} \right| \leqslant \left| \sum_ {k = 1} ^ {m} g (i _ {k}) \mu_ {i _ {k}} (n) - \sum_ {k = 1} ^ {m} g (i _ {k}) \mu_ {i _ {k}} \right| + \\ \Big | \sum_ {k = m + 1} ^ {\infty} g (i _ {k}) \mu_ {i _ {k}} (n) \Big | + \Big | \sum_ {k = m + 1} ^ {\infty} g (i _ {k}) \mu_ {i _ {k}} \Big | \\ \leqslant \| g \| \sum_ {k = 1} ^ {m} | \mu_ {i _ {k}} (n) - \mu_ {i _ {k}} | + 2 \| g \| \varepsilon . \\ \end{array}
$$

取极限得

$$
\operatorname * {l i m s u p} _ {n \to \infty} \Big | \sum_ {i \in E} g (i) \mu_ {i} (n) - \sum_ {i \in E} g (i) \mu_ {i} \Big | \leqslant 2 \| g \| \varepsilon .
$$

由  $\varepsilon > 0$  的任意性即得 (5.3.4) 式. □

---

5.3 强遍历定理

139

定理 5.3.3 (强遍历定理) 设 X 为不可约正常返马氏链, 则对 E 上的任何有界函数 g 几乎必然地有

$$
\lim _ {n \to \infty} \frac {1}{n} \sum_ {k = 0} ^ {n - 1} g (X _ {k}) = \sum_ {i \in E} g (i) \pi_ {i}. \tag {5.3.5}
$$

证明 根据定理 5.3.1, 随机概率测度  $(\rho_{i}(n)/n:i\in E)$  几乎必然地逐点收敛到概率测度  $(\pi_{i}:i\in E)$ . 再注意

$$
\frac {1}{n} \sum_ {k = 0} ^ {n - 1} g (X _ {k}) = \frac {1}{n} \sum_ {k = 0} ^ {n - 1} \sum_ {i \in E} g (i) 1 _ {\{X _ {k} = i \}} = \frac {1}{n} \sum_ {i \in E} g (i) \rho_ {i} (n).
$$

应用引理 5.3.2 即得 (5.3.5) 式. □

推论 5.3.4 若 X 是不可约正常返的平稳马氏链, 则对 E 上的任何有界函数 g 几乎必然有

$$
\lim _ {n \to \infty} \frac {1}{n} \sum_ {k = 0} ^ {n - 1} g (X _ {k}) = \mathbf {E} [ g (X _ {0}) ].
$$

证明 由定理5.2.2和推论5.2.7知 $\pi = (\pi_i:i\in E)$ 是 $P$ 的唯一平稳分布，因而$X$ 必有初分布 $\pi,$ 从而

$$
\mathbf {E} [ g (X _ {0}) ] = \sum_ {i \in E} g (i) \pi_ {i}.
$$

再根据定理5.3.3即得结论.□

## 5.3.2 平稳链的遍历性

考虑定义于概率空间  $(\Omega, \mathcal{F}, \mathbf{P})$  上, 具有状态空间 E, 以 P 为转移矩阵, 以其平稳分布  $\mu$  为初分布的平稳马氏链  $X = (X_{n} : n \geqslant 0)$ . 对于  $n \geqslant 0$  记  $\mathcal{F}_{n} = \sigma(X_{k} : 0 \leqslant k \leqslant n)$ . 再记  $\mathcal{F}_{\infty} = \sigma(X_{k} : k \geqslant 0)$ . 用 E 表示可数集 E 的所有子集构成的  $\sigma$  代数. 用  $E^{\infty}$  表示 E 的可数无穷乘积空间  $E^{\infty}$  上的乘积  $\sigma$  代数. 由高等概率论中的结果, 对任何  $F \in bF_{\infty}$ , 存在  $E^{\infty}$  上的函数  $f \in bE^{\infty}$  使  $F = f(X_{0}, X_{1}, \cdots)$ . 令

$$
\mathscr {F} _ {I} = \sigma \{F \in \mathrm{b} \mathscr {F} _ {\infty}: \text {存在} f \in \mathrm{b} \mathscr {E} ^ {\infty}, \text {使对任何} n \geqslant 0, \text {几乎}
$$

$$
\text {必然地} F = f (X _ {n}, X _ {n + 1}, \dots) \}.
$$

定理 5.3.5 在上述情况下, 以下性质等价:

(1)  $\mu$  只在一个正常返互通类 H 上有负荷;

---

140

第五章 马氏链的遍历理论

(2) 对 $E$ 上的任何有界函数 $g$ 几乎必然有

$$
\lim _ {n \to \infty} \frac {1}{n} \sum_ {k = 0} ^ {n - 1} g (X _ {k}) = \mathbf {E} [ g (X _ {0}) ]; \tag {5.3.6}
$$

(3) $\mathcal{F}_I$ 中仅含概率为0或1的事件.

证明 “(1)  $\Rightarrow$  (2)” 因为初分布  $\mu$  只在一个正常返互通类 H 上有测度, 对任何  $n \geqslant 0$  有  $\mathbf{P}(X_{n} \in H^{c}) = 0$ . 这样, 我们可以把 X 限制在 H 上, 视之为以 H 为状态空间的不可约正常返链, 再利用推论 5.3.4 就得到 (5.3.6) 式.

“(2) $\Rightarrow$ (3)”设 $F\in b\mathscr{F}_{I}\subseteq b\mathscr{F}_{\infty}$ . 用 $E_{i}$ 表示相对于 $\mathbf{P}_{i}=\mathbf{P}(\cdot|X_{0}=i)$ 的期望. 令 $\phi(i)=\mathbf{E}_{i}(F)=\mathbf{E}(F|X_{0}=i)$ . 不难发现

$$
\mathbf {E} (F | \mathcal {F} _ {n}) = \mathbf {E} [ f (X _ {n}, X _ {n + 1}, \dots) | \mathcal {F} _ {n} ] = \mathbf {E} [ f (X _ {n}, X _ {n + 1}, \dots) | X _ {n} ] = \phi (X _ {n}).
$$

可见 $\{\phi(X_n): n \geqslant 0\}$ 是杜布鞅. 于是几乎必然地有 $\lim_{n \to \infty} \phi(X_n) = F$, 进而

$$
\lim _ {n \to \infty} \frac {1}{n} \sum_ {k = 0} ^ {n - 1} \phi (X _ {k}) = F.
$$

但另一方面, 由 (5.3.6) 式几乎必然有

$$
\frac {1}{n} \sum_ {k = 0} ^ {n - 1} \phi (X _ {k}) \rightarrow \mathbf {E} \phi (X _ {0}) = \mathbf {E} [ \mathbf {E} (F | X _ {0}) ] = \mathbf {E} (F).
$$

所以 $F = \mathbf{E}(F)$ 几乎必然为常数. 特别地, 对任何 $A \in \mathcal{F}_I$ 示性函数 $1_A$ 几乎必然是常数, 也就是 $\mathbf{P}(A) = 0$ 或 1.

“(3)  $\Rightarrow$  (1)”用反证法. 假设 (3) 成立但 (1) 不成立. 因为平稳初分布不可能在非常返态和零常返态上有负荷, 所以  $\mu$  至少在两个正常返互通类  $H_{1}$  和  $H_{2}$  上有负荷. 令  $\Omega_{1} = \{X_{0} \in H_{1}\}$  和  $\Omega_{2} = \{X_{0} \in H_{2}\}$ . 则有

$$
\mathbf {P} (\varOmega_ {1}) = \mu (H _ {1}) > 0, \quad \mathbf {P} (\varOmega_ {2}) = \mu (H _ {2}) > 0.
$$

由 $X$ 的平稳性和常返互通类的性质, 在去掉 $\Omega$ 的一个零测子集后, 对任何 $n \geqslant 0$ 有 $\Omega_1 = \{X_n \in H_1\}$ 和 $\Omega_2 = \{X_n \in H_2\}$. 由此可知 $\Omega_1, \Omega_2 \in \mathcal{F}_I$, 而这与 (3) 成立的假设矛盾. $\square$

定理 5.3.6 设 $X = \{X_{n}: n \geqslant 0\}$ 是平稳马氏链, 而 $f$ 为 $(E^{\infty}, \mathcal{E}^{\infty})$ 上的可测函数, 满足 $\mathbf{P}[|f(X_0, X_1, \cdots)|] < \infty$. 若在 $L^{1}$ 意义下有

$$
\lim _ {n \to \infty} \frac {1}{n} \sum_ {k = 0} ^ {n - 1} f (X _ {k}, X _ {k + 1}, \dots) = G, \tag {5.3.7}
$$

则 G 关于  $F_{I}$  可测且  $G = \mathbf{E}[f(X_{0}, X_{1}, \cdots) | \mathcal{F}_{I}]$ .

---

5.3 强遍历定理

141

证明 若极限 (5.3.7) 存在, 显然 G 关于  $F_{\infty}$  可测. 根据高等概率论中的结果, 有  $(E^{\infty}, \mathcal{E}^{\infty})$  上的可测函数 g 使  $G = g(X_{0}, X_{1}, \cdots)$ . 由 (5.3.7) 式不难看出, 对任何  $m \geqslant 1$  有

$$
G = \lim _ {n \to \infty} \frac {1}{n} \sum_ {k = 0} ^ {n - 1} f (X _ {k + m}, X _ {k + m + 1}, \dots) = g (X _ {m}, X _ {m + 1}, \dots),
$$

从而 G 关于  $F_{I}$  可测. 另外, 对  $A \in F_{I}$ , 有  $(E^{\infty}, \mathcal{E}^{\infty})$  上的可测函数  $\psi$  使对任何  $k \geqslant 0$  有  $1_{A} = \psi(X_{k}, X_{k+1}, \cdots)$ . 由 (5.3.7) 式有

$$
\mathbf {E} (G 1 _ {A}) = \lim _ {n \to \infty} \frac {1}{n} \sum_ {k = 0} ^ {n - 1} \mathbf {E} [ f (X _ {k}, X _ {k + 1}, \dots) \psi (X _ {k}, X _ {k + 1}, \dots) ].
$$

由于 X 的平稳性, 上式变为

$$
\mathbf {E} (G 1 _ {A}) = \mathbf {E} [ f (X _ {0}, X _ {1}, \dots) \psi (X _ {0}, X _ {1}, \dots) ] = \mathbf {E} [ f (X _ {0}, X _ {1}, \dots) 1 _ {A} ].
$$

故有  $G = \mathbf{E}[f(X_{0}, X_{1}, \cdots) | \mathscr{F}_{I}]$ . ☐

称离散时间随机过程  $X = (X_{0}, X_{1}, X_{2}, \cdots)$  是平稳的，是指对任意的  $n \geqslant 0$  和  $k \geqslant 0$  下面的随机向量具有相同的概率分布:

$$
(X _ {0}, X _ {1}, \dots , X _ {k}), \quad (X _ {n}, X _ {n + 1}, \dots , X _ {n + k}).
$$

类似地, 可以定义连续时间平稳随机过程. 显然, 平稳马氏链是一种特殊的平稳过程. 平稳过程有丰富的理论和广泛的应用, 参见 [26,33].

## 练习题

1. 在定理 5.3.1 中假定 $X_0 = i$. 利用关于更新过程的结果给出该定理的简单证明.

提示: 此时与定理的原证明中类似地可知  $\eta_{0}, \eta_{1}, \eta_{2}, \cdots$  是独立同分布随机变量, 故  $S_{n}$  是 n 个独立同分布随机变量之和. 于是可以定义更新过程:

$$
N _ {i} (t) = \sum_ {k = 1} ^ {\infty} 1 _ {\{S _ {k} \leqslant t \}}, \quad t \geqslant 0.
$$

易知 $N_{i}(n) = \rho_{i}(n + 1) - 1$. 再由更新过程的性质可得定理结论.

2. 在一般情况下, 应用关于更新过程的结果给出定理 5.3.1 的证明.

提示: 对 $n \geqslant 0$ 令 $S_{n}^{*} = S_{n+1} - S_{1}$. 则 $S_{n}^{*} = \sum_{k=1}^{n} \eta_{k}$. 由定理 5.3.1 的原证明知 $\eta_{1}, \eta_{2}, \cdots$ 是独立同分布随机变量. 于是可以定义更新过程:

$$
N _ {i} ^ {*} (t) = \sum_ {k = 1} ^ {\infty} 1 _ {\{S _ {k} ^ {*} \leqslant t \}}, \quad t \geqslant 0.
$$

---

142

第五章 马氏链的遍历理论

易知 $N_{i}^{*}(n) = \rho_{i}(n + S_{1} + 1) - 1$. 再由更新过程的性质可得定理结论.

3. 设平稳马氏链 X 的正常返互通类为  $H_{1}, H_{2}, \cdots$  。再记  $\Omega_{k} = \{X_{0} \in H_{k}\}$  。证明  $\Omega$  上的关于  $F_{I}$  可测的函数在各个  $\Omega_{k}$  上几乎必然取常数值。

提示: 由 $X$ 的平稳性, 在去掉 $\Omega$ 的一个零测子集后, 对任何 $n \geqslant 0$ 有 $\Omega_k = \{X_n \in H_k\}$, 故 $\Omega_k \in \mathscr{F}_I$. 另一方面, 将 $X$ 限制在 $\Omega_k$ 应用定理 5.3.5 (3) 知对任何 $A \in \Omega_k \cap \mathscr{F}_I$ 有 $\mathbf{P}(A) = 0$ 或 $\mathbf{P}(\Omega_k)$.

4. 令 X 是例 5.1.2 中定义的埃伦菲斯特模型. 证明对  $E := \{0, 1, \cdots, m\}$  上的任何有界函数 g 几乎必然有

$$
\lim _ {n \to \infty} \frac {1}{n} \sum_ {k = 1} ^ {n} g (X _ {k}) = \sum_ {i = 0} ^ {m} \pi_ {i} g (i).
$$

## 5.4 转移矩阵的收敛性

本节里我们研究转移矩阵的遍历性和收敛性. 为此要用到一个重要的方法, 即耦合方法. 这里用到的只是非常特殊的情况. 关于耦合方法的系统理论和应用, 可参阅 [4,5].

## 5.4.1 马氏链的独立耦合

假定 $P = (p_{ij})_{i,j \in E}$ 是可数状态空间 $E$ 上的转移矩阵.考虑两个有相同转移矩阵 $P$ 的独立马氏链 $X = (X_n : n \geqslant 0)$ 与 $Y = (Y_n : n \geqslant 0)$.由独立性不难证明 $Z = \{(X_n, Y_n) : n \geqslant 0\}$ 是 $E^2$ 上的以

$$
(q _ {(i, j) (k, l)}: (i, j), (k, l) \in E ^ {2}) = (p _ {i k} p _ {j l}: (i, j), (k, l) \in E ^ {2}) \tag {5.4.1}
$$

为转移矩阵的马氏链. 我们称 $Z$ 为 $X$ 和 $Y$ 的独立耦合. 令 $D = \{(i, i) : i \in E\}$ 和 $\tau_{D} = \min \{n \geqslant 0 : (X_{n}, Y_{n}) \in D\}$.

命题5.4.1 对于 $n \geqslant 0$ 和 $j \in E$ 我们有

$$
\left| \mathbf {P} (Y _ {n} = j) - \mathbf {P} (X _ {n} = j) \right| \leqslant \mathbf {P} (\tau_ {D} > n).
$$

证明 令 $C_{mk} = \{\tau_D = m, Z_m = (k, k)\} = \{Z_m = (k, k), Z_l \notin D; l < m\}$. 利用 $Z$ 的强马氏性不难发现

$$
\mathbf {P} (X _ {n} = j, \tau_ {D} \leqslant n) = \sum_ {m = 0} ^ {n} \sum_ {i, k \in E} \mathbf {P} (Z _ {n} = (j, i), \tau_ {D} = m, Z _ {m} = (k, k))
$$

---

5.4 转移矩阵的收敛性

143

$$
\begin{array}{l} = \sum_ {m = 0} ^ {n} \sum_ {i, k \in E} \mathbf {P} (C _ {m k}) \mathbf {P} (Z _ {n} = (j, i) | C _ {m k}) \\ = \sum_ {m = 0} ^ {n} \sum_ {i, k \in E} \mathbf {P} (C _ {m k}) \mathbf {P} (Z _ {n} = (j, i) | Z _ {m} = (k, k)) \\ = \sum_ {m = 0} ^ {n} \sum_ {i, k \in E} \mathbf {P} (C _ {m k}) p _ {k j} (n - m) p _ {k i} (n - m) \\ = \sum_ {m = 0} ^ {n} \sum_ {k \in E} \mathbf {P} (C _ {m k}) p _ {k j} (n - m). \\ \end{array}
$$

类似地, 可证明 $\mathbf{P}(Y_n = j, \tau_D \leqslant n)$ 也具有上式最终的表达式, 从而

$$
\mathbf {P} (X _ {n} = j, \tau_ {D} \leqslant n) = \mathbf {P} (Y _ {n} = j, \tau_ {D} \leqslant n).
$$

这样, 我们有

$$
\begin{array}{l} \mathbf {P} (X _ {n} = j) = \mathbf {P} (X _ {n} = j, \tau_ {D} \leqslant n) + \mathbf {P} (X _ {n} = j, \tau_ {D} > n) \\ \leqslant \mathbf {P} (Y _ {n} = j, \tau_ {D} \leqslant n) + \mathbf {P} (\tau_ {D} > n) \\ \leqslant \mathbf {P} (Y _ {n} = j) + \mathbf {P} (\tau_ {D} > n). \\ \end{array}
$$

同理可证

$$
\mathbf {P} (Y _ {n} = j) \leqslant \mathbf {P} (X _ {n} = j) + \mathbf {P} (\tau_ {D} > n).
$$

综合上面两个不等式即得预证结论. $\square$

## 5.4.2 非周期矩阵的收敛性

下面的定理说明, 不可约、正常返、非周期的转移矩阵是遍历的.

定理 5.4.2 若 P 是不可约、正常返、非周期的, 则有  $\lim_{n\to\infty}P^{n}=L$ , 其中 L 由定理 5.2.2 给出.

证明 由定理5.2.2知 $P$ 有点点严格正的平稳分布 $\pi = (\pi_i : i \in E)$. 考虑前面定义的独立耦合 $Z = \{(X_n, Y_n) : n \geqslant 0\}$. 假定 $X_0 = i \in E$ 而 $Y_0$ 服从分布 $\pi$, 所以 $(Y_n : n \geqslant 0)$ 是一个平稳链. 因为 $P$ 是不可约非周期的, 由(5.4.1)式定义的转移矩阵 $(q_{(i,j)(k,l)})$ 显然也是不可约非周期的. 不难验证 $(\pi_i \pi_j : (i,j) \in E^2)$ 是 $(q_{(i,j)(k,l)})$ 的平稳分布, 且点点严格正. 再由推论5.2.6知 $Z$ 也是正常返的, 从而 $\mathbf{P}(\tau_D < \infty) = 1$. 利用命题5.4.1对于 $j \in E$ 有 $\lim_{n \to \infty} |\mathbf{P}(X_n = j) - \mathbf{P}(Y_n = j)| = 0$, 故得

$$
\lim _ {n \to \infty} p _ {i j} (n) = \lim _ {n \to \infty} \mathbf {P} (X _ {n} = j) = \lim _ {n \to \infty} \mathbf {P} (Y _ {n} = j) = \pi_ {j}.
$$

这就是定理的结论. $\square$

---

144

第五章 马氏链的遍历理论

定理 5.4.3 若 P 是不可约、零常返、非周期的, 则有  $\lim_{n\to\infty}P^{n}=0$ .

证明 类似于定理 5.4.2 的证明, 考虑独立耦合 $Z = \{(X_n, Y_n) : n \geqslant 0\}$. 这里假定 $X_0 = i \in E$ 而 $Y_0 = j \in E$. 分别考虑 $Z$ 非常返和常返两种情况. 若 $Z$ 非常返, 则对任何 $i \in E$ 有

$$
\sum_ {n = 0} ^ {\infty} p _ {i i} ^ {2} (n) <   \infty \Rightarrow \lim _ {n \to \infty} p _ {i i} (n) = 0,
$$

从而定理的结论成立. 若 $Z$ 常返, 则 $\mathbf{P}(\tau_D < \infty) = 1$. 再由命题5.4.1有

$$
\lim _ {n \to \infty} | p _ {i j} (n) - p _ {j j} (n) | = \lim _ {n \to \infty} | \mathbf {P} (X _ {n} = j) - \mathbf {P} (Y _ {n} = j) | = 0. \tag {5.4.2}
$$

取子列 $n_k \to \infty$ 使得

$$
\alpha_ {j} := \operatorname * {l i m s u p} _ {n \to \infty} p _ {j j} (n) = \lim _ {k \to \infty} p _ {j j} (n _ {k}).
$$

由 (5.4.2) 式有 $\lim_{k\to \infty}p_{ij}(n_k) = \alpha_j$. 利用法图定理得

$$
\sum_ {j \in E} \alpha_ {j} \leqslant \lim _ {k \to \infty} \sum_ {j \in E} p _ {i j} (n _ {k}) = 1.
$$

而由控制收敛定理, 我们有

$$
\lim _ {k \to \infty} p _ {i j} (n _ {k} + 1) = \lim _ {k \to \infty} \sum_ {l \in E} p _ {i l} p _ {l j} (n _ {k}) = \sum_ {l \in E} p _ {i l} \alpha_ {j} = \alpha_ {j}.
$$

再次应用法图定理得

$$
\alpha_ {j} = \lim _ {k \to \infty} p _ {i j} (n _ {k} + 1) = \lim _ {k \to \infty} \sum_ {l \in E} p _ {i l} (n _ {k}) p _ {l j} \geqslant \sum_ {l \in E} \alpha_ {l} p _ {l j}.
$$

上式中只能成立等号, 否则对 $j \in E$ 求和得出矛盾的结论 $\sum_{j \in E} \alpha_j > \sum_{l \in E} \alpha_l$. 这说明 $(\alpha_j : j \in E)$ 是 $P$ 的不变测度. 假若有某个 $j \in E$ 使 $\alpha_j > 0$, 则推出 $P$ 有平稳分布. 再由定理 5.2.2 知 $P$ 正常返, 这与假设矛盾. 因此对一切 $j \in E$ 有 $\alpha_j = 0$. $\square$

定理 5.4.4 设 P 是 E 上的非周期转移矩阵, 且此状态空间有分解

$$
E = U \cup H _ {1} ^ {0} \cup H _ {2} ^ {0} \cup \dots \cup H _ {k} ^ {0} \cup \dots \cup H _ {1} \cup H _ {2} \cup \dots ,
$$

其中 U 为非常返类,  $H_{k}^{0}$  为零常返类, 而  $H_{k}$  为正常返类 ( $k=1,2,\cdots$ ), 则有

$$
\lim _ {n \to \infty} P ^ {n} = L = (L _ {i j}),
$$

---

5.4 转移矩阵的收敛性

145

其中

$$
L _ {i j} = \left\{ \begin{array}{l l} \left(^ {k} \pi\right) _ {j}, & i, j \in H _ {k}, \\ f _ {i j} ^ {*} \left(^ {k} \pi\right) _ {j}, & i \in U, j \in H _ {k}, \\ 0, & \text {其他}, \end{array} \right.
$$

亦即

$$
\begin{array}{l} U H _ {1} ^ {0} H _ {2} ^ {0} \dots \quad H _ {1} \quad \quad H _ {2} \quad \dots \\ L = \begin{array}{c} U \\ H _ {1} ^ {0} \\ H _ {2} ^ {0} \\ \vdots \\ H _ {1} \\ H _ {2} \\ \vdots \end{array} \left( \begin{array}{c c c c c c c} 0 & 0 & 0 & \dots & (f _ {i j} ^ {*} (^ {1} \pi) _ {j}) & (f _ {i j} ^ {*} (^ {2} \pi) _ {j}) & \dots \\ 0 & 0 & 0 & \dots & 0 & 0 & \dots \\ 0 & 0 & 0 & \dots & 0 & 0 & \dots \\ \vdots & \vdots & \vdots & & \vdots & \vdots \\ 0 & 0 & 0 & \dots & 1 (^ {1} \pi) & 0 & \dots \\ 0 & 0 & 0 & \dots & 0 & 1 (^ {2} \pi) & \dots \\ \vdots & \vdots & \vdots & & \vdots & \vdots \end{array} \right). \\ \end{array}
$$

证明 当 $j \in H_k$ 时, 考虑 $P$ 在 $H_k$ 上的限制, 该限制为不可约、正常返、非周期的转移矩阵. 根据定理5.4.2有 $\lim_{n \to \infty} p_{jj}(n) = \pi_j$. 类似地, 当 $j \in H_k^0$ 时, 利用定理5.4.3得 $\lim_{n \to \infty} p_{jj}(n) = 0$. 当 $j \in U$ 时, 由 $\sum_{n=1}^{\infty} p_{jj}(n) < \infty$ 得 $\lim_{n \to \infty} p_{jj}(n) = 0$. 一般地, 对于 $i, j \in E$, 由(4.3.2)式有

$$
p _ {i j} (n) = \sum_ {k = 1} ^ {\infty} f _ {i j} (k) p _ {j j} (n - k) 1 _ {\{k \leqslant n \}}.
$$

对上式应用控制收敛定理就得定理的结论. $\square$

## \*5.4.3 周期矩阵的收敛性

定理 5.4.5 设 P 是 E 上的以  $d \geqslant 1$  为周期的、不可约、正常返转移矩阵. 令  $\pi$  是 P 的唯一平稳分布, 而  $E = C_{0} \cup C_{1} \cup \cdots \cup C_{d-1}$  是其周期环分解, 则对任意的  $i \in C_{0}$  和  $0 \leqslant k < d$  有

$$
\lim _ {n \to \infty} p _ {i j} (n d + k) = d \pi_ {j} 1 _ {C _ {k}} (j), \quad j \in E.
$$

证明 任意 $(p_{ij}(d):i,j\in C_k)$ 是 $C_k$ 上的不可约非周期转移矩阵. 根据定理5.4.2, 对任何 $j\in C_k$ 极限 $\lim_{n\to \infty}p_{jj}(nd)$ 存在. 再由 $P$ 的周期性, 应用定理5.2.2和推论5.2.7

---

146

第五章 马氏链的遍历理论

有

$$
\pi_ {j} = \lim _ {n \to \infty} \frac {1}{n d} \sum_ {k = 0} ^ {n d - 1} p _ {j j} (k) = \lim _ {n \to \infty} \frac {1}{n d} \sum_ {k = 0} ^ {n - 1} p _ {j j} (k d) = \frac {1}{d} \lim _ {n \to \infty} p _ {j j} (n d).
$$

现取 $i \in C_0$. 对于 $j \notin C_k$, 显然有 $p_{ij}(nd + k) = 0$. 对于 $j \in C_k$, 应用上式得

$$
\begin{array}{l} \lim _ {n \to \infty} p _ {i j} (n d + k) = \lim _ {n \to \infty} \sum_ {s = 0} ^ {n d + k} f _ {i j} (s) p _ {j j} (n d + k - s) \\ = \lim _ {n \to \infty} \sum_ {r = 0} ^ {n d} f _ {i j} (k + r) p _ {j j} (n d - r) \\ = \lim _ {n \to \infty} \sum_ {k = 0} ^ {n} f _ {i j} (t _ {i j} + k d) p _ {j j} (n d - k d) = f _ {i j} ^ {*} d \pi_ {j} = d \pi_ {i}, \\ \end{array}
$$

其中最后的等号成立还用到了 P 的常返性. □

例 5.4.1 令  $P=(p_{ij}:0\leqslant i,j\leqslant m)$  是例 5.1.2 中定义的埃伦菲斯特模型的转移矩阵. 分别用  $C_{0}$  和  $C_{1}$  表示  $[0,m]$  中的全体偶数和全体奇数构成的集合. 根据定理 5.4.5, 对  $i\in C_{0}$  和  $j\in E$  当  $n\to\infty$  时有

$$
p _ {i j} (2 n) \rightarrow 2 \pi_ {j} 1 _ {C _ {0}} (j), p _ {i j} (2 n + 1) \rightarrow 2 \pi_ {j} 1 _ {C _ {1}} (j).
$$

类似地, 对  $i \in C_{1}$  和  $j \in E$  当  $n \to \infty$  时有

$$
p _ {i j} (2 n) \rightarrow 2 \pi_ {j} 1 _ {C _ {1}} (j), p _ {i j} (2 n + 1) \rightarrow 2 \pi_ {j} 1 _ {C _ {0}} (j).
$$

所以  $\lim_{n\to\infty}p_{n}(i,\cdot)=\pi$  不成立.

## 练习题

1. 假定 $(X_{n}: n \geqslant 0)$ 和 $(Y_{n}: n \geqslant 0)$ 是可数状态空间 $E$ 上的具有转移矩阵 $P$ 的独立马氏链. 记 $\tau = \min \{n \geqslant 0 : X_{n} = Y_{n}\}$. 再令

$$
\xi_ {n} = \left\{ \begin{array}{l l} Y _ {n}, & n \leqslant \tau , \\ X _ {n}, & n > \tau . \end{array} \right.
$$

证明 $(\xi_{n}:n\geqslant 0)$ 和 $\{(X_n,\xi_n):n\geqslant 0\}$ 都是马氏链,并给出它们的转移矩阵.

2. 利用上题的结论给出命题 5.4.1 的证明.

3. 设 $X = (X_{n}: n \geqslant 0)$ 是例4.3.4中定义的离散区间 $[a, b] \subseteq \mathbb{Z}$ 上的吸收边界简单随机游动. 讨论 $X$ 的平稳分布和转移矩阵的极限行为.

---

5.4 转移矩阵的收敛性

147

4. 设 $X = (X_{n}: n \geqslant 0)$ 是例5.1.2中定义的埃伦菲斯特模型且有 $\mathbf{P}(X_0 \in C_0) = \mathbf{P}(X_0 \in C_1) = 1/2$.

(1) 证明对任何 $j \in E$ 有 $\lim_{n \to \infty} \mathbf{P}(X_n = j) = \pi_j$;
(2) 求极限期望 $\lim_{n\to \infty}\mathbf{E}X_n$ 和极限方差 $\lim_{n\to \infty}\mathbf{Var}X_n$ 并说明计算依据.

提示: 用 $\mu = (\mu_{i} : i \in E)$ 表示 $X$ 的初始分布, 则有

$$
\begin{array}{l} \lim _ {n \to \infty} \mathbf {P} (X _ {2 n} = j) = \lim _ {n \to \infty} \Big [ \sum_ {i \in C _ {0}} \mu_ {i} p _ {i j} (2 n) + \sum_ {i \in C _ {1}} \mu_ {i} p _ {i j} (2 n) \Big ] \\ = 2 \sum_ {i \in C _ {0}} \mu_ {i} 1 _ {C _ {0}} (j) \pi_ {j} + 2 \sum_ {i \in C _ {1}} \mu_ {i} 1 _ {C _ {1}} (j) \pi_ {j} = \pi_ {j}. \\ \end{array}
$$

类似地有 $\lim_{n\to \infty}\mathbf{P}(X_{2n + 1} = j) = \pi_j$ .注意 $\pi$ 是参数为1/2的二项分布.因此有 $\lim_{n\to \infty}\mathbf{E}X_n$ $= m / 2$ 和 $\lim_{n\to \infty}\mathbf{Var}X_n = m / 4.$
