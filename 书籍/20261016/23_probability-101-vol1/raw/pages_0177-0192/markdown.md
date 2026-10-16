$$
\begin{array}{l} \leqslant \sum_ {k = 1} ^ {N - 1} \mathbf {P} \left(\left| \xi_ {n _ {k}} - \xi \right| \geqslant \varepsilon\right) + \sum_ {k = N} ^ {\infty} \mathbf {P} \left(\left| \xi_ {n _ {k}} - \xi \right| \geqslant 1 / k\right) \\ \leqslant \sum_ {k = 1} ^ {N - 1} \mathbf {P} (| \xi_ {n _ {k}} - \xi | \geqslant \varepsilon) + \sum_ {k = N} ^ {\infty} \frac {1}{2 ^ {k}} <   \infty , \\ \end{array}
$$

故  $\xi_{n_{k}}\stackrel{c}{\rightarrow}\xi.$  应用定理 6.1.2 即知  $\xi_{n_{k}}\stackrel{a.s.}{\rightarrow}\xi.$

定义 6.1.4 称随机变量列  $\{\xi_{n}\}$  为依概率收敛的基本列或柯西列, 是指对任意的  $\varepsilon > 0$ , 当  $m, n \to \infty$  时有

$$
\mathbf {P} (| \xi_ {m} - \xi_ {n} | \geqslant \varepsilon) = \mathbf {P} \big (\omega \in \Omega : | \xi_ {m} (\omega) - \xi_ {n} (\omega) | \geqslant \varepsilon \big) \to 0.
$$

定理 6.1.6 若随机变量序列  $\{\xi_{n}\}$  是依概率收敛的基本列, 则存在  $\{\xi_{n}\}$  的子列  $\{\xi_{n_{k}}\}$ , 使当  $k \to \infty$  时  $\xi_{n_{k}} \stackrel{a.s.}{\rightarrow}$  某个随机变量  $\xi$ .

证明 在假设条件下, 对任意的 $k \geqslant 1$ 可取 $m_{k}$, 使当 $m, n \geqslant m_{k}$ 时有

$$
\mathrm{P} \{| \xi_ {m} - \xi_ {n} | \geqslant 1 / 2 ^ {k} \} <   1 / 2 ^ {k}.
$$

令 $n_1 = m_1$ ，并对 $k \geqslant 1$ 定义 $n_{k+1} = (n_k + 1) \vee m_{k+1}$. 显然 $n_k \to \infty$. 再令

$$
F _ {m} = \bigcup_ {k = m} ^ {\infty} \{| \xi_ {n _ {k}} - \xi_ {n _ {k + 1}} | \geqslant 1 / 2 ^ {k} \}.
$$

于是  $\{F_{m}\}$  为递降的事件序列且

$$
\mathbf {P} (F _ {m}) \leqslant \sum_ {k = m} ^ {\infty} \mathbf {P} \{| \xi_ {n _ {k}} - \xi_ {n _ {k + 1}} | \geqslant 1 / 2 ^ {k} \} \leqslant \sum_ {k = m} ^ {\infty} \frac {1}{2 ^ {k}} = \frac {1}{2 ^ {m - 1}}.
$$

令 $N = \bigcap_{m=1}^{\infty} F_m$. 则有 $\mathbf{P}(N) = \lim_{m \to \infty} \mathbf{P}(F_m) = 0$. 注意当

$$
\omega \in F _ {m} ^ {c} = \bigcap_ {k = m} ^ {\infty} \{| \xi_ {n _ {k}} - \xi_ {n _ {k + 1}} | <   1 / 2 ^ {k} \}.
$$

易知 $\{\xi_{n_k}(\omega)\}$ 是通常意义下的基本列. 于是, 当 $\omega \in N^c = \bigcup_{m=1}^{\infty} F_m^c$ 时 $\{\xi_{n_k}(\omega)\}$ 是通常意义下的基本列, 故当 $n \to \infty$ 时 $\xi_{n_k}(\omega) \to$ 某个数 $\xi(\omega)$. 对于 $\omega \in N$, 令 $\xi(\omega) = 0$. 显然 $\xi_{n_k} \stackrel{\text{a.s.}}{\rightarrow} \xi$. □

定理 6.1.7 随机变量列  $\{\xi_{n}\}$  是依概率收敛的基本列的充要条件是当  $n \rightarrow \infty$  时  $\xi_{n} \stackrel{P}{\rightarrow}$  某个随机变量  $\xi$ .

证明 假设 $\xi_{n} \stackrel{\mathrm{P}}{\rightarrow} \xi$。则对任意的 $\varepsilon > 0$ 和 $\delta > 0$, 存在 $N = N(\varepsilon, \delta) \geqslant 1$ 使当 $n \geqslant N$ 时有

$$
\mathbf {P} \{| \xi_ {n} - \xi | \geqslant \varepsilon / 2 \} <   \delta / 2.
$$

所以当 $m, n \geqslant N$ 时, 根据次可加性有

$$
\mathbf {P} \{| \xi_ {m} - \xi_ {n} | \geqslant \varepsilon \} \leqslant \mathbf {P} (\{| \xi_ {m} - \xi | \geqslant \varepsilon / 2 \} \cup \{| \xi_ {n} - \xi | \geqslant \varepsilon / 2 \}) \leqslant \delta .
$$

这说明 $\{\xi_n\}$ 是依概率收敛的基本列. 反之, 假设 $\{\xi_n\}$ 是依概率收敛的基本列. 根据定理 6.1.6, 有子列 $\{\xi_{n_k}\} \subseteq \{\xi_n\}$ 使得 $\xi_{n_k} \stackrel{\mathrm{a.s.}}{\rightarrow}$ 某个随机变量 $\xi$. 于是有 $\xi_{n_k} \stackrel{\mathrm{p}}{\rightarrow} \xi$. 这样, 对任意的 $\varepsilon > 0$ 和 $\delta > 0$, 存在 $N = N(\varepsilon, \delta) \geqslant 1$ 使当 $m, n \geqslant N$ 时有

$$
\mathrm{P} \{| \xi_ {n} - \xi_ {m} | \geqslant \varepsilon / 2 \} <   \delta .
$$

对于 $n \geqslant N$ 取 $n_k \geqslant n$, 此时有

$$
\begin{array}{l} \mathbf {P} \{| \xi_ {n} - \xi | \geqslant \varepsilon \} \leqslant \mathbf {P} \{| \xi_ {n} - \xi_ {n _ {k}} | \geqslant \varepsilon / 2 \} + \mathbf {P} \{| \xi_ {n _ {k}} - \xi | \geqslant \varepsilon / 2 \} \\ \leqslant \delta + \mathbf {P} \{| \xi_ {n _ {k}} - \xi | \geqslant \varepsilon / 2 \}. \\ \end{array}
$$

在上式中令 $k \to \infty$ 即知 $\mathbf{P}\{| \xi_n - \xi| \geqslant \varepsilon\} \leqslant \delta$. 所以当 $n \to \infty$ 时有 $\xi_n \xrightarrow{\mathrm{p}} \xi$.

显然, 定理 6.1.7 中的随机变量  $\xi$  在几乎必然相等的意义下是唯一的.

## 6.1.3 平均收敛

设 $r > 0$ 为常数. 用 $L^r$ 表示概率空间 $(\Omega, \mathcal{F}, \mathbf{P})$ 上的所有满足 $\mathbf{E}(|\xi|^r) < \infty$ 的随机变量 $\xi$ 构成的集合.

定义 6.1.5 设有  $\xi, \xi_{1}, \xi_{2}, \cdots \in L^{r}$ . 称  $\{\xi_{n}\} L^{r}$  收敛或 r 阶平均收敛于  $\xi$ , 并记作  $\xi_{n} \stackrel{L^{r}}{\rightarrow} \xi$ , 是指当  $n \to \infty$  时有  $\mathbf{E}(|\xi_{n} - \xi|^{r}) \to 0$ .

