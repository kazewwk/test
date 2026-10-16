这样, 对 (5.2.5) 式应用控制收敛定理得

$$
F ^ {\prime} (x) = \frac {1}{2 \pi} \int_ {- \infty} ^ {\infty} \mathrm{e} ^ {- \mathrm{i} t x} f (t) \lim _ {\delta \to 0} \frac {1 - \mathrm{e} ^ {- \mathrm{i} t \delta}}{\mathrm{i} t \delta} \mathrm{d} t = \frac {1}{2 \pi} \int_ {- \infty} ^ {\infty} \mathrm{e} ^ {- \mathrm{i} t x} f (t) \mathrm{d} t.
$$

所以 $F$ 是绝对连续型分布函数, 且具有所给的密度函数 $p(x)$. 再次应用控制收敛定理可知 $p(x)$ 为连续函数. $\square$

## 练习题

1. 称随机变量 $\xi$ 是对称的, 是指对于任何 $x \geqslant 0$ 有 $\mathbf{P}(\xi \geqslant x) = \mathbf{P}(\xi \leqslant -x)$. 证明 $\xi$ 为对称随机变量当且仅当其特征函数 $f_{\xi}$ 为实值偶函数.
2. 设非负数列  $\{r_{1}, r_{2}, \cdots\}$  满足  $\sum_{k=1}^{\infty} r_{k} = 1$ . 证明  $f(t) = \sum_{k=1}^{\infty} r_{k} \cos(kt)$  是某个概率分布的特征函数, 并给出此概率分布.
3. 设 $\mathbb{R}$ 上的概率分布函数 $F$ 有特征函数 $f$. 证明对任何 $x \in \mathbb{R}$ 有

$$
\lim _ {T \to \infty} \frac {1}{2 T} \int_ {- T} ^ {T} \mathrm{e} ^ {- \mathrm{i} t x} f (t) \mathrm{d} t = F (x) - F (x -).
$$

提示: 注意

$$
\frac {1}{2 T} \int_ {- T} ^ {T} \mathrm{e} ^ {- \mathrm{i} t x} f (t) \mathrm{d} t = \int_ {- \infty} ^ {\infty} g _ {T} (x, y) \mathrm{d} F (y),
$$

其中

$$
g _ {T} (x, y) = \frac {1}{T} \int_ {0} ^ {T} \cos [ t (y - x) ] \mathrm{d} t \rightarrow 1 _ {\{x = y \}}, \quad T \rightarrow \infty .
$$

4. 设 $X$ 为绝对连续型随机变量。令 $f(t)$ 为其特征函数。证明当 $t \to \infty$ 时有 $f(t) \to 0$.

提示: 称为泊松引理. 利用一致连续性和模可积性.

5. 设 $\mathbb{R}$ 上的概率分布函数 $F$ 有特征函数 $f$. 对于 $n \geqslant 1$ 令

$$
F _ {n} (x) = \frac {n}{2} \int_ {x - 1 / n} ^ {x + 1 / n} F (y) \mathrm{d} y, \quad x \in \mathbb {R}.
$$

(1) 证明每个 $F_{n}$ 都是绝对连续型概率分布函数;
(2) 证明当 $n \to \infty$ 时对 $F$ 的任何连续点 $x \in \mathbb{R}$ 有 $F_{n}(x) \to F(x)$;
(3) 求 $F_{n}$ 的特征函数 $f_{n}$, 并证明当 $n \to \infty$ 时对一切 $t \in \mathbb{R}$ 有 $f_{n}(t) \to f(t)$.

## 5.3 多元特征函数

## 5.3.1 定义和基本性质

定义 5.3.1 设  $\xi=(\xi_{1},\xi_{2},\cdots,\xi_{d})$  是定义在概率空间  $(\Omega,\mathcal{F},\mathbf{P})$  上的 d 维随机向量，且有联合分布函数 F. 我们称

$$
f (t) := \mathbf {E} (\mathrm{e} ^ {\mathrm{i} \langle t, \xi \rangle}) = \mathbf {E} \big [ \mathrm{e} ^ {\mathrm{i} (t _ {1} \xi_ {1} + t _ {2} \xi_ {2} + \dots + t _ {n} \xi_ {n})} \big ], \quad t = (t _ {1}, t _ {2}, \dots , t _ {d}) \in \mathbb {R} ^ {d}
$$

为  $\xi$  或 F 的特征函数, 这里  $\langle t, \xi \rangle = t_{1}\xi_{1} + t_{2}\xi_{2} + \cdots + t_{n}\xi_{n}$  表示内积. 为了强调, 有时也称 f 为多元特征函数.

利用随机向量的特征函数可以容易地得到其分量的特征函数, 这就是

命题 5.3.1 令 f 为随机向量  $\xi = (\xi_{1}, \xi_{2}, \cdots, \xi_{d})$  的特征函数. 则对  $1 \leqslant k \leqslant d$  分量  $\xi_{k}$  的特征函数为

$$
f _ {k} (t _ {k}) = f (0, \dots , t _ {k}, \dots , 0), \quad t _ {k} \in \mathbb {R}.
$$

上式右端 $f$ 的第 $k$ 个变量取 $t_k$ 而其余的变量全部取零.

多元特征函数有着与一元特征函数类似的性质. 下面的命题和定理的证明可模仿一元情况给出, 这里省略.

命题 5.3.2 随机向量  $\xi=(\xi_{1},\xi_{2},\cdots,\xi_{d})$  的特征函数 f 具有如下性质:

(1) 有界性:  $|f(t)| = |f(t_{1}, t_{2}, \cdots, t_{d})| \leqslant f(0) = f(0, 0, \cdots, 0) = 1;$
(2) 共轭对称性:  $f(-t_{1}, -t_{2}, \cdots, -t_{d}) = \overline{f(t_{1}, t_{2}, \cdots, t_{d})}$ ;
(3) 线性变换的特征函数: 对于 $a \in \mathbb{R}$ 和 $b \in \mathbb{R}^d$, 随机变量 $\eta := a + \langle b, \xi \rangle$ 的特征函数为

$$
f _ {\eta} (t) = \mathrm{e} ^ {\mathrm{i} a t} f (b t) = \mathrm{e} ^ {\mathrm{i} a t} f (b _ {1} t, b _ {2} t, \dots , b _ {d} t), \quad t \in \mathbb {R}.
$$

(4) 一致连续性: $f$ 在 $\mathbb{R}^d$ 上一致连续;
(5) 与矩的关系: 若随机变量  $\xi_{1}^{k_{1}}\xi_{2}^{k_{2}}\cdots\xi_{d}^{k_{d}}$  可积, 则

$$
\mathbf {E} \big (\xi_ {1} ^ {k _ {1}} \xi_ {2} ^ {k _ {2}} \dots \xi_ {d} ^ {k _ {d}} \big) = \mathrm{i} ^ {- k} \frac {\partial^ {k} f}{\partial t _ {1} ^ {k _ {1}} \partial t _ {2} ^ {k _ {2}} \cdots \partial t _ {d} ^ {k _ {d}}} (0, 0, \dots , 0),
$$

其中  $k = k_{1} + k_{2} + \cdots + k_{d}.$

定理 5.3.3（反演公式）设 d 维随机向量  $\xi = (\xi_{1}, \xi_{2}, \cdots, \xi_{d})$  有特征函数 f. 对于  $1 \leqslant k \leqslant d$  用  $C_{F_{k}}$  表示分量  $\xi_{k}$  的边缘分布函数  $F_{k}$  的连续点集，并取  $a_{k} \leqslant b_{k} \in C_{F_{k}}$ . 则有

$$
\mathbf {P} \big (a _ {1} <   \xi_ {1} <   b _ {1}, a _ {2} <   \xi_ {2} <   b _ {2}, \dots , a _ {d} <   \xi_ {d} <   b _ {d} \big)
$$

