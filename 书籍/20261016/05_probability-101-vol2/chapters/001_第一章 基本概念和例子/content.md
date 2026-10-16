# 第一章 基本概念和例子

原始 PDF 第 10–42 页。

2

第一章 基本概念和例子

随机过程描述某个系统在随机因素影响下随时间演进的过程. 这里的时间参量可以是离散的, 也可以是连续的. 本章介绍随机过程的基本结构和性质, 并讨论若干典型的例子, 主要内容包括过程的适应性、修正与实现、有限维分布族、随机游动、布朗运动、泊松过程、复合泊松过程和泊松随机测度等.

## 1.1 基本概念

## 1.1.1 随机过程的定义

定义在某个概率空间 $(\Omega, \mathcal{F}, \mathbf{P})$ 上, 取值于可测空间 $(E, \mathcal{E})$ 的随机变量族 $X = (X_t : t \in I)$ 称为随机过程, 简称过程. 此时, 称 $(E, \mathcal{E})$ 或 $E$ 为 $X$ 的状态空间. 我们经常会考虑 $E$ 为度量拓扑空间的情况, 此时一般取 $\mathcal{E}$ 为其博雷尔 $\sigma$ 代数, 即由 $E$ 的全体开子集生成的 $\sigma$ 代数. 特别地, 当 $E = \mathbb{R}$ 为欧氏空间时, 称 $X$ 为实数值过程.

原则上, 随机过程的指标集 $I$ 可以是任意的集合. 我们通常假定 $I$ 是整数集 $\mathbb{Z}$ 或实数集 $\mathbb{R}$ 中的某个区间, 分别称为离散时间集与连续时间集. 此时 $X$ 描述某个随机系统在时间区间 $I$ 的变化情况. 在指标集明确的情况下, 我们也会将 $(X_{t}: t \in I)$ 简写为 $(X_{t})$. 经常考虑的指标集 $I$ 的特例为 $\mathbb{Z}_{+} = \{0, 1, 2, \cdots\}$ 或 $\mathbb{R}_{+} = [0, \infty)$. 此时也将 $(X_{t}: t \in I)$ 写作 $(X_{t}: t \geqslant 0)$ 或 $(X_{n}: n \geqslant 0)$. 注意 $(X_{n}: n \geqslant 0)$ 就是随机变量序列 $(X_{0}, X_{1}, X_{2}, \cdots)$, 它也可以看作一个可数无穷维随机向量.

设 $(X_{t}:t\in I)$ 和 $(Y_{t}:t\in J)$ 是定义在某个概率空间 $(\Omega,\mathscr{F},\mathbf{P})$ 上的随机过程, 其指标集或状态空间都可以相同或不同. 若对任意的有限集 $(s_{1},s_{2},\cdots,s_{m})\subseteq I$ 和 $(t_{1},t_{2},\cdots,t_{n})\subseteq J$, 随机向量 $(X_{s_{1}},X_{s_{2}},\cdots,X_{s_{m}})$ 和 $(Y_{t_{1}},Y_{t_{2}},\cdots,Y_{t_{n}})$ 独立, 则称这两个随机过程是独立的.

例 1.1.1 设  $\{\xi_{n}: n \geqslant 1\}$  是概率空间  $(\Omega, \mathcal{F}, \mathbf{P})$  上的独立实数值随机变量序列，令  $X(0) = 0$  并对  $n \geqslant 1$  令  $X_{n} = \xi_{1} + \xi_{2} + \cdots + \xi_{n}$ ，则  $(X_{n}: n \geqslant 0)$  是一个随机过程。显然，对任何  $k \geqslant 1$ ，过程  $(X_{n \wedge k}: n \geqslant 0)$  和  $(X_{k+n} - X_{k}: n \geqslant 0)$  独立，其中  $n \wedge k = \min(n, k)$ 。

## 1.1.2 轨道和修正

设 $(X_{t}:t\in I)$ 是定义在某个概率空间 $(\Omega ,\mathcal{F},\mathbf{P})$ 上以 $(E,\mathcal{E})$ 为状态空间的随机过程.在固定 $\omega \in \Omega$ 后,由 $I$ 到 $\mathbb{R}^d$ 的映射 $t\mapsto X_t(\omega)$ 称为 $X$ 的轨道.轨道是一个随机过程的基本要素,关于轨道的结构与性质的研究是随机过程理论的重要内容.特别地,称

---

1.1 基本概念

3

以度量空间 $E$ 为状态空间的连续时间随机过程 $(X_{t}:t\geqslant 0)$ 是右连续的 (连续的, 左极右连的等), 是指其所有轨道右连续 (连续, 左极右连等).

定义 1.1.1 假定 $X = (X_{t}: t \in I)$ 和 $Y = (Y_{t}: t \in I)$ 是定义在概率空间 $(\Omega, \mathscr{F}, \mathbf{P})$ 上的以 $(E, \mathscr{E})$ 为状态空间的随机过程。若对任何 $t \in I$ 有 $N_{t} \in \mathscr{F}$ 满足 $\{X_{t} \neq Y_{t}\} \subset N_{t}$ 且 $\mathbf{P}(N_{t}) = 0$，则称 $X$ 和 $Y$ 互为修正。若存在 $\Omega_{1} \in \mathscr{F}$ 满足

$$
\Omega_ {1} \subseteq \Omega_ {0} := \{X _ {t} = Y _ {t} \text {对所有} t \in I \text {成立} \}
$$

且有  $\mathbf{P}(\Omega_{1})=1$ ，则称 X 和 Y 是无区别的。

易知, 当 $I$ 为可数集时, $X$ 和 $Y$ 是无区别的当且仅当它们互为修正. 对于一般的指标集, 无区别的过程互为修正, 但反之未必成立.

例 1.1.2 设 X 和 Y 都是实数值随机过程, 则对  $t \in I$  都有  $\{X_{t} = Y_{t}\} \in F$ . 此时 X 和 Y 互为修正当且仅当对一切  $t \in I$  有  $\mathbf{P}(X_{t} \neq Y_{t}) = 0$ .

例 1.1.3 设非负随机变量 T 的分布函数在 R 上连续. 对于  $t \geqslant 0$  和  $\omega \in \Omega$  定义  $\xi_{t}(\omega) = 0$  和  $\eta_{t}(\omega) = 1_{\{T(\omega)=t\}}$ ，则对任何  $t \geqslant 0$  有

$$
\mathbf {P} (\xi_ {t} \neq \eta_ {t}) = \mathbf {P} (\eta_ {t} = 1) = \mathbf {P} (T = t) = 0,
$$

故 $\mathbf{P}(\xi_t = \eta_t) = 1$ ，因而 $(\xi_t:t\geqslant 0)$ 与 $(\eta_t:t\geqslant 0)$ 互为修正.另一方面，显然有

$$
\mathbf {P} \left(\xi_ {t} = \eta_ {t} \text {对所有} t \geqslant 0 \text {成立}\right) = \mathbf {P} (\varnothing) = 0 \neq 1,
$$

其中 $\varnothing$ 表示空集. 因此 $(\xi_t : t \geqslant 0)$ 与 $(\eta_t : t \geqslant 0)$ 不是无区别的.

例 1.1.4 设  $\{\tau_{k}: k=1,2,\cdots\}$  为独立随机变量序列, 其中所有随机变量都服从参数为  $\alpha>0$  的指数分布. 记  $S_{n}=\sum_{k=1}^{n}\tau_{k}$ . 对任何  $t\geqslant0$  令

$$
N _ {t} = \sum_ {n = 1} ^ {\infty} 1 _ {\{S _ {n} \leqslant t \}}, \quad X _ {t} = \sum_ {n = 1} ^ {\infty} 1 _ {\{S _ {n} <   t \}},
$$

则随机过程 $(N_{t}:t\geqslant 0)$ 左极右连, 而 $(X_{t}:t\geqslant 0)$ 左连右极. 它们互为修正, 但不是无区别的.

命题 1.1.1 设  $(X_{t}:t\geqslant0)$  和  $(Y_{t}:t\geqslant0)$  是定义在概率空间  $(\Omega,\mathscr{F},\mathbf{P})$  上的以度量空间 E 为状态空间右连续的实数值随机过程, 而 D 是  $[0,\infty)$  的可数稠子集. 若对每个  $s\in D$  都有  $\mathbf{P}(X_{s}=Y_{s})=1$ , 则  $(X_{t}:t\geqslant0)$  和  $(Y_{t}:t\geqslant0)$  是无区别的.

证明 在假设条件下, 对每个 $s \geqslant 0$, 有 $N_{s} \in \mathcal{F}$, 满足 $\{X_{s} \neq Y_{s}\} \subset N_{s}$ 且 $\mathbf{P}(N_{s}) = 0$. 令 $\Omega_{1} = \bigcap_{s \in D} N_{s}^{c} \in \mathcal{F}$. 易知 $\mathbf{P}(\Omega_{1}) = 1$, 且对 $\omega \in \Omega_{1}$ 和 $s \in D$, 有 $X_{s}(\omega) = Y_{s}(\omega)$. 对任何 $t \geqslant 0$, 可取 $\{s_{n}\} \subseteq D$ 使 $s_{n} \downarrow t$. 根据两个过程的右连续性, 对

---

4 第一章 基本概念和例子

$\omega \in \Omega_1$ 有

$$
X _ {t} (\omega) = \lim _ {n \to \infty} X _ {s _ {n}} (\omega) = \lim _ {n \to \infty} Y _ {s _ {n}} (\omega) = Y _ {t} (\omega).
$$

所以 $(X_{t}:t\geqslant 0)$ 和 $(Y_{t}:t\geqslant 0)$ 无区别. □

设 $(X_{t}:t\geqslant 0)$ 是以 $\mathbb{R}^d$ 为状态空间的随机过程.称 $(X_{t}:t\geqslant 0)$ 是随机右连续的，是指对于所有 $t\geqslant 0$ 当 $s\downarrow t$ 时有 $X_{s}\stackrel {\mathrm{p}}{\to}X_{t}$ ，其中“ $\stackrel{\mathrm{p}}{\to}$ ”表示依概率收敛，即对任何$\varepsilon >0$ 有

$$
\lim _ {s \downarrow t} \mathbf {P} (\rho (X _ {s}, X _ {t}) \geqslant \varepsilon) = 0,
$$

其中 $\rho$ 表示 $\mathbb{R}^d$ 上的欧氏距离. 类似地, 可以定义随机左连续. 如果随机过程 $(X_t : t \geqslant 0)$ 既随机右连续又随机左连续, 就称其为随机连续.

命题 1.1.2 设  $(X_{t}: t \geqslant 0)$  是以  $R^{d}$  为状态空间的随机过程. (1) 若  $(X_{t}: t \geqslant 0)$  随机右连续且对  $t \geqslant 0$  右极限  $X_{t+}$  几乎必然存在, 则几乎必然地  $X_{t+} = X_{t}$ ; (2) 若  $(X_{t}: t \geqslant 0)$  随机左连续且对 t > 0 左极限  $X_{t-}$  几乎必然存在, 则几乎必然地  $X_{t-} = X_{t}$ .

证明 设 $(X_{t}: t \geqslant 0)$ 随机右连续且对 $t \geqslant 0$ 右极限 $X_{t+}$ 几乎必然存在. 根据依概率收敛的性质, 存在数列 $t_{n} \downarrow t$ 使得几乎必然有 $\lim_{n} X_{t_{n}} = X_{t}$. 但是 $\lim_{n} X_{t_{n}} = X_{t+}$, 因此几乎必然地 $X_{t+} = X_{t}$, 即 (1) 成立. 类似地可证 (2) 成立. $\square$

例 1.1.5 设非负随机变量 T 的分布函数 F 为 R 上的连续函数. 令  $X_{t}=1_{\{T\leqslant t\}}$ ，则对于任意的  $\varepsilon>0$  和  $t>s\geqslant0$  显然有

$$
\mathbf {P} (| X _ {s} - X _ {t} | \geqslant \varepsilon) \leqslant \mathbf {P} (X _ {s} = 0, X _ {t} = 1) = \mathbf {P} (s <   T \leqslant t) = F (t) - F (s).
$$

由此易知 $(X_{t}:t\geqslant0)$ 随机连续.

## 1.1.3 有限维分布族

考虑可测空间 $(E, \mathcal{E})$. 给定指标集 $I$, 我们用 $s(I)$ 表示 $I$ 的有序的有限子集全体, 即

$$
s (I) = \{(t _ {1}, t _ {2}, \dots , t _ {n}): n \geqslant 1; t _ {i} \in I; i = 1, 2, \dots , n \}.
$$

对  $J = (t_{1}, t_{2}, \cdots, t_{n}) \in s(I)$  写  $|J| = n$ . 若每个  $J \in s(I)$  都对应于乘积可测空间  $(E^{|J|}, \mathcal{E}^{|J|})$  上的一个概率测度  $\mu_{J}$ , 我们称

$$
\mathscr {D} = \{\mu_ {J}: J \in s (I) \}
$$

为 E 或  $(E, \mathcal{E})$  上的有限维分布族, 而称其中的每个  $\mu_{J}$  为有限维分布.

---

1.1 基本概念

5

设  $X = (X_{t} : t \in I)$  是定义在概率空间  $(\Omega, \mathcal{F}, \mathbf{P})$  上以  $(E, \mathcal{E})$  为状态空间的随机过程. 对  $J \in s(I)$ ，用  $\mu_{J}^{X}$  表示  $|J|$  维随机向量  $X_{J} := (X_{t_{1}}, X_{t_{2}}, \cdots, X_{t_{n}})$  在  $(E^{|J|}, \mathcal{E}^{|J|})$  上的分布，即对任何  $H \in E^{|J|}$ ，有

$$
\mu_ {J} ^ {X} (H) = \mu_ {(t _ {1}, t _ {2}, \dots , t _ {n})} ^ {X} (H) = \mathbf {P} \{(X _ {t _ {1}}, X _ {t _ {2}}, \dots , X _ {t _ {n}}) \in H \}. \tag {1.1.1}
$$

我们称 $\mu_J^X$ 为 $X$ 的一个有限维分布, 而称 $\mathcal{D}_X = \{\mu_J^X : J \in s(I)\}$ 为 $X$ 的有限维分布族.

定义 1.1.2 给定  $(E, \mathcal{E})$  上的有限维分布族 D, 若存在随机过程  $X = (X_{t} : t \in I)$  使  $D_{X} = D$ , 则称  $(X_{t} : t \in I)$  为 D 的实现. 若两个随机过程  $(X_{t} : t \in I)$  和  $(Y_{t} : t \in I)$  有相同的有限维分布族, 则称它们为等价的. 两个等价的过程互称为实现.

显然, 若两个过程 $(X_{t}: t \in I)$ 和 $(Y_{t}: t \in I)$ 定义在同一概率空间上, 且互为修正, 则它们一定是等价的; 但反之未必成立.

例 1.1.6 设随机变量  $\xi$  服从正态分布  $N(0,1)$ . 对任何  $t \geqslant 0$  令  $x(t) = \xi$  和  $y(t) = -\xi$ , 则  $\{x(t): t \geqslant 0\}$  与  $\{y(t): t \geqslant 0\}$  等价, 但不互为修正.

对于指标集  $I = Z_{+}$ ，可将状态空间  $E = R$  上的随机过程  $X = (X_{t}: t \in I)$  等同于无穷维随机向量  $(X_{0}, X_{1}, X_{2}, \cdots)$ 。此时 X 在可数维乘积可测空间  $(E^{I}, \mathcal{E}^{I}) := (\mathbb{R}^{\infty}, \mathcal{B}^{\infty})$  上的概率分布  $\mu_{X}$  定义为

$$
\mu_ {X} (A) = \mathbf {P} (X \in A), \quad A \in \mathscr {B} ^ {\infty}.
$$

应用测度论中的测度扩张定理可以证明, 过程 $X = (X_{t}: t \in I)$ 和 $Y = (Y_{t}: t \in I)$ 等价当且仅当它们在 $(\mathbb{R}^{\infty}, \mathcal{B}^{\infty})$ 上有相同的概率分布. 对于 $I$ 是一般指标集的情况, 令 $E^{I}$ 为由 $I$ 到 $E$ 的所有映射 $w = \{w(t): t \in I\}$ 构成的集合, 再令 $\mathscr{E}^{I}$ 为 $E^{I}$ 上由所有函数类 $\{w \mapsto w(t): t \in I\}$ 生成的 $\sigma$ 代数. 则随机过程 $X = (X_{t}: t \in I)$ 可视为取值于 $(E^{I}, \mathscr{E}^{I})$ 的随机变量.

## 1.1.4 左极右连修正和实现

设 $t \mapsto X(t)$ 是定义在某个集合 $D \subset [0, \infty)$ 上的实数值函数. 给定 $a < b \in \mathbb{R}$, 我们定义该函数对区间 $[a, b]$ 的上穿次数如下:

$$
U _ {D} ^ {X} [ a, b ] = \sup \left\{k \geqslant 0: \text {存在} s _ {1} <   t _ {1} <   s _ {2} <   t _ {2} <   \dots <   s _ {k} <   t _ {k} \in D \right.
$$

$$
\text {使对} 1 \leqslant i \leqslant k \text {有} X (s _ {i}) \leqslant a \text {和} X (t _ {i}) \geqslant b \}. \tag {1.1.2}
$$

令 $\mathbb{Q}$ 表示有理数集.

引理 1.1.3 设 D 在  $[0, \infty)$  中稠密，则函数  $t \mapsto X(t)$  在  $[0, \infty)$  上每点处沿 D 的左右极限存在当且仅当对任意的 K > 0 和  $a < b \in Q$  该函数在  $D_{K} := D \cap [0, K]$  上有界且上穿次数  $U_{D_{K}}^{X}[a, b]$  有限.

---

6

第一章 基本概念和例子

证明 假若 $t \mapsto X(t)$ 在某点 $t_0 \geqslant 0$ 处的右极限不存在, 则有 $\limsup_{D \ni t \Downarrow t_0} |X(t)| = \infty$ 或者 $\liminf_{D \ni t \Downarrow t_0} X(t) < \limsup_{D \ni t \Downarrow t_0} X(t)$, 其中 $t \Downarrow t_0$ 表示 $t > t_0$ 且 $t \downarrow t_0$. 在第一种情况下, 令 $K = t_0 + 1$, 则显然 $t \mapsto X(t)$ 在 $D_K$ 上无界. 在第二种情况下, 可取 $a, b \in \mathbb{Q}$ 满足

$$
\operatorname * {l i m i n f} _ {D \ni t \Downarrow t _ {0}} X (t) <   a <   b <   \operatorname * {l i m s u p} _ {D \ni t \Downarrow t _ {0}} X (t).
$$

