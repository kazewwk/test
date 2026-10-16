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

2. 固定 $c < b \in \mathbb{Z}_{+}$. 设 $W = (W_{n}: n \geqslant 0)$ 是 $\mathbb{Z}_{0,b}$ 上的从 $W_{0} = c \geqslant 0$ 出发的一维反射简单随机游动, 其转移矩阵 $P^{0,b}$ 由 (4.4.6) 式给出, 其中 $a = 0$ 而 $p, q > 0$ 满足 $p + q = 1$ (不要求 $q \leqslant p$). 取 $k \geqslant 1$ 并用 $\tau$ 表示 $(W_{n})$ 的第 $k$ 次下穿水平 0 的时刻. 对 $0 \leqslant a \leqslant b - 1$ 令 $X_{a}$ 为 $(W_{n \wedge \tau}: n \geqslant 0)$ 下穿水平 $a$ 的次数. 证明:

(1) $(X_{b}:c-1\leqslant a\leqslant b-1)$ 是分支过程, 其后代分布由 (6.3.1) 式给出;
(2) $\{X_b: 0 \leqslant b \leqslant c - 1\}$ 为带移民的分支过程, 其后代分布由 (6.3.1) 式给出, 而移民分布为集中于 1 的退化分布.

3. 设 $W = (W_{n}: n \geqslant 0)$ 是 $\mathbb{Z}$ 上的从 $W_{0} = 0$ 出发的一维简单随机游动, 其转移矩阵 $P$ 由 (4.4.3) 式给出, 其中 $0 < p < q < 1$. 令 $X_{a}$ 为 $W$ 下穿水平 $a \in \mathbb{Z}$ 的次数. 记 $r = p / q$. 证明:

(1) $\mathbf{P}(X_0 = i) = r^i (1 - r), i \geqslant 0;$
(2) 对 $a \geqslant 0$ 有 $\mathbf{P}(X_a = 0) = 1 - r^{a + 1}$, $\mathbf{P}(X_a = i) = r^{a + i}(1 - r)$, $i \geqslant 1$.

4. 在上题假设条件下, 证明对 $a \leqslant -1$ 下穿次数 $X_{a}$ 服从几何分布 $G(1 - r)$, 即有 $\mathbf{P}(X_{a} = i) = r^{i-1}(1 - r), i \geqslant 1$.

连续时间马氏链是指具有连续时间和可数状态的马氏过程, 其典型的例子包括泊松过程、连续时间随机游动等. 本章我们介绍连续时间马氏链的基本理论, 包括连续时间转移矩阵、马氏性与强马氏性、密度矩阵、向前和向后方程、最小链及其随机方程等.

## 7.1 连续时间转移矩阵

研究连续时间马氏链也需要使用转移矩阵的工具. 考虑到连续时间的结构, 这里实际上需要一族矩阵. 本节给出连续时间转移矩阵和马氏链的定义及若干基本性质. 特别地, 我们将证明右连续的马氏链一定具有强马氏性. 这里有些结论的证明与离散时间情况类似.

## 7.1.1 转移矩阵和马氏性

定义 7.1.1 我们称可数空间 E 上的矩阵族  $(P_{t})_{t\geqslant0}=\{(p_{t}(i,j):i,j\in E):t\geqslant0\}$  为转移矩阵或转移半群, 是指它有下面的性质:

(1) 对  $t \geqslant 0$  和  $i, j \in E$  有  $p_{t}(i, j) \geqslant 0;$
(2) 对 $t \geqslant 0$ 和 $i \in E$ 有 $\sum_{j \in E} p_t(i, j) \leqslant 1$;
(3) 对 $s, t \geqslant 0$ 和 $i, j \in E$ 有下面的查普曼-柯尔莫哥洛夫 (Chapman-Kolmogorov) 方程成立:

$$
p _ {s + t} (i, j) = \sum_ {k \in E} p _ {s} (i, k) p _ {t} (k, j); \tag {7.1.1}
$$

(4) 对 $i, j \in E$ 有 $\lim_{t \to 0+} p_t(i, j) = \delta_{ij}$.

查普曼-柯尔莫哥洛夫方程 (7.1.1) 也称为 $(P_t)_{t \geqslant 0}$ 的半群性质. 如果在性质 (2) 中对所有 $t \geqslant 0$ 和 $i \in E$ 等号成立, 则称转移矩阵 $(P_t)_{t \geqslant 0}$ 是马氏的. 有时为了对比, 在一般情况下也称 $(P_t)_{t \geqslant 0}$ 是准马氏的. 在很多文献中, 转移矩阵的定义只包含上面的性质 (1), (2) 和 (3), 而把满足性质 (4) 的转移矩阵称为标准的. 若 $E$ 上的概率分布 $\mu = (\mu(i): i \in E)$ 使得 $\mu P_t = \mu$ 对一切 $t \geqslant 0$ 成立, 则称其为 $(P_t)_{t \geqslant 0}$ 的平稳分布.

定义 7.1.2 令  $(P_{t})_{t\geqslant0}$  为 E 上的马氏转移矩阵. 设  $(\Omega,\mathcal{G},\mathbf{P})$  是概率空间, 且带有  $\sigma$  代数流  $(\mathcal{G}_{t}:t\geqslant0)$ , 再设  $X=(X_{t}:t\geqslant0)$  为 E 上的关于流  $(\mathcal{G}_{t}:t\geqslant0)$  适应的连续时间随机过程. 我们称 X 为关于流  $(\mathcal{G}_{t}:t\geqslant0)$  以  $(P_{t})_{t\geqslant0}$  为转移矩阵的马氏链, 是指对任意的  $s,t\geqslant0,G\in\mathcal{G}_{s}$  和  $i,j\in E$  有

$$
\mathbf {P} (X _ {s + t} = j | G \cap \{X _ {s} = i \}) = p _ {t} (i, j). \tag {7.1.2}
$$

上式表达的性质称为关于流 $(\mathcal{G}_{t}:t\geqslant0)$ 以 $(P_{t})_{t\geqslant0}$ 为转移矩阵的马氏性.

显然, 若马氏性 (7.1.2) 关于 $X$ 的任何适应流 $(\mathcal{G}_t)$ 成立, 则它关于 $X$ 的自然流也成立. 在定义 7.1.2 的情况下, 令 $\mu(i) = \mathbf{P}(X_0 = i)$, 称 $(\mu(i): i \in E)$ 为 $X$ 的初始分布. 特别地, 若 $\mathbf{P}(X_0 = i) = 1$, 则称 $X$ 是从 $i$ 出发的.

定理 7.1.1 过程 X 是相对其自然流  $(\mathcal{F}_{t})$  以  $(P_{t})$  为转移矩阵的马氏链当且仅当对任意的  $t \geqslant 0, 0 \leqslant s_{1} \leqslant s_{2} \leqslant \cdots \leqslant s_{n} = s$  和  $\{i_{1}, i_{2}, \cdots, i_{n} = i, j\} \subseteq E$  有

$$
\mathbf {P} (X _ {s + t} = j | X _ {s _ {1}} = i _ {1}, X _ {s _ {2}} = i _ {2}, \dots , X _ {s _ {n}} = i _ {n}) = p _ {t} (i, j). \tag {7.1.3}
$$

证明 若 X 是关于自然流  $(\mathcal{F})$  以  $(P_{t})_{t\geqslant0}$  为转移矩阵的马氏链, 则 (7.1.2) 式对任何  $G\in F_{s}$  成立, 故 (7.1.3) 式成立. 反之, 假设 (7.1.3) 式对任意的  $t\geqslant0,0\leqslant s_{1}\leqslant s_{2}\leqslant\cdots\leqslant s_{n}=s$  和  $\{i_{1},i_{2},\cdots,i_{n}=i,j\}\subseteq E$  成立, 下证 (7.1.2) 式对于自然流  $(\mathcal{F}_{t})$  成立. 为此只需证明对任意的  $s,t\geqslant0,G\in\mathcal{F}_{s}$  和  $i,j\in E$  有

