例4.3.1 设随机变量 $\xi$ 服从泊松分布 $P(\lambda)$. 由例4.2.7有 $\mathbf{E}\xi = \lambda$. 再注意

$$
\begin{array}{l} \mathbf {E} (\xi^ {2}) = \sum_ {i = 1} ^ {\infty} \frac {i ^ {2} \lambda^ {i}}{i !} \mathrm{e} ^ {- \lambda} = \lambda \sum_ {i = 1} ^ {\infty} \frac {i \lambda^ {i - 1}}{(i - 1) !} \mathrm{e} ^ {- \lambda} \\ = \lambda \left[ \sum_ {i = 1} ^ {\infty} \frac {\lambda^ {i - 1}}{(i - 1) !} + \lambda \sum_ {i = 2} ^ {\infty} \frac {\lambda^ {i - 2}}{(i - 2) !} \right] e ^ {- \lambda} \\ = \lambda (1 + \lambda). \\ \end{array}
$$

所以  $\mathbf{Var}\xi = \mathbf{E}(\xi^{2}) - (\mathbf{E}\xi)^{2} = \lambda.$

例 4.3.2 设随机变量  $\xi$  服从指数分布  $E(\lambda)$ . 根据例 4.2.9 有  $E\xi = 1/\lambda$ . 再注意

$$
\begin{array}{l} \mathbf {E} (\xi^ {2}) = \int_ {0} ^ {\infty} x ^ {2} \lambda \mathrm{e} ^ {- \lambda x} \mathrm{d} x = - x ^ {2} \mathrm{e} ^ {- \lambda x} | _ {0} ^ {\infty} + 2 \int_ {0} ^ {\infty} x \mathrm{e} ^ {- \lambda x} \mathrm{d} x \\ = - 2 x \mathrm{e} ^ {- \lambda x} \big | _ {0} ^ {\infty} + \frac {2}{\lambda} \int_ {0} ^ {\infty} \mathrm{e} ^ {- \lambda x} \mathrm{d} x = \frac {2}{\lambda^ {2}}. \\ \end{array}
$$

所以 $\mathbf{Var}\xi = \mathbf{E}(\xi^2) - (\mathbf{E}\xi)^2 = 1 / \lambda^2.$

例 4.3.3 设随机变量  $\xi$  服从正态分布  $N(a,\sigma^{2})$ . 由例 4.2.10 有  $E\xi = a$ . 所以

$$
\begin{array}{l} \mathrm{Var} \xi = \frac {1}{\sqrt {2 \pi} \sigma} \int_ {- \infty} ^ {\infty} (x - a) ^ {2} \mathrm{e} ^ {- \frac {(x - a) ^ {2}}{2 \sigma^ {2}}} \mathrm{d} x \\ = \frac {\sigma^ {2}}{\sqrt {2 \pi}} \int_ {- \infty} ^ {\infty} u ^ {2} \mathrm{e} ^ {- \frac {u ^ {2}}{2}} \mathrm{d} u \\ = \frac {\sigma^ {2}}{\sqrt {2 \pi}} \Big (- u \mathrm{e} ^ {- \frac {u ^ {2}}{2}} \Big | _ {- \infty} ^ {\infty} + \int_ {- \infty} ^ {\infty} \mathrm{e} ^ {- \frac {u ^ {2}}{2}} \mathrm{d} u \Big) = \sigma^ {2}. \\ \end{array}
$$

## 4.3.2 协方差和协方差矩阵

定义 4.3.2 给定随机变量  $\xi, \eta \in L^{2}$ ，我们称

$$
\mathbf {C o v} (\xi , \eta) := \mathbf {E} [ (\xi - \mathbf {E} \xi) (\eta - \mathbf {E} \eta) ] = \mathbf {E} (\xi \eta) - \mathbf {E} \xi \mathbf {E} \eta \tag {4.3.3}
$$

为  $\xi$  与  $\eta$  的协方差.

由 (4.3.3) 式可以看出, 粗略地讲, 若 $\mathbf{Cov}(\xi, \eta) > 0$, 则随机变量 $\xi - \mathbf{E}\xi$ 和 $\eta - \mathbf{E}\eta$ 倾向于取同号. 反之, 若 $\mathbf{Cov}(\xi, \eta) < 0$, 则随机变量 $\xi - \mathbf{E}\xi$ 和 $\eta - \mathbf{E}\eta$ 倾向于取异号.

命题 4.3.4 令  $\xi,\eta,\zeta\in L^{2}$ . 下面的性质成立:

(1) (对称性)  $\mathbf{Cov}(\xi,\eta)=\mathbf{Cov}(\eta,\xi);$
(2) (双线性性) 对任意的 $a, b \in \mathbb{R}$;

$$
\mathbf {C o v} (a \xi + b \eta , \zeta) = a \mathbf {C o v} (\xi , \zeta) + b \mathbf {C o v} (\eta , \zeta),
$$

$$
\mathbf {C o v} (\xi , a \eta + b \zeta) = a \mathbf {C o v} (\xi , \eta) + b \mathbf {C o v} (\xi , \zeta);
$$

(3) $\mathbf{Var}(\xi + \eta) = \mathbf{Var}\xi + \mathbf{Var}\eta + 2\mathbf{Cov}(\xi, \eta)$.

证明 显然 (1), (2) 成立. 记 $a = \mathbf{E}\xi$ 和 $b = \mathbf{E}\eta$. 则有

$$
\begin{array}{l} \mathbf {V a r} (\xi + \eta) = \mathbf {E} \left\{\left[ (\xi + \eta) - (a + b) \right] ^ {2} \right\} \\ = \mathbf {E} \left\{\left[ (\xi - a) + (\eta - b) \right] ^ {2} \right\} \\ = \mathbf {E} [ (\xi - a) ^ {2} ] + \mathbf {E} [ (\eta - b) ^ {2} ] + 2 \mathbf {E} [ (\xi - a) (\eta - b) ], \\ \end{array}
$$

即 (3) 成立.

定义 4.3.3 给定随机变量  $\xi_{1}, \xi_{2}, \cdots, \xi_{n} \in L^{2}$ ，我们称

$$
B = (b (i, j)) _ {1 \leqslant i, j \leqslant n} := (\mathbf {C o v} (\xi_ {i}, \xi_ {j})) _ {1 \leqslant i, j \leqslant n}
$$

为随机向量  $\xi := (\xi_{1}, \xi_{2}, \cdots, \xi_{n})$  的协方差矩阵, 并记作  $B = \mathbf{Var}(\xi)$ .

定理 4.3.5 对于  $\xi_{1}, \xi_{2}, \cdots, \xi_{n} \in L^{2}$ ，随机向量  $(\xi_{1}, \xi_{2}, \cdots, \xi_{n})$  的协方差矩阵 B 为半正定对称矩阵.

证明 根据命题 4.3.4 (1) 知 $B$ 为对称矩阵. 对于 $x \in \mathbb{R}^n$, 我们有

$$
\begin{array}{l} \sum_ {i, j} x _ {i} x _ {j} \mathbf {C o v} (\xi_ {i}, \xi_ {j}) = \sum_ {i, j} x _ {i} x _ {j} \mathbf {E} [ (\xi_ {i} - \mathbf {E} \xi_ {i}) (\xi_ {j} - \mathbf {E} \xi_ {j}) ] \\ = \mathbf {E} \Big [ \sum_ {i, j} x _ {i} x _ {j} (\xi_ {i} - \mathbf {E} \xi_ {i}) (\xi_ {j} - \mathbf {E} \xi_ {j}) \Big ] \\ = \mathbf {E} \left\{\left[ \sum_ {i = 1} ^ {n} x _ {i} (\xi_ {i} - \mathbf {E} \xi_ {i}) \right] ^ {2} \right\} \geqslant 0. \\ \end{array}
$$

