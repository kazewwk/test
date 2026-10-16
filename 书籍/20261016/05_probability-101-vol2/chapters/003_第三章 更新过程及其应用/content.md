# 第三章 更新过程及其应用

原始 PDF 第 75–92 页。

70

第三章 更新过程及其应用

在应用中经常需要考虑比泊松过程更广的一类计数过程, 它们的跳跃间隔时间由独立同分布随机变量给出, 但这些随机变量未必服从指数分布. 这样的计数过程就是 “更新过程”. 本章讨论更新过程的若干基本性质, 包括更新方程、基本更新定理、大数定律、中心极限定理等, 并介绍该模型对于随机游动和若干实际问题的应用.

## 3.1 更新过程

## 3.1.1 定义和性质

考虑某概率空间 $(\Omega, \mathcal{F}, \mathbf{P})$ 上的独立同分布的非负随机变量序列 $\{\xi_n : n \geqslant 1\}$. 令 $F$ 为其共同的分布函数. 假定 $F(0) = \mathbf{P}(\xi_n = 0) < 1$, 因而 $\mu := \mathbf{E}(\xi_n) > 0$. 这里我们不排除 $\mu = \infty$ 的情况. 记 $S_0 = 0$, 并令

$$
S _ {n} = \sum_ {k = 1} ^ {n} \xi_ {k}, \quad n \geqslant 1, \tag {3.1.1}
$$

则 $(S_{n}:n\geqslant0)$ 是具有非负跳幅的随机游动.

命题 3.1.1 当  $n \to \infty$  时几乎必然地  $S_{n}/n \to \mu$ .

证明 当 $\mu < \infty$ 时, 由强大数定律知命题的结论成立. 下面考虑 $\mu = \infty$ 的情况. 对 $n, k \geqslant 1$ 记 $\xi_{n}^{(k)} = \xi_{n} \wedge k$. 则 $\{\xi_{n}^{(k)} : n \geqslant 1\}$ 是独立同分布非负随机变量序列, 且当 $k$ 充分大时有 $0 < \mu^{(k)} := \mathbf{E}(\xi_{1}^{(k)}) < \infty$. 令 $(S_{n}^{(k)} : n \geqslant 0)$ 为由 $\{\xi_{n}^{(k)} : n \geqslant 1\}$ 定义的具有非负跳幅的随机游动. 显然有 $\xi_{n}^{(k)} \leqslant \xi_{n}$ 和 $S_{n}^{(k)} \leqslant S_{n}$. 根据强大数定律, 几乎必然有

$$
\operatorname * {l i m i n f} _ {n \to \infty} \frac {S _ {n}}{n} \geqslant \lim _ {n \to \infty} \frac {S _ {n} ^ {(k)}}{n} = \mu^ {(k)}.
$$

因  $\lim_{k\to\infty}\mu^{(k)}=\mu=\infty,$  在上式两端取极限知几乎必然  $\lim_{n\to\infty}S_{n}/n=\infty.$  ☐

在实践中, 人们经常用 (3.1.1) 式定义的序列 $\{S_n : n \geqslant 1\}$ 表示一系列更新发生的时刻. 显然, 对 $t \geqslant 0$ 在时间区间 $(0, t]$ 更新发生的次数为

$$
N (t) := \sum_ {n = 1} ^ {\infty} 1 _ {\{S _ {n} \leqslant t \}} = \sup \{n \geqslant 0: S _ {n} \leqslant t \}. \tag {3.1.2}
$$

根据命题3.1.1几乎必然地 $\lim_{n\to \infty}S_n = \infty$ ，故对任何 $t\geqslant 0$ 至多只有有限个 $n$ 使得$S_{n}\leqslant t,$ 进而 $N(t) <   \infty$ .由(3.1.2)式不难看出，对于 $n\geqslant 0$ 和 $t\geqslant 0$ 有

$$
N (t) \geqslant n \Leftrightarrow S _ {n} \leqslant t; \tag {3.1.3}
$$

---

3.1 更新过程

71

而对于 $t \geqslant 0$ 有

$$
S _ {N (t)} \leqslant t <   S _ {N (t) + 1}. \tag {3.1.4}
$$

定义 3.1.1 我们称由 (3.1.2) 式定义的零初值不降非负整数值过程  $(N(t): t \geqslant 0)$  为更新过程, 称  $S_{n}$  为其第 n 次更新时间, 而称每个  $\xi_{n}$  为其更新间隔时间.

例 3.1.1 设有一批同类型的电子元件, 其寿命是独立同分布的随机变量. 在某台机器上使用着一个此种元件, 当它损坏时立即用备件进行替换. 设  $\{\xi_{n}: n \geqslant 1\}$  为依次使用的元件的寿命, 则  $S_{n}$  代表第 n 个备件安装的时刻, 而  $N(t)$  代表到 t 时刻为止更换元件的次数.

下面的命题表明, 由更新过程  $(N(t): t \geqslant 0)$  描述的更新现象的总更新次数  $N(\infty) := \lim_{t \to \infty} N(t)$  几乎必然是无穷大.

命题 3.1.2 几乎必然有  $N(\infty)=\infty$ .

证明 若 $N(\infty)$ 为有限数, 则它必为非负整数, 同时必有 $S_{N(\infty)} < \infty$ 且 $S_{N(\infty)+1} = \infty$, 而这意味着 $\xi_{N(\infty)+1} = \infty$, 故

$$
\mathbf {P} (N (\infty) <   \infty) \leqslant \mathbf {P} \Big (\bigcup_ {n = 1} ^ {\infty} \{\xi_ {n} = \infty \} \Big) \leqslant \sum_ {n = 1} ^ {\infty} \mathbf {P} (\xi_ {n} = \infty) = 0.
$$

因此几乎必然有 $N(\infty) = \infty$ ，□

根据假设, 随机变量序列 $\{\xi_n\}$ 有共同的分布函数 $F$. 所以 $S_n$ 的分布就是 $F$ 的 $n$ 重卷积 $F^{*n}$. 再由 (3.1.3) 式有

$$
\begin{array}{l} \mathbf {P} (N (t) = n) = \mathbf {P} (N (t) \geqslant n) - \mathbf {P} (N (t) \geqslant n + 1) \\ = \mathbf {P} (S _ {n} \leqslant t) - \mathbf {P} (S _ {n + 1} \leqslant t) \\ = F ^ {* n} (t) - F ^ {* (n + 1)} (t). \tag {3.1.5} \\ \end{array}
$$

例3.1.2 设 $\{\xi_n\}$ 服从几何分布 $G(p)$, 其中 $0 \leqslant p \leqslant 1$, 即 $\mathbf{P}(\xi_n = k) = p(1 - p)^{k-1}$, $k \geqslant 1$. 此时 $S_n$ 代表伯努利试验中第 $n$ 次成功出现的时间, 它服从帕斯卡分布, 即

$$
\mathbf {P} (S _ {n} = k) = \mathrm{C} _ {k - 1} ^ {n - 1} p ^ {n} (1 - p) ^ {k - n}, \quad k \geqslant n.
$$

用 $\lfloor t\rfloor$ 表示不超过 $t$ 的最大整数. 则 $\mathbf{P}(N(t) = n)$ 就是在前 $\lfloor t\rfloor$ 次试验中出现 $n$ 次成功的概率, 故有

$$
\mathbf {P} (N (t) = n) = \mathrm{C} _ {\lfloor t \rfloor} ^ {n} p ^ {n} (1 - p) ^ {\lfloor t \rfloor - n}, \quad 0 \leqslant n \leqslant \lfloor t \rfloor ,
$$

即  $N(t)$  服从二项分布  $B(\lfloor t \rfloor, p)$ .

---

72

第三章 更新过程及其应用

例 3.1.3 设  $\{\xi_{n}\}$  服从以  $\lambda > 0$  为参数的指数分布, 即  $F(x) = 1 - \mathrm{e}^{-\lambda x}, x > 0$ . 此时  $S_{n}$  的分布  $F^{*n}$  为伽马分布  $\Gamma(\lambda, n)$ , 它有分布密度