此时令 $K = t_0 + 1$，则有 $U_{D_K}^X[a, b] = \infty$。类似地，假若 $t \mapsto X(t)$ 在某点 $t_0 > 0$ 处的左极限不存在，令 $K = t_0$，则可推出 $t \mapsto X(t)$ 在 $D_K$ 上无界或者 $U_{D_K}^X[a, b] = \infty$。根据上面的推导和反证法可知，若对任意的 $K > 0$ 和 $a < b \in \mathbb{Q}$ 函数 $t \mapsto X(t)$ 在 $D_K$ 上有界且 $U_{D_K}^X[a, b]$ 有限，则该函数在 $[0, \infty)$ 上每点处沿 $D$ 的左右极限存在。反之，假设对 $K > 0$ 和 $a < b \in \mathbb{Q}$ 函数 $t \mapsto X(t)$ 在 $D_K$ 上无界或者 $U_{D_K}^X[a, b]$ 无限。在第一种情况下，对每个 $n \geqslant 1$ 可取 $t_n \in D_K$ 使得 $|X(t_n)| \geqslant n$，再取子列 $\{t_{n_k}\} \subset \{t_n\}$ 使当 $k \to \infty$ 时 $t_{n_k} \to$ 某个 $t_0 \in [0, K]$。此时显然 $t \mapsto X(t)$ 在 $t_0$ 处沿 $D$ 的左极限或右极限不存在。在第二种情况下，有 $U_{D_K}^X[a, b] = \infty$。此时可取 $[0, K]$ 的递降区间套 $I_1 \supset I_2 \supset \cdots$ 使对每个 $n \geqslant 1$ 有 $|I_{n+1}| = |I_n| / 2$ 且 $U_{D \cap I_n}^X[a, b] = \infty$，其中 $|I_n|$ 表示区间 $I_n$ 的长度。根据区间套原理，存在唯一的点 $t_0 \in \bigcap_{n=1}^{\infty} I_n \subset [0, K]$。显然 $t \mapsto X(t)$ 在 $t_0$ 处沿 $D$ 的左极限或右极限不存在。再根据反证法可知，若函数 $t \mapsto X(t)$ 在 $[0, \infty)$ 上每点处沿 $D$ 的左右极限存在，则对任意的 $K > 0$ 和 $a < b \in \mathbb{Q}$ 该函数在 $D_K := D \cap [0, K]$ 上有界且 $U_{D_K}^X[a, b]$ 有限。$\square$

定理 1.1.4 状态空间  $R^{d}$  上的随机过程  $(X_{t}: t \geqslant 0)$  有左极右连的修正当且仅当它有左极右连的实现.

证明 显然, 若  $(X_{t}: t \geqslant 0)$  有左极右连的修正, 它必然有左极右连的实现. 下面假定  $(X_{t}: t \geqslant 0)$  有左极右连的实现  $(\xi_{t}: t \geqslant 0)$ , 我们来证明  $(X_{t}: t \geqslant 0)$  有左极右连的修正. 显然, 我们只需考虑 d = 1 的情况. 取  $R_{+}$  的一个可数稠子集  $D = \{r_{1}, r_{2}, \cdots\}$  并对  $n \geqslant 1$  记  $D^{n} = \{r_{1}, r_{2}, \cdots, r_{n}\}$ . 对于 K > 0 记  $D_{K} = D \cap [0, a]$  和  $D_{K}^{n} = D^{n} \cap [0, K]$ . 注意

$$
\begin{array}{l} \mathbf {P} \Big \{\sup _ {t \in D _ {K}} | X _ {t} | = \infty \Big \} = \lim _ {k \to \infty} \mathbf {P} \Big \{\sup _ {t \in D _ {K}} | X _ {t} | > k \Big \} \\ = \lim _ {k \to \infty} \lim _ {n \to \infty} \mathbf {P} \Big \{\sup _ {t \in D _ {K} ^ {n}} | X _ {t} | > k \Big \}. \\ \end{array}
$$

显然, 将 $X_{t}$ 替换为 $\xi_{t}$ 上面的等式仍然成立. 由于 $(X_{t}: t \geqslant 0)$ 和 $(\xi_{t}: t \geqslant 0)$ 互为实现, 有限维随机向量 $(X_{t}: t \in D_{K}^{n})$ 和 $(\xi_{t}: t \in D_{K}^{n})$ 同分布. 又因为 $(\xi_{t}: t \geqslant 0)$ 左极右连, 由上式得

$$
\mathbf {P} \Bigl \{\sup _ {t \in D _ {K}} | X _ {t} | <   \infty \Bigr \} = 1 - \lim _ {k \to \infty} \lim _ {n \to \infty} \mathbf {P} \Bigl \{\sup _ {t \in D _ {K} ^ {n}} | \xi_ {t} | > k \Bigr \}
$$

---

1.1 基本概念

7

$$
= 1 - \mathbf {P} \Big \{\sup _ {t \in D _ {K}} | \xi_ {t} | = \infty \Big \} = 1, \tag {1.1.3}
$$

其中最后的等式用到了引理 1.1.3. 另一方面, 由 (1.1.2) 式不难看出, 对于任意的 $a < b \in \mathbb{R}$ 有 $U_{D_K^n}^X[a, b] \stackrel{\mathrm{d}}{=} U_{D_K^n}^\xi[a, b]$, 进而

$$
U _ {D _ {K}} ^ {X} [ a, b ] = \lim _ {n \to \infty} U _ {D _ {K} ^ {n}} ^ {X} [ a, b ] \stackrel {{\mathrm{d}}} {{=}} \lim _ {n \to \infty} U _ {D _ {K} ^ {n}} ^ {\xi} [ a, b ] = U _ {D _ {K}} ^ {\xi} [ a, b ].
$$

再因为 $(\xi_t: t \geqslant 0)$ 左极右连, 根据引理1.1.3有

$$
\mathbf {P} \big \{U _ {D _ {K}} ^ {X} [ a, b ] <   \infty \big \} = \mathbf {P} \big \{U _ {D _ {K}} ^ {\xi} [ a, b ] <   \infty \big \} = 1. \tag {1.1.4}
$$

现在令

$$
\Omega_ {\infty} = \bigcap_ {K = 1} ^ {\infty} \Big (\Big \{\sup _ {t \in D _ {K}} | X _ {t} | <   \infty \Big \} \cap \Omega_ {K} \Big),
$$

其中

$$
\Omega_ {K} = \bigcap_ {a, b \in \mathbb {Q}, a <   b} \left\{U _ {D _ {K}} ^ {X} [ a, b ] <   \infty \right\}.
$$

根据 (1.1.3) 式和 (1.1.4) 式有 $\mathbf{P}(\Omega_{\infty}) = 1$. 再由引理 1.1.3 知对 $\omega \in \Omega_{\infty}$ 和 $t \geqslant 0$ 极限 $Y_{t}(\omega) := \lim_{D \ni s \to t+} X_{s}(\omega)$ 存在, 而对 $\omega \in \Omega_{\infty}$ 和 $t > 0$ 极限 $Z_{t}(\omega) := \lim_{D \ni s \to t-} X_{s}(\omega)$ 存在. 取定 $x_{0} \in \mathbb{R}$, 对所有 $t \geqslant 0$ 和 $\omega \in \Omega \setminus \Omega_{\infty}$ 令 $Y_{t}(\omega) = x_{0}$. 显然 ($Y_{t}: t \geqslant 0$) 是左极右连过程且对 $t > 0$ 有 $Y_{t-} = Z_{t}$. 因为 ($X_{t}: t \geqslant 0$) 有左极右连的实现, 它必然随机右连续, 故对任何 $t \geqslant 0$ 可取 $\{s_{n}\} \subseteq D$ 满足 $s_{n} \downarrow t$ 且几乎必然 $X_{t} = \lim_{n \to \infty} X_{s_{n}}$. 因此几乎必然有 $Y_{t} = X_{t}$, 即 ($Y_{t}: t \geqslant 0$) 是 ($X_{t}: t \geqslant 0$) 的修正. □

定理 1.1.4 可以推广到状态空间为完备可分度量空间的随机过程, 详见 [24, p.415, Theorem A.7]. 该定理建立了随机过程的左极右连实现和左极右连修正的存在性的等价关系. 尽管这是一个颇为基本的结果, 我们没有在更早的文献中找到对其明确的阐述.

## 练习题

1. 设 $(X_{t}: t \geqslant 0)$ 是定义在概率空间 $(\Omega, \mathcal{F}, \mathbf{P})$ 上的随机过程。证明对于任意的 $s, t \geqslant 0$ 和 $\varepsilon > 0$ 有 $\{\rho(X_{s}, X_{t}) \geqslant \varepsilon\} \in \mathcal{F}$。
2. 令 $\mathcal{D}_X = \{\mu_J^X : J \in s(I)\}$ 是状态空间 $E = \mathbb{R}^d$ 上的随机过程 ($X_t : t \in I$) 的有限维分布族. 任取 $(s_1, s_2) \in s(I)$ 和 $J = (t_1, t_2, \cdots, t_n) \in s(I)$. 记 $K_1 = (s_1, s_2, t_1, t_2, \cdots, t_n) \in s(I)$ 和 $K_2 = (s_2, s_1, t_1, t_2, \cdots, t_n) \in s(I)$. 证明: 对于 $A_1, A_2 \in \mathscr{E}$ 和 $B \in \mathscr{E}^n$, 有

$$
\mu_ {K _ {1}} ^ {X} (A _ {1} \times A _ {2} \times B) = \mu_ {K _ {2}} ^ {X} (A _ {2} \times A _ {1} \times B)
$$

---

8

第一章 基本概念和例子

和

$$
\mu_ {K _ {1}} ^ {X} (E \times E \times B) = \mu_ {K _ {2}} ^ {X} (E \times E \times B) = \mu_ {J} ^ {X} (B).
$$

3. 证明例 1.1.4 中定义的随机过程  $(N_{t}: t \geqslant 0)$  和  $(X_{t}: t \geqslant 0)$  互为修正, 但不是无区别的.

提示: 利用强大数定律证明几乎必然地有  $\lim_{n\to\infty}S_{n}=\infty$ . 所以  $N_{t}$  和  $X_{t}$  的表达式实际上都是有限和.

4. 证明例 1.1.4 中定义的随机过程  $(N_{t}: t \geqslant 0)$  和  $(X_{t}: t \geqslant 0)$  随机连续.
5. 设 $(\Omega, \mathcal{F}, \mathbf{P})$ 为完备概率空间. 证明 $(\Omega, \mathcal{F}, \mathbf{P})$ 上的随机过程无区别当且仅当 $\mathbf{P}(X_t = Y_t$ 对一切 $t \in I$ 成立) = 1.
6. 设  $\{(X_{t}^{1}, X_{t}^{2}, \cdots, X_{t}^{d}): t \geqslant 0\}$  是 d 维随机过程. 证明: 若对于  $1 \leqslant i \leqslant d$  每个  $(X_{t}^{i}: t \geqslant 0)$  有修正  $(\xi_{t}^{i}: t \geqslant 0)$ , 则  $\{(\xi_{t}^{1}, \xi_{t}^{2}, \cdots, \xi_{t}^{d}): t \geqslant 0\}$  是  $\{(X_{t}^{1}, X_{t}^{2}, \cdots, X_{t}^{d}): t \geqslant 0\}$  的修正.

## 1.2 随机游动

随机游动是最简单和最早被研究的随机过程之一. 设 $\{\xi_n : n \geqslant 1\}$ 是独立同分布 $d$ 维随机变量序列, 而 $X_0$ 是与之独立的另一个 $d$ 维随机变量. 令

$$
X _ {n} = X _ {0} + \sum_ {i = 1} ^ {n} \xi_ {i}, \quad n \geqslant 1, \tag {1.2.1}
$$

称 $(X_{n}:n\geqslant 0)$ 为 $d$ 维随机游动, 并称 $\{\xi_n:n\geqslant 1\}$ 为其步长列.

例 1.2.1 令  $(X_{n}: n \geqslant 0)$  是 (1.2.1) 式定义的 d 维随机游动, 并记  $X_{n} = (X_{n}^{1}, X_{n}^{2}, \cdots, X_{n}^{d})$ . 对于正整数  $d_{1} \leqslant d$  令  $Y_{n} = (X_{n}^{1}, X_{n}^{2}, \cdots, X_{n}^{d_{1}})$ , 则  $(Y_{n}: n \geqslant 0)$  是  $d_{1}$  维随机游动.

在很多时候, 我们假定  $X_{0}$  和  $\{\xi_{n}: n \geqslant 1\}$  都是取值于 d 维整数格点空间  $Z^{d}$  的随机变量. 此时, 随机游动  $(X_{n}: n \geqslant 0)$  的状态空间可取为  $Z^{d}$ . 特别地, 若有  $\mathbf{P}(|\xi_{i}| = 1) = 1$ , 则称  $(X_{n}: n \geqslant 0)$  为 d 维简单随机游动. 令  $v_{1}, v_{2}, \cdots, v_{d}$  为  $Z^{d}$  中的 d 个单位向量. 若  $\mathbf{P}(\xi_{1} = \pm v_{k}) = 1/2d, k = 1, 2, \cdots, d$ , 则称  $(X_{n}: n \geqslant 0)$  为 d 维对称简单随机游动.

例 1.2.2 令  $(S_{n}: n \geqslant 0)$  为从原点出发的 d 维对称简单随机游动. 注意, 该游动只可能在偶数步以严格正概率返回原点. 特别地, 当 d = 1 时, 若由原点出发的游动在第 2n 步返回该点, 则它必有 n 步向左而另外 n 步向右运动. 所以

$$
\mathbf {P} (S _ {2 n} = 0) = \frac {1}{2 ^ {2 n}} \binom {2 n} {n} = \frac {1}{2 ^ {2 n}} \frac {(2 n) !}{(n !) ^ {2}}.
$$

---

1.2 随机游动

9

当 $d = 2$ 时, 若由原点出发的游动在第 $2n$ 步返回该点, 则必存在 $0 \leqslant k \leqslant n$ 使游动的运动为 $k$ 步向上, $k$ 步向下, $n - k$ 步向左, $n - k$ 步向右. 因此, 利用二项分布的卷积公式有

$$
\begin{array}{l} \mathbf {P} (S _ {2 n} = 0) = \frac {1}{4 ^ {2 n}} \sum_ {k = 0} ^ {n} \frac {(2 n) !}{(k !) ^ {2} [ (n - k) ! ] ^ {2}} = \frac {1}{4 ^ {2 n}} \frac {(2 n) !}{(n !) ^ {2}} \sum_ {k = 0} ^ {n} \mathrm{C} _ {k} ^ {n} \mathrm{C} _ {n - k} ^ {n} \\ = \frac {1}{4 ^ {2 n}} \frac {(2 n) !}{(n !) ^ {2}} \mathrm{C} _ {n} ^ {2 n} = \frac {1}{4 ^ {2 n}} \bigg (\frac {(2 n) !}{(n !) ^ {2}} \bigg) ^ {2}. \\ \end{array}
$$

当 d=3 时, 与上面的分析类似地有

$$
\begin{array}{l} \mathbf {P} (S _ {2 n} = 0) = \frac {1}{6 ^ {2 n}} \sum_ {i + j + k = n} \frac {(2 n) !}{(i ! j ! k !) ^ {2}} = \frac {1}{6 ^ {2 n}} \frac {(2 n) !}{(n !) ^ {2}} \sum_ {i + j + k = n} \left(\frac {n !}{i ! j ! k !}\right) ^ {2} \\ = \frac {1}{2 ^ {2 n}} \frac {(2 n) !}{(n !) ^ {2}} \sum_ {i + j + k = n} \left(\frac {1}{3 ^ {n}} \frac {n !}{i ! j ! k !}\right) ^ {2}. \\ \end{array}
$$

当  $d \geqslant 4$  时,  $\mathbf{P}(S_{2n} = 0)$  也有类似的表达式.

## 1.2.1 轨道的无界性

为了方便讨论, 我们考虑 $\mathbb{Z}$ 上的简单随机游动 $(S_{n}: n \geqslant 0)$. 其构造如下: 设 $\{\xi_{n}: n \geqslant 1\}$ 为独立同分布的随机变量序列, 且有

$$
\mathbf {P} (\xi_ {n} = 1) = p, \mathbf {P} (\xi_ {n} = - 1) = q, \tag {1.2.2}
$$

其中 $p, q \geqslant 0$ 且 $p + q = 1$. 令 $S_0$ 为取值于 $\mathbb{Z}$ 且与 $\{\xi_n : n \geqslant 1\}$ 独立的随机变量, 再令

$$
S _ {n} = S _ {0} + \sum_ {k = 1} ^ {n} \xi_ {k}, \quad n \geqslant 1, \tag {1.2.3}
$$

则 $(S_{n}:n\geqslant0)$ 是Z上的简单随机游动.

命题 1.2.1 简单随机游动 ( $S_{n}: n \geqslant 0$ ) 的轨道是几乎必然无界的, 即

$$
\mathbf {P} \Big \{\sup _ {n \geqslant 0} | S _ {n} | = \infty \Big \} = 1. \tag {1.2.4}
$$

证明 (1) 考虑 $p = q = 1/2$ 的情况. 此时 $(S_n)$ 是对称简单随机游动. 不妨设 $S_0 = 0$. 这样, 对任意的 $M, k \geqslant 1$ 有

$$
\mathbf {P} \Big \{\sup _ {n \geqslant 0} | S _ {n} | \leqslant M \Big \} \leqslant \mathbf {P} \{| S _ {k} | \leqslant M \} = \mathbf {P} \Bigg \{\left| \frac {S _ {k}}{\sqrt {k}} \right| \leqslant \frac {M}{\sqrt {k}} \Bigg \}. \tag {1.2.5}
$$

---

10

第一章 基本概念和例子

根据假设条件, 对每个  $i \geqslant 1$  有  $E\xi_{i} = 0$  和  $Var\xi_{i} = 1$ . 由中心极限定理, 当  $k \to \infty$  时随机变量

$$
\frac {S _ {k}}{\sqrt {k}} = \frac {1}{\sqrt {k}} \sum_ {i = 1} ^ {k} \xi_ {i}
$$

的分布弱收敛到标准正态分布. 所以当 $k \to \infty$ 时 (1.2.5) 式右端的概率趋于零, 故其左端的概率为零. 再由概率的次可加性知

$$
\begin{array}{l} \mathbf {P} \Big \{\sup _ {n \geqslant 0} | S _ {n} | <   \infty \Big \} = \mathbf {P} \Big (\bigcup_ {M = 1} ^ {\infty} \Big \{\sup _ {n \geqslant 0} | S _ {n} | \leqslant M \Big \} \Big) \\ = \sum_ {M = 1} ^ {\infty} \mathbf {P} \Big (\sup _ {n \geqslant 0} | S _ {n} | \leqslant M \Big) = 0, \\ \end{array}
$$

即 (1.2.4) 式成立.

(2) 考虑 $p \neq q$ 的情况. 此时由大数定律, 当 $n \to \infty$ 时几乎必然有 $S_{n} / n \to p - q \neq 0$, 故 $|S_{n}| \to \infty$, 进而 (1.2.4) 式成立. $\square$

