故知  $\mathbf{P}(\zeta=\infty)=1.$  □

## 7.2.3 嵌入链

定理 7.2.6 设 E 上的连续时间马氏链  $(X_{t}: t \geqslant 0)$  的密度矩阵 Q 为保守的, 且无吸收状态. 则  $(X_{S_{n}}: n \geqslant 0)$  是离散时间马氏链, 且有转移矩阵  $P := (q_{i}^{-1} q_{ij} (1 - \delta_{ij}) : i, j \in E)$ .

证明 因 $Q$ 无吸收状态, 每个 $S_{n}$ 都是有限停时. 注意 $X_{S_n}$ 关于 $\mathcal{F}_{S_n}$ 可测. 根据强马氏性, 对 $i \in E$ 和 $F \in \mathcal{F}_{S_n}$, 在条件概率 $\mathbf{P}(\cdot | F \cap \{X_{S_n} = i\})$ 之下 ($X_{S_n + t}: t \geqslant 0$) 为与 $X$ 有相同密度矩阵的马氏链. 再利用定理 7.2.2, 对于任何 $j \neq i$ 有

$$
\mathbf {P} (X _ {S _ {n + 1}} = j | F \cap \{X _ {S _ {n}} = i \}) = q _ {i} ^ {- 1} q _ {i j}.
$$

因而 $(X_{S_n}:n\geqslant 0)$ 关于流 $(\mathcal{F}_{S_n}:n\geqslant 0)$ 是以 $P$ 为转移矩阵的马氏链. □

在上面定理的情况下, 我们称离散时间马氏链  $(X_{S_{n}}: n \geqslant 0)$  为  $(X_{t}: t \geqslant 0)$  的嵌入链. 通过考虑嵌入链, 可将一些有关连续时间马氏链的问题转化为离散时间问题来处理.

例 7.2.1 考虑状态空间  $Z_{+}$  上参数为  $\alpha > 0$  的泊松过程, 其转移矩阵  $(P_{t})_{t \geqslant 0}$  由例 7.1.2 给出. 特别地, 我们有

$$
p _ {t} (i, i) = \mathrm{e} ^ {- \alpha t}, p _ {t} (i, i + 1) = \alpha t \mathrm{e} ^ {- \alpha t}, p _ {t} (i, i + 2) = \frac {(\alpha t) ^ {2}}{2} \mathrm{e} ^ {- \alpha t}.
$$

经简单计算知, 相应的密度矩阵为

$$
Q = \alpha \left( \begin{array}{c c c c} - 1 & 1 & 0 & \dots \\ 0 & - 1 & 1 & \dots \\ 0 & 0 & - 1 & \dots \\ \vdots & \vdots & \vdots \end{array} \right). \tag {7.2.16}
$$

由定理 1.4.1 或定理 7.2.2, 泊松过程在  $Z_{+}$ 中每个点停留一个以  $\alpha$  为参数的指数分布时间后跳到该点右边相邻的整数点, 如此一直运动下去.

例 7.2.2 由 (7.1.6) 式定义的转移矩阵有密度矩阵  $Q = \alpha(\pi - I)$ .

例 7.2.3 令  $E = \{-1, 1\}^{S}$ ，其中  $S \subseteq Z^{d}$  为非空有限集合。对于  $k \in S$  和  $x = \{x(i) : i \in S\} \in E$  定义  $x_{k} = \{x_{k}(i) : i \in S\} \in E$  如下:

$$
x _ {k} (i) = \left\{ \begin{array}{l l} x (i), & i \neq k, \\ - x (i), & i = k. \end{array} \right.
$$

给定常数 $\beta > 0$, 我们可以定义 $E$ 上的保守密度矩阵 $Q = \{q_{xy} : x, y \in E\}$ 如下: 当

$y = x_{k}$ $(k\in S)$ 时令

$$
q _ {x x _ {k}} = \exp \Bigg \{- \sum_ {| k - j | = 1} \beta x (k) x (j) \Bigg \}, \tag {7.2.17}
$$

当 $y \neq x$ 为其他状态时令 $q_{xy} = 0$. 以 $Q$ 为密度矩阵的马氏链称为伊辛 (Ising) 模型, 它描述了铁磁体的磁化过程, 其中 $\beta$ 与绝对温度的倒数成正比. 关于伊辛模型的详细讨论, 可参见 [4,25].

## 练习题

1. 设 $P = (p_{ij}(t): i, j \in E, t \geqslant 0)$ 是以 $Q$ 为密度矩阵的马氏转移矩阵. 证明: 若 $M := \sup_{i \in E} q_i < \infty$, 则 $\lim_{t \to 0+} p_{ii}(t) = 1$ 对 $i \in E$ 一致地成立, 进而函数族 $\{p_{ij}(\cdot): i, j \in E\}$ 在 $[0, \infty)$ 上等度连续.

提示: 由 (7.2.6) 式有 $p_{ii}(t) = \mathrm{e}^{-\phi_i(t)} \geqslant \mathrm{e}^{-t q_i} \geqslant \mathrm{e}^{-t M}$, 再应用定理 7.1.9.

2. 设 $P = (p_{ij}(t): i, j \in E, t \geqslant 0)$ 是以 $Q$ 为密度矩阵的马氏转移矩阵. 对 $i, j \in E$ 和 $\lambda > 0$ 令

$$
u _ {i j} (\lambda) = \int_ {0} ^ {\infty} \mathrm{e} ^ {- \lambda t} p _ {i j} (t) \mathrm{d} t.
$$

证明: (1) 对  $i \in E$  和  $\lambda > 0$  有  $\sum_{j} \lambda u_{ij}(\lambda) = 1$ ;

(2) 对 $i, j \in E$ 有

$$
\lim _ {\lambda \to \infty} \lambda u _ {i j} (\lambda) = \delta_ {i j}, \quad \lim _ {\lambda \to \infty} \lambda [ \lambda u _ {i j} (\lambda) - \delta_ {i j} ] = q _ {i j};
$$

(3) 对 $i, j \in E$ 和 $\lambda, \mu > 0$ 有

$$
u _ {i j} (\lambda) - u _ {i j} (\mu) = (\mu - \lambda) \sum_ {k \in E} u _ {i k} (\lambda) u _ {k j} (\mu).
$$

3. 设 $(\xi_{n}: n \geqslant 0)$ 是从 $x \in \mathbb{Z}$ 出发的离散时间一维对称简单随机游动, 而 $(N_{t}: t \geqslant 0)$ 与之独立, 从原点出发且以 $\alpha > 0$ 为参数的泊松过程. 证明连续时间对称简单随机游动 $(\xi_{N_{t}}: t \geqslant 0)$ 是鞅.
4. 设 $(X_{t}: t \geqslant 0)$ 是从 $x \in \mathbb{Z}$ 出发的连续时间一维对称简单随机游动. 对 $y \in \mathbb{Z}$ 令 $T_{y} = \inf \{t > 0 : X_{t} = y\}$. 利用 $(X_{t}: t \geqslant 0)$ 的鞅性质证明: 若 $a, b \in \mathbb{Z}$ 满足 $a < x < b$, 则

$$
\mathbf {P} (T _ {a} > T _ {b}) = \frac {x - a}{b - a}, \quad \mathbf {P} (T _ {b} > T _ {a}) = \frac {b - x}{b - a}.
$$

5. 设 $(\xi_{n}: n \geqslant 0)$ 是从原点出发的一维简单随机游动, 而 $(N_{t}: t \geqslant 0)$ 与之独立, 从原点出发, 以 $a > 0$ 为参数的泊松过程. 令 $X_{n} = \xi_{n} - \min_{0 \leqslant k \leqslant n} \xi_{k}$ 和 $Y_{n} = \max_{0 \leqslant k \leqslant n} \xi_{k} - \xi_{n}$. 证明 $(X_{N_{t}}: t \geqslant 0)$ 和 $(Y_{N_{t}}: t \geqslant 0)$ 都是连续时间马氏链, 并给出其密度矩阵.

提示: 令 $p = \mathbf{P}(\xi_1 = 1)$ 和 $q = \mathbf{P}(\xi_1 = -1)$. 再令 $\tau_1 = \inf \{n \geqslant 0 : X_n = 1\}$ 和 $S_1 = \inf \{t \geqslant 0 : X_{N_t} = 1\}$. 注意对 $k \geqslant 1$ 有 $\mathbf{P}(\tau_1 = k) = pq^{k-1}$, 且在条件概率 $\mathbf{P}(\cdot | \tau_1 = k)$ 之下 $S_1$ 是 $k$ 个独立且均服从参数为 $\alpha$ 的指数分布的随机变量之和. 根据全期望公式有

$$
\mathbf {P} (\mathrm{e} ^ {- \lambda S _ {1}}) = \sum_ {k = 1} ^ {\infty} p q ^ {k - 1} \Big (\frac {a}{a + \lambda} \Big) ^ {k} = \frac {a p}{a p + \lambda}.
$$

因此 $S_{1}$ 服从参数为 $ap$ 的指数分布. 类似地可知 $T_{1} = \inf \{t \geqslant 0 : Y_{N_{t}} = 1\}$ 服从参数为 $aq$ 的指数分布.

## 7.3 向前和向后方程

设 $(P(t))_{t\geqslant 0} = \{(p_{ij}(t):i,j\in E):t\geqslant 0\}$ 是可数状态空间 $E$ 上的准马氏转移矩阵, 则对于 $t\geqslant 0$ 和 $h > 0$ 有

$$
p _ {i j} (t + h) - p _ {i j} (t) = \sum_ {k \neq j} p _ {i k} (t) p _ {k j} (h) - p _ {i j} (t) [ 1 - p _ {j j} (h) ] \tag {7.3.1}
$$

和

$$
p _ {i j} (t + h) - p _ {i j} (t) = \sum_ {k \neq i} p _ {i k} (h) p _ {k j} (t) - [ 1 - p _ {i i} (h) ] p _ {i j} (t). \tag {7.3.2}
$$

令 $Q = (q_{ij}:i,j\in E)$ 为 $(P(t))_{t\geqslant 0}$ 的密度矩阵.我们自然地希望可以在上面二式两边同除以 $h$ 并令 $h\to 0+$ 得到

$$
p _ {i j} ^ {\prime} (t) = \sum_ {k \neq j} p _ {i k} (t) q _ {k j} - p _ {i j} (t) q _ {j} \tag {7.3.3}
$$

和

$$
p _ {i j} ^ {\prime} (t) = \sum_ {k \neq i} q _ {i k} p _ {k j} (t) - q _ {i} p _ {i j} (t). \tag {7.3.4}
$$

这两个式子分别称为 (柯尔莫哥洛夫) 向前微分方程和向后微分方程. 显然 (7.2.1) 式和 (7.2.2) 式可视为 (7.3.3) 式和 (7.3.4) 式当 $t = 0$ 时的特例.

## 7.3.1 向后方程

定理 7.3.1 向后微分方程 (7.3.4) 等价于积分方程

$$
p _ {i j} (t) = \delta_ {i j} + \sum_ {k \neq i} \int_ {0} ^ {t} q _ {i k} p _ {k j} (s) \mathrm{d} s - \int_ {0} ^ {t} q _ {i} p _ {i j} (s) \mathrm{d} s. \tag {7.3.5}
$$

证明 由定理 7.1.9 知 $p_{ij}(t)$ 关于 $t \geqslant 0$ 一致连续. 若 (7.3.4) 式成立, 根据控制收敛定理可知 $p_{ij}'(t)$ 也关于 $t \geqslant 0$ 一致连续, 对该式两边积分并应用富比尼定理即得 (7.3.5) 式. 反之, 设 (7.3.5) 式成立. 根据富比尼定理有

$$
p _ {i j} (t) = \delta_ {i j} + \int_ {0} ^ {t} \left[ \sum_ {k \neq i} q _ {i k} p _ {k j} (s) \right] \mathrm{d} s - \int_ {0} ^ {t} q _ {i} p _ {i j} (s) \mathrm{d} s.
$$

注意这里积分中的级数对 $s \geqslant 0$ 一致收敛且一致连续, 由此可见 $p_{ij}(t)$ 关于 $t \geqslant 0$ 连续可导. 在上式两边对 $t \geqslant 0$ 求导即得 (7.3.4) 式. □

定理 7.3.2 向后微分方程 (7.3.4) 等价于积分方程

$$
p _ {i j} (t) = \delta_ {i j} \mathrm{e} ^ {- q _ {i} t} + \sum_ {k \neq i} \int_ {0} ^ {t} q _ {i k} p _ {k j} (s) \mathrm{e} ^ {- q _ {i} (t - s)} \mathrm{d} s. \tag {7.3.6}
$$

证明 显然, 向后微分方程 (7.3.4) 等价于

$$
\left[ \mathrm{e} ^ {q _ {i} t} p _ {i j} (t) \right] ^ {\prime} = \sum_ {k \neq i} \mathrm{e} ^ {q _ {i} t} q _ {i k} p _ {k j} (t).
$$

另一方面, 积分方程 (7.3.6) 等价于

$$
\mathrm{e} ^ {q _ {i} t} p _ {i j} (t) = \delta_ {i j} + \sum_ {k \neq i} \int_ {0} ^ {t} q _ {i k} p _ {k j} (s) \mathrm{e} ^ {q _ {i} s} \mathrm{d} s. \tag {7.3.7}
$$

与定理 7.3.1 的证明中类似地, 可以看到以上二式等价, 故 (7.3.4) 式和 (7.3.6) 式等价. $\square$

引理 7.3.3 令 $a < b \in \mathbb{R}$. 若连续函数 $f$ 在区间 $[a, b]$ 上有连续的右导数 $f'_+$, 则存在 $z \in [a, b)$ 使得

$$
(b - a) f _ {+} ^ {\prime} (z) = f (b) - f (a). \tag {7.3.8}
$$

证明 首先, 考虑 $f(a) = f(b) = c$ 的特例. 假若对一切 $x \in [a, b]$ 有 $f(x) \leqslant c$, 则 $f_{+}^{\prime}(a) \leqslant 0$. 否则函数 $f$ 在某点 $x_1 \in (a, b)$ 取到其最大值, 因而 $f_{+}^{\prime}(x_1) \leqslant 0$. 所以总有 $x_1 \in [a, b)$ 使得 $f_{+}^{\prime}(x_1) \leqslant 0$. 类似地, 有 $x_2 \in [a, b)$ 使得 $f_{+}^{\prime}(x_1) \geqslant 0$. 由 $f_{+}^{\prime}$ 的连续性, 存在 $z \in [a, b)$ 使得 $f_{+}^{\prime}(z) = 0$. 对于一般情况, 将前面的结论应用于函数

$$
g (x) := f (x) - \frac {f (b) - f (a)}{b - a} (x - a),
$$

知存在 $z \in [a, b)$ 使得 $g_{+}^{\prime}(z) = 0$, 故 (7.3.8) 式成立. $\square$

引理7.3.4 令 $a < b \in \mathbb{R}$. 若连续函数 $f$ 在区间 $[a, b]$ 上有连续的右导数 $f_{+}^{\prime}$, 则 $f$ 在 $[a, b]$ 上连续可导且 $f' = f_{+}^{\prime}$.

证明 对于 $a \leqslant x < y \leqslant b$, 根据引理 7.3.3 有 $z \in [x, y)$ 使得

$$
(y - x) f _ {+} ^ {\prime} (z) = f (y) - f (x).
$$

类似地, 对于 $a \leqslant y < x \leqslant b$, 存在 $z \in [y, x)$ 使上面关系成立. 由 $f_{+}^{\prime}$ 的连续性得

$$
\lim _ {y \to x} \frac {f (y) - f (x)}{y - x} = \lim _ {y \to x} f _ {+} ^ {\prime} (z) = f _ {+} ^ {\prime} (x).
$$

因此 $f$ 在 $[a,b]$ 上连续可导且 $f^{\prime} = f_{+}^{\prime}$. □

定理 7.3.5 (柯尔莫哥洛夫) 设转移矩阵  $(P(t))_{t\geqslant0}$  有保守的密度矩阵 Q，则对任意的  $i,j\in E$ ，函数  $t\mapsto p_{ij}(t)$  在  $[0,\infty)$  上连续可导且向后微分方程 (7.3.4) 成立.

证明 一方面, 由 (7.3.2) 式和法图定理可得

$$
\operatorname * {l i m i n f} _ {h \to 0 +} \frac {1}{h} [ p _ {i j} (h + t) - p _ {i j} (t) ] \geqslant \sum_ {k \neq i} q _ {i k} p _ {k j} (t) - q _ {i} p _ {i j} (t). \tag {7.3.9}
$$

另一方面, 取有限集合 $A \subseteq E$ 使 $i \in A$, 并记 $A^c = E \setminus A$. 由 (7.3.2) 式有

$$
\begin{array}{l} p _ {i j} (h + t) - p _ {i j} (t) \leqslant \sum_ {k \in A, k \neq i} p _ {i k} (h) p _ {k j} (t) - [ 1 - p _ {i i} (h) ] p _ {i j} (t) + \sum_ {k \in A ^ {c}} p _ {i k} (h) \\ \leqslant \sum_ {k \in A, k \neq i} p _ {i k} (h) p _ {k j} (t) - [ 1 - p _ {i i} (h) ] p _ {i j} (t) + \\ 1 - p _ {i i} (h) - \sum_ {k \in A, k \neq i} p _ {i k} (h) \\ = \sum_ {k \in A, k \neq i} p _ {i k} (h) p _ {k j} (t) + [ 1 - p _ {i i} (h) ] [ 1 - p _ {i j} (t) ] - \\ \sum_ {k \in A, k \neq i} p _ {i k} (h). \\ \end{array}
$$

将上式两端同除以 h > 0 并取上极限得

$$
\operatorname * {l i m s u p} _ {h \to 0 +} \frac {1}{h} [ p _ {i j} (h + t) - p _ {i j} (t) ] \leqslant \sum_ {k \in A, k \neq i} q _ {i k} p _ {k j} (t) + q _ {i} [ 1 - p _ {i j} (t) ] - \sum_ {k \in A, k \neq i} q _ {i k}.
$$

因为密度矩阵 Q 保守, 由有限集合  $A \subseteq E$  的任意性得

$$
\begin{array}{l} \operatorname * {l i m s u p} _ {h \to 0 +} \frac {1}{h} [ p _ {i j} (h + t) - p _ {i j} (t) ] \\ \leqslant \sum_ {k \neq i} q _ {i k} p _ {k j} (t) + q _ {i} [ 1 - p _ {i j} (t) ] - \sum_ {k \neq i} q _ {i k} \\ \end{array}
$$

$$
= \sum_ {k \neq i} q _ {i k} p _ {k j} (t) - q _ {i} p _ {i j} (t). \tag {7.3.10}
$$

由 (7.3.9) 式和 (7.3.10) 式, 若将 $p_{ij}'(t)$ 理解为右导数, 则 (7.3.4) 式成立, 而由控制收敛定理易知该右导数关于 $t \geqslant 0$ 连续. 再应用引理 7.3.4 知 $t \mapsto p_{ij}(t)$ 连续可导且满足方程 (7.3.4). □

推论 7.3.6 马氏转移矩阵  $(P(t))_{t\geqslant0}$  的向后微分方程 (7.3.4) 成立当且仅当其密度矩阵 Q 保守.

证明 若密度矩阵 $Q$ 保守, 由定理7.3.5知向后微分方程(7.3.4)成立. 反之, 假设向后微分方程(7.3.4)成立. 由(7.3.4)式和控制收敛定理知 $t \mapsto p_{ij}'(t)$ 在 $[0, \infty)$ 上连续, 而且有

$$
\sum_ {j \in E} | p _ {i j} ^ {\prime} (t) | \leqslant \sum_ {k \neq i} q _ {i k} + q _ {i} = 2 q _ {i}
$$

和

$$
\sum_ {j \in E} p _ {i j} ^ {\prime} (t) = \sum_ {k \neq i} q _ {i k} - q _ {i}.
$$

再根据富比尼定理有

$$
\Bigl (\sum_ {k \neq i} q _ {i k} - q _ {i} \Bigr) t = \sum_ {j \in E} \int_ {0} ^ {t} p _ {i j} ^ {\prime} (s) \mathrm{d} s = \sum_ {j \in E} p _ {i j} (t) - 1 = 0,
$$

其中最后一个等号成立是根据 $(P(t))_{t\geqslant 0}$ 的马氏性.故密度矩阵 $Q$ 保守.□

## 7.3.2 向前方程

与向后微分方程类似地, 向前微分方程也可写为等价的积分方程形式. 为了简化证明, 下面只对保守的密度矩阵讨论此问题.

定理 7.3.7 设密度矩阵 Q 保守, 则向前微分方程 (7.3.3) 等价于积分方程

$$
p _ {i j} (t) = \delta_ {i j} + \sum_ {k \neq j} \int_ {0} ^ {t} p _ {i k} (s) q _ {k j} \mathrm{d} s - \int_ {0} ^ {t} p _ {i j} (s) q _ {j} \mathrm{d} s. \tag {7.3.11}
$$

证明 由定理7.3.5知 $t \mapsto p_{ij}(t)$ 在 $[0, \infty)$ 上连续可导. 若(7.3.3)式成立, 对两边积分即得(7.3.11)式. 反之, 设(7.3.11)式成立. 对 $t \geqslant 0$ 和 $h > 0$, 我们有

$$
\frac {1}{h} [ p _ {i j} (t + h) - p _ {i j} (t) ] = \sum_ {k \neq j} \frac {1}{h} \int_ {0} ^ {h} p _ {i k} (t + s) q _ {k j} \mathrm{d} s - \frac {1}{h} \int_ {0} ^ {h} p _ {i j} (t + s) q _ {j} \mathrm{d} s.
$$

对上式取极限  $h \rightarrow 0+$  并利用法图定理得到

$$
p _ {i j} ^ {\prime} (t) \geqslant \sum_ {k \neq j} p _ {i k} (t) q _ {k j} - p _ {i j} (t) q _ {j}.
$$

假若 (7.3.3) 式不成立, 则当 $t$ 属于某个非空开区间 $(u, v) \subseteq (0, \infty)$ 时上式中的严格大于号成立, 故当 $t > u$ 时有

$$
p _ {i j} (t) - \delta_ {i j} > \sum_ {k \neq j} \int_ {0} ^ {t} p _ {i k} (s) q _ {k j} \mathrm{d} s - \int_ {0} ^ {t} p _ {i j} (s) q _ {j} \mathrm{d} s,
$$

这与 (7.3.11) 式矛盾, 故 (7.3.3) 式必然成立. 这就证明了 (7.3.3) 式和 (7.3.11) 式的等价性. $\square$

与定理 7.3.7 的证明中类似地, 可以证明如下的:

定理 7.3.8 设密度矩阵 Q 保守, 则向前微分方程 (7.3.3) 等价于积分方程

$$
p _ {i j} (t) = \delta_ {i j} \mathrm{e} ^ {- q _ {j} t} + \sum_ {k \neq j} \int_ {0} ^ {t} p _ {i k} (s) q _ {k j} \mathrm{e} ^ {- q _ {j} (t - s)} \mathrm{d} s. \tag {7.3.12}
$$

与向后方程有所不同, 即使对保守的密度矩阵, 向前方程也并非总成立; 详见 [35] 中的讨论.

## 7.3.3 最小转移矩阵

设 $Q = (q_{ij}:i,j\in E)$ 为保守密度矩阵. 称准马氏转移矩阵 $(F(t))_{t\geqslant 0} = \{(f_{ij}(t):i,j\in E):t\geqslant 0\}$ 是向前方程(7.3.3)的最小解, 是指它满足(7.3.3)式且对任何满足该方程的准转移矩阵 $(P(t))_{t\geqslant 0} = \{(p_{ij}(t):i,j\in E):t\geqslant 0\}$ 都有

$$
f _ {i j} (t) \leqslant p _ {i j} (t), \quad i, j \in E, t \geqslant 0.
$$

类似地可定义向后方程 (7.3.4) 的最小解. 受到定理 7.2.3 和推论 7.2.4 的结果的启发, 对于 $t \geqslant 0$ 和 $i, j \in E$, 令 $g_{ij}^{(0)}(t) = \delta_{ij} \mathrm{e}^{-q_i t}$, 并对于 $n \geqslant 1$ 依次定义

$$
g _ {i j} ^ {(n)} (t) = \sum_ {k \neq i} \int_ {0} ^ {t} \mathrm{e} ^ {- q _ {i} s} q _ {i k} g _ {k j} ^ {(n - 1)} (t - s) \mathrm{d} s. \tag {7.3.13}
$$

在此基础上, 我们定义

$$
f _ {i j} ^ {(n)} (t) = \sum_ {k = 0} ^ {n} g _ {i j} ^ {(k)} (t), \quad f _ {i j} (t) = \sum_ {k = 0} ^ {\infty} g _ {i j} ^ {(k)} (t). \tag {7.3.14}
$$

再令  $F(t)=(f_{ij}(t):i,j\in E)$ .

命题7.3.9 对任意的 $n \geqslant 1$ 和 $i, j \in E$, 有

$$
g _ {i j} ^ {(n)} (t) = \sum_ {k \neq j} \int_ {0} ^ {t} g _ {i k} ^ {(n - 1)} (t - s) q _ {k j} \mathrm{e} ^ {- q _ {j} s} \mathrm{d} s, \quad t \geqslant 0. \tag {7.3.15}
$$

证明 使用归纳法证明. 根据 (7.3.13) 式我们有

$$
\begin{array}{l} g _ {i j} ^ {(1)} (t) = \sum_ {k \neq i} \int_ {0} ^ {t} \mathrm{e} ^ {- q _ {i} s} q _ {i k} g _ {k j} ^ {(0)} (t - s) \mathrm{d} s = \sum_ {k \neq i} \int_ {0} ^ {t} \mathrm{e} ^ {- q _ {i} s} q _ {i k} \delta_ {k j} \mathrm{e} ^ {- q _ {k} (t - s)} \mathrm{d} s \\ = 1 _ {\{i \neq j \}} \int_ {0} ^ {t} \mathrm{e} ^ {- q _ {i} s} q _ {i j} \mathrm{e} ^ {- q _ {j} (t - s)} \mathrm{d} s = \sum_ {k \neq j} \int_ {0} ^ {t} \mathrm{e} ^ {- q _ {i} s} \delta_ {i k} q _ {k j} \mathrm{e} ^ {- q _ {j} (t - s)} \mathrm{d} s \\ = \sum_ {k \neq j} \int_ {0} ^ {t} g _ {i k} ^ {(0)} (s) q _ {k j} \mathrm{e} ^ {- q _ {j} (t - s)} \mathrm{d} s, \\ \end{array}
$$

故 (7.3.15) 式对 $n = 1$ 成立. 下设 (7.3.15) 式对某个 $n \geqslant 1$ 成立. 由 (7.3.13) 式和归纳法假设有

$$
\begin{array}{l} g _ {i j} ^ {(n + 1)} (t) = \sum_ {k \neq i} \int_ {0} ^ {t} \mathrm{e} ^ {- q _ {i} s} q _ {i k} g _ {k j} ^ {(n)} (t - s) \mathrm{d} s \\ = \sum_ {k \neq i} \int_ {0} ^ {t} \mathrm{e} ^ {- q _ {i} s} q _ {i k} \bigg [ \sum_ {l \neq j} \int_ {0} ^ {t - s} g _ {k l} ^ {(n - 1)} (t - s - v) q _ {l j} \mathrm{e} ^ {- q _ {j} v} \mathrm{d} v \bigg ] \mathrm{d} s \\ = \sum_ {l \neq j} \int_ {0} ^ {t} q _ {l j} \left[ \sum_ {k \neq i} \int_ {0} ^ {t - v} g _ {k l} ^ {(n - 1)} (t - v - s) q _ {i k} \mathrm{e} ^ {- q _ {i} s} \mathrm{d} s \right] \mathrm{e} ^ {- q _ {j} v} \mathrm{d} v \\ = \sum_ {l \neq j} \int_ {0} ^ {t} q _ {l j} g _ {i l} ^ {(n)} (t - v) \mathrm{e} ^ {- q _ {j} v} \mathrm{d} v. \\ \end{array}
$$

于是知 (7.3.15) 式对所有 $n \geqslant 1$ 成立. $\square$

命题7.3.10 对任意的 $n \geqslant 0$ 和 $i, j \in E$ 有

$$
g _ {i j} ^ {(n)} (r + t) = \sum_ {m = 0} ^ {n} \sum_ {l \in E} g _ {i l} ^ {(m)} (r) g _ {l j} ^ {(n - m)} (t), \quad r, t \geqslant 0. \tag {7.3.16}
$$

证明 显然 (7.3.16) 式对于 $n = 0$ 成立. 假设该式对某个 $n \geqslant 0$ 成立. 根据 (7.3.13) 式及归纳假设有

$$
\begin{array}{l} g _ {i j} ^ {(n + 1)} (r + t) = \sum_ {k \neq i} \left(\int_ {0} ^ {r} + \int_ {r} ^ {r + t}\right) \mathrm{e} ^ {- q _ {i} s} q _ {i k} g _ {k j} ^ {(n)} (r + t - s) \mathrm{d} s \\ = \sum_ {k \neq i} \left[ \int_ {0} ^ {r} \mathrm{e} ^ {- q _ {i} s} q _ {i k} g _ {k j} ^ {(n)} (r + t - s) \mathrm{d} s + \right. \\ \mathrm{e} ^ {- q _ {i} r} \int_ {0} ^ {t} \mathrm{e} ^ {- q _ {i} s} q _ {i k} g _ {k j} ^ {(n)} (t - s) \mathrm{d}s \Biggr ] \\ \end{array}
$$

$$
\begin{array}{l} = \sum_ {k \neq i} \left[ \int_ {0} ^ {r} \mathrm{e} ^ {- q _ {i} s} q _ {i k} \sum_ {l \in E} \sum_ {m = 0} ^ {n} g _ {k l} ^ {(m)} (r - s) g _ {l j} ^ {(n - m)} (t) \mathrm{d} s \right] \\ + \mathrm{e} ^ {- q _ {i} r} g _ {i j} ^ {(n + 1)} (t) \\ = \sum_ {l \in E} \left[ \sum_ {m = 0} ^ {n} g _ {i l} ^ {(m + 1)} (r) g _ {l j} ^ {(n - m)} (t) + g _ {i l} ^ {(0)} (r) g _ {l j} ^ {(n + 1)} (t) \right] \\ = \sum_ {l \in E} \sum_ {m = 0} ^ {n + 1} g _ {i l} ^ {(m)} (r) g _ {l j} ^ {(n + 1 - m)} (t). \\ \end{array}
$$

由数学归纳法知 (7.3.16) 式对一切 $n \geqslant 0$ 成立. $\square$

命题7.3.11 对任意的 $n \geqslant 1$ 和 $i, j \in E$ 有

$$
f _ {i j} ^ {(n)} (t) = \delta_ {i j} \mathrm{e} ^ {- q _ {i} t} + \sum_ {k \neq j} \int_ {0} ^ {t} f _ {i k} ^ {(n - 1)} (t - s) q _ {k j} \mathrm{e} ^ {- q _ {j} s} \mathrm{d} s \tag {7.3.17}
$$

和

$$
f _ {i j} ^ {(n)} (t) = \delta_ {i j} \mathrm{e} ^ {- q _ {i} t} + \sum_ {k \neq i} \int_ {0} ^ {t} \mathrm{e} ^ {- q _ {i} s} q _ {i k} f _ {k j} ^ {(n - 1)} (t - s) \mathrm{d} s. \tag {7.3.18}
$$

证明 由于 $g_{ij}^{(0)}(t) = \delta_{ij}\mathrm{e}^{-q_it}$, 分别将 (7.3.13) 式和 (7.3.15) 式两边对 $n \geqslant 1$ 求和即得欲证结果. $\square$

定理 7.3.12 由 (7.3.14) 式定义的  $F(t) = (f_{ij}(t) : i, j \in E, t \geqslant 0)$  是准马氏转移矩阵, 而且是向前微分方程 (7.3.3) 的最小解, 也是向后微分方程 (7.3.4) 的最小解.

证明 首先, 我们证明 $\sum_{j \in E} f_{ij}(t) \leqslant 1$. 为此只需证明 $\sum_{j \in E} f_{ij}^{(n)}(t) \leqslant 1$ 对一切 $n \geqslant 0$ 成立. 采用数学归纳法. 注意

$$
\sum_ {j \in E} f _ {i j} ^ {(0)} (t) = \sum_ {j \in E} g _ {i j} ^ {(0)} (t) = \sum_ {j \in E} \delta_ {i j} \mathrm{e} ^ {- q _ {i} t} = \mathrm{e} ^ {- q _ {i} t} \leqslant 1.
$$

假设 $\sum_{j\in E}f_{ij}^{(n)}(t)\leqslant 1$ 对某个 $n\geqslant 0$ 成立.由(7.3.18)式有

$$
\begin{array}{l} \sum_ {j \in E} f _ {i j} ^ {(n + 1)} (t) = \mathrm{e} ^ {- q _ {i} t} + \sum_ {j \in E} \sum_ {k \neq i} \int_ {0} ^ {t} \mathrm{e} ^ {- q _ {i} s} q _ {i k} f _ {k j} ^ {(n)} (t - s) \mathrm{d}s \\ \leqslant \mathrm{e} ^ {- q _ {i} t} + \sum_ {k \neq i} \int_ {0} ^ {t} \mathrm{e} ^ {- q _ {i} s} q _ {i k} \mathrm{d} s \\ \leqslant \mathrm{e} ^ {- q _ {i} t} + \int_ {0} ^ {t} q _ {i} \mathrm{e} ^ {- q _ {i} s} \mathrm{d} s = 1. \\ \end{array}
$$

因此 $\sum_{j\in E}f_{ij}^{(n)}(t)\leqslant 1$ 对所有 $n\geqslant 0$ 成立.根据命题7.3.10有

$$
\begin{array}{l} f _ {i j} (s + t) = \sum_ {n = 0} ^ {\infty} g _ {i j} ^ {(n)} (s + t) = \sum_ {n = 0} ^ {\infty} \sum_ {m = 0} ^ {n} \sum_ {l \in E} g _ {i l} ^ {(m)} (s) g _ {l j} ^ {(n - m)} (t) \\ = \sum_ {l \in E} \sum_ {m = 0} ^ {\infty} \sum_ {k = 0} ^ {\infty} g _ {i l} ^ {(m)} (s) g _ {l j} ^ {(k)} (t) = \sum_ {l \in E} f _ {i l} (s) f _ {l j} (t). \\ \end{array}
$$

所以 $F$ 是转移矩阵. 在 (7.3.18) 式两边令 $n \to \infty$ 知 $F$ 满足向后积分方程 (7.3.6), 再据定理 7.3.2 知 $F$ 满足向后微分方程 (7.3.4). 故 $f_{ij}(t)$ 关于 $t \geqslant 0$ 可导. 在 (7.3.17) 式两边令 $n \to \infty$ 知 $F$ 满足向前积分方程 (7.3.12). 应用定理 7.3.8 知 $F$ 满足向前微分方程 (7.3.3). 设有准转移矩阵 $(P(t))_{t \geqslant 0}$ 满足向前微分方程 (7.3.3), 则它也满足向前积分方程 (7.3.12). 因此 $p_{ij}(t) \geqslant \delta_{ij} \mathrm{e}^{-q_i t} = f_{ij}^{(0)}(t)$. 而若设 $p_{ij}(t) \geqslant f_{ij}^{(n)}(t)$, 则由 (7.3.12) 式得

$$
p _ {i j} (t) \geqslant \delta_ {i j} \mathrm{e} ^ {- q _ {i} t} + \sum_ {k \neq j} \int_ {0} ^ {t} f _ {i k} ^ {(n)} (t - s) q _ {k j} \mathrm{e} ^ {- q _ {i} s} \mathrm{d} s = f _ {i j} ^ {(n + 1)} (t).
$$

根据归纳法, 对一切 $n \geqslant 0$ 有 $p_{ij}(t) \geqslant f_{ij}^{(n)}(t)$. 取极限即得 $p_{ij}(t) \geqslant f_{ij}(t)$. 类似地可证, 若转移矩阵 $(P(t))_{t \geqslant 0}$ 满足向后微分方程 (7.3.4), 也有 $p_{ij}(t) \geqslant f_{ij}(t)$ 成立. $\square$

推论 7.3.13 若对任意  $t \geqslant 0$  和  $i \in E$  都有  $\sum_{j \in E} f_{ij}(t) = 1$ ，则 Q 的向前方程和向后方程均存在唯一解且二者相同.

根据定理 7.3.12 知, 密度矩阵 Q 的向前和向后微分方程有公共的最小解  $(F(t))_{t \geqslant 0}$ , 我们称之为 Q 的最小转移矩阵. 以  $(F(t))_{t \geqslant 0}$  为转移矩阵的马氏链称为 Q 的最小链.

具有给定密度矩阵的连续时间转移矩阵的唯一性的判别准则是基本的理论问题. 侯振挺 [18] 给出了该唯一性成立的简洁的充要条件, 解决了该领域长期遗留的难题. 关于连续时间马氏链的研究有丰富而深刻的理论, 参见 [4,35].

## \*7.3.4 最小链的随机方程

利用泊松随机测度驱动的随机积分方程的轨道唯一解, 可以构造出具有给定密度矩阵的右连续最小马氏链. 为了表达上的方便, 这里假定 $E \subseteq \mathbb{Z}$. 考虑 $E$ 上的保守密度矩阵 $Q = (q_{ij}: i, j \in E)$. 用 $\pi(\mathrm{d}z)$ 表示 $E$ 上的计数测度.

设 $N(\mathrm{ds},\mathrm{dz},\mathrm{du})$ 为 $(0,\infty)\times E\times (0,\infty)$ 上的以 $\mathrm{ds}\pi (\mathrm{dz})\mathrm{du}$ 为强度的泊松随机测度，而 $X_0$ 是取值于 $E$ 且与 $N(\mathrm{ds},\mathrm{dz},\mathrm{du})$ 独立的随机变量.这里 $\mathrm{ds}$ 和 $\mathrm{du}$ 表示 $(0,\infty)$ 上的勒贝格测度.记 $q(i,j) = q_{ij}1_{\{i\neq j\}}$ .考虑随机积分方程

$$
X _ {t} = X _ {0} + \int_ {0} ^ {t} \int_ {E} \int_ {0} ^ {q (X _ {s -}, z)} (z - X _ {s -}) N (\mathrm{d} s, \mathrm{d} z, \mathrm{d} u). \tag {7.3.19}
$$

此处及以后约定 $\int_{a}^{b} = \int_{(a,b]}$ 该方程的确切含义如下:根据泊松随机测度的构造，存在$(0,\infty)\times E\times (0,\infty)$ 的可数的随机子集 $\operatorname {supp}(N) = \{(s_i,z_i,u_i):i\in I\}$ 使得

$$
N (\mathrm{d} s, \mathrm{d} z, \mathrm{d} u) = \sum_ {i \in I} \delta_ {(s _ {i}, z _ {i}, u _ {i})} (\mathrm{d} s, \mathrm{d} z, \mathrm{d} u). \tag {7.3.20}
$$

注意, 方程 (7.3.19) 可以写为

$$
X _ {t} = X _ {0} + \sum_ {s _ {i} \leqslant t} (z _ {i} - X _ {s _ {i} -}) 1 _ {\{u _ {i} \leqslant q (X _ {s -}, z _ {i}) \}}. \tag {7.3.21}
$$

易证 $\mathbf{P}$ (存在 $i \neq j$ 使得 $s_i = s_j$) = 0. 方程 (7.3.19) 式或 (7.3.21) 式给出了轨道 $t \mapsto X_t$ 每次跳跃的时刻和跳幅. 它的第 1 次跳跃发生在时刻

$$
S _ {1} := \inf \{s > 0: N ((0, s ] \times E \times (0, q (X _ {0}, z) ]) > 0 \}.
$$

对 $0 \leqslant t < S_{1}$ 有 $X_{t} = X_{0}$. 由 (7.3.19) 式和 (7.3.20) 式不难看出, 存在唯一的 $(Z_{1}, U_{1}) \in E \times (0, q(X_{0}, z)]$ 满足 $(S_{i}, Z_{i}, U_{i}) \in \operatorname{supp}(N)$. 再由 (7.3.19) 式有

$$
X _ {S _ {1}} = X _ {S _ {1} -} + (Z _ {1} - X _ {S _ {1} -}) = X _ {0} + (Z _ {1} - X _ {0}) = Z _ {1}.
$$

轨道 $t \mapsto X_{t}$ 的第2次跳跃发生在时刻

$$
S _ {2} := \inf \{s > S _ {1}: N ((S _ {1}, s ] \times E \times (0, q (X _ {S _ {1}}, z) ]) > 0 \},
$$

其后轨道的运动情况类似. 用 $S_{n}$ 表示 $t \mapsto X_{t}$ 的第 $n$ 次跳跃发生的时刻, 则 $S_{n}$ 为停时且序列 $\{S_{n}\}$ 严格单增. 令 $\zeta = \lim_{n \to \infty} S_{n}$. 显然 $t \mapsto X_{t}$ 在时间区间 $[0, \zeta)$ 内的运动由 (7.3.19) 式唯一决定. 对于 $\zeta \leqslant t < \infty$, 我们补充定义 $X_{t} = \infty$. 则 $X = (X_{t}: t \geqslant 0)$ 是取值于 $\tilde{E} := E \cup \{\infty\}$ 的右连续过程. 注意, 在 (7.3.19) 式中将 $t$ 替换为 $t \wedge S_{n}$ 后, 该等式对于每个 $n \geqslant 1$ 几乎必然成立.

在上述意义下, 我们说 $X$ 是 (7.3.19) 式的轨道唯一解. 对于 $t \geqslant 0$ 令 $\mathcal{G}_t$ 是下面的随机变量族生成的 $\sigma$ 代数:

$$
\{X _ {0}, N ((0, s ] \times A \times B): 0 \leqslant s \leqslant t, A \subseteq E, B \in \mathscr {B} (0, \infty) \}.
$$

不难看出, 过程 X 关于流  $(\mathcal{G}_{t}: t \geqslant 0)$  适应.

定理 7.3.14 随机积分方程 (7.3.19) 的轨道唯一解 X 关于流  $(\mathcal{G}_{t}: t \geqslant 0)$  是以 Q 为密度矩阵的马氏链, 且其转移矩阵  $(F(t))_{t \geqslant 0}$  是 Q 的最小转移矩阵.

证明 记 $\mathbf{P}_i = \mathbf{P}(\cdot |X_0 = i)$ 和 $f_{ij}(t) = \mathbf{P}_i(X_t = j)$. 由方程 (7.3.19), 对任何 $t, r \geqslant 0$ 有

$$
X _ {r + t} = X _ {r} + \int_ {0} ^ {t} \int_ {E} \int_ {0} ^ {q (X _ {r + s -}, z)} (z - X _ {r + s -}) N (r + \mathrm{d} s, \mathrm{d} z, \mathrm{d} u). \tag {7.3.22}
$$

根据泊松随机测度的性质, 对任何 $G \in \mathcal{G}_r$ 在 $\mathbf{P}(\cdot | G \cap \{X_r = i\})$ 之下 $N(r + \mathrm{d}s, \mathrm{d}z, \mathrm{d}u)$ 仍是 $(0, \infty) \times E \times (0, \infty)$ 上以 $\mathrm{ds}\pi(\mathrm{dz})\mathrm{d}u$ 为强度的泊松随机测度. 比较 (7.3.19) 式和 (7.3.22) 式知 $\mathbf{P}(X_{r+t} = j|G \cap \{X_r = i\}) = f_{ij}(t)$. 由全概率公式得

$$
\begin{array}{l} f _ {i j} (r + t) = \mathbf {P} (X _ {r + t} = j | X _ {0} = i) \\ = \sum_ {k \in E} \mathbf {P} (X _ {r} = k | X _ {0} = i) \mathbf {P} (X _ {r + t} = j | X _ {r} = k, X _ {0} = i) \\ = \sum_ {k \in E} f _ {i k} (r) f _ {k j} (t). \\ \end{array}
$$

这说明 $(F(t))_{t\geqslant 0} = \{f_{ij}(t):i,j\in E):t\geqslant 0\}$ 为 $E$ 上的转移矩阵, 而 $(X_{t}:t\geqslant 0)$ 是以 $(F(t))_{t\geqslant 0}$ 为转移矩阵的马氏链. 注意 $f_{ij}(t) = \mathbf{P}_i(\zeta >t,X_t = j)$. 根据推论7.2.4知$(F(t))_{t\geqslant 0}$ 由(7.2.15)式或(7.3.14)式给出. 再由定理7.3.12知 $F$ 是其密度矩阵的最小转移矩阵. 下面证明 $(F(t))_{t\geqslant 0}$ 的密度矩阵为 $Q$. 对于固定的 $i\in E$, 定义左极右连过程

