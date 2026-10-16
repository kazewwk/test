定理 4.1.13 设 G 是跳跃点集为  $E := \{x_{i} : i = 1, 2, \cdots\}$  的离散型分布函数，而 f 在 R 上局部有界且在 E 的每点处连续。则有

$$
\int_ {- \infty} ^ {\infty} f (x) \mathrm{d} G (x) = \sum_ {i = 1} ^ {\infty} f (x _ {i}) [ G (x _ {i}) - G (x _ {i} -) ]. \tag {4.1.15}
$$

定理 4.1.12 和定理 4.1.13 给出了两种典型的情况下, 全空间上斯蒂尔切斯积分的常用的计算方法. 定理中的等式的含义为: 只要等号两端有一边的积分存在则另一边的积分也存在且等式成立.

设分布函数 $F$ 和 $G$ 满足关系 (4.1.12) 式, 而 $\nu$ 和 $\mu$ 分别是 $F$ 和 $G$ 对应的 $(\mathbb{R}, \mathcal{B})$ 上的局部有限测度. 在这种情况下, 我们称 $F$ 或 $\nu$ 相对于 $G$ 或 $\mu$ 绝对连续且有密度函数 $g$, 简记作

$$
\mathrm{d} F (x) = g (x) \mathrm{d} G (x) \text {或} \nu (\mathrm{d} x) = g (x) \mu (\mathrm{d} x).
$$

这样, 此前定义的绝对连续型分布函数的概念就相当于这里 $G(x) \equiv x$ 的特例.

参考数学分析中的黎曼瑕积分的定义, 也可以讨论 $f$ 或 $G$ 在一个或多个点附近无界时的 $G$ 积分. 例如, 在定义4.1.2中将 $a \to -\infty$ 换为 $a \to 0+$ 就可以给出 $f$ 或 $G$ 在0右侧附近无界时在 $(0, \infty)$ 上的积分的定义.

## 4.1.4 多维空间上的积分

前面的讨论可以类似地拓展到多维空间的情况. 设 $G$ 是 $(\mathbb{R}^d, \mathcal{B}^d)$ 上的某个局部有限测度 $\mu$ 的分布函数, 即存在欧氏可测空间 $(\mathbb{R}^d, \mathcal{B}^d)$ 上的局部有限测度 $\mu$ 满足

$$
\mu (a, b ] = G (b) - G (a), \quad a \leqslant b \in \mathbb {R} ^ {d}. \tag {4.1.16}
$$

定义 4.1.3 令 f 为区间  $[a,b]=[a_{1},b_{1}]\times[a_{2},b_{2}]\times\cdots\times[a_{d},b_{d}]\subseteq\mathbb{R}^{d}$  上的函数. 对整数  $k\geqslant1$  和  $i=1,2,\cdots,d$ ，取区间  $[a_{i},b_{i}]$  的分割点  $a_{i}=x_{k,i,0}<x_{k,i,1}<\cdots<x_{k,i,n_{i,k}}=b_{i}$  满足

$$
\delta_ {k} := \max _ {1 \leqslant i \leqslant d} \max _ {1 \leqslant r \leqslant n _ {i, k}} (x _ {k, i, r} - x _ {k, i, r - 1}) \to 0, \quad k \to \infty ,
$$

并取 $t_{k,i,r}\in [x_{k,i,r - 1},x_{k,i,r}]$ .令

$$
\sigma_ {k} (f, G; a, b) = \sum_ {r _ {1} = 1} ^ {n _ {1, k}} \dots \sum_ {r _ {d} = 1} ^ {n _ {d, k}} f (t _ {k, 1, r _ {1}}, t _ {k, 2, r _ {2}}, \dots , t _ {k, d, r _ {d}}) \mu (\varDelta_ {k, r _ {1}, r _ {2}, \dots , r _ {d}}),
$$

其中

$$
\Delta_ {k, r _ {1}, r _ {2}, \dots , r _ {d}} = (x _ {k, 1, r _ {1} - 1}, x _ {k, 1, r _ {1}} ] \times (x _ {k, 2, r _ {2} - 1}, x _ {k, 2, r _ {2}} ] \times \dots \times (x _ {k, d, r _ {d} - 1}, x _ {k, d, r _ {d}} ].
$$

若存在有限的极限 $\lim_{k\to \infty}\sigma_k(f,G;a,b)$ 且该极限与 $\{x_{k,i,r}\}$ 和 $\{t_{k,i,r}\}$ 的具体选取无关，则称 $f$ 在 $[a,b]$ 上相对于 $G$ 斯蒂尔切斯可积，简称 $G$ 可积.称该极限为 $f$ 在 $[a,b]$ 上相对于 $G$ 的斯蒂尔切斯积分，简称 $G$ 积分，并记作

$$
\int_ {a _ {1}} ^ {b _ {1}} \dots \int_ {a _ {d}} ^ {b _ {d}} f (x _ {1}, x _ {2}, \dots , x _ {d}) \mathrm{d} G (x _ {1}, x _ {2}, \dots , x _ {d}) = \lim _ {k \to \infty} \sigma_ {k} (f, G; a, b).
$$

定义 4.1.4 设  $R^{d}$  上的函数 f 在每个有界区间  $[a,b]=[a_{1},b_{1}]\times[a_{2},b_{2}]\times\cdots\times[a_{d},b_{d}]\subseteq\mathbb{R}^{d}$  上 G 可积. 如果极限

$$
\begin{array}{l} \int_ {- \infty} ^ {\infty} \dots \int_ {- \infty} ^ {\infty} f ^ {\pm} (x _ {1}, x _ {2}, \dots , x _ {d}) \mathrm{d} G (x _ {1}, x _ {2}, \dots , x _ {d}) \\ \begin{array}{r l} & {:= \lim _ {a _ {1}, \dots , a _ {d} \to - \infty} \lim _ {b _ {1}, \dots , b _ {d} \to \infty} \int_ {a _ {1}} ^ {b _ {1}} \dots \int_ {a _ {d}} ^ {b _ {d}} f ^ {\pm} (x _ {1}, x _ {2}, \dots , x _ {d}) \mathrm{d} G (x _ {1}, x _ {2}, \dots , x _ {d})} \end{array} \tag {4.1.17} \\ \end{array}
$$

中至少有一个有限, 我们就称 $f$ 在 $\mathbb{R}^d$ 上相对于 $G$ 的斯蒂尔切斯积分存在, 并将该积分定义为

$$
\begin{array}{l} \int_ {- \infty} ^ {\infty} \dots \int_ {- \infty} ^ {\infty} f (x _ {1}, x _ {2}, \dots , x _ {d}) \mathrm{d} G (x _ {1}, x _ {2}, \dots , x _ {d}) \\ = \int_ {- \infty} ^ {\infty} \dots \int_ {- \infty} ^ {\infty} f ^ {+} (x _ {1}, x _ {2}, \dots , x _ {d}) \mathrm{d} G (x _ {1}, x _ {2}, \dots , x _ {d}) - \\ \int_ {- \infty} ^ {\infty} \dots \int_ {- \infty} ^ {\infty} f ^ {-} (x _ {1}, x _ {2}, \dots , x _ {d}) \mathrm{d} G (x _ {1}, x _ {2}, \dots , x _ {d}). \\ \end{array}
$$

上式也简称为 $f$ 在 $\mathbb{R}^d$ 上的 $G$ 积分. 如果 (4.1.17) 式中的两个极限都有限, 就称 $f$ 在 $\mathbb{R}^d$ 上相对于 $G$ 斯蒂尔切斯可积, 简称 $G$ 可积.

特别地, 当 G 在  $R^{d}$  上有界时, 通过 (3.1.7) 式可以定义 G 的边缘分布函数  $G_{1}, G_{2}, \cdots, G_{d}$ . 此时, 若函数 f 只依赖于  $(x_{1}, x_{2}, \cdots, x_{d})$  的某个分量  $x_{i}$ , 则有

$$
\int_ {- \infty} ^ {\infty} \dots \int_ {- \infty} ^ {\infty} f (x _ {i}) \mathrm{d} G (x _ {1}, x _ {2}, \dots , x _ {d}) = \int_ {- \infty} ^ {\infty} f (x) \mathrm{d} G _ {i} (x).
$$

更一般地, 若函数 $f$ 只依赖于 $(x_{1}, x_{2}, \cdots, x_{d})$ 的某个子向量 $(x_{i_{1}}, x_{i_{2}}, \cdots, x_{i_{r}})$, 则它关于 $G$ 的积分可以转化为 $r$ 维空间上的斯蒂尔切斯积分.