$$
p _ {n} (x) = \frac {\lambda^ {n}}{\Gamma (n)} x ^ {n - 1} \mathrm{e} ^ {- \lambda x}, \quad x > 0.
$$

所以

$$
\begin{array}{l} 1 - F ^ {* n} (t) = \frac {\lambda^ {n}}{\Gamma (n)} \int_ {t} ^ {\infty} y ^ {n - 1} \mathrm{e} ^ {- \lambda y} \mathrm{d} y \\ = \frac {\lambda^ {n}}{n \Gamma (n)} \left[ y ^ {n} \mathrm{e} ^ {- \lambda y} \Big | _ {t} ^ {\infty} + \lambda \int_ {t} ^ {\infty} y ^ {n} \mathrm{e} ^ {- \lambda y} \mathrm{d} y \right] \\ = - \frac {(\lambda t) ^ {n}}{n !} \mathrm{e} ^ {- \lambda t} + 1 - F ^ {* (n + 1)} (t). \\ \end{array}
$$

再由 (3.1.5) 式可得

$$
\mathbf {P} (N (t) = n) = \frac {(\lambda t) ^ {n}}{n !} \mathrm{e} ^ {- \lambda t}, \quad n \geqslant 0.
$$

事实上, 由定理 1.4.3 知  $(N(t): t \geqslant 0)$  就是以  $\lambda$  为参数的泊松过程.

## 3.1.2 更新方程

称 $m(t) := \mathbf{E}[N(t)]$, $t \geqslant 0$ 为更新过程 $(N(t): t \geqslant 0)$ 的更新函数. 由 (3.1.3) 式和非负整数值随机变量的期望的计算公式可得

$$
m (t) = \sum_ {n = 1} ^ {\infty} \mathbf {P} (N (t) \geqslant n) = \sum_ {n = 1} ^ {\infty} \mathbf {P} (S _ {n} \leqslant t) = \sum_ {n = 1} ^ {\infty} F ^ {* n} (t), \quad t \geqslant 0, \tag {3.1.6}
$$

其中  $F^{*n}$  表示 F 的 n 重卷积.

命题 3.1.3 对任何  $t \geqslant 0$  有  $m(t) < \infty$ .

证明 显然  $F^{*n}(t)$  关于  $n \geqslant 1$  单调不增, 且当 n 充分大 ( $n \geqslant 1$ ) 时有

$$
F ^ {* n} (t) = \mathbf {P} \Big (\sum_ {k = 1} ^ {n} \xi_ {k} \leqslant t \Big) <   1.
$$

再由 (3.1.6) 式得

$$
m (t) = \sum_ {k = 0} ^ {\infty} \sum_ {i = 1} ^ {n} F ^ {* k n} * F ^ {* i} (t) \leqslant \sum_ {k = 0} ^ {\infty} \sum_ {i = 1} ^ {n} F ^ {* k n} (t) \leqslant n \Big [ 1 + \sum_ {k = 1} ^ {\infty} F ^ {* n} (t) ^ {k} \Big ].
$$

显然上式右端有限. □

由 (3.1.6) 式和命题 3.1.3 知更新函数 $m(t)$ 是 $[0, \infty)$ 上的非负不降有限函数. 再由 (3.1.6) 式可得如下的通过卷积表达的方程:

$$
m (t) = F (t) + m * F (t), \quad t \geqslant 0. \tag {3.1.7}
$$

---

3.1 更新过程

73

定义 3.1.2 设 H 为  $[0, \infty)$  上的局部有界可测函数, 而 F 为  $[0, \infty)$  上的概率分布函数. 称如下方程为更新方程

$$
K (t) = H (t) + K * F (t), \quad t \geqslant 0, \tag {3.1.8}
$$

其中  $K*F$  表示 K 和 F 的卷积, 即

$$
K * F (t) = \int_ {0} ^ {t} K (t - x) \mathrm{d} F (x). \tag {3.1.9}
$$

这里一般应将等式 (3.1.9) 右边理解为关于 $F$ 决定的概率测度的积分. 利用测度论中的富比尼 (Fubini) 定理, 可以证明该式定义了一个局部有界可测函数 $K * F$. 显然方程 (3.1.8) 是更新函数的方程 (3.1.7) 的推广.

定理 3.1.4 方程 (3.1.8) 存在唯一的局部有界可测函数解 K, 且该解具有如下的卷积表达形式

$$
K (t) = H (t) + H * m (t), \quad t \geqslant 0. \tag {3.1.10}
$$

证明 由富比尼定理可知 (3.1.10) 式确实定义了一个局部有界可测函数 $K$. 再根据 (3.1.6) 式和 (3.1.10) 式有

$$
\begin{array}{l} K (t) = H (t) + \Big (H * \sum_ {n = 1} ^ {\infty} F ^ {* n} \Big) (t) \\ = H (t) + H * F (t) + H * \Big (\sum_ {n = 2} ^ {\infty} F ^ {* (n - 1)} * F \Big) (t) \\ = H (t) + (H + H * m) * F (t). \\ \end{array}
$$

所以 $K$ 满足方程 (3.1.8), 即该方程有解. 反之, 设 $K$ 为方程 (3.1.8) 的局部有界可测函数解. 反复应用该方程可得

$$
\begin{array}{l} K (t) = H (t) + (H + K * F) * F (t) \\ = H (t) + H * F (t) + K * F ^ {* 2} (t) = \dots \\ = H (t) + H * \Big (\sum_ {k = 1} ^ {n - 1} F ^ {* k} \Big) (t) + K * F ^ {* n} (t). \tag {3.1.11} \\ \end{array}
$$

对上式右边的最后一项可做如下估计:

$$
| K * F ^ {* n} (t) | \leqslant \int_ {0} ^ {t} | K (t - x) | \mathrm{d} F ^ {* n} (x) \leqslant \sup _ {0 \leqslant s \leqslant t} | K (s) | F ^ {* n} (t).
$$

由 (3.1.6) 式和命题 3.1.3 知, 当 $n \to \infty$ 时有 $F^{*n}(t) \to 0$, 从而 $K * F^{*n}(t) \to 0$. 在 (3.1.11) 式两端令 $n \to \infty$ 即得 (3.1.10)式. 这就证明了该方程的解的唯一性. $\square$

---

74

第三章 更新过程及其应用

定理3.1.5 对任何 $0 \leqslant s \leqslant t$ 有

$$
\mathbf {P} (S _ {N (t)} \leqslant s) = 1 - F (t) + \int_ {0} ^ {s} [ 1 - F (t - x) ] \mathrm{d} m (x).
$$

证明 对任何 $0 \leqslant s \leqslant t$ 可写

$$
\begin{array}{l} \mathbf {P} (S _ {N (t)} \leqslant s) = \mathbf {P} (N (t) = 0) + \sum_ {n = 1} ^ {\infty} \mathbf {P} (S _ {N (t)} \leqslant s, N (t) = n) \\ = \mathbf {P} (\xi_ {1} > t) + \sum_ {n = 1} ^ {\infty} \mathbf {P} (S _ {n} \leqslant s, \xi_ {n + 1} > t - S _ {n}) \\ = 1 - F (t) + \sum_ {n = 1} ^ {\infty} \mathbf {E} \big [ 1 _ {\{S _ {n} \leqslant s \}} \mathbf {P} (\xi_ {n + 1} > t - S _ {n} | S _ {n}) \big ]. \\ \end{array}
$$

因随机变量序列  $\{\xi_{n}\}$  独立同分布, 利用 (3.1.6) 式可以推得

$$
\begin{array}{l} \mathbf {P} (S _ {N (t)} \leqslant s) = 1 - F (t) + \sum_ {n = 1} ^ {\infty} \int_ {0} ^ {s} \mathbf {P} (\xi_ {n + 1} > t - x | S _ {n} = x) \mathrm{d} F ^ {* n} (x) \\ = 1 - F (t) + \sum_ {n = 1} ^ {\infty} \int_ {0} ^ {s} [ 1 - F (t - x) ] \mathrm{d} F ^ {* n} (x) \\ = 1 - F (t) + \int_ {0} ^ {s} [ 1 - F (t - x) ] \mathrm{d} m (x), \\ \end{array}
$$