## 1.2.2 首达时分布

定义 $(S_{n}:n\geqslant 0)$ 到位置 $x\in \mathbb{Z}$ 的首达时 $\tau_{x} = \inf \{n\geqslant 0:S_{n} = x\}$. 因为该游动每步只跳跃一个单位长度, 不难看出 $\tau_{x}\geqslant |x - S_{0}|$, 故几乎必然地

$$
\lim _ {| x | \to \infty} \tau_ {x} = \infty . \tag {1.2.6}
$$

下面设 $a \leqslant i \leqslant b \in \mathbb{Z}$, 并记 $\mathbf{P}_i = \mathbf{P}(\cdot | S_0 = i)$. 再令

$$
P _ {i} = \mathbf {P} _ {i} (\tau_ {b} <   \tau_ {a}), \quad Q _ {i} = \mathbf {P} _ {i} (\tau_ {a} <   \tau_ {b}),
$$

显然有 $P_{a} = 0$ 和 $Q_{a} = 1$. 另外, 由命题 1.2.1 知 $\mathbf{P}_i(\tau_a \wedge \tau_b < \infty) = 1$. 因此

$$
P _ {i} + Q _ {i} = 1, \quad a \leqslant i \leqslant b. \tag {1.2.7}
$$

令  $A_{1}=\{\xi_{1}=1\}$ . 由全概率公式,

$$
P _ {i} = \mathbf {P} _ {i} (A _ {1}) P _ {i + 1} + \mathbf {P} _ {i} (A _ {1} ^ {c}) P _ {i - 1} = p P _ {i + 1} + q P _ {i - 1},
$$

故有

$$
P _ {i + 1} - P _ {i} = \frac {q}{p} (P _ {i} - P _ {i - 1}), \quad a + 1 \leqslant i \leqslant b - 1. \tag {1.2.8}
$$

---

1.2 随机游动

11

定理 1.2.2 (1) 当 p = q = 1/2 时, 对  $a \leqslant i \leqslant b \in Z$  有

$$
\mathbf {P} _ {i} (\tau_ {b} <   \tau_ {a}) = \frac {i - a}{b - a}, \quad \mathbf {P} _ {i} (\tau_ {a} <   \tau_ {b}) = \frac {b - i}{b - a}. \tag {1.2.9}
$$

(2) 当 $p \neq q$ 时, 对 $a \leqslant i \leqslant b \in \mathbb{Z}$ 有

$$
\mathbf {P} _ {i} (\tau_ {b} <   \tau_ {a}) = \frac {1 - \left(\frac {q}{p}\right) ^ {i - a}}{1 - \left(\frac {q}{p}\right) ^ {b - a}}, \quad \mathbf {P} _ {i} (\tau_ {a} <   \tau_ {b}) = \frac {\left(\frac {q}{p}\right) ^ {i - a} - \left(\frac {q}{p}\right) ^ {b - a}}{1 - \left(\frac {q}{p}\right) ^ {b - a}}. \tag {1.2.10}
$$

证明 (1) 当 $p = q = 1 / 2$ 时, 由 (1.2.8) 式有 $P_{i+1} - P_i = P_i - P_{i-1}$, 即

$$
\{P _ {i}: i = a, a + 1, \dots , b - 1, b \}
$$

为等差数列.再由 $P_{a} = 0$ 和 $P_{b} = 1$ 得 $P_{i + 1} - P_{i} = 1 / (b - a)$ .利用(1.2.7)式即得(1.2.9)式.

(2) 当  $p \neq q$  时, 因  $P_{a} = 0$ , 由 (1.2.8) 式有

$$
\begin{array}{l} P _ {i} - P _ {i - 1} = \frac {q}{p} (P _ {i - 1} - P _ {i - 2}) = \dots \\ = \left(\frac {q}{p}\right) ^ {i - 1} (P _ {a + 1} - P _ {a}) = \left(\frac {q}{p}\right) ^ {i - 1} P _ {a + 1}. \\ \end{array}
$$

对上式求和得

$$
P _ {i} = \sum_ {k = a + 1} ^ {i} \left(\frac {q}{p}\right) ^ {k - a - 1} P _ {a + 1} = \sum_ {k = 1} ^ {i - a} \left(\frac {q}{p}\right) ^ {k - 1} P _ {a + 1} = \left[ \frac {1 - \left(\frac {q}{p}\right) ^ {i - a}}{1 - \frac {q}{p}} \right] P _ {a + 1}.
$$

因 $P_{b} = 1$ ，有

$$
P _ {a + 1} = \frac {1 - \frac {q}{p}}{1 - \left(\frac {q}{p}\right) ^ {b - a}}.
$$

再由 (1.2.7) 式即得 (1.2.10) 式. □

在定理 1.2.2 的结论的基础上, 可以容易地给出从固定位置出发的简单随机游动的首达时的分布. 这就是下面的:

推论 1.2.3 (1) 当  $p \geqslant q$  时, 对  $a \leqslant i \leqslant b \in Z$  有

$$
\mathbf {P} _ {i} (\tau_ {a} <   \infty) = \left(\frac {q}{p}\right) ^ {i - a}, \mathbf {P} _ {i} (\tau_ {b} <   \infty) = 1.
$$

(2) 当 $p \leqslant q$ 时, 对 $a \leqslant i \leqslant b \in \mathbb{Z}$ 有

$$
\mathbf {P} _ {i} (\tau_ {a} <   \infty) = 1, \mathbf {P} _ {i} (\tau_ {b} <   \infty) = \left(\frac {p}{q}\right) ^ {b - i}.
$$

---

12

第一章 基本概念和例子

证明 利用 (1.2.6) 式不难得到

$$
\mathbf {P} _ {i} (\tau_ {a} <   \infty) = \lim _ {b \to \infty} \mathbf {P} _ {i} (\tau_ {a} <   \tau_ {b}), \quad \mathbf {P} _ {i} (\tau_ {b} <   \infty) = \lim _ {a \to - \infty} \mathbf {P} _ {i} (\tau_ {b} <   \tau_ {a}).
$$

再由定理 1.2.1 即得 (1). 类似地可证 (2). □

## 练习题

1. 设 $(X_{n}: n \geqslant 0)$ 是简单随机游动. 证明 $(-X_{n}: n \geqslant 0)$ 也是简单随机游动.

2. 设 $\{(X_n, Y_n) : n \geqslant 0\}$ 是二维随机游动. 证明 $(X_n : n \geqslant 0)$ 和 $(Y_n : n \geqslant 0)$ 都是一维随机游动.

3. 设  $(S_{n})$  是由 (1.2.3) 式定义的一维简单随机游动.

(1) 证明对任意的  $n \geqslant 0$  和  $\{i_{0}, i_{1}, \cdots, i_{n}, j\} \subseteq Z$  有

$$
\mathbf {P} (X _ {n + 1} = j | X _ {k} = i _ {k}: 0 \leqslant k \leqslant n) = p 1 _ {\{j = i _ {n} + 1 \}} + q 1 _ {\{j = i _ {n} - 1 \}}.
$$

(2) 说明上面的条件概率与 $\mathbf{P}(X_{n+1} = j | X_n = i_n)$ 的关系并解释其原因.

4. 令 $(X_{n})$ 是由 (1.2.1) 式定义的 $d$ 维随机游动, 其中序列 $\{\xi_{n}\}$ 满足 $\mathbf{P}(|\xi_i| \geqslant 1) > 0$. 证明:

$$
\mathbf {P} \Big \{\sup _ {n \geqslant 0} | X _ {n} | = \infty \Big \} = 1.
$$

5. 令 $(S_{n})$ 是一维对称简单随机游动. 证明对于任何 $a \in \mathbb{Z}$ 该游动首次到达 $a$ 的时刻 $\tau_{a}$ 几乎必然有限.

## 1.3 布朗运动

布朗运动是英国植物学家布朗 (Robert Brown) 发现的一种自然现象. 布朗 1827 年发现漂浮在液体表面的花粉颗粒会无序地运动. 爱因斯坦 (Albert Einstein) 在 1905 年发表的论文 [11] 中指出, 花粉的运动是因为液体分子在各个方向撞击它们的缘故. 爱因斯坦还计算出了布朗运动增量的分布. 后来维纳 (Norbert Wiener) 在 1923 年的论文 [36] 中证明这种随机过程可以在连续轨道上实现, 因此布朗运动也称为维纳过程.

## 1.3.1 背景和定义

定义 1.3.1 假定 $\sigma^{2} \geqslant 0$ 为常数. 称具有连续轨道的实值过程 ($B_{t}: t \geqslant 0$) 是以 $\sigma^{2}$ 为参数的 (一维) 布朗运动, 是指它具有下面两个性质:

---

1.3 布朗运动

13

(1) 对任何 $0 \leqslant s \leqslant t$, 增量 $B_{t} - B_{s}$ 服从高斯分布 $N(0, \sigma^{2}(t - s))$, 即

$$
\mathrm{Ee} ^ {\mathrm{i} \theta (B _ {t} - B _ {s})} = \mathrm{e} ^ {- \sigma^ {2} (t - s) \theta^ {2} / 2}, \quad \theta \in \mathbb {R};
$$

(2) 对任何  $0 \leqslant t_{0} < t_{1} < \cdots < t_{n}$ ，随机变量  $B_{t_{0}}, B_{t_{1}} - B_{t_{0}}, \cdots, B_{t_{n}} - B_{t_{n-1}}$  相互独立.

特别地, 当  $\sigma^{2}=1$  时称  $(B_{t}:t\geqslant0)$  为标准布朗运动.

有限维分布为正态分布的随机过程称为正态过程. 根据定义 1.3.1, 若 $B_{0}$ 服从正态分布, 则布朗运动 $(B_{t}: t \geqslant 0)$ 是高斯过程. 显然, 若 $(B_{t}: t \geqslant 0)$ 是以 $\sigma^{2}$ 为参数的布朗运动, 则 $(-B_{t}: t \geqslant 0)$ 也是以 $\sigma^{2}$ 为参数的布朗运动. 布朗运动描述了微观粒子在理想介质中随机运动的速度随时间的变化情况. 下面的例子通过变尺度极限给出了该模型的直观解释.

例 1.3.1 设  $\{\xi_{k}: k \geqslant 1\}$  是独立同分布的零均值平方可积随机变量序列且  $\sigma^{2} := \mathbf{Var}(\xi_{k}) > 0$ . 记  $X(0) = 0$  和

$$
X (n) = \sum_ {k = 1} ^ {n} \xi_ {k}, \quad n \geqslant 1,
$$

则 $\{X(n): n \geqslant 0\}$ 是一个随机游动. 这里 $\xi_k$ 可以解释为粒子由于介质分子的第 $k$ 次撞击所产生的速度的增量, 而 $X(n)$ 代表粒子在受到介质分子的 $n$ 次撞击后的速度. 通常相对于粒子而言介质分子的质量非常小, 而单位时间内粒子受到介质分子撞击的次数非常多. 为了近似这种情况, 我们考虑变尺度过程:

$$
X _ {n} (t) = \frac {1}{\sqrt {n}} X (\lfloor n t \rfloor), \quad t \geqslant 0, \tag {1.3.1}
$$

其中 $\lfloor x\rfloor$ 表示不超过 $x\in \mathbb{R}$ 的最大整数, 则 $\{X_n(t):t\geqslant 0\}$ 为连续时间随机过程. 对于 $t > s\geqslant 0$ 有

$$
\begin{array}{l} X _ {n} (t) - X _ {n} (s) = \frac {1}{\sqrt {n}} \big [ X (\lfloor n t \rfloor) - X (\lfloor n s \rfloor) \big ] \\ = \frac {1}{\sqrt {n}} \bigg [ \sum_ {k = \lfloor n s \rfloor + 1} ^ {\lfloor n t \rfloor} \xi_ {k} \bigg ] = a _ {n} (s, t) Z _ {n} (s, t), \\ \end{array}
$$

其中

$$
a _ {n} (s, t) = \frac {\sigma}{\sqrt {n}} \sqrt {\lfloor n t \rfloor - \lfloor n s \rfloor},
$$

而

$$
Z _ {n} (s, t) = \frac {1}{\sigma \sqrt {\lfloor n t \rfloor - \lfloor n s \rfloor}} \sum_ {k = \lfloor n s \rfloor + 1} ^ {\lfloor n t \rfloor} \xi_ {k}.
$$

---

14

第一章 基本概念和例子

这里 $Z_{n}(s,t)$ 是 $\lfloor nt\rfloor -\lfloor ns\rfloor$ 个独立同分布随机变量的标准化部分和, 其中 $\lfloor nt\rfloor -\lfloor ns\rfloor \geqslant (t - s) / n - 1$. 根据林德伯格中心极限定理, 当 $n\to \infty$ 时 $Z_{n}(s,t)$ 依分布收敛到标准正态随机变量. 又因为

$$
\lim _ {n \to \infty} a _ {n} (s, t) = \sigma \sqrt {t - s},
$$

易知 $X_{n}(t) - X_{n}(s)$ 的分布弱收敛到正态分布 $N(0, \sigma^{2}(t - s))$. 另外, 对任何 $0 \leqslant t_{0} < t_{1} < \dots < t_{n}$, 利用 (1.3.1) 式可以证明随机变量 $X_{n}(t_{0}), X_{n}(t_{1}) - X_{n}(t_{0}), \dots, X_{n}(t_{n}) - X_{n}(t_{n-1})$ 相互独立. 据此不难证明 $\{X_{n}(t): t \geqslant 0\}$ 的任何有限维分布弱收敛到从原点出发的以 $\sigma^{2}$ 为参数的一维布朗运动的相应的有限维分布. 所以布朗运动近似地描述了粒子在介质中随机运动的速度的变化情况.

## 1.3.2 布朗运动的构造

在本小节中, 我们利用随机插值法给出布朗运动的严格构造, 说明前面定义的布朗运动在数学上是存在的. 注意, 若 $(B_{t}: t \geqslant 0)$ 是从原点出发的标准布朗运动, 对 $\sigma \geqslant 0$ 和 $x \in \mathbb{R}$ 记 $X_{t} = x + \sigma B_{t}$, 则 $(X_{t}: t \geqslant 0)$ 就是从 $x$ 出发且以 $\sigma^{2}$ 为参数的布朗运动. 因此, 我们只需讨论从原点出发的标准布朗运动的构造. 显然, 后者可以容易地转化为以 $[0,1]$ 为时间集的标准布朗运动的构造问题.

对 $n \geqslant 0$ 令 $I_{n}$ 为 0 和 $2^{n}$ 之间的奇数构成的集合. 例如 $I_{0} = I_{1} = \{1\}, I_{2} = \{1,3\}, I_{3} = \{1,3,5,7\}$. 再令 $C_{n} = \{k / 2^{n} : k = 0,1,\dots ,2^{n}\}$. 则对 $n \geqslant 1$ 有 $C_{n-1} \subseteq C_n$. 记 $C = \bigcup_{n=0}^{\infty} C_n$.

设 $\xi_{n,k}, n \geqslant 0, k \geqslant 1$ 是定义在某个概率空间 $(\Omega, \mathcal{F}, \mathbf{P})$ 上的可数个独立同分布标准正态随机变量. 对 $n \geqslant 0$ 令 $B(0) = 0$. 再令 $B_0(1) = \xi_{0,1}$. 设 $\{B(s): s \in C_{n-1}\}$ 已给定. 注意对 $k \in I_n$ 有 $(k \pm 1)/2^n \in C_{n-1}$. 令

$$
B \Big (\frac {k}{2 ^ {n}} \Big) = \frac {1}{2} \Big [ B \Big (\frac {k - 1}{2 ^ {n}} \Big) + B \Big (\frac {k + 1}{2 ^ {n}} \Big) \Big ] + \frac {\xi_ {n , k}}{2 ^ {(n + 1) / 2}}. \tag {1.3.2}
$$

这样, 就归纳地定义了零均值的正态过程 $\{B(s): s \in C\}$.

引理 1.3.1 对任何 $n \geqslant 0$, 离散时间正态过程 $\{B(s): s \in C_n\}$ 的单步增量

$$
B \Big (\frac {k}{2 ^ {n}} \Big) - B \Big (\frac {k - 1}{2 ^ {n}} \Big), \quad k = 1, 2, \dots , 2 ^ {n} \tag {1.3.3}
$$

是独立同分布的零均值正态随机变量且有方差 $1 / 2^n$

证明 显然, 欲证结论对离散时间正态过程 $\{B(s): s \in C_0\} = \{B(0), B(1)\}$ 成立. 假设正态过程 $\{B(s): s \in C_{n-1}\}$ 的单步增量是独立同分布的零均值正态随机变量且有方差 $1/2^{n-1}$. 对任何 $k \in I_n$ 由 (1.3.2) 式有

$$
B \Big (\frac {k}{2 ^ {n}} \Big) - B \Big (\frac {k - 1}{2 ^ {n}} \Big) = \frac {1}{2} \Big [ B \Big (\frac {k + 1}{2 ^ {n}} \Big) - B \Big (\frac {k - 1}{2 ^ {n}} \Big) \Big ] + \frac {\xi_ {n , k}}{2 ^ {(n + 1) / 2}} \tag {1.3.4}
$$

---

1.3 布朗运动

15

和

$$
B \Big (\frac {k + 1}{2 ^ {n}} \Big) - B \Big (\frac {k}{2 ^ {n}} \Big) = \frac {1}{2} \Big [ B \Big (\frac {k + 1}{2 ^ {n}} \Big) - B \Big (\frac {k - 1}{2 ^ {n}} \Big) \Big ] - \frac {\xi_ {n , k}}{2 ^ {(n + 1) / 2}}. \tag {1.3.5}
$$

注意 $(k\pm 1) / 2^{n}\in C_{n - 1}$ ，而 $\xi_{n,k}$ 与 $\{B(s):s\in C_{n - 1}\}$ 独立.由(1.3.4)式，(1.3.5)式和归纳假设有

$$
\begin{array}{l} \mathbf {E} \Big \{\Big [ B \Big (\frac {k}{2 ^ {n}} \Big) - B \Big (\frac {k - 1}{2 ^ {n}} \Big) \Big ] ^ {2} \Big \} \\ = \mathbf {E} \Bigl \{\left[ B \Bigl (\frac {k + 1}{2 ^ {n}} \Bigr) - B \Bigl (\frac {k}{2 ^ {n}} \Bigr) \right] ^ {2} \Bigr \} \\ = \frac {1}{2 ^ {2}} \mathbf {E} \Big \{\left[ B \Big (\frac {k + 1}{2 ^ {n}} \Big) - B \Big (\frac {k - 1}{2 ^ {n}} \Big) \right] ^ {2} \Big \} + \mathbf {E} \Big [ \frac {\xi_ {n , k} ^ {2}}{2 ^ {n + 1}} \Big ] \\ = \frac {1}{2 ^ {2}} \frac {1}{2 ^ {n - 1}} + \frac {1}{2 ^ {n + 1}} = \frac {1}{2 ^ {n}}. \\ \end{array}
$$