前面证明的一维空间上的斯蒂尔切斯积分的性质都可以推广到多维空间.

## 4.1.5 关于积分的说明

设 $d$ 维欧氏可测空间 $(\mathbb{R}^d, \mathcal{B}^d)$ 上的局部有限测度 $\mu$ 有分布函数 $G$. 我们也称 $\mathbb{R}^d$ 上的函数 $f(x) = f(x_1, x_2, \dots, x_d)$ 关于 $G$ 的斯蒂尔切斯积分为它关于 $\mu$ 的斯蒂尔切斯

积分, 简称积分, 并将该积分写为

$$
\int_ {\mathbb {R} ^ {d}} f (x) \mathrm{d} G (x) = \int_ {\mathbb {R} ^ {d}} f (x) \mu (\mathrm{d} x).
$$

对于 $E \in \mathcal{B}^d$ 写

$$
\int_ {E} f (x) \mu (\mathrm{d} x) = \int_ {\mathbb {R} ^ {d}} f (x) 1 _ {E} (x) \mu (\mathrm{d} x).
$$

注意, 在此约定之下对 $a \leqslant b \in \mathbb{R}^d$ 有

$$
\int_ {a} ^ {b} f (x) \mathrm{d} G (x) = \int_ {(a, b ]} f (x) \mathrm{d} G (x) = \int_ {(a, b ]} f (x) \mu (\mathrm{d} x).
$$

设 $\mu_{1}$ 和 $\mu_{2}$ 是 $(\mathbb{R}^{d},\mathcal{B}^{d})$ 上的两个局部有限测度. 对于 $B\in \mathcal{B}^d$ 令 $\eta (B) = \mu_1(B) -$ $\mu_{2}(B)$ .称 $\eta$ 为符号测度，它是两个测度之差. 给定 $\mathbb{R}^d$ 上的函数 $f$ ，定义其关于 $\eta$ 的积分为

$$
\int_ {\mathbb {R} ^ {d}} f (x) \eta (\mathrm{d} x) = \int_ {\mathbb {R} ^ {d}} f (x) \mu_ {1} (\mathrm{d} x) - \int_ {\mathbb {R} ^ {d}} f (x) \mu_ {2} (\mathrm{d} x),
$$

这里要求等号右端的表达式有意义.分别用 $F_{1}, F_{2}$ 表示 $\mu_{1}, \mu_{2}$ 的分布函数.则函数 $F := F_{1} - F_{2}$ 作为两个单调函数之差在任何有界区间上有有界变差.我们也可以将上式右端解释为 $f$ 相对于 $F$ 的积分.关于有界变差函数的斯蒂尔切斯积分的更多讨论，可以参见[6].

斯蒂尔切斯积分与黎曼积分的定义方式非常相似, 因此对初学者比较容易理解. 但这种积分有个很大的缺点, 就是对于被积函数的要求太强, 以至于很多自然的函数在斯蒂尔切斯积分意义下不可积分. 例如, 在定理 4.1.7 和定理 4.1.13 中, 关于被积函数在分布函数的跳跃点的连续性就非常不自然.

本册书附录中介绍了函数对 $\sigma$ 有限测度的积分, 它大为扩展了可积分的函数类. 特别地, 在抽象测度积分的意义下, 任何有界可测函数相对于有限测度都是可积的. 在定理4.1.13的情况下, 可测函数 $f$ 相对于 $G$ 决定的局部有限测度的积分仍由(4.1.15)式给出. 由于这个原因, 后面在遇到 $\mathbb{R}$ 上的函数关于离散型分布函数的积分时, 我们并不严格要求被积函数的连续性, 而直接将积分理解为(4.1.15)式右端的级数. 对于多维空间的情况也做类似的理解.

## 练习题

1. 设 $G$ 是 $\mathbb{R}$ 上的连续分布函数. 证明: 若函数 $f$ 在有界区间 $[a, b]$ 上每点处有有限的左、右极限, 且至多在有限个点不连续, 则它在 $[a, b]$ 上 $G$ 可积.

2. 设 $G$ 是 $\mathbb{R}$ 上的分布函数. 证明: 若函数 $f$ 在有界区间 $[a, b]$ 上 $G$ 可积, 则它在任何子区间 $[c, d] \subseteq [a, b]$ 上 $G$ 可积.

3. 设 $G$ 是 $\mathbb{R}$ 上的分布函数, 而函数 $f$ 在 $[a, b]$ 上连续可微. 证明分部积分公式:

$$
\int_ {a} ^ {b} f (x) \mathrm{d} G (x) = f (x) G (x) \big | _ {a} ^ {b} - \int_ {a} ^ {b} f ^ {\prime} (x) G (x) \mathrm{d} x.
$$

4. 设 $G$ 是 $\mathbb{R}$ 上的分布函数. 证明:

(1) 若函数 $f_{1}, f_{2}$ 均在有界区间 $[a, b] \subseteq \mathbb{R}$ 上 $G$ 可积, 则 $f_{1} + f_{2}$ 在 $[a, b]$ 上 $G$ 可积且

$$
\int_ {a} ^ {b} [ f _ {1} (x) + f _ {2} (x) ] \mathrm{d} G (x) = \int_ {a} ^ {b} f _ {1} (x) \mathrm{d} G (x) + \int_ {a} ^ {b} f _ {2} (x) \mathrm{d} G (x).
$$

(2) 若函数 $f_{1}, f_{2}$ 均在 $\mathbb{R}$ 上 $G$ 可积, 则 $f_{1} + f_{2}$ 在 $\mathbb{R}$ 上 $G$ 可积且

$$
\int_ {- \infty} ^ {\infty} [ f _ {1} (x) + f _ {2} (x) ] \mathrm{d} G (x) = \int_ {- \infty} ^ {\infty} f _ {1} (x) \mathrm{d} G (x) + \int_ {- \infty} ^ {\infty} f _ {2} (x) \mathrm{d} G (x).
$$

## 4.2 随机变量的数学期望

数学期望是随机变量的取值对相应的概率的加权平均, 可以用相对于分布函数的斯蒂尔切斯积分表示. 特别地, 离散型随机变量的数学期望进一步可以转化为级数的求和, 而绝对连续型随机变量的数学期望的计算可用黎曼积分计算.

## 4.2.1 定义和基本性质

定义 4.2.1 设  $\xi$  是定义于概率空间  $(\Omega, \mathcal{F}, \mathbf{P})$  的随机变量, 有分布  $\mu_{\xi}$  和分布函数  $F_{\xi}$ . 如果函数  $f_{1}(x) \equiv x$  在 R 上关于分布函数  $F_{\xi}$  的斯蒂尔切斯积分存在, 就称该积分为  $\xi$  的数学期望或均值, 并记作  $E\xi$  或  $\mathbf{E}(\xi)$ , 即

$$
\mathbf {E} \xi = \int_ {- \infty} ^ {\infty} x \mathrm{d} F _ {\xi} (x). \tag {4.2.1}
$$

若函数 $f_{1}$ 在 $\mathbb{R}$ 上 $F_{\xi}$ 可积, 则称随机变量 $\xi$ 是可积的.

根据定理4.1.12和定理4.1.13有

命题 4.2.1 设  $\xi$  为绝对连续型随机变量且有分布密度 p. 若  $\xi$  的数学期望存在, 则

$$
\mathbf {E} \xi = \int_ {- \infty} ^ {\infty} x p (x) \mathrm{d} x.
$$

命题 4.2.2 设  $\xi$  为取值于可数集  $E := \{x_{1}, x_{2}, \cdots\} \subseteq R$  的离散型随机变量且有分布密度 p. 若  $\xi$  的数学期望存在, 则

$$
\mathbf {E} \xi = \sum_ {i = 1} ^ {\infty} x _ {i} p (x _ {i}).
$$

数学期望是随机变量的典型的数字特征, 它反映了该随机变量的整体性质.

例 4.2.1 根据医学数据分析, 某种流行病的患病率为 q (0 < q < 1). 现把 k (k ≥ 1) 个人分为一组, 将其血样混合后进行化验. 若结果为阴性, 则通过检验; 若结果为阳性, 则这 k 个人需要再分别化验一次. 记这 k 个人的化验次数为  $\xi$ , 则

$$
\mathbf {P} (\xi = 1) = (1 - q) ^ {k}, \quad \mathbf {P} (\xi = k + 1) = 1 - (1 - q) ^ {k}.
$$

所以

