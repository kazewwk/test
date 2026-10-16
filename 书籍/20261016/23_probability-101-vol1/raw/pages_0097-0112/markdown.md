所以

$$
\begin{array}{l} \mathbf {P} (X = - 1) = \sum_ {n = 0} ^ {\infty} \mathbf {P} (\eta = 2 n + 1) = \sum_ {n = 0} ^ {\infty} (1 - p) ^ {2 n} p \\ = \frac {p}{1 - (1 - p) ^ {2}} = \frac {1}{2 - p}, \\ \end{array}
$$

进而

$$
\mathbf {P} (X = 1) = \frac {1 - p}{2 - p}.
$$

例3.3.2 设 $\xi$ 服从均匀分布 $U(-\pi / 2, \pi / 2)$. 求 $\eta = \tan \xi$ 的分布.

解 因为 $\xi$ 有密度函数 $q(x) = 1 / \pi, |x| < \pi / 2$, 对于 $y \in \mathbb{R}$ 有

$$
\begin{array}{l} F _ {\eta} (y) = \mathbf {P} (\tan \xi \leqslant y) \\ = \mathbf {P} (\xi \leqslant \arctan y, | \xi | <   \pi / 2) \\ = \int_ {- \frac {\pi}{2}} ^ {\arctan y} \frac {1}{\pi} \mathrm{d} x = \left. \frac {1}{\pi} x \right| _ {- \frac {\pi}{2}} ^ {\arctan y} \\ = \frac {1}{\pi} \arctan y + \frac {1}{2} \\ \end{array}
$$

求导得 $\eta$ 的密度函数为

$$
p (y) = \frac {1}{\pi (1 + y ^ {2})}, \quad y \in \mathbb {R}.
$$

直线上的绝对连续型概率分布称为具有参数 $a \in \mathbb{R}$ 和 $\lambda > 0$ 的柯西 (Cauchy) 分布, 是指它有密度函数

$$
p (x) = \frac {1}{\pi [ \lambda^ {2} + (x - a) ^ {2} ]}, \quad x \in \mathbb {R}.
$$

所以例 3.3.2 中得到的分布是柯西分布当 a = 0,  $\lambda = 1$  时的特殊形式.

注意, 例 3.3.2 的计算中用到了函数 $y = \tan x$ 在 $(- \pi / 2, \pi / 2)$ 内的严格单增性质. 在这种情况下, 有 $\tan \xi \leqslant y$ 当且仅当 $\xi \leqslant \arctan y$, $|\xi| < \pi / 2$.

定理3.3.1 设区间 $(a, b)$ 上的绝对连续型随机变量 $\xi$ 有密度函数 $p$, 而函数 $f$ 在 $(a, b)$ 上可导且单调. 令 $\alpha = f(a) \wedge f(b)$ 和 $\beta = f(a) \vee f(b)$. 再令 $h: (\alpha, \beta) \to (a, b)$ 为 $f$ 的反函数. 则 $\eta := f(\xi)$ 为区间 $(\alpha, \beta)$ 上的绝对连续型随机变量且有密度函数

$$
p _ {\eta} (y) = p (h (y)) | h ^ {\prime} (y) |, \quad y \in (\alpha , \beta).
$$

证明 不妨设函数 $f$ 在 $(a, b)$ 上不降. 则 $\eta$ 有分布函数

$$
F _ {\eta} (y) = \mathbf {P} (f (\xi) \leqslant y) = \int_ {\{\alpha <   f (x) \leqslant y \}} p (x) \mathrm{d} x, \quad y \in (\alpha , \beta).
$$

注意 $\alpha = f(a)$. 令 $x = h(t)$, 利用换元法计算积分得

$$
F _ {\eta} (y) = \int_ {\alpha} ^ {y} p (h (t)) h ^ {\prime} (t) \mathrm{d} t.
$$

对上式求导即得  $\eta$  的密度函数  $p_{\eta}$  的表达式.

上面定理的证明包含了求解绝对连续型随机变量函数密度方法的基本思想. 在实际问题中, 往往需要根据具体情况灵活运用.

例3.3.3 设 $\xi$ 服从正态分布 $N(0,1)$. 求 $\eta = \xi^2$ 的分布.

解 显然, 可以认为 $\eta = \xi^2$ 以概率 1 取值于开区间 $(0, \infty)$. 对 $y > 0$ 有

$$
F (y) = \mathbf {P} (| \xi | \leqslant \sqrt {y}) = \int_ {- \sqrt {y}} ^ {\sqrt {y}} \frac {1}{\sqrt {2 \pi}} \mathrm{e} ^ {- \frac {x ^ {2}}{2}} \mathrm{d} x = \sqrt {2} \int_ {0} ^ {\sqrt {y}} \frac {1}{\sqrt {\pi}} \mathrm{e} ^ {- \frac {x ^ {2}}{2}} \mathrm{d} x.
$$

求导得 $\eta$ 的密度函数

$$
p (y) = \frac {1}{\sqrt {2 \pi y}} \mathrm{e} ^ {- \frac {y}{2}}, \quad y > 0.
$$

半直线 $(0,\infty)$ 上的绝对连续型分布称为卡方分布, 并记作 $\chi^2 (n)$, 是指它有密度函数

$$
p _ {n} (y) = \frac {1}{2 ^ {\frac {n}{2}} \Gamma \left(\frac {n}{2}\right)} y ^ {\frac {n}{2} - 1} \mathrm{e} ^ {- \frac {y}{2}}, \quad y > 0.
$$

参数 $n$ 称为 $\chi^2 (n)$ 的自由度. 注意 $\chi^2 (n)$ 就是伽马分布 $\Gamma(1 / 2, n / 2)$. 例3.3.3中得到的分布就是自由度为1的卡方分布.

定理3.3.2 设随机变量 $\xi$ 和 $\eta$ 独立. 则对任何博雷尔可测函数 $f$ 和 $g$, 随机变量 $f(\xi)$ 和 $g(\eta)$ 也相互独立.

证明 因为 $f, g$ 是博雷尔可测函数, 由定理2.1.8知 $f(\xi), g(\eta)$ 都是随机变量. 对任意的 $A, B \in \mathcal{B}$ 有 $f^{-1}(A), g^{-1}(B) \in \mathcal{B}$. 故由 $\xi$ 和 $\eta$ 的独立性,

$$
\begin{array}{l} \mathbf {P} \{f (\xi) \in A, g (\eta) \in B \} = \mathbf {P} \{\xi \in f ^ {- 1} (A), \eta \in g ^ {- 1} (B) \} \\ = \mathbf {P} \{\xi \in f ^ {- 1} (A) \} \mathbf {P} (\eta \in g ^ {- 1} (B) \} \\ = \mathbf {P} \{f (\xi) \in A \} \mathbf {P} \{g (\eta) \in B \}. \\ \end{array}
$$

所以 $f(\xi)$ 和 $g(\eta)$ 相互独立.

## 3.3.2 二维随机向量的函数

设 $(\xi, \eta)$ 为概率空间 $(\Omega, \mathcal{F}, \mathbf{P})$ 上的二维随机向量, 而 $f$ 为 $\mathbb{R}^2$ 上的可测函数. 由定理3.1.3知 $\zeta := f(\xi, \eta)$ 也是随机变量, 其分布函数可以通过下式确定:

$$
F (z) = \mathbf {P} \{f (\xi , \eta) \leqslant z \}, \quad z \in \mathbb {R}. \tag {3.3.3}
$$

下面的定理显然成立.

定理 3.3.3（和的分布列） 若  $(\xi,\eta)$  为取非负整数值的离散型随机向量且有联合分布列

