令 $k \to \infty$ 得 $\mathbf{E}(X_n 1_A) = \mathbf{E}(X 1_A)$. 因而 $\mathbf{E}(X|\mathcal{F}_n) = X_n$. $\square$

推论 2.4.6 设  $(X_{n})$  为非负上鞅, 则当  $n \to \infty$  时有  $X_{n} \stackrel{a.s.}{\rightarrow} X$ , 其中 X 是一个可积随机变量.

证明 因为 $(X_{n})$ 是非负上鞅, 序列 $\mathbf{E}|X_n| = \mathbf{E}(X_n)$ 不增, 从而有界. 应用定理2.4.5于下鞅 $(-X_{n})$ 即可. □

推论 2.4.7 对任何可积随机变量 Y 和  $\sigma$  代数流  $(\mathcal{F}_{n})_{n\geqslant0}$ ，当  $n\to\infty$  时  $X_{n}:=$ 

$\mathbf{E}(Y|\mathcal{F}_{n})$  几乎必然且  $L^{1}$  收敛于  $X_{\infty}:=\mathbf{E}(Y|\mathcal{F}_{\infty})$ ，其中  $\mathcal{F}_{\infty}=\sigma\left(\bigcup_{n}\mathcal{F}_{n}\right)$ .

证明 由命题2.2.5知杜布鞅 $(X_{n})$ 一致可积.根据定理2.4.5,在几乎必然和 $L^1$ 意义下，极限 $X = \lim_{n\to \infty}X_n\in \mathcal{F}_\infty$ 存在且 $X_{n} = \mathbf{E}(X|\mathcal{F}_{n})$ .这样

$$
\mathbf {E} (X _ {\infty} | \mathcal {F} _ {n}) = \mathbf {E} [ \mathbf {E} (Y | \mathcal {F} _ {\infty}) | \mathcal {F} _ {n} ] = \mathbf {E} (Y | \mathcal {F} _ {n}) = X _ {n} = \mathbf {E} (X | \mathcal {F} _ {n}). \tag {2.4.5}
$$

令 $\mathcal{M}$ 是使等式 $\mathbf{E}(X_{\infty};A) = \mathbf{E}(X;A)$ 成立的所有事件 $A\in \mathcal{F}_{\infty}$ 构成的集类.应用单调收敛定理可以证明 $\mathcal{M}$ 是一个单调类.由(2.4.5)式对任何 $A\in \mathcal{F}_n$ 有

$$
\mathbf {E} (X _ {\infty}; A) = \mathbf {E} (X _ {n}; A) = \mathbf {E} (X; A).
$$

所以  $M \supseteq \bigcup_{n} F_{n}$ . 注意  $\bigcup_{n} F_{n}$  是一个集代数. 根据单调类定理有  $M \supseteq m \left( \bigcup_{n} F_{n} \right) = \sigma \left( \bigcup_{n} F_{n} \right) = \mathcal{F}_{\infty}$ , 即上式对任何  $A \in F_{\infty}$  也成立. 所以几乎必然地  $X = X_{\infty}$ . □

推论 2.4.8 设有随机变量序列  $(Y_{n})_{n\geqslant0}$  和  $\sigma$  代数流  $(\mathcal{F}_{n})_{n\geqslant0}$ . 如果几乎必然地  $\lim_{n\to\infty}Y_{n}=Y$  且有可积随机变量 Z 使得  $|Y_{n}|\leqslant Z$ , 那么  $X_{n}:=\mathbf{E}(Y_{n}|\mathcal{F}_{n})$  几乎必然且  $L^{1}$  收敛于  $X_{\infty}:=\mathbf{E}(Y|\mathcal{F}_{\infty})$ , 其中  $\mathcal{F}_{\infty}=\sigma\left(\bigcup_{n}\mathcal{F}_{n}\right)$ .

证明 令 $W_{n} = \sup_{k\geqslant n}|Y_{k} - Y|$, 则 $|W_{n}| \leqslant 2Z$ 且几乎必然地 $W_{n} \to 0$. 再由推论2.4.7有 $X_{\infty} = \lim_{n\to \infty}\mathbf{E}(Y|\mathcal{F}_n)$, 故对于任何 $m \geqslant 0$ 有

$$
\begin{array}{l} \operatorname * {l i m s u p} _ {n \to \infty} | X _ {n} - X _ {\infty} | = \operatorname * {l i m s u p} _ {n \to \infty} | X _ {n} - \mathbf {E} (Y | \mathscr {F} _ {n}) | = \operatorname * {l i m s u p} _ {n \to \infty} | \mathbf {E} (Y _ {n} - Y | \mathscr {F} _ {n}) | \\ \leqslant \operatorname * {l i m s u p} _ {n \to \infty} \mathbf {E} (| Y _ {n} - Y | | \mathscr {F} _ {n}) = \operatorname * {l i m s u p} _ {n \to \infty} \mathbf {E} (W _ {n} | \mathscr {F} _ {n}) \\ \leqslant \lim _ {n \to \infty} \mathbf {E} (W _ {m} | \mathcal {F} _ {n}) = \mathbf {E} (W _ {m} | \mathcal {F} _ {\infty}), \\ \end{array}
$$

其中最后一个等号成立再次用到了推论 2.4.7. 根据条件期望的控制收敛定理, 上式右端当 $m \to \infty$ 时趋于零. 所以结论中的几乎必然收敛成立. 另一方面, 由于

$$
| X _ {n} | \leqslant \mathbf {E} (| Y _ {n} | \big | \mathscr {F} _ {n}) \leqslant \mathbf {E} (Z | \mathscr {F} _ {n}),
$$

且右边的随机变量序列一致可积, 显然  $(X_{n})$  一致可积, 故结论中的  $L^{1}$  收敛也成立. □

## 2.4.4 向后收敛定理

