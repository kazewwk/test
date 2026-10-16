# 第二章 鞅论基础

原始 PDF 第 43–74 页。

36

第二章 鞅论基础

鞅是一类非常重要的随机过程. 从条件期望的观点看, 鞅具有相对平稳性. 鞅方法是现代随机过程理论中最重要的工具之一. 本章介绍鞅论的基本结果, 包括鞅 (上、下鞅) 的概念、离散时间下鞅的不等式、有界停止定理、收敛定理、连续时间鞅论等. 作为预备知识, 回顾了期望和条件期望的基本性质, 并对流和停时进行了简单的讨论.

## 2.1 预备知识

## 2.1.1 数学期望

考虑概率空间 $(\Omega, \mathcal{F}, \mathbf{P})$. 设 $\xi$ 为此概率空间上的随机变量. 令 $\mu_{\xi}$ 和 $F_{\xi}$ 分别为 $\xi$ 在 $\mathbb{R}^d$ 上的概率分布和分布函数. 若 $f$ 为 $\mathbb{R}^d$ 上的博雷尔可测函数, 则随机变量 $f(\xi)$ 的数学期望可表示为斯蒂尔切斯积分

$$
\mathbf {E} f (\xi) = \int_ {\mathbb {R} ^ {d}} f (x) \mathrm{d} F _ {\xi} (x), \tag {2.1.1}
$$

或者用测度积分表示为

$$
\mathbf {E} f (\xi) = \int_ {\Omega} f (\xi (\omega)) \mathbf {P} (\mathrm{d} \omega) = \int_ {\mathbb {R} ^ {d}} f (x) \mu_ {\xi} (\mathrm{d} x). \tag {2.1.2}
$$

若  $\mathbf{E}|f(\xi)|<\infty,$  则称随机变量  $f(\xi)$  是可积的.

值得指出的是, 上面借助斯蒂尔切斯积分定义数学期望的方法有一定的局限性. 例如, 即使 $f$ 为 $\mathbb{R}^d$ 上的有界博雷尔可测函数, (2.1.1) 式右边的积分也可能没有意义. 利用测度积分的表示 (2.1.2) 式则没有这样的问题. 不过对于本书中所遇到的函数, 上面两种积分都是有意义的. 想了解关于测度的严格积分理论的读者, 可以参考高等概率论的著作. 根据本书上册中的讨论, 关于数学期望有如下的定理:

定理 2.1.1 设可积随机变量  $\xi$  和  $\eta$  关于子  $\sigma$  代数  $G \subseteq F$  可测, 则  $\mathbf{P}(\xi \leqslant \eta) = 1$  当且仅当对任何  $A \in G$  都有  $\mathbf{E}(\xi 1_{A}) \leqslant \mathbf{E}(\eta 1_{A})$ .

推论 2.1.2 设可积随机变量  $\xi$  和  $\eta$  关于子  $\sigma$  代数  $G \subseteq F$  可测, 则  $\mathbf{P}(\xi = \eta) = 1$  当且仅当对任何  $A \in G$  都有  $\mathbf{E}(\xi 1_{A}) = \mathbf{E}(\eta 1_{A})$ .

定理 2.1.3 (单调收敛定理) 设  $\xi, \xi_{n}, n = 1, 2, \cdots$  为非负随机变量且单调不降地有  $\lim_{n \to \infty} \xi_{n} \stackrel{a.s.}{=} \xi$ ，则有  $\lim_{n \to \infty} E\xi_{n} = E\xi$ .

定理 2.1.4 (法图 (Fatou) 定理) 对于任何非负随机变量  $\xi_{n}, n = 1, 2, \cdots$ ，有

$$
\operatorname * {l i m i n f} _ {n \to \infty} \mathbf {E} \xi_ {n} \geqslant \mathbf {E} \big (\operatorname * {l i m i n f} _ {n \to \infty} \xi_ {n} \big). \tag {2.1.3}
$$

---

2.1 预备知识

37

定理 2.1.5（控制收敛定理） 设随机变量  $\xi, \xi_{n}, n = 1, 2, \cdots$  满足  $\lim_{n \to \infty} \xi_{n} \stackrel{a.s.}{=} \xi$ .
若有非负可积随机变量  $\eta$  使得  $|\xi_{n}| \leqslant \eta$  (a.s.),  $n = 1, 2, \cdots$ ，则有  $\lim_{n \to \infty} E\xi_{n} = E\xi$ .

上面的控制收敛定理的条件可以弱化. 称 $(\Omega, \mathcal{F}, \mathbf{P})$ 上的一列随机变量 $\{\xi_n\}$ 是一致可积的, 是指当 $c \to \infty$ 时有

$$
\sup _ {n \geqslant 1} \mathbf {E} \big (| \xi_ {n} | 1 _ {\{| \xi_ {n} | \geqslant c \}} \big) \to 0.
$$

特别地, 不难看出对任何  $\alpha > 1$  有

$$
\mathbf {E} (| \xi_ {n} | 1 _ {\{| \xi_ {n} | \geqslant c \}}) \leqslant c ^ {1 - \alpha} \mathbf {E} (| \xi_ {n} | ^ {\alpha} 1 _ {\{| \xi_ {n} | \geqslant c \}}) \leqslant c ^ {1 - \alpha} \mathbf {E} (| \xi_ {n} | ^ {\alpha}).
$$

因此, 若 $\sup_{n\geqslant 1}\mathbf{E}(|\xi_n|^{\alpha}) < \infty$ ，则 $\{\xi_n\}$ 是一致可积的.

定理 2.1.6 设随机变量  $\xi, \xi_{1}, \xi_{2}, \cdots$  满足  $\lim_{n\to\infty}\xi_{n}\stackrel{a.s.}{=} \xi$ . 若序列  $\{\xi_{n}\}$  一致可积,
则有  $\lim_{n\to\infty}\mathbf{E}\xi_{n}=\mathbf{E}\xi.$

证明 由一致可积性, 对任何 $\varepsilon > 0$, 当 $c(c > 0)$ 充分大时有

$$
\sup _ {n \geqslant 1} \mathbf {E} \big (\xi_ {n} 1 _ {\{\xi_ {n} <   - c \}} \big) \geqslant - \sup _ {n \geqslant 1} \mathbf {E} \big (| \xi_ {n} | 1 _ {\{| \xi_ {n} | > c \}} \big) \geqslant - \varepsilon .
$$

因此有

$$
\mathbf {E} \xi_ {n} = \mathbf {E} \big (\xi_ {n} 1 _ {\{\xi_ {n} \geqslant - c \}} \big) + \mathbf {E} \big (\xi_ {n} 1 _ {\{\xi_ {n} <   - c \}} \big) \geqslant \mathbf {E} \big (\xi_ {n} 1 _ {\{\xi_ {n} \geqslant - c \}} \big) - \varepsilon .
$$

对 $(\xi_{n} - c)1_{\{\xi_{n}\geqslant -c\}}$ 应用法图定理可得

$$
\operatorname * {l i m i n f} _ {n \to \infty} \mathbf {E} \big (\xi_ {n} 1 _ {\{\xi_ {n} \geqslant - c \}} \big) \geqslant \mathbf {E} \big (\operatorname * {l i m i n f} _ {n \to \infty} \xi_ {n} 1 _ {\{\xi_ {n} \geqslant - c \}} \big) \geqslant \mathbf {E} \big (\operatorname * {l i m i n f} _ {n \to \infty} \xi_ {n} \big).
$$

因此有

$$
\operatorname * {l i m i n f} _ {n \to \infty} \mathbf {E} \xi_ {n} \geqslant \mathbf {E} \big (\operatorname * {l i m i n f} _ {n \to \infty} \xi_ {n} \big) - \varepsilon .
$$

再由 $\varepsilon > 0$ 的任意性得

$$
\operatorname * {l i m i n f} _ {n \to \infty} \mathbf {E} \xi_ {n} \geqslant \mathbf {E} \big (\operatorname * {l i m i n f} _ {n \to \infty} \xi_ {n} \big).
$$

类似地, 可得

$$
\operatorname * {l i m s u p} _ {n \to \infty} \mathbf {E} \xi_ {n} \leqslant \mathbf {E} \big (\operatorname * {l i m s u p} _ {n \to \infty} \xi_ {n} \big).
$$

因为  $\lim_{n\to\infty}\xi_{n}\stackrel{a.s.}{=} \xi,$  以上二式右边的积分都等于  $E\xi,$  故欲证结果成立. □

---

38

第二章 鞅论基础

值域为有限集合的可测函数称为简单函数. 根据上面的关于数学期望的收敛定理, 经常可以利用结构较为简单的随机变量的期望逼近一般随机变量的期望. 典型的做法如下: 对于整数 $n \geqslant 1$ 令

$$
\phi_ {n} (x) = n 1 _ {\{x \geqslant n \}} + \sum_ {k = 1} ^ {n 2 ^ {n}} 2 ^ {- n} (k - 1) 1 _ {[ (k - 1) / 2 ^ {n}, k / 2 ^ {n})} (x), \quad x \geqslant 0. \tag {2.1.4}
$$

显然, 对任意的 $x \geqslant 0$ 有 $\phi_n(x) \uparrow x$. 对于非负随机变量 $\xi$, 当 $n \to \infty$ 时有 $\phi_n(\xi) \uparrow \xi$. 再由积分单调收敛定理有 $\mathbf{E}[\phi_n(\xi)] \uparrow \mathbf{E}\xi$.

## 2.1.2 条件数学期望

定义 2.1.1 设 X 为概率空间  $(\Omega, \mathcal{F}, \mathbf{P})$  上的可积随机变量. 考虑子  $\sigma$  代数  $G \subseteq F$ . 如果对于一切事件  $A \in G$  有

$$
\mathbf {E} (1 _ {A} \xi) = \mathbf {E} (1 _ {A} X), \tag {2.1.5}
$$

则称关于 $\mathcal{G}$ 可测的随机变量 $\xi$ 为 $X$ 的给定 $\mathcal{G}$ 的条件数学期望或条件期望, 并记之为 $\mathbf{E}(X|\mathcal{G})$. 对于 $B \in \mathcal{F}$, 称条件期望 $\mathbf{E}(1_B|\mathcal{G})$ 为 $B$ 的给定 $\mathcal{G}$ 的条件概率, 并记之为 $\mathbf{P}(B|\mathcal{G})$.

根据高等概率论中的结果, 满足定义 2.1.1 中要求的随机变量 $\xi$ 存在; 如可参见 [37]. 由推论 2.1.2 知, 该随机变量在几乎必然相等的意义下唯一. 若 $Z$ 是另一随机变量, 我们写 $\mathbf{E}(X|Z) = \mathbf{E}[X|\sigma(Z)]$. 注意, 这个记号与上册中定义的条件期望相吻合.

定理 2.1.7 设 X 和 Y 是概率空间  $(\Omega, \mathcal{F}, \mathbf{P})$  上的可积随机变量, 则有如下性质:

(1)  $\mathbf{E}[\mathbf{E}(X|\mathcal{G})]=\mathbf{E}(X);$
(2) 若 X 与 G 独立, 则  $\mathbf{E}(X|\mathcal{G}) = \mathbf{E}(X)$ ;
(3) 对任何 $a \in \mathbb{R}$ 有 $\mathbf{E}(aX|\mathcal{G}) = a\mathbf{E}(X|\mathcal{G})$;
(4) $\mathbf{E}(X + Y|\mathcal{G}) = \mathbf{E}(X|\mathcal{G}) + \mathbf{E}(Y|\mathcal{G})$;
(5) 若 $X \leqslant Y$, 则有 $\mathbf{E}(X|\mathcal{G}) \leqslant \mathbf{E}(Y|\mathcal{G})$.

证明 在 (2.1.5) 式中取 $A = \Omega$ 即可得性质 (1). 若 $X$ 与 $\mathcal{G}$ 独立, 则对任何 $A \in \mathcal{G}$ 随机变量 $1_A$ 与 $X$ 独立, 故有

$$
\mathbf {E} (1 _ {A} X) = \mathbf {E} (1 _ {A}) \mathbf {E} X = \mathbf {E} (1 _ {A} \mathbf {E} X),
$$

再由推论 2.1.2 知性质 (2) 成立. 对任何 $A \in \mathcal{G}$ 有

$$
\mathbf {E} (1 _ {A} a X) = a \mathbf {E} (1 _ {A} X) = a \mathbf {E} [ 1 _ {A} \mathbf {E} (X | \mathscr {G}) ] = \mathbf {E} [ 1 _ {A} a \mathbf {E} (X | \mathscr {G}) ],
$$

因而性质 (3) 成立. 类似地可以证明性质 (4) 和 (5) 成立. $\square$

---

