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