前面考虑的离散时间鞅的参数集为  $\{0,1,2,\cdots\}$ . 形象地说, 定理 2.4.5 中的下鞅收敛是向前收敛. 接下来我们讨论下鞅的向左收敛定理, 也就是考虑时间集为  $\{\cdots,-2,-1,0\}$  的情况.

定理 2.4.9 设  $(X_{n}: n \leqslant 0)$  是关于流  $(\mathcal{F}_{n})_{n \leqslant 0}$  的下鞅且  $\inf_{n} \mathbf{E}(X_{n}) > -\infty$ ，则  $(X_{n})$  是一致可积的。而且当  $n \to -\infty$  时， $X_{n}$  几乎必然且  $L^{1}$  收敛于一个可积随机变量  $X_{-\infty}$ ，且对任何 n 有  $\mathbf{E}(X_{n} | \mathcal{F}_{-\infty}) \geqslant X_{-\infty}$ ，其中  $F_{-\infty} = \bigcap_{n=0}^{-\infty} F_{n}$ 。

证明 对任何 $n \leqslant 0$ 有 $\mathbf{E}(X_{n-1}) \leqslant \mathbf{E}(X_n)$. 所以 $\inf_{n} \mathbf{E}(X_n) > -\infty$ 蕴涵极限 $x := \lim_{n \to -\infty} \mathbf{E}(X_n)$ 单调递降地存在且有限. 对于 $\varepsilon > 0$ 取 $k \leqslant 0$ 使 $\mathbf{E}(X_k) < x + \varepsilon$. 注意, 对 $n \leqslant k$ 有 $\mathbf{E}(X_n) \geqslant x > \mathbf{E}(X_k) - \varepsilon$, 所以

$$
\begin{array}{l} \mathbf {E} (| X _ {n} |; | X _ {n} | > \lambda) = \mathbf {E} (X _ {n}; X _ {n} > \lambda) - \mathbf {E} (X _ {n}; X _ {n} <   - \lambda) \\ = \mathbf {E} (X _ {n}; X _ {n} > \lambda) - \mathbf {E} (X _ {n}) + \mathbf {E} (X _ {n}; X _ {n} \geqslant - \lambda) \\ \leqslant \mathbf {E} [ \mathbf {E} (X _ {k} | \mathscr {F} _ {n}); X _ {n} > \lambda ] - \mathbf {E} (X _ {n}) + \\ \mathbf {E} [ \mathbf {E} (X _ {k} | \mathscr {F} _ {n}); X _ {n} \geqslant - \lambda ] \\ \leqslant \mathbf {E} (X _ {k}; X _ {n} > \lambda) - \mathbf {E} (X _ {k}) + \varepsilon + \mathbf {E} (X _ {k}; X _ {n} \geqslant - \lambda) \\ = \mathbf {E} (X _ {k}; X _ {n} > \lambda) - \mathbf {E} (X _ {k}; X _ {n} <   - \lambda) + \varepsilon \\ \leqslant \mathbf {E} (| X _ {k} |; | X _ {n} | > \lambda) + \varepsilon . \\ \end{array}
$$

取 $L := L_k \geqslant 1$ 充分大使得 $\mathbf{E}(|X_k|; |X_k| > L) < \varepsilon$. 由上式

$$
\begin{array}{l} \mathbf {E} (| X _ {n} |; | X _ {n} | > \lambda) \leqslant \mathbf {E} (| X _ {k} |; | X _ {k} | \leqslant L, | X _ {n} | > \lambda) + 2 \varepsilon \\ \leqslant L \mathbf {E} (| X _ {n} | > \lambda) + 2 \varepsilon . \\ \end{array}
$$

另外, 由马尔可夫不等式,

$$
\mathbf {P} (| X _ {n} | > \lambda) \leqslant \frac {1}{\lambda} \mathbf {E} | X _ {n} | = \frac {1}{\lambda} \big [ 2 \mathbf {E} (X _ {n} ^ {+}) - \mathbf {E} (X _ {n}) \big ] \leqslant \frac {1}{\lambda} \big [ 2 \mathbf {E} (X _ {0} ^ {+}) - x \big ],
$$

其中最后的不等号是由于 $x \leqslant \mathbf{E}(X_n)$ 而 $X = (X_n^+)_{n \leqslant 0}$ 也是下鞅. 由上述两个不等式得

$$
\sup _ {n \leqslant k} \mathbf {E} (| X _ {n} |; | X _ {n} | > \lambda) \leqslant \frac {1}{\lambda} L \left[ 2 \mathbf {E} (X _ {0} ^ {+}) - x \right] + 2 \varepsilon ,
$$

从而

$$
\operatorname * {l i m s u p} _ {\lambda \to \infty} \sup _ {n \leqslant k} \mathbf {E} (| X _ {n} |; | X _ {n} | > \lambda) \leqslant 2 \varepsilon .
$$

另外, 不难取常数  $N \geqslant 1$  使当  $\lambda \geqslant N$  时

$$
\sup _ {k \leqslant n \leqslant 0} \mathbf {E} (| X _ {n} |; | X _ {n} | > \lambda) \leqslant 2 \varepsilon .
$$

综合以上二式得

$$
\operatorname * {l i m s u p} _ {\lambda \to \infty} \sup _ {n \leqslant 0} \mathbf {E} (| X _ {n} |; | X _ {n} | > \lambda) \leqslant 2 \varepsilon .
$$

由  $\varepsilon > 0$  的任意性即知  $(X_{n})_{n \leqslant 0}$  一致可积，故第一个断言得证.类似于定理 2.4.5 的证明.令  $X_{*} = \liminf_{n \to -\infty} X_{n}$  和  $X^{*} = \limsup_{n \to -\infty} X_{n}$ .对非负整数 N，用  $V_{N}^{X}[a, b]$  表示下鞅  $\{X_{-N}, X_{-N+1}, \cdots, X_{0}\}$  对区间 [a, b] 的上穿次数，则

$$
\mathbf {E} \{V _ {N} ^ {X} [ a, b ] \} \leqslant \frac {1}{b - a} \mathbf {E} | X _ {0} - a | <   \infty .
$$