2.1 预备知识

39

定理 2.1.8 设 X 为概率空间  $(\Omega, \mathcal{F}, \mathbf{P})$  上的随机变量且数学期望 EX 存在, 再设  $\xi$  为关于子  $\sigma$  代数  $G \subseteq F$  可测的随机变量, 则  $\xi = \mathbf{E}(X|\mathcal{G})$  当且仅当对任何 G 可测随机变量 Y, 只要  $Y\xi$  或 YX 可积, 就有

$$
\mathbf {E} (Y \xi) = \mathbf {E} (Y X). \tag {2.1.6}
$$

证明 若 (2.1.6) 式成立, 则对 $A \in \mathcal{G}$ 取 $Y = 1_A$ 即知 $\xi = \mathbf{E}(X|\mathcal{G})$. 反之, 假设 $\xi = \mathbf{E}(X|\mathcal{G})$, 下证 (2.1.6) 式成立. 根据数学期望的线性性, 只需考虑 $X, \xi$ 和 $Y$ 都是非负随机变量的情况. 此时, 显然 (2.1.5) 式对于任意的 $A \in \mathcal{G}$ 成立. 因此, 当 $Y$ 是 $\mathcal{G}$ 中有限个集合的示性函数的线性组合时 (2.1.6) 式成立. 特别地, 若 $\phi_n$ 由 (2.1.4) 式给出, 则有 $\mathbf{E}[\phi_n(Y)X] = \mathbf{E}[\phi_n(Y)\xi]$. 令 $n \to \infty$ 并应用单调收敛定理即得 (2.1.6) 式. □

推论 2.1.9 设 X, Y 是  $(\Omega, \mathcal{F}, \mathbf{P})$  上的随机变量且 Y 关于 G 可测. 若 X 和 YX 都可积, 则

$$
\mathbf {E} (Y X | \mathcal {G}) = Y \mathbf {E} (X | \mathcal {G}). \tag {2.1.7}
$$

证明 对任何 $A \in \mathcal{G}$, 因 $1_A Y$ 和 $1_A$ 都关于 $\mathcal{G}$ 可测, 应用 (2.1.6) 式得

$$
\mathbf {E} \big [ 1 _ {A} Y \mathbf {E} (X | \mathcal {G}) \big ] = \mathbf {E} (1 _ {A} Y X) = \mathbf {E} \big [ 1 _ {A} \mathbf {E} (Y X | \mathcal {G}) \big ].
$$

又因  $Y\mathbf{E}(X|\mathcal{G})$  关于 G 可测, 故 (2.1.7) 式成立. □

推论 2.1.10 设 X 为可积随机变量, 而  $G_{1} \subseteq G_{2}$  都是 F 的子  $\sigma$  代数, 则

$$
\mathbf {E} \big [ \mathbf {E} (X | \mathcal {G} _ {2}) | \mathcal {G} _ {1} \big ] = \mathbf {E} (X | \mathcal {G} _ {1}).
$$

证明 对任何 $A \in \mathcal{G}_1 \subseteq \mathcal{G}_2$, 应用 (2.1.7) 式得

$$
\mathbf {E} \big \{1 _ {A} \mathbf {E} \big [ \mathbf {E} (X | \mathcal {G} _ {2}) | \mathcal {G} _ {1} \big ] \big \} = \mathbf {E} \big \{\mathbf {E} \big [ \mathbf {E} (1 _ {A} X | \mathcal {G} _ {2}) | \mathcal {G} _ {1} \big ] \big \} = \mathbf {E} (1 _ {A} X).
$$

因  $\mathbf{E}[\mathbf{E}(1_{A}X|\mathcal{G}_{2})|\mathcal{G}_{1}]$  关于  $G_{1}$  可测, 故知欲证结论成立. □

## 2.1.3 流和停时

考虑概率空间 $(\Omega, \mathcal{F}, \mathbf{P})$. 令 $I = \mathbb{Z}_{+}$ 或 $\mathbb{R}_{+}$. 如果 $\mathcal{F}$ 的子 $\sigma$ 代数族 $(\mathcal{F}_t : t \in I)$ 满足对任何 $s < t \in I$ 都有 $\mathcal{F}_s \subseteq \mathcal{F}_t$, 就称它是 $\sigma$ 代数流或简称流. 对应于 $I = \mathbb{Z}_{+}$ 或 $\mathbb{R}_{+}$, 我们也经常将 $(\mathcal{F}_t : t \in I)$ 写为 $(\mathcal{F}_t : t \geqslant 0)$ 或 $(\mathcal{F}_n : n \geqslant 0)$. 直观上, 可以将 $\sigma$ 代数 $\mathcal{F}_t$ 解释为观测某些随机现象到 $t \in I$ 时刻所积累的知识或信息.

称状态空间 $(E, \mathcal{E})$ 上的随机过程 $X = (X_{t}: t \in I)$ 关于某个流 $(\mathcal{F}_{t}: t \in I)$ 是适应的, 是指对任何 $t \in I$, 随机变量 $X_{t}$ 都是 $\mathcal{F}_{t}$ 可测的. 直观上, 过程 $X$ 关于流 $(\mathcal{F}_{t})$ 适应

---

40

第二章 鞅论基础

可以解释为 X 的运动情况在我们的观测范围内, 或者说我们到任何时刻 t 积累的知识都包含了 X 在此时刻前的运动情况的所有信息. 给定过程 X, 定义

$$
\mathscr {F} ^ {X} = \sigma (\{X _ {s}: s \in I \}), \mathscr {F} _ {t} ^ {X} = \sigma (\{X _ {s}: s \in I, s \leqslant t \}), \tag {2.1.8}
$$

则 $(\mathcal{F}_t^X: t \in I)$ 构成一个流, 称为 $X$ 的自然流, 称 $(\mathcal{F}^X, \mathcal{F}_t^X: t \in I)$ 为 $X$ 的自然 $\sigma$ 代数. 显然 $X$ 关于其自然流 $(\mathcal{F}_t^X: t \in I)$ 适应, 且它在 $X$ 所适应的流中是最小的.

定义 2.1.2 称映射 $T: \Omega \to I \cup \{\infty\}$ 为关于流 $(\mathcal{F}_t : t \in I)$ 的停时或可选时, 是指对任何 $t \in I$ 都有

$$
\{T \leqslant t \} = \{\omega \in \Omega : T (\omega) \leqslant t \} \in \mathscr {F} _ {t}. \tag {2.1.9}
$$

对于给定的 $(\mathcal{F}_{t})$ 停时T, 定义

$$
\mathcal {F} _ {T} = \{A \in \mathcal {F} _ {\infty}: \text {对任意} t \in I \text {有} A \cap \{T \leqslant t \} \in \mathcal {F} _ {t} \},
$$

其中 $\mathcal{F}_{\infty} = \sigma \left( \bigcup_{t \in I} \mathcal{F}_t \right)$. 易证 $\mathcal{F}_T$ 是一个 $\sigma$ 代数, 称为 $T$ 前 $\sigma$ 代数.

停时 $T$ 是相对于某个流而言的. 当流 $(\mathcal{F}_t)$ 明确时, 我们简单地称 $T$ 为停时. 直观上, 性质 $\{T \leqslant t\} \in \mathcal{F}_t$ 表示根据时刻 $t$ 我们掌握的信息 $\mathcal{F}_t$ 可以判断 $T$ 是否已经在 $t$ 时刻或更早地到来. 停时 $\sigma$ 代数 $\mathcal{F}_T$ 可以解释为到随机时刻 $T$ 我们掌握的所有知识或信息的总和. 不难证明, 停时 $T$ 关于 $\sigma$ 代数 $\mathcal{F}_T$ 可测. 另外, 若 $S$ 和 $T$ 都是停时且 $S \leqslant T$, 则 $\mathcal{G}_S \subseteq \mathcal{G}_T$.

命题 2.1.11 若 S 和 T 是  $(\mathcal{F}_{t})$  的停时, 则  $S \vee T, S \wedge T$  和  $S + T$  也是  $(\mathcal{F}_{t})$  的停时.

证明 由 $\{S \vee T \leqslant t\} = \{S \leqslant t\} \cap \{T \leqslant t\}$ 和 $\{S \wedge T \leqslant t\} = \{S \leqslant t\} \cup \{T \leqslant t\}$ 知 $S \vee T$ 和 $S \wedge T$ 是 $(\mathcal{F}_t)$ 的停时. 若 $I = \mathbb{Z}_+$, 则对 $t \in I$ 有

$$
\{S + T = t \} = \bigcup_ {k = 0} ^ {t} \{S = k, T = t - k \} \in \mathscr {F} _ {t},
$$

因而 $S + T$ 是 $(\mathcal{F}_t)$ 的停时.下面考虑 $I = \mathbb{R}_{+}$ 的情况.此时，对任何 $t\geqslant 0$ 有 $\{S>$ $t\} \cup \{T > t\} \in \mathcal{F}_t.$ 而且

$$
\begin{array}{l} \{S + T > t \} = \{S > t \} \cup \{S + T > t, S \leqslant t \} \\ = \{S > t \} \cup \{t - T <   S \leqslant t \}, \tag {2.1.10} \\ \end{array}
$$

其中  $\{S > t\} \in F_{t}$ . 令 Q 表示有理数集, 则有

$$
\{t - T <   S \leqslant t \} = \bigcup_ {r \in [ 0, t) \cap \mathbb {Q}} \{t - T <   r \leqslant S \leqslant t \}
$$

---

2.1 预备知识

41

$$
= \bigcup_ {r \in [ 0, t) \cap \mathbb {Q}} \{T > t - r \} \cap \{S \geqslant r \} \cap \{S \leqslant t \},
$$

其中 $\{T > t - r\} \in \mathcal{F}_{t-r} \subseteq \mathcal{F}_t, \{S \geqslant r\} \in \mathcal{F}_r \subseteq \mathcal{F}_t$ 而 $\{S \leqslant t\} \in \mathcal{F}_t$. 所以 $\{t - T < S \leqslant t\} \in \mathcal{F}_t$. 由 (2.1.10) 式知 $\{S + T > t\} \in \mathcal{F}_t$, 故 $T + S$ 是 $(\mathcal{F}_t)$ 的停时. □

例 2.1.1 映射 $T: \Omega \to \{0, 1, \cdots\} \cup \{\infty\}$ 是关于离散时间流 $(\mathcal{F}_n)$ 的停时当且仅当对任何 $n \geqslant 0$ 都有 $\{T = n\} \in \mathcal{F}_n$. 此时 $A \in \mathcal{F}_T$ 当且仅当对任何 $n \geqslant 0$ 都有 $A \cap \{T = n\} \in \mathcal{F}_n$.

例 2.1.2 设离散时间随机过程  $(X_{n})$  关于流  $(\mathcal{F}_{n})$  适应. 再设 T 为  $(\mathcal{F}_{n})$  的停时, 则对任意的  $n \geqslant 0$  和  $i \in E$  有

$$
\{T <   \infty \} \cap \{X _ {T} = i \} \cap \{T = n \} = \{X _ {n} = i \} \cap \{T = n \} \in \mathcal {G} _ {n},
$$

故有 $\{T < \infty\} \cap \{X_T = i\} \in \mathcal{G}_T$. 这说明映射 $\omega \mapsto X_{T(\omega)}(\omega)$ 限制在 $\{T < \infty\}$ 上关于 $\{T < \infty\} \cap \mathcal{G}_T$ 可测.

设 $X = (X_{t}:t\in I)$ 是以 $E$ 为状态空间的随机过程. 分别称 $\tau_A\coloneqq \inf \{t\in I:X_t\in A\}$ 和 $T_{A}:= \inf \{t\in I:t > 0,X_{t}\in A\}$ 为 $X$ 对于集合 $A\subseteq E$ 的首达时与击中时. 直观上 $\tau_{A}$ 和 $T_{A}$ 分别是在考虑和不考虑初始位置的情况下, 随机过程 $X$ 首次进入集合 $A$ 的时刻.

例 2.1.3 设状态空间  $(E, \mathcal{E})$  上的离散时间随机过程  $(X_{n})$  关于流  $(\mathcal{F}_{n})$  适应, 则 X 对于集合  $A \in E$  的首达时  $\tau_{A}$  和击中时  $T_{A}$  都是停时. 例如, 我们有  $\{\tau_{A} \leqslant n\} = \bigcup_{k=0}^{n} \{X_{k} \in A\} \in \mathscr{F}_{n}$ .

设 $\{\xi_n : n \geqslant 1\}$ 是独立同分布随机变量序列. 令 $(\mathcal{F}_n)$ 是 $(\xi_n)$ 的自然 $\sigma$ 代数流. 再定义从原点出发的随机游动

