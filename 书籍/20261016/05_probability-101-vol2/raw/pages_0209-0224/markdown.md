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

令 $(\mu_t)$ 是由(8.1.16)式给出的卷积半群, 而 $(P_t)$ 是由(8.1.19)式定义的费勒转移半群. 我们称二维随机过程 $\{(X_1(t), X_2(t)): t \geqslant 0\}$ 为耦合莱维过程, 是指 $\{X_1(t): t \geqslant 0\}$和 $\{X_{2}(t): t \geqslant 0\}$ 都是具有转移半群 $(P_{t})$ 的莱维过程. 特别地, 取 $X_{1}(0) = x_{1}$ 和 $X_{2}(0) = x_{2}$, 则有

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