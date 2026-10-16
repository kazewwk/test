梯函数. 记

$$
P _ {k} (t) = \mathbf {P} \left(N _ {t} = k\right), \quad k = 0, 1, 2, \dots . \tag {2.2.10}
$$

从理论和应用两方面, 下面的假定都是自然的:

- 独立增量性: 对 $0 \leqslant t_1 < t_2 \leqslant t_3 < t_4$ 和 $k_1, k_2 \geqslant 0$, 随机事件 $\{N_{t_1} - N_{t_2} = k_1\}$ 与 $\{N_{t_3} - N_{t_4} = k_2\}$ 独立;
- 平稳增量性: 对任意的 $s, t \geqslant 0$ 有 $\mathbf{P}(N_{s+t} - N_s = k) = P_k(t)$;
- 普通性: 当 $t \to 0$ 时有

$$
1 - P _ {0} (t) - P _ {1} (t) = \sum_ {k = 2} ^ {\infty} P _ {k} (t) = o (t).
$$

假定上面三个条件成立. 因为 $t \mapsto N_t$ 是右连续不降整数值阶梯函数, 由全概率公式和独立平稳增量性, 对于 $n \geqslant 0$ 和 $t, s > 0$,

$$
\begin{array}{l} \mathbf {P} \left(N _ {t + s} = n\right) = \sum_ {k = 0} ^ {n} \mathbf {P} \left(N _ {s} = k\right) \mathbf {P} \left(N _ {t + s} = n \mid N _ {s} = k\right) \\ = \sum_ {k = 0} ^ {n} \mathbf {P} \left(N _ {s} = k\right) \mathbf {P} \left(N _ {t + s} - N _ {s} = n - k \mid N _ {s} = k\right) \\ = \sum_ {k = 0} ^ {n} \mathbf {P} \left(N _ {s} = k\right) \mathbf {P} \left(N _ {t + s} - N _ {s} = n - k\right) \\ = \sum_ {k = 0} ^ {n} \mathbf {P} (N _ {s} = k) \mathbf {P} (N _ {t} = n - k). \\ \end{array}
$$

因此有方程

$$
P _ {n} (t + s) = \sum_ {k = 0} ^ {n} P _ {n - k} (t) P _ {k} (s). \tag {2.2.11}
$$

基于方程 (2.2.11), 我们可以证明:

定理 2.2.4 在前面三个假定条件之下, 存在  $\lambda > 0$  使对任意 t > 0 有

$$
P _ {n} (t) = \frac {(\lambda t) ^ {n}}{n !} \mathrm{e} ^ {- \lambda t}, \quad n = 0, 1, 2, \dots . \tag {2.2.12}
$$

证明 第1步. 根据方程(2.2.11), 对 $t > 0, \delta > 0$ 有

$$
P _ {0} (t + \delta) = P _ {0} (t) P _ {0} (\delta). \tag {2.2.13}
$$

反复应用上式得 $P_0(nt) = P_0(t)^n$ ，故 $P_0(t / n) = P_0(t)^{1 / n}$ ，进而有

$$
P _ {0} (k / n) = P _ {0} (1 / n) ^ {k} = P _ {0} (1) ^ {k / n}, \quad n \geqslant 1, k \geqslant 0.
$$

由 (2.2.13) 式知 $P_0(t)$ 关于 $t \geqslant 0$ 单调减, 故得 $P_0(t) = P_0(1)^t$.

第2步. 往证 $P_0(1) > 0$. 若此结论不成立, 则对任何 $t > 0$ 有 $P_0(t) = P_0(1)^t = 0$, 故

$$
\mathbf {P} (N _ {t} \geqslant 1) = 1 - \mathbf {P} (N _ {t} = 0) = 1 - P _ {0} (t) = 1.
$$

注意

$$
\{N _ {t} \geqslant n \} \supseteq \bigcap_ {k = 1} ^ {n} \{N _ {k t / n} - N _ {(k - 1) t / n} \geqslant 1 \}.
$$

故由独立增量性和平稳增量性有

$$
\begin{array}{l} \mathbf {P} (N _ {t} \geqslant n) \geqslant \mathbf {P} \left(\bigcap_ {k = 1} ^ {n} \left\{N _ {k t / n} - N _ {(k - 1) t / n} \geqslant 1 \right\}\right) \\ = \prod_ {k = 1} ^ {n} \mathbf {P} \left(N _ {k t / n} - N _ {(k - 1) t / n} \geqslant 1\right) \\ = \prod_ {k = 1} ^ {n} \mathbf {P} \left(N _ {t / n} \geqslant 1\right) = \left[ 1 - P _ {0} (t / n) \right] ^ {n} = 1. \\ \end{array}
$$

再由概率的上连续性得 $\mathbf{P}(N_t = \infty) = \lim_{n\to \infty}\mathbf{P}(N_t\geqslant n) = 1,$ 这与 $N_{t}$ 几乎必然有限的假定矛盾.所以 $P_0(1) > 0$

第3步. 令 $\lambda = -\ln P_0(1)$. 则 $P_0(t) = \mathrm{e}^{-\lambda t}$, 即欲证等式 (2.2.12) 对于 $n = 0$ 成立. 设 (2.2.12) 式对 $n - 1$ 成立. 由普通性, 当 $\delta \to 0$ 时有

$$
\sum_ {k = 2} ^ {n} P _ {n - k} (t) P _ {k} (\delta) \leqslant \sum_ {k = 2} ^ {\infty} P _ {k} (\delta) = o (\delta),
$$

故由 (2.2.11) 式得

$$
P _ {n} (t + \delta) = P _ {n} (t) P _ {0} (\delta) + P _ {n - 1} (t) P _ {1} (\delta) + o (\delta). \tag {2.2.14}
$$

根据泰勒展开式有

$$
P _ {0} (\delta) = \mathrm{e} ^ {- \lambda \delta} = 1 - \lambda \delta + o (\delta),
$$

再次应用普通性得

$$
P _ {1} (\delta) = 1 - P _ {0} (\delta) - \sum_ {i = 2} ^ {\infty} P _ {i} (\delta) = \lambda \delta + o (\delta),
$$