$$
X _ {n} = \sum_ {i = 1} ^ {n} \xi_ {i}, \quad n \geqslant 0. \tag {2.1.11}
$$

注意 $(\mathcal{F}_n)$ 也是 $(X_{n})$ 的自然流. 下面命题的结论称为沃尔德 (Wald) 恒等式.

命题 2.1.12 (沃尔德恒等式) 设  $\mathbf{E}(\xi_{1})$  存在而 T 是关于  $(\mathcal{F}_{n})$  的停时, 则

$$
\mathbf {E} (X _ {T}) = \mathbf {E} (T) \mathbf {E} (\xi_ {1}).
$$

证明 因 $T$ 是 $(\mathcal{F}_n)$ 的停时, 事件 $\{T \geqslant n\} = \{T \leqslant n - 1\}^c \in \mathcal{F}_{n-1}$ 独立于 $\xi_n$. 从而

$$
\begin{array}{l} \mathbf {E} (X _ {T}) = \mathbf {E} \Big (\sum_ {n = 1} ^ {\infty} \xi_ {n} 1 _ {\{n \leqslant T \}} \Big) = \sum_ {n = 1} ^ {\infty} \mathbf {E} \big (\xi_ {n} 1 _ {\{n \leqslant T \}} \big) \\ = \sum_ {n = 1} ^ {\infty} \mathbf {E} (\xi_ {n}) \mathbf {E} (1 _ {\{n \leqslant T \}}) = \mathbf {E} (\xi_ {1}) \sum_ {n = 1} ^ {\infty} \mathbf {P} (n \leqslant T). \\ \end{array}
$$

---

42

第二章 鞅论基础

再由非负整数值随机变量 T 的期望的计算公式即得欲证等式. □

## 2.1.4 完备化和加强化

给定概率空间 $(\Omega, \mathcal{F}, \mathbf{P})$, 我们称 $N \subseteq \Omega$ 为 $\mathbf{P}$ 零集, 如果存在 $A \in \mathcal{F}$ 满足 $N \subseteq A$ 且 $\mathbf{P}(A) = 0$. 用 $\mathcal{N}$ 表示所有 $\mathbf{P}$ 零集构成的集类. 记 $\mathcal{F}^* = \sigma(\mathcal{F} \cup \mathcal{N})$.

命题 2.1.13 我们有  $\mathscr{F}^{*}=\{F\cup N:F\in\mathscr{F},N\in\mathscr{N}\}$ .

证明 记 $\bar{\mathcal{F}} = \{F \cup N : F \in \mathcal{F}, N \in \mathcal{N}\}$. 显然 $\bar{\mathcal{F}} \subseteq \sigma(\mathcal{F} \cup \mathcal{N}) = \mathcal{F}^*$. 另一方面, 易见 $\Omega \in \bar{\mathcal{F}}$ 且 $\bar{\mathcal{F}}$ 对可数并运算封闭. 现设 $B = F \cup N \in \bar{\mathcal{F}}$, 其中 $F \in \mathcal{F}$ 且 $N \in \mathcal{N}$, 则存在 $A \in \mathcal{F}$ 满足 $N \subseteq A$ 且 $\mathbf{P}(A) = 0$. 注意

$$
B ^ {c} = F ^ {c} \cap N ^ {c} = (F ^ {c} \cap A ^ {c}) \cup (F ^ {c} \cap N ^ {c} \cap A),
$$

其中 $(F^{c} \cap A^{c}) \in \mathcal{F}$ 且 $(F^{c} \cap N^{c} \cap A) \in \mathcal{N}$, 故 $B^{c} \in \bar{\mathcal{F}}$. 所以 $\bar{\mathcal{F}}$ 是 $\sigma$ 代数. 又因为 $\bar{\mathcal{F}} \supseteq \mathcal{F} \cup \mathcal{N}$, 故有 $\bar{\mathcal{F}} \supseteq \sigma(\mathcal{F} \cup \mathcal{N}) = \mathcal{F}^{*}$. □

若 $A \in \mathcal{F}^*$ 可表示为 $A = F \cup N$, 其中 $F \in \mathcal{F}$ 而 $N \in \mathcal{N}$, 我们记 $\mathbf{P}^*(A) = \mathbf{P}(F)$. 易证该记号无歧义, 且 $\mathbf{P}^*$ 为 $\mathcal{F}^*$ 上的概率测度. 分别称 $\mathcal{F}^*$ 和 $\mathbf{P}^*$ 为 $\mathcal{F}$ 和 $\mathbf{P}$ 的完备化. 当 $\mathcal{F} = \mathcal{F}^*$ 时, 称 $\mathcal{F}$ 或 $\mathbf{P}$ 是完备的, 此时也称 $(\Omega, \mathcal{F}, \mathbf{P})$ 是完备概率空间.

对于 $\mathcal{F}$ 的子 $\sigma$ 代数 $\mathcal{G}$, 称 $\mathcal{G}^* := \sigma(\mathcal{G} \cup \mathcal{N})$ 为 $\mathcal{G}$ 的加强化. 若 $\mathcal{G} = \mathcal{G}^*$, 则称 $\mathcal{G}$ 是加强的. 如果一个流 $(\mathcal{G}_t : t \in I)$ 中的每个 $\mathcal{G}_t$ 都是加强的 $\sigma$ 代数, 就称该流是加强的.

我们称 $A \triangle B := (A \setminus B) \cup (B \setminus A)$ 为集合 $A, B \subseteq \Omega$ 的对称差. 易知, 对于 $A, B, C \subseteq \Omega$ 有

$$
A = B \triangle C \Leftrightarrow B = C \triangle A \Leftrightarrow C = A \triangle B.
$$

若有 $A \triangle B \in \mathcal{N}$, 则写成 $A \sim B$. 不难看出“$\sim$”是 $\Omega$ 的子集间的等价关系.

命题 2.1.14 令  $G^{*}$  为 F 的子  $\sigma$  代数 G 的完备化, 则有

$\mathcal{G}^{*} = \{B\triangle C:B\in \mathcal{G},C\in \mathcal{N}\} = \{A\subseteq \Omega :$ 有 $B\in \mathcal{G}$ 使 $A\triangle B\in \mathcal{N}\}$

证明 记 $\bar{\mathcal{G}} = \{A := B \triangle C : B \in \mathcal{G}, C \in \mathcal{N}\}$. 易知欲证等式中的第二个等号成立, 只需证明 $\mathcal{G}^* = \bar{\mathcal{G}}$. 显然 $\bar{\mathcal{G}} \subseteq \sigma(\mathcal{G} \cup \mathcal{N}) = \mathcal{G}^*$. 下面证明 $\bar{\mathcal{G}} \supseteq \mathcal{G}^*$, 而因 $\bar{\mathcal{G}} \supseteq \mathcal{G} \cup \mathcal{N}$, 只需证 $\bar{\mathcal{G}}$ 是 $\sigma$ 代数. 显然 $\Omega \in \bar{\mathcal{G}}$. 设 $A \in \bar{\mathcal{G}}$. 则存在 $B \in \mathcal{G}$ 使 $A \triangle B \in \mathcal{N}$. 易见 $A^c \triangle B^c = A \triangle B \in \mathcal{N}$. 再因 $B^c \in \mathcal{G}$, 有 $A^c \in \bar{\mathcal{G}}$. 所以 $\bar{\mathcal{G}}$ 对取余运算封闭. 对于集合列 $\{A_n\} \subseteq \bar{\mathcal{G}}$, 存在 $\{B_n\} \subseteq \mathcal{G}$ 使对每个 $n \geqslant 0$ 有 $A_n \triangle B_n \in \mathcal{N}$. 注意 $\bigcup_{n} B_n \in \mathcal{G}$ 且

$$
\bigg (\bigcup_ {n} A _ {n} \bigg) \triangle \bigg (\bigcup_ {n} B _ {n} \bigg) \subseteq \bigcup_ {n} (A _ {n} \triangle B _ {n}) \in \mathcal {N},
$$

---

2.1 预备知识

43

故 $\bigcup_{n}A_{n}\in \bar{\mathcal{G}}$ 因此 $\bar{\mathcal{G}}$ 是一个 $\sigma$ 代数. □

例2.1.4 设 $\Omega = \Omega_0 \cup \Omega_1$, 其中 $\Omega_0, \Omega_1$ 为不交的非空集合. 令 $\mathcal{F} = \{\varnothing, \Omega_0, \Omega_1, \Omega\}$. 再设 $\mathbf{P}$ 为 $(\Omega, \mathcal{F})$ 上的概率测度, 且满足 $\mathbf{P}(\Omega_0) = 0$ 和 $\mathbf{P}(\Omega_1) > 0$, 则每个 $A \in \mathcal{F}^*$ 都可表示为 $A = A_0 \cup B$ 的形式, 其中 $A_0 \subseteq \Omega_0$ 而 $B \in \mathcal{F}$. 此时有 $\mathbf{P}^*(A) = \mathbf{P}(B)$.

## 2.1.5 连续时间流

考虑概率空间 $(\Omega, \mathcal{G}, \mathbf{P})$ 上的连续时间 $\sigma$ 代数流 $(\mathcal{G}_t : t \geqslant 0)$. 对 $t \geqslant 0$ 令 $\mathcal{G}_{t+} = \bigcap_{s > t} \mathcal{G}_s$, 则 $\mathcal{G}_{t+} \supseteq \mathcal{G}_t$ 且 $(\mathcal{G}_{t+})$ 也是 $\sigma$ 代数流. 如果对一切 $t \geqslant 0$ 有 $\mathcal{G}_{t+} = \mathcal{G}_t$, 就称流 $(\mathcal{G}_t)$ 右连续. 对于 $(\mathcal{G}_{t+})$ 的停时 $T$, 将相应的 $T$ 前 $\sigma$ 代数记为 $\mathcal{G}_{T+}$.

命题 2.1.15 非负随机变量 T 是  $(\mathcal{G}_{t+})$  的停时当且仅当对任何  $t \geqslant 0$  都有  $\{T < t\} \in G_t$ .

证明 若 $T$ 是 $(\mathcal{G}_{t+})$ 的停时, 则对任何 $t \geqslant 0$ 有 $\{T < t\} = \bigcup_{n} \{T \leqslant t - 1/n\} \in \mathcal{G}_t$. 反之, 假设对任何 $t \geqslant 0$ 都有 $\{T < t\} \in \mathcal{G}_t$. 对于 $k \geqslant 1$, 有

$$
\{T \leqslant t \} = \bigcap_ {n = k} ^ {\infty} \{T <   t + 1 / n \} \in \mathscr {G} _ {t + 1 / k},
$$

故 $\{T\leqslant t\} \in \bigcap_{k\geqslant 1}\mathcal{G}_{t + 1 / k} = \mathcal{G}_{t + }$ 故 $T$ 是 $(\mathcal{G}_{t + })$ 的停时. □

命题 2.1.16 令 T 是  $(\mathcal{G}_{t+})$  的停时. 再设  $A \in G_{\infty}$ ，则  $A \in G_{T+}$  当且仅当对任何  $t \geqslant 0$  都有  $A \cap \{T < t\} \in \mathcal{G}_{t}$ .

证明 若 $A \in \mathcal{F}_{T+}$, 则对任何 $n \geqslant 1$ 有 $A \cap \{T \leqslant t - 1/n\} \in \mathcal{F}_{(T \leqslant t - 1/n)+} \subseteq \mathcal{F}_t$, 进而

$$
A \cap \{T <   t \} = \bigcup_ {n = 1} ^ {\infty} (A \cap \{T \leqslant t - 1 / n \}) \in \mathscr {F} _ {t}.
$$

反之, 若对任何 $t \in I$ 都有 $A \cap \{T < t\} \in \mathscr{F}_t$, 则对任何 $k \geqslant 1$ 有

$$
A \cap \{T \leqslant t \} = \bigcap_ {n = k} ^ {\infty} \left(A \cap \{T <   t + 1 / n \}\right) \in \mathscr {F} _ {t + 1 / k}.
$$

故知 $A \cap \{T \leqslant t\} \in \bigcap_{k=1}^{\infty} \mathscr{F}_{t+1/k} = \mathscr{F}_{t+}$, 因而 $A \in \mathscr{F}_{T+}$. $\square$

命题 2.1.17 设每个  $T_{n}$  是  $(\mathcal{G}_{t}: t \geqslant 0)$  的停时且序列  $\{T_{n}\}$  单调不增，则  $T := \lim_{n} T_{n}$  是  $(\mathcal{G}_{t+})$  的停时.

---

44

第二章 鞅论基础

证明 因 $\{T_n\}$ 单调不增, 有 $\{T < t\} = \bigcup_{n} \{T_n < t\} \in \mathcal{G}_t$. 由命题2.1.15知 $T$ 是 $(\mathcal{G}_{t+})$ 的停时. □