$$
Z _ {t} = \int_ {0} ^ {t} \int_ {E} \int_ {0} ^ {q (i, z)} z N (\mathrm{d} s, \mathrm{d} z, \mathrm{d} u), \quad t \geqslant 0.
$$

由定理 1.5.8 知  $(Z_{t}: t \geqslant 0)$  是以  $q_{i}$  为跳跃速率以  $q_{i}^{-1} q(i, z) \pi(\mathrm{d}z)$  为跳跃分布的复合泊松过程. 令  $T_{1}$  为其首次跳跃时间. 注意, 在  $P_{i}$  之下有

$$
X _ {t \wedge T _ {1}} = i + \int_ {0} ^ {t \wedge T _ {1}} \int_ {E} \int_ {0} ^ {q (i, z)} (z - i) N (\mathrm{d} s, \mathrm{d} z, \mathrm{d} u).
$$

故 $T_{1}$ 也是 $(X_{t}:t\geqslant 0)$ 的首次跳跃时间且

$$
X _ {T _ {1}} = i + \int_ {\{T _ {1} \}} \int_ {E} \int_ {0} ^ {q (i, z)} (z - i) N (\mathrm{d} s, \mathrm{d} z, \mathrm{d} u) = Z _ {T _ {1}}.
$$

所以有