$$
\mathbf {E} \xi = (1 - q) ^ {k} + (k + 1) [ 1 - (1 - q) ^ {k} ] = k + 1 - k (1 - q) ^ {k}.
$$

通常 $q$ 的值很小, 此时可取适当的 $k$ 使 $k(1 - q)^k > 1$, 故 $\mathbf{E}\xi < k$. 也就是说, 用这样的方式可以减少化验次数, 从而降低成本.

若两个随机变量 $\xi$ 和 $\eta$ 满足 $\xi \stackrel{\mathrm{a.s.}}{=} \eta$, 则它们有相同的分布函数, 根据 (4.2.1) 式有 $\mathbf{E}\xi = \mathbf{E}\eta$.

定理4.2.3 设 $\xi$ 为非负随机变量. 则 $\mathbf{E}\xi \geqslant 0$, 且 $\mathbf{E}\xi = 0$ 当且仅当 $\xi = 0$ (a.s.).

证明 因 $\xi$ 是非负随机变量, 当 $x < 0$ 有 $F_{\xi}(x) = 0$. 根据斯蒂尔切斯积分的定义和性质易知

$$
\mathbf {E} \xi = \int_ {0} ^ {\infty} x \mathrm{d} F _ {\xi} (x) \geqslant 0.
$$

若 $\xi = 0$ (a.s.), 则 $F_{\xi}(x) = 1_{\{x \geqslant 0\}}$, 故由命题4.2.2有 $\mathbf{E}\xi = 0$. 反之, 若 $\mathbf{E}\xi = 0$, 则对任意的 $a > 0$ 有

$$
0 = \int_ {0} ^ {\infty} x \mathrm{d} F _ {\xi} (x) \geqslant \int_ {a} ^ {\infty} x \mathrm{d} F _ {\xi} (x) \geqslant a \int_ {a} ^ {\infty} \mathrm{d} F _ {\xi} (x) = a [ 1 - F _ {\xi} (a) ],
$$

故 $F_{\xi}(a) = 1$ ，再由右连续性得 $F_{\xi}(0) = 1$ ，从而 $\xi = 0$ (a.s.).

定理4.2.4 给定随机变量 $\xi$ ，令 $\xi^{+} = 0\lor \xi$ 和 $\xi^{-} = 0\lor (-\xi)$ .则有

$$
\mathbf {E} \xi^ {+} = \int_ {0} ^ {\infty} x \mathrm{d} F _ {\xi} (x) = \int_ {0} ^ {\infty} [ 1 - F _ {\xi} (t) ] \mathrm{d} t
$$

和

$$
\mathbf {E} \xi^ {-} = - \int_ {- \infty} ^ {0} x \mathrm{d} F _ {\xi} (x) = \int_ {- \infty} ^ {0} F _ {\xi} (t) \mathrm{d} t.
$$

证明 由于 $\xi^{+},\xi^{-}$ 都是非负随机变量, 对于 $x < 0$ 有 $F_{\xi^{+}}(x) = F_{\xi^{-}}(x) = 0$. 对任意的 $x \geqslant 0$, 显然有 $F_{\xi^{+}}(x) = F_{\xi}(x)$. 根据数学期望的定义, 并交换积分次序 (承认这是允许的) 得

$$
\begin{array}{l} \mathbf {E} \xi^ {+} = \int_ {0} ^ {\infty} x \mathrm{d} F _ {\xi} (x) = \int_ {0} ^ {\infty} \mathrm{d} F _ {\xi} (x) \int_ {0} ^ {x} \mathrm{d} t \\ = \int_ {0} ^ {\infty} \mathrm{d} t \int_ {t} ^ {\infty} \mathrm{d} F _ {\xi} (x) = \int_ {0} ^ {\infty} [ 1 - F _ {\xi} (t) ] \mathrm{d} t. \\ \end{array}
$$

所以定理中关于 $\mathbf{E}\xi^{+}$ 的表达式成立. 此外, 对 $x \geqslant 0$ 有

$$
F _ {\xi^ {-}} (x) = \mathbf {P} (\xi^ {-} \leqslant x) = \mathbf {P} (\xi \geqslant - x) = 1 - \mathbf {P} (\xi <   - x) = 1 - F _ {\xi} (- x -),
$$

注意这里 $x \mapsto -F_{\xi}(-x-)$ 是 $[0, \infty)$ 上的右连续不降函数. 在该函数的连续点集中取不降数列 $b_n \to \infty$. 根据上式有

$$
\begin{array}{l} \mathbf {E} \xi^ {-} = - \int_ {0} ^ {\infty} x \mathrm{d} F _ {\xi} (- x -) = - \lim _ {n \to \infty} \int_ {0} ^ {b _ {n}} x \mathrm{d} F _ {\xi} (- x -) \\ = - \lim _ {n \to \infty} \int_ {- b _ {n}} ^ {0} x \mathrm{d} F _ {\xi} (x) = - \int_ {- \infty} ^ {0} x \mathrm{d} F _ {\xi} (x) \\ = \int_ {- \infty} ^ {0} \mathrm{d} F _ {\xi} (x) \int_ {x} ^ {0} \mathrm{d} t = \int_ {- \infty} ^ {0} \mathrm{d} t \int_ {- \infty} ^ {t} \mathrm{d} F _ {\xi} (x) \\ = \int_ {- \infty} ^ {0} F _ {\xi} (t) \mathrm{d} t. \\ \end{array}
$$

这说明定理中关于  $E\xi^{-}$  的表达式成立.

由 (4.2.10) 和定理 4.2.4 易得

定理4.2.5 若随机变量 $\xi$ 的数学期望存在, 则有

$$
\mathbf {E} \xi = \int_ {0} ^ {\infty} \mathbf {P} (\xi > t) \mathrm{d} t - \int_ {- \infty} ^ {0} \mathbf {P} (\xi \leqslant t) \mathrm{d} t
$$

和

$$
\mathbf {E} | \xi | = \int_ {0} ^ {\infty} \mathbf {P} (\xi > t) \mathrm{d} t + \int_ {- \infty} ^ {0} \mathbf {P} (\xi \leqslant t) \mathrm{d} t.
$$

例 4.2.2 设  $\xi$  为取值于数集  $\{0,1,2,\cdots\}$  的离散型随机变量. 则

$$
\begin{array}{l} \mathbf {E} \xi = \int_ {0} ^ {\infty} \mathbf {P} (\xi > t) \mathrm{d} t = \sum_ {n = 1} ^ {\infty} \int_ {n - 1} ^ {n} \mathbf {P} (\xi > t) \mathrm{d} t \\ = \sum_ {n = 1} ^ {\infty} \int_ {n - 1} ^ {n} \mathbf {P} (\xi \geqslant n) \mathrm{d} t = \sum_ {n = 1} ^ {\infty} \mathbf {P} (\xi \geqslant n). \\ \end{array}
$$

## 4.2.2 随机变量函数的期望

假设随机变量 $\xi$ 有分布函数 $F_{\xi}$. 我们之前讨论过如何对可测函数 $f$ 求出随机变量 $f(\xi)$ 的分布函数 $F_{f(\xi)}$. 按照数学期望的定义有

$$
\mathbf {E} f (\xi) = \int_ {- \infty} ^ {\infty} x \mathrm{d} F _ {f (\xi)} (x).
$$

因此, 可以先求出 $f(\xi)$ 的分布, 再根据上式计算其数学期望 $\mathbf{E}f(\xi)$. 事实上, 我们也可以从 $\xi$ 的分布出发直接计算 $\mathbf{E}f(\xi)$.

命题 4.2.6 设  $\xi$  为取值于可数集  $E := \{x_{1}, x_{2}, \cdots\} \subseteq R$  的离散型随机变量，且有分布密度 p。再设 f 为 E 上的函数。若随机变量  $f(\xi)$  的数学期望存在，则有

$$
\mathbf {E} f (\xi) = \sum_ {i = 1} ^ {\infty} f (x _ {i}) p (x _ {i}).
$$

证明 令 $\{z_k : k = 1,2,\cdots\}$ 是去除数列 $\{f(x_i) : i = 1,2,\cdots\}$ 中多余的重复元素所得的集合. 则 $\zeta := f(\xi)$ 是取值于 $\{z_k : k = 1,2,\cdots\}$ 的离散型随机变量, 且其分布密度 $q$ 由 (3.3.2) 式给出. 再由命题 4.2.2 即知欲证结论成立. □

命题 4.2.6 中的结论可以推广到一般分布的形式. 为此注意, 根据定理 4.1.9, 对任意的  $a \leqslant b \in R$  有