定义6.1.6 称 $\{\xi_n\} \subseteq L^r$ 为 $L^r$ 基本列或 $L^r$ 柯西列, 是指当 $m, n \to \infty$ 时有 $\mathbf{E}(|\xi_m - \xi_n|^r) \to 0$.

根据推论 4.3.12, 函数 $r \mapsto [\mathbf{E}(|X|^r)]^{1/r}$ 在 $(0, \infty)$ 上不降. 因此, 对于 $0 < q < r$, 若 $\xi_n \xrightarrow{L^r} \xi$, 则 $\xi_n \xrightarrow{L^q} \xi$. 类似地, 若 $\{\xi_n\}$ 是 $L^r$ 中的基本列, 则它是 $L^q$ 中的基本列.

引理6.1.8 设对常数 $r > 0$ 有 $\mathbf{E}[|\xi|^r] < \infty$. 则对任意的 $\varepsilon > 0$ 有

$$
\mathbf {P} (| \xi | \geqslant \varepsilon) \leqslant \varepsilon^ {- r} \mathbf {E} [ | \xi | ^ {r} ].
$$

证明 注意 $|\xi|^r \geqslant |\xi|^r 1_{\{|\xi| \geqslant \varepsilon\}} \geqslant \varepsilon^r 1_{\{|\xi| \geqslant \varepsilon\}}$。因此有

$$
\mathbf {E} [ | \xi | ^ {r} ] \geqslant \mathbf {E} [ | \xi | ^ {r} 1 _ {\{| \xi | \geqslant \varepsilon \}} ] \geqslant \mathbf {E} [ \varepsilon^ {r} 1 _ {\{| \xi | \geqslant \varepsilon \}} ] = \varepsilon^ {r} \mathbf {P} (| \xi | \geqslant \varepsilon),
$$

故欲证不等式成立.

上面引理中的不等式称为马尔可夫 (Markov) 不等式.

定理 6.1.9 (i) 若  $\xi_{n} \stackrel{L^{r}}{\rightarrow} \xi$ ，则  $\xi_{n} \stackrel{P}{\rightarrow} \xi$ ; (ii) 若  $\{\xi_{n}\}$  是  $L^{r}$  中的基本列，则它是依概率收敛的基本列.

证明 由马尔可夫不等式易证.

定理6.1.10 随机变量列 $\{\xi_n\}$ 是 $L^r$ 中的基本列的充要条件是当 $n\to \infty$ 时$\xi_{n}\stackrel {L^{r}}{\rightarrow}$ 某个随机变量 $\xi$

证明 假设 $\xi_{n}\stackrel {L^{r}}{\rightarrow}\xi$ 对于 $\varepsilon >0$ ，存在 $N = N(\varepsilon)$ 使当 $n\geqslant N$ 时有

$$
\mathbf {E} [ | \xi_ {n} - \xi | ^ {r} ] <   \varepsilon / 2.
$$

于是当 $m, n \geqslant N$ 时有

$$
\mathbf {E} [ | \xi_ {m} - \xi_ {n} | ^ {r} ] \leqslant c _ {r} \mathbf {E} [ | \xi_ {m} - \xi | ^ {r} ] + c _ {r} \mathbf {E} [ | \xi - \xi_ {m} | ^ {r} ] \leqslant c _ {r} \varepsilon .
$$

其中 $c_{r} = 1$ (当 $0 < r \leqslant 1$ 时) 或 $c_{r} = 2^{r - 1}$ (当 $r > 1$ 时). 因此 $\{\xi_n\}$ 是 $L^r$ 中的基本列. 反之, 设 $\{\xi_n\}$ 是 $L^r$ 中的基本列. 由定理6.1.9知 $\{\xi_n\}$ 是依概率收敛的基本列. 根据定理6.1.6存在 $\{\xi_n\}$ 的子列 $\{\xi_{n_k}\}$, 使当 $k \to \infty$ 时 $\xi_{n_k} \stackrel{\mathrm{a.s.}}{\rightarrow}$ 某个随机变量 $\xi$. 对于任意的 $\varepsilon > 0$, 可取 $N = N(\varepsilon)$ 使当 $m, n \geqslant N$ 时有 $\mathbf{E}[|\xi_m - \xi_n|^r] < \varepsilon$. 特别地, 对 $n_k \geqslant n \geqslant N$ 有 $\mathbf{E}[|\xi_{n_k} - \xi_n|^r] < \varepsilon$. 再由法图定理有

$$
\mathbf {E} [ | \xi - \xi_ {n} | ^ {r} ] = \mathbf {E} \Big [ \operatorname * {l i m i n f} _ {k \to \infty} | \xi_ {n _ {k}} - \xi_ {n} | ^ {r} \Big ] \leqslant \operatorname * {l i m i n f} _ {k \to \infty} \mathbf {E} [ | \xi_ {n _ {k}} - \xi_ {n} | ^ {r} ] \leqslant \varepsilon .
$$

这就证明了  $\xi_{n}\stackrel{L^{r}}{\rightarrow}\xi.$

□

不难证明, 定理 6.1.10 中的随机变量  $\xi$  在几乎必然相等的意义下是唯一的.

例 6.1.3 令  $(\Omega, \mathcal{F}, \mathbf{P})$  如例 6.1.2 所定义. 对  $n \geqslant 1$  令  $X_{n} = n^{1/r} 1_{(0,1/n]}$ . 则  $\lim_{n \to \infty} X_{n}(\omega) = 0$  对所有  $\omega \in \Omega$  成立, 故  $X_{n} \stackrel{a.s.}{\rightarrow} 0$ . 但  $E[|X_{n}|^{r}] = 1$ , 故  $X_{n} \stackrel{L^{r}}{\rightarrow} 0$  不成立.

例 6.1.4 令  $\{\eta_{ki}: k \geqslant 1, 1 \leqslant i \leqslant k\}$  和  $\{\xi_{n}: n \geqslant 1\}$  如例 6.1.2 所定义, 则  $\xi_{n} \stackrel{a.s.}{\rightarrow} \xi$  不成立. 但对任意的 r > 0 有  $\mathbf{E}(|\eta_{ki}|^{r}) = 1/k \rightarrow 0$ , 由此易知  $\xi_{n} \stackrel{L^{r}}{\rightarrow} 0$ .

## 练习题

1. 设  $\{\xi_{n}\}$  为独立随机变量序列. 证明:  $\xi_{n} \xrightarrow{c} 0$  和  $\xi_{n} \xrightarrow{a.s.} 0$  等价.
2. 设  $\{X_{n}\}$  为不增的非负随机变量序列且  $X_{n} \stackrel{p}{\rightarrow} 0$ . 证明  $X_{n} \stackrel{a.s.}{\rightarrow} 0$ .
3. 证明:对于任何实随机变量 $X$，存在只取有理数值的随机变量序列 $\{X_n\}$ 满足 $X_n \stackrel{\text{a.s.}}{\rightarrow} X$.
4. 设 $f$ 为 $\mathbb{R}_+$ 上的非负不降函数且当 $x > 0$ 时有 $f(x) > 0$. 证明对任何随机变量 $\xi$ 和常数 $\varepsilon > 0$ 有

$$
\mathbf {P} (| \xi | \geqslant \varepsilon) \leqslant \frac {1}{f (\varepsilon)} \mathbf {E} [ f (| \xi |) ].
$$

5. 设有 $\xi_{n} \xrightarrow{\mathrm{p}} \xi$ 和 $\eta_{n} \xrightarrow{\mathrm{p}} \eta$. 证明 $\xi_{n} \pm \eta_{n} \xrightarrow{\mathrm{p}} \xi \pm \eta$ 和 $\xi_{n} \eta_{n} \xrightarrow{\mathrm{p}} \xi \eta$.

6. 设 $f$ 为 $\mathbb{R}_{+}$ 上的有界非负不降的连续函数且有 $f(0) = 0$ 和 $f(x) > 0 (x > 0)$. 证明 $\xi_{n} \stackrel{\mathrm{p}}{\to} 0$ 的充要条件是 $\mathbf{E}f(|\xi_{n}|) \to 0$.