$$
\mathbf {P} (\{X _ {s + t} = j \} \cap G \cap \{X _ {s} = i \}) = p _ {t} (i, j) \mathbf {P} (G \cap \{X _ {s} = i \}). \tag {7.1.4}
$$

令 $\mathcal{M}$ 为使 (7.1.4) 式成立的所有 $G \in \mathcal{F}_s$ 构成的事件类. 利用有界收敛定理易证 $\mathcal{M}$ 是一个单调类. 由 (7.1.3) 式易知对任意的 $t \geqslant 0, 0 \leqslant s_1 \leqslant s_2 \leqslant \dots \leqslant s_n \leqslant s$ 和 $\{i_1, i_2, \dots, i_n, i, j\} \subseteq E$ 有

$$
\begin{array}{l} \mathbf {P} (\{X _ {s + t} = j \} \cap \{X _ {s _ {1}} = i _ {1}, X _ {s _ {2}} = i _ {2}, \dots , X _ {s _ {n}} = i _ {n} \} \cap \{X _ {s _ {n}} = i \}) \\ = p _ {t} (i, j) \mathbf {P} (\{X _ {s _ {1}} = i _ {1}, X _ {s _ {2}} = i _ {2}, \dots , X _ {s _ {n}} = i _ {n} \} \cap \{X _ {s _ {n}} = i \}). \\ \end{array}
$$

令 A 为所有形如  $\{X_{s_{1}}=i_{1},X_{s_{2}}=i_{2},\cdots,X_{s_{n}}=i_{n}\}$  的事件的有限并构成的类. 则 A 是一个集代数且  $\sigma(\mathcal{A})=\mathcal{F}_{s}$ . 上式说明  $M\supseteq A$ . 根据单调类定理, 有  $\mathcal{M}\supseteq m(\mathcal{A})=\sigma(\mathcal{A})=\mathcal{F}_{s}$ , 即 (7.1.4) 式对一切  $G\in F_{s}$  成立. □

定理 7.1.2 过程 X 相对其自然流是以  $(P_{t})_{t\geqslant0}$  为转移矩阵以  $(\mu(i):i\in E)$  为初始分布的马氏链当且仅当对于任意的  $0=t_{0}\leqslant t_{1}\leqslant\cdots\leqslant t_{n}$  和  $\{i_{0},i_{1},\cdots,i_{n}\}\subseteq E$  有

$$
\mathbf {P} (X _ {t _ {k}} = i _ {k}: 0 \leqslant k \leqslant n) = \mu (i _ {0}) p _ {t _ {1} - t _ {0}} (i _ {0}, i _ {1}) \dots p _ {t _ {n} - t _ {n - 1}} (i _ {n - 1}, i _ {n}). \tag {7.1.5}
$$

证明 假设 X 是以  $(P_{t})_{t\geqslant0}$  为转移矩阵, 以  $(\mu(i):i\in E)$  为初始分布的马氏链. 由定理 7.1.1 知 (7.1.3) 式成立. 下面用数学归纳法证明 (7.1.5) 式成立. 显然该式对 n=0 成立. 假若它对于某个  $n\geqslant0$  成立. 根据 (7.1.3) 式并应用乘法公式, 对于任意的  $0=t_{0}\leqslant t_{1}\leqslant\cdots\leqslant t_{n}\leqslant t_{n+1}$  和  $\{i_{0},i_{1},\cdots,i_{n},i_{n+1}\}\subseteq E$  有

$$
\begin{array}{l} \mathbf {P} (X _ {t _ {0}} = i _ {0}, X _ {t _ {1}} = i _ {1}, \dots , X _ {t _ {n}} = i _ {n}, X _ {t _ {n + 1}} = i _ {n + 1}) \\ = \mathbf {P} (X _ {t _ {0}} = i _ {0}, X _ {t _ {1}} = i _ {1}, \dots , X _ {t _ {n}} = i _ {n}) \cdot \\ \end{array}
$$

$$
\begin{array}{l} \mathbf {P} (X _ {t _ {n + 1}} = i _ {n + 1} | X _ {t _ {0}} = i _ {0}, X _ {t _ {1}} = i _ {1}, \dots , X _ {t _ {n}} = i _ {n}) \\ = \mu (i _ {0}) p _ {t _ {1} - t _ {0}} (i _ {0}, i _ {1}) \dots p _ {t _ {n} - t _ {n - 1}} (i _ {n - 1}, i _ {n}) p _ {t _ {n + 1} - t _ {n}} (i _ {n}, i _ {n + 1}), \\ \end{array}
$$

即在 (7.1.5) 式中将 n 替换为  $n+1$  该式仍然成立. 这就证明了 (7.1.5) 式对所有  $n \geqslant 0$  成立. 反之, 假设 X 具有性质 (7.1.5). 显然  $X_{0}$  有分布  $(\mu(i): i \in E)$  且对于任意的  $t \geqslant 0, 0 \leqslant s_{1} \leqslant \cdots \leqslant s_{n} = s$  和  $\{i_{1}, i_{2}, \cdots, i_{n} = i, j\} \subseteq E$  有

$$
\begin{array}{l} \mathbf {P} (\{X _ {s _ {k}} = i _ {k}: 0 \leqslant k \leqslant n \} \cap \{X _ {s + t} = j \}) \\ = \mu (i _ {0}) p _ {s _ {1} - s _ {0}} (i _ {0}, i _ {1}) \dots p _ {s _ {n} - s _ {n - 1}} (i _ {n - 1}, i _ {n}) p _ {t} (i, j). \\ \end{array}
$$

将上式两端分别除以 (7.1.5) 式的两端即得 (7.1.3) 式. 再由定理 7.1.1 知 $X$ 是以 $P$ 为转移矩阵的马氏链. $\square$

例 7.1.1 设  $(X_{t}: t \geqslant 0)$  是关于流  $(\mathcal{G}_{t}: t \geqslant 0)$  以  $(P_{t})_{t \geqslant 0}$  为转移矩阵的马氏链。对于 h > 0 令  $P_{h} = (p_{h}(i, j): i, j \in E)$ 。则离散时间过程  $(X_{nh}: n \geqslant 0)$  关于流  $(\mathcal{G}_{nh}: n \geqslant 0)$  是以  $P_{h}$  为转移矩阵的离散时间马氏链。

例 7.1.2 设  $(N_{t})$  是参数为  $\alpha \geqslant 0$  的泊松过程且  $N_{0} \in Z_{+}$ . 令  $(\mathcal{F}_{t})$  为其自然流. 对于  $s, t \geqslant 0, G \in F_{s}$  和  $i, j \in Z_{+}$ , 利用  $N_{s+t} - N_{s}$  与  $G \cap \{N_{s} = i\}$  的独立性易知

$$
\mathbf {P} (N _ {s + t} = j | G \cap \{N _ {s} = i \}) = \mathbf {P} (N _ {s + t} - N _ {s} = j - i | G \cap \{N _ {s} = i \}) = p _ {t} (i, j),
$$

其中