$$
\int_ {- \infty} ^ {\infty} 1 _ {(a, b ]} (x) \mathrm{d} F _ {\xi} (x) = F _ {\xi} (b) - F _ {\xi} (a) = \mathbf {P} (a <   \xi \leqslant b).
$$

事实上, 对于相当一般的集合 $B \in \mathcal{B}$ 可以证明

$$
\int_ {- \infty} ^ {\infty} 1 _ {B} (x) \mathrm{d} F _ {\xi} (x) = \mathbf {P} (\xi \in B) = \mu_ {\xi} (B). \tag {4.2.2}
$$

定理4.2.7 设随机变量 $\xi$ 有分布函数 $F_{\xi}$, 而 $f$ 为 $\mathbb{R}$ 上的可测函数. 则随机变量 $f(\xi)$ 的数学期望存在当且仅当 $f$ 的 $F_{\xi}$ 积分存在, 且此时

$$
\mathbf {E} f (\xi) = \int_ {- \infty} ^ {\infty} f (x) \mathrm{d} F _ {\xi} (x). \tag {4.2.3}
$$

证明 此证明假定 (4.2.2) 式对于形如 $\{x \in \mathbb{R} : f(x) > t\}$ 和 $\{x \in \mathbb{R} : f(x) \leqslant t\}$ 的集合成立. 根据定理 4.2.5 有

$$
\begin{array}{l} \mathbf {E} f (\xi) = \int_ {0} ^ {\infty} \mathbf {P} (f (\xi) > t) \mathrm{d} t - \int_ {- \infty} ^ {0} \mathbf {P} (f (\xi) \leqslant t) \mathrm{d} t \\ = \int_ {0} ^ {\infty} \mathrm{d} t \int_ {- \infty} ^ {\infty} 1 _ {\{f (x) > t \}} \mathrm{d} F _ {\xi} (x) - \int_ {- \infty} ^ {0} \mathrm{d} t \int_ {- \infty} ^ {\infty} 1 _ {\{f (x) \leqslant t \}} \mathrm{d} F _ {\xi} (x) \\ \end{array}
$$

$$
\begin{array}{l} = \int_ {- \infty} ^ {\infty} \mathrm{d} F _ {\xi} (x) \int_ {0} ^ {\infty} 1 _ {\{f (x) > t \}} \mathrm{d} t - \int_ {- \infty} ^ {\infty} \mathrm{d} F _ {\xi} (x) \int_ {- \infty} ^ {0} 1 _ {\{f (x) \leqslant t \}} \mathrm{d} t \\ = \int_ {- \infty} ^ {\infty} f ^ {+} (x) \mathrm{d} F _ {\xi} (x) - \int_ {- \infty} ^ {\infty} f ^ {-} (x) \mathrm{d} F _ {\xi} (x). \\ \end{array}
$$

这里假定上面的积分换序是允许的. 因此定理结论成立.

![](images/page_119_image_4.jpg)

基于上面的定理, 并利用关于斯蒂尔切斯积分的结果可得

命题 4.2.8 设  $\xi$  为绝对连续型随机变量且有分布密度 p. 再设 f 为 R 上的可测函数. 若随机变量  $f(\xi)$  的数学期望存在, 则有

$$
\mathbf {E} f (\xi) = \int_ {- \infty} ^ {\infty} f (x) p (x) \mathrm{d} x.
$$

## 4.2.3 随机向量函数的期望

前面小节中的定理可以推广到随机向量的函数的情况. 为了表述上的方便, 这里只给出若干结果的二维形式.

定理4.2.9 设二维随机向量 $(\xi, \eta)$ 有联合分布函数 $F$，而 $f$ 为 $\mathbb{R}^2$ 上的可测函数。则随机变量 $f(\xi, \eta)$ 的数学期望存在当且仅当 $f$ 的 $F$ 积分存在，且此时

$$
\mathbf {E} f (\xi , \eta) = \int_ {- \infty} ^ {\infty} \int_ {- \infty} ^ {\infty} f (x, y) \mathrm{d} F (x, y). \tag {4.2.4}
$$

推论 4.2.10 设  $\alpha, \beta$  为常数而  $\xi, \eta$  为可积随机变量. 则  $\alpha\xi + \beta\eta$  为可积随机变量且

$$
\mathbf {E} (\alpha \xi + \beta \eta) = \alpha \mathbf {E} \xi + \beta \mathbf {E} \eta .
$$

推论 4.2.11 若  $\xi, \eta$  为可积随机变量且  $\xi \leqslant \eta$  (a.s.), 则  $E\xi \leqslant E\eta$ .

证明 在假定条件下有 $\eta -\xi \geqslant 0$ (a.s.). 再由定理4.2.3和推论4.2.10知 $\mathbf{E}\eta -\mathbf{E}\xi = \mathbf{E}(\eta -\xi)\geqslant 0.$

定理4.2.12 设 $\xi, \eta$ 为可积随机变量. 则 $\xi \leqslant \eta$ (a.s.) 当且仅当对任何 $A \in \mathcal{F}$ 都有 $\mathbf{E}(1_A\xi) \leqslant \mathbf{E}(1_A\eta)$.

证明 若 $\xi \leqslant \eta$ (a.s.), 则对 $A \in \mathcal{F}$ 显然有 $1_A\xi \leqslant 1_A\eta$ (a.s.), 由推论4.2.11有 $\mathbf{E}(1_A\xi) \leqslant \mathbf{E}(1_A\eta)$. 反之, 假设对任何 $A \in \mathcal{F}$ 都有 $\mathbf{E}(1_A\xi) \leqslant \mathbf{E}(1_A\eta)$. 取 $A = \{\xi - \eta > 0\}$ 得 $\mathbf{E}[1_A(\xi - \eta)] = \mathbf{E}(1_A\xi) - \mathbf{E}(1_A\eta) \leqslant 0$. 另一方面, 因 $1_A(\xi - \eta) \geqslant 0$, 必有 $\mathbf{E}[1_A(\xi - \eta)] = 0$, 再由定理4.2.3有 $1_A(\xi - \eta) = 0$ (a.s.). 因此 $\mathbf{P}(A) = 0$, 即 $\mathbf{P}(\xi \leqslant \eta) = 1$.

推论4.2.13 设 $\xi, \eta$ 为可积随机变量. 则 $\xi = \eta$ (a.s.) 当且仅当对任何 $A \in \mathcal{F}$ 都有 $\mathbf{E}(1_A\xi) = \mathbf{E}(1_A\eta)$.

命题 4.2.14 设  $(\xi,\eta)$  为取值于可数集  $E:=\{(x_{i},y_{j}):i,j=1,2,\cdots\}$  的二维离散型随机向量且有联合分布密度 p. 再设 f 为 E 上的函数. 若随机变量  $f(\xi,\eta)$  的数学期望存在, 则有

$$
\mathbf {E} f (\xi , \eta) = \sum_ {i = 1} ^ {\infty} \sum_ {j = 1} ^ {\infty} f (x _ {i}, y _ {j}) p (x _ {i}, y _ {j}).
$$

命题 4.2.15 设  $(\xi,\eta)$  为绝对连续型二维随机向量且有联合分布密度 p. 再设 f 为  $R^{2}$  上的函数. 若随机变量  $f(\xi,\eta)$  的数学期望存在, 则有

$$
\mathbf {E} f (\xi , \eta) = \int_ {- \infty} ^ {\infty} \int_ {- \infty} ^ {\infty} f (x, y) p (x, y) \mathrm{d} x \mathrm{d} y.
$$

下面是关于两个独立随机变量积的数学期望的一个常用的结果.

定理 4.2.16 若可积随机变量  $\xi$  和  $\eta$  相互独立, 则有  $\mathbf{E}(\xi\eta)=\mathbf{E}\xi\mathbf{E}\eta$ .

证明 因为 $\xi$ 和 $\eta$ 相互独立, 随机向量 $(\xi, \eta)$ 的联合分布函数 $F$ 为两个边缘分布函数之积, 即 $F(x, y) = F_{\xi}(x)F_{\eta}(y)$. 考虑有界区间 $[a, b] \subseteq \mathbb{R}^2$. 对于 $k \geqslant 1$ 令 $\{x_{k,i}\}$ 和 $\{t_{k,r,i}\}$ 如定义4.1.3给出. 分别用 $\mu$ 和 $\mu_{\xi}, \mu_{\eta}$ 表示 $(\xi, \eta)$ 的联合分布和两个边缘分布. 令