$$
p (i, j) = \mathbf {P} (\xi = i, \eta = j), \quad i, j = 0, 1, 2, \dots .
$$

则 $\zeta := \xi + \eta$ 为离散型随机变量且有分布

$$
\mathbf {P} (\zeta = k) = \sum_ {(i, j): i + j = k} p (i, j) = \sum_ {i = 0} ^ {k} p (i, k - i) = \sum_ {j = 0} ^ {k} p (k - j, j), \tag {3.3.4}
$$

其中  $k=0,1,2,\cdots$

例3.3.4 设 $\xi, \eta$ 分别服从二项分布 $B(n, p)$ 和 $B(m, p)$ 且相互独立. 根据 (3.3.4) 式有

$$
\begin{array}{l} \mathbf {P} (\xi + \eta = k) = \sum_ {i = 0} ^ {k} \mathrm{C} _ {n} ^ {i} p ^ {i} q ^ {n - i} \mathrm{C} _ {m} ^ {k - i} p ^ {k - i} q ^ {m - k + i} \\ = p ^ {k} q ^ {n + m - k} \sum_ {i = 0} ^ {k} \mathrm{C} _ {n} ^ {i} \mathrm{C} _ {m} ^ {k - i} = \mathrm{C} _ {n + m} ^ {k} p ^ {k} q ^ {n + m - k}. \\ \end{array}
$$

因此 $\xi +\eta$ 服从分布 $B(m + n,p)$ .此性质称为二项分布的再生性.

例3.3.5 设 $\xi, \eta$ 分别服从泊松分布 $P(\lambda_1), P(\lambda_2)$ 且相互独立. 利用 (3.3.4) 式有

$$
\begin{array}{l} \mathbf {P} (\xi + \eta = k) = \sum_ {i = 0} ^ {k} \frac {\lambda_ {1} ^ {i}}{i !} \mathrm{e} ^ {- \lambda_ {1}} \frac {\lambda_ {2} ^ {k - i}}{(k - i) !} \mathrm{e} ^ {- \lambda_ {2}} \\ = \mathrm{e} ^ {- \lambda_ {1} - \lambda_ {2}} \frac {1}{k !} \sum_ {i = 0} ^ {k} \frac {k !}{i ! (k - i) !} \lambda_ {1} ^ {i} \lambda_ {2} ^ {k - i} \\ = \frac {1}{k !} (\lambda_ {1} + \lambda_ {2}) ^ {k} \mathrm{e} ^ {- \lambda_ {1} - \lambda_ {2}}, \\ \end{array}
$$

故 $\xi +\eta$ 服从分布 $P(\lambda_1 + \lambda_2)$ .此性质称为泊松分布的再生性.

定理3.3.4（和的密度函数） 若 $(\xi, \eta)$ 为绝对连续型随机向量且有联合分布密度 $p(x, y)$，则 $\zeta := \xi + \eta$ 为绝对连续型随机变量且有密度函数

$$
p _ {\zeta} (z) = \int_ {- \infty} ^ {\infty} p (x, z - x) \mathrm{d} x = \int_ {- \infty} ^ {\infty} p (z - y, y) \mathrm{d} y, \quad z \in \mathbb {R}. \tag {3.3.5}
$$

证明 根据 (3.3.3) 式有

$$
\begin{array}{l} F _ {\xi + \eta} (z) = \iint_ {\{x + y \leqslant z \}} p (x, y) \mathrm{d} x \mathrm{d} y = \int_ {- \infty} ^ {\infty} \mathrm{d} x \int_ {- \infty} ^ {z - x} p (x, y) \mathrm{d} y \\ = \int_ {- \infty} ^ {\infty} \mathrm{d} x \int_ {- \infty} ^ {z} p (x, v - x) \mathrm{d} v = \int_ {- \infty} ^ {z} \mathrm{d} v \int_ {- \infty} ^ {\infty} p (x, v - x) \mathrm{d} x. \\ \end{array}
$$

对上式求导知欲证等式中的第一个等号成立, 同理可知第二个等号成立.

![](images/page_98_image_19.jpg)

我们分别称 (3.3.4) 式和 (3.3.5) 式为离散型和绝对连续型随机向量的卷积公式.

例 3.3.6 设  $X_{1}, X_{2}, \cdots, X_{n}$  相互独立且均服从指数分布  $E(\lambda)$ . 证明  $\eta_{n} := X_{1} + X_{2} + \cdots + X_{n}$  服从伽马分布  $\Gamma(\lambda, n)$ .

证明 利用数学归纳法证明. 显然, 当 $n = 1$ 时结论成立, 即 $\eta_1 = X_1$ 有密度函数 $p_1(x) = \lambda \mathrm{e}^{-\lambda x}, x > 0$. 设 $\eta_{n-1}$ 服从伽马分布 $\Gamma(\lambda, n-1)$, 即它有密度函数

$$
p _ {n - 1} (x) = \frac {\lambda^ {n - 1}}{\Gamma (n - 1)} x ^ {n - 2} \mathrm{e} ^ {- \lambda x}, \quad x > 0.
$$

注意 $\eta_{n} = \eta_{n - 1} + X_{n}$ ，其中 $X_{n}$ 有密度函数 $p_1$ .利用卷积公式知 $\eta_{n}$ 有密度函数

$$
\begin{array}{l} p _ {n} (z) = \int_ {- \infty} ^ {\infty} p _ {n - 1} (x) p _ {1} (z - x) \mathrm{d} x \\ = \frac {\lambda^ {n}}{\Gamma (n - 1)} \int_ {0} ^ {z} x ^ {n - 2} \mathrm{e} ^ {- \lambda z} \mathrm{d} x = \frac {\lambda^ {n}}{\Gamma (n)} z ^ {n - 1} \mathrm{e} ^ {- \lambda z}, \quad z > 0 \\ \end{array}
$$

即  $\eta_{n}$  服从伽马分布  $\Gamma(\lambda, n)$ .

定理 3.3.5（积的密度函数） 若绝对连续型随机向量  $(\xi,\eta)$  有联合分布密度  $p(x,y)$ ，则  $\xi\eta$  为绝对连续型随机变量且有密度函数

$$
p _ {\xi \eta} (z) = \int_ {- \infty} ^ {\infty} | y | ^ {- 1} p (y ^ {- 1} z, y) 1 _ {\{y \neq 0 \}} \mathrm{d} y, \quad z \in \mathbb {R}.
$$

证明 在假设条件之下, 我们来计算 $\xi \eta$ 的分布函数 $F_{\xi \eta}$. 注意 $\eta$ 为绝对连续型随机变量. 故对于 $z \in \mathbb{R}$ 有

$$
\begin{array}{l} F _ {\xi \eta} (z) = \mathbf {P} (\xi \eta \leqslant z, \eta \neq 0) = \iint_ {\{x y <   z, y \neq 0 \}} p (x, y) \mathrm{d} x \mathrm{d} y \\ = \iint_ {\{x <   y ^ {- 1} z, y > 0 \}} p (x, y) \mathrm{d} x \mathrm{d} y + \iint_ {\{x > y ^ {- 1} z, y <   0 \}} p (x, y) \mathrm{d} x \mathrm{d} y \\ = \int_ {0} ^ {\infty} \mathrm{d} y \int_ {- \infty} ^ {y ^ {- 1} z} p (x, y) \mathrm{d} x + \int_ {- \infty} ^ {0} \mathrm{d} y \int_ {y ^ {- 1} z} ^ {\infty} p (x, y) \mathrm{d} x \\ = \int_ {0} ^ {\infty} \mathrm{d} y \int_ {- \infty} ^ {z} y ^ {- 1} p (y ^ {- 1} u, y) \mathrm{d} u + \int_ {- \infty} ^ {0} \mathrm{d} y \int_ {z} ^ {- \infty} y ^ {- 1} p (y ^ {- 1} u, y) \mathrm{d} u \\ = \int_ {- \infty} ^ {z} \mathrm{d} u \int_ {- \infty} ^ {\infty} | y | ^ {- 1} p (y ^ {- 1} u, y) 1 _ {\{y \neq 0 \}} \mathrm{d} y. \\ \end{array}
$$