$$
= \lim _ {c \to \infty} \frac {1}{(2 \pi) ^ {d}} \int_ {[ - c, c ] ^ {d}} \Big (\prod_ {k = 1} ^ {d} \frac {\mathrm{e} ^ {- \mathrm{i} t _ {k} a _ {k}} - \mathrm{e} ^ {- \mathrm{i} t _ {k} b _ {k}}}{\mathrm{i} t _ {k}} \Big) f (t) \mathrm{d} t.
$$

定理 5.3.4（唯一性定理） 随机向量的联合分布函数由其特征函数唯一决定.

## 5.3.2 独立性条件

由独立随机变量构成的随机向量的特征函数具有非常简单的结构. 事实上, 下面的定理给出了有限个随机变量相互独立的充要条件.

定理 5.3.5 设随机向量  $\xi = (\xi_{1}, \xi_{2}, \cdots, \xi_{d})$  有特征函数 f. 则  $\xi_{1}, \xi_{2}, \cdots, \xi_{d}$  相互独立当且仅当

$$
f (t) = f _ {1} (t _ {1}) f _ {2} (t _ {2}) \dots f _ {d} (t _ {d}), \quad t = (t _ {1}, t _ {2}, \dots , t _ {d}) \in \mathbb {R} ^ {d}, \tag {5.3.1}
$$

其中  $f_{k}$  表示分量  $\xi_{k}$  的特征函数.

证明 假设  $\xi_{1},\xi_{2},\cdots,\xi_{d}$  相互独立. 则  $e^{it\xi_{1}},e^{it\xi_{2}},\cdots,e^{it\xi_{d}}$  相互独立. 因此

$$
f (t) = \mathbf {E} \big [ \mathrm{e} ^ {\mathrm{i} (t _ {1} \xi_ {1} + t _ {2} \xi_ {2} + \dots + t _ {d} \xi_ {d})} \big ] = \mathbf {E} (\mathrm{e} ^ {\mathrm{i} t _ {1} \xi_ {1}}) \mathbf {E} (\mathrm{e} ^ {\mathrm{i} t _ {2} \xi_ {2}}) \dots \mathbf {E} (\mathrm{e} ^ {\mathrm{i} t _ {d} \xi_ {d}}) = f _ {1} (t _ {1}) f _ {2} (t _ {2}) \dots f _ {d} (t _ {d}).
$$

反之，假设(5.3.1)式成立.设 $x = (x_{1}, x_{2}, \dots, x_{d}) \in \mathbb{R}^{d}$.对于 $1 \leqslant k \leqslant d$ 可取 $a_{k,n} \leqslant b_{k,n} \in C_{F_k}$ 使当 $n \to \infty$ 时有 $a_{k,n} \downarrow -\infty$ 且 $b_{k,n} \downarrow x_k$.由反演公式和(5.3.1)式易得

$$
\begin{array}{l} \mathrm{P} \left(a _ {1, n} <   \xi_ {1} <   b _ {1, n}, a _ {2, n} <   \xi_ {2} <   b _ {2, n}, \dots , a _ {d, n} <   \xi_ {d} <   b _ {d, n}\right) \\ = \lim _ {c \to \infty} \frac {1}{(2 \pi) ^ {d}} \int_ {[ - c, c ] ^ {d}} \Big (\prod_ {k = 1} ^ {d} \frac {\mathrm{e} ^ {- \mathrm{i} t _ {k} a _ {k , n}} - \mathrm{e} ^ {- \mathrm{i} t _ {k} b _ {k , n}}}{\mathrm{i} t _ {k}} \Big) f (t) \mathrm{d} t \\ = \lim _ {c \to \infty} \frac {1}{(2 \pi) ^ {d}} \int_ {[ - c, c ] ^ {d}} \left[ \prod_ {k = 1} ^ {d} \frac {\mathrm{e} ^ {- \mathrm{i} t _ {k} a _ {k , n}} - \mathrm{e} ^ {- \mathrm{i} t _ {k} b _ {k , n}}}{\mathrm{i} t _ {k}} f _ {k} (t _ {k}) \right] \mathrm{d} t \\ = \lim _ {c \to \infty} \frac {1}{(2 \pi) ^ {d}} \prod_ {k = 1} ^ {d} \int_ {[ - c, c ]} \left[ \frac {\mathrm{e} ^ {- \mathrm{i} t _ {k} a _ {k , n}} - \mathrm{e} ^ {- \mathrm{i} t _ {k} b _ {k , n}}}{\mathrm{i} t _ {k}} f _ {k} (t _ {k}) \right] \mathrm{d} t _ {k} \\ = \mathbf {P} \big (a _ {1, n} <   \xi_ {1} <   b _ {1, n} \big) \mathbf {P} (a _ {2, n} <   \xi_ {2} <   b _ {2, n}) \dots \mathbf {P} \big (a _ {d, n} <   \xi_ {d} <   b _ {d, n} \big). \\ \end{array}
$$

在上式两端令 $n\to \infty$ 得

$$
F (x _ {1}, x _ {2}, \dots , x _ {d}) = F _ {1} (x _ {1}) F _ {2} (x _ {2}) \dots F _ {d} (x _ {d}).
$$

由此知  $\xi_{1},\xi_{2},\cdots,\xi_{d}$  相互独立.

![](images/page_162_image_16.jpg)

## 5.3.3 独立和的特征函数

定理 5.3.6 设随机变量  $\xi_{1}, \xi_{2}, \cdots, \xi_{d}$  相互独立. 对  $1 \leqslant k \leqslant d$  用  $f_{k}$  表示分量  $\xi_{k}$  的特征函数. 令  $\eta = \xi_{1} + \xi_{2} + \cdots + \xi_{d}$ . 则

$$
f _ {\eta} (t) = f _ {1} (t) f _ {2} (t) \dots f _ {d} (t), \quad t \in \mathbb {R}. \tag {5.3.2}
$$

证明 用  $f_{\xi}$  表示随机向量  $\xi = (\xi_{1}, \xi_{2}, \cdots, \xi_{d})$  的特征函数. 则对任意  $t \in R$  有

$$
f _ {\eta} (t) = \mathbf {E} [ \mathrm{e} ^ {\mathrm{i} t (\xi_ {1} + \xi_ {2} + \dots + \xi_ {d})} ] = \mathbf {E} [ \mathrm{e} ^ {\mathrm{i} (t \xi_ {1} + t \xi_ {2} + \dots + t \xi_ {d})} ] = f _ {\xi} (t, t, \dots , t).
$$

由定理 5.3.5 即得欲证结论.

在定理 5.3.6 的情况下, 令  $\mu_{1}, \mu_{2}, \cdots, \mu_{d}$  分别为随机变量  $\xi_{1}, \xi_{2}, \cdots, \xi_{d}$  的分布, 称  $\eta = \xi_{1} + \xi_{2} + \cdots + \xi_{d}$  的分布  $\mu$  为  $\mu_{1}, \mu_{2}, \cdots, \mu_{d}$  的卷积, 并记作  $\mu = \mu_{1} * \mu_{2} * \cdots * \mu_{d}$ . 类似地, 令  $F_{1}, F_{2}, \cdots, F_{d}$  分别为随机变量  $\xi_{1}, \xi_{2}, \cdots, \xi_{d}$  的分布函数, 称  $\eta = \xi_{1} + \xi_{2} + \cdots + \xi_{d}$  的分布函数 F 为  $F_{1}, F_{2}, \cdots, F_{d}$  的多重卷积, 并记作  $F = F_{1} * F_{2} * \cdots * F_{d}$ . 根据定理 5.2.7 和定理 5.3.6, 卷积  $\mu$  和 F 由其特征函数 (5.3.2) 式唯一决定.