$$
\sigma_ {k} (a, b) = \sum_ {i = 1} ^ {m _ {k}} \sum_ {j = 1} ^ {m _ {k}} t _ {k, 1, i} t _ {k, 2, j} \mu \big ((x _ {k, 1, i - 1}, x _ {k, 1, i} ] \times (x _ {k, 2, j - 1}, x _ {k, 2, j} ] \big).
$$

由定理3.2.2知

$$
\mu \big ((x _ {k, 1, i - 1}, x _ {k, 1, i} ] \times (x _ {k, 2, j - 1}, x _ {k, 2, j} ] \big) = \mu_ {\xi} \big ((x _ {k, 1, i - 1}, x _ {k, 1, i} ] \big) \mu_ {\eta} \big ((x _ {k, 2, j - 1}, x _ {k, 2, j} ] \big).
$$

因此

$$
\sigma_ {k} (a, b) = \sum_ {i = 1} ^ {m _ {k}} t _ {k, 1, i} \mu_ {\xi} \big ((x _ {k, 1, i - 1}, x _ {k, 1, i} ] \big) \sum_ {j = 1} ^ {m _ {k}} t _ {k, 2, j} \mu_ {\eta} \big ((x _ {k, 2, j - 1}, x _ {k, 2, j} ] \big).
$$

令 $k\to \infty$ 得

$$
\int_ {a _ {1}} ^ {b _ {1}} \int_ {a _ {2}} ^ {b _ {2}} x y \mathrm{d} F (x, y) = \int_ {a _ {1}} ^ {b _ {1}} x \mathrm{d} F _ {\xi} (x) \int_ {a _ {2}} ^ {b _ {2}} y \mathrm{d} F _ {\eta} (y).
$$

再令 $a_{r}\rightarrow -\infty$ 和 $b_{r}\to \infty ,r = 1,2$ 得

$$
\int_ {- \infty} ^ {\infty} x y \mathrm{d} F (x, y) = \int_ {- \infty} ^ {\infty} x \mathrm{d} F _ {\xi} (x) \int_ {- \infty} ^ {\infty} y \mathrm{d} F _ {\eta} (y).
$$

这说明  $\mathbf{E}(\xi\eta)=\mathbf{E}\xi\mathbf{E}\eta.$

例4.2.3 令 $\xi$ 为给定的随机变量. 若 $\mathbb{R}$ 上的不降函数 $f, g$ 满足 $\mathbf{E}[|f(\xi)| + |g(\xi)|] < \infty$. 则有

$$
\mathbf {E} [ f (\xi) ] \mathbf {E} [ g (\xi) ] \leqslant \mathbf {E} [ f (\xi) g (\xi) ]. \tag {4.2.5}
$$

为说明上式成立, 令 $\eta$ 为与 $\xi$ 独立同分布的随机变量. 因为 $f, g$ 都是不降函数, 总有 $[f(\xi) - f(\eta)][g(\xi) - g(\eta)] \geqslant 0$. 于是

$$
\begin{array}{l} 0 \leqslant \mathbf {E} \left\{\left[ f (\xi) - f (\eta) \right] \left[ g (\xi) - g (\eta) \right] \right\} \\ \leqslant \mathbf {E} [ f (\xi) g (\xi) ] - \mathbf {E} [ f (\eta) g (\xi) ] - \mathbf {E} [ f (\xi) g (\eta) ] + \mathbf {E} [ f (\eta) g (\eta) ] \\ \leqslant 2 \mathbf {E} [ f (\xi) g (\xi) ] - \mathbf {E} [ f (\eta) ] \mathbf {E} [ g (\xi) ] - \mathbf {E} [ f (\xi) ] \mathbf {E} [ g (\eta) ] \\ \leqslant 2 \mathbf {E} [ f (\xi) g (\xi) ] - 2 \mathbf {E} [ f (\xi) ] \mathbf {E} [ g (\xi) ]. \\ \end{array}
$$

所以 (4.2.5) 式成立.

## 4.2.4 常见分布的期望

例 4.2.4 设  $\xi$  服从伯努利分布  $B(1,p)$ . 则  $\mathbf{E}\xi = 1 \cdot p + 0 \cdot (1 - p) = p$ .

例 4.2.5 设  $\xi$  服从二项分布  $B(n,p)$ . 则  $\xi \stackrel{d}{=} \xi_{1} + \xi_{2} + \cdots + \xi_{n}$ ，其中  $\xi_{1}, \xi_{2}, \cdots, \xi_{n}$  相互独立且服从伯努利分布  $B(1,p)$ . 所以  $E\xi = E\xi_{1} + E\xi_{2} + \cdots + E\xi_{n} = np$ .

例4.2.6 设 $\xi$ 服从几何分布 $G(p)$. 利用幂级数的求导公式

$$
\begin{array}{l} \mathbf {E} \xi = \sum_ {i = 1} ^ {\infty} i (1 - p) ^ {i - 1} p = p \sum_ {i = 1} ^ {\infty} i (1 - p) ^ {i - 1} \\ = - p \frac {\mathrm{d}}{\mathrm{d} p} \sum_ {i = 1} ^ {\infty} (1 - p) ^ {i} = - p \frac {\mathrm{d}}{\mathrm{d} p} \left(\frac {1}{p} - 1\right) = \frac {1}{p}. \\ \end{array}
$$

我们知道, $\xi$ 同分布于可数重伯努利试验中到第 1 次成功时的试验次数. 由上式可以看出, 当 $p$ 变小时 $\mathbf{E}\xi$ 会变大, 即平均试验次数变大.

例 4.2.7 设随机变量  $\xi$  服从泊松分布  $P(\lambda)$ . 则

$$
\mathbf {E} \xi = \sum_ {i = 1} ^ {\infty} \frac {i \lambda^ {i}}{i !} \mathrm{e} ^ {- \lambda} = \lambda \sum_ {i = 1} ^ {\infty} \frac {\lambda^ {i - 1}}{(i - 1) !} \mathrm{e} ^ {- \lambda} = \lambda .
$$

例 4.2.8 设  $\xi$  服从均匀分布  $U(a,b)$ . 则

$$
\mathbf {E} \xi = \int_ {a} ^ {b} \frac {x}{b - a} \mathrm{d} x = \frac {a + b}{2}.
$$

例4.2.9 设随机变量 $\xi$ 服从指数分布 $E(\lambda)$. 则

$$
\mathbf {E} \xi = \int_ {0} ^ {\infty} x \lambda \mathrm{e} ^ {- \lambda x} \mathrm{d} x = - x \mathrm{e} ^ {- \lambda x} \big | _ {0} ^ {\infty} + \int_ {0} ^ {\infty} \mathrm{e} ^ {- \lambda x} \mathrm{d} x = \frac {1}{\lambda}.
$$

例4.2.10 设随机变量 $\xi$ 服从正态分布 $N(a, \sigma^2)$. 则

$$
\begin{array}{l} \mathbf {E} \xi = \frac {1}{\sqrt {2 \pi} \sigma} \int_ {- \infty} ^ {\infty} x \mathrm{e} ^ {- \frac {(x - a) ^ {2}}{2 \sigma^ {2}}} \mathrm{d} x \\ = \frac {1}{\sqrt {2 \pi} \sigma} \int_ {- \infty} ^ {\infty} (x + a) \mathrm{e} ^ {- \frac {x ^ {2}}{2 \sigma^ {2}}} \mathrm{d} x = a. \\ \end{array}
$$

例 4.2.11 设  $\xi$  服从卡方分布  $\chi^{2}(n)$ . 则  $\xi \stackrel{d}{=} \sum_{i=1}^{n} \xi_{i}^{2}$ , 其中  $\xi_{i}, i=1,2,\cdots,n$  独立且服从分布  $N(0,1)$ . 因此

$$
\mathbf {E} \xi = \sum_ {i = 1} ^ {n} \mathbf {E} (\xi_ {i} ^ {2}) = n \mathbf {E} (\xi_ {1} ^ {2}) = \frac {n}{\sqrt {2 \pi}} \int_ {- \infty} ^ {\infty} x ^ {2} \mathrm{e} ^ {- \frac {x ^ {2}}{2}} \mathrm{d} x = n.
$$

例 4.2.12 设  $\xi$  服从学生分布  $t(n)$ . 根据学生分布的定义, 若取 X 服从分布  $N(0,1)$  和 Y 服从分布  $\chi^{2}(n)$  且二者相互独立, 则  $\xi \stackrel{\mathrm{d}}{=} X / \sqrt{Y / n}$ . 利用独立性得

