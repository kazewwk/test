# 第八章 连续时间马氏过程

原始 PDF 第 190–217 页。

194

第八章 连续时间马氏过程

在本章中, 我们对连续时间的马氏过程的基本概念和性质做简单的介绍, 主要内容包括转移半群、马氏性、强马氏性、费勒半群和费勒过程、卷积半群、莱维过程、强费勒性以及若干典型的例子等.

## 8.1 马氏转移半群

研究马氏过程的基本工具是转移半群, 它给出了过程的某种条件分布. 利用转移半群可以对马氏过程的若干基本分布给出简洁的表达. 本节讨论与转移半群相关的若干基本概念, 并简单介绍欧氏空间上的卷积半群.

## 8.1.1 转移核与半群

考虑可测空间 $(E, \mathcal{E})$. 严格来说, 后面涉及的积分都是指抽象测度的积分. 对该理论不熟悉的读者可假定 $(E, \mathcal{E})$ 是欧氏空间 $(\mathbb{R}^d, \mathcal{B}^d)$ 的可测子空间, 并将这里关于测度的积分理解为关于相应分布函数的斯蒂尔切斯积分. 用 $\mathrm{b}\mathcal{E}$ 表示 $E$ 上的全体关于 $\mathcal{E}$ 可测的有界函数构成的线性空间. 对于 $f \in \mathrm{b}\mathcal{E}$ 定义其上确界范数:

$$
\| f \| = \sup _ {x \in E} | f (x) |. \tag {8.1.1}
$$

注意 b$\mathcal{E}$ 在范数 $\|\cdot\|$ 之下是完备的, 因此是巴拿赫 (Banach) 空间.

定义 8.1.1 设  $(E, \mathcal{E})$  和  $(F, \mathcal{F})$  是两个可测空间. 称映射  $K: E \times F \to [0, \infty)$  为由  $(E, \mathcal{E})$  到  $(F, \mathcal{F})$  上的转移核, 是指它满足如下条件:

(1) 当 $B \in \mathcal{F}$ 固定时, $x \mapsto K(x, B)$ 是 $(E, \mathcal{E})$ 上的可测函数;
(2) 当 $x \in E$ 固定时, $B \mapsto K(x, B)$ 是 $(F, \mathscr{F})$ 上的有限测度.

称转移核 $K$ 是有界的, 是指它在 $E \times \mathcal{F}$ 上有界. 特别地, 当 $K(\cdot, F) \equiv 1$ 时称 $K$ 是马氏转移核; 当 $K(\cdot, F) \leqslant 1$ 时称 $K$ 是准马氏转移核; 当 $E = F$ 且 $\mathcal{E} = \mathcal{F}$ 时称 $K$ 是 $(E, \mathcal{E})$ 或 $E$ 上的转移核.

核与函数空间上的线性算子之间有密切的联系. 设 $K$ 是 $(E, \mathcal{E})$ 到 $(F, \mathcal{F})$ 的有界核. 对于 $f \in \mathrm{b}\mathcal{F}$, 令

$$
K f (x) = \int_ {F} f (y) K (x, \mathrm{d} y), \quad x \in E.
$$

易知 $Kf \in \mathrm{b}\mathcal{E}$, 且 $f \mapsto Kf$ 是由线性空间 $\mathrm{b}\mathcal{F}$ 到线性空间 $\mathrm{b}\mathcal{E}$ 的线性算子. 显然该线性算子与核 $K$ 相互唯一决定. 对于 $(E, \mathcal{E})$ 上的有限测度 $\mu$ 令

$$
\mu K (B) = \int_ {E} K (x, B) \mu (\mathrm{d} x), \quad B \in \mathcal {F}.
$$

---

8.1 马氏转移半群

195

则 $\mu K$ 是 $(F, \mathcal{F})$ 上的有限测度. 因此 $K$ 诱导一个将 $(E, \mathcal{E})$ 上的有限测度映至 $(F, \mathcal{F})$ 上的有限测度的算子. 显然当 $K$ 是马氏转移核时, 它将概率测度映为概率测度.

设 $K$ 和 $L$ 分别是可测空间 $(E, \mathcal{E})$ 到 $(F, \mathcal{F})$ 和 $(F, \mathcal{F})$ 到 $(G, \mathcal{G})$ 的有界核. 对 $x \in E$ 和 $A \in \mathcal{G}$ 定义

$$
K L (x, A) = \int_ {F} K (x, \mathrm{d} y) L (y, A).
$$

则 $KL$ 是一个 $(E, \mathcal{E})$ 到 $(G, \mathcal{G})$ 的有界核, 称为 $K$ 与 $L$ 的复合. 显然有

$$
K (L f) = (K L) f, \quad (\mu K) L = \mu (K L).
$$

所以今后遇到上述运算时, 我们简写作 KLf 或  $\mu KL$ .

定义 8.1.2 称  $(E, \mathcal{E})$  上的一族准马氏转移核  $(P_{t})_{t \geqslant 0}$  为转移半群, 是指  $P_{0}(x, \cdot) = \delta_{x}$  且对任意  $s, t \geqslant 0$ , 有  $P_{s}P_{t} = P_{s+t}$ , 这等价于

$$
P _ {t + s} (x, B) = \int_ {E} P _ {s} (x, \mathrm{d} y) P _ {t} (y, B), \quad x \in E, B \in \mathscr {E}.
$$

上式称为查普曼-柯尔莫哥洛夫方程.

根据上面的说明, 转移半群 $(P_{t})_{t\geqslant 0}$ 决定了巴拿赫空间 $\mathrm{b}\mathcal{E}$ 的一族线性算子 $(P_{t})_{t\geqslant 0}$. 显然在算子运算之下 $(P_{t})_{t\geqslant 0}$ 仍然构成一个半群. 由于 $P_{t}$ 是准马氏转移核, 易知

$$
\| P _ {t} f \| \leqslant \| f \|, \quad f \in \mathrm{b} \mathscr {E}. \tag {8.1.2}
$$

所以  $(P_{t})_{t\geqslant0}$  是 bE 上的压缩线性算子半群.

称转移半群 $(P_{t})_{t\geqslant 0}$ 是可测的, 是指对于任何 $f\in \mathrm{b}\mathcal{E}$ 映射 $(t,x)\mapsto P_t f(x)$ 关于乘积 $\sigma$ 代数 $\mathcal{B}[0,\infty)\times \mathcal{E}$ 可测. 此时, 令

$$
U ^ {\alpha} f (x) = \int_ {0} ^ {\infty} \mathrm{e} ^ {- \alpha t} P _ {t} f (x) \mathrm{d} t, \quad x \in E, \tag {8.1.3}
$$

称 $U^{\alpha}$ 为 $(P_t)_{t\geqslant 0}$ 的 $\alpha$ 位势算子, 而称 $(U^{\alpha})_{\alpha >0}$ 为 $(P_t)_{t\geqslant 0}$ 的预解式. 易证下面的预解方程

$$
U ^ {\beta} f (x) = U ^ {\alpha} f (x) - (\beta - \alpha) U ^ {\alpha} U ^ {\beta} f (x), \quad \alpha , \beta > 0. \tag {8.1.4}
$$

例 8.1.1 对于  $t \geqslant 0$  令  $R_{t}(x, \mathrm{d}y) = \delta_{x+t}(\mathrm{d}y)$ ，则  $(R_{t})_{t \geqslant 0}$  构成 R 上的马氏转移半群，也可限定为  $R_{+}$ 上的马氏转移半群，或者限定为  $\mathbb{R}_{-} := (-\infty, 0]$  上的准马氏转移半群.

例 8.1.2 对于  $t \geqslant 0$  令  $Q_{t}(x, \mathrm{d}y) = \delta_{x + \operatorname{sgn}(x)t}(\mathrm{d}y)$ ，则  $(R_{t})_{t \geqslant 0}$  构成 R 上的马氏转移半群，也可限定为  $R_{+} := [0, \infty)$  上的马氏转移半群.

---

196

第八章 连续时间马氏过程

例8.1.3 设 $\pi$ 为可测空间 $(E, \mathcal{E})$ 上的马氏转移核. 记 $\pi^0(x, \mathrm{dy}) = \delta_x(\mathrm{dy})$, 并对 $n \geqslant 1$ 令 $\pi^n$ 是 $\pi$ 的 $n$ 重复合. 再设 $\alpha \geqslant 0$ 为常数. 对于 $t \geqslant 0$ 利用泊松分布定义 $(E, \mathcal{E})$ 上的转移核

$$
P _ {t} (x, \mathrm{d} y) = \mathrm{e} ^ {- \alpha t} \sum_ {n = 0} ^ {\infty} \frac {(\alpha t) ^ {n}}{n !} \pi^ {n} (x, \mathrm{d} y).
$$

易证 $(P_{t})_{t\geqslant0}$ 构成 $(E,\mathscr{E})$ 上的马氏转移半群.

考虑 $(E, \mathcal{E})$ 上的准马氏转移半群 $(P_t)_{t \geqslant 0}$. 对于 $\partial \notin E$ 令 $\tilde{E} = E \cup \{\partial\}$. 再令 $\tilde{\mathcal{E}}$ 为 $\tilde{E}$ 上的由 $\mathcal{E}$ 和 $\{\partial\}$ 生成的 $\sigma$ 代数. 不难证明 $\tilde{\mathcal{E}} = \mathcal{E} \cup \{B \cup \{\partial\} : B \in \mathcal{E}\}$. 则对于 $t \geqslant 0$ 存在 $(\tilde{E}, \tilde{\mathcal{E}})$ 上唯一的马氏转移核 $\tilde{P}_t$ 满足