即欲证等式成立. (因为可能有 $\mathbf{P}(S_n = x) = 0$, 所以上式中第一个等号的严格论证需要更多工作, 这里从略.) $\square$

由 (3.1.4) 式可知 $W(t) := S_{N(t)+1} - t$ 为严格正的随机变量, 它给出 $t$ 时刻的待更新时间. 令 $(\mathscr{F}_n)$ 为 $(S_n : n \geqslant 0)$ 的自然流, 由 (3.1.3) 式有

$$
\{N (t) + 1 = n \} = \{n - 1 \leqslant N (t) <   n \} = \{S _ {n - 1} \leqslant t <   S _ {n} \} \in \mathscr {F} _ {n}, \tag {3.1.12}
$$

故 $N(t) + 1$ 是 $(\mathcal{F}_n)$ 的停时. 应用沃尔德恒等式易得

$$
\mathbf {E} [ W (t) ] = \mu [ m (t) + 1 ] - t.
$$

所以  $m(t)$  和  $\mathbf{E}[W(t)]$  相互唯一决定.

定理 3.1.6 对任何  $t, x \geqslant 0$  有

$$
\mathbf {P} (W (t) > x) = 1 - F (t + x) + \int_ {0} ^ {t} [ 1 - F (t + x - y) ] \mathrm{d} m (y).
$$

证明 记 $K_{x}(t) = \mathbf{P}(W(t) > x)$, 则有