$$
\mathbf {P} _ {i} (T _ {1} \leqslant t, X _ {T _ {1}} = j) = \mathbf {P} _ {i} (T _ {1} \leqslant t, Z _ {T _ {1}} = j) = (1 - \mathrm{e} ^ {- q _ {i} t}) q _ {i} ^ {- 1} q (i, j).
$$

再由定理7.2.2知 $(F(t))_{t\geqslant 0}$ 有密度矩阵 $Q$ □

随机积分方程 (7.3.19) 的关键结构是通过在随机区间 $(0, q(X_{s-}, z)]$ 上的积分得到解的随机跳跃强度 $q(X_{s-}, z)$. 关于泊松随机测度驱动的随机方程的研究, 可以参考 [20] 等.

## 练习题

1. 设向前微分方程 (7.3.3) 成立, 则对 $s, t \geqslant 0$ 和 $i, j \in E$ 有

$$
p _ {i j} ^ {\prime} (s + t) = \sum_ {l \in E} p _ {i l} (s) p _ {l j} ^ {\prime} (t).
$$

2. 设向后微分方程 (7.3.4) 成立, 则对 $s, t \geqslant 0$ 和 $i, j \in E$ 有

$$
p _ {i j} ^ {\prime} (s + t) = \sum_ {l \in E} p _ {i l} (s) p _ {l j} ^ {\prime} (t).
$$