即 B 为半正定矩阵.

定义 4.3.4 若随机变量  $\xi, \eta \in L^{2}$  满足  $\mathbf{Cov}(\xi, \eta) = 0$ ，则称它们是不相关的.

由定义 4.3.2 和命题 4.3.4 不难得到:

命题 4.3.6 对于  $\xi, \eta \in L^{2}$  下面的性质相互等价:

(1) $\xi, \eta$ 不相关;
(2)  $\mathbf{E}(\xi\eta)=\mathbf{E}\xi\mathbf{E}\eta;$

(3) $\mathbf{Var}(\xi + \eta) = \mathbf{Var}\xi + \mathbf{Var}\eta$.

命题 4.3.7 若  $\xi, \eta \in L^{2}$  相互独立, 则它们不相关.

例 4.3.4 已知  $\theta$  服从分布  $U(-\pi, \pi)$ . 令  $\xi = \sin\theta, \eta = \cos\theta$ . 证明  $\xi, \eta$  不相关且不独立.

证明 此时, 显然有 $\mathbf{E}\xi = \mathbf{E}\eta = 0$. 而因为 $\sin x\cos x$ 是奇函数, 所以

$$
\mathbf {E} (\xi \eta) = \frac {1}{2 \pi} \int_ {- \pi} ^ {\pi} \sin x \cos x \mathrm{d} x = 0.
$$

因此 $\xi, \eta$ 不相关. 注意

$$
\mathbf {P} (0 <   \xi <   1 / 2) = \mathbf {P} (\{0 <   \theta <   \pi / 6 \} \cup \{5 \pi / 6 <   \theta <   \pi \}) = 1 / 6,
$$

$$
\mathbf {P} (0 <   \eta <   1 / 2) = \mathbf {P} (\{- \pi / 2 <   \theta <   - \pi / 3 \} \cup \{\pi / 3 <   \theta <   \pi / 2 \}) = 1 / 6.
$$

另外，

$$
\mathbf {P} (0 <   \xi <   1 / 2, 0 <   \eta <   1 / 2) = \mathbf {P} (\varnothing) = 0.
$$

所以  $\xi,\eta$  不独立.

例4.3.5 设 $\xi$ 服从伯努利分布 $B(1,p)$. 则有 $\mathbf{E}\xi = p$ 和

$$
\mathbf {V a r} \xi = \mathbf {E} [ (\xi - p) ^ {2} ] = (1 - p) ^ {2} p + p ^ {2} (1 - p) = p (1 - p).
$$

例 4.3.6 设  $\xi$  服从二项分布  $B(n,p)$ . 则  $\xi \stackrel{d}{=} \xi_{1} + \xi_{2} + \cdots + \xi_{n}$ ，其中  $\xi_{1}, \xi_{2}, \cdots, \xi_{n}$  相互独立且服从伯努利分布  $B(1,p)$ . 所以有 E\xi = np 和 Var\x = np(1 - p).

## 4.3.3 相关系数

根据之前定义的概念, 随机变量 $\xi$ 是退化的, 是指存在常数 $a$ 使得 $\mathbf{P}(\xi = a) = 1$. 否则 $\xi$ 就是非退化的. 显然 $\xi \in L^2$ 非退化当且仅当 $\operatorname{Var}\xi > 0$.

定义 4.3.5 对于非退化的随机变量  $\xi \in L^{2}$ ，我们定义其标准化随机变量

$$
\xi^ {*} := \frac {\xi - \mathbf {E} \xi}{\sqrt {\mathbf {V a r} \xi}}.
$$

注意  $\mathbf{E}(\xi^{*})=0$  而  $\mathbf{Var}(\xi^{*})=1$ .

定义 4.3.6 假设随机变量  $\xi, \eta \in L^{2}$  非退化. 我们称

$$
r := \mathbf {E} (\xi^ {*} \eta^ {*}) = \mathbf {C o v} (\xi^ {*}, \eta^ {*}) = \frac {\mathbf {C o v} (\xi , \eta)}{\sqrt {\mathbf {V a r} \xi \cdot \sqrt {\mathbf {V a r} \eta}}}
$$

为  $\xi$  和  $\eta$  的相关系数.

显然, 当 $r = 0$ 时 $\xi$ 与 $\eta$ 不相关. 在一般情况下, 相关系数 $r$ 体现了 $\xi$ 和 $\eta$ 相互关联或影响的程度.

定理4.3.8 假设 $\xi, \eta \in L^2$ 非退化. 则有 $|r| \leqslant 1$ 且

(1) $r = 1 \Leftrightarrow \xi^{*} \stackrel{\text{a.s.}}{=} \eta^{*}$; (2) $r = -1 \Leftrightarrow \eta^{*} \stackrel{\text{a.s.}}{=} -\xi^{*}$.

证明 根据柯西-施瓦茨不等式, 有

$$
| r | = | \mathbf {E} (\xi^ {*} \eta^ {*}) | \leqslant \left\{\mathbf {E} [ (\xi^ {*}) ^ {2} ] \mathbf {E} [ (\eta^ {*}) ^ {2} ] \right\} ^ {1 / 2} = \sqrt {\mathbf {V a r} (\xi^ {*}) \mathbf {V a r} (\eta^ {*})} = 1,
$$

且等号成立当且仅当有 $t \in \mathbb{R}$ 使得 $\eta^{*} = t\xi^{*}$. 此时, 由上式得

$$
1 = | r | = | \mathbf {E} (\xi^ {*} \eta^ {*}) | = | t | \mathbf {E} [ (\xi^ {*}) ^ {2} ] = | t |.
$$

进而易知结论成立.

推论4.3.9 假设 $\xi$ 和 $\eta \in L^2$ 非退化. 若 $|r| = 1$, 则存在常数 $a, b$, 使 $\eta \stackrel{\mathrm{a.s.}}{=} a + b\xi$ 且 $rb > 0$.

证明 先考虑 $r = 1$ 的情况. 此时, 由定理4.3.8有 $\eta^{*} \stackrel{\mathrm{a.s.}}{=} \xi^{*}$, 即

$$
\frac {\xi - \mathbf {E} \xi}{\sqrt {\mathbf {V a r} \xi}} = \frac {\eta - \mathbf {E} \eta}{\sqrt {\mathbf {V a r} \eta}},
$$

从而 (a.s.)

$$
\eta = \mathbf {E} \eta + \frac {\sqrt {\mathbf {V a r} \eta}}{\sqrt {\mathbf {V a r} \xi}} (\xi - \mathbf {E} \xi) = a + b \xi ,
$$

其中

$$
a = \mathbf {E} \eta - \frac {\sqrt {\mathbf {V a r} \eta}}{\sqrt {\mathbf {V a r} \xi}} \mathbf {E} \xi , \quad b = \frac {\sqrt {\mathbf {V a r} \eta}}{\sqrt {\mathbf {V a r} \xi}} > 0.
$$

当 r = -1 时, 证明类似.

例 4.3.7 设随机向量  $(\xi,\eta)$  服从二维正态分布  $N(a_{1},a_{2};\sigma_{1}^{2},\sigma_{2}^{2};r)$ . 证明  $\xi,\eta$  有协方差  $r\sigma_{1}\sigma_{2}$  和相关系数 r.

证明 根据假设, 随机向量  $(\xi, \eta)$  的联合分布密度为