定理5.3.7 给定 $\mathbb{R}$ 上的概率分布函数 $F, G,$ 令 $H = F * G.$ 则

$$
H (x) = \int_ {- \infty} ^ {\infty} G (x - z) \mathrm{d} F (z), \quad x \in \mathbb {R}. \tag {5.3.3}
$$

证明 令 $H$ 由 (5.3.3) 式定义. 则对任意 $t \in \mathbb{R}$ 有

$$
\begin{array}{l} \int_ {- \infty} ^ {\infty} \mathrm{e} ^ {\mathrm{i} t x} \mathrm{d} H (x) = \int_ {- \infty} ^ {\infty} \mathrm{d} F (z) \int_ {- \infty} ^ {\infty} \mathrm{e} ^ {\mathrm{i} t x} \mathrm{d} G (x - z) \\ = \int_ {- \infty} ^ {\infty} \mathrm{e} ^ {\mathrm{i} t z} \mathrm{d} F (z) \int_ {- \infty} ^ {\infty} \mathrm{e} ^ {\mathrm{i} t x} \mathrm{d} G (x). \\ \end{array}
$$

由定理 5.3.5 即知  $H = F * G$ .

积分表达式 (5.3.3) 称为卷积公式. 该定义也用于 $F, G$ 为 $\mathbb{R}$ 上的任意有界分布函数的情况.

例 5.3.1 假设  $\xi,\eta$  独立且均服从泊松分布  $P(\lambda)$ . 则有  $f_{\xi}(t)=f_{\eta}(t)=\mathrm{e}^{\lambda(\mathrm{e}^{\mathrm{i}t}-1)}$ . 由  $\xi,\eta$  的独立性, 有

$$
f _ {\xi + \eta} (t) = f _ {\xi} (t) f _ {\eta} (t) = \mathrm{e} ^ {2 \lambda (\mathrm{e} ^ {\mathrm{i} t} - 1)}.
$$

再根据唯一性定理知  $\xi + \eta$  服从分布  $P(2\lambda)$ .

例 5.3.2 利用定理 5.3.6 及二项分布与伯努利分布的关系, 可得二项分布  $B(n,p)$  的特征函数为  $f(t)=(1-p+pe^{it})^{n}$ .

定理5.3.8 假设 $g$ 是母函数, 而 $f$ 是特征函数. 则 $g(f(t))$ 也是一个特征函数.

证明 设  $\eta, \xi_{1}, \xi_{2}, \cdots$  为独立随机变量, 其中  $\eta$  只取非负整数值且有母函数 g, 而  $\xi_{1}, \xi_{2}, \cdots$  同分布且有特征函数 f. 再令  $X = \sum_{k=1}^{\eta} \xi_{k}$ . 利用全期望公式和定理 5.3.6 得

$$
\begin{array}{l} \mathbf {E} (\mathrm{e} ^ {\mathrm{i} t X}) = \mathbf {E} \Big (\exp \left\{\mathrm{i} t \sum_ {k = 1} ^ {\eta} \xi_ {k} \right\} \Big) \\ = \sum_ {n = 0} ^ {\infty} \mathbf {P} (\eta = n) \mathbf {E} \left(\exp \left\{\mathrm{i} t \sum_ {k = 1} ^ {\eta} \xi_ {k} \right\} \mid \eta = n\right) \\ = \sum_ {n = 0} ^ {\infty} \mathbf {P} (\eta = n) \mathbf {E} \left(\exp \left\{\mathrm{i} t \sum_ {k = 1} ^ {n} \xi_ {k} \right\} \mid \eta = n\right) \\ = \sum_ {n = 0} ^ {\infty} \mathbf {P} (\eta = n) \mathbf {E} \left(\exp \left\{\mathrm{i} t \sum_ {k = 1} ^ {n} \xi_ {k} \right\}\right) \\ = \sum_ {n = 0} ^ {\infty} \mathbf {P} (\eta = n) f (t) ^ {n} = g (f (t)). \\ \end{array}
$$

所以  $g(f(t))$  是 X 的特征函数.

![](images/page_164_image_5.jpg)

推论 5.3.9 若 f 是特征函数, 则对任意  $\lambda \geqslant 0$  函数  $e^{\lambda[f(t)-1]}$  也是特征函数.

证明 令 $\eta$ 服从泊松分布 $P(\lambda)$. 则它有母函数 $g(z) = \mathrm{e}^{\lambda (z - 1)}$. 再应用命题5.3.8即得欲证结论. □

## \*5.3.4 拉普拉斯变换

特征函数涉及复值函数的积分, 有时会带来一些处理上的不便. 对于非负随机变量, 有一种简便和常用的变换, 即拉普拉斯变换, 它可以作为特征函数的替代工具.

定义 5.3.2 设  $\xi=(\xi_{1},\xi_{2},\cdots,\xi_{d})$  是取值于  $R_{+}^{d}$  的随机向量，且有联合分布函数 F. 我们称

$$
L (t) := \mathbf {E} (\mathrm{e} ^ {- \langle t, \xi \rangle}) = \mathbf {E} \big [ \mathrm{e} ^ {- (t _ {1} \xi_ {1} + t _ {2} \xi_ {2} + \dots + t _ {n} \xi_ {n})} \big ], \quad t = (t _ {1}, t _ {2}, \dots , t _ {d}) \in \mathbb {R} _ {+} ^ {d}
$$

为  $\xi$  或 F 的拉普拉斯变换, 这里  $\langle t, \xi \rangle = t_{1}\xi_{1} + t_{2}\xi_{2} + \cdots + t_{n}\xi_{n}$  表示内积.

拉普拉斯变换本质上是特征函数的特殊情况. 若分别用 $L$ 和 $f$ 表示取值于 $\mathbb{R}_+^d$ 的随机向量 $\xi$ 的拉普拉斯变换和特征函数, 则形式上有

$$
L (t) = f (\mathrm{i} t), \quad t = (t _ {1}, t _ {2}, \dots , t _ {d}) \in \mathbb {R} ^ {d}.
$$

对于拉普拉斯变换, 我们不加证明地给出如下的定理.

定理 5.3.10（唯一性定理） 取值于  $R_{+}^{d}$  的随机向量的联合分布函数由其拉普拉斯变换唯一决定.

定理 5.3.11 设取值于  $R_{+}^{d}$  的随机向量  $\xi = (\xi_{1}, \xi_{2}, \cdots, \xi_{d})$  有拉普拉斯变换 L. 则  $\xi_{1}, \xi_{2}, \cdots, \xi_{d}$  相互独立当且仅当

$$
L (t) = L _ {1} (t _ {1}) L _ {2} (t _ {2}) \dots L _ {d} (t _ {d}), \quad t = (t _ {1}, t _ {2}, \dots , t _ {d}) \in \mathbb {R} _ {+} ^ {d},
$$

其中  $L_{k}$  表示分量  $\xi_{k}$  的拉普拉斯变换.

定理 5.3.12 设非负随机变量  $\xi_{1}, \xi_{2}, \cdots, \xi_{d}$  相互独立. 对  $1 \leqslant k \leqslant d$ , 用  $L_{k}$  表示分量  $\xi_{k}$  的特征函数. 则  $\eta := \xi_{1} + \xi_{2} + \cdots + \xi_{d}$  的拉普拉斯变换为

$$
L _ {\eta} (t) = L _ {1} (t) L _ {2} (t) \dots L _ {d} (t), \quad t \in \mathbb {R} _ {+}. \tag {5.3.4}
$$

例5.3.3 伽马分布 $\Gamma (\lambda ,r)$ 的拉普拉斯变换为