这里应用了积分变量替换 $x = y^{-1}u$。对上式求导即得 $p_{\xi \eta}(z)$ 的表达式。

## 3.3.3 多维随机向量的函数

在应用中, 我们经常需要计算多个独立随机变量的最大或最小值的分布. 这时独立性假定可以大为化简相应的计算. 这里只讨论绝对连续型随机向量的情况. 离散型随机向量的情况可以类似地处理.

例 3.3.7 设  $\xi_{1}, \xi_{2}, \cdots, \xi_{n}$  相互独立且均服从参数为  $\lambda > 0$  的指数分布。证明  $\eta := \xi_{1} \wedge \xi_{2} \wedge \cdots \wedge \xi_{n}$  服从参数为  $n\lambda > 0$  的指数分布。

证明 根据假设, 对任何 x > 0 有  $\mathbf{P}(\xi_{i} > x) = \mathrm{e}^{-\lambda x}$ . 再由  $\xi_{1}, \xi_{2}, \cdots, \xi_{n}$  的独立性得

$$
\begin{array}{l} \mathbf {P} (\eta > x) = \mathbf {P} (\xi_ {1} > x, \xi_ {2} > x, \dots , \xi_ {n} > x) \\ = \mathbf {P} (\xi_ {1} > x) \mathbf {P} (\xi_ {2} > x) \dots \mathbf {P} (\xi_ {n} > x) = \mathrm{e} ^ {- n \lambda x}, \\ \end{array}
$$

故

$$
F _ {\eta} (x) = \mathbf {P} (\eta \leqslant x) = 1 - \mathrm{e} ^ {- n \lambda x}.
$$

所以  $\eta$  服从参数为  $n\lambda > 0$  的指数分布.

定理 3.3.6（最大最小值的分布）设  $\xi_{1}, \xi_{2}, \cdots, \xi_{n}$  为独立随机变量，有共同的分布函数  $F(x)$  与密度函数  $p(x)$ . 令  $\eta = \xi_{1} \wedge \xi_{2} \wedge \cdots \wedge \xi_{n}$  和  $\zeta = \xi_{1} \vee \xi_{2} \vee \cdots \vee \xi_{n}$ . 则  $(\eta, \zeta)$  有联合密度

$$
p _ {(\eta , \zeta)} (x, y) = n (n - 1) [ F (y) - F (x) ] ^ {n - 2} p (x) p (y), \quad x <   y.
$$

证明 当 $x \geqslant y$ 时,

$$
F _ {(\eta , \zeta)} (x, y) = \mathbf {P} (\eta \leqslant x, \zeta \leqslant y) = \mathbf {P} (\xi_ {1} \leqslant y, \xi_ {2} \leqslant y, \dots , \xi_ {n} \leqslant y) = F (y) ^ {n}.
$$

当 x < y 时,

$$
\begin{array}{l} F _ {(\eta , \zeta)} (x, y) = \mathbf {P} (\eta \leqslant x, \zeta \leqslant y) = \mathbf {P} (\zeta \leqslant y) - \mathbf {P} (\eta > x, \zeta \leqslant y) \\ = \mathbf {P} (\xi_ {1} \leqslant y, \xi_ {2} \leqslant y, \dots , \xi_ {n} \leqslant y) - \mathbf {P} (x <   \xi_ {1} \leqslant y, x <   \xi_ {2} \leqslant y, \dots , x <   \xi_ {n} \leqslant y) \\ = F (y) ^ {n} - [ F (y) - F (x) ] ^ {n}. \\ \end{array}
$$

对 x, y 求导即得  $p_{(\eta,\zeta)}(x,y)$  的表达式.

例 3.3.8 向区间  $(0,1)$  中独立地随机投掷 n 个点. 求这些个点全分布在长为 1/2 的子区间内的概率.

解 以  $\xi_{i}$  表示第 i 个点的坐标,  $i=1,2,\cdots,n$ . 根据假设, 这些随机变量相互独立, 且每个  $\xi_{i}$  服从分布  $U(0,1)$ . 令  $\eta=\xi_{1}\wedge\xi_{2}\wedge\cdots\wedge\xi_{n}$  和  $\zeta=\xi_{1}\vee\xi_{2}\vee\cdots\vee\xi_{n}$ . 根据定理 3.3.6,

$$
\begin{array}{l} \mathbf {P} (\zeta - \eta <   1 / 2) = \iint_ {\{y - x <   1 / 2, 0 <   x <   y <   1 \}} n (n - 1) (y - x) ^ {n - 2} \mathrm{d} x \mathrm{d} y \\ = \int_ {0} ^ {1 / 2} \mathrm{d} x \int_ {x} ^ {x + 1 / 2} n (n - 1) (y - x) ^ {n - 2} \mathrm{d} y + \\ \end{array}
$$

$$
\begin{array}{l} \int_ {1 / 2} ^ {1} \mathrm{d} x \int_ {x} ^ {1} n (n - 1) (y - x) ^ {n - 2} \mathrm{d} y \\ = \int_ {0} ^ {1 / 2} \left[ n (y - x) ^ {n - 1} \Big | _ {y = x} ^ {y = x + 1 / 2} \right] \mathrm{d} x + \\ \int_ {1 / 2} ^ {1} \left[ n (y - x) ^ {n - 1} \Big | _ {y = x} ^ {y = 1} \right] \mathrm{d} x \\ = \int_ {0} ^ {1 / 2} \frac {n}{2 ^ {n - 1}} \mathrm{d} x + \int_ {1 / 2} ^ {1} n (1 - x) ^ {n - 1} \mathrm{d} x = \frac {n + 1}{2 ^ {n}}. \\ \end{array}
$$

此即为所求概率.

![](images/page_101_image_4.jpg)

与定理 3.3.2 类似地可以证明:

定理 3.3.7 设随机向量  $\xi := (\xi_{1}, \xi_{2}, \cdots, \xi_{m})$  和  $\eta := (\eta_{1}, \eta_{2}, \cdots, \eta_{n})$  独立. 再设 f 和 g 分别为  $R^{m}$  和  $R^{n}$  上的博雷尔可测函数. 则随机变量  $f(\xi)$  和  $g(\eta)$  也相互独立.

## \*3.3.4 随机向量的向量值函数

在本小节中, 我们讨论绝对连续型随机向量的向量值函数的分布问题.

定理3.3.8 若 $(\xi, \eta)$ 为绝对连续型随机向量且有联合分布密度 $p(x, y)$，则 $(\xi, -\eta)$ 为绝对连续型随机向量且有联合分布密度 $p(x, -y)$.

证明 根据假设, 对于任何 $x, y \in \mathbb{R}$, 作积分变量替换 $v = -w$, 我们有

$$
\begin{array}{l} \mathrm{P} (\xi \leqslant x, - \eta \leqslant y) = \iint_ {\{u \leqslant x, - v \leqslant y \}} p (u, v) \mathrm{d} u \mathrm{d} v \\ = \iint_ {\{u \leqslant x, w \leqslant y \}} p (u, - w) \mathrm{d} u \mathrm{d} w. \\ \end{array}
$$