$$
\begin{array}{l} p (x, y) = \frac {1}{2 \pi \sigma_ {1} \sigma_ {2} \sqrt {1 - r ^ {2}}} \exp \left\{- \frac {1}{2 (1 - r ^ {2})} \left[ \frac {(x - a _ {1}) ^ {2}}{\sigma_ {1} ^ {2}} - \right. \right. \\ \left. 2 r \frac {(x - a _ {1}) (y - a _ {2})}{\sigma_ {1} \sigma_ {2}} + \frac {(y - a _ {2}) ^ {2}}{\sigma_ {2} ^ {2}} \right] \Bigg \}. \\ \end{array}
$$

所以

$$
\begin{array}{l} \mathbf {C o v} (\xi , \eta) = \int_ {- \infty} ^ {\infty} \int_ {- \infty} ^ {\infty} (x - a _ {1}) (y - a _ {2}) p (x, y) \mathrm{d} x \mathrm{d} y \\ = \frac {\sigma_ {1} \sigma_ {2}}{2 \pi \sqrt {1 - r ^ {2}}} \int_ {- \infty} ^ {\infty} \int_ {- \infty} ^ {\infty} u v \mathrm{e} ^ {- \frac {u ^ {2} - 2 r u v + v ^ {2}}{2 (1 - r ^ {2})}} \mathrm{d} u \mathrm{d} v, \\ \end{array}
$$

其中

$$
u = \frac {x - a _ {1}}{\sigma_ {1}}, v = \frac {y - a _ {2}}{\sigma_ {2}}.
$$

再作变量替换