$$
L (t) = \frac {\lambda^ {r}}{\Gamma (r)} \int_ {0} ^ {\infty} x ^ {r - 1} \mathrm{e} ^ {- (\lambda + t) x} \mathrm{d} x = \frac {\lambda^ {r}}{(\lambda + t) ^ {r}}.
$$

因此, 若独立随机变量 $\xi_{1}$ 和 $\xi_{2}$ 分别服从分布 $\Gamma(\lambda, r_{1})$ 和 $\Gamma(\lambda, r_{2})$, 则 $\xi_{1} + \xi_{2}$ 服从分布 $\Gamma(\lambda, r_{1} + r_{2})$.

关于拉普拉斯变换的更多的讨论, 可以参阅 [7,8,11].

## 练习题

1. 设随机向量 $(\xi, \eta)$ 服从二维正态分布 $N(a_{1}, a_{2}; \sigma^{2}, \sigma^{2}; r)$. 证明

$$
\mathbf {E} (\xi \vee \eta) = \sqrt {\frac {1 - r}{\pi}}.
$$

2. 设随机变量  $\xi_{1}, \xi_{2}, \cdots, \xi_{n}$  相互独立且均服从  $N(0,1)$ . 记

$$
X = \sum_ {k = 1} ^ {n} a _ {k} \xi_ {k}, \quad Y = \sum_ {k = 1} ^ {n} b _ {k} \xi_ {k},
$$

证明 $X$ 与 $Y$ 独立的充要条件为 $\sum_{k=1}^{n} a_k b_k = 0$.

3. 设随机向量  $(\xi,\eta)$  服从  $N(a_{1},a_{2};\sigma_{1}^{2},\sigma_{2}^{2};r)$ . 记

$$
U = a \xi + b \eta , \quad V = c \xi + d \eta .
$$

(1) 求 U 与 V 的数学期望, 方差及相关系数;
(2) 写出 $(U, V)$ 的分布;
(3) 在何种情况下  $(U, V)$  的分布退化为一维分布?
(4) 在何种情况下 U 与 V 独立?

4. 伽马分布 $\Gamma(\lambda, r)$ 的密度函数为

$$
p (x) = \frac {\lambda^ {r}}{\Gamma (r)} x ^ {r - 1} \mathrm{e} ^ {- \lambda x}, \quad x > 0.
$$

对满足 a > 0 的复数  $c = a + ib$ ，承认如下等式成立:

$$
c ^ {r} \int_ {0} ^ {\infty} x ^ {r - 1} \mathrm{e} ^ {- c x} \mathrm{d} x = \Gamma (r).
$$

求  $\Gamma(\lambda,r)$  的特征函数.

5. 设随机变量  $\xi_{1}, \xi_{2}, \cdots, \xi_{n}$  相互独立且均服从指数分布  $E(\lambda)$ . 证明  $\xi_{1} + \xi_{2} + \cdots + \xi_{n}$  服从伽马分布  $\Gamma(\lambda, n)$ .
6. 设  $\xi_{1}, \xi_{2}, \cdots$  是某个概率空间上的随机变量序列，且对任何  $n \geqslant 1$  随机向量  $(\xi_{1}, \xi_{2}, \cdots, \xi_{n})$  和  $\xi_{n+1}$  独立。证明  $\xi_{1}, \xi_{2}, \cdots$  相互独立。

## \*5.4 正态随机向量

本节讨论多维正态随机向量, 多元特征函数的工具在这里发挥了关键作用. 后面提到的正态分布允许是退化的.

## 5.4.1 多维正态分布

定理5.4.1 设 $a \in \mathbb{R}^d$ 是 $d$ 维行向量, 而 $B$ 是 $d$ 阶正定矩阵. 对于 $x \in \mathbb{R}^d$, 令

$$
p (x) = \frac {1}{(2 \pi) ^ {d / 2} | B | ^ {1 / 2}} \exp \Big \{- \frac {1}{2} \big \langle (x - a) B ^ {- 1}, x - a \big \rangle \Big \}. \tag {5.4.1}
$$

则 $p$ 为 $\mathbb{R}^d$ 上的分布密度函数, 且相应的特征函数为

$$
f (t) = \exp \left\{\mathrm{i} \langle a, t \rangle - \frac {1}{2} \langle t B, t \rangle \right\}, \quad x \in \mathbb {R} ^ {d}.
$$

证明 由于 $B$ 正定, 存在可逆矩阵 $A$ 使得 $B = A^{\mathrm{T}}A$. 令 $y = (x - a)A^{-1}$, 则 $x = a + yA$. 容易计算该变换的雅可比行列式为

$$
\left| \frac {\mathrm{d} x}{\mathrm{d} y} \right| = | A | = | B | ^ {1 / 2}.
$$

所以

$$
\int_ {\mathbb {R} ^ {d}} p (x) \mathrm{d} x = \frac {1}{(2 \pi) ^ {d / 2}} \int_ {\mathbb {R} ^ {d}} \exp \Big \{- \frac {1}{2} \langle y, y \rangle \Big \} \mathrm{d} y
$$

$$
= \prod_ {k = 1} ^ {d} \frac {1}{\sqrt {2 \pi}} \int_ {- \infty} ^ {\infty} \exp \left\{- \frac {1}{2} y _ {k} ^ {2} \right\} \mathrm{d} y _ {k} = 1,
$$

故 $p$ 为 $\mathbb{R}^d$ 上的分布密度函数. 对应的特征函数为

$$
\begin{array}{l} f (t) = \int_ {\mathbb {R} ^ {d}} \exp \{\mathrm{i} \langle t, x \rangle \} p (x) \mathrm{d} x \\ = \frac {1}{(2 \pi) ^ {d / 2}} \int_ {\mathbb {R} ^ {d}} \exp \left\{\mathrm{i} \langle t, a + y A \rangle - \frac {1}{2} \langle y, y \rangle \right\} \mathrm{d} y \\ = \exp \{\mathrm{i} \langle t, a \rangle \} \frac {1}{(2 \pi) ^ {d / 2}} \int_ {\mathbb {R} ^ {d}} \exp \left\{\mathrm{i} t (y A) ^ {\mathrm{T}} - \frac {1}{2} \langle y, y \rangle \right\} \mathrm{d} y \\ = \exp \left\{\mathrm{i} \langle t, a \rangle \right\} \frac {1}{(2 \pi) ^ {d / 2}} \int_ {\mathbb {R} ^ {d}} \exp \left\{\mathrm{i} t A ^ {\mathrm{T}} y ^ {\mathrm{T}} - \frac {1}{2} \langle y, y \rangle \right\} \mathrm{d} y \\ = \exp \{\mathrm{i} \langle a, t \rangle \} \frac {1}{(2 \pi) ^ {d / 2}} \int_ {\mathbb {R} ^ {d}} \exp \left\{\mathrm{i} \langle s, y \rangle - \frac {1}{2} \langle y, y \rangle \right\} \mathrm{d} y, \\ \end{array}
$$

其中 $s = tA^{\mathrm{T}}$ 利用一维标准正态分布的特征函数的表达式得

$$
\begin{array}{l} f (t) = \exp \{\mathrm{i} \langle a, t \rangle \} \prod_ {k = 1} ^ {d} \frac {1}{(2 \pi) ^ {1 / 2}} \int_ {- \infty} ^ {\infty} \exp \left\{i s _ {k} y _ {k} - \frac {1}{2} y _ {k} ^ {2} \right\} \mathrm{d} y _ {k} \\ = \exp \{\mathrm{i} \langle a, t \rangle \} \prod_ {k = 1} ^ {d} \exp \left\{- \frac {1}{2} s _ {k} ^ {2} \right\} \\ = \exp \left\{\mathrm{i} \langle a, t \rangle - \frac {1}{2} \langle s, s \rangle \right\} \\ = \exp \left\{\mathrm{i} \langle a, t \rangle - \frac {1}{2} \langle t A ^ {\mathrm{T}}, t A ^ {\mathrm{T}} \rangle \right\} \\ = \exp \left\{\mathrm{i} \langle a, t \rangle - \frac {1}{2} t A ^ {\mathrm{T}} A t ^ {\mathrm{T}} \right\} \\ = \exp \left\{\mathrm{i} \langle a, t \rangle - \frac {1}{2} \langle t B, t \rangle \right\}. \\ \end{array}
$$