## 6.2 分布函数的弱收敛

## 6.2.1 不降函数的弱收敛

定义 6.2.1 设  $G, G_{1}, G_{2}, \cdots$  为某个区间  $U \subseteq R$  上的不降函数. 令  $C_{G} \subseteq U$  为 G 的连续点集. 若

$$
\lim _ {n \to \infty} G _ {n} (x) = G (x), \quad x \in C _ {G}, \tag {6.2.1}
$$

则称序列  $\{G_{n}\}$  弱收敛于 G, 记作  $G_{n} \xrightarrow{w} G$ .

定理 6.2.1 设  $G_{n}, n=1,2,\cdots$  和 G 为开区间  $U \subseteq R$  上的不降函数. 若对于 U 的某个稠子集 D 有

$$
\lim _ {n \to \infty} G _ {n} (x) = G (x), \quad x \in D,
$$

则 $G_{n}\xrightarrow{\mathrm{w}}G.$

证明 设 $x \in C_G \subseteq U$. 可取 $y, z \in D$ 使 $y < x < z$. 这样有

$$
G _ {n} (y) \leqslant G _ {n} (x) \leqslant G _ {n} (z).
$$

令 $n\to \infty$ 得

$$
\begin{array}{l} G (y) = \lim _ {n \to \infty} G _ {n} (y) \leqslant \operatorname * {l i m i n f} _ {n \to \infty} G _ {n} (x) \\ \leqslant \operatorname * {l i m s u p} _ {n \to \infty} G _ {n} (x) \leqslant \lim _ {n \to \infty} G _ {n} (z) = G (z). \\ \end{array}
$$

在上式中令 $y \uparrow x$ 和 $z \downarrow x$ 得

$$
G (x) \leqslant \operatorname * {l i m   i n f} _ {n \to \infty} G _ {n} (x) \leqslant \operatorname * {l i m   s u p} _ {n \to \infty} G _ {n} (x) \leqslant G (x).
$$

故 $\lim_{n\to \infty}G_n(x) = G(x)$. 因此有 $G_{n}\stackrel{\mathrm{w}}{\rightarrow}G$.

例6.2.1 对于任何 $n \geqslant 1$ 可以定义 $\mathbb{R}$ 上的概率分布函数 $F_{n}$ 如下:

$$
F _ {n} (x) = 1 _ {\{x \geqslant n \}} = \left\{ \begin{array}{l l} 0, & x <   n, \\ 1, & x \geqslant n, \end{array} \right.
$$

则显然 $F_{n} \stackrel{\mathrm{w}}{\rightarrow} 0$. 这说明概率分布函数序列的弱收敛极限未必还是概率分布函数.

## 6.2.2 依分布收敛

定义 6.2.2 设随机变量  $\xi, \xi_{1}, \xi_{2}, \cdots$  分别具有分布函数  $F, F_{1}, F_{2}, \cdots$ . 若当  $n \to \infty$  时有  $F_{n} \stackrel{w}{\rightarrow} F$ , 则称序列  $\{\xi_{n}\}$  依分布收敛或弱收敛于  $\xi$ , 记作  $\xi_{n} \stackrel{d}{\rightarrow} \xi$  或  $\xi_{n} \stackrel{w}{\rightarrow} \xi$ .

根据定义 6.2.1, 这里  $F_{n} \xrightarrow{w} F$  意味着  $F_{n}(x) \to F(x)$  对所有  $x \in C_{F}$  成立, 其中  $C_{F}$  为 F 的连续点集. 注意, 该定义并不要求随机变量  $\xi, \xi_{1}, \xi_{2}, \cdots$  定义在同一个概率空间之上.

例6.2.2 定义 $\xi_{n}(\omega) = 1 / n$ 和 $\xi (\omega) = 0, \omega \in \Omega$. 则显然 $\xi_{n} \stackrel{\mathrm{a.s.}}{\rightarrow} \xi$. 注意 $\xi_{n}$ 和 $\xi$ 的分布函数分别为

$$
F _ {n} (x) = 1 _ {\{x \geqslant 1 / n \}}, \quad F (x) = 1 _ {\{x \geqslant 0 \}}.
$$

因此 $F_{n} \stackrel{\mathrm{w}}{\rightarrow} F$，但在点 $0 \notin C_{F}$ 有 $F_{n}(0) = 0 \nrightarrow 1 = F(0)$.

定理 6.2.2 若  $\xi_{n} \stackrel{p}{\rightarrow} \xi,$  则  $\xi_{n} \stackrel{w}{\rightarrow} \xi.$

证明 设 $\xi_{n}$ 和 $\xi$ 的分布函数分别为 $F_{n}$ 和 $F$. 注意, 对 $y < x$ 有

$$
\begin{array}{l} \{\xi \leqslant y \} = \{\xi \leqslant y, \xi_ {n} \leqslant x \} \cup \{\xi \leqslant y, \xi_ {n} > x \} \\ \subseteq \{\xi_ {n} \leqslant x \} \cup \{| \xi_ {n} - \xi | > x - y \}, \\ \end{array}
$$

故由概率测度的次可加性得

$$
F (y) \leqslant F _ {n} (x) + \mathbf {P} (| \xi_ {n} - \xi | > x - y)
$$

由于 $\xi_{n} \xrightarrow{\mathrm{P}} \xi$ ，在上式中令 $n \to \infty$ 知

$$
F (y) \leqslant \liminf _ {n \to \infty} F _ {n} (x), \quad y <   x.
$$

类似地可以得到

$$
F (z) \geqslant \operatorname * {l i m s u p} _ {n \to \infty} F _ {n} (x), \quad z > x.
$$

对于 $x \in C_F$ 取 $y \uparrow x$ 和 $z \downarrow x$, 综合上面二式得

$$
\begin{array}{l} F (x) = \lim _ {y \uparrow x} F (y) \leqslant \operatorname * {l i m i n f} _ {n \to \infty} F _ {n} (x) \\ \leqslant \operatorname * {l i m s u p} _ {n \to \infty} F _ {n} (x) \leqslant \lim _ {z \downarrow x} F (z) = F (x). \\ \end{array}
$$

故有  $\lim_{n\to\infty}F_{n}(x)=F(x)$ .

例 6.2.3 设随机变量  $\xi, \eta$  相互独立且均服从伯努利分布  $B(1,1/2)$ . 令  $\xi_{n} = \eta, n \geqslant 1$ . 则显然有  $\xi_{n} \stackrel{a.s.}{\rightarrow} \eta$  和  $\xi_{n} \stackrel{w}{\rightarrow} \xi$ . 但

$$
\begin{array}{l} \mathbf {P} (| \xi_ {n} - \xi | = 1) = \mathbf {P} (\xi_ {n} = 1, \xi = 0) + \mathbf {P} (\xi_ {n} = 0, \xi = 1) \\ = \mathbf {P} (\xi_ {n} = 1) \mathbf {P} (\xi = 0) + \mathbf {P} (\xi_ {n} = 0) \mathbf {P} (\xi = 1) \\ = \frac {1}{2} \times \frac {1}{2} + \frac {1}{2} \times \frac {1}{2} = \frac {1}{2} \nrightarrow 0. \\ \end{array}
$$

故  $\xi_{n}\stackrel{P}{\rightarrow}\xi$  不成立.

定理 6.2.3 若  $\xi_{n}\xrightarrow{w}c$  (常数), 则  $\xi_{n}\xrightarrow{p}c$ .

证明 注意, 常值随机变量 $\xi = c$ 的分布函数为 $F(x) = 1_{\{x \geqslant c\}}$, $x \in \mathbb{R}$. 对任意的 $\varepsilon > 0$, 有

$$
\begin{array}{l} \mathbf {P} (| \xi_ {n} - c | \geqslant \varepsilon) = \mathbf {P} (\xi_ {n} \geqslant c + \varepsilon) + \mathbf {P} (\xi_ {n} \leqslant c - \varepsilon) \\ = 1 - \mathbf {P} (\xi_ {n} <   c + \varepsilon) + F _ {n} (c - \varepsilon). \tag {6.2.2} \\ \end{array}
$$

因为 $c - \varepsilon$ 是 $F$ 的连续点, 所以 $F_{n}(c - \varepsilon) \to F(c - \varepsilon) = 0$. 另外注意

$$
\begin{array}{l} \mathbf {P} (\xi_ {n} <   c + \varepsilon) \geqslant \mathbf {P} (\xi_ {n} \leqslant c + \varepsilon / 2) \\ = F _ {n} (c + \varepsilon / 2) \rightarrow F (c + \varepsilon / 2) = 1. \\ \end{array}
$$

因此 $\mathbf{P}(\xi_n < c + \varepsilon) \to 1$. 再由 (6.2.2) 式得 $\mathbf{P}(|\xi_n - c| \geqslant \varepsilon) \to 0$, 即 $\xi_n \xrightarrow{\mathrm{p}} c$.

定理 6.2.4 设有  $\xi_{n} \stackrel{w}{\rightarrow} \xi$  和  $\eta_{n} \stackrel{p}{\rightarrow} a$ ，其中  $a \in R$  为常数而  $\xi_{n}$  和  $\eta_{n}$  定义在同一个概率空间上。则  $X_{n} := \xi_{n} + \eta_{n} \stackrel{w}{\rightarrow} \xi + a$ 。

证明 首先, 考虑 $a = 0$ 的情况. 令 $C_{F_{\xi}}$ 为 $F_{\xi}$ 的连续点集. 对于 $x \in C_{F_{\xi}}$ 存在序列 $\{z_k\} \subseteq C_{F_{\xi}}$ 满足 $z_k > x$ 且 $z_k \downarrow x$. 由于 $\eta_n \stackrel{\mathrm{P}}{\to} 0$, 对任何 $k \geqslant 1$, 可取 $N_k \geqslant 1$ 使当 $n \geqslant N_k$ 有 $\mathbf{P}(|\eta_n| \geqslant z_k - x) < 1 / k$. 此时

$$
\begin{array}{l} F _ {X _ {n}} (x) = \mathbf {P} (\xi_ {n} + \eta_ {n} \leqslant x, | \eta_ {n} | \geqslant z _ {k} - x) + \mathbf {P} (\xi_ {n} + \eta_ {n} \leqslant x, | \eta_ {n} | <   z _ {k} - x) \\ \leqslant \mathbf {P} \left(\left| \eta_ {n} \right| \geqslant z _ {k} - x\right) + \mathbf {P} \left(\xi_ {n} \leqslant x - \eta_ {n}, - \eta_ {n} <   z _ {k} - x\right) \\ \leqslant 1 / k + \mathbf {P} (\xi_ {n} \leqslant z _ {k}) = 1 / k + F _ {\xi_ {n}} (z _ {k}). \\ \end{array}
$$

由于 $\xi_{n}\xrightarrow{\mathrm{w}}\xi$ ，在上式两端先后令 $n\to \infty$ 得

$$
\operatorname * {l i m s u p} _ {n \to \infty} F _ {X _ {n}} (x) \leqslant 1 / k + F _ {\xi} (z _ {k}),
$$

再令 $k \to \infty$ 得 $\limsup_{n\to \infty}F_{X_n}(x) \leqslant F_\xi(x)$. 类似地有 $\liminf_{n\to \infty}F_{X_n}(x) \geqslant F_\xi(x)$. 这说明 $X_n \stackrel{\mathrm{w}}{\to} \xi$ 成立. 对于一般情况, 由 $\xi_n \stackrel{\mathrm{w}}{\to} \xi$ 和 $\eta_n \stackrel{\mathrm{p}}{\to} a$ 有 $\xi_n + a \stackrel{\mathrm{w}}{\to} \xi + a$ 和 $\eta_n - a \stackrel{\mathrm{p}}{\to} 0$. 再由前面证明的结论知 $X_n = (\xi_n + a) + (\eta_n - a) \stackrel{\mathrm{w}}{\to} \xi + a$.

定理 6.2.5 设有  $\xi_{n} \stackrel{w}{\rightarrow} \xi$  和  $\zeta_{n} \stackrel{p}{\rightarrow} a$ ，其中  $a \in R$  为常数而  $\xi_{n}$  和  $\eta_{n}$  定义在同一个概率空间上。则  $Y_{n} := \zeta_{n} \xi_{n} \stackrel{w}{\rightarrow} a \xi$ 。

证明 首先, 考虑 $a = 0$ 的情况. 对于任意的 $\delta > 0$ 可取充分大的 $c > 0$ 满足 $\{c, -c\} \subseteq C_{F_{\xi}}$ 和

$$
\mathbf {P} (| \xi | > c) = \mathbf {P} (\xi <   - c) + \mathbf {P} (\xi > c) \leqslant F _ {\xi} (- c) + 1 - F _ {\xi} (c) <   \delta .
$$

这样, 对于 $\varepsilon > 0$ 有

$$
\mathbf {P} (| Y _ {n} | \geqslant \varepsilon) = \mathbf {P} (| \zeta_ {n} \xi_ {n} | \geqslant \varepsilon , | \xi_ {n} | \leqslant c) + \mathbf {P} (| \zeta_ {n} \xi_ {n} | \geqslant \varepsilon , | \xi_ {n} | > c)
$$

$$
\begin{array}{l} \leqslant \mathbf {P} (| \zeta_ {n} | \geqslant \varepsilon / c, | \xi_ {n} | \leqslant c) + \mathbf {P} (| \xi_ {n} | > c) \\ \leqslant \mathbf {P} (| \zeta_ {n} | \geqslant \varepsilon / c) + F _ {\xi_ {n}} (- c) + 1 - F _ {\xi_ {n}} (c). \\ \end{array}
$$

因为 $\xi_{n}\stackrel{\mathrm{w}}{\rightarrow}\xi$ 和 $\zeta_n\stackrel{\mathrm{P}}{\rightarrow}0,$ 在上式两端令 $n\to \infty$ 得

$$
\operatorname * {l i m s u p} _ {n \to \infty} \mathbf {P} (| Y _ {n} | \geqslant \varepsilon) \leqslant F _ {\xi} (- c) + 1 - F _ {\xi} (c) <   \delta .
$$

再由 $\delta > 0$ 的任意性即知 $Y_{n} = \zeta_{n}\xi_{n} \xrightarrow{\mathrm{P}} 0$, 从而 $Y_{n} \xrightarrow{\mathrm{W}} 0$. 对于一般情况, 由 $\xi_{n} \xrightarrow{\mathrm{W}} \xi$ 和 $\zeta_{n} \xrightarrow{\mathrm{P}} a$ 易得 $a\xi_{n} \xrightarrow{\mathrm{W}} a\xi$ 和 $\zeta_{n} - a \xrightarrow{\mathrm{P}} 0$, 故由前面证明的结论知 $(\zeta_{n} - a)\xi_{n} \xrightarrow{\mathrm{W}} 0$, 再根据定理6.2.4有 $Y_{n} = a\xi_{n} + (\zeta_{n} - a)\xi_{n} \xrightarrow{\mathrm{W}} a\xi$.

## 6.2.3 斯科罗霍德表示定理

我们前面讨论过一维不降函数的广义逆. 根据一般的定义, 概率分布函数 $F$ 的广义逆 $F^{-1}$ 是区间 $(0,1)$ 上的左连续不降函数, 并且

$$
F ^ {- 1} (y) = \inf \{x \in \mathbb {R}: F (x) \geqslant y \}, \quad 0 <   y <   1. \tag {6.2.3}
$$

命题 6.2.6 设  $F, F_{1}, F_{2}, \cdots$  为 R 上的概率分布函数. 若  $F_{n} \xrightarrow{w} F$ , 则  $F_{n}^{-1} \xrightarrow{w} F^{-1}$ .

证明 设 $y \in (0,1)$ 为 $F^{-1}$ 的连续点. 取 $x, z \in U \cap C_F$ 使 $x < F^{-1}(y) < z$. 由命题2.4.2的(6)知 $F(x) < y < F(z)$, 故当 $n$ 充分大时有 $F_n(x) < y < F_n(z)$. 再由 $F^{-1}$ 的定义有 $x < F_n^{-1}(y) \leqslant z$. 综上, 当 $n$ 充分大时有 $|F_n^{-1}(y) - F^{-1}(y)| \leqslant z - x$. 因 $x, z \in U \cap C_F$ 可以任意接近, 故推知 $F_n^{-1}(y) \to F^{-1}(y)$. □

下面的结果称为斯科罗霍德表示定理.

定理 6.2.7（斯科罗霍德）设概率分布函数序列  $\{F_{n}\}$  弱收敛到概率分布函数 F. 则存在某个概率空间上的随机变量序列  $\{\xi_{n}\}$  和随机变量  $\xi$  满足性质: $\xi_{n}$  和  $\xi$  分别有分布函数  $F_{n}$  和 F 且  $\xi_{n} \stackrel{a.s.}{\rightarrow} \xi$ .

证明 取 $\Omega = (0,1)$ 和 $\mathcal{F} = (0,1) \cap \mathcal{B}$, 并令 $\mathbf{P}$ 为 $(\Omega, \mathcal{F})$ 上的勒贝格测度. 则 $(\Omega, \mathcal{F}, \mathbf{P})$ 是概率空间. 对 $\omega \in \Omega$ 令 $\eta(\omega) = \omega$. 则 $\eta$ 服从均匀分布 $U(0,1)$. 令 $C_{F^{-1}} \subseteq \Omega$ 为 $F^{-1}$ 的连续点集, 则 $D_{F^{-1}} := \Omega \setminus C_{F^{-1}}$ 可数, 故 $\mathbf{P}(D_{F^{-1}}) = 0$, 从而 $\mathbf{P}(C_{F^{-1}}) = 1$. 对 $\omega \in \Omega$ 令

$$
\xi_ {n} (\omega) = F _ {n} ^ {- 1} (\eta (\omega)) = F _ {n} ^ {- 1} (\omega), \quad \xi (\omega) = F ^ {- 1} (\eta (\omega)) = F ^ {- 1} (\omega),
$$

由定理2.4.3知随机变量 $\xi_{n}$ 和 $\xi$ 分别有分布函数 $F_{n}$ 和 $F$. 再由命题6.2.6知对 $\omega \in C_{F^{-1}}$ 有 $\xi_{n}(\omega) \to \xi(\omega)$, 故 $\xi_{n} \stackrel{\mathrm{a.s.}}{\rightarrow} \xi$.

## 练习题

1. 设 $\{\xi_n\}$ 为独立同分布随机变量序列且有 $\mathbf{P}(\xi_n = 1) = \mathbf{P}(\xi_n = 0) = 1/2$。令 $X_n = \sum_{k=1}^{n} \xi_k / 2^k$。证明 $X_n$ 的分布弱收敛于 $(0,1)$ 上的均匀分布。
2. 在上题的假设条件下, 令 $X = \sum_{k=1}^{\infty} \xi_k / 2^k$. 证明 $X$ 服从 $(0,1)$ 上的均匀分布.
3. 证明: 若概率分布函数序列 $\{F_n\}$ 弱收敛到连续的概率分布函数 $F$, 则 $\{F_n\}$ 在 $\mathbb{R}$ 上逐点且一致收敛到 $F$.
4. 证明:对于任何概率分布函数 F，存在离散型的概率分布函数序列  $\{F_{n}\}$  满足  $F_{n} \stackrel{w}{\rightarrow} F$ .
5. 证明: 对于任何概率分布函数 $F$, 存在绝对连续型的概率分布函数序列 $\{F_n\}$ 满足 $F_n \xrightarrow{\mathrm{w}} F$.

## 6.3 弱收敛的等价条件

概率分布函数的弱收敛是一个重要的概念, 在很多概率论问题的研究中发挥着关键作用.

## 6.3.1 黑利定理

引理 6.3.1 设对每个整数  $n \geqslant 1$  有实数列  $S_{n} := \{S_{n,i} : i = 1, 2, \cdots\} \subseteq [0, 1]$ .
则存在子列  $\{S_{k_{n}}\}\subseteq\{S_{n}\}$  使对每个  $i\geqslant1$  极限  $\lim_{n\to\infty}S_{k_{n},i}=T_{i}$  存在.

证明 因  $\{S_{n,1}: n=1,2,\cdots\}\subseteq[0,1]$  是有界数列, 可取  $\{S_{n}\}$  的子列  $\{S_{n}^{(1)}\}$  使极限  $\lim_{n\to\infty}S_{n,1}^{(1)}=T_{1}$  存在. 类似地, 可取  $\{S_{n}^{(1)}\}$  的子列  $\{S_{n}^{(2)}\}$  使极限  $\lim_{n\to\infty}S_{n,2}^{(2)}=T_{2}$  存在. 注意  $\lim_{n\to\infty}S_{n,1}^{(2)}=\lim_{n\to\infty}S_{n,1}^{(1)}=T_{1}$ . 如此下去, 对  $i\geqslant3$  可取  $\{S_{n}^{(i-1)}\}$  的子列  $\{S_{n}^{(i)}\}$  使极限  $\lim_{n\to\infty}S_{n,i}^{(i)}=T_{i}$  存在. 同时对  $1\leqslant j\leqslant i-1$  有  $\lim_{n\to\infty}S_{n,j}^{(i)}=T_{j}$ . 最后, 记  $S_{k_{n}}=S_{n}^{(n)}$ . 则  $\{S_{n_{k}}\}$  为  $\{S_{n}\}$  的子列, 且对每个  $i\geqslant1$  有  $\lim_{n\to\infty}S_{k_{n},i}=T_{i}$ . □

定理6.3.2（黑利第一定理） 实直线 $\mathbb{R}$ 上的任何概率分布函数序列 $\{F_n\}$ 都有子列弱收敛于某个有界右连续不降函数 $F$

证明 记有理数集为 $D = \{r_1, r_2, \cdots, r_i, \cdots\} \subseteq \mathbb{R}$. 对于 $S_n = \{F_n(r_i) : i = 1, 2, \cdots\} \subseteq [0, 1]$, 应用引理 6.3.1 知, 存在子列 $\{F_{k_n}\} \subseteq \{F_n\}$, 使对每个 $i \geqslant 1$ 极限 $G(r_i) := \lim_{k \to \infty} F_{n_k}(r_i)$ 存在. 因 $F_{n_k}$ 是概率分布函数, 故 $G$ 为 $D$ 上的有界不降函数. 补充定义

$$
G (x) = \inf \{G (r): r \in D, r > x \}, \quad x \in \mathbb {R} \setminus D.
$$

则 $G$ 成为 $\mathbb{R}$ 上的有界不降函数. 根据定理6.2.1有 $F_{n_k} \stackrel{\mathrm{w}}{\rightarrow} G$. 注意 $G$ 在 $\mathbb{R}$ 上未必右连续, 但作为不降函数, 它至多只有可数个不连续点. 再定义

$$
F (x) = \inf \{G (r): r \in D, r > x \}, \quad x \in \mathbb {R}.
$$

则 $F$ 是 $\mathbb{R}$ 上的有界右连续不降函数. 显然 $C_F = C_G$, 故 $F_{n_k} \stackrel{\mathrm{w}}{\to} F$.

定理 6.3.3（黑利第二定理） 设  $F, F_{1}, F_{2}, \cdots$  为 R 上的概率分布函数.则  $F_{n} \stackrel{w}{\rightarrow} F$  当且仅当对于 R 上的任何有界连续函数 f 有

$$
\int_ {- \infty} ^ {\infty} f (x) \mathrm{d} F _ {n} (x) \rightarrow \int_ {- \infty} ^ {\infty} f (x) \mathrm{d} F (x). \tag {6.3.1}
$$

证明 “$\Rightarrow$”证法 1 设 $F_{n} \stackrel{\mathrm{w}}{\rightarrow} F$, 即 $F_{n}(x) \to F(x)$ 对所有 $x \in C_{F}$ 成立, 其中 $C_{F}$ 为 $F$ 的连续点集. 给定 $\varepsilon > 0$, 取 $a, b \in C_{F}$ 满足 $a \leqslant b$ 且 $1 - F(b) + F(a) < \varepsilon$. 于是, 存在充分大的 $N \geqslant 1$, 使当 $n \geqslant N$ 时有 $1 - F_{n}(b) + F_{n}(a) < \varepsilon$. 对于 $k \geqslant 1$, 取 $[a, b]$ 的分割点 $\{x_{k,i}\} \subseteq C_{F}$ 使之满足定义 4.1.1 中的条件. 因为 $C_{F}$ 在 $\mathbb{R}$ 中稠密, 这是可以做到的. 再令

$$
f _ {k} (x) = \sum_ {i = 1} ^ {m _ {k}} f (x _ {k, i}) 1 _ {(x _ {k, i - 1}, x _ {k, i} ]} (x), \quad x \in [ a, b ]. \tag {6.3.2}
$$

由 $f$ 在 $[a, b]$ 上的一致连续性, 存在充分大的 $k \geqslant 1$ 使 $|f_k(x) - f(x)| < \varepsilon$, $x \in [a, b]$. 于是有

$$
\int_ {a} ^ {b} | f _ {k} (x) - f (x) | \mathrm{d} F (x) \leqslant \varepsilon [ F (b) - F (a) ] \leqslant \varepsilon
$$

和

$$
\int_ {a} ^ {b} | f _ {k} (x) - f (x) | \mathrm{d} F _ {n} (x) \leqslant \varepsilon [ F _ {n} (b) - F _ {n} (a) ] \leqslant \varepsilon .
$$

记 $\| f\| := \sup_{x\in \mathbb{R}}|f(x)|$ ，我们有

$$
\begin{array}{l} \left| \int_ {- \infty} ^ {\infty} f (x) \mathrm{d} F _ {n} (x) - \int_ {- \infty} ^ {\infty} f (x) \mathrm{d} F (x) \right| \\ \leqslant \left| \int_ {a} ^ {b} f (x) \mathrm{d} F _ {n} (x) - \int_ {a} ^ {b} f (x) \mathrm{d} F (x) \right| + \| f \| [ 1 - F _ {n} (b) + F _ {n} (a) ] + \\ \| f \| [ 1 - F (b) + F (a) ] \\ \leqslant \left| \int_ {a} ^ {b} f _ {k} (x) \mathrm{d} F _ {n} (x) - \int_ {a} ^ {b} f _ {k} (x) \mathrm{d} F (x) \right| + \int_ {a} ^ {b} | f _ {k} (x) - f (x) | \mathrm{d} F _ {n} (x) + \\ \int_ {a} ^ {b} | f _ {k} (x) - f (x) | \mathrm{d} F (x) + 2 \varepsilon \| f \| \\ \end{array}
$$

$$
\leqslant \sum_ {i = 1} ^ {m _ {k}} | f (x _ {k, i}) | \big | F _ {n} (x _ {k, i}) - F (x _ {k, i}) - F _ {n} (x _ {k, i - 1}) + F (x _ {k, i - 1}) \big | + 2 \varepsilon (1 + \| f \|).
$$

在上式两端令 $n\to \infty$ 得

$$
\operatorname * {l i m s u p} _ {n \to \infty} \Big | \int_ {- \infty} ^ {\infty} f (x) \mathrm{d} F _ {n} (x) - \int_ {- \infty} ^ {\infty} f (x) \mathrm{d} F (x) \Big | \leqslant 2 \varepsilon (1 + \| f \|).
$$

再由  $\varepsilon > 0$  的任意性知 (6.3.1) 式成立.

“$\Rightarrow$”证法2 根据斯科罗霍德表示定理, 存在某个概率空间上的随机变量序列 $\{\xi_n\}$ 和随机变量 $\xi$ 满足性质: $\xi_n$ 和 $\xi$ 分别有分布函数 $F_n$ 和 $F$ 且 $\xi_n \stackrel{\mathrm{a.s.}}{\rightarrow} \xi$. 因函数 $f$ 连续, 有 $f(\xi_n) \stackrel{\mathrm{a.s.}}{\rightarrow} f(\xi)$. 再根据有界收敛定理, 有 $\mathbf{E}f(\xi_n) \to \mathbf{E}f(\xi)$. 此即为 (6.3.1) 式.

“$\Leftarrow$”设(6.3.1)式对于 $\mathbb{R}$ 上的任何有界连续函数 $f$ 成立. 对于 $y < z \in \mathbb{R}$ 可取 $\mathbb{R}$ 上的有界连续函数 $f$ 满足 $1_{(-\infty, y]} \leqslant f \leqslant 1_{(-\infty, z]}$. 于是

$$
F (y) \leqslant \int_ {- \infty} ^ {\infty} f (t) \mathrm{d} F (t) = \lim _ {n \to \infty} \int_ {- \infty} ^ {\infty} f (t) \mathrm{d} F _ {n} (t) \leqslant \operatorname * {l i m i n f} _ {n \to \infty} F _ {n} (z)
$$

和

$$
F (z) \geqslant \int_ {- \infty} ^ {\infty} f (t) \mathrm{d} F (t) = \lim _ {n \to \infty} \int_ {- \infty} ^ {\infty} f (t) \mathrm{d} F _ {n} (t) \geqslant \operatorname * {l i m s u p} _ {n \to \infty} F _ {n} (y).
$$

特别地, 对 $x \in C_F$ 和 $\delta > 0$ 有

$$
F (x - \delta) \leqslant \operatorname * {l i m i n f} _ {n \to \infty} F _ {n} (x) \leqslant \operatorname * {l i m s u p} _ {n \to \infty} F _ {n} (x) \leqslant F (x + \delta)
$$

在上式中令 $\delta \to 0$ 即得

$$
\operatorname * {l i m i n f} _ {n \to \infty} F _ {n} (x) = \operatorname * {l i m s u p} _ {n \to \infty} F _ {n} (x) = F (x),
$$

故知  $F_{n} \xrightarrow{w} F,$

我们知道, 欧氏空间 $(\mathbb{R}^d, \mathcal{B}^d)$ 上的概率测度和其分布函数相互唯一决定. 基于黑利第二定理, 我们可以引入下面的一般性的概念.

定义 6.3.1 设  $\mu,\mu_{1},\mu_{2},\cdots$  为  $(\mathbb{R}^{d},\mathcal{B}^{d})$  上的概率测度. 若对于  $R^{d}$  上的任何有界连续函数 f 都有

$$
\int_ {\mathbb {R} ^ {d}} f (x) \mu_ {n} (\mathrm{d} x) \rightarrow \int_ {\mathbb {R} ^ {d}} f (x) \mu (\mathrm{d} x). \tag {6.3.3}
$$

则称序列  $\{\mu_{n}\}$  弱收敛于  $\mu,$  并记作  $\mu_{n} \stackrel{w}{\rightarrow} \mu.$

显然，对于 $d = 1$ 概率测度的弱收敛 $\mu_{n} \stackrel{\mathrm{w}}{\rightarrow} \mu$ 与相应的概率分布函数的弱收敛 $F_{n} \stackrel{\mathrm{w}}{\rightarrow} F$ 是等价的.

## 6.3.2 莱维连续性定理

我们在本小节将要证明, 概率分布函数与其特征函数之间的对应关系具有某种连续性, 此类结果称为莱维连续性定理.

引理 6.3.4 设概率分布函数  $F, F_{1}, F_{2}, \cdots$  分别有特征函数  $f, f_{1}, f_{2}, \cdots$ . 若  $F_{n} \stackrel{w}{\rightarrow} F$ , 则  $f_{n}$  逐点收敛到函数 f.

证明 假设 $F_{n} \stackrel{\mathrm{w}}{\rightarrow} F$. 因为 $\cos(tx)$ 和 $\sin(tx)$ 都是有界连续函数, 由黑利第二定理, 对任何 $t \in \mathbb{R}$ 有

$$
\begin{array}{l} f _ {n} (t) = \int_ {- \infty} ^ {\infty} \cos (t x) \mathrm{d} F _ {n} (x) + \mathrm{i} \int_ {- \infty} ^ {\infty} \sin (t x) \mathrm{d} F _ {n} (x) \\ \rightarrow \int_ {- \infty} ^ {\infty} \cos (t x) \mathrm{d} F (x) + \mathrm{i} \int_ {- \infty} ^ {\infty} \sin (t x) \mathrm{d} F (x) = f (t), \\ \end{array}
$$

即 $f_{n}$ 逐点收敛到函数 $f$.

定理 6.3.5（莱维连续性定理）设  $\{f_{n}\}$  为概率分布函数序列  $\{F_{n}\}$  的特征函数序列。若  $f_{n}$  逐点收敛到函数 f，且后者在 t=0 处连续，则 f 是某个概率分布函数 F 的特征函数且  $F_{n} \stackrel{w}{\rightarrow} F$ 。

证明 由黑利第一定理, 存在 $\{F_n\}$ 的子序列 $\{F_{n_k}\}$, 使得当 $k \to \infty$ 时 $F_{n_k} \stackrel{\mathrm{w}}{\rightarrow} F$, 其中 $F$ 是 $\mathbb{R}$ 上的右连续不降函数. 显然有 $0 \leqslant F(-\infty) \leqslant F(\infty) \leqslant 1$. 对于 $t > 0$ 有 (这里承认积分和期望可以交换次序)

$$
\begin{array}{l} \frac {1}{2 t} \int_ {- t} ^ {t} f _ {n _ {k}} (s) \mathrm{d} s = \frac {1}{2 t} \int_ {- t} ^ {t} \mathbf {E} (\mathrm{e} ^ {\mathrm{i} s \xi_ {n _ {k}}}) \mathrm{d} s = \frac {1}{2 t} \mathbf {E} \Big (\int_ {- t} ^ {t} \mathrm{e} ^ {\mathrm{i} s \xi_ {n _ {k}}} \mathrm{d} s \Big) \\ = \frac {1}{2 t} \mathbf {E} \Big [ \int_ {- t} ^ {t} \cos (s \xi_ {n _ {k}}) \mathrm{d} s \Big ] = \mathbf {E} \Big [ \frac {\sin (t \xi_ {n _ {k}})}{t \xi_ {n _ {k}}} \Big ], \\ \end{array}
$$

从而

$$
\begin{array}{l} 1 - \frac {1}{2 t} \int_ {- t} ^ {t} f _ {n _ {k}} (s) \mathrm{d} s = \mathbf {E} \left[ 1 - \frac {\sin (t \xi_ {n _ {k}})}{t \xi_ {n _ {k}}} \right] \\ \geqslant \mathbf {E} \Big [ \Big (1 - \frac {1}{| t \xi_ {n _ {k}} |} \Big) 1 _ {\{| t \xi_ {n _ {k}} | \geqslant 2 \}} \Big ] \\ \geqslant \frac {1}{2} \mathbf {P} (| t \xi_ {n _ {k}} | \geqslant 2) \\ \geqslant \frac {1}{2} \big [ \mathbf {P} (t \xi_ {n _ {k}} \leqslant - 2) + \mathbf {P} (t \xi_ {n _ {k}} > 2) \big ] \\ = \frac {1}{2} \big [ F _ {n _ {k}} (- 2 / t) + 1 - F _ {n _ {k}} (2 / t) \big ], \\ \end{array}
$$

故有

$$
F _ {n _ {k}} (2 / t) - F _ {n _ {k}} (- 2 / t) \geqslant \frac {1}{t} \int_ {- t} ^ {t} f _ {n _ {k}} (s) \mathrm{d} s - 1.
$$

由于 $F_{n_k} \stackrel{\mathrm{w}}{\to} F$ 而 $f_{n_k}$ 逐点收敛到 $f$, 限制 $-2 / t, 2 / t \in C_F$, 并对上式应用有界收敛定理有

$$
F (2 / t) - F (- 2 / t) \geqslant \frac {1}{t} \int_ {- t} ^ {t} f (s) \mathrm{d} s - 1 = \int_ {- 1} ^ {1} f (t s) \mathrm{d} s - 1.
$$

因为 $f(0) = \lim_{n\to \infty}f_n(0) = 1$ 且 $f$ 在 $t = 0$ 处连续, 在上式两端令 $t\to 0$ 知 $F(\infty) - F(-\infty) = 1$. 这说明 $F$ 是概率分布函数. 根据引理6.3.4知 $f$ 是 $F$ 的特征函数.

最后, 用反证法证明 $F_{n} \stackrel{\mathrm{w}}{\rightarrow} F$. 假如该结论不成立, 则存在 $x_{0} \in C_{F}$, 使 $F_{n}(x_{0}) \nrightarrow F(x_{0})$. 于是有子列 $\{F_{m_k}\} \subseteq \{F_n\}$ 使 $F_{m_k}(x_0) \to y^* \neq F(x_0)$. 根据前面的证明, 有子列 $\{F_{m_k}^*\} \subseteq \{F_{m_k}\}$ 使 $F_{m_k}^* \stackrel{\mathrm{w}}{\rightarrow}$ 某个概率分布函数 $F^*$. 由前面的证明 $F^*$ 也有特征函数 $f$, 故有 $F^* = F$ 和 $C_{F^*} = C_F \ni x_0$. 这导致 $F_{m_k}(x_0) \to F(x_0) \neq y^*$, 与子列 $\{F_{m_k}\} \subseteq \{F_n\}$ 的取法矛盾.

综合引理 6.3.4 和定理 6.3.5, 我们有

定理 6.3.6（莱维连续性定理） 设概率分布函数 F 和  $F_{n}$  分别有特征函数 f 和  $f_{n}, n=1,2,\cdots$  则  $F_{n}\stackrel{w}{\rightarrow}F$  当且仅当  $f_{n}$  逐点收敛到函数 f.

上面的定理 6.3.5 和定理 6.3.6 给出了莱维连续性定理的两种形式, 它们是概率极限定理研究的重要工具. 这两个定理都可以推广到多维的情况.

## 练习题

1. 设 $F_{n}$ 是指数分布 $E(\lambda_{n})$ 的分布函数且 $F_{n} \stackrel{\mathrm{w}}{\rightarrow} F$. 证明极限 $\lambda_{n} \to \lambda$ 存在且 $F$ 是指数分布 $E(\lambda)$ 的分布函数.

2. 设正态分布函数序列 $\{F_n\}$ 弱收敛到概率分布函数 $F$. 证明:

(1) 极限分布函数 F 也是正态的;

(2) $F_{n}$ 的期望收敛到F的期望;

(3) $F_{n}$ 的方差收敛到F的方差.

3. 设 $g$ 为 $\mathbb{R}$ 上的有界非负连续函数, 而 $G, G_{n}$ 为 $\mathbb{R}$ 上的有界分布函数, $G(-\infty) = G_{n}(-\infty) = 0, n \geqslant 1$. 根据定理4.1.10, 可以定义 $\mathbb{R}$ 上的有界分布函数 $F, F_{n}, n \geqslant 1$ 如下:

$$
F (x) = \int_ {- \infty} ^ {x} g (x) \mathrm{d} G (x), F _ {n} (x) = \int_ {- \infty} ^ {x} g (x) \mathrm{d} G _ {n} (x).
$$

证明: (1) 若 $G_{n} \stackrel{\mathrm{w}}{\to} G$, 则 $F_{n} \stackrel{\mathrm{w}}{\to} F$; (2) 若 $F_{n} \stackrel{\mathrm{w}}{\to} F$ 且 $\inf_{x \in \mathbb{R}} g(x) > 0$, 则 $G_{n} \stackrel{\mathrm{w}}{\to} G$.

提示: 应用定理 4.1.11 和定理 6.3.3.

4. 对 $n \geqslant 1$, 令 $f_n$ 是具有分布密度 $p_n(x) = (2n)^{-1}1_{(-n,n)}(x)$ 的绝对连续型概率分布的特征函数.

(1) 证明 $f_n(t) = \frac{\sin(nt)}{nt}$ (规定 $f_n(0) = 1$);
(2) 说明 $f(t) := \lim_{n \to \infty} f_n(t)$ 是否是某个概率分布的特征函数？

## 本章所讲的随机变量的几种收敛的关系图:

完全收敛 → 几乎必然收敛 ← (斯科罗霍德表示定理)

↓↑(子列) ↑

依概率收敛  $\rightleftharpoons$  依分布收敛
(极限退化)

↑ 立面不舍随意映射，↓↑

依 r 阶平均收敛 特征函数逐点收敛

## 第七章

## 概率极限定理

极限定理的研究在概率论中占有重要的地位, 其内容经常是与随机变量列的部分和有关的收敛性质. 本章介绍独立随机变量列的弱大数定律、强大数定律和中心极限定理. 关于中心极限定理, 我们分别给出了基于特征函数和基于斯坦方程的两种方法. 由大数定律可以推出频率的稳定性, 而中心极限定理则说明在很多情况下随机变量的部分和是渐近正态的. 作为中心极限定理的应用, 还讨论了随机事件对的卡方独立性检验.

## 7.1 大数定律

在大量重复的随机试验中, 随机事件出现的频率呈现几乎必然的规律. 更确切地说, 就是在试验条件不变的情况下, 随机事件在多次重复试验中出现的频率近似于它的概率, 偶然中包含着某种必然! 这个规律就是最早的大数定律. 概率论历史上第一个严格描述这个规律的极限定理属于伯努利. 后来的大数定律通常讨论随机变量序列的算术平均值到相应的数学期望的算术平均值的收敛性.

## 7.1.1 大数定律的定义

假设 $\{\xi_n\}$ 为可积的随机变量序列. 为了叙述方便, 我们定义其部分和 $S_{n}$ 与平均部分和 $\bar{S}_{n}$ 如下:

$$
S _ {n} = \sum_ {k = 1} ^ {n} \xi_ {k}, \quad \bar {S} _ {n} = \frac {1}{n} \sum_ {k = 1} ^ {n} \xi_ {k}. \tag {7.1.1}
$$

定义7.1.1 称序列 $\{\xi_n\}$ 服从（弱）大数定律，是指当 $n\to \infty$ 时有

$$
\bar {S} _ {n} - \mathbf {E} \bar {S} _ {n} = \frac {1}{n} \sum_ {k = 1} ^ {n} (\xi_ {k} - \mathbf {E} \xi_ {k}) \xrightarrow {\mathrm{P}} 0. \tag {7.1.2}
$$

根据定义, 大数定律是指当 $n \to \infty$ 时平均部分和 $\bar{S}_n$ 与其数学期望有较大偏差的概率会趋近于零. 显然, 序列 $\{\xi_n\}$ 和 $\{\xi_n - \mathbf{E}\xi_n\}$ 同时满足或不满足大数定律.

特别地, 若 $\{\xi_n\}$ 为同分布随机变量序列, 则 (7.1.2) 式等价于

$$
\bar {S} _ {n} = \frac {1}{n} \sum_ {k = 1} ^ {n} \xi_ {k} \xrightarrow {\mathrm{p}} \mathbf {E} \xi_ {1}. \tag {7.1.3}
$$

## 7.1.2 马尔可夫大数定律

证明 (弱) 大数定律常用的工具是马尔可夫不等式及其如下的特例: 对于任何平方可积随机变量 $\xi$ 及 $\varepsilon > 0$ 有

$$
\mathbf {P} (| \xi - \mathbf {E} \xi | \geqslant \varepsilon) \leqslant \frac {1}{\varepsilon^ {2}} \mathbf {V a r} \xi . \tag {7.1.4}
$$

上式称为切比雪夫 (Chebyshev) 不等式. 由此易证下面的定理.

定理 7.1.1（马尔可夫大数定律）设  $\{\xi_{n}\}$  为平方可积随机变量序列. 则对于任意的  $\varepsilon > 0$  有

$$
\mathbf {P} \big (| \bar {S} _ {n} - \mathbf {E} \bar {S} _ {n} | \geqslant \varepsilon \big) \leqslant \frac {1}{\varepsilon^ {2}} \mathbf {V a r} (\bar {S} _ {n}) = \frac {1}{n ^ {2} \varepsilon^ {2}} \mathbf {V a r} (S _ {n}).
$$

特别地, 若当 $n \to \infty$ 时有 $\mathbf{Var}(\bar{S}_n) = \mathbf{Var}(S_n)/n^2 \to 0$, 则序列 $\{\xi_n\}$ 满足大数定律 (7.1.2).

推论 7.1.2 (切比雪夫大数定律) 若  $\{\xi_{n}\}$  两两不相关且方差有界, 即有常数  $C \geqslant 0$  使得  $\mathrm{Var}(\xi_{n}) \leqslant C, n = 1, 2, \cdots$ , 则  $\{\xi_{n}\}$  满足大数定律 (7.1.2).

证明 只需注意, 在假设条件下有 $\mathbf{Var}(S_n) = \sum_{k=1}^{n} \mathbf{Var}(\xi_k) \leqslant nC$. 故定理 7.1.1 的条件显然满足. □

推论7.1.3(伯努利大数定律) 假设 $0 < p < 1$. 令 $S_{n}$ 是以 $p$ 为成功概率的伯努利试验前 $n$ 次试验中的成功次数. 则对于任意的 $\varepsilon > 0$ 有

$$
\mathbf {P} \Big (\Big | \frac {S _ {n}}{n} - p \Big | \geqslant \varepsilon \Big) \leqslant \frac {1}{n ^ {2} \varepsilon^ {2}} \mathbf {V a r} (S _ {n}) = \frac {1}{n \varepsilon^ {2}} p (1 - p).
$$

故当  $n \to \infty$  时有  $\bar{S}_{n} := S_{n}/n \xrightarrow{P} p.$

证明 注意 $S_{n} = \sum_{k=1}^{n} \xi_{k}$, 其中 $\xi_{k}$ 表示第 $k$ 次试验中的成功次数. 显然 $\{\xi_{k}\}$ 为独立同分布的随机变量序列且

$$
\mathbf {P} (\xi_ {k} = 1) = p, \quad \mathbf {P} (\xi_ {k} = 0) = 1 - p.
$$

所以

$$
\mathbf {E} (\xi_ {k}) = p, \quad \mathbf {V a r} (\xi_ {k}) = p (1 - p),
$$

进而 $\mathbf{Var}(S_n) = \sum_{k=1}^{n} \mathbf{Var}(\xi_k) = np(1-p)$. 根据推论 7.1.2 即得结论.

例 7.1.1 根据推论 7.1.3, 对于独立重复试验, 当试验次数 n 很大时, 某个随机事件 A 发生的频率与其概率值  $\mathbf{P}(A)$  出现较大偏差的概率很小. 这就基于大数定律给出了频率的稳定性的严格数学解释. 该案例体现了抽象数学理论在认识客观现象和指导实践活动中的作用. 特别地, 在例 1.1.1 的掷硬币试验中, 当投掷次数 n 很大时, 正面出现的频率  $S_{n}/n$  与其概率值 1/2 发生较大偏差的情况很少出现, 与我们的直观经验相吻合.