$$
\mathbf {E} \xi = \mathbf {E} X \cdot \mathbf {E} \Big (\frac {1}{\sqrt {Y / n}} \Big) = 0.
$$

例 4.2.13 柯西分布的数学期望不存在. 以具有参数  $(0,1)$  的柯西分布为例. 该分布的密度函数为

$$
p (x) = \frac {1}{\pi (1 + x ^ {2})}, \quad x \in \mathbb {R}.
$$

因此有

$$
\int_ {- \infty} ^ {\infty} | x | p (x) \mathrm{d} x = \int_ {- \infty} ^ {\infty} \frac {| x |}{\pi (1 + x ^ {2})} \mathrm{d} x = \infty .
$$

## 4.2.5 期望和积分收敛定理

定理 4.2.17（有界收敛定理） 设随机变量  $\xi, \xi_{n}, n=1,2,\cdots$  满足  $\lim_{n\to\infty}\xi_{n}\stackrel{a.s.}{=} \xi$ . 若有常数  $M \geqslant 0$  使得  $|\xi_{n}| \leqslant M$  (a.s.),  $n=1,2,\cdots$ , 则有  $\lim_{n\to\infty}E\xi_{n}=E\xi$ .

证明 显然, 可以假定在全空间 $\Omega$ 上有 $\lim_{n\to \infty}\xi_n = \xi$ 且 $|\xi_n| \leqslant M, n = 1,2,\dots$. 这样, 显然有 $|\xi| \leqslant M$, 故随机变量 $\xi, \xi_n, n = 1,2,\dots$ 均可积. 对于 $\varepsilon > 0$, 令 $A_n = \{\omega \in \Omega : \sup_{k \geqslant n} |\xi_k(\omega) - \xi(\omega)| \geqslant \varepsilon\}$. 则事件序列 $\{A_n\} \subseteq \mathscr{F}$ 不增且有 $\bigcap_{n=1}^{\infty} A_n = \varnothing$. 由数学期望的性质,

$$
\left| \mathbf {E} \xi_ {n} - \mathbf {E} \xi \right| \leqslant \mathbf {E} | \xi_ {n} - \xi | \leqslant \mathbf {E} (2 M 1 _ {A _ {n}} + \varepsilon) = 2 M \mathbf {P} (A _ {n}) + \varepsilon .
$$

根据概率的上连续性有 $\lim_{n\to \infty}\mathbf{P}(A_n) = 0$ ，故得 $\limsup_{n\to \infty}|\mathbf{E}\xi_n - \mathbf{E}\xi |\leqslant \varepsilon .$ 再由 $\varepsilon >0$ 的任意性知 $\limsup_{n\to \infty}|\mathbf{E}\xi_n - \mathbf{E}\xi | = 0,$ 故有 $\lim_{n\to \infty}\mathbf{E}\xi_n = \mathbf{E}\xi .$ □定理 4.2.17 称为有界收敛定理. 在此基础上, 可以证明下面的单调收敛定理、法图 (Fatou) 定理和控制收敛定理. 它们构成关于随机变量的数学期望收敛性质的基本定理.

定理 4.2.18（单调收敛定理） 设  $\xi, \xi_{n}, n = 1, 2, \cdots$  为非负随机变量且单调不降地  $\lim_{n \to \infty} \xi_{n} \stackrel{a.s.}{=} \xi$ . 则有  $\lim_{n \to \infty} E\xi_{n} = E\xi$ .

证明 当 $\xi$ 有界时, 根据定理4.2.17有 $\lim_{n\to \infty}\mathbf{E}\xi_n = \mathbf{E}\xi$. 下面考虑一般情况. 显然 $\limsup_{n\to \infty}\mathbf{E}\xi_n\leqslant \mathbf{E}\xi$. 另一方面, 任取 $k\geqslant 1$ 并对随机变量 $\xi \wedge k$ 和 $\xi_{n}\wedge k$ 应用定理4.2.17得

$$
\operatorname * {l i m i n f} _ {n \to \infty} \mathbf {E} \xi_ {n} \geqslant \lim _ {n \to \infty} \mathbf {E} (\xi_ {n} \wedge k) = \mathbf {E} (\xi \wedge k) \geqslant \mathbf {E} (\xi 1 _ {\{\xi \leqslant k \}}),
$$

其中

$$
\mathbf {E} (\xi 1 _ {\{\xi \leqslant k \}}) = \int_ {0} ^ {\infty} x 1 _ {\{x \leqslant k \}} \mathrm{d} F (x) = \int_ {0} ^ {k} x \mathrm{d} F (x).
$$

根据斯蒂尔切斯积分的定义有 $\lim_{k\to \infty}\mathbf{E}(\xi 1_{\{\xi \leqslant k\}}) = \infty$ ，因此有 $\liminf_{n\to \infty}\mathbf{E}\xi_n\geqslant \mathbf{E}\xi .$

定理 4.2.19（法图定理） 对于任何非负随机变量  $\xi_{n}, n=1,2,\cdots$  有

$$
\operatorname * {l i m i n f} _ {n \to \infty} \mathbf {E} \xi_ {n} \geqslant \mathbf {E} \big (\operatorname * {l i m i n f} _ {n \to \infty} \xi_ {n} \big). \tag {4.2.6}
$$

证明 令 $\eta_{n} = \inf_{k\geqslant n}\xi_{k}$ .则有 $0\leqslant \eta_n\leqslant \xi_n$ 且单调不降地 $\lim_{n\to \infty}\eta_n = \liminf_{n\to \infty}\xi_n$ 利用单调收敛定理即得(4.2.6)式.

定理 4.2.20（控制收敛定理） 设随机变量  $\xi, \xi_{n}, n=1,2,\cdots$  满足  $\lim_{n\to\infty}\xi_{n}\stackrel{a.s.}{=} \xi$ . 若有非负可积随机变量  $\eta$  使得  $|\xi_{n}|\leqslant\eta$  (a.s.),  $n=1,2,\cdots$ , 则有  $\lim_{n\to\infty}E\xi_{n}=E\xi$ .

证明 在假设条件下  $\eta \pm \xi_{n}, n = 1, 2, \cdots$  均为非负随机变量. 根据法图定理有

$$
\operatorname * {l i m   i n f} _ {n \to \infty} (\mathbf {E} \eta \pm \mathbf {E} \xi_ {n}) = \operatorname * {l i m   i n f} _ {n \to \infty} \mathbf {E} (\eta \pm \xi_ {n}) \geqslant \mathbf {E} (\eta \pm \xi) = \mathbf {E} \eta \pm \mathbf {E} \xi .
$$

因此有  $\lim_{n\to\infty}E\xi_{n}=E\xi.$

例 4.2.14 取  $\Omega=(0,1)$  和  $\mathcal{F}=(0,1)\cap\mathcal{B}$ ，令 P 为  $(\Omega,\mathcal{F})$  上的勒贝格测度。则  $(\Omega,\mathcal{F},\mathbf{P})$  为概率空间。对  $n\geqslant1$  令  $\xi_{n}=n1_{(0,1/n]}$ 。显然  $\lim_{n\to\infty}\xi_{n}=0$  在  $\Omega$  上处处成立。但是  $\lim_{n\to\infty}\mathbf{E}\xi_{n}=1\neq0$ 。这说明极限与数学期望次序的交换并不是无条件成立的。

因为随机变量的数学期望是用关于其分布或分布函数的积分定义的, 所以上面的基本收敛定理本质上是关于积分的收敛定理. 下面分别给出了便于应用的有界收敛定理和控制收敛定理的积分形式.

定理 4.2.21（有界收敛定理）令 G 是  $(\mathbb{R}, \mathcal{B})$  上的有限测度  $\mu$  的分布函数。设  $f, f_{n}, n = 1, 2, \cdots$  是 R 上的 G 可积函数且相对  $\mu$  有  $\lim_{n \to \infty} f_{n} = f$  (a.e.)。若有常数  $M \geqslant 0$  使得  $|f_{n}| \leqslant M$  (a.e.),  $n = 1, 2, \cdots$ ，则

$$
\lim _ {n \to \infty} \int_ {- \infty} ^ {\infty} f _ {n} (x) \mathrm{d} G (x) = \int_ {- \infty} ^ {\infty} f (x) \mathrm{d} G (x). \tag {4.2.7}
$$

