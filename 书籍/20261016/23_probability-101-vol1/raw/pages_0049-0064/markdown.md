## 第二章

## 随机变量及其分布

在随机现象中, 有很多问题与带有随机性的数量有关. 例如, 在产品检验中我们关心抽样中残次品的数量, 在电话服务中我们关心某个时间段内的呼叫和服务次数等. 有些与随机现象有关的问题初看起来与数量无关, 但与数值联系起来之后, 可以简化表示或分析. 为研究这些问题, 需要引进随机变量的概念. 在数学上, 随机变量就是定义在概率空间上的可测函数, 而随机变量的分布或分布函数给出其取值概率的定量描述.

本章讨论随机变量及分布函数的基本构造与性质, 并分别介绍离散型和绝对连续型概率分布的若干典型的例子.

## 2.1 可测函数与随机变量

在数学上, 我们将随机变量定义为概率空间上的具有可测性质的函数, 可测性保证了它在一些常见的集合中取值的概率有意义.

## 2.1.1 可测映射

设 $\xi$ 为由集合 $\Omega$ 到集合 $E$ 的映射. 特别地, 当 $E = \mathbb{R}$ 或 $= \mathbb{R}^d$ 时 $\xi$ 就是 $\Omega$ 上的函数. 集合 $B \subseteq E$ 在 $\xi$ 下的原像定义为

$$
\xi^ {- 1} (B) = \{\omega \in \Omega : \xi (\omega) \in B \}.
$$

我们有时也会把上面的集合写为 $\{\xi \in B\}$ 或 $(\xi \in B)$. 给定 $E$ 的子集类 $\mathcal{C}$, 记

$$
\xi^ {- 1} (\mathcal {C}) = \{\xi^ {- 1} (B): B \in \mathcal {C} \}.
$$

集合 $A \subseteq \Omega$ 的示性函数 $1_A$ 定义为