$$
\left\{ \begin{array}{l l} u = \sqrt {1 - r ^ {2}} s + r t, \\ v = t, \end{array} \right.
$$

相应的雅可比行列式为

$$
J = \left| \begin{array}{c c} \sqrt {1 - r ^ {2}} & r \\ 0 & 1 \end{array} \right| = \sqrt {1 - r ^ {2}}.
$$

继续上面的运算，

$$
\begin{array}{l} \mathbf {C o v} (\xi , \eta) = \frac {\sigma_ {1} \sigma_ {2}}{2 \pi} \int_ {- \infty} ^ {\infty} \int_ {- \infty} ^ {\infty} \left(\sqrt {1 - r ^ {2}} s + r t\right) t \mathrm{e} ^ {- \frac {s ^ {2} + t ^ {2}}{2}} \mathrm{d} s \mathrm{d} t \\ = \frac {\sigma_ {1} \sigma_ {2} r}{2 \pi} \int_ {- \infty} ^ {\infty} \int_ {- \infty} ^ {\infty} \mathrm{e} ^ {- \frac {s ^ {2}}{2}} t ^ {2} \mathrm{e} ^ {- \frac {t ^ {2}}{2}} \mathrm{d} s \mathrm{d} t \\ = \frac {\sigma_ {1} \sigma_ {2} r}{2 \pi} \int_ {- \infty} ^ {\infty} \mathrm{e} ^ {- \frac {s ^ {2}}{2}} \mathrm{d} s \int_ {- \infty} ^ {\infty} t ^ {2} \mathrm{e} ^ {- \frac {t ^ {2}}{2}} \mathrm{d} t = r \sigma_ {1} \sigma_ {2}. \\ \end{array}
$$

所以  $\xi,\eta$  有协方差  $r\sigma_{1}\sigma_{2}$ ，从而它们有相关系数 r.

例4.3.8 设 $(\xi, \eta)$ 服从二维正态分布 $N(a_{1}, a_{2}; \sigma_{1}^{2}, \sigma_{2}^{2}; r)$. 显然 $\mathbf{Cov}(\xi, \eta) = 0$ 当且仅当 $r = 0$. 而此时有

$$
p (x, y) = \frac {1}{2 \pi \sigma_ {1} \sigma_ {2}} \exp \bigg \{- \left[ \frac {(x - a _ {1}) ^ {2}}{\sigma_ {1} ^ {2}} + \frac {(y - a _ {2}) ^ {2}}{\sigma_ {2} ^ {2}} \right] \bigg \},
$$

故 $\xi, \eta$ 独立. 再根据定理3.2.4知 $\xi, \eta$ 独立当且仅当它们不相关.

## 4.3.4 原点矩和中心矩

随机变量的矩是反映其性质的重要数字特征, 前面讨论的数学期望和方差分别属于一阶矩和二阶矩. 本小节对于随机变量的一般的矩进行简单的讨论. 令 $r > 0$. 若概率空间 $(\Omega, \mathcal{F}, \mathbf{P})$ 上的随机变量 $\xi$ 满足 $\mathbf{E}(|\xi|^r) < \infty$, 我们写 $\xi \in L^r$.

定义 4.3.7 对整数 $k \geqslant 1$, 我们称 $m_k := \mathbf{E}(\xi^k)$ 为 $\xi \in L^k$ 的 $k$ 阶原点矩, 而称 $c_k := \mathbf{E}[(\xi - \mathbf{E}\xi)^k]$ 为 $\xi \in L^k$ 的 $k$ 阶中心矩.

利用数学期望的计算公式不难证明:

命题 4.3.10 当  $\mathbf{E}(|\xi|^{k})<\infty$  时, 有

$$
c _ {k} = \sum_ {i = 0} ^ {k} \mathrm{C} _ {k} ^ {i} (- m _ {1}) ^ {k - i} m _ {i}, \qquad m _ {k} = \sum_ {i = 0} ^ {k} \mathrm{C} _ {k} ^ {i} c _ {k - i} m _ {1} ^ {i}.
$$

例 4.3.9 (正态分布随机变量的各阶矩) 设  $\xi$  服从分布  $N(0,1)$ . 则

$$
\int_ {- \infty} ^ {\infty} | x | ^ {n} \frac {1}{\sqrt {2 \pi}} \mathrm{e} ^ {- \frac {x ^ {2}}{2}} \mathrm{d} x <   \infty .
$$

当 $n = 2k - 1$ 为奇数时，显然有 $m_{2k - 1} = 0$ 当 $n = 2k$ 为偶数时，有

$$
\begin{array}{l} m _ {2 k} = \int_ {- \infty} ^ {\infty} | x | ^ {2 k} \frac {1}{\sqrt {2 \pi}} \mathrm{e} ^ {- \frac {x ^ {2}}{2}} \mathrm{d} x = \sqrt {\frac {2}{\pi}} \int_ {0} ^ {\infty} x ^ {2 k} \mathrm{e} ^ {- \frac {x ^ {2}}{2}} \mathrm{d} x \quad (x = \sqrt {2 t}) \\ = \frac {2 ^ {k}}{\sqrt {\pi}} \int_ {0} ^ {\infty} t ^ {k - \frac {1}{2}} \mathrm{e} ^ {- t} \mathrm{d} t = \frac {2 ^ {k}}{\sqrt {\pi}} \Gamma \left(k + \frac {1}{2}\right). \\ \end{array}
$$

由熟知的结果,

$$
\Gamma (\alpha + 1) = \alpha \Gamma (\alpha), \quad \Gamma \Big (\frac {1}{2} \Big) = \sqrt {\pi},
$$

故有

$$
m _ {2 k} = \frac {2 ^ {k}}{\sqrt {\pi}} \left(k - \frac {1}{2}\right) \left(k - \frac {3}{2}\right) \dots \frac {1}{2} \cdot \Gamma \left(\frac {1}{2}\right) = (2 k - 1)!!,
$$

再利用命题 4.3.10 给出的关系即可得到  $\xi$  的所有中心矩.

下面定理的结论称为赫尔德 (Hölder) 不等式, 它是前面证明的柯西-施瓦茨不等式的自然推广.

定理4.3.11 假设 $p, q > 1$ 满足 $1 / p + 1 / q = 1$. 若有 $\xi \in L^p$ 和 $\eta \in L^q$, 则有 $\xi \eta \in L^1$ 且

$$
\mathbf {E} (| \xi \eta |) \leqslant \left[ \mathbf {E} (| \xi | ^ {p}) \right] ^ {1 / p} \left[ \mathbf {E} (| \eta | ^ {q}) \right] ^ {1 / q}.
$$

证明 当 $\mathbf{E}(|\xi \eta|) = 0$ 时, 欲证不等式显然成立. 下面假设 $\mathbf{E}(|\xi \eta|) > 0$, 因而有 $\mathbf{E}(|\xi|) > 0$ 和 $\mathbf{E}(|\eta|) > 0$. 根据对数函数的凹性, 对 $x, y > 0$ 有

$$
\frac {1}{p} \ln x + \frac {1}{q} \ln y \leqslant \ln \left(\frac {x}{p} + \frac {y}{q}\right).
$$

因此易知, 对任何 $x, y \geqslant 0$ 有

$$
x ^ {1 / p} y ^ {1 / q} \leqslant \frac {x}{p} + \frac {y}{q}.
$$

在上式中令 $x = |\xi|^p / \mathbf{E}(|\xi|^p)$ 和 $y = |\eta|^q / \mathbf{E}(|\eta|^q)$，再对所得不等式取期望即得欲证结论. □

推论 4.3.12 对任何随机变量 X, 函数  $r \mapsto [\mathbf{E}(|X|^{r})]^{1/r}$  在  $(0, \infty)$  上不降.

证明 取 $r > q > 0$ 并注意 $q / r + (r - q) / r = 1$. 对 $\xi = |X|^q$ 和 $\eta = 1$ 应用定理4.3.11即知 $[\mathbf{E}(|X|^q)]^{1 / q} \leqslant [\mathbf{E}(|X|^r)]^{1 / r}$.

## 练习题

1. 袋子里有编号为 1 至 $n$ 的卡片 $n$ 张. 从中随机抽取 $k$ 张. 针对以下两种情形求 $k$ 张卡片编号之和 $\xi$ 的期望和方差: (1) 有放回抽取; (2) 无放回抽取 $(m \leqslant n)$.

2. 设绝对连续型平方可积随机变量 $X$ 的密度函数为 $\mathbb{R}$ 上的偶函数. 证明 $X$ 与 $|X|$ 不相关但不独立.

3. 设  $(X,Y)$  的密度函数为

$$
p (x, y) = \left\{ \begin{array}{l l} 1, & 0 <   x <   1, | y | <   x <   1, \\ 0, & \text {其他.} \end{array} \right.
$$

求 $(X,Y)$ 的协方差矩阵.

4. 设随机变量  $\xi_{1}, \xi_{2}, \cdots, \xi_{m+n} (n \geqslant m \geqslant 1)$  是独立同分布随机变量, 且有有限的方差  $\sigma^{2}$ . 求  $X = \xi_{1} + \xi_{2} + \cdots + \xi_{n}$  与  $Y = \xi_{m+1} + \xi_{m+2} + \cdots + \xi_{m+n}$  的协方差和相关系数.

5. 设随机变量 $\xi$ 服从指数分布 $E(\lambda)$. 证明对 $n \geqslant 0$ 有 $\mathbf{E}(\xi^n) = n! / \lambda^n$.

## 4.4 条件期望和预测

## 4.4.1 条件期望的定义和计算

考虑概率空间 $(\Omega, \mathcal{F}, \mathbf{P})$，设事件 $B \in \mathcal{F}$ 满足 $\mathbf{P}(B) > 0$。我们知道，给定事件 $B$ 的条件概率测度 $\mathbf{P}_B := \mathbf{P}(\cdot | B)$ 定义为

$$
\mathbf {P} _ {B} (A) = \mathbf {P} (A | B) = \frac {\mathbf {P} (A B)}{\mathbf {P} (B)}, \quad A \in \mathcal {F}. \tag {4.4.1}
$$

注意 $(\Omega, \mathcal{F}, \mathbf{P}_B)$ 构成一个概率空间, 而原概率空间上的随机变量 $\xi$ 也可视为 $(\Omega, \mathcal{F}, \mathbf{P}_B)$ 上的随机变量.

定义 4.4.1 随机变量  $\xi$  在概率空间  $(\Omega, \mathcal{F}, \mathbf{P}_{B})$  上的数学期望称为它的给定事件 B 的条件期望，并记作  $\mathbf{E}(\xi|B)$ .

显然有 $\mathbf{P}_B(B) = 1$ 和 $\mathbf{P}_B(B^c) = 0$. 我们用 $F_{\xi}(\cdot |B)$ 表示 $\xi$ 作为 $(\Omega, \mathcal{F}, \mathbf{P}_B)$ 上的随机变量的分布函数. 给定 $\mathbb{R}$ 上的博雷尔可测函数, 根据定理4.2.7有

$$
\mathbf {E} [ f (\xi) | B ] = \int_ {- \infty} ^ {\infty} f (x) \mathrm{d} F _ {\xi} (x | B). \tag {4.4.2}
$$

特别地, 若  $\xi$  为取值于可数集  $\{x_{1}, x_{2}, \cdots\} \subseteq R$  的离散型随机变量, 应用命题 4.2.6 得

$$
\mathbf {E} [ f (\xi) | B ] = \sum_ {i = 1} ^ {\infty} f (x _ {i}) \mathbf {P} (\xi = x _ {i} | B). \tag {4.4.3}
$$

定理 4.4.1 设  $(\xi,\eta)$  为取值于  $\{(x_{i},y_{j}):i,j=1,2,\cdots\}$  的离散型随机向量，且有联合分布列

$$
p (x _ {i}, y _ {j}) = \mathbf {P} (\xi = x _ {i}, \eta = y _ {j}), \quad i, j = 1, 2, \dots
$$

及边缘分布列

$$
p _ {\xi} (x _ {i}) = \mathbf {P} (\xi = x _ {i}), p _ {\eta} (y _ {j}) = \mathbf {P} (\eta = y _ {j}), i, j = 1, 2, \dots .
$$

再设 $p_{\eta}(y_j) = \mathbf{P}(\eta = y_j) > 0.$ 则对 $\mathbb{R}^2$ 上的函数 $f$ 有

$$
\mathbf {E} [ f (\xi , \eta) | \eta = y _ {j} ] = \sum_ {i = 1} ^ {\infty} f (x _ {i}, y _ {j}) p _ {\xi} (x _ {i} | \eta = y _ {j}), \tag {4.4.4}
$$

其中 $p_{\xi}(x_i|\eta = y_j) = p(x_i,y_j) / p_\eta (y_j)$ 为条件分布列.

证明 注意, 在条件概率 $\mathbf{P}(\cdot|\eta = y_j)$ 之下有 $f(\xi, \eta) \stackrel{\mathrm{a.s.}}{=} f(\xi, y_j)$. 对于事件 $B = \{\eta = y_j\}$ 和随机变量 $f(\xi, y_j)$ 应用 (4.4.3) 式即得 (4.4.4) 式. □

如果 $\mathbf{P}(B) = 0$ ，我们不能用(4.4.2)式确定相应的条件期望.但是，对于绝对连续型随机向量，类比定理4.4.1的结果，可以借助条件分布密度给出如下的:

定义4.4.2 设 $(\xi, \eta)$ 为绝对连续型随机向量, 且有联合分布密度 $p$ 及边缘分布密度 $p_{\xi}$ 和 $p_{\eta}$. 再设 $p_{\eta}(y) > 0$. 对于 $\mathbb{R}^2$ 上的可测函数 $f$ 我们定义给定 $\eta = y$ 时 $f(\xi, \eta)$ 的条件期望为

$$
\mathbf {E} [ f (\xi , \eta) | \eta = y ] = \int_ {- \infty} ^ {\infty} f (x, y) p _ {\xi} (x | \eta = y) \mathrm{d} x, \tag {4.4.5}
$$

其中 $p_{\xi}(x|\eta = y) = p(x,y) / p_{\eta}(y)$ 为条件分布密度.

定义 4.4.3 对于离散型或绝对连续型随机变向量  $(\xi,\eta)$ ，若  $p_{\eta}(y)>0$ ，我们称

$$
\mathbf {V a r} (\xi | \eta = y) := \mathbf {E} \big \{[ \xi - \mathbf {E} (\xi | \eta = y) ] ^ {2} | \eta = y \big \}
$$

为给定  $\eta = y$  时  $\xi$  的条件方差.

例 4.4.1 设随机向量  $(\xi, \eta)$  服从单位圆盘上的二维均匀分布. 根据例 3.2.1, 对于  $|y| < 1$  有

$$
p _ {\xi} (x | \eta = y) = \frac {1}{2 \sqrt {1 - y ^ {2}}}, \quad | x | <   \sqrt {1 - y ^ {2}}.
$$

故有

$$
\mathbf {E} (\xi | \eta = y) = \int_ {- \sqrt {1 - y ^ {2}}} ^ {\sqrt {1 - y ^ {2}}} \frac {x \mathrm{d} x}{2 \sqrt {1 - y ^ {2}}} = 0
$$

和

$$
\mathbf {V a r} (\xi | \eta = y) = \mathbf {E} (\xi^ {2} | \eta = y) = \int_ {- \sqrt {1 - y ^ {2}}} ^ {\sqrt {1 - y ^ {2}}} \frac {x ^ {2} \mathrm{d} x}{2 \sqrt {1 - y ^ {2}}} = \frac {1 - y ^ {2}}{3}.
$$

例4.4.2 设 $(\xi, \eta)$ 服从二维正态分布 $N(a_{1}, a_{2}; \sigma_{1}^{2}, \sigma_{2}^{2}; r)$. 根据例3.2.2, 给定 $\eta = y$ 时 $\xi$ 服从条件分布

$$
N (a _ {1} + r \sigma_ {1} (y - a _ {2}) / \sigma_ {2}, \sigma_ {1} ^ {2} (1 - r ^ {2})).
$$

据此立知

$$
\mathbf {E} (\xi | \eta = y) = a _ {1} + r \sigma_ {1} (y - a _ {2}) / \sigma_ {2}
$$

和

$$
\mathbf {V a r} (\xi | \eta = y) = \sigma_ {1} ^ {2} (1 - r ^ {2}).
$$

## 4.4.2 全期望公式及应用

定理4.4.2（全期望公式） 假定数学期望 $\mathbf{E}f(\xi)$ 存在. 则对 $\Omega$ 的可数划分 $\{B_n\} \subseteq \mathcal{F}$ 有

$$
\mathbf {E} f (\xi) = \sum_ {n = 1} ^ {\infty} \mathbf {P} (B _ {n}) \mathbf {E} [ f (\xi) | B _ {n} ]. \tag {4.4.6}
$$

证明 根据全概率公式, 对于任何 $x \in \mathbb{R}$ 有

$$
F _ {\xi} (x) = \sum_ {n = 1} ^ {\infty} \mathbf {P} (B _ {n}) F _ {\xi} (x | B _ {n}).
$$

根据斯蒂尔切斯积分的性质不难证明

$$
\int_ {- \infty} ^ {\infty} f (x) \mathrm{d} F _ {\xi} (x) = \sum_ {n = 1} ^ {\infty} \mathbf {P} (B _ {n}) \int_ {- \infty} ^ {\infty} f (x) \mathrm{d} F _ {\xi} (x | B _ {n}).
$$

该等式意味着只要等号一边正、负部之一有限则另一边也如此且两边相等.所以等式(4.4.6)式成立. □

与全概率公式类似, 当 $\mathbf{P}(B_i) = 0$ 时我们规定 $\mathbf{P}(B_i)\mathbf{E}[f(\xi)|B_i] = 0$, 故在全期望公式 (4.4.6) 式中并不需假定 $\mathbf{P}(B_i) > 0$. 全期望公式经常被用来计算形如 $\mathbf{E}f(\xi)$ 的数学期望. 下面是一个典型的例子.

例 4.4.3 设  $\{\xi_{i}\}$  为独立同分布可积随机变量序列, 而  $\eta$  为与  $\{\xi_{i}\}$  独立的非负整数值可积随机变量. 则有 (规定  $\sum_{i=1}^{0}=0$ )

$$
\mathbf {E} \left(\sum_ {i = 1} ^ {\eta} \xi_ {i}\right) = \mathbf {E} \eta \mathbf {E} \xi_ {1}. \tag {4.4.7}
$$

事实上, 因为 $\eta$ 与 $\{\xi_i\}$ 独立, 在给定 $B_k := \{\eta = k\}$ 的条件下 $\{\xi_i\}$ 仍为独立同分布随机变量序列, 且分布保持不变 (请读者自行证明). 故对于 $k \geqslant 0$ 有

$$
\mathbf {E} \left(\sum_ {i = 1} ^ {\eta} \xi_ {i} \Big | \eta = k\right) = \mathbf {E} \left(\sum_ {i = 1} ^ {k} \xi_ {i} \Big | \eta = k\right) = \mathbf {E} \left(\sum_ {i = 1} ^ {k} \xi_ {i}\right) = k \mathbf {E} \xi_ {1}.
$$

再由全期望公式得

$$
\begin{array}{l} \mathbf {E} \left(\sum_ {i = 1} ^ {\eta} \xi_ {i}\right) = \sum_ {k = 0} ^ {\infty} \mathbf {P} (\eta = k) \mathbf {E} \left(\sum_ {i = 1} ^ {\eta} \xi_ {i} \Big | \eta = k\right) \\ = \sum_ {k = 1} ^ {\infty} \mathbf {P} (\eta = k) k \mathbf {E} \xi_ {1} = \mathbf {E} \eta \mathbf {E} \xi_ {1}. \\ \end{array}
$$

## 4.4.3 给定随机变量的条件期望

定义 4.4.4 设  $(\xi,\eta)$  是具有联合分布密度 p 的离散型或绝对连续型随机向量. 分别用  $p_{\xi}$  和  $p_{\eta}$  表示  $\xi$  和  $\eta$  的边缘分布密度, 并记

$$
U = \{x \in \mathbb {R}: p _ {\xi} (x) > 0 \}, \quad V = \{y \in \mathbb {R}: p _ {\eta} (y) > 0 \}. \tag {4.4.8}
$$

注意, 在离散或绝对连续两种情况下都有 $\mathbf{P}(\xi \in U) = 1$ 和 $\mathbf{P}(\eta \in V) = 1$. 给定 $\mathbb{R}^2$ 上的可测函数 $f$, 令

$$
h (y) = 1 _ {V} (y) \mathbf {E} [ f (\xi , \eta) | \eta = y ] = 1 _ {V} (y) \mathbf {E} [ f (\xi , y) | \eta = y ], \tag {4.4.9}
$$

其中的条件期望由(4.4.4)式或(4.4.5)式定义. 我们称 $h(\eta)$ 为给定 $\eta$ 时随机变量 $f(\xi, \eta)$ 的条件期望, 并记作 $\mathbf{E}[f(\xi, \eta)|\eta]$. 类似地, 可以定义 $\mathbf{E}[f(\xi, \eta)|\xi]$.

可以证明, 由 (4.4.9) 式定义的 $h$ 是 $\mathbb{R}$ 上的可测函数, 故 $\mathbf{E}[f(\xi, \eta)|\eta]$ 是关于 $\sigma$ 代数 $\sigma(\eta)$ 可测的随机变量. 类似地可知 $\mathbf{E}[f(\xi, \eta)|\xi]$ 是关于 $\sigma$ 代数 $\sigma(\xi)$ 可测的随机变量.

例 4.4.4 设  $\eta$  服从泊松分布  $P(\lambda)$ ，而  $\xi$  是成功概率为 p (0 < p < 1) 的  $\eta$  重伯努利试验的成功次数。于是在给定  $\eta$  的条件下  $\xi$  服从二项分布  $B(\eta, p)$ 。因此有  $\mathbf{E}(\xi | \eta) = \eta p$  和

$$
\mathbf {E} \xi = \mathbf {E} (\eta p) = p \mathbf {E} \eta = p \lambda .
$$

上式可认为是例 4.4.3 中结果的特殊情况.

例 4.4.5 设  $(\xi,\eta)$  是概率空间  $(\Omega,\mathcal{F},\mathbf{P})$  上的取值于  $\{(x_{i},y_{j}):i,j=1,2,\cdots\}$  的离散型随机向量. 令 V 由 (4.4.8) 式定义. 不妨设  $V=\{y_{j}:j=1,2,\cdots\}$ . 注意  $\eta$  所生成的  $\sigma$  代数  $\sigma(\eta)$  是形如  $B_{j}=\{\eta=y_{j}\}\in\mathcal{F}, j=1,2,\cdots$  的事件的所有可能的并集构成的集类 (规定零个集合的并为空集). 设对每个  $y_{j}\in V$ , 在给定  $\eta=y_{j}$  条件下  $\xi$  可积, 并记

$$
h (y _ {j}) = 1 _ {V} (y _ {j}) \mathbf {E} (\xi | \eta = y _ {j}) = 1 _ {V} (y _ {j}) \mathbf {E} (\xi | B _ {j}).
$$

若 $\omega \in B_{j}$ ，则 $\eta (\omega) = y_{j}$ ，因而

$$
\mathbf {E} (\xi | \eta) (\omega) = h (\eta (\omega)) = h (y _ {j}) = \mathbf {E} (\xi | \eta = y _ {j}) = \mathbf {E} (\xi | B _ {j}).
$$

所以有

$$
\mathbf {E} (\xi | \eta) = \sum_ {j = 1} ^ {\infty} 1 _ {\{\eta = y _ {j} \}} \mathbf {E} (\xi | \eta = y _ {j}) = \sum_ {j = 1} ^ {\infty} 1 _ {B _ {j}} \mathbf {E} (\xi | B _ {j}).
$$

这说明随机变量 $\mathbf{E}(\xi|\eta)$ 至多取可数个不同的值, 且在事件 $B_{j} = \{\eta = y_{j}\} \in \mathcal{F}$ 上的取值为 $\mathbf{E}(\xi|B_{j}) = \mathbf{E}(\xi|\eta = y_{j})$, 而后者为经典意义下的条件期望.

例 4.4.6 设随机向量  $(\xi,\eta)$  服从区域  $D:=\{(x,y):x,y>0,x+y<1\}$  上的均匀分布, 即其联合分布密度为

$$
p (x, y) = 2, \quad (x, y) \in D.
$$

则 $\eta$ 的边缘分布密度为

$$
p _ {\eta} (y) = 2 \int_ {0} ^ {1 - y} \mathrm{d} x = 2 (1 - y), \quad 0 <   y <   1.
$$

所以

$$
p _ {\xi} (x | \eta = y) = \frac {1}{1 - y}, \quad 0 <   x <   1 - y.
$$

可见给定 $\eta = y$ 时 $\xi$ 的条件分布是 $(0,1 - y)$ 上的均匀分布，因而有

$$
\mathbf {E} (\xi | \eta = y) = \frac {1}{1 - y} \int_ {0} ^ {1 - y} x \mathrm{d} x = \frac {1 - y}{2}.
$$

所以  $\mathbf{E}(\xi|\eta)=(1-\eta)/2.$

定理4.4.3 设 $(\xi, \eta)$ 为离散型或绝对连续型随机向量，而 $f$ 为 $\mathbb{R}$ 上的可测函数且 $f(\xi)$ 可积。若 $\xi$ 和 $\eta$ 独立，则几乎必然有

$$
\mathbf {E} [ f (\xi) | \eta ] = \mathbf {E} [ f (\xi) ]. \tag {4.4.10}
$$

证明 因为 $\xi$ 和 $\eta$ 独立, 根据定理 3.2.3 和定理 3.2.4 可取 $p(x,y) := p_{\xi}(x)p_{\eta}(y)$ 为 $(\xi, \eta)$ 的联合分布密度. 于是对 $y \in V$ 有 $p_{\xi}(\cdot|\eta = y) = p_{\xi}(\cdot)$. 由 (4.4.4) 式和 (4.4.5) 式, 在两种情况下对 $y \in V$ 都有

$$
\mathbf {E} [ f (\xi) | \eta = y ] = \mathbf {E} [ f (\xi) ].
$$

再因 $\mathbf{P}(\eta \in V) = 1$ ，由定义4.4.4即知(4.4.10)式成立.

## 4.4.4 条件期望的平滑性质

对于离散型随机向量的函数的数学期望, 作为全期望公式的特殊情况, 我们有

定理 4.4.4 设  $(\xi,\eta)$  为取值于  $\{(x_{i},y_{j}):i,j=1,2,\cdots\}$  的离散型随机向量，且有边缘分布密度  $p_{\xi}(x_{i})$  和  $p_{\eta}(y_{j})$ . 再设  $f(\xi,\eta)$  可积. 则

$$
\mathbf {E} [ f (\xi , \eta) ] = \sum_ {j = 1} ^ {\infty} \mathbf {E} [ f (\xi , \eta) | \eta = y _ {j} ] p _ {\eta} (y _ {j}).
$$

对于绝对连续型随机向量的函数的数学期望,与上面结果类似地有

定理4.4.5 假设 $(\xi, \eta)$ 服从绝对连续型分布，且有边缘分布密度 $p_{\xi}(x)$ 和 $p_{\eta}(y)$. 再设 $f$ 为 $\mathbb{R}^2$ 上的可测函数且 $f(\xi, \eta)$ 可积. 则

$$
\mathbf {E} [ f (\xi , \eta) ] = \int_ {- \infty} ^ {\infty} \mathbf {E} [ f (\xi , y) | \eta = y ] p _ {\eta} (y) \mathrm{d} y.
$$

证明 设 $(\xi, \eta)$ 有联合分布密度 $p(x, y)$ 和边缘分布密度 $p_{\xi}(x), p_{\eta}(y)$. 根据条件分布密度的定义有 $p(x, y) = p_{\eta}(y)p_{\xi}(x|\eta = y)$. 于是有

$$
\begin{array}{l} \mathbf {E} [ f (\xi , \eta) ] = \int_ {- \infty} ^ {\infty} \int_ {- \infty} ^ {\infty} f (x, y) p (x, y) \mathrm{d} x \mathrm{d} y \\ = \int_ {- \infty} ^ {\infty} p _ {\eta} (y) \mathrm{d} y \int_ {- \infty} ^ {\infty} f (x, y) p _ {\xi} (x | \eta = y) \mathrm{d} x. \\ \end{array}
$$

再由 (4.4.5) 式即得欲证者.

定理 4.4.6（条件期望的平滑性） 假设  $(\xi,\eta)$  为离散型或绝对连续型随机向量. 再设 f 为  $R^{2}$  上的可测函数且  $f(\xi,\eta)$  可积. 则

$$
\mathbf {E} \{\mathbf {E} [ f (\xi , \eta) | \eta ] \} = \mathbf {E} [ f (\xi , \eta) ].
$$

证明 两种情况的证明类似. 这里只考虑 $(\xi, \eta)$ 服从绝对连续型分布的情况. 令 $h(y)$ 由 (4.4.9) 式定义. 应用定理 4.4.5 有

$$
\mathbf {E} [ f (\xi , \eta) ] = \int_ {- \infty} ^ {\infty} \mathbf {E} [ f (\xi , \eta) | \eta = y ] p _ {\eta} (y) \mathrm{d} y = \int_ {- \infty} ^ {\infty} h (y) p _ {\eta} (y) \mathrm{d} y = \mathbf {E} [ h (\eta) ].
$$

故得欲证结果.

定理 4.4.6 给出的平滑性是条件期望的一个基本性质, 可认为是例 4.4.4 中结果的一般化. 该定理的证明主要基于定理 4.4.4 和定理 4.4.5 给出的全期望公式. 因此我们可以认为该平滑性实质上是全期望公式的另外一种表达形式.

例 4.4.7 设  $\eta$  服从指数分布  $E(\lambda)$ ，而在给定  $\eta$  的条件下  $\xi$  服从均匀分布  $U(0,\eta)$ ，下面求  $\mathbf{E}(\xi|\eta)$  和  $E\xi$ 。根据题意，有  $p_{\xi}(x|\eta=y)=y^{-1}1_{\{0<x<y\}}$ ，故

$$
\mathbf {E} (\xi | \eta = y) = \frac {1}{y} \int_ {0} ^ {y} x \mathrm{d} x = \frac {y}{2}.
$$

根据定理4.4.5有

$$
\mathbf {E} \xi = \lambda \int_ {0} ^ {\infty} \mathbf {E} (\xi | \eta = y) \mathrm{e} ^ {- \lambda y} \mathrm{d} y = \frac {\lambda}{2} \int_ {0} ^ {\infty} y \mathrm{e} ^ {- \lambda y} \mathrm{d} y = \frac {1}{2 \lambda}.
$$

该结果也可以利用条件期望的平滑性得到

$$
\mathbf {E} \xi = \mathbf {E} [ \mathbf {E} (\xi | \eta) ] = \mathbf {E} \Big (\frac {\eta}{2} \Big) = \frac {1}{2 \lambda}.
$$

定理4.4.7 设 $(\xi, \eta)$ 为离散型或绝对连续型随机向量，而 $g$ 为博雷尔可测函数。令 $V$ 由(4.4.8)式定义。再设 $f$ 为 $\mathbb{R}^2$ 上的可测函数，且对任何 $y \in V$ ，在给定 $\eta = y$ 条件下 $f(\xi, \eta)$ 和 $g(y)f(\xi, \eta)$ 均可积。则

$$
\mathbf {E} [ g (\eta) f (\xi , \eta) | \eta ] = g (\eta) \mathbf {E} [ f (\xi , \eta) | \eta ].
$$

证明 定义 $h(y) = 1_V(y)\mathbf{E}[f(\xi, \eta)|\eta = y]$ 和 $H(y) = 1_V(y)\mathbf{E}[g(\eta)f(\xi, \eta)|\eta = y]$. 注意对 $y \in V$ 有

$$
H (y) = \mathbf {E} [ g (y) f (\xi , \eta) | \eta = y ] = g (y) \mathbf {E} [ f (\xi , \eta) | \eta = y ] = g (y) h (y).
$$

所以

$$
\mathbf {E} [ g (\eta) f (\xi , \eta) | \eta ] = H (\eta) = g (\eta) h (\eta) = g (\eta) \mathbf {E} [ f (\xi , \eta) | \eta ].
$$

故得欲证结果.

推论 4.4.8 设  $(\xi,\eta)$  为离散型或绝对连续型随机向量, 而 g 为博雷尔可测函数. 再设对任何  $y \in V$ , 在给定  $\eta = y$  条件下  $f(\xi,\eta)$  和  $g(\eta)f(\xi,\eta)$  均可积. 则

$$
\mathbf {E} [ g (\eta) f (\xi , \eta) ] = \mathbf {E} \big \{g (\eta) \mathbf {E} [ f (\xi , \eta) | \eta ] \big \}.
$$

推论4.4.9 设 $(\xi, \eta)$ 为离散型或绝对连续型随机向量. 再设对任何 $y \in V$, 在给定 $\eta = y$ 条件下 $f(\xi, \eta)$ 可积. 则对任何 $B \in \sigma(\eta)$ 有

$$
\mathbf {E} [ 1 _ {B} f (\xi , \eta) ] = \mathbf {E} \big \{1 _ {B} \mathbf {E} [ f (\xi , \eta) | \eta ] \big \}.
$$

证明 注意, 存在 $C \in \mathcal{B}$ 使得 $B = \eta^{-1}(C)$, 故 $1_B = 1_C(\eta)$. 再由推论4.4.8即得欲证结果. □

显然, 推论 4.4.8 和推论 4.4.9 都加强了定理 4.4.6 中给出的条件期望的平滑性质.

例 4.4.8 设  $\eta$  服从泊松分布  $P(\lambda)$ ，而  $\xi$  为伯努利试验  $B(p,\eta)$  的成功次数。根据定理 4.4.7 和例 4.3.1 的结论有

$$
\mathbf {E} (\xi \eta) = \mathbf {E} [ \mathbf {E} (\xi \eta | \eta) ] = \mathbf {E} [ \eta \mathbf {E} (\xi | \eta) ] = p \mathbf {E} (\eta^ {2}) = p \lambda (1 + \lambda).
$$

本节的讨论可以容易地推广到  $\eta$  是多维随机向量的情况.

## \*4.4.5 条件期望的最优预测性

定理4.4.10 设 $(\xi, \eta)$ 为平方可积的离散型或绝对连续型随机向量. 取 $\mathbb{R}$ 上的可测函数 $f$, 并以形如 $f(\eta)$ 的随机变量作为 $\xi$ 的估计. 则使 $\mathbf{E}\{[\xi - f(\eta)]^2\}$ 达最小的估计为 $f(\eta) = \mathbf{E}(\xi|\eta)$.

证明 以绝对连续型分布情况为例. 根据定理4.4.6, 我们有

$$
\begin{array}{l} \mathbf {E} \big \{[ \xi - f (\eta) ] ^ {2} \big \} = \mathbf {E} \big \{\mathbf {E} \big [ (\xi - f (\eta)) ^ {2} | \eta \big ] \big \} \\ = \int_ {- \infty} ^ {\infty} \mathbf {E} \big [ (\xi - f (y)) ^ {2} | \eta = y \big ] p _ {\eta} (y) \mathrm{d} y. \\ \end{array}
$$

再由命题4.3.3知，当 $f(y) = \mathbf{E}(\xi |\eta = y)$ 时 $\mathbf{E}[(\xi -f(y))^2 |\eta = y]$ 达最小.因此定理结论成立. □

基于上面定理, 我们可以把 $f(\eta) = \mathbf{E}(\xi|\eta)$ 作为在已知 $\eta$ 的情况下对于随机变量 $\xi$ 的最优预测.

例4.4.9 设 $(\xi, \eta)$ 服从二维正态分布 $N(a_{1}, a_{2}; \sigma_{1}^{2}, \sigma_{2}^{2}; r)$. 根据例4.4.2的结果知 $f(\eta) = a_{1} + r\sigma_{1}(\eta - a_{2}) / \sigma_{2}$ 是对 $\xi$ 的最优预测. 所以正态情形的最优预测是线性的.

## 练习题

1. 设随机向量 $(\xi, \eta)$ 服从区域 $G := \{(x, y) : x, y > 0, x + y^2 < 1\}$ 上的均匀分布. 求条件期望 $\mathbf{E}(\xi|\eta)$.
2. 设  $(\xi,\eta)$  为概率空间  $(\Omega,\mathcal{F},\mathbf{P})$  上的随机向量, 其中  $\eta$  为取值于可数集  $V:=\{y_{j}:j=1,2,\cdots\}$  的离散型随机变量且有分布列  $p_{\eta}(y_{j})=\mathbf{P}(\eta=y_{j})$ . 再设存在  $R\times V$  上的严格正可积函数  $p(x,y_{j})$  使得

$$
\mathbf {P} (a \leqslant \xi \leqslant b, \eta = y _ {j}) = \int_ {a} ^ {b} p (x, y _ {j}) \mathrm{d} x, \quad a \leqslant b \in \mathbb {R}.
$$

(1) 证明 $\xi$ 为绝对连续型随机变量, 并求出它的密度函数 $p_{\xi}(x)$.
(2) 求  $\xi$  的条件分布函数  $F_{\xi}(x|\eta = y_{j})$  和条件密度函数  $p_{\xi}(x|\eta = y_{j})$ .
(3) 令 $f$ 为 $\mathbb{R}$ 上的有界连续函数. 求 $f(\xi)$ 条件期望 $h(y_j) := \mathbf{E}[f(\xi) | \eta = y_j]$.
(4) 记  $\mathbf{E}[f(\xi)|\eta]=h(\eta)$ . 证明  $\mathbf{E}\{\mathbf{E}[f(\xi)|\eta]\}=\mathbf{E}[f(\xi)]$ .

3. 设 $\eta$ 服从泊松分布 $P(\lambda)$, 而在给定 $\eta$ 的条件下 $\xi$ 服从均匀分布 $U(0, \eta)$. 求 $\mathbf{E}(\xi|\eta)$ 和 $\mathbf{E}\xi$.
4. 设 $\{\xi_i\}$ 为独立同分布可积随机变量列, 而 $\eta$ 为与 $\{\xi_i\}$ 独立的非负整数值可积随机变量. 再设 $\{\xi_i\}$ 和 $\eta$ 都是平方可积随机变量. 证明:

$$
\mathrm{Var} \Big (\sum_ {k = 1} ^ {\eta} \xi_ {k} \Big) = \mathbf {E} \eta \mathrm{Var} \xi_ {1} + \mathrm{Var} \eta (\mathbf {E} \xi_ {1}) ^ {2}.
$$

## 4.5 随机变量的母函数

取非负整数值的随机变量在概率论中占有重要的位置. 我们前面讨论的二项分布、几何分布、帕斯卡分布和泊松分布都属于这种类型. 对于这类随机变量, 母函数是重要的研究工具. 随机变量的母函数与其分布列相互唯一决定, 可以认为是分布列或分布函数的一种变换, 还是后面将要系统讨论的特征函数的先导.

## 4.5.1 母函数的定义

定义 4.5.1 给定数列  $\{a(i): i=0,1,2,\cdots\}\subseteq[0,1]$ ，我们称幂级数

$$
f (s) := \sum_ {i = 0} ^ {\infty} a (i) s ^ {i} \tag {4.5.1}
$$

为其母函数. 显然, 上面级数至少在区间 $[-1, 1]$ 上绝对收敛且一致收敛. 若 $\{p(i)\}$ 为非负整数值随机变量 $\xi$ 的分布列, 我们也称 $\{p(i)\}$ 的母函数 $g$ 为 $\xi$ 的母函数, 注意此时 $g(s) = \mathbf{E}(s^{\xi})$.

定理 4.5.1（唯一性） 数列  $\{a(i): i=0,1,2,\cdots\}\subseteq[0,1]$  与其母函数 f 相互唯一决定.

证明 显然母函数 $f$ 由数列 $\{a(i)\}$ 唯一决定. 另一方面, 对 (4.5.1) 式两端求导数, 当 $|s| < 1$ 时有

$$
f ^ {(k)} (s) = \sum_ {i = k} ^ {\infty} i (i - 1) \dots (i - k + 1) a (i) s ^ {i - k}.
$$

于是

$$
a (k) = \frac {1}{k !} f ^ {(k)} (0), \quad k = 0, 1, 2, \dots . \tag {4.5.2}
$$

所以数列  $\{a(i)\}$  也由母函数 f 唯一决定.

定理4.5.2 假设 $\xi$ 是以 $g$ 为母函数的非负整数值随机变量，则

$$
\mathbf {E} \xi = g ^ {\prime} (1 -), \quad \mathbf {E} (\xi^ {2}) = g ^ {\prime \prime} (1 -) + g ^ {\prime} (1 -).
$$

证明 对母函数的定义式逐项求导, 当  $|s| < 1$  时有

$$
g ^ {\prime} (s) = \sum_ {i = 1} ^ {\infty} i s ^ {i - 1} p (i), \quad g ^ {\prime \prime} (s) = \sum_ {i = 2} ^ {\infty} i (i - 1) s ^ {i - 2} p (i).
$$

令 $s \uparrow 1$ 得

$$
g ^ {\prime} (1 -) = \sum_ {i = 1} ^ {\infty} i p (i) = \mathbf {E} \xi
$$

和

$$
g ^ {\prime \prime} (1 -) = \sum_ {i = 1} ^ {\infty} i (i - 1) p (i).
$$

所以有

$$
g ^ {\prime \prime} (1 -) + g ^ {\prime} (1 -) = \sum_ {i = 1} ^ {\infty} i ^ {2} p (i) = \mathbf {E} (\xi^ {2}).
$$

故得欲证结果.

例4.5.1 二项分布 $B(n,p)$ 的母函数为 $(q = 1 - p)$

$$
g (s) = \sum_ {i = 0} ^ {n} \mathrm{C} _ {n} ^ {i} q ^ {n - i} p ^ {i} s ^ {i} = (q + p s) ^ {n}.
$$

其收敛域为 $(-∞,∞)$ .

例4.5.2 几何分布 $G(p)$ 的母函数为 $(q = 1 - p)$

$$
g (s) = \sum_ {i = 1} ^ {\infty} q ^ {i - 1} p s ^ {i} = p s \sum_ {i = 1} ^ {\infty} (q s) ^ {i - 1} = \frac {p s}{1 - q s}.
$$

其收敛域为 $(-1/q,1/q)$ .

例 4.5.3 根据泰勒展开式, 对  $|x| < 1$  有

$$
\begin{array}{l} (1 - x) ^ {- n} = \sum_ {k = 0} ^ {\infty} \frac {n (n + 1) \cdots (n + k - 1)}{k !} x ^ {k} \\ = \sum_ {k = 0} ^ {\infty} \mathrm{C} _ {n + k - 1} ^ {n - 1} x ^ {k} = \sum_ {k = n} ^ {\infty} \mathrm{C} _ {k - 1} ^ {n - 1} x ^ {k - n}. \\ \end{array}
$$

所以帕斯卡分布 $Pa(n,p)$ 的母函数为 $(q = 1 - p)$

$$
\sum_ {k = n} ^ {\infty} \mathrm{C} _ {k - 1} ^ {n - 1} p ^ {n} q ^ {k - n} s ^ {k} = (p s) ^ {n} \sum_ {k = n} ^ {\infty} \mathrm{C} _ {k - 1} ^ {n - 1} (q s) ^ {k - n} = \left(\frac {p s}{1 - q s}\right) ^ {n}.
$$

其收敛域为 $(-1/q,1/q)$ .

例4.5.4 泊松分布 $P(\lambda)$ 的母函数为

$$
g (s) = \sum_ {i = 0} ^ {\infty} \mathrm{e} ^ {- \lambda} \frac {\lambda^ {i}}{i !} s ^ {i} = \mathrm{e} ^ {- \lambda} \mathrm{e} ^ {\lambda s} = \mathrm{e} ^ {\lambda (s - 1)}.
$$

其收敛域为 $(-∞,∞)$ .