证明 只需考虑 G 为概率分布函数的情况. 此时, 令  $\xi$  是以 G 为分布函数的随机变量. 根据假定条件, 显然有  $\lim_{n\to\infty}f_n(\xi)=f(\xi)$  和  $|f_n(\xi)|\leqslant M$  (a.s.),  $n=1,2,\cdots$ . 由定理 4.2.7 和定理 4.2.17 即得欲证结论. □

称 $\mathbb{R}$ 上的函数 $f$ 有有界支撑, 是指存在常数 $A \geqslant 0$ 使当 $|x| \geqslant A$ 有 $f(x) = 0$.

推论4.2.22 设 $F$ 和 $G$ 是 $\mathbb{R}$ 上的有界分布函数且 $F(-\infty) = G(-\infty) = 0$. 若对于任何有有界支撑的连续函数 $f$ 都有

$$
\int_ {- \infty} ^ {\infty} f (x) \mathrm{d} F (x) = \int_ {- \infty} ^ {\infty} f (x) \mathrm{d} G (x), \tag {4.2.8}
$$

则 $F$ 和 $G$ 在 $\mathbb{R}$ 上恒相等.

证明 任取 $a < b \in \mathbb{R}$. 易证 $g(x) := \inf \{|x - y| : y \in (a, b)^c\}$ 为 $\mathbb{R}$ 上的非负连续函数, 且对 $x \in (a, b)$ 有 $g(x) > 0$, 而对 $x \in (a, b)^c$ 有 $g(x) = 0$. 再对 $k \geqslant 1$ 令 $f_k(x) = 1 \wedge [kg(x)]$. 则 $f_k$ 为 $\mathbb{R}$ 上的有有界支撑的非负连续函数, 且当 $k \to \infty$ 时单调不降地 $f_k(x) \to 1_{(a, b)}(x)$. 对函数 $f_k$ 应用 (4.2.8) 式, 再令 $k \to \infty$, 由定理 4.2.21 得

$$
\int_ {- \infty} ^ {\infty} 1 _ {(a, b)} (x) \mathrm{d} F (x) = \int_ {- \infty} ^ {\infty} 1 _ {(a, b)} (x) \mathrm{d} G (x),
$$

即有 $F(b - ) - F(a) = G(b - ) - G(a)$. 取 $a = x - n$ 和 $b = x + 1 / n$ 并令 $n\to \infty$ 即得$F(x) = G(x)$ □

定理 4.2.23（控制收敛定理）令 G 是  $(\mathbb{R}, \mathcal{B})$  上的局部有限测度  $\mu$  的分布函数。设  $f, f_{n}, n = 1, 2, \cdots$  是 R 上的 G 可积函数且相对  $\mu$  有  $\lim_{n \to \infty} f_{n} = f$  (a.e.). 若有非负 G 可积函数 g 使得  $|f_{n}| \leqslant g$  (a.e.),  $n = 1, 2, \cdots$ ，则

$$
\lim _ {n \to \infty} \int_ {- \infty} ^ {\infty} f _ {n} (x) \mathrm{d} G (x) = \int_ {- \infty} ^ {\infty} f (x) \mathrm{d} G (x). \tag {4.2.9}
$$

证明 令 $F$ 是由 (4.1.12) 式定义的分布函数. 因为 $g$ 是 $G$ 可积函数, 所以 $F$ 在 $\mathbb{R}$ 上有界, 故它是某个有限测度 $\nu$ 的分布函数. 显然相对 $\nu$ 有 $\lim_{n\to \infty}f_n g^{-1}1_{\{g > 0\}} = fg^{-1}1_{\{g > 0\}}$ (a.e.). 根据定理 4.1.11 有

$$
\int_ {- \infty} ^ {\infty} f _ {n} (x) \mathrm{d} G (x) = \int_ {- \infty} ^ {\infty} f _ {n} (x) g (x) ^ {- 1} 1 _ {\{g (x) > 0 \}} \mathrm{d} F (x).
$$

对有界函数序列 $\{f_n g^{-1} 1_{\{g > 0\}}\}$ 和分布函数 $F$ 应用定理4.2.21即得欲证结论.

## 4.2.6 斯坦方程

设随机变量 $Z$ 服从标准正态分布 $N(0,1)$. 给定 $\mathbb{R}$ 上的有界可测函数 $h$, 考虑下面的关于该函数的斯坦 (Stein) 方程:

$$
f ^ {\prime} (x) - x f (x) = h (x) - \mathbf {E} h (Z). \tag {4.2.10}
$$

称绝对连续函数 $f$ 是方程 (4.2.10) 的解, 是指该方程对几乎所有 $x \in \mathbb{R}$ 成立. 将方程两边同乘因子 $\mathrm{e}^{-x^2 / 2}$ 得

$$
\left[ \mathrm{e} ^ {- x ^ {2} / 2} f (x) \right] ^ {\prime} = \mathrm{e} ^ {- x ^ {2} / 2} \big [ h (x) - \mathbf {E} h (Z) \big ].
$$

由此易知方程 (4.2.10) 有特解

$$
f _ {-} (x) = \mathrm{e} ^ {x ^ {2} / 2} \int_ {- \infty} ^ {x} \left[ h (y) - \mathbf {E} h (Z) \right] \mathrm{e} ^ {- y ^ {2} / 2} \mathrm{d} y \tag {4.2.11}
$$

和

$$
f _ {+} (x) = - \mathrm{e} ^ {x ^ {2} / 2} \int_ {x} ^ {\infty} \big [ h (y) - \mathbf {E} h (Z) \big ] \mathrm{e} ^ {- y ^ {2} / 2} \mathrm{d} y. \tag {4.2.12}
$$

注意, 对  $x \geqslant 1$  有

$$
| f _ {+} (x) | \leqslant 2 \| h \| \mathrm{e} ^ {x ^ {2} / 2} \int_ {x} ^ {\infty} y \mathrm{e} ^ {- y ^ {2} / 2} \mathrm{d} y = 2 \| h \|.
$$

所以 $f_{+}$ 在任何形如 $[a, \infty)$ 的区间上有界；同理 $f_{-}$ 在任何形如 $(- \infty, a]$ 的区间上有界。斯坦方程在正态分布及相关极限定理的研究中有重要的应用。基于该方程的方法称为斯坦方法。

定理4.2.24 随机变量 $X$ 服从正态分布 $N(0,1)$ 当且仅当对 $\mathbb{R}$ 上的任何满足 $\mathbf{E}|f'(X)| < \infty$ 的连续且分段连续可微函数 $f$ 有

$$
\mathbf {E} f ^ {\prime} (X) = \mathbf {E} [ X f (X) ]. \tag {4.2.13}
$$

证明 假设随机变量 $X$ 服从分布 $N(0,1)$. 再设连续且分段连续可微函数 $f$ 满足 $\mathbf{E}|f'(X)| < \infty$. 则

$$
\begin{array}{l} \mathbf {E} f ^ {\prime} (X) = \frac {1}{\sqrt {2 \pi}} \int_ {- \infty} ^ {\infty} f ^ {\prime} (y) \mathrm{e} ^ {- y ^ {2} / 2} \mathrm{d} y \\ = \frac {1}{\sqrt {2 \pi}} \int_ {0} ^ {\infty} f ^ {\prime} (y) \mathrm{d} y \int_ {y} ^ {\infty} x \mathrm{e} ^ {- x ^ {2} / 2} \mathrm{d} x - \frac {1}{\sqrt {2 \pi}} \int_ {- \infty} ^ {0} f ^ {\prime} (y) \mathrm{d} y \int_ {- \infty} ^ {y} x \mathrm{e} ^ {- x ^ {2} / 2} \mathrm{d} x \\ = \frac {1}{\sqrt {2 \pi}} \int_ {0} ^ {\infty} x \mathrm{e} ^ {- x ^ {2} / 2} \mathrm{d} x \int_ {0} ^ {x} f ^ {\prime} (y) \mathrm{d} y - \frac {1}{\sqrt {2 \pi}} \int_ {- \infty} ^ {0} x \mathrm{e} ^ {- x ^ {2} / 2} \mathrm{d} x \int_ {x} ^ {0} f ^ {\prime} (y) \mathrm{d} y \\ = \frac {1}{\sqrt {2 \pi}} \int_ {- \infty} ^ {\infty} [ f (x) - f (0) ] x \mathrm{e} ^ {- x ^ {2} / 2} \mathrm{d} x. \\ \end{array}
$$