$$
p _ {t} (i, j) = \left\{ \begin{array}{l l} \frac {(\alpha t) ^ {j - i}}{(j - i) !} \mathrm{e} ^ {- \alpha t}, & j - i \geqslant 0, \\ 0, & \text {其他}, \end{array} \right.
$$

所以 $(N_{t})$ 是以 $Z_{+}$ 为状态空间的连续时间马氏链,且其转移矩阵 $(P_{t})_{t\geqslant0}$ 由上式定义.

定理 7.1.3 设  $(\xi_{n}: n \geqslant 0)$  是以  $(\pi(i,j), i, j \in E)$  为转移矩阵的离散时间马氏链，而  $(N_{t}: t \geqslant 0)$  是与之独立，从原点出发且以  $\alpha \geqslant 0$  为参数的泊松过程。令  $X_{t} = \xi_{N_{t}}$ 。则连续时间过程  $(X_{t}: t \geqslant 0)$  是相对其自然流的马氏链，且其转移矩阵  $(p_{t}(i,j), i, j \in E, t \geqslant 0)$  由下式给出:

$$
p _ {t} (i, j) = \mathrm{e} ^ {- \alpha t} \sum_ {n = 0} ^ {\infty} \frac {(\alpha t) ^ {k}}{k !} \pi_ {k} (i, j), \tag {7.1.6}
$$

其中  $(\pi_{n}(i,j),i,j\in E)$  表示  $(\xi_{n}:n\geqslant0)$  的 n 步转移矩阵.

证明 不难验证 (7.1.6) 式确实定义了一个转移矩阵  $(p_{t}(i,j), i, j \in E, t \geqslant 0)$ . 利用定理 4.2.3 以及  $(\xi_{n}: n \geqslant 0)$  和  $(N_{t}: t \geqslant 0)$  的独立性, 对于  $0 = s_{0} \leqslant s_{1} \leqslant \cdots \leqslant s_{n}$  和  $\{i_{1}, i_{2}, \cdots, i_{n}\} \subseteq E$  有

$$
\mathbf {P} (X _ {s _ {1}} = i _ {1}, X _ {s _ {2}} = i _ {2}, \dots , X _ {s _ {n}} = i _ {n}) = \sum_ {k _ {1}, k _ {2}, \dots , k _ {n}} \prod_ {r = 1} ^ {n} \mathbf {P} (N _ {s _ {r}} - N _ {s _ {r - 1}} = k _ {r}) \pi_ {k _ {r}} (i _ {r - 1}, i _ {r}).
$$

进而, 对于  $t \geqslant 0, 0 = s_{0} \leqslant s_{1} \leqslant \cdots \leqslant s_{n} = s$  和  $\{i_{1}, i_{2}, \cdots, i_{n} = i, j\} \subseteq E$  有

$$
\begin{array}{l} \mathbf {P} (X _ {s _ {1}} = i _ {1}, X _ {s _ {2}} = i _ {2}, \dots , X _ {s _ {n}} = i _ {n}, X _ {s + t} = j) \\ = \sum_ {k _ {1}, k _ {2} \dots , k _ {n}} \prod_ {r = 1} ^ {n} \mathbf {P} (N _ {s _ {r}} - N _ {s _ {r - 1}} = k _ {r}) \pi_ {k _ {r}} (i _ {r - 1}, i _ {r}). \\ \sum_ {k} \mathbf {P} (N _ {s + t} - N _ {s} = k) \pi_ {k} (i, j) \\ = \mathbf {P} (X _ {s _ {1}} = i _ {1}, X _ {s _ {2}} = i _ {2}, \dots , X _ {s _ {n}} = i _ {n}) p _ {t} (i, j). \\ \end{array}
$$

再由定理 7.1.1 知  $(X_{t}: t \geqslant 0)$  是相对其自然流的马氏链，且其转移矩阵由 (7.1.6) 式给出.☐

## 7.1.2 右连续链的强马氏性

考虑可数状态空间 E, 并赋予其离散距离 r, 即对  $x, y \in E$  有  $r(x, y) = 1_{\{x \neq y\}}$ .

定理 7.1.4 设  $(X_{t})$  是 E 上的关于流  $(\mathcal{G}_{t})$  以  $(P_{t})$  为转移矩阵的右连续马氏链，而  $\tau$  为  $(\mathcal{G}_{t+})$  的停时，则对于任意的  $t \geqslant 0, i, j \in E$  和  $G \in G_{\tau+}$  有

$$
\mathbf {P} (X _ {\tau + t} = j | G \cap \{X _ {\tau} = i, \tau <   \infty \}) = p _ {t} (i, j). \tag {7.1.7}
$$

证明 令 $\tau_{n}$ 是 $\tau$ 的由 (2.1.12) 式定义的二分点离散化. 根据命题 2.1.18 有 $G \in \mathcal{G}_{\tau_n}$, 故 $G \cap \{\tau_n = k / 2^n\} \in \mathcal{G}_{k / 2^n}$. 应用马氏性 (7.1.2) 得

$$
\mathbf {P} (X _ {\tau_ {n} + t} = j | G \cap \{\tau_ {n} = k / 2 ^ {n}, X _ {\tau_ {n}} = i \}) = p _ {t} (i, j),
$$

或写为

$$
\mathbf {P} (G \cap \{\tau_ {n} = k / 2 ^ {n}, X _ {\tau_ {n}} = i, X _ {\tau_ {n} + t} = j \}) = \mathbf {P} (G \cap \{\tau_ {n} = k / 2 ^ {n}, X _ {\tau_ {n}} = i \}) p _ {t} (i, j).
$$

对 $k \geqslant 0$ 求和得

$$
\mathbf {P} (G \cap \{\tau_ {n} <   \infty , X _ {\tau_ {n}} = i, X _ {\tau_ {n} + t} = j \}) = \mathbf {P} (G \cap \{\tau_ {n} <   \infty , X _ {\tau_ {n}} = i \}) p _ {t} (i, j).
$$

再注意到 $\{\tau < \infty\} = \{\tau_n < \infty\}$ 有

$$
\mathbf {P} (G \cap \{\tau <   \infty , X _ {\tau_ {n}} = i, X _ {\tau_ {n} + t} = j \}) = \mathbf {P} (G \cap \{\tau <   \infty , X _ {\tau_ {n}} = i \}) p _ {t} (i, j).
$$

由 $X$ 的右连续性, 当 $n \to \infty$ 时有 $1_{\{X_{\tau_n} = i\}} \to 1_{\{X_{\tau} = i\}}$ 和 $1_{\{X_{\tau_n + t} = j\}} \to 1_{\{X_{\tau + t} = j\}}$. 对上式应用控制收敛定理得

$$
\mathbf {P} (G \cap \{\tau <   \infty , X _ {\tau} = i, X _ {\tau + t} = j \}) = \mathbf {P} (G \cap \{\tau <   \infty , X _ {\tau} = i \}) p _ {t} (i, j)
$$

所以 (7.1.7) 式成立. □

等式 (7.1.7) 所表达的性质称为 $(X_{t})$ 关于流 $(\mathcal{G}_{t+})$ 以 $(P_{t})_{t\geqslant 0}$ 为转移矩阵的强马氏性. 特别地, 它说明 $(X_{t})$ 是关于流 $(\mathcal{G}_{t+})$ 以 $(P_{t})_{t\geqslant 0}$ 为转移矩阵的马氏链. 所以在谈到右连续马氏链的时候, 总可以假定相应的流是右连续的. 基于定理 7.1.4, 与离散时间情况类似, 可以证明如下的:

定理 7.1.5 设  $(X_{t}:t\geqslant0)$  是关于流  $(\mathcal{G}_{t}:t\geqslant0)$  以  $(P_{t})_{t\geqslant0}$  为转移矩阵的右连续马氏链. 再设  $\tau$  为  $(\mathcal{G}_{t+})$  的停时, 而事件  $A\in\mathcal{G}_{\tau}$  满足  $\mathbf{P}(A\cap\{\tau<\infty\})>0$ , 则在条件概率  $\mathbf{P}_{A}:=\mathbf{P}(\cdot|A\cap\{\tau<\infty\})$  之下  $(X_{\tau+t}:t\geqslant0)$  具有关于流  $(\mathcal{G}_{\tau+t+}:t\geqslant0)$  以  $(P_{t})_{t\geqslant0}$  为转移矩阵的强马氏性.

定理 7.1.6 设 X 为关于流  $(\mathcal{G}_{t})$  以  $(P_{t})_{t\geqslant0}$  为转移矩阵的右连续马氏链，而  $\tau$  是  $(\mathcal{G}_{t})$  的停时。记  $\mathcal{F}^{\tau}=\sigma(X_{\tau+t}:t\geqslant0)$ ，则对于任意的  $i\in E,G\in\mathcal{G}_{\tau}$  和  $F\in\mathcal{F}^{\tau}$  有

$$
\mathbf {P} (F | G \cap \{\tau <   \infty , X _ {\tau} = i \}) = \mathbf {P} (F | \tau <   \infty , X _ {\tau} = i). \tag {7.1.8}
$$

推论 7.1.7 设 X 为关于流  $(\mathcal{G}_{t})$  以  $(P_{t})_{t\geqslant0}$  为转移矩阵的右连续马氏链, 而  $\tau$  是  $(\mathcal{G}_{t})$  的停时, 则对于任意的  $i\in E$ , 在条件概率  $\mathbf{P}(\cdot|\tau<\infty,X_{\tau}=i)$  之下  $(X_{t\wedge\tau}:t\geqslant0)$  和  $(X_{\tau+t}:t\geqslant0)$  是独立的.

考虑可数状态空间 $E$ 上的准马氏转移矩阵 $(P_{t})_{t\geqslant 0} = \{(p_{t}(i,j):i,j\in E):t\geqslant 0\}$. 令 $\tilde{E} = E\cup \{\partial \}$, 其中 $\partial \notin E$ 为抽象点. 对于 $t\geqslant 0$ 我们令

$$
\tilde {p} _ {t} (i, j) = \left\{ \begin{array}{l l} p _ {t} (i, j), & i, j \in E, \\ 1 - p _ {t} (i, E), & i \in E, j = \partial , \\ \delta_ {\partial j}, & i = \partial , j \in \tilde {E}, \end{array} \right. \tag {7.1.9}
$$

其中 $p_t(i,E) = \sum_{i\in E}p_t(i,j)\leqslant 1$ .则 $(\tilde{P}_t)_{t\geqslant 0} = \{(\tilde{p}_t(i,j):i,j\in \tilde{E}):t\geqslant 0\}$ 是 $\tilde{E}$ 上的马氏转移矩阵.对于任何取值于 $\tilde{E}$ 且以 $(\tilde{P}_t)_{t\geqslant 0}$ 为转移矩阵的右连续马氏链 $X = (X_{t}:t\geqslant 0)$ ，令 $\zeta = \inf \{t\geqslant 0:X_t = \partial \}$ .利用强马氏性可以看到， $X$ 到达状态 $\partial$ 后不再运动.我们也称 $X$ 为 $E$ 上以 $(P_t)_{t\geqslant 0}$ 为转移矩阵的马氏链或准马氏链，而称 $\zeta$ 为其生命时.

## 7.1.3 转移矩阵的连续性

命题 7.1.8 设  $(P_{t})_{t\geqslant0}=\{(p_{t}(i,j):i,j\in E):t\geqslant0\}$  为可数状态空间 E 上的准马氏转移矩阵, 则有

(1) $\sum_{j\in E}p_{t}(i,j)$ 是 $t\geqslant0$ 的减函数;
(2) 对任何  $t \geqslant 0$  及  $i \in E$  有  $p_{t}(i, i) > 0;$
(3) 若对某个 s > 0 有  $p_{s}(i, i) = 1$ ，则对一切  $t \geqslant 0$  有  $p_{t}(i, i) = 1$ ;
(4) 若对某个 $s > 0$ 有 $p_s(i,j) > 0$, 则对一切 $t \geqslant s$ 有 $p_t(i,j) > 0$.

证明 (1) 根据定义 7.1.1 中的假定, 对 $t \geqslant s \geqslant 0$ 有

$$
\sum_ {j \in E} p _ {t} (i, j) = \sum_ {k \in E} \sum_ {j \in E} p _ {s} (i, k) p _ {t - s} (k, j) \leqslant \sum_ {k \in E} p _ {s} (i, k).
$$

(2) 根据定义 7.1.1, 可取 $\delta > 0$ 使当 $0 \leqslant t \leqslant \delta$ 时有 $p_t(i, i) > 0$. 对于 $t \geqslant 0$ 取正整数 $n \geqslant 0$ 使 $t = n\delta + s$, 其中 $0 \leqslant s < \delta$. 由 (7.1.1) 式易知

$$
p _ {t} (i, i) \geqslant p _ {\delta} (i, i) ^ {n} p _ {s} (i, i) > 0.
$$

(3) 对任何整数 $n \geqslant 1$ 有 $p_{ns}(i, i) \geqslant p_s(i, i)^n$. 故在假设条件下 $p_{ns}(i, i) = 1$. 再由 (1) 的结论易知, 对一切 $t \geqslant 0$ 有 $\sum_{j \in E} p_t(i, j) = 1$. 假若对某个 $t \geqslant 0$ 有 $p_t(i, i) < 1$, 则存在 $j \neq i$ 使 $p_t(i, j) > 0$. 取 $n \geqslant 1$ 满足 $ns \geqslant t$. 利用 (2) 的结论有

$$
p _ {n s} (i, j) \geqslant p _ {t} (i, j) p _ {n s - t} (j, j) > 0.
$$

这导致与上面矛盾的结论 $p_{ns}(i,i) < 1$.

(4) 只需注意 $p_t(i,j) \geqslant p_s(i,j)p_{t-s}(j,j)$，并应用 (2) 的结论。□

定理 7.1.9 设  $(P_{t})_{t\geqslant0}=\{(p_{t}(i,j):i,j\in E):t\geqslant0\}$  为可数状态空间 E 上的准马氏转移矩阵, 则  $p_{t}(i,j)$  关于  $t\geqslant0$  一致连续且有

$$
| p _ {t} (i, j) - p _ {s} (i, j) | \leqslant 1 - p _ {t - s} (i, i), \quad t \geqslant s \geqslant 0, i, j \in E.
$$

证明 根据半群性质 (7.1.1) 有

$$
\begin{array}{l} p _ {t} (i, j) - p _ {s} (i, j) = \sum_ {k} p _ {t - s} (i, k) p _ {s} (k, j) - p _ {s} (i, j) \\ = \sum_ {k \neq i} p _ {t - s} (i, k) p _ {s} (k, j) - [ 1 - p _ {t - s} (i, i) ] p _ {s} (i, j). \\ \end{array}
$$

注意上式右端为两个正数之差, 且有

$$
\sum_ {k \neq i} p _ {t - s} (i, k) p _ {s} (k, j) \leqslant \sum_ {k \neq i} p _ {t - s} (i, k) \leqslant 1 - p _ {t - s} (i, i)
$$

和

$$
[ 1 - p _ {t - s} (i, i) ] p _ {s} (i, j) \leqslant 1 - p _ {t - s} (i, i).
$$

所以欲证估计成立. □

## 练习题

1. 设 $(P_t)_{t \geqslant 0}$ 为连续时间转移矩阵. 证明极限 $\lim_{t \to \infty} p_t(i, j)$ 存在当且仅当对于一切 $h > 0$, 极限 $\lim_{n \to \infty} p_{nh}(i, j)$ 存在.

提示: 应用定理 7.1.9 的结论.

2. 设 $(P_t)_{t \geqslant 0}$ 为连续时间马氏转移矩阵. 对 $h > 0$ 令 $P_h = (p_h(i, j): i, j \in E)$. 证明 $i \in E$ 关于转移矩阵 $P_h$ 是常返态当且仅当 $\int_0^\infty p_t(i, i) \mathrm{d}t = \infty$.

提示: 根据命题 7.1.8 有  $\delta(h):=\min_{0\leqslant t\leqslant h}p_{t}(i,i)>0$ . 注意

$$
\begin{array}{l} p _ {(n - 1) h} (i, i) \delta (h) \leqslant \inf _ {(n - 1) h \leqslant t \leqslant n h} p _ {t} (i, i) \\ \leqslant \sup _ {(n - 1) h \leqslant t \leqslant n h} p _ {t} (i, i) \leqslant p _ {n h} (i, i) \delta (h) ^ {- 1}. \\ \end{array}
$$

3. 设 $(S_{n}: n \geqslant 0)$ 是离散时间对称简单随机游动, 而 $(N_{t}: t \geqslant 0)$ 与之独立, 从原点出发且以 $\alpha \geqslant 0$ 为参数的泊松过程. 令 $X_{t} = S_{N_{t}}$, 则 $(X_{t}: t \geqslant 0)$ 为连续时间马氏链, 称为连续时间对称简单随机游动, 并称 $\alpha$ 为其跳跃速率. 证明: 若 $(X_{t}: t \geqslant 0)$ 和 $(Y_{t}: t \geqslant 0)$ 分别是速度为 $\alpha \geqslant 0$ 和 $\beta \geqslant 0$ 的连续时间对称简单随机游动, 且二者独立, 则 $(X_{t} + Y_{t}: t \geqslant 0)$ 也是连续时间对称简单随机游动, 并求出其速度.

4. 令 $(X_{t}: t \geqslant 0)$ 是速度为 $\alpha > 0$ 的连续时间一维对称简单随机游动. 证明在依分布收敛的意义下有

$$
\lim _ {t \to \infty} \frac {X _ {t}}{\sqrt {\alpha t}} = \lim _ {t \to \infty} \frac {X _ {t}}{\sqrt {N _ {t}}} = \xi ,
$$

其中  $\xi$  是标准正态分布随机变量.

5. 设 $(X_{t}: t \geqslant 0)$ 是速度为 $\alpha > 0$ 的连续时间 $d$ 维对称简单随机游动. 基于例4.3.1的结论, 证明对于任何非空有界集 $B \subseteq \mathbb{Z}^{d}$, 几乎必然有

$$
\int_ {0} ^ {\infty} 1 _ {B} (X _ {s}) \mathrm{d} s \left\{ \begin{array}{l l} = \infty , & d = 1, 2, \\ <   \infty , & d \geqslant 3. \end{array} \right.
$$

提示: 应用推论 4.3.2 的结论, 并注意泊松过程  $(N_{t}: t \geqslant 0)$  在各个状态停留的时间独立且均服从以  $\alpha > 0$  为参数的指数分布.

## 7.2 密度矩阵

马氏链的密度矩阵就是转移矩阵在时间零点的导数, 因此是连续时间情形所独有的. 密度矩阵的元素具有明确的概率含义. 在适当条件下, 密度矩阵唯一决定相应的转移矩阵. 这些特性使密度矩阵成为研究连续时间马氏链的重要工具. 为了表述上的方便, 本节及以后我们经常会记 $p_t(i,j)$ 为 $p_{ij}(t)$.

## 7.2.1 转移矩阵的可微性

定理 7.2.1 (柯尔莫哥洛夫) 设  $(P(t))_{t \geqslant 0} = \{(p_{ij}(t): i, j \in E): t \geqslant 0\}$  为 E 上的准马氏转移矩阵, 则有:

(1) 对任何 $i \in E$ 存在极限

$$
\lim _ {t \to 0 +} \frac {1}{t} (1 - p _ {i i} (t)) = q _ {i} := \sup _ {t > 0} \frac {1}{t} (1 - p _ {i i} (t)) \in [ 0, \infty ]. \tag {7.2.1}
$$

(2) 对任何 $i \neq j \in E$ 存在极限

$$
\lim _ {t \to 0 +} \frac {1}{t} p _ {i j} (t) = q _ {i j} \in [ 0, \infty). \tag {7.2.2}
$$

(3) 对任何 $i \in E$ 有

$$
\sum_ {j \neq i} q _ {i j} \leqslant q _ {i}. \tag {7.2.3}
$$

证明 (1) 根据命题 7.1.8, 对 $t \geqslant 0$ 有 $p_{ii}(t) > 0$, 故可定义 $\phi_i(t) = -\ln p_{ii}(t)$. 注意

$$
1 - p _ {i i} (t) = 1 - \mathrm{e} ^ {- \phi_ {i} (t)} \leqslant \phi_ {i} (t). \tag {7.2.4}
$$

对任何 $s, t > 0$, 由 $p_{ii}(s + t) \geqslant p_{ii}(s)p_{ii}(t)$ 有

$$
\phi_ {i} (s + t) \leqslant \phi_ {i} (s) + \phi_ {i} (t). \tag {7.2.5}
$$

取整数 $n \geqslant 0$ 与 $0 \leqslant \delta < s$ 使 $t = ns + \delta$. 由 (7.2.5) 式得

$$
\frac {\phi_ {i} (t)}{t} \leqslant \frac {n \phi_ {i} (s) + \phi_ {i} (\delta)}{t} = \frac {n s \phi_ {i} (s)}{s t} + \frac {\phi_ {i} (\delta)}{t}.
$$

显然, 当  $s \rightarrow 0+$  时有  $ns/t \rightarrow 1$  和  $\delta \rightarrow 0$ , 故  $\phi_{i}(\delta) \rightarrow 0$ . 由上式得

$$
\frac {\phi_ {i} (t)}{t} \leqslant \operatorname * {l i m i n f} _ {s \to 0 +} \frac {\phi_ {i} (s)}{s},
$$

进而

$$
\operatorname * {l i m s u p} _ {s \to 0 +} \frac {\phi_ {i} (s)}{s} \leqslant \sup _ {t > 0} \frac {\phi_ {i} (t)}{t} \leqslant \operatorname * {l i m i n f} _ {s \to 0 +} \frac {\phi_ {i} (s)}{s}.
$$

由此得

$$
\lim _ {t \to 0 +} \frac {\phi_ {i} (t)}{t} = q _ {i} := \sup _ {t > 0} \frac {\phi_ {i} (t)}{t}. \tag {7.2.6}
$$

再注意到 (7.2.4) 式即得

$$
\lim _ {t \to 0 +} \frac {1}{t} (1 - p _ {i i} (t)) = q _ {i} = \sup _ {t > 0} \frac {1}{t} (1 - p _ {i i} (t)). \tag {7.2.7}
$$

(2) 设 $i \neq j \in E$. 由定理 7.1.9 知函数 $t \mapsto p_{ij}(t)$ 在 $[0, \infty)$ 上一致连续. 因此, 对任给的 $\varepsilon > 0$, 存在 $t_0 > 0$ 使得当 $t \in (0, t_0)$ 时有

$$
p _ {j i} (t) <   \varepsilon , \quad p _ {i i} (t) > 1 - \varepsilon , \quad p _ {j j} (t) > 1 - \varepsilon .
$$

设 $(X_{t}:t\geqslant 0)$ 是以 $(P(t))_{t\geqslant 0}$ 为转移矩阵的马氏链.对 $h > 0$ 令

$$
_ {k} p _ {i j} ^ {(r)} (h) = \mathbf {P} _ {i} (X _ {r h} = j; X _ {s h} \neq k, 0 \leqslant s \leqslant r - 1).
$$

于是由

$$
p _ {i i} (r h) = _ {j} p _ {i i} ^ {(r)} (h) + \sum_ {m = 1} ^ {r - 1} _ {j} p _ {i j} ^ {(m)} (h) p _ {j i} ((r - m) h)
$$

易知当  $rh \leqslant nh < t_{0}$  时,

$$
\begin{array}{l} { } _ { j } p _ { i i } ^ { ( r ) } ( h ) \geqslant p _ { i i } ( r h ) - \max _ { 1 \leqslant k \leqslant r } p _ { j i } ( k h ) \sum _ { m = 1 } ^ { r - 1 } { } _ { j } p _ { i j } ^ { ( m ) } \\ \geqslant p _ {i i} (r h) - \max _ {1 \leqslant k \leqslant r} p _ {j i} (k h) > 1 - 2 \varepsilon , \\ \end{array}
$$

进而有

$$
\begin{array}{l} p _ {i j} (n h) = \sum_ {r = 1} ^ {n} _ {j} p _ {i j} ^ {(r)} (h) p _ {j j} ((n - r) h) \\ \geqslant \sum_ {r = 1} ^ {n} _ {j} p _ {i i} ^ {(r - 1)} (h) p _ {i j} (h) p _ {j j} ((n - r) h) \\ \geqslant (1 - 2 \varepsilon) \sum_ {r = 1} ^ {n} p _ {i j} (h) (1 - \varepsilon) \geqslant n (1 - 3 \varepsilon) p _ {i j} (h). \\ \end{array}
$$

所以当 $0 < nh < t_0$ 时有

$$
\frac {p _ {i j} (n h)}{n h} \geqslant (1 - 3 \varepsilon) \frac {p _ {i j} (h)}{h}. \tag {7.2.8}
$$

在上式中置 $h = t_0 / 2n$ 得到

$$
q _ {i j} := \operatorname * {l i m i n f} _ {t \to 0 +} \frac {p _ {i j} (t)}{t} \leqslant \operatorname * {l i m i n f} _ {n \to \infty} \frac {p _ {i j} (t _ {0} / 2 n)}{t _ {0} / 2 n} \leqslant \frac {1}{1 - 3 \varepsilon} \frac {p _ {i j} (t _ {0} / 2)}{t _ {0} / 2} <   \infty .
$$

另一方面, 由上面 $q_{ij}$ 的定义, 存在 $t_1 \in (0, t_0/2)$ 使 $p_{ij}(t_1)/t_1 < q_{ij} + \varepsilon$. 再由 $p_{ij}(t)/t$ 的右连续性, 可找到 $h_0 \in (0, t_0/2)$, 使当 $t_1 \leqslant t < t_1 + h_0$ 时有

$$
\frac {p _ {i j} (t)}{t} <   q _ {i j} + 2 \varepsilon . \tag {7.2.9}
$$

而对 $0 < h < h_0 \wedge t_1$, 存在整数 $n \geqslant 0$ 使 $t_1 \leqslant nh < t_1 + h_0 \leqslant t_0$. 于是由 (7.2.8) 式和 (7.2.9) 式得

$$
\frac {p _ {i j} (h)}{h} \leqslant \frac {1}{1 - 3 \varepsilon} \frac {p _ {i j} (n h)}{n h} <   \frac {q _ {i j} + 2 \varepsilon}{1 - 3 \varepsilon}.
$$

再由 $\varepsilon > 0$ 的任意性可知 $\limsup_{h\to 0 + }(p_{ij}(h) / h)\leqslant q_{ij}$. 综上即得 (7.2.2) 式.

(3) 由转移矩阵的定义, 对 t > 0 和  $i \in E$  有

$$
\frac {1}{t} \sum_ {j \neq i} p _ {i j} (t) \leqslant \frac {1}{t} (1 - p _ {i i} (t)).
$$

令 $t \to 0+$ 并利用法图定理即得 (7.2.3) 式. □

定义 7.2.1 称状态空间 E 上的方形矩阵  $Q = (q_{ij} : i, j \in E)$  为一个密度矩阵, 或者 Q 矩阵, 是指它满足条件

(1) 对任何 $i \in E$ 有 $q_{i} := -q_{ii} \in [0, \infty]$;
(2) 对任何 $i \neq j \in E$ 有 $0 \leqslant q_{ij} < \infty$;
(3) 对任何 $i \in E$ 有 $\sum_{j \neq i} q_{ij} \leqslant q_i$.

如果 $q_{i} < \infty$, 那么我们称状态 $i \in E$ 是稳定的. 所有状态都稳定的密度矩阵称为全稳定的. 如果对任何 $i \in E$ 都有

$$
\sum_ {j \neq i} q _ {i j} = q _ {i} <   \infty ,
$$

则称密度矩阵 Q 是保守的.

根据定理 7.2.1, 状态空间 E 上连续时间转移矩阵的  $(P(t))_{t \geqslant 0} = \{(p_{ij}(t) : i, j \in E) : t \geqslant 0\}$  的导数矩阵  $Q := (p'_{ij}(0) : i, j \in E)$  是就一个密度矩阵, 称为  $(P(t))_{t \geqslant 0}$  的密度矩阵. 在这种情况下, 若 X 是以  $(P(t))_{t \geqslant 0}$  为转移矩阵的马氏链, 我们也称 Q 为 X 的密度矩阵, 或称 X 为 Q 过程.

如无特别申明, 后面只考虑全稳定的密度矩阵.

## 7.2.2 轨道的跳跃性质

定理 7.2.2 设状态空间 E 上的右连续马氏链  $X = (X_{t} : t \geqslant 0)$  具有保守的密度矩阵  $Q = (q_{ij} : i, j \in E)$ . 对  $i \in E$  记  $\mathbf{P}_{i} = \mathbf{P}_{i} (\cdot | X_{0} = i)$ . 定义 X 的首跳时间

$$
\tau = \inf \{t > 0: X _ {t} \neq X _ {0} \}. \tag {7.2.10}
$$

则  $\tau$  是停时, 且如下性质成立:

(1) 对任何 $t \geqslant 0$ 有 $\mathbf{P}_i(\tau \leqslant t) = 1 - \mathrm{e}^{-q_i t}$, 即在 $\mathbf{P}_i$ 下 $\tau$ 服从参数为 $q_i$ 的指数分布;
(2) 当 $q_{i} \neq 0$ 时, 对 $i \neq j \in E$ 和 $t \geqslant 0$ 有 $\mathbf{P}_{i}(\tau \leqslant t, X_{\tau} = j) = (1 - \mathrm{e}^{-t q_{i}}) q_{i}^{-1} q_{ij}$;
(3) 当 $q_{i} \neq 0$ 时, 对 $i \neq j \in E$ 有 $\mathbf{P}_{i}(X_{\tau} = j) = q_{i}^{-1}q_{ij}$.

此外, 当  $q_{i} \neq 0$  时, 随机变量  $\tau$  与  $X_{\tau}$  在  $P_{i}$  之下独立.

证明 (1) 记 $X$ 的自然流为 $(\mathcal{F}_t: t \geqslant 0)$. 因为 $\{\tau > t\} = \{X_r = X_0; r \in [0, t)$ 为有理数 $\} \cap \{X_t = X_0\} \in \mathcal{F}_t$, 所以 $\tau$ 是停时. 注意, 由定理7.2.1(1)有

$$
\begin{array}{l} \lim _ {s \to 0 +} p _ {i i} (s t) ^ {1 / s} = \lim _ {s \to 0 +} \exp \left\{\frac {t \ln p _ {i i} (s t)}{s t} \right\} \\ = \lim _ {s \to 0 +} \exp \left\{\frac {- t [ 1 - p _ {i i} (s t) ]}{s t} \right\} = \mathrm{e} ^ {- q _ {i} t}. \tag {7.2.11} \\ \end{array}
$$

因此, 利用 X 的右连续性和马氏性 (7.1.5) 得

$$
\begin{array}{l} \mathbf {P} _ {i} (\tau > t) = \mathbf {P} _ {i} \big (X _ {k t / 2 ^ {n}} = i: n \geqslant 1, k = 0, 1, \dots , 2 ^ {n} \big) \\ = \lim _ {n \to \infty} \mathbf {P} _ {i} \big (X _ {k t / 2 ^ {n}} = i: k = 0, 1, \dots , 2 ^ {n} \big) \\ = \lim _ {n \to \infty} p _ {i i} (t / 2 ^ {n}) ^ {2 ^ {n}} = \mathrm{e} ^ {- q _ {i} t}. \\ \end{array}
$$

(2) 令 $\tau_{n} = \inf \{k / 2^{n} > 0 : X_{k / 2^{n}} \neq i\}$. 显然 $\{\tau_{n}\}$ 为递降的停时列, 并且 $\tau_{n} \geqslant \tau$, 故 $\tilde{\tau} := \lim_{n \to \infty} \tau_{n} \geqslant \tau$. 显然, 对任何 $k / 2^{n} < \tilde{\tau}$ 有 $X_{k / 2^{n}} = i$. 由轨道右连续性, 对任何 $t \in [0, \tilde{\tau})$ 有 $X_{t} = i$. 这意味着 $\tau \geqslant \tilde{\tau}$, 故得 $\tau = \lim_{n \to \infty} \tau_{n}$. 因为 $\mathbf{P}_{i}(\tau = t) = 0$, 利用控制收敛定理得

$$
\begin{array}{l} \mathbf {P} _ {i} (\tau \leqslant t, X _ {\tau} = j) = \mathbf {P} _ {i} (1 _ {\{\tau <   t \}} 1 _ {\{X _ {\tau} = j \}}) = \lim _ {n \to \infty} \mathbf {P} _ {i} (1 _ {\{\tau_ {n} <   t \}} 1 _ {\{X _ {\tau_ {n}} = j \}}) \\ \leqslant \lim _ {n \to \infty} \mathbf {P} _ {i} (\tau_ {n} \leqslant t, X _ {\tau_ {n}} = j) \leqslant \lim _ {n \to \infty} \mathbf {P} _ {i} (\tau \leqslant t, X _ {\tau_ {n}} = j) \\ = \mathbf {P} _ {i} (\tau \leqslant t, X _ {\tau} = j). \\ \end{array}
$$

利用定理 7.2.1 和 (7.2.11) 式有

$$
\begin{array}{l} \mathbf {P} _ {i} (\tau \leqslant t, X _ {\tau} = j) = \lim _ {n \to \infty} \mathbf {P} _ {i} (\tau_ {n} \leqslant t, X _ {\tau_ {n}} = j) \\ = \lim _ {n \to \infty} \sum_ {k / 2 ^ {n} \leqslant t} \mathbf {P} _ {i} (\tau_ {n} = k / 2 ^ {n}, X _ {k / 2 ^ {n}} = j) \\ \end{array}
$$

$$
\begin{array}{l} = \lim _ {n \to \infty} \sum_ {k \leqslant 2 ^ {n} t} \mathbf {P} _ {i} (X _ {r / 2 ^ {n}} = i, X _ {k / 2 ^ {n}} = j: r \leqslant k - 1) \\ = \lim _ {n \to \infty} \sum_ {k = 1} ^ {\lfloor 2 ^ {n} t \rfloor} p _ {i i} (1 / 2 ^ {n}) ^ {k - 1} p _ {i j} (1 / 2 ^ {n}) \\ = \lim _ {n \to \infty} \frac {\left[ 1 - p _ {i i} (1 / 2 ^ {n}) ^ {\lfloor 2 ^ {n} t \rfloor} \right] p _ {i j} (1 / 2 ^ {n})}{1 - p _ {i i} (1 / 2 ^ {n})} \\ = (1 - \mathrm{e} ^ {- q _ {i} t}) q _ {i} ^ {- 1} q _ {i j}. \\ \end{array}
$$

(3) 在上面所证的结果中令 $t \to \infty$ 立得. $\square$

设右连续马氏链 $X$ 有保守的密度矩阵 $Q$. 根据定理7.2.2, 当 $q_{i} < \infty$ 时, 该马氏链在状态 $i \in E$ 停留的时间服从以 $q_{i}$ 为参数的指数分布, 此时 $i$ 称为逗留态; 当 $q_{i} = 0$ 时有

$$
\mathbf {P} _ {i} (\text {对一切} t \geqslant 0 \text {有} X _ {t} = i) = 1,
$$

此时 i 称为吸收态.

令 $S_0 = 0$ 并对于 $n \geqslant 1$ 归纳地定义停时 $S_n = \inf \{t > S_{n-1}: X_t \neq X_{S_{n-1}}\}$. 显然, 对于 $n \geqslant 1$, 当 $S_n < \infty$ 时, 该停时就是 $(X_t)$ 的第 $n$ 个跳跃时.

定理 7.2.3 设右连续马氏链  $X = (X_{t} : t \geqslant 0)$  有保守的密度矩阵 Q. 令

$$
\begin{array}{l} g _ {i j} ^ {(n)} (t) = \mathbf {P} _ {i} (X \text {在} [ 0, t ] \text {中跳} n \text {次且} X _ {t} = j) \\ = \mathbf {P} _ {i} (S _ {n} \leqslant t <   S _ {n + 1}, X _ {t} = j), \tag {7.2.12} \\ \end{array}
$$

则函数 $t \mapsto g_{ij}^{(n)}(t)$ 连续可导且有 $g_{ij}^{(0)}(t) = \delta_{ij}\mathrm{e}^{-q_it}$ 和

$$
g _ {i j} ^ {(n)} (t) = \sum_ {k \neq i} \int_ {0} ^ {t} \mathrm{e} ^ {- q _ {i} s} q _ {i k} g _ {k j} ^ {(n - 1)} (t - s) \mathrm{d} s, \quad t \geqslant 0, n \geqslant 1. \tag {7.2.13}
$$

证明 由定理7.2.2, 显然 $t \mapsto g_{ij}^{(0)}(t) = \delta_{ij}\mathrm{e}^{-q_it}$ 连续可导. 现在对于 $n \geqslant 1$, 设 $t \mapsto g_{ij}^{(n-1)}(t)$ 连续可导. 根据概率的可数可加性,

$$
\begin{array}{l} g _ {i j} ^ {(n)} (t) = \sum_ {k \neq i} \mathbf {P} _ {i} \big (X _ {S _ {1}} = k, S _ {n} \leqslant t <   S _ {n + 1}, X _ {t} = j \big) \\ = \sum_ {k \neq i} \mathbf {P} _ {i} \big (S _ {1} \leqslant t, X _ {S _ {1}} = k, S _ {n} \leqslant t <   S _ {n + 1}, X _ {t} = j \big) \\ = \sum_ {k \neq i} \mathbf {P} _ {i} (A _ {k}) \mathbf {P} _ {i} \big (S _ {n} \leqslant t <   S _ {n + 1}, X _ {t} = j | A _ {k} \big), \\ \end{array}
$$

其中 $A_{k} = \{S_{1}\leqslant t,X_{S_{1}} = k\}$ .令 $(\mathcal{F}_t)$ 为 $(X_{t})$ 的自然流.对 $q\geqslant 1$ 定义函数

$$
r _ {q} (s) = \frac {1}{2 ^ {q}} (\lfloor 2 ^ {q} s \rfloor + 1) = \sum_ {k = 1} ^ {\infty} \frac {k}{2 ^ {q}} 1 _ {\{\frac {k - 1}{2 ^ {q}} \leqslant s <   \frac {k}{2 ^ {q}} \}}, \quad s \geqslant 0,
$$

则 $r_q(t - S_1)$ 关于 $\mathcal{F}_{S_1}$ 可测, 故对任何 $r \geqslant 1$ 有 $G_{k,q,r} := A_k \cap \{r_q(t - S_1) = r / 2^q\} \in \mathcal{F}_{S_1}$. 根据定理7.1.5在 $\mathbf{P}_i(\cdot | G_{k,q,r})$ 之下 $(X_{S_1 + t}: t \geqslant 0)$ 是具有密度矩阵 $Q$ 的马氏链, 所以有

$$
\mathbf {P} _ {i} \big (S _ {n} \leqslant S _ {1} + r / 2 ^ {q} <   S _ {n + 1}, X _ {S _ {1} + r / 2 ^ {q}} = j | G _ {k, q, r} \big) = g _ {k j} ^ {(n - 1)} (r / 2 ^ {q}).
$$

注意, 当  $q \rightarrow \infty$  时, 递降地  $r_{q}(t - S_{1}) \rightarrow t - S_{1}$ , 故利用轨道的右连续性,

$$
\begin{array}{l} \mathbf {P} _ {i} (S _ {n} \leqslant t <   S _ {n + 1}, X _ {t} = j | A _ {k}) \\ = \lim _ {q \to \infty} \sum_ {r = 1} ^ {\infty} \mathbf {P} _ {i} \big (r _ {q} (t - S _ {1}) = r / 2 ^ {q} | A _ {k} \big) g _ {k j} ^ {(n - 1)} (r / 2 ^ {q}) \\ = \lim _ {q \to \infty} \sum_ {r = 1} ^ {\infty} \mathbf {P} _ {i} \big [ g _ {k j} ^ {(n - 1)} (r _ {q} (t - S _ {1})) 1 _ {\{r _ {q} (t - S _ {1}) = r / 2 ^ {q} \}} | A _ {k} \big ] \\ = \lim _ {q \to \infty} \mathbf {P} _ {i} \big [ g _ {k j} ^ {(n - 1)} (r _ {q} (t - S _ {1})) | A _ {k} \big ]. \\ \end{array}
$$

$$
= \lim _ {q \to \infty} \mathbf {P} _ {i} \big (S _ {n} \leqslant S _ {1} + r _ {q} (t - S _ {1}) <   S _ {n + 1}, X _ {S _ {1} + r _ {q} (t - S _ {1})} = j | A _ {k} \big)
$$

因为 Q 保守, 根据上面关系及定理 7.2.2 给出的  $\tau = S_{1}$  与  $X_{\tau}$  的联合分布,

$$
\begin{array}{l} g _ {i j} ^ {(n)} (t) = \lim _ {q \to \infty} \sum_ {k \neq i} \mathbf {P} _ {i} (A _ {k}) \mathbf {P} _ {i} \big [ g _ {k j} ^ {(n - 1)} (r _ {q} (t - S _ {1})) | A _ {k} \big ] \\ = \lim _ {q \to \infty} \sum_ {k \neq i} \mathbf {P} _ {i} \left[ g _ {k j} ^ {(n - 1)} (r _ {q} (t - S _ {1})) 1 _ {\{S _ {1} \leqslant t, X _ {S _ {1}} = k \}} \right] \\ = \lim _ {q \to \infty} \sum_ {k \neq i} \int_ {0} ^ {t} \mathrm{e} ^ {- q _ {i} s} q _ {i k} g _ {k j} ^ {(n - 1)} (r _ {q} (t - s)) \mathrm{d} s \\ = \sum_ {k \neq i} \int_ {0} ^ {t} \mathrm{e} ^ {- q _ {i} s} q _ {i k} g _ {k j} ^ {(n - 1)} (t - s) \mathrm{d} s \\ = \sum_ {k \neq i} \int_ {0} ^ {t} \mathrm{e} ^ {- q _ {i} (t - s)} q _ {i k} g _ {k j} ^ {(n - 1)} (s) \mathrm{d} s. \\ \end{array}
$$

故 $t \mapsto g_{ij}^{(n)}(t)$ 连续可导. 根据数学归纳法知 (7.2.13) 式对所有 $n \geqslant 1$ 成立. □

推论 7.2.4 设右连续马氏链 X 有保守密度的矩阵 Q. 令  $\zeta = \lim_{n \to \infty} S_n$  和

$$
f _ {i j} (t) = \mathbf {P} _ {i} (X \text {在} [ 0, t ] \text {中跳有限次且} X _ {t} = j) = \mathbf {P} _ {i} (t <   \zeta , X _ {t} = j), \tag {7.2.14}
$$

则有

$$
f _ {i j} (t) = \sum_ {k = 0} ^ {\infty} g _ {i j} ^ {(k)} (t). \tag {7.2.15}
$$

推论 7.2.4 中定义的停时  $\zeta$  就是 X 的第一个无穷多次跳跃时刻的聚点, 称为 X 的第一个飞跃时. 不难看出, 在  $[0,\zeta)$  上 X 的轨道是阶梯函数, 即当  $S_{n} \leqslant t < S_{n+1}$  时有 $X_{t} = X_{S_{n}}$。特别地, 密度矩阵 $Q$ 完全决定马氏链在第一个飞跃时 $\zeta$ 以前的运动规律. 关于 $\zeta$ 我们有下面的:

定理 7.2.5 若密度矩阵 Q 保守且  $M := \sup_{i \in E} q_i < \infty$ ，则  $\mathbf{P}(\zeta = \infty) = 1$ .

证明 令 $(\mathcal{F}_t)$ 为 $X$ 的自然流. 对 $n \geqslant 1$, 当 $S_{n-1} < \infty$ 时令 $\tau_n = S_n - S_{n-1}$. 强马氏性和定理7.2.2, 对于任意的 $a > 0$ 和 $A \in \mathcal{F}_{S_{n-1}}$ 有

$$
\begin{array}{l} \mathbf {P} (\tau_ {n} \leqslant a | A \cap \{S _ {n - 1} <   \infty \}) \\ = \sum_ {i \in E} \mathbf {P} (X _ {S _ {n - 1}} = i | A \cap \{S _ {n - 1} <   \infty \}) \cdot \\ \mathbf {P} (\tau_ {n} \leqslant a | A \cap \{S _ {n - 1} <   \infty , X _ {S _ {n - 1}} = i \}) \\ = \sum_ {i \in E} \mathbf {P} (X _ {S _ {n - 1}} = i | A \cap \{S _ {n - 1} <   \infty \}) (1 - \mathrm{e} ^ {- a q _ {i}}) \\ \leqslant \sum_ {i \in E} \mathbf {P} (X _ {S _ {n - 1}} = i | A \cap \{S _ {n - 1} <   \infty \}) (1 - \mathrm{e} ^ {- a M}) = 1 - \mathrm{e} ^ {- a M}. \\ \end{array}
$$

对于 $k, l \geqslant 1$ 令 $A_{k,l} = \bigcap_{n=k}^{k+l}\{S_{n-1} < \infty, \tau_n \leqslant a\}$. 由上式有

$$
\begin{array}{l} \mathbf {P} (A _ {k, l}) = \mathbf {P} \big (A _ {k, l - 1} \cap \{S _ {k + l - 1} <   \infty \} \cap \{\tau_ {k + l} \leqslant a \} \big) \\ = \mathbf {P} \big (A _ {k, l - 1} \cap \{S _ {k + l - 1} <   \infty \} \big)  . \\ \mathbf {P} \big (\tau_ {k + l} \leqslant a | A _ {k, l - 1} \cap \{S _ {k + l - 1} <   \infty \} \big) \\ \leqslant \mathbf {P} \big (A _ {k, l - 1} \cap \{S _ {k + l - 1} <   \infty \} \big) (1 - \mathrm{e} ^ {- a M}) \\ \leqslant \mathbf {P} \big (A _ {k, l - 1} \big) (1 - \mathrm{e} ^ {- a M}) = \dots = (1 - \mathrm{e} ^ {- a M}) ^ {l + 1}. \\ \end{array}
$$

再由概率测度的上连续性得

$$
\mathbf {P} \Big (\bigcap_ {n = k} ^ {\infty} \{S _ {n - 1} <   \infty , \tau_ {n} \leqslant a \} \Big) = \lim _ {l \to \infty} \mathbf {P} (A _ {k, l}) = \lim _ {l \to \infty} (1 - \mathrm{e} ^ {- a M}) ^ {l + 1} = 0.
$$

显然, 若 $\zeta < \infty$, 则每个 $S_{n-1}, n \geqslant 1$ 有限且至多只有有限个 $n \geqslant 1$ 使得 $\tau_n > a$, 故

$$
\begin{array}{l} \{\zeta <   \infty \} \subseteq \left(\bigcap_ {n = 1} ^ {\infty} \{S _ {n - 1} <   \infty \}\right) \cap \left(\bigcup_ {k = 1} ^ {\infty} \bigcap_ {n = k} ^ {\infty} \{\tau_ {n} \leqslant a \}\right) \\ = \bigcup_ {k = 1} ^ {\infty} \left(\bigcap_ {n = 1} ^ {\infty} \{S _ {n - 1} <   \infty \} \cap \bigcap_ {n = k} ^ {\infty} \{\tau_ {n} \leqslant a \}\right) \\ = \bigcup_ {k = 1} ^ {\infty} \bigcap_ {n = k} ^ {\infty} \{S _ {n - 1} <   \infty , \tau_ {n} \leqslant a \}, \\ \end{array}
$$

其中的等号成立是由于停时列 $\{S_n\}$ 单增. 因此有

$$
\mathbf {P} (\zeta <   \infty) \leqslant \sum_ {k = 1} ^ {\infty} \mathbf {P} \Big (\bigcap_ {n = k} ^ {\infty} \{S _ {n - 1} <   \infty , \tau_ {n} \leqslant a \} \Big) = 0,
$$