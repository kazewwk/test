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

证明 记 $P^n = (p_{ij}(n))_{i,j \in E}$ 和 $L_n = (L_{ij}(n))_{i,j \in E}$. 对于 $i, j \in E$ 序列 $\{L_{ij}(n): n \geqslant 0\}$ 非负有界, 故存在非负整数列 $n_k(i, j) \to \infty$ 使极限 $\lim_{k \to \infty} L_{ij}(n_k(i, j)) = L_{ij}$ 存在. 利用对角线抽取法可得到不依赖于 $(i,j)$ 的子列 $n_k \to \infty$ 使

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