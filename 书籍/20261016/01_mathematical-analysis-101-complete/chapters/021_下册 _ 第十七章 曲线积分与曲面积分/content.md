# 下册 / 第十七章 曲线积分与曲面积分

原始 PDF 第 683–707 页。

## 第十七章

## 曲线积分与曲面积分

---

42

第十七章 曲线积分与曲面积分

本章讨论欧氏空间  $R^{n}$  中曲线以及曲面上的积分理论，包括曲线的长度、曲面的面积，以及曲线曲面上函数和向量值函数的积分，这些积分往往有着明显的几何或物理背景.

## 17.1 第一型曲线积分

我们从曲线的长度开始. 在第九章中, 对于 $C^1$ 的平面曲线 $\sigma: [\alpha, \beta] \to \mathbb{R}^2$, 利用折线逼近曲线的办法, 我们定义了其长度为

$$
L (\sigma) = \int_ {\alpha} ^ {\beta} \sqrt {[ x ^ {\prime} (t) ] ^ {2} + [ y ^ {\prime} (t) ] ^ {2}}   \mathrm{d} t.
$$

现在考虑一般的情形. 考虑映射 $\sigma : [\alpha, \beta] \to \mathbb{R}^n$, 它称为 $\mathbb{R}^n$ 中的参数曲线. 我们仍然用折线逼近曲线的办法定义 $\sigma$ 的长度 (图 17.1). 为此, 任取 $[\alpha, \beta]$ 的分割

$$
\mathrm{P}: \alpha = t _ {0} <   t _ {1} <   t _ {2} <   \dots <   t _ {m} = \beta,
$$

![](../../raw/pages_0673-0688/images/page_683_image_8.jpg)

<details>
<summary>natural_image</summary>

Abstract blue line drawing resembling a stylized spiral or helical shape (no text or symbols)
</details>

图 17.1 折线逼近

相继用直线段连接曲线上的分点 $\sigma (t_{i - 1})$ 与 $\sigma (t_i)(1\leqslant t\leqslant m)$ ，得到的折线的长度为

$$
L (\sigma ; \mathrm{P}) = \sum_ {i = 1} ^ {m} \| \sigma (t _ {i}) - \sigma (t _ {i - 1}) \|.
$$

如果这些折线的长度有上界, 即

$$
\sup _ {\mathrm{P}} \sum_ {i = 1} ^ {m} \| \sigma (t _ {i}) - \sigma (t _ {i - 1}) \| <   + \infty ,
$$

则称 $\sigma$ 是可求长曲线, 其长度定义为

$$
L (\sigma) = \sup _ {\mathrm{P}} \sum_ {i = 1} ^ {m} \| \sigma (t _ {i}) - \sigma (t _ {i - 1}) \|.
$$

---

17.1 第一型曲线积分

43

从定义可以得到可求长曲线的下列性质:

\- 如果 $\sigma$ 为可求长曲线, 则当 $[\gamma, \delta] \subseteq [\alpha, \beta]$ 时, $\sigma|_{[\gamma, \delta]}$ 也是可求长曲线;

\- 如果 $\sigma$ 为可求长曲线, 则任给 $\gamma \in [\alpha, \beta]$, 均有

$$
L (\sigma) = L (\sigma | _ {[ \alpha , \gamma ]}) + L (\sigma | _ {[ \gamma , \beta ]}).
$$

这是曲线长度的可加性, 利用三角不等式不难加以证明.

如果 $\sigma(t)$ 的每一个分量均为 $C^1$ 函数, 则由 §9.7 节的推导方法可知 $\sigma$ 是可求长曲线, 且其长度可以表示为积分:

$$
L (\sigma) = \int_ {\alpha} ^ {\beta} \| \sigma^ {\prime} (t) \|   \mathrm{d} t.
$$

为了导出一般曲线可求长的充要条件, 我们引入有界变差函数的概念.

定义 17.1.1 (有界变差函数) 设 f 为定义在  $[\alpha, \beta]$  上的函数. 任给分割

$$
\mathrm{P}: \alpha = t _ {0} <   t _ {1} <   t _ {2} <   \dots <   t _ {m} = \beta ,
$$

记

$$
V (f; \mathrm{P}) = \sum_ {i = 1} ^ {m} | f (t _ {i}) - f (t _ {i - 1}) |,
$$

如果 $V(f; \mathrm{P})$ 有不依赖于 $\mathrm{P}$ 的上界, 则称 $f$ 为 $[\alpha, \beta]$ 上的有界变差函数, 它在 $[\alpha, \beta]$ 中的全变差记为

$$
\bigvee_ {\alpha} ^ {\beta} (f) = \sup _ {\mathrm{P}} V (f; \mathrm{P}).
$$

有界变差函数的例子有:

\- 单调函数. 如果 $f$ 为 $[\alpha, \beta]$ 上的单调函数, 例如单调递增, 则任给分割 $\mathrm{P}$, 有

$$
V (f; \mathrm{P}) = \sum_ {i = 1} ^ {m} | f (t _ {i}) - f (t _ {i - 1}) | = \sum_ {i = 1} ^ {m} [ f (t _ {i}) - f (t _ {i - 1}) ] = f (\beta) - f (\alpha),
$$

这说明

$$
\bigvee_ {\alpha} ^ {\beta} (f) = | f (\beta) - f (\alpha) |.
$$

\- Lipschitz 函数. 设 $|f(x) - f(y)| \leqslant L|x - y|$, 则

$$
V (f; \mathrm{P}) = \sum_ {i = 1} ^ {m} | f (t _ {i}) - f (t _ {i - 1}) | \leqslant \sum_ {i = 1} ^ {m} L (t _ {i} - t _ {i - 1}) = L (\beta - \alpha),
$$

因而 $f$ 是有界变差函数.

---

44

第十七章 曲线积分与曲面积分

\- $C^1$ 函数. 根据微分中值定理可以知道, 闭区间上的 $C^1$ 函数都是 Lipschitz 函数, 因而是有界变差函数. 当 $g \in R[\alpha, \beta]$ 时, 记

$$
f (x) = \int_ {\alpha} ^ {x} g (t)   \mathrm{d} t, x \in [ \alpha , \beta ],
$$

则 f 是 Lipschitz 函数, 因此也是有界变差函数.

下面的结果刻画了可求长曲线.

定理 17.1.1 (Jordan 定理) 参数曲线  $\sigma$  为可求长曲线当且仅当其分量均为有界变差函数.

证明 记  $\sigma(t)=(x_{1}(t),x_{2}(t),\cdots,x_{n}(t))$ ,  $t\in[\alpha,\beta]$ . 若  $\sigma$  为可求长曲线, 则任给  $[\alpha,\beta]$  的分割 P, 有

$$
V (x _ {i}; \mathrm{P}) = \sum_ {j = 1} ^ {m} | x _ {i} (t _ {j}) - x _ {i} (t _ {j - 1}) | \leqslant \sum_ {j = 1} ^ {m} \| \sigma (t _ {j}) - \sigma (t _ {j - 1}) \| \leqslant L (\sigma),
$$

这说明  $x_{i}$  为有界变差函数.

反之, 如果每一个 $x_{i}$ 都是有界变差函数, 则

$$
\begin{array}{l} L (\sigma ; \mathrm{P}) = \sum_ {j = 1} ^ {m} \| \sigma (t _ {j}) - \sigma (t _ {j - 1}) \| \\ \leqslant \sum_ {j = 1} ^ {m} \big (| x _ {1} (t _ {j}) - x _ {1} (t _ {j - 1}) | + | x _ {2} (t _ {j}) - x _ {2} (t _ {j - 1}) | + \dots + | x _ {n} (t _ {j}) - x _ {n} (t _ {j - 1}) | \big) \\ = \sum_ {i = 1} ^ {n} V (x _ {i}; \mathrm{P}) \leqslant \sum_ {i = 1} ^ {n} \bigvee_ {\alpha} ^ {\beta} (x _ {i}). \\ \end{array}
$$

这说明  $\sigma$  是可求长曲线.

为了刻画有界变差函数, 我们先来说明

引理17.1.2 设 $\gamma \in (\alpha, \beta)$. 则 $f$ 为 $[\alpha, \beta]$ 上的有界变差函数当且仅当 $f$ 在 $[\alpha, \gamma]$ 和 $[\gamma, \beta]$ 上均为有界变差函数, 此时

$$
\bigvee_ {\alpha} ^ {\beta} (f) = \bigvee_ {\alpha} ^ {\gamma} (f) + \bigvee_ {\gamma} ^ {\beta} (f). \tag {17.1.1}
$$

证明 设 $f$ 为 $[\alpha, \beta]$ 上的有界变差函数, 任取 $[\alpha, \gamma]$ 的分割 $\mathrm{P}_1$ 和 $[\gamma, \beta]$ 的分割 $\mathrm{P}_2$, 有

$$
V \big (f \big | _ {[ a, c ]}; \mathrm{P} _ {1} \big) + V \big (f \big | _ {[ c, b ]}; \mathrm{P} _ {2} \big) = V (f; \mathrm{P} _ {1} \cup \mathrm{P} _ {2}) \leqslant \bigvee_ {\alpha} ^ {\beta} (f),
$$

---

17.1 第一型曲线积分

45

这说明 $f$ 在 $[\alpha, \gamma]$ 和 $[\gamma, \beta]$ 上均为有界变差函数，且

$$
\bigvee_ {\alpha} ^ {\gamma} (f) + \bigvee_ {\gamma} ^ {\beta} (f) \leqslant \bigvee_ {\alpha} ^ {\beta} (f). \tag {17.1.2}
$$

反之, 如果 $f$ 在 $[\alpha, \gamma]$ 和 $[\gamma, \beta]$ 上均为有界变差函数, 则任取 $[\alpha, \beta]$ 的分割 $\mathrm{P}$, 如果 $\gamma$ 不是 $\mathrm{P}$ 的分点, 则添加 $\gamma$ 为分点, 此时

$$
V (f; \mathrm{P}) \leqslant \bigvee_ {\alpha} ^ {\gamma} (f) + \bigvee_ {\gamma} ^ {\beta} (f),
$$

这说明 $f$ 在 $[\alpha, \beta]$ 上也是有界变差函数，且

$$
\bigvee_ {\alpha} ^ {\beta} (f) \leqslant \bigvee_ {\alpha} ^ {\gamma} (f) + \bigvee_ {\gamma} ^ {\beta} (f). \tag {17.1.3}
$$

(17.1.2)式和(17.1.3)式结合起来就得到了(17.1.1)式.

![](../../raw/pages_0673-0688/images/page_686_image_9.jpg)

下面的结果刻画了有界变差函数.

定理 17.1.3 f 为有界变差函数当且仅当它是两个单调递增函数之差.