$$
\mathbf {P} (W (t) > x | \xi_ {1} = y) = \left\{ \begin{array}{l l} 1, & y > t + x, \\ 0, & t <   y \leqslant t + x, \\ K _ {x} (t - y), & 0 <   y \leqslant t. \end{array} \right.
$$

---

3.1 更新过程

75

所以

$$
\begin{array}{l} K _ {x} (t) = \int_ {0} ^ {\infty} \mathbf {P} (W (t) > x | \xi_ {1} = y) \mathrm{d} F (y) \\ = 1 - F (t + x) + \int_ {0} ^ {t} K _ {x} (t - y) \mathrm{d} F (y). \\ \end{array}
$$

上式为 (3.1.8) 式的特例. 由定理 3.1.4 即得欲证等式. $\square$

例3.1.4 设更新间隔时间服从均匀分布 $U(0,1)$, 即 $F(t) = t$, $0 \leqslant t \leqslant 1$. 由定理3.1.4有

$$
m (t) = F (t) + \int_ {0} ^ {t} m (t - x) \mathrm{d} F (x) = t + \int_ {0} ^ {t} m (x) \mathrm{d} x.
$$

求导得  $m'(t)=1+m(t)$ . 又因  $m(0)=0$ , 解微分方程得  $m(t)=\mathrm{e}^{t}-1$ .

## 练习题

1. 设  $(N(t): t \geqslant 0)$  为 (3.1.2) 式定义的更新过程, 求  $g(t) := \mathbf{E}[N(t)^{2}]$ .

提示: 令  $S_{1}$  是第一次更新的时间, 则

$$
g (t) = \mathbf {E} \{\mathbf {E} [ N (t) ^ {2} | S _ {1} ] \} = \int_ {0} ^ {t} \mathbf {E} [ N (t) ^ {2} | S _ {1} = x ] \mathrm{d} F (x).
$$

证明

$$
g (t) = F (t) + 2 \int_ {0} ^ {t} m (t - x) \mathrm{d} F (x) + \int_ {0} ^ {t} g (t - x) \mathrm{d} F (x).
$$

由 (3.1.7) 式知 $g$ 是如下方程的解:

$$
g (t) = 2 m (t) - F (t) + \int_ {0} ^ {t} g (t - x) \mathrm{d} F (x),
$$

根据定理 3.1.4 有

$$
g (t) = 2 m (t) - F (t) + [ 2 m - F ] * m (t).
$$

再应用 (3.1.7) 式得  $g(t)=m(t)+2m*m(t)$ .

2. 在例 3.1.1 中, 设 $L(t) = S_{N(t)+1} - S_{N(t)}$, 则 $L(t)$ 代表时刻 $t$ 在用元件的总寿命. 证明 $\mathbf{P}(L(t) > x) \geqslant \mathbf{P}(\xi_1 > x)$.

提示: 当  $t \leqslant x$  时结论显然. 当 t > x 时有

$$
\mathbf {P} (L (t) > x) = \sum_ {k = 0} ^ {\infty} \mathbf {P} (\xi_ {k + 1} > x, S _ {k} \leqslant t, \xi_ {k + 1} > t - S _ {k})
$$

---

76

第三章 更新过程及其应用

$$
\begin{array}{l} = \sum_ {k = 1} ^ {\infty} \mathbf {P} (\xi_ {k + 1} > x, t - x <   S _ {k} \leqslant t) + \sum_ {k = 0} ^ {\infty} \mathbf {P} (\xi_ {k + 1} > t - S _ {k}, S _ {k} \leqslant t - x) \\ = \mathbf {P} (\xi_ {1} > x) \mathbf {E} [ (N (t) - N (t - x)) ] + \mathbf {P} \{N (t) = N (t - x) \} \\ = \mathbf {P} (\xi_ {1} > x) + \mathbf {P} (\xi_ {1} > x) \mathbf {E} \big [ (N (t) - N (t - x) - 1) 1 _ {\{N (t) > N (t - x) \}} \big ] - \\ \mathbf {P} (\xi_ {1} > x) \mathbf {E} \big (1 _ {\{N (t) = N (t - x) \}} \big) + \mathbf {P} \{N (t) = N (t - x) \} \\ \geqslant \mathbf {P} (\xi_ {1} > x). \\ \end{array}
$$

3. 设更新间隔时间服从均匀分布 $U(0,1)$. 对于 $0 < t < 1$ 求 $S_{N(t)}$ 的概率分布和 $\mathbf{E}[S_{N(t)}]$.
4. 投掷一枚均匀硬币, 直到连续出现两次正面, 称为一次更新. 连续不断地投掷该硬币, 到第 $k$ 次投掷为止, 更新的次数记为 $N(k)$. 求更新的间隔时间 $T$ 的分布和期望. 简答: 记 $p_n = \mathbf{P}(T = n)$. 显然有 $p_1 = 0$ 和 $p_2 = 1/4$. 令 $A_i$ 表示第 $i$ 次出现正面. 当 $n \geqslant 3$ 时, 根据全概率公式有

$$
\mathbf {P} (T = n) = \mathbf {P} (A _ {1} ^ {c}) \mathbf {P} (T = n | A _ {1} ^ {c}) + \mathbf {P} (A _ {1} A _ {2} ^ {c}) \mathbf {P} (T = n | A _ {1} A _ {2} ^ {c}).
$$

也即

$$
p _ {n} = \frac {1}{2} p _ {n - 1} + \frac {1}{4} p _ {n - 2}.
$$

由上面递推关系得

$$
p _ {n} = \frac {1}{2 \sqrt {5}} \Big [ \Big (\frac {1 + \sqrt {5}}{4} \Big) ^ {n - 1} - \Big (\frac {1 - \sqrt {5}}{4} \Big) ^ {n - 1} \Big ].
$$

另一方面, 根据全期望公式有

$$
\mathbf {E} (T) = \mathbf {P} (A _ {1} ^ {c}) \mathbf {E} (T | A _ {1} ^ {c}) + \mathbf {P} (A _ {1} A _ {2} ^ {c}) \mathbf {E} (T | A _ {1} A _ {2} ^ {c}) + \mathbf {P} (A _ {1} A _ {2}) \mathbf {E} (T | A _ {1} A _ {2}),
$$

故有

$$
\mathbf {E} (T) = \frac {1}{2} [ 1 + \mathbf {E} (T) ] + \frac {1}{4} [ 2 + \mathbf {E} (T) ] + \frac {1}{2} = \frac {3}{4} \mathbf {E} (T) + \frac {3}{2},
$$

解出得  $\mathbf{E}(T)=6.$

## 3.2 长程极限行为

设 $(N(t):t\geqslant 0)$ 是由(3.1.2)式给出的更新过程.我们已经看到，对于此更新过程几乎必然有 $N(\infty) = \infty$ .本节中我们讨论 $N(t)$ 和 $m(t)$ 的长时间的增长速度和极限行为.

---

3.2 长程极限行为

77

## 3.2.1 基本更新定理

定理 3.2.1 当  $t \rightarrow \infty$  时几乎必然地  $N(t)/t \rightarrow 1/\mu$ .

证明 根据命题3.1.1, 可以取 $\Omega_1 \in \mathcal{F}$ 满足 $\mathbf{P}(\Omega_1) = 1$ 且当 $\omega \in \Omega_1$ 时有 $\lim_{n \to \infty} S_n(\omega)/n = \mu$. 再根据命题3.1.2, 可以取 $\Omega_2 \in \mathcal{F}$ 满足 $\mathbf{P}(\Omega_2) = 1$ 且当 $\omega \in \Omega_2$ 时有 $\lim_{t \to \infty} N(t, \omega) = N(\infty, \omega) = \infty$. 显然 $\Omega_0 := \Omega_1 \cap \Omega_2 \in \mathcal{F}$ 满足 $\mathbf{P}(\Omega_0) = 1$ 且在 $\Omega_0$ 上有

$$
\lim _ {t \to \infty} \frac {S _ {N (t)}}{N (t)} = \lim _ {t \to \infty} \frac {S _ {N (t) + 1}}{N (t) + 1} = \mu , \quad \lim _ {t \to \infty} \frac {N (t) + 1}{N (t)} = 1.
$$

由 (3.1.4) 式有

$$
\frac {S _ {N (t)}}{N (t)} \leqslant \frac {t}{N (t)} <   \frac {S _ {N (t) + 1}}{N (t)} = \frac {S _ {N (t) + 1}}{N (t) + 1} \cdot \frac {N (t) + 1}{N (t)},
$$

所以在  $\Omega_{0}$  上有  $N(t)/t \rightarrow 1/\mu.$  ☐

基于定理 3.2.1 的结论, 我们称  $1/\mu$  为平均更新速率. 注意, 即便有  $\mu = \infty$ , 定理 3.2.1 仍然成立, 此时我们将该结论理解为  $N(t)/t \to 0$ .

定理 3.2.2 (基本更新定理) 当  $t \rightarrow \infty$  时有  $m(t)/t \rightarrow 1/\mu$ .

证明 令 $(\mathcal{F}_n)$ 为 $\{\xi_n : n \geqslant 0\}$ 的自然流, 由 (3.1.12) 式知 $N(t) + 1$ 是 $(\mathcal{F}_n)$ 的停时. 再由 (3.1.4) 式有

$$
S _ {N (t) + 1} = \sum_ {n = 1} ^ {N (t) + 1} \xi_ {n} > t.
$$

应用沃尔德恒等式得

$$
[ m (t) + 1 ] \mu = \mathbf {E} [ N (t) + 1 ] \mu = \mathbf {E} [ S _ {N (t) + 1} ] > t,
$$

故有

$$
\operatorname * {l i m i n f} _ {t \to \infty} \frac {m (t)}{t} = \operatorname * {l i m i n f} _ {t \to \infty} \frac {m (t) + 1}{t} \geqslant \frac {1}{\mu}. \tag {3.2.1}
$$

显然 (3.2.1) 式对于 $\mu = \infty$ 的情况仍然成立. 另一方面, 设 $\{\xi_n^{(k)} : n \geqslant 1\}$ 和 $(S_n^{(k)} : n \geqslant 0)$ 如命题 3.1.1 的证明中所定义. 令 $(N^{(k)}(t) : t \geqslant 0)$ 为相应的更新过程. 由 (3.1.4) 式有

$$
S _ {N ^ {(k)} (t) + 1} ^ {(k)} = S _ {N ^ {(k)} (t)} ^ {(k)} + \xi_ {N ^ {(k)} (t) + 1} ^ {(k)} \leqslant t + k,
$$

记 $\mu^{(k)} = \mathbf{E}(\xi_1^{(k)})$ 和 $m^{(k)}(t) = \mathbf{E}[N^{(k)}(t)]$. 再次应用沃尔德恒等式得

$$
[ m ^ {(k)} (t) + 1 ] \mu^ {(k)} = \mathbf {E} [ N ^ {(k)} (t) + 1 ] \mu^ {(k)} = \mathbf {E} \big [ S _ {N ^ {(k)} (t) + 1} ^ {(k)} \big ] \leqslant t + k,
$$

---

78

第三章 更新过程及其应用

故有

$$
\operatorname * {l i m s u p} _ {t \to \infty} \frac {m ^ {(k)} (t)}{t} \leqslant \frac {1}{\mu^ {(k)}},
$$

由于 $S_{n}^{(k)}\leqslant S_{n}$ ，有 $N^{(k)}(t)\geqslant N(t)$ 和 $m^{(k)}(t)\geqslant m(t)$ ，因而

$$
\operatorname * {l i m s u p} _ {t \to \infty} \frac {m (t)}{t} \leqslant \frac {1}{\mu^ {(k)}}.
$$

对上式取极限 $k \to \infty$ 即知

$$
\operatorname * {l i m s u p} _ {t \to \infty} \frac {m (t)}{t} \leqslant \frac {1}{\mu}. \tag {3.2.2}
$$

综合 (3.2.1) 式和 (3.2.2) 式即得定理的结果. $\square$

## 3.2.2 中心极限定理

假定更新间隔时间序列  $\{\xi_{n}\}$  平方可积, 并记  $\mu = \mathbf{E}(\xi_{1})$  和  $\sigma^{2} = \mathbf{Var}(\xi_{1})$ . 下面的定理说明当 t 充分大时  $N(t)$  近似地服从均值为  $t/\mu$ , 方差为  $t\sigma^{2}/\mu^{3}$  的正态分布.

定理 3.2.3（中心极限定理） 对于任何 $x \in \mathbb{R}$, 当 $t \to \infty$ 时有

$$
\mathbf {P} \Big (\frac {N (t) - t / \mu}{\sqrt {t \sigma^ {2} / \mu^ {3}}} \leqslant x \Big) \rightarrow \varPhi (x) := \frac {1}{\sqrt {2 \pi}} \int_ {- \infty} ^ {x} \mathrm{e} ^ {- y ^ {2} / 2} \mathrm{d} y.
$$

证明 令 $r(t) = t / \mu + y\sigma \sqrt{t / \mu^3}$. 注意

$$
\frac {N (t) - t / \mu}{\sqrt {t \sigma^ {2} / \mu^ {3}}} \geqslant y \Leftrightarrow N (t) \geqslant r (t) \Rightarrow N (t) \geqslant \lfloor r (t) \rfloor .
$$

由 (3.1.3) 式知 $N(t) \geqslant \lfloor r(t) \rfloor$ 当且仅当 $S_{\lfloor r(t) \rfloor} \leqslant t$. 所以

$$
\frac {N (t) - t / \mu}{\sqrt {t \sigma^ {2} / \mu^ {3}}} \geqslant y \Rightarrow S _ {\lfloor r (t) \rfloor} \leqslant t \Leftrightarrow \frac {S _ {\lfloor r (t) \rfloor} - \lfloor r (t) \rfloor \mu}{\sigma \sqrt {\lfloor r (t) \rfloor}} \leqslant \frac {t - \lfloor r (t) \rfloor \mu}{\sigma \sqrt {\lfloor r (t) \rfloor}}.
$$

于是有

$$
\mathbf {P} \Big (\frac {N (t) - t / \mu}{\sqrt {t \sigma^ {2} / \mu^ {3}}} \geqslant y \Big) \leqslant \mathbf {P} \Big (\frac {S _ {\lfloor r (t) \rfloor} - \lfloor r (t) \rfloor \mu}{\sigma \sqrt {\lfloor r (t) \rfloor}} \leqslant \frac {t - \lfloor r (t) \rfloor \mu}{\sigma \sqrt {\lfloor r (t) \rfloor}} \Big). \tag {3.2.3}
$$

注意当 $t \to \infty$ 时 $r(t) \to \infty$, 并且

$$
\frac {t - r (t) \mu}{\sigma \sqrt {r (t)}} = \frac {- y \sqrt {t / \mu}}{(t / \mu + y \sigma \sqrt {t / \mu^ {3}}) ^ {1 / 2}} = - y \Big (1 + \frac {y \sigma}{\sqrt {t \mu}} \Big) ^ {- \frac {1}{2}} \to - y.
$$

---

3.2 长程极限行为

79

另外, 注意当  $r(t) > 1$  时有

$$
\frac {t - r (t) \mu}{\sigma \sqrt {r (t)}} \leqslant \frac {t - \lfloor r (t) \rfloor \mu}{\sigma \sqrt {\lfloor r (t) \rfloor}} \leqslant \frac {t - (r (t) - 1) \mu}{\sigma \sqrt {r (t) - 1}}.
$$

综合上面二式易知, 当  $t \to \infty$  时,

$$
\frac {t - \lfloor r (t) \rfloor \mu}{\sigma \sqrt {\lfloor r (t) \rfloor}} \to - y.
$$

因此, 对 (3.2.3) 式中的  $S_{\lfloor r(t) \rfloor}$  应用独立同分布随机变量和的中心极限定理可得

$$
\operatorname * {l i m s u p} _ {t \to \infty} \mathbf {P} \Big (\frac {N (t) - t / \mu}{\sqrt {t \sigma^ {2} / \mu^ {3}}} \geqslant y \Big) \leqslant \varPhi (- y) = 1 - \varPhi (y). \tag {3.2.4}
$$

另一方面, 注意

$$
\frac {N (t) - t / \mu}{\sqrt {t \sigma^ {2} / \mu^ {3}}} \geqslant y \Leftrightarrow N (t) \geqslant r (t) \Leftarrow N (t) \geqslant \lfloor r (t) \rfloor + 1.
$$

基于上式, 与前面推导类似地可以得到

$$
\operatorname * {l i m i n f} _ {t \to \infty} \mathbf {P} \Big (\frac {N (t) - t / \mu}{\sqrt {t \sigma^ {2} / \mu^ {3}}} \geqslant y \Big) \geqslant \varPhi (- y) = 1 - \varPhi (y). \tag {3.2.5}
$$

综合 (3.2.4) 式和 (3.2.5) 式即得定理的结论. $\square$

## 练习题

1. 有一台使用单个电池的收音机, 电池的寿命 (单位: h) 服从参数为 $\lambda = 1/30$ 的指数分布. 问长远来看, 需要以什么样的频率更换电池?
2. 考虑平均更新间隔时间为 $\mu$ 的原更新过程. 假设每次更新以概率 $p$ 被记录, 且各次的记录与各次更新都相互独立. 以 $N_{r}(t)$ 表示到时刻 $t$ 为止被记录的更新次数. 问记录的过程 $(N_{r}(t): t \geqslant 0)$ 是更新过程吗? 求记录过程的长程平均更新次数 $\lim_{t \to \infty} N_{r}(t)/t$.

提示: 可以证明记录的更新间隔时间仍然是独立同分布的随机变量, 所以记录的过程仍然是更新过程.

3. 容器里有无限多枚硬币, 其中每枚在投掷时正面朝上的概率都是服从 (0,1) 上的均匀分布的随机变量且相互独立. 现从容器中随机取一枚硬币并连续投掷, 直到出现正面朝上, 称为一次更新. 然后重新从容器中随机取一枚硬币, 并重复上述过程. 用 $N(n)$ 表示前 $n$ 次投掷中正面朝上的次数. 求 $\lim_{n\to \infty}N(n)/n$.

提示: 设到第一次正面朝上为止的投掷次数为 $\xi_{1}$. 用 $X$ 表示第一枚硬币正面朝上的概率. 根据假设 $X$ 服从均匀分布 $U(0,1)$, 且在给定 $X = x$ 条件下 $\xi_{1}$ 服从几何分布, 即

$$
\mathbf {P} (\xi_ {1} = n | X = x) = (1 - x) ^ {n - 1} x.
$$

---

80

第三章 更新过程及其应用

于是 $\mathbf{E}(\xi_1|X = x) = 1 / x$ 所以

$$
\mathbf {E} (\xi_ {1}) = \int_ {0} ^ {1} \mathbf {E} (\xi_ {1} | X = x) \mathrm{d} x = \int_ {0} ^ {1} \frac {\mathrm{d} x}{x} = \infty .
$$

4. 设更新过程 $(N(t): t \geqslant 0)$ 的更新间隔时间序列 $\{\xi_n\}$ 取正整数值。记 $A_{n} = \{\text{在时刻 } n \text{ 发生更新}\}$。证明:若极限 $a := \lim_{n \to \infty} \mathbf{P}(A_{n})$ 存在，则有 $a = 1 / \mathbf{E}(\xi_1)$。

提示: 注意到时刻 n 为止的更新次数为  $N(n)=\sum_{k=1}^{n}1_{A_{k}}$ . 因此

$$
m (n) = \mathbf {E} [ N (n) ] = \sum_ {k = 1} ^ {n} \mathbf {P} (A _ {k}).
$$

根据分析结果有  $m(n)/n \rightarrow a$ . 再应用基本更新定理.

5. 两台机器各自独立地处理无穷个同种工序. 设 1 号机器处理一个工序的时间服从参数为 1 的指数分布, 而 2 号机器处理的时间服从均匀分布 $U(0,2)$. 求到时刻 100 两台机器共处理 190 个及以上工序的概率的近似值.

简答: 用 $N_{i}(t)$ 表示 $i$ 号机器到时刻 $t$ 共处理的工序数, 则 $(N_{1}(t): t \geqslant 0)$ 和 $(N_{2}(t): t \geqslant 0)$ 是两个独立的更新过程. 用 $\mu_{i}$ 和 $\sigma_{i}^{2}$ 分别表示 $i$ 号机器的更新间隔时间的期望和方差, 则有

$$
\mu_ {1} = 1, \sigma_ {1} ^ {2} = 1, \mu_ {2} = 1, \sigma_ {2} ^ {2} = 1 / 3.
$$

根据更新过程的中心极限定理, 独立随机变量

$$
\frac {N _ {1} (1 0 0) - 1 0 0}{\sqrt {1 0 0}}, \quad \frac {N _ {2} (1 0 0) - 1 0 0}{\sqrt {1 0 0 / 3}}
$$

渐近服从标准正态分布. 因此

$$
X _ {1 0 0} := \frac {N _ {1} (1 0 0) + N _ {2} (1 0 0) - 2 0 0}{2 \sqrt {1 0 0 / 3}}
$$

渐近服从标准正态分布, 故

$$
\mathbf {P} (N _ {1} (1 0 0) + N _ {2} (1 0 0) \geqslant 1 9 0) = \mathbf {P} \Big (X _ {1 0 0} \geqslant - \frac {\sqrt {3}}{2} \Big).
$$

## 3.3 更新过程的应用

本节介绍更新过程理论的应用, 包括在随机游动研究中的应用和对若干实际问题的应用.

---

3.3 更新过程的应用

81

## 3.3.1 随机游动的爬升时间

设 $\{\xi_n : n \geqslant 1\}$ 是独立同分布的可积随机变量序列且满足 $\mathbf{E}\xi_n > 0$. 令 $(W_n : n \geqslant 0)$ 是以 $\{\xi_n\}$ 为跳幅的随机游动, 其中 $W_0 = 0$. 根据强大数定律, 当 $n \to \infty$ 时几乎必然地 $W_n / n \to \mathbf{E}\xi_1 > 0$, 故 $W_n \to \infty$. 令 $(\mathscr{F}_n)$ 为 $(W_n)$ 的自然流. 记 $S_0 = 0$ 并对 $n \geqslant 1$ 递推地定义整数值 $(\mathscr{F}_n)$ 停时

$$
S _ {n} = \min \left\{k \geqslant S _ {n - 1}: W _ {k} > W _ {S _ {n - 1}} \right\}.
$$

称每个 $S_{n}$ 为 $(W_{n})$ 的爬升时间.

定理3.3.1 对于 $n \geqslant 1$ 令 $\eta_{n} = S_{n} - S_{n-1}$. 则 $\{\eta_{n}\}$ 是独立同分布的非负随机变量序列.

证明 对  $n \geqslant 1$  和  $k_{n} > \cdots > k_{2} > k_{1} \geqslant 1$  显然有  $\{S_{1} = k_{1}, S_{2} = k_{2}, \cdots, S_{n} = k_{n}\} \in \mathscr{F}_{k_{n}}$ ，故该事件与  $\{\xi_{k_{n}+j} : j \geqslant 1\}$  独立。因此对  $\theta_{1}, \theta_{2}, \cdots, \theta_{m} \in R$  有

$$
\begin{array}{l} \mathbf {E} \bigg (\exp \left\{\mathrm{i} \sum_ {j = 1} ^ {m} \theta_ {j} \xi_ {S _ {n} + j} \right\} \Big | S _ {1} = k _ {1}, S _ {2} = k _ {2}, \dots , S _ {n} = k _ {n} \bigg) \\ = \mathbf {E} \bigg (\exp \left\{\mathrm{i} \sum_ {j = 1} ^ {m} \theta_ {j} \xi_ {k _ {n} + j} \right\} \Big | S _ {1} = k _ {1}, S _ {2} = k _ {2}, \dots , S _ {n} = k _ {n} \bigg) \\ = \mathbf {E} \bigg (\exp \left\{\mathrm{i} \sum_ {j = 1} ^ {m} \theta_ {j} \xi_ {k _ {n} + j} \right\} \bigg) = \prod_ {j = 1} ^ {m} \mathbf {E} \Big (\exp \left\{\mathrm{i} \theta_ {j} \xi_ {j} \right\} \Big). \\ \end{array}
$$

再应用全期望公式可得

$$
\mathbf {E} \bigg (\exp \left\{\mathrm{i} \sum_ {j = 1} ^ {m} \theta_ {j} \xi_ {S _ {n} + j} \right\} \bigg) = \prod_ {j = 1} ^ {m} \mathbf {E} \bigg (\exp \left\{\mathrm{i} \theta_ {j} \xi_ {j} \right\} \bigg).
$$

这说明  $\{\xi_{S_{n}+k}:k\geqslant1\}$  为独立随机变量序列,与  $\xi_{1}$  同分布且与  $(S_{1},S_{2},\cdots,S_{n})$  独立.
注意  $(W_{S_{n}+k}-W_{S_{n}}:k\geqslant0)$  是以  $(\xi_{S_{n}+k}:k\geqslant1)$  为跳幅的随机游动. 易见

$$
\eta_ {n + 1} = \min \left\{k \geqslant 0: W _ {S _ {n} + k} - W _ {S _ {n}} > 0 \right\}.
$$

所以  $\eta_{n+1}$  与  $\eta_{1}=S_{1}$  同分布且与  $(S_{1},S_{2},\cdots,S_{n})$  独立, 从而  $\eta_{n+1}$  与  $(\eta_{1},\eta_{2},\cdots,\eta_{n})$  独立. 由此易知  $\{\eta_{n}\}$  独立同分布. □

根据定理 3.3.1 知  $\{\eta_{n}\}$  是非负整数值独立同分布随机变量. 因此爬升时间序列  $(S_{n})$  是以  $\{\eta_{n}\}$  为跳幅的随机游动. 借助基本更新定理, 可以给出随机游动  $(W_{n})$  保持恒非负的概率的一个表达. 这就是下面的:

定理 3.3.2 我们有

$$
\mathbf {P} (W _ {1} > 0, W _ {2} > 0, \dots) = \frac {1}{\mathbf {E} (S _ {1})}. \tag {3.3.1}
$$

---

82

第三章 更新过程及其应用

证明 令 $(N(t):t\geqslant 0)$ 是由 $\{\eta_n\}$ 和 $(S_{n})$ 决定的更新过程.对 $n\geqslant 1$ 记

$A_{n}=\{n$  为爬升时间 $\}=\{ 存在某个 k\geqslant1 使得 S_{k}=n\}.$

注意

$$
\begin{array}{l} \mathbf {P} (A _ {n}) = \mathbf {P} (W _ {n} > W _ {n - 1}, \dots , W _ {n} > W _ {1}, W _ {n} > 0) \\ = \mathbf {P} (W _ {n} - W _ {n - 1} > 0, \dots , W _ {n} - W _ {1} > 0, W _ {n} > 0) \\ = \mathbf {P} (W _ {1} > 0, \dots , W _ {n - 1} > 0, W _ {n} > 0). \\ \end{array}
$$

所以有

$$
\lim _ {n \to \infty} \mathbf {P} (A _ {n}) = \mathbf {P} (W _ {1} > 0, W _ {2} > 0, \dots).
$$

另一方面, 不难发现

$$
m (n) = \mathbf {E} [ N (n) ] = \mathbf {E} \Bigl (\sum_ {k = 1} ^ {n} 1 _ {A _ {k}} \Bigr) = \sum_ {k = 1} ^ {n} \mathbf {P} (A _ {k}).
$$

于是, 根据级数的极限性质有

$$
\lim _ {n \to \infty} \frac {m (n)}{n} = \mathbf {P} (W _ {1} > 0, W _ {2} > 0, \dots).
$$

再由基本更新定理即得(3.3.1)式. □

## 3.3.2 更新累积过程

设 $\{(\xi_n, \eta_n): n \geqslant 1\}$ 为独立同分布的二维随机变量序列, 且其中的 $\{\xi_n : n \geqslant 1\}$ 均非负. 令 $(N(t): t \geqslant 0)$ 是以 $\{\xi_n : n \geqslant 1\}$ 为更新间隔时间的更新过程. 此模型可以描述某种数量指标随时间的增加过程, 即在第 $n$ 次更新发生时, 该指标相应地有一个增量 $\eta_n$. 这样, 我们可以定义下面的更新累积过程:

$$
A (t) = \sum_ {n = 1} ^ {N (t)} \eta_ {n}, \quad t \geqslant 0.
$$

很多应用中的概率模型都可归结为此模型的特殊情况.

定理 3.3.3 设有 $0 < \mathbf{E}(\xi_1) < \infty$ 和 $\mathbf{E}(|\eta_1|) < \infty$, 则几乎必然地

$$
\lim _ {t \to \infty} \frac {A (t)}{t} = \frac {\mathbf {E} (\eta_ {1})}{\mathbf {E} (\xi_ {1})}.
$$

证明 根据定理 3.2.1, 当  $t \to \infty$  时几乎必然地  $N(t)/t \to 1/\mathbf{E}(\xi_{1})$ . 再由强大数定律, 此时几乎必然地有  $A(t)/N(t) \to \mathbf{E}(\eta_{1})$ . 综合二者即得结论. □

---

3.3 更新过程的应用

83

定理 3.3.4 设有 $0 < \mathbf{E}(\xi_1) < \infty$ 和 $\mathbf{E}(|\eta_1|) < \infty$, 则

$$
\lim _ {t \to \infty} \frac {\mathbf {E} [ A (t) ]}{t} = \frac {\mathbf {E} (\eta_ {1})}{\mathbf {E} (\xi_ {1})}.
$$

证明 令 $(\mathcal{F}_n)$ 为 $\{(\xi_n, \eta_n): n \geqslant 1\}$ 的自然流. 由 (3.1.12) 式知 $N(t) + 1$ 是 $(\mathcal{F}_n)$ 的停时. 根据沃尔德恒等式有

$$
\mathbf {E} [ A (t) ] = \mathbf {E} \Big (\sum_ {n = 1} ^ {N (t) + 1} \eta_ {n} \Big) - g (t) = [ m (t) + 1 ] \mathbf {E} (\eta_ {1}) - g (t),
$$

其中 $g(t) = \mathbf{E}(\eta_{N(t) + 1})$ 根据上式和基本更新定理，只需要证明 $\lim_{t\to \infty}g(t) / t = 0$ 记$h(t) = \mathbf{E}(\eta_1;\xi_1 > t)$ .因 $\{(\xi_n,\eta_n):n\geqslant 1\}$ 独立同分布，利用(3.1.6)式有

$$
\begin{array}{l} g (t) = \sum_ {k = 0} ^ {\infty} \mathbf {E} (\eta_ {N (t) + 1}; N (t) = k) \\ = \sum_ {k = 0} ^ {\infty} \mathbf {E} (\eta_ {k + 1}; S _ {k} \leqslant t, S _ {k} + \xi_ {k + 1} > t) \\ = \sum_ {k = 0} ^ {\infty} \mathbf {E} [ 1 _ {\{S _ {k} \leqslant t \}} \mathbf {E} (\eta_ {k + 1}; \xi_ {k + 1} > t - S _ {k} | S _ {k}) ] \\ = h (t) + \sum_ {k = 1} ^ {\infty} \mathbf {E} [ h (t - S _ {k}) 1 _ {\{S _ {k} \leqslant t \}} ] \\ = h (t) + \sum_ {k = 1} ^ {\infty} \int_ {0} ^ {t} h (t - s) \mathrm{d} F ^ {* k} (s) \\ = h (t) + \int_ {0} ^ {t} h (t - s) \mathrm{d} m (s). \\ \end{array}
$$

由控制收敛定理有  $\lim_{t\to\infty}h(t)=0$  。故对任意的  $\varepsilon>0$  ，存在 T>0 使对  $t\geqslant T$  有  $h(t)<\varepsilon$  。所以当  $t\geqslant T$  时有

$$
\begin{array}{l} \frac {g (t)}{t} = \frac {h (t)}{t} + \int_ {0} ^ {t - T} \frac {h (t - s)}{t} \mathrm{d} m (s) + \int_ {t - T} ^ {t} \frac {h (t - s)}{t} \mathrm{d} m (s) \\ \leqslant \frac {\varepsilon}{t} [ 1 + m (t - T) ] + \frac {1}{t} \mathbf {E} (| \eta_ {1} |) [ m (t) - m (t - T) ]. \\ \end{array}
$$

由上式和基本更新定理易得  $\lim_{t\to\infty}g(t)/t=0.$  □

在更新累积模型中, 每发生一次更新, 我们就说完成了一个循环. 这样, 定理 3.3.3 和定理 3.3.4 说明, 单位时间内的长程平均累积速率等于一个循环内得到的期望累积除以循环的期望长度.

例 3.3.1 某车间所用机器的寿命是具有分布函数 F 的随机变量. 当机器损坏或使用到达 T 年时, 将其报废并更换新机器. 证明: (1) 机器的长程平均替换速率为

$$
\frac {1}{T [ 1 - F (T) ] + \int_ {0} ^ {T} x \mathrm{d} F (x)};
$$

---

84

第三章 更新过程及其应用

(2) 机器的长程平均失效速率为

$$
\frac {F (T)}{T [ 1 - F (T) ] + \int_ {0} ^ {T} x \mathrm{d} F (x)}.
$$

解 根据假设, 机器的寿命列为具有相同分布函数 $F$ 的独立随机变量序列 $\{X_{n}\}$, 而更新间隔时间序列为 $\{\xi_{n}\}$, 其中 $\xi_{n} := X_{n} \wedge T$. 每更换一台机器就完成一个循环, 而一个循环的平均长度为

$$
\mathbf {E} (\xi_ {1}) = T \mathbf {P} (X _ {1} > T) + \mathbf {E} (X _ {1} 1 _ {\{X \leqslant T \}}) = T [ 1 - F (T) ] + \int_ {0} ^ {T} x \mathrm{d} F (x).
$$

注意, 第 $n$ 个循环中失效的机器数可表示为 $\eta_{n} = 1_{\{X_{n} \leqslant T\}}$. 易知 $\mathbf{E}(\eta_1) = F(T)$. 故得欲证结果. $\square$

例 3.3.2 设某零件的更换由更新过程  $\{N(t):t\geqslant0\}$  刻画, 且更新间隔时间  $\{\xi_{n}\}$  有有限的方差. 用  $U(t)=t-S_{N(t)}$  表示零件的 “使用年龄”. 证明零件的长程平均使用年龄的表达式

$$
\lim _ {T \to \infty} \frac {1}{T} \int_ {0} ^ {T} U (t) \mathrm{d} t = \frac {\mathbf {E} (\xi_ {1} ^ {2})}{2 \mathbf {E} (\xi_ {1})}.
$$

证明 根据 (3.1.4) 式有 $S_{N(T)} \leqslant T$, 故

$$
\begin{array}{l} \int_ {0} ^ {T} U (t) \mathrm{d} t \geqslant \sum_ {i = 1} ^ {N (T)} \int_ {S _ {i - 1}} ^ {S _ {i}} U (t) \mathrm{d} t = \sum_ {i = 1} ^ {N (T)} \int_ {S _ {i - 1}} ^ {S _ {i}} (t - S _ {i - 1}) \mathrm{d} t \\ = \frac {1}{2} \sum_ {i = 1} ^ {N (T)} (S _ {i} - S _ {i - 1}) ^ {2} = \frac {1}{2} \sum_ {i = 1} ^ {N (T)} \xi_ {i} ^ {2}. \\ \end{array}
$$

类似地有

$$
\int_ {0} ^ {T} U (t) \mathrm{d} t \leqslant \frac {1}{2} \sum_ {i = 1} ^ {N (T) + 1} (S _ {i} - S _ {i - 1}) ^ {2} = \frac {1}{2} \sum_ {i = 1} ^ {N (T) + 1} \xi_ {i} ^ {2}.
$$

根据定理 3.2.1 和定理 3.3.3 易得

$$
\lim _ {T \to \infty} \frac {1}{2 T} \sum_ {i = 1} ^ {N (T)} \xi_ {i} ^ {2} = \frac {\mathbf {E} (\xi_ {1} ^ {2})}{2 \mathbf {E} (\xi_ {1})}.
$$

同理

$$
\lim _ {T \to \infty} \frac {1}{2 T} \sum_ {i = 1} ^ {N (T) + 1} \xi_ {i} ^ {2} = \frac {\mathbf {E} (\xi_ {1} ^ {2})}{2 \mathbf {E} (\xi_ {1})}.
$$

所以长程平均使用年龄的表达式成立. □

---

3.3 更新过程的应用

85

例 3.3.3 某车站的乘客按照更新间隔时间均值为  $\mu$  的更新过程到达. 车站当乘客数量达到 x 时发一班车. 当有 n 个乘客等候时, 候车室会产生每小时 cn 元的费用. 给出候车室的长程平均费用计算公式. 设每开出一班车, 车站会产生 a 元的费用. 给出车站的长程平均费用计算公式. 问 x 取何值车站的长程平均费用最低?

解 用 $T_{n}$ 表示第 $n$ 位与第 $n + 1$ 位乘客到达的间隔时间. 根据假设有 $\mathbf{E}(T_n) = \mu$. 在此模型中, 每发出一班车就称完成了一次循环. 用 $\xi_{1}$ 表示第一班车发车的时刻. 则每次循环的期望时间为 $\mathbf{E}(\xi_1) = x\mu$. 用 $\eta_{1}$ 表示到第一班车发车时候车室的费用. 则 $\eta_{1} = c[T_{1} + 2T_{2} + \dots + (x - 1)T_{x - 1}]$, 故在每个循环中候车室的期望费用为

$$
\mathbf {E} (\eta_ {1}) = c \mu \big [ 1 + 2 + \dots + (x - 1) \big ] = \frac {1}{2} c \mu x (x - 1).
$$

所以候车室的长程平均费用为

$$
f (x) = \frac {\mathbf {E} (\eta_ {1})}{\mathbf {E} (\xi_ {1})} = \frac {c \mu x (x - 1)}{2 \mu x} = \frac {1}{2} c (x - 1).
$$

车站的长程平均费用为

$$
g (x) = \frac {a + c \mu x (x - 1) / 2}{\mu x} = \frac {2 a + c \mu x (x - 1)}{2 \mu x}.
$$

对上式求导有

$$
g ^ {\prime} (x) = \frac {2 c \mu^ {2} x (2 x - 1) - 4 a \mu - 2 c \mu^ {2} x (x - 1)}{(2 \mu x) ^ {2}} = \frac {2 c \mu^ {2} x ^ {2} - 4 a \mu}{(2 \mu x) ^ {2}}.
$$

令 $g'(x) = 0$ ，得 $c\mu x^{2} - 2a = 0.$ 该方程的解为

$$
x = \sqrt {2 a / c \mu}.
$$

所以, 取 x 为离  $\sqrt{2a/c\mu}$  最近的正整数, 车站的长程平均费用最低.

## 练习题

1. 设某零件的更换由更新过程 $(N(t): t \geqslant 0)$ 刻画, 且更新间隔时间随机变量 $X$ 的方差有限. 用 $R(t) = S_{N(t)+1} - t$ 表示零件的“剩余寿命”. 求零件的长程平均剩余寿命

$$
\lim _ {T \to \infty} \frac {1}{T} \int_ {0} ^ {T} R (t) \mathrm{d} t.
$$

2. 到达电影院的观众人数是参数为 $\lambda$ 的泊松流. 假设电影 $t (\geqslant 0)$ 时刻开演. 令 $A(t)$ 表示时间区间 $(0, t]$ 内到达的观众的总等待时间. 求 $\mathbf{E}[A(t)]$.

---

86

第三章 更新过程及其应用

提示: 用 $V_{k}$ 表示第 $k$ 名观众的到达时刻. 设在时间区间 $(0, t]$ 内到达的观众数为 $N(t)$, 则有

$$
A (t) = \sum_ {k = 1} ^ {N (t)} (t - V _ {k}).
$$

由泊松过程的构造知  $\sum_{k=1}^{\infty}\delta_{V_{k}}$  是  $(0,\infty)$  的以  $\lambda dt$  为强度的泊松随机测度. 因此  $V_{1}, V_{2}, \cdots, V_{n}$  与  $(0,t)$  中的相互独立且均服从均匀分布随机变量  $U_{1}, U_{2}, \cdots, U_{n}$  的次序统计量有相同的分布, 故

$$
\mathbf {E} \Big [ \sum_ {k = 1} ^ {n} V _ {k} \Big | N (t) = n \Big ] = \mathbf {E} \Big (\sum_ {k = 1} ^ {n} U _ {k} \Big) = \frac {n t}{2}.
$$

3. 某车间机器的寿命是绝对连续型随机变量, 其密度为 $p$. 当机器损坏或使用到达 $T$ 年时, 将其报废并更换新机器. 设新机器价格为 $C_1$ 万元, 且若因旧机器损坏而更换, 则需要额外花费 $C_2$ 万元. (1) 给出车间的长程平均运行费用计算公式. (2) 若已知 $C_1 = 10$, $C_2 = 0.5$ 且机器寿命服从均匀分布, 问当 $T$ 取何值时长程平均运行费用最低?

提示: 在此问题中, 每更换一台机器, 就完成一个循环. 若用 $\xi$ 表示第一台机器的寿命, 则第一个循环的长度是 $\xi_1 := \xi \wedge T$. 显然

$$
\mathbf {E} (\xi_ {1}) = T \mathbf {P} (\xi > T) + \mathbf {E} (\xi 1 _ {\{\xi \leqslant T \}}) = T \int_ {T} ^ {\infty} p (x) \mathrm{d} x + \int_ {0} ^ {T} x p (x) \mathrm{d} x.
$$

注意, 第一个循环完成时的费用为

$$
\eta_ {1} := C _ {1} 1 _ {\{\xi > T \}} + (C _ {1} + C _ {2}) 1 _ {\{\xi \leqslant T \}} = C _ {1} + C _ {2} 1 _ {\{\xi \leqslant T \}}.
$$

所以

$$
\mathbf {E} (\eta_ {1}) = C _ {1} + C _ {2} \mathbf {P} (\xi \leqslant T) = C _ {1} + C _ {2} \int_ {0} ^ {T} p (x) \mathrm{d} x.
$$

因此车间的长程平均运行费用计算公式为

$$
g (T) = \frac {C _ {1} + C _ {2} \int_ {0} ^ {T} p (x) \mathrm{d} x}{T \int_ {T} ^ {\infty} p (x) \mathrm{d} x + \int_ {0} ^ {T} x p (x) \mathrm{d} x}.
$$

4. 生产线按顺序生产某种产品, 且每件产品合格的概率为 $p (0 < p < 1)$. 执行以下抽样质检方案: 开始时逐一检查每件产品, 直到连续出现 $k$ 件合格品, 之后以概率 $\alpha (0 < \alpha < 1)$ 检查每件产品, 直到查出不合格品, 此时一个循环结束. 接着重新开始逐一检查每件产品, 如此循环下去. 求长时间看被检查的产品所占的比例.

---

3.3 更新过程的应用

87

提示: 将此问题的流程看作更新累积过程. 为方便叙述, 不妨称在检查中连续出现的 $k$ 件合格品为 $k$ 件合格品串. 令 $N_k$ 为第一个 $k$ 件合格品串结束时的产品数. 下面推导关于 $M_k := \mathbf{E}(N_k)$ 的递推公式. 为此在第一个 $k-1$ 件合格品串结束后, 对下一件产品的情况分类考虑. 令 $G_k$ 表示 “下一件产品合格”. 若 $G_k$ 发生, 则此前的 $k-1$ 件合格品串与此件合格品构成一个 $k$ 件合格品串, 故 $\mathbf{E}(N_k - N_{k-1}|G_k) = 1$; 而若 $G_k^c$ 发生, 则此前出现的 $k-1$ 件合格品串失效, 需要等待新的 $k$ 件合格品串, 故 $\mathbf{E}(N_k - N_{k-1}|G_k^c) = \mathbf{E}(N_k + 1)$. 由于 $\mathbf{P}(G_k) = p$, 根据全期望公式有

$$
\mathbf {E} (N _ {k} - N _ {k - 1}) = p + (1 - p) \mathbf {E} (N _ {k} + 1),
$$

亦即

$$
M _ {k} - M _ {k - 1} = p + (1 - p) (1 + M _ {k}).
$$

由此可得

$$
p M _ {k} = M _ {k - 1} + 1, \quad p M _ {k - 1} = M _ {k - 2} + 1.
$$

将上面二式相减得 $p(M_k - M_{k-1}) = M_{k-1} - M_{k-2}$. 故有

$$
M _ {k} = \frac {1}{p} + \frac {1}{p ^ {2}} + \dots + \frac {1}{p ^ {k}} = \frac {1 / p ^ {k} - 1}{1 - p}.
$$

由于每件产品为不合格品的概率为 $q := 1 - p$, 根据几何分布的性质, 要发现一件不合格品需要检查的平均产品数为 $1 / q$. 因此

$$
\mathbf {E} (\mathrm{一个循环中被检查的产品数}) = \mathbf {E} (N _ {k}) + 1 / q.
$$

在产品随机检查阶段, 每件产品被发现是不合格品的概率为  $\alpha q$ , 故发现一件不合格品需要的平均产品数为  $1/\alpha q$ . 因此

$$
\mathbf {E} (\text {一个循环中的产品的个数}) = \mathbf {E} (N _ {k}) + 1 / \alpha q.
$$