对于  $n \geqslant 0$  记  $D_{n} = \{i/2^{n} : i = 0, 1, 2, \cdots\}$ . 给定  $(\mathcal{G}_{t+})$  的停时 T, 令  $T_{n} = \inf\{t \in D_{n} : t > T\}$ . 注意

$$
T _ {n} = \frac {1}{2 ^ {n}} (\lfloor 2 ^ {n} T \rfloor + 1) = \sum_ {k = 1} ^ {\infty} \frac {k}{2 ^ {n}} 1 _ {\{(k - 1) / 2 ^ {n} \leqslant T <   k / 2 ^ {n} \}} + \infty 1 _ {\{T = \infty \}}. \tag {2.1.12}
$$

显然当 $n \to \infty$ 时, 递降地 $T_{n} \to T$. 称 $T_{n}$ 为 $T$ 的二分点离散化.

命题 2.1.18 由 (2.1.12) 式定义的  $T_{n}$  是关于离散时间流  $(\mathcal{G}_{k/2^{n}}:k\geqslant0)$  的停时且有  $G_{T+}\subseteq G_{T_{n}}$ .

证明 对于 $k \geqslant 0$, 根据命题2.1.15有

$$
\{T _ {n} = k / 2 ^ {n} \} = \{T <   k / 2 ^ {n} \} \cap \{T <   (k - 1) / 2 ^ {n} \} ^ {c} \in \mathscr {G} _ {k / 2 ^ {n}}.
$$

所以 $T_{n}$ 是关于流 $(\mathcal{G}_{k / 2^n}:k\geqslant 0)$ 的停时.对于 $G\in \mathcal{G}_{T + }$ ，由命题2.1.15和命题2.1.16有

$$
G \cap \{T _ {n} = k / 2 ^ {n} \} = G \cap \{T <   k / 2 ^ {n} \} \cap \{T <   (k - 1) / 2 ^ {n} \} ^ {c} \in \mathcal {G} _ {k / 2 ^ {n}},
$$

故 $G \in \mathcal{G}_{T_n}$. 因此 $\mathcal{G}_{T+} \subseteq \mathcal{G}_{T_n}$. $\square$

定义 2.1.3 称完备概率空间  $(\Omega, \mathcal{G}, \mathbf{P})$  上的连续时间流  $(\mathcal{G}_{t}: t \geqslant 0)$  满足通常条件, 是指它是右连续的且每个  $G_{t}$  都是加强的.

## 2.1.6 循序可测过程

设 $(\mathcal{G}_t:t\geqslant 0)$ 为概率空间 $(\Omega ,\mathcal{G},\mathbf{P})$ 上的连续时间 $\sigma$ 代数流.称空间 $\mathbb{R}^d$ 上的连续时间过程 $(X_{t}:t\geqslant 0)$ 关于该流循序可测，是指对任意的 $t\geqslant 0$ 映射 $(s,\omega)\mapsto X_s(\omega)$ 限定在 $[0,t]\times \Omega$ 上关于 $\sigma$ 代数 $\mathcal{B}[0,t]\times \mathcal{G}_t$ 可测,其中 $\mathcal{B}[0,t]$ 表示 $[0,t]$ 上的 $\sigma$ 代数.显然,若 $(X_{t})$ 关于 $(\mathcal{G}_t)$ 循序可测，则它关于该流是适应的.

命题 2.1.19 若连续时间随机过程  $(X_{t})$  关于流  $(\mathcal{G}_{t})$  适应且右连续或左连续, 则  $(X_{t})$  关于  $(\mathcal{G}_{t})$  循序可测.

证明 我们只考虑 $(X_{t})$ 为右连续适应过程的情况, 左连续的情况类似. 对于 $n \geqslant 1$, 定义 $X_{n}(0) = X_{0}$ 和

$$
X _ {n} (s) = X _ {k t / 2 ^ {n}}, \quad (k - 1) t / 2 ^ {n} <   s \leqslant k t / 2 ^ {n}, k = 1, 2, 3, \dots , 2 ^ {n},
$$

则对任何 $B \in \mathcal{B}^d$ 有

$$
\{(s, \omega) \in [ 0, t ] \times \Omega : X _ {n} (s, \omega) \in B \}
$$

---

2.1 预备知识

45

$$
= \{0 \} \times X _ {0} ^ {- 1} (B) \cup \bigcup_ {k = 1} ^ {2 ^ {n}} ((k - 1) t / 2 ^ {n}, k t / 2 ^ {n}) \times X _ {k t / 2 ^ {n}} ^ {- 1} (B),
$$

其中 $X_{kt / 2^n}^{-1}(B)\in \mathcal{G}_{kt / 2^n}\subseteq \mathcal{G}_t$ .显然，上面的集合属于 $\mathcal{B}[0,t]\times \mathcal{G}_t$ .所以映射 $(s,\omega)\mapsto$ $X_{n}(s,\omega)$ 关于 $\mathcal{B}[0,t]\times \mathcal{G}_t$ 可测.因 $X$ 是右连续的，故 $X_{s}(\omega) = \lim_{n}X_{n}(s,\omega)$ 因此$(s,\omega)\mapsto X_s(\omega)$ 关于 $\mathcal{B}[0,t]\times \mathcal{G}_t$ 可测. □

命题 2.1.20 设连续时间随机过程  $(X_{t})$  关于流  $(\mathcal{G}_{t})$  循序可测, 则对任何  $(\mathcal{G}_{t})$  停时的 T, 映射  $\omega \mapsto X_{T(\omega)}(\omega)$  限制在  $\Omega_{T} := \{T < \infty\}$  上关于  $\Omega_{T} \cap G_{T}$  可测.

证明 易证 $\omega \mapsto T(\omega) \wedge t$ 是 $(\Omega, \mathcal{G}_t)$ 到 $([0, t], \mathcal{B}[0, t])$ 的可测映射, 故 $\omega \mapsto (T(\omega) \wedge t, \omega)$ 是 $(\Omega, \mathcal{G}_t)$ 到 $([0, t] \times \Omega, \mathcal{B}[0, t] \times \mathcal{G}_t)$ 的可测映射. 根据命题 2.1.19, 对任何 $t \geqslant 0$ 映射 $(s, \omega) \to X_s(\omega)$ 限定在 $[0, t] \times \Omega$ 上关于 $\sigma$ 代数 $\mathcal{B}[0, t] \times \mathcal{G}_t$ 和 $\mathcal{B}^d$ 可测. 因此复合 $\omega \mapsto (T(\omega) \wedge t, \omega) \mapsto X_{T(\omega) \wedge t}(\omega)$ 是 $(\Omega, \mathcal{G}_t)$ 到 $(\mathbb{R}^d, \mathcal{B}^d)$ 的可测映射. 这样对任意的 $B \in \mathcal{B}^d$ 有

$$
\{X _ {T} \in B \} \cap \Omega_ {T} \cap \{T \leqslant t \} = \{X _ {T \wedge t} \in B \} \cap \{T \leqslant t \} \in \mathscr {G} _ {t},
$$

故 $\{X_T\in B\} \cap \Omega_T\in \mathcal{G}_T$ ，即映射 $\omega \mapsto X_{T(\omega)}(\omega)$ 限制在 $\Omega_T$ 上关于 $\Omega_T\cap \mathcal{G}_T$ 可测.□

命题 2.1.21 设  $(X_{t})$  是关于流  $(\mathcal{G}_{t})$  适应的右连续过程, 则 X 到任何开集  $A \subseteq E$  的首达时  $\tau_{A} := \inf\{t \geqslant 0 : X_{t} \in A\}$  和击中时  $\tau_{A} := \inf\{t > 0 : X_{t} \in A\}$  重合且是  $(\mathcal{G}_{t+})$  的停时.

证明 因 $A$ 是开集, 显然有 $\tau_{A} = T_{A}$. $\mathbb{Q}$ 表示有理数集. 由于 $(X_{t})$ 右连续且关于流 $(\mathcal{G}_{t})$ 适应, 对任何 $t > 0$ 有

$$
\{\tau_ {A} <   t \} = \bigcup_ {s \in [ 0, t) \cap \mathbb {Q}} \{X _ {s} \in A \}.
$$

事实上, 假定 $\tau_{A} < t$, 必有某个 $s \in [\tau_{A}, t)$ 使得 $X_{s} \in A$. 而因 $(X_{t})$ 右连续, 有某个有理数 $r \in [s, t) \subseteq [0, t)$ 使 $X_{r} \in A$, 故上式左端是右端的子集. 相反的包含关系显然, 故上式成立. 显然上式右端属于 $\mathcal{G}_{t}$, 故得 $\{\tau_{A} < t\} \in \mathcal{G}_{t}$. 由命题2.1.15知 $\tau_{A}$ 是 $(\mathcal{G}_{t+})$ 的停时. $\square$

可以证明, 若流 $(\mathcal{G}_t)$ 满足通常条件, 则 $(\mathcal{G}_t)$ 循序可测过程 $(X_t)$ 对于任何集合 $A \in \mathcal{B}^d$ 的首达时 $\tau_A$ 和击中时 $T_A$ 都是 $(\mathcal{G}_t)$ 的停时; 如可参见 [38, p.186, 定理 3.2.13].

## 练习题

1. 设 $\{B_n\} \subseteq \mathcal{F}$ 是 $\Omega$ 的可数划分, 且对每个 $n \geqslant 1$ 有 $\mathbf{P}(B_n) > 0$. 令 $\xi$ 为可积随机变量. 证明 $\mathcal{G} := \sigma(\{B_n\})$ 由 $\{B_n\}$ 中的集合的所有可能的并构成 (规定零个集合的

---

46

第二章 鞅论基础

并为空集)且

$$
\mathbf {E} (\xi | \mathcal {G}) = \sum_ {n = 1} ^ {\infty} 1 _ {B _ {n}} \mathbf {E} (\xi | B _ {n}).
$$

2. 证明对任何 $(\mathcal{F}_t)$ 的停时 $T$ 有 $\{T = \infty\} \in \mathcal{F}_{\infty}$.
3. 证明常数值随机变量 $T \equiv t$ 是停时, 且此时有 $\mathcal{F}_T = \mathcal{F}_t$.
4. 证明泊松过程 $(N_{t})$ 的第 $n$ 次跳跃时间 $S_{n}$ 是关于其自然流 $(\mathcal{F}_t^N)$ 的停时.
5. 直接证明左连续适应过程是循序可测的.

## 2.2 鞅、上鞅和下鞅

在本节中, 我们取 $I = \mathbb{Z}_{+}$ 或 $\mathbb{R}_{+}$. 考虑完备概率空间 $(\Omega, \mathcal{F}, \mathbf{P})$ 上给定的 $\sigma$ 代数流 $(\mathcal{F}_t : t \in I)$.

## 2.2.1 定义和基本性质

定义 2.2.1 设实数值过程 $(X_{t}: t \in I)$ 可积且关于流 $(\mathscr{F}_{t}: t \in I)$ 适应. 若对任何 $t \geqslant s \in I$ 都有 $\mathbf{E}(X_{t} | \mathscr{F}_{s}) = X_{s}$, 则称 $(X_{t})$ 为关于 $(\mathscr{F}_{t})$ 的鞅. 若这里的 “=” 替换为 “$\leqslant$” 或 “$\geqslant$”, 则对应地称 $(X_{t})$ 为关于 $(\mathscr{F}_{t})$ 的上鞅或下鞅. 在流 $(\mathscr{F}_{t})$ 明确的情况下, 简称 $(X_{t})$ 为鞅、上鞅或下鞅.

当 $I = \mathbb{Z}_{+}$ 时, 对应的鞅称为离散时间鞅或者鞅序列; 当 $I = \mathbb{R}_{+}$ 时, 对应的鞅称为连续时间鞅. 显然 $(X_{n}: n \geqslant 0)$ 是离散时间鞅当且仅当对任何 $n \geqslant 0$ 都有 $\mathbf{E}(X_{n+1}|\mathcal{F}_n) = X_n$. 由定义, 立刻得到下列简单性质:

命题 2.2.1 (1) 令 M 和  $M^{+}$  分别表示关于某个给定  $\sigma$  代数流的鞅和下鞅的全体, 那么 M 是一个线性空间, 而  $M^{+}$  是凸锥且对取大运算 V 封闭.