证明 只要证明必要性就可以了. 设 $f$ 为 $[\alpha, \beta]$ 上的有界变差函数, 记

$$
g (x) = \bigvee_ {\alpha} ^ {x} (f), h (x) = g (x) - f (x), x \in [ \alpha , \beta ],
$$

则 $f = g - h$. 由上述引理可知 $g$ 为单调递增函数, 我们来说明 $h$ 也是单调递增的. 为此, 任取 $x, y \in [\alpha, \beta]$, 当 $x < y$ 时, 有

$$
\begin{array}{l} h (y) - h (x) = [ g (y) - g (x) ] - [ f (y) - f (x) ] \\ = \bigvee_ {x} ^ {y} (f) - [ f (y) - f (x) ] \geqslant | f (y) - f (x) | - [ f (y) - f (x) ] \geqslant 0, \\ \end{array}
$$

这说明 h 的确是单调递增函数.

![](../../raw/pages_0673-0688/images/page_686_image_17.jpg)

需要注意的是, 可求长参数曲线未必连续. 例如, 定义 $\sigma: [0,1] \to \mathbb{R}^2$ 如下:

$$
\sigma (t) = (0, 0), \quad 0 \leqslant t <   \frac {1}{2}; \quad \sigma (t) = (1, 0), \quad \frac {1}{2} \leqslant t \leqslant 1,
$$

容易验证 $\sigma$ 是可求长参数曲线, 且 $L(\sigma) = 1$. 不过, $\sigma$ 在平面上的像由两个点构成, 这不符合人们对曲线的直观印象. 为了简单起见, 我们通常考虑连续的可求长参数曲线.

引理 17.1.4 设  $\sigma:[\alpha,\beta]\to R^{n}$  为连续的可求长参数曲线, 记

$$
s (t) = L (\sigma | _ {[ \alpha , t ]}), \quad t \in [ \alpha , \beta ],
$$

则 $s$ 是关于 $t$ 的连续函数.

---

46

第十七章 曲线积分与曲面积分

