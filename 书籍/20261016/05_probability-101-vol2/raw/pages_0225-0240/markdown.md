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