由此可以推出几乎必然地 $X_{*} = X^{*}$。所以几乎必然存在有限或无限的极限 $X_{-\infty} := \lim_{n \to -\infty} X_{n}$。显然 $X_{-\infty}$ 关于 $\mathscr{F}_{-\infty}$ 可测。再由 $(X_{n}: n \leqslant 0)$ 的一致可积性知 $X_{-\infty}$ 为有限可积随机变量且 $X_{n} \xrightarrow{L^{1}} X_{-\infty}$。另外对任何 $k < n \leqslant 0$ 和 $A \in \mathscr{F}_{-\infty} \subseteq \mathscr{F}_{k}$ 有

$$
\mathbf {E} [ \mathbf {E} (X _ {n} | \mathscr {F} _ {- \infty}) 1 _ {A} ] = \mathbf {E} (X _ {n} 1 _ {A}) = \mathbf {E} [ \mathbf {E} (X _ {n} | \mathscr {F} _ {k}) 1 _ {A} ] \geqslant \mathbf {E} (X _ {k} 1 _ {A}).
$$

令 $k \to -\infty$ 得 $\mathbf{E}[\mathbf{E}(X_n|\mathcal{F}_{-\infty})1_A] \geqslant \mathbf{E}(X_{-\infty}1_A)$, 故 $\mathbf{E}(X_n|\mathcal{F}_{-\infty}) \geqslant X_{-\infty}$. $\square$

推论 2.4.10 对可积随机变量 Y 和  $\sigma$  代数流  $(\mathcal{F}_{n})_{n\leqslant0}$ ，几乎必然地

$$
\mathbf {E} (Y | \mathscr {F} _ {- \infty}) = \lim _ {n \to - \infty} \mathbf {E} (Y | \mathscr {F} _ {n}),
$$

其中  $\mathscr{F}_{-\infty}=\bigcap_{n}\mathscr{F}_{n}.$

推论 2.4.11 设有随机变量序列  $(Y_{n})_{n\leqslant0}$  和  $\sigma$  代数流  $(\mathcal{F}_{n})_{n\leqslant0}$ . 若几乎必然地  $\lim_{n\to-\infty}Y_{n}=Y$  且有可积随机变量 Z 使得  $|Y_{n}|\leqslant Z$ , 则  $X_{n}:=\mathbf{E}(Y_{n}|\mathcal{F}_{n})$  几乎必然且  $L^{1}$  收敛于  $X_{-\infty}:=\mathbf{E}(Y|\mathcal{F}_{-\infty})$ , 其中  $F_{-\infty}=\bigcap_{n}\mathcal{F}_{n}$ .

上面推论的证明与推论 2.4.7 和推论 2.4.8 的类似, 因此省略.

## 练习题

1. 证明推论 2.4.10 和推论 2.4.11.

2. 设 $\{\xi_n\}$ 为零均值平方可积独立随机变量序列. 令 $S_{n} = \sum_{k=1}^{n} \xi_{k}$, 则对 $n \geqslant 1$ 和 $\lambda > 0$ 有 (柯尔莫哥洛夫不等式)

$$
\mathbf {P} \Big (\max _ {1 \leqslant k \leqslant n} | S _ {k} | \geqslant \lambda \Big) \leqslant \frac {1}{\lambda^ {2}} \mathbf {E} (S _ {n} ^ {2}).
$$

利用鞅不等式给出上式的证明.

3. 设 $(X_{n}: n \geqslant 0)$ 为离散时间鞅, 且对某个 $p > 1$ 有 $\sup_{n \geqslant 0} \mathbf{E}[|X_{n}|^{p}] < \infty$. 证明存在可积随机变量 $X$ 使得 $X_{n} \xrightarrow{L^{1}} X (n \to \infty)$.
4. 在上题的情况下, 证明 $X_{n} \xrightarrow{L^{p}} X (n \to \infty)$.
5. 设 $(X_{n}: n \geqslant 0)$ 为平方可积离散时间鞅. 根据杜布分解定理, 存在唯一的从原点出发的可料增过程 $(\langle X \rangle_{n}: n \geqslant 0)$ 使得 $(X_{n} - \langle X \rangle_{n}: n \geqslant 0)$ 是鞅. 证明下面4个性质等价: (1) $\sup_{n \geqslant 0} \mathbf{E}[X_{n}^{2}] < \infty$; (2) $\sup_{n \geqslant 0} \mathbf{E}[\langle X \rangle_{n}] < \infty$; (3) $(X_{n})$ 在 $L^{2}$ 意义下收敛; (4) $(X_{n})$ 在 $L^{2}$ 和几乎必然意义下收敛.

## 2.5 连续时间下鞅

本节讨论连续时间下鞅的轨道的正则性. 考虑完备概率空间 $(\Omega, \mathcal{F}, \mathbf{P})$ 及其上的加强流 $(\mathcal{F}_t)_{t \geqslant 0}$. 设 $D$ 是 $[0, \infty)$ 的一个可数稠子集且包含所有正整数. 对于整数 $K \geqslant 1$, 令 $D_K = [0, K] \cap D$. 后面的很多结果都是在几乎必然意义下叙述的.

## 2.5.1 轨道的正则化

设 $X = (X_{t}: t \geqslant 0)$ 是一个 $(\mathcal{F}_{t})$ 下鞅. 对给定的整数 $N \geqslant 1$, 取有限集 $F := \{0 = t_{0} < t_{1} < \cdots < t_{N} = K\} \subseteq D_{K}$. 对 $0 \leqslant n \leqslant N$, 令 $Y_{n} = X_{t_{n}}$ 和 $\mathcal{G}_{n} = \mathcal{F}_{t_{n}}$. 显然 $Y = (Y_{n}: 0 \leqslant n \leqslant N)$ 关于流 $(\mathcal{G}_{n}: 0 \leqslant n \leqslant N)$ 是一个下鞅. 由杜布上穿不等式得