证明 以右连续为例, 设 $\alpha \leqslant t < \beta$, 我们要说明 $s$ 在 $t$ 处右连续. 任给 $\varepsilon > 0$, 由一致连续性可知, 存在 $\eta > 0$, 使得当 $t', t'' \in [\alpha, \beta]$ 且 $|t' - t''| \leqslant \eta$ 时, $\|\sigma(t') - \sigma(t'')\| < \varepsilon$. 由参数曲线长度的定义可知, 存在 $[\alpha, \beta]$ 的分割

$$
\mathrm{P}: \alpha = t _ {0} <   t _ {1} <   t _ {2} <   \dots <   t _ {m} = \beta ,
$$

使得

$$
\sum_ {i = 1} ^ {m} \| \sigma (t _ {i}) - \sigma (t _ {i - 1}) \| > L (\sigma) - \varepsilon .
$$

由三角不等式可知, 添加分点时所得折线的长度不会变小, 因此不妨设  $\|P\|\leqslant\eta$  且  $t=t_{k-1}$ . 此时, 由

$$
L (\sigma) = \sum_ {i = 1} ^ {m} L \big (\sigma | _ {[ t _ {i - 1}, t _ {i} ]} \big) \geqslant \sum_ {j \neq k} \| \sigma (t _ {j}) - \sigma (t _ {j - 1}) \| + L \big (\sigma | _ {[ t _ {k - 1}, t _ {k} ]} \big)
$$

可知

$$
\| \sigma (t _ {k}) - \sigma (t _ {k - 1}) \| > L \big (\sigma \big | _ {[ t _ {k - 1}, t _ {k} ]} \big) - \varepsilon .
$$

记 $\delta = t_k - t_{k-1}$. 则当 $0 < t' - t_{k-1} \leqslant \delta$ 时, 有

$$
L \big (\sigma | _ {[ t _ {k - 1}, t ^ {\prime} ]} \big) \leqslant L \big (\sigma | _ {[ t _ {k - 1}, t _ {k} ]} \big) <   \| \sigma (t _ {k}) - \sigma (t _ {k - 1}) \| + \varepsilon <   2 \varepsilon ,
$$

即 $0 \leqslant s(t') - s(t) < 2\varepsilon$, 这说明 $s$ 在 $t$ 处的确右连续.

我们称 $s(t)$ 为 $\sigma$ 的弧长函数. 如果 $\sigma$ 不在任何子区间上取常值, 则 $s(t)$ 为严格单调递增函数. 当 $\sigma$ 为连续的可求长参数曲线且 $\sigma$ 不在任何子区间上取常值时, $s: [\alpha, \beta] \to [0, L(\sigma)]$ 是连续的严格单调递增函数, 从而可逆, 其反函数记为 $t = t(s)$. 这时, $\tilde{\sigma}(s) = \sigma(t(s))$ 可以看成以 $s$ 为参数的参数曲线, $\tilde{\sigma}$ 和 $\sigma$ 在 $\mathbb{R}^n$ 中具有相同的像, 在不引起混淆时往往不区分它们. 注意

$$
L (\tilde {\sigma} | _ {[ s _ {1}, s _ {2} ]}) = s _ {2} - s _ {1}, \forall 0 \leqslant s _ {1} <   s _ {2} \leqslant L (\sigma).
$$

s 常称为  $\sigma$  的弧长参数.

当 $\sigma$ 为 $C^1$ 参数曲线且 $\| \sigma'(t) \|$ 在任何子区间上均不恒为零（例如，处处非零）时，上一段的讨论对 $\sigma$ 完全适用，此时

$$
s ^ {\prime} (t) = \| \sigma^ {\prime} (t) \| \text {或} \mathrm{d} s = \| \sigma^ {\prime} (t) \| \mathrm{d} t.
$$

下面我们考虑一个物理问题: 已知某线状物质的密度函数为  $\rho$ , 求该物质的质量. 利用 “微元法” 可以将它转化为积分问题. 为此, 用可求长参数曲线  $\sigma : [\alpha, \beta] \to R^{3}$  表示该线状物体. 当  $t \in [\alpha, \beta]$ ,  $\delta t$  充分小时,  $\sigma$  在  $[t, t + \delta t]$  这一小段上的质量记为  $\delta m$ , 则  $\delta m \approx \rho(\sigma(t))\delta s$ , 其中  $\delta s = L(\sigma|_{[t, t + \delta t]})$ . 如果  $\sigma$  为  $C^{1}$  曲线, 则  $\delta s \approx \| \sigma'(t) \| \delta t$ , 因此

$$
\delta m \approx \rho (\sigma (t)) \delta s \approx \rho (\sigma (t)) \| \sigma^ {\prime} (t) \|   \delta t.
$$

---

17.1 第一型曲线积分

47

求和并取极限, 总质量 $m$ 就可以表示为积分

$$
m = \int_ {\alpha} ^ {\beta} \rho (\sigma (t)) \| \sigma^ {\prime} (t) \|   \mathrm{d} t.
$$

类似地, 该物质的质心 $(\bar{x}, \bar{y}, \bar{z})$ 可由如下公式确定:

$$
\bar {x} = \frac {1}{m} \int_ {\alpha} ^ {\beta} x (t) \rho (\sigma (t)) \| \sigma^ {\prime} (t) \| \mathrm{d} t, \bar {y} = \frac {1}{m} \int_ {\alpha} ^ {\beta} y (t) \rho (\sigma (t)) \| \sigma^ {\prime} (t) \| \mathrm{d} t,
$$

$$
\bar {z} = \frac {1}{m} \int_ {\alpha} ^ {\beta} z (t) \rho (\sigma (t)) \| \sigma^ {\prime} (t) \| \mathrm{d} t,
$$

其中  $\sigma(t)=(x(t),y(t),z(t))$ .

一般地, 我们考虑可求长参数曲线上有界函数的积分. 设 $\sigma: [\alpha, \beta] \to \mathbb{R}^n$ 为参数曲线, $f$ 是定义在 $\sigma$ 上的有界函数, 任给 $[\alpha, \beta]$ 的分割 P, 取 $\xi_i \in [t_{i-1}, t_i] (1 \leqslant i \leqslant m)$, 考虑和 $\sum_{i=1}^{m} f(\sigma(\xi_i)) \Delta s_i$, 其中 $\Delta s_i = s(t_i) - s(t_{i-1})$. 如果极限 $\lim_{\|P\| \to 0} \sum_{i=1}^{m} f(\sigma(\xi_i)) \Delta s_i$ 存在且与 $\{\xi_i\}$ 的选取无关, 则称此极限为 $f$ 在 $\sigma$ 上的第一型曲线积分, 记为

$$
\int_ {\sigma} f \mathrm{d} s = \lim _ {\| P \| \to 0} \sum_ {i = 1} ^ {m} f (\sigma (\xi_ {i})) \Delta s _ {i}.
$$

当 $f = 1$ 时，第一型曲线积分也就是曲线的长度.

当曲线 $\sigma$ 的弧长参数存在时, 第一型曲线积分可以转化为 Riemann 积分:

$$
\int_ {\sigma} f \mathrm{d} s = \int_ {0} ^ {L (\sigma)} f (\sigma (s)) \mathrm{d} s;
$$

如果 $\sigma (t)$ 为分段 $C^1$ 曲线, 则 $f$ 在 $\sigma$ 上的第一型曲线积分可以写为

$$
\int_ {\sigma} f \mathrm{d} s = \int_ {\alpha} ^ {\beta} f (\sigma (t)) \| \sigma^ {\prime} (t) \| \mathrm{d} t.
$$

例 17.1.1 设曲线  $\sigma$  是椭圆  $\frac{x^{2}}{a^{2}} + \frac{y^{2}}{b^{2}} = 1$  在第一象限内的部分 (图 17.2)，计算积分  $I = \int_{\sigma} xy \, ds$ .

![](../../raw/pages_0689-0704/images/page_688_image_16.jpg)

<details>
<summary>text_image</summary>

y
b
O
a x
</details>

图17.2 椭圆

---

48

第十七章 曲线积分与曲面积分

解 $\sigma$ 可以表示为参数曲线:

$$
\sigma (t) = (a \cos t, b \sin t), \quad t \in [ 0, \pi / 2 ].
$$

此时 $\| \sigma'(t)\| = \sqrt{a^2\sin^2t + b^2\cos^2t}$ ，所求积分为

$$
\begin{array}{l} I = \int_ {0} ^ {\frac {\pi}{2}} a \cos t \cdot b \sin t \cdot \sqrt {a ^ {2} \sin^ {2} t + b ^ {2} \cos^ {2} t} \mathrm{d} t \\ = \frac {a b}{2} \int_ {0} ^ {\frac {\pi}{2}} \sin 2 t \sqrt {\frac {a ^ {2} + b ^ {2}}{2} + \frac {b ^ {2} - a ^ {2}}{2} \cos 2 t} \mathrm{d} t \\ = \frac {a b}{4} \int_ {- 1} ^ {1} \sqrt {\frac {a ^ {2} + b ^ {2}}{2} + \frac {b ^ {2} - a ^ {2}}{2} u} \mathrm{d} u \\ = \frac {a b}{3} \frac {a ^ {2} + a b + b ^ {2}}{a + b}. \\ \end{array}
$$

例 17.1.2 设  $\sigma$  是球面  $x^{2} + y^{2} + z^{2} = a^{2}$  被平面  $x + z = a$  所截出的圆 (图 17.3)，计算积分  $\int_{\sigma} xz ds$ .

![](../../raw/pages_0689-0704/images/page_689_image_7.jpg)

<details>
<summary>text_image</summary>

z
a
a/2
O
a/2
a
x
</details>

图17.3 截面圆

解 先求 $\sigma$ 的方程: 以 $z = a - x$ 代入球面方程得

$$
x ^ {2} + y ^ {2} + (a - x) ^ {2} = a ^ {2},
$$

整理后成为

$$
\left(x - a / 2\right) ^ {2} + y ^ {2} / 2 = (a / 2) ^ {2},
$$

用参数表示为

$$
x (t) = \frac {a}{2} + \frac {a}{2} \cos t, y (t) = \frac {a}{\sqrt {2}} \sin t, z (t) = \frac {a}{2} - \frac {a}{2} \cos t, t \in [ 0, 2 \pi ].
$$

此时

$$
\| \sigma^ {\prime} (t) \| = \sqrt {\left(- a \sin t / 2\right) ^ {2} + \left(a \cos t / \sqrt {2}\right) ^ {2} + \left(a \sin t / 2\right) ^ {2}} = \frac {a}{\sqrt {2}},
$$

从而有

$$
\int_ {\sigma} x z \mathrm{d} s = \int_ {0} ^ {2 \pi} (a / 2) ^ {2} \sin^ {2} t \cdot (a / \sqrt {2}) \mathrm{d} t = \frac {\pi a ^ {3}}{4 \sqrt {2}}.
$$

□

---

17.1 第一型曲线积分

49

## 习题 17.1

1. 设 $\sigma : [\alpha, \beta] \to \mathbb{R}^n$ 为可求长参数曲线, $\phi : [a, b] \to [\alpha, \beta]$ 为连续的可逆映射. 证明: $\sigma \circ \phi$ 和 $\sigma$ 具有相同的长度.

2. 设 $\sigma$ 为连续的可求长参数曲线, 证明: $L(\sigma) = \lim_{\|P\| \to 0} L(\sigma; P)$.

3. 计算下列空间曲线的长度:

(1) $x(t) = t, y(t) = t^2, z(t) = \frac{2}{3} t^3, t \in [0,1]$;
(2) $x(t) = t, y(t) = \ln \sec t, z(t) = \ln (\sec t + \tan t), 0 \leqslant t \leqslant \frac{\pi}{4}$;
(3) $x(t) = a\cos \omega t, y(t) = a\sin \omega t, z(t) = b\omega t, \omega > 0, 0 \leqslant t \leqslant \frac{2\pi}{\omega}$;
(4) $x + y + z = a$ $(|a| < \sqrt{3}), x^2 + y^2 + z^2 = 1.$

4. 计算下列曲线积分  $(a, b > 0)$ :

(1) $\int_{\sigma} y^2 \, \mathrm{d}s$, 其中 $\sigma$ 是摆线的一拱: $x(t) = a(t - \sin t)$, $y(t) = a(1 - \cos t)$, $0 \leqslant t \leqslant 2\pi$;

(2) $\int_{\sigma} y \, \mathrm{d}s$, 其中 $\sigma$ 是抛物线 $y^2 = 2ax$ 从 $(0,0)$ 到 $(2a,2a)$ 的部分;

(3) $\int_{\sigma} \sqrt{x^2 + y^2} \, \mathrm{d}s,$ 其中 $\sigma$ 是圆周 $x^2 + y^2 = ax;$

(4) $\int_{\sigma} y \, \mathrm{d}s$, 其中 $\sigma$ 是椭圆 $\frac{x^2}{a^2} + \frac{y^2}{b^2} = 1$ 在 $x$ 轴上方的部分;

(5) $\int_{\sigma} x^{2} \, \mathrm{d}s$, 其中 $\sigma$ 是圆周 $x^{2} + y^{2} + z^{2} = a^{2}$, $x + y + z = 0$;

(6) $\int_{\sigma}(x + y)\mathrm{d}s,$ 其中 $\sigma$ 是顶点为 $(0,0),(1,0),(0,1)$ 的三角形.

5. 形状为椭圆 $\frac{x^2}{a^2} + \frac{y^2}{b^2} = 1$ 的物质在 $(x, y)$ 处的密度为 $\rho(x, y) = |y|$, 求其质量.

6. 设某种物质均匀分布在摆线 $\sigma(t) = (a(t - \sin t), a(1 - \cos t))$ ($0 \leqslant t \leqslant \pi$) 上, 求该物质的质心.

7. 定义平面参数曲线  $\sigma(x)=(x,y(x))$  为

$$
y (x) = \left\{ \begin{array}{l l} x \cos \frac {1}{x}, & 0 <   x \leqslant \pi / 2, \\ 0, & x = 0. \end{array} \right.
$$

验证  $\sigma$  连续但不是可求长参数曲线.

8. 设 $\sigma : [\alpha, \beta] \to \mathbb{R}^n$ 为连续单射. 如果 $\sigma$ 为可求长参数曲线, 证明:

$$
\lim _ {m \to \infty} \sup \left\{| t ^ {\prime \prime} - t ^ {\prime} | \Big | L (\sigma | _ {[ t ^ {\prime}, t ^ {\prime \prime} ]}) \leqslant \frac {1}{m} \right\} = 0.
$$

9. 设  $f \in C^{1}[\alpha, \beta]$ ，证明:

$$
\bigvee_ {\alpha} ^ {\beta} (f) = \int_ {\alpha} ^ {\beta} | f ^ {\prime} (t) |   \mathrm{d} t.
$$

---

50

第十七章 曲线积分与曲面积分

10. 设 $\sigma : [\alpha, \beta] \to \mathbb{R}^n$ 为连续的可求长参数曲线, $n \geqslant 2$. 证明: $\sigma([\alpha, \beta])$ 为 $\mathbb{R}^n$ 中的零测集, 由此说明Peano曲线不是可求长参数曲线.

## 17.2 第二型曲线积分

我们考虑一个新的物理问题: 设质点在力场 F 中沿一条曲线  $\sigma$  运动, 求力场 F 对该质点所做的功. 我们还是可以用 “微元法” 将这个问题转化为曲线上的一个积分问题. 力场 F 沿  $\sigma|_{[t,t+\delta t]}$  这一小段所做的功记为  $\delta W$ , 则

$$
\delta W \approx \boldsymbol {F} (\sigma (t)) \cdot [ \sigma (t + \delta t) - \sigma (t) ].
$$

当 $\sigma$ 为 $C^1$ 曲线时，

$$
\delta W \approx \boldsymbol {F} (\sigma (t)) \cdot \sigma^ {\prime} (t) \delta t,
$$

于是总的功 $W$ 可以表示为

$$
W = \int_ {\alpha} ^ {\beta} \boldsymbol {F} (\sigma (t)) \cdot \sigma^ {\prime} (t)   \mathrm{d} t.
$$

一般地, 设 $\sigma : [\alpha, \beta] \to \mathbb{R}^n$ 为参数曲线, $F$ 是定义在 $\sigma$ 上取值在 $\mathbb{R}^n$ 中的向量值函数. 任取 $[\alpha, \beta]$ 的一个分割

$$
\mathrm{P}: \alpha = t _ {0} <   t _ {1} <   t _ {2} <   \dots <   t _ {m} = \beta ,
$$

如果极限 $\lim_{\| P\| \to 0}\sum_{j = 1}^{m}\pmb {F}(\sigma (\xi_j))\cdot [\sigma (t_j) - \sigma (t_{j - 1})]$ 存在且与 $\{\xi_j\in [t_{j - 1},t_j]\}$ 的选取无关，则称此极限为 $\pmb{F}$ 沿曲线 $\sigma$ 的第二型曲线积分，记为

$$
\int_ {\sigma} f _ {1} \mathrm{d} x _ {1} + f _ {2} \mathrm{d} x _ {2} + \dots + f _ {n} \mathrm{d} x _ {n} = \int_ {\sigma} \boldsymbol {F} \cdot \mathrm{d} \vec {s},
$$

其中  $\boldsymbol{F}=(f_{1},f_{2},\cdots,f_{n}),\mathrm{d}\vec{s}=(\mathrm{d}x_{1},\mathrm{d}x_{2},\cdots,\mathrm{d}x_{n})$ . 对于分段  $C^{1}$  曲线, 第二型曲线积分可以转化为 Riemann 积分:

$$
\int_ {\sigma} f _ {1} \mathrm{d} x _ {1} + f _ {2} \mathrm{d} x _ {2} + \dots + f _ {n} \mathrm{d} x _ {n} = \int_ {\alpha} ^ {\beta} \boldsymbol {F} (\sigma) \cdot \boldsymbol {\sigma} ^ {\prime} (t) \mathrm{d} t, \tag {17.2.1}
$$

其中  $\sigma'(t)=(x_{1}^{\prime}(t),x_{2}^{\prime}(t),\cdots,x_{n}^{\prime}(t))$  为曲线  $\sigma$  的切向量.

初看起来第二型曲线积分似乎和第一型曲线积分并无本质不同. 但这两类积分有一个重要的区别, 这个区别和曲线的方向有关. 为了说明这一点, 我们考虑曲线的重新参

---

17.2 第二型曲线积分

51

数化. 设 $\phi : [\gamma, \delta] \to [\alpha, \beta]$ 为严格单调的可逆连续映射, 则复合映射 $\sigma \circ \phi : [\gamma, \delta] \to \mathbb{R}^n$ 也是一条参数曲线, 它和 $\sigma$ 的像完全相同, 这两条参数曲线只是选取了不同的参数而已. 如果 $\phi$ 是严格单调递增的, 则称这两个参数是同向的; 如果 $\phi$ 是严格单调递减的, 则称这两个参数是反向的 (不同向).

从定义不难看出, 对于同向的两个参数, 第二曲线积分的值不变; 而对于反向的两个参数, 第二型曲线积分的值正好相差一个符号! 这和第一型曲线积分不同, 比如曲线的长度就不依赖于参数的选取. 因此, 为了使第二型曲线积分有意义, 我们总是要给曲线指定一个方向, 这个方向是由某个参数决定的. 给定了方向的曲线称为有向曲线.

设 $f \in R[a, b]$, 则 $f$ 在 $[a, b]$ 上的 Riemann 积分可视为 $f$ 沿区间 $[a, b]$ 的第二型曲线积分, 其中区间 $[a, b]$ 作为一条曲线, 其方向是参数 $x$ 给出的, 即 $x$ 轴的正向. 我们之所以规定

$$
\int_ {b} ^ {a} f (x) \mathrm{d} x = - \int_ {a} ^ {b} f (x) \mathrm{d} x,
$$

就是因为 $f$ 沿 $[a,b]$ 的相反方向的第二型曲线积分要变一个符号.

如果 $\sigma$ 为一条闭曲线 (环路), 即 $\sigma(\alpha) = \sigma(\beta)$, 则选定了方向以后, 不论从曲线上哪一点出发, 沿此闭曲线的第二型曲线积分的值不变, 这样的积分常记为

$$
\oint_ {\sigma} f _ {1} \mathrm{d} x _ {1} + f _ {2} \mathrm{d} x _ {2} + \dots + f _ {n} \mathrm{d} x _ {n}.
$$

平面上的单位圆周  $S^{1}$  就是一条闭曲线, 如果用参数方程

$$
\sigma (t) = (\cos t, \sin t), \quad t \in [ 0, 2 \pi ]
$$

表示, 则  $S^{1}$  的方向就是所谓逆时针方向.

例17.2.1 计算第二型曲线积分

$$
I = \oint_ {\sigma} \frac {y}{x ^ {2} + y ^ {2}} \mathrm{d} x - \frac {x}{x ^ {2} + y ^ {2}} \mathrm{d} y,
$$

其中  $\sigma$  为圆周  $x^{2} + y^{2} = a^{2}$ ，方向为逆时针方向 (图 17.4).

![](../../raw/pages_0689-0704/images/page_692_image_15.jpg)

<details>
<summary>text_image</summary>

y
a
O
a
x
</details>

图 17.4 圆周 (逆时针方向)

---

52

第十七章 曲线积分与曲面积分

解 按照给定的方向取 $\sigma$ 的参数方程为

$$
x (t) = a \cos t, y (t) = a \sin t, t \in [ 0, 2 \pi ].
$$

此时有

$$
I = \int_ {0} ^ {2 \pi} \frac {1}{a ^ {2}} \left[ a \sin t (a \cos t) ^ {\prime} - a \cos t (a \sin t) ^ {\prime} \right] \mathrm{d} t = - 2 \pi .
$$

例17.2.2 计算第二型曲线积分

$$
I = \oint_ {\sigma} (y - z)   \mathrm{d} x + (z - x)   \mathrm{d} y + (x - y)   \mathrm{d} z,
$$

其中 $\sigma$ 是圆周 $x^{2} + y^{2} + z^{2} = a^{2}, y = x\tan \alpha (0 <   \alpha <  \pi /2)$ ，从 $x$ 的正向看去， $\sigma$ 的方向是逆时针的(图17.5).

![](../../raw/pages_0689-0704/images/page_693_image_9.jpg)

<details>
<summary>text_image</summary>

y
a
α
O
x
a
</details>

图17.5 球面圆

解 根据方向取 $\sigma$ 的参数方程为

$$
x (\theta) = a \cos \theta \cos \alpha , y (\theta) = a \cos \theta \sin \alpha , z (\theta) = a \sin \theta,
$$

其中 $\theta \in [0,2\pi]$. 于是所求积分为

$$
\begin{array}{l} I = \int_ {0} ^ {2 \pi} (a \cos \theta \sin \alpha - a \sin \theta) (- a \sin \theta \cos \alpha) \mathrm{d} \theta + (a \sin \theta - a \cos \theta \cos \alpha) \times \\ (- a \sin \theta \sin \alpha) \mathrm{d} \theta + (a \cos \theta \cos \alpha - a \cos \theta \sin \alpha) a \cos \theta \mathrm{d} \theta \\ = \int_ {0} ^ {2 \pi} a ^ {2} (\cos \alpha - \sin \alpha) \mathrm{d} \theta = 2 \pi a ^ {2} (\cos \alpha - \sin \alpha). \\ \end{array}
$$

例 17.2.3 考虑位于原点处的电荷 q 产生的静电场, 计算单位正电荷沿  $C^{1}$  曲线  $\sigma$  从点  $A = \sigma(\alpha)$  运动到点  $B = \sigma(\beta)$  时电场所做的功 W (图 17.6).

解 根据库仑定律, $(x,y,z)$ 处的单位正电荷在静电场中所受的力为

$$
\boldsymbol {F} = \frac {\kappa q}{r ^ {3}} (x, y, z) = \nabla \phi ,
$$

---

17.2 第二型曲线积分

53

其中 $\kappa$ 为常数, $\phi = -\kappa q / r$, $r = \sqrt{x^2 + y^2 + z^2}$. 因此 $\pmb{F}$ 沿 $\sigma$ 所做的功为

$$
\begin{array}{l} W = \int_ {\alpha} ^ {\beta} \boldsymbol {F} (\sigma) \cdot \sigma^ {\prime} (t) \mathrm{d} t \\ = \int_ {\alpha} ^ {\beta} (\phi \circ \sigma) ^ {\prime} \mathrm{d} t \\ = \frac {\kappa q}{r (\alpha)} - \frac {\kappa q}{r (\beta)}. \\ \end{array}
$$

这说明,静电场所做的功只与电荷的起始位置和终点位置有关,与具体运动路径无关.□

![](../../raw/pages_0689-0704/images/page_694_image_5.jpg)

<details>
<summary>text_image</summary>

y
σ(α)
F
q
x
z
σ(β)
</details>

图17.6 电场做功

## 习题 17.2

1. 计算下列第二型曲线积分:

(1) $\int_{\sigma} x \, \mathrm{d}x + y \, \mathrm{d}y + z \, \mathrm{d}z,$ 其中 $\sigma$ 是从 (1,1,1) 到 (2,3,4) 的直线段;
(2) $\int_{\sigma}(x^{2} + y^{2})\mathrm{d}x + (x^{2} - y^{2})\mathrm{d}y,$ 其中 $\sigma$ 是以(1,0)，(2,0)，(2,1)，(1,1)为顶点的正方形，逆时针方向；
(3) $\oint_{\sigma} \frac{(x + y) \, \mathrm{d}x - (x - y) \, \mathrm{d}y}{x^2 + y^2}$, 其中 $\sigma$ 是圆 $x^2 + y^2 = a^2$, 逆时针方向;
(4) $\int_{\sigma}(x^2 - 2xy)\mathrm{d}x + (y^2 - 2xy)\mathrm{d}y,$ 其中 $\sigma$ 是抛物线 $y = x^{2}$ 从 $(-1,1)$ 到(1,1)的一段；
(5) $\oint_{\sigma}(x + y)\mathrm{d}x + (x - y)\mathrm{d}y,$ 其中 $\sigma$ 是椭圆 $\frac{x^2}{a^2} +\frac{y^2}{b^2} = 1,$ 逆时针方向.

2. 计算第二型曲线积分

$$
\int_ {\sigma} (y - z) \mathrm{d} x + (z - x) \mathrm{d} y + (x - y) \mathrm{d} z,
$$

其中 $\sigma$ 是椭圆 $x^{2} + y^{2} = 1, x + z = 1,$ 从 $x$ 的正向看去，$\sigma$ 为顺时针方向.

3. 计算第二型曲线积分

$$
\int_ {\sigma} (y ^ {2} - z ^ {2}) \mathrm{d} x + (z ^ {2} - x ^ {2}) \mathrm{d} y + (x ^ {2} - y ^ {2}) \mathrm{d} z,
$$

---

54

第十七章 曲线积分与曲面积分

其中 $\sigma$ 是球面三角形 $x^{2} + y^{2} + z^{2} = 1, x \geqslant 0, y \geqslant 0, z \geqslant 0$ 的边界，从球外看去，$\sigma$ 为逆时针方向.

4. 计算第二型曲线积分  $\oint_{\sigma}\frac{y\,dx-x\,dy}{x^{2}+y^{2}}$ ，其中  $\sigma$  是椭圆  $\frac{x^{2}}{a^{2}}+\frac{y^{2}}{b^{2}}=1$ ，顺时针方向.

5. 求力场 F 对运动的单位质点所做的功, 此质点沿曲线  $\sigma$  从 A 点运动到 B 点:

(1) $F=(x-2xy^{2},y-2x^{2}y)$ ，其中 $\sigma$ 是平面曲线 $y=x^{2},A=(0,0),B=(1,1);$

(2) $F=(x-y,y-z,z-x)$ ，其中 $\sigma(t)=(t,t^{2},t^{3})$ ， $A=(0,0,0)$ ， $B=(1,1,1)$ .

6. 计算质量为 $m$ 的质点在重力场的作用下沿曲线 $\sigma$ 从点 $A = \sigma(\alpha)$ 运动到点 $B = \sigma(\beta)$ 时所做的功 $W$.

7. 设  $P(x,y)$ ,  $Q(x,y)$  在可求长曲线  $\sigma$  上连续, 证明:

$$
\left| \int_ {\sigma} P (x, y)   \mathrm{d} x + Q (x, y)   \mathrm{d} y \right| \leqslant L (\sigma) M,
$$

其中 $M = \sup_{\sigma}\sqrt{P^2 + Q^2}$

8. 设 $\sigma$ 为圆周 $x^{2} + y^{2} = R^{2}$, 方向为逆时针. 利用上一题证明 $\lim_{R\to +\infty}I_R = 0$, 其中

$$
I _ {R} = \oint_ {\sigma} \frac {y \mathrm{d} x - x \mathrm{d} y}{(x ^ {2} + x y + y ^ {2}) ^ {2}}.
$$

## 17.3 第一型曲面积分

我们从参数曲面的面积开始. 设 $m \leqslant n$, $\Omega$ 为 $\mathbb{R}^m$ 中的开集. 映射 $\varphi: \Omega \to \mathbb{R}^n$ 称为 $\mathbb{R}^n$ 中的参数曲面, 我们想要定义参数曲面的面积.

先从线性映射开始. 设 $\varphi: \mathbb{R}^m \to \mathbb{R}^n$ 为线性映射, $I \subset \mathbb{R}^m$ 为矩形 (图17.7). 如果 $\varphi$ 是退化的 (秩小于 $m$), 则 $\varphi(\mathbb{R}^m)$ 包含在一个维数小于 $m$ 的子向量空间中, 我们自然定义 $\varphi(I)$ 的 $m$ 维容积为零; 如果 $\varphi$ 非退化, 则 $\varphi(\mathbb{R}^m)$ 维数为 $m$, $\varphi(I)$ 为 $m$ 维欧氏空间中的 Jordan 可测集, 我们来计算它的 $m$ 维容积. 以下为了区分不同维数的容积, 我们将 $m$ 维容积称为面积, 并用记号 $\sigma$ 来表示它.

![](../../raw/pages_0689-0704/images/page_695_image_16.jpg)

<details>
<summary>text_image</summary>

I
R^m
φ
R^n
φ(I)
O
</details>

图 17.7 矩形在线性映射下的像

---

17.3 第一型曲面积分

55

不妨设 $I = [0,1]^m$ 记 $\pmb{v}_j = \varphi (\pmb{e}_j)$ ，其中 $\{\pmb{e}_j\}_{j = 1}^m$ 为 $\mathbb{R}^m$ 的一组标准基.则

$$
\varphi (I) = \left\{\sum_ {j = 1} ^ {m} x _ {j} \boldsymbol {v} _ {j}   \Big |   0 \leqslant x _ {j} \leqslant 1, j = 1, 2, \dots , m \right\}.
$$

我们要计算 $\varphi (I)$ 的面积. 先看 $m = 2$ 的情形. 此时, $\varphi (I)$ 是由 $\pmb{v}_1, \pmb{v}_2$ 所张成的平行四边形 (图17.8).

![](../../raw/pages_0689-0704/images/page_696_image_5.jpg)

<details>
<summary>text_image</summary>

y
v₂
v₁
O
x
z
</details>

图 17.8 平行四边形

设  $v_{1}, v_{2}$  的夹角为  $\theta$ ，从几何的角度我们就有

$$
\sigma (\varphi (I)) = \| \boldsymbol {v} _ {1} \| \cdot \| \boldsymbol {v} _ {2} \| \cdot \sin \theta .
$$

利用 $\pmb{v}_1\cdot \pmb{v}_2 = \| \pmb {v}_1\| \cdot \| \pmb {v}_2\| \cdot \cos \theta$ 可得

$$
\begin{array}{l} \left| \sigma (\boldsymbol {\varphi} (I)) \right| ^ {2} = \left\| \boldsymbol {v} _ {1} \right\| ^ {2} \cdot \left\| \boldsymbol {v} _ {2} \right\| ^ {2} - \left(\boldsymbol {v} _ {1} \cdot \boldsymbol {v} _ {2}\right) ^ {2} \\ = \det \left(\boldsymbol {v} _ {i} \cdot \boldsymbol {v} _ {j}\right) _ {2 \times 2}. \\ \end{array}
$$

当 n=3 时, 利用外积上式还可表示为  $\sigma(\varphi(I))=\|\boldsymbol{v}_{1}\times\boldsymbol{v}_{2}\|$ .

一般地, 我们断言 $\sigma(\varphi(I)) = \sqrt{\det\left(\boldsymbol{v}_i \cdot \boldsymbol{v}_j\right)_{m \times m}}$. 当 $m = n - 1$ 时, 利用 $\mathbb{R}^n$ 中外积运算的性质还可得到

$$
\sigma (\varphi (I)) = \| \boldsymbol {v} _ {1} \times \boldsymbol {v} _ {2} \times \dots \times \boldsymbol {v} _ {n - 1} \|\cdot
$$

事实上, 以 $\{\pmb{v}_i\}_{i=1}^m$ 为列向量的矩阵记为 $\pmb{A}$. 当 $m = n$ 时, 由例 16.4.1 可知

$$
\sigma (\boldsymbol {\varphi} (I)) = | \det \boldsymbol {A} | = \sqrt {\det (\boldsymbol {A} ^ {\mathrm{T}} \boldsymbol {A})} = \sqrt {\det (\boldsymbol {v} _ {i} \cdot \boldsymbol {v} _ {j}) _ {m \times m}}.
$$

当 $n > m$ 时, 选取正交变换 $\mathbf{O}:\mathbb{R}^n\to \mathbb{R}^n$ ，使得

$$
\{\boldsymbol {O} (\boldsymbol {v} _ {i}) \} _ {i = 1} ^ {m} \subset \mathbb {R} ^ {m} \times \{0 \} \subset \mathbb {R} ^ {n}.
$$

假定面积在正交变换下具有不变性, 则有

$$
\sigma (\varphi (I)) = \sqrt {\det \left(\boldsymbol {O} (\boldsymbol {v} _ {i}) \cdot \boldsymbol {O} (\boldsymbol {v} _ {j})\right) _ {m \times m}} = \sqrt {\det \left(\boldsymbol {v} _ {i} \cdot \boldsymbol {v} _ {j}\right) _ {m \times m}}
$$

---

56

第十七章 曲线积分与曲面积分

一般地, 如果 $\Omega$ 为 $\mathbb{R}^m$ 中的 Jordan 可测集, 则 $\varphi(\Omega)$ 为 $\mathbb{R}^n$ 中一个 $m$ 维子空间中的 Jordan 可测集, 且

$$
\sigma (\boldsymbol {\varphi} (\Omega)) = \sqrt {\det \left(\boldsymbol {A} ^ {\mathrm{T}} \boldsymbol {A}\right)} \sigma (\Omega). \tag {17.3.1}
$$

考虑一般的参数曲面  $\varphi: \Omega \rightarrow R^{n}$ ，我们假设  $\varphi$  是  $C^{1}$  映射。取  $\boldsymbol{x}^{0} = (x_{1}^{0}, x_{2}^{0}, \cdots, x_{m}^{0}) \in \Omega$ ，设  $J\varphi(\boldsymbol{x}^{0})$  非退化（秩为 m），定义  $L: R^{m} \rightarrow R^{n}$  为

$$
\boldsymbol {L} (\boldsymbol {x}) = \varphi (\boldsymbol {x} ^ {0}) + J \varphi (\boldsymbol {x} ^ {0}) (\boldsymbol {x} - \boldsymbol {x} ^ {0}), \quad \boldsymbol {x} \in \mathbb {R} ^ {m}.
$$

在  $x^{0}$  附近取小矩形  $\delta I = [x_{1}^{0}, x_{1}^{0} + \delta u_{1}] \times [x_{2}^{0}, x_{2}^{0} + \delta u_{2}] \times \cdots \times [x_{m}^{0}, x_{m}^{0} + \delta u_{m}]$ ，在  $x^{0}$  附近，由  $\varphi(\boldsymbol{x}) = \boldsymbol{L}(\boldsymbol{x}) + o(\|\boldsymbol{x} - \boldsymbol{x}^{0}\|)$  可得

$$
\delta \sigma = \sigma (\varphi (\delta I)) \approx \sigma (\boldsymbol {L} (\delta I)) = \sqrt {\det [ (J \varphi) ^ {\mathrm{T}} (\boldsymbol {x} ^ {0}) J \varphi (\boldsymbol {x} ^ {0}) ]} \delta u _ {1} \delta u _ {2} \dots \delta u _ {m}.
$$

于是我们自然用积分来表示  $C^{1}$  参数曲面的面积.

定义 17.3.1 (面积公式) 设  $\varphi: \Omega \rightarrow R^{n}$  为非退化的  $C^{1}$  映射,  $\Omega$  为  $R^{m}$  中的 Jordan 可测集, 则  $\varphi(\Omega)$  的面积定义为

$$
\sigma (\varphi (\Omega)) = \int_ {\varphi (\Omega)} \mathrm{d} \sigma = \iint \dots \int_ {\Omega} \sqrt {\det [ (J \varphi) ^ {\mathrm{T}} J \varphi ]} \mathrm{d} u _ {1} \mathrm{d} u _ {2} \dots \mathrm{d} u _ {m}. \tag {17.3.2}
$$

注 17.3.1 (1) 如果 m = 1，则 (17.3.2) 就是  $C^{1}$  曲线的弧长公式.

(2) 与曲线一样, 曲面可以选取不同的参数化. 如果 $\phi: \Omega' \to \Omega$ 是 $C^1$ 的可逆映射, 则 $\varphi \circ \phi: \Omega' \to \mathbb{R}^m$ 也是参数曲面, 它们的面积用 (17.3.2) 式定义出来是一致的.

设  $R^{3}$  中  $C^{1}$  参数曲面由  $\boldsymbol{r}(u,v)=(x(u,v),y(u,v),z(u,v))((u,v)\in D)$  给出，则其面积为

$$
\sigma = \iint_ {D} \| \boldsymbol {r} _ {u} \times \boldsymbol {r} _ {v} \| \mathrm{d} u \mathrm{d} v = \iint_ {D} \sqrt {E G - F ^ {2}} \mathrm{d} u \mathrm{d} v, \tag {17.3.3}
$$

其中

$$
E = \boldsymbol {r} _ {u} \cdot \boldsymbol {r} _ {u} = x _ {u} ^ {2} + y _ {u} ^ {2} + z _ {u} ^ {2}, G = \boldsymbol {r} _ {v} \cdot \boldsymbol {r} _ {v} = x _ {v} ^ {2} + y _ {v} ^ {2} + z _ {v} ^ {2},
$$

$$
F = \boldsymbol {r} _ {u} \cdot \boldsymbol {r} _ {v} = x _ {u} x _ {v} + y _ {u} y _ {v} + z _ {u} z _ {v}.
$$

特别地, 当曲面由方程 $z = f(x, y)$, $((x, y) \in D)$ 给出时, $\boldsymbol{r}_x = (1, 0, f_x)$, $\boldsymbol{r}_y = (0, 1, f_y)$, 此时

$$
E G - F ^ {2} = (1 + f _ {x} ^ {2}) (1 + f _ {y} ^ {2}) - (f _ {x} f _ {y}) ^ {2} = 1 + f _ {x} ^ {2} + f _ {y} ^ {2},
$$

曲面的面积公式成为

$$
\sigma = \iint_ {D} \sqrt {1 + f _ {x} ^ {2} + f _ {y} ^ {2}} \mathrm{d} x \mathrm{d} y. \tag {17.3.4}
$$

---

17.3 第一型曲面积分

57

例 17.3.1 设 a > 0, 求球面  $x^{2} + y^{2} + z^{2} = a^{2}$  的面积.

解 球面的参数表示为

$$
x = a \sin \varphi \cos \theta , y = a \sin \varphi \sin \theta , z = a \cos \varphi , \varphi \in [ 0, \pi ], \theta \in [ 0, 2 \pi ].
$$

此时

$$
\boldsymbol {r} _ {\varphi} = (a \cos \varphi \cos \theta , a \cos \varphi \sin \theta , - a \sin \varphi), \quad \boldsymbol {r} _ {\theta} = (- a \sin \varphi \sin \theta , a \sin \varphi \cos \theta , 0).
$$

由此可以算出 $EG - F^2 = a^4\sin^2\varphi$ ，从而球面的面积为

$$
\sigma = \int_ {0} ^ {2 \pi} \mathrm{d} \theta \int_ {0} ^ {\pi} a ^ {2} \sin \varphi \mathrm{d} \varphi = 4 \pi a ^ {2}.
$$

![](../../raw/pages_0689-0704/images/page_698_image_9.jpg)

一般地, 设  $\varphi: \Omega \rightarrow R^{n}$  为超曲面, 其中

$$
\varphi (\boldsymbol {u}) = \varphi (u _ {1}, u _ {2}, \dots , u _ {n - 1}), \quad \boldsymbol {u} = (u _ {1}, u _ {2}, \dots , u _ {n - 1}) \in \Omega .
$$

超曲面的切向量为  $\varphi_{u_{1}},\varphi_{u_{2}},\cdots,\varphi_{u_{n-1}}$ . 根据前面的讨论, 超曲面的面积为

$$
\sigma = \iint \dots \int_ {\Omega} \| \varphi_ {u _ {1}} \times \varphi_ {u _ {2}} \times \dots \times \varphi_ {u _ {n - 1}} \| \mathrm{d} u _ {1} \mathrm{d} u _ {2} \dots \mathrm{d} u _ {n - 1}. \tag {17.3.5}
$$

特别地, 设 $f: D \to \mathbb{R}$ 为 $C^1$ 函数, 其中 $D \subseteq \mathbb{R}^{n-1}$. 则 $\operatorname{graph}(f)$ 为 $\mathbb{R}^n$ 中的超曲面, 其面积公式为

$$
\sigma = \iint \dots \int_ {D} \sqrt {1 + \| \nabla f \| ^ {2}}   \mathrm{d} x _ {1}   \mathrm{d} x _ {2} \dots \mathrm{d} x _ {n - 1}, \tag {17.3.6}
$$

其中  $\nabla f = (f_{x_{1}}, f_{x_{2}}, \cdots, f_{x_{n-1}})$  是 f 的梯度. 事实上, graph(f) 的参数表示为

$$
\varphi (\boldsymbol {x}) = (x _ {1}, x _ {2}, \dots , x _ {n - 1}, f (x _ {1}, x _ {2}, \dots , x _ {n - 1})), \quad \boldsymbol {x} = (x _ {1}, x _ {2}, \dots , x _ {n - 1}) \in D.
$$

此时

$$
\varphi_ {x _ {1}} \times \varphi_ {x _ {2}} \times \dots \times \varphi_ {x _ {n - 1}} = (- 1) ^ {n} (f _ {x _ {1}}, f _ {x _ {2}}, \dots , f _ {x _ {n - 1}}, - 1).
$$

于是 $(17.3.6)$ 式可从 $(17.3.5)$ 式导出.

例 17.3.2 设 a > 0, 求  $\{x_{1} + x_{2} + \cdots + x_{n} = a, x_{i} \geqslant 0, i = 1, 2, \cdots, n\}$  的面积.
解 记

$$
\Delta_ {n - 1} (a) = \left\{x \in \mathbb {R} ^ {n - 1} \mid x _ {1} + x _ {2} + \dots + x _ {n - 1} \leqslant a, x _ {i} \geqslant 0, 1 \leqslant i \leqslant n - 1 \right\},
$$

则所考虑的曲面有如下参数表示:

$$
\varphi : \Delta_ {n - 1} (a) \to \mathbb {R} ^ {n}, \varphi (\boldsymbol {x}) = (\boldsymbol {x}, f (\boldsymbol {x})),
$$

---

58

第十七章 曲线积分与曲面积分

其中  $f(x)=a-x_{1}-\cdots-x_{n-1}$ . 由 (17.3.6) 式可得

$$
\sigma = \int_ {\Delta_ {n - 1} (a)} \sqrt {1 + \| \nabla f \| ^ {2}} \mathrm{d} \boldsymbol {x} = \int_ {\Delta_ {n - 1} (a)} \sqrt {n} \mathrm{d} \boldsymbol {x},
$$

由例16.3.7可得

$$
\sigma = \sqrt {n}   \sigma (\Delta_ {n - 1} (a)) = \frac {\sqrt {n}}{(n - 1) !} a ^ {n - 1}.
$$

例 17.3.3 设 a > 0, 求球面  $x^{2} + y^{2} + z^{2} + w^{2} = a^{2}$  的面积.

解 根据对称性, 只要计算上半球面的面积即可. 上半球面的方程为

$$
w = \sqrt {a ^ {2} - x ^ {2} - y ^ {2} - z ^ {2}}, x ^ {2} + y ^ {2} + z ^ {2} \leqslant a ^ {2},
$$

此时有

$$
1 + \| \nabla w \| ^ {2} = 1 + (- x / w) ^ {2} + (- y / w) ^ {2} + (- z / w) ^ {2} = (a / w) ^ {2}.
$$

根据 (17.3.6) 式可得

$$
\sigma = 2 \iiint_ {x ^ {2} + y ^ {2} + z ^ {2} \leqslant a ^ {2}} \frac {a}{\sqrt {a ^ {2} - x ^ {2} - y ^ {2} - z ^ {2}}} \mathrm{d} x \mathrm{d} y \mathrm{d} z.
$$

利用 $\mathbb{R}^3$ 中的球面坐标可得

$$
\sigma = 2 \int_ {0} ^ {a} \frac {a r ^ {2}}{\sqrt {a ^ {2} - r ^ {2}}} \mathrm{d} r \int_ {0} ^ {\pi} \sin \theta \mathrm{d} \theta \int_ {0} ^ {2 \pi} \mathrm{d} \varphi = 8 \pi \int_ {0} ^ {a} \frac {a r ^ {2}}{\sqrt {a ^ {2} - r ^ {2}}} \mathrm{d} r,
$$

在上式中利用变量代换 $r = a\sin t$ ，最后可得

$$
\sigma = 8 \pi \int_ {0} ^ {\frac {\pi}{2}} a ^ {3} \sin^ {2} t \mathrm{d} t = 2 \pi^ {2} a ^ {3}.
$$

值得指出的是, 我们定义参数曲面面积的方法与定义参数曲线长度的方法似乎有些不同. 参数曲线的长度可以用折线段的长度去逼近. 那么, 能否像参数曲线那样, 通过在参数曲面上取分点, 然后用以分点为顶点的多边形 (比如三角形) 的面积和去逼近参数曲面的面积呢? Schwarz 曾经举过一个例子 (圆柱面) 说明这样的定义方式是行不通的. 对于一般的曲面, 定义面积需要引入 Hausdorff 测度的概念, 进一步的讨论超出了本课程的范围, 有兴趣的读者可以参看几何测度论的著作.

有了参数曲面面积的定义, 我们可以讨论参数曲面上有界函数的积分, 为了简单起见, 只考虑连续函数的情形.

定义 17.3.2 (第一型曲面积分) 设  $\varphi: \Omega \rightarrow R^{n}$  为  $C^{1}$  的参数曲面, f 是定义在  $\Sigma = \varphi(\Omega)$  上的连续函数, 则 f 在  $\Sigma$  上的曲面积分定义为

$$
\int_ {\Sigma} f \mathrm{d} \sigma = \iint \dots \int_ {\Omega} f \circ \varphi \sqrt {\det \left[ (J \varphi) ^ {\mathrm{T}} J \varphi \right]} \mathrm{d} u _ {1} \mathrm{d} u _ {2} \dots \mathrm{d} u _ {m}.
$$

---

17.3 第一型曲面积分

59

第一型曲面积分的物理解释: 分布在曲面上的某种物质, 如果其密度函数为  $\rho$ , 则  $\rho$  在曲面上的积分就是物质的总质量.

例 17.3.4 计算曲面积分  $\int_{\Sigma}\frac{1}{z}d\sigma,$  其中  $\Sigma$  为球面  $x^{2}+y^{2}+z^{2}=a^{2}$  被平面 z=h (0<h<a) 所截下的顶部 (图 17.9).

![](../../raw/pages_0689-0704/images/page_700_image_4.jpg)

<details>
<summary>text_image</summary>

z
h
O
y
</details>

图17.9 球帽

解 $\Sigma$ 的方程为

$$
z = \sqrt {a ^ {2} - x ^ {2} - y ^ {2}}, x ^ {2} + y ^ {2} \leqslant a ^ {2} - h ^ {2}.
$$

因此

$$
\begin{array}{l} \int_ {\Sigma} \frac {1}{z} \mathrm{d} \sigma = \iint_ {x ^ {2} + y ^ {2} \leqslant a ^ {2} - h ^ {2}} \frac {1}{z} \sqrt {1 + z _ {x} ^ {2} + z _ {y} ^ {2}} \mathrm{d} x \mathrm{d} y \\ = \iint_ {x ^ {2} + y ^ {2} \leqslant a ^ {2} - h ^ {2}} \frac {a}{a ^ {2} - x ^ {2} - y ^ {2}} \mathrm{d} x \mathrm{d} y \\ = \int_ {0} ^ {\sqrt {a ^ {2} - h ^ {2}}} \frac {a r}{a ^ {2} - r ^ {2}} \mathrm{d} r \int_ {0} ^ {2 \pi} \mathrm{d} \theta \\ = 2 \pi a \ln (a / h). \\ \end{array}
$$

例 17.3.5 设抛物面  $z = 2 - (x^{2} + y^{2})$ ,  $z \geqslant 0$  上分布着密度为  $\rho(x, y) = x^{2} + y^{2}$  的物质 (图 17.10), 求该物质的质量.

![](../../raw/pages_0689-0704/images/page_700_image_11.jpg)

<details>
<summary>text_image</summary>

z
2
O
√2
y
</details>

图17.10 抛物面

解 该物质的质量 $m$ 为 $\rho(x, y) = x^2 + y^2$ 在曲面上的积分，即

$$
m = \iint_ {x ^ {2} + y ^ {2} \leqslant 2} (x ^ {2} + y ^ {2}) \sqrt {1 + z _ {x} ^ {2} + z _ {y} ^ {2}} \mathrm{d} x \mathrm{d} y
$$

---

60

第十七章 曲线积分与曲面积分

$$
\begin{array}{l} = \iint_ {x ^ {2} + y ^ {2} \leqslant 2} (x ^ {2} + y ^ {2}) \sqrt {1 + 4 (x ^ {2} + y ^ {2})} \mathrm{d} x \mathrm{d} y \\ = \int_ {0} ^ {\sqrt {2}} r ^ {2} \sqrt {1 + 4 r ^ {2}} r \mathrm{d} r \int_ {0} ^ {2 \pi} \mathrm{d} \theta \\ = \frac {1 4 9}{3 0} \pi . \\ \end{array}
$$

与重积分类似, 利用第一型曲面积分可以求面状物质的质心、转动惯量、引力等, 我们仅举一例加以说明.

例 17.3.6 设 a > 0，曲面  $\Sigma: x^{2} + y^{2} + z^{2} = a^{2}, x, y, z \geqslant 0$  上均匀分布着某种物质，求该物质的质心.

解 不妨设物质的密度为 1. 曲面的参数表示为

$$
x = a \sin \varphi \cos \theta , y = a \sin \varphi \sin \theta , z = a \cos \varphi , \varphi \in [ 0, \pi / 2 ], \theta \in [ 0, \pi / 2 ].
$$

记质心坐标为 $(\bar{x},\bar{y},\bar{z})$ ，则

$$
\bar {x} = \frac {1}{m} \int_ {\Sigma} x \mathrm{d} \sigma , \bar {y} = \frac {1}{m} \int_ {\Sigma} y \mathrm{d} \sigma , \bar {z} = \frac {1}{m} \int_ {\Sigma} z \mathrm{d} \sigma ,
$$

其中 $m = \sigma (\Sigma) = \frac{1}{2}\pi a^2$ .于是

$$
\bar {x} = \frac {2}{\pi a ^ {2}} \int_ {0} ^ {\frac {\pi}{2}} \mathrm{d} \theta \int_ {0} ^ {\frac {\pi}{2}} a \sin \varphi \cos \theta \cdot a ^ {2} \sin \varphi \mathrm{d} \varphi = \frac {1}{2} a.
$$

利用对称性可得  $\bar{y} = \bar{z} = \frac{1}{2}a.$

## 习题 17.3

1. 用重积分的变量替换公式证明: $C^1$ 参数曲面的面积与参数的选取无关.

2. 设 a > 0, 求 z = axy 包含在圆柱  $x^{2} + y^{2} = a^{2}$  内那部分的面积.

3. 设 a > 0, 计算球面  $x^{2} + y^{2} + z^{2} = a^{2}$  被柱面  $x^{2} + y^{2} = ax$  所截下那部分的面积.

4. 求曲面  $z = \sqrt{2xy}$  被平面  $x + y = 1, x = 1$  及 y = 1 所截下那部分的面积.

5. 设 a > 0, 计算  $R^{n}$  中的曲面  $|x_{1}| + |x_{2}| + \cdots + |x_{n}| = a$  的面积.

6. 设 $a > 0$, 证明: $\mathbb{R}^n$ 中半径为 $a$ 的球面的面积等于 $n\omega_n a^{n-1}$, 其中 $\omega_n$ 是 $\mathbb{R}^n$ 中半径为 1 的球体的容积.

7. 计算下列曲面积分  $(a, b, c > 0)$ :

(1) $\int_{\Sigma}(x + y + z)\mathrm{d}\sigma ,\Sigma$ 为 $x^{2} + y^{2} + z^{2} = a^{2},z\geqslant 0;$
(2) $\int_{\Sigma} \frac{\mathrm{d}\sigma}{(1 + x + y)^2}, \Sigma$ 为 $x + y + z = 1, x, y, z \geqslant 0;$

---

17.4 第二型曲面积分

61

(3) $\int_{\Sigma} \sqrt{x^2 / a^4 + y^2 / b^4 + z^2 / c^4} \, \mathrm{d}\sigma, \Sigma$ 为 $\frac{x^2}{a^2} + \frac{y^2}{b^2} + \frac{z^2}{c^2} = 1;$
(4) $\int_{\Sigma} xyz \, \mathrm{d}\sigma, \Sigma$ 为 $z = x^2 + y^2, z \leqslant 1;$
(5) $\int_{\Sigma}(x^2 + y^2) \, \mathrm{d}\sigma, \Sigma$ 为 $x^2 + y^2 + z^2 = a^2.$

8. 设 a > 0, 某种物质均匀分布在曲面  $z = \sqrt{x^{2} + y^{2}}$  被柱面  $x^{2} + y^{2} = ax$  所割下的部分上, 求该物质的质心.

9. 设球面  $x^{2} + y^{2} + z^{2} = a^{2}$  上分布着密度为  $\rho$  的均匀物质, 求该物质的引力场.

10. 用 $S^2$ 表示球面 $x^{2} + y^{2} + z^{2} = 1$. 当 $f$ 为连续函数, $\alpha, \beta, \gamma \in \mathbb{R}$ 时, 证明如下 Poisson 公式:

$$
\int_ {S ^ {2}} f (\alpha x + \beta y + \gamma z) \mathrm{d} \sigma = 2 \pi \int_ {- 1} ^ {1} f \big (u \sqrt {\alpha^ {2} + \beta^ {2} + \gamma^ {2}} \big) \mathrm{d} u.
$$

## 17.4 第二型曲面积分

我们来考虑一个物理问题: 设空间中有流速为 $V = (P, Q, R)$ 的流体, 求单位时间内该流体通过曲面 $\Sigma$ 的流量. 要计算流量, 必须给曲面指定方向. 我们规定, 曲面在某点的方向是指该点处的一个单位法向量. 指定方向以后, 可用所谓的“微元法”计算流量如下: 任取 $\Sigma$ 的一小片, 其面积记为 $\delta \sigma$, 经过这一小片的流体速度为 $V$, 曲面的单位法向量为 $n$, 则单位时间内通过这一小片曲面的流体的流量 $\delta \Phi$ 为 $V \cdot n \delta \sigma$. 于是单位时间内经过 $\Sigma$ 的流量 $\Phi$ 可以表示为积分

$$
\varPhi = \int_ {\Sigma} \boldsymbol {V} \cdot \boldsymbol {n} \mathrm{d} \sigma = \int_ {\Sigma} \boldsymbol {V} \cdot \mathrm{d} \vec {\sigma}, \tag {17.4.1}
$$

其中  $d\vec{\sigma}=n\,d\sigma$  称为有向面积元.

从 (17.4.1) 式可以看出, 流量与曲面方向的选取有关. 方向的变化可导致流量的数值相差一个正负号. 如果在曲面上存在连续的单位法向量场, 则称该曲面可定向, 否则就称该曲面不可定向. 本节所涉及的曲面都假定是可定向的. 对于可定向曲面, 其定向 (方向) 是指一个连续的单位法向量场 $n$.

为了计算 (17.4.1) 式中的积分, 我们通常要给曲面选取适当的参数表示. 设 $\varphi: D \to \mathbb{R}^3$ 为 $\Sigma$ 的参数表示, 其中

$$
\varphi (u, v) = \big (x (u, v), y (u, v), z (u, v) \big), (u, v) \in D.
$$

记 $N = \varphi_{u} \times \varphi_{v} = (y_{u}z_{v} - z_{u}y_{v}, z_{u}x_{v} - x_{u}z_{v}, x_{u}y_{v} - y_{u}x_{v})$, 则 $N$ 为曲面的法向量. 如果 $N / \| N\| = n$, 则称 $\varphi$ 是与给定定向相容的参数表示. 根据前节中的讨论, 曲面的面

---

62

第十七章 曲线积分与曲面积分

积元可写为 $\mathrm{d}\sigma = \| N\| \mathrm{d}u\mathrm{d}v$ 此时(17.4.1)式可写为

$$
\Phi = \iint_ {D} \boldsymbol {V} \cdot \boldsymbol {N} \mathrm{d} u \mathrm{d} v = \iint_ {D} \left[ P \frac {\partial (y , z)}{\partial (u , v)} + Q \frac {\partial (z , x)}{\partial (u , v)} + R \frac {\partial (x , y)}{\partial (u , v)} \right] \mathrm{d} u \mathrm{d} v. \tag {17.4.2}
$$

另一方面，记

$$
\mathrm{d} \vec {\sigma} = (\mathrm{d} y \land \mathrm{d} z, \mathrm{d} z \land \mathrm{d} x, \mathrm{d} x \land \mathrm{d} y),
$$

其中 $\mathrm{dy}\wedge \mathrm{dz}$ 表示有向面积元 $\mathrm{d}\vec{\sigma}$ 在 $yOz$ 平面上的投影， $\mathrm{dz}\wedge \mathrm{dx}$ 表示 $\mathrm{d}\vec{\sigma}$ 在 $zOx$ 平面上的投影， $\mathrm{dx}\wedge \mathrm{dy}$ 表示 $\mathrm{d}\vec{\sigma}$ 在 $xOy$ 平面上的投影.此时(17.4.1)式也可写为

$$
\varPhi = \int_ {\Sigma} \boldsymbol {V} \cdot \mathrm{d} \vec {\sigma} = \int_ {\Sigma} P \mathrm{d} y \wedge \mathrm{d} z + Q \mathrm{d} z \wedge \mathrm{d} x + R \mathrm{d} x \wedge \mathrm{d} y. \tag {17.4.3}
$$

由 $\mathrm{d}\vec{\sigma} = N\mathrm{d}u\mathrm{d}v$ 可见

$$
\mathrm{d} y \wedge \mathrm{d} z = \frac {\partial (y , z)}{\partial (u , v)} \mathrm{d} u \mathrm{d} v, \mathrm{d} z \wedge \mathrm{d} x = \frac {\partial (z , x)}{\partial (u , v)} \mathrm{d} u \mathrm{d} v, \mathrm{d} x \wedge \mathrm{d} y = \frac {\partial (x , y)}{\partial (u , v)} \mathrm{d} u \mathrm{d} v.
$$

由此也可以看出 (17.4.2) 式和 (17.4.3) 式是一回事. 我们规定以下关系式成立:

$$
\mathrm{d} z \wedge \mathrm{d} y = - \mathrm{d} y \wedge \mathrm{d} z, \quad \mathrm{d} x \wedge \mathrm{d} z = - \mathrm{d} z \wedge \mathrm{d} x, \quad \mathrm{d} y \wedge \mathrm{d} x = - \mathrm{d} x \wedge \mathrm{d} y.
$$

根据以上讨论, 我们可以提出如下定义:

定义 17.4.1 (第二型曲面积分) 设  $\Sigma$  为  $R^{3}$  中的可定向曲面, 其连续的单位法向量场为 n. 对于定义在  $\Sigma$  上的连续向量值函数  $\boldsymbol{X} = (P, Q, R)$ , 定义它在  $\Sigma$  上的第二型曲面积分为

$$
\varPhi = \int_ {\Sigma} \boldsymbol {X} \cdot \mathrm{d} \vec {\sigma} = \int_ {\Sigma} \boldsymbol {X} \cdot \boldsymbol {n} \mathrm{d} \sigma ,
$$

也记为

$$
\Phi = \int_ {\Sigma} P \mathrm{d} y \wedge \mathrm{d} z + Q \mathrm{d} z \wedge \mathrm{d} x + R \mathrm{d} x \wedge \mathrm{d} y.
$$

设 $\varphi$ 是该曲面的与给定定向相容的参数表示:

$$
\varphi (u, v) = \big (x (u, v), y (u, v), z (u, v) \big), (u, v) \in D.
$$

则第二型曲面积分可以化为重积分:

$$
\varPhi = \iint_ {D} \left[ P \frac {\partial (y , z)}{\partial (u , v)} + Q \frac {\partial (z , x)}{\partial (u , v)} + R \frac {\partial (x , y)}{\partial (u , v)} \right] \mathrm{d} u \mathrm{d} v.
$$

如果参数表示 $\varphi$ 与曲面上给定的定向不相容, 则用上式计算第二型曲面积分时要添加一个负号.

记 $n = (\cos \alpha, \cos \beta, \cos \gamma)$, 其中 $\alpha, \beta, \gamma$ 分别是 $n$ 与三个坐标轴的夹角. 当 $\cos \gamma \geqslant 0$, 即 $n$ 和 $z$ 轴的夹角不超过 $\pi / 2$ 时, $n$ 所决定的方向称为参数曲面的上侧方

---

17.4 第二型曲面积分

63

向; 反之, $n$ 所决定的方向称为参数曲面的下侧方向. 对于封闭的曲面, 指向曲面所围区域外部的单位法向量所决定的方向称为参数曲面的外侧方向, 指向曲面所围区域内部的单位法向量所决定的方向称为参数曲面的内侧方向 (图 17.11).

![](../../raw/pages_0705-0720/images/page_704_image_3.jpg)

<details>
<summary>text_image</summary>

n
</details>

(a)

![](../../raw/pages_0705-0720/images/page_704_image_5.jpg)

<details>
<summary>text_image</summary>

n
n
</details>

(b)

图 17.11 内法向和外法向

例 17.4.1 计算积分  $\int_{\Sigma} xyz \, dx \wedge dy$ ，其中  $\Sigma = \{x^{2} + y^{2} + z^{2} = 1, x \geqslant 0, y \geqslant 0\}$ ，方向为外侧.

解 将曲面分成两部分:

$$
\Sigma_ {1}: z = \sqrt {1 - x ^ {2} - y ^ {2}}, (x, y) \in D = \{x ^ {2} + y ^ {2} \leqslant 1, x \geqslant 0, y \geqslant 0 \},
$$

$$
\Sigma_ {2}: z = - \sqrt {1 - x ^ {2} - y ^ {2}}, (x, y) \in D = \{x ^ {2} + y ^ {2} \leqslant 1, x \geqslant 0, y \geqslant 0 \}.
$$

参数 $(x,y)$ 决定的法向量为 $(1,0,z_x)\times (0,1,z_y) = (-z_x, - z_y,1)$，因此，这个参数在 $\Sigma_{1}$ 上决定的方向就是外侧方向，在 $\Sigma_{2}$ 上决定的方向是内侧方向。于是

$$
\begin{array}{l} \int_ {\Sigma} x y z \mathrm{d} x \wedge \mathrm{d} y = \int_ {\Sigma_ {1}} x y z \mathrm{d} x \wedge \mathrm{d} y + \int_ {\Sigma_ {2}} x y z \mathrm{d} x \wedge \mathrm{d} y \\ = \iint_ {D} x y \sqrt {1 - x ^ {2} - y ^ {2}} \mathrm{d} x \mathrm{d} y - \iint_ {D} x y \left(- \sqrt {1 - x ^ {2} - y ^ {2}}\right) \mathrm{d} x \mathrm{d} y \\ = 2 \int_ {0} ^ {\frac {\pi}{2}} \mathrm{d} \theta \int_ {0} ^ {1} r ^ {3} \sin \theta \cos \theta \sqrt {1 - r ^ {2}} \mathrm{d} r = \frac {2}{1 5}. \\ \end{array}
$$

例17.4.2 计算积分 $\Phi = \int_{\Sigma} x^2 \, \mathrm{d}y \wedge \mathrm{d}z + y^2 \, \mathrm{d}z \wedge \mathrm{d}x + z^2 \, \mathrm{d}x \wedge \mathrm{d}y,$ 其中 $\Sigma$ 为球面 $(x - a)^2 + (y - b)^2 + (z - c)^2 = R^2,$ 方向为外侧.

解 球面的单位外法向量为 $R^{-1}(x - a, y - b, z - c)$, 于是

$$
\varPhi = \int_ {\Sigma} (x ^ {2}, y ^ {2}, z ^ {2}) \cdot R ^ {- 1} (x - a, y - b, z - c)   \mathrm{d} \sigma .
$$

记 $u = x - a, v = y - b, w = z - c, \Sigma' = \{u^2 + v^2 + w^2 = R^2\}$, 则

$$
\Phi = \frac {1}{R} \int_ {\Sigma^ {\prime}} \left(2 a u ^ {2} + 2 b v ^ {2} + 2 c w ^ {2} + \dots\right) \mathrm{d} \sigma ,
$$

---

64

第十七章 曲线积分与曲面积分

其中省略掉的项是关于 u, v, w 的一次幂项和三次幂项，由球面的对称性可知这些项的积分为零。同理， $u^{2}$ ， $v^{2}$ ， $w^{2}$  项的积分都相等，于是

$$
\begin{array}{l} \Phi = \frac {2 a + 2 b + 2 c}{3 R} \int_ {\Sigma^ {\prime}} \left(u ^ {2} + v ^ {2} + w ^ {2}\right) \mathrm{d} \sigma \\ = \frac {2 a + 2 b + 2 c}{3 R} R ^ {2} \cdot \sigma \left(\Sigma^ {\prime}\right) = \frac {2 a + 2 b + 2 c}{3 R} R ^ {2} \cdot 4 \pi R ^ {2} \\ = \frac {8 \pi}{3} (a + b + c) R ^ {3}. \\ \end{array}
$$

第二型积分可以推广到 $\mathbb{R}^n$ 中的可定向曲面上. 以超曲面为例, 设 $\Sigma$ 为 $\mathbb{R}^n$ 中的超曲面, 如果 $\Sigma$ 上存在连续的单位法向量场, 则称 $\Sigma$ 可定向. 我们用一个连续的单位法向量场 $n$ 来表示它的定向. 当 $X$ 为 $\Sigma$ 上的连续向量场时, 它在 $\Sigma$ 上的第二型曲面积分定义为

$$
\Phi = \int_ {\Sigma} \boldsymbol {X} \cdot \boldsymbol {n}   \mathrm{d} \sigma.
$$

记  $\boldsymbol{X}=(f_{1},f_{2},\cdots,f_{n})$ . 设  $\varphi:D\to R^{n}$  为  $\Sigma$  的参数表示, 其中  $D\subset R^{n-1}$ ,

$$
\begin{array}{l} \varphi (u _ {1}, u _ {2}, \dots , u _ {n - 1}) = (x _ {1} (u _ {1}, u _ {2}, \dots , u _ {n - 1}), x _ {2} (u _ {1}, u _ {2}, \dots , u _ {n - 1}), \dots , \\ x _ {n} (u _ {1}, u _ {2}, \dots , u _ {n - 1})), \quad (u _ {1}, u _ {2}, \dots , u _ {n - 1}) \in D. \\ \end{array}
$$

如果法向量  $\varphi_{u_{1}} \times \varphi_{u_{2}} \times \cdots \times \varphi_{u_{n-1}}$  与 n 同向, 则

$$
\begin{array}{l} \Phi = \int_ {D} \boldsymbol {X} \cdot \varphi_ {u _ {1}} \times \varphi_ {u _ {2}} \times \dots \times \varphi_ {u _ {n - 1}} \mathrm{d} u _ {1} \mathrm{d} u _ {2} \dots \mathrm{d} u _ {n - 1} \\ = \int_ {D} \sum_ {i = 1} ^ {n} (- 1) ^ {i - 1} f _ {i} \circ \varphi \frac {\partial \left(x _ {1} , x _ {2} , \cdots , \hat {x} _ {i} , \cdots , x _ {n}\right)}{\partial \left(u _ {1} , u _ {2} , \cdots , u _ {n - 1}\right)} \mathrm{d} u _ {1} \mathrm{d} u _ {2} \dots \mathrm{d} u _ {n - 1}, \\ \end{array}
$$

其中  $\hat{x}_{i}$  表示不含  $x_{i}$  这一项.

## 习题 17.4

1. 计算积分

$$
\Phi = \int_ {\Sigma} x \mathrm{d} y \wedge \mathrm{d} z + y \mathrm{d} z \wedge \mathrm{d} x + z \mathrm{d} x \wedge \mathrm{d} y,
$$

其中 $\Sigma$ 为三角形 $x + y + z = 1, x, y, z \geqslant 0$, 单位法向量与 (1,1,1) 同向.

2. 设某流体的流速为 $V = (yz, zx, xy)$，求该流体流出圆柱体 $x^2 + y^2 \leqslant a^2$，$0 \leqslant z \leqslant h$ 的流量.

3. 设某流体的流速为  $\boldsymbol{V} = (f(x), g(y), h(z))$ ，求该流体流出矩形  $[0, a] \times [0, b] \times [0, c]$  的流量.

---

17.4 第二型曲面积分

65

4. 计算积分

$$
\varPhi = \int_ {\Sigma} x \mathrm{d} y \wedge \mathrm{d} z + y \mathrm{d} z \wedge \mathrm{d} x + z \mathrm{d} x \wedge \mathrm{d} y,
$$

其中 $\Sigma$ 为球面 $(x - a)^2 + (y - b)^2 + (z - c)^2 = R^2$ ，方向为外侧.

5. 计算积分

$$
\varPhi = \int_ {\Sigma} x ^ {3}   \mathrm{d} y \wedge \mathrm{d} z,
$$

其中 $\Sigma$ 为上半椭球面 $\frac{x^2}{a^2} +\frac{y^2}{b^2} +\frac{z^2}{c^2} = 1 (z\geqslant 0)$ ，方向为上侧

6. 计算积分

$$
\Phi = \int_ {\Sigma} y z \mathrm{d} y \wedge \mathrm{d} z + z x \mathrm{d} z \wedge \mathrm{d} x + x y \mathrm{d} x \wedge \mathrm{d} y,
$$

其中  $\Sigma$  为四面体  $x + y + z \leqslant a, x \geqslant 0, y \geqslant 0, z \geqslant 0$  的外侧面.

7. 计算积分

$$
\varPhi = \int_ {\Sigma} x ^ {3} \mathrm{d} y \wedge \mathrm{d} z + y ^ {3} \mathrm{d} z \wedge \mathrm{d} x + z ^ {3} \mathrm{d} x \wedge \mathrm{d} y,
$$

其中  $\Sigma$  为球面  $x^{2}+y^{2}+z^{2}=a^{2}$ ，方向为内侧.

8. 计算积分

$$
\Phi = \int_ {\Sigma} x   \mathrm{d} y \wedge \mathrm{d} z \wedge \mathrm{d} w,
$$

其中  $\Sigma$  为球面  $x^{2}+y^{2}+z^{2}+w^{2}=a^{2}$ ，方向为外侧.