所以 $B(k / 2^n) - B((k - 1) / 2^n)$ 和 $B((k + 1) / 2^n) - B(k / 2^n)$ 都是方差为 $1 / 2^n$ 正态随机变量. 这就证明了 (1.3.3) 式中的增量是同分布的正态随机变量. 类似地, 有

$$
\begin{array}{l} \mathbf {E} \Big \{\left[ B \Big (\frac {k}{2 ^ {n}} \Big) - B \Big (\frac {k - 1}{2 ^ {n}} \Big) \right] \Big [ B \Big (\frac {k + 1}{2 ^ {n}} \Big) - B \Big (\frac {k}{2 ^ {n}} \Big) \Big ] \Big \} \\ = \frac {1}{2 ^ {2}} \mathbf {E} \Big \{\left[ B \Big (\frac {k + 1}{2 ^ {n}} \Big) - B \Big (\frac {k - 1}{2 ^ {n}} \Big) \right] ^ {2} \Big \} - \mathbf {E} \Big [ \frac {\xi_ {n , k} ^ {2}}{2 ^ {n + 1}} \Big ] \\ = \frac {1}{2 ^ {2}} \frac {1}{2 ^ {n - 1}} - \frac {1}{2 ^ {n + 1}} = 0, \\ \end{array}
$$

因而 $B(k / 2^n) - B((k - 1) / 2^n)$ 与 $B((k + 1) / 2^n) - B(k / 2^n)$ 独立. 由归纳假设不难看出, 若 $j \in I_n$ 且 $j \neq k$, 则随机向量 $(B(j / 2^n) - B((j - 1) / 2^n), B((j + 1) / 2^n) - B(j / 2^n))$ 与 $(B(k / 2^n) - B((k - 1) / 2^n), B((k + 1) / 2^n) - B(k / 2^n))$ 独立. 所以 (1.3.3) 式中的正态随机变量相互独立. 根据数学归纳法, 引理结论对所有 $n \geqslant 0$ 成立. $\square$

现在, 对每个 $n \geqslant 0$, 基于 $\{B(s): s \in C_n\}$, 通过线性插值可以定义随机过程 $\{B_n(t): t \in [0,1]\}$. 令 $h_{0,1}(t) = 1$. 对 $n \geqslant 1$ 和 $k \in I_n$ 令

$$
h _ {n, k} (t) = 2 ^ {(n - 1) / 2} \big [ 1 _ {((k - 1) / 2 ^ {n}, k / 2 ^ {n})} (t) - 1 _ {(k / 2 ^ {n}, (k + 1) / 2 ^ {n})} (t) \big ].
$$

再对 $n \geqslant 0$ 和 $k \in I_n$ 定义函数

$$
S _ {n, k} (t) = \int_ {0} ^ {t} h _ {n, k} (s) \mathrm{d} s, \quad t \in [ 0, 1 ].
$$

该函数的图像的非零部分由底边为 $[(k - 1) / 2^n, (k + 1) / 2^n]$, 高度为 $1 / 2^{(n + 1) / 2}$ 的等腰三角形的两个腰构成. 不难看出, 对 $n \geqslant 0$ 和 $\omega \in \Omega$ 有

$$
B _ {n} (\omega , t) = \sum_ {m = 0} ^ {n} \sum_ {k \in I _ {m}} S _ {m, k} (t) \xi_ {m, k} (\omega), \quad t \in [ 0, 1 ]. \tag {1.3.6}
$$

---

16

第一章 基本概念和例子

引理 1.3.2 存在  $\Omega_{0} \in F$  满足  $\mathbf{P}(\Omega_{0}) = 1$  且对每个  $\omega \in \Omega_{0}$  当  $n \to \infty$  时  $\{B_{n}(t, \omega): t \in [0, 1]\}$  一致收敛到某个连续函数  $\{B(t, \omega): t \in [0, 1]\}$ .

证明 对 $n \geqslant 0$ 令 $X_{n} = \max_{k \in I_{n}} |\xi_{n,k}|$. 因为 $\xi_{n,k}$ 服从标准正态分布, 对任何 $c > 0$ 有

$$
\begin{array}{l} \mathbf {P} (| \xi_ {n, k} | > c) = \frac {\sqrt {2}}{\sqrt {\pi}} \int_ {c} ^ {\infty} \mathrm{e} ^ {- x ^ {2} / 2} \mathrm{d} x \\ \leqslant \frac {\sqrt {2}}{\sqrt {\pi}} \int_ {c} ^ {\infty} \frac {x}{c} \mathrm{e} ^ {- x ^ {2} / 2} \mathrm{d} x = \frac {\sqrt {2}}{c \sqrt {\pi}} \mathrm{e} ^ {- c ^ {2} / 2}, \\ \end{array}
$$

进而

$$
\begin{array}{l} \mathbf {P} (X _ {n} > n) = \mathbf {P} \Big (\bigcup_ {k \in I _ {n}} \{| \xi_ {n, k} | > n \} \Big) \\ \leqslant 2 ^ {n} \mathbf {P} (| \xi_ {n, 1} | > n) \leqslant \frac {2 ^ {n} \sqrt {2}}{n \sqrt {\pi}} \mathrm{e} ^ {- n ^ {2} / 2}. \\ \end{array}
$$

所以 $\sum_{n=0}^{\infty} \mathbf{P}(X_n > n) < \infty$. 令 $\Omega_0 = \bigcup_{k=1}^{\infty} \bigcap_{n=k}^{\infty} \{X_n \leqslant n\}$. 根据博雷尔-坎泰利引理有 $\mathbf{P}(\Omega_0) = 1$. 显然, 对每个 $\omega \in \Omega_0$ 存在整数 $k(\omega) \geqslant 1$ 使当 $n \geqslant k(\omega)$ 时 $X_n(\omega) \leqslant n$, 从而

$$
\begin{array}{l} \sum_ {n = k (\omega)} ^ {\infty} \sum_ {i \in I _ {n}} S _ {n, i} (t) | \xi_ {n, i} (\omega) | \leqslant \sum_ {n = k (\omega)} ^ {\infty} X _ {n} (\omega) \sum_ {i \in I _ {n}} S _ {n, i} (t) \\ \leqslant \sum_ {n = k (\omega)} ^ {\infty} n 2 ^ {- (n + 1) / 2} <   \infty , \\ \end{array}
$$

其中第二个不等号成立是由于函数 $S_{n,i}, i \in I_n$ 的支撑集不重叠. 所以 $\{B_n(t, \omega): t \in [0,1]\}$ 一致收敛到某个连续函数 $\{B(t, \omega): t \in [0,1]\}$. □

对于 $\omega \in \Omega \setminus \Omega_0$ 补充定义 $B(t,\omega) = 0, t \in [0,1]$. 这样我们就得到连续随机过程 $\{B(t): t \in [0,1]\}$.

定理 1.3.3 如上定义的连续随机过程  $\{B(t): t \in [0,1]\}$  是从原点出发的标准布朗运动.

证明 由 $\{B(t): t \in [0,1]\}$ 的构造, 对于 $n \geqslant 0$ 和 $t \in C_n$ 有 $B(t) = B_n(t)$ (a.s.). 根据引理 1.3.1 不难证明, 定义 1.3.1 中的两个性质对 $C_n$ 中的点 $s \leqslant t$ 和 $0 \leqslant t_0 < t_1 < \dots < t_n$ 成立. 对于 $s \leqslant t \in [0,1]$, 显然有 $s_n := \inf C_n \cap [s,1] \downarrow s$ 和 $t_n := \inf C_n \cap [t,1] \downarrow t$. 再由 $\{B(t): t \in [0,1]\}$ 的连续性有 $B(s) = \lim_{n \to \infty} B(s_n)$ 和 $B(t) = \lim_{n \to \infty} B(t_n)$ (a.s.). 根据控制收敛定理有

$$
\mathbf {E} \mathrm{e} ^ {\mathrm{i} \theta [ B (t) - B (s) ]} = \lim _ {n \to \infty} \mathbf {E} \mathrm{e} ^ {\mathrm{i} \theta [ B (t _ {n}) - B (s _ {n}) ]} = \lim _ {n \to \infty} \mathrm{e} ^ {- (t _ {n} - s _ {n}) \theta^ {2} / 2} = \mathrm{e} ^ {- (t - s) \theta^ {2} / 2}.
$$

---

1.3 布朗运动

17

所以定义 1.3.1 中的性质 (1) 对于  $s \leqslant t \in [0,1]$  成立. 类似地, 可以证明该定义中的性质 (2) 对于 [0,1] 中的  $0 \leqslant t_{0} < t_{1} < \cdots < t_{n}$  也成立. 所以  $\{B(t): t \in [0,1]\}$  是从原点出发的标准布朗运动. □

定义 1.3.2 令 $W = C_{\mathbb{R}}[0, \infty)$ 是所有连续实值函数 $w: [0, \infty) \to \mathbb{R}$ 构成的集合，而 $\mathcal{W}$ 是其上的坐标过程 $\{w(t): t \geqslant 0\}$ 生成的 $\sigma$ 代数。令 $Q$ 为从原点出发的标准布朗运动 $(B_t: t \geqslant 0)$ 在 $(W, \mathcal{W})$ 上的分布，则 $\{w(t): t \geqslant 0\}$ 是定义在概率空间 $(W, \mathcal{W}, Q)$ 上的从原点出发的标准布朗运动。我们称 $(W, \mathcal{W}, Q)$ 为维纳空间，而称 $Q$ 为维纳测度。

## 1.3.3 几个基本性质

布朗运动属于几类重要的随机过程的交集. 特别地, 运用高斯过程的语言, 可以给出对布朗运动的如下的刻画:

定理 1.3.4 从原点出发的零均值高斯过程  $(B_{t}: t \geqslant 0)$  是标准布朗运动当且仅当对任意的  $s, t \geqslant 0$  有  $\mathbf{E}(B_{t}B_{s}) = t \wedge s$ .

证明 若 $(B_{t}: t \geqslant 0)$ 是从原点出发的标准布朗运动, 易知它是中心化的高斯过程, 且对 $t \geqslant s \geqslant 0$ 有 $\mathbf{E}(B_t B_s) = \mathbf{E}[(B_t - B_s)B_s + B_s^2] = s$, 故对任意的 $s, t \geqslant 0$ 有 $\mathbf{E}(B_t B_s) = t \wedge s$. 反之, 假设 $(B_t: t \geqslant 0)$ 是从原点出发的中心化连续实值高斯过程, 且对任意的 $s, t \geqslant 0$ 有 $\mathbf{E}(B_t B_s) = t \wedge s$. 则对于 $t > s \geqslant r \geqslant 0$ 有 $\mathbf{E}[(B_t - B_s)^2] = t - s$ 和 $\mathbf{E}[B_r(B_t - B_s)] = 0$, 故 $B_t - B_s$ 服从高斯分布 $N(0, t - s)$ 且与 $B_r$ 独立. 由此易知 $(B_t: t \geqslant 0)$ 满足定义1.3.1中的两条性质. □

定理 1.3.5 设  $(B_{t}: t \geqslant 0)$  是定义在概率空间  $(\Omega, \mathcal{F}, \mathbf{P})$  上的标准布朗运动. 对  $t > r \geqslant 0$  和  $n \geqslant 1$ , 取区间  $[r, t] \subseteq R_{+}$  的划分

$$
\pi_ {n} := \{r = t _ {n, 0} <   t _ {n, 1} <   t _ {n, 2} <   \dots <   t _ {n, k _ {n}} = t \}
$$

使当 $n\to \infty$ 时有 $\delta_n\coloneqq \max_{i}|t_{n,i} - t_{n,i - 1}|\to 0.$ 则当 $n\to \infty$ 时，在 $L^2$ 收敛的意义下有

$$
\sum_ {i = 1} ^ {k _ {n}} (B _ {t _ {n, i}} - B _ {t _ {n, i - 1}}) ^ {2} \rightarrow t - r. \tag {1.3.7}
$$

证明 根据正态分布的矩的计算公式, 对  $t > s \geqslant 0$  有

$$
\begin{array}{l} \mathbf {E} \bigl \{[ (B _ {t} - B _ {s}) ^ {2} - (t - s) ] ^ {2} \bigr \} = \mathbf {E} \bigl [ (B _ {t} - B _ {s}) ^ {4} - 2 (t - s) (B _ {t} - B _ {s}) ^ {2} + (t - s) ^ {2} \bigr ] \\ = 3 (t - s) ^ {2} - 2 (t - s) ^ {2} + (t - s) ^ {2} = 2 (t - s) ^ {2}. \\ \end{array}
$$

另外, 对  $t_{2} > s_{2} \geqslant t_{1} > s_{1} \geqslant 0$ , 由独立增量性,

$$
\mathbf {E} \bigl \{\bigl [ (B _ {t _ {1}} - B _ {s _ {1}}) ^ {2} - (t _ {1} - s _ {1}) \bigr ] \bigl [ (B _ {t _ {2}} - B _ {s _ {2}}) ^ {2} - (t _ {2} - s _ {2}) \bigr ] \bigr \} = 0.
$$

---

18

第一章 基本概念和例子

针对划分 $\pi_{n}$ 记 $\Delta B_{t_{n,j}} = B_{t_{n,j}} - B_{t_{n,j-1}}$ 和 $\Delta t_{n,j} = t_{n,j} - t_{n,j-1}$. 根据上面的分析, 计算得到

$$
\begin{array}{l} \mathbf {E} \Bigl \{\left[ \sum_ {j = 1} ^ {k _ {n}} (\Delta B _ {t _ {n, j}}) ^ {2} - (t - s) \right] ^ {2} \Bigr \} = \mathbf {E} \Bigl \{\left[ \sum_ {j = 1} ^ {k _ {n}} \bigl ((\Delta B _ {t _ {n, j}}) ^ {2} - \Delta t _ {n, j} \bigr) \right] ^ {2} \Bigr \} \\ = \sum_ {j = 1} ^ {k _ {n}} \mathbf {E} \bigl \{[ (\Delta B _ {t _ {n, j}}) ^ {2} - \Delta t _ {n, j} ] ^ {2} \bigr \} \\ = \sum_ {j = 1} ^ {k _ {n}} 2 (\Delta t _ {n, i}) ^ {2} \leqslant 2 (t - s) \delta_ {n}. \\ \end{array}
$$

因此当 $n\to \infty$ 时在 $L^2$ 收敛意义下有(1.3.7)式成立. □

推论 1.3.6 存在  $\Omega_{0} \in F$  满足  $\mathbf{P}(\Omega_{0}) = 1$  且对  $\omega \in \Omega_{0}$  轨道  $t \mapsto B_{t}(\omega)$  在  $R_{+}$  的任何长度非零的区间上都有无限变差.

证明 根据定理 1.3.5, 存在  $\{\pi_{n}\}$  的某个子列, 仍然记为  $\{\pi_{n}\}$ , 使当  $n \to \infty$  时几乎必然地有

$$
\sum_ {i = 1} ^ {k _ {n}} (B _ {t _ {n, i}} - B _ {t _ {n, i - 1}}) ^ {2} \rightarrow t - r > 0.
$$

因 $(B_{t}:t\geqslant 0)$ 连续，使上式成立的轨道 $s\mapsto B_s(\omega)$ 在 $[r,t]$ 上有无限变差，故可取$\Omega_{r,t}\in \mathcal{F}$ 满足 $\mathbf{P}(\Omega_{r,t}) = 1$ 且对 $\omega \in \Omega_{r,t}$ 轨道 $s\mapsto B_s(\omega)$ 在 $[r,t]$ 上有有界无限变差.再令

$$
\Omega_ {0} = \bigcap_ {r, t \in \mathbb {Q}, 0 \leqslant r <   t} \Omega_ {r, t} \in \mathscr {F},
$$

其中 $\mathbb{Q}$ 表示有理数集. 则 $\mathbf{P}(\Omega_0) = 1$ 且对 $\omega \in \Omega_0$ 轨道 $s \mapsto B_s(\omega)$ 在任何长度非零的区间上都有无限变差. $\square$

根据推论 1.3.6 易知, 几乎必然地布朗运动的轨道处处不可导.

## 练习题

1. 设 $(B_{t}: t \geqslant 0)$ 是标准布朗运动. 证明对任何 $r \geqslant 0$ 随机过程 $(B_{t + r} - B_{r}: t \geqslant 0)$ 是从0出发的标准布朗运动.
2. 设 $(B_{t}: t \geqslant 0)$ 是从原点出发的标准布朗运动。证明对任何 $c > 0$ 随机过程 $(cB_{t/c^2}: t \geqslant 0)$ 也是从原点出发的标准布朗运动。
3. 设 $(X_{t}: t \geqslant 0)$ 和 $(Y_{t}: t \geqslant 0)$ 是相互独立的标准布朗运动, 而 $\alpha, \beta \in \mathbb{R}$ 为常数. 证明 $(\alpha X_{t} + \beta Y_{t}: t \geqslant 0)$ 是以 $\alpha^{2} + \beta^{2}$ 为参数的布朗运动.

---

1.4 泊松过程

19

4. 设 $(B_{t}: t \geqslant 0)$ 是从原点出发的标准布朗运动. 定义 $X_{0} = 0$ 和 $X_{t} = tB_{1 / t}$. 根据重对数率, 几乎必然有

$$
\operatorname * {l i m s u p} _ {t \to \infty} \frac {B (t)}{\sqrt {2 t \ln \ln t}} = 1.
$$

基于上面结论证明  $(X_{t}: t \geqslant 0)$  也是从原点出发的标准布朗运动.

## 1.4 泊松过程

令 $(N_{t}:t\geqslant 0)$ 是参数为 $\alpha \geqslant 0$ 的泊松过程. 我们知道, 它是一个不降的左极右连非负整数值随机过程, 且具有如下两个性质:

(1) 对任何 $s, t \geqslant 0$, 增量 $N_{s+t} - N_s$ 服从参数为 $\alpha t$ 的泊松分布, 即

$$
\mathbf {P} (N _ {s + t} - N _ {s} = k) = \frac {\alpha^ {k} t ^ {k}}{k !} \mathrm{e} ^ {- \alpha t}, \quad k = 0, 1, 2, \dots ; \tag {1.4.1}
$$

(2) 对任何  $0 \leqslant t_{0} < t_{1} < \cdots < t_{n}$ ，随机变量  $N_{t_{0}}, N_{t_{1}} - N_{t_{0}}, \cdots, N_{t_{n}} - N_{t_{n-1}}$  相互独立.

这里, 我们只假定  $(N_{t}: t \geqslant 0)$  具有上面两个性质, 而不要求  $N_{0} = 0$ .

## 1.4.1 跳跃间隔时间