(2) 若 $(X_{t})$ 是 $(\mathcal{F}_{t})$ 下鞅, 则 $t \mapsto \mathbf{E}(X_{t})$ 递增. 另外, 下鞅 $(X_{t})$ 是鞅当且仅当 $t \mapsto \mathbf{E}(X_{t})$ 是常数.
(3) 若 $(X_{t})$ 是鞅, $\phi$ 是凸函数且每个 $\phi(X_{t})$ 可积, 则 $(\phi(X_{t}))$ 是下鞅. 因此 $(|X_{t}|)$ 是下鞅, 而若每个 $X_{t}$ 平方可积, 则 $(X_{t}^{2})$ 是下鞅.
(4) 若 $(X_{t})$ 是下鞅, $\phi$ 是递增凸函数且每个 $\phi(X_{t})$ 可积, 则 $(\phi(X_{t}))$ 也是下鞅. 因此 $(X_{t}^{+})$ 是下鞅.

例 2.2.1 设  $\{\xi_{n}: n \geqslant 1\}$  为独立同分布的随机变量序列, 且有  $\mathbf{P}(\xi_{n}=1)=p$  和  $\mathbf{P}(\xi_{n}=-1)=q$ , 其中  $p, q \geqslant 0$  且  $p+q=1$ . 任取整数值  $X_{0}=k$  并令  $X_{n}=X_{0}+\sum_{i=1}^{n}\xi_{i}$

---

2.2 鞅、上鞅和下鞅

47

$(n \geqslant 1)$ , 则  $(X_{n})$  为简单随机游动. 再令  $(\mathscr{F}_{n})$  为  $(X_{n})$  的自然流. 我们有

$$
\begin{array}{l} \mathbf {E} (X _ {n + 1} | \mathcal {F} _ {n}) = \mathbf {E} (X _ {n + 1} - X _ {n} | \mathcal {F} _ {n}) + \mathbf {E} (X _ {n} | \mathcal {F} _ {n}) \\ = \mathbf {E} (\xi_ {n + 1} | \mathcal {F} _ {n}) + X _ {n} = \mathbf {E} (\xi_ {n + 1}) + X _ {n} \\ = (p - q) + X _ {n}. \\ \end{array}
$$

当 $p = q$ 时, $(X_{n})$ 是对称的简单随机游动, 此时它是鞅. 当 $p \geqslant q$ 时, $(X_{n})$ 是下鞅; 当 $p \leqslant q$ 时, $(X_{n})$ 是上鞅. 简单随机游动可用来描述赌博中某个赌徒的赌资. 从概率平均的角度看, 鞅的情况对应于对双方公平的博弈.

例 2.2.2 设  $\sigma^{2} \geqslant 0$  和  $b \in R$  为常数, 而  $(B_{t}: t \geqslant 0)$  是以  $\sigma^{2}$  为参数的布朗运动. 称  $(B_{t} + bt : t \geqslant 0)$  为带漂移的布朗运动. 设  $E|B_{0}| < \infty$ , 则当  $b = 0 (\geqslant 0, \leqslant 0)$  时  $(B_{t} + bt : t \geqslant 0)$  是关于  $(B_{t} : t \geqslant 0)$  的自然流的鞅 (下鞅, 上鞅).

鞅、上鞅或下鞅的概念与流有关. 若 $X$ 关于大的适应流是鞅, 它关于小的适应流也是鞅. 显然, $X$ 是上鞅当且仅当 $-X$ 是下鞅, 而 $X$ 是鞅当且仅当它既是上鞅也是下鞅. 因此, 后面的结果只对上鞅或下鞅叙述.

命题 2.2.2 设可积过程  $(X_{t})$  关于  $(\mathcal{F}_{t})$  适应. 那么  $(X_{t})$  是关于流  $(\mathcal{F}_{t})$  的下鞅当且仅当对于  $s \leqslant t \in I$  和  $A \in F_{s}$  有  $\mathbf{E}(X_{s}; A) \leqslant \mathbf{E}(X_{t}; A)$ .

证明 由定理2.1.1知 $(X_{t})$ 关于流 $(\mathcal{F}_t)$ 是下鞅当且仅当对于任意 $s\leqslant t\in I$ 和$A\in \mathcal{F}_s$ 有 $\mathbf{E}(X_s;A)\leqslant \mathbf{E}[\mathbf{E}(X_t|\mathcal{F}_s);A] = \mathbf{E}(X_t;A)$ □

命题 2.2.3 如果  $(X_{t})$  是关于流  $(\mathcal{F}_{t})$  的下鞅, 它也是关于加强的流  $(\mathcal{F}_{t}^{*})$  的下鞅.

证明 因为 $(X_{t})$ 关于 $(\mathcal{F}_t)$ 适应, 它也关于 $(\mathcal{F}_t^*)$ 适应. 考虑 $s \leqslant t \in I$ 和 $B \in \mathcal{F}_s^*$. 根据命题2.1.14, 存在 $A \in \mathcal{F}_s$ 使得 $\mathbf{P}(A \triangle B) = 0$. 而由命题2.2.2有

$$
\mathbf {E} (X _ {s}; B) = \mathbf {E} (X _ {s}; A) \leqslant \mathbf {E} (X _ {t}; A) = \mathbf {E} (X _ {t}; B).
$$

再由命题 2.2.2 知  $(X_{t})$  是  $(\mathcal{F}_{t}^{*})$  下鞅. □

定理 2.2.4 (杜布分解) 若  $(X_{n})$  相对流  $(\mathcal{F}_{n})$  为下鞅, 则存在相对该流的鞅  $(Z_{n})$  和从原点出发的可料单增过程  $(A_{n})$ , 使得  $X_{n}=Z_{n}+A_{n}, n\geqslant0$ . 此外, 这样的分解是唯一的且

$$
A _ {n} = \sum_ {i = 1} ^ {n} \left[ \mathbf {E} (X _ {i} | \mathscr {F} _ {i - 1}) - X _ {i - 1} \right].
$$

证明 假设有 $(\mathcal{F}_n)$ 适应过程 $(Z_{n})$ 和从原点出发的可料过程 $(A_{n})$ 使得 $X_{n} = Z_{n} + A_{n}$. 对于 $n \geqslant 1$, 定义 $\mathcal{F}_{n-1}$ 可测随机变量 $\xi_{n} = A_{n} - A_{n-1}$. 注意 $A_{n} = \sum_{i=1}^{n} \xi_{i}$. 另

---

48

第二章 鞅论基础

外

$$
\begin{array}{l} \xi_ {n} = \mathbf {E} (X _ {n} - Z _ {n} - X _ {n - 1} + Z _ {n - 1} | \mathcal {F} _ {n - 1}) \\ = \mathbf {E} (X _ {n} | \mathscr {F} _ {n - 1}) - \mathbf {E} (Z _ {n} | \mathscr {F} _ {n - 1}) - X _ {n - 1} + Z _ {n - 1}. \\ \end{array}
$$

所以 $(Z_{n})$ 是鞅当且仅当 $\xi_{n} = \mathbf{E}(X_{n}|\mathcal{F}_{n - 1}) - X_{n - 1}$ ($n\geqslant 1$), 而此时 $(X_{n})$ 为 $(\mathcal{F}_n)$ 的下鞅当且仅当 $(\xi_n)$ 为非负可料过程, 即 $(A_{n})$ 为从原点出发的单增可料过程. 这就证明了定理结论成立. □

例 2.2.3 设  $(S_{n}: n \geqslant 1)$  是从原点出发的一维对称简单随机游动. 根据定理 2.2.4 有下鞅分解  $|S_{n}| = M_{n} + A_{n}$ ，其中  $(A_{n})$  为从原点出发的可料单增过程且

$$
A _ {n} = \sum_ {i = 1} ^ {n} \left[ \mathbf {E} (| S _ {i} | | \mathcal {F} _ {i - 1}) - | S _ {i - 1} | \right].
$$

易知, 对  $i \geqslant 1$  有