$$
\lambda \mathbf {P} \Big (\max _ {0 \leqslant n \leqslant N} | Y _ {n} | > \lambda \Big) \leqslant 2 \mathbf {E} (Y _ {N} ^ {+}) - \mathbf {E} (Y _ {0}) = 2 \mathbf {E} (X _ {K} ^ {+}) - \mathbf {E} (X _ {0})
$$

和

$$
\mathbf {E} \{U _ {N} ^ {Y} [ a, b ] \} \leqslant \frac {1}{b - a} \mathbf {E} [ (Y _ {N} - a) ^ {+} ] = \frac {1}{b - a} \mathbf {E} [ (X _ {K} - a) ^ {+} ],
$$

其中 $\lambda > 0, a < b$. 显然 $U_N^Y[a, b]$ 也就是 $X$ 限制在 $F$ 上对 $[a, b]$ 的上穿次数. 因此, 我们也将其记为 $U_F^X[a, b]$. 再令

$$
U _ {D _ {K}} ^ {X} [ a, b ] = \sup \{U _ {F} ^ {X} [ a, b ]: F \subseteq D _ {K} \text {为有限集合} \},
$$

它是 $X$ 限制在 $D_K$ 上对区间 $[a, b]$ 的上穿次数. 因为 $D_K$ 可数, 故其有限子集全体是可数的, 因此 $U_{D_K}^X[a, b]$ 是一个正随机变量. 由上面的不等式和法图定理容易推出

$$
\lambda \mathbf {P} \Big (\sup _ {t \in D _ {K}} | X _ {t} | > \lambda \Big) \leqslant 2 \mathbf {E} (X _ {K} ^ {+}) - \mathbf {E} (X _ {0}) \tag {2.5.1}
$$

和

$$
\mathbf {E} \{U _ {D _ {K}} ^ {X} [ a, b ] \} \leqslant \frac {1}{b - a} \mathbf {E} [ (X _ {K} - a) ^ {+} ]. \tag {2.5.2}
$$

为了简化叙述, 我们用 $s \uparrow t$ 表示 $s < t$ 且 $s \uparrow t$, 符号 $\Downarrow$ 的含义类似. 下面是连续时间下鞅正则化的第一个基本定理.

定理 2.5.1 设  $X = (X_{t} : t \geqslant 0)$  是一个  $(\mathcal{F}_{t})$  下鞅, 而 D 是  $[0, \infty)$  的一个可数稠子集. 那么

(1) 对几乎所有的 $\omega \in \Omega$, 映射 $t \mapsto X_t(\omega)$ 对任何 $K > 0$ 在 $D_K$ 上有界且存在极限:

$$
\left\{ \begin{array}{l l} X _ {t +} ^ {D} (\omega) := \lim _ {D \ni s \Downarrow t} X _ {s} (\omega) & (t \geqslant 0), \\ X _ {t -} ^ {D} (\omega) := \lim _ {D \ni s \uparrow t} X _ {s} (\omega) & (t > 0). \end{array} \right. \tag {2.5.3}
$$

这里  $X_{+}^{D}=(X_{t+}^{D}:t\geqslant0)$  左极右连, 而  $X_{-}^{D}=(X_{t-}^{D}:t>0)$  左连右极.

(2) 对每个 $t \geqslant 0$ 随机变量 $X_{t+}^{D}$ 可积且 $X_{t} \leqslant \mathbf{E}(X_{t+}^{D}|\mathcal{F}_{t})$. 特别地, 若均值函数 $t \mapsto \mathbf{E}(X_{t})$ 右连续, 则 $X_{t} = \mathbf{E}(X_{t+}^{D}|\mathcal{F}_{t})$.
(3) 过程 $X_{+}^{D} = (X_{t + }^{D}: t \geqslant 0)$ 是 $(\mathcal{F}_{t + })$ 下鞅; 且当 $X$ 是 $(\mathcal{F}_t)$ 鞅时, $X_{+}^{D}$ 是 $(\mathcal{F}_{t + })$ 鞅.

证明 (1) 记 $N_0$ 为 $\Omega$ 中使轨道 $t \mapsto X_t(\omega)$ 在某个 $D_K$ 上无界或在某个点 $t \geqslant 0$ 处 (2.5.3) 式中右或左极限不存在的 $\omega$ 全体. 只需证明 $N_0 \in \mathcal{F}$ 且 $\mathbf{P}(N_0) = 0$. $\mathbb{Q}$ 表示有理数集. 根据引理 1.1.3 有

$$
N _ {0} = \bigcup_ {K = 1} ^ {\infty} \Big (\Big \{\sup _ {t \in D _ {K}} | X _ {t} | = \infty \Big \} \cup N _ {K} \Big), \tag {2.5.4}
$$

其中

$$
N _ {K} = \bigcup_ {a, b \in \mathbb {Q}, a <   b} \left\{U _ {D _ {K}} ^ {X} [ a, b ] = \infty \right\}.
$$

对任何整数 $K \geqslant 1$ 及 $a < b$, 由 (2.5.1) 式有

$$
\begin{array}{l} \mathbf {P} \Big \{\sup _ {t \in D _ {K}} | X _ {t} | = \infty \Big \} = \lim _ {\lambda \to \infty} \mathbf {P} \Big \{\sup _ {t \in D _ {K}} | X _ {t} | > \lambda \Big \} \\ \leqslant \lim _ {\lambda \rightarrow \infty} \frac {1}{\lambda} \left[ 2 \mathbf {E} (X _ {K} ^ {+}) - \mathbf {E} (X _ {0}) \right] = 0, \\ \end{array}
$$

而由 (2.5.2) 式有

$$
\mathbf {P} \big \{U _ {D _ {K}} ^ {X} [ a, b ] = \infty \big \} = \lim _ {N \to \infty} \mathbf {P} \big \{U _ {D _ {K}} ^ {X} [ a, b ] \geqslant N \big \}
$$

$$
\begin{array}{l} \leqslant \lim _ {N \to \infty} \frac {1}{N} \mathbf {E} \big \{U _ {D _ {K}} ^ {X} [ a, b ] \big \} \\ \leqslant \lim _ {N \to \infty} \frac {1}{N (b - a)} \mathbf {E} [ (X _ {K} - a) ^ {+} ] = 0. \\ \end{array}
$$

再由 (2.5.4) 式得  $\mathbf{P}(N_{0})=0$ .

(2) 对任何 $t \geqslant 0$, 取序列 $\{s_k : k \geqslant 0\} \subseteq D$ 满足 $s_k \Downarrow t$. 对整数 $n \leqslant 0$ 令 $Y_n = X_{s_{-n}}$ 和 $\mathcal{G}_n = \mathcal{F}_{s_{-n}}$, 则 $Y = (Y_n : n \leqslant 0)$ 是关于 $(\mathcal{G}_n : n \leqslant 0)$ 的下鞅, 且

$$
\mathbf {E} (Y _ {n}) = \mathbf {E} (X _ {s _ {- n}}) \geqslant \mathbf {E} (X _ {t}).
$$

由定理 2.4.9 知 Y 一致可积, 而且当  $n \to -\infty$  时  $Y_{n} = X_{s_{-n}}$  几乎必然且  $L^{1}$  收敛于某个随机变量  $Y_{-\infty}$ , 显然  $Y_{-\infty} = X_{t+}^{D}$ . 特别地,  $X_{t+}^{D}$  可积. 又因为  $X_{t} \leqslant \mathbf{E}(X_{s_{-n}} | \mathcal{F}_{t})$ , 对于任何  $A \in F_{t}$  有  $\mathbf{E}(X_{t}; A) \leqslant \mathbf{E}(X_{s_{-n}}; A)$ . 由  $L^{1}$  收敛性推出

$$
\mathbf {E} (X _ {t}; A) \leqslant \mathbf {E} (X _ {t +} ^ {D}; A) = \mathbf {E} [ \mathbf {E} (X _ {t +} ^ {D} 1 _ {A} | \mathcal {F} _ {t}) ] = \mathbf {E} [ \mathbf {E} (X _ {t +} ^ {D} | \mathcal {F} _ {t}); A ],
$$

所以 $X_{t} \leqslant \mathbf{E}(X_{t+}^{D}|\mathcal{F}_{t})$. 若 $t \mapsto \mathbf{E}(X_{t})$ 右连续, 则

$$
\mathbf {E} (X _ {t}) = \lim _ {k \to \infty} \mathbf {E} (X _ {s _ {k}}) = \mathbf {E} (X _ {t +} ^ {D}) = \mathbf {E} [ \mathbf {E} (X _ {t +} ^ {D} | \mathscr {F} _ {t}) ].
$$

从而  $X_{t}=\mathbf{E}(X_{t+}^{D}|\mathcal{F}_{t})$ .

(3) 首先由于 $(\mathcal{F}_{t+})$ 是加强流, 易知 $X_{+}^{D}$ 是 $(\mathcal{F}_{t+})$ 适应的可积过程. 另外对 $t > s \geqslant 0$, 令 $s_{0} = t$ 并取 $\{s_{n}: n \geqslant 1\} \subseteq D$ 使 $s_{0} \geqslant s_{n} \Downarrow s$. 根据推论2.4.10得到

$$
X _ {s +} ^ {D} = \lim _ {n \to \infty} X _ {s _ {n}} \leqslant \lim _ {n \to \infty} \mathbf {E} (X _ {s _ {0}} | \mathcal {F} _ {s _ {n}}) = \mathbf {E} \left(X _ {s _ {0}} | \bigcap_ {n \geqslant 0} \mathcal {F} _ {s _ {n}}\right) = \mathbf {E} (X _ {t} | \mathcal {F} _ {s +}).
$$

再取 $\{t_n : n \geqslant 0\} \subseteq D$ 满足 $t_n \Downarrow t$. 令 $A \in \mathcal{F}_{s+}$. 对 $t_n$ 应用上式得

$$
\mathbf {E} (X _ {s +} ^ {D}; A) \leqslant \mathbf {E} [ \mathbf {E} (X _ {t _ {n}} | \mathcal {F} _ {s +}); A ] = \mathbf {E} [ \mathbf {E} (X _ {t _ {n}} 1 _ {A} | \mathcal {F} _ {s +}) ] = \mathbf {E} (X _ {t _ {n}}; A).
$$

再令 $n\to \infty$ ，由 $L^1$ 收敛得

$$
\mathbf {E} (X _ {s +} ^ {D}; A) \leqslant \mathbf {E} (X _ {t +} ^ {D}; A) = \mathbf {E} [ \mathbf {E} (X _ {t +} ^ {D} 1 _ {A} | \mathscr {F} _ {s +}) ] = \mathbf {E} [ \mathbf {E} (X _ {t +} ^ {D} | \mathscr {F} _ {s +}); A ],
$$

从而 $X_{s+}^{D} \leqslant \mathbf{E}(X_{t+}^{D}|\mathcal{F}_{s+})$, 即 $X_{+}^{D}$ 是关于 $(\mathcal{F}_{t+})$ 的下鞅. 若 $X$ 是鞅, 则 $\mathbf{E}(X_t)$ 是常数, 那么 $\mathbf{E}(X_{t+}^{D})$ 也是常数, 故 $X_{s+}^{D} = \mathbf{E}(X_{t+}^{D}|\mathcal{F}_{s+})$, 因而 $X_{+}^{D}$ 是鞅. $\square$

注意, 上面右极限过程 $X_{+}^{D}$ 的定义与可数稠集 $D$ 有关, 但显然由两个不同可数稠集所定义的右极限过程是无区别的.

定理 2.5.2 (1) 若 X 是随机右连续的  $(\mathcal{F}_{t})$  下鞅, 则它有左极右连的  $(\mathcal{F}_{t+})$  下鞅修正; (2) 若 X 是右连续的  $(\mathcal{F}_{t})$  下鞅, 则它是几乎必然左极右连的  $(\mathcal{F}_{t+})$  下鞅.

证明 由定理2.5.1知 $X_{+}^{D}$ 为左极右连的 $(\mathcal{F}_{t+})$ 下鞅.若 $X$ 随机右连续，由命题1.1.2知 $X_{+}^{D}$ 是 $X$ 的一个修正.若假定 $X$ 右连续，由命题1.1.1知 $X_{+}^{D}$ 与 $X$ 无区别，因而 $X$ 是几乎必然左极右连的 $(\mathcal{F}_{t+})$ 下鞅.□

定理 2.5.3 设流  $(\mathcal{F}_{t})$  满足通常条件. 若下鞅 X 的均值函数  $t \mapsto \mathbf{E}(X_{t})$  右连续, 则 X 有左极右连的  $(\mathcal{F}_{t})$  下鞅修正. 特别地, 在通常条件下, 鞅总有左极右连的修正.

证明 根据定理 2.5.1, 因  $(\mathcal{F}_{t})$  右连续, 知  $X_{+}^{D}$  为左极右连的  $(\mathcal{F}_{t})$  下鞅. 再因  $t \mapsto \mathbf{E}(X_{t})$  是右连续, 有

$$
X _ {t} = \mathbf {E} (X _ {t +} ^ {D} | \mathcal {F} _ {t}) = \mathbf {E} (X _ {t +} ^ {D} | \mathcal {F} _ {t +}) = X _ {t +} ^ {D}.
$$

故 $X_{+}^{D}$ 是 $X$ 的修正. $\square$

定义 2.5.1 称连续的实数值  $(\mathcal{F}_{t})$  适应随机过程  $(B_{t}: t \geqslant 0)$  是关于流  $(\mathcal{F}_{t})$  的以  $\sigma^{2} \geqslant 0$  为参数的布朗运动, 是指对任意的  $t > s \geqslant 0$  增量  $B_{t} - B_{s}$  独立于  $F_{s}$  且服从高斯分布  $N(0, \sigma^{2}(t - s))$ , 即对  $\theta \in R$  有

$$
\mathbf {E} [ \mathrm{e} ^ {\mathrm{i} \theta (B _ {t} - B _ {s})} | \mathcal {F} _ {s} ] = \mathbf {E} [ \mathrm{e} ^ {\mathrm{i} \theta (B _ {t} - B _ {s})} ] = \mathrm{e} ^ {- \sigma^ {2} (t - s) \theta^ {2} / 2}. \tag {2.5.5}
$$

特别地, 当 $\sigma^2 = 1$ 时称 $(B_t : t \geqslant 0)$ 为关于流 $(\mathcal{F}_t)$ 的标准布朗运动.

显然, 当 $(\mathcal{F}_t)$ 为 $(B_t)$ 的自然 $\sigma$ 代数流时, 这里关于 $(\mathcal{F}_t)$ 的布朗运动的定义与定义1.3.1等价. 另外, 若 $(B_t)$ 是关于 $(\mathcal{F}_t)$ 的布朗运动且 $\mathbf{E}|B_0| < \infty$, 则它是关于该流的鞅.

命题 2.5.4 若  $(B_{t}: t \geqslant 0)$  关于流  $(\mathcal{F}_{t})$  是以  $\sigma^{2}$  为参数的布朗运动, 则它关于右连续加强流  $(\mathcal{F}_{t+}^{*})$  也是以  $\sigma^{2}$  为参数的布朗运动.

证明 在假定条件下, 显然 (2.5.5) 式对于加强流 $(\mathcal{F}_t^*)$ 也成立, 故对 $t > s \geqslant 0$ 和 $\theta \in \mathbb{R}$ 有

$$
\mathbf {E} [ \mathrm{e} ^ {\mathrm{i} \theta B _ {t}} | \mathcal {F} _ {s} ^ {*} ] = \exp \left\{\mathrm{i} \theta B _ {s} - \frac {1}{2} \sigma^ {2} (t - s) \theta^ {2} \right\}.
$$

根据推论 2.4.10, 并利用  $(B_{t}: t \geqslant 0)$  的连续性得

$$
\mathbf {E} [ \mathrm{e} ^ {\mathrm{i} \theta B _ {t}} | \mathcal {F} _ {s +} ^ {*} ] = \exp \left\{\mathrm{i} \theta B _ {s} - \frac {1}{2} \sigma^ {2} (t - s) \theta^ {2} \right\}.
$$

所以 $(B_{t}:t\geqslant0)$ 关于 $(\mathcal{F}_{t+}^{*})$ 也是以 $\sigma^{2}$ 为参数的布朗运动. □

## 2.5.2 有界停止定理

下面的定理是杜布有界停止定理的连续时间版本.

定理 2.5.5 设 X 为右连续  $(\mathcal{F}_{t})$  下鞅,  $\tau$  和  $\sigma$  是有界停时且  $\sigma \leqslant \tau$ , 则  $X_{\sigma}$  和  $X_{\tau}$  是可积的且

$$
X _ {\sigma} \leqslant \mathbf {E} (X _ {\tau} | \mathcal {F} _ {\sigma}). \tag {2.5.6}
$$

证明 对  $n \geqslant 0$  令  $D_{n} = \{i/2^{n} : i = 0, 1, 2, \cdots\}$ . 再令  $\sigma_{n} = \inf\{t \in D_{n} : t > \sigma\}$  为  $\sigma$  的二分点离散化. 注意  $D_{n} \subseteq D_{n+1}$  且  $\sigma_{n}$  和  $\sigma_{n+1}$  都是值域为  $D_{n+1}$  的关于流  $(\mathcal{F}_{t} : t \in D_{n+1})$  的有界停时. 另外, 单调下降地  $\sigma_{n} \to \sigma$ . 所以应用离散时间杜布有界停止定理于  $(\mathcal{F}_{t} : t \in D_{n+1})$  下鞅  $(X_{t} : t \in D_{n+1})$  知  $X_{\sigma_{n}}$  与  $X_{\sigma_{n+1}}$  是可积的且

$$
X _ {\sigma_ {n + 1}} \leqslant \mathbf {E} (X _ {\sigma_ {n}} | \mathscr {F} _ {\sigma_ {n + 1}}).
$$

对 $k \leqslant 0$, 令 $Y_{k} = X_{\sigma_{-k}}$ 和 $\mathcal{G}_k = \mathcal{F}_{\sigma_{-k}}$. 上式说明 $(Y_k : k \leqslant 0)$ 是关于 $(\mathcal{G}_k : k \leqslant 0)$ 的下鞅. 对任何 $k \leqslant 0$ 我们有 $\mathbf{E}(Y_k) = \mathbf{E}(X_{\sigma_{-k}}) \geqslant \mathbf{E}(X_0)$. 由定理2.4.9, 当 $k \to -\infty$ 时 $Y_k$ 几乎必然且 $L^1$ 收敛于某个随机变量 $Y_{-\infty}$. 因为 $X$ 右连续, 当 $n \to \infty$ 时 $X_{\sigma_n} = Y_{-n}$ 几乎必然且 $L^1$ 收敛于 $X_{\sigma_+} = X_\sigma = Y_{-\infty}$. 再令 $\tau_n = \inf \{t \in D_n : t > \tau\}$ 为 $\tau$ 的二分点离散化. 与上面类似地可知, 当 $n \to \infty$ 时 $X_{\tau_n}$ 几乎必然且 $L^1$ 收敛于 $X_\tau = X_{\tau_+}$. 由于 $\tau_n \geqslant \sigma_n$, 应用离散时间杜布停止定理得 $X_{\sigma_n} \leqslant \mathbf{E}(X_{\tau_n} | \mathcal{F}_{\sigma_n})$. 所以, 对任何 $A \in \mathcal{F}_\sigma \subseteq \mathcal{F}_{\sigma_n}$ 有

$$
\mathbf {E} (X _ {\sigma_ {n}}; A) \leqslant \mathbf {E} [ \mathbf {E} (X _ {\tau_ {n}} | \mathcal {F} _ {\sigma_ {n}}); A ] = \mathbf {E} [ \mathbf {E} (X _ {\tau_ {n}} 1 _ {A} | \mathcal {F} _ {\sigma_ {n}}) ] = \mathbf {E} (X _ {\tau_ {n}}; A).
$$

在上式两端令 $n\to \infty$ ，并利用 $L^1$ 收敛性得

$$
\mathbf {E} (X _ {\sigma}; A) \leqslant \mathbf {E} (X _ {\tau}; A) = \mathbf {E} [ \mathbf {E} (X _ {\tau} 1 _ {A} | \mathcal {F} _ {\sigma}) ] = \mathbf {E} [ \mathbf {E} (X _ {\tau} | \mathcal {F} _ {\sigma}); A ].
$$

此蕴涵欲证不等式(2.5.6). □

推论 2.5.6 关于  $(\mathcal{F}_{t})$  适应的右连续可积过程 X 是鞅当且仅当对任何有界停时  $\sigma \leqslant \tau$  有  $\mathbf{E}(X_{\sigma}) = \mathbf{E}(X_{\tau})$ ，或等价地对任何有界停时  $\tau$  有  $\mathbf{E}(X_{\tau}) = \mathbf{E}(X_{0})$ .

下面定理的结论类似于定理 2.3.6, 说明一个右连续正上鞅在到达零点后, 会永远停留在零点.

定理 2.5.7 设 X 为非负右连续  $(\mathcal{F}_{t})$  上鞅. 令  $\tau = \inf\{t \geqslant 0 : X_{t} \text{ 或 } X_{t-} = 0\}$ . 则对任何  $t \geqslant 0$  有  $P\{X_{t} > 0, \tau < t\} = 0$ .

证明 根据定理 2.5.2 可以假定  $(\mathcal{F}_{t})$  右连续. 再由命题 2.1.21 知  $\tau_{n} := \inf\{t \geqslant 0 : X_{t} < 1/n\}$  为  $(\mathcal{F}_{t})$  停时. 当  $\tau_{n} < \infty$  时, 显然  $X_{\tau_{n}} \leqslant 1/n$ . 由定理 2.5.5 有  $\mathbf{E}(X_{t}|\mathcal{F}_{t \wedge \tau_{n}}) \leqslant X_{t \wedge \tau_{n}}$ . 注意  $\tau_{n} \leqslant \tau$  且  $\{\tau_{n} < t\} = \{t \wedge \tau_{n} < t\} \in \mathcal{F}_{t \wedge \tau_{n}}$ . 利用 X 的正性和上鞅性,

$$
\begin{array}{l} \mathbf {E} (X _ {t}; \tau <   t) \leqslant \mathbf {E} (X _ {t}; \tau_ {n} <   t) = \mathbf {E} [ \mathbf {E} (X _ {t} | \mathscr {F} _ {t \wedge \tau_ {n}}); \tau_ {n} <   t ] \\ \leqslant \mathbf {E} (X _ {t \wedge \tau_ {n}}; \tau_ {n} <   t) = \mathbf {E} (X _ {\tau_ {n}}; \tau_ {n} <   t) \leqslant 1 / n. \\ \end{array}
$$

由 $n \geqslant 1$ 的任意性, 我们有 $\mathbf{E}(X_t; \tau < t) = 0$, 故得定理结论. $\square$

## 2.5.3 下鞅不等式

通过对时间集进行可数稠子集逼近, 可以将关于离散时间下鞅的很多结果推广到连续时间情况. 为此, 取 $[0, \infty)$ 的可数稠子集 $D = \{r_1, r_2, \cdots\}$. 对 $t \geqslant 0$, 令 $D_n(t) = [0, t] \cap \{r_1, r_2, \cdots, r_n, t\}$. 注意, 对于任何右连续随机过程 $X = (X_t : t \geqslant 0)$ 有

$$
\sup _ {0 \leqslant s \leqslant t} X _ {s} = \lim _ {n \to \infty} \sup _ {s \in D _ {n} (t)} X _ {s}.
$$

应用离散时间情况的相应结果和法图定理, 可以推得关于右连续下鞅的不等式:

定理 2.5.8 设  $(X_{t})$  是右连续的  $(\mathcal{F}_{t})$  下鞅, 则对任何  $\lambda > 0$  及  $t \geqslant 0$  有

$$
\lambda \mathbf {P} \Big (\sup _ {0 \leqslant s \leqslant t} X _ {s} \geqslant \lambda \Big) \leqslant \mathbf {E} \Big (X _ {t}; \sup _ {0 \leqslant s \leqslant t} X _ {s} \geqslant \lambda \Big) \leqslant \mathbf {E} (X _ {t} ^ {+})
$$

和

$$
\lambda \mathbf {P} \Big (\sup _ {0 \leqslant s \leqslant t} | X _ {s} | \geqslant \lambda \Big) \leqslant 2 \mathbf {E} (X _ {t} ^ {+}) - \mathbf {E} (X _ {0}).
$$

推论 2.5.9 设  $(X_{t})$  是右连续的正  $(\mathcal{F}_{t})$  上鞅, 则对任何  $\lambda > 0$  及  $t \geqslant 0$  有

$$
\lambda \mathbf {P} \Big (\sup _ {s \geqslant 0} X _ {s} \geqslant \lambda \Big) = \lambda \mathbf {P} \Big (\sup _ {s \geqslant 0} | - X _ {s} | \geqslant \lambda \Big) \leqslant \mathbf {E} (X _ {0}).
$$

定理 2.5.10 设  $(X_{t})$  是右连续的  $(\mathcal{F}_{t})$  鞅或正下鞅, 则对任何  $\lambda > 0, p \geqslant 1$  及  $t \geqslant 0$  有

$$
\lambda^ {p} \mathbf {P} \Big (\sup _ {0 \leqslant s \leqslant t} | X _ {s} | \geqslant \lambda \Big) \leqslant \mathbf {E} (| X _ {t} | ^ {p});
$$

而对任何 $p > 1$ 及 $t \geqslant 0$ 有

$$
\mathbf {E} \Big (\sup _ {0 \leqslant s \leqslant t} | X _ {s} | ^ {p} \Big) \leqslant \Big (\frac {p}{p - 1} \Big) ^ {p} \mathbf {E} (| X _ {t} | ^ {p}).
$$

另外, 与离散时间的情况和定理 2.5.1 的证明类似地, 可以将鞅序列的收敛定理推广到连续时间的情况. 例如, 我们有:

定理 2.5.11 设  $(\mathcal{F}_{t})$  满足通常条件, 而  $(X_{t})$  是右连续下鞅且  $\sup_{t\geqslant0}P|X_{t}|<\infty$ , 则当  $t\to\infty$  时有  $X_{t}\stackrel{a.s.}{\rightarrow}X$ , 其中 X 是一个可积随机变量. 另外若  $(X_{t})$  是一致可积下鞅, 则  $X_{t}\stackrel{L^{1}}{\rightarrow}X$ ; 若  $(X_{t})$  是一致可积鞅, 则还有  $X_{t}=\mathbf{E}(X|\mathcal{F}_{t})$ .

连续时间下鞅的基本理论主要是法国数学家梅耶 (Paul-André Meyer) 建立的. 梅耶是著名的斯特拉斯堡概率论学派的领导者. 他最著名的工作之一是连续时间下鞅的杜布-梅耶分解定理, 即杜布的离散时间下鞅分解定理的连续时间版本.

## 练习题

1. 设 $\{(M_t, \mathcal{F}_t): t \geqslant 0\}$ 和 $\{(N_t, \mathcal{G}_t): t \geqslant 0\}$ 是连续时间鞅, 且 $\mathcal{F}_{\infty} := \sigma \left( \bigcup_{t \geqslant 0} \mathcal{F}_t \right)$ 和 $\mathcal{G}_{\infty} := \sigma \left( \bigcup_{t \geqslant 0} \mathcal{G}_t \right)$ 独立. 令 $\mathcal{H}_t = \sigma \left( \mathcal{F}_t \bigcup \mathcal{G}_t \right)$. 证明 $\{(M_t N_t, \mathcal{H}_t): t \geqslant 0\}$ 是鞅.
2. 设 $(M_t : t \geqslant 0)$ 为非负连续下鞅. 再设 $\{T_n\}$ 为有界单增停时列. 令 $T = \lim_{n \to \infty} T_n$. 证明 $\mathbf{E}(M_T) = \lim_{n \to \infty} \mathbf{E}(M_{T_n})$.
3. 设 $(M_t : t \geqslant 0)$ 是连续鞅且 $M_0 = 0$. 再设 $a < 0 < b$, 并令 $\tau = \inf \{t \geqslant 0 : M_t \notin [a, b]\}$. 已知 $\mathbf{P}(\tau < \infty) = 1$, 求概率 $\mathbf{P}(M_\tau = a)$ 和 $\mathbf{P}(M_\tau = b)$ 的值.
4. 通过对时间集进行可数稠子集逼近, 给出定理 2.5.10 的证明.
5. 设 $(M_t : t \geqslant 0)$ 是右连续平方可积鞅, 且对于有界停时 $T$ 有 $\mathbf{E}(M_T^2) = 0$. 证明 $\mathbf{P}(M_{t \wedge T} = 0 : t \geqslant 0) = 1$.
6. 设 $(M_t : t \geqslant 0)$ 是连续局部鞅且 $M_0 = 0$. 证明: 存在局部化序列 $\{T_k\}$ 使得每个 $(M_{t \wedge T_k})$ 是有界连续鞅.

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