故 p 具有所给的特征函数.

定义 5.4.1 设  $a \in R^{d}$ ，而 B 为 d 阶半正定矩阵。我们称特征函数

$$
f (t) = \exp \left\{\mathrm{i} \langle a, t \rangle - \frac {1}{2} \langle t B, t \rangle \right\}, \quad t \in \mathbb {R} ^ {d} \tag {5.4.2}
$$

所对应的 $\mathbb{R}^d$ 上的概率分布为 $d$ 维正态分布, 并记作 $N(a, B)$. 当 $B$ 退化时, 称 $N(a, B)$ 为退化 $d$ 维正态分布.

令 $I$ 为 $d$ 阶单位矩阵. 若 $B$ 为 $d$ 阶半正定矩阵, 则 $B_{n} := B + I / n$ 为 $d$ 阶正定矩阵, 且当 $n \to \infty$ 时有 $\langle tB_{n}, t \rangle \to \langle tB, t \rangle$. 令 $f_{n}$ 是将 (5.4.2) 式中的 $B$ 换为 $B_{n}$ 后所定义的函数. 由定理 5.4.1 知 $f_{n}$ 是 $\mathbb{R}^{d}$ 上的某个绝对连续型概率分布的特征函数. 据此, 利用后面将要学习的莱维连续性定理的多维形式可知, $f$ 的确是 $\mathbb{R}^{d}$ 上的某个概率分布的特征函数. 下面我们给出 $d$ 维正态分布的若干性质.

## 5.4.2 子向量的分布

定理 5.4.2 设随机向量  $\xi=(\xi_{1},\xi_{2},\cdots,\xi_{d})$  服从 d 维正态分布  $N(a,B)$ ，而  $1\leqslant k_{1}<k_{2}<\cdots<k_{n}\leqslant d$ 。则  $\xi$  的子向量  $\eta=(\xi_{k_{1}},\xi_{k_{2}},\cdots,\xi_{k_{n}})$  服从 n 维正态分布  $N(b,C)$ ，其中 b 是由 a 的第  $k_{1},k_{2},\cdots,k_{n}$  个分量构成的子向量，而 C 是由矩阵 B 的第  $k_{1},k_{2},\cdots,k_{n}$  行和列构成的子矩阵。

证明 令 $s = (s_1, s_2, \cdots, s_n) \in \mathbb{R}^n$, 并令 $t = (t_1, t_2, \cdots, t_d) \in \mathbb{R}^d$ 是第 $k_1, k_2, \cdots, k_n$ 个分量由 $s$ 的分量给出且其他分量为零的 $d$ 维向量. 则

$$
\mathbf {E} \exp \{\mathrm{i} \langle \eta , s \rangle \} = \mathbf {E} \exp \{\mathrm{i} \langle \xi , t \rangle \} = \exp \left\{\mathrm{i} \langle a, t \rangle - \frac {1}{2} \langle t B, t \rangle \right\},
$$

其中 $\langle a, t \rangle = \langle b, s \rangle$ 而 $\langle tB, t \rangle = \langle sC, s \rangle$. 因此 $\eta$ 服从分布 $N(b, C)$.

定理5.4.3 设随机向量 $\xi$ 服从 $d$ 维正态分布 $N(a, B)$. 则有 $a = \mathbf{E}\xi$ 和 $B = \operatorname{Var}\xi$.

证明 写  $a=(a_{1},a_{2},\cdots,a_{d})$  和  $B=(b_{kj})_{d\times d}$ . 对子向量  $\xi_{k}$  应用定理 5.4.2 知  $\xi_{k}$  服从正态分布  $N(a_{k},b_{kk})$ ，故有  $a_{k}=\mathbf{E}(\xi_{k})$  和  $b_{kk}=\mathbf{Var}(\xi_{k})$ . 再对子向量  $(\xi_{j},\xi_{k})$  应用定理 5.4.2 得

$$
\mathbf {E} \exp \{\mathrm{i} s _ {1} \xi_ {j} + \mathrm{i} s _ {2} \xi_ {k} \} = \exp \left\{\mathrm{i} a _ {j} s _ {1} + \mathrm{i} a _ {k} s _ {2} - \frac {b _ {j j} s _ {1} ^ {2}}{2} - \frac {b _ {k k} s _ {2} ^ {2}}{2} - b _ {j k} s _ {1} s _ {2} \right\}.
$$

在上式两端求 $s_1 = s_2 = 0$ 处的偏导数得 $\mathbf{E}(\xi_j\xi_k) = a_ja_k + b_{jk}$，故有 $b_{jk} = \mathbf{Cov}(\xi_j,\xi_k)$

定理 5.4.4 设随机向量  $\xi = (\xi_{1}, \xi_{2}, \cdots, \xi_{d})$  服从 d 维正态分布  $N(a, B)$ . 则  $\xi$  的 d 个分量相互独立当且仅当  $B = Var\xi$  为对角矩阵.

证明 “$\Rightarrow$” 设 $\xi$ 的分量相互独立. 则这些分量两两不相关, 故 $\mathbf{Cov}(\xi_j, \xi_k) = 0$ 对所有 $1 \leqslant j < k \leqslant d$ 成立, 即 $B$ 为对角矩阵.

“$\Leftarrow$”设 $B$ 为对角矩阵. 则 $\xi$ 的特征函数是其 $d$ 个分量的特征函数之积. 由定理5.3.5知这些分量相互独立. □

显然, 在定理 5.4.4 的情况下, $\xi$ 非退化当且仅当 $B = \operatorname{Var} \xi$ 的主对角线元素均严格正.

## 5.4.3 线性变换

定理5.4.5 设 $d$ 维随机向量 $\xi$ 服从分布 $N(a, B)$, 而 $C$ 为 $d \times n$ 矩阵. 则 $n$ 维随机向量 $\eta := \xi C$ 服从分布 $N(aC, C^{\mathrm{T}}BC)$.

证明 对于任意的  $s=(s_{1},s_{2},\cdots,s_{n})\in\mathbb{R}^{n}$ ，我们有

$$
\mathbf {E} \exp \{\mathrm{i} \langle \eta , s \rangle \} = \mathbf {E} \exp \{\mathrm{i} \langle \xi C, s \rangle \} = \exp \left\{\mathrm{i} \langle a C, s \rangle - \frac {1}{2} s C ^ {\mathrm{T}} B C s ^ {\mathrm{T}} \right\}.
$$

因此 $\eta$ 服从分布 $N(aC, C^{\mathrm{T}}BC)$.

定理5.4.6 设 $\xi$ 服从分布 $N(a, B)$. 则存在正交矩阵 $C$ 使 $\eta := \xi C$ 的所有分量相互独立.

证明 由矩阵论的结果, 存在正交矩阵 $C$ 使 $C^{\mathrm{T}}BC$ 为对角矩阵. 由定理5.4.4和定理5.4.5知 $\eta$ 的分量相互独立. □

定理5.4.7 随机向量 $\xi$ 服从 $d$ 维正态分布当且仅当对任意的 $s \in \mathbb{R}^d$ 线性组合 $\langle \xi, s \rangle$ 服从一维正态分布.