3. 对于有限状态空间 $E$, 任何马氏转移矩阵 $(P(t))_{t \geqslant 0}$ 的密度矩阵 $Q$ 是保守的, 而且向前和向后方程都成立.

提示: 由定理 7.2.1(3) 的证明不难看出, 当状态空间 E 有限时, 任何马氏转移矩阵的密度矩阵保守. 分别将 (7.3.1) 式和 (7.3.2) 式两边同除以 h 并令  $h \rightarrow 0+$  即得 (7.3.3) 式和 (7.3.4) 式.

4. 设 $E$ 是有限状态空间, 而 $Q$ 为 $E$ 上的保守密度矩阵, 则可定义 $E$ 上的马氏转移矩阵 $P = (P(t): t \geqslant 0)$ 如下:

$$
P (t) = \mathrm{e} ^ {Q t} := \sum_ {n = 0} ^ {\infty} \frac {t ^ {n}}{n !} Q ^ {n}, \quad t \geqslant 0.
$$

证明  $Q = P'(0)$  且  $(P(t))_{t \geqslant 0}$  是 Q 的向后方程的唯一解, 也是 Q 的向前方程的唯一解.

5. 考虑状态空间 $\mathbb{Z}_{+}$ 上参数为 $\alpha > 0$ 的泊松过程, 其转移矩阵 $(P(t): t \geqslant 0)$ 和密度矩阵 $Q$ 分别由例7.1.2和例7.2.1给出. 证明 $P(t) = \mathrm{e}^{Qt}$.

提示: 令  $D = Q + I$ , 则

$$
\begin{array}{l} P (t) = \mathrm{e} ^ {- \alpha t} \sum_ {k = 0} ^ {\infty} \frac {(\alpha t) ^ {k}}{k !} D ^ {k} = \sum_ {k = 0} ^ {\infty} \frac {(\alpha t) ^ {k}}{k !} D ^ {k} \sum_ {i = 0} ^ {\infty} \frac {(- 1) ^ {i} (\alpha t) ^ {i}}{i !} \\ = \sum_ {n = 0} ^ {\infty} \sum_ {k = 0} ^ {n} \frac {(- 1) ^ {n - k} (\alpha t) ^ {n}}{k ! (n - k) !} D ^ {k} = \sum_ {n = 0} ^ {\infty} \frac {(\alpha t) ^ {n}}{n !} (D - I) ^ {n} = \mathrm{e} ^ {Q t}. \\ \end{array}
$$

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