回到 (2.2.14) 式得

$$
P _ {n} (t + \delta) = P _ {n} (t) [ 1 - \lambda \delta ] + P _ {n - 1} (t) \lambda \delta + o (\delta),
$$

从而有

$$
\frac {[ P _ {n} (t + \delta) - P _ {n} (t) ]}{\delta} + \lambda P _ {n} (t) = \lambda P _ {n - 1} (t) + o (1).
$$

令 $\delta \to 0$ ，并利用归纳假设得

$$
P _ {n} ^ {\prime} (t) + \lambda P _ {n} (t) = \frac {\lambda^ {n} t ^ {n - 1}}{(n - 1) !} \mathrm{e} ^ {- \lambda t}.
$$

注意对 $n \geqslant 1$ 有 $P_{n}(0) = 0$, 求解上述微分方程得到

$$
P _ {n} (t) = \frac {(\lambda t) ^ {n}}{n !} \mathrm{e} ^ {- \lambda t}.
$$

根据数学归纳法知 (2.2.12) 式对任意 $n \geqslant 0$ 成立.

根据定理2.2.4, 对于任何 $\delta > 0$ 有 $P_0(\delta) = \mathrm{e}^{-\lambda \delta}$ 和 $P_1(\delta) = \lambda \delta \mathrm{e}^{-\lambda \delta}$, 因而对 $t > 0$ 有

$$
\mathbf {P} (N _ {t} - N _ {t - \delta} = 1 | N _ {t} - N _ {t - \delta} \geqslant 1) = \frac {\lambda \delta \mathrm{e} ^ {- \lambda \delta}}{1 - \mathrm{e} ^ {- \lambda \delta}} \rightarrow 1, \quad \delta \rightarrow 0.
$$

这说明, 若在某时刻 $t > 0$ 有粒子到达, 则到达的粒子数几乎必然为 1 个.

基于定理 2.2.4 的结论, 我们自然地给出下面的定义.

定义2.2.1 称随机变量族 $(N_{t}:t\geqslant 0)$ 是参数为 $\lambda \geqslant 0$ 的泊松过程, 是指当 $\omega \in \Omega$ 固定后 $t\mapsto N_t(\omega)$ 是右连续不降整数值阶梯函数, 且下面两个性质成立:

(i) 对任何 $s, t \geqslant 0$, 增量 $N_{s + t} - N_s$ 服从参数为 $\alpha t$ 的泊松分布, 即

$$
\mathbf {P} (N _ {s + t} - N _ {s} = k) = \frac {\lambda^ {k} t ^ {k}}{k !} \mathrm{e} ^ {- \lambda t}, \quad k = 0, 1, 2, \dots ; \tag {2.2.15}
$$

(ii) 对任何 $0 = t_0 < t_1 < \cdots < t_n$ 及 $k_1, k_2, \cdots, k_n \geqslant 0$, 随机事件 $\{N_{t_1} = k_1\}, \{N_{t_2} - N_{t_1} = k_2\}, \cdots, \{N_{t_n} - N_{t_{n-1}} = k_n\}$ 相互独立.

泊松过程由法国数学家泊松 (Siméon-Denis Poisson, 1781—1840) 提出. 该模型在应用中经常出现. 例如, 其取值 $N_{t}$ 常被视为某个服务系统在 $t \geqslant 0$ 时刻前接到的服务请求的次数, 而过程的第 $n$ 次跳跃发生的时间 $S_{n}$ 可理解为第 $n$ 次服务请求的时刻. 关于泊松过程的构造和性质, 我们将在本书下册做更详细的讨论.

## 练习题

1. 设某市不同路口的红绿灯独立工作, 每个路口的红灯、绿灯出现的时间相同. 用 X 表示一辆汽车首次遇到红灯时已经经过的路口数. 求 X 的概率分布.
2. 用 $\xi$ 表示成功概率为 $p (0 \leqslant p \leqslant 1)$ 的伯努利实验中第一个游程（即连续成功或连续失败）的长度. 求 $\xi$ 的分布.

3. 连续射击某个目标, 直至第一次击中目标或者射击次数达到 5 次就停止. 假定一次射击击中目标的概率为 $p (0 \leqslant p \leqslant 1)$ 且各次射击结果独立. 用 $X$ 表示停止时的射击次数. 求 $X$ 的概率分布.

4. 某种昆虫在单位时间内产卵的个数 $\xi$ 服从泊松分布 $P(\lambda)$, 其中每个卵孵化出幼虫的概率为 $p$, 各个卵是否孵化相互独立, 并且虫子产卵的个数和产出卵是否孵化相互独立. 以 $\eta$ 表示单位时间内幼虫的个数. 求 $\eta$ 的概率分布.

5. 设随机变量 $X$ 服从泊松分布 $P(\lambda)$. 记 $p = \mathbf{P}(X$ 为奇数) 和 $q = \mathbf{P}(X$ 为偶数). 证明:

$$
p = \mathrm{e} ^ {- \lambda} \sinh \lambda = \frac {1}{2} (1 - \mathrm{e} ^ {- 2 \lambda}), \quad q = \mathrm{e} ^ {- \lambda} \cosh \lambda = \frac {1}{2} (1 + \mathrm{e} ^ {- 2 \lambda}).
$$

提示: 注意  $q + p = 1$  和  $q - p = e^{-2\lambda}$ .

## 2.3 绝对连续型随机变量

称随机变量 $\xi$ 是绝对连续型的, 是指它具有绝对连续型概率分布函数 $F$, 即 $F$ 可以表示为

$$
F (x) = \int_ {- \infty} ^ {x} p (u) \mathrm{d} u, \quad x \in \mathbb {R}, \tag {2.3.1}
$$

其中 $p$ 为 $F$ 的密度函数, 它是 $\mathbb{R}$ 上的非负可积函数且满足

$$
\int_ {- \infty} ^ {\infty} p (u) \mathrm{d} u = 1.
$$

我们也将 $p$ 称为 $\xi$ 的分布密度或密度. 注意