证明 “$\Rightarrow$” 设 $\xi$ 服从 $d$ 维正态分布 $N(a, B)$. 由定理 5.4.5 知 $\langle \xi, s \rangle$ 服从一维正态分布.

“$\Leftarrow$”设 $\xi = (\xi_1, \xi_2, \cdots, \xi_d)$ 是 $d$ 维随机向量，且对任意的 $s \in \mathbb{R}^d$ 线性组合 $\langle \xi, s \rangle$ 服从一维正态分布。则 $\xi$ 的分量 $\xi_1, \xi_2, \cdots, \xi_d$ 均服从一维正态分布，故它们都是平方可积的。令 $a = (a_1, a_2, \cdots, a_d)$ 和 $B = (b_{jk})_{d \times d}$，其中 $a_j = \mathbf{E}(\xi_j)$ 而 $b_{jk} = \mathbf{Cov}(\xi_j, \xi_k)$。则对 $t \in \mathbb{R}^d$，线性组合 $\eta := \langle \xi, t \rangle$ 有期望 $\langle a, t \rangle$ 和方差 $\langle tB, t \rangle$。再由假定知 $\eta$ 服从一维正态分布 $N(\langle a, t \rangle, \langle tB, t \rangle)$。所以 $\eta$ 有特征函数

$$
f _ {\eta} (s) = \mathbf {E} \exp \{\mathrm{i} s \langle \xi , t \rangle \} = \exp \left\{\mathrm{i} s \langle a, t \rangle - \frac {1}{2} s ^ {2} \langle t B, t \rangle \right\}, \quad s \in \mathbb {R}.
$$

在上式中取 $s = 1$ 知 $\xi$ 有特征函数

$$
f (t) = \mathbf {E} \exp \{\mathrm{i} \langle \xi , t \rangle \} = \exp \left\{\mathrm{i} \langle a, t \rangle - \frac {1}{2} \langle t B, t \rangle \right\}, \quad t \in \mathbb {R} ^ {d}.
$$

这说明  $\xi$  服从 d 维正态分布  $N(a,B)$ .

例5.4.1 设 $\xi, \eta$ 相互独立且均服从正态分布 $N(0,1)$. 令