$$
| S _ {i} | = \left\{ \begin{array}{l l} | S _ {i - 1} | + \xi_ {i}, & S _ {i - 1} > 0, \\ | S _ {i - 1} | - \xi_ {i}, & S _ {i - 1} <   0, \\ 1, & S _ {i - 1} = 0. \end{array} \right.
$$

因此

$$
\mathbf {E} (| S _ {i} | | \mathscr {F} _ {i - 1}) = \left\{ \begin{array}{l l} | S _ {i - 1} |, & S _ {i - 1} \neq 0, \\ 1, & S _ {i - 1} = 0. \end{array} \right.
$$

故有 $A_{n} = \mathrm{Card}\{i:1\leqslant i\leqslant n:S_{i - 1} = 0\}$ .由于

$$
\mathbf {P} (S _ {2 k - 1} = 0) = 0, \quad \mathbf {P} (S _ {2 k} = 0) = \binom{2 k}{k} \frac {1}{4 ^ {k}},
$$

不难计算出

$$
\mathbf {E} (| S _ {n} |) = \sum_ {i = 0} ^ {n - 1} \mathbf {P} (S _ {i} = 0) = \sum_ {i = 0} ^ {\lfloor (n - 1) / 2 \rfloor} \binom{2 k}{k} \frac {1}{4 ^ {k}}.
$$

中文的“鞅”为形声字. 这里“央”为聚拢之意, 而“革”指皮带, 联合起来本义是一头套在牛马颈部, 另一头掌握在驾驭者手里的皮带. 主要指双马双牛或多马多牛齐驱并驾时抓在驾驭者手里的牛马颈带. 英文词 martingale 原意是一种用来控制马头的皮带, 也指一类于 18 世纪流行于法国的投注策略, 其中最简单的一种为博弈而设计. 在此博弈中, 赌徒每局投掷一枚硬币, 若硬币正面朝上, 则赌徒赢得赌本; 若硬币反面朝上, 则赌徒输掉赌本. 概率论中的鞅的概念由莱维 (Paul Pierre Lévy) 提出, 而其基础理论则是杜布 (Joseph Leo Doob) 建立的.

---

2.2 鞅、上鞅和下鞅

49

## 2.2.2 杜布鞅

定义 2.2.2 设 Y 为实可积随机变量. 对于  $t \in I$  令  $X_{t} = \mathbf{E}(Y|\mathcal{F}_{t})$ , 则  $X = (X_{t}: t \in I)$  是一个关于  $(\mathcal{F}_{t})$  的鞅, 称为右闭鞅或杜布鞅.

命题 2.2.5 杜布鞅  $X = (X_{t} : t \in I)$  是一致可积的.

证明 设 $X_{t} = \mathbf{E}(Y|\mathcal{F}_{t})$ 由上面定义给出, 其中 $Y$ 为可积随机变量. 由延森 (Jensen) 不等式得 $|X_{t}| \leqslant \mathbf{E}(|Y||\mathcal{F}_{t})$. 根据定理 2.1.1, 对任意的 $\lambda > 0$ 有

$$
\mathbf {E} (| X _ {t} |; | X _ {t} | > \lambda) \leqslant \mathbf {E} [ \mathbf {E} (| Y | | \mathscr {F} _ {t}); | X _ {t} | > \lambda ] = \mathbf {E} (| Y |; | X _ {t} | > \lambda).
$$

再取 $n \geqslant 1$ 得

$$
\begin{array}{l} \mathbf {E} (| Y |; | X _ {t} | > \lambda) \leqslant \mathbf {E} (| Y |; | X _ {t} | > \lambda , | Y | > n) + n \mathbf {P} (| X _ {t} | > \lambda , | Y | \leqslant n) \\ \leqslant \mathbf {E} (| Y |; | Y | > n) + n \mathbf {P} (| X _ {t} | > \lambda), \\ \end{array}
$$

其中

$$
\mathbf {P} (| X _ {t} | > \lambda) \leqslant \frac {1}{\lambda} \mathbf {E} | X _ {t} | = \frac {1}{\lambda} \mathbf {E} [ | \mathbf {E} (Y | \mathscr {F} _ {t}) | ] \leqslant \frac {1}{\lambda} \mathbf {E} | Y |.
$$

所以

$$
\operatorname * {l i m s u p} _ {\lambda \to \infty} \sup _ {t \in I} \mathbf {E} (| X _ {t} |; | X _ {t} | > \lambda) \leqslant \mathbf {E} (| Y |; | Y | > n).
$$

由 $n \geqslant 1$ 的任意性知上式左边为零, 即 $X = (X_{t}: t \in I)$ 是一致可积的. $\square$

## 2.2.3 局部鞅

定义 2.2.3 关于流  $(\mathcal{F}_{t}: t \in I)$  适应的实值过程  $M = (M_{t}: t \in I)$  称为局部鞅，是指存在单增的停时列  $\{\tau_{k}\}$  满足  $\lim_{k \to \infty} \tau_{k} \stackrel{a.s.}{=} \infty$ ，且对任何  $k \geqslant 1$ ，停止过程  $M^{\tau_{k}} = (M_{t \wedge \tau_{k}}: t \in I)$  关于流  $(\mathcal{F}_{t}: t \in I)$  是鞅。此时  $\{\tau_{k}\}$  称为 M 的局部化序列。

显然, 鞅是局部鞅.

命题 2.2.6 可积的非负局部鞅是上鞅.

证明 设 $X = (X_{t}: t \in I)$ 是非负局部鞅, 而 $\{\tau_{k}\}$ 为相应的局部化序列. 对于任意 $t \geqslant r \in I$, 由条件数学期望的法图定理有

$$
\mathbf {E} (X _ {t} | \mathscr {F} _ {r}) \leqslant \operatorname * {l i m i n f} _ {k \to \infty} \mathbf {E} (X _ {t \wedge \tau_ {k}} | \mathscr {F} _ {r}) = \operatorname * {l i m i n f} _ {k \to \infty} X _ {r \wedge \tau_ {k}} = X _ {r}.
$$

所以 $X$ 是上鞅. $\square$

---

50

第二章 鞅论基础

## 练习题

1. 设 $\alpha \geqslant 0$ 和 $\beta \in \mathbb{R}$ 为常数, 而 $(N_t : t \geqslant 0)$ 是以 $\alpha$ 为参数的泊松过程. 设 $\mathbf{E}(N_0) < \infty$. 证明当 $\beta = \alpha (\geqslant \alpha, \leqslant \alpha)$ 时 $(N_t - \beta t : t \geqslant 0)$ 是关于 $(N_t : t \geqslant 0)$ 的自然流的鞅 (上鞅, 下鞅).
2. 设 $\{\xi_n : n \geqslant 0\}$ 是独立随机变量序列且 $\mathbf{E}(\xi_n) = 1 (n \geqslant 0)$. 令 $(\mathscr{F}_n)$ 为 $(\xi_n)$ 的自然流, 再对 $n \geqslant 0$ 令 $X_n = \prod_{i=0}^{n} \xi_i$. 证明 $(X_n)$ 是关于 $(\mathscr{F}_n)$ 的鞅.
3. 设流 $(\mathcal{F}_t: t \in I)$ 和 $(\mathcal{G}_t: t \in I)$ 满足 $\mathcal{F}_t \subseteq \mathcal{G}_t$ ($t \in I$) 而实值过程 $(X_t: t \in I)$ 关于流 $(\mathcal{F}_t: t \in I)$ 适应. 证明: 若 $(X_t)$ 关于流 $(\mathcal{G}_t)$ 是下鞅, 则它关于流 $(\mathcal{F}_t)$ 是下鞅.
4. 设 $(X_{t}: t \geqslant 0)$ 和 $(Y_{t}: t \geqslant 0)$ 都是关于流 $(\mathcal{F}_t)_{t \geqslant 0}$ 的下鞅. 证明 $(X_{t} \vee Y_{t}: t \geqslant 0)$ 是关于 $(\mathcal{F}_t)_{t \geqslant 0}$ 的下鞅.
5. 设 $(X_{t}: t \geqslant 0)$ 和 $(Y_{t}: t \geqslant 0)$ 都是关于流 $(\mathcal{F}_t)_{t \geqslant 0}$ 的上鞅. 证明 $(X_{t} \wedge Y_{t}: t \geqslant 0)$ 是关于 $(\mathcal{F}_t)_{t \geqslant 0}$ 的上鞅.
6. 设 $(X_{t}: t \geqslant 0)$ 是关于流 $(\mathcal{F}_t)_{t \geqslant 0}$ 的非负平方可积下鞅, 而 $C$ 为常数. 证明 $(X_{t}^{2} \vee C: t \geqslant 0)$ 是关于 $(\mathcal{F}_t)_{t \geqslant 0}$ 的下鞅.

## 2.3 杜布停止定理

本节主要讨论离散时间下鞅, 即 $I = \mathbb{Z}_{+}$ 的情况. 设 $(\Omega, \mathcal{F}, \mathbf{P})$ 是完备的概率空间, 而 $(\mathcal{F}_n : n \geqslant 0)$ 是其上的离散时间 $\sigma$ 代数流. 随机过程 $(H_n : n \geqslant 0)$ 称为可料的, 是指 $H_0$ 是 $\mathcal{F}_0$ 可测的且对任意的 $n \geqslant 1$, 随机变量 $H_n$ 关于 $\mathcal{F}_{n-1}$ 可测.

## 2.3.1 下鞅的停止过程

设有实值适应过程 $X = (X_{n}:n\geqslant 0)$ 和可料过程 $H = (H_n:n\geqslant 0)$. 令 $(H\cdot X)_0 = H_0X_0$. 对 $n\geqslant 1$ 令

$$
(H \cdot X) _ {n} = (H \cdot X) _ {n - 1} + H _ {n} (X _ {n} - X _ {n - 1}). \tag {2.3.1}
$$

称 $\{(H\cdot X)_n:n\geqslant 0\}$ 为 $H$ 关于 $X$ 的离散积分.由上面递推公式得

$$
(H \cdot X) _ {n} = H _ {0} X _ {0} + \sum_ {i = 1} ^ {n} H _ {i} (X _ {i} - X _ {i - 1}), \quad n \geqslant 1. \tag {2.3.2}
$$

---

2.3 杜布停止定理

51

(为了在符号上区别乘积与随机积分, 我们写乘积时一般不用点.) 上式实际上是随机分析中的随机积分的离散时间形式.

命题 2.3.1 设  $H \cdot X$  可积. 若 X 是鞅, 则  $H \cdot X$  是鞅; 若 X 是下鞅且 H 非负, 则  $H \cdot X$  是下鞅.

证明 显然 $H \cdot X$ 是适应的. 对 $n \geqslant 1$ 我们有

$$
\begin{array}{l} \mathbf {E} [ (H \cdot X) _ {n} - (H \cdot X) _ {n - 1} | \mathcal {F} _ {n - 1} ] = \mathbf {E} (H _ {n} (X _ {n} - X _ {n - 1}) | \mathcal {F} _ {n - 1}) \\ = H _ {n} \mathbf {E} (X _ {n} - X _ {n - 1} | \mathscr {F} _ {n - 1}). \\ \end{array}
$$

因此 X 是鞅 (对应地, X 是下鞅且 H 非负) 蕴涵着  $H \cdot X$  是鞅 (对应地, 下鞅). □

给定停时 $\tau$, 令 $H_{n} = 1_{\{n \leqslant \tau\}} = 1 - 1_{\{\tau \leqslant n - 1\}}$. 注意 $H_{0} = 1$, 且 $H_{n}$ 关于 $\mathscr{F}_{n-1}$ 可测. 再利用 (2.3.2) 式得

$$
X _ {\tau \wedge n} = X _ {0} + \sum_ {i = 1} ^ {n \wedge \tau} (X _ {i} - X _ {i - 1}) = X _ {0} + \sum_ {i = 1} ^ {n} 1 _ {\{i \leqslant \tau \}} (X _ {i} - X _ {i - 1}) = (H \cdot X) _ {n}.
$$

显然, 每个 $(H \cdot X)_n$ 可积. 根据命题 2.3.1, 我们有

命题 2.3.2 若 X 是下鞅而  $\tau$  是停时, 则停止过程  $X^{\tau} = (X_{\tau \wedge n} : n \geqslant 0)$  也是下鞅.

## 2.3.2 杜布有界停止定理

若对任意的 $n$, 随机变量 $H_{n}$ 有界, 则称过程 $H = (H_{n}: n \geqslant 0)$ 是局部有界的. 不难证明, 如果 $X$ 可积, 且 $H$ 局部有界, 那么 $H \cdot X$ 是可积的. 下面的定理称为杜布有界停止定理, 是鞅论中非常本质的结果.

定理 2.3.3 设 X 为下鞅,  $\sigma$  和  $\tau$  是有界停时且  $\sigma \leqslant \tau$ , 那么  $X_{\sigma}$  和  $X_{\tau}$  是可积的且

$$
\mathbf {E} (X _ {\tau} | \mathscr {F} _ {\sigma}) \geqslant X _ {\sigma}.
$$

证明 取 $N$ 使得 $\tau \leqslant N$. 由命题2.3.2知 $X_{\sigma} = X_{N}^{\sigma}$ 和 $X_{\tau} = X_{N}^{\tau}$ 均可积. 根据定理2.1.1, 只需证明对任意的 $B \in \mathcal{F}_{\sigma}$ 有

$$
\mathbf {E} (X _ {\sigma}; B) \leqslant \mathbf {E} [ \mathbf {E} (X _ {\tau} | \mathscr {F} _ {\sigma}); B ] = \mathbf {E} (X _ {\tau}; B).
$$

以下分两步进行讨论:

(1) 设 $0 \leqslant \tau - \sigma \leqslant 1$. 此时, 我们可以写

$$
\mathbf {E} (X _ {\tau} - X _ {\sigma}; B) = \sum_ {n = 1} ^ {N} \mathbf {E} (X _ {\tau} - X _ {\sigma}; B \cap \{\sigma = n - 1 \} \cap \{\tau = n \})
$$

---

52

第二章 鞅论基础

$$
= \sum_ {n = 1} ^ {N} \mathbf {E} (X _ {n} - X _ {n - 1}; B \cap \{\sigma = n - 1 \} \cap \{\tau = n \}).
$$

注意对任意的 $1 \leqslant n \leqslant N$ 有

$$
B \cap \{\sigma = n - 1 \} \cap \{\tau = n \} = B \cap \{\sigma = n - 1 \} \cap \{\tau > n - 1 \} \in \mathcal {F} _ {n - 1}.
$$

由下鞅性

$$
\begin{array}{l} \mathbf {E} (X _ {\tau} - X _ {\sigma}; B) = \sum_ {n = 1} ^ {N} \mathbf {E} \{\mathbf {E} [ (X _ {n} - X _ {n - 1}) 1 _ {B \cap \{\sigma = n - 1 \} \cap \{\tau = n \}} | \mathcal {F} _ {n - 1} ] \} \\ = \sum_ {n = 1} ^ {N} \mathbf {E} [ \mathbf {E} (X _ {n} - X _ {n - 1} | \mathscr {F} _ {n - 1}) 1 _ {B \cap \{\sigma = n - 1 \} \cap \{\tau = n \}} ] \geqslant 0. \\ \end{array}
$$

(2) 在一般情形, 令 $\tau_{n} = \tau \wedge (\sigma + n)$, 其中 $0 \leqslant n \leqslant N$, 则每个 $\tau_{n}$ 为停时且 $0 \leqslant \tau_{n} - \tau_{n-1} \leqslant 1$. 由于 $B \in \mathscr{F}_{\sigma} \subseteq \mathscr{F}_{\tau_{n}}$, 由上面证明的结论

$$
\mathbf {E} (X _ {\sigma}; B) = \mathbf {E} (X _ {\tau_ {0}}; B) \leqslant \mathbf {E} (X _ {\tau_ {1}}; B) \leqslant \dots \leqslant \mathbf {E} (X _ {\tau_ {N}}; B) = \mathbf {E} (X _ {\tau}; B).
$$

故得欲证结论. □

推论 2.3.4 设 X 为可积适应过程, 则 X 是鞅当且仅当对任何有界停时  $\sigma \leqslant \tau$  有  $\mathbf{E}(X_{\sigma}) = \mathbf{E}(X_{\tau})$ , 或等价地对任何有界停时  $\tau$  有  $\mathbf{E}(X_{\tau}) = \mathbf{E}(X_{0})$ .

证明 设 $X$ 为鞅. 由定理2.3.3, 对任何有界停时 $\sigma \leqslant \tau$ 有 $X_{\sigma} = \mathbf{E}(X_{\tau}|\mathcal{F}_{\sigma})$, 两端取期望得 $\mathbf{E}(X_{\sigma}) = \mathbf{E}(X_{\tau})$. 反之, 设对任何有界停时 $\sigma \leqslant \tau$ 有 $\mathbf{E}(X_{\sigma}) = \mathbf{E}(X_{\tau})$. 取 $N$ 使得 $\tau \leqslant N$. 对任何 $B \in \mathscr{F}_{\sigma} \subseteq \mathscr{F}_{\tau}$ 令

$$
\sigma_ {B} = \sigma 1 _ {B} + N 1 _ {B ^ {c}}, \quad \tau_ {B} = \tau 1 _ {B} + N 1 _ {B ^ {c}}.
$$

下面验证  $\sigma_{B}$  和  $\tau_{B}$  是停时. 事实上, 若 n < N, 则

$$
\{\sigma_ {B} \leqslant n \} = \{\sigma \leqslant n \} \cap B \in \mathscr {F} _ {n}, \quad \{\tau_ {B} \leqslant n \} = \{\tau \leqslant n \} \cap B \in \mathscr {F} _ {n};
$$

而若 $n \geqslant N$, 则 $\{\sigma_B \leqslant n\} = \{\tau_B \leqslant n\} = \Omega \in \mathscr{F}_n$. 因此, 由假定有 $\mathbf{E}(X_{\sigma_B}) = \mathbf{E}(X_{\tau_B})$, 或写为

$$
\mathbf {E} (X _ {\sigma}; B) + \mathbf {E} (X _ {N}; B ^ {c}) = \mathbf {E} (X _ {\tau}; B) + \mathbf {E} (X _ {N}; B ^ {c}).
$$

这推出

$$
\mathbf {E} (X _ {\sigma}; B) = \mathbf {E} (X _ {\tau}; B) = \mathbf {E} [ \mathbf {E} (X _ {\tau} 1 _ {B} | \mathcal {F} _ {\sigma}) ] = \mathbf {E} [ \mathbf {E} (X _ {\tau} | \mathcal {F} _ {\sigma}); B ].
$$

再由推论2.1.2得 $X_{\sigma} = \mathbf{E}(X_{\tau}|\mathcal{F}_{\sigma})$ .因而 $X$ 是鞅. □

---

2.3 杜布停止定理

53

若 $\{X_{n}: n \geqslant 0\}$ 是鞅且 $\tau$ 是有界停时, 则由推论2.3.4有 $\mathbf{E}(X_{\tau}) = \mathbf{E}(X_{0})$. 下面的定理说明这个等式对于某些无界停时也是正确的.

定理 2.3.5 设  $(X_{n}: n \geqslant 0)$  是鞅,  $\tau$  是停时. 如果 (1)  $\mathbf{P}(\tau < \infty) = 1$ ;

(2)  $P|X_{\tau}| < \infty$ ; (3)  $\lim_{n \to \infty} \mathbf{E}(X_{n}; \tau > n) = 0$ , 那么  $\mathbf{E}(X_{\tau}) = \mathbf{E}(X_{0})$ .

证明 利用有界停止定理, 有

$$
\mathbf {E} (X _ {0}) = \mathbf {E} (X _ {\tau \wedge n}) = \mathbf {E} (X _ {\tau}; \tau \leqslant n) + \mathbf {E} (X _ {n}; \tau > n) \rightarrow \mathbf {E} (X _ {\tau}) \quad (n \rightarrow \infty).
$$

这里最后的极限关系成立是由于条件 (1), (2), (3) 及控制收敛定理. □

例 2.3.1 我们在例 2.2.1 中提到过, 在赌博对局中, 鞅表达了一种公平性原则. 然而, 它只说明赌博的每一局是公平的, 其最后的结果仍然可能是不公平的. 考虑由从 0 出发的对称简单随机游动描述的赌博游戏. 赌徒开局时持有赌资为零. 如果他可以决定赌博的停止时间, 那么他可以规定自己在钱数达到 a > 0 后离开. 根据游动的常返性, 他总可实现该目标. 之所以会出现这种不公平的结果, 是因为赌徒可以无利息无限制地借款, 而且可以随意决定停止的时刻. 所以同一个具有无限赌资的赌徒进行赌博是不公平的. 此例还说明杜布停止定理对于一般的 (有限但无界) 停时未必成立.

## 2.3.3 非负上鞅的吸收性

定理 2.3.6 设 X 为非负上鞅. 令  $\sigma = \min\{k \geqslant 0 : X_{k} = 0\}$ ，那么对任意的  $n \geqslant 0$  有  $P\{\sigma \leqslant n, X_{n} > 0\} = 0$ .

证明 固定 $a > 0$, 并令 $\tau = \min \{k \geqslant \sigma : X_k \geqslant a\}$. 易证 $\sigma$ 和 $\tau$ 是停时, 而且 $\sigma \leqslant \tau$. 另外, 显然有 $X_{\sigma} = 0$ 和 $X_{\tau} \geqslant a$. 由定理2.3.3, 对任意的 $n \geqslant 0$ 有

$$
\begin{array}{l} 0 \geqslant \mathbf {E} (X _ {\tau \wedge n} - X _ {\sigma \wedge n}) \\ = \mathbf {E} (X _ {\tau} - X _ {\sigma}; \tau \leqslant n) + \mathbf {E} (X _ {n} - X _ {\sigma}; \sigma <   n <   \tau) + \mathbf {E} (X _ {n} - X _ {n}; \sigma \geqslant n) \\ \geqslant a \mathbf {P} (\tau \leqslant n) + \mathbf {E} (X _ {n}; \sigma <   n <   \tau) \\ \geqslant a \mathbf {P} (\tau \leqslant n). \\ \end{array}
$$

因此 $\mathbf{P}(\tau \leqslant n) = 0$。显然 $\{\sigma \leqslant n, X_n \geqslant a\} \subseteq \{\tau \leqslant n\}$，故 $\mathbf{P}(\sigma \leqslant n, X_n \geqslant a) = 0$。令 $a \to 0$ 即得所需结论。$\square$

上述定理说明非负上鞅在某时刻到达零点后会被该点吸收.

## 练习题

1. 设实值过程 $(X_{n}: n \geqslant 0)$ 关于流 $(\mathcal{F}_n: n \geqslant 0)$ 是可料的鞅. 证明对任何 $n \geqslant 1$ 有 $X_{n} \stackrel{\mathrm{a.s.}}{=} X_{0}$.

---

54

第二章 鞅论基础

2. 设 $(X_{n}: n \geqslant 0)$ 是关于流 $(\mathcal{F}_n: n \geqslant 0)$ 的下鞅. 令 $X_{n}^{*} = \max_{0 \leqslant k \leqslant n} X_{k}$. 证明 $(X_{n}^{*}: n \geqslant 0)$ 是关于 $(\mathcal{F}_n)$ 的下鞅.
3. 设 $(X_{n}: n \geqslant 0)$ 是关于流 $(\mathcal{F}_n: n \geqslant 0)$ 的下鞅, 而 $\{\tau_n : n \geqslant 0\}$ 是单增的有界停时序列. 证明 $(X_{\tau_n})$ 是关于 $(\mathcal{F}_{\tau_n})$ 的下鞅.
4. 设 $(X_{n}: n \geqslant 0)$ 是鞅, 且对有限停时 $\tau$ 满足 $\mathbf{E}(\sup_{k \geqslant 0} |X_{\tau \wedge k}|) < \infty$. 证明 $\mathbf{E}[X_{\tau}] = \mathbf{E}[X_{0}]$.
5. 设 $(S_{n}: n \geqslant 0)$ 是从 $x \in \mathbb{Z}$ 出发的对称简单随机游动. 对 $y \in \mathbb{Z}$ 令 $\tau_{y} = \inf \{n \geqslant 0 : S_{n} = y\}$. 利用 $(S_{n}: n \geqslant 0)$ 的鞅性质证明: 若 $a, b \in \mathbb{Z}$ 满足 $a < x < b$, 则有

$$
\mathbf {P} (\tau_ {b} > \tau_ {a}) = \frac {b - x}{b - a}, \quad \mathbf {P} (\tau_ {a} > \tau_ {b}) = \frac {x - a}{b - a}.
$$

6. 设 $(S_{n}: n \geqslant 0)$ 是从原点出发的对称简单随机游动. 设 $a, b \in \mathbb{Z}$ 满足 $a < 0 < b$. 采用上题的记号, 求 $\tau = \tau_{a} \wedge \tau_{b}$ 的数学期望, 并证明 $\mathbf{E}(\tau_{a}) = \mathbf{E}(\tau_{b}) = \infty$.

提示: 易证  $(S_{n}^{2}-n:n\geqslant0)$  是鞅. 因  $\sup_{k\geqslant0}S_{\tau\wedge k}^{2}\leqslant a^{2}\vee b^{2}$ , 根据有界停止定理和上题的结论,

$$
\mathbf {E} (\tau) = \mathbf {E} (S _ {\tau} ^ {2}) = \frac {a ^ {2} b - a b ^ {2}}{b - a} = - a b.
$$

## 2.4 不等式和收敛定理

鞅、上鞅和下鞅的基本理论是美国数学家杜布建立的.关于它们的很多不等式在随机过程理论中起着重要的作用.本节就离散时间情况讨论这些不等式，并在此基础上证明下鞅的若干收敛定理.这里我们假定所讨论的过程和流定义在概率空间 $(\Omega,\mathscr{F},\mathbf{P})$ 上.

## 2.4.1 基本不等式

定理 2.4.1 设  $(X_{n}: n \geqslant 0)$  是下鞅. 则对任何  $\lambda > 0$  及整数  $n \geqslant 0$  有

$$
\lambda \mathbf {P} \Big (\max _ {0 \leqslant k \leqslant n} X _ {k} \geqslant \lambda \Big) \leqslant \mathbf {E} \Big (X _ {n}; \max _ {0 \leqslant k \leqslant n} X _ {k} \geqslant \lambda \Big) \leqslant \mathbf {E} (X _ {n} ^ {+}) \tag {2.4.1}
$$

和

$$
\lambda \mathbf {P} \Big (\max _ {0 \leqslant k \leqslant n} | X _ {k} | \geqslant \lambda \Big) \leqslant 2 \mathbf {E} (X _ {n} ^ {+}) - \mathbf {E} (X _ {0}). \tag {2.4.2}
$$

---

2.4 不等式和收敛定理

55

证明 令 $\tau = \inf \{k\geqslant 0:X_k\geqslant \lambda \}$ ，则 $\tau$ 是停时，所以

$$
\begin{array}{l} \mathbf {E} (X _ {n}) \geqslant \mathbf {E} (X _ {\tau \wedge n}) = \mathbf {E} \Big (X _ {\tau}; \max _ {0 \leqslant k \leqslant n} X _ {k} \geqslant \lambda \Big) + \mathbf {E} \Big (X _ {n}; \max _ {0 \leqslant k \leqslant n} X _ {k} <   \lambda \Big) \\ \geqslant \lambda \mathbf {E} \Big (\max _ {0 \leqslant k \leqslant n} X _ {k} \geqslant \lambda \Big) + \mathbf {E} \Big (X _ {n}; \max _ {0 \leqslant k \leqslant n} X _ {k} <   \lambda \Big). \\ \end{array}
$$

因此

$$
\lambda \mathbf {P} \Big (\max _ {0 \leqslant k \leqslant n} X _ {k} \geqslant \lambda \Big) \leqslant \mathbf {E} (X _ {n}) - \mathbf {E} \Big (X _ {n}; \max _ {0 \leqslant k \leqslant n} X _ {k} <   \lambda \Big),
$$

故得 (2.4.1) 式. 再令 $\sigma = \inf \{k \geqslant 0 : X_k \leqslant -\lambda\}$. 与上面类似地, 有

$$
\begin{array}{l} \mathbf {E} (X _ {0}) \leqslant \mathbf {E} (X _ {\sigma \wedge n}) = \mathbf {E} \Big (X _ {\sigma}; \min _ {0 \leqslant k \leqslant n} X _ {k} \leqslant - \lambda \Big) + \mathbf {E} \Big (X _ {n}; \min _ {0 \leqslant k \leqslant n} X _ {k} > - \lambda \Big) \\ \leqslant - \lambda \mathbf {P} \Big (\min _ {0 \leqslant k \leqslant n} X _ {k} \leqslant - \lambda \Big) + \mathbf {E} \Big (X _ {n}; \min _ {0 \leqslant k \leqslant n} X _ {k} > - \lambda \Big). \\ \end{array}
$$

因此

$$
\begin{array}{l} \lambda \mathbf {P} \Big (\min _ {0 \leqslant k \leqslant n} X _ {k} \leqslant - \lambda \Big) \leqslant \mathbf {E} \Big (X _ {n}; \min _ {0 \leqslant k \leqslant n} X _ {k} > - \lambda \Big) - \mathbf {E} (X _ {0}) \\ \leqslant \mathbf {E} (X _ {n} ^ {+}) - \mathbf {E} (X _ {0}). \\ \end{array}
$$

结合上式与 (2.4.1) 式即得 (2.4.2) 式. □

推论 2.4.2 设  $(X_{n}: n \geqslant 0)$  是非负上鞅, 则对任何  $\lambda > 0$  及整数  $n \geqslant 0$  有

$$
\lambda \mathbf {P} \Big (\max _ {0 \leqslant k \leqslant n} X _ {k} \geqslant \lambda \Big) = \lambda \mathbf {P} \Big (\max _ {0 \leqslant k \leqslant n} | - X _ {k} | \geqslant \lambda \Big) \leqslant \mathbf {E} (X _ {0}).
$$

定理 2.4.3 设  $(X_{n}: n \geqslant 0)$  是鞅或非负下鞅, 则对任何  $\lambda > 0, p \geqslant 1$  及整数  $n \geqslant 0$  有

$$
\lambda^ {p} \mathbf {P} \Big (\max _ {0 \leqslant k \leqslant n} | X _ {k} | \geqslant \lambda \Big) \leqslant \mathbf {E} (| X _ {n} | ^ {p}); \tag {2.4.3}
$$

而对任何 $p > 1$ 及整数 $n \geqslant 0$ 有

$$
\mathbf {E} \Big (\max _ {0 \leqslant k \leqslant n} | X _ {k} | ^ {p} \Big) \leqslant \Big (\frac {p}{p - 1} \Big) ^ {p} \mathbf {E} (| X _ {n} | ^ {p}). \tag {2.4.4}
$$

证明 不妨设 $\mathbf{E}[|X_n|^p] < \infty$. 此时, 由延森不等式易知 $(|X_k|^p : 0 \leqslant k \leqslant n)$ 为下鞅. 再由 (2.4.1) 式得 (2.4.3) 式. 令 $M_n = \max_{0 \leqslant k \leqslant n} |X_k|$. 对下鞅 $(|X_n| : n \geqslant 0)$ 应用 (2.4.1) 式有

$$
t \mathbf {E} (1 _ {\{M _ {n} \geqslant t \}}) = t \mathbf {P} (M _ {n} \geqslant t) \leqslant \mathbf {E} (| X _ {n} |; M _ {n} \geqslant t) = \mathbf {E} (| X _ {n} | 1 _ {\{M _ {n} \geqslant t \}}).
$$

---

56

第二章 鞅论基础

令  $q = p/(p - 1)$ . 由上式及赫尔德 (Hölder) 不等式得到

$$
\begin{array}{l} \mathbf {E} (M _ {n} ^ {p}) = \mathbf {E} \bigg (\int_ {0} ^ {\infty} p t ^ {p - 1} 1 _ {\{t \leqslant M _ {n} \}} \mathrm{d} t \bigg) = p \int_ {0} ^ {\infty} t ^ {p - 1} \mathbf {E} (1 _ {\{t \leqslant M _ {n} \}}) \mathrm{d} t \\ \leqslant p \int_ {0} ^ {\infty} t ^ {p - 2} \mathbf {E} (| X _ {n} | 1 _ {\{t \leqslant M _ {n} \}}) \mathrm{d} t = p \mathbf {E} \bigg (| X _ {n} | \int_ {0} ^ {M _ {n}} t ^ {p - 2} \mathrm{d} t \bigg) \\ = \frac {p}{p - 1} \mathbf {E} (| X _ {n} | M _ {n} ^ {p - 1}) \leqslant q [ \mathbf {E} (| X _ {n} | ^ {p}) ] ^ {\frac {1}{p}} [ \mathbf {E} (M _ {n} ^ {(p - 1) q}) ] ^ {\frac {1}{q}} \\ = q [ \mathbf {E} (| X _ {n} | ^ {p}) ] ^ {\frac {1}{p}} [ \mathbf {E} (M _ {n} ^ {p}) ] ^ {\frac {1}{q}}, \\ \end{array}
$$

两边同除以  $\left[\mathbf{E}(M_{n}^{p})\right]^{\frac{1}{q}}$  即得 (2.4.4) 式. □

## 2.4.2 上穿不等式

下面证明另外一个非常重要的不等式. 考虑实值随机过程 $(X_{n}: n \geqslant 0)$. 对于给定的常数 $-\infty < a < b < \infty$, 我们定义 $\tau_{0} = 0$ 和

$$
\begin{array}{l} \tau_ {1} = \inf \{n \geqslant 0: X _ {n} \leqslant a \}, \\ \tau_ {2} = \inf \{n \geqslant \tau_ {1}: X _ {n} \geqslant b \}, \\ \tau_ {2 k + 1} = \inf \{n \geqslant \tau_ {2 k}: X _ {n} \leqslant a \}, \\ \tau_ {2 k + 2} = \inf \{n \geqslant \tau_ {2 k + 1}: X _ {n} \geqslant b \}, \\ \end{array}
$$

...

...

则 $\{\tau_n : n \geqslant 1\}$ 是一个严格单调上升的停时序列. 对 $N \geqslant 1$ 令

$$
U _ {N} ^ {X} [ a, b ] = \max \{k: \tau_ {2 k} \leqslant N \}.
$$

随机变量  $U_{N}^{X}[a,b]$  记录了过程 X 在时刻 0 到 N 之间上穿区间  $[a,b]$  的次数. 下面是著名的杜布上穿不等式.

定理 2.4.4 设  $(X_{n}: n \geqslant 0)$  是一个下鞅, 则对任何常数 a < b 和非负整数 N, 有

$$
\mathbf {E} \big \{U _ {N} ^ {X} [ a, b ] \big \} \leqslant \frac {1}{b - a} \mathbf {E} \big [ (X _ {N} - a) ^ {+} - (X _ {0} - a) ^ {+} \big ] \leqslant \frac {1}{b - a} \mathbf {E} \big | X _ {N} - a \big |.
$$

证明 令 $Y_{n} = (X_{n} - a)^{+}$, 显然 $(Y_{n})$ 也是一个下鞅. 自然地有 $U_{N}^{X}[a, b] = U_{N}^{Y}[0, b - a]$. 取 $k$ 使 $2k - 1 \geqslant N$, 那么 $\tau_{2k} \geqslant 2k - 1 \geqslant N$, 因此

$$
Y _ {N} - Y _ {0} = \sum_ {n = 1} ^ {2 k} (Y _ {\tau_ {n} \wedge N} - Y _ {\tau_ {n - 1} \wedge N})
$$

---

2.4 不等式和收敛定理

57

$$
\begin{array}{l} = \sum_ {n = 1} ^ {k} (Y _ {\tau_ {2 n} \wedge N} - Y _ {\tau_ {2 n - 1} \wedge N}) + \sum_ {n = 0} ^ {k - 1} (Y _ {\tau_ {2 n + 1} \wedge N} - Y _ {\tau_ {2 n} \wedge N}) \\ \geqslant (b - a) U _ {N} ^ {Y} [ 0, b - a ] + \sum_ {n = 0} ^ {k - 1} (Y _ {\tau_ {2 n + 1} \wedge N} - Y _ {\tau_ {2 n} \wedge N}). \\ \end{array}
$$

因为  $\tau_{2n+1} \geqslant \tau_{2n}$ ，由定理 2.3.3 得

$$
\begin{array}{l} \mathbf {E} (Y _ {N} - Y _ {0}) \geqslant (b - a) \mathbf {E} \big \{U _ {N} ^ {X} [ a, b ] \big \} + \sum_ {n = 0} ^ {k - 1} \big [ \mathbf {P} (Y _ {\tau_ {2 n + 1} \wedge N}) - \mathbf {P} (Y _ {\tau_ {2 n} \wedge N}) \big ] \\ \geqslant (b - a) \mathbf {E} \big \{U _ {N} ^ {X} [ a, b ] \big \}. \\ \end{array}
$$

此即为欲证不等式. □

## 2.4.3 向前收敛定理

利用上穿不等式, 可以证明下面的下鞅收敛定理.

定理 2.4.5 设  $(X_{n}: n \geqslant 0)$  是下鞅且  $K := \sup_{n \geqslant 0} P |X_{n}| < \infty$ ，则当  $n \to \infty$  时有  $X_{n} \stackrel{a.s.}{\rightarrow} X$ ，其中 X 是一个可积随机变量。另外，若  $(X_{n})$  是一致可积下鞅，则  $X_{n} \stackrel{L^{1}}{\rightarrow} X$ ；若  $(X_{n})$  是一致可积鞅，则还有  $X_{n} = \mathbf{E}(X|\mathscr{F}_{n})$ 。

证明 令 $X_{*} = \liminf_{n\to \infty}X_{n}$ 和 $X^{*} = \limsup_{n\to \infty}X_{n}$. $\mathbb{Q}$ 表示有理数集. 显然

$$
\{X _ {*} <   X ^ {*} \} = \bigcup_ {a <   b \in \mathbb {Q}} \{X _ {*} <   a <   b <   X ^ {*} \}.
$$

由上穿不等式

$$
\mathbf {E} \big \{U _ {N} ^ {X} [ a, b ] \big \} \leqslant \frac {1}{b - a} \mathbf {E} | X _ {N} - a | \leqslant \frac {K + | a |}{b - a}.
$$

由单调收敛定理 $\mathbf{E}\big\{\lim_{N\to \infty}U_N^X [a,b]\big\} < \infty$ .因此几乎必然 $\lim_{N\to \infty}U_N^X [a,b] < \infty$ .但是

$$
\{X _ {*} <   a <   b <   X ^ {*} \} \subseteq \Big \{\lim _ {N \to \infty} U _ {N} ^ {X} [ a, b ] = \infty \Big \},
$$

故 $\mathbf{P}\{X_{*} < a < b < X^{*}\} = 0$ ，推出几乎必然 $X^{*} = X_{*}$ .所以几乎必然存在有限或无限的极限 $X\coloneqq = \lim_{n\to \infty}X_n$ .由法图定理有

$$
\mathbf {E} | X | = \mathbf {E} \Big (\operatorname * {l i m i n f} _ {n \to \infty} | X _ {n} | \Big) \leqslant \operatorname * {l i m i n f} _ {n \to \infty} \mathbf {E} | X _ {n} | \leqslant K <   \infty ,
$$

故 $X$ 可积, 因而几乎必然有限. 如果 $\{X_{n}\}$ 是一致可积下鞅, 则由控制收敛定理有 $X_{n} \xrightarrow{L^{1}} X$. 若 $\{X_{n}\}$ 是一致可积鞅, 则有 $X_{n} \xrightarrow{L^{1}} X$ 且对 $k \geqslant n$ 和 $A \in \mathscr{F}_{n}$ 有

$$
\mathbf {E} (X _ {n} 1 _ {A}) = \mathbf {E} [ \mathbf {E} (X _ {k} | \mathcal {F} _ {n}) 1 _ {A} ] = \mathbf {E} (X _ {k} 1 _ {A}),
$$

---

58

第二章 鞅论基础

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

---

2.4 不等式和收敛定理

59

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

---

60

第二章 鞅论基础

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

---

2.5 连续时间下鞅

61

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

---

62

第二章 鞅论基础

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

---

2.5 连续时间下鞅

63

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

---

64

第二章 鞅论基础

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

---

2.5 连续时间下鞅

65

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

---

66

第二章 鞅论基础

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

---

2.5 连续时间下鞅

67

## 练习题

1. 设 $\{(M_t, \mathcal{F}_t): t \geqslant 0\}$ 和 $\{(N_t, \mathcal{G}_t): t \geqslant 0\}$ 是连续时间鞅, 且 $\mathcal{F}_{\infty} := \sigma \left( \bigcup_{t \geqslant 0} \mathcal{F}_t \right)$ 和 $\mathcal{G}_{\infty} := \sigma \left( \bigcup_{t \geqslant 0} \mathcal{G}_t \right)$ 独立. 令 $\mathcal{H}_t = \sigma \left( \mathcal{F}_t \bigcup \mathcal{G}_t \right)$. 证明 $\{(M_t N_t, \mathcal{H}_t): t \geqslant 0\}$ 是鞅.
2. 设 $(M_t : t \geqslant 0)$ 为非负连续下鞅. 再设 $\{T_n\}$ 为有界单增停时列. 令 $T = \lim_{n \to \infty} T_n$. 证明 $\mathbf{E}(M_T) = \lim_{n \to \infty} \mathbf{E}(M_{T_n})$.
3. 设 $(M_t : t \geqslant 0)$ 是连续鞅且 $M_0 = 0$. 再设 $a < 0 < b$, 并令 $\tau = \inf \{t \geqslant 0 : M_t \notin [a, b]\}$. 已知 $\mathbf{P}(\tau < \infty) = 1$, 求概率 $\mathbf{P}(M_\tau = a)$ 和 $\mathbf{P}(M_\tau = b)$ 的值.
4. 通过对时间集进行可数稠子集逼近, 给出定理 2.5.10 的证明.
5. 设 $(M_t : t \geqslant 0)$ 是右连续平方可积鞅, 且对于有界停时 $T$ 有 $\mathbf{E}(M_T^2) = 0$. 证明 $\mathbf{P}(M_{t \wedge T} = 0 : t \geqslant 0) = 1$.
6. 设 $(M_t : t \geqslant 0)$ 是连续局部鞅且 $M_0 = 0$. 证明: 存在局部化序列 $\{T_k\}$ 使得每个 $(M_{t \wedge T_k})$ 是有界连续鞅.