给定参数为 $\alpha \geqslant 0$ 的泊松过程 $(N_{t}:t\geqslant 0)$, 记 $S_0 = 0$ 并对 $n\geqslant 1$ 令 $S_{n} = \inf \{t\geqslant 0:N_{t} - N_{0}\geqslant n\}$ 和 $\eta_{n} = S_{n} - S_{n - 1}$. 直观上 $S_{n}$ 是 $(N_{t}:t\geqslant 0)$ 的第 $n$ 次跳跃的等待时间, 而 $\eta_{n}$ 是它由第 $n - 1$ 次到第 $n$ 次的跳跃间隔时间.

定理 1.4.1 随机变量  $\eta_{n}, n \geqslant 1$  相互独立且同服从参数为  $\alpha$  的指数分布.

证明 首先计算随机向量  $(S_{1}, S_{2}, \cdots, S_{n})$  的分布. 该随机向量的状态空间为

$$
H _ {n} := \{(x _ {1}, x _ {2}, \dots , x _ {n}) \in \mathbb {R} ^ {n}: 0 <   x _ {1} <   x _ {2} <   \dots <   x _ {n} \}.
$$

对 $0 = t_0 < r_1 < t_1 < r_2 < t_2 < \dots < r_n < t_n$，根据独立增量性有

$$
\begin{array}{l} \mathbf {P} \big (r _ {i} <   S _ {i} \leqslant t _ {i}, i = 1, \dots , n \big) \\ = \mathbf {P} \big (\{N _ {r _ {1}} - N _ {t _ {0}} = \dots = N _ {r _ {n}} - N _ {t _ {n - 1}} = 0 \} \cap \\ \{N _ {t _ {1}} - N _ {r _ {1}} = \dots = N _ {t _ {n - 1}} - N _ {r _ {n - 1}} = 1 \} \cap \\ \left. \left\{N _ {t _ {n}} - N _ {r _ {n}} \geqslant 1 \right\}\right) \\ \end{array}
$$

---

20

第一章 基本概念和例子

$$
\begin{array}{l} = \prod_ {i = 1} ^ {n} \mathrm{e} ^ {- \alpha (r _ {i} - t _ {i - 1})} \cdot \prod_ {i = 1} ^ {n - 1} \alpha (t _ {i} - r _ {i}) \mathrm{e} ^ {- \alpha (t _ {i} - r _ {i})} \cdot (1 - \mathrm{e} ^ {- \alpha (t _ {n} - r _ {n})}) \\ = \mathrm{e} ^ {- \alpha (r _ {n} - t _ {n - 1})} \cdot \prod_ {i = 1} ^ {n - 1} \mathrm{e} ^ {- \alpha (t _ {i} - t _ {i - 1})} \cdot \prod_ {i = 1} ^ {n - 1} \alpha (t _ {i} - r _ {i}) \cdot (1 - \mathrm{e} ^ {- \alpha (t _ {n} - r _ {n})}) \\ = \mathrm{e} ^ {- \alpha (r _ {n} - t _ {0})} \cdot \prod_ {i = 1} ^ {n - 1} \alpha (t _ {i} - r _ {i}) \cdot (1 - \mathrm{e} ^ {- \alpha (t _ {n} - r _ {n})}) \\ = \prod_ {i = 1} ^ {n - 1} \alpha (t _ {i} - r _ {i}) \cdot (\mathrm{e} ^ {- \alpha r _ {n}} - \mathrm{e} ^ {- \alpha t _ {n}}) \\ = \alpha^ {n - 1} \int_ {r _ {1}} ^ {t _ {1}} \mathrm{d} x _ {1} \int_ {r _ {2}} ^ {t _ {2}} \mathrm{d} x _ {2} \dots \int_ {r _ {n - 1}} ^ {t _ {n - 1}} \mathrm{d} x _ {n - 1} \int_ {r _ {n}} ^ {t _ {n}} \alpha \mathrm{e} ^ {- \alpha x _ {n}} \mathrm{d} x _ {n}. \\ \end{array}
$$

所以  $(S_{1}, S_{2}, \cdots, S_{n})$  有联合分布密度

$$
p (x _ {1}, x _ {2}, \dots , x _ {n}) := \alpha^ {n} \mathrm{e} ^ {- \alpha x _ {n}} 1 _ {H _ {n}} (x _ {1}, x _ {2}, \dots , x _ {n}). \tag {1.4.2}
$$

对于  $t_{1}>0, t_{2}>0, \cdots, t_{n}>0$  有

$$
\begin{array}{l} \mathbf {P} \big (\eta_ {1} > t _ {1}, \eta_ {2} > t _ {2}, \dots , \eta_ {n} > t _ {n} \big) \\ = \mathbf {P} \big (S _ {1} > t _ {1}, S _ {2} - S _ {1} > t _ {2}, \dots , S _ {n} - S _ {n - 1} > t _ {n} \big) \\ = \int_ {\{x _ {1} > t _ {1} \}} \mathrm{d} x _ {1} \dots \int_ {\{x _ {n - 1} - x _ {n - 2} > t _ {n - 1} \}} \mathrm{d} x _ {n - 1} \int_ {\{x _ {n} - x _ {n - 1} > t _ {n} \}} \alpha^ {n} \mathrm{e} ^ {- \alpha x _ {n}} \mathrm{d} x _ {n} \\ = \int_ {\{x _ {1} > t _ {1} \}} \mathrm{d} x _ {1} \dots \int_ {\{x _ {n - 1} - x _ {n - 2} > t _ {n - 1} \}} \alpha^ {n - 1} \mathrm{e} ^ {- \alpha x _ {n - 1}} \mathrm{d} x _ {n - 1} \cdot \mathrm{e} ^ {- \alpha t _ {n}} \\ = \dots = \prod_ {i = 1} ^ {n} \mathrm{e} ^ {- \alpha t _ {i}}, \\ \end{array}
$$

故 $\{\eta_n : n \geqslant 1\}$ 是独立同分布的随机变量序列, 且服从参数 $\alpha$ 的指数分布. $\square$

推论 1.4.2 随机变量  $S_{n}$  服从伽马分布  $\Gamma(\alpha, n)$ .

例 1.4.1 设  $(X_{n}: n \geqslant 0)$  是 (1.2.1) 式定义的 d 维随机游动, 而  $(N_{t}: t \geqslant 0)$  是以  $\alpha > 0$  为参数的泊松过程. 称随机过程  $(X_{N_{t}}: t \geqslant 0)$  为连续时间随机游动. 可见  $(X_{N_{t}}: t \geqslant 0)$  的每次的跳幅与  $(X_{n}: n \geqslant 0)$  相同, 只是跳跃的间隔时间由单位时间变为独立同分布的指数分布随机变量.

## 1.4.2 轨道的重构

直观上, 定理 1.4.1 中定义的随机变量 $S_{n}$ 就是泊松过程的第 $n$ 次跳跃时间, 而 $\eta_{n}$ 为第 $n - 1$ 次到第 $n$ 次的跳跃间隔时间. 由该定理知 $\{\eta_{n}: n \geqslant 1\}$ 是独立同分布的随机变量序列. 利用这个分布性质, 可以重构泊松过程轨道. 这就是下面的:

---

1.4 泊松过程

21

定理 1.4.3 设  $\{\eta_{n}: n \geqslant 1\}$  是独立同分布随机变量序列, 服从参数为  $\alpha > 0$  的指数分布. 令  $S_{0} = 0$  和  $S_{n} = \sum_{i=1}^{n} \eta_{i}$ . 对  $t \geqslant 0$  令

$$
N _ {t} = \sum_ {n = 1} ^ {\infty} 1 _ {\{S _ {n} \leqslant t \}} = \sup \{n \geqslant 0: S _ {n} \leqslant t \},
$$

则随机过程 $(N_{t}:t\geqslant0)$ 是参数为 $\alpha$ 的泊松过程.

证明 令 $H_{n} = \{(x_{1}, x_{2}, \cdots, x_{n}) \in \mathbb{R}^{n} : 0 < x_{1} < x_{2} < \cdots < x_{n}\}$. 对于 $0 = t_{0} < r_{1} < t_{1} < r_{2} < t_{2} < \cdots < r_{n} < t_{n}$, 我们有

$$
\begin{array}{l} \mathbf {P} \big (r _ {1} <   S _ {1} \leqslant t _ {1}, r _ {2} <   S _ {2} \leqslant t _ {2}, \dots , r _ {n - 1} <   S _ {n - 1} \leqslant t _ {n - 1}, r _ {n} <   S _ {n} \leqslant t _ {n} \big) \\ = \mathbf {P} \big (r _ {1} <   \eta_ {1} \leqslant t _ {1}, r _ {2} <   \eta_ {1} + \eta_ {2} \leqslant t _ {2}, \dots , r _ {n} <   \eta_ {1} + \eta_ {2} + \dots + \eta_ {n} \leqslant t _ {n} \big) \\ = \alpha^ {n} \int_ {\{r _ {1} <   y _ {1} \leqslant t _ {1} \}} \mathrm{e} ^ {- \alpha y _ {1}} \mathrm{d} y _ {1} \int_ {\{r _ {2} <   y _ {1} + y _ {2} \leqslant t _ {2} \}} \mathrm{e} ^ {- \alpha y _ {2}} \mathrm{d} y _ {2} \cdot \dots \\ \int_ {\{r _ {n - 1} <   y _ {1} + y _ {2} + \dots + y _ {n - 1} \leqslant t _ {n - 1} \}} \mathrm{e} ^ {- \alpha y _ {n - 1}} \mathrm{d} y _ {n - 1} \int_ {\{r _ {n} <   y _ {1} + y _ {2} + \dots + y _ {n} \leqslant t _ {n} \}} \mathrm{e} ^ {- \alpha y _ {n}} \mathrm{d} y _ {n} \\ = \alpha^ {n} \int_ {\{r _ {1} <   y _ {1} \leqslant t _ {1} \}} \mathrm{d} y _ {1} \int_ {\{r _ {2} <   y _ {1} + y _ {2} \leqslant t _ {2} \}} \mathrm{d} y _ {2} \dots \\ \int_ {\{r _ {n - 1} <   y _ {1} + y _ {2} + \dots + y _ {n - 1} \leqslant t _ {n - 1} \}} \mathrm{d} y _ {n - 1} \int_ {\{r _ {n} <   x _ {n} \leqslant t _ {n} \}} \mathrm{e} ^ {- \alpha x _ {n}} \mathrm{d} x _ {n} \\ = \alpha^ {n} \int_ {\{r _ {1} <   x _ {1} \leqslant t _ {1} \}} \mathrm{d} x _ {1} \dots \int_ {\{r _ {n - 1} <   x _ {n - 1} \leqslant t _ {n - 1} \}} \mathrm{d} x _ {n - 1} \int_ {\{r _ {n} <   x _ {n} \leqslant t _ {n} \}} \mathrm{e} ^ {- \alpha x _ {n}} \mathrm{d} x _ {n}, \\ \end{array}
$$

其中  $x_{k}=y_{1}+y_{2}+\cdots+y_{k}$ . 所以  $(S_{1},S_{2},\cdots,S_{n})$  有联合分布密度 (1.4.2). 这样, 对于  $1\leqslant i_{1}<i_{2}$  和  $0<a_{1}<b_{1}<a_{2}<b_{2}$  可算得

$$
\begin{array}{l} \mathbf {P} \big (a _ {1} <   S _ {i _ {1}} \leqslant b _ {1}, a _ {2} <   S _ {i _ {2}} \leqslant b _ {2} \big) \\ = \alpha^ {i _ {2}} \int_ {a _ {1}} ^ {b _ {1}} \mathrm{d} x _ {i _ {1}} \int_ {0} ^ {x _ {i _ {1}}} \mathrm{d} x _ {i _ {1} - 1} \dots \int_ {0} ^ {x _ {3}} \mathrm{d} x _ {2} \int_ {0} ^ {x _ {2}} \mathrm{d} x _ {1}. \\ \int_ {a _ {2}} ^ {b _ {2}} \mathrm{e} ^ {- \alpha x _ {i _ {2}}} \mathrm{d} x _ {i _ {2}} \int_ {x _ {i _ {1}}} ^ {x _ {i _ {2}}} \mathrm{d} x _ {i _ {2} - 1} \dots \int_ {x _ {i _ {1}}} ^ {x _ {i _ {1} + 2}} \mathrm{d} x _ {i _ {1} + 1} \\ = \alpha^ {i _ {2}} \int_ {a _ {1}} ^ {b _ {1}} \frac {x _ {i _ {1}} ^ {i _ {1} - 1}}{(i _ {1} - 1) !} \mathrm{d} x _ {i _ {1}} \int_ {a _ {2}} ^ {b _ {2}} \frac {(x _ {i _ {2}} - x _ {i _ {1}}) ^ {i _ {2} - i _ {1} - 1}}{(i _ {2} - i _ {1} - 1) !} \mathrm{e} ^ {- \alpha x _ {i _ {2}}} \mathrm{d} x _ {i _ {2}}, \\ \end{array}
$$

故 $(S_{i_{1}}, S_{i_{2}})$ 有联合分布密度

$$
q (y _ {1}, y _ {2}) := \frac {y _ {1} ^ {i _ {1} - 1}}{(i _ {1} - 1) !} \cdot \frac {(y _ {2} - y _ {1}) ^ {i _ {2} - i _ {1} - 1}}{(i _ {2} - i _ {1} - 1) !} \cdot \alpha^ {i _ {2}} \mathrm{e} ^ {- \alpha y _ {2}} 1 _ {H _ {2}} (y _ {1}, y _ {2}).
$$

对于  $1 \leqslant i_{1} < i_{2} < \cdots < i_{n}$ ，类似地可算出  $(S_{i_{1}}, S_{i_{2}}, \cdots, S_{i_{n}})$  的联合分布密度为

$$
q (y _ {1}, y _ {2}, \dots , y _ {n}) := \frac {y _ {1} ^ {i _ {1} - 1}}{(i _ {1} - 1) !} \cdot \frac {(y _ {2} - y _ {1}) ^ {i _ {2} - i _ {1} - 1}}{(i _ {2} - i _ {1} - 1) !} \cdot \frac {(y _ {3} - y _ {2}) ^ {i _ {3} - i _ {2} - 1}}{(i _ {3} - i _ {2} - 1) !} \dots
$$

---

22

第一章 基本概念和例子

$$
\frac {(y _ {n} - y _ {n - 1}) ^ {i _ {n} - i _ {n - 1} - 1}}{(i _ {n} - i _ {n - 1} - 1) !} \cdot \alpha^ {i _ {n}} \mathrm{e} ^ {- \alpha y _ {n}} 1 _ {H _ {n}} (y _ {1}, y _ {2}, \dots , y _ {n}).
$$

现在对于  $0 \leqslant t_{1} < t_{2} < \cdots < t_{n}$ ，应用上面的联合分布密度计算  $N_{t_{1}}, N_{t_{2}} - N_{t_{1}}, \cdots, N_{t_{n}} - N_{t_{n-1}}$  的联合分布。取正整数组  $k_{1}, k_{2}, \cdots, k_{n}$ 。特别地，对于 n = 2 的情况，有

$$
\begin{array}{l} \mathbf {P} \big (N _ {t _ {1}} = k _ {1}, N _ {t _ {2}} - N _ {t _ {1}} = k _ {2} \big) \\ = \mathbf {P} \big (N _ {t _ {1}} = k _ {1}, N _ {t _ {2}} = k _ {1} + k _ {2} \big) \\ = \mathbf {P} \big (S _ {k _ {1}} \leqslant t _ {1} <   S _ {k _ {1} + 1}, S _ {k _ {1} + k _ {2}} \leqslant t _ {2} <   S _ {k _ {1} + k _ {2} + 1} \big) \\ = \alpha^ {k _ {1} + k _ {2} + 1} \int_ {0} ^ {t _ {1}} \frac {x _ {1} ^ {k _ {1} - 1}}{(k _ {1} - 1) !} \mathrm{d} x _ {1} \int_ {t _ {1}} ^ {t _ {2}} \mathrm{d} y _ {1} \int_ {y _ {1}} ^ {t _ {2}} \frac {(x _ {2} - y _ {1}) ^ {k _ {2} - 2}}{(k _ {2} - 2) !} \mathrm{d} x _ {2} \int_ {t _ {2}} ^ {\infty} \mathrm{e} ^ {- \alpha y _ {2}} \mathrm{d} y _ {2} \\ = \alpha^ {k _ {1} + k _ {2}} \int_ {0} ^ {t _ {1}} \frac {x _ {1} ^ {k _ {1} - 1}}{(k _ {1} - 1) !} \mathrm{d} x _ {1} \int_ {t _ {1}} ^ {t _ {2}} \frac {(t _ {2} - y _ {1}) ^ {k _ {2} - 1}}{(k _ {2} - 1) !} \mathrm{d} y _ {1} \cdot \mathrm{e} ^ {- \alpha t _ {2}} \\ = \frac {\alpha^ {k _ {1}} t _ {1} ^ {k _ {1}}}{k _ {1} !} \mathrm{e} ^ {- \alpha t _ {1}} \cdot \frac {\alpha^ {k _ {2}} (t _ {2} - t _ {1}) ^ {k _ {2}}}{k _ {2} !} \mathrm{e} ^ {- \alpha (t _ {2} - t _ {1})}. \\ \end{array}
$$

对于一般情况, 写  $i_{m}=k_{1}+k_{2}+\cdots+k_{m}, m=1,2,\cdots,n.$  我们有

$$
\begin{array}{l} \mathbf {P} \big (N _ {t _ {1}} = k _ {1}, N _ {t _ {2}} - N _ {t _ {1}} = k _ {2}, \dots , N _ {t _ {n}} - N _ {t _ {n - 1}} = k _ {n} \big) \\ = \mathbf {P} \big (N _ {t _ {1}} = i _ {1}, N _ {t _ {2}} = i _ {2}, \dots , N _ {t _ {n}} = i _ {n} \big) \\ = \mathbf {P} \big (S _ {i _ {1}} \leqslant t _ {1} <   S _ {i _ {1} + 1}, S _ {i _ {2}} \leqslant t _ {2} <   S _ {i _ {2} + 1}, \dots , S _ {i _ {n}} \leqslant t _ {n} <   S _ {i _ {n} + 1} \big) \\ = \dots \\ = \frac {\alpha^ {k _ {1}} t _ {1} ^ {k _ {1}}}{k _ {1} !} \mathrm{e} ^ {- \alpha t _ {1}} \cdot \frac {\alpha^ {k _ {2}} (t _ {2} - t _ {1}) ^ {k _ {2}}}{k _ {2} !} \mathrm{e} ^ {- \alpha (t _ {2} - t _ {1})} \dots \frac {\alpha^ {k _ {n}} (t _ {n} - t _ {n - 1}) ^ {k _ {n}}}{k _ {n} !} \mathrm{e} ^ {- \alpha (t _ {n} - t _ {n - 1})}. \\ \end{array}
$$

这说明 $(N_{t}:t\geqslant0)$ 是参数为 $\alpha$ 的泊松过程. □