所以 $(\xi,-\eta)$ 为绝对连续型随机向量且有联合分布密度 $p(x,-y)$ .

推论 3.3.9 若  $(\xi,\eta)$  为绝对连续型随机向量且有联合分布密度  $p(x,y)$ ，则  $\zeta:=\xi-\eta$  为绝对连续型随机变量且有密度

$$
p _ {\zeta} (z) = \int_ {- \infty} ^ {\infty} p (x, x - z) \mathrm{d} x = \int_ {- \infty} ^ {\infty} p (z - y, - y) \mathrm{d} y, \quad z \in \mathbb {R}.
$$

定理3.3.10 若 $(\xi, \eta)$ 为绝对连续型随机向量且有联合分布密度 $p(x, y)$，则 $(\xi, \eta^{-1})$ 为绝对连续型随机向量且有联合分布密度 $p(x, y^{-1})y^{-2}1_{\{y \neq 0\}}$.

证明 在假设条件之下 $\eta$ 为绝对连续型随机变量, 故 $\mathbf{P}(\eta = 0) = 0$. 因此, 对任何 $x, y \in \mathbb{R}$ 有

$$
\begin{array}{l} \mathrm{P} (\xi \leqslant x, 1 / \eta \leqslant y) = \iint_ {\{u \leqslant x, 1 / v \leqslant y, v \neq 0 \}} p (u, v) \mathrm{d} v \\ = \iint_ {\{u \leqslant x, w \leqslant y, w \neq 0 \}} p (u, w ^ {- 1}) w ^ {- 2} \mathrm{d} u \mathrm{d} w. \\ \end{array}
$$

故 $(\xi, \eta^{-1})$ 为绝对连续型随机向量且有联合分布密度 $p(x, y^{-1})y^{-2}1_{\{y \neq 0\}}$.

推论 3.3.11 (商的密度函数) 若绝对连续型随机向量  $(\xi, \eta)$  有联合分布密度  $p(x, y)$ ，则  $\xi/\eta$  为绝对连续型随机变量且有密度

$$
p _ {\xi / \eta} (z) = \int_ {- \infty} ^ {\infty} | v | p (z v, v) \mathrm{d} v, \quad z \in \mathbb {R}.
$$

证明 根据定理3.3.10知 $(\xi, \eta^{-1})$ 为绝对连续型随机向量且有联合分布密度 $q(x, y) = p(x, y^{-1})y^{-2}1_{\{y \neq 0\}}$. 再由定理3.3.5知 $\xi / \eta = \xi \eta^{-1}$ 为绝对连续型随机变量且有密度

$$
\begin{array}{l} p _ {\xi / \eta} (z) = \int_ {- \infty} ^ {\infty} | y | ^ {- 1} q (y ^ {- 1} z, y) 1 _ {\{y \neq 0 \}} \mathrm{d} y \\ = \int_ {- \infty} ^ {\infty} | y | ^ {- 1} p (y ^ {- 1} z, y ^ {- 1}) y ^ {- 2} 1 _ {\{y \neq 0 \}} \mathrm{d} y \\ = \int_ {- \infty} ^ {\infty} | v | p (v z, v) 1 _ {\{v \neq 0 \}} \mathrm{d} v. \\ \end{array}
$$

故得欲证结果.

定理 3.3.12 设  $\xi := (\xi_{1}, \xi_{2}, \cdots, \xi_{n})$  是区域  $E \subseteq R^{n}$  上的绝对连续型随机向量，且有联合密度函数 p. 再设  $f := (f_{1}, f_{2}, \cdots, f_{n})$  是 E 到区域  $F \subseteq R^{n}$  的映射，且对每一点  $y := (y_{1}, y_{2}, \cdots, y_{n}) \in F$ ，方程