$$
\tilde {P} _ {t} (x, A) = \left\{ \begin{array}{l l} P _ {t} (x, A), & x \in E, A \in \mathscr {E}, \\ 1 - P _ {t} (x, E), & x \in E, A = \{\partial \}, \\ \delta_ {\partial} (A), & x = \partial , A \in \tilde {\mathscr {E}}. \end{array} \right. \tag {8.1.5}
$$

易证 $(\tilde{P}_t)_{t\geqslant 0}$ 构成 $(\tilde{E},\tilde{\mathcal{E}})$ 上的马氏转移半群. 所以, 任何一个准马氏转移半群总可扩张为马氏转移半群.

命题 8.1.1 设 E 为度量拓扑空间, 而 E 为其博雷尔  $\sigma$  代数. 再设  $\mu$  和  $\nu$  是  $(E, \mathcal{E})$  上的有限测度, 则  $\mu = \nu$  当且仅当有

$$
\int_ {E} f (x) \mu (\mathrm{d} x) = \int_ {E} f (x) \nu (\mathrm{d} x), \quad f \in C _ {b} (E), \tag {8.1.6}
$$

其中  $C_{b}(E)$  表示 E 上的有界连续函数的全体.

证明 若有 $\mu = \nu$，则显然 (8.1.6) 式成立。反之，设 (8.1.6) 式成立。任取开集 $G \subseteq E$。对 $x \in E$ 令 $g(x) = \inf \{\rho(x, y) : y \in G^c\}$。易证 $g$ 为 $E$ 上的连续函数，且当 $x \in G$ 时有 $g(x) > 0$，而当 $x \in G^c$ 时有 $g(x) = 0$。对 $n \geqslant 1$ 令 $f_n = 1 \wedge (ng)$。显然 $f_n \in C_b(E)$，故 (8.1.6) 式中的等式对每个 $f_n$ 成立。注意，在逐点收敛的意义下单调不降地 $\lim_{n \to \infty} f_n = 1_G$。根据单调收敛定理有 $\mu(G) = \nu(G)$，再由邓肯类定理知 $\mu(A) = \nu(A)$ 对一切 $A \in \mathcal{E}$ 成立。$\square$

## 8.1.2 费勒转移半群

本小节假定 $E$ 是可分局部紧度量空间, 其典型的特例包括欧氏空间 $\mathbb{R}^d$ 及其各种类型的区间. 对此概念不熟悉的读者可假定 $E$ 是 $\mathbb{R}^d$ 或其中的某个区间. 令 $\mathcal{E}$ 为 $E$ 的博雷尔 $\sigma$ 代数, 即由 $E$ 的所有开集生成的 $\sigma$ 代数. 令 $\tilde{E} = E \cup \{\infty\}$ 是 $E$ 的单点紧化空间. 也就是说, 点 $\infty$ 的邻域系就是 $E$ 的所有紧子集在 $\tilde{E}$ 中的补集. 这样 $\tilde{E}$ 是一个

---

8.1 马氏转移半群

197

紧度量空间, 取其上的一个度量 $\rho$. 令 $C_0(E)$ 是由 $E$ 上的满足 $\lim_{x \to \infty} f(x) = 0$ 的连续函数 $f$ 构成的线性空间. 注意, 在 (8.1.1) 式定义的上确界范数 $\|\cdot\|$ 之下 $C_0(E)$ 是巴拿赫空间 $\mathrm{b}\mathcal{E}$ 的闭线性子空间, 故它也是巴拿赫空间.

命题 8.1.2 设  $\mu$  和  $\nu$  是  $(E, \mathcal{E})$  上的有限测度, 则  $\mu = \nu$  当且仅当有

$$
\int_ {E} f (x) \mu (\mathrm{d} x) = \int_ {E} f (x) \nu (\mathrm{d} x), \quad f \in C _ {0} (E). \tag {8.1.7}
$$

证明 若有 $\mu = \nu$, 则显然 (8.1.7) 式成立. 反之, 设 (8.1.7) 式成立. 下证 (8.1.6) 式成立. 令 $\tilde{E} = E \cup \{\infty\}$ 是 $E$ 的单点紧化空间, 并取其上的一个度量 $\rho$. 注意, 对任何 $x \in E$ 有 $h(x) := \rho(x, \infty) > 0$, 并且 $h \in C_0(E)$. 对 $n \geqslant 1$ 令 $h_n = 1 \wedge (nh)$. 则当 $f \in C_b(E)$ 时有 $f_n := f h_n \in C_0(E)$, 故 (8.1.7) 式中的等式对 $f_n$ 成立. 因为 $\lim_{n \to \infty} f_n = f$, 由控制收敛定理知 (8.1.6) 式成立. 再根据命题 8.1.1 有 $\mu = \nu$. □

定义 8.1.3 称  $(E, \mathcal{E})$  上的马氏转移半群  $(P_{t})_{t \geqslant 0}$  为费勒半群, 是指下面的两个性质成立:

(1) 对任意的 $t \geqslant 0$ 和 $f \in C_0(E)$, 有 $P_t f \in C_0(E)$;
(2) 对任意的 $x \in E$ 和 $f \in C_0(E)$, 有 $\lim_{t \to 0} P_t f(x) = f(x)$.

显然, 费勒半群  $(P_{t})_{t\geqslant0}$  是可测半群. 令  $(U^{\alpha})_{\alpha>0}$  是由 (8.1.3) 式定义的预解式.

命题 8.1.3 对  $\alpha > 0$ , 记  $\mathcal{D} := U^{\alpha} C_{0}(E)$ , 则 D 为  $C_{0}(E)$  的稠密线性子空间且不依赖于常数  $\alpha$  的选择.

证明 首先, 我们证明对 $\alpha > 0$ 和 $f \in C_0(E)$, 有 $U^\alpha f \in C_0(E)$. 由于 $P_t f \in C_0(E)$, 根据有界收敛定理, 当 $x \to x_0 \in E$ 时有

$$
U ^ {\alpha} f (x) = \int_ {0} ^ {\infty} \mathrm{e} ^ {- \alpha t} P _ {t} f (x) \mathrm{d} t \rightarrow \int_ {0} ^ {\infty} \mathrm{e} ^ {- \alpha t} P _ {t} f (x _ {0}) \mathrm{d} t = U ^ {\alpha} f (x _ {0}).
$$

类似地, 当 $x \to \infty$ 时有 $U^{\alpha}f(x) \to 0$. 这就证明了 $U^{\alpha}f \in C_0(E)$, 故 $\mathcal{D}$ 为 $C_0(E)$ 的线性子空间. 从预解方程不难看出 $\mathcal{D}$ 与 $\alpha$ 的选择无关. 下证 $\mathcal{D}$ 在 $C_0(E)$ 中稠密. 否则, 存在 $g \in C_0(E)$ 满足 $\inf_{f \in \mathcal{D}} \|f - g\| > 0$. 根据哈恩-巴拿赫 (Hahn-Banach) 定理, 存在 $C_0(E)$ 上的有界线性泛函 $\phi$ 使 $\phi(g) \neq 0$, 同时对任意 $f \in \mathcal{D}$ 有 $\phi(f) = 0$, 参见 [17, p.214]. 利用里斯 (Riesz) 表示定理, 有 $(E, \mathcal{E})$ 上的有限符号测度 $\mu$ 使得

$$
\phi (f) = \int_ {E} f (x) \mu (\mathrm{d} x), \quad f \in C _ {0} (E),
$$

参见 [7, p.75]. 由于 $\alpha U^{\alpha}g\in \mathcal{D}$, 我们有

$$
0 = \phi (\alpha U ^ {\alpha} g) = \int_ {E} \alpha U ^ {\alpha} g (x) \mu (\mathrm{d} x) = \int_ {E} \mu (\mathrm{d} x) \int_ {0} ^ {\infty} \mathrm{e} ^ {- s} P _ {s / \alpha} g (x) \mathrm{d} s.
$$

在上式中令  $\alpha \rightarrow \infty$ ，利用有界收敛定理和定义 8.1.3 中的性质 (2) 得

$$
0 = \int_ {\mathbb {R} ^ {d}} g (x) \mu (\mathrm{d} x) = \phi (g),
$$

---

198

第八章 连续时间马氏过程

而这与 $\phi$ 的取法矛盾. 故 $\mathcal{D}$ 在 $C_0(E)$ 中稠密. $\square$

定理8.1.4 对任何 $f \in C_0(E)$ 有 $\lim_{t \to 0} \|P_t f - f\| = 0$.

证明 由命题8.1.3知 $\mathcal{D} := U^{\alpha} C_0(E)$ 在 $C_0(E)$ 中稠密. 对于 $t, \alpha > 0$ 和 $g \in C_0(E)$ 有

$$
\begin{array}{l} P _ {t} U ^ {\alpha} g (x) - U ^ {\alpha} g (x) = \int_ {0} ^ {\infty} \mathrm{e} ^ {- \alpha s} P _ {t + s} g (x) \mathrm{d} s - \int_ {0} ^ {\infty} \mathrm{e} ^ {- \alpha s} P _ {s} g (x) \mathrm{d} s \\ = \int_ {t} ^ {\infty} \mathrm{e} ^ {- \alpha (s - t)} P _ {s} g (x) \mathrm{d} s - \int_ {0} ^ {\infty} \mathrm{e} ^ {- \alpha s} P _ {s} g (x) \mathrm{d} s \\ = (\mathrm{e} ^ {\alpha t} - 1) \int_ {t} ^ {\infty} \mathrm{e} ^ {- \alpha s} P _ {s} g (x) \mathrm{d} s - \int_ {0} ^ {t} \mathrm{e} ^ {- \alpha s} P _ {s} g (x) \mathrm{d} s. \\ \end{array}
$$

显然, 当 $t \to 0$ 时上式在上确界范数下趋于零. 所以对 $f \in \mathcal{D}$ 有 $\lim_{t \to 0} \|P_t f - f\| = 0$. 再由 $\mathcal{D}$ 在 $C_0(E)$ 中的稠密性和算子 $P_t$ 的压缩性易得欲证结论. $\square$

推论 8.1.5 映射  $(s, x, f) \mapsto P_{s}f(x)$  在  $[0, \infty) \times E \times C_{0}(E)$  上连续.

证明 对于 $[0, \infty) \times E \times C_0(E)$ 中的 $(s, x, f)$ 和 $(t, y, g)$ 有

$$
\begin{array}{l} | P _ {s} f (x) - P _ {t} g (y) | \leqslant | P _ {s} f (x) - P _ {s} g (x) | + | P _ {s} g (x) - P _ {t} g (x) | + \\ | P _ {t} g (x) - P _ {t} g (y) | \\ \leqslant | P _ {s} (f - g) (x) | + P _ {s \wedge t} | P _ {| t - s |} g - g | (x) + \\ \left| P _ {t} g (x) - P _ {t} g (y) \right| \\ \leqslant \| f - g \| + \| P _ {| t - s |} g - g \| + | P _ {t} g (x) - P _ {t} g (y) |. \\ \end{array}
$$

由定理 8.1.4, 上式右端当  $(s, x, f) \rightarrow (t, y, g)$  时趋于零. □

定理 8.1.4 所建立的性质称为费勒半群  $(P_{t})$  的强连续性. 费勒半群  $(P_{t})$  将  $C_{0}(E)$  中的函数映射到  $C_{0}(E)$  的函数. 由此可以推出  $(P_{t})$  将 E 上的有界连续函数映成有界连续函数. 有些半群具有更好的分析性质, 即对 t > 0 算子  $P_{t}$  将 E 上的有界可测函数映成有界连续函数, 此时我们说  $(P_{t})$  满足强费勒性.

例 8.1.4 对于  $t \geqslant 0$  和  $x \in R$  令  $P_{t}(x, \cdot)$  为正态分布  $N(x, t)$  的分布密度. 特别地, 当 t > 0 时有

$$
P _ {t} f (x) = \int_ {\mathbb {R}} f (x + z) p (t, z) \mathrm{d} z, \quad f \in C _ {0} (\mathbb {R}), \tag {8.1.8}
$$

其中

$$
p (t, z) = \frac {1}{\sqrt {2 \pi t}} \mathrm{e} ^ {- z ^ {2} / 2 t}.
$$

易证 $(P_{t})_{t\geqslant0}$ 为R上的费勒转移半群.此外,不难验证

$$
\partial_ {t} p (t, x) = \frac {1}{2 t} \Big (\frac {x ^ {2}}{t} - 1 \Big) p (t, x) = \frac {1}{2} \partial_ {x x} p (t, x).
$$

---

8.1 马氏转移半群

199

令 $C_0^2 (\mathbb{R})$ 为 $C_0(\mathbb{R})$ 中具有连续的一阶和二阶导数且这些导数均属于 $C_0(\mathbb{R})$ 的函数的全体. 基于上式和(8.1.8)式可以证明, 当 $f\in C_0^2 (\mathbb{R})$ 时有

$$
\partial_ {t} P _ {t} f (x) = \frac {1}{2} \partial_ {x x} P _ {t} f (x) = \frac {1}{2} P _ {t} \partial_ {x x} f (x). \tag {8.1.9}
$$

特别地, 函数  $u(t,x):=P_{t}f(x)$  满足下面的热方程:

$$
\partial_ {t} u (t, x) = \frac {1}{2} \partial_ {x x} u (t, x). \tag {8.1.10}
$$

由于这样的缘故, 上面定义的转移半群 $(P_{t})$ 也称为热半群. 利用控制收敛定理可以证明, 该半群具有强费勒性.

例 8.1.5 用  $\mathcal{B}_{++}$  表示  $\mathbb{R}_{++} = (0, \infty)$  上的博雷尔  $\sigma$  代数. 给定常数  $a \geqslant 0$  可以定义  $(\mathbb{R}_{++}, \mathcal{B}_{++})$  上的准马氏转移半群  $(P_{t}^{\circ})$  如下: 对  $x \in R_{++}$  和  $f \in bB_{++}$ ,

$$
P _ {t} ^ {\circ} f (x) = \frac {1}{\sqrt {2 \pi a t}} \int_ {\mathbb {R} _ {+ +}} f (y) [ \mathrm{e} ^ {- (y - x) ^ {2} / 2 a t} - \mathrm{e} ^ {- (y + x) ^ {2} / 2 a t} ] \mathrm{d} y.
$$

它可以自然地扩张为  $\mathbb{R}_{+}=[0,\infty)$  上的费勒马氏转移半群.

## 8.1.3 无穷可分分布

称欧氏可测空间 $(\mathbb{R},\mathcal{B})$ 上的概率分布 $\mu$ 是无穷可分的, 是指对任意的整数 $n \geqslant 1$ 都有概率测度 $\mu_{n}$, 使得

$$
\mu = \mu_ {n} * \dots * \mu_ {n} \quad (n \text {重卷积}). \tag {8.1.11}
$$

此时称  $\mu_{n}$  为  $\mu$  的 n 次方根.

设 $\sigma^2 \geqslant 0$ 和 $\beta$ 为实常数而 $(1 \wedge z^2)\nu(\mathrm{d}z)$ 为 $\mathbb{R} \setminus \{0\}$ 上的有限测度. 基于三元组 $(\beta, \sigma^2, \nu)$ 可以定义 $\mathbb{R}$ 上的连续复数值函数

$$
\psi (\lambda) = \mathrm{i} \beta \lambda - \frac {\sigma^ {2}}{2} \lambda^ {2} + \int_ {\mathbb {R} \backslash \{0 \}} \left(\mathrm{e} ^ {\mathrm{i} \lambda z} - 1 - \frac {\mathrm{i} \lambda z}{1 + z ^ {2}}\right) \nu (\mathrm{d} z). \tag {8.1.12}
$$

此表达式称为莱维-辛钦 (Lévy-Khintchine) 表示.

我们经常用到莱维-辛钦公式另一种形式. 对于每个 $\lambda \in \mathbb{R}$ 可以定义 $\mathbb{R}$ 上的有界连续复函数 $K(\lambda, \cdot)$ 如下: 令 $K(\lambda, 0) = -\lambda^2 / 2$ 并对 $z \neq 0$ 令

$$
K (\lambda , z) = \Bigl (\mathrm{e} ^ {\mathrm{i} \lambda z} - 1 - \frac {\mathrm{i} \lambda z}{1 + z ^ {2}} \Bigr) \frac {1 + z ^ {2}}{z ^ {2}}.
$$

再定义 $\mathbb{R}$ 上的有限测度 $G(\mathrm{d}z)$: 令 $G(\{0\}) = \sigma^2$ 和

$$
1 _ {\{z \neq 0 \}} G (\mathrm{d} z) = \Bigl (\frac {z ^ {2}}{1 + z ^ {2}} \Bigr) \nu (\mathrm{d} z), \quad z \in \mathbb {R}.
$$

---

200

第八章 连续时间马氏过程

则可将 (8.1.12) 式等价地写作

$$
\psi (\lambda) = \mathrm{i} \beta \lambda + \int_ {\mathbb {R}} K (\lambda , z) G (\mathrm{d} z), \quad \lambda \in \mathbb {R}. \tag {8.1.13}
$$

命题 8.1.6 设  $\{\psi_{n}\}$  是具有形如 (8.1.12) 式或 (8.1.13) 式的表达式的函数列. 若当  $n \to \infty$  时  $\psi_{n}$  局部一致地收敛到函数  $\psi$ , 则后者也具有形如 (8.1.12) 式或 (8.1.13) 式的表达式.

证明 不妨设 $\psi_{n}$ 可通过 $(\beta_{n}, G_{n})$ 表达为 (8.1.13) 式的形式. 不难发现

$$
V _ {n} (\lambda) := 2 \psi_ {n} (\lambda) - \int_ {\lambda - 1} ^ {\lambda + 1} \psi_ {n} (s) \mathrm{d} s = \int_ {\mathbb {R}} \mathrm{e} ^ {\mathrm{i} \lambda z} H _ {n} (\mathrm{d} z),
$$

其中

$$
H _ {n} (\mathrm{d} z) = 2 \Big (1 - \frac {\sin z}{z} \Big) \frac {1 + z ^ {2}}{z ^ {2}} G _ {n} (\mathrm{d} z).
$$

在假设条件下, 当  $n \rightarrow \infty$  时局部一致地有

$$
V _ {n} (\lambda) \rightarrow V (\lambda) := 2 \psi (\lambda) - \int_ {\lambda - 1} ^ {\lambda + 1} \psi (s) \mathrm{d} s.
$$

根据莱维连续性定理易知 $V$ 是 $\mathbb{R}$ 上的某个有限测度 $H$ 的特征函数且 $H_{n} \stackrel{\mathrm{w}}{\rightarrow} H$. 显然存在常数 $c_{1} > c_{0} > 0$ 使得

$$
c _ {0} \leqslant \Big (1 - \frac {\sin z}{z} \Big) \frac {1 + z ^ {2}}{z ^ {2}} \leqslant c _ {1}, \quad z \in \mathbb {R}.
$$

因此有 $G_{n}\stackrel{\mathrm{w}}{\rightarrow}G$ ，其中

$$
G (\mathrm{d} z) = \frac {1}{2} \bigg (1 - \frac {\sin z}{z} \bigg) ^ {- 1} \frac {z ^ {2}}{1 + z ^ {2}} H (\mathrm{d} z).
$$

于是有

$$
\lim _ {n \to \infty} \int_ {\mathbb {R}} K (\lambda , z) G _ {n} (\mathrm{d} z) = \int_ {\mathbb {R}} K (\lambda , z) G (\mathrm{d} z).
$$

注意

$$
\beta_ {n} = \mathrm{i} \Big [ \int_ {\mathbb {R}} K (1, z) G _ {n} (\mathrm{d} z) - \psi_ {n} (1) \Big ].
$$

所以极限 $\beta := \lim_{n\to \infty}\beta_n$ 存在，故 $\psi$ 有表达式 (8.1.13). 等价地，它也有表达式(8.1.12). □

命题 8.1.7 设  $\psi$  由 (8.1.12) 式或 (8.1.13) 式给出, 则  $\phi = e^{\psi}$  是 R 上的某个无穷可分概率分布  $\mu$  的特征函数.

---

8.1 马氏转移半群

201

证明 由关于复合泊松过程的结果, 对任意的 $k \geqslant 1$ 存在 $\mathbb{R}$ 上的概率分布 $m_k$ 有特征函数 $\hat{m}_k(\lambda) = \mathrm{e}^{\rho_k(\lambda)}$, 其中

$$
\rho_ {k} (\lambda) = \int_ {\{| z | > 1 / k \}} (\mathrm{e} ^ {\mathrm{i} \lambda z} - 1) \nu (\mathrm{d} z).
$$

事实上, 若  $N(\mathrm{d}z)$  是以  $\nu(\mathrm{d}z)$  为强度的泊松随机测度, 则随机变量

$$
\xi_ {k} := \int_ {\{| z | > 1 / k \}} z N (\mathrm{d} z)
$$

就有分布  $m_{k}$ . 记  $\gamma := N(0, \sigma^{2})$  和

$$
\beta_ {k} = \beta - \int_ {\{| z | > 1 / k \}} \Big (\frac {z}{1 + z ^ {2}} \Big) \nu (\mathrm{d} z).
$$

则概率分布  $\eta_{k}:=\delta_{\beta_{k}}*\gamma*m_{k}$  有特征函数  $\hat{\eta}_{k}(\lambda)=\mathrm{e}^{\psi_{k}(\lambda)}$ ，其中

$$
\psi_ {k} (\lambda) = \mathrm{i} \beta \lambda - \frac {\sigma^ {2}}{2} \lambda^ {2} + \int_ {\{| z | > 1 / k \}} \Big (\mathrm{e} ^ {\mathrm{i} \lambda z} - 1 - \frac {\mathrm{i} \lambda z}{1 + z ^ {2}} \Big) \nu (\mathrm{d} z).
$$

注意, 当 $k \to \infty$ 时在 $\mathbb{R}$ 上有 $\hat{\eta}_k \to \phi = \mathrm{e}^{\psi}$. 利用 (8.1.13) 式和有界收敛定理不难看出 $\phi$ 在 $\mathbb{R}$ 上连续. 再由莱维连续性定理知 $\phi$ 是 $\mathbb{R}$ 上的某个概率分布 $\mu$ 的特征函数. 类似地, 对于 $n \geqslant 1$ 可知 $\phi_n := \mathrm{e}^{\psi / n}$ 是 $\mathbb{R}$ 上的某个概率分布 $\mu_n$ 的特征函数. 显然 (8.1.11) 式成立. 所以 $\mu$ 是无穷可分的. $\square$

定理 8.1.8 欧氏空间 R 上的概率分布  $\mu$  是无穷可分的当且仅当它有特征函数  $\hat{\mu} = e^{\psi}$ ，其中  $\psi$  有表达式 (8.1.12) 或 (8.1.13).

证明 若概率分布 $\mu$ 有特征函数 $\hat{\mu} = \mathrm{e}^{\psi}$, 其中 $\psi$ 有表达式 (8.1.12) 或 (8.1.13), 由命题 8.1.7 知它是无穷可分的. 反之, 设 $\mu$ 是 $\mathbb{R}$ 上的无穷可分分布, 则其特征函数 $\hat{\mu}$ 在 $\mathbb{R}$ 上无零点; 参见 [31, p.32, Lemma 7.5], 故可写 $\hat{\mu} = \mathrm{e}^{\psi}$, 其中 $\psi = \ln \hat{\mu}$. 令 $\mu_{n}$ 为 $\mu$ 的 $n$ 次方根. 根据泰勒展式有

$$
\hat {\mu} _ {n} (\lambda) = \mathrm{e} ^ {\psi (\lambda) / n} = 1 + \frac {1}{n} \psi (\lambda) + \frac {1}{n ^ {2}} \varepsilon_ {n} (\lambda),
$$

其中 $\varepsilon_{n}(\lambda)$ 为 $\mathbb{R}$ 上的局部有界函数. 因此局部一致地有

$$
\psi (\lambda) = \lim _ {n \to \infty} n [ \hat {\mu} _ {n} (\lambda) - 1 ] = \lim _ {n \to \infty} n \int_ {\mathbb {R}} (\mathrm{e} ^ {\mathrm{i} \lambda z} - 1) \mu_ {n} (\mathrm{d} z). \tag {8.1.14}
$$

若记

$$
\beta_ {n} = \int_ {\mathbb {R}} \frac {n z}{1 + z ^ {2}} \mu_ {n} (\mathrm{d} z), \quad G _ {n} (\mathrm{d} z) = \frac {n z ^ {2}}{1 + z ^ {2}} \mu_ {n} (\mathrm{d} z),
$$

则可将 (8.1.14) 式写为

$$
\psi (\lambda) = \lim _ {n \to \infty} \left[ \mathrm{i} \beta_ {n} \lambda + \int_ {\mathbb {R}} K (\lambda , z) G _ {n} (\mathrm{d} z) \right].
$$

再由命题 8.1.6 知  $\psi$  有表达式 (8.1.12) 或 (8.1.13). □

---

202

第八章 连续时间马氏过程

## 8.1.4 卷积半群

定义 8.1.4 称 R 上的概率测度族  $(\mu_{t})_{t\geqslant0}$  为卷积半群, 是指当  $t\to0+$  时  $\mu_{t}\stackrel{w}{\rightarrow}\delta_{0}$  且

$$
\mu_ {s} * \mu_ {t} = \mu_ {s + t}, \quad s, t \geqslant 0. \tag {8.1.15}
$$

定理 8.1.9 欧氏空间 R 上的概率测度族  $(\mu_{t})_{t\geqslant0}$  构成一个卷积半群当且仅当其特征函数有表达式

$$
\hat {\mu} _ {t} (\lambda) := \int_ {\mathbb {R}} \mathrm{e} ^ {\mathrm{i} \lambda x} \mu_ {t} (\mathrm{d} x) = \mathrm{e} ^ {t \psi (\lambda)}, \quad t \geqslant 0, \lambda \in \mathbb {R}, \tag {8.1.16}
$$

其中  $\psi$  有莱维-辛钦表示 (8.1.12).

证明 设 $(\mu_t)_{t \geqslant 0}$ 的特征函数有表达式 (8.1.16). 根据定理 8.1.8, 每个概率测度 $\mu_t$ 无穷可分, 且有

$$
\hat {\mu} _ {s} (\lambda) \hat {\mu} _ {t} (\lambda) = \hat {\mu} _ {s + t} (\lambda), \quad s, t \geqslant 0, \lambda \in \mathbb {R}. \tag {8.1.17}
$$

由特征函数的唯一性知 $(\mu_t)_{t\geqslant 0}$ 构成一个卷积半群. 反之, 假设 $(\mu_t)_{t\geqslant 0}$ 是卷积半群. 由(8.1.15)式不难看出, 每个概率测度 $\mu_t$ 无穷可分, 故有形如(8.1.12)式或(8.1.13)式的连续函数 $\psi_t(\lambda)$ 使得

$$
\hat {\mu} _ {t} (\lambda) = \mathrm{e} ^ {\psi_ {t} (\lambda)}, \quad t \geqslant 0, \lambda \in \mathbb {R}.
$$

再由卷积半群的定义, 当  $t \rightarrow s+$  时  $\mu_{t-s} \stackrel{w}{\rightarrow} \delta_{0}$ , 故有

$$
\hat {\mu} _ {t} (\lambda) = \hat {\mu} _ {s} (\lambda) \hat {\mu} _ {t - s} (\lambda) \rightarrow \hat {\mu} _ {s} (\lambda).
$$

所以  $t \mapsto \psi_{t}(\lambda)$  右连续. 由关系  $\mu_{t} = \mu_{t/n} * \cdots * \mu_{t/n}$  (n 重卷积) 得  $\psi_{t}(\lambda) = n \psi_{t/n}(\lambda)$ .
故对任何正有理数 m/n 有

$$
\psi_ {m / n} (\lambda) = \frac {1}{n} \psi_ {m} (\lambda) = \frac {m}{n} \psi_ {1} (\lambda), \quad \lambda \in \mathbb {R}.
$$

令 $\psi (\lambda) = \psi_1(\lambda)$. 由上式和 $t\mapsto \psi_t(\lambda)$ 的右连续性知 $\psi_t(\lambda) = t\psi (\lambda)$ 对所有 $t\geqslant 0$ 成立. 因此有表达式(8.1.16). □

利用卷积半群, 可以构造出一类重要的费勒转移半群. 令 $(\mu_t)_{t \geqslant 0}$ 为 $\mathbb{R}$ 上的卷积半群. 对于 $t \geqslant 0$ 定义 $\mathbb{R}$ 上的马氏转移核 $P_t$ 如下:

$$
P _ {t} (x, \cdot) = \delta_ {x} * \mu_ {t}, \quad x \in \mathbb {R}. \tag {8.1.18}
$$

易知, 对任何 $f \in \mathrm{b}\mathcal{B}$ 有

$$
P _ {t} f (x) = \int_ {\mathbb {R}} f (y) P _ {t} (x, \mathrm{d} y) = \int_ {\mathbb {R}} f (x + z) \mu_ {t} (\mathrm{d} z). \tag {8.1.19}
$$

---

8.1 马氏转移半群

203

定理 8.1.10 如上定义的  $(P_{t})_{t\geqslant0}$  是费勒转移半群.

证明 根据 (8.1.19) 式易证当 $f \in C_0(\mathbb{R})$ 时有 $P_t f \in C_0(\mathbb{R})$. 因为当 $t \to 0+$ 时 $\mu_t \xrightarrow{\mathrm{w}} \delta_0$, 所以对任何 $x \in \mathbb{R}$ 有 $P_t f(x) \to f(x)$. 另外, 对于 $s, t \geqslant 0$ 有

$$
\begin{array}{l} \int_ {\mathbb {R}} P _ {s} (x, \mathrm{d} y) \int_ {\mathbb {R}} f (z) P _ {t} (y, \mathrm{d} z) = \int_ {\mathbb {R}} P _ {s} (x, \mathrm{d} y) \int_ {\mathbb {R}} f (y + z) \mu_ {t} (\mathrm{d} z) \\ = \int_ {\mathbb {R}} \mu_ {s} (\mathrm{d} y) \int_ {\mathbb {R}} f (x + y + z) \mu_ {t} (\mathrm{d} z) \\ = \int_ {\mathbb {R}} f (x + z) \mu_ {s + t} (\mathrm{d} z) \\ = \int_ {\mathbb {R}} f (z) P _ {s + t} (x, \mathrm{d} z). \\ \end{array}
$$

所以 $(P_{t})_{t\geqslant 0}$ 是费勒转移半群.□

例 8.1.6 设  $\alpha \geqslant 0$  为常数. 对  $t \geqslant 0$  令  $\mu_{t}$  为泊松分布  $P(\alpha t)$ , 则  $(\mu_{t})_{t \geqslant 0}$  构成卷积半群, 而由 (8.1.18) 式定义的费勒转移半群  $(P_{t})_{t \geqslant 0}$  由下式给出:

$$
P _ {t} f (x) = \sum_ {k = 0} ^ {\infty} \frac {\alpha^ {k} t ^ {k}}{k !} \mathrm{e} ^ {- \alpha t} f (x + k), \quad x \in \mathbb {R}, f \in C _ {0} (\mathbb {R}). \tag {8.1.20}
$$

例 8.1.7 对  $t \geqslant 0$  令  $\nu_{t}$  为正态分布  $N(0, t)$ ，则  $(\nu_{t})_{t \geqslant 0}$  构成卷积半群，而对应的费勒转移半群  $(P_{t})_{t \geqslant 0}$  就是 (8.1.8) 式定义的热半群.

## 练习题

1. 证明预解方程 (8.1.4).
2. 证明例 8.1.3, 例 8.1.4, 例 8.1.5 和例 8.2.3 中定义的转移核满足查普曼-柯尔莫哥洛夫方程.
3. 例 8.1.1 和例 8.1.2 中定义的马氏转移半群是费勒半群吗？为什么？
4. 设 $\{X(n): n \geqslant 0\}$ 是可数状态空间 $E$ 上的以 $P = (P_{ij}: i, j \in E)$ 为转移矩阵的离散时间马氏链, 而 $(N_t: t \geqslant 0)$ 是以 $\alpha \geqslant 0$ 为参数且与 $\{X(n): n \geqslant 0\}$ 独立的泊松过程. 证明 $\{X(N_t): t \geqslant 0\}$ 是马氏过程并给出其转移半群的表达式.
5. 构造一个具有例 8.1.3 中定义的转移半群的马氏过程.
6. 证明例 8.1.4 中定义的热半群满足强费勒性.

---

204

第八章 连续时间马氏过程

## 8.2 马氏性和强马氏性

基于马氏转移半群的工具, 本节讨论一般连续时间马氏过程的基本概念和性质, 包括马氏性、有限维分布性质和强马氏性, 并导出右连续费勒过程的强马氏性.

## 8.2.1 马氏性的定义

考虑完备概率空间 $(\Omega, \mathcal{G}, \mathbf{P})$ 及其上的 $\sigma$ 代数流 $(\mathcal{G}_t : t \geqslant 0)$. 假定状态空间 $(E, \mathcal{E})$ 上的随机过程 $X = (X_t : t \geqslant 0)$ 关于此流是适应的, 即对于任意的 $t \geqslant 0$ 随机变量 $X_t$ 关于 $\mathcal{G}_t$ 可测. 再设 $(P_t)_{t \geqslant 0}$ 为 $E$ 上的马氏转移半群.

定义 8.2.1 称 X 是关于流  $(\mathcal{G}_{t})$  以  $(P_{t})$  为转移半群的马氏过程, 是指对任意的  $s, t \geqslant 0$  和  $B \in E$  都有

$$
\mathbf {P} (X _ {s + t} \in B | \mathcal {G} _ {s}) = P _ {t} (X _ {s}, B). \tag {8.2.1}
$$

性质 (8.2.1) 称为以 $(P_t)$ 为转移半群的马氏性. 在这种情况下, 称 $X_0$ 在 $(E, \mathcal{E})$ 上的分布 $\mu$ 为 $X$ 的初始分布.

由于 (8.2.1) 式右边的随机变量关于 $\sigma(X_s) \subseteq \mathcal{G}_s$ 可测, 该式成立的充要条件是对于任意的 $G \in \mathcal{G}_s$ 都有

$$
\mathbf {P} (\{X _ {s + t} \in B \} \cap G) = \mathbf {E} [ P _ {t} (X _ {s}, B); G ]. \tag {8.2.2}
$$

在这种情况下, 当  $\mathbf{P}(G) > 0$  时有

$$
\mathbf {P} (X _ {s + t} \in B | G) = \mathbf {E} [ P _ {t} (X _ {s}, B) | G ].
$$

特别地, 若对 $x \in E$ 有 $\mathbf{P}(G \cap \{X_s = x\}) > 0$, 则

$$
\mathbf {P} (X _ {s + t} \in B | G \cap \{X _ {s} = x \}) = P _ {t} (x, B). \tag {8.2.3}
$$

可见直观上 $P_{t}(x,B)$ 代表了给定 $G\cap \{X_s = x\}$ 时 $\{X_{s + t}\in B\}$ 的条件概率.但是，与可数状态空间的情况不同，此时可能对每个 $x\in E$ 都有 $\mathbf{P}(X_s = x) = 0,$ 故不能以(8.2.3)式作为一般状态空间的马氏性的定义.

定理 8.2.1 若 X 关于流  $(\mathcal{G}_{t})$  具有以  $(P_{t})$  为转移半群的马氏性, 则它关于加强的流  $(\mathcal{G}_{t}^{*})$  也具有以  $(P_{t})$  为转移半群的马氏性.

证明 根据命题 2.1.14 对任何 $G \in \mathcal{G}_s^*$ 存在 $G_0 \in \mathcal{G}_s$ 使得 $\mathbf{P}(G \triangle G_0) = 0$. 在假定条件下 (8.2.2) 式对任何 $G \in \mathcal{G}_s$ 成立, 故它对任何 $G \in \mathcal{G}_s^*$ 也成立. $\square$

---

8.2 马氏性和强马氏性

205

定理 8.2.2 过程 X 关于流  $(\mathcal{G}_{t})$  具有以  $(P_{t})$  为转移半群的马氏性的充要条件是对任意的  $s, t \geqslant 0$  和  $f \in bE$  都有

$$
\mathbf {E} [ f (X _ {s + t}) | \mathcal {G} _ {s} ] = P _ {t} f (X _ {s}). \tag {8.2.4}
$$

证明 显然 (8.2.4) 式蕴涵马氏性 (8.2.1). 反之, 假设 (8.2.1) 式成立, 下证 (8.2.4) 式成立. 为此只需证明对任意的 $G \in \mathcal{G}_s$ 有

$$
\mathbf {E} [ f (X _ {s + t}); G ] = \mathbf {E} \big [ P _ {t} f (X _ {s}); G \big ]. \tag {8.2.5}
$$

由 (8.2.1) 式或 (8.2.2) 式知 (8.2.5) 式对于 $B \in \mathcal{E}$ 当 $f = 1_B$ 时成立. 由数学期望的线性性知 (8.2.5) 式对形如 $f = \sum_{i=1}^{n} a_i 1_{B_i} \in \mathrm{b}\mathcal{E}$ 的简单函数成立. 对于一般的 $f \in \mathrm{b}\mathcal{E}$, 令 $f_n = \phi_n(f^+) - \phi_n(f^-)$, 其中 $\phi_n$ 由 (2.1.4) 式给出而 $f^\pm$ 表示 $f$ 的正负部, 则有

$$
\mathbf {E} [ f _ {n} (X _ {s + t}); G ] = \mathbf {E} \big [ P _ {t} f _ {n} (X _ {s}); G \big ].
$$

注意, 当 $n \geqslant \| f\|$ 时 $\| P_t f_n - P_t f\| = \| P_t(f_n - f)\| \leqslant \| f_n - f\| \leqslant 1/2^n$. 在上式两端令 $n \to \infty$ 即知 (8.2.5) 式成立. $\square$

推论 8.2.3 过程 X 关于流  $(\mathcal{G}_{t})$  具有以  $(P_{t})$  为转移半群的马氏性当且仅当对任意的  $t \geqslant 0$  和  $f \in bE$  有界过程  $\{P_{t-s}f(X_{s}): s \in [0, t]\}$  关于流  $\{\mathcal{G}_{s}: s \in [0, t]\}$  是鞅.

定理 8.2.4 设  $(X_{t}: t \geqslant 0)$  是关于流  $(\mathcal{G}_{t}: t \geqslant 0)$  以  $(P_{t})_{t \geqslant 0}$  为转移半群的马氏过程。再设对  $r \geqslant 0$  和  $A \in G_{r}$  有  $\mathbf{P}(A) > 0$ 。则在条件概率  $\mathbf{P}_{A} := \mathbf{P}(\cdot | A)$  之下  $(X_{r+t}: t \geqslant 0)$  是关于流  $(\mathcal{G}_{r+t}: t \geqslant 0)$  以  $(P_{t})_{t \geqslant 0}$  为转移半群的马氏过程。

证明 任取 $s \geqslant 0$ 和 $G \in \mathcal{G}_{r+s}$. 由于 $G \cap A \in \mathcal{G}_{r+s}$, 根据 (8.2.2)式, 对 $f \in \mathrm{bE}$ 有

$$
\mathbf {E} [ f (X _ {r + s + t}); G \cap A ] = \mathbf {E} [ P _ {t} f (X _ {r + s}); G \cap A ].
$$

用  $E_{A}$  表示在  $P_{A}$  之下的数学期望. 将上式两端同除以  $\mathbf{P}(A)$  得

$$
\mathbf {E} _ {A} [ f (X _ {r + s + t}); G ] = \mathbf {E} _ {A} [ P _ {t} f (X _ {r + s}); G ].
$$

这说明在  $P_{A}$  之下  $(X_{r+t}:t\geqslant0)$  是关于流  $(\mathcal{G}_{r+t}:t\geqslant0)$  以  $(P_{t})_{t\geqslant0}$  为转移半群的马氏过程. □

定理 8.2.5 过程 X 关于其自然流  $(\mathcal{F}_{t})$  具有以  $(P_{t})$  为转移半群的马氏性当且仅当对任意的  $t \geqslant 0, 0 \leqslant s_{1} < s_{2} < \cdots < s_{n} = s$  和  $f \in bE$  有

$$
\mathbf {E} \big [ f (X _ {s + t}) | X _ {s _ {1}}, X _ {s _ {2}}, \dots , X _ {s _ {n}} \big ] = P _ {t} f (X _ {s}). \tag {8.2.6}
$$

证明 设 X 关于其自然流  $(\mathcal{F}_{t})$  具有以  $(P_{t})$  为转移半群的马氏性. 则 (8.2.4) 式对于  $(\mathcal{F}_{t})$  成立. 对该式取关于  $\sigma(X_{s_{1}}, X_{s_{2}}, \cdots, X_{s_{n}})$  的条件期望即得 (8.2.6) 式. 反之,

---

206

第八章 连续时间马氏过程

假设 (8.2.6) 式对任意的 $t \geqslant 0, 0 \leqslant s_1 < s_2 < \dots < s_n = s$ 和 $f \in \mathrm{b}\mathcal{E}$ 成立, 下证 (8.2.4) 式对于自然流 $(\mathcal{F}_t)$ 成立. 为此只需证明 (8.2.5) 式对任意的 $G \in \mathcal{F}_s$ 成立. 令 $\mathcal{D}$ 为使 (8.2.5) 式成立的所有 $G \in \mathcal{F}_s$ 构成的事件类. 易证 $\mathcal{D}$ 是一个邓肯类. 由 (8.2.6) 式知, 对任意的 $B_1, B_2, \dots, B_n \in \mathcal{E}$ 有

$$
\begin{array}{l} \mathbf {E} \left[ f (X _ {s + t}); X _ {s _ {1}} \in B _ {1}, X _ {s _ {2}} \in B _ {2}, \dots , X _ {s _ {n}} \in B _ {n} \right] \\ = \mathbf {E} \big [ P _ {t} f (X _ {s}); X _ {s _ {1}} \in B _ {1}, X _ {s _ {2}} \in B _ {2}, \dots , X _ {s _ {n}} \in B _ {n} \big ]. \tag {8.2.7} \\ \end{array}
$$

令 C 为所有形如  $\{X_{s_{1}}\in B_{1},X_{s_{2}}\in B_{2},\cdots,X_{s_{n}}\in B_{n}\}$  的事件构成的类. 显然 C 对交运算封闭且  $\sigma(\mathcal{C})=\mathcal{F}_{s}$ . 上式说明  $D\supseteq C$ . 根据邓肯类定理, 有  $\mathcal{D}\supseteq d(\mathcal{C})=\sigma(\mathcal{C})=\mathcal{F}_{s}$ , 即 (8.2.5) 式对一切  $G\in F_{s}$  成立. □

例 8.2.1 设  $\mu$  为纵轴上的区间  $E_{1}:=(0,1)$  上的概率测度. 考虑一个粒子在  $E_{1}$  中的随机运动: 在初始时刻粒子自点  $\xi(0)\in E_{1}$  出发, 向下以单位速度匀速运动直至触及原点, 此时该粒子根据概率分布  $\mu$  在  $E_{1}$  中选取一个新的位置, 然后从新位置开始向下以单位速度匀速运动, 如此不断重复下去. 用  $\xi(t)$  表示粒子在  $t\geqslant0$  时刻的位置, 则  $\{\xi(t):t\geqslant0\}$  是一个右连续马氏过程. 用  $(P_{t})_{t\geqslant0}$  表示其转移半群, 则对  $t\geqslant0, x\in E_{1}$  和  $E_{1}$  上的有界连续函数 f 有

$$
\begin{array}{l} P _ {t} f (x) = f (x - t) 1 _ {\{0 \leqslant t <   x \}} + \int_ {E _ {1}} f (x + x _ {1} - t) 1 _ {\{x \leqslant t <   x + x _ {1} \}} \mu (\mathrm{d} x _ {1}) + \\ \int_ {E _ {1}} \mu (\mathrm{d} x _ {1}) \int_ {E _ {1}} f (x + x _ {1} + x _ {2} - t) 1 _ {\{s _ {1} \leqslant t <   s _ {2} \}} \mu (\mathrm{d} x _ {2}) + \\ \sum_ {n = 3} ^ {\infty} \int_ {E _ {1}} \mu (\mathrm{d} x _ {1}) \dots \int_ {E _ {1}} f (s _ {n} - t) 1 _ {\{s _ {n - 1} \leqslant t <   s _ {n} \}} \mu (\mathrm{d} x _ {n}), \\ \end{array}
$$

其中 $s_n = x + \sum_{i=1}^{n} x_i$. 根据上式有方程

$$
P _ {t} f (x) = 1 _ {\{0 \leqslant t <   x \}} f (x - t) + 1 _ {\{t \geqslant x \}} \int_ {E _ {1}} P _ {t - x} f (y) \mu (\mathrm{d} y).
$$

设 $(P_{t})_{t\geqslant 0}$ 是 $(E,\mathcal{E})$ 上的准马氏转移半群, 而 $(\tilde{P}_t)_{t\geqslant 0}$ 是由(8.1.5)式定义的 $(\tilde{E},\tilde{\mathcal{E}})$ 上的扩张马氏转移半群. 设 $X = (X_{t}:t\geqslant 0)$ 相对于流 $(\mathcal{G}_t:t\geqslant 0)$ 是以 $(\tilde{P}_t)_{t\geqslant 0}$ 为转移半群的马氏过程. 也就是说, 任意的 $s,t\geqslant 0$ 和 $f\in \mathrm{b}\tilde{\mathcal{E}}$ 有

$$
\mathbf {E} [ \tilde {f} (X _ {s + t}) | \mathcal {G} _ {s} ] = \tilde {P} _ {t} \tilde {f} (X _ {s}). \tag {8.2.8}
$$

由 (8.1.5) 式不难发现, 若 $X_{s} = \partial$, 则 $X_{s + t} = \partial$. 我们把 $E$ 上的函数 $f$ 视为 $\tilde{E}$ 上的函数并约定 $f(\partial) = 0$. 于是对于 $t \geqslant 0$ 和 $f \in \mathrm{b}\mathcal{E}$ 有 $\tilde{P}_t f(\partial) = 0$ 和

$$
\tilde {P} _ {t} f (x) = \int_ {\tilde {E}} f (y) \tilde {P} _ {t} (x, \mathrm{d} y) = \int_ {E} f (y) P _ {t} (x, \mathrm{d} y) = P _ {t} f (x), \quad x \in E.
$$

---

8.2 马氏性和强马氏性

207

在上述约定之下, 由 (8.2.8) 式有

$$
\mathbf {E} [ f (X _ {s + t}) | \mathcal {G} _ {s} ] = P _ {t} f (X _ {s}).
$$

这里去掉了所有“波浪”号, 从而简化了表达. 注意上式与 (8.2.4) 式完全同型. 在很多情况下, 我们感兴趣的只是过程在 $E$ 中的行为, 因此也称 $X$ 为 $E$ 上的以 $(P_t)_{t \geqslant 0}$ 为转移半群的马氏过程.

## 8.2.2 有限维分布性质

设 $(P_{t})_{t\geqslant0}$ 是 $(E,\mathscr{E})$ 上的马氏转移半群, 则对 $x\in E$ 及 $J:=\{0\leqslant t_{1}<t_{2}<\cdots<t_{n}\}$, 存在 $(E^{n},\mathscr{E}^{n})$ 上唯一的概率测度 $P_{J}(x,\cdot)$ 使对 $B_{1},B_{2},\cdots,B_{n}\in\mathscr{E}$ 有

$$
\begin{array}{l} P _ {J} (x, B _ {1} \times B _ {2} \times \dots \times B _ {n}) = \int_ {B _ {1}} P _ {t _ {1}} (x, \mathrm{d} x _ {1}) \int_ {B _ {2}} P _ {t _ {2} - t _ {1}} (x _ {1}, \mathrm{d} x _ {2}) \dots \\ \int_ {B _ {n}} P _ {t _ {n} - t _ {n - 1}} (x _ {n - 1}, \mathrm{d} x _ {n}). \tag {8.2.9} \\ \end{array}
$$

注意上式是 $x \in E$ 的可测函数. 利用邓肯类定理不难证明 $P_{J}$ 是 $E$ 到 $E^{n}$ 的马氏转移核. 注意对任何 $t \geqslant 0$ 有 $P_{\{t\}} = P_{t}$.

定理 8.2.6 过程 $(X_t)$ 关于流 $(\mathcal{G}_t)$ 具有以 $(P_t)$ 为转移半群的马氏性当且仅当对任意的 $s \geqslant 0$, 有限集 $J = \{0 \leqslant t_1 < t_2 < \cdots < t_n\}$ 和 $f \in \mathrm{b}\mathscr{E}^n$ 有

$$
\mathbf {E} [ f (X _ {s + t _ {1}}, X _ {s + t _ {2}}, \dots , X _ {s + t _ {n}}) | \mathscr {G} _ {s} ] = P _ {J} f (X _ {s}). \tag {8.2.10}
$$

证明 显然马氏性 (8.2.1) 是 (8.2.10) 式的特殊形式. 下面假设 (8.2.1) 式成立, 我们证明 (8.2.10) 式. 等价地, 这需要证明对 $G \in \mathcal{G}_s$ 有

$$
\mathbf {E} [ f (X _ {s + t _ {1}}, X _ {s + t _ {2}}, \dots , X _ {s + t _ {n}}); G ] = \mathbf {E} [ P _ {J} f (X _ {s}); G ]. \tag {8.2.11}
$$

根据单调类定理, 只需证明对于任意的  $f_{1}, f_{2}, \cdots, f_{n} \in bE$  有

$$
\begin{array}{l} \mathbf {E} \Big [ 1 _ {G} f _ {1} (X _ {s + t _ {1}}) f _ {2} (X _ {s + t _ {2}}) \dots f _ {n} (X _ {s + t _ {n}}) \Big ] \\ = \mathbf {E} \Big [ 1 _ {G} \int_ {E} f _ {1} (x _ {1}) P _ {t _ {1}} (X _ {s}, \mathrm{d} x _ {1}) \int_ {E} f _ {2} (x _ {2}) P _ {t _ {2} - t _ {1}} (x _ {1}, \mathrm{d} x _ {2}) \dots \\ \left. \int_ {E} f _ {n} (x _ {n}) P _ {t _ {n} - t _ {n - 1}} (x _ {n - 1}, \mathrm{d} x _ {n}) \right]. \tag {8.2.12} \\ \end{array}
$$

由 (8.2.4) 式知当 $n = 1$ 时 (8.2.12) 式成立. 设该式对某个 $n \geqslant 1$ 成立. 再取 $t_{n+1} > t_n$ 和 $f_{n+1} \in \mathrm{b}\mathcal{E}$, 则有

$$
\mathbf {E} \Big [ 1 _ {G} f _ {1} (X _ {s + t _ {1}}) \dots f _ {n} (X _ {s + t _ {n}}) f _ {n + 1} (X _ {s + t _ {n + 1}}) \Big ]
$$

---

208

第八章 连续时间马氏过程

$$
\begin{array}{l} = \mathbf {E} \Big \{1 _ {G} f _ {1} (X _ {s + t _ {1}}) \dots f _ {n} (X _ {s + t _ {n}}) \mathbf {E} \big [ f _ {n + 1} (X _ {s + t _ {n + 1}}) | \mathscr {G} _ {s + t _ {n}} \big ] \Big \} \\ = \mathbf {E} \left[ 1 _ {G} f _ {1} (X _ {s + t _ {1}}) \dots f _ {n} (X _ {s + t _ {n}}) P _ {t _ {n + 1} - t _ {n}} f _ {n + 1} (X _ {s + t _ {n}}) \right] \\ = \mathbf {E} \Big [ 1 _ {G} \int_ {E} f _ {1} (x _ {1}) P _ {t _ {1}} (X _ {s}, \mathrm{d} x _ {1}) \int_ {E} f _ {2} (x _ {2}) P _ {t _ {2} - t _ {1}} (x _ {1}, \mathrm{d} x _ {2}) \dots \\ \int_ {E} f _ {n} (x _ {n}) P _ {t _ {n + 1} - t _ {n}} f _ {n + 1} (x _ {n}) P _ {t _ {n} - t _ {n - 1}} (x _ {n - 1}, \mathrm{d} x _ {n}) \Big ] \\ = \mathbf {E} \Big [ 1 _ {G} \int_ {E} f _ {1} (x _ {1}) P _ {t _ {1}} (X _ {s}, \mathrm{d} x _ {1}) \int_ {E} f _ {2} (x _ {2}) P _ {t _ {2} - t _ {1}} (x _ {1}, \mathrm{d} x _ {2}) \dots \\ \left. \int_ {E} f _ {n + 1} (x _ {n + 1}) P _ {t _ {n + 1} - t _ {n}} (x _ {n}, \mathrm{d} x _ {n + 1}) \right]. \\ \end{array}
$$

上式说明, 将 $n$ 换为 $n + 1$ 后 (8.2.12) 式仍然成立. 因此该式对所有 $n \geqslant 1$ 成立. $\square$

在定理 8.2.6 中令 s = 0, 再对 (8.2.10) 式取期望就得到:

定理 8.2.7 设  $(X_{t})$  为关于流  $(\mathcal{G}_{t})$  以  $\mu$  为初始分布、以  $(P_{t})$  为转移半群的马氏过程, 则对任意的  $J=\{t_{1}<t_{2}<\cdots<t_{n}\}\subseteq[0,\infty)$  和  $f\in bE^{n}$  有

$$
\mathbf {E} [ f (X _ {t _ {1}}, X _ {t _ {2}}, \dots , X _ {t _ {n}}) ] = \int_ {E} P _ {J} f (x) \mu (\mathrm{d} x). \tag {8.2.13}
$$

显然 (8.2.13) 式给出了 $(X_{t})$ 的有限维分布族的一个表示. 下面的定理说明在一定意义下定理 8.2.7 的逆命题也成立:

定理 8.2.8 若过程  $(X_{t})$  的有限维分布族由 (8.2.13) 式给出, 则  $(X_{t})$  是以  $\mu$  为初始分布、以  $(P_{t})$  为转移半群的马氏过程.

证明 在 (8.2.13) 式取 $J = \{0\}$ 即知 $X_0$ 服从分布 $\mu$. 利用 (8.2.9) 式和 (8.2.13) 式易证 (8.2.7) 式成立. 再由定理 8.2.5 的证明知 $(X_t)$ 是以 $(P_t)$ 为转移半群的马氏过程. □

## 8.2.3 强马氏性

定义 8.2.2 设状态空间  $(E, \mathcal{E})$  上的随机过程  $X = (X_{t} : t \geqslant 0)$  关于流  $(\mathcal{G}_{t} : t \geqslant 0)$  循序可测. 如果对任意的  $t \geqslant 0, f \in bE$  和  $(\mathcal{G}_{t})$  的停时 T 都有

$$
\mathbf {E} [ f (X _ {T + t}) 1 _ {\{T <   \infty \}} | \mathscr {G} _ {T} ] = P _ {t} f (X _ {T}) 1 _ {\{T <   \infty \}}, \tag {8.2.14}
$$

那么称 $X$ 具有关于流 $(\mathcal{G}_t)$ 以 $(P_t)$ 为转移半群的强马氏性, 也称 $X$ 为关于流 $(\mathcal{G}_t)$ 以 $(P_t)$ 为转移半群的强马氏过程.

在上面的定义中, 因为 $(X_{t})$ 关于流 $(\mathcal{G}_{t})$ 循序可测, 根据命题 2.1.20, 映射 $\omega \mapsto X_{T(\omega)}(\omega)$ 限制在 $\{T < \infty\}$ 上关于 $\{T < \infty\} \cap \mathcal{G}_T$ 可测. 另外, 易知 (8.2.14) 式等价于对任意的 $G \in \mathcal{G}_T$ 有

$$
\mathbf {E} \big [ f (X _ {T + t}); \{T <   \infty \} \cap G \big ] = \mathbf {E} \big [ P _ {t} f (X _ {T}); \{T <   \infty \} \cap G \big ]. \tag {8.2.15}
$$

---

8.2 马氏性和强马氏性

209

下面的定理给出了这个等价条件的另外一种形式:

定理 8.2.9 设过程  $(X_{t})$  关于流  $(\mathcal{G}_{t})$  循序可测, 则强马氏性 (8.2.14) 成立的充要条件是对任意的  $t \geqslant 0, f \in bE$  和  $(\mathcal{G}_{t})$  的停时 T 有

$$
\mathbf {E} [ f (X _ {T + t}); T <   \infty ] = \mathbf {E} [ P _ {t} f (X _ {T}); T <   \infty ]. \tag {8.2.16}
$$

证明 若强马氏性 (8.2.14) 成立, 在该式两端取期望即得 (8.2.16) 式. 反之, 设 (8.2.16) 式对任意的 $t \geqslant 0$, $f \in \mathrm{b}\mathcal{E}$ 和 $(\mathcal{G}_t)$ 的停时 $T$ 成立. 对于 $G \in \mathcal{G}_T$ 令 $T_G = T \cdot 1_G + \infty \cdot 1_{G^c}$, 不难验证 $T_G$ 也是 $(\mathcal{G}_t)$ 的停时. 对于其应用 (8.2.16) 式得

$$
\begin{array}{l} \mathbf {E} \big [ f (X _ {T + t}); \{T <   \infty \} \cap G \big ] = \mathbf {E} \big [ f (X _ {T _ {G} + t}); T _ {G} <   \infty \big ] \\ = \mathbf {E} \big [ P _ {t} f (X _ {T _ {G}}); T _ {G} <   \infty \big ] \\ = \mathbf {E} \big [ P _ {t} f (X _ {T _ {G}}); \{T _ {G} <   \infty \} \cap G \big ] \\ = \mathbf {E} \big [ P _ {t} f (X _ {T}); \{T <   \infty \} \cap G \big ], \\ \end{array}
$$

即 (8.2.15) 式对任意的 $G \in \mathcal{G}_T$ 成立. 所以 (8.2.14) 式成立. $\square$

我们知道, 两个停时之和仍然是停时. 基于这一事实, 与关于简单马氏性的讨论类似地, 可以证明如下的:

定理 8.2.10 设  $(X_{t}: t \geqslant 0)$  是关于流  $(\mathcal{G}_{t}: t \geqslant 0)$  以  $(P_{t})_{t \geqslant 0}$  为转移半群的强马氏过程. 再设 T 为  $(\mathcal{G}_{t})$  的停时, 而事件  $A \in G_{T}$  满足  $\mathbf{P}(A \cap \{T < \infty\}) > 0$ , 则在条件概率  $\mathbf{P}_{A} := \mathbf{P}(\cdot | A \cap \{T < \infty\})$  之下  $(X_{T+t}: t \geqslant 0)$  具有相对于流  $(\mathcal{G}_{T+t}: t \geqslant 0)$  以  $(P_{t})_{t \geqslant 0}$  为转移半群的强马氏性.

定理 8.2.11 过程 $(X_t)$ 关于流 $(\mathcal{G}_t)$ 具有以 $(P_t)$ 为转移半群的强马氏性当且仅当对任意的 $(\mathcal{G}_t)$ 的停时 $T$, 有限集 $J = \{0 \leqslant t_1 < t_2 < \cdots < t_n\}$ 和 $f \in \mathrm{bE}^n$ 有

$$
\mathbf {E} [ f (X _ {T + t _ {1}}, X _ {T + t _ {2}}, \dots , X _ {T + t _ {n}}) | \mathscr {G} _ {T} ] = P _ {J} f (X _ {T}). \tag {8.2.17}
$$

直观上, 定理 8.2.10 说明, 在给定 $\mathcal{G}_T$ 的条件下 $(X_{T + t}:t\geqslant 0)$ 具有相对于流 $(\mathcal{G}_{T + t}:t\geqslant 0)$ 以 $(P_t)_{t\geqslant 0}$ 为转移半群的强马氏性. 另外, 可以证明任何费勒过程都有左极右连的实现; 参见 [8, pp.54-55]. 下面的定理说明, 这样的实现具有强马氏性.

定理 8.2.12 设  $(P_{t})$  为可分局部紧度量空间 E 上的费勒转移半群, 而  $(X_{t})$  是关于流  $(\mathcal{G}_{t})$  以  $(P_{t})$  为转移半群的右连续马氏过程, 则  $(X_{t})$  是关于右连续加强流  $(\mathcal{G}_{t+}^{*})$  以  $(P_{t})$  为转移半群的强马氏过程.

证明 由定理8.2.1知 $(X_{t})$ 关于加强的流 $(\mathcal{G}_t^*)$ 也具有以 $(P_t)$ 为转移半群的马氏性.因 $(X_{t})$ 右连续,它是循序可测的.根据命题8.1.2和定理8.2.9,只需证明对任意的$t\geqslant 0,f\in C_0(E)$ 和 $(\mathcal{G}_{t + }^{*})$ 的停时 $T$ 有(8.2.16)式成立.对 $n\geqslant 1$ 令 $T_{n}$ 为 $T$ 的二分点离散化,即 $T_{n} = 2^{-n}(\lfloor 2^{n}T\rfloor +1)$.注意

$$
\{T _ {n} = k / 2 ^ {n} \} = \{(k - 1) / 2 ^ {n} \leqslant T <   k / 2 ^ {n} \} \in \mathscr {G} _ {k / 2 ^ {n}} ^ {*}
$$

---

210

第八章 连续时间马氏过程

根据马氏性有

$$
\mathbf {E} [ f (X _ {k / 2 ^ {n} + t}); T _ {n} = k / 2 ^ {n} ] = \mathbf {E} [ P _ {t} f (X _ {k / 2 ^ {n}}); T _ {n} = k / 2 ^ {n} ],
$$

亦即

$$
\mathbf {E} [ f (X _ {T _ {n} + t}); T _ {n} = k / 2 ^ {n} ] = \mathbf {E} [ P _ {t} f (X _ {T _ {n}}); T _ {n} = k / 2 ^ {n} ].
$$

将上式对 $k \geqslant 0$ 求和并注意 $\{T_n < \infty\} = \{T < \infty\}$ 得

$$
\mathbf {E} [ f (X _ {T _ {n} + t}); T <   \infty ] = \mathbf {E} [ P _ {t} f (X _ {T _ {n}}); T <   \infty ].
$$

由于 $f, P_t f \in C_0(E)$ 且 $(X_t)$ 右连续, 对上式取极限 $n \to \infty$ 并应用有界收敛定理即得 (8.2.16) 式. □

定理 8.2.13 设  $(P_{t})$  是可分局部紧度量空间 E 上的费勒转移半群, 而  $(X_{t})$  是关于流  $(\mathcal{G}_{t})$  以  $(P_{t})$  为转移半群的右连续马氏过程. 再设 T 是关于右连续加强流  $(\mathcal{G}_{t+}^{*})$  的停时, 而 S 是关于  $G_{T+}^{*}$  可测的非负随机变量. 则对于任何  $f \in bE$  有

$$
\mathbf {E} [ f (X _ {T + S}) | \mathcal {G} _ {T +} ^ {*} ] = P _ {S} f (X _ {T}), \tag {8.2.18}
$$

其中右端理解为函数  $P_{t}f(x)$  在  $(t,x)=(S,X_{T})$  处的值.

证明 令 $\{S_n\}$ 是 $S$ 的二分点离散化序列, 即 $S_n = 2^{-n} (\lfloor 2^n S \rfloor + 1)$. 因为 $S \in \mathcal{G}_{T+}^*$, 所以 $S_n \in \mathcal{G}_{T+}^*$. 特别地, 有 $\{S_n = k/2^n\} \in \mathcal{G}_{T+}^*$. 设 $A \in \mathcal{G}_{T+}^*$. 则 $A_{n,k} := A \cap \{S_n = k/2^n\} \in \mathcal{G}_{T+}^*$. 根据定理 8.2.12 建立的强马氏性,

$$
\begin{array}{l} \mathbf {E} [ 1 _ {A} f (X _ {T + S _ {n}}) ] = \sum_ {k = 1} ^ {\infty} \mathbf {E} \big [ 1 _ {A _ {n, k}} f (X _ {T + k / 2 ^ {n}}) \big ] \\ = \sum_ {k = 1} ^ {\infty} \mathbf {E} \bigl \{1 _ {A _ {n, k}} \mathbf {E} \bigl [ f (X _ {T + k / 2 ^ {n}}) | \mathcal {G} _ {T +} ^ {*} \bigr ] \bigr \} \\ = \sum_ {k = 1} ^ {\infty} \mathbf {E} \big [ 1 _ {A _ {n, k}} P _ {k / 2 ^ {n}} f (X _ {T}) \big ] = \mathbf {E} \big [ 1 _ {A} P _ {S _ {n}} f (X _ {T}) \big ]. \\ \end{array}
$$

注意, 当 $n \to \infty$ 时单调不降地 $S_{n} \to S$. 当 $f \in C_{0}(E)$ 时, 在上式两端令 $n \to \infty$, 利用 $t \mapsto X_{t}$ 和 $t \mapsto P_{t}f(x)$ 的右连续性得

$$
\mathbf {E} \big [ 1 _ {A} f (X _ {T + S}) \big ] = \mathbf {E} \big [ 1 _ {A} P _ {S} f (X _ {T}) \big ].
$$

根据命题 8.1.2 可知上式对一切  $f \in bE$  成立, 故 (8.2.18) 式成立. □

例 8.2.2 给定常数 b > 0, 可以定义正半直线  $R_{+}$  上的一族转移核  $(P_{t})_{t \geqslant 0}$  如下: 若 x > 0 令  $P_{t}(x, \mathrm{d}y) = \delta_{x+t}(\mathrm{d}y)$ , 再令

$$
P _ {t} (0, \mathrm{d} y) = \mathrm{e} ^ {- b t} \delta_ {0} (\mathrm{d} y) + b \int_ {0} ^ {t} \delta_ {t - s} (\mathrm{d} y) \mathrm{e} ^ {- b s} \mathrm{d} s. \tag {8.2.19}
$$

---

8.2 马氏性和强马氏性

211

取 $r, t \geqslant 0$ 和 $f \in \mathrm{b}\mathcal{B}(\mathbb{R}_+)$. 对于 $x > 0$ 有

$$
P _ {r} P _ {t} f (x) = P _ {t} f (x + r) = f (x + t + r) = P _ {r + t} f (x).
$$

另外, 我们有

$$
\begin{array}{l} P _ {r} P _ {t} f (0) = P _ {t} f (0) \mathrm{e} ^ {- b r} + b \int_ {0} ^ {r} P _ {t} f (r - s) \mathrm{e} ^ {- b s} \mathrm{d} s \\ = f (0) \mathrm{e} ^ {- b (r + t)} + b \mathrm{e} ^ {- b r} \int_ {0} ^ {t} f (t - s) \mathrm{e} ^ {- b s} \mathrm{d} s + \\ b \int_ {0} ^ {r} f (r + t - s) \mathrm{e} ^ {- b s} \mathrm{d} s \\ = f (0) \mathrm{e} ^ {- b (r + t)} + b \int_ {r} ^ {r + t} f (r + t - s) \mathrm{e} ^ {- b s} \mathrm{d} s + \\ b \int_ {0} ^ {r} f (r + t - s) \mathrm{e} ^ {- b s} \mathrm{d} s \\ = P _ {r + t} f (0). \\ \end{array}
$$

所以 $(P_{t})_{t\geqslant 0}$ 是 $\mathbb{R}_{+}$ 上的转移半群. 该转移半群描述了一个粒子在上半直线 $\mathbb{R}_{+}$ 中随机运动. 用 $X_{t}$ 表示粒子在时刻 $t$ 的位置. 若 $X_0 > 0$, 则粒子从该位置开始以单位速度向上运动; 而若 $X_0 = 0$, 则粒子先在 0 点停留一个以 $b$ 为参数的指数分布的随机时间, 然后再开始以单位速度向上运动.

关于一般连续时间马氏过程的深入讨论, 可以参考著作 [8,10].

## 8.2.4 布朗运动的强马氏性

根据定义 2.5.1, 关于流  $(\mathcal{F}_{t})$  的标准布朗运动  $(B_{t}: t \geqslant 0)$  是一个连续的实数值  $(\mathcal{F}_{t})$  适应过程, 且对任意的  $t > s \geqslant 0$  增量  $B_{t} - B_{s}$  独立于  $F_{s}$  且服从高斯分布  $N(0, t - s)$ . 下面的定理给出了  $(B_{t}: t \geqslant 0)$  的强马氏性.

定理 8.2.14 设  $(B_{t})$  是关于流  $(\mathcal{F}_{t})$  的标准布朗运动, 则  $(B_{t})$  是关于右连续加强流  $(\mathcal{F}_{t+}^{*})$  的强马氏过程, 而其转移半群  $(P_{t})$  是 (8.1.8) 式定义的热半群.

证明 由命题2.5.4知 $(B_{t})$ 也是关于右连续加强流 $(\mathcal{F}_{t+}^{*})$ 的标准布朗运动. 因此对于 $s, t \geqslant 0$ 增量 $B_{s+t} - B_{s}$ 独立于 $\mathcal{F}_{s+}^{*}$ 且服从高斯分布 $N(0, t)$, 故对 $G \in \mathcal{F}_{s+}^{*}$ 和 $\theta \in \mathbb{R}$ 有

$$
\begin{array}{l} \mathbf {E} [ 1 _ {G} \mathrm{e} ^ {\mathrm{i} \theta B _ {s + t}} ] = \mathbf {E} [ 1 _ {G} \mathrm{e} ^ {\mathrm{i} \theta B _ {s}} ] \mathbf {E} \big [ \mathrm{e} ^ {\mathrm{i} \theta (B _ {s + t} - B _ {s})} \big ] \\ = \mathbf {E} [ 1 _ {G} \mathrm{e} ^ {\mathrm{i} \theta B _ {s}} ] \mathrm{e} ^ {- t \theta^ {2} / 2} = \mathbf {E} \big [ 1 _ {G} \mathrm{e} ^ {\mathrm{i} \theta B _ {s} - t \theta^ {2} / 2} \big ], \\ \end{array}
$$

或者写为

$$
\mathbf {E} [ 1 _ {G} \mathrm{e} ^ {\mathrm{i} \theta B _ {s + t}} ] = \mathbf {E} \Big [ 1 _ {G} \int_ {\mathbb {R}} \mathrm{e} ^ {\mathrm{i} \theta y} P _ {t} (B _ {s}, \mathrm{d} y) \Big ].
$$

---

212

第八章 连续时间马氏过程

再由特征函数的唯一性, 对一切  $f \in C_{0}(\mathbb{R})$  有

$$
\mathbf {E} [ 1 _ {G} f (B _ {s + t}) ] = \mathbf {E} \Big [ 1 _ {G} \int_ {\mathbb {R}} f (y) P _ {t} (B _ {s}, \mathrm{d} y) \Big ] = \mathbf {E} \big [ 1 _ {G} P _ {t} f (B _ {s}) \big ].
$$

上式说明 $(B_{t})$ 关于流 $(\mathcal{F}_{t+}^{*})$ 是以 $(P_{t})$ 为转移半群的马氏过程. 再由定理8.2.12知相应的强马氏性成立. □

定理 8.2.15 (反射原理) 设  $(B_{t})$  是从原点出发的标准布朗运动, 则对任意的  $t \geqslant 0$  和 x > 0 有

$$
\mathbf {P} \Big (\max _ {0 \leqslant s \leqslant t} B _ {s} \geqslant x \Big) = 2 \mathbf {P} (B _ {t} \geqslant x) = \mathbf {P} (| B _ {t} | \geqslant x). \tag {8.2.20}
$$

证明 令 $(\mathcal{F}_t)$ 为 $(B_t)$ 的自然流. 由定理8.2.14知 $(B_t)$ 关于右连续加强流 $(\mathcal{F}_{t+}^*)$ 是以(8.1.8)式定义的热半群 $(P_t)$ 为转移半群的强马氏过程. 定义 $(\mathcal{F}_{t+}^*)$ 的停时

$$
\tau_ {x} := \inf \{s \geqslant 0: B _ {s} = x \} = \inf \{s \geqslant 0: B _ {s} \geqslant x \}.
$$

记 $M_{t} = \max_{0\leqslant s\leqslant t}B_{s}$ ，则有

$$
\begin{array}{l} \mathbf {P} (M _ {t} \geqslant x) = \mathbf {P} \big (M _ {t} \geqslant x, B _ {t} \geqslant x \big) + \mathbf {P} \big (M _ {t} \geqslant x, B _ {t} <   x\left. \right) \\ = \mathbf {P} (B _ {t} \geqslant x) + \mathbf {P} \big (\tau_ {x} \leqslant t, B _ {t} \leqslant x \big). \\ \end{array}
$$

根据定理 8.2.13 有

$$
\begin{array}{l} \mathbf {P} \big (\tau_ {x} \leqslant t, B _ {t} \leqslant x \big) = \mathbf {E} \big [ 1 _ {\{\tau_ {x} \leqslant t \}} \mathbf {P} \big (B _ {\tau_ {x} + (t - \tau_ {x})} \leqslant x | \mathscr {F} _ {\tau_ {x} +} \big) \big ] \\ = \mathbf {E} \big [ 1 _ {\{\tau_ {x} \leqslant t \}} P _ {t - \tau_ {x}} (B _ {\tau_ {x}}, (- \infty , x ]) \big ] \\ = \mathbf {E} \big [ 1 _ {\{M _ {t} \geqslant x \}} P _ {t - \tau_ {x}} (x, (- \infty , x ]) \big ] = \mathbf {P} (M _ {t} \geqslant x) / 2. \\ \end{array}
$$

所以 (8.2.20) 式成立. □

推论 8.2.16 设  $(B_{t})$  是从原点出发的标准布朗运动, 则对任意的  $x \in R$  几乎必然有  $\tau_{x} := \inf\{t \geqslant 0 : B_{t} = x\} < \infty$ .

证明 不妨设 $x > 0$. 注意 $\lim_{t\to \infty}\mathbf{P}(|B_t|\geqslant x) = 1$. 根据 (8.2.20) 式有

$$
\mathbf {P} (\tau_ {x} <   \infty) = \lim _ {t \to \infty} \mathbf {P} (\tau_ {x} \leqslant t) = \lim _ {t \to \infty} \mathbf {P} \Big (\max _ {0 \leqslant s \leqslant t} B _ {s} \geqslant x \Big) = 1.
$$

由布朗运动的对称性, 当 x < 0 时也有  $\mathbf{P}(\tau_{x} < \infty) = 1$ . □

例 8.2.3 设  $(B_{t}: t \geqslant 0)$  是关于右连续加强流  $(\mathcal{G}_{t})$  的标准布朗运动, 称  $(|B_{t}|: t \geqslant 0)$  为  $R_{+} = [0, \infty)$  上的反射边界布朗运动. 对  $t \geqslant 0$  定义  $R_{+}$ 上的马氏转移核  $Q_{t}$  如下: 对  $x \in R_{+}$ 和  $f \in C_{0}(\mathbb{R}_{+})$ ,

$$
Q _ {t} f (x) = \frac {1}{\sqrt {2 \pi t}} \int_ {\mathbb {R} _ {+}} f (y) [ \mathrm{e} ^ {- (y - x) ^ {2} / 2 t} + \mathrm{e} ^ {- (y + x) ^ {2} / 2 t} ] \mathrm{d} y.
$$

---

8.2 马氏性和强马氏性

213

易证 $(Q_{t})_{t\geqslant 0}$ 构成 $\mathbb{R}_{+}$ 上的费勒半群. 由定理8.2.14知 $(B_{t})$ 关于流 $(\mathcal{G}_t)$ 是以(8.1.8)式定义的热半群 $(P_{t})$ 为转移半群的马氏过程. 因此对任意的 $s,t\geqslant 0$ 和 $a\geqslant 0$ 有

$$
\begin{array}{l} \mathbf {P} (| B _ {s + t} | \geqslant a | \mathscr {G} _ {s}) = P _ {t} (B _ {s}, (- \infty , - a ] \cup [ a, \infty)) \\ = P _ {t} (| B _ {s} |, (- \infty , - a ] \cup [ a, \infty)) \\ = Q _ {t} (| B _ {s} |, [ a, \infty)). \\ \end{array}
$$

所以 $(|B_{t}|:t\geqslant0)$ 关于流 $(\mathcal{G}_{t})$ 是以 $(Q_{t})_{t\geqslant0}$ 为转移半群的马氏过程.

例 8.2.4 设  $(B_{t}: t \geqslant 0)$  是关于右连续加强流  $(\mathcal{G}_{t})$  的标准布朗运动且  $B_{0} > 0$ . 根据推论 8.2.16, 几乎必然有  $\tau_{0} := \inf\{t \geqslant 0 : B_{t} < 0\} < \infty$ . 称  $(B_{t \wedge \tau_{0}} : t \geqslant 0)$  为  $R_{+} = [0, \infty)$  上的吸收边界布朗运动. 令  $(\tilde{P}_{t})_{t \geqslant 0}$  为例 8.1.5 给出的  $R_{++}$  上的准马氏转移半群  $(P_{t}^{\circ})_{t \geqslant 0}$  在  $R_{+}$ 上的费勒马氏扩张半群. 由定理 8.2.14 知  $(B_{t})$  关于流  $(\mathcal{G}_{t})$  是以 (8.1.8) 式定义的热半群  $(P_{t})$  为转移半群的马氏过程. 因此对任意的  $t > s \geqslant 0$  和 a > 0 有

$$
\begin{array}{l} \mathbf {P} (B _ {t \wedge \tau_ {0}} \geqslant a | \mathcal {G} _ {s}) = \mathbf {P} (B _ {t} \geqslant a, \tau_ {0} > s, \tau_ {0} > t | \mathcal {G} _ {s}) \\ = \mathbf {P} (\tau_ {0} > s, B _ {t} \geqslant a | \mathscr {G} _ {s}) - \mathbf {P} (s <   \tau_ {0} \leqslant t, B _ {t} \geqslant a | \mathscr {G} _ {s}) \\ = 1 _ {\{\tau_ {0} > s \}} P _ {t} (B _ {s}, [ a, \infty)) - 1 _ {\{\tau_ {0} > s \}} \mathbf {P} (\tau_ {0} \leqslant t, B _ {t} \geqslant a | \mathscr {G} _ {s}). \\ \end{array}
$$

根据定理 8.2.13, 在事件  $\{\tau_{0}>s\}$  上有

$$
\begin{array}{l} \mathbf {P} (\tau_ {0} \leqslant t, B _ {t} \geqslant a | \mathcal {G} _ {s}) = \mathbf {E} \big [ 1 _ {\{\tau_ {0} \leqslant t \}} \mathbf {P} (B _ {t} \geqslant a | \mathcal {G} _ {\tau_ {0}}) | \mathcal {G} _ {s} \big ] \\ = \mathbf {E} \big [ 1 _ {\{\tau_ {0} \leqslant t \}} P _ {t - \tau_ {0}} (0, [ a, \infty)) | \mathcal {G} _ {s} \big ] \\ = \mathbf {E} \big [ 1 _ {\{\tau_ {0} \leqslant t \}} P _ {t - \tau_ {0}} (0, (- \infty , - a ]) | \mathcal {G} _ {s} \big ] \\ = \mathbf {E} \big [ 1 _ {\{\tau_ {0} \leqslant t \}} \mathbf {P} (B _ {t} \leqslant - a | \mathcal {G} _ {\tau_ {0}}) | \mathcal {G} _ {s} \big ] \\ = \mathbf {P} (\tau_ {0} \leqslant t, B _ {t} \leqslant - a | \mathcal {G} _ {s}) \\ = \mathbf {P} (B _ {t} \leqslant - a | \mathcal {G} _ {s}) = P _ {t} (B _ {s}, (- \infty , - a ]). \\ \end{array}
$$

综合上面的计算得

$$
\begin{array}{l} \mathbf {P} (B _ {t \wedge \tau_ {0}} \geqslant a | \mathscr {G} _ {s}) = 1 _ {\{\tau_ {0} > s \}} P _ {t} (B _ {s}, [ a, \infty)) - 1 _ {\{\tau_ {0} > s \}} P _ {t} (B _ {s}, (- \infty , - a ]) \\ = 1 _ {\{\tau_ {0} > s \}} P _ {t} (B _ {s}, [ a, \infty)) - 1 _ {\{\tau_ {0} > s \}} P _ {t} (- B _ {s}, [ a, \infty)) \\ = 1 _ {\{\tau_ {0} > s \}} P _ {t} ^ {\circ} (B _ {s \wedge \tau_ {0}}, [ a, \infty)) = 1 _ {\{\tau_ {0} > s \}} \tilde {P} _ {t} (B _ {s \wedge \tau_ {0}}, [ a, \infty)). \\ \end{array}
$$

所以  $(B_{s\wedge\tau_{0}}:t\geqslant0)$  关于流  $(\mathcal{G}_{t})$  是以  $(\tilde{P}_{t})_{t\geqslant0}$  为转移半群的马氏过程.

## 练习题

1. 设 $X_0$ 为实数值随机变量. 令 $X_t = X_0 + t$. 证明 $(X_t : t \geqslant 0)$ 是费勒马氏过程.

---

214

第八章 连续时间马氏过程

2. 设 $(N_{t}: t \geqslant 0)$ 是以 $\alpha > 0$ 为参数的左极右连泊松过程. 证明 $(N_{t}: t \geqslant 0)$ 关于其自然流 $(\mathcal{F}_{t}: t \geqslant 0)$ 是马氏过程, 并给出其转移半群的表达式. 问 $(N_{t}: t \geqslant 0)$ 关于流 $(\mathcal{F}_{t}: t \geqslant 0)$ 是否为强马氏过程? 为什么?
3. 在上题的情况下, 令 $X_{t} = N_{t-}$. 问 $(X_{t}: t \geqslant 0)$ 关于流 $(\mathcal{F}_{t}: t \geqslant 0)$ 是否为马氏过程? 是否为强马氏过程? 为什么?
4. 证明左极右连的复合泊松过程是费勒强马氏过程.
5. 例 8.2.2 中定义的马氏转移半群是否费勒半群？该例中描述的随机运动是否具有强马氏性？
6. 证明例 8.2.1 中定义的马氏转移核  $(P_{t})_{t\geqslant0}$  满足查普曼-柯尔莫哥洛夫方程, 并对于  $E_{1}$  上的有界连续函数 f 说明:

(1) $t \mapsto P_t f(x)$ 右连续;
(2) $t \mapsto P_{t}f(x)$ 未必左连续;
(3) $x \mapsto P_t f(x)$ 未必右连续.

提示: 对于  $E_{1}$  上的有界连续函数 f, 显然  $t \mapsto P_{t}f(x)$  右连续. 如果极限  $f(0+) := \lim_{x \to 0+} f(x)$  存在, 由上面方程可知对  $x \in E_{1}$ , 有

$$
P _ {x} f (x) = \mu (f), \quad P _ {x -} f (x) = P _ {x} f (x +) = f (0 +).
$$

因此一般  $t \mapsto P_{t}f(x)$  未必左连续, 而  $x \mapsto P_{t}f(x)$  未必右连续.

## 8.3 莱维过程

莱维过程是具有独立增量性的费勒过程, 其最典型的特例是泊松过程和布朗运动. 莱维过程的转移半群由一个卷积半群确定, 这种结构大大增加了其可计算性. 本节讨论莱维过程的基本结构和性质. 为简单起见, 我们只讨论一维的情况.

## 8.3.1 独立增量性

定义 8.3.1 定义在概率空间  $(\Omega, \mathcal{G}, \mathbf{P})$  上的实数值随机过程  $(X_{t}: t \geqslant 0)$  称为关于流  $(\mathcal{G}_{t}: t \geqslant 0)$  的独立增量过程, 是指它关于该流适应且对任何  $s, t \geqslant 0$ , 增量  $X_{s+t} - X_{s}$  与  $G_{s}$  独立. 此时, 若增量  $X_{s+t} - X_{s}$  的分布只依赖于 t 而与 s 无关, 则称  $(X_{t})$  为关于流  $(\mathcal{G}_{t})$  的平稳独立增量过程. 称具有左极右连轨道的平稳独立增量过程为莱维过程.

假定 $(X_{t}:t\geqslant 0)$ 是关于流 $(\mathcal{G}_t)_{t\geqslant 0}$ 的平稳独立增量过程, 则零初值过程 $(X_{t} - X_{0}: t\geqslant 0)$ 也是关于该流的平稳独立增量过程. 再设 $(X_{t}:t\geqslant 0)$ 随机连续, 并令 $\mu_t$ 为

---

8.3 莱维过程

215

$X_{t}-X_{0}$  的分布, 则显然  $(\mu_{t})_{t\geqslant0}$  构成一个卷积半群, 称为  $(X_{t}:t\geqslant0)$  的卷积半群. 注意  $(X_{t}:t\geqslant0)$  和  $(X_{t}-X_{0}:t\geqslant0)$  具有相同的卷积半群. 由于有上述关系, 很多时候我们只讨论零初值的平稳独立增量过程, 而将一般初值的结果作为推论.

定理 8.3.1 令  $(P_{t})$  是由 (8.1.19) 式定义的费勒半群. 若  $(X_{t})$  相对于流  $(\mathcal{G}_{t})$  是以  $(\mu_{t})$  为卷积半群的平稳独立增量过程, 则它是关于流  $(\mathcal{G}_{t})$  以  $(P_{t})$  为转移半群的马氏过程.

证明 根据假设, 对于 $s, t \geqslant 0$, 增量 $X_{s+t} - X_s$ 独立于 $\mathcal{G}_s$ 且服从分布 $\mu_t$. 对于 $G \in \mathcal{G}_s$ 和 $\lambda \in \mathbb{R}$, 由 (8.1.16) 式有

$$
\begin{array}{l} \mathbf {E} (1 _ {G} \mathrm{e} ^ {\mathrm{i} \lambda X _ {s + t}}) = \mathbf {E} (\mathrm{e} ^ {\mathrm{i} \lambda X _ {s}}) \mathbf {E} \big [ \mathrm{e} ^ {\mathrm{i} \lambda (X _ {s + t} - X _ {s})} \big ] = \mathbf {E} (1 _ {G} \mathrm{e} ^ {\mathrm{i} \lambda X _ {s}}) \int_ {\mathbb {R}} \mathrm{e} ^ {\mathrm{i} \lambda z} \mu_ {t} (\mathrm{d} z) \\ = \mathbf {E} \Big [ 1 _ {G} \mathrm{e} ^ {\mathrm{i} \lambda X _ {s}} \int_ {\mathbb {R}} \mathrm{e} ^ {\mathrm{i} \lambda z} \mu_ {t} (\mathrm{d} z) \Big ] = \mathbf {E} \Big [ 1 _ {G} \int_ {\mathbb {R}} \mathrm{e} ^ {\mathrm{i} \lambda y} P _ {t} (X _ {s}, \mathrm{d} y) \Big ]. \\ \end{array}
$$

再由特征函数的唯一性, 对一切  $f \in C_{0}(\mathbb{R})$  有

$$
\mathbf {E} \big [ 1 _ {G} f (X _ {s + t}) \big ] = \mathbf {E} \Big [ 1 _ {G} \int_ {\mathbb {R}} f (y) P _ {t} (X _ {s}, \mathrm{d} y) \Big ] = \mathbf {E} \big [ 1 _ {G} P _ {t} f (X _ {s}) \big ].
$$

上式说明 $(X_{t})$ 关于流 $(\mathcal{G}_t)$ 是以 $(P_t)$ 为转移半群的马氏过程. □

定理 8.3.2 若  $(X_{t})$  是关于流  $(\mathcal{G}_{t})$  以  $(P_{t})$  为转移半群的马氏过程, 则它是相对于流  $(\mathcal{G}_{t})$  以  $(\mu_{t})$  为卷积半群的平稳独立增量过程.

证明 任取 $s, t \geqslant 0$ 和 $f \in \mathrm{b}\mathcal{B}$. 对 $J = (0, t)$ 和 $f(x, y) = f(y - x)$ 应用定理8.2.6得

$$
\mathbf {E} [ f (X _ {s + t} - X _ {s}) | \mathscr {G} _ {s} ] = \int_ {\mathbb {R}} f (y - X _ {s}) P _ {t} (X _ {s}, \mathrm{d} y) = \int_ {\mathbb {R}} f (z) \mu_ {t} (\mathrm{d} z).
$$

因此对任意的 $G \in \mathrm{b}\mathcal{G}_s$ 有

$$
\mathbf {E} [ G f (X _ {s + t} - X _ {s}) ] = \mathbf {E} \Big [ G \int_ {\mathbb {R}} f (z) \mu_ {t} (\mathrm{d} z) \Big ] = \mathbf {E} (G) \int_ {\mathbb {R}} f (z) \mu_ {t} (\mathrm{d} z).
$$

这说明 $X_{s + t} - X_s$ 独立于 $\mathcal{G}_s$ 且有分布 $\mu_t$, 因而 $X$ 关于流 $(\mathcal{G}_t)$ 是以 $(\mu_t)$ 为卷积半群的平稳独立增量过程. $\square$

例8.3.1 设 $(X_{t})$ 是关于流 $(\mathcal{G}_t)$ 的零初值可积莱维过程. 由(8.1.16)式不难推出 $\mathbf{E}(X_t) = t\mathbf{E}(X_1)$. 对于 $t \geqslant s \geqslant 0$ 有

$$
\mathbf {E} (X _ {t} | \mathcal {G} _ {s}) = \mathbf {E} [ X _ {s} + (X _ {t} - X _ {s}) | \mathcal {G} _ {s} ] = X _ {s} + (t - s) \mathbf {E} (X _ {1}).
$$

因此当  $\mathbf{E}(X_{1})\geqslant0$  时,  $(X_{t})$  是下鞅; 当  $\mathbf{E}(X_{1})\leqslant0$  时,  $(X_{t})$  是上鞅; 当  $\mathbf{E}(X_{1})=0$  时,  $(X_{t})$  是鞅.

---

216

第八章 连续时间马氏过程

例 8.3.2 以  $\alpha \geqslant 0$  为参数的泊松过程是右连续的平稳独立增量过程, 因而是莱维过程. 令  $(\mu_{t})_{t \geqslant 0}$  为其卷积半群, 则  $\mu_{t}$  就是泊松分布  $P(\alpha t)$ , 而对应的费勒转移半群  $(P_{t})_{t \geqslant 0}$  由 (8.1.20) 式给出.

例 8.3.3 标准布朗运动  $(B_{t}: t \geqslant 0)$  是连续的平稳独立增量过程, 因而是莱维过程. 用  $(\nu_{t})_{t \geqslant 0}$  表示其卷积半群, 则  $\nu_{t}$  为正态分布  $N(0, t)$ , 而对应的费勒转移半群  $(P_{t})_{t \geqslant 0}$  就是 (8.1.8) 式定义的热半群.

## 8.3.2 莱维-伊藤表示

现在我们讨论莱维过程的轨道的构造问题. 设 $(\mu_t)_{t \geqslant 0}$ 是由 (8.1.16) 式给出的卷积半群. 为方便后面的讨论, 我们将 $\psi$ 的莱维-辛钦表示 (8.1.12) 式改写为

$$
\psi (\lambda) = \mathrm{i} b \lambda - \frac {\sigma^ {2}}{2} \lambda^ {2} + \int_ {\mathbb {R} \setminus \{0 \}} \big (\mathrm{e} ^ {\mathrm{i} \lambda z} - 1 - \mathrm{i} \lambda z 1 _ {\{| z | \leqslant 1 \}} \big) \nu (\mathrm{d} z), \tag {8.3.1}
$$

其中

$$
b = \beta + \int_ {\mathbb {R} \setminus \{0 \}} \Big (z 1 _ {\{| z | \leqslant 1 \}} - \frac {z}{1 + z ^ {2}} \Big) \nu (\mathrm{d} z).
$$

设 $(\Omega, \mathcal{F}, \mathbf{P})$ 是完备的概率空间, 且在此概率空间上定义了零初值的标准布朗运动 $\{B(t)\}$ 和 $(0, \infty) \times \mathbb{R}$ 上的强度为 $\mathrm{ds}\nu(\mathrm{dz})$ 的泊松随机测度 $N(\mathrm{ds}, \mathrm{dz})$. 令 $\tilde{N}(\mathrm{ds}, \mathrm{dz}) = N(\mathrm{ds}, \mathrm{dz}) - \mathrm{ds}\nu(\mathrm{dz})$ 为 $N(\mathrm{ds}, \mathrm{dz})$ 的补偿的随机测度. 在当前情况下, 若 $B \in \mathcal{B}$ 满足 $\nu(B) < \infty$, 则泊松过程

$$
N _ {t} (B) := N ((0, t ] \times B), \quad t \geqslant 0
$$

独立于布朗运动 $\{B(t)\}$; 如可参见 [20, p.77]. 据此可以证明 $\{B(t)\}$ 和 $\{N(\mathrm{ds},\mathrm{dz})\}$ 相互独立. 对于 $t \geqslant 0$, 令 $\mathcal{G}_t$ 是由下面的随机变量族生成的加强 $\sigma$ 代数:

$$
\{B (s), N ((0, s ] \times B): 0 \leqslant s \leqslant t, B \in \mathcal {B} \text {且} \nu (B) <   \infty \}.
$$

再定义左极右连复合泊松过程

$$
\eta (t) = \int_ {(0, t ]} \int_ {\{| z | > 1 \}} z N (\mathrm{d} s, \mathrm{d} z), \quad t \geqslant 0 \tag {8.3.2}
$$

和零均值平方可积 $(\mathcal{G}_{t})$ 鞅

$$
\xi (t) = \int_ {(0, t ]} \int_ {\{0 <   | z | \leqslant 1 \}} z \tilde {N} (\mathrm{d} s, \mathrm{d} z), \quad t \geqslant 0.
$$

注意, 对于  $t \geqslant r \geqslant 0$  有  $\mathbf{E}[\xi(t) - \xi(r)] = 0$  和

$$
\mathbf {E} [ | \xi (t) - \xi (r) | ^ {2} ] = (t - r) \int_ {\{0 <   | z | \leqslant 1 \}} z ^ {2} \nu (\mathrm{d} z).
$$

---

8.3 莱维过程

217

所以  $\{\xi(t)\}$  随机连续, 由定理 2.5.2 它有左极右连修正. 现在令

$$
X (t) = b t + \sigma B (t) + \int_ {(0, t ]} \int_ {\{0 <   | z | \leqslant 1 \}} z \tilde {N} (\mathrm{d} s, \mathrm{d} z) + \int_ {(0, t ]} \int_ {\{| z | > 1 \}} z N (\mathrm{d} s, \mathrm{d} z), \tag {8.3.3}
$$

则过程  $\{X(t):t\geqslant0\}$  有左极右连修正.

定理 8.3.3 由 (8.3.3) 式定义的  $\{X(t)\}$  关于流  $(\mathcal{G}_{t})$  是以  $(\mu_{t})$  为卷积半群的平稳独立增量过程.

证明 我们首先证明 $X(t)$ 有分布 $\mu_t$. 根据复合泊松过程的结果, 对于 $\lambda \in \mathbb{R}$ 有

$$
\begin{array}{l} \mathbf {E} \Big (\exp \left\{\mathrm{i} \lambda \int_ {(0, t ]} \int_ {\{| z | > 1 \}} z N (\mathrm{d} s, \mathrm{d} z) \right\} \Big) \\ = \exp \Big \{t \int_ {\{| z | > 1 \}} (\mathrm{e} ^ {\mathrm{i} \lambda z} - 1) \nu (\mathrm{d} z) \Big \}. \tag {8.3.4} \\ \end{array}
$$

对 $k \geqslant 1$ 令

$$
\xi_ {k} (t) = \int_ {(0, t ]} \int_ {\{1 / k <   | z | \leqslant 1 \}} z \tilde {N} (\mathrm{d} s, \mathrm{d} z).
$$

不难发现

$$
\mathbf {E} (\mathrm{e} ^ {\mathrm{i} \lambda \xi_ {k} (t)}) = \exp \Big \{t \int_ {\{1 / k <   | z | \leqslant 1 \}} \big (\mathrm{e} ^ {\mathrm{i} \lambda z} - 1 - \mathrm{i} \lambda z \big) \nu (\mathrm{d} z) \Big \}.
$$

在上式中令 $k\to \infty$ 并应用控制收敛定理得

$$
\mathbf {E} (\mathrm{e} ^ {\mathrm{i} \lambda \xi (t)}) = \exp \left\{t \int_ {\{0 <   | z | \leqslant 1 \}} \big (\mathrm{e} ^ {\mathrm{i} \lambda z} - 1 - \mathrm{i} \lambda z \big) \nu (\mathrm{d} z) \right\}. \tag {8.3.5}
$$

因为 $\sigma B(t)$ 服从正态分布 $N(0, \sigma^2 t)$, 再综合 (8.3.4) 式与 (8.3.5) 式知 $X(t)$ 与 $\mu_t$ 有相同的特征函数, 故 $X(t)$ 服从分布 $\mu_t$. 对于 $t \geqslant r \geqslant 0$, 由 (8.3.3) 式及布朗运动和泊松随机测度的性质易知 $X(t) - X(r)$ 与 $\mathcal{G}_r$ 独立且与 $X(t - r)$ 同分布. 所以 $\{X(t)\}$ 关于流 $(\mathcal{G}_t)$ 是以 $(\mu_t)$ 为卷积半群的平稳独立增量过程. $\square$

通常称 (8.3.3) 式为莱维过程 $\{X(t): t \geqslant 0\}$ 的莱维-伊藤表示. 它给出了以 $(\mu_t)_{t \geqslant 0}$ 为卷积半群的莱维过程的一个构造. 事实上, 任何以 $(\mu_t)_{t \geqslant 0}$ 为卷积半群的莱维过程的轨道都可以分解为 (8.3.3) 式的形式; 参见 [31, pp.120-121].

## 8.3.3 半群的强费勒性

令 $(\mu_t)$ 是由(8.1.16)式给出的卷积半群, 而 $(P_t)$ 是由(8.1.19)式定义的费勒转移半群. 我们称二维随机过程 $\{(X_1(t), X_2(t)): t \geqslant 0\}$ 为耦合莱维过程, 是指 $\{X_1(t): t \geqslant 0\}$

---

218

第八章 连续时间马氏过程

和 $\{X_{2}(t): t \geqslant 0\}$ 都是具有转移半群 $(P_{t})$ 的莱维过程. 特别地, 取 $X_{1}(0) = x_{1}$ 和 $X_{2}(0) = x_{2}$, 则有

$$
\| P _ {t} (x _ {1}, \cdot) - P _ {t} (x _ {2}, \cdot) \| _ {\text {var}} = \sup _ {f \in \mathscr {B} _ {1}} \left| \mathbf {P} [ f (X _ {1} (t)) - f (X _ {2} (t)) ] \right|, \tag {8.3.6}
$$

其中  $\|\cdot\|_{var}$  表示全变差范数, 而  $B_{1}$  表示 R 上的满足  $|f| \leqslant 1$  的博雷尔可测函数 f 的全体.

定理 8.3.4 若  $\sigma > 0$ ，则对于任意的 t > 0 和  $x_{1}, x_{2} \in R$  有

$$
\| P _ {t} (x _ {1}, \cdot) - P _ {t} (x _ {2}, \cdot) \| _ {\mathrm{var}} \leqslant \frac {\sqrt {2}}{\sigma \sqrt {\pi t}} | x _ {1} - x _ {2} |. \tag {8.3.7}
$$

证明 不妨设 $x_{1} \geqslant x_{2}$. 令 $\{X(t): t \geqslant 0\}$ 是由莱维-伊藤表示 (8.3.3) 式定义的莱维过程. 记 $\zeta(t) = (x_{1} - x_{2}) + 2\sigma B(t)$. 定义停时 $\tau = \inf \{t \geqslant 0 : \zeta(t) < 0\}$, 再令

$$
B ^ {*} (t) = B (t) - 2 B (t \wedge \tau) = - B (t \wedge \tau) + \big [ B (t) - B (t \wedge \tau) \big ].
$$

注意, 对 $0 \leqslant t \leqslant \tau$ 有 $B^{*}(t) = -B(t)$, 而对 $t \geqslant \tau$ 有 $B^{*}(t) = B(t) - 2B(\tau)$. 利用强马氏性可以证明 $\{B^{*}(t): t \geqslant 0\}$ 也是标准布朗运动. 令

$$
X ^ {*} (t) = b t + \sigma B ^ {*} (t) + \int_ {(0, t ]} \int_ {\{| z | \leqslant 1 \}} z \tilde {N} (\mathrm{d} s, \mathrm{d} z) + \int_ {(0, t ]} \int_ {\{| z | > 1 \}} z N (\mathrm{d} s, \mathrm{d} z).
$$

显然 $\{X^{*}(t):t\geqslant 0\}$ 也是具有转移半群 $(P_{t})$ 的莱维过程.记 $X_{1}(t) = x_{1} + X(t)$ 和$X_{2}(t) = x_{2} + X^{*}(t)$ ，则 $\{(X_1(t),X_2(t)):t\geqslant 0\}$ 是耦合莱维过程.另外，易见

$$
X _ {1} (t) - X _ {2} (t) = (x _ {1} - x _ {2}) + \sigma \big [ B (t) - B ^ {*} (t) \big ] = \zeta (t \wedge \tau).
$$

所以当 $t \geqslant \tau$ 时有 $X_{1}(t) = X_{2}(t)$. 再由 (8.3.6) 式不难看出

$$
\| P _ {t} (x _ {1}, \cdot) - P _ {t} (x _ {2}, \cdot) \| _ {\text {var}} \leqslant 2 \mathbf {P} (\tau > t).
$$

利用布朗运动的反射原理, 我们有

$$
\begin{array}{l} \mathbf {P} (\tau > t) = \mathbf {P} \Big (\sup _ {0 \leqslant s \leqslant t} B (s) <   | x _ {1} - x _ {2} | / 2 \sigma \Big) \\ = \mathbf {P} \Big (| B (t) | <   | x _ {1} - x _ {2} | / 2 \sigma \Big) \\ = \frac {1}{\sqrt {2 \pi t}} \int_ {- | x _ {1} - x _ {2} | / 2 \sigma} ^ {| x _ {1} - x _ {2} | / 2 \sigma} \mathrm{e} ^ {- x ^ {2} / 2 t} \mathrm{d} x \leqslant \frac {1}{\sigma \sqrt {2 \pi t}} | x _ {1} - x _ {2} |. \\ \end{array}
$$

所以 (8.3.7) 式成立. □

推论 8.3.5 若  $\sigma > 0$ ，则  $(P_{t})_{t \geqslant 0}$  具有强费勒性.

---

8.3 莱维过程

219

下面考虑 $\nu (\mathbb{R}) > 0$ 的情况. 此时可取充分小的常数 $0 < \varepsilon < 1$ 使得 $0 < \nu (\bar{B}_{\varepsilon}^{c}) < \infty$, 其中 $\bar{B}_{\varepsilon}^{c} = \mathbb{R} \setminus \bar{B}_{\varepsilon}$ 而 $\bar{B}_{\varepsilon} = [-\varepsilon, \varepsilon]$. 注意莱维-伊藤表示 (8.3.3) 式可以改写为

$$
X (t) = b _ {\varepsilon} t + \sigma B _ {t} + \int_ {(0, t ]} \int_ {\bar {B} _ {\varepsilon}} z \tilde {N} (\mathrm{d} s, \mathrm{d} z) + \int_ {(0, t ]} \int_ {\bar {B} _ {\varepsilon} ^ {c}} z N (\mathrm{d} s, \mathrm{d} z), \tag {8.3.8}
$$

其中

$$
b _ {\varepsilon} = b - \int_ {\mathbb {R}} 1 _ {\{\varepsilon <   | z | \leqslant 1 \}} z \nu (\mathrm{d} z).
$$

对 $A \in \mathcal{B}(\mathbb{R})$ 写 $\nu_{\varepsilon}(A) = \nu(A \cap \bar{B}_{\varepsilon}^{c})$, 则 $\nu_{\varepsilon}$ 是 $\mathbb{R}$ 上的有限测度. 定义概率测度 $\gamma_{\varepsilon} = \nu_{\varepsilon}(\mathbb{R})^{-1}\nu_{\varepsilon}$. 考虑条件

$$
\operatorname * {l i m s u p} _ {| x | \to 0} | x | ^ {- 1} \| \gamma_ {\varepsilon} - \delta_ {x} * \gamma_ {\varepsilon} \| _ {\text {var}} <   \infty , \tag {8.3.9}
$$

显然, 上面的条件等价于

$$
K _ {\varepsilon} := \sup _ {x \in \mathbb {R}} | x | ^ {- 1} \| \gamma_ {\varepsilon} - \delta_ {x} * \gamma_ {\varepsilon} \| _ {\text {var}} <   \infty . \tag {8.3.10}
$$

定理 8.3.6 假设条件 (8.3.9) 成立, 则对  $t \geqslant 0$  和  $x_{1}, x_{2} \in R$  有

$$
\| P _ {t} (x _ {1}, \cdot) - P _ {t} (x _ {2}, \cdot) \| _ {\mathrm{var}} \leqslant 2 \mathrm{e} ^ {- \nu (\bar {B} _ {\varepsilon} ^ {c}) t} + K _ {\varepsilon} | x _ {1} - x _ {2} |.
$$

证明 令 $\{X(t):t\geqslant 0\}$ 由(8.3.8)式给出, 并令 $X_{i}(t) = x_{i} + X(t), i = 1,2.$ 显然 $\{(X_1(t),X_2(t)):t\geqslant 0\}$ 是耦合莱维过程. 记

$$
\eta_ {\varepsilon} (t) = \int_ {(0, t ]} \int_ {\bar {B} _ {\varepsilon} ^ {c}} z N (\mathrm{d} s, \mathrm{d} z),
$$

由定理 1.5.7 知  $\{\eta_{\varepsilon}(t):t\geqslant0\}$  是具有跳跃速率  $\nu(\bar{B}_{\varepsilon}^{c})$  和跳跃分布  $\gamma_{\varepsilon}$  的复合泊松过程.
令  $\tau_{1}=\inf\{t\geqslant0:\eta_{\varepsilon}(t)\neq\eta_{\varepsilon}(t-)\}$  为其首次跳跃的时间, 则对  $f\in B_{1}$  有

$$
\left| P _ {t} f (x _ {1}) - P _ {t} f (x _ {2}) \right| = \left| \mathbf {E} \big [ f (X _ {1} (t)) - f (X _ {2} (t)) \big ] \right| \leqslant 2 \mathbf {P} (\tau_ {1} > t) + p _ {\varepsilon} (t),
$$

其中  $\mathbf{P}(\tau_{1}>t)=\mathrm{e}^{-\nu(\bar{B}_{\varepsilon}^{c})t}$  而

$$
p _ {\varepsilon} (t) = \left| \mathbf {E} \big \{\big [ f (X _ {1} (t)) - f (X _ {2} (t)) \big ] 1 _ {\{\tau_ {1} \leqslant t \}} \big \} \right|.
$$

注意对任何 $t \geqslant 0$ 有 $X_{2}(t) = (x_{2} - x_{1}) + X_{1}(t)$. 根据强马氏性和 (8.3.10) 式有

$$
p _ {\varepsilon} (t) = \left| \mathbf {E} \bigg \{\int_ {0} ^ {t} \nu (\bar {B} _ {\varepsilon} ^ {c}) \mathrm{e} ^ {- \nu (\bar {B} _ {\varepsilon} ^ {c}) s} \bigg [ \int_ {\mathbb {R}} P _ {t - s} f (X _ {1} (s -) + z) \gamma_ {\varepsilon} (\mathrm{d} z) - \right.
$$

$$
\left. \int_ {\mathbb {R}} P _ {t - s} f (X _ {2} (s -) + z) \gamma_ {\varepsilon} (\mathrm{d} z) \right] \mathrm{d} s \Bigg \} \Bigg |
$$

---

220

第八章 连续时间马氏过程

$$
\begin{array}{l} = \left| \mathbf {E} \left\{\int_ {0} ^ {t} \nu \left(\bar {B} _ {\varepsilon} ^ {c}\right) \mathrm{e} ^ {- \nu \left(\bar {B} _ {\varepsilon} ^ {c}\right) s} \left[ \int_ {\mathbb {R}} P _ {t - s} f \left(X _ {1} (s) + z\right) \gamma_ {\varepsilon} (\mathrm{d} z) - \right. \right. \right. \\ \left. \int_ {\mathbb {R}} P _ {t - s} f (X _ {1} (s) + z) \delta_ {x _ {2} - x _ {1}} * \gamma_ {\varepsilon} (\mathrm{d} z) \right] \mathrm{d} s \Bigg \}\left. \right| \\ \leqslant \int_ {0} ^ {t} \nu (\bar {B} _ {\varepsilon} ^ {c}) \mathrm{e} ^ {- \nu (\bar {B} _ {\varepsilon} ^ {c}) s} \| \gamma_ {\varepsilon} - \delta_ {x _ {2} - x _ {1}} * \gamma_ {\varepsilon} \| \mathrm{d} s \\ \leqslant K _ {\varepsilon} \nu (\bar {B} _ {\varepsilon} ^ {c}) | x _ {2} - x _ {1} | \int_ {0} ^ {t} \mathrm{e} ^ {- \nu (\bar {B} _ {\varepsilon} ^ {c}) s} \mathrm{d} s \leqslant K _ {\varepsilon} | x _ {2} - x _ {1} |. \\ \end{array}
$$

所以

$$
\big | P _ {t} f (x _ {1}) - P _ {t} f (x _ {2}) \big | \leqslant 2 \mathrm{e} ^ {- \nu (\bar {B} _ {\varepsilon} ^ {c}) t} + K _ {\varepsilon} | x _ {1} - x _ {2} |.
$$

将上式对  $f \in B_{1}$  取上确界即得欲证结果. □

推论 8.3.7 假设存在序列  $\{\varepsilon_{n}\} \subseteq (0,1]$  满足  $\lim_{n\to\infty}\nu(\bar{B}_{\varepsilon_{n}}^{c})=\infty$  且 (8.3.9) 式对每个  $\varepsilon_{n}$  成立. 则有

$$
\lim _ {x \to y} \| P _ {t} (x, \cdot) - P _ {t} (y, \cdot) \| _ {\text {var}} = 0, \tag {8.3.11}
$$

因而 $(P_{t})_{t\geqslant0}$ 具有强费勒性.

证明 根据定理 8.3.6, 显然对任意的 t > 0 和  $n \geqslant 1$  有

$$
\operatorname * {l i m s u p} _ {x \to y} \| P _ {t} (x, \cdot) - P _ {t} (y, \cdot) \| _ {\text {var}} \leqslant 2 \mathrm{e} ^ {- \nu (\bar {B} _ {\varepsilon_ {n}} ^ {c}) t}.
$$

在上式中令 $n\to \infty$ 即知(8.3.11)式成立.□

例 8.3.4 假设  $\nu(\mathrm{d}z)=1_{\{z>0\}}z^{-(1+\alpha)}\mathrm{d}z,$  其中  $0<\alpha<2.$  于是对 x>0 有

$$
\gamma_ {\varepsilon} (\mathrm{d} z) = \frac {1 _ {\{z > \varepsilon \}} \mathrm{d} z}{\alpha \varepsilon^ {\alpha} z ^ {1 + \alpha}}, \quad \delta_ {x} * \gamma_ {\varepsilon} (\mathrm{d} z) = \frac {1 _ {\{z - x > \varepsilon \}} \mathrm{d} z}{\alpha \varepsilon^ {\alpha} (z - x) ^ {1 + \alpha}}
$$

和

$$
| \gamma_ {\varepsilon} - \delta_ {x} * \gamma_ {\varepsilon} | (\mathrm{d} z) = \frac {1}{\alpha \varepsilon^ {\alpha}} \Big [ \frac {1 _ {\{\varepsilon <   z \leqslant x + \varepsilon \}}}{z ^ {1 + \alpha}} + 1 _ {\{z > x + \varepsilon \}} \Big (\frac {1}{(z - x) ^ {1 + \alpha}} - \frac {1}{z ^ {1 + \alpha}} \Big) \Big ] \mathrm{d} z.
$$

不难看出

$$
\| \gamma_ {\varepsilon} - \delta_ {x} * \gamma_ {\varepsilon} \| _ {\mathrm{var}} = | \gamma_ {\varepsilon} - \delta_ {x} * \gamma_ {\varepsilon} | (0, \infty) = \frac {2}{\alpha^ {2} \varepsilon^ {\alpha}} \Big (\frac {1}{\varepsilon^ {\alpha}} - \frac {1}{(x + \varepsilon) ^ {\alpha}} \Big).
$$

根据中值定理, 存在  $\varepsilon < \xi < x + \varepsilon$  使得

$$
\| \gamma_ {\varepsilon} - \delta_ {x} * \gamma_ {\varepsilon} \| _ {\mathrm{var}} = \frac {2 x}{\alpha \varepsilon^ {\alpha} \xi^ {1 + \alpha}} \leqslant \frac {2 x}{\alpha \varepsilon^ {1 + 2 \alpha}}.
$$

当 $x < 0$ 时也有类似的估计. 所以此时条件 (8.3.9) 成立.

---

8.3 莱维过程

221

本小节的讨论提供了应用概率方法证明分析结果的典型案例.耦合过程的方法在这里发挥了关键的作用.由于耦合考虑了过程轨道的结构, 以此给出的有关分布的估计往往比纯分析的方法更为精确.关于耦合与距离方法的系统理论和应用, 可以参阅著作[4,5,34].

## 练习题

1. 设 $(X_{t})$ 是莱维过程. 对于 $\lambda \in \mathbb{R}$ 记 $f_{t}(\lambda) = \mathbf{E}[\mathrm{e}^{\mathrm{i}\lambda X_{t}}]$, 再令 $M_{t} = f_{t}(\lambda)^{-1}\mathrm{e}^{\mathrm{i}\lambda X_{t}}$. 证明 $(M_{t})$ 关于其自然流是复鞅 (即实部和虚部都是鞅).

2. 令 $t > 0$ 且 $\mu_t$ 由 (8.1.16) 式和 (8.3.1) 式定义. 证明下面的两个积分条件等价:

(1) $\int_{\mathbb{R}} |x| \mu_t(\mathrm{d}x) < \infty$;
(2) $\int_{\{|z| > 1\}} |z|\nu(\mathrm{d}z) < \infty.$

提示: 根据定理 8.3.3, 由 (8.3.3) 式定义的随机变量  $X(t)$  具有分布  $\mu_{t}$ . 令

$$
X _ {0} (t) = b t + \sigma B (t) + \int_ {(0, t ]} \int_ {\{0 <   | z | \leqslant 1 \}} z \tilde {N} (\mathrm{d} s, \mathrm{d} z)
$$

和

$$
X _ {1} (t) = \int_ {(0, t ]} \int_ {\{z > 1 \}} z N (\mathrm{d} s, \mathrm{d} z), X _ {2} (t) = - \int_ {(0, t ]} \int_ {\{z <   - 1 \}} z N (\mathrm{d} s, \mathrm{d} z),
$$

则 $X(t) = X_0(t) + X_1(t) - X_2(t)$ 且 $X_0(t), X_1(t)$ 和 $X_2(t)$ 相互独立. 因 $\mathbf{E}[X_0(t)^2] < \infty$, 易知 $\mathbf{E}[|X(t)|] < \infty$ 当且仅当 $\mathbf{E}[X_1(t) + X_2(t)] < \infty$. 再由泊松随机测度的矩的计算公式即得结论.

3. 设上题中的积分条件满足. 证明

$$
\int_ {\mathbb {R}} x \mu_ {t} (\mathrm{d} x) = t \bigg [ b + \int_ {\{| z | > 1 \}} z \nu (\mathrm{d} z) \bigg ].
$$

4. 证明由 (8.3.3) 式构造的莱维过程 $\{X(t)\}$ 的轨道取连续函数, 取阶梯函数和取单增函数的概率都是 0 或 1.
5. 设 $\{X(t)\}$ 是由 (8.3.3) 式构造的莱维过程. 再设 $\nu(0, \infty) > 0$. 对 $t > 0$ 令 $D(t) = \sup_{0 < s \leqslant t} [X(s) - X(s-)]$. 证明: 对于任何 $t > 0$ 几乎必然地 $D(t) = \max_{0 < s \leqslant t} [X(s) - X(s-)]$, 且对任何 $x > 0$ 有

$$
\mathbf {P} \big \{D (t) > x \big \} = 1 - \mathrm{e} ^ {- t \nu (x, \infty)}.
$$

提示: 对 $x, t > 0$ 令 $J_x(t)$ 为集合 $\{s \in (0, t] : X(s) - X(s-) > x\}$ 中元素的个数, 即 $X$ 在时间区间 $(0, t]$ 中的跳幅严格大于 $x$ 的跳跃的次数. 根据莱维-伊藤表示知 $J_x(t)$ 服从参数为 $t\nu(x, \infty)$ 的泊松分布. 特别地, 有 $\mathbf{P}\{J_x(t) < \infty\} = 1$, 故几乎必然地 $D(t) = \max_{0 < s \leqslant t} [X(s) - X(s-)]$. 再由 $\mathbf{P}\{D(t) > x\} = \mathbf{P}\{J_x(t) \geqslant 1\}$ 即得欲证等式.