泊松过程在应用中经常出现. 例如, 泊松过程的取值 $N_{t}$ 常被视为某个服务系统在 $t \geqslant 0$ 时刻前接到的服务请求的次数, 而过程的第 $n$ 次跳跃发生的时间 $S_{n}$ 可理解为第 $n$ 次服务请求的时刻.

## 1.4.3 长时间极限行为

设 $(N_{t}:t\geqslant 0)$ 是以 $\alpha >0$ 为参数的泊松过程.本小节中我们讨论 $(N_{t}:t\geqslant 0)$ 的长时间极限行为.下面的定理给出了 $N_{t}$ 的强大数定律和中心极限定理.

定理 1.4.4 (强大数定律) 当  $t \rightarrow \infty$  时几乎必然地有  $N_{t}/t \rightarrow \alpha$ .

证明 记 $\xi_{k} := N_{k} - N_{k-1}$, 则 $\{\xi_{k}\}$ 是独立同分布随机变量序列且服从参数为 $\alpha$ 的泊松分布. 注意 $N_{n} = \sum_{k=1}^{n} \xi_{k}$ 且 $\mathbf{E}(\xi_{k}) = \mathbf{Var}(\xi_{k}) = \alpha$. 根据强大数定律, 当 $n \to \infty$

---

1.4 泊松过程

23

时几乎必然地有 $N_{n} / n\to \alpha$ .注意

$$
\frac {\lfloor t \rfloor}{t} \frac {N _ {\lfloor t \rfloor}}{\lfloor t \rfloor} \leqslant \frac {N _ {t}}{t} \leqslant \frac {\lfloor t \rfloor + 1}{t} \frac {N _ {\lfloor t \rfloor + 1}}{\lfloor t \rfloor + 1}.
$$

显然

$$
\lim _ {t \to \infty} \frac {\lfloor t \rfloor}{t} = \lim _ {t \to \infty} \frac {\lfloor t \rfloor + 1}{t} = 1.
$$

故当 $t\to \infty$ 时几乎必然地有 $N_{t} / t\rightarrow \alpha$ □

定理 1.4.5（中心极限定理） 对于任何  $x \in R$ ，当  $t \to \infty$  时有

$$
\mathrm{P} \Big (\frac {N _ {\alpha t} - \alpha t}{\sqrt {\alpha t}} \leqslant x \Big) \rightarrow \varPhi (x) := \frac {1}{\sqrt {2 \pi}} \int_ {- \infty} ^ {x} \mathrm{e} ^ {- y ^ {2} / 2} \mathrm{d} y. \tag {1.4.3}
$$

证明 令 $\{\xi_k\}$ 如定理1.4.4的证明中所定义. 根据中心极限定理, 当 $n \to \infty$ 时有

$$
\mathbf {P} \Big (\frac {N _ {n} - \alpha n}{\sqrt {\alpha n}} \leqslant x \Big) \rightarrow \varPhi (x). \tag {1.4.4}
$$

注意

$$
\frac {N _ {t} - \alpha t}{\sqrt {\alpha t}} = \frac {N _ {t} - N _ {t - \lfloor t \rfloor} - \alpha \lfloor t \rfloor}{\sqrt {\alpha t}} + \frac {N _ {t - \lfloor t \rfloor} - \alpha (t - \lfloor t \rfloor)}{\sqrt {\alpha t}},
$$

其中 $N_{t} - N_{t - \lfloor t\rfloor}$ 与 $N_{\lfloor t\rfloor}$ 同分布. 故由(1.4.4)式知当 $t\to \infty$ 时有

$$
\mathbf {P} \Big (\frac {N _ {t} - N _ {t - \lfloor t \rfloor} - \alpha \lfloor t \rfloor}{\sqrt {\alpha \lfloor t \rfloor}} \leqslant x \Big) = \mathbf {P} \Big (\frac {N _ {\lfloor t \rfloor} - \alpha \lfloor t \rfloor}{\sqrt {\alpha \lfloor t \rfloor}} \leqslant x \Big) \rightarrow \varPhi (x),
$$

进而

$$
\mathbf {P} \Big (\frac {N _ {t} - N _ {t - \lfloor t \rfloor} - \alpha \lfloor t \rfloor}{\sqrt {\alpha t}} \leqslant x \Big) \to \varPhi (x).
$$

再注意

$$
\Big | \frac {N _ {t - \lfloor t \rfloor} - \alpha (t - \lfloor t \rfloor)}{\sqrt {\alpha t}} \Big | \leqslant \frac {N _ {1} + \alpha}{\sqrt {\alpha t}} \stackrel {{\text {a.s.}}} {{\to}} 0, \quad t \to \infty .
$$

所以 (1.4.3) 式成立. □

推论 1.4.6 对于任何 s, x > 0, 当  $\lambda \rightarrow \infty$  时有

$$
\mathrm{e} ^ {- \lambda s} \sum_ {k \leqslant \lambda x} \frac {(\lambda s) ^ {k}}{k !} \rightarrow 1 _ {\{0 <   s <   x \}} + \frac {1}{2} 1 _ {\{s = x \}}.
$$

证明 设 $(N_{t}: t \geqslant 0)$ 是以 1 为参数的泊松过程. 则欲证结果等价于, 当 $\lambda \to \infty$ 时有

$$
\mathbf {P} (N _ {\lambda s} \leqslant \lambda x) = \mathbf {P} \bigg (\frac {N _ {\lambda s} - \lambda s}{\sqrt {\lambda s}} \leqslant \frac {\sqrt {\lambda} (x - s)}{\sqrt {s}} \bigg) \rightarrow 1 _ {\{0 \leqslant s <   x \}} + \frac {1}{2} 1 _ {\{s = x \}}.
$$

由定理 1.4.5 知上式成立. □

---

24

第一章 基本概念和例子

定理 1.4.7 设非负随机变量  $\xi$  有拉普拉斯变换 L, 则对任何 x > 0 有

$$
\lim _ {\lambda \to \infty} \sum_ {k \leqslant \lambda x} \frac {(- \lambda) ^ {k}}{k !} \frac {\mathrm{d} ^ {k}}{\mathrm{d} \lambda^ {k}} L (\lambda) = \mathbf {P} (\xi <   x) + \frac {1}{2} \mathbf {P} (\xi = x). \tag {1.4.5}
$$

证明 用 $F$ 表示 $\xi$ 的分布函数, 则对 $\lambda > 0$ 有

$$
\begin{array}{l} \sum_ {k \leqslant \lambda x} \frac {(- \lambda) ^ {k}}{k !} \frac {\mathrm{d} ^ {k}}{\mathrm{d} \lambda^ {k}} L (\lambda) = \sum_ {k \leqslant \lambda x} \frac {(- \lambda) ^ {k}}{k !} \int_ {0} ^ {\infty} (- y) ^ {k} \mathrm{e} ^ {- \lambda y} \mathrm{d} F (y) \\ = \int_ {0} ^ {\infty} \left[ \mathrm{e} ^ {- \lambda y} \sum_ {k \leqslant \lambda x} \frac {(\lambda y) ^ {k}}{k !} \right] \mathrm{d} F (y). \\ \end{array}
$$

根据推论 1.4.6, 并应用有界收敛定理即得欲证结果. □

我们称 (1.4.5) 式为非负随机变量的拉普拉斯变换的反演公式. 不难看出, 根据此公式可以由拉普拉斯变换唯一地确定其相应的概率分布函数.

## 1.4.4 复合泊松过程

令 $\mu$ 是 $\mathbb{R}$ 上的概率测度且 $\mu (\{0\}) = 0$. 设 $(N_{t}:t\geqslant 0)$ 是以 $\alpha \geqslant 0$ 为参数的零初值泊松过程, 而 $\{\xi_n:n\geqslant 1\}$ 是与之独立的随机变量序列且有相同的分布 $\mu$. 再设 $X_0$ 是与 $(N_{t})$ 和 $\{\xi_n\}$ 独立的随机变量. 令

$$
X _ {t} = X _ {0} + \sum_ {n = 1} ^ {N _ {t}} \xi_ {n}, \quad t \geqslant 0. \tag {1.4.6}
$$

我们称 $(X_{t}:t\geqslant0)$ 是以 $\alpha$ 为跳跃速率以 $\mu$ 为跳跃分布的复合泊松过程.

形象地说, 复合泊松过程是泊松过程与具有一般步长的随机游动的复合, 它的跳跃时间由某个泊松过程给出, 而跳跃幅度是独立同分布的随机变量.

定理 1.4.8 设  $(X_{t}: t \geqslant 0)$  是由 (1.4.6) 式定义的以  $\alpha$  为跳跃速率以  $\mu$  为跳跃分布的复合泊松过程. 则下面的性质成立:

(1) 对任意的 $s, t \geqslant 0$ 和 $\theta \in \mathbb{R}$ 有

$$
\mathrm{Ee} ^ {\mathrm{i} \theta (X _ {s + t} - X _ {s})} = \exp \Big \{t \int_ {\mathbb {R}} (\mathrm{e} ^ {\mathrm{i} \theta x} - 1) \mu (\mathrm{d} x) \Big \}; \tag {1.4.7}
$$

(2) 对任何  $0 \leqslant t_{0} < t_{1} < \cdots < t_{n}$ ，随机变量  $X_{t_{0}}, X_{t_{1}} - X_{t_{0}}, \cdots, X_{t_{n}} - X_{t_{n-1}}$  相互独立.

证明 根据全期望公式, 并利用  $(N_{t}: t \geqslant 0)$  与  $\{\xi_{n}: n \geqslant 1\}$  的独立性, 对于任意的  $s \geqslant 0$  和  $\theta_{1}, \theta_{2}, \cdots, \theta_{n} \in R$  有

$$
\mathbf {E} \exp \left\{\mathrm{i} \sum_ {j = 1} ^ {n} \theta_ {j} \xi_ {N _ {s} + j} \right\} = \sum_ {k = 0} ^ {\infty} \mathbf {P} (N _ {s} = k) \mathbf {E} \bigg (\exp \left\{\mathrm{i} \sum_ {j = 1} ^ {n} \theta_ {j} \xi_ {k + j} \right\} \Big | N _ {s} = k \bigg)
$$

---

1.4 泊松过程

25

$$
\begin{array}{l} = \sum_ {k = 0} ^ {\infty} \mathbf {P} (N _ {s} = k) \mathbf {E} \bigg (\exp \left\{\mathrm{i} \sum_ {j = 1} ^ {n} \theta_ {j} \xi_ {k + j} \right\} \bigg) \\ = \sum_ {k = 0} ^ {\infty} \mathbf {P} (N _ {s} = k) \prod_ {j = 1} ^ {n} \int_ {\mathbb {R}} \mathrm{e} ^ {\mathrm{i} \theta_ {j} x} \mu (\mathrm{d} x) \\ = \prod_ {j = 1} ^ {n} \int_ {\mathbb {R}} \mathrm{e} ^ {\mathrm{i} \theta_ {j} x} \mu (\mathrm{d} x), \\ \end{array}
$$

所以 $\{\xi_{N_s + n}:n\geqslant 1\}$ 是独立同分布随机变量序列且有分布 $\mu$ .再由(1.4.6)式有

$$
X _ {s + t} - X _ {s} = \sum_ {n = 1} ^ {N _ {s + t} - N _ {s}} \xi_ {N _ {s} + n}. \tag {1.4.8}
$$

易知 $(N_{s + t} - N_s:t\geqslant 0)$ 是以 $\alpha \geqslant 0$ 为参数的零初值泊松过程, 且与 $\{\xi_{N_s + n}:n\geqslant 1\}$ 独立. 因此, 在 $N_{s + t} - N_s = k$ 条件下, 上式右边为 $k$ 个以 $\mu$ 为分布的独立同分布随机变量之和. 再根据全期望公式有

$$
\begin{array}{l} \mathbf {E} \mathrm{e} ^ {\mathrm{i} \theta (X _ {s + t} - X _ {s})} = \mathbf {E} \exp \left\{\mathrm{i} \theta \sum_ {n = 1} ^ {N _ {s + t} - N _ {s}} \xi_ {N _ {s} + n} \right\} \\ = \mathrm{e} ^ {- \alpha t} \sum_ {k = 0} ^ {\infty} \frac {(\alpha t) ^ {k}}{k !} \left[ \int_ {\mathbb {R}} \mathrm{e} ^ {\mathrm{i} \theta x} \mu (\mathrm{d} x) \right] ^ {k} \\ = \exp \left\{t \int_ {\mathbb {R}} (\mathrm{e} ^ {\mathrm{i} \theta x} - 1) \mu (\mathrm{d} x) \right\}. \\ \end{array}
$$

即 (1.4.7) 式成立. 对任何  $0 \leqslant t_{0} < t_{1} < t_{2} < \cdots < t_{n}$  及实数  $\theta_{1}, \theta_{2}, \cdots, \theta_{n}$ ，利用形如 (1.4.8) 式的表达可以得到

$$
\mathbf {E} \exp \left\{\mathrm{i} \sum_ {k = 1} ^ {n} \theta_ {k} (X _ {t _ {k}} - X _ {t _ {k - 1}}) \right\} = \prod_ {k = 1} ^ {n} \mathbf {E} \exp \left\{\mathrm{i} \theta_ {k} (X _ {t _ {k}} - X _ {t _ {k - 1}}) \right\}.
$$

由随机向量的特征函数的性质知  $X_{t_{1}} - X_{t_{0}}, X_{t_{2}} - X_{t_{1}}, \cdots, X_{t_{n}} - X_{t_{n-1}}$  相互独立. 显然这些随机变量与  $X_{t_{0}} = X_{0} = \xi_{0}$  独立. □

例 1.4.2 在某保险公司的理赔业务中, 申请赔偿的顾客按照参数为 $\alpha > 0$ 的零初值泊松过程 $(N_{t}: t \geqslant 0)$ 到达, 而顾客申请赔偿的金额由独立同分布的非负随机变量序列 $\{\xi_{n}: n \geqslant 0\}$ 给出. 这样, 在时间段 $(0, t]$ 到来的顾客申请赔偿金额的总和 $X_{t}$ 就由 (1.4.6) 式给出, 而 $(X_{t}: t \geqslant 0)$ 是一个复合泊松过程. 则对任何 $x \geqslant 0$ 有

$$
\mathbf {P} (X _ {t} \geqslant x) = \mathrm{e} ^ {- \alpha t} \sum_ {k = 0} ^ {\infty} \frac {(\alpha t) ^ {k}}{k !} \mu^ {* k} [ x, \infty),
$$

其中 $\mu^{*k}$ 表示 $\mu$ 的 $k$ 重卷积. 对于足够小的概率值 $p (0 < p < 1)$, 由上式可确定出最小的 $x = x_{t}(p) \geqslant 0$ 使得 $\mathbf{P}(X_{t} \geqslant x) \leqslant p$. 这样只要准备额度为 $x_{t}(p)$ 的预备金, 在时间段 $(0, t]$ 出现赔偿金不足的概率就不会超过 $p$.

---

26

第一章 基本概念和例子

例 1.4.3 考虑某个服务站的工作情况. 设其顾客按照参数为  $\alpha > 0$  的零初值泊松过程 ( $N_{t}: t \geqslant 0$ ) 到达, 而顾客所需服务的工作量由独立同分布的非负随机变量序列  $\{\xi_{n}: n \geqslant 0\}$  给出. 令 ( $X_{t}: t \geqslant 0$ ) 是由 (1.4.6) 式定义的复合泊松过程, 则  $X_{t}$  表示在时间段 (0, t] 到来的顾客所需服务工作量的总和. 设服务站的工作效率为  $\beta > 0$ , 则其在时间段 (0, t] 能够提供的最大服务量为  $\beta t$ . 记  $Y_{t} = X_{t} - \beta t$ . 考虑到在等待顾客数量清零时服务器不提供服务, 可以发现 t 时刻等待的顾客所需服务的工作总量应为  $Z_{t} = Y_{t} - \inf_{0 \leqslant s \leqslant t} Y_{s}$ .

## 练习题

1. 设 $(N(t): t \geqslant 0)$ 是参数为 $\lambda > 0$ 的泊松过程。对 $t > s > 0$ 求条件概率 $\mathbf{P}(N(s) = k | N(t) = n)$。
2. 设  $(N_{t}: t \geqslant 0)$  是从零出发参数为  $\alpha > 0$  的泊松过程。对  $n \geqslant 1$  令  $S_{n} = \inf\{t \geqslant 0 : N_{t} \geqslant n\}$  是  $(N_{t}: t \geqslant 0)$  的第 n 次跳跃的等待时间。证明对于 t > 0 在给定  $\{N(t) = n\}$  之下  $(S_{1}, S_{2}, \cdots, S_{n})$  的联合条件概率分布密度为