因此 (4.2.13) 式成立. 反之, 假设对任何满足 $\mathbf{E}|f'(X)| < \infty$ 的连续且分段连续可微函数 $f$ 有 (4.2.13) 式成立. 将特解表达式 (4.2.11) 和 (4.2.12) 应用于函数 $h(x) = 1_{\{x \leqslant a\}}$, 对于 $x \leqslant a$ 有

$$
f _ {-} (x) = \mathrm{e} ^ {x ^ {2} / 2} \int_ {- \infty} ^ {x} \mathrm{e} ^ {- y ^ {2} / 2} [ 1 - \varPhi (a) ] \mathrm{d} y = \sqrt {2 \pi} \mathrm{e} ^ {x ^ {2} / 2} \varPhi (x) [ 1 - \varPhi (a) ],
$$

而对于 $x \geqslant a$ 有

$$
f _ {+} (x) = - \mathrm{e} ^ {x ^ {2} / 2} \int_ {x} ^ {\infty} \mathrm{e} ^ {- y ^ {2} / 2} \varPhi (a) \mathrm{d} y = \sqrt {2 \pi} \mathrm{e} ^ {x ^ {2} / 2} \varPhi (a) [ 1 - \varPhi (x) ].
$$

显然, 函数 $f_{a}(x) := f_{-}(x)1_{\{x \leqslant a\}} + f_{+}(x)1_{\{x > a\}}$ 在 $\mathbb{R}$ 上有界连续、分段连续可微, 并且也是关于 $h(x) = 1_{\{x \leqslant a\}}$ 的斯坦方程的解. 再根据 (4.2.10) 式和 (4.2.13) 式有

$$
0 = \mathbf {E} \big [ f _ {a} ^ {\prime} (X) - X f _ {a} (X) \big ] = \mathbf {E} \big [ 1 _ {\{X \leqslant a \}} - \varPhi (a) \big ] = \mathbf {P} (X \leqslant a) - \varPhi (a).
$$

所以 X 服从标准正态分布  $N(0,1)$ .

## 练习题

1. 设  $\xi$  为非负整数值随机变量且有常数 a, b > 0 使得

$$
\mathbf {P} (\xi = n) = \frac {a b ^ {n}}{n !}, \quad n = 0, 1, 2, \dots .
$$

已知  $E\xi = A$ . 求 a, b 的值.

2. 设 $\xi$ 是非负整数值随机变量. 证明 $\xi$ 服从参数为 $\lambda > 0$ 的泊松分布当且仅当对任何整数 $k \geqslant 1$ 有 $\lambda \mathbf{P}(\xi = k - 1) = k \mathbf{P}(\xi = k)$.
3. 设  $\xi, \eta$  独立同分布且服从正态分布  $N(0,1)$ . 证明  $\mathbf{E}(\xi \vee \eta) = 1/\sqrt{\pi}$ .
4. 某城市共有 N 辆汽车, 车牌号从 1 到 N. 现随机地记下 n 辆车的牌号, 记其最大牌号为  $\xi$ . 求数学期望  $E\xi$ .
5. 设随机变量  $\xi, \eta$  相互独立且均服从指数分布  $E(\lambda)$ . 求数学期望  $\mathbf{E}[(\xi + \eta)^{2}]$ .
6. 在  $(0,1)$  区间随机取 n 个点, 求相距最远的两点距离的期望.

## 4.3 方差、协方差和高阶矩

方差是随机变量的二阶中心矩, 反映了它的取值与期望偏离的程度, 具有非常重要的统计学意义. 协方差包含了两个随机变量之间相互关系有用的信息.

## 4.3.1 方差和标准差

设 $(\Omega, \mathcal{F}, \mathbf{P})$ 是一个概率空间. 称随机变量 $\xi$ 平方可积, 是指满足 $\mathbf{E}(\xi^2) < \infty$. 此时有 $\mathbf{E}|\xi| < \mathbf{E}(1 + \xi^2) < \infty$, 故 $\xi$ 可积. 令 $L^2$ 是由 $(\Omega, \mathcal{F}, \mathbf{P})$ 上的所有平方可积随机变量构成的集合.

定理4.3.1 假设有 $\xi, \eta \in L^2$. 则随机变量 $\xi \eta$ 可积且有

$$
\left[ \mathbf {E} (\xi \eta) \right] ^ {2} \leqslant \mathbf {E} (\xi^ {2}) \mathbf {E} (\eta^ {2}), \tag {4.3.1}
$$

且其中的等号成立当且仅当存在 $t \in \mathbb{R}$ 使 $\eta \stackrel{\mathrm{a.s.}}{=} t\xi$.

证明 考虑 $\mathbb{R}$ 上的二次函数

$$
u (t) := \mathbf {E} [ (t \xi - \eta) ^ {2} ] = \mathbf {E} (\xi^ {2}) t ^ {2} - 2 \mathbf {E} (\xi \eta) t + \mathbf {E} (\eta^ {2}).
$$

由 $u(t) \geqslant 0$ 知 (4.3.1) 式成立, 且等号成立当且仅当方程 $u(t) = 0$ 有唯一实根 $t \in \mathbb{R}$. 此时, 根据定理 4.2.3 有 $\eta \stackrel{\mathrm{a.s.}}{=} t\xi$. □

通常称 (4.3.1) 式为柯西-施瓦茨 (Cauchy-Schwarz) 不等式.

命题 4.3.2 平方可积随机变量集  $L^{2}$  是一个线性空间.

证明 假设 $\xi, \eta \in L^2$. 对任何 $\alpha, \beta \in \mathbb{R}$, 由柯西-施瓦茨不等式有

$$
\begin{array}{l} \mathbf {E} \big [ (\alpha \xi + \beta \eta) ^ {2} \big ] = \alpha^ {2} \mathbf {E} (\xi^ {2}) + 2 \alpha \beta \mathbf {E} (\xi \eta) + \beta^ {2} \mathbf {E} (\eta^ {2}) \\ \leqslant \alpha^ {2} \mathbf {E} (\xi^ {2}) + 2 | \alpha \beta | \left[ \mathbf {E} (\xi^ {2}) \mathbf {E} (\eta^ {2}) \right] ^ {1 / 2} + \beta^ {2} \mathbf {E} (\eta^ {2}) <   \infty . \\ \end{array}
$$

所以  $L^{2}$  是一个线性空间.

定义 4.3.1 对于  $\xi \in L^{2}$  记  $a = E\xi$ . 我们称

$$
\mathbf {V a r} \xi := \mathbf {E} [ (\xi - a) ^ {2} ] = \mathbf {E} (\xi^ {2}) - a ^ {2} = \mathbf {E} (\xi^ {2}) - (\mathbf {E} \xi) ^ {2} \tag {4.3.2}
$$

为 $\xi$ 的方差, 而称 $\sqrt{\mathrm{Var}\xi}$ 为 $\xi$ 的标准差.

粗略地讲, 方差 $\operatorname{Var} \xi$ 给出了随机变量 $\xi$ 与其期望值 $\mathbf{E}\xi$ 之间的偏差大小的一个度量. 由 (4.3.2) 式, 显然 $\operatorname{Var} \xi \geqslant 0$. 由定理 4.2.3 易知 $\operatorname{Var} \xi = 0$ 当且仅当 $(\xi - a)^2 \stackrel{\mathrm{a.s.}}{=} 0$, 而这等价于 $\xi \stackrel{\mathrm{a.s.}}{=} a = \mathbf{E}\xi$. 另外, 显然对任何 $c \in \mathbb{R}$ 有

$$
\mathbf {V a r} (\xi + c) = \mathbf {V a r} \xi , \quad \mathbf {V a r} (c \xi) = c ^ {2} \mathbf {V a r} \xi .
$$

命题 4.3.3 对于  $\xi \in L^{2}$ ，函数  $f(c) = \mathbf{E}[(\xi - c)^{2}]$  当且仅当  $c = E\xi$  时取得最小值 Var $\xi$ .

证明 记 $a = \mathbf{E}\xi$ . 由数学期望的性质, 有

$$
\begin{array}{l} f (c) = \mathbf {E} \big \{[ (\xi - a) - (c - a) ] ^ {2} \big \} \\ = \mathbf {E} [ (\xi - a) ^ {2} ] + (c - a) ^ {2} - 2 \mathbf {E} [ (\xi - a) (c - a) ] \\ = \mathbf {V a r} \xi + (c - a) ^ {2} = \mathbf {V a r} \xi + (c - \mathbf {E} \xi) ^ {2} \geqslant \mathbf {V a r} \xi , \\ \end{array}
$$

其中等号当且仅当  $c = E\xi$  时成立.