$$
\left\{ \begin{array}{l} y _ {1} = f _ {1} (x _ {1}, x _ {2}, \dots , x _ {n}), \\ y _ {2} = f _ {2} (x _ {1}, x _ {2}, \dots , x _ {n}), \\ \dots \dots \\ y _ {n} = f _ {n} (x _ {1}, x _ {2}, \dots , x _ {n}) \end{array} \right. \tag {3.3.6}
$$

有唯一解  $x := (x_{1}, x_{2}, \cdots, x_{n}) \in E$ ，即

$$
\left\{ \begin{array}{l} x _ {1} = h _ {1} (y _ {1}, y _ {2}, \dots , y _ {n}), \\ x _ {2} = h _ {2} (y _ {2}, y _ {2}, \dots , y _ {n}), \\ \dots \dots \\ x _ {n} = h _ {n} (y _ {1}, y _ {2}, \dots , y _ {n}). \end{array} \right.
$$

若  $h := (h_{1}, h_{2}, \cdots, h_{n})$  连续可微，则  $\eta := (f_{1}(\xi), f_{2}(\xi), \cdots, f_{n}(\xi))$  为 F 上的绝对连续型随机向量，且有联合分布密度

$$
q (y) = p (h _ {1} (y), h _ {2} (y), \dots , h _ {n} (y)) | J (y) |, \quad y = (y _ {1}, y _ {2}, \dots , y _ {n}) \in F,
$$

其中 $J(y)$ 为坐标变换的雅可比 (Jacobi) 行列式, 即

$$
J (y) = \frac {\mathrm{d} (x _ {1} , x _ {2} , \cdots , x _ {n})}{\mathrm{d} (y _ {1} , y _ {2} , \cdots , y _ {n})} = \left| \begin{array}{c c c c} \frac {\mathrm{d} x _ {1}}{\mathrm{d} y _ {1}} & \frac {\mathrm{d} x _ {1}}{\mathrm{d} y _ {2}} & \dots & \frac {\mathrm{d} x _ {1}}{\mathrm{d} y _ {n}} \\ \frac {\mathrm{d} x _ {2}}{\mathrm{d} y _ {1}} & \frac {\mathrm{d} x _ {2}}{\mathrm{d} y _ {2}} & \dots & \frac {\mathrm{d} x _ {2}}{\mathrm{d} y _ {n}} \\ \vdots & \vdots & & \vdots \\ \frac {\mathrm{d} x _ {n}}{\mathrm{d} y _ {1}} & \frac {\mathrm{d} x _ {n}}{\mathrm{d} y _ {2}} & \dots & \frac {\mathrm{d} x _ {n}}{\mathrm{d} y _ {n}} \end{array} \right|.
$$

证明 记  $F_{\eta}(z_{1},z_{2},\cdots,z_{n})=\mathbf{P}\{f_{1}(\xi)\leqslant z_{1},f_{2}(\xi)\leqslant z_{2},\cdots,f_{n}(\xi)\leqslant z_{n}\}$ . 则

$$
F _ {\eta} (z _ {1}, z _ {2}, \dots , z _ {n}) = \int_ {\{f _ {1} (x) \leqslant z _ {1} \}} \dots \int_ {\{f _ {n} (x) \leqslant z _ {n} \}} p (x _ {1}, x _ {2}, \dots , x _ {n}) \mathrm{d} x _ {1} \mathrm{d} x _ {2} \dots \mathrm{d} x _ {n}.
$$

由重积分的变量替换公式,

$$
F _ {\eta} (z _ {1}, z _ {2}, \dots , z _ {n}) = \int_ {- \infty} ^ {z _ {1}} \dots \int_ {- \infty} ^ {z _ {n}} p (h _ {1} (y), h _ {2} (y), \dots , h _ {n} (y)) | J (y) | \mathrm{d} y _ {1} \mathrm{d} y _ {2} \dots \mathrm{d} y _ {n}.
$$

求导即得  $q(y_{1},y_{2},\cdots,y_{n})$  的表达式.

例3.3.9 设 $\xi, \eta$ 服从分布 $N(0,1)$ 且相互独立. 求 $(\xi, \eta)$ 的极坐标 $(\rho, \theta)$ 的分布密度.

解 为了使定理3.3.12的条件得到满足, 我们可以认为 $(\xi, \eta)$ 是区域 $E := \mathbb{R}^2 \setminus \{(x, 0) : x \geqslant 0\}$ 上的绝对连续型随机向量. 因为 $\mathbf{P}\{(\xi, \eta) \in E\} = 1$, 这样的做法是合理的. 由题意 $\xi = \rho \cos \theta$ 和 $\eta = \rho \sin \theta$, 其中随机向量 $(\rho, \theta)$ 取值于区域 $F := (0, \infty) \times (0, 2\pi)$. 定义坐标变换 $x = r \cos t$ 和 $y = r \sin t$. 则

$$
J (r, t) = \left| \begin{array}{c c} \cos t & - r \sin t \\ \sin t & r \cos t \end{array} \right| = r.
$$

注意 $(\xi, \eta)$ 的联合分布密度为

$$
p (x, y) = \frac {1}{2 \pi} \mathrm{e} ^ {- (x ^ {2} + y ^ {2}) / 2}, \quad (x, y) \in E.
$$

所以 $(\rho, \theta)$ 有联合分布密度

$$
q (r, t) = p (r \cos t, r \sin t) | J (r, t) | = \frac {r}{2 \pi} \mathrm{e} ^ {- \frac {r ^ {2}}{2}},
$$

其中 $(r,t)\in F$

显然, 上例中得到的随机向量 $(\rho, \theta)$ 相互独立. 注意 $\theta$ 服从分布 $U(0, 2\pi)$, 而 $\rho$ 服从以 $q_{1}(r) = r e^{-r^{2} / 2}, r > 0$ 为密度的绝对连续型分布. 后一分布称为瑞利 (Rayleigh) 分布.

例3.3.10 设 $(\xi, \eta)$ 有联合分布密度 $p(x, y) = 3x, 0 < y < x < 1$. 求 $\xi - \eta$ 的分布.

解 解法1（利用公式） 定义随机变量 $\alpha = \xi -\eta ,\beta = \eta .$ 对应的坐标变换为

$$
\left\{ \begin{array}{l} u = x - y, \\ v = y. \end{array} \right. \quad \left\{ \begin{array}{l} x = u + v, \\ y = v. \end{array} \right.
$$

显然, 变换的雅可比行列式为

$$
\left| \frac {\mathrm{d} (x , y)}{\mathrm{d} (u , v)} \right| = \left| \begin{array}{c c} 1 & 1 \\ 0 & 1 \end{array} \right| = 1 > 0.
$$

显然 $0 < y < x < 1$ 当且仅当 $u, v > 0$ 且 $u + v < 1$. 由此得到 $(\alpha, \beta)$ 的密度函数为 $q(u, v) = 3(u + v)$, 其中 $u, v > 0$ 且 $u + v < 1$. 故 $\alpha$ 的边缘分布密度为

$$
q _ {\alpha} (u) = \int_ {0} ^ {1 - u} 3 (u + v) \mathrm{d} v = \frac {3}{2} (1 - u ^ {2}), \quad 0 \leqslant u <   1.
$$

解法2（直接计算）令 $\alpha = \xi -\eta$ 对于 $0\leqslant z <   1$ 有

$$
\begin{array}{l} F _ {\alpha} (z) = \iint_ {\{x - y \leqslant z, 0 <   y <   x <   1 \}} 3 x \mathrm{d} x \mathrm{d} y \\ = \int_ {0} ^ {z} \mathrm{d} x \int_ {0} ^ {x} 3 x \mathrm{d} y + \int_ {z} ^ {1} \mathrm{d} x \int_ {x - z} ^ {x} 3 x \mathrm{d} y \\ = z ^ {3} + \int_ {z} ^ {1} 3 x z \mathrm{d} x = z ^ {3} + \frac {3}{2} z (1 - z ^ {2}) \\ = \frac {3}{2} z - \frac {1}{2} z ^ {3}. \\ \end{array}
$$

求导得到分布密度

$$
q _ {\alpha} (z) = \frac {3}{2} (1 - z ^ {2}), \quad 0 \leqslant z <   1.
$$

## 练习题

1. 设随机变量 $\xi$ 和 $\eta$ 独立且都服从均匀分布 $U(0,1)$. 求 $\xi + \eta$ 的分布密度.

2. 设  $\xi$  和  $\eta$  独立且都服从标准正态分布. 求  $\eta + \xi, \eta - \xi, \eta\xi$  和  $\eta/\xi$  的分布密度.

3. 设随机变量  $\xi_{1}$  和  $\xi_{2}$  独立且分别服从泊松分布  $P(\lambda_{1})$  和  $P(\lambda_{2})$ . 求

(1) $\xi_{1} + \xi_{2}$ 的分布列；(2) 在给定 $\xi_{1} + \xi_{2} = n$ 时 $\xi_{1}$ 的条件分布列.

4. 设随机变量  $\xi_{1}$  和  $\xi_{2}$  独立且均服从指数分布  $E(\lambda)$ . 证明  $\xi_{1} + \xi_{2}$  与  $\xi_{1}/\xi_{2}$  独立.

5. 设  $\xi_{1}, \xi_{2}, \cdots, \xi_{n}$  独立且都服从标准正态分布. 求  $X_{n} = \xi_{1}^{2} + \xi_{2}^{2} + \cdots + \xi_{n}^{2}$  的分布.

6. 设随机变量  $\xi_{1}, \xi_{2}, \cdots, \xi_{n}$  独立且分别服从指数分布  $E(\lambda_{1}), E(\lambda_{2}), \cdots, E(\lambda_{n})$ . 求  $\eta_{n} = \xi_{1} \wedge \xi_{2} \wedge \cdots \wedge \xi_{n}$  的分布.

## 第四章

## 积分和数学期望

数学期望是概率论中最基本的概念之一. 某个随机变量的数学期望直观上是其取值按照相应概率的平均, 在数学上可以通过相对于其分布函数的斯蒂尔切斯 (Stieltjes) 积分定义. 本章首先对斯蒂尔切斯积分的定义和性质做简单的介绍, 在此基础上讨论随机变量的数学期望、方差和高阶矩、条件期望和预测等, 还介绍了非负整数值随机变量的母函数.

## 4.1 斯蒂尔切斯积分

本节讨论的斯蒂尔切斯积分是数学分析中的黎曼积分的直接推广. 由于这里的证明与黎曼积分的情况类似, 很多时候我们只给出结论, 而将证明留给读者.

## 4.1.1 有界区间上的积分

考虑有界区间 $[a, b] \subseteq \mathbb{R}$. 设 $G$ 是 $[a, b]$ 上的右连续不降函数. 根据定理 2.4.4 不难证明, 存在 $(\mathbb{R}, \mathcal{B})$ 上的有限测度 $\mu$ 使得

$$
\mu ([ a, x ]) = G (x) - G (a), \quad a \leqslant x \leqslant b.
$$

因此, 可以认为 $G$ 是 $\mu$ 的某个分布函数在 $[a, b]$ 上的限制.

定义 4.1.1 设 f 为区间  $[a, b]$  上的函数. 对整数  $k \geqslant 1$ , 取  $[a, b]$  的分割点  $a = x_{k,0} < x_{k,1} < \cdots < x_{k,n_{k}} = b$  满足

$$
\delta_ {k} := \max _ {1 \leqslant i \leqslant n _ {k}} (x _ {k, i} - x _ {k, i - 1}) \to 0, \quad k \to \infty ,
$$

并取 $t_{k,i}\in [x_{k,i - 1},x_{k,i}]$ .令

$$
\begin{array}{l} \sigma_ {k} (f, G; a, b) = \sum_ {i = 1} ^ {n _ {k}} f (t _ {k, i}) [ G (x _ {k, i}) - G (x _ {k, i - 1}) ] \\ = \sum_ {i = 1} ^ {n _ {k}} f (t _ {k, i}) \mu ((x _ {k, i - 1}, x _ {k, i} ]). \tag {4.1.1} \\ \end{array}
$$

若存在有限的极限 $\lim_{k\to \infty}\sigma_k(f,G;a,b)$ 且该极限与 $\{x_{k,i}\}$ 和 $\{t_{k,i}\}$ 的具体选取无关，则称 $f$ 在 $[a,b]$ 上相对于 $G$ 斯蒂尔切斯可积，简称 $G$ 可积.称该极限为 $f$ 在 $[a,b]$ 上相对于 $G$ 的斯蒂尔切斯积分，简称 $G$ 积分，并记作

$$
\int_ {a} ^ {b} f (x) \mathrm{d} G (x) = \lim _ {k \to \infty} \sigma_ {k} (f, G; a, b).
$$

例 4.1.1 若在定义 4.1.1 中取  $G(x) \equiv x + c$ ，其中 c 为常数，则 f 在  $[a, b]$  上相对于 G 的斯蒂尔切斯积分就是它的黎曼积分.

对于 $k \geqslant 1$ 令 $[a, b]$ 的分割点 $\{x_{k,i}\}$ 如定义4.1.1给出，并分别用 $M_{k,i}(f)$ 和 $m_{k,i}(f)$ 表示函数 $f$ 在区间 $[x_{k,i-1}, x_{k,i}]$ 上的上确界和下确界。再记

$$
D _ {k} (f, G; a, b) = \sum_ {i = 1} ^ {n _ {k}} [ M _ {k, i} (f) - m _ {k, i} (f) ] [ G (x _ {k, i}) - G (x _ {k, i - 1}) ]. \tag {4.1.2}
$$

定理4.1.1 函数 $f$ 在区间 $[a,b]$ 上 $G$ 可积的充要条件是 $\lim_{k\to \infty}D_k(f,G;a,b) = 0.$

定理4.1.2 有界区间上的 $G$ 积分具有如下性质:

(1) 区间  $[a, b]$  上的任何有界连续函数在该区间上 G 可积;
(2) 设 $a \leqslant b \leqslant c \in \mathbb{R}$. 若 $f$ 在 $[a, c]$ 上 $G$ 可积, 则 $f$ 在 $[a, b]$ 和 $[b, c]$ 上 $G$ 可积且

$$
\int_ {a} ^ {c} f (x) \mathrm{d} G (x) = \int_ {a} ^ {b} f (x) \mathrm{d} G (x) + \int_ {b} ^ {c} f (x) \mathrm{d} G (x);
$$

(3) 设 $\alpha \geqslant 0, \beta \in \mathbb{R}$ 而 $f$ 在 $[a, b]$ 上 $G$ 可积. 则 $\beta f$ 在该区间上 $\alpha G$ 可积且

$$
\int_ {a} ^ {b} \beta f (x) \mathrm{d} (\alpha G) (x) = \beta \alpha \int_ {a} ^ {b} f (x) \mathrm{d} G (x);
$$

(4) 若 $f_{1}, f_{2}$ 均在 $[a, b]$ 上 $G$ 可积, 则 $f_{1} + f_{2}$ 在 $[a, b]$ 上 $G$ 可积且

$$
\int_ {a} ^ {b} [ f _ {1} (x) + f _ {2} (x) ] \mathrm{d} G (x) = \int_ {a} ^ {b} f _ {1} (x) \mathrm{d} G (x) + \int_ {a} ^ {b} f _ {2} (x) \mathrm{d} G (x);
$$

(5) 若 $f$ 在 $[a, b]$ 上 $G_{1}$ 可积且 $G_{2}$ 可积, 则 $f$ 在 $[a, b]$ 上 $G_{1} + G_{2}$ 可积且

$$
\int_ {a} ^ {b} f (x) \mathrm{d} (G _ {1} + G _ {2}) (x) = \int_ {a} ^ {b} f (x) \mathrm{d} G _ {1} (x) + \int_ {a} ^ {b} f (x) \mathrm{d} G _ {2} (x);
$$

(6) 若 $f_{1}, f_{2}$ 均在 $[a, b]$ 上 $G$ 可积且 $f_{1} \leqslant f_{2}$, 则

$$
\int_ {a} ^ {b} f _ {1} (x) \mathrm{d} G (x) \leqslant \int_ {a} ^ {b} f _ {2} (x) \mathrm{d} G (x).
$$

上述两个定理的证明与黎曼积分的相应结果类似, 请读者自行完成. 对于函数 $f$, 定义其正部 $f^{+} = 0 \vee f$ 和负部 $f^{-} = 0 \vee (-f)$. 注意 $f^{+}$ 和 $f^{-}$ 都是非负函数, 且有 $f = f^{+} - f^{-}$.

定理4.1.3 函数 $f$ 在 $[a,b]$ 上 $G$ 可积当且仅当 $f^{+}$ 和 $f^{-}$ 均在 $[a,b]$ 上 $G$ 可积.在这种情况下有

$$
\int_ {a} ^ {b} f (x) \mathrm{d} G (x) = \int_ {a} ^ {b} f ^ {+} (x) \mathrm{d} G (x) - \int_ {a} ^ {b} f ^ {-} (x) \mathrm{d} G (x). \tag {4.1.3}
$$

证明 假定 $f$ 在 $[a, b]$ 上 $G$ 可积. 注意 $M_{k,i}(f^{+}) - m_{k,i}(f^{+}) \leqslant M_{k,i}(f) - m_{k,i}(f)$. 由定理4.1.1不难看出 $f^{+}$ 在 $[a, b]$ 上 $G$ 可积, 类似地可知 $f^{-}$ 在 $[a, b]$ 上 $G$ 可积. 另一方面, 若 $f^{+}$ 和 $f^{-}$ 均在 $[a, b]$ 上 $G$ 可积, 由定理4.1.2知 $f = f^{+} - f^{-}$ 在 $[a, b]$ 上 $G$ 可积且(4.1.3)式成立.

## 4.1.2 常用积分性质

定理4.1.4 设 $g$ 是 $[a, b]$ 上的非负 $G$ 可积函数。固定 $F(a)$ 并定义积分上限的函数

$$
F (y) = F (a) + \int_ {a} ^ {y} g (x) \mathrm{d} G (x), \quad y \in [ a, b ]. \tag {4.1.4}
$$

则 $F$ 在 $[a, b]$ 上右连续且不降.

证明 显然 $F$ 是 $[a, b]$ 上的不降函数, 故它在每点处存在左、右极限. 下证 $F$ 在 $[a, b]$ 上右连续. 分两种情况讨论: (i) 若存在 $r \in (a, b]$ 使当 $x \in [a, r]$ 时有 $G(x) = G(a)$, 则显然对 $y \in [a, r]$ 有 $F(y) = F(a)$. (ii) 若对一切 $x \in (a, b]$ 有 $G(x) > G(a)$, 则由 $g$ 的 $G$ 可积性必有 $r \in (a, b]$ 使 $M := \sup_{a \leqslant x \leqslant r} g(x) < \infty$, 故当 $y \in [a, r]$ 有

$$
0 \leqslant F (y) - F (a) = \int_ {a} ^ {y} g (x) \mathrm{d} G (x) \leqslant M [ G (y) - G (a) ].
$$

由 $G$ 的右连续性得 $\lim_{y\to a+}F(y) = F(a)$, 故 $F$ 在 $a$ 处右连续. 再应用定理4.1.2中的性质(3)易知 $F$ 在 $[a,b]$ 上右连续. 所以定理的结论成立. □

定理4.1.5 设 $g$ 是 $[a, b]$ 上的非负 $G$ 可积函数，而 $F$ 是由(4.1.4)式定义的右连续不降函数。则有界函数 $f$ 在 $[a, b]$ 上 $F$ 可积当且仅当 $fg$ 在 $[a, b]$ 上 $G$ 可积，且在这种情况下有

$$
\int_ {a} ^ {b} f (x) \mathrm{d} F (x) = \int_ {a} ^ {b} f (x) g (x) \mathrm{d} G (x). \tag {4.1.5}
$$

证明 对于 $k \geqslant 1$ 令 $\{x_{k,i}\}$ 和 $\{t_{k,i}\}$ 如定义4.1.1给出，并分别用 $M_{k,i}(g)$ 和 $m_{k,i}(g)$ 表示函数 $g$ 在区间 $[x_{k,i-1}, x_{k,i}]$ 上的上确界和下确界. 注意

$$
\begin{array}{l} \left| \sigma_ {k} (f, F; a, b) - \sigma_ {k} (f g, G; a, b) \right| \\ = \left| \sum_ {i = 1} ^ {n _ {k}} f (t _ {k, i}) \left[ \int_ {x _ {k, i - 1}} ^ {x _ {k, i}} g (x) \mathrm{d} G (x) - g (t _ {k, i}) [ G (x _ {k, i}) - G (x _ {k, i - 1}) ] \right] \right| \\ = \left| \sum_ {i = 1} ^ {n _ {k}} f (t _ {k, i}) \int_ {x _ {k, i - 1}} ^ {x _ {k, i}} [ g (x) - g (t _ {k, i}) ] \mathrm{d} G (x) \right| \\ \leqslant \| f \| \sum_ {i = 1} ^ {n _ {k}} [ M _ {k, i} (g) - m _ {k, i} (g) ] [ G (x _ {k, i}) - G (x _ {k, i - 1}) ]. \\ \end{array}
$$

因 $g$ 在 $[a, b]$ 上 $G$ 可积, 上式右端当 $k \to \infty$ 时趋于零, 故有欲证结论.

推论4.1.6 设 $F$ 是以 $g$ 为密度函数的绝对连续型分布函数. 则有界函数 $f$ 在 $[a, b]$ 上 $F$ 可积当且仅当 $fg$ 在 $[a, b]$ 上黎曼可积, 且在这种情况下有

$$
\int_ {a} ^ {b} f (x) \mathrm{d} F (x) = \int_ {a} ^ {b} f (x) g (x) \mathrm{d} x. \tag {4.1.6}
$$

定理 4.1.7 设 G 是离散型分布函数且在左开右闭区间  $(a, b]$  中的跳跃点集为  $S := \{y_j : j = 1, 2, \cdots\}$ . 若函数 f 在  $[a, b]$  上有界且在 S 的每点处连续（当  $b \in S$  时只要求 f 在此处左连续），则它在  $[a, b]$  上 G 可积且有

$$
\int_ {a} ^ {b} f (x) \mathrm{d} G (x) = \sum_ {j = 1} ^ {\infty} f (y _ {j}) [ G (y _ {j}) - G (y _ {j} -) ]. \tag {4.1.7}
$$

证明 对于任何 $\varepsilon > 0$, 可取充分大的 $m \geqslant 1$ 使得

$$
\sum_ {j = m + 1} ^ {\infty} \left[ G (y _ {j}) - G (y _ {j} -) \right] = \sum_ {j = m + 1} ^ {\infty} \mu (\{y _ {j} \}) <   \varepsilon .
$$

对于 $k \geqslant 1$ 令 $[a, b]$ 的分割点 $\{x_{k,i}\}$ 如定义4.1.1给出。当 $k \geqslant 1$ 充分大时，有限集 $\{y_1, y_2, \dots, y_m\}$ 中的不同的点属于 $[x_{k,i-1}, x_{k,i}]$，$i = 1, 2, \dots, n_k$ 中不同的区间。不妨设 $y_j \in [x_{k,i_j-1}, x_{k,i_j}]$，$j = 1, 2, \dots, m$。不难发现

$$
\begin{array}{l} \left| \sigma_ {k} (f, G; a, b) - \sum_ {j = 1} ^ {\infty} f (y _ {j}) [ G (y _ {j}) - G (y _ {j} -) ] \right| \\ \leqslant \left| \sum_ {i = 1} ^ {n _ {k}} f (t _ {k, i}) [ G (x _ {k, i}) - G (x _ {k, i - 1}) ] - \sum_ {j = 1} ^ {m} f (y _ {j}) [ G (y _ {j}) - G (y _ {j} -) ] \right| + \\ \sum_ {j = m + 1} ^ {\infty} | f (y _ {j}) | [ G (y _ {j}) - G (y _ {j} -) ] \\ \leqslant \left| \sum_ {j = 1} ^ {m} f (t _ {k, i _ {j}}) [ G (y _ {j}) - G (y _ {j} -) ] - \sum_ {j = 1} ^ {m} f (y _ {j}) [ G (y _ {j}) - G (y _ {j} -) ] \right| + \\ 2 \| f \| \sum_ {j = m + 1} ^ {\infty} [ G (y _ {j}) - G (y _ {j} -) ] \\ \leqslant \sum_ {j = 1} ^ {m} | f (t _ {k, i _ {j}}) - f (y _ {j}) | [ G (y _ {j}) - G (y _ {j} -) ] + 2 \| f \| \varepsilon . \\ \end{array}
$$

显然, 当 $k \to \infty$ 时有 $|t_{k,i_j} - y_j| \to 0$, 故 $|f(t_{k,i_j}) - f(y_j)| \to 0$. 在上式两端令 $k \to \infty$ 取上极限, 再由 $\varepsilon > 0$ 的任意性即知 (4.1.7) 式成立. □

定理 4.1.8 设函数  $f_{n}, n=1,2,\cdots$  在  $[a,b]$  上 G 可积且一致地  $\lim_{n\to\infty}f_{n}=f$ . 则 f 在  $[a,b]$  上 G 可积且

$$
\lim _ {n \to \infty} \int_ {a} ^ {b} f _ {n} (x) \mathrm{d} G (x) = \int_ {a} ^ {b} f (x) \mathrm{d} G (x). \tag {4.1.8}
$$

证明 对于 $k \geqslant 1$ 令 $[a, b]$ 的分割点 $\{x_{k,i}\}$ 如定义4.1.1给出. 对于任意的 $\varepsilon > 0$ 可取充分大的 $N \geqslant 1$, 使当 $n \geqslant N$ 时, 对 $x \in [a, b]$ 有 $|f_n(x) - f(x)| \leqslant \varepsilon$. 此时显然有

$$
M _ {k, i} (f) - m _ {k, i} (f) \leqslant M _ {k, i} (f _ {n}) - m _ {k, i} (f _ {n}) + 2 \varepsilon .
$$

再由 (4.1.2) 式易见

$$
D _ {k} (f, G; a, b) \leqslant D _ {k} (f _ {n}, G; a, b) + 2 \varepsilon [ G (b) - G (a) ].
$$

因 $f_{n}$ 在 $[a,b]$ 上 $G$ 可积, 根据定理4.1.1有 $\lim_{k\to \infty}D_k(f_n,G;a,b) = 0$. 在上式两端取上极限得

$$
\operatorname * {l i m s u p} _ {k \to \infty} D _ {k} (f, G; a, b) \leqslant 2 \varepsilon [ G (b) - G (a) ].
$$

由 $\varepsilon > 0$ 的任意性有 $\lim_{k \to \infty} D_k(f, G; a, b) = 0$. 再由定理4.1.1知 $f$ 在 $[a, b]$ 上 $G$ 可积. 此外, 应用定理4.1.2不难看出, 当 $n \geqslant N$ 时有

$$
\left| \int_ {a} ^ {b} f _ {n} (x) \mathrm{d} G (x) - \int_ {a} ^ {b} f (x) \mathrm{d} G (x) \right| \leqslant \int_ {a} ^ {b} | f _ {n} (x) - f (x) | \mathrm{d} G (x) \leqslant \varepsilon [ G (b) - G (a) ].
$$

在上式两端令  $n \rightarrow \infty$  取上极限, 再由  $\varepsilon > 0$  的任意性可知 (4.1.8) 式成立.

## 4.1.3 全空间上的积分

现在考虑一维欧氏空间 $\mathbb{R}$ 上的积分. 设 $G$ 是 $\mathbb{R}$ 上的分布函数, 即存在 $(\mathbb{R}, \mathcal{B})$ 上的局部有限测度 $\mu$ 使得

$$
G (b) - G (a) = \mu (a, b ], \quad a \leqslant b \in \mathbb {R}. \tag {4.1.9}
$$

定义4.1.2 设 $\mathbb{R}$ 上的函数 $f$ 在每个有界区间 $[a, b] \subseteq \mathbb{R}$ 上 $G$ 可积. 令 $f^{+} = 0 \vee f$ 和 $f^{-} = 0 \vee (-f)$ 分别是 $f$ 的正部和负部. 如果两个极限

$$
\int_ {- \infty} ^ {\infty} f ^ {\pm} (x) \mathrm{d} G (x) := \lim _ {a \to - \infty} \lim _ {b \to \infty} \int_ {a} ^ {b} f ^ {\pm} (x) \mathrm{d} G (x) \tag {4.1.10}
$$

中至少有一个有限, 就称 $f$ 在 $\mathbb{R}$ 上相对于 $G$ 的斯蒂尔切斯积分存在. 在这种情况下, 定义 $f$ 相对于 $G$ 的斯蒂尔切斯积分为

$$
\int_ {- \infty} ^ {\infty} f (x) \mathrm{d} G (x) = \int_ {- \infty} ^ {\infty} f ^ {+} (x) \mathrm{d} G (x) - \int_ {- \infty} ^ {\infty} f ^ {-} (x) \mathrm{d} G (x). \tag {4.1.11}
$$

上式也简称为 $f$ 在 $\mathbb{R}$ 上的 $G$ 积分. 如果 (4.1.10) 式中的两个极限都有限, 就称 $f$ 在 $\mathbb{R}$ 上关于 $G$ 斯蒂尔切斯可积, 简称 $G$ 可积.

基于有界区间上斯蒂尔切斯积分的相应结论, 不难证明如下的几个定理:

定理4.1.9 一维空间 $\mathbb{R}$ 上的 $G$ 积分具有如下性质:

(1) 若 $f$ 在 $\mathbb{R}$ 上 $G$ 可积, 则它在 $[a, b] \subseteq \mathbb{R}$ 上 $G$ 可积且

$$
\int_ {a} ^ {b} f (x) \mathrm{d} G (x) = \int_ {- \infty} ^ {\infty} 1 _ {(a, b ]} (x) f (x) \mathrm{d} G (x);
$$

(2) 设 $\alpha \geqslant 0, \beta \in \mathbb{R}$ 而 $f$ 在 $\mathbb{R}$ 上 $G$ 可积. 则 $\beta f$ 在 $\mathbb{R}$ 上 $\alpha G$ 可积且

$$
\int_ {- \infty} ^ {\infty} \beta f (x) \mathrm{d} (\alpha G) (x) = \beta \alpha \int_ {- \infty} ^ {\infty} f (x) \mathrm{d} G (x);
$$

(3) 若 $f_{1}, f_{2}$ 均在 $\mathbb{R}$ 上 $G$ 可积, 则 $f_{1} + f_{2}$ 在 $\mathbb{R}$ 上 $G$ 可积且

$$
\int_ {- \infty} ^ {\infty} [ f _ {1} (x) + f _ {2} (x) ] \mathrm{d} G (x) = \int_ {- \infty} ^ {\infty} f _ {1} (x) \mathrm{d} G (x) + \int_ {- \infty} ^ {\infty} f _ {2} (x) \mathrm{d} G (x);
$$

(4) 若 $f$ 在 $\mathbb{R}$ 上 $G_{1}$ 可积且 $G_{2}$ 可积, 则 $f$ 在 $\mathbb{R}$ 上 $G_{1} + G_{2}$ 可积且

$$
\int_ {- \infty} ^ {\infty} f (x) \mathrm{d} (G _ {1} + G _ {2}) (x) = \int_ {- \infty} ^ {\infty} f (x) \mathrm{d} G _ {1} (x) + \int_ {- \infty} ^ {\infty} f (x) \mathrm{d} G _ {2} (x);
$$

(5) 若 $f_{1}, f_{2}$ 均在 $\mathbb{R}$ 上 $G$ 可积且 $f_{1} \leqslant f_{2}$, 则

$$
\int_ {- \infty} ^ {\infty} f _ {1} (x) \mathrm{d} G (x) \leqslant \int_ {- \infty} ^ {\infty} f _ {2} (x) \mathrm{d} G (x).
$$

定理4.1.10 设非负函数 $g$ 在 $\mathbb{R}$ 的每个有界闭区间上 $G$ 可积. 固定常数 $a$ 和 $F(a)$, 并定义 $\mathbb{R}$ 上的函数

$$
F (y) = F (a) - 1 _ {\{y \leqslant a \}} \int_ {y} ^ {a} g (x) \mathrm{d} G (x) + 1 _ {\{y > a \}} \int_ {a} ^ {y} g (x) \mathrm{d} G (x). \tag {4.1.12}
$$

则 F 是 R 上的分布函数.

定理4.1.11 设非负函数 $g$ 在 $\mathbb{R}$ 的每个有界闭区间上 $G$ 可积, 而 $F$ 是由(4.1.12)式定义的分布函数. 则局部有界函数 $f$ 在 $\mathbb{R}$ 上 $F$ 可积当且仅当 $fg$ 在 $\mathbb{R}$ 上 $G$ 可积, 且在这种情况下有

$$
\int_ {- \infty} ^ {\infty} f (x) \mathrm{d} F (x) = \int_ {- \infty} ^ {\infty} f (x) g (x) \mathrm{d} G (x). \tag {4.1.13}
$$

定理4.1.12 设 $F$ 是以 $g$ 为密度函数的绝对连续型分布函数, 而 $fg$ 在每个有界区间上黎曼可积. 则有

$$
\int_ {- \infty} ^ {\infty} f (x) \mathrm{d} F (x) = \int_ {- \infty} ^ {\infty} f (x) g (x) \mathrm{d} x. \tag {4.1.14}
$$