$$
\zeta = \left\{ \begin{array}{l l} | \eta |, & \xi \geqslant 0, \\ - | \eta |, & \xi <   0. \end{array} \right.
$$

由  $\xi,\eta$  的独立性, 我们有

$$
\begin{array}{l} F _ {\zeta} (x) = \mathbf {P} (\zeta \leqslant x, \xi \geqslant 0) + \mathbf {P} (\zeta \leqslant x, \xi <   0) \\ = \mathbf {P} (| \eta | \leqslant x, \xi \geqslant 0) + \mathbf {P} (- | \eta | \leqslant x, \xi <   0) \\ = \frac {1}{2} \mathbf {P} (| \eta | \leqslant x) + \frac {1}{2} \mathbf {P} (| \eta | \geqslant - x). \\ \end{array}
$$

不论 $x > 0$ 或 $x \leqslant 0$, 均有 $F_{\zeta}(x) = \Phi(x)$, 故 $\zeta$ 服从分布 $N(0,1)$.

例 5.4.2 在上例中, 随机变量  $\xi, \zeta$  均服从正态分布  $N(0,1)$ . 特别地, 有  $\mathbf{P}(\xi \geqslant 0) = \mathbf{P}(\xi < 0) = 1/2$ . 再由  $\xi, \eta$  的独立性,

$$
\mathbf {P} (\eta \geqslant 0 | \xi \geqslant 0) = \mathbf {P} (\eta <   0 | \xi \geqslant 0)
$$

$$
\begin{array}{l} = \mathbf {P} (\eta \geqslant 0 | \xi <   0) \\ = \mathbf {P} (\eta <   0 | \xi <   0) = 1 / 2. \\ \end{array}
$$

这样, 根据全概率公式,

$$
\begin{array}{l} \mathbf {P} (\zeta + \eta = 0) = \mathbf {P} (\xi \geqslant 0) \mathbf {P} (\zeta + \eta = 0 | \xi \geqslant 0) + \mathbf {P} (\xi <   0) \mathbf {P} (\zeta + \eta = 0 | \xi <   0) \\ = \mathbf {P} (\xi \geqslant 0) \mathbf {P} (\eta <   0 | \xi \geqslant 0) + \mathbf {P} (\xi <   0) \mathbf {P} (\eta \geqslant 0 | \xi <   0) = 1 / 2. \\ \end{array}
$$

所以线性组合 $\zeta +\eta$ 不服从一维正态分布.这说明随机向量 $(\eta ,\zeta)$ 不服从二维正态分布，故两个一维正态分布随机变量并不一定构成一个二维正态分布随机向量.

## 练习题

1. 设随机向量 $\xi = (\xi_1, \xi_2)$ 服从二维正态分布 $N(a, B)$, 其中 $B = \begin{pmatrix} \sigma^2 & r\sigma^2 \\ r\sigma^2 & \sigma^2 \end{pmatrix}$. 证明 $\eta_1 = \xi_1 + \xi_2$ 与 $\eta_2 = \xi_1 - \xi_2$ 独立.
2. 设随机向量 $(\xi_1, \xi_2)$ 服从二维正态分布 $N(a, B)$, 其中 $B = \begin{pmatrix} \sigma_1^2 & r\sigma_1\sigma_2 \\ r\sigma_1\sigma_2 & \sigma_2^2 \end{pmatrix}$. 求 $\xi_1 + \xi_2$ 的密度函数.
3. 设随机向量 $(\xi_1, \xi_2, \xi_3)$ 服从三维正态分布 $N(a, B)$, 其中 $B = \begin{pmatrix} 2 & 1 & 0 \\ 1 & 1 & 0 \\ 0 & 0 & 2 \end{pmatrix}$. 证明 $\xi_1$ 与 $\xi_2$ 不独立, 但 $(\xi_1, \xi_2)$ 与 $\xi_3$ 独立.
4. 设随机向量  $(\xi_{1}, \xi_{2}, \cdots, \xi_{n})$  服从 n 维正态分布. 证明对任何常数  $b_{1}, b_{2}, \cdots, b_{n}, x$  有  $\mathbf{P}(b_{1}\xi_{1} + b_{2}\xi_{2} + \cdots + b_{n}\xi_{n} = x) = 0$  或 1.
5. 设随机变量  $\xi_{1}, \xi_{2}, \cdots, \xi_{n}$  独立且均服从正态分布  $N(a, \sigma^{2})$ . 定义  $\eta_{1} = \sum_{i=1}^{n} \alpha_{i} \xi_{i}$  和  $\eta_{2} = \sum_{i=1}^{n} \beta_{i} \xi_{i}$ , 其中  $\alpha_{i}$  和  $\beta_{i}$  为实常数且满足  $\sum_{i=1}^{n} \alpha_{i} \beta_{i} = 0$ . 证明  $\eta_{1}$  与  $\eta_{2}$  独立且均服从正态分布.

## 第六章

## 收敛性质

收敛性质是随机变量及其分布的重要性质。经常使用的随机变量列的收敛包括几乎必然收敛、依概率收敛、平均收敛和依分布收敛。在本章中，我们对上述几种收敛的概念、基本性质和相互关系进行简单的讨论，还将介绍关于分布函数收敛的斯科罗霍德(Skorokhod)表示定理，黑利(Helly)定理和莱维(Lévy)连续性定理。这里的讨论是后面的概率极限定理的基础。

## 6.1 随机变量的收敛

本节中我们讨论几乎必然收敛、依概率收敛和平均收敛. 考虑某个概率空间  $(\Omega, \mathcal{F}, \mathbf{P})$  上的随机变量  $\xi, \xi_{1}, \xi_{2}, \cdots$ .

## 6.1.1 几乎必然收敛

定义 6.1.1 称序列  $\{\xi_{n}\}$  几乎必然收敛到  $\xi,$  并记作  $\xi_{n} \rightarrow \xi$  (a.s.) 或  $\xi_{n} \stackrel{a.s.}{\rightarrow} \xi,$  是指有

$$
\mathbf {P} \Big (\lim _ {n \to \infty} \xi_ {n} = \xi \Big) = \mathbf {P} \Big (\omega \in \varOmega : \lim _ {n \to \infty} \xi_ {n} (\omega) = \xi (\omega) \Big) = 1.
$$

注意 $E := \{\lim_{n \to \infty} \xi_n = \xi\} \in \mathscr{F}$, 这可由下面的表示看出:

$$
E = \bigcap_ {k = 1} ^ {\infty} \bigcup_ {n = 1} ^ {\infty} \bigcap_ {i = n} ^ {\infty} \left\{| \xi_ {i} - \xi | <   1 / k \right\}. \tag {6.1.1}
$$

上面的等式可以用语言表述为: $\omega \in E$ 当且仅当对任何 $k \geqslant 1$, 存在 $n \geqslant 1$ 使当 $i \geqslant n$ 时有 $|\xi_i(\omega) - \xi(\omega)| < 1/k$ 成立.

定理6.1.1 收敛 $\xi_{n}\stackrel {\mathrm{a.s.}}{\rightarrow}\xi$ 成立的充要条件是对任意的 $\varepsilon >0$ 有

$$
\mathbf {P} \Big (\bigcap_ {n = 1} ^ {\infty} \bigcup_ {i = n} ^ {\infty} \left\{| \xi_ {i} - \xi | \geqslant \varepsilon \right\} \Big) = \lim _ {n \to \infty} \mathbf {P} \Big (\bigcup_ {i = n} ^ {\infty} \left\{| \xi_ {i} - \xi | \geqslant \varepsilon \right\} \Big) = 0. \tag {6.1.2}
$$

证明 由概率的上连续性知 (6.1.2) 式中的第一个等号总成立. 由 (6.1.1) 式有

$$
E ^ {c} = \bigcup_ {k = 1} ^ {\infty} \bigcap_ {n = 1} ^ {\infty} \bigcup_ {i = n} ^ {\infty} \left\{| \xi_ {i} - \xi | \geqslant 1 / k \right\} = \bigcup_ {k = 1} ^ {\infty} \bigcap_ {n = 1} ^ {\infty} A _ {k, n},
$$

其中

$$
A _ {k, n} = \bigcup_ {i = n} ^ {\infty} \left\{| \xi_ {i} - \xi | \geqslant 1 / k \right\} \in \mathcal {F}.
$$

所以  $\xi_{n}\stackrel{a.s.}{\rightarrow}\xi\Leftrightarrow\mathbf{P}(E)=1\Leftrightarrow\mathbf{P}(E^{c})=0\Leftrightarrow$

$$
\mathbf {P} \Big (\bigcap_ {n = 1} ^ {\infty} A _ {k, n} \Big) = 0, \quad k \geqslant 1.
$$

注意 $A_{k,n} \supseteq A_{k,n + 1}$, 由概率的上连续性知上式等价于对任意的 $k \geqslant 1$ 有

$$
\lim _ {n \to \infty} \mathbf {P} (A _ {k, n}) = \lim _ {n \to \infty} \mathbf {P} \Big (\bigcup_ {i = n} ^ {\infty} \left\{| \xi_ {i} - \xi | \geqslant 1 / k \right\} \Big) = 0,
$$

而这等价于 (6.1.2) 式对任意的 $\varepsilon > 0$ 成立.

定义 6.1.2 称序列  $\{\xi_{n}\}$  完全收敛到  $\xi$ ，并记作  $\xi_{n} \stackrel{c}{\rightarrow} \xi$ ，是指对任何  $\varepsilon > 0$  有

$$
\sum_ {n = 1} ^ {\infty} \mathbf {P} (| \xi_ {n} - \xi | \geqslant \varepsilon) <   \infty , \tag {6.1.3}
$$

定理 6.1.2 若  $\xi_{n}\stackrel{c}{\rightarrow}\xi,$  则  $\xi_{n}\stackrel{a.s.}{\rightarrow}\xi.$

证明 根据概率测度的次可加性, 对任何  $\varepsilon > 0$  有

$$
\mathrm{P} \Big (\bigcup_ {i = n} ^ {\infty} \left\{| \xi_ {i} - \xi | \geqslant \varepsilon \right\} \Big) \leqslant \sum_ {i = n} ^ {\infty} \mathrm{P} (| \xi_ {i} - \xi | \geqslant \varepsilon).
$$

若 $\xi_{n} \stackrel{\mathrm{c}}{\rightarrow} \xi$，则上式右边当 $n \to \infty$ 时趋于零。再根据定理6.1.1即知 $\xi_{n} \stackrel{\mathrm{a.s.}}{\rightarrow} \xi$。

我们可以将完全收敛性 (6.1.3) 理解为关于概率 $\mathbf{P}(|\xi_n - \xi| \geqslant \varepsilon)$ 当 $n \to \infty$ 时的衰减速度的一个条件, 它给出了随机变量列几乎必然收敛的自然的和便于验证的充分条件. 完全收敛性经常与下面的博雷尔-坎泰利 (Borel-Cantelli) 引理结合使用. 回忆记号

$$
\operatorname * {l i m s u p} _ {n \to \infty} A _ {n} = \bigcap_ {n = 1} ^ {\infty} \bigcup_ {i = n} ^ {\infty} A _ {i}.
$$

引理 6.1.3 (博雷尔-坎泰利引理) (1) 对于任意事件列  $\{A_{n}\}$  有

$$
\sum_ {n = 1} ^ {\infty} \mathbf {P} (A _ {n}) <   \infty \Rightarrow \mathbf {P} \Big (\limsup _ {n \to \infty} A _ {n} \Big) = 0.
$$

(2) 若 $\{A_{n}\}$ 为独立事件序列, 则

$$
\sum_ {n = 1} ^ {\infty} \mathbf {P} (A _ {n}) = \infty \Rightarrow \mathbf {P} \Big (\limsup _ {n \to \infty} A _ {n} \Big) = 1.
$$

证明 (1) 假设 $\sum_{n=1}^{\infty} \mathbf{P}(A_n) < \infty$. 记 $B_n = \bigcup_{i=n}^{\infty} A_i$, 则 $B_n \downarrow \limsup_{n} A_n$. 由概率的上连续性,

$$
\mathbf {P} \Big (\operatorname * {l i m s u p} _ {n \to \infty} A _ {n} \Big) = \lim _ {n \to \infty} \mathbf {P} (B _ {n}) \leqslant \lim _ {n \to \infty} \sum_ {i = n} ^ {\infty} \mathbf {P} (A _ {i}) = 0.
$$

(2) 设 $\{A_{n}\}$ 为独立事件序列, 且 $\sum_{n=1}^{\infty} \mathbf{P}(A_{n}) = \infty$. 由独立性有

$$
\mathbf {P} \Big (\bigcap_ {i = n} ^ {n + k} A _ {i} ^ {c} \Big) = \prod_ {i = n} ^ {n + k} [ 1 - \mathbf {P} (A _ {i}) ] = \exp \Big \{\sum_ {i = n} ^ {n + k} \ln [ 1 - \mathbf {P} (A _ {i}) ] \Big \}.
$$

令 $k\to \infty$ ，并应用上连续性得

$$
\mathbf {P} \Big (\bigcap_ {i = n} ^ {\infty} A _ {i} ^ {c} \Big) = \exp \Big \{\sum_ {i = n} ^ {\infty} \ln [ 1 - \mathbf {P} (A _ {i}) ] \Big \},
$$

其中 $\ln [1 - \mathbf{P}(A_i)]\leqslant -\mathbf{P}(A_i)$ .所以

$$
\begin{array}{l} \sum_ {i = n} ^ {\infty} \mathbf {P} (A _ {i}) = \infty \Rightarrow \sum_ {i = n} ^ {\infty} \ln [ 1 - \mathbf {P} (A _ {i}) ] = - \infty \\ \Rightarrow \mathbf {P} \Big (\bigcap_ {i = n} ^ {\infty} A _ {i} ^ {c} \Big) = 0 \\ \Rightarrow \mathbf {P} \Big (\bigcup_ {n = 1} ^ {\infty} \bigcap_ {i = n} ^ {\infty} A _ {i} ^ {c} \Big) = 0, \\ \end{array}
$$

进而

$$
\mathbf {P} \Big (\operatorname * {l i m s u p} _ {n \to \infty} A _ {n} \Big) = \mathbf {P} \Big (\bigcap_ {n = 1} ^ {\infty} \bigcup_ {i = n} ^ {\infty} A _ {i} \Big) = 1 - \mathbf {P} \Big (\bigcup_ {n = 1} ^ {\infty} \bigcap_ {i = n} ^ {\infty} A _ {i} ^ {c} \Big) = 1.
$$

故得欲证结论.

根据博雷尔-坎泰利引理, 若 $\{A_{n}\}$ 为独立事件序列, 则事件 $\limsup_{n\to \infty}A_n$ 发生的概率只可能是0或1. 这个现象称为0-1律.

例 6.1.1 设有  $\xi_{n} \stackrel{a.s.}{\rightarrow} \xi$  和  $\eta_{n} \stackrel{a.s.}{\rightarrow} \eta$ . 则对  $R^{2}$  上的任何连续函数 f 有  $f(\xi_{n}, \eta_{n}) \stackrel{a.s.}{\rightarrow} f(\xi, \eta)$ . 事实上, 根据假设有  $\mathbf{P}(\lim_{n \to \infty} \xi_{n} = \xi) = 1$  和  $\mathbf{P}(\lim_{n \to \infty} \eta_{n} = \eta) = 1$ . 因此

$$
\mathbf {P} \Big (\Big \{\lim _ {n \to \infty} \xi_ {n} = \xi \Big \} \cap \Big \{\lim _ {n \to \infty} \eta_ {n} = \eta \Big \} \Big) = 1.
$$

再注意

$$
\Big \{\lim _ {n \to \infty} \xi_ {n} = \xi \Big \} \cap \Big \{\lim _ {n \to \infty} \eta_ {n} = \eta \Big \} \subseteq \Big \{\lim _ {n \to \infty} f (\xi_ {n}, \eta_ {n}) = f (\xi , \eta) \Big \},
$$

故有

$$
\mathbf {P} \Big (\lim _ {n \to \infty} f (\xi_ {n}, \eta_ {n}) = f (\xi , \eta) \Big) = 1,
$$

即  $f(\xi_{n},\eta_{n}) \stackrel{\mathrm{a.s.}}{\rightarrow} f(\xi,\eta).$

## 6.1.2 依概率收敛

定义 6.1.3 称随机变量序列  $\{\xi_{n}\}$  依概率收敛于随机变量  $\xi$ ，并记作  $\xi_{n} \stackrel{P}{\rightarrow} \xi$ ，是指对任意的  $\varepsilon > 0$ ，当  $n \to \infty$  时有

$$
\mathbf {P} (| \xi_ {n} - \xi | \geqslant \varepsilon) = \mathbf {P} \big (\omega \in \Omega : | \xi_ {n} (\omega) - \xi (\omega) | \geqslant \varepsilon \big) \rightarrow 0.
$$

定理 6.1.4 若  $\xi_{n} \stackrel{a.s.}{\rightarrow} \xi$ ，则  $\xi_{n} \stackrel{p}{\rightarrow} \xi$ .

证明 只需注意 $\{|\xi_n - \xi| \geqslant \varepsilon\} \subseteq \bigcup_{i=n}^{\infty} \{|\xi_i - \xi| \geqslant \varepsilon\}$ 并应用定理6.1.1.

例 6.1.2 取  $\Omega=(0,1]$  和  $\mathcal{F}=(0,1]\cap\mathcal{B}$ ，再令 P 为  $(\Omega,\mathcal{F})$  上的勒贝格测度。则  $(\Omega,\mathcal{F},\mathbf{P})$  是概率空间。对于  $\omega\in\Omega$ ，令  $\eta_{11}(\omega)=1$ ，再令

$$
\eta_ {2 1} (\omega) = 1 _ {(0, 1 / 2 ]} (\omega), \quad \eta_ {2 2} (\omega) = 1 _ {(1 / 2, 1 ]} (\omega).
$$

一般地, 对整数 $k \geqslant 1$ 和 $1 \leqslant i \leqslant k$, 令

$$
\eta_ {k i} (\omega) = 1 _ {((i - 1) / k, i / k ]} (\omega), \quad \omega \in \Omega .
$$

这样, 我们得到可数个随机变量

$$
\begin{array}{l} \eta_ {1 1}, \\ \eta_ {2 1}, \quad \eta_ {2 2}, \\ \eta_ {3 1}, \quad \eta_ {3 2}, \quad \eta_ {3 3}, \\ \dots , \\ \eta_ {k 1}, \quad \eta_ {k 2}, \quad \eta_ {k 3}, \quad \dots , \quad \eta_ {k k}, \\ \dots , \end{array}
$$

显然, 对于 $0 < \varepsilon < 1$ 当 $k \to \infty$ 时有

$$
\mathbf {P} (| \eta_ {k i} | \geqslant \varepsilon) = \mathbf {P} (\eta_ {k i} = 1) = \frac {1}{k} \rightarrow 0.
$$

现将 $\{\eta_{ki}: k \geqslant 1, 1 \leqslant i \leqslant k\}$ 按字典式排序得到序列 $\{\xi_n : n \geqslant 1\}$. 由上式易见 $\xi_n \stackrel{\mathrm{P}}{\to} 0$. 另一方面, 对任意的 $\omega \in (0,1]$ 和任意的 $k \geqslant 1$, 必然存在 $1 \leqslant i \leqslant k$ 满足 $\omega \in ((i-1)/k, i/k]$, 故 $\eta_{ki}(\omega) = 1$. 因此 $\xi_n(\omega) \to 0$ 不成立. 这说明 $\xi_n \stackrel{\mathrm{a.s.}}{\to} \xi$ 不成立.

定理 6.1.5 若  $\xi_{n}\stackrel{p}{\rightarrow}\xi$ ，则存在  $\{\xi_{n}\}$  的子列  $\{\xi_{n_{k}}\}$  使当  $k\to\infty$  时有  $\xi_{n_{k}}\stackrel{a.s.}{\rightarrow}\xi$ .

证明 根据假设, 对任意的整数 $k \geqslant 1$, 存在整数 $n_k \geqslant 1$ 使得

$$
\mathbf {P} (| \xi_ {n _ {k}} - \xi | \geqslant 1 / k) \leqslant 1 / 2 ^ {k}.
$$

对任意的 $\varepsilon > 0$, 取整数 $N \geqslant 1 / \varepsilon$, 有

$$
\sum_ {k = 1} ^ {\infty} \mathbf {P} (| \xi_ {n _ {k}} - \xi | \geqslant \varepsilon) = \sum_ {k = 1} ^ {N - 1} \mathbf {P} (| \xi_ {n _ {k}} - \xi | \geqslant \varepsilon) + \sum_ {k = N} ^ {\infty} \mathbf {P} (| \xi_ {n _ {k}} - \xi | \geqslant \varepsilon)
$$