$$
\mathbf {P} (a \leqslant \xi \leqslant b) = \int_ {a} ^ {b} p (u) \mathrm{d} u, \quad a \leqslant b \in \mathbb {R}.
$$

显然 $\xi$ 取任何一个固定值 $a \in \mathbb{R}$ 的概率为零. 特别地, 若密度函数 $p$ 在点 $x \in \mathbb{R}$ 连续, 则当 $\delta \to 0$ 时,

$$
\mathbf {P} (x - \delta / 2 \leqslant \xi \leqslant x + \delta / 2) = \int_ {x - \delta / 2} ^ {x + \delta / 2} p (u) \mathrm{d} u = p (x) \delta + o (\delta).
$$

可见  $p(x)$  的值反映了  $\xi$  落入 x 附近的概率的大小.

若有集合 $E \in \mathcal{B}$ 使当 $x \in E^c$ 有 $p(x) = 0$, 也说 $\xi$ 是集合 $E$ 上的绝对连续型随机变量. 此时

$$
\mathbf {P} (a \leqslant \xi \leqslant b) = \int_ {[ a, b ] \cap E} p (u) \mathrm{d} u, \quad a \leqslant b \in \mathbb {R}.
$$

对于绝对连续型随机变量的概率问题, 通常可以借助定积分的理论进行处理. 对于包括绝对连续型随机变量在内的一般随机变量的严格构造, 我们将在下节进行系统的讨论. 本节下面介绍几种常见的绝对连续型分布.

## 2.3.1 均匀分布

定义 2.3.1 给定实数 a < b, 定义

