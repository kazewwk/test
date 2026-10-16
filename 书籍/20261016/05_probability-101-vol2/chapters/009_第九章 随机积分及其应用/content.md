# 第九章 随机积分及其应用

原始 PDF 第 218–243 页。

224

第九章 随机积分及其应用

本章介绍关于布朗运动的随机积分理论及若干应用, 内容包括随机积分的定义、伊藤过程的伊藤公式、局部时和田中公式、随机微分方程、扩散过程与偏微分方程, 还讨论了几何布朗运动、奥恩斯坦-乌伦贝克过程等扩散过程的例子.

## 9.1 随机积分的定义

在本节中, 我们将定义一类循序可测过程相对于布朗运动的轨道的伊藤随机积分. 由于布朗运动的轨道在任何长度非零的区间上几乎必然有无限变差, 我们无法将其分解为两条单调不降轨道之差, 因此不能像黎曼-斯蒂尔切斯积分那样定义随机积分. 这里的思路是先定义简单过程的积分, 再用简单过程逼近循序可测过程, 然后通过 $L^2$ 收敛的极限来定义一般的随机积分.

## 9.1.1 简单过程的积分

设 $(\Omega, \mathcal{F}, \mathbf{P})$ 是完备概率空间且带有满足通常条件的连续时间流 $(\mathcal{F}_t : t \geqslant 0)$, 令 $(B_t : t \geqslant 0)$ 是 $(\mathcal{F}_t)$ 标准布朗运动且 $B_0 = 0$.

定义 9.1.1 我们称严格增的序列  $\pi=\{0=t_{0}<t_{1}<t_{2}<\cdots\}$  为  $[0,\infty)$  的分割.
称  $(\mathcal{F}_{t})$  适应随机过程  $\phi=\{\phi(t):t\geqslant0\}$  为简单过程, 是指存在  $[0,\infty)$  的分割  $\pi$  使得

$$
\phi (t) = \phi (0) 1 _ {\{0 \}} (t) + \sum_ {i = 1} ^ {\infty} \phi (t _ {i - 1}) 1 _ {(t _ {i - 1}, t _ {i} ]} (t), \quad t \geqslant 0, \tag {9.1.1}
$$

其中 $\phi(t_{i-1})$ 是 $\mathcal{F}_{t_{i-1}}$ 可测随机变量且有 $\mathbf{E}[\phi(t_{i-1})^2] < \infty$. 对于由 (9.1.1) 式给出的简单过程 $\phi$, 定义

$$
I _ {t} (\phi) = \sum_ {i = 1} ^ {\infty} \phi (t _ {i - 1}) (B _ {t _ {i} \wedge t} - B _ {t _ {i - 1} \wedge t}), \quad t \geqslant 0. \tag {9.1.2}
$$

我们指出, 如上定义的 $I_{t}(\phi)$ 并不依赖于简单过程 $\phi$ 的具体表示, 而且当 $t_{n} \leqslant t < t_{n+1}$ 时有

$$
I _ {t} (\phi) = \sum_ {i = 1} ^ {n} \phi (t _ {i - 1}) (B _ {t _ {i}} - B _ {t _ {i - 1}}) + \phi (t _ {n}) (B _ {t} - B _ {t _ {n}}). \tag {9.1.3}
$$

对于 $t \geqslant r \geqslant 0$ 定义

$$
\int_ {r} ^ {t} \phi (s) \mathrm{d} B _ {s} = I _ {t} (\phi) - I _ {r} (\phi). \tag {9.1.4}
$$

---

9.1 随机积分的定义

225

引理 9.1.1 由 (9.1.2) 式定义的随机过程  $\{I_{t}(\phi): t \geqslant 0\}$  是连续的平方可积  $(\mathcal{F}_{t})$  鞅.

证明 易知 $\{I_t(\phi): t \geqslant 0\}$ 是连续的 $(\mathcal{F}_t)$ 适应过程. 由布朗运动的独立增量性有

$$
\begin{array}{l} \mathbf {E} \big [ \phi (t _ {i - 1}) ^ {2} (B _ {t _ {i}} - B _ {t _ {i - 1}}) ^ {2} \big ] = \mathbf {E} \big \{\phi (t _ {i - 1}) ^ {2} \mathbf {E} \big [ (B _ {t _ {i}} - B _ {t _ {i - 1}}) ^ {2} | \mathscr {F} _ {t _ {i - 1}} \big ] \big \} \\ = (t _ {i} - t _ {i - 1}) \mathbf {E} [ \phi (t _ {i - 1}) ^ {2} ] <   \infty . \tag {9.1.5} \\ \end{array}
$$

因此 (9.1.3) 式的等号右边的每项都平方可积, 故 $I_{t}(\phi)$ 平方可积. 另外, 显然 (9.1.2) 式的等号右边的每项都是 $(\mathcal{F}_t)$ 鞅, 故 $\{I_t(\phi): t \geqslant 0\}$ 是 $(\mathcal{F}_t)$ 鞅. □

引理 9.1.2 对于任意的简单过程  $\phi$  和  $t \geqslant 0$  有

$$
\mathbf {E} \bigg \{\left[ \int_ {0} ^ {t} \phi (s) \mathrm{d} B _ {s} \right] ^ {2} \bigg \} = \mathbf {E} \Big [ \int_ {0} ^ {t} \phi (s) ^ {2} \mathrm{d} s \Big ].
$$

证明 令 $\Delta_{i}(t) = B_{t_{i}\wedge t} - B_{t_{i - 1}\wedge t}$. 若有 $i\neq j$ 和 $t_{i - 1} <   t_i\leqslant t_{j - 1}$, 则

$$
\begin{array}{l} \mathbf {E} \big [ \phi (t _ {i - 1}) \phi (t _ {j - 1}) \Delta_ {i} (t) \Delta_ {j} (t) \big ] = \mathbf {E} \big \{\mathbf {E} \big [ \phi (t _ {i - 1}) \phi (t _ {j - 1}) \Delta_ {i} (t) \Delta_ {j} (t) | \mathscr {F} _ {t _ {i - 1} \wedge t} \big ] \big \} \\ = \mathbf {E} \bigl \{\phi (t _ {i - 1}) \phi (t _ {j - 1}) \Delta_ {i} (t) \mathbf {E} [ \Delta_ {j} (t) | \mathcal {F} _ {t _ {i - 1} \wedge t} ] \bigr \}. \\ \end{array}
$$

根据布朗运动的独立正态增量性, 有 $\mathbf{E}[\Delta_j(t)|\mathscr{F}_{t_{i-1}\wedge t}] = 0$. 这样, 与 (9.1.5) 式类似地可以看到

$$
\begin{array}{l} \mathbf {E} \bigg \{\Big [ \int_ {0} ^ {t} \phi (s) \mathrm{d} B _ {s} \Big ] ^ {2} \bigg \} = \sum_ {i, j = 1} ^ {\infty} \mathbf {E} \big [ \phi (t _ {i - 1}) \phi (t _ {j - 1}) \varDelta_ {i} (t) \varDelta_ {j} (t) \big ] \\ = \sum_ {i = 0} ^ {\infty} \mathbf {E} \big [ \phi (t _ {i - 1}) ^ {2} \varDelta_ {i} (t) ^ {2} \big ] \\ = \sum_ {i = 0} ^ {\infty} \mathbf {E} [ \phi (t _ {i - 1}) ^ {2} ] (t _ {i} \wedge t - t _ {i} \wedge t). \\ \end{array}
$$

再利用富比尼定理即得欲证等式. □

## 9.1.2 循序可测过程的逼近

定义 9.1.2 令  $L^{2}$  是满足下面积分条件的  $(\mathcal{F}_{t})$  循序可测随机过程  $f = \{f(t) : t \geqslant 0\}$  的全体构成的集合:

$$
\mathbf {E} \Big [ \int_ {0} ^ {t} f (s) ^ {2} \mathrm{d} s \Big ] <   \infty , \quad t \geqslant 0. \tag {9.1.6}
$$

显然, 由 (9.1.1) 式给出的简单过程属于 $\mathcal{L}^2$. 我们下面将证明: 在一定意义下, 所有的简单过程构成 $\mathcal{L}^2$ 的一个稠密子集.

---

226

第九章 随机积分及其应用

引理 9.1.3 对于任何 $f \in \mathscr{L}^2$, 存在序列 $\{f_n\} \subseteq \mathscr{L}^2$ 使得每个 $f_n$ 都有界且

$$
\lim _ {n \to \infty} \mathbf {E} \Big [ \int_ {0} ^ {t} | f _ {n} (s) - f (s) | ^ {2} \mathrm{d} s \Big ] = 0, \quad t \geqslant 0. \tag {9.1.7}
$$

证明 对于 $n \geqslant 1$ 定义 $f_{n} = \{f_{n}(t): t \geqslant 0\}$ 如下:

$$
f _ {n} (t) = \left\{ \begin{array}{l l} - n, & f (t) <   - n, \\ f (t), & - n \leqslant f (t) \leqslant n, \\ n, & f (t) > n. \end{array} \right.
$$

显然  $f_{n}$  是  $(\mathcal{F}_{t})$  循序可测的, 且

$$
[ f _ {n} (t) - f (t) ] ^ {2} \leqslant 2 [ f _ {n} (t) ^ {2} + f (t) ^ {2} ] \leqslant 4 f (t) ^ {2}.
$$

由控制收敛定理知 (9.1.7) 式成立. □

引理 9.1.4 若 $f \in \mathcal{L}^2$ 是有界的, 则存在有界连续过程列 $\{g_n\} \subseteq \mathcal{L}^2$ 满足

$$
\lim _ {n \to \infty} \mathbf {E} \Big [ \int_ {0} ^ {t} | g _ {n} (s) - f (s) | ^ {2} \mathrm{d} s \Big ] = 0, \quad t \geqslant 0. \tag {9.1.8}
$$

证明 因为 $f$ 是 $(\mathcal{F}_t)$ 循序可测的, 映射 $(t,\omega)\mapsto f(t,\omega)$ 限制于 $[0,t]\times \Omega$ 关于乘积 $\sigma$ 代数 $\mathcal{B}([0,t]\times \mathcal{F}_t$ 可测. 对 $(t,\omega)\in [-1,\infty)\times \Omega$ 令

$$
F (t, \omega) = \int_ {- 1} ^ {t} f (s \vee 0, \omega) \mathrm{d} s,
$$

则 $\omega \mapsto F(t,\omega)$ 关于 $\mathcal{F}_{t\vee 0}$ 可测, 可参见 [23, p.90, Theorem 5.3]. 对于 $(t,\omega) \in [0,\infty) \times \Omega$, 令

$$
g _ {n} (t, \omega) = n [ F (t, \omega) - F (t - 1 / n, \omega) ],
$$

容易看出 $\omega \mapsto g_n(t, \omega)$ 关于 $\mathcal{F}_t$ 可测，所以过程 $g_n$ 是 $(\mathcal{F}_t)$ 循序可测的。由勒贝格定理，对每一个 $\omega \in \Omega$，当 $n \to \infty$ 时对几乎处处的 $t \geqslant 0$ 有 $g_n(t, \omega) \to h(t, \omega)$；参见 [17, p.275]。于是由控制收敛定理知 (9.1.8) 式成立。$\square$

引理 9.1.5 若  $g \in L^{2}$  是有界且连续的, 则存在简单过程列  $\{\phi_{n}\} \subseteq L^{2}$  满足

$$
\lim _ {n \to \infty} \mathbf {E} \Big [ \int_ {0} ^ {t} | \phi_ {n} (t) - g (t) | ^ {2} \mathrm{d} t \Big ] = 0, \quad t \geqslant 0. \tag {9.1.9}
$$

证明 定义有界的简单过程

$$
\phi_ {n} (t) = g (0) 1 _ {\{0 \}} (t) + \sum_ {i = 1} ^ {\infty} g ((i - 1) / n) 1 _ {((i - 1) / n, i / n ]} (t).
$$

显然, 对于任意的 $t \geqslant 0$ 和 $\omega \in \Omega$, 当 $n \to \infty$ 时有 $\phi_n(t, \omega) \to g(t, \omega)$. 根据控制收敛定理知 (9.1.9) 式成立. $\square$

---

9.1 随机积分的定义

227

综合引理 9.1.3, 引理 9.1.4 和引理 9.1.5, 我们得到如下的:

定理 9.1.6 对于任意的 $f \in \mathscr{L}^2$, 存在简单过程序列 $\{\phi_n\} \subseteq \mathscr{L}^2$ 满足

$$
\lim _ {n \to \infty} \mathbf {E} \Big [ \int_ {0} ^ {t} [ \phi_ {n} (t) - f (t) ] ^ {2} \mathrm{d} t \Big ] = 0, \quad t \geqslant 0. \tag {9.1.10}
$$

根据定理 9.1.6, 任意的过程  $f \in L^{2}$  都可以由一列简单过程  $\{\phi_{n}\} \subseteq L^{2}$  在 (9.1.10) 式的意义下逼近.

## 9.1.3 伊藤随机积分

引理 9.1.7 设  $f \in L^{2}$  和简单过程列  $\{\phi_{n}\} \subseteq L^{2}$  满足 (9.1.10) 式, 则对任意的  $t \geqslant 0$  极限  $\lim_{n \to \infty} I_{t}(\phi_{n})$  在  $L^{2}$  收敛意义下存在.

证明 令 $\lambda$ 表示实直线上的勒贝格测度. 则由 (9.1.10) 式知 $\{\phi_n\}$ 限制于 $[0, t] \times \Omega$ 是 $L^2([0, t] \times \Omega, \lambda \times \mathbf{P})$ 中的柯西列, 即对于任何 $\varepsilon > 0$, 存在 $N = N(\varepsilon)$ 使得

$$
\mathbf {E} \Big [ \int_ {0} ^ {t} | \phi_ {n} (s) - \phi_ {k} (s) | ^ {2} \mathrm{d} s \Big ] <   \varepsilon , \quad n \geqslant k \geqslant N.
$$

由引理9.1.2知

$$
\begin{array}{l} \mathbf {E} \big \{[ I _ {t} (\phi_ {n}) - I _ {t} (\phi_ {k}) ] ^ {2} \big \} = \mathbf {E} \bigg \{\Big [ \int_ {0} ^ {t} (\phi_ {n} (s) - \phi_ {k} (s)) \mathrm{d} B _ {s} \Big ] ^ {2} \bigg \} \\ = \mathbf {E} \bigg \{\int_ {0} ^ {t} (\phi_ {n} (s) - \phi_ {k} (s)) ^ {2} \mathrm{d} s \bigg \} <   \varepsilon . \\ \end{array}
$$

这说明随机变量序列 $\{I_t(\phi_n)\}$ 是 $L^2$ 收敛意义下的柯西列. 因此极限 $\lim_{n\to \infty}I_t(\phi_n)$ 在 $L^2$ 收敛意义下存在. □

定义 9.1.3 给定 $f \in \mathcal{L}^2$, 令 $\{\phi_n\} \subseteq \mathcal{L}^2$ 为满足 (9.1.10) 式的简单过程列. 我们利用 $L^2$ 收敛极限定义

$$
\int_ {0} ^ {t} f (s) \mathrm{d} B _ {s} = I _ {t} (f) := \lim _ {n \to \infty} I _ {t} (\phi_ {n}). \tag {9.1.11}
$$

更一般地, 对于有限 $(\mathcal{F}_t)$ 的停时 $\sigma \leqslant \tau$ 令

$$
\int_ {\sigma} ^ {\tau} f (s) \mathrm{d} B _ {s} = I _ {\tau} (f) - I _ {\sigma} (f), \tag {9.1.12}
$$

我们分别称 (9.1.11) 式和 (9.1.12) 式中的随机变量为过程 $f \in \mathcal{L}^2$ 相对于 $(\mathcal{F}_t)$ 标准布朗运动 $(B_t : t \geqslant 0)$ 在区间 $[0, t]$ 和 $[\sigma, \tau]$ 上的随机积分.

注意, 在几乎必然相等的意义下, (9.1.11) 式和 (9.1.12) 式中的随机变量不依赖于序列 $\{\phi_n\}$ 的选取.

---

228

第九章 随机积分及其应用

定理 9.1.8 对于 $f \in \mathcal{L}^2$, 由 (9.1.11) 式定义的过程 $\{I_t(f): t \geqslant 0\}$ 是平方可积的 $(\mathscr{F}_t)$ 鞅.

证明 若 $f \in \mathcal{L}^2$ 是简单过程, 则结论由引理 9.1.1 可知. 由于 (9.1.11) 式在 $L^2$ 收敛意义下成立, 该结论对一般的 $f \in \mathcal{L}^2$ 也成立. $\square$

定理 9.1.9 (伊藤等距) 对于任意的 $t \geqslant 0$ 和 $f \in \mathscr{L}^2$ 有

$$
\mathbf {E} \Big \{\Big [ \int_ {0} ^ {t} f (s) \mathrm{d} B _ {s} \Big ] ^ {2} \Big \} = \mathbf {E} \Big [ \int_ {0} ^ {t} f (s) ^ {2} \mathrm{d} s \Big ]. \tag {9.1.13}
$$

证明 由(9.1.11)式和引理9.1.2立即得证. $\square$

定理 9.1.10 对于 $f \in \mathcal{L}^2$ 由 (9.1.11) 式定义的平方可积 $(\mathcal{F}_t)$ 鞅 $\{I_t(f): t \geqslant 0\}$ 有连续的修正.

证明 令 $\{\phi_n\} \subseteq \mathcal{L}^2$ 为满足 (9.1.10) 式的简单过程列. 对 $\{I_t(\phi_n) - I_t(\phi_m): t \geqslant 0\}$ 应用鞅不等式可得

$$
\begin{array}{l} \mathbf {E} \Big \{\sup _ {0 \leqslant s \leqslant t} | I _ {s} (\phi_ {n}) - I _ {s} (\phi_ {m}) | ^ {2} \Big \} \leqslant 4 \mathbf {E} [ | I _ {t} (\phi_ {n}) - I _ {t} (\phi_ {m}) | ^ {2} ] \\ = 4 \mathbf {E} \Big [ \int_ {0} ^ {t} (\phi_ {n} (s) - \phi_ {m} (s)) ^ {2} \mathrm{d} s \Big ], \tag {9.1.14} \\ \end{array}
$$

故对 $\varepsilon > 0$ 有

$$
\mathbf {P} \Bigl \{\sup _ {0 \leqslant s \leqslant t} | I _ {s} (\phi_ {n}) - I _ {s} (\phi_ {m}) | \geqslant \varepsilon \Bigr \} \leqslant \frac {4}{\varepsilon^ {2}} \mathbf {E} \Bigl [ \int_ {0} ^ {t} (\phi_ {n} (s) - \phi_ {m} (s)) ^ {2} \mathrm{d} s \Bigr ].
$$

上式右边当 $n, m \to \infty$ 时趋于零. 因此可以选择递增的数列 $n_k \to \infty$ 使得

$$
\mathbf {P} \Big \{\sup _ {0 \leqslant s \leqslant t} | I _ {s} (\phi_ {n}) - I _ {s} (\phi_ {n _ {k}}) | \geqslant 2 ^ {- k} \Big \} <   2 ^ {- k}, \quad n \geqslant n _ {k},
$$

进而

$$
\sum_ {k = 1} ^ {\infty} \mathbf {P} \Bigl \{\sup _ {0 \leqslant s \leqslant t} | I _ {s} (\phi_ {n _ {k}}) - I _ {s} (\phi_ {n _ {k + 1}}) | \geqslant 2 ^ {- k} \Bigr \} <   \infty .
$$

根据博雷尔-坎泰利引理可知

$\mathbf{P}\Big\{\sup_{0\leqslant s\leqslant t}|I_s(\phi_{n_k}) - I_s(\phi_{n_{k + 1}})|\geqslant 2^{-k}$ 对无穷多个 $k\geqslant 1$ 成立 $\Big\} = 0,$

即存在 $N \in \mathcal{F}_0$ 满足 $\mathbf{P}(N) = 0$ 且对每个 $\omega \in N^c$ 有 $l(\omega) \geqslant 1$ 使得

$$
\sup _ {0 \leqslant s \leqslant t} | I _ {s} (\phi_ {n _ {k}}, \omega) - I _ {s} (\phi_ {n _ {k + 1}}, \omega) | <   2 ^ {- k}, \quad k \geqslant l (\omega). \tag {9.1.15}
$$

---

9.1 随机积分的定义

229

注意对 $\omega \in N^{c}$ 有

$$
I _ {t} (\phi_ {n _ {k}}, \omega) = I _ {t} (\phi_ {n _ {1}}, \omega) + \sum_ {i = 1} ^ {k - 1} [ I _ {t} (\phi_ {n _ {i + 1}}, \omega) - I _ {t} (\phi_ {n _ {i}}, \omega) ],
$$

由 (9.1.15) 式易知对任何 $T > 0$ 上式等号右边的级数当 $k \to \infty$ 时关于 $t \in [0, T]$ 一致收敛. 令

$$
J _ {t} (f, \omega) = \lim _ {k \to \infty} I _ {t} (\phi_ {n _ {k}}, \omega) 1 _ {N ^ {c}} (\omega).
$$

显然 $\{J_t(f): t \geqslant 0\}$ 为 $(\mathcal{F}_t)$ 适应连续过程. 在 (9.1.14) 式两端令 $m = n_k \to \infty$ 并应用法图定理得

$$
\mathbf {E} \Big \{\sup _ {0 \leqslant s \leqslant t} | I _ {s} (\phi_ {n}) - J _ {s} (\phi) | ^ {2} \Big \} \leqslant 4 \mathbf {E} \Big [ \int_ {0} ^ {t} (\phi_ {n} (s) - \phi (s)) ^ {2} \mathrm{d} s \Big ],
$$

因而在 $L^2$ 收敛意义下有 $J_{t}(f) = \lim_{n\to \infty}I_{t}(\phi_{n}) = I_{t}(f)$. 所以 $\{J_t(f):t\geqslant 0\}$ 是 $\{I_t(f):t\geqslant 0\}$ 的连续修正. □

根据定理 9.1.10, 对于 $f \in \mathscr{L}^2$ 由 (9.1.11) 式定义的随机积分过程 $\{I_t(f): t \geqslant 0\}$ 有平方可积的连续 $(\mathscr{F}_t)$ 鞅修正. 我们规定后面 $\{I_t(f): t \geqslant 0\}$ 总表示这样的修正.

命题 9.1.11 (1) 对于  $t \geqslant 0$  和  $f, h \in L^{2}$  有

$$
\int_ {0} ^ {t} [ f (s) + h (s) ] \mathrm{d} B _ {s} = \int_ {0} ^ {t} f (s) \mathrm{d} B _ {s} + \int_ {0} ^ {t} h (s) \mathrm{d} B _ {s}.
$$

(2) 对于 $t \geqslant r \geqslant 0$ 和 $f \in \mathcal{L}^2$ 有

$$
\int_ {r} ^ {t} f (s) \mathrm{d} B _ {s} = \int_ {0} ^ {t} f (s) \mathrm{d} B _ {s} - \int_ {0} ^ {r} f (s) \mathrm{d} B _ {s}.
$$

(3) 对于 $t \geqslant r \geqslant 0, \eta \in \mathrm{b}\mathcal{F}_r$ 和 $f \in \mathcal{L}^2$ 有

$$
\eta \int_ {r} ^ {t} f (s) \mathrm{d} B _ {s} = \int_ {0} ^ {t} 1 _ {\{s \geqslant r \}} \eta f (s) \mathrm{d} B _ {s}.
$$

证明 性质 (1) 对简单过程 $f, h \in \mathcal{L}^2$ 显然, 对一般循序可测过程 $f, h \in \mathcal{L}^2$ 可利用 (9.1.11) 式导出. 性质 (2) 是 (9.1.12) 式的直接推论. 性质 (3) 也可通过简单过程逼近得到. □

命题 9.1.12 令  $h=\{h(t):t\geqslant0\}$  是  $[0,\infty)$  上的确定性的连续函数且满足

$$
\sigma (t) := \int_ {0} ^ {t} h (s) ^ {2} \mathrm{d} s <   \infty , \quad t > 0,
$$

则伊藤积分

$$
Z (t) := \int_ {0} ^ {t} h (s) \mathrm{d} B _ {s}
$$

服从方差为  $\sigma(t)$  的零均值正态分布.

---

230

第九章 随机积分及其应用

证明 固定  $t \geqslant 0$ . 对于  $n \geqslant 1$  定义确定性的简单过程  $\phi_{n} \in L^{2}$  如下:

$$
\phi_ {n} (s) = \sum_ {i = 1} ^ {n} h ((i - 1) t / n) 1 _ {((i - 1) t / n, i t / n ]} (s), \quad s \geqslant 0.
$$

容易看出

$$
\lim _ {n \to \infty} \int_ {0} ^ {t} [ \phi_ {n} (s) - h (s) ] ^ {2} \mathrm{d} s = 0.
$$

由伊藤积分的定义, 在  $L^{2}$  收敛的意义下有

$$
Z (t) = \lim _ {n \to \infty} \int_ {0} ^ {t} \phi_ {n} (s) \mathrm{d} B _ {s} = \lim _ {n \to \infty} \sum_ {i = 1} ^ {n} h ((i - 1) t / n) (B _ {i t / n} - B _ {(i - 1) t / n}).
$$

由布朗运动的性质不难看出, 上面和式定义的随机变量服从零均值正态分布, 其方差为

$$
\sum_ {i = 1} ^ {n} h ((i - 1) t / n) ^ {2} [ i t / n - (i - 1) t / n ] = \sum_ {i = 1} ^ {n} h ((i - 1) t / n) ^ {2} t / n.
$$

当 $n\to \infty$ 时该方差收敛到 $\sigma (t)$ ，所以 $Z(t)$ 服从方差为 $\sigma (t)$ 的零均值正态分布.□

命题 9.1.13 设  $(B_{t}: t \geqslant 0)$  为标准布朗运动, 则对任意的  $t \geqslant 0$  有

$$
B _ {t} ^ {2} = B _ {0} ^ {2} + 2 \int_ {0} ^ {t} B _ {s} \mathrm{d} B _ {s} + t.
$$

证明 固定 $t \geqslant 0$. 对于 $n \geqslant 1$ 定义简单过程 $\phi_n \in \mathcal{L}^2$ 如下:

$$
\phi_ {n} (s) = \sum_ {i = 1} ^ {\infty} B _ {(i - 1) t / n} 1 _ {((i - 1) t / n, i t / n ]} (s), \quad s \geqslant 0. \tag {9.1.16}
$$

则当 $n\to \infty$ 时有

$$
\begin{array}{l} \mathbf {E} \Big \{\int_ {0} ^ {t} [ \phi_ {n} (s) - B _ {s} ] ^ {2} \mathrm{d} s \Big \} = \mathbf {E} \Big [ \sum_ {i = 1} ^ {n} \int_ {(i - 1) t / n} ^ {i t / n} (B _ {(i - 1) t / n} - B _ {s}) ^ {2} \mathrm{d} s \Big ] \\ = \sum_ {i = 1} ^ {n} \int_ {(i - 1) t / n} ^ {i t / n} \mathbf {E} [ (B _ {(i - 1) t / n} - B _ {s}) ^ {2} ] \mathrm{d} s \\ = \sum_ {i = 1} ^ {n} \int_ {(i - 1) t / n} ^ {i t / n} [ s - (i - 1) t / n ] \mathrm{d} s \\ = n \int_ {0} ^ {t / n} s \mathrm{d} s = \frac {t ^ {2}}{2 n} \rightarrow 0. \\ \end{array}
$$

根据伊藤积分的定义, 在  $L^{2}$  收敛的意义下有

$$
\int_ {0} ^ {t} B _ {s} \mathrm{d} B _ {s} = \lim _ {n \to \infty} \int_ {0} ^ {t} \phi_ {n} (s) \mathrm{d} B _ {s}.
$$

---

9.1 随机积分的定义

231

再注意

$$
\begin{array}{l} B _ {t} ^ {2} - B _ {0} ^ {2} = \sum_ {i = 1} ^ {n} (B _ {i t / n} ^ {2} - B _ {(i - 1) t / n} ^ {2}) \\ = \sum_ {i = 1} ^ {n} \left[ (B _ {i t / n} - B _ {(i - 1) t / n}) ^ {2} + 2 B _ {(i - 1) t / n} (B _ {i t / n} - B _ {(i - 1) t / n}) \right] \\ = \sum_ {i = 1} ^ {n} (B _ {i t / n} - B _ {(i - 1) t / n}) ^ {2} + 2 \int_ {0} ^ {t} \phi_ {n} (s) \mathrm{d} B _ {s}. \\ \end{array}
$$

在上式两端令 $n\to \infty$ ，并应用定理1.3.5即得欲证等式.□

例 9.1.1 固定  $t \geqslant 0$ . 对于  $n \geqslant 1$  定义

$$
I _ {n} (t) = \sum_ {i = 1} ^ {n} B _ {(i - 1) t / n} (B _ {i t / n} - B _ {(i - 1) t / n}).
$$

注意上式可以写成简单过程的随机积分

$$
I _ {n} (t) = \int_ {0} ^ {t} \phi_ {n} (s) \mathrm{d} B _ {s},
$$

其中 $\phi_n \in \mathcal{L}^2$ 由 (9.1.16) 式给出. 根据命题 9.1.13 的证明, 在 $L^2$ 收敛意义下有

$$
\lim _ {n \to \infty} I _ {n} (t) = \int_ {0} ^ {t} B _ {s} \mathrm{d} B _ {s}.
$$

## 练习题

1. 固定 $t > 0$. 对于 $n \geqslant 1$ 定义

$$
J _ {n} (t) = \sum_ {i = 1} ^ {n} B _ {i t / n} (B _ {i t / n} - B _ {(i - 1) t / n}).
$$

极限关系

$$
\lim _ {n \to \infty} J _ {n} (t) = \int_ {0} ^ {t} B _ {s} \mathrm{d} B _ {s}
$$

在 $L^2$ 收敛意义下是否成立？为什么？

提示: 不成立. 所给等式右边是零均值的平方可积鞅. 但另一方面, 有

$$
\begin{array}{l} \mathbf {E} [ J _ {n} (t) ] = \sum_ {i = 1} ^ {n} \mathbf {E} \big [ B _ {i t / n} (B _ {i t / n} - B _ {(i - 1) t / n}) \big ] \\ = \sum_ {i = 1} ^ {n} \left\{\mathbf {E} \left[ B _ {i t / n} (B _ {i t / n} - B _ {(i - 1) t / n}) \right] + \right. \\ \end{array}
$$

---

232

第九章 随机积分及其应用

$$
\begin{array}{l} \left. \mathbf {E} \left[ B _ {(i - 1) t / n} \left(B _ {i t / n} - B _ {(i - 1) t / n}\right) \right] \right\} \\ = \sum_ {i = 1} ^ {n} \mathbf {E} [ (B _ {i t / n} - B _ {(i - 1) t / n}) ^ {2} ] = \sum_ {i = 1} ^ {n} t / n = t. \\ \end{array}
$$

因此, 所给极限关系对 t > 0 不成立.

2. 利用伊藤积分的定义直接证明

(1) $tB_{t} = \int_{0}^{t}s\mathrm{d}B_{s} + \int_{0}^{t}B_{s}\mathrm{d}s;\quad (2)B_{t}^{3} = 3\int_{0}^{t}B_{s}^{2}\mathrm{d}B_{s} + 3\int_{0}^{t}B_{s}\mathrm{d}s.$

3. 证明 $M_{t} := B_{t}^{3} - 3tB_{t}$ 是连续的平方可积鞅.

4. 令 $t \geqslant r \geqslant 0$. 设 $f \in \mathcal{L}^2$ 而 $\xi$ 是 $\mathscr{F}_r$ 可测随机变量且有

$$
\mathbf {E} \bigg [ \int_ {0} ^ {t} \xi^ {2} f (s) ^ {2} \mathrm{d} s \bigg ] <   \infty .
$$

证明:

$$
\int_ {r} ^ {t} \xi f (s) \mathrm{d} B _ {s} = \xi \int_ {r} ^ {t} f (s) \mathrm{d} B _ {s}.
$$

## 9.2 伊藤公式

我们知道,链式法则是黎曼积分理论中非常重要的基本公式.在随机积分理论中,最重要的公式之一是随机版本的链式法则,即伊藤公式.本节中我们分别给出布朗运动和伊藤过程的伊藤公式.

## 9.2.1 布朗运动的伊藤公式

引理 9.2.1 设  $\{g(t):t\geqslant0\}$  是有界连续  $(\mathcal{F}_{t})$  循序可测过程. 对每个  $n\geqslant1$  取区间  $[0,t]$  的分割

$$
\pi_ {n} := \{0 = t _ {n, 0} <   t _ {n, 1} <   \dots <   t _ {n, k _ {n}} = t \}.
$$

再设当 $n\to \infty$ 时有 $\delta_n\coloneqq \max_{i}(t_{n,i + 1} - t_{n,i})\to 0.$ 则当 $n\to \infty$ 时在 $L^2$ 收敛意义下有

$$
Y _ {n} (t) := \sum_ {i = 1} ^ {k _ {n}} g (t _ {n, i - 1}) (B _ {t _ {n, i}} - B _ {t _ {n, i - 1}}) ^ {2} \rightarrow \int_ {0} ^ {t} g (s) \mathrm{d} s. \tag {9.2.1}
$$

证明 为了简单起见, 在此证明中我们写 $t_{n,i}$ 为 $t_i$. 注意当 $n \to \infty$ 时几乎必然地

$$
Z _ {n} (t) := \sum_ {i = 1} ^ {k _ {n}} g (t _ {i - 1}) (t _ {i} - t _ {i - 1}) \rightarrow \int_ {0} ^ {t} g (s) \mathrm{d} s. \tag {9.2.2}
$$

---

9.2 伊藤公式

233

由控制收敛定理, 上述极限在  $L^{2}$  收敛意义下也成立. 另一方面, 根据命题 9.1.13 有

$$
B _ {t _ {i}} ^ {2} - B _ {t _ {i - 1}} ^ {2} = 2 \int_ {t _ {i - 1}} ^ {t _ {i}} B _ {s} \mathrm{d} B _ {s} + (t _ {i} - t _ {i - 1}),
$$

所以

$$
\begin{array}{l} Y _ {n} (t) - Z _ {n} (t) = \sum_ {i = 1} ^ {k _ {n}} g (t _ {i - 1}) \big [ (B _ {t _ {i}} - B _ {t _ {i - 1}}) ^ {2} - (t _ {i} - t _ {i - 1}) \big ] \\ = \sum_ {i = 1} ^ {k _ {n}} g (t _ {i - 1}) \big [ (B _ {t _ {i}} ^ {2} - B _ {t _ {i - 1}} ^ {2}) - (t _ {i} - t _ {i - 1}) - 2 B _ {t _ {i - 1}} (B _ {t _ {i}} - B _ {t _ {i - 1}}) \big ] \\ = 2 \sum_ {i = 1} ^ {k _ {n}} g (t _ {i - 1}) \Big [ \int_ {t _ {i - 1}} ^ {t _ {i}} B _ {s} \mathrm{d} B _ {s} - B _ {t _ {i - 1}} (B _ {t _ {i}} - B _ {t _ {i - 1}}) \Big ]. \\ \end{array}
$$

定义简单过程

$$
g _ {n} (s) = \sum_ {i = 1} ^ {k _ {n}} g (t _ {i - 1}) 1 _ {(t _ {i - 1}, t _ {i} ]} (s), \quad B _ {n} (s) = \sum_ {i = 1} ^ {k _ {n}} B _ {t _ {i - 1}} 1 _ {(t _ {i - 1}, t _ {i} ]} (s), \tag {9.2.3}
$$

则有

$$
\begin{array}{l} Y _ {n} (t) - Z _ {n} (t) = 2 \sum_ {i = 1} ^ {k _ {n}} \Big [ \int_ {t _ {i - 1}} ^ {t _ {i}} g _ {n} (s) B _ {s} \mathrm{d} B _ {s} - \int_ {t _ {i - 1}} ^ {t _ {i}} g _ {n} (s) B _ {n} (s) \mathrm{d} B _ {s} \Big ] \\ = 2 \int_ {0} ^ {t} g _ {n} (s) (B _ {s} - B _ {n} (s)) \mathrm{d} B _ {s}. \\ \end{array}
$$

令 C > 0 是  $\{g(s) : s \geqslant 0\}$  的一个上界, 根据伊藤等距公式有

$$
\begin{array}{l} \mathbf {E} \big \{[ Y _ {n} (t) - Z _ {n} (t) ] ^ {2} \big \} = 4 \int_ {0} ^ {t} \mathbf {E} \big \{[ g _ {n} (s) (B _ {s} - B _ {n} (s)) ] ^ {2} \big \} \mathrm{d} s \\ \leqslant 4 C ^ {2} \int_ {0} ^ {t} \mathbf {E} \{[ B _ {s} - B _ {n} (s) ] ^ {2} \} \mathrm{d} s \\ = 4 C ^ {2} \sum_ {i = 1} ^ {k _ {n}} \int_ {t _ {i - 1}} ^ {t _ {i}} (s - t _ {i - 1}) \mathrm{d} s = 2 C ^ {2} \sum_ {i = 1} ^ {k _ {n}} (t _ {i} - t _ {i - 1}) ^ {2}. \\ \end{array}
$$

显然当 $n\to \infty$ 时上式右端趋近于零.再结合(9.2.2)式即得(9.2.1)式.□

定理 9.2.2（伊藤公式） 设 f 是 R 上的二次连续可微函数, 其对任意的  $t \geqslant 0$  满足

$$
\mathbf {E} \Big [ \int_ {0} ^ {t} f ^ {\prime} (B _ {s}) ^ {2} \mathrm{d} s \Big ] <   \infty . \tag {9.2.4}
$$

则有

$$
f (B _ {t}) - f (B _ {0}) = \int_ {0} ^ {t} f ^ {\prime} (B _ {s}) \mathrm{d} B _ {s} + \frac {1}{2} \int_ {0} ^ {t} f ^ {\prime \prime} (B _ {s}) \mathrm{d} s. \tag {9.2.5}
$$

---

234

第九章 随机积分及其应用

证明 我们仅对 $f'$ 和 $f''$ 有界的情形进行证明. 对 $n \geqslant 1$ 令 $\pi_n$ 是如引理9.2.1中给定的区间 $[0, t]$ 的分割. 下面简写 $t_{n,i}$ 为 $t_i$. 根据泰勒展式,

$$
\begin{array}{l} f (B _ {t}) - f (B _ {0}) = \sum_ {i = 1} ^ {k _ {n}} [ f (B _ {t _ {i}}) - f (B _ {t _ {i - 1}}) ] \\ = \sum_ {i = 1} ^ {k _ {n}} \left[ f ^ {\prime} (B _ {t _ {i - 1}}) (B _ {t _ {i}} - B _ {t _ {i - 1}}) + \frac {1}{2} f ^ {\prime \prime} (\xi_ {i}) (B _ {t _ {i}} - B _ {t _ {i - 1}}) ^ {2} \right] \\ = \int_ {0} ^ {t} f ^ {\prime} (B _ {n} (s)) \mathrm{d} B _ {s} + \frac {1}{2} \sum_ {i = 1} ^ {k _ {n}} f ^ {\prime \prime} (B _ {t _ {i}}) (B _ {t _ {i}} - B _ {t _ {i - 1}}) ^ {2} + \\ \frac {1}{2} \sum_ {i = 1} ^ {k _ {n}} \left[ f ^ {\prime \prime} (\xi_ {i}) - f ^ {\prime \prime} (B _ {t _ {i - 1}}) \right] (B _ {t _ {i}} - B _ {t _ {i - 1}}) ^ {2}, \\ \end{array}
$$

其中 $\xi_{i}$ 是 $B_{t_{i - 1}}$ 和 $B_{t_i}$ 之间的某个点, 而 $\{B_n(s)\}$ 是由 (9.2.3) 式定义的简单过程. 由伊藤等距公式,

$$
\begin{array}{l} \mathbf {E} \Bigg \{\Big [ \int_ {0} ^ {t} f ^ {\prime} (B _ {n} (s)) \mathrm{d} B _ {s} - \int_ {0} ^ {t} f ^ {\prime} (B _ {s}) \mathrm{d} B _ {s} \Big ] ^ {2} \Bigg \} \\ = \mathbf {E} \left\{\left[ \int_ {0} ^ {t} [ f ^ {\prime} (B _ {n} (s)) - f ^ {\prime} (B _ {s}) ] \mathrm{d} B _ {s} \right] ^ {2} \right\} \\ = \int_ {0} ^ {t} \mathbf {E} \{[ f ^ {\prime} (B _ {n} (s)) - f ^ {\prime} (B _ {s}) ] ^ {2} \} \mathrm{d} s. \\ \end{array}
$$

由控制收敛定理, 上式右端当 $n \to \infty$ 时趋于零. 这说明在 $L^2$ 收敛意义下有

$$
\int_ {0} ^ {t} f ^ {\prime} (B _ {n} (s)) \mathrm{d} B _ {s} \rightarrow \int_ {0} ^ {t} f ^ {\prime} (B _ {s}) \mathrm{d} B _ {s}. \tag {9.2.6}
$$

根据引理 9.2.1, 在  $L^{2}$  收敛意义下有

$$
\sum_ {i = 1} ^ {k _ {n}} f ^ {\prime \prime} (B _ {t _ {i - 1}}) (B _ {t _ {i}} - B _ {t _ {i - 1}}) ^ {2} \rightarrow \int_ {0} ^ {t} f ^ {\prime \prime} (B _ {s}) \mathrm{d} s. \tag {9.2.7}
$$

注意

$$
\begin{array}{l} \Big | \sum_ {i = 1} ^ {k _ {n}} \big [ f ^ {\prime \prime} (\xi_ {i}) - f ^ {\prime \prime} (B _ {t _ {i - 1}}) \big ] (B _ {t _ {i}} - B _ {t _ {i - 1}}) ^ {2} \Big | \\ \leqslant \max _ {1 \leqslant i \leqslant k _ {n}} \left| f ^ {\prime \prime} (\xi_ {i}) - f ^ {\prime \prime} (B _ {t _ {i - 1}}) \right| \sum_ {i = 1} ^ {k _ {n}} (B _ {t _ {i}} - B _ {t _ {i - 1}}) ^ {2}. \\ \end{array}
$$

根据布朗运动的轨道的连续性, 几乎必然地  $\max_{i}|f''(\xi_{i})-f''(B_{t_{i-1}})|\to0$ , 故由定理 1.3.5 易知上式右边依概率收敛于零. 再综合 (9.2.6) 式和 (9.2.7) 式, 即得 (9.2.5) 式. ☐

例 9.2.1 由布朗运动的伊藤公式知  $X_{t} = e^{B_{t}}$  满足方程

$$
X _ {t} = 1 + \int_ {0} ^ {t} X _ {s} \mathrm{d} B _ {s} + \frac {1}{2} \int_ {0} ^ {t} X _ {s} \mathrm{d} s, \quad t \geqslant 0.
$$

---

9.2 伊藤公式

235

## 9.2.2 伊藤过程的伊藤公式

定义 9.2.1 令  $(B_{t}: t \geqslant 0)$  是  $(\mathcal{F}_{t})$  标准布朗运动. 称随机过程  $(X_{t}: t \geqslant 0)$  为伊藤过程, 是指它有下面的表示

$$
X _ {t} = X _ {0} + \int_ {0} ^ {t} v (s) \mathrm{d} B _ {s} + \int_ {0} ^ {t} u (s) \mathrm{d} s, \quad t \geqslant 0, \tag {9.2.8}
$$

其中 $v = \{v(t):t\geqslant 0\} \in \mathcal{L}^2$ 而 $u = \{u(t):t\geqslant 0\}$ 是 $(\mathcal{F}_t)$ 循序可测过程且满足

$$
\int_ {0} ^ {t} | u (s) | \mathrm{d} s <   \infty , \quad t \geqslant 0.
$$

为了表达上的简单, 在定义 9.2.1 的情况下, 我们经常将 (9.2.8) 式写成其微分形式:

$$
\mathrm{d} X _ {t} = v (t) \mathrm{d} B _ {t} + u (t) \mathrm{d} t, \quad t \geqslant 0. \tag {9.2.9}
$$

在本小节中, 我们将给出伊藤过程的函数所对应的伊藤公式. 这里的证明的基本想法和上节的非常类似. 因此这里只给出证明的概要.

定理 9.2.3 设  $v \in L^{2}$ . 对  $n \geqslant 1$  令  $\pi_{n}$  是如引理 9.2.1 中给定的区间  $[0, t]$  的分割, 则当  $n \to \infty$  时在  $L^{2}$  收敛意义下有

$$
\sum_ {j = 1} ^ {k _ {n}} \left[ I _ {t _ {n, j}} (v) - I _ {t _ {n, j - 1}} (v) \right] ^ {2} \rightarrow \int_ {0} ^ {t} v (s) ^ {2} \mathrm{d} s. \tag {9.2.10}
$$

证明 (概要) 只考虑 $v \in \mathcal{L}^2$ 是有界连续过程的情况. 为简单起见, 依然简写 $t_{n,j}$ 为 $t_j$. 于是当 $n \to \infty$ 时有

$$
\begin{array}{l} \sum_ {j = 1} ^ {k _ {n}} \left[ I _ {t _ {n, j}} (v) - I _ {t _ {n, j - 1}} (v) \right] ^ {2} = \sum_ {j = 1} ^ {k _ {n}} \left[ \int_ {t _ {j - 1}} ^ {t _ {j}} v (s) \mathrm{d} B _ {s} \right] ^ {2} \\ = \sum_ {j = 1} ^ {k _ {n}} v (t _ {j - 1}) ^ {2} (B _ {t _ {j}} - B _ {t _ {j - 1}}) ^ {2} + o (1). \\ \end{array}
$$

根据引理 9.2.1 即得 (9.2.10) 式. □

定理 9.2.4（伊藤公式）令  $(X_{t}: t \geqslant 0)$  是由 (9.2.8) 式给出的伊藤过程。设  $[0, \infty) \times \mathbb{R}$  上的函数  $f = f(t, x)$  对 t 一次连续可微而对 x 二次连续可微。若对  $t \geqslant 0$  有

$$
\mathbf {E} \bigg [ \int_ {0} ^ {t} f _ {x} ^ {\prime} (s, X _ {s}) ^ {2} v (s) ^ {2} \mathrm{d} s \bigg ] <   \infty ,
$$

则有

$$
\begin{array}{l} f (t, X _ {t}) - f (0, X _ {0}) = \int_ {0} ^ {t} f _ {x} ^ {\prime} (s, X _ {s}) v (s) \mathrm{d} B _ {s} + \int_ {0} ^ {t} f _ {x} ^ {\prime} (s, X _ {s}) u (s) \mathrm{d} s + \\ \int_ {0} ^ {t} f _ {t} ^ {\prime} (s, X _ {s}) \mathrm{d} s + \frac {1}{2} \int_ {0} ^ {t} f _ {x x} ^ {\prime \prime} (s, X _ {s}) v (s) ^ {2} \mathrm{d} s. \tag {9.2.11} \\ \end{array}
$$

---

236

第九章 随机积分及其应用

证明 (概要) 对 $n \geqslant 1$ 令 $\pi_n$ 是如引理 9.2.1 中给定的区间 $[0, t]$ 的分割, 简写 $t_{n,i}$ 为 $t_i$, 则当 $n \to \infty$ 时有

$$
\begin{array}{l} f (t, X _ {t}) - f (0, X _ {0}) = \sum_ {i = 1} ^ {k _ {n}} \left[ f (t _ {i}, X _ {t _ {i}}) - f (t _ {i}, X _ {t _ {i - 1}}) \right] + \\ \sum_ {i = 1} ^ {k _ {n}} \left[ f (t _ {i}, X _ {t _ {i - 1}}) - f (t _ {i - 1}, X _ {t _ {i - 1}}) \right] \\ = \sum_ {i = 1} ^ {k _ {n}} f _ {x} ^ {\prime} (t _ {i}, X _ {t _ {i - 1}}) (X _ {t _ {i}} - X _ {t _ {i - 1}}) + \\ \frac {1}{2} \sum_ {i = 1} ^ {k _ {n}} f _ {x x} ^ {\prime \prime} (t _ {i}, X _ {t _ {i - 1}}) (X _ {t _ {i}} - X _ {t _ {i - 1}}) ^ {2} + \\ \sum_ {i = 1} ^ {k _ {n}} f _ {t} ^ {\prime} (t _ {i - 1}, X _ {t _ {i - 1}}) (t _ {i} - t _ {i - 1}) + o (1). \\ \end{array}
$$

根据命题 9.1.11 有

$$
\begin{array}{l} \sum_ {i = 1} ^ {k _ {n}} f _ {x} ^ {\prime} (t _ {i}, X _ {t _ {i - 1}}) (X _ {t _ {i}} - X _ {t _ {i - 1}}) \\ = \sum_ {i = 1} ^ {k _ {n}} f _ {x} ^ {\prime} (t _ {i}, X _ {t _ {i - 1}}) \left[ \int_ {t _ {i - 1}} ^ {t _ {i}} v (s) \mathrm{d} B _ {s} + \int_ {t _ {i - 1}} ^ {t _ {i}} u (s) \mathrm{d} s \right] \\ = \int_ {0} ^ {t} g _ {n} (s, X _ {n} (s)) v (s) \mathrm{d} B _ {s} + \int_ {0} ^ {t} g _ {n} (s, X _ {n} (s)) u (s) \mathrm{d} s \\ = \int_ {0} ^ {t} f _ {x} ^ {\prime} (s, X _ {s}) v (s) \mathrm{d} B _ {s} + \int_ {0} ^ {t} f _ {x} ^ {\prime} (s, X _ {s}) u (s) \mathrm{d} s + o (1), \\ \end{array}
$$

其中

$$
g _ {n} (s, x) = \sum_ {i = 1} ^ {k _ {n}} f _ {x} ^ {\prime} (t _ {i}, x) 1 _ {(t _ {i - 1}, t _ {i} ]} (s), \quad X _ {n} (s) = \sum_ {i = 1} ^ {k _ {n}} X _ {t _ {i - 1}} 1 _ {(t _ {i - 1}, t _ {i} ]} (s).
$$

再注意

$$
\sum_ {i = 1} ^ {k _ {n}} f _ {t} ^ {\prime} (t _ {i - 1}, X _ {t _ {i - 1}}) (t _ {i} - t _ {i - 1}) = \int_ {0} ^ {t} f _ {t} ^ {\prime} (s, X _ {s}) \mathrm{d} s + o (1)
$$

和

$$
\begin{array}{l} \sum_ {i = 1} ^ {k _ {n}} f _ {x x} ^ {\prime \prime} (t _ {i}, X _ {t _ {i - 1}}) (X _ {t _ {i}} - X _ {t _ {i - 1}}) ^ {2} \\ = \sum_ {i = 1} ^ {k _ {n}} f _ {x x} ^ {\prime \prime} (t _ {i}, X _ {t _ {i - 1}}) \left[ \int_ {t _ {i - 1}} ^ {t _ {i}} v (s) \mathrm{d} B _ {s} + \int_ {t _ {i - 1}} ^ {t _ {i}} u (s) \mathrm{d} s \right] ^ {2} \\ \end{array}
$$

---

9.2 伊藤公式

237

$$
\begin{array}{l} = \sum_ {i = 1} ^ {k _ {n}} f _ {x x} ^ {\prime \prime} (t _ {i}, X _ {t _ {i - 1}}) \Big [ \int_ {t _ {i - 1}} ^ {t _ {i}} v (s) \mathrm{d} B _ {s} \Big ] ^ {2} + \\ 2 \sum_ {i = 1} ^ {k _ {n}} f _ {x x} ^ {\prime \prime} (t _ {i}, X _ {t _ {i - 1}}) \Big [ \int_ {t _ {i - 1}} ^ {t _ {i}} v (s) \mathrm{d} B _ {s} \int_ {t _ {i - 1}} ^ {t _ {i}} u (s) \mathrm{d} s \Big ] + \\ \sum_ {i = 1} ^ {k _ {n}} f _ {x x} ^ {\prime \prime} (t _ {i}, X _ {t _ {i - 1}}) \Big [ \int_ {t _ {i - 1}} ^ {t _ {i}} u (s) \mathrm{d} s \Big ] ^ {2}. \\ \end{array}
$$

由定理9.2.3有

$$
\sum_ {i = 1} ^ {k _ {n}} f _ {x x} ^ {\prime \prime} (t _ {i}, X _ {t _ {i - 1}}) \Big [ \int_ {t _ {i - 1}} ^ {t _ {i}} v (s) \mathrm{d} B _ {s} \Big ] ^ {2} = \int_ {0} ^ {t} f _ {x x} ^ {\prime \prime} (s, X _ {s}) v (s) ^ {2} \mathrm{d} s + o (1).
$$

经适当的误差估计后可得到

$$
\begin{array}{l} \Big | \sum_ {i = 1} ^ {k _ {n}} f _ {x x} ^ {\prime \prime} (t _ {i}, X _ {t _ {i - 1}}) \Big [ \int_ {t _ {i - 1}} ^ {t _ {i}} v (s) \mathrm{d} B _ {s} \int_ {t _ {i - 1}} ^ {t _ {i}} u (s) \mathrm{d} s \Big ] \Big | \\ \leqslant \max _ {1 \leqslant i \leqslant k _ {n}} \Big | \int_ {t _ {i - 1}} ^ {t _ {i}} v (s) \mathrm{d} B _ {s} \Big | \cdot \int_ {0} ^ {t} | f _ {x x} ^ {\prime \prime} (s, X _ {s}) u (s) | \mathrm{d} s + o (1), \\ \end{array}
$$

类似地，

$$
\begin{array}{l} \Big | \sum_ {i = 1} ^ {k _ {n}} f _ {x x} ^ {\prime \prime} (t _ {i}, X _ {t _ {i - 1}}) \Big [ \int_ {t _ {i - 1}} ^ {t _ {i}} u (s) \mathrm{d} s \Big ] ^ {2} \Big | \\ \leqslant \max _ {1 \leqslant i \leqslant k _ {n}} \Big | \int_ {t _ {i - 1}} ^ {t _ {i}} u (s) \mathrm{d} s \Big | \cdot \int_ {0} ^ {t} | f _ {x x} ^ {\prime \prime} (s, X _ {s}) u (s) | \mathrm{d} s + o (1). \\ \end{array}
$$

由相关过程的连续性, 上面二式中的最大值当 $n \to \infty$ 时都几乎必然趋于零. 综合上面的计算即得 (9.2.11)式. $\square$

例 9.2.2 令  $Z_{t}=B_{t}-t/2$ ，根据伊藤公式有

$$
\mathrm{de} ^ {Z _ {t}} = \mathrm{e} ^ {Z _ {t}} \mathrm{d} Z _ {t} + \frac {1}{2} \mathrm{e} ^ {Z _ {t}} \mathrm{d} t = \mathrm{e} ^ {Z _ {t}} \mathrm{d} B _ {t}.
$$

因此  $\{e^{Z_{t}}:t\geqslant0\}$  是连续鞅, 称为布朗运动的指数鞅.

## \*9.2.3 局部时和田中公式

设 $(B_{t}:t\geqslant 0)$ 是标准布朗运动.作为伊藤随机积分和伊藤公式的应用,我们将证明对于任意的 $t\geqslant 0$ 和 $x\in \mathbb{R}$ 存在 $L^2$ 极限

$$
L (t, x) = \lim _ {\varepsilon \to 0} \frac {1}{2 \varepsilon} \int_ {0} ^ {t} 1 _ {\{| B _ {s} - x | \leqslant \varepsilon \}} \mathrm{d} s. \tag {9.2.12}
$$

---

238

第九章 随机积分及其应用

随机变量 $L(t,x)$ 称为 $(B_{t}:t\geqslant 0)$ 在时刻 $t\geqslant 0$ 前在点 $x\in \mathbb{R}$ 处的局部时. 它描述了布朗运动处在位置 $x$ 的累积时间的变化过程. 定义函数

$$
f _ {\varepsilon} (z) = \left\{ \begin{array}{l l} | z - x |, & | z - x | > \varepsilon , \\ (\varepsilon + (z - x) ^ {2} / \varepsilon) / 2, & | z - x | \leqslant \varepsilon . \end{array} \right.
$$

引理 9.2.5 对于每个  $t \geqslant 0$ ，几乎必然地有

$$
f _ {\varepsilon} (B _ {t}) - f _ {\varepsilon} (B _ {0}) = \int_ {0} ^ {t} f _ {\varepsilon} ^ {\prime} (B _ {s}) \mathrm{d} B _ {s} + \frac {1}{2 \varepsilon} \int_ {0} ^ {t} 1 _ {\{| B _ {s} - x | \leqslant \varepsilon \}} \mathrm{d} s. \tag {9.2.13}
$$

证明 我们将用无限可微函数列对  $f_{\varepsilon}$  进行逼近, 并以此为基础导出 (9.2.13) 式.
注意

$$
f _ {\varepsilon} ^ {\prime} (z) = \left\{ \begin{array}{l l} 1, & z > x + \varepsilon , \\ - 1, & z <   x - \varepsilon , \\ (z - x) / \varepsilon , & | z - x | \leqslant \varepsilon . \end{array} \right.
$$

另外, 当 $|z - x| \neq \varepsilon$ 时有 $f_{\varepsilon}^{\prime \prime}(z) = \varepsilon^{-1}1_{\{|z - x| \leqslant \varepsilon\}}$. 定义

$$
\phi (z) = \left\{ \begin{array}{l l} c \exp \{- (1 - z ^ {2}) ^ {- 1} \}, & | z | <   1, \\ 0, & | z | \geqslant 1, \end{array} \right.
$$

其中 $c > 0$ 为规范化常数, 使得 $\int_{\mathbb{R}}\phi (y)\mathrm{d}y = 1$. 再定义 $\phi_n(z) = n\phi (nz)$ 和

$$
g _ {n} (z) = \int_ {\mathbb {R}} f _ {\varepsilon} (z - y) \phi_ {n} (y) \mathrm{d} y, \quad z \in \mathbb {R},
$$

则 $g_{n}$ 是无限可微的函数. 易知当 $n \to \infty$ 时有 $g_{n}(z) \to f_{\varepsilon}(z)$ 和 $g_{n}^{\prime}(z) \to f_{\varepsilon}^{\prime}(z)$ 且收敛对 $z \in \mathbb{R}$ 一致成立, 同时 $g_{n}^{\prime \prime}(z) \to \varepsilon^{-1}1_{\{|z - x| \leqslant \varepsilon\}}$ 除了 $z = x \pm \varepsilon$ 外逐点成立. 对于 $g_{n}(B_{t})$ 应用伊藤公式得

$$
g _ {n} (B _ {t}) - g _ {n} (B _ {0}) = \int_ {0} ^ {t} g _ {n} ^ {\prime} (B _ {s}) \mathrm{d} B _ {s} + \frac {1}{2} \int_ {0} ^ {t} g _ {n} ^ {\prime \prime} (B _ {s}) \mathrm{d} s. \tag {9.2.14}
$$

根据控制收敛定理有

$$
\lim _ {n \to \infty} \mathbf {E} \Bigl \{\int_ {0} ^ {t} [ g _ {n} ^ {\prime} (B _ {s}) - f _ {\varepsilon} ^ {\prime} (B _ {s}) ] ^ {2} \mathrm{d} s \Bigr \} = 0.
$$

再由伊藤同构, 在  $L^{2}$  收敛意义下,

$$
\lim _ {n \to \infty} \int_ {0} ^ {t} g _ {n} ^ {\prime} (B _ {s}) \mathrm{d} B _ {s} = \int_ {0} ^ {t} f _ {\varepsilon} ^ {\prime} (B _ {s}) \mathrm{d} B _ {s}.
$$

---

9.2 伊藤公式

239

注意, 对每个 $s > 0$ 有 $\mathbf{P}(B_s = x + \varepsilon$ 或 $x - \varepsilon) = 0$, 故 $\lim_{n\to \infty}g_n''(B_s) = \varepsilon^{-1}1_{\{|B_s - x|\leqslant \varepsilon \}}$ 几乎必然成立. 根据富比尼定理, 几乎必然地该收敛对几乎处处的 $s\geqslant 0$ 成立. 由于 $g_n''(z)\leqslant \varepsilon^{-1}$, 根据有界收敛定理, 在几乎必然和 $L^2$ 收敛意义下有

$$
\lim _ {n \to \infty} \int_ {0} ^ {t} g _ {n} ^ {\prime \prime} (B _ {s}) \mathrm{d} s = \frac {1}{\varepsilon} \int_ {0} ^ {t} 1 _ {\{| B _ {s} - x | \leqslant \varepsilon \}} \mathrm{d} s.
$$

这样, 在 (9.2.14) 式令 $n \to \infty$ 即知 (9.2.13) 式几乎必然成立. $\square$

定理 9.2.6 对  $t \geqslant 0$  和  $x \in R$  令  $L(t, x)$  由 (9.2.12) 式定义, 则几乎必然有

$$
| B _ {t} - x | - | B _ {0} - x | = \int_ {0} ^ {t} \mathrm{sgn} (B _ {s} - x) \mathrm{d} B _ {s} + L (t, x). \tag {9.2.15}
$$

证明 注意当 $\varepsilon \to 0$ 时对 $z \in \mathbb{R}$ 一致地有 $|f_{\varepsilon}(z) \to |z - x|$. 根据控制收敛定理有

$$
\lim _ {\varepsilon \to 0} \mathbf {E} \Bigl \{\int_ {0} ^ {t} [ f _ {\varepsilon} ^ {\prime} (B _ {s}) - \mathrm{sgn} (B _ {s} - x) ] ^ {2} \mathrm{d} s \Bigr \} = 0.
$$

再由伊藤同构, 在  $L^{2}$  收敛意义下有

$$
\lim _ {n \to \infty} \int_ {0} ^ {t} f _ {\varepsilon} ^ {\prime} (B _ {s}) \mathrm{d} B _ {s} = \int_ {0} ^ {t} \mathrm{sgn} (B _ {s} - x) \mathrm{d} B _ {s}.
$$

由 (9.2.13) 式可知 $L^2$ 极限 (9.2.12) 存在且 (9.2.15) 式成立. $\square$

通常称 (9.2.15) 式为田中 (Tanaka) 公式. 局部时和田中公式在布朗运动的理论中扮演着关键角色. 由 (9.2.13) 式可以看出 $t \mapsto L(t, x)$ 有连续的修正, 再由 (9.2.13) 式知该修正几乎必然关于 $t \geqslant 0$ 单调不降. 实际上 $L(t, x)$ 有一个关于 $(t, x) \in [0, \infty) \times \mathbb{R}$ 连续的版本; 参见 [22, p.239, Theorem 9.4].

## 练习题

1. 利用伊藤公式将下列泛函写成形如 (9.2.9) 式的形式:

(1) $X_{t} = B_{t}^{2}$; (2) $Y_{t} = B_{t}^{3}$; (3) $Z_{t} = t + \mathrm{e}^{B_{t}}$.

2. 对 $v \in \mathcal{L}^2$ 令

$$
Z _ {t} = \exp \Bigl \{\int_ {0} ^ {t} v (s) \mathrm{d} B _ {s} - \frac {1}{2} \int_ {0} ^ {t} v (s) ^ {2} \mathrm{d} s \Bigr \}.
$$

假设  $\{v(t)Z_{t}\}\in\mathscr{L}^{2}$ . 证明  $\mathrm{d}Z_{t}=v(t)Z_{t}\mathrm{d}B_{t}$ .

3. 设 $(B_{t})$ 是标准布朗运动. 对 $t \geqslant 0$ 和 $n \geqslant 1$ 令 $\beta_{n}(t) = \mathbf{E}(B_{t}^{n})$. 证明

$$
\beta_ {n} (t) = \frac {1}{2} n (n - 1) \int_ {0} ^ {t} \beta_ {n - 2} (s) \mathrm{d} s, \quad n \geqslant 2,
$$

---

240

第九章 随机积分及其应用

并据此求出  $\mathbf{E}(B_{t}^{4})$  和  $\mathbf{E}(B_{t}^{6})$ .

4. 证明下列过程是鞅:

(1) $X_{t} = \mathrm{e}^{t / 2}\cos B_{t};$ (2) $Y_{t} = \mathrm{e}^{t / 2}\sin B_{t};$ (3) $Z_{t} = (B_{t} + t)\mathrm{e}^{-B_{t} - t / 2}$.

5. 证明对 $t \geqslant 0$ 和 $x \in \mathbb{R}$ 几乎必然有

$$
(B _ {t} - x) \vee 0 - (B _ {0} - x) \vee 0 = \int_ {0} ^ {t} 1 _ {\{B _ {s} > x \}} \mathrm{d} B _ {s} + \frac {1}{2} L (t, x).
$$

## 9.3 随机微分方程

在本节中, 我们对于系数满足利普希茨 (Lipschitz) 条件的一维随机方程, 建立其解的存在性和唯一性, 证明解的强马氏性, 并简单讨论抛物型偏微分方程的柯西初值问题的概率表示.

## 9.3.1 解和解的唯一性

设 $(\Omega, \mathcal{F}, \mathbf{P})$ 是完备概率空间, 而 $(\mathcal{F}_t : t \geqslant 0)$ 是此空间上的满足通常条件的 $\sigma$ 代数流. 令 $(B_t : t \geqslant 0)$ 是 $(\mathcal{F}_t)$ 标准布朗运动. 给定 $\mathbb{R}$ 上的连续函数 $\sigma$ 和 $b$, 我们考虑随机微分方程:

$$
\mathrm{d} X _ {t} = \sigma (X _ {t}) \mathrm{d} B _ {t} + b (X _ {t}) \mathrm{d} t, \quad t \geqslant 0. \tag {9.3.1}
$$

称函数  $\sigma$  和 b 满足利普希茨条件, 是指存在常数  $K \geqslant 0$  使得

$$
\left| \sigma (x) - \sigma (y) \right| + \left| b (x) - b (y) \right| \leqslant K | x - y |, \quad x, y \in \mathbb {R}. \tag {9.3.2}
$$

定义 9.3.1 称连续的  $(\mathcal{F}_{t})$  循序可测过程  $(X_{t}: t \geqslant 0)$  是随机微分方程 (9.3.1) 的解, 是指几乎必然地

$$
X _ {t} = X _ {0} + \int_ {0} ^ {t} \sigma (X _ {s}) \mathrm{d} B _ {s} + \int_ {0} ^ {t} b (X _ {s}) \mathrm{d} s, \quad t \geqslant 0. \tag {9.3.3}
$$

称方程 (9.3.1) 的解的唯一性或解的轨道唯一性成立, 是指它的任何满足 $X_0 \stackrel{\text{a.s.}}{=} Y_0$ 的解 $(X_t : t \geqslant 0)$ 和 $(Y_t : t \geqslant 0)$ 都是无区别的, 即有

$$
\mathbf {P} (X _ {t} = Y _ {t} \text {对一切} t \geqslant 0 \text {成立}) = 1.
$$

引理 9.3.1 设 h 为区间  $[0, T]$  上的可积函数. 若有常数  $C \geqslant 0$  使得

$$
f (t) = h (t) + C \int_ {0} ^ {t} \mathrm{e} ^ {C (t - s)} h (s) \mathrm{d} s, \quad 0 \leqslant t \leqslant T, \tag {9.3.4}
$$

---

9.3 随机微分方程

241

则有

$$
f (t) = h (t) + C \int_ {0} ^ {t} f (s) \mathrm{d} s, \quad 0 \leqslant t \leqslant T. \tag {9.3.5}
$$

证明 由 (9.3.4) 式以及分部积分公式可得

$$
\begin{array}{l} h (t) + C \int_ {0} ^ {t} f (s) \mathrm{d} s \\ = h (t) + C \int_ {0} ^ {t} h (s) \mathrm{d} s + C \int_ {0} ^ {t} \left[ C \mathrm{e} ^ {C s} \int_ {0} ^ {s} \mathrm{e} ^ {- C r} h (r) \mathrm{d} r \right] \mathrm{d} s \\ = h (t) + C \mathrm{e} ^ {C t} \int_ {0} ^ {t} \mathrm{e} ^ {- C r} h (r) \mathrm{d} r = f (t). \\ \end{array}
$$

这就证明了(9.3.5)式. $\square$

下面的结果称为格朗沃尔 (Gronwall) 不等式:

引理 9.3.2 设 g 和 h 是区间  $[0, T]$  上的可积函数. 若有常数  $C \geqslant 0$  使得

$$
g (t) \leqslant h (t) + C \int_ {0} ^ {t} g (s) \mathrm{d} s, \quad 0 \leqslant t \leqslant T, \tag {9.3.6}
$$

则有

$$
g (t) \leqslant h (t) + C \int_ {0} ^ {t} \mathrm{e} ^ {C (t - s)} h (s) \mathrm{d} s, \quad 0 \leqslant t \leqslant T. \tag {9.3.7}
$$

证明 令 $f(t)$ 由 (9.3.4) 式给出, 并记 $\Delta(t) = f(t) - g(t)$. 由 (9.3.5) 式和 (9.3.6) 式可得

$$
\Delta (t) \geqslant C \int_ {0} ^ {t} \Delta (s) \mathrm{d} s, \quad 0 \leqslant t \leqslant T.
$$

反复应用上式有

$$
\begin{array}{l} \Delta (t) \geqslant C ^ {2} \int_ {0} ^ {t} \mathrm{d} s \int_ {0} ^ {s} \Delta (r) \mathrm{d} r = C ^ {2} \int_ {0} ^ {t} (t - r) \Delta (r) \mathrm{d} r \\ \geqslant C ^ {3} \int_ {0} ^ {t} (t - r) \mathrm{d} r \int_ {0} ^ {r} \Delta (s) \mathrm{d} s = \frac {C ^ {3}}{2} \int_ {0} ^ {t} (t - s) ^ {2} \Delta (s) \mathrm{d} s \\ \geqslant \dots \geqslant \frac {C ^ {n}}{(n - 1) !} \int_ {0} ^ {t} (t - s) ^ {n - 1} \Delta (s) \mathrm{d} s. \\ \end{array}
$$

在上式两端令 $n\to \infty$ 得 $\Delta (t)\geqslant 0$ ，即(9.3.7)式成立.□

定理 9.3.3 设函数  $\sigma$  和 b 满足利普希茨条件 (9.3.2)，则存在常数  $C \geqslant 0$  使对 (9.3.3) 式的任意的两个解  $(X_{t}: t \geqslant 0)$  和  $(Y_{t}: t \geqslant 0)$  有

$$
\mathbf {E} [ (Y _ {t} - X _ {t}) ^ {2} ] \leqslant 3 \mathbf {E} [ (Y _ {0} - X _ {0}) ^ {2} ] \exp \left\{C t (t + 1) \right\}, \quad t \geqslant 0. \tag {9.3.8}
$$

---

242

第九章 随机积分及其应用

证明 只需考虑 $\mathbf{E}[(Y_0 - X_0)^2] < \infty$ 的情形. 为简单起见, 此证明假定 $\sigma$ 和 $b$ 是有界的利普希茨函数. 对于一般情况类似结果的证明, 可以参见 [22, pp.216-218]. 因为 $(X_t : t \geqslant 0)$ 和 $(Y_t : t \geqslant 0)$ 都是 (9.3.3) 式的解, 我们有

$$
X _ {t} - Y _ {t} = X _ {0} - Y _ {0} + \int_ {0} ^ {t} [ \sigma (X _ {s}) - \sigma (Y _ {s}) ] \mathrm{d} B _ {s} + \int_ {0} ^ {t} [ b (X _ {s}) - b (Y _ {s}) ] \mathrm{d} s.
$$

由伊藤等距公式和柯西-施瓦茨不等式, 有

$$
\begin{array}{l} \mathbf {E} [ (X _ {t} - Y _ {t}) ^ {2} ] \leqslant 3 \mathbf {E} [ (X _ {0} - Y _ {0}) ^ {2} ] + 3 \mathbf {E} \bigg \{\left[ \int_ {0} ^ {t} (\sigma (X _ {s}) - \sigma (Y _ {s})) \mathrm{d} B _ {s} \right] ^ {2} \bigg \} + \\ 3 \mathbf {E} \Bigg \{\Big [ \int_ {0} ^ {t} (b (X _ {s}) - b (Y _ {s})) \mathrm{d} s \Big ] ^ {2} \Bigg \} \\ \leqslant 3 \mathbf {E} \{(X _ {0} - Y _ {0}) ^ {2} \} + 3 \int_ {0} ^ {t} \mathbf {E} \{[ \sigma (X _ {s}) - \sigma (Y _ {s}) ] ^ {2} \} \mathrm{d} s + \\ 3 t \int_ {0} ^ {t} \mathbf {E} \{[ b (X _ {s}) - b (Y _ {s}) ] ^ {2} \} \mathrm{d} s. \tag {9.3.9} \\ \end{array}
$$

任取 $T \geqslant 0$. 因为 $\sigma$ 和 $b$ 是有界函数, 由上式知函数 $t \mapsto \mathbf{E}[(X_t - Y_t)^2]$ 在区间 $[0, T]$ 上有界, 因而可积. 再由 (9.3.9) 式和利普希茨性质有

$$
\mathbf {E} [ (X _ {t} - Y _ {t}) ^ {2} ] \leqslant 3 \mathbf {E} [ (X _ {0} - Y _ {0}) ^ {2} ] + 3 K ^ {2} (T + 1) \int_ {0} ^ {t} \mathbf {E} [ (X _ {s} - X _ {s}) ^ {2} ] \mathrm{d} s.
$$

根据格朗沃尔不等式,

$$
\mathbf {E} [ (Y _ {t} - X _ {t}) ^ {2} ] \leqslant 3 \mathbf {E} [ (Y _ {0} - X _ {0}) ^ {2} ] \exp \left\{3 K ^ {2} (T + 1) t \right\}, \quad 0 \leqslant t \leqslant T.
$$

最后令 $C = 3K^2$ 和 $t = T$ 即得(9.3.8)式. □

定理 9.3.4 设函数  $\sigma$  和 b 满足利普希茨条件 (9.3.2)，则随机微分方程 (9.3.1) 的解的轨道唯一性成立.

证明 当 $X_0 \stackrel{\mathrm{a.s.}}{=} Y_0$ 时, 由定理 9.3.3 可知对 $t \geqslant 0$ 有 $\mathbf{E}[(X_t - Y_t)^2] = 0$, 从而 $\mathbf{P}(X_t = Y_t) = 1$. 再由 $(X_t : t \geqslant 0)$ 和 $(Y_t : t \geqslant 0)$ 的连续性知它们是无区别的, 即解的轨道唯一性对 (9.3.3) 式成立. $\square$

## 9.3.2 解的存在性

引理 9.3.5 对于任何给定的  $T \geqslant 0$  存在连续  $(\mathcal{F}_{t})$  循序可测过程  $(X_{t}: t \in [0, T])$  使得 (9.3.3) 式几乎必然对一切  $t \in [0, T]$  成立.

证明 此证明仍然假定 $\sigma$ 和 $b$ 是有界的利普希茨函数. 对于一般情况类似结果的证明, 可以参见 [22, pp.216-218]. 令 $\xi_0(t) = X_0$ 并对 $n \geqslant 0$ 递推地定义 $\xi_n(t)$ 如下

$$
\xi_ {n + 1} (t) = X _ {0} + \int_ {0} ^ {t} \sigma (\xi_ {n} (s)) \mathrm{d} B _ {s} + \int_ {0} ^ {t} b (\xi_ {n} (s)) \mathrm{d} s, \tag {9.3.10}
$$

---

9.3 随机微分方程

243

则每个  $\{\xi_{n}(t):t\geqslant0\}$  都连续  $(\mathcal{F}_{t})$  循序可测过程. 注意

$$
\begin{array}{l} \xi_ {n + 1} (t) - \xi_ {n} (t) = \int_ {0} ^ {t} [ \sigma (\xi_ {n} (s)) - \sigma (\xi_ {n - 1} (s)) ] \mathrm{d} B _ {s} + \\ \int_ {0} ^ {t} [ b (\xi_ {n} (s)) - b (\xi_ {n - 1} (s)) ] \mathrm{d} s. \tag {9.3.11} \\ \end{array}
$$

类似于定理 9.3.3 的证明中的讨论, 函数  $t \mapsto \mathbf{E}\{[\xi_{n+1}(t) - \xi_n(t)]^2\}$  在区间  $[0, T]$  上有界且

$$
\mathbf {E} \bigl \{[ \xi_ {n + 1} (t) - \xi_ {n} (t) ] ^ {2} \bigr \} \leqslant 2 K ^ {2} (T + 1) \int_ {0} ^ {t} \mathbf {E} \bigl \{[ \xi_ {n} (s) - \xi_ {n - 1} (s) ] ^ {2} \bigr \} \mathrm{d} s.
$$

记 $C = 2K^{2}(T + 1)$ 和 $G_{n}(t) = \mathbf{E}\{[\xi_{n + 1}(t) - \xi_{n}(t)]^{2}\}$, 则有

$$
\begin{array}{l} G _ {n} (t) \leqslant C \int_ {0} ^ {t} G _ {n - 1} (s _ {1}) \mathrm{d} s _ {1} \leqslant C ^ {2} \int_ {0} ^ {t} \mathrm{d} s _ {1} \int_ {0} ^ {s _ {1}} G _ {n - 2} (s _ {2}) \mathrm{d} s _ {2} \\ \leqslant \dots \leqslant C ^ {n} \int_ {0} ^ {t} \mathrm{d} s _ {1} \int_ {0} ^ {s _ {1}} \mathrm{d} s _ {2} \dots \int_ {0} ^ {s _ {n - 1}} G _ {0} (s _ {n}) \mathrm{d} s _ {n}. \tag {9.3.12} \\ \end{array}
$$

注意到

$$
G _ {0} (t) = \mathbf {E} \{[ \sigma (X _ {0}) B _ {t} + t b (X _ {0}) ] ^ {2} \} \leqslant 2 (\| \sigma \| ^ {2} + \| b \| ^ {2} t) t \leqslant A,
$$

其中 $A = 2(\| \sigma|^2 + \| b\|^2 T)T.$ 将上式代入(9.3.12)式并对右侧积分可得

$$
\mathbf {E} \{[ \xi_ {n + 1} (t) - \xi_ {n} (t) ] ^ {2} \} \leqslant \frac {A C ^ {n} t ^ {n}}{n !}, \quad 0 \leqslant t \leqslant T. \tag {9.3.13}
$$

由 (9.3.11) 式可得

$$
\begin{array}{l} \sup _ {0 \leqslant t \leqslant T} | \xi_ {n + 1} (t) - \xi_ {n} (t) | \leqslant \sup _ {0 \leqslant t \leqslant T} \Big | \int_ {0} ^ {t} [ \sigma (\xi_ {n} (s)) - \sigma (\xi_ {n - 1} (s)) ] \mathrm{d} B _ {s} \Big | + \\ \int_ {0} ^ {T} | b (\xi_ {n} (s)) - b (\xi_ {n - 1} (s)) | \mathrm{d} s. \\ \end{array}
$$

根据鞅不等式和伊藤等距公式,

$$
\begin{array}{l} \mathbf {P} \Big \{\sup _ {0 \leqslant t \leqslant T} | \xi_ {n + 1} (t) - \xi_ {n} (t) | \geqslant 2 ^ {- n} \Big \} \\ \leqslant \mathbf {P} \Big \{\sup _ {0 \leqslant t \leqslant T} \Big | \int_ {0} ^ {t} [ \sigma (\xi_ {n} (s)) - \sigma (\xi_ {n - 1} (s)) ] \mathrm{d} B _ {s} \Big | \geqslant 2 ^ {- n - 1} \Big \} + \\ \mathbf {P} \Big \{\int_ {0} ^ {T} | b (\xi_ {n} (s)) - b (\xi_ {n - 1} (s)) | \mathrm{d} s \geqslant 2 ^ {- n - 1} \Big \} \\ \leqslant 4 ^ {n + 1} \mathbf {E} \Big \{\Big | \int_ {0} ^ {T} [ \sigma (\xi_ {n} (s)) - \sigma (\xi_ {n - 1} (s)) ] \mathrm{d} B _ {s} \Big | ^ {2} \Big \} + \\ 4 ^ {n + 1} \mathbf {E} \Big \{\left[ \int_ {0} ^ {T} | b (\xi_ {n} (s)) - b (\xi_ {n - 1} (s)) | \mathrm{d} s \right] ^ {2} \Big \} \\ \end{array}
$$

---

244

第九章 随机积分及其应用

$$
\leqslant 4 ^ {n + 1} \int_ {0} ^ {T} \mathbf {E} \{| \sigma (\xi_ {n} (s)) - \sigma (\xi_ {n - 1} (s)) | ^ {2} \} \mathrm{d} s +
$$

$$
4 ^ {n + 1} T \int_ {0} ^ {T} \mathbf {E} \{| b (\xi_ {n} (s)) - b (\xi_ {n - 1} (s)) | ^ {2} \} \mathrm{d} s.
$$

由 $\sigma$ 和 $b$ 的利普希茨性质并应用 (9.3.13) 式得

$$
\begin{array}{l} \mathbf {P} \Big \{\sup _ {0 \leqslant t \leqslant T} | \xi_ {n + 1} (t) - \xi_ {n} (t) | \geqslant 2 ^ {- n} \Big \} \\ \leqslant 4 ^ {n + 1} K ^ {2} (T + 1) \int_ {0} ^ {T} \mathbf {E} \left\{\left| \xi_ {n} (s) - \xi_ {n - 1} (s) \right| ^ {2} \right\} \mathrm{d} s \\ \leqslant 4 ^ {n + 1} K ^ {2} (T + 1) \int_ {0} ^ {T} \frac {A C ^ {n - 1} s ^ {n - 1}}{(n - 1) !} \mathrm{d} s \\ \leqslant 4 ^ {n + 1} K ^ {2} (T + 1) \frac {A C ^ {n - 1} T ^ {n}}{n !} \\ = \frac {4 ^ {n + 1}}{2 n !} A C ^ {n} T ^ {n}. \\ \end{array}
$$

于是

$$
\sum_ {n = 1} ^ {\infty} \mathbf {P} \Big \{\sup _ {0 \leqslant t \leqslant T} | \xi_ {n + 1} (t) - \xi_ {n} (t) | \geqslant 2 ^ {- n} \Big \} <   \infty .
$$

根据博雷尔-坎泰利引理,

$$
\mathbf {P} \Big \{\sup _ {0 \leqslant t \leqslant T} | \xi_ {n + 1} (t) - \xi_ {n} (t) | \geqslant 2 ^ {- n} \text {对无穷多个} n \text {成立} \Big \} = 0.
$$

所以存在 $\Omega_T \in \mathcal{F}_0$ 满足 $\mathbf{P}(\Omega_T) = 1$ 且对一切 $\omega \in \Omega_T$ 当 $n \to \infty$ 时

$$
\xi_ {n} (t, \omega) = X _ {0} + \sum_ {k = i} ^ {n} [ \xi_ {k} (t, \omega) - \xi_ {k - 1} (t, \omega) ]
$$

关于 $t \in [0, T]$ 一致收敛. 现在令

$$
X _ {t} (\omega) = \lim _ {n \to \infty} \xi_ {n} (t, \omega) 1 _ {\varOmega_ {T}} (\omega), \quad \omega \in \varOmega . \tag {9.3.14}
$$

因为每个  $\{\xi_{n}(t):t\in[0,T]\}$  都是连续  $(\mathcal{F}_{t})$  循序可测过程, 所以  $\{X_{t}:t\in[0,T]\}$  也是连续  $(\mathcal{F}_{t})$  循序可测过程. 由于 b 有界且连续, 根据控制收敛定理, 对  $\omega\in\Omega_{T}$  和  $t\in[0,T]$  有

$$
\lim _ {n \to \infty} \int_ {0} ^ {t} b (\xi_ {n} (s, \omega)) \mathrm{d} s = \int_ {0} ^ {t} b (X _ {s} (\omega)) \mathrm{d} s. \tag {9.3.15}
$$

同样根据控制收敛定理, 对  $t \in [0, T]$  有

$$
\lim _ {n \to \infty} \int_ {0} ^ {t} \mathbf {E} \{[ \sigma (\xi_ {n} (s)) - \sigma (X _ {s}) ] ^ {2} \} \mathrm{d} s = 0.
$$

---

9.3 随机微分方程

245

由伊藤等距公式, 在  $L^{2}$  收敛意义下有

$$
\lim _ {n \to \infty} \int_ {0} ^ {t} \sigma (\xi_ {n} (s)) \mathrm{d} B _ {s} = \int_ {0} ^ {t} \sigma (X _ {s}) \mathrm{d} B _ {s}, \tag {9.3.16}
$$

进而该收敛对某个子列在几乎处处收敛的意义下成立. 综合 (9.3.10) 式以及 (9.3.14)—(9.3.16) 式可知 (9.3.3) 式对 $t \in [0, T]$ 几乎必然成立. 再由等号两边的连续性知方程 (9.3.3) 几乎必然对以一切 $t \in [0, T]$ 成立. $\square$

定理 9.3.6 设函数  $\sigma$  和 b 满足利普希茨条件 (9.3.2)，则对任意给定的  $F_{0}$  可测的随机变量  $X_{0}$ ，随机微分方程 (9.3.3) 有唯一的解 ( $X_{t}: t \geqslant 0$ ).

证明 方程 (9.3.3) 的解的轨道唯一性由定理 9.3.4 保证. 所以我们只需证明 (9.3.3) 式的解的存在性. 由引理 9.3.5, 对每个 $n \geqslant 1$ 存在连续 $(\mathcal{F}_t)$ 循序可测过程 $\{X_n(t): t \in [0, n]\}$ 满足 (9.3.3) 式且 $X_n(0) = X_0$. 与定理 9.3.4 的证明类似地不难看出 $\{X_n(t): t \in [0, n]\}$ 和 $\{X_{n+1}(t): t \in [0, n]\}$ 是无区别的, 即存在 $\Omega_n \in \mathcal{F}_0$ 满足 $\mathbf{P}(\Omega_n) = 1$ 且对 $\omega \in \Omega_n$ 和 $t \in [0, n]$ 有 $X_n(t) = X_{n+1}(t)$. 令 $\Omega_0 = \bigcap_{n \geqslant 1} \Omega_n \in \mathcal{F}_0$, 则 $\mathbf{P}(\Omega_0) = 1$. 再定义

$$
X _ {t} (\omega) = \sum_ {n = 1} ^ {\infty} X _ {n} (t, \omega) 1 _ {[ n - 1, n)} (t) 1 _ {\Omega_ {0}} (\omega), \quad t \geqslant 0, \omega \in \Omega .
$$

显然 $(X_{t}:t\geqslant0)$ 是方程(9.3.3)的解. □

例 9.3.1 令  $\sigma$  和 b 为实常数. 再设  $(B_{t}: t \geqslant 0)$  为  $(\mathcal{F}_{t})$  标准布朗运动. 给定  $F_{0}$  可测的初值  $X_{0}$ , 定义连续  $(\mathcal{F}_{t})$  循序可测随机过程:

$$
X _ {t} = \mathrm{e} ^ {- b t} \Big (X _ {0} + \sigma \int_ {0} ^ {t} \mathrm{e} ^ {b s} \mathrm{d} B _ {s} \Big). \tag {9.3.17}
$$

通常称 $(X_{t}:t\geqslant 0)$ 为奥恩斯坦-乌伦贝克 (Ornstein-Uhlenbeck) 过程. 由 (9.3.17) 式和伊藤公式可以看出, 此过程满足下面的朗之万 (Langevin) 方程:

$$
\mathrm{d} X _ {t} = \sigma \mathrm{d} B _ {t} - b X _ {t} \mathrm{d} t, \quad t \geqslant 0. \tag {9.3.18}
$$

朗之万方程最初被用于描述微观粒子在粘性介质中的运动速度随时间的变化. 该模型在金融研究中也有很多应用, 参见 [21].

例 9.3.2 令  $\sigma$  和  $\beta$  是给定的实常数. 再设  $(B_{t}: t \geqslant 0)$  为  $(\mathcal{F}_{t})$  标准布朗运动. 我们称连续  $(\mathcal{F}_{t})$  循序可测随机过程  $(S_{t}: t \geqslant 0)$  为几何布朗运动, 是指它满足随机微分方程:

$$
\mathrm{d} S _ {t} = \sigma S _ {t} \mathrm{d} B _ {t} + \beta S _ {t} \mathrm{d} t, \quad t \geqslant 0. \tag {9.3.19}
$$

根据定理 9.3.4, 对于任意的  $F_{0}$  可测的初值  $S_{0}$  方程 (9.3.19) 有唯一的解  $(S_{t}: t \geqslant 0)$ .
该解可以表示为

$$
S _ {t} = S _ {0} \mathrm{e} ^ {b t + \sigma B _ {t}}, \quad t \geqslant 0, \tag {9.3.20}
$$

---

246

第九章 随机积分及其应用

其中  $b = \beta - \sigma^{2}/2$ . 对 (9.3.20) 式取期望得

$$
\mathbf {E} (S _ {t}) = \mathbf {E} (S _ {0}) \mathrm{e} ^ {\beta t}.
$$

可见 $t \mapsto \mathbf{E}(S_t)$ 以指数函数的速度变化. 几何布朗运动就是金融学中著名的布莱克-斯科尔斯 (Black-Scholes) 模型, 在期权定价等理论中有重要的应用, 参见 [21].

## 9.3.3 解的强马氏性

设 $(\Omega, \mathcal{F}, \mathbf{P})$ 是带有加强流 $(\mathcal{F}_t : t \geqslant 0)$ 的完备概率空间, 而 $(B_t : t \geqslant 0)$ 是 $(\mathcal{F}_t)$ 标准布朗运动. 再设函数 $\sigma$ 和 $b$ 满足利普希茨条件 (9.3.2). 根据定理 9.3.6, 给定 $\mathcal{F}_0$ 可测随机变量 $X_0$, 随机微分方程 (9.3.1) 有唯一的解 $(X_t : t \geqslant 0)$. 特别地, 对 $x \in \mathbb{R}$ 有 (9.3.1) 式的唯一解 $(X_t^x : t \geqslant 0)$ 满足 $X_0^x = x$. 用 $P_t(x, \cdot)$ 表示 $X_t^x$ 在 $(\mathbb{R}, \mathcal{B})$ 上的分布, 即

$$
P _ {t} (x, A) = \mathbf {P} (X _ {t} ^ {x} \in A), \quad A \in \mathscr {B}. \tag {9.3.21}
$$

再令

$$
P _ {t} f (x) = \int_ {\mathbb {R}} f (y) P _ {t} (x, \mathrm{d} y), \quad f \in \mathrm{b} \mathcal {B}. \tag {9.3.22}
$$

根据定理 9.3.3, 当 $x_{n} \to x \in \mathbb{R}$ 时在 $L^{2}$ 收敛意义下有 $X_{t}^{x_{n}} \to X_{t}^{x}$, 故 $P_{t}(x_{n}, \cdot) \stackrel{\mathrm{w}}{\to} P_{t}(x, \cdot)$. 令 $C_{b}(\mathbb{R})$ 表示 $\mathbb{R}$ 上的有界连续函数的全体. 根据上面的分析不难证明, 当 $f \in C_{b}(\mathbb{R})$ 时有 $P_{t}f \in C_{b}(\mathbb{R})$. 利用邓肯类定理可以证明, 对任意的 $A \in \mathcal{B}$ 函数 $x \mapsto P_{t}(x, A)$ 关于 $\mathcal{B}$ 可测, 因此 $P_{t}$ 是 $(\mathbb{R}, \mathcal{B})$ 上的马氏转移核. 此外, 由 $(X_{t}^{x}: t \geqslant 0)$ 的轨道的连续性, 当 $f \in C_{b}(\mathbb{R})$ 时有

$$
\lim _ {t \to 0} P _ {t} f (x) = \lim _ {t \to 0} \mathbf {E} [ f (X _ {t} ^ {x}) ] = f (x), \quad x \in \mathbb {R}. \tag {9.3.23}
$$

定理 9.3.7 由 (9.3.21) 式定义的马氏转移核  $(P_{t})_{t\geqslant0}$  构成转移半群, 且 (9.3.3) 式的解  $(X_{t}:t\geqslant0)$  相对于流  $(\mathcal{F}_{t})$  满足以  $(P_{t})_{t\geqslant0}$  为转移半群的强马氏性.

证明 给定 $r \geqslant 0$ 令 $B_{r,t} = B_{r + t} - B_r$ 和 $\mathcal{F}_{r + t} = \mathcal{F}_{r + t}$. 易知 $(B_{r,t}:t \geqslant 0)$ 是关于流 $(\mathcal{F}_{r,t}:t \geqslant 0)$ 的标准布朗运动. 由 (9.3.3) 式得

$$
X _ {r + t} = X _ {r} + \int_ {0} ^ {t} \sigma (X _ {r + s}) \mathrm{d} B _ {r, s} + \int_ {0} ^ {t} b (X _ {r + s}) \mathrm{d} s, \quad t \geqslant 0. \tag {9.3.24}
$$

注意, 这里 $X_{r}$ 关于 $\mathcal{F}_{r,0} = \mathcal{F}_{r}$ 可测. 对比 (9.3.3) 式和 (9.3.24) 式我们发现 $(X_{r,t}: t \geqslant 0)$ 也是具有系数 $\sigma$ 和 $b$ 的随机微分方程的以 $X_{r}$ 为初值的解. 由 (9.3.21) 式和 (9.3.24) 式直观地推得

$$
\mathbf {P} (X _ {r + t} \in A | \mathscr {F} _ {r}) = P _ {t} (X _ {r}, A), \quad A \in \mathscr {B}. \tag {9.3.25}
$$

---

9.3 随机微分方程

247

(此步的严格论证需要更多工作, 这里从略, 详见 [22, pp.221-222].) 特别地, 对 $(X_{t}^{x}: t \geqslant 0)$ 应用 (9.3.25) 式得

$$
\mathbf {P} (X _ {r + t} ^ {x} \in A) = \mathbf {E} [ \mathbf {P} (X _ {r + t} ^ {x} \in A | \mathcal {F} _ {r}) ] = \mathbf {E} [ P _ {t} (X _ {r} ^ {x}, A) ],
$$

即有

$$
P _ {r + t} (x, A) = \int_ {\mathbb {R}} P _ {r} (x, \mathrm{d} y) P _ {t} (y, A), \quad A \in \mathscr {B}.
$$

所以 $(P_t)_{t\geqslant 0}$ 构成 $(\mathbb{R},\mathcal{B})$ 上的马氏转移半群, 而 (9.3.25) 式说明 $(X_{t}:t\geqslant 0)$ 满足相对于流 $(\mathcal{F}_t)$ 以 $(P_t)_{t\geqslant 0}$ 为转移半群的马氏性. 利用 (9.3.23)式, 与定理8.2.12的证明类似地可以推出强马氏性成立. □

通常称连续的强马氏过程为扩散过程. 根据定理 9.3.7, 随机微分方程 (9.3.3) 的解  $(X_{t}: t \geqslant 0)$  相对于流  $(\mathcal{F}_{t})$  是具有转移半群  $(P_{t})_{t \geqslant 0}$  的扩散过程. 分别称  $\sigma$  和 b 为  $(X_{t}: t \geqslant 0)$  的扩散系数和漂移系数.

命题 9.3.8 若  $\sigma$  和 b 是有界的利普希茨函数, 则  $(P_{t})_{t\geqslant0}$  是费勒半群.

证明 因 (9.3.23) 式对于一切有界连续函数 $f$ 成立, 只需证明当 $f \in C_0(\mathbb{R})$ 时有 $P_t f \in C_0(\mathbb{R})$. 根据 (9.3.3) 式有

$$
\begin{array}{l} \mathbf {E} [ (X _ {t} ^ {x} - x) ^ {2} ] \leqslant 2 \mathbf {E} \Bigg \{\left[ \int_ {0} ^ {t} \sigma (X _ {s} ^ {x}) \mathrm{d} B _ {s} \right] ^ {2} \Bigg \} + 2 \mathbf {E} \Bigg \{\left[ \int_ {0} ^ {t} b (X _ {s} ^ {x}) \mathrm{d} s \right] ^ {2} \Bigg \} \\ \leqslant 2 \mathbf {E} \Big [ \int_ {0} ^ {t} \sigma (X _ {s} ^ {x}) ^ {2} \mathrm{d} s \Big ] + 2 t \mathbf {E} \Big [ \int_ {0} ^ {t} b (X _ {s} ^ {x}) ^ {2} \mathrm{d} s \Big ] \\ \leqslant 2 t \big (\| \sigma \| ^ {2} + t \| b \| ^ {2} \big). \\ \end{array}
$$

根据上式和马尔可夫不等式,

$$
\lim _ {r \to \infty} \sup _ {x \in \mathbb {R}} \mathbf {P} \big (| X _ {t} ^ {x} - x | > r \big) = 0.
$$

对于 $r > 0$ 有

$$
\mathbf {E} [ f (X _ {t} ^ {x}) ] \leqslant \mathbf {E} \big [ f (X _ {t} ^ {x}) 1 _ {\{| X _ {t} ^ {x} - x | \leqslant r \}} \big ] + \| f \| \mathbf {P} \big (| X _ {t} ^ {x} - x | > r \big).
$$

由上式和有界收敛定理得

$$
\operatorname * {l i m s u p} _ {| x | \to \infty} \mathbf {E} [ f (X _ {t} ^ {x}) ] \leqslant \| f \| \sup _ {x \in \mathbb {R}} \mathbf {P} \big (| X _ {t} ^ {x} - x | > r \big).
$$

再由 r > 0 的任意性,

$$
\lim _ {| x | \to \infty} P _ {t} f (x) = \lim _ {| x | \to \infty} \mathbf {E} [ f (X _ {t} ^ {x}) ] = 0.
$$

因此有 $P_{t}f\in C_{0}(\mathbb{R})$ □

---

248

第九章 随机积分及其应用

## \*9.3.4 柯西初值问题

设 $(X_{t}:t\geqslant 0)$ 是由随机微分方程(9.3.3)定义的的扩散过程.这里假定扩散系数$\sigma$ 和漂移系数 $b$ 都是有界利普希茨函数.令 $C_b^2 (\mathbb{R})$ 是 $\mathbb{R}$ 上二次连续可微且其本身和前两阶导数均有界的函数全体构成的集合.对于 $f\in C_b^2 (\mathbb{R})$ 写

$$
L f (x) = \frac {1}{2} \sigma^ {2} (x) \partial_ {x x} f (x) + b (x) \partial_ {x} f (x), \quad x \in \mathbb {R}. \tag {9.3.26}
$$

根据 (9.3.3) 式和伊藤公式,

$$
f (X _ {t}) = f (X _ {0}) + \int_ {0} ^ {t} f ^ {\prime} (X _ {s}) \sigma (X _ {s}) \mathrm{d} B _ {s} + \int_ {0} ^ {t} L f (X _ {s}) \mathrm{d} s.
$$

令 $X_0 = x$ 并对上式取期望得

$$
P _ {t} f (x) = f (x) + \int_ {0} ^ {t} P _ {s} L f (x) \mathrm{d} s.
$$

对 $t \geqslant 0$ 求导数, 并应用控制收敛定理得

$$
\partial_ {t} P _ {t} f (x) = P _ {t} L f (x), \quad x \in \mathbb {R}. \tag {9.3.27}
$$

给定 $[0, \infty) \times \mathbb{R}$ 上的函数 $u = u(t, x)$, 我们写 $u \in C^{1,2}([0, \infty) \times \mathbb{R})$, 是指该函数有连续的导数 $\partial_t u$, $\partial_x u$ 和 $\partial_{xx} u$ 且函数 $|u| + |\partial_t u| + |\partial_x u| + |\partial_{xx} u|$ 在 $[0, \infty) \times \mathbb{R}$ 上有界. 对于函数 $u \in C^{1,2}([0, \infty) \times \mathbb{R})$, 考虑抛物型偏微分方程:

$$
\partial_ {t} u (t, x) = L u (t, x), \quad t \geqslant 0, x \in \mathbb {R}. \tag {9.3.28}
$$

显然 (9.3.28) 式是例 8.1.4 中的热方程 (8.1.10) 的推广. 求解 (9.3.28) 式满足初值条件 $u(0, \cdot) = f$ 的解的问题称为柯西问题.

对于 (9.3.1) 式的解 $(X_{t}: t \geqslant 0)$ 和 $[0, t] \times \mathbb{R}$ 上的函数 $(r, x) \mapsto u(t - r, x)$ 应用伊藤公式得

$$
\begin{array}{l} u (t - r, X _ {r}) = u (t, X _ {0}) + \int_ {0} ^ {r} \partial_ {x} u (t - s, X _ {s}) \sigma (X _ {s}) \mathrm{d} B _ {s} + \\ \int_ {0} ^ {r} \partial_ {x} u (t - s, X _ {s}) b (X _ {s}) \mathrm{d} s - \int_ {0} ^ {r} \partial_ {t} u (t - s, X _ {s}) \mathrm{d} s + \\ \frac {1}{2} \int_ {0} ^ {r} \partial_ {x x} u (t - s, X _ {s}) \sigma (X _ {s}) ^ {2} \mathrm{d} s \\ = u (t, X _ {0}) + \int_ {0} ^ {r} \partial_ {x} u (t - s, X _ {s}) \sigma (X _ {s}) \mathrm{d} B _ {s}. \\ \end{array}
$$

所以 $\{u(t - r, X_r) : r \in [0, t]\}$ 是有界的 $(\mathcal{F}_t)$ 鞅.特别地，上式对 (9.3.1) 式的满足 $X_0^x = x$ 的唯一解 $(X_t^x : t \geqslant 0)$ 成立.再令 $r = t$ 并取期望得

$$
u (t, x) = P _ {t} f (x) = \mathbf {E} [ f (X _ {t} ^ {x}) ]. \tag {9.3.29}
$$

---

9.3 随机微分方程

249

这就给出了 (9.3.28) 式的柯西问题的解的一个概率表示. 事实上, 在 $b, \sigma$ 和 $f$ 满足适当正则条件的情况下, 由 (9.3.29) 式定义的函数 $u$ 是 (9.3.28) 式的初值问题的唯一解, 参见 [19, p.227, 定理 24.1]. 关于随机微分方程和扩散过程的更为深入的讨论, 还可以参考 [20, 22, 29, 38] 等.

## 练习题

1. 令 $(X_{t})$ 为由(9.3.17)式定义的奥恩斯坦-乌伦贝克过程.

(1) 证明 $(X_{t})$ 是朗之万方程 (9.3.18) 的解;
(2) 给出  $(X_{t})$  的转移半群  $(P_{t})$ ;
(3) 证明 $(P_{t})$ 是费勒半群; (4) 证明: 若 $b > 0$, 则 $X_{t}$ 的分布弱收敛到正态分布 $N(0, \sigma^{2} / 2b)$.
2. 证明由 (9.3.20) 式给出的过程 $(S_{t})$ 是 (9.3.19) 式的解.
3. 利用关于正态分布的积分给出由 (9.3.20) 式定义的几何布朗运动 $(S_{t})$ 的转移半群 $(P_{t})$ 的表示并证明 $(P_{t})$ 是费勒半群.
4. 令 $g \in C_b^2(\mathbb{R})$ 而 $L$ 是由 (9.3.26) 式定义的微分算子. 再设 $[0, \infty) \times \mathbb{R}$ 上的函数 $v = v(t, x)$ 有连续的导数 $\partial_t v, \partial_x v$ 和 $\partial_{xx} v$ 且函数 $|v| + |\partial_t v| + |\partial_x v| + |\partial_{xx} v|$ 在 $[0, \infty) \times \mathbb{R}$ 上有界. 证明: 若 $v$ 满足偏微分方程

$$
\partial_ {t} v (t, x) = L v (t, x) + g (x) v (t, x),
$$

则它可以表示为

$$
v (t, x) = \mathbf {E} \Big [ v (0, X _ {t} ^ {x}) \exp \Big \{\int_ {0} ^ {t} g (X _ {s} ^ {x}) \mathrm{d} s \Big \} \Big ].
$$

提示: 参见 [19, p.230, 定理 24.2].