$$
f (x _ {1}, x _ {2}, \dots , x _ {n}) = \left\{ \begin{array}{l l} n! / t ^ {n}, & 0 <   x _ {1} <   x _ {2} <   \dots <   x _ {n}, \\ 0, & \text {其他.} \end{array} \right.
$$

3. 对 t > 0 令  $(X_{1}, X_{2}, \cdots, X_{n})$  是服从均匀分布  $U(0, t)$  的独立随机变量序列. 再令  $(Z_{1}, Z_{2}, \cdots, Z_{n})$  是  $(X_{1}, X_{2}, \cdots, X_{n})$  的由小到大排列的顺序统计量. 证明  $(Z_{1}, Z_{2}, \cdots, Z_{n})$  具有上题中给出的概率分布密度.
4. 设 $(X_{t}: t \geqslant 0)$ 和 $(Y_{t}: t \geqslant 0)$ 分别是以 $\alpha > 0$ 和 $\beta > 0$ 为参数的泊松过程且二者相互独立. 证明 $(X_{t} + Y_{t}: t \geqslant 0)$ 是以 $\alpha + \beta$ 为参数的泊松过程.
5. 设 $(X_{n}: n \geqslant 0)$ 是离散时间一维随机游动, 而 $(X_{N_{t}}: t \geqslant 0)$ 是例1.4.1中定义的连续时间随机游动. 分别讨论二者的长时间极限行为.

## 1.5 泊松随机测度

## 1.5.1 定义和存在性

考虑可测空间 $(E, \mathcal{E})$。为具体起见，我们假定 $(E, \mathcal{E})$ 是某个有限维欧氏空间的博雷尔可测子空间，即 $E \in \mathcal{B}^d$ ($d \geqslant 1$) 且 $\mathcal{E} = E \cap \mathcal{B}^d$。设 $\mu$ 为 $(E, \mathcal{E})$ 上的 $\sigma$ 有限测度。

---

1.5 泊松随机测度

27

定义 1.5.1 称取值于  $\{0,1,2,\cdots,\infty\}$  的随机变量族  $X=\{X(B):B\in\mathcal{E}\}$  是以  $\mu$  为强度的整数值随机测度, 是指它满足下列条件:

(1) 若 $B \in \mathscr{E}$ 满足 $\mu(B) < \infty$, 则 $\mathbf{E}[X(B)] = \mu(B)$;
(2) 若  $B_{1}, B_{2}, \cdots \in E$  两两不相交, 则

$$
X \Big (\bigcup_ {k = 1} ^ {\infty} B _ {k} \Big) = \sum_ {k = 1} ^ {\infty} X (B _ {k}). \tag {1.5.1}
$$

定义 1.5.2 称  $(E, \mathcal{E})$  上的以  $\mu$  为强度的整数值随机测度是泊松随机测度, 是指它满足下列条件:

(1) 若 $B \in \mathscr{E}$ 满足 $\mu(B) < \infty$, 则 $X(B)$ 服从参数为 $\mu(B)$ 的泊松分布, 即

$$
\mathbf {P} (X (B) = k) = \frac {\mu (B) ^ {k}}{k !} \mathrm{e} ^ {- \mu (B)}, \quad k = 0, 1, 2, \dots ;
$$

(2) 若  $B_{1}, B_{2}, \cdots, B_{n} \in E$  两两不相交, 则  $X(B_{1}), X(B_{2}), \cdots, X(B_{n})$  相互独立.

根据泊松分布的性质, 若 $X$ 是以 $\mu$ 为强度的泊松随机测度且 $B \in \mathcal{E}$ 满足 $\mu(B) < \infty$, 则有

$$
\mathbf {E} [ X (B) ] = \mu (B), \quad \mathbf {V a r} [ X (B) ] = \mu (B). \tag {1.5.2}
$$

例 1.5.1 设  $E=\{1,2\}$ ，而  $\mu$  为 E 上的计数测度。再设  $\xi_{1},\xi_{2}$  和  $\xi_{3}$  是独立同分布随机变量，且均服从参数为 1 的泊松分布。令

$$
X (\{1 \}) = \xi_ {1}, X (\{2 \}) = \xi_ {2}, X (\{1, 2 \}) = \xi_ {1} + \xi_ {3},
$$

则 $X$ 满足定义 1.5.2 中的性质 (1) 和 (2). 但 (1.5.1) 式不成立, 故 $X$ 不是整数值随机测度.

定理 1.5.1 设 X 为  $(E, \mathcal{E})$  上的以  $\mu$  为强度的整数值随机测度, 则 X 是泊松随机测度的充要条件是对任意的  $\theta_{1}, \theta_{2}, \cdots, \theta_{n} \in R$  和两两不相交的  $B_{1}, B_{2}, \cdots, B_{n} \in E$  当  $\mu(B_{1}) < \infty, \mu(B_{2}) < \infty, \cdots, \mu(B_{n}) < \infty$  时有

$$
\mathbf {E} \exp \left\{\mathrm{i} \sum_ {k = 1} ^ {n} \theta_ {k} X (B _ {k}) \right\} = \exp \left\{\sum_ {k = 1} ^ {n} (\mathrm{e} ^ {\mathrm{i} \theta_ {k}} - 1) \mu (B _ {k}) \right\}. \tag {1.5.3}
$$

证明 只需注意 (1.5.3) 式成立当且仅当  $X(B_{1}), X(B_{2}), \cdots, X(B_{n})$  独立且分别服从参数为  $\mu(B_{1}), \mu(B_{2}), \cdots, \mu(B_{n})$  的泊松分布. □

定理 1.5.2 设  $\mu$  为非零有限测度. 令  $\eta$  是以  $\mu(E)$  为参数的泊松随机变量, 而  $\xi_{1}, \xi_{2}, \cdots$  是取值于  $(E, \mathcal{E})$  的随机变量且有相同的分布  $\mu(E)^{-1}\mu$ . 再设  $\eta, \xi_{1}, \xi_{2}, \cdots$  相互独立, 则  $X := \sum_{j=1}^{\eta} \delta_{\xi_{j}}$  是以  $\mu$  为强度的泊松随机测度.

---

28

第一章 基本概念和例子

证明 显然 X 满足 (1.5.1)式. 根据关于  $\eta, \xi_{1}, \xi_{2}, \cdots$  的分布和独立性的假定, 对于  $\theta_{1}, \theta_{2}, \cdots, \theta_{n} \in R$  和两两不交的  $B_{1}, B_{2}, \cdots, B_{n} \in E$  有

$$
\begin{array}{l} \mathbf {E} \exp \left\{\mathrm{i} \sum_ {k = 1} ^ {n} \theta_ {k} X (B _ {k}) \right\} = \sum_ {m = 0} ^ {\infty} \mathbf {P} (\eta = m) \mathbf {E} \exp \left\{\mathrm{i} \sum_ {j = 1} ^ {m} \sum_ {k = 1} ^ {n} \theta_ {k} \delta_ {\xi_ {j}} (B _ {k}) \right\} \\ = \sum_ {m = 0} ^ {\infty} \mathrm{e} ^ {- \mu (E)} \frac {\mu (E) ^ {m}}{m !} \mathbf {E} \exp \left\{\mathrm{i} \sum_ {j = 1} ^ {m} \sum_ {k = 1} ^ {n} \theta_ {k} 1 _ {B _ {k}} (\xi_ {j}) \right\} \\ = \sum_ {m = 0} ^ {\infty} \mathrm{e} ^ {- \mu (E)} \frac {1}{m !} \left[ \int_ {E} \exp \left\{\mathrm{i} \sum_ {k = 1} ^ {n} \theta_ {k} 1 _ {B _ {k}} (x) \right\} \mu (\mathrm{d} x) \right] ^ {m} \\ = \exp \left\{- \mu (E) + \int_ {E} \exp \left\{\mathrm{i} \sum_ {k = 1} ^ {n} \theta_ {k} 1 _ {B _ {k}} (x) \right\} \mu (\mathrm{d} x) \right\} \\ = \exp \left\{\int_ {E} \left(\exp \left\{\mathrm{i} \sum_ {k = 1} ^ {n} \theta_ {k} 1 _ {B _ {k}} (x) \right\} - 1\right) \mu (\mathrm{d} x) \right\} \\ = \exp \left\{\int_ {E} \sum_ {k = 1} ^ {n} (\mathrm{e} ^ {\mathrm{i} \theta_ {k}} - 1) 1 _ {B _ {k}} (x) \mu (\mathrm{d} x) \right\} \\ = \exp \left\{\sum_ {k = 1} ^ {n} (\mathrm{e} ^ {\mathrm{i} \theta_ {k}} - 1) \mu (B _ {k}) \right\}. \\ \end{array}
$$

由定理 1.5.1 知 X 是以  $\mu$  为强度的泊松随机测度. □

基于定理 1.5.1 和定理 1.5.2, 显然有下面的:

定理 1.5.3 设  $\mu$  是无限的  $\sigma$  有限测度, 而  $\{E_{k}\} \subseteq E$  是两两不相交集合列, 满足  $\bigcup_{k=1}^{\infty} E_{k} = E$  且对每个  $k \geqslant 1$  有  $0 < \mu(E_{k}) < \infty$  且. 令  $\mu_{k}$  为  $\mu$  在  $E_{k}$  上的限制, 即对任何  $B \in E$  有  $\mu_{k}(B) = \mu(B \cap E_{k})$ . 令  $\{X_{k}\}$  为 E 上的独立泊松随机测度列, 其中  $X_{k}$  有强度  $\mu_{k}$ . 对  $B \in E$  令  $X(B) = \sum_{k=1}^{\infty} X_{k}(B)$ . 则  $X = \{X(B) : B \in E\}$  是以  $\mu$  为强度的泊松随机测度.

## 1.5.2 积分和补偿的测度

设 $X$ 为定义在某个概率空间 $(\Omega, \mathcal{F}, \mathbf{P})$ 上以 $(E, \mathcal{E})$ 上的 $\sigma$ 有限测度 $\mu$ 为强度的整数值随机测度. 由 (1.5.1) 式知映射 $B \mapsto X(B)$ 的确是 $(E, \mathcal{E})$ 上的 $\sigma$ 有限测度. 因此可以考虑 $E$ 上的可测函数 $f$ 相对于 $X$ 的积分

$$
\int_ {E} f (x) X (\mathrm{d} x) = \int_ {E} f ^ {+} (x) X (\mathrm{d} x) - \int_ {E} f ^ {-} (x) X (\mathrm{d} x),
$$

其中 $f^{\pm}$ 分别表示 $f$ 的正负部. 这里当然需要假定上式右端的两个积分中至少有一个有限. 为简化记号, 我们将上面的积分记为 $X(f)$. 特别地, 当 $f$ 为 $\mu$ 可积函数时, 通过

---

1.5 泊松随机测度

29

简单函数逼近的方法易证

$$
\mathbf {E} [ X (f) ] = \mu (f). \tag {1.5.4}
$$

定理 1.5.2 给出了有限强度泊松随机测度 X 的具体构造或表示. 在这种情况下, 显然有

$$
X (f) = \sum_ {i = 1} ^ {\eta} f (\xi_ {i}).
$$

更一般地, 若 X 由定理 1.5.3 给出, 则 f 相对于 X 的积分可以表示为

$$
X (f) = \sum_ {k = 1} ^ {\infty} X _ {k} (f) = \sum_ {k = 1} ^ {\infty} X _ {k} (f ^ {+}) - \sum_ {k = 1} ^ {\infty} X _ {k} (f ^ {-}).
$$

这里要求上式右端的级数中至少有一个有限.

定理 1.5.4 设 X 为  $(E, \mathcal{E})$  上的以  $\sigma$  有限测度  $\mu$  为强度的整数值随机测度, 则 X 是泊松随机测度当且仅当对  $(E, \mathcal{E})$  上的任何  $\mu$  可积函数 f 有

$$
\mathrm{Ee} ^ {\mathrm{i} X (f)} = \exp \Big \{\int_ {E} (\mathrm{e} ^ {\mathrm{i} f (x)} - 1) \mu (\mathrm{d} x) \Big \}. \tag {1.5.5}
$$

证明 注意 $|\mathrm{e}^{\mathrm{i}f} - 1| \leqslant |f|$. 所以当 $f$ 为 $\mu$ 可积函数时 (1.5.5) 式右边关于 $\mu$ 的积分有限. 设 $X$ 为以 $\mu$ 为强度的泊松随机测度. 若 $B_1, B_2, \dots, B_n \in \mathcal{E}$ 两两不相交且 $\mu(B_1) < \infty$, $\mu(B_2) < \infty, \dots, \mu(B_n) < \infty$, 则 $X(B_1), X(B_2), \dots, X(B_n)$ 相互独立且分别服从参数为 $\mu(B_1), \mu(B_2), \dots, \mu(B_n)$ 的泊松分布. 因此对任何实数 $\theta_1, \theta_2, \dots, \theta_n$ (1.5.3) 式成立. 这说明 (1.5.5) 式对于 $\mu$ 可积的简单函数 $f = \sum_{k=1}^{n} \theta_k 1_{B_k}$ 成立. 利用简单函数列的逼近和控制收敛定理, 易证 (1.5.5) 式对于任何 $\mu$ 可积函数 $f$ 成立. 反之, 假设 (1.5.5) 式对任意的 $\mu$ 可积函数 $f \in \mathcal{E}$ 成立. 取 $B_1, B_2, \dots, B_n \in \mathcal{E}$ 两两不相交且满足 $\mu(B_1) < \infty, \mu(B_2) < \infty, \dots, \mu(B_n) < \infty$. 对于 $\mu$ 可积的简单函数 $f = \sum_{k=1}^{n} \theta_k 1_{B_k}$ 应用 (1.5.5) 式得 (1.5.3)式, 再由定理 1.5.1 即知 $X$ 是以 $\mu$ 为强度的泊松随机测度. □

定理 1.5.5 设  $\mu$  是  $(E, \mathcal{E})$  上的  $\sigma$  有限测度, 而  $\phi$  是由  $(E, \mathcal{E})$  到可测空间  $(F, \mathcal{F})$  的可测映射, 且像测度  $\mu \circ \phi^{-1}$  也是  $\sigma$  有限测度. 若 X 是以  $\mu$  为强度的泊松随机测度, 则像测度  $X \circ \phi^{-1}$  是以  $\mu \circ \phi^{-1}$  为强度的泊松随机测度.

证明 注意对 $(F, \mathcal{F})$ 上的任何 $\mu \circ \phi^{-1}$ 可积函数 $f$ 有 $\mu \circ \phi^{-1}(f) = \mu (\phi \circ f)$ 和 $X \circ \phi^{-1}(f) = X(\phi \circ f)$, 应用定理 1.5.4 即得结论. □

给定以 $\sigma$ 有限测度 $\mu$ 为强度的整数值随机测度 $X$, 其补偿的测度指的是随机的符号测度 $\tilde{X} := X - \mu$, 而 $E$ 上的函数 $f$ 关于该补偿的测度的积分自然定义为 $\tilde{X}(f) = X(f) - \mu(f)$, 该表达式对于任何 $\mu$ 可积函数 $f$ 有意义.

---

30

第一章 基本概念和例子

对于泊松随机测度 $X$, 关于其补偿的测度的积分可以做进一步的扩展. 设 $f$ 和 $f^2$ 都关于 $\mu$ 可积. 通过简单函数逼近的方法易证

$$
\mathbf {E} [ X (f) ^ {2} ] = \mu (f ^ {2}) + \mu (f) ^ {2}, \quad \mathbf {E} [ \tilde {X} (f) ^ {2} ] = \mu (f ^ {2}).
$$

对于一般的 $\mu$ 平方可积函数 $f$, 可取函数列 $\{f_n\}$, 其中每个 $f_n$ 关于 $\mu$ 可积且平方可积, 同时当 $n \to \infty$ 时有 $\mu(|f_n - f|^2) \to 0$. 这样 $\{f_n\}$ 就是 $L^2(\mu)$ 中的基本列, 即当 $m, n \to \infty$ 时有 $\mu(|f_m - f_n|^2) \to 0$. 注意

$$
\mathbf {E} [ | \tilde {X} (f _ {m}) - \tilde {X} (f _ {n}) | ^ {2} ] = \mu (| f _ {m} - f _ {n} | ^ {2}).
$$

因此随机变量序列 $\{\tilde{X}(f_n)\}$ 是 $L^2 (\mathbf{P})$ 中的基本列. 于是存在几乎必然意义下唯一的平方可积随机变量 $\tilde{X}(f)$ 使当 $n\to \infty$ 时有 $\mathbf{E}[|\tilde{X} (f_n) - \tilde{X} (f)|^2 ]\to 0.$ 我们称 $\tilde{X}(f)$ 为 $f$ 关于 $\tilde{X}$ 的积分. 由上式易得

$$
\mathbf {E} [ \tilde {X} (f) ^ {2} ] = \mu (f ^ {2}).
$$

## 1.5.3 随机测度的应用

随机测度在随机过程的研究中有很多重要的应用. 作为泊松随机测度的应用, 下面给出复合泊松过程的另外一种构造. 设 $\nu$ 是 $\mathbb{R}$ 上的非零有限测度且有 $\nu(\{0\}) = 0$. 设 $N(\mathrm{ds}, \mathrm{dz})$ 是 $(0, \infty) \times \mathbb{R}$ 上的以 $\mathrm{ds}\nu(\mathrm{dz})$ 为强度的泊松随机测度, 其中 $\mathrm{ds}$ 表示勒贝格测度, 而 $X_0$ 是与之独立的随机变量. 令

$$
X _ {t} = X _ {0} + \int_ {(0, t ]} \int_ {\mathbb {R}} z N (\mathrm{d} s, \mathrm{d} z), \quad t \geqslant 0. \tag {1.5.6}
$$

记 $N_{t} = N((0,t]\times \mathbb{R})$ ，由定义1.5.2中的性质，易知 $(N_{t})$ 是以 $\alpha := \nu (\mathbb{R})$ 为参数的泊松过程.

命题 1.5.6 令  $S = \inf\{t \geqslant 0 : N_{t} > 0\}$  为  $(N_{t})$  首次跳跃的时刻, 则  $(X_{t})$  在此时刻的跳幅  $\Delta X_{S} := X_{S} - X_{S-}$  服从分布  $\mu := \alpha^{-1}\nu$ .

证明 注意 $S$ 也是 $(X_{t})$ 首次跳跃的时刻. 对 $n \geqslant 1$ 令 $\tau_{n} = \inf \{k / 2^{n} > 0 : X_{k / 2^{n}} \neq i\}$. 显然 $\{\tau_{n}\}$ 为递降的停时列, 并且 $\tau_{n} \geqslant S$, 故 $\tau := \lim_{n \to \infty} \tau_{n} \geqslant S$. 显然, 对任何 $k / 2^{n} < \tau$ 有 $X_{k / 2^{n}} = i$. 由轨道右连续性, 对任何 $t \in [0, \tau)$ 有 $X_{t} = i$. 这意味着 $S \geqslant \tau$, 故得 $S = \lim_{n \to \infty} \tau_{n}$. 因为 $\mathbf{P}_{i}(S = t) = 0$, 利用控制收敛定理得

$$
\mathbf {P} (S \leqslant t) = \mathbf {P} (S <   t) = \lim _ {n \to \infty} \mathbf {P} (\tau_ {n} <   t) \leqslant \lim _ {n \to \infty} \mathbf {P} (\tau_ {n} \leqslant t) \leqslant \mathbf {P} (S \leqslant t).
$$

再由过程轨道的右连续性得

$$
\mathbf {E} (\mathrm{e} ^ {\mathrm{i} \theta \varDelta X _ {S}}; S \leqslant t) = \lim _ {n \to \infty} \mathbf {E} (\mathrm{e} ^ {\mathrm{i} \theta \varDelta X _ {S}}; \tau_ {n} \leqslant t) = \lim _ {n \to \infty} \sum_ {k = 1} ^ {\lfloor 2 ^ {n} t \rfloor} \mathbf {E} (\mathrm{e} ^ {\mathrm{i} \theta Z _ {k}}; \tau_ {n} = k / 2 ^ {n}),
$$

---

1.5 泊松随机测度

31

其中  $Z_{k}=X_{k/2^{n}}-X_{(k-1)/2^{n}}$ . 根据泊松随机测度的独立增量性,

$$
\begin{array}{l} \mathbf {E} (\mathrm{e} ^ {\mathrm{i} \theta Z _ {k}}; \tau_ {n} = k / 2 ^ {n}) \\ = \mathbf {E} (\mathrm{e} ^ {\mathrm{i} \theta (X _ {k / 2 ^ {n}} - X _ {(k - 1) / 2 ^ {n}})}; N _ {(k - 1) / 2 ^ {n}} = 0, N _ {k / 2 ^ {n}} - N _ {(k - 1) / 2 ^ {n}} \geqslant 1) \\ = \mathbf {P} (N _ {(k - 1) / 2 ^ {n}} = 0) \mathbf {E} (\mathrm{e} ^ {\mathrm{i} \theta (X _ {k / 2 ^ {n}} - X _ {(k - 1) / 2 ^ {n}})}; N _ {k / 2 ^ {n}} - N _ {(k - 1) / 2 ^ {n}} \geqslant 1) \\ = \mathrm{e} ^ {- \alpha (k - 1) / 2 ^ {n}} \mathbf {E} (\mathrm{e} ^ {\mathrm{i} \theta (X _ {1 / 2 ^ {n}} - X _ {0})}; N _ {1 / 2 ^ {n}} \geqslant 1) \\ = \mathrm{e} ^ {- \alpha (k - 1) / 2 ^ {n}} \mathbf {E} [ \mathrm{e} ^ {\mathrm{i} \theta (X _ {1 / 2 ^ {n}} - X _ {0})} (1 - 1 _ {\{N _ {1 / 2 ^ {n}} = 0 \}}) ] \\ = \mathrm{e} ^ {- \alpha (k - 1) / 2 ^ {n}} \left[ \exp \left\{\frac {1}{2 ^ {n}} \int_ {\mathbb {R}} (\mathrm{e} ^ {\mathrm{i} \theta z} - 1) \nu (\mathrm{d} z) \right\} - \mathrm{e} ^ {- \alpha / 2 ^ {n}} \right] \\ = \mathrm{e} ^ {- \alpha k / 2 ^ {n}} \left[ \exp \left\{\frac {\alpha}{2 ^ {n}} \int_ {\mathbb {R}} \mathrm{e} ^ {\mathrm{i} \theta z} \mu (\mathrm{d} z) \right\} - 1 \right]. \\ \end{array}
$$

回到上面的等式得

$$
\begin{array}{l} \mathbf {E} (\mathrm{e} ^ {\mathrm{i} \theta \Delta X _ {S}}; S \leqslant t) = \lim _ {n \to \infty} \sum_ {k = 1} ^ {\lfloor 2 ^ {n} t \rfloor} \mathrm{e} ^ {- \alpha k / 2 ^ {n}} \Big [ \exp \left\{\frac {\alpha}{2 ^ {n}} \int_ {\mathbb {R}} \mathrm{e} ^ {\mathrm{i} \theta z} \mu (\mathrm{d} z) \right\} - 1 \Big ] \\ = \lim _ {n \to \infty} \frac {\mathrm{e} ^ {- \alpha / 2 ^ {n}} [ 1 - \mathrm{e} ^ {- \alpha \lfloor 2 ^ {n} t \rfloor / 2 ^ {n}} ]}{1 - \mathrm{e} ^ {- \alpha / 2 ^ {n}}} \Big [ \exp \Big \{\frac {\alpha}{2 ^ {n}} \int_ {\mathbb {R}} \mathrm{e} ^ {\mathrm{i} \theta z} \mu (\mathrm{d} z) \Big \} - 1 \Big ] \\ = (1 - \mathrm{e} ^ {- \alpha t}) \int_ {\mathbb {R}} \mathrm{e} ^ {\mathrm{i} \theta z} \mu (\mathrm{d} z). \\ \end{array}
$$

在上式中令  $t \rightarrow \infty$  即知  $\Delta X_{S}$  服从分布  $\mu$ . □

定理 1.5.7 由 (1.5.6) 式定义的  $(X_{t}: t \geqslant 0)$  是有跳跃速率  $\alpha$  和跳跃分布  $\mu := \alpha^{-1}\nu$  的复合泊松过程.

证明 令 $S_{k}$ 为 $(N_{t})$ 的第 $k$ 次跳跃发生的时刻。我们需要证明跳幅 $\Delta X_{S_k} = X_{S_k} - X_{S_{k-}}$, $k = 1,2,\cdots$ 独立且服从相同的分布 $\mu$。为简单起见，下面只证明关于前两个跳幅的结论。有兴趣的读者可以参考下面的论证方法自行完成一般情况的证明。对 $n \geqslant 0$ 令 $D_n = \{i/2^n : i = 0,1,2,\cdots\}$。再令 $\tau_{k,n} = \inf \{t \in D_n : t > S_k\}$ 为 $S_k$ 的二分点离散化。显然序列 $\{S_k\}$ 是严格增的。对 $t \geqslant 0$ 和 $\theta_1, \theta_2 \in \mathbb{R}$，与命题1.5.6的证明中类似地有

$$
\begin{array}{l} \mathbf {E} \big (\mathrm{e} ^ {\mathrm{i} (\theta_ {1} \Delta X _ {S _ {1}} + \theta_ {2} \Delta X _ {S _ {2}})}; S _ {2} \leqslant t \big) \\ = \lim _ {n \to \infty} \mathbf {E} \big (\mathrm{e} ^ {\mathrm{i} (\theta_ {1} \varDelta X _ {S _ {1}} + \theta_ {2} \varDelta X _ {S _ {2}})}; \tau_ {2, n} \leqslant t \big) \\ = \lim _ {n \to \infty} \sum_ {k = 1} ^ {\lfloor 2 ^ {n} t \rfloor} \sum_ {j = 1} ^ {k} \mathbf {E} (\mathrm{e} ^ {\mathrm{i} (\theta_ {1} Z _ {j} + \theta_ {2} Z _ {k})}; \tau_ {1, n} = j / 2 ^ {n}, \tau_ {2, n} = k / 2 ^ {n}), \tag {1.5.7} \\ \end{array}
$$

其中 $Z_{k} = X_{k / 2^{n}} - X_{(k - 1) / 2^{n}}$ .注意

$$
\sum_ {k = 1} ^ {\lfloor 2 ^ {n} t \rfloor} \mathbf {P} \big (\tau_ {1, n} = \tau_ {2, n} = k / 2 ^ {n} \big)
$$

---

32

第一章 基本概念和例子

$$
\begin{array}{l} = \sum_ {k = 1} ^ {\lfloor 2 ^ {n} t \rfloor} \mathbf {P} \big (N _ {(k - 1) / 2 ^ {n}} = 0, N _ {k / 2 ^ {n}} - N _ {(k - 1) / 2 ^ {n}} \geqslant 2 \big) \\ = \sum_ {k = 1} ^ {\lfloor 2 ^ {n} t \rfloor} \mathrm{e} ^ {- \alpha (k - 1) / 2 ^ {n}} \left(1 - \mathrm{e} ^ {- \alpha / 2 ^ {n}} - \frac {\alpha}{2 ^ {n}} \mathrm{e} ^ {- \alpha / 2 ^ {n}}\right) \\ \leqslant 2 ^ {n} t \Big (1 - \mathrm{e} ^ {- \alpha / 2 ^ {n}} - \frac {\alpha}{2 ^ {n}} \mathrm{e} ^ {- \alpha / 2 ^ {n}} \Big). \\ \end{array}
$$

所以有

$$
\lim _ {n \to \infty} \sum_ {k = 1} ^ {\lfloor 2 ^ {n} t \rfloor} \mathbf {P} \big (\tau_ {1, n} = \tau_ {2, n} = k / 2 ^ {n} \big) = 0.
$$

另一方面, 当 $1 \leqslant j \leqslant k - 1$ 时有

$$
\begin{array}{l} \mathbf {E} \big (\mathrm{e} ^ {\mathrm{i} (\theta_ {1} Z _ {j} + \theta_ {2} Z _ {k})}; \tau_ {1, n} = j / 2 ^ {n}, \tau_ {2, n} = k / 2 ^ {n} \big) \\ = \mathbf {E} \big (\mathrm{e} ^ {\mathrm{i} \left(\theta_ {1} Z _ {j} + \theta_ {2} Z _ {k}\right)} 1 _ {\left\{N _ {(j - 1) / 2 ^ {n}} = 0 \right\}} 1 _ {\left\{N _ {j / 2 ^ {n}} - N _ {(j - 1) / 2 ^ {n}} \geqslant 1 \right\}}. \\ \left. 1 _ {\{N _ {(k - 1) / 2 ^ {n}} - N _ {j / 2 ^ {n}} = 0 \}} 1 _ {\{N _ {k / 2 ^ {n}} - N _ {(k - 1) / 2 ^ {n}} \geqslant 1 \}}\right) \\ = \mathbf {E} \big (N _ {(j - 1) / 2 ^ {n}} = 0 \big) \mathbf {E} \big (\mathrm{e} ^ {\mathrm{i} \theta_ {1} Z _ {j}} 1 _ {\{N _ {j / 2 ^ {n}} - N _ {(j - 1) / 2 ^ {n}} \geqslant 1 \}} \big)  . \\ \mathbf {E} \big (N _ {(k - 1) / 2 ^ {n}} - N _ {j / 2 ^ {n}} = 0 \big) \mathbf {E} \big (\mathrm{e} ^ {\mathrm{i} \theta_ {2} Z _ {k}}) 1 _ {\{N _ {k / 2 ^ {n}} - N _ {(k - 1) / 2 ^ {n}} \geqslant 1 \}}\left. \right) \\ = \mathrm{e} ^ {- \alpha (k - 2) / 2 ^ {n}} \mathbf {E} \big (\mathrm{e} ^ {\mathrm{i} \theta_ {1} Z _ {1}}; N _ {1 / 2 ^ {n}} \geqslant 1 \big) \mathbf {E} \big (\mathrm{e} ^ {\mathrm{i} \theta_ {2} Z _ {1}}; N _ {1 / 2 ^ {n}} \geqslant 1 \big) \\ = \mathrm{e} ^ {- \alpha (k - 2) / 2 ^ {n}} \mathbf {E} \big [ \mathrm{e} ^ {\mathrm{i} \theta_ {1} Z _ {1}} (1 - 1 _ {\{N _ {1 / 2 ^ {n}} = 0 \}}) \big ] \mathbf {E} \big [ \mathrm{e} ^ {\mathrm{i} \theta_ {2} Z _ {1}} (1 - 1 _ {\{N _ {1 / 2 ^ {n}} = 0 \}}) \big ] \\ = \mathrm{e} ^ {- \alpha (k - 2) / 2 ^ {n}} \left[ \exp \left\{\frac {1}{2 ^ {n}} \int_ {\mathbb {R}} (\mathrm{e} ^ {\mathrm{i} \theta_ {1} z} - 1) \nu (\mathrm{d} z) \right\} - \mathrm{e} ^ {- \alpha / 2 ^ {n}} \right]. \\ \left[ \exp \left\{\frac {1}{2 ^ {n}} \int_ {\mathbb {R}} (\mathrm{e} ^ {\mathrm{i} \theta_ {2} z} - 1) \nu (\mathrm{d} z) \right\} - \mathrm{e} ^ {- \alpha / 2 ^ {n}} \right] \\ = \mathrm{e} ^ {- \alpha k / 2 ^ {n}} \Big [ \exp \left\{\frac {\alpha}{2 ^ {n}} \int_ {\mathbb {R}} \mathrm{e} ^ {\mathrm{i} \theta_ {1} z} \mu (\mathrm{d} z) \right\} - 1 \Big ]. \\ \left[ \exp \left\{\frac {\alpha}{2 ^ {n}} \int_ {\mathbb {R}} \mathrm{e} ^ {\mathrm{i} \theta_ {2} z} \mu (\mathrm{d} z) \right\} - 1 \right]. \\ \end{array}
$$