$$
p (x) = \left\{ \begin{array}{l l} { \frac {1}{b - a},} & {a <   x <   b,} \\ {0,} & {x \leqslant a \text {或} x \geqslant b.} \end{array} \right.
$$

以此函数为密度的绝对连续型分布称为区间 $(a,b)$ 上的均匀分布，记作 $U(a,b)$.

均匀分布 $U(a,b)$ 描述的就是区间 $(a,b)$ 上的几何概率模型. 由(2.3.1)式得到均匀分布 $U(a,b)$ 的分布函数为

$$
F (x) = \left\{ \begin{array}{l l} 0, & x <   a, \\ \frac {x - a}{b - a}, & a \leqslant x <   b, \\ 1, & x \geqslant b. \end{array} \right.
$$

## 2.3.2 指数分布

假设 $\{N_{t}:t\geqslant 0\}$ 是以 $\lambda >0$ 为参数的泊松过程，且有 $N_0 = 0$ ，它描述了某个随机粒子流的粒子数的变化过程.令 $\tau$ 为第一个粒子的到达时间.显然 $\tau$ 的分布函数 $F$ 满足

$$
F (x) = \mathbf {P} (\tau \leqslant x) = \mathbf {P} (N _ {x} \geqslant 1) = 1 - \mathrm{e} ^ {- \lambda x}, \quad x > 0.
$$

对上式求导得到 $\tau$ 的密度函数

$$
p (x) = \lambda \mathrm{e} ^ {- \lambda x}, \quad x > 0. \tag {2.3.2}
$$

称以 (2.3.2) 式为密度的绝对连续型分布为指数分布, 记作 $E(\lambda)$.

定理2.3.1 取值于非负实数的随机变量 $\tau$ 服从指数分布当且仅当对任意的 $t \geqslant 0, s \geqslant 0$ 有

$$
\mathbf {P} (\tau > s + t | \tau > t) = \mathbf {P} (\tau > s). \tag {2.3.3}
$$

证明 “$\Rightarrow$” 假设 $\tau$ 服从指数分布, 则对任意的 $t \geqslant 0$ 有 $\mathbf{P}(\tau > t) = \mathrm{e}^{-\lambda t}$, 故 (2.3.3) 式成立.

“$\Leftarrow$”假设(2.3.3)式成立.记 $f(s) = \mathbf{P}(\tau >s)$, 则 $s\mapsto f(s)$ 单调减.根据(2.3.3)式得 $f(s + t) = f(s)f(t)$, 故有

$$
f (n s) = f (s) ^ {n}, f (s) = f (s / n) ^ {n}, f (s / n) = f (s) ^ {1 / n}.
$$

这样, 对任何非负有理数 $m / n$ 有

$$
f (m / n) = f (1 / n) ^ {m} = f (1) ^ {m / n}.
$$

再利用 $f$ 的单调性, 对任何非负实数 $s$ 有

$$
f (s) = f (1) ^ {s} = \mathrm{e} ^ {s \ln f (1)} = \mathrm{e} ^ {- \lambda s},
$$

其中  $\lambda = -\ln f(1) \geqslant 0.$

由 (2.3.3) 式表达的性质称为指数分布的无记忆性. 该分布经常被用作寿命的模型, 而无记忆性可以解释为 “永远年轻”.

## 2.3.3 伽马分布

假设 $\{N_{t}:t\geqslant 0\}$ 是泊松过程, 考虑第 $n$ 个粒子的到达时间 $S_{n}$. 显然 $S_{n}$ 的分布函数 $F$ 满足

$$
F (t) = \mathbf {P} (S _ {n} \leqslant t) = \mathbf {P} (N _ {t} \geqslant n) = \sum_ {k = n} ^ {\infty} \frac {(\lambda t) ^ {k}}{k !} \mathrm{e} ^ {- \lambda t}, \quad t > 0,
$$

求导得到

$$
F ^ {\prime} (t) = \sum_ {k = n} ^ {\infty} \frac {\lambda^ {k} t ^ {k - 1}}{(k - 1) !} \mathrm{e} ^ {- \lambda t} - \sum_ {k = n} ^ {\infty} \frac {\lambda^ {k + 1} t ^ {k}}{k !} \mathrm{e} ^ {- \lambda t}.
$$

所以上述分布有密度函数

$$
p (t) = \frac {\lambda^ {n} t ^ {n - 1}}{(n - 1) !} \mathrm{e} ^ {- \lambda t}, \quad t > 0.
$$

上面的观察导出一类重要的绝对连续型概率分布. 我们先来回忆伽马 (Gamma) 函数的定义

$$
\Gamma (r) = \int_ {0} ^ {\infty} x ^ {r - 1} \mathrm{e} ^ {- x} \mathrm{d} x, \quad r > 0.
$$

所以对任何 $\lambda > 0$ 有

$$
\frac {\lambda^ {r}}{\Gamma (r)} \int_ {0} ^ {\infty} x ^ {r - 1} \mathrm{e} ^ {- \lambda x} \mathrm{d} x = \frac {1}{\Gamma (r)} \int_ {0} ^ {\infty} y ^ {r - 1} \mathrm{e} ^ {- y} \mathrm{d} y = 1.
$$

定义2.3.2 称一个绝对连续型概率分布为以 $\lambda, r > 0$ 为参数的伽马分布，并记作 $\Gamma(\lambda, r)$，是指它有密度函数

$$
p (x) = \frac {\lambda^ {r}}{\Gamma (r)} x ^ {r - 1} \mathrm{e} ^ {- \lambda x}, \quad x > 0. \tag {2.3.4}
$$

例2.3.1 伽马函数具有如下的基本性质:

$$
\Gamma (r + 1) = r \Gamma (r), \quad r > 0.
$$

特别地, 若 $n \geqslant 1$ 为整数, 则

$$
\Gamma (n + 1) = n \Gamma (n) = \dots = n!.
$$

另外有

$$
\Gamma \Big (\frac {1}{2} \Big) = \int_ {0} ^ {\infty} x ^ {- 1 / 2} \mathrm{e} ^ {- x} \mathrm{d} x = \sqrt {2} \int_ {0} ^ {\infty} \mathrm{e} ^ {- t ^ {2} / 2} \mathrm{d} t = \sqrt {\pi}.
$$

显然, 指数分布 $E(\lambda)$ 是伽马分布 $\Gamma(\lambda, r)$ 当 $r = 1$ 时的特例. 事实上, 指数分布与伽马分布的关系类似于几何分布与帕斯卡分布的关系.

## 2.3.4 正态分布

给定常数 $a \in \mathbb{R}$ 和 $\sigma > 0$, 我们定义函数

$$
\phi_ {a, \sigma} (x) = \frac {1}{\sigma \sqrt {2 \pi}} \mathrm{e} ^ {- \frac {(x - a) ^ {2}}{2 \sigma^ {2}}}, \quad x \in \mathbb {R}.
$$

利用广义积分的计算可以证明:

$$
\int_ {- \infty} ^ {\infty} \phi_ {a, \sigma} (x) \mathrm{d} x = 1.
$$

定义2.3.3 对于 $a \in \mathbb{R}$ 和 $\sigma > 0$, 以 $\phi_{a, \sigma}(x)$ 为密度函数的绝对连续型分布称为参数为 $(a, \sigma^2)$ 的正态分布或高斯 (Gauss) 分布, 记作 $N(a, \sigma^2)$. 称 $N(0,1)$ 为标准正态分布.

为了叙述上的方便, 人们也经常把分布函数 $F(x) \equiv 1_{\{x \geqslant a\}}$ 确定的离散型概率分布解释为对应于 $\sigma = 0$ 的正态分布, 即退化正态分布.

不难发现, 正态分布的密度函数  $\phi_{a,\sigma}(x)$  有如下性质:

- 此分布关于 $x = a$ 对称, 即有 $\phi_{a,\sigma}(a - x) = \phi_{a,\sigma}(a + x), x \in \mathbb{R}$.
- 函数 $\phi_{a,\sigma}$ 最大值在 $x = a$ 取到, 且 $\max \phi_{a,\sigma}(x) = 1 / (\sigma \sqrt{2\pi})$.
- 数 $\sigma^2$ 越大密度函数的图像越平缓; 数 $\sigma^2$ 越小密度函数的图像越陡峭.

定义正态分布 $N(a,\sigma^2)$ 的分布函数

$$
\varPhi_ {a, \sigma} (x) = \int_ {- \infty} ^ {x} \phi_ {a, \sigma} (y) \mathrm{d} y, \quad x \in \mathbb {R}. \tag {2.3.5}
$$

特别地, 我们分别用 $\phi := \phi_{0,1}$ 和 $\Phi := \Phi_{0,1}$ 表示标准正态分布 $N(0,1)$ 的密度函数和分布函数. 易见正态分布函数具有如下性质:

$$
\varPhi_ {a, \sigma} (x) = \varPhi \Big (\frac {x - a}{\sigma} \Big), \quad \varPhi (x) + \varPhi (- x) = 1, \quad x \in \mathbb {R}.
$$

一般地, 受大量微小因素叠加影响的随机变量服从正态分布, 我们将在第五章给出这个说法的严格数学解释.

例 2.3.2 (3σ 原则) 设随机变量  $\xi$  服从正态分布  $N(a, \sigma^{2})$ . 由 (2.3.5) 式计算可以得到

$$
\begin{array}{l} \mathbf {P} (| \xi - a | \leqslant \sigma) = 0. 6 8 2 6, \quad \mathbf {P} (| \xi - a | \leqslant 2 \sigma) = 0. 9 5 4 4, \\ \mathbf {P} (| \xi - a | \leqslant 3 \sigma) = 0. 9 9 7 4. \\ \end{array}
$$

可见  $\xi$  的取值主要集中于 a 附近.

例2.3.3 注意标准正态分布 $N(0,1)$ 的密度函数满足 $\phi'(x) = -x\phi(x)$. 设随机变量 $\xi$ 服从分布 $N(0,1)$. 根据分部积分公式, 对任何 $x > 0$ 有

$$
\mathbf {P} (\xi \geqslant x) = \int_ {x} ^ {\infty} \phi (z) \mathrm{d} z = \frac {\phi (x)}{x} - \int_ {x} ^ {\infty} \frac {\phi (z) \mathrm{d} z}{z ^ {2}} \geqslant \frac {\phi (x)}{x} - \frac {1}{x ^ {2}} \mathbf {P} (\xi \geqslant x).
$$

所以有

$$
\mathbf {P} (\xi \geqslant x) \geqslant \frac {x \phi (x)}{1 + x ^ {2}}.
$$

此式给出了概率 $\mathbf{P}(\xi \geqslant x)$ 的一个非常有用的下界估计.

正态分布是对数学、统计学、物理及工程等领域都非常重要的一种概率分布. 该分布最早由法国裔英国籍的数学家棣莫弗 (Abraham de Moivre, 1667—1754) 在求二项分布的渐近公式中得到. 德国数学家高斯 (Carolus Fridericus Gauss, 1777—1855) 在研究测量误差时从另一个角度导出了正态分布, 并系统地讨论了它的性质.

## 练习题

1. 设 $\xi$ 为绝对连续型随机变量. 证明对任意的 $a \in \mathbb{R}$ 有 $\mathbf{P}(\xi = a) = 0$.
2. 设 $f, g$ 都是 $\mathbb{R}$ 上的概率分布密度函数, 而 $p, q \in [0,1]$ 满足 $p + q = 1$. 证明 $pf + qg$ 是 $\mathbb{R}$ 上的概率分布密度函数.

3. 设绝对连续型随机变量 $X$ 的密度函数 $p$ 满足

$$
p (x) = \left\{ \begin{array}{l l} 2 a x, & 0 \leqslant x <   1, \\ 2 - x, & 1 \leqslant x <   2, \\ 0, & \text {其他.} \end{array} \right.
$$

求常数 $a$ 和概率 $\mathbf{P}(X < 3 / 2)$.

4. 设 $\mathbb{R}$ 上的绝对连续型随机变量 $\xi$ 有密度函数 $f(x) = \mathrm{e}^{-x - \mathrm{e}^{-x}}$. 求 $\xi$ 的分布函数 $F$ (称为极值分布).
5. 设随机变量 $\xi$ 服从标准正态分布 $N(0,1)$. 令 $X = \sigma \xi + a$, 其中 $\sigma \neq 0$ 和 $a$ 为常数. 证明 $X$ 服从正态分布 $N(a, \sigma^2)$.
6. 设随机变量  $\xi$  服从指数分布  $E(\lambda)$ . 求  $\eta = \lfloor \xi \rfloor + 1$  的分布.

## 2.4 概率分布函数的实现与分解

本节讨论概率分布函数的两个基本问题, 即可实现性和分解定理. 在命题 2.2.1 中我们给出了离散型随机变量的构造. 那么, 任给 R 上的概率分布函数 F, 是否必然存在以其为分布函数的随机变量  $\xi$  呢? 如果存在, 我们就称  $\xi$  为 F 的一个实现.

命题2.4.1 取 $\Omega = (0,1)$, 令 $\mathcal{F} = (0,1) \cap \mathcal{B} = \{(0,1) \cap B : B \in \mathcal{B}\}$, 再令 $\mathbf{P}$ 为 $(\Omega, \mathcal{F})$ 上的勒贝格测度. 对于 $\omega \in \Omega$ 令 $\eta(\omega) = \omega$. 则 $(\Omega, \mathcal{F}, \mathbf{P})$ 是概率空间, 而 $\eta$ 是服从均匀分布 $U(0,1)$ 的随机变量.

上面命题的证明很简单, 请大家自行完成.

例2.4.1 设随机变量 $\eta$ 服从均匀分布 $U(0,1)$. 对实数 $a < b$, 令 $\xi = a + (b - a)\eta$. 则 $a < \xi < b$ 且有

$$
F _ {\xi} (x) = \mathbf {P} (\xi \leqslant x) = \mathbf {P} \Big (\eta \leqslant \frac {x - a}{b - a} \Big) = \frac {x - a}{b - a}, \quad a <   x <   b.
$$

故 $\xi$ 服从均匀分布 $U(a,b)$

上例启发我们, 从服从均匀分布 $U(0,1)$ 的随机变量出发, 构造具有一般分布函数的随机变量. 为此需要用到不降函数的广义逆.

## 2.4.1 不降函数的广义逆

给定非空开区间 $(a,b)\subseteq \mathbb{R}$ 上的不降函数 $G$ ，令 $\alpha = G(a+)$ 和 $\beta = G(b-)$ .若区间

$(\alpha,\beta)$  非空, 令

$$
G ^ {- 1} (y) = \inf \{x \in (a, b): y \leqslant G (x) \}, \quad \alpha <   y <   \beta . \tag {2.4.1}
$$

称 $G^{-1}$ 为 $G$ 的广义逆.

命题2.4.2 设 $F$ 为 $\mathbb{R}$ 上的右连续不降函数且满足 $F(-\infty) = 0$ 和 $F(\infty) = 1$. 则如下性质成立:

(1) 对任何  $y \in (0,1)$  有  $F(F^{-1}(y)) \geqslant y;$
(2) 对 $x \in \mathbb{R}$ 和 $y \in (0,1)$ 有 $F^{-1}(y) \leqslant x \Leftrightarrow y \leqslant F(x)$, 进而 $x < F^{-1}(y) \Leftrightarrow F(x) < y$;
(3) $F^{-1}$  在  $(0,1)$  上不降且左连续;
(4) 若 F 在 x 处有跳跃, 则  $F^{-1}$  在区间  $[F(x-), F(x)]$  上恒等于 x;
(5) 若 $F$ 在非空区间 $(a, b)$ 上恒等于 $y$, 则 $F^{-1}$ 在点 $y$ 处有跳幅不小于 $b - a$ 的跳跃;
(6) 若 $F^{-1}$ 在 $y$ 处连续, 则当 $F^{-1}(y) < z$ 时有 $y < F(z)$, 而当 $z < F^{-1}(y)$ 时有 $F(z) < y$.

证明 (1) 记 $x_0 = F^{-1}(y)$. 由 (2.4.1) 式可取 $x_n \downarrow x_0$ 满足 $F(x_n) \geqslant y$. 再由 $F$ 的右连续性知

$$
F (x _ {0}) = \lim _ {n \to \infty} F (x _ {n}) \geqslant y.
$$

(2) 若 $F^{-1}(y) \leqslant x$, 则 $F(F^{-1}(y)) \leqslant F(x)$. 再由 (1) 得 $y \leqslant F(x)$. 反之, 若 $y \leqslant F(x)$, 则由 (2.4.1) 式得 $F^{-1}(y) \leqslant x$.

(3) 显然 $F^{-1}$ 在 $(0,1)$ 内不降. 任取 $(0,1) \ni y_n \uparrow y$. 则 $F^{-1}(y_n) \leqslant F^{-1}(y)$ 且 $\{F^{-1}(y_n)\}$ 不降. 故存在极限 $z := \lim_{n \to \infty} F^{-1}(y_n)$. 显然 $F^{-1}(y_n) \leqslant z \leqslant F^{-1}(y)$. 因 $F$ 不降, 再利用 (2) 中所证结果有 $F(z) \geqslant F(F^{-1}(y_n)) \geqslant y_n$. 令 $n \to \infty$ 得 $F(z) \geqslant y$. 由 (2.4.1) 式有 $z \geqslant F^{-1}(y)$. 综上得 $z = F^{-1}(y)$.

(4) 和 (5) 由图 2.1 易见.

![](images/page_73_chart_18.jpg)

<details>
<summary>line</summary>

| X | Y |
| --- | --- |
| ~0.25 | ~0.35 |
| ~0.65 | ~0.65 |
</details>

图 2.1 函数  $F: x \mapsto y$  (黑色) 和广义逆  $F^{-1}: y \mapsto X$  (蓝色)

(6) 设 $F^{-1}$ 在 $y$ 处连续且 $F^{-1}(y) < z$. 显然有 $y \leqslant F(z)$. 假若 $y = F(z)$, 则 $F$ 在 $[F^{-1}(y), z]$ 上恒等于 $y$. 由 (5) 这与 $F^{-1}$ 在 $y$ 处连续相矛盾. 根据反证法有 $y < F(z)$. 类似地, 当 $z < F^{-1}(y)$ 时有 $F(z) < y$.

## 2.4.2 随机变量的构造

我们前面已经严格构造了服从均匀分布的随机变量. 从服从均匀分布 $U(0,1)$ 的随机变量出发, 可以构造出具有任意给定分布函数的随机变量. 这就是下面定理的结果.

定理2.4.3 设 $F$ 为 $\mathbb{R}$ 上的右连续不降函数且满足 $F(-\infty) = 0$ 和 $F(\infty) = 1$ 而 $\eta$ 是服从均匀分布 $U(0,1)$ 的随机变量. 则 $\xi := F^{-1}(\eta)$ 是随机变量且具有分布函数 $F$, 因而 $F$ 是概率分布函数.

证明 由推论2.1.6知不降函数 $F^{-1}$ 可测，再由定理2.1.8知 $\xi = F^{-1}(\eta)$ 为随机变量.根据命题2.4.2(2)，对任何 $x\in \mathbb{R}$ 有

$$
\mathbf {P} (\xi \leqslant x) = \mathbf {P} \{F ^ {- 1} (\eta) \leqslant x \} = \mathbf {P} \{\eta \leqslant F (x) \} = F (x).
$$

所以 $\xi$ 有分布函数 $F$.

例2.4.2 指数分布 $E(1)$ 的分布函数为 $F(x) = 1 - \mathrm{e}^{-x}, x > 0$. 易知

$$
F ^ {- 1} (y) = - \ln (1 - y), \quad y \in (0, 1).
$$

设 $\eta$ 服从分布 $U(0,1)$. 则 $-\ln (1 - \eta)$ 服从分布 $E(1)$.

例 2.4.3 标准正态分布  $N(0,1)$  的分布函数  $\Phi$  严格单增, 故必有反函数  $\Phi^{-1}$ . (该反函数无显示表达, 但其取值可以通过反查正态分布表得到.) 若  $\eta$  服从分布  $U(0,1)$ , 则  $\xi := \Phi^{-1}(\eta)$  服从分布  $N(0,1)$ .

例2.4.4 定理2.4.3的结论提供了人工生成具有任意分布函数 $F$ 的随机变量的方法.这可分成下面的步骤来实现:

(1) 在  $0,1,\cdots,9$  中有放回地随机抽取 n 个数  $a_{1},a_{2},\cdots,a_{n}$ ;
(2) 构造小数  $\eta_{n}=0.a_{1}a_{2}\cdots a_{n}$ . 则  $\eta_{n}$  近似服从分布  $U(0,1)$ ，且 n 越大精度越高；
(3) 定义  $\xi_{n}=F^{-1}(\eta_{n})$ . 则  $\xi_{n}$  为分布函数近似于 F 的随机变量.

## 2.4.3 有限测度的构造

定理2.4.4 设 $G$ 为 $\mathbb{R}$ 上的有界右连续不降函数. 则存在 $(\mathbb{R},\mathcal{B})$ 上的唯一的有限测度 $\mu$ 以 $G$ 为分布函数.

证明 不妨设 $G(-\infty) = 0$。当 $G(\infty) = 0$ 时，定理的结论显然成立。下面考虑 $G(\infty) > 0$ 的情况。令 $F(x) = G(\infty)^{-1}G(x), x \in \mathbb{R}$。则 $F$ 右连续不降且满足 $F(-\infty) = 0$ 和 $F(\infty) = 1$。根据定理2.4.3，存在 $(\mathbb{R}, \mathcal{B})$ 上概率测度 $\mu$ 以 $F$ 为分布函数。显然 $\nu := G(\infty)\mu$ 是 $(\mathbb{R}, \mathcal{B})$ 上的以 $G$ 为分布函数的有限测度，其唯一性由定理2.1.13保证。

上面的定理说明 $\mathbb{R}$ 上的任何有界右连续不降函数都是某个有限测度的分布函数. 基于该定理, 可以证明 $\mathbb{R}$ 上的任何右连续不降函数都是某个局部有限测度的分布函数.

## \*2.4.4 概率分布函数的分解

前面介绍过两种典型的概率分布函数, 即离散型和绝对连续型的分布函数. 我们称分布函数 $F$ 是奇异连续型的, 是指 $F$ 连续, $F'$ 几乎处处存在且为零 (即使 $F'(x) \neq 0$ 的所有点 $x$ 构成的集合的勒贝格测度为零). 下面的定理给出了概率分布函数的基本结构的描述.

定理 2.4.5（勒贝格分解）任何概率分布函数 F 有唯一的如下形式的分解:

$$
F (x) = C _ {1} F _ {1} (x) + C _ {2} F _ {2} (x) + C _ {3} F _ {3} (x), \quad x \in \mathbb {R}, \quad C _ {1}, C _ {2}, C _ {3} \geqslant 0 \text {且} C _ {1} + C _ {2} + C _ {3} = 1
$$

其中 $F_{1}$ 是离散型概率分布函数, $F_{2}$ 是绝对连续型概率分布函数, 而 $F_{3}$ 是奇异绝对连续型概率分布函数.

对于上面定理的证明感兴趣的读者, 可以参考实分析方面的著作, 如见 [10, pp.335-337].

例 2.4.5 如图 2.2 所示, 利用著名的康托尔 (Cantor) 集合, 可以分步构造单位区间 [0,1] 上的康托尔函数 F 如下:

$$
F (x) = \frac {1}{2}, x \in \left[ \frac {1}{3}, \frac {2}{3} \right]; F (x) = \left\{ \begin{array}{l l} \frac {1}{2 ^ {2}}, & x \in \left[ \frac {1}{3 ^ {2}}, \frac {2}{3 ^ {2}} \right], \\ \frac {1}{2} + \frac {1}{2 ^ {2}}, & x \in \left[ \frac {2}{3} + \frac {1}{3 ^ {2}}, \frac {2}{3} + \frac {2}{3 ^ {2}} \right]; \end{array} \right. \dots .
$$

可以证明, 函数 $F$ 在 $[0,1]$ 上连续不降, 且有 $F(0+) = 0$ 和 $F(1-) = 1$. 因此可以将其扩张为 $\mathbb{R}$ 上的概率分布函数.

![](images/page_75_image_11.jpg)

图 2.2 康托尔函数的构造

另外, 显然满足  $\dot{F}^{\prime}(x)=0$  的点  $x\in[0,1]$  构成的集合 U 的勒贝格测度为

$$
m (U) = \frac {1}{3} + \frac {2}{3 ^ {2}} + \dots + \frac {2 ^ {n - 1}}{3 ^ {n}} + \dots = 1.
$$

所以 F 的如上扩张是奇异型的概率分布函数.

## 练习题

1. 设随机变量  $\xi$  服从均匀分布  $U(0,1)$ . 求方程  $x^{2} + 3\xi x + 1 = 0$  有实根的概率.
2. 设 $F$ 为 $\mathbb{R}$ 上的概率分布函数. 定义

$$
\hat {F} (x) = 1 - F ((- x) -), \tilde {F} (x) = \frac {1}{2} [ F (x) + \hat {F} (x) ], \quad x \in \mathbb {R}.
$$

证明  $\hat{F}$  和  $\tilde{F}$  都是 R 上的概率分布函数.

3. 在上题的情况下, 设随机变量 $X, \hat{X}$ 和 $\tilde{X}$ 分别具有概率分布函数 $F, \hat{F}$ 和 $\tilde{F}$. 证明: 对任何 $a \in \mathbb{R}$ 有 $\mathbf{P}(X \geqslant a) = \mathbf{P}(\hat{X} \leqslant -a)$ 和 $\mathbf{P}(\tilde{X} \geqslant a) = \mathbf{P}(\tilde{X} \leqslant -a)$.
4. 设 $X$ 是取值于非空区间 $(0, a)$ 的随机变量且有连续的分布函数. 再设对任何子区间 $(b, c) \subseteq (0, a)$ 概率 $\mathbf{P}(b < X < c)$ 只和区间长度 $c - b$ 有关. 求 $X$ 的分布.
5. 设一个质点在零时刻从原点出发, 在数轴的整数点上进行随机游动, 每个单位时间移动一格, 每次向右移动的概率为 $p (0 \leqslant p \leqslant 1)$, 向左移动的概率为 $1 - p$, 且每次的移动相互独立. 用 $X_{n}$ 表示 $n$ 时刻质点所处的位置. 对 $0 \leqslant k \leqslant n$ 求概率 $\mathbf{P}(X_{n} = k)$.

## 第三章

## 随机向量和独立性

在随机现象的描述中, 我们经常需要同时考虑多个随机变量. 将多个随机变量组合起来, 就得到了随机向量, 也称为多维或高维随机变量. 从抽象的角度看, 随机向量与随机变量都是可测函数, 后者的分布是多维欧氏空间上的概率测度, 有更丰富的结构和性质. 本章介绍随机向量的联合分布、边缘分布、条件分布与独立性、随机向量的函数等基本概念和性质, 并分别讨论离散型和绝对连续型随机向量的典型例子.

## 3.1 随机向量与联合分布

对于随机向量, 经常需要研究它们的联合与边缘分布. 为此我们首先对 $d$ 维欧氏空间上的有限测度及其分布函数做简单的介绍.

## 3.1.1 多维分布函数

称 $\mathbb{R}^2$ 上的函数 $G$ 为分布函数, 是指存在欧氏可测空间 $(\mathbb{R}^2, \mathcal{B}^2)$ 上的局部有限测度 $\mu$ 满足: 任何矩形 $(a, b] \times (c, d] \subseteq \mathbb{R}^2$ 有

$$
G (b, d) - G (a, d) - G (b, c) + G (a, c) = \mu ((a, b ] \times (c, d ]). \tag {3.1.1}
$$

此时也称 $G$ 是 $\mu$ 的分布函数. 不难证明下面的命题:

命题 3.1.1 二维欧氏可测空间  $(\mathbb{R}^{2}, \mathcal{B}^{2})$  上的局部有限测度  $\mu$  的分布函数 G 具有性质:

(1) $G$ 右连续且在任何矩形 $(a,b]\times (c,d]\subseteq \mathbb{R}^2$ 上有非负增量，即

$$
\Delta G ((a, b ] \times (c, d ]) := G (b, d) - G (a, d) - G (b, c) + G (a, c) \geqslant 0; \tag {3.1.2}
$$

(2) $G$ 有界当且仅当 $\mu$ 是有限测度, 且此时有

$$
\mu (\mathbb {R} ^ {2}) = G (\infty , \infty) - G (- \infty , - \infty); \tag {3.1.3}
$$

(3) 若 $G$ 是 $\mu$ 的分布函数, 则 $G + c$ 也是 $\mu$ 的分布函数, 其中 $c$ 为常数.

例3.1.1 对于 $(x,y)\in \mathbb{R}^2$ 令 $F(x,y) = 1$ 若 $x + y\geqslant 1$; $F(x,y) = 0$ 若 $x + y < 1$. 则函数 $F(x,y)$ 关于 $x$ 和 $y$ 都是不降的, 但命题3.1.1的条件(1)不满足. 因此 $F$ 不是 $\mathbb{R}^2$ 上的分布函数.

设 $(\mathbb{R}^2, \mathcal{B}^2)$ 上的局部有限测度 $\mu$ 有分布函数 $G$. 称 $(x, y) \in \mathbb{R}^2$ 为 $\mu$ 或 $G$ 的跳跃点, 是指

$$
\Delta G (x, y) := G (x, y) - G (x -, y) - G (x, y -) + G (x -, y -) > 0.
$$

此时称  $\Delta G(x,y)=\mu(\{(x,y)\})$  为  $\mu$  或 G 在点  $(x,y)$  的跳幅。易知，跳跃点集  $E:=\{(x,y)\in\mathbb{R}^{2}:\Delta G(x,y)>0\}$  至多为可数集。写该集合为  $E=\{(x_{1},y_{1}),(x_{2},y_{2}),\cdots\}$ ，并记  $q(x_{i},y_{i})=\Delta G(x_{i},y_{i})$ 。称  $\mu$  或 G 是离散型的，是指有

$$
\Delta G ((a, b ] \times (c, d ]) = \sum_ {x _ {i} \in (a, b ]} \sum_ {y _ {i} \in (c, d ]} q (x _ {i}, y _ {i}), \quad (a, b ] \times (c, d ] \subseteq \mathbb {R} ^ {2}. \tag {3.1.4}
$$

此时称 $q$ 为 $\mu$ 或 $G$ 的密度函数或密度. 与一维情况不同, 当 $E$ 非空时分布函数 $G$ 并不在整个集合 $E^{c} = \mathbb{R}^{2} \setminus E$ 上连续.

称 $(\mathbb{R}^2, \mathcal{B}^2)$ 上的局部有限测度 $\mu$ 或其分布函数 $G$ 是绝对连续型的, 是指存在 $\mathbb{R}^2$ 上的非负黎曼可积函数 $q$ 使得

$$
\Delta G ((a, b ] \times (c, d ]) = \int_ {a} ^ {b} \int_ {c} ^ {d} q (x, y) \mathrm{d} x \mathrm{d} y, \quad (a, b ] \times (c, d ] \subseteq \mathbb {R} ^ {2}. \tag {3.1.5}
$$

此时称 $q$ 为 $\mu$ 或 $G$ 的密度函数或密度. 显然, 绝对连续型分布函数是 $\mathbb{R}$ 上的连续函数. 另外, 根据数学分析的结果, 若函数 $G$ 二次连续可微, 则 (3.1.5) 式对 $q = G_{xy}^{\prime \prime}$ 成立.

这里的讨论可以平行地推广到多维情况. 多维空间  $(\mathbb{R}^{d}, \mathcal{B}^{d})$  上的局部有限测度也由其分布函数唯一决定. 特别地, 对应于  $(\mathbb{R}^{d}, \mathcal{B}^{d})$  上的有限测度  $\mu$ , 有唯一的分布函数 G 满足  $G(-\infty, -\infty, \cdots, -\infty) = 0$ . 该分布函数由下式给出:

$$
G (x _ {1}, x _ {2}, \dots , x _ {d}) = \mu ((- \infty , x _ {1} ] \times (- \infty , x _ {2} ] \times \dots \times (- \infty , x _ {d} ]), \tag {3.1.6}
$$

其中  $(x_{1}, x_{2}, \cdots, x_{d}) \in \mathbb{R}^{d}$ . 后面当提到  $(\mathbb{R}^{d}, \mathcal{B}^{d})$  上的有限测度  $\mu$  的分布函数时, 总是指由 (3.1.6) 式定义的函数. 此时, 对  $1 \leqslant k \leqslant d$  令

$$
\mu_ {k} (B) = \mu (\mathbb {R} \times \dots \times \mathbb {R} \times B \times \mathbb {R} \times \dots \times \mathbb {R}), \quad B \in \mathcal {B},
$$

其中等号右端乘积集中的第 $k$ 个集合取 $B$ 而其他集合均取 $\mathbb{R}$. 显然 $\mu_k$ 是 $(\mathbb{R}, \mathcal{B})$ 上的有限测度, 称为 $\mu$ 的第 $k$ 个边缘分布. 称 $\mu_k$ 的分布函数 $G_k$ 为 $\mu$ 的第 $k$ 个边缘分布函数. 易见

$$
G _ {k} (x) = G (\infty, \dots , \infty , x, \infty , \dots , \infty), \quad x \in \mathbb {R}, \tag {3.1.7}
$$

其中等号右端第 k 个分量取 x 而其他分量取  $\infty$ .

## 3.1.2 随机向量的分布

定义 3.1.1 设  $(\Omega, \mathcal{F}, \mathbf{P})$  为概率空间，而  $\xi_{1}, \xi_{2}, \cdots, \xi_{d}$  为其上的 d 个随机变量。我们称  $\xi := (\xi_{1}, \xi_{2}, \cdots, \xi_{d})$  为 d 维随机向量或 d 维随机变量。