$$
1 _ {A} (\omega) = \left\{ \begin{array}{l l} 1, & \omega \in A, \\ 0, & \omega \in A ^ {c}. \end{array} \right.
$$

例2.1.1 对于任何 $B \subseteq \mathbb{R}$, 显然有

$$
\begin{array}{l} B \cap \{0, 1 \} = \varnothing \Rightarrow 1 _ {A} ^ {- 1} (B) = \varnothing ; \\ B \cap \{0, 1 \} = \{1 \} \Rightarrow 1 _ {A} ^ {- 1} (B) = A; \\ B \cap \{0, 1 \} = \{0 \} \Rightarrow 1 _ {A} ^ {- 1} (B) = A ^ {c}; \\ B \cap \{0, 1 \} = \{0, 1 \} \Rightarrow 1 _ {A} ^ {- 1} (B) = \Omega . \\ \end{array}
$$

下面的引理罗列了关于映射的原像的几个常用的结果, 请读者自行给出其证明.

引理2.1.1 对于映射 $\xi : \Omega \to E$，有如下性质成立:

(1) $\xi^{-1}(E) = \Omega, \xi^{-1}(B^c) = \xi^{-1}(B)^c;$
(2) $\xi^{-1}\left(\bigcup_{i}B_{i}\right) = \bigcup_{i}\xi^{-1}(B_{i}),\xi^{-1}\left(\bigcap_{i}B_{i}\right) = \bigcap_{i}\xi^{-1}(B_{i});$
(3) 对 $B \subseteq C \subseteq E$ 有 $\xi^{-1}(B) \subseteq \xi^{-1}(C)$;
(4) 若 $\mathcal{E}$ 是 $E$ 上的 $\sigma$ 代数, 则 $\xi^{-1}(\mathcal{E})$ 是 $\Omega$ 上的 $\sigma$ 代数.

设 $\mathcal{E}$ 是 $E$ 上的 $\sigma$ 代数. 考虑可测空间 $(E, \mathcal{E})$. 再设 $\{\xi_i : i \in I\}$ 是由 $\Omega$ 到 $E$ 的一族映射, 其中 $I$ 为指标集. 我们称 $\Omega$ 上的 $\sigma$ 代数

$$
\sigma \left(\left\{\xi_ {i}: i \in I \right\}\right) := \sigma \left(\left\{\xi_ {i} ^ {- 1} (B): B \in \mathcal {E}, i \in I \right\}\right) \tag {2.1.1}
$$

为由 $\{\xi_i : i \in I\}$ 生成的 $\sigma$ 代数. 特别地, 由引理2.1.1(4)不难看出, 由单个映射 $\xi$ 生成的 $\sigma$ 代数为

$$
\sigma (\xi) = \xi^ {- 1} (\mathscr {E}) = \{\xi^ {- 1} (B): B \in \mathscr {E} \}. \tag {2.1.2}
$$

命题2.1.2 对于 $E$ 的任何子集类 $\mathcal{C}$ 有 $\sigma (\xi^{-1}(\mathcal{C})) = \xi^{-1}(\sigma (\mathcal{C}))$.

证明 由引理2.1.1(4)知 $\xi^{-1}(\sigma(\mathcal{C}))$ 是 $\sigma$ 代数.因 $\xi^{-1}(\mathcal{C})\subseteq \xi^{-1}(\sigma (\mathcal{C}))$ ，有$\sigma (\xi^{-1}(\mathcal{C}))\subseteq \xi^{-1}(\sigma (\mathcal{C}))$ .另一方面，令

$$
\mathscr {G} = \{B \subseteq E: \xi^ {- 1} (B) \in \sigma (\xi^ {- 1} (\mathscr {C})) \}.
$$

显然

$$
\xi^ {- 1} (\mathcal {G}) = \{\xi^ {- 1} (B): B \in \mathcal {G} \} \subseteq \sigma (\xi^ {- 1} (\mathcal {C})). \tag {2.1.3}
$$

利用引理2.1.1易证 $\mathcal{G}$ 为 $E$ 上的 $\sigma$ 代数.若 $B\in \mathcal{C}$ ，则

$$
\xi^ {- 1} (B) \in \xi^ {- 1} (\mathscr {C}) \subseteq \sigma (\xi^ {- 1} (\mathscr {C})),
$$

故 $B \in \mathcal{G}$. 这说明 $\mathcal{C} \subseteq \mathcal{G}$, 故 $\sigma(\mathcal{C}) \subseteq \mathcal{G}$. 于是

$$
\xi^ {- 1} (\sigma (\mathscr {C})) \subseteq \xi^ {- 1} (\mathscr {G}) \subseteq \sigma (\xi^ {- 1} (\mathscr {C})).
$$

其中最后的包含关系是由于 $(2.1.3)$ 式.

定义 2.1.1 设  $(\Omega, \mathcal{F})$  和  $(E, \mathcal{E})$  均为可测空间. 我们称  $\xi: \Omega \rightarrow E$  为可测映射, 是指有

$$
\sigma (\xi) = \xi^ {- 1} (\mathcal {E}) \subseteq \mathcal {F},
$$

即对任何 $B \in \mathcal{E}$ 都有 $\xi^{-1}(B) = \{\xi \in B\} \in \mathcal{F}$.

下面命题的结论显然成立.

命题 2.1.3 (1) 一族映射  $\{\xi_{i}: i \in I\}$  中的每个元素都关于  $\sigma(\{\xi_{i}: i \in I\})$  可测；

(2) 一族映射 $\{\xi_i : i \in I\}$ 中的每个元素都关于 $\mathcal{F}$ 可测当且仅当 $\sigma(\{\xi_i : i \in I\}) \subseteq \mathcal{F}$.

例 2.1.2 设  $E=\{x_{1},x_{2},\cdots\}$  是可数集, 而 E 是 E 的一切子集构成的  $\sigma$  代数. 则映射  $\xi:\Omega\to E$  可测当且仅当对每个  $k=1,2,\cdots$  有  $A_{k}:=\{\xi=x_{k}\}\in\mathcal{F}$ .

由 $(\Omega, \mathcal{F})$ 到 $(\mathbb{R}, \mathcal{B})$ 或 $(\mathbb{R}^d, \mathcal{B}^d)$ 的可测映射称为可测函数；而 $(\mathbb{R}^d, \mathcal{B}^d)$ 上的可测函数也称为博雷尔函数.

## 2.1.2 可测函数的性质

定理2.1.4 定义在可测空间 $(\Omega, \mathcal{F})$ 上的实值函数 $\xi$ 可测的充要条件是，对于任意的 $x \in \mathbb{R}$ 有 $\xi^{-1}(-\infty, x] \in \mathcal{F}$.

证明 必要性. 若 $\xi$ 可测, 对 $x \in \mathbb{R}$, 因 $(- \infty, x] \in \mathcal{B}$, 有 $\xi^{-1}(-\infty, x] \in \mathcal{F}$.

充分性. 设对任何 $x \in \mathbb{R}$ 有 $\xi^{-1}(-\infty, x] \in \mathcal{F}$. 由引理2.1.1易证 $\mathcal{E} = \{B \in \mathcal{B} : \xi^{-1}(B) \in \mathcal{F}\}$ 为 $\sigma$ 代数. 依假设有 $\mathcal{E} \supseteq \mathcal{P} := \{(-\infty, x] : x \in \mathbb{R}\}$, 故 $\mathcal{E} \supseteq \sigma(\mathcal{P}) = \mathcal{B}$, 即对任何 $B \in \mathcal{B}$ 有 $\xi^{-1}(B) \in \mathcal{F}$. 因此 $\xi$ 可测.

推论2.1.5 定义在可测空间 $(\Omega, \mathcal{F})$ 上的实值函数 $\xi$ 可测的充要条件是下列性质之一成立:

(1) 对于任意的  $x \in R$  有  $\xi^{-1}(-\infty, x) \in \mathcal{F}$ ;
(2) 对于任意的 $x \in \mathbb{R}$ 有 $\xi^{-1}(x, \infty) \in \mathcal{F}$;
(3) 对于任意的 $x \in \mathbb{R}$ 有 $\xi^{-1}[x, \infty) \in \mathcal{F}$.

推论 2.1.6 定义在 R 上的单调函数 f 是博雷尔可测的.

证明 不妨设 $f$ 不降. 则对 $x \in \mathbb{R}$, 原像 $f^{-1}(-\infty, x]$ 是形如 $(- \infty, a]$ 或 $(- \infty, a)$ 的区间. 两种情况下都有 $f^{-1}(-\infty, x] \in \mathcal{B}$. 根据定理2.1.4函数 $f$ 关于博雷尔 $\sigma$ 代数可测.

定理2.1.7 定义在 $\mathbb{R}^d$ 上的连续函数 $f$ 是博雷尔可测的.

证明 因为 $f$ 在 $\mathbb{R}^d$ 上连续, 对任何 $G \in \mathcal{O}$ 有 $f^{-1}(G) \in \mathcal{O}^d$, 故 $f^{-1}(\mathcal{O}) \subseteq \mathcal{O}^d$. 所以

$$
f ^ {- 1} (\mathcal {B}) = f ^ {- 1} (\sigma (\mathcal {O})) = \sigma (f ^ {- 1} (\mathcal {O})) \subseteq \sigma (\mathcal {O} ^ {d}) = \mathcal {B} ^ {d}.
$$

这说明 f 关于  $B^{d}$  可测.

定理2.1.8 设 $\xi$ 为 $\Omega$ 上的函数, 而 $f$ 为 $\mathbb{R}$ 上的博雷尔可测函数. 则 $\eta := f(\xi)$ 关于 $\Omega$ 上的 $\sigma$ 代数 $\sigma(\xi)$ 可测. 特别地, 若 $\xi$ 为 $(\Omega, \mathcal{F})$ 上的可测函数, 则 $\eta$ 为 $(\Omega, \mathcal{F})$ 上的可测函数.

证明 任取 $B \in \mathcal{B}$. 因 $f$ 为 $(\mathbb{R}, \mathcal{B})$ 上的可测函数, 有 $f^{-1}(B) \in \mathcal{B}$, 因而

$$
\eta^ {- 1} (B) = \xi^ {- 1} (f ^ {- 1} (B)) \in \sigma (\xi).
$$

这就证明了第1个结论. 第2个结论显然成立.

定理2.1.9 若 $\xi$ 和 $\eta$ 为 $(\Omega, \mathcal{F})$ 上的可测函数, 则 $\xi + \eta, \xi - \eta$ 和 $\xi \eta$ 均为 $(\Omega, \mathcal{F})$ 上的可测函数. 而且, 若还有 $\eta \neq 0$, 则 $\xi / \eta$ 也为 $(\Omega, \mathcal{F})$ 上的可测函数.

证明 对于 $x \in \mathbb{R}$ 令 $Q_x = \{(r, s): r$ 和 $s$ 均为有理数且满足 $r + s < x\}$. 则 $Q_x$ 为可数集且

$$
\{\xi + \eta <   x \} = \bigcup_ {(r, s) \in Q _ {x}} \{\xi <   r \} \cap \{\eta <   s \}. \tag {2.1.4}
$$

事实上, 若 $\omega \in \Omega$ 属于 (2.1.4) 式右边的集合, 它显然属于该式左边的集合. 反之, 设 $\omega \in \Omega$ 属于 (2.1.4) 式左边的集合. 则 $\delta := x - \xi(\omega) - \eta(\omega) > 0$. 取有理数 $r \in (\xi(\omega), \xi(\omega) + \delta/2)$ 和 $s \in (\eta(\omega), \eta(\omega) + \delta/2)$. 显然 $r + s < \xi(\omega) + \eta(\omega) + \delta = x$ 且有 $\xi(\omega) < r$ 和 $\eta(\omega) < s$, 故 $\omega$ 属于 (2.1.4) 式右边的集合. 由推论 2.1.5 和 (2.1.4) 式知 $\xi + \eta$ 为 $(\Omega, \mathcal{F})$ 上的可测函数. 其他结论的证明类似. □

定理2.1.10 若 $\xi$ 和 $\eta$ 为 $(\Omega, \mathcal{F})$ 上的可测函数，则下面的集合均可测:

$$
\{\xi <   \eta \}, \{\eta <   \xi \}, \{\xi \neq \eta \}, \{\xi = \eta \}.
$$

证明 注意有理数集 $\mathbb{Q}$ 可数且在实轴上稠密. 易知

$$
\{\xi <   \eta \} = \bigcup_ {r \in \mathbb {Q}} \{\xi <   r <   \eta \} = \bigcup_ {r \in \mathbb {Q}} \big (\{\xi <   r \} \cap \{r <   \eta \} \big),
$$

其中 $\{\xi < r\}, \{r < \eta\} \in \mathcal{F}$, 故知 $\{\xi < \eta\} \in \mathcal{F}$. 类似地有 $\{\eta < \xi\} \in \mathcal{F}$, 进而有 $\{\xi \neq \eta\} = \{\xi < \eta\} \cup \{\eta < \xi\} \in \mathcal{F}$ 和 $\{\xi = \eta\} = \{\xi \neq \eta\}^c \in \mathcal{F}$.

定理2.1.11 设 $\{\xi_n\}$ 为 $(\Omega, \mathcal{F})$ 上的可测函数列. 则下面函数 (若有限) 可测:

$$
\sup _ {n} \xi_ {n}, \quad \inf _ {n} \xi_ {n}, \quad \lim _ {n} \sup _ {n} \xi_ {n}, \quad \lim _ {n} \inf _ {n} \xi_ {n}.
$$

证明 对任意的 $x \in \mathbb{R}$, 我们有

$$
\{\sup _ {n} \xi_ {n} \leqslant x \} = \bigcap_ {n} \{\xi_ {n} \leqslant x \}
$$

和

$$
\{\inf _ {n} \xi_ {n} <   x \} = \bigcup_ {n} \{\xi_ {n} <   x \}.
$$

由推论2.1.5知 $\sup_{n}\xi_n$ 和 $\inf_{n}\xi_n$ 可测，进而 $\lim_{n}\sup_{n}\xi_n$ 和 $\lim_{n}\inf_{n}\xi_n$ 可测.

设 $(\Omega, \mathcal{F}, \mu)$ 为测度空间. 若可测函数 $\xi$ 和 $\eta$ 满足 $\mu (\xi \neq \eta) = 0$, 则称它们相对于 $\mu$ 几乎处处相等, 记作 $\xi = \eta$ (a.e.) 或 $\xi \stackrel{\mathrm{a.e.}}{=} \eta$. 更一般地, 若存在 $N \in \mathcal{F}$ 使得 $\mu(N) = 0$ 且某个性质对于所有 $\omega \in N^c$ 成立, 我们称该性质相对于测度 $\mu$ 几乎处处 (a.e.) 成立.

例 2.1.3 设  $\Omega$  上的实函数  $\xi$  的取值范围是可数集  $E = \{x_{1}, x_{2}, \cdots\}$ . 令  $A = \{A_{k} : k = 1, 2, \cdots\}$ , 其中  $A_{k} = \{\xi = x_{k}\}$ . 则  $\sigma(\xi) = \sigma(\mathcal{A})$  是由 A 中的集合的所有可能的并构成的集类 (规定零个集合的并为空集). 注意  $\xi$  关于  $\sigma(\xi)$  可测.

例 2.1.4 在上例的情况下, 若 f 为 R 上的博雷尔可测函数, 根据定理 2.1.8 知  $X := f(\xi)$  关于  $\sigma(\xi)$  可测. 反之, 若  $\Omega$  上的函数 X 关于  $\sigma(\xi)$  可测, 则它在每个集合  $A_{k}$  上必为常数, 不妨设  $X = \sum_{k=1}^{\infty} a_{k} 1_{A_{k}}$ . 显然  $f := \sum_{k=1}^{\infty} a_{k} 1_{\{x_{k}\}}$  为 R 上的博雷尔可测函数且  $X = f(\xi)$ . 所以  $\Omega$  上的函数 X 关于  $\sigma(\xi)$  可测当且仅当存在 R 上的博雷尔可测函数 f 使得  $X = f(\xi)$ .

## 2.1.3 测度的分布函数

称 $\mathbb{R}$ 上的函数 $G$ 为分布函数, 是指存在欧氏可测空间 $(\mathbb{R}, \mathcal{B})$ 上的局部有限测度 $\mu$ 满足

$$
G (b) - G (a) = \mu (a, b ], \quad a \leqslant b \in \mathbb {R}. \tag {2.1.5}
$$

此时也称 $G$ 是 $\mu$ 的分布函数. 特别地, 若 $\mu$ 是概率测度, 则称 $G$ 为概率分布函数.

根据测度的性质, 不难证明:

命题 2.1.12 欧氏可测空间  $(\mathbb{R}, \mathcal{B})$  上的局部有限测度  $\mu$  的分布函数 G 具有性质:

(1) G 右连续且单调不降;
(2) G 有界当且仅当  $\mu$  是有限测度, 且此时有  $\mu(\mathbb{R}) = G(\infty) - G(-\infty)$ ;
(3) 若 $G$ 是 $\mu$ 的分布函数, 则 $G + c$ 也是 $\mu$ 的分布函数, 其中 $c \in \mathbb{R}$ 为常数.

例2.1.5 利用分布函数 $G$ ，可以确定相应的局部有限测度 $\mu$ 在一些典型的集合上的取值.特别地，对于任何 $a\leqslant b\in \mathbb{R}$ 有

$$
\mu (a, b ] = G (b) - G (a); \quad \mu (a, b) = G (b -) - G (a);
$$

$$
\mu [ a, b ] = G (b) - G (a -); \quad \mu [ a, b) = G (b -) - G (a -).
$$

若 $\mu$ 是有限测度, 则有

$$
\mu (- \infty , b ] = G (b) - G (- \infty); \quad \mu (- \infty , b) = G (b -) - G (- \infty);
$$

$$
\mu (a, \infty) = G (\infty) - G (a); \quad \mu [ a, \infty) = G (\infty) - G (a -).
$$

设 $(\mathbb{R},\mathcal{B})$ 上的局部有限测度 $\mu$ 有分布函数 $G$. 称 $x\in \mathbb{R}$ 为 $\mu$ 或 $G$ 的跳跃点, 是指

$$
\Delta G (x) := G (x) - G (x -) = \mu (\{x \}) > 0.
$$

此时称  $\Delta G(x)$  为  $\mu$  或 G 在点 x 的跳幅. 显然, 跳跃点集  $E := \{x \in \mathbb{R} : \Delta G(x) > 0\}$  至多为可数集, 且 G 在  $E^{c} = R \setminus E$  上连续. 写该集合为  $E = \{x_{1}, x_{2}, \cdots\}$ , 并记  $q(x_{i}) = \Delta G(x_{i})$ . 称  $\mu$  或 G 是离散型的, 是指有

$$
G (b) - G (a) = \sum_ {x _ {i} \in (a, b ]} q (x _ {i}), \quad a \leqslant b \in \mathbb {R}. \tag {2.1.6}
$$

此时称 $q$ 为 $\mu$ 或 $G$ 的密度函数或密度.

称 $(\mathbb{R},\mathcal{B})$ 上的局部有限测度 $\mu$ 或其分布函数 $G$ 是绝对连续型的, 是指存在 $\mathbb{R}$ 上的非负黎曼可积函数 $q$ 使得

$$
G (b) - G (a) = \int_ {a} ^ {b} q (u) \mathrm{d} u, \quad a \leqslant b \in \mathbb {R}. \tag {2.1.7}
$$

此时称 $q$ 为 $\mu$ 或 $G$ 的密度函数或密度. 显然, 绝对连续型分布函数是 $\mathbb{R}$ 上的连续函数. 另外, 根据数学分析的结果, 若函数 $G$ 连续可微, 则 (2.1.7) 式对 $q = G'$ 成立.

下面的定理说明 $(\mathbb{R},\mathcal{B})$ 上的局部有限测度由其分布函数唯一决定. 定理的证明需要用到附录中介绍的邓肯类定理.

定理2.1.13 设 $\mu$ 和 $\nu$ 是欧氏可测空间 $(\mathbb{R},\mathcal{B})$ 上的局部有限测度. 若这两个测度以同一个函数 $G$ 为分布函数, 则它们相等, 即对一切 $B \in \mathcal{B}$ 有 $\mu(B) = \nu(B)$.

证明 (1) 考虑 $G$ 为有界分布函数的情况. 令 $\mathcal{D} = \{A \in \mathcal{B} : \mu(A) = \nu(A)\}$. 显然 $\mu(\mathbb{R}) = G(\infty) - G(-\infty) = \nu(\mathbb{R})$, 故有 $\mathbb{R} \in \mathcal{D}$. 若 $A, B \in \mathcal{D}$ 且 $A \subseteq B$, 则有 $\mu(A) = \nu(A)$ 和 $\mu(B) = \nu(B)$, 进而

$$
\mu (B \setminus A) = \mu (B) - \mu (A) = \nu (B) - \nu (A) = \nu (B \setminus A),
$$

故 $B \setminus A \in \mathcal{D}$. 若 $\{A_n\} \subseteq \mathcal{D}$ 单调不降, 由测度的下连续性有

$$
\mu \Big (\bigcup_ {n = 1} ^ {\infty} A _ {n} \Big) = \lim _ {n \to \infty} \mu (A _ {n}) = \lim _ {n \to \infty} \nu (A _ {n}) = \nu \Big (\bigcup_ {n = 1} ^ {\infty} A _ {n} \Big),
$$

故 $\bigcup_{n=1}^{\infty} A_n \in \mathcal{D}$. 这就证明了 $\mathcal{D}$ 是邓肯类.

(2) 继续考虑 $G$ 为有界分布函数的情况. 令 $\mathcal{C}$ 是一切形如 $(a, b] \subseteq \mathbb{R}$ 的区间构成的集类. 显然 $\mathcal{C}$ 对于交运算封闭. 因为 $\mu(a, b] = G(b) - G(a) = \nu(a, b]$, 所以有 $\mathcal{C} \subseteq \mathcal{D}$. 根据邓肯类定理有 $\mathcal{D} \supseteq d(\mathcal{C}) = \sigma(\mathcal{C}) = \mathcal{B}$, 即对一切 $A \in \mathcal{B}$ 有 $\mu(A) = \nu(A)$.
(3) 考虑 $G$ 为一般分布函数的情况. 对于 $n \geqslant 1$ 和 $A \in \mathcal{B}$ 定义 $\mu_n(A) = \mu(A \cap (-n, n])$ 和 $\nu_n(A) = \nu(A \cap (-n, n])$. 则 $\mu_n$ 和 $\nu_n$ 都是有限测度, 且有共同的分布函数 $G_n(x) = G(x \vee (-n) \wedge n)$. 根据前两步证明的结论, 对任何 $n \geqslant 1$ 有 $\mu_n = \nu_n$, 进而易知 $\mu = \nu$.

对应于 $(\mathbb{R},\mathcal{B})$ 上的有限测度 $\mu$ ，有唯一的分布函数 $G$ 满足 $G(-\infty) = 0$ .该分布函数由

$$
G (x) = \mu (- \infty , x ], \quad x \in \mathbb {R} \tag {2.1.8}
$$

给出. 后面当提到有限测度的分布函数时, 总是指由 (2.1.8) 式定义的函数.

## 2.1.4 随机变量的概念

定义2.1.2 设 $(\Omega, \mathcal{F}, \mathbf{P})$ 为概率空间. 称由 $(\Omega, \mathcal{F})$ 到某个可测空间 $(E, \mathcal{E})$ 的可测映射 $\xi$ 为随机变量. 特别地, 当 $(E, \mathcal{E})$ 为欧氏可测空间 $(\mathbb{R}, \mathcal{B})$ 时, 称 $\xi$ 为实值随机变量.

给定取值于 $(E, \mathcal{E})$ 的随机变量 $\xi$, 对于集合 $B \in \mathcal{E}$ 我们自然希望可以讨论 $\{\xi \in B\}$ 发生的概率, 而概率测度 $\mathbf{P}$ 是 $\mathcal{F}$ 上的集函数. 所以定义2.1.2中要求 $\{\xi \in B\} \in \mathcal{F}$ 是合理的. 若某个性质在 $\Omega$ 上相对于 $\mathbf{P}$ 几乎处处成立, 就称该性质几乎必然成立.

定理2.1.14 设 $\xi$ 为定义在概率空间 $(\Omega, \mathcal{F}, \mathbf{P})$ 上取值于可测空间 $(E, \mathcal{E})$ 的随机变量. 令

$$
\mu (B) = \mathbf {P} (\xi^ {- 1} (B)) = \mathbf {P} (\xi \in B), \quad B \in \mathscr {E}. \tag {2.1.9}
$$

则  $\mu$  为  $(E, \mathcal{E})$  上的概率测度.

证明 显然, 对任何 $B \in \mathcal{E}$ 有 $\mu(B) \geqslant 0$, 且 $\mu(E) = 1$. 现设 $\{B_n\} \subseteq \mathcal{E}$ 是两两不交的集合列. 则当 $i \neq j$ 时有

$$
\xi^ {- 1} (B _ {i}) \cap \xi^ {- 1} (B _ {j}) = \xi^ {- 1} (B _ {i} \cap B _ {j}) = \varnothing ,
$$

也即 $\{\xi^{-1}(B_n)\}$ 两两不交. 由概率 $\mathbf{P}$ 的可数可加性和引理2.1.1得

$$
\begin{array}{l} \mu \left(\bigcup_ {n = 1} ^ {\infty} B _ {n}\right) = \mathbf {P} \left(\xi^ {- 1} \left(\bigcup_ {n = 1} ^ {\infty} B _ {n}\right)\right) \\ = \mathbf {P} \left(\bigcup_ {n = 1} ^ {\infty} \xi^ {- 1} (B _ {n})\right) \\ = \sum_ {n = 1} ^ {\infty} \mathbf {P} (\xi^ {- 1} (B _ {n})) = \sum_ {n = 1} ^ {\infty} \mu (B _ {n}). \\ \end{array}
$$

所以  $\mu$  为  $(E, \mathcal{E})$  上的概率测度.

定义 2.1.3 称由 (2.1.9) 式定义的  $(E, \mathcal{E})$  上的概率测度  $\mu$  为随机变量  $\xi$  的概率分布，简称分布。特别地，当  $(E, \mathcal{E})$  为欧氏可测空间  $(\mathbb{R}, \mathcal{B})$  时，也称  $\mu$  的分布函数 F 为  $\xi$  的分布函数。后面经常将二者分别写作  $\mu_{\xi}$  和  $F_{\xi}$ ，以标明其与  $\xi$  的关系。

如无特别申明, 后面所说的随机变量都指实值随机变量. 对于概率空间 $(\Omega, \mathcal{F}, \mathbf{P})$ 上的随机变量 $\xi$ 和 $\eta$, 如果有 $\mathbf{P}(\xi = \eta) = 1$, 就称 $\xi$ 和 $\eta$ 几乎必然相等, 记作 $\xi = \eta$ (a.s.) 或 $\xi \stackrel{\mathrm{a.s.}}{=} \eta$. 特别地, 若有 $a \in E$ 使得 $\xi \stackrel{\mathrm{a.s.}}{=} a$, 则称 $\xi$ 是退化的. 否则称 $\xi$ 是非退化的.

将随机变量定义为概率空间上的可测函数, 其优点是具有广泛的适用性. 但由于概率空间是抽象空间, 在很多时候不便于进行分析和计算. 分布和分布函数给出了随机变量的取值概率的定量描述. 它们将很多计算转移到欧氏空间 $\mathbb{R}$, 为相关的讨论提供了方便.

若随机变量 $\xi$ 和 $\eta$ 具有相同的概率分布, 则称它们同分布, 并记作 $\xi \stackrel{\mathrm{d}}{=} \eta$. 根据前面的讨论, 某个随机变量 $\xi$ 的概率分布函数 $F$ 为 $\mathbb{R}$ 上的右连续不降函数且满足

$$
F (- \infty) = 0, \quad F (\infty) = 1.
$$

例2.1.6 设随机变量 $\xi$ 有分布函数 $F_{\xi}$. 则对任何 $a \leqslant b \in \mathbb{R}$ 有

$$
\mathbf {P} (a <   \xi \leqslant b) = F _ {\xi} (b) - F _ {\xi} (a), \quad \mathbf {P} (a <   \xi <   b) = F _ {\xi} (b -) - F _ {\xi} (a),
$$

$$
\mathbf {P} (a \leqslant \xi \leqslant b) = F _ {\xi} (b) - F _ {\xi} (a -), \quad \mathbf {P} (a \leqslant \xi <   b) = F _ {\xi} (b -) - F _ {\xi} (a -).
$$

例 2.1.7 设  $(\Omega, \mathcal{F}, \mathbf{P})$  为例 1.2.11 中定义的关于成功事件  $A \subseteq \Omega$  的伯努利概率空间, 其中  $F = \{\varnothing, A, A^{c}, \Omega\}$ , 而  $\mathbf{P}(A) = p (0 \leqslant p \leqslant 1)$ . 令  $\xi(\omega) = 1_{A}(\omega)$ . 则  $\xi$  是  $(\Omega, \mathcal{F}, \mathbf{P})$  上的随机变量. 它取值 1 或 0, 代表一次伯努利随机试验中成功的次数. 显然

$$
\mathbf {P} (\xi = 1) = \mathbf {P} (A) = p, \quad \mathbf {P} (\xi = 0) = \mathbf {P} (A ^ {c}) = 1 - p.
$$

该随机变量有分布函数

$$
F _ {\xi} (x) = (1 - p) 1 _ {\{0 \leqslant x <   1 \}} + 1 _ {\{x \geqslant 1 \}}, \quad x \in \mathbb {R}.
$$

特别地, 当 $\xi$ 是取值为 $a \in \mathbb{R}$ 的退化随机变量, 其分布 $\mu_{\xi}$ 就是狄拉克测度 $\delta_{a}$. 此时我们有

$$
\mu_ {\xi} (B) = 1 _ {B} (a), \quad B \in \mathcal {B}
$$

和

$$
F _ {\xi} (x) = 1 _ {\{x \geqslant a \}}, \quad x \in \mathbb {R}.
$$

在这种情况下, 我们分别称 $\mu$ 和 $F$ 为退化概率分布和退化分布函数.

## 练习题

1. 设 $\xi$ 为定义在非空集 $\Omega$ 上的实值函数. 证明:

(1) $\xi^{-1}(\mathbb{R}) = \Omega, \xi^{-1}(B^c) = \xi^{-1}(B)^c;$
(2) $\xi^{-1}\left(\bigcup_{i}B_{i}\right) = \bigcup_{i}\xi^{-1}(B_{i}),\xi^{-1}\left(\bigcap_{i}B_{i}\right) = \bigcap_{i}\xi^{-1}(B_{i});$
(3) 对 $B \subseteq C \subseteq \mathbb{R}$ 有 $\xi^{-1}(B) \subseteq \xi^{-1}(C)$;
(4) 若 $\mathcal{E}$ 是 $\mathbb{R}$ 上的 $\sigma$ 代数, 则 $\xi^{-1}(\mathcal{E})$ 是 $\Omega$ 上的 $\sigma$ 代数.

2. 设 $\xi$ 为可测空间 $(\Omega, \mathcal{F})$ 上的实函数. 证明: 对于任何 $A \subseteq \Omega$ 示性函数 $1_A$ 关于 $\mathcal{F}$ 可测当且仅当 $A \in \mathcal{F}$.

3. 设 $\xi$ 和 $\eta$ 为 $(\Omega, \mathcal{F})$ 上的可测函数. 证明:

(1)  $\xi - \eta$  和  $\xi\eta$  均为  $(\Omega, \mathcal{F})$  上的可测函数;

(2) 若 $\eta \neq 0$, 则 $\xi / \eta$ 为 $(\Omega, \mathcal{F})$ 上的可测函数.

4. 给出有界区间  $(a, b) \subseteq \mathbb{R}$  上的勒贝格测度的分布函数 G.

5. 设随机变量 $\xi$ 满足 $\mathbf{P}(\xi \geqslant a) \geqslant 1 - \alpha$ 和 $\mathbf{P}(\xi \leqslant b) \geqslant 1 - \beta$, 其中 $a \leqslant b \in \mathbb{R}$, 而 $\alpha, \beta \in [0,1]$. 证明

$$
\mathbf {P} (a \leqslant \xi \leqslant b) \geqslant 1 - \alpha - \beta.
$$

## 2.2 离散型随机变量

称随机变量  $\xi$  是离散型的, 是指它具有离散型概率分布函数 F. 此时  $\xi$  的可能的取值范围是某个可数集  $E := \{x_{1}, x_{2}, \cdots\} \subseteq R$ . 令 p 为 F 的密度函数. 则有

$$
F (x) = \mathbf {P} (\xi \leqslant x) = \sum_ {x _ {i} \leqslant x} p (x _ {i}), \quad x \in \mathbb {R}, \tag {2.2.1}
$$

其中

$$
p (x _ {i}) = \mathbf {P} (\xi = x _ {i}), \quad i = 1, 2, \dots . \tag {2.2.2}
$$

注意

$$
\sum_ {i = 1} ^ {\infty} p (x _ {i}) = 1.
$$

此时也将 p 称为  $\xi$  的分布列、分布密度或密度. 利用概率测度的可数可加性得

$$
\mathbf {P} (\xi \in B) = \sum_ {x _ {i} \in B} p (x _ {i}), \quad B \in \mathcal {B}.
$$

给定可数集  $E := \{x_{1}, x_{2}, \cdots\} \subseteq R$  上的以 p 为密度函数的离散型概率测度  $\mu$ ，是否一定存在以  $\mu$  为分布的离散型随机变量呢？下面的命题回答了这个问题.

命题 2.2.1 在上述情况下, 令  $\Omega=\{1,2,\cdots\}$ , 并令 F 为  $\Omega$  的所有子集构成的  $\sigma$  代数. 对于  $A\in F$ , 令

$$
\mathbf {P} (A) = \sum_ {i \in A} p (x _ {i}). \tag {2.2.3}
$$

对任何 $i \in \Omega$ 令 $\xi(i) = x_i$. 则 $\xi$ 为概率空间 $(\Omega, \mathcal{F}, \mathbf{P})$ 上的离散型随机变量, 且有分布列 $\{p(x_1), p(x_2), \dots\}$.

证明 显然, 由 (2.2.3) 式定义的 $\mathbf{P}$ 是可测空间 $(\Omega, \mathcal{F})$ 上的概率测度. 因 $\mathcal{F}$ 包含 $\Omega$ 的所有子集, 所以 $\xi$ 可测. 由 (2.2.3) 式知 (2.2.2) 式成立. 所以 $\xi$ 为离散型随机变量, 且有分布列 $\{p(x_1), p(x_2), \cdots\}$.

例 2.2.1 令  $(\Omega_{1},\mathcal{F}_{1},\mathbf{P}_{1})$  为关于成功事件  $A \subseteq \Omega_{1}$  的伯努利概率空间, 其中  $F_{1} = \{\varnothing, A, A^{c}, \Omega\}$ . 设成功概率为  $\mathbf{P}_{1}(A) = p (0 \leqslant p \leqslant 1)$ . 考虑其可数无穷维乘积概率空间  $(\Omega, \mathcal{F}, \mathbf{P}) := (\Omega_{1}^{\infty}, \mathcal{F}_{1}^{\infty}, \mathbf{P}_{1}^{\infty})$ . 此概率空间描述可数无穷次伯努利试验. 对  $k \geqslant 1$  记  $B_{k} = \Omega_{1}^{k-1} \times A \times \Omega_{1}^{\infty}$ , 它表示第 k 次试验成功. 注意事件  $B_{1}, B_{2}, \cdots$  相互独立. 再记

$$
\xi_ {k} (\omega) = 1 _ {B _ {k}} (\omega) = 1 _ {A} (\omega_ {k}), \quad \omega = (\omega_ {1}, \omega_ {2}, \dots) \in \Omega_ {1} ^ {\infty}. \tag {2.2.4}
$$

则  $\xi_{k}$  是  $(\Omega, \mathcal{F}, \mathbf{P})$  上的随机变量. 直观上, 若第 k 次试验成功, 则  $\xi_{k}=1$ ; 否则  $\xi_{k}=0$ . 显然有  $\mathbf{P}(\xi_{k}=1)=\mathbf{P}(B_{k})=p$  和  $\mathbf{P}(\xi_{k}=0)=\mathbf{P}(B_{k}^{c})=1-p$ . 注意前 n 次试验中成功的总次数可表示为  $\xi:=\xi_{1}+\xi_{2}+\cdots+\xi_{n}$ . 由定理 2.1.9 知  $\xi$  是  $(\Omega, \mathcal{F}, \mathbf{P})$  上的随机变量.

对于离散型变量的概率问题, 一般可以借助级数和的方法处理, 这为很多计算带来了方便. 本节下面讨论伯努利试验中出现的几个离散型随机变量的分布.

## 2.2.1 二项分布

令 $(\Omega, \mathcal{F}, \mathbf{P})$ 是例2.2.1中定义的伯努利概率空间的可数无穷维乘积空间，而 $\xi$ 和 $\xi_k$ 也如那里定义。不难算出

$$
\mathbf {P} (\xi = i) = \mathrm{C} _ {n} ^ {i} p ^ {i} q ^ {n - i}, \quad i = 0, 1, \dots , n. \tag {2.2.5}
$$

上式右端给出的离散型概率分布称为二项分布, 记作 $B(n,p)$. 特别地, 称 $B(1,p)$ 为伯努利分布. 注意

$$
\sum_ {i = 0} ^ {n} \mathrm{C} _ {n} ^ {i} p ^ {i} q ^ {n - i} = (p + q) ^ {n} = 1.
$$

由(2.2.5)式得

$$
\frac {\mathbf {P} (\xi = i)}{\mathbf {P} (\xi = i - 1)} = 1 + \frac {(n + 1) p - i}{i q}.
$$

注意当 $i < (n + 1)p$ 时, $\mathbf{P}(\xi = i) > \mathbf{P}(\xi = i - 1)$, 而当 $i > (n + 1)p$ 时, $\mathbf{P}(\xi = i) < \mathbf{P}(\xi = i - 1)$. 所以 $\mathbf{P}(\xi = i)$ 的值先随 $i$ 的增加而上升, 再随 $i$ 的增加而下降. 使 $\mathbf{P}(\xi = i)$ 取得最大值的 $i$ 称为二项分布的最可能值.

我们用 $\lfloor x\rfloor$ 表示不超过 $x\in \mathbb{R}$ 的最大整数. 显然 $i_0\coloneqq \lfloor (n + 1)p\rfloor$ 是最可能值. 若 $(n + 1)p$ 是整数, 则 $i_0$ 和 $i_0 - 1$ 同为最可能值.

例 2.2.2 掷一枚质地均匀的硬币 2n 次, 记正面朝上的次数为  $\xi$ . 则  $\xi$  服从  $B(2n, 1/2)$  分布, 其最可能值为  $\lfloor(2n+1)p\rfloor=n$ . 利用斯特林 (Stirling) 公式有  $n!\approx n^{n}e^{-n}\sqrt{2\pi n}$ , 得到

$$
\begin{array}{l} \mathbf {P} (\xi = n) = \mathrm{C} _ {2 n} ^ {n} \Big (\frac {1}{2} \Big) ^ {2 n} = \frac {(2 n) !}{(n !) ^ {2} 2 ^ {2 n}} \\ \approx \frac {2 ^ {2 n + 1} n ^ {2 n} \mathrm{e} ^ {- 2 n} \sqrt {\pi n}}{n ^ {2 n + 1} \mathrm{e} ^ {- 2 n} 2 ^ {2 n + 1} \pi} = \frac {1}{\sqrt {n \pi}} \rightarrow 0, \quad n \rightarrow \infty . \\ \end{array}
$$

## 2.2.2 几何分布

令 $(\Omega, \mathcal{F}, \mathbf{P})$ 是例 2.2.1 中定义的伯努利概率空间的可数无穷维乘积空间.对于 $\omega = (\omega_1, \omega_2, \cdots) \in \Omega$ 和 $k = 1, 2, \cdots$ 定义

$$
\eta (\omega) = k, \quad \omega_ {1} \in A ^ {c}, \dots , \omega_ {k - 1} \in A ^ {c} \text {且} \omega_ {k} \in A.
$$

则 $\eta$ 代表了首次成功时的试验次数, 称为首次成功时间. 显然

$$
\{\eta = k \} = (A ^ {c}) ^ {k - 1} \times A \times \Omega_ {1} ^ {\infty}.
$$

根据乘积概率测度的定义, 有

$$
\mathbf {P} (\eta = k) = (1 - p) ^ {k - 1} p, \quad k = 1, 2, \dots .
$$

上式右端给出的离散型概率分布称为以 $p$ 为参数的几何分布，记作 $G(p)$

定理2.2.2 取值为非负整数的随机变量 $\eta$ 服从几何分布当且仅当对任意的 $n, k \geqslant 1$ 有

$$
\mathbf {P} (\eta > k + n | \eta > n) = \mathbf {P} (\eta > k). \tag {2.2.6}
$$

证明 “$\Rightarrow$” 假设 $\eta$ 服从几何分布 $G(p)$. 则

$$
\mathbf {P} (\eta > n) = \sum_ {k = n + 1} ^ {\infty} (1 - p) ^ {k - 1} p = \frac {p (1 - p) ^ {n}}{1 - q} = (1 - p) ^ {n}.
$$

由此易得 (2.2.6) 式.

“$\Leftarrow$”令 $q_{n} = \mathbf{P}(\xi > n)$. 由 (2.2.6) 式有

$$
\frac {q _ {k + n}}{q _ {n}} = q _ {k} \quad \Rightarrow \quad q _ {k + n} = q _ {n} q _ {k}.
$$

因此 $q_{k} = q_{1}^{k}$ .取 $p = 1 - q_{1}$ 得

$$
\mathbf {P} (\eta = k) = q _ {k - 1} - q _ {k} = (1 - p) ^ {k - 1} p,
$$

即  $\eta$  服从几何分布  $G(p)$ .

由 (2.2.6) 式表达的性质称为几何分布的无记忆性, 其成立的原因是由于伯努利试验是独立重复进行的.

例 2.2.3 在一串 10 把外形相同的钥匙中, 只有一把能打开某扇房门, 现用这些钥匙尝试开门, 试对放回与不放回的情形, 分别求出  $E = \{ \text{至多试三次打开门} \}$  的概率.

解 (1) 每次取一把钥匙试开, 然后放回, 以 $\xi$ 表示首次打开门的试开次数. 则 $\xi$ 服从参数为 $p = 0.1$ 的几何分布, 故

$$
\mathbf {P} (E) = \mathbf {P} (\xi \leqslant 3) = 0. 1 + 0. 9 \times 0. 1 + 0. 9 ^ {2} \times 0. 1 = 0. 2 7 1.
$$

(2) 每次取一把钥匙试开, 不放回, 则

$$
\mathbf {P} (E) = 1 - \mathbf {P} (E ^ {c}) = 1 - \frac {\mathrm{C} _ {9} ^ {3}}{\mathrm{C} _ {1 0} ^ {3}} = 0. 3.
$$

## 2.2.3 帕斯卡分布

考虑可数重伯努利试验. 对于 $n = 1,2,\dots$ ，令 $\eta_{n}$ 为到第 $n$ 次成功时的试验次数，称为第 $n$ 次成功的时间. 则 $\{\eta_n = k\} = \{\text{前} k - 1\text{次试验中恰有} n - 1\text{次成功且第} k\text{次试验成功}\}$. 由此易得

$$
\mathbf {P} (\eta_ {n} = k) = \mathrm{C} _ {k - 1} ^ {n - 1} p ^ {n} (1 - p) ^ {k - n}, \quad k = n, n + 1, n + 2, \dots . \tag {2.2.7}
$$

上式右端给出的离散型概率分布称为以 $(n,p)$ 为参数的帕斯卡(Pascal)分布,记作 $Pa(n,p)$ .

显然, 几何分布  $G(p)$  是帕斯卡分布  $Pa(n,p)$  当 n=1 时的特例.

考虑泰勒 (Taylor) 展开式: 对  $|x| < 1$  有

$$
\begin{array}{l} (1 - x) ^ {- n} = \sum_ {k = 0} ^ {\infty} \frac {n (n + 1) \cdots (n + k - 1)}{k !} x ^ {k} \\ = \sum_ {k = 0} ^ {\infty} \mathrm{C} _ {n + k - 1} ^ {n - 1} x ^ {k} = \sum_ {k = n} ^ {\infty} \mathrm{C} _ {k - 1} ^ {n - 1} x ^ {k - n}. \\ \end{array}
$$

取 x = 1 - p 即知 (2.2.7) 式右端之和确实为 1.

在可数重伯努利试验中, 令 $\zeta_{n} = \eta_{n} - n$ 为第 $n$ 次成功前的失败次数. 不难看出, 对 $k = 0,1,2,\dots$ 有

$$
\begin{array}{l} \mathbf {P} (\zeta_ {n} = k) = \mathrm{C} _ {k + n - 1} ^ {n - 1} p ^ {n} (1 - p) ^ {k} = \mathrm{C} _ {k + n - 1} ^ {k} p ^ {n} (1 - p) ^ {k} \\ = \frac {(k + n - 1) \cdots (n + 1) n}{k !} p ^ {n} (1 - p) ^ {k} \\ = \frac {(- n) (- n - 1) \cdots (- n - k + 1)}{k !} p ^ {n} (p - 1) ^ {k}. \\ \end{array}
$$

对组合记号作简单推广后, 可将上式表示为

$$
\mathbf {P} (\zeta_ {n} = k) = \mathrm{C} _ {- n} ^ {k} p ^ {n} (p - 1) ^ {k}, \quad k = 0, 1, 2, \dots . \tag {2.2.8}
$$

上式右端给出的离散型概率分布称为以 $(n,p)$ 为参数的负二项分布，记作 $NB(n,p)$.

例 2.2.4 口袋中有两盒火柴, 开始时每盒中都有 n 根火柴, 每次从中任取一盒并任取一根. 求此人掏出一盒发现已空而另一盒尚余 r 根的概率.

解 令 $E = \{$ 掏出甲盒已空而乙盒尚余 $r$ 根 $\}$. 我们将 $\{$ 取出甲盒 $\}$ 解释为成功, 则

$$
E = \{\text {第} n + 1 \text {次成功发生在第} n + 1 + n - r \text {次试验} \}.
$$

根据帕斯卡分布的概率表达式有

$$
\mathbf {P} (E) = \mathrm{C} _ {2 n - r} ^ {n} \Big (\frac {1}{2} \Big) ^ {2 n - r + 1},
$$

由对称性知所求概率为  $2\mathbf{P}(E)$ .

例 2.2.5 (分赌注问题) 甲、乙两人赌博水平相当, 各下赌注 d 元, 商量先胜三局者胜. 如果甲胜一局而乙尚未获胜时终止, 问赌注如何分配合理?

解 假若在目前的形势下二人继续赌博, 则甲取得赌注 $\Leftrightarrow$ 在后面 $p = 1/2$ 的可数重伯努利试验中, 第 2 次成功发生在第 3 次失败之前 $\Leftrightarrow$ 到第 2 次成功为止的试验次数小于 $5 \Leftrightarrow \eta_{2} < 5$, 这里 $\eta_{2}$ 服从帕斯卡分布 $Pa(2,1/2)$. 根据该帕斯卡分布的概率表达式有

$$
\mathbf {P} (\eta_ {2} <   5) = \left(\frac {1}{2}\right) ^ {2} + \mathrm{C} _ {2} ^ {1} \left(\frac {1}{2}\right) ^ {3} + \mathrm{C} _ {3} ^ {1} \left(\frac {1}{2}\right) ^ {4} = \frac {1 1}{1 6}.
$$

## 2.2.4 泊松分布

在伯努利试验的应用中, 我们经常会遇到成功概率很小, 且试验次数很多的情况. 在这种时候, 下面的定理给出了相应的二项分布的一种近似.

定理2.2.3 设对每个 $n \geqslant 1$ 有随机变量 $\xi_{n}$ 服从二项分布 $B(n, p_n)$ 且 $\lim_{n \to \infty} np_n = \lambda > 0$. 则

$$
\lim _ {n \to \infty} \mathbf {P} (\xi_ {n} = k) = \frac {\lambda^ {k}}{k !} \mathrm{e} ^ {- \lambda}, \quad k = 0, 1, 2, \dots . \tag {2.2.9}
$$

证明 注意

$$
\begin{array}{l} \mathbf {P} (\xi_ {n} = k) = \frac {n (n - 1) \cdots (n - k + 1)}{k !} p _ {n} ^ {k} (1 - p _ {n}) ^ {n - k} \\ = \frac {(n p _ {n}) ^ {k}}{k !} \cdot 1 \cdot \left(1 - \frac {1}{n}\right) \dots \left(1 - \frac {k - 1}{n}\right) (1 - p _ {n}) ^ {n - k}, \\ \end{array}
$$

在假设条件下有

$$
\lim _ {n \to \infty} (1 - p _ {n}) ^ {n} = \lim _ {n \to \infty} (1 - p _ {n}) ^ {(1 / p _ {n}) (n p _ {n})} = \mathrm{e} ^ {- \lambda},
$$

故得欲证结果.

等式 (2.2.9) 右端的数列构成一个离散型概率分布, 称为参数为 $\lambda$ 的泊松 (Poisson) 分布, 记作 $P(\lambda)$. 上面的定理称为泊松定理. 该定理说明, 当 $n$ 很大而 $np$ 不太大时, 二项分布 $B(n, p)$ 可用泊松分布 $P(np)$ 近似代替.

例 2.2.6 泊松分布  $P(\lambda)$  的最可能的值为  $\lfloor\lambda\rfloor$ ，即不超过  $\lambda$  的最大整数。当  $\lambda$  为整数时，最可能值有两个，即  $\lambda$  和  $\lambda-1$ 。

例 2.2.7 用  $\xi$  表示在一定时间内某种仪器发射出的粒子数, 设它服从泊松分布  $P(\lambda)$ . 再假定发射出的每个粒子被记录下来的概率为 p (0 < p < 1), 没有被记录的概率为 1 - p, 且各个粒子是否被记录相互独立. 令记录下的粒子数为  $\eta$ , 则  $\eta$  服从泊松分布  $P(\lambda p)$ .

证明 记 q = 1 - p. 利用全概率公式,

$$
\begin{array}{l} \mathbf {P} (\eta = k) = \sum_ {n = k} ^ {\infty} \mathbf {P} (\xi = n) \mathbf {P} (\eta = k | \xi = n) \\ = \sum_ {n = k} ^ {\infty} \frac {\lambda^ {n}}{n !} \mathrm{e} ^ {- \lambda} \mathrm{C} _ {n} ^ {k} p ^ {k} q ^ {n - k} \\ = \sum_ {n = k} ^ {\infty} \frac {(\lambda p) ^ {k}}{k !} \mathrm{e} ^ {- \lambda p} \frac {(q \lambda) ^ {n - k}}{(n - k) !} \mathrm{e} ^ {- \lambda (1 - p)} \\ = \frac {(\lambda p) ^ {k}}{k !} \mathrm{e} ^ {- \lambda p} \sum_ {i = 0} ^ {\infty} \frac {(q \lambda) ^ {i}}{i !} \mathrm{e} ^ {- \lambda q} \\ = \frac {(\lambda p) ^ {k}}{k !} \mathrm{e} ^ {- \lambda p}. \\ \end{array}
$$

这说明  $\eta$  服从泊松分布  $P(\lambda p)$ .

## 2.2.5 泊松粒子流

设有一个随机粒子流, 对于 $t \geqslant 0$ 在时段 $(0, t]$ 内到达的粒子个数 $N_{t}$ 有限, 特别地, $N_{0} = 0$. 这里的 $N_{t}$ 是随机变量, 而当 $\omega \in \Omega$ 固定后 $t \mapsto N_{t}(\omega)$ 是右连续不降整数值阶