根据上面的计算, 回到 (1.5.7) 式有

$$
\begin{array}{l} \mathbf {E} \big (\mathrm{e} ^ {\mathrm{i} (\theta_ {1} \varDelta X _ {S _ {1}} + \theta_ {2} \varDelta X _ {S _ {2}})}; S _ {2} \leqslant t \big) \\ = \lim _ {n \to \infty} \sum_ {k = 1} ^ {\lfloor 2 ^ {n} t \rfloor} \sum_ {j = 1} ^ {k - 1} \mathrm{e} ^ {- \alpha k / 2 ^ {n}} \Big [ \exp \left\{\frac {\alpha}{2 ^ {n}} \int_ {\mathbb {R}} \mathrm{e} ^ {\mathrm{i} \theta_ {1} z} \mu (\mathrm{d} z) \right\} - 1 \Big ]. \\ \left[ \exp \left\{\frac {\alpha}{2 ^ {n}} \int_ {\mathbb {R}} \mathrm{e} ^ {\mathrm{i} \theta_ {2} z} \mu (\mathrm{d} z) \right\} - 1 \right] \\ = \lim _ {n \to \infty} \alpha^ {2} \sum_ {k = 1} ^ {\lfloor 2 ^ {n} t \rfloor} \sum_ {j = 1} ^ {k - 1} \mathrm{e} ^ {- \alpha k / 2 ^ {n}} \frac {1}{2 ^ {2 n}} \int_ {\mathbb {R}} \mathrm{e} ^ {\mathrm{i} \theta_ {1} z} \mu (\mathrm{d} z) \int_ {\mathbb {R}} \mathrm{e} ^ {\mathrm{i} \theta_ {2} z} \mu (\mathrm{d} z) \\ \end{array}
$$

---

1.5 泊松随机测度

33

$$
\begin{array}{l} = \lim _ {n \to \infty} \alpha^ {2} \sum_ {k = 1} ^ {\lfloor 2 ^ {n} t \rfloor} (k - 1) \mathrm{e} ^ {- \alpha k / 2 ^ {n}} \frac {1}{2 ^ {2 n}} \int_ {\mathbb {R}} \mathrm{e} ^ {\mathrm{i} \theta_ {1} z} \mu (\mathrm{d} z) \int_ {\mathbb {R}} \mathrm{e} ^ {\mathrm{i} \theta_ {2} z} \mu (\mathrm{d} z) \\ = \alpha^ {2} \int_ {0} ^ {t} s \mathrm{e} ^ {- \alpha s} \mathrm{d} s \int_ {\mathbb {R}} \mathrm{e} ^ {\mathrm{i} \theta_ {1} z} \mu (\mathrm{d} z) \int_ {\mathbb {R}} \mathrm{e} ^ {\mathrm{i} \theta_ {2} z} \mu (\mathrm{d} z) \\ = \left(1 - \mathrm{e} ^ {- \alpha t} - \alpha t \mathrm{e} ^ {- \alpha t}\right) \int_ {\mathbb {R}} \mathrm{e} ^ {\mathrm{i} \theta_ {1} z} \mu (\mathrm{d} z) \int_ {\mathbb {R}} \mathrm{e} ^ {\mathrm{i} \theta_ {2} z} \mu (\mathrm{d} z). \\ \end{array}
$$

在上式中令 $t\to \infty$ 时得

$$
\mathbf {E} \big (\mathrm{e} ^ {\mathrm{i} (\theta_ {1} \varDelta X _ {S _ {1}} + \theta_ {2} \varDelta X _ {S _ {2}})} \big) = \int_ {\mathbb {R}} \mathrm{e} ^ {\mathrm{i} \theta_ {1} z} \mu (\mathrm{d} z) \int_ {\mathbb {R}} \mathrm{e} ^ {\mathrm{i} \theta_ {2} z} \mu (\mathrm{d} z).
$$

所以跳幅  $\Delta X_{S_{1}}$  和  $\Delta X_{S_{2}}$  独立且服从相同的分布  $\mu$ . ☐

设 $q$ 为 $\mathbb{R}$ 上的非负博雷尔可测函数, 而 $\mu$ 是 $\mathbb{R}$ 上的 $\sigma$ 有限测度. 再设 $\mu(\{0\}) = 0$ 且 $0 < \beta := \mu(q) < \infty$. 令 $N(\mathrm{d}s, \mathrm{d}z, \mathrm{d}u)$ 是 $(0, \infty) \times \mathbb{R} \times (0, \infty)$ 上的以 $\mathrm{d}s\mu(\mathrm{d}z)\mathrm{d}u$ 为强度的泊松随机测度, 而 $Z_0$ 是与之独立的随机变量. 再令

$$
Z _ {t} = Z _ {0} + \int_ {0} ^ {t} \int_ {\mathbb {R}} \int_ {0} ^ {q (z)} z N (\mathrm{d} s, \mathrm{d} z, \mathrm{d} u), \quad t \geqslant 0. \tag {1.5.8}
$$

定理 1.5.8 由 (1.5.8) 式定义的  $(Z_{t}: t \geqslant 0)$  是有跳跃速率  $\beta$  和跳跃分布  $\beta^{-1} q(z)$   $\mu(\mathrm{d}z)$  的复合泊松过程.

证明 令 $N_{q}(\mathrm{d}s,\mathrm{d}z)$ 为 $1_{\{u\leqslant q(z)\}}N(\mathrm{d}s,\mathrm{d}z,\mathrm{d}u)$ 在映射 $(s,z,u)\mapsto (s,z)$ 之下的像测度.应用定理1.5.5不难证明 $N_{q}(\mathrm{d}s,\mathrm{d}z)$ 是 $(0,\infty)\times \mathbb{R}$ 上的以 $q(z)\mathrm{d}s\mu (\mathrm{d}z)$ 为强度的泊松随机测度,而且与 $Z_0$ 独立.由(1.5.8)式有

$$
Z _ {t} = Z _ {0} + \int_ {0} ^ {t} \int_ {\mathbb {R}} z N _ {q} (\mathrm{d} s, \mathrm{d} z), \quad t \geqslant 0.
$$

再根据定理 1.5.7 即得欲证结论. □

## 练习题

1. 在定理 1.4.8 的条件下, 证明:

(1) $(N_{s+t}-N_{s}:t\geqslant0)$ 是以 $\alpha\geqslant0$ 为参数的零初值泊松过程,而 $\{\xi_{N_{s}+n}:n\geqslant1\}$ 是与之独立的独立同分布随机变量序列且有分布 $\mu;$
(2) 定理 1.4.8 中定义的过程  $(X_{t}: t \geqslant 0)$  满足定理 1.4.8 中的性质 (2).

2. 设 $\mu$ 是可测空间 $(E, \mathcal{E})$ 上的 $\sigma$ 有限测度. 证明 $(E, \mathcal{E})$ 上的以 $\mu$ 为强度的整数值随机测度 $X$ 是泊松随机测度当且仅当对 $(E, \mathcal{E})$ 上的任何非负可测函数 $f$ 有

$$
\mathrm{Ee} ^ {- X (f)} = \exp \bigg \{- \int_ {E} (1 - \mathrm{e} ^ {- f (x)}) \mu (\mathrm{d} x) \bigg \}.
$$

---

34

第一章 基本概念和例子

3. 令 $X$ 是 $(E, \mathcal{E})$ 上的以有限测度 $\mu$ 为强度的泊松随机测度. 证明对任意的 $f, g \in \mathrm{p}\mathcal{E}$, 有

(1) $\mathbf{E}[X(f)\mathrm{e}^{-X(g)}] = \mu (f\mathrm{e}^{-g})\mathbf{E}[\mathrm{e}^{-X(g)}]$;
(2) $\mathbf{E}[X(f)^2\mathrm{e}^{-X(g)}] = [\mu (f^2\mathrm{e}^{-g}) + \mu (f\mathrm{e}^{-g})^2 ]\mathbf{E}[\mathrm{e}^{-X(g)}];$
(3) $\mathbf{E}[\tilde{X}(f)^4] = \mu(f^4) + 3\mu(f^2)^2.$
