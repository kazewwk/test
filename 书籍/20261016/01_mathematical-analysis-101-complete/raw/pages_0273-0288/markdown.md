对于第一项积分, 有

1. 当  $\ell = 1$  时,

$$
\int \frac {u}{u ^ {2} + \mu^ {2}} \mathrm{d} u = \frac {1}{2} \ln (u ^ {2} + \mu^ {2}) + c = \frac {1}{2} \ln (x ^ {2} + p x + q) + c.
$$

2. 当 $\ell > 1$ 时,

$$
\int \frac {u}{(u ^ {2} + \mu^ {2}) ^ {\ell}} \mathrm{d} u = \frac {1}{2 (1 - \ell)} (u ^ {2} + \mu^ {2}) ^ {1 - \ell} + c = \frac {1}{2 (1 - \ell)} (x ^ {2} + p x + q) ^ {1 - \ell} + c.
$$

对于第二项积分, 本质上是求不定积分

$$
\int \frac {1}{(u ^ {2} + \mu^ {2}) ^ {\ell}} \mathrm{d} u,
$$

这是前面例 8.3.4 中讨论过的情景.

综上, 原则上我们证明了下面的结论.

定理 8.4.2 有理函数的不定积分能积出来.

定理 8.4.1 给出了有理函数分解的结论, 从而从理论证明了有理函数一定能积出来, 但在具体计算中, 最关键的工作是分解  $Q(x)$  和确定诸多系数. 这是一件理论上思路明了但实际操作中比较烦琐的事情. 为了确定这些系数通常采用待定系数法. 但请注意, 虽然待定系数法本质上是求解线性方程组的问题, 理论上总是可解的, 但最好根据具体情况尝试一下是否有更合适的方法, 而不是墨守成规.

例 8.4.1 求不定积分  $\int\frac{1}{1+x^{3}}dx$ .

解 我们用待定系数法求解. 由于

$$
\frac {1}{1 + x ^ {3}} = \frac {1}{(1 + x) (x ^ {2} - x + 1)} = \frac {A}{x + 1} + \frac {B x + C}{x ^ {2} - x + 1},
$$

消去分母, 得

$$
1 = A (x ^ {2} - x + 1) + (B x + C) (1 + x),
$$

比较两端同次幂的系数, 可得

$$
A + B = 0, \quad - A + B + C = 0, \quad A + C = 1,
$$

有

$$
A = \frac {1}{3}, \quad B = - \frac {1}{3}, \quad C = \frac {2}{3}.
$$

因此

$$
\begin{array}{l} \int \frac {1}{1 + x ^ {3}} \mathrm{d} x = \frac {1}{3} \int \frac {1}{x + 1} \mathrm{d} x + \frac {1}{3} \int \frac {- x + 2}{x ^ {2} - x + 1} \mathrm{d} x \\ = \frac {1}{3} \ln | x + 1 | - \frac {1}{6} \ln (x ^ {2} - x + 1) + \frac {1}{2} \int \frac {1}{x ^ {2} - x + 1} \mathrm{d} x \\ = \frac {1}{3} \ln | x + 1 | - \frac {1}{6} \ln (x ^ {2} - x + 1) + \frac {1}{\sqrt {3}} \arctan \left(\frac {2}{\sqrt {3}} \left(x - \frac {1}{2}\right)\right) + c. \\ \end{array}
$$

例8.4.2 求不定积分 $I = \int \frac{1}{1 + x^4}\mathrm{d}x.$

解 我们完全可以按照上面例子中同样的做法, 即通过待定系数法进行计算. 考虑到分母的多项式的分解和后续的待定系数, 计算量将会比上一例题大得多. 因此, 我们尝试采用另一种做法, 引入另一个不定积分

$$
J = \int \frac {x ^ {2}}{1 + x ^ {4}} \mathrm{d} x.
$$

我们有

$$
\begin{array}{l} I + J = \int \frac {1 + x ^ {2}}{1 + x ^ {4}} \mathrm{d} x = \int \frac {\frac {1}{x ^ {2}} + 1}{\frac {1}{x ^ {2}} + x ^ {2}} \mathrm{d} x = \int \frac {\mathrm{d} \left(x - \frac {1}{x}\right)}{\left(x - \frac {1}{x}\right) ^ {2} + 2} \\ = \frac {1}{\sqrt {2}} \arctan \left(\frac {\sqrt {2}}{2} \left(x - \frac {1}{x}\right)\right) + c _ {1}. \\ \end{array}
$$

$$
\begin{array}{l} I - J = \int \frac {1 - x ^ {2}}{1 + x ^ {4}} \mathrm{d} x = \int \frac {\frac {1}{x ^ {2}} - 1}{\frac {1}{x ^ {2}} - x ^ {2}} \mathrm{d} x = - \int \frac {\mathrm{d} \left(x + \frac {1}{x}\right)}{\left(x + \frac {1}{x}\right) ^ {2} - 2} \\ = \frac {\sqrt {2}}{4} \left(\ln | x + \frac {1}{x} + \sqrt {2} | - \ln | x + \frac {1}{x} - \sqrt {2} |\right) + c _ {2}. \\ \end{array}
$$

因此，有

$$
I = \frac {\sqrt {2}}{8} \ln \left| \frac {x ^ {2} + \sqrt {2} x + 1}{x ^ {2} - \sqrt {2} x + 1} \right| + \frac {\sqrt {2}}{4} \arctan \left(\frac {\sqrt {2}}{2} \left(x - \frac {1}{x}\right)\right) + c.
$$

例8.4.3 求不定积分 $I = \int \frac{1 + x^4}{x^5 + x^4 - x^3 - x^2} \, \mathrm{d}x.$

解 因为

$$
x ^ {5} + x ^ {4} - x ^ {3} - x ^ {2} = x ^ {2} (x ^ {3} + x ^ {2} - x - 1) = x ^ {2} (x + 1) ^ {2} (x - 1).
$$

所以被积函数可以分解为

$$
\frac {1 + x ^ {4}}{x ^ {5} + x ^ {4} - x ^ {3} - x ^ {2}} = \frac {A}{x} + \frac {B}{x ^ {2}} + \frac {C}{x - 1} + \frac {D}{x + 1} + \frac {E}{(x + 1) ^ {2}}. \tag {8.4.1}
$$

为了确定这些系数, 可以在 (8.4.1) 式两端进行如下运算:

两端乘  $x^{2}$ ，再令 x=0，可得 B=-1。

两端乘 $x - 1$ ，再令 $x = 1$ ，可得 $C = \frac{1}{2}$

两端乘 $(x+1)^{2}$ ，再令x=-1，可得E=-1.

将 $B = -1, C = \frac{1}{2}, E = -1$ 代入 (8.4.1) 式并整理, 可得

$$
\frac {1 + x ^ {4}}{x ^ {2} (x - 1) (x + 1) ^ {2}} + \frac {1}{(x + 1) ^ {2}} = \frac {A}{x} - \frac {1}{x ^ {2}} + \frac {1}{2 (x - 1)} + \frac {D}{x + 1}. \tag {8.4.2}
$$

(8.4.2) 式两端乘 $x + 1$, 并令 $x \to -1$, 由于等式左端的极限为 $-\frac{1}{2}$, 右端的极限为 $D$, 故得 $D = -\frac{1}{2}$.

最后 (8.4.1) 式两端乘 $x$, 再令 $x \to \infty$, 可得 $A + C + D = 1$, 从而 $A = 1$. 从而得所求不定积分

$$
I = \ln | x | + \frac {1}{x} + \frac {1}{x + 1} + \frac {1}{2} \ln \left| \frac {x - 1}{x + 1} \right| + c.
$$

## 8.4.2 几类可有理化函数的不定积分

本节简要介绍以下几类函数的不定积分:

1. 三角函数有理式的不定积分
2. 形如  $\int R\left(x,\sqrt[p]{\frac{ax+b}{cx+d}},\cdots,\sqrt[q]{\frac{ax+b}{cx+d}}\right)\mathrm{d}x$  的不定积分
3. 形如 $\int R\left(x, \sqrt{ax^2 + bx + c}\right) \mathrm{d}x (a \neq 0)$ 的不定积分
4. 形如 $\int x^{m}(a + bx^{n})^{p}\mathrm{d}x$ 的不定积分

## 1. 三角函数有理式的不定积分

三角函数有理式是指形如 $R(\sin x, \cos x)$ 的函数, 其中 $R(u, v)$ 是二元有理函数, 后者是指两个二元多项式比值的函数, 即

$$
R (u, v) = \frac {P (u , v)}{Q (u , v)},
$$

其中  $P(u,v)$  和  $Q(u,v)$  都是二元多项式函数. 比如

$$
R (\sin x, \cos x) = \frac {1}{2 \sin x + 3 \cos x}
$$

就是三角函数的有理式, 而  $\sin\frac{1}{x}$  和  $\cos\sqrt{x}$  就不属于这类函数.

下面我们简要讨论三角函数有理式的不定积分

$$
I = \int R (\sin x, \cos x) \mathrm{d} x.
$$

我们证明,这类函数总可以通过所谓的万能变换

$$
t = \tan {\frac {x}{2}} \left(- \pi <   x <   \pi\right) \quad \text {或} \quad x = 2 \arctan t
$$

把它化为有理函数的积分, 从而总是可以积出来.

事实上, 注意到

$$
\sin x = 2 \sin \frac {x}{2} \cos \frac {x}{2} = \frac {2 \tan \frac {x}{2}}{1 + \tan^ {2} \frac {x}{2}} = \frac {2 t}{1 + t ^ {2}},
$$

$$
\cos x = \cos^ {2} \frac {x}{2} - \sin^ {2} \frac {x}{2} = \frac {1 - \tan^ {2} \frac {x}{2}}{1 + \tan^ {2} \frac {x}{2}} = \frac {1 - t ^ {2}}{1 + t ^ {2}},
$$

$$
\mathrm{d} x = \frac {2 \mathrm{d} t}{1 + t ^ {2}}.
$$

于是可把原来的不定积分化为

$$
I = \int R \left(\frac {2 t}{1 + t ^ {2}}, \frac {1 - t ^ {2}}{1 + t ^ {2}}\right) \frac {2 \mathrm{d} t}{1 + t ^ {2}}.
$$

由于有理函数的复合函数还是有理函数, 因此我们得到的关于 t 的被积函数的确是有理函数. 根据前面的讨论, 我们理论上证明了三角函数有理式的不定积分总是能积出来的.

注意, 在实际计算中可以视被积函数的具体情况, 采用灵活的变量替换, 比如 $t = \sin x$, $t = \cos x$, 或者 $t = \tan x$.

例8.4.4 求不定积分 $\int \frac{\mathrm{d}x}{\sin x + 2\cos x + 3}$

解 令 $t = \tan \frac{x}{2}$, 则有

$$
\begin{array}{l} \int \frac {\mathrm{d} x}{\sin x + 2 \cos x + 3} = 2 \int \frac {\mathrm{d} t}{t ^ {2} + 2 t + 5} \\ = 2 \int \frac {\mathrm{d} t}{(t + 1) ^ {2} + 4} = \arctan \frac {t + 1}{2} + c \\ = \arctan \left(\frac {1}{2} \left(1 + \tan \frac {x}{2}\right)\right) + c. \\ \end{array}
$$

例 8.4.5 求下面与著名的 Poisson 核函数有关的不定积分:

$$
\int \frac {(1 - r ^ {2}) \mathrm{d} x}{1 - 2 r \cos x + r ^ {2}}.
$$

该被积函数在后续的分析类课程中会时常遇到.

解 令 $t = \tan \frac{x}{2}$, 则有

$$
\begin{array}{l} \int \frac {(1 - r ^ {2}) \mathrm{d} x}{1 - 2 r \cos x + r ^ {2}} = 2 \int \frac {(1 - r ^ {2}) \mathrm{d} t}{(1 + r ^ {2}) (1 + t ^ {2}) - 2 r (1 - t ^ {2})} \\ = 2 (1 - r ^ {2}) \int \frac {\mathrm{d} t}{(1 - r) ^ {2} + (1 + r) ^ {2} t ^ {2}} \\ = 2 \arctan \left(\frac {1 + r}{1 - r} \tan \frac {x}{2}\right) + c. \\ \end{array}
$$

2. 形如  $\int R\left(x,\sqrt[p]{\frac{ax+b}{cx+d}},\cdots,\sqrt[q]{\frac{ax+b}{cx+d}}\right)\mathrm{d}x$  的不定积分

设  $R(x_{1}, x_{2}, \cdots, x_{n})$  是关于 n 元变量  $x_{1}, x_{2}, \cdots, x_{n}$  的有理函数, 即可以写成这些变量的两个多项式的比值. 我们研究被积函数形如

$R\left(x,\sqrt[p]{\frac{ax+b}{cx+d}},\cdots,\sqrt[q]{\frac{ax+b}{cx+d}}\right),\quad(p,\cdots,q \text{是大于1的自然数}),\quad ad-bc\neq0$

的不定积分. 注意此时, 被积函数关于 $x$ 而言是无理函数.

处理这类函数积分的基本思路是考虑如下的变量变换: 设 k 为这些自然数  $p, \cdots, q$  的最小公倍数, 令

$$
t = \sqrt [ k ]{\frac {a x + b}{c x + d}},
$$

则

$$
x = \frac {d t ^ {k} - b}{a - c t ^ {k}}, \quad \mathrm{d} x = \frac {a d - b c}{(a - c t ^ {k}) ^ {2}} k t ^ {k - 1} \mathrm{d} t.
$$

从而基于有理函数在复合运算下的封闭性, 可知 R 的不定积分就转化为关于 t 的有理函数的积分, 后者是能积出来的.

例8.4.6 计算不定积分 $I = \int \sqrt[3]{\frac{1 - x}{1 + x}}\frac{\mathrm{d}x}{1 - x}.$

解 我们简要介绍一下思路: 令 $\frac{1 - x}{1 + x} = t^3$, 则可以把原来的不定积分转化为

$$
I = - 3 \int \frac {\mathrm{d} t}{1 + t ^ {3}}.
$$

注意右端的不定积分, 除了相差常数 -3 外, 刚好是例 8.4.1 的情况, 因此

$$
I = - \ln | t + 1 | + \frac {1}{2} \ln (t ^ {2} - t + 1) - \sqrt {3} \arctan \left(\frac {2}{\sqrt {3}} \Big (t - \frac {1}{2} \Big)\right) + c.
$$

最后再将  $t = \sqrt[3]{\frac{1 - x}{1 + x}}$  代入上式即可.

3. 形如 $\int R\left(x, \sqrt{ax^2 + bx + c}\right) \mathrm{d}x (a \neq 0)$ 的不定积分

这里假设  $R(u,v)$  为变量 u,v 的有理函数, 因此, 关于 x 而言则是 x 的无理函数. 注意到

$$
a x ^ {2} + b x + c = a \left(x + \frac {b}{2 a}\right) ^ {2} + c - \frac {b ^ {2}}{4 a} = \pm \left(\sqrt {| a |} \left(x + \frac {b}{2 a}\right)\right) ^ {2} \pm \left(\sqrt {\left| c - \frac {b ^ {2}}{4 a} \right|}\right) ^ {2}.
$$

令 $u = \sqrt{|a|}\left(x + \frac{b}{2a}\right)$, 则 $\sqrt{ax^2 + bx + c}$ 可以转化为下面三种情况之一:

$$
\sqrt {u ^ {2} + \mu^ {2}}, \quad \sqrt {u ^ {2} - \mu^ {2}}, \quad \sqrt {\mu^ {2} - u ^ {2}}.
$$

被积函数的微分 $R\left(x,\sqrt{ax^2 + bx + c}\right)\mathrm{d}x$ 相应分别转化为

$$
R _ {1} (u, \sqrt {u ^ {2} + \mu^ {2}}) \mathrm{d} u, \quad R _ {2} (u, \sqrt {u ^ {2} - \mu^ {2}}) \mathrm{d} u, \quad R _ {3} (u, \sqrt {\mu^ {2} - u ^ {2}}) \mathrm{d} u.
$$

对于这三种情况, 再分别令

$$
u = \mu \tan t, \qquad u = \mu \sec t, \qquad u = \mu \sin t,
$$

则被积函数表达式就转化为三角函数的有理式, 后者我们已经讨论过了.

形如 $\int R\left(x,\sqrt{ax^2 + bx + c}\right)\mathrm{d}x(a\neq 0)$ 的不定积分还有一种经典的做法就是Euler替换.我们简要介绍如下.

情形 (i) a > 0, 此时令

$$
\sqrt {a x ^ {2} + b x + c} = t - \sqrt {a} x \quad (\text {或} \sqrt {a x ^ {2} + b x + c} = t + \sqrt {a} x),
$$

即所谓的第一种 Euler 替换. 可以得到

$$
b x + c = t ^ {2} - 2 \sqrt {a} t x, \quad x = \frac {t ^ {2} - c}{2 \sqrt {a} t + b},
$$

$$
\sqrt {a x ^ {2} + b x + c} = \frac {\sqrt {a} t ^ {2} + b t + c \sqrt {a}}{2 \sqrt {a} t + b}, \quad \mathrm{d} x = \frac {2 (\sqrt {a} t ^ {2} + b t + c \sqrt {a})}{(2 \sqrt {a} t + b) ^ {2}} \mathrm{d} t.
$$

把这些式子全部代入原不定积分, 得到关于 t 的有理函数的不定积分. 利用前面的讨论, 再求得关于 t 的原函数后, 再把  $t = \sqrt{ax^{2} + bx + c} + \sqrt{ax}$  代入表达式即可.

情形 (ii) c > 0, 此时令

$$
\sqrt {a x ^ {2} + b x + c} = x t + \sqrt {c} \quad (\text {或} \sqrt {a x ^ {2} + b x + c} = x t - \sqrt {c}),
$$

即所谓的第二种 Euler 替换. 可以得到

$$
a x + b = x t ^ {2} + 2 \sqrt {c} t, \quad x = \frac {2 \sqrt {c} t - b}{a - t ^ {2}},
$$

$$
\sqrt {a x ^ {2} + b x + c} = \frac {\sqrt {c} t ^ {2} - b t + \sqrt {c} a}{a - t ^ {2}}, \quad \mathrm{d} x = \frac {2 (\sqrt {c} t ^ {2} - b t + \sqrt {c} a)}{(a - t ^ {2}) ^ {2}} \mathrm{d} t.
$$

情形 (iii) 当二次式 $ax^2 + bx + c$ 有两个互异的实根 $\lambda$ 和 $\mu$ 时, 可以作下面的所谓的第三种 Euler 替换: 由

$$
a x ^ {2} + b x + c = a (x - \lambda) (x - \mu),
$$

令

$$
\sqrt {a x ^ {2} + b x + c} = t (x - \lambda).
$$

可得

$$
x = \frac {\lambda t ^ {2} - a \mu}{t ^ {2} - a}, \quad \sqrt {a x ^ {2} + b x + c} = \frac {a (\lambda - \mu) t}{t ^ {2} - a}, \quad \mathrm{d} x = \frac {2 a (\mu - \lambda) t}{(t ^ {2} - a) ^ {2}} \mathrm{d} t.
$$

以下可以按照前面情况下的程序讨论即可.

注意, 上面的几种 Euler 替换看起来多少有点突兀, 实则它们有明确的几何背景, 即代数曲线的有理参数化的常用做法. 事实上, 考虑平面二次曲线 $y^{2} = ax^{2} + bx + c$, 取过曲线上的任一点 $P_{0}(x_{0}, y_{0})$ 的割线 $\ell: y - y_{0} = t(x - x_{0})$, 其中 $t$ 是参数, $\ell$ 与曲线交于两点 $P_{0}$ 和 $P(x(t), y(t))$, 满足

$$
y _ {0} ^ {2} = a x _ {0} ^ {2} + b x _ {0} + c, \quad (y _ {0} + t (x - x _ {0})) ^ {2} = a x ^ {2} + b x + c.
$$

整理得

$$
2 y _ {0} t + t ^ {2} (x - x _ {0}) = a (x + x _ {0}) + b,
$$

由此可知  $P(x(t), y(t))$  的坐标为

$$
x (t) = x _ {0} - \frac {2 y _ {0} t - 2 a x _ {0} - b}{t ^ {2} - a}, \quad y (t) = y _ {0} - \frac {(2 y _ {0} t - 2 a x _ {0} - b) t}{t ^ {2} - a}.
$$

然后被积函数就可以化为关于 t 的有理函数从而可以积出来了.

容易看出一种特殊情况, 如果 $c = 0$, 形如 $\int R(x, y) \mathrm{d}x = R(x, \sqrt{ax^2 + bx}) \mathrm{d}x$ 的不定积分, 则可以选 $(x_0, y_0) = (0, 0)$, 从而有有理参数化

$$
x = \frac {b}{t ^ {2} - a}, \quad y = \frac {b t}{t ^ {2} - a}, \quad \mathrm{d} x = \frac {- 2 b t}{(t ^ {2} - a) ^ {2}}.
$$

更一般些, 由二元多项式 $P(x, y) = 0$ 给出的代数曲线, 如果有一个好的有理参数化表达, 那么与此有关的由隐函数确定的不定积分就能积出来. 我们仅举一个例子简单介绍这个做法.

例8.4.7 设 $y = y(x)$ 是方程 $y^{2}(x - y) = x^{2}$ 确定的隐函数. 计算不定积分

$$
\int \frac {1}{y ^ {2}} \mathrm{d} x.
$$

解 由方程看出 $x = 0 \iff y = 0$, 要计算的积分要求 $y \neq 0$.

令 y = tx, t 为参数,  $t \neq 0$ . 代入方程, 则隐函数  $y = y(x)$  可以写成参数方程

$$
\left\{ \begin{array}{l l} x = \frac {1}{t ^ {2} (1 - t)}, \\ y = \frac {1}{t (1 - t)}, \end{array} \right. \quad \text {从而有} \quad \mathrm{d} x = \frac {3 t - 2}{t ^ {3} (1 - t) ^ {2}} \mathrm{d} t.
$$

利用换元法

$$
\begin{array}{l} \int \frac {1}{y ^ {2}} \mathrm{d} x = \int t ^ {2} (1 - t) ^ {2} \frac {3 t - 2}{t ^ {3} (1 - t) ^ {2}} \mathrm{d} t = \int \left(3 - \frac {2}{t}\right) \mathrm{d} t \\ = 3 t - 2 \ln | t | + c = \frac {3 y}{x} - 2 \ln \left| \frac {y}{x} \right| + c. \\ \end{array}
$$

4. 形如 $\int x^{m}(a + bx^{n})^{p} \mathrm{~d}x$ 的不定积分

这里的常数 $a, b \in \mathbb{R}, m, n, p \in \mathbb{Q}, abnp \neq 0$.

稍微观察一下这个函数的表达式, 不难发现有可能出现根号套根号的情况. 所以我们从尽可能去掉根号这一基本出发点入手, 比如作变换

$$
x ^ {n} = t, \quad x = t ^ {\frac {1}{n}}, \quad \mathrm{d} x = \frac {1}{n} t ^ {\frac {1}{n} - 1} \mathrm{d} t.
$$

所以被积函数的微分表示式为

$$
x ^ {m} (a + b x ^ {n}) ^ {p} \mathrm{d} x = t ^ {\frac {m}{n}} (a + b t) ^ {p} \cdot \frac {1}{n} t ^ {\frac {1}{n} - 1} \mathrm{d} t = \frac {1}{n} t ^ {\frac {m + 1}{n} + p - 1} \left(\frac {a + b t}{t}\right) ^ {p} \mathrm{d} t.
$$

可以看出, 如果

$$
\frac {m + 1}{n} \in \mathbb {Z}, \quad \text {或者} \quad \frac {m + 1}{n} + p \in \mathbb {Z}, \quad \text {或者} \quad p \in \mathbb {Z},
$$

则上面的式子就完全转化为前面已经讨论过的情况. 在微积分早期就已经知道这些情况能积出来. 有趣的是, Chebyshev 在 19 世纪中叶证明了这也是能积出来的所有情况. 换句话说, 我们 (不加证明) 介绍 Chebyshev 的一个结论:

形如 $\int x^{m}(a + bx^{n})^{p}\mathrm{d}x$ （$m, n, p$ 均为有理数）的积分能积出来的充要条件是 $p$, $\frac{m+1}{n}, p + \frac{m+1}{n}$ 三者至少有一个是整数. 根据这个结论, 我们可以构造如下积不出来的不定积分 (椭圆积分):

$$
\int \frac {1}{\sqrt {1 - x ^ {3}}} \mathrm{d} x, \quad \int \frac {1}{\sqrt {1 - x ^ {4}}} \mathrm{d} x.
$$

另一方面, 通过调整 $m, n, p$ 可以知道不定积分

$$
\int \frac {\sqrt {x}}{\sqrt {1 - x ^ {3}}} \mathrm{d} x
$$

是能积出来的, 读者可自行思考.

例8.4.8 求不定积分 $I = \int \frac{\sqrt[3]{1 + \sqrt[4]{x}}}{\sqrt{x}}\mathrm{d}x = \int x^{-\frac{1}{2}}\left(1 + x^{\frac{1}{4}}\right)^{\frac{1}{3}}\mathrm{d}x.$

解 $m = -\frac{1}{2}, n = \frac{1}{4}, p = \frac{1}{3}$. 由于 $\frac{m + 1}{n} = 2 \in \mathbb{Z}$, 所以此积分能积出来. 作变量替换 $t = \sqrt[3]{1 + \sqrt[4]{x}}$, 直接运算可得如下结论:

$$
I = \frac {3}{7} t ^ {4} (4 t ^ {3} - 7) + c.
$$

再把 $t = t(x)$ 代入即可.

## 习题8.4

1. 求下列不定积分:

(1) $\int \frac{\mathrm{d}x}{(x + 1)(x + 2)^2}$;

(2) $\int \frac{\mathrm{d}x}{x^4 + x^2 + 1}$;

(3) $\int \frac{1 + x^4}{1 + x^6} \, \mathrm{d}x$;

(4) $\int \frac{\mathrm{d}x}{1 + x^3}$;

(5) $\int \frac{x^4\mathrm{d}x}{x^2 + 1}$;

(6) $\int \frac{(x^4 + 1)\mathrm{d}x}{(x^2 + 1)^2}$.

2. 求下列不定积分:

(1) $\int \sin^{-\frac{3}{2}} x \cos^{-\frac{5}{2}} x \, \mathrm{d}x;$

(2) $\int \sin^{-\frac{1}{2}} x \cos^{\frac{1}{2}} x \, \mathrm{d}x;$

(3) $\int \sqrt{1 + \sin x} \, \mathrm{d}x$;

(4) $\int \frac{x + \sin x}{1 + \cos x} \, \mathrm{d}x;$

(5) $\int \frac{\mathrm{d}x}{\sin x - \sin \alpha}$;

(6) $\int \frac{\mathrm{d}x}{\sin(x + a)\cos(x + b)}.$

3. 计算不定积分 $\int \frac{x^2}{(x\sin x + \cos x)^2}\mathrm{d}x.$

4. 设 $y = y(x)$ 是方程 $x^3 + y^3 = x^2 + y^2$ 确定的隐函数, 试计算不定积分 $\int \frac{1}{y^3} \, \mathrm{d}x$.

5. 在承认 $\int \frac{\mathrm{e}^x}{x} \, \mathrm{d}x$ 不是初等函数的前提下, 问 $\int \mathrm{e}^x P_n\left(\frac{1}{x}\right) \, \mathrm{d}x$ 何时为初等函数, 其中 $P_n(x)$ 为 $n$ 次多项式.

## 参考文献

[1] SAYEL A A. The mth ratio test: new convergence tests for series. The American Mathematical Monthly, 2008, 115(6): 514-524.
[2] 波利亚, 舍贵. 数学分析中的问题和定理: 第一卷. 张奠宙, 宋国栋, 等, 译. 上海: 上海科学技术出版社, 1981.
[3] 陈传章, 金福临, 朱学炎, 等. 数学分析: 上册. 2 版. 北京: 高等教育出版社, 1983.
[4] 陈传章, 金福临, 朱学炎, 等. 数学分析: 下册. 2 版. 北京: 高等教育出版社, 1983.
[5] 陈纪修, 於崇华, 金路. 数学分析: 上册. 3 版. 北京: 高等教育出版社, 2019.
[6] 陈纪修, 於崇华, 金路. 数学分析: 下册. 3 版. 北京: 高等教育出版社, 2019.
[7] 陈天权. 数学分析讲义: 第一册. 北京: 北京大学出版社, 2009.
[8] 陈天权. 数学分析讲义: 第二册. 北京: 北京大学出版社, 2010.
[9] 陈天权. 数学分析讲义: 第三册. 北京: 北京大学出版社, 2010.
[10] 程艺, 陈卿, 李平. 数学分析讲义: 第一册. 北京: 高等教育出版社, 2019.
[11] 程艺, 陈卿, 李平. 数学分析讲义: 第二册. 北京: 高等教育出版社, 2020.
[12] 程艺, 陈卿, 李平, 等. 数学分析讲义: 第三册. 北京: 高等教育出版社, 2020.
[13] 常庚哲, 史济怀. 数学分析教程: 上册. 3 版. 合肥: 中国科学技术大学出版社, 2012.
[14] 常庚哲, 史济怀. 数学分析教程: 下册. 3 版. 合肥: 中国科学技术大学出版社, 2013.
[15] 崔尚斌. 数学分析教程: 上册. 北京: 科学出版社, 2013.
[16] 崔尚斌. 数学分析教程: 中册. 北京: 科学出版社, 2013.
[17] 崔尚斌. 数学分析教程: 下册. 北京: 科学出版社, 2013.
[18] 布雷苏. 微积分溯源: 伟大思想的历程. 陈见柯, 林开亮, 叶卢庆, 译. 北京: 人民邮电出版社, 2022.
[19] 丁传松, 李秉彝, 布伦. 实分析导论. 北京: 科学出版社, 1998.
[20] DUNHAM W. 微积分的历程: 从牛顿到勒贝格. 李伯民, 汪军, 张怀勇, 译. 北京: 人民邮电出版社, 2010.
[21] 菲赫金哥尔茨. 微积分学教程 (第 8 版): 第一卷. 杨弢亮, 叶彦谦, 译. 北京: 高等教育出版社, 2006.
[22] 菲赫金哥尔茨. 微积分学教程 (第 8 版): 第二卷. 徐献瑜, 冷生明, 梁文骐, 译. 北京: 高等教育出版社, 2006.
[23] 菲赫金哥尔茨. 微积分学教程 (第 8 版): 第三卷. 路见可, 余家荣, 吴亲仁, 译. 北京: 高等教育出版社, 2006.
[24] 郝兆宽, 杨睿之, 杨跃. 数理逻辑证明及其限度. 上海: 复旦大学出版社, 2014.
[25] 华东师范大学数学系. 数学分析: 上册. 5 版. 北京: 高等教育出版社, 2019.
[26] 华东师范大学数学系. 数学分析: 下册. 5 版. 北京: 高等教育出版社, 2019.
[27] 郦中丹, 刘永平, 王昆扬. 简明数学分析. 2 版. 北京: 高等教育出版社, 2009.
[28] 黄玉民, 李成章. 数学分析. 2 版. 北京: 科学出版社, 2004.
[29] HUNT R A. On the convergence of Fourier series//Proceedings of the Conference on Orthogonal Expansions and Their Continuous Analogues. Carbondale: Southern Illinois University Press, 1968: 235-255.
[30] HUYNH E. A second Raabe's test and other series tests. The American Mathematical Monthly, 2022, 129(9): 865-875.
[31] 吉林大学数学系. 数学分析: 上册. 北京: 人民教育出版社, 1978.
[32] 吉林大学数学系. 数学分析: 中册. 北京: 人民教育出版社, 1978.
[33] 吉林大学数学系. 数学分析: 下册. 北京: 人民教育出版社, 1978.
[34] KOLMOGOROFF A N. Une série de Fourier-Lebesgue divergente presque partout. Fundamenta mathematicae, 1923(4): 324-328.
[35] KOLMOGOROFF A N. Une série de Fourier-Lebesgue divergente partout. Comptes Rendus de l'Académie des Sciences Paris, 1926, 183: 1327-1328.
[36] KÖRNER T W. Uniqueness for trigonometric series. Annals of Mathematics, 1987, 126(1): 1-34.
[37] 李逸. 基本分析讲义:第一卷 上册. 北京: 高等教育出版社, 2025.
[38] 李逸. 基本分析讲义:第一卷 下册. 北京: 高等教育出版社, 2025.
[39] 刘玉琏, 傅沛仁, 林玎, 等. 数学分析讲义: 上册. 5 版. 北京: 高等教育出版社, 2008.
[40] 刘玉琏, 傅沛仁, 林玎, 等. 数学分析讲义: 下册. 5 版. 北京: 高等教育出版社, 2008.
[41] 楼红卫. 数学分析——要点 · 难点 · 拓展. 北京: 高等教育出版社, 2020.
[42] 楼红卫. 微积分进阶. 北京: 科学出版社, 2009.
[43] 楼红卫. 数学分析: 上册. 北京: 高等教育出版社, 2022.
[44] 楼红卫. 数学分析: 下册. 北京: 高等教育出版社, 2023.
[45] 楼红卫. 数学分析技巧选讲. 北京: 高等教育出版社, 2022.
[46] 梅加强. 数学分析. 2 版. 北京: 高等教育出版社, 2020.
[47] 欧阳光中, 朱学炎, 秦曾复. 数学分析: 上册. 上海: 上海科学技术出版社, 1983.
[48] 欧阳光中, 朱学炎, 秦曾复. 数学分析: 下册. 上海: 上海科学技术出版社, 1982.
[49] 裴礼文. 数学分析中的典型问题与方法. 3 版. 北京: 高等教育出版社, 2021.
[50] PRUS-WIŚNIOWSKI F. A refinement of Raabe's test. The American Mathematical Monthly, 2008, 115(3): 249-252.
[51] 齐民友. 重温微积分. 北京: 高等教育出版社, 2004.
[52] RUDIN W. 数学分析原理（原书第3版）. 赵慈庚, 蒋铎, 译. 北京: 机械工业出版社, 2004.
[53] SCHRAMM M, TROUTMAN J, WATERMAN D. Segmentally alternating series. The American Mathematical Monthly, 2014, 121(8): 717-722.
[54] 佘志坤. 全国大学生数学竞赛参赛指南. 北京: 科学出版社, 2022.
[55] 佘志坤. 全国大学生数学竞赛解析教程（数学专业类）——数学分析:上册. 北京:科学出版社，2024.
[56] STUART C. An inequality involving  $\sin(n)$ . The American Mathematical Monthly, 2018, 125(2): 173–174.
[57] 陶哲轩. 陶哲轩实分析. 王昆扬, 译. 北京: 人民邮电出版社, 2008.
[58] TRENCH W F. Introduction to Real Analysis. Upper Saddle River: Prentice Hall, 2003.
[59] 王昆扬. 数学分析简明教材. 北京: 高等教育出版社, 2015.
[60] WATSON G N. A Treatise on the Theory of Bessel Functions. 2nd ed. Cambridge: Cambridge University Press, 1944.
[61] 伍胜健. 数学分析: 第一册. 北京: 北京大学出版社, 2009.
[62] 伍胜健. 数学分析: 第二册. 北京: 北京大学出版社, 2010.
[63] 伍胜健. 数学分析: 第三册. 北京: 北京大学出版社, 2010.
[64] 小平邦彦. 微积分入门 I: 一元微积分. 裴东河, 译. 北京: 人民邮电出版社, 2008.
[65] 小平邦彦. 微积分入门 II: 多元微积分. 裴东河, 译. 北京: 人民邮电出版社, 2008.
[66] 肖文灿. 集合论初步. 2 版. 北京: 商务印书馆, 1950.
[67] 谢惠民, 恽自求, 易法槐, 等. 数学分析习题课讲义: 上册. 2 版. 北京: 高等教育出版社, 2018.
[68] 谢惠民, 恽自求, 易法槐, 等. 数学分析习题课讲义: 下册. 2 版. 北京: 高等教育出版社, 2019.
[69] 辛钦. 数学分析八讲. 王会林, 齐民友, 译. 北京: 人民邮电出版社, 2010.
[70] 叶怀安. 连续函数列的极限函数的一个性质及其应用. 湖南数学年刊, 1985, 5(2): 87-88.
[71] 张福保, 薛星美. 数学分析 (全三册). 北京: 科学出版社, 2022.
[72] 张锦文. 公理集合论导引. 北京: 科学出版社, 1991.
[73] 张筑生. 数学分析新讲:第一册. 北京:北京大学出版社，1990.
[74] 张筑生. 数学分析新讲:第二册. 北京: 北京大学出版社, 1990.
[75] 张筑生. 数学分析新讲:第三册. 北京:北京大学出版社，1991.
[76] 周民强. 实变函数论. 3 版. 北京: 北京大学出版社, 2016.
[77] 周民强. 数学分析习题演练: 第一册. 北京: 科学出版社, 2006.
[78] 周民强. 数学分析习题演练: 第二册. 北京: 科学出版社, 2006.
[79] 卓里奇. 数学分析 (第 4 版): 第一卷. 蒋铎, 王昆扬, 周美珂, 等, 译. 北京: 高等教育出版社, 2006.
[80] 卓里奇. 数学分析 (第 4 版): 第二卷. 蒋铎, 钱珮玲, 周美珂, 等, 译. 北京: 高等教育出版社, 2006.
[81] ZYGMUND A. Trigonometric Series. 3rd ed. Cambridge: Cambridge University Press, 2002.

## 常用符号

| N | 自然数集 |
| --- | --- |
| $\mathbb{Z},\mathbb{Z}_{+}$ | 整数集,正整数集 |
| $\mathbb{Q},\mathbb{Q}_{+}$ | 有理数域,正有理数集 |
| $\mathbb{R},\mathbb{R}_{+}$ | 实数域,正实数集 |
| $\mathbb{R}^{n}$ | n维欧氏空间 |
| C | 复数域 |
| $\mathbb{C}^{n}$ | n维复空间 |
| $S^{n-1}$ | $\mathbb{R}^{n}$中单位球面,即$\{x\in\mathbb{R}^{n}\|\\\|x\\\|=1\}$ |
| $\mathbb{S}^{n}$ | n阶实对称矩阵全体 |
| $B_{r}(x)$ | 半径为r,中心在$x\in\mathbb{R}^{n}$的开球 |
| $\overset{\circ}{B}_{r}(x)$ | 半径为r,中心在$x\in\mathbb{R}^{n}$的去心开球 |
| $I_{r}(x)$ | 边长为2r,中心在$x\in\mathbb{R}^{n}$且各边平行于坐标轴的闭方体 |
| $A^{\mathrm{T}},x^{\mathrm{T}}$ | 矩阵A,向量x的转置 |
| $x\cdot y$ | $\mathbb{R}^{n}$中向量x与y的内积,也常用$\langle x,y\rangle,x^{\mathrm{T}}y$表示 |
| $\langle x,y\rangle$ | 内积空间中两个元素x,y的内积 |
| $\\\|x\\\|_{p}$ | $\mathbb{R}^{n}$中向量$x=(x_{1},x_{2},\cdots,x_{n})^{\mathrm{T}}$的p-范数$\left(\sum_{k=1}^{n}\|x_{k}\|^{p}\right)^{\frac{1}{p}}$ |
| $\\\|A\\\|_{p}$ | 方阵$A\in\mathbb{R}^{n\times n}$的诱导范数$\\\|A\\\|_{p}:=\max_{\\\|x\\\|_{p}=1}\\\|Ax\\\|_{p}$ |
| $\\\|x\\\|$ | $\mathbb{R}^{n}$中向量x通常的范数,即$\\\|x\\\|_{2}$ |
| $\\\|A\\\|$ | 方阵$A\in\mathbb{R}^{n\times n}$通常的诱导范数$\\\|A\\\|_{2}$ |
| $\nu(E)$ | $\mathbb{R}^{n}$中Jordan可测集E的Jordan测度(容积)——长度、面积、体积 |
| $a^{+},a^{-}$ | 实数a的正部$(\|a\|+a)/2$与负部$(\|a\|-a)/2$ |
| $a \lor b, a \land b$ | 实数 $a, b$ 的最大值和最小值 |
| Re z, Im z | 复数 $z = a + bi$ 的实部 $a$ 和虚部 $b$, 其中 $a, b$ 为实数 |
| $\chi_E$ | 集合 $E$ 的特征函数, 即在 $E$ 上取值为 1, 在其余点上取值为 0 的函数 |
| ∃ | 存在 |
| ∀ | 对于所有 |
| ≫,≪ | 大大大于, 大大小于 |
| a.e. | 几乎处处 |
| s.t. | 使得 |
| ∅ | 空集 |
| ∈, ∃ | $a \in E$ 和 $E \ni a$ 均表示 $a$ 是 $E$ 的元素 |
| ⊆, ⊆ | $E \subseteq F$ 和 $F \supseteq E$ 均表示集合 $E$ 包含于集合 $F$, 即 $F$ 包含 $E$ |
| ⊂, ⊃ | $E \subset F$ 和 $F \supset E$ 均表示集合 $E$ 真包含于集合 $F$, 即 $F$ 真包含 $E$ |
| ⊂⊂ | 集合的紧包含关系, $E \subset \subset F$ 当且仅当 $\overline{E}$ 是 $F$ 的紧子集 |
| $E\{\varphi \in F\}$ | 表示集合 $\{x \in E \| \varphi(x) \in F\}$. 在 $E$ 明确的情况下, 简记为 $\{\varphi \in F\}$ |
| $f(D)$ | 当 $f$ 是映射, $D$ 是集合时, 表示 $D$ 的像集 $\{f(x) \| x \in D\}$ |
| ∩ | 集合的交, $A \cap B$ 表示同时属于 $A$ 和 $B$ 的所有元素组成的集合 |
| ∪ | 集合的并, $A \cup B$ 表示属于 $A$ 或属于 $B$ 的所有元素组成的集合 |
| \\ | 集合的差, $A \setminus B$ 表示属于 $A$ 而不属于 $B$ 的所有元素组成的集合 |
| C | 集合的补, CE 表示在全集 $X$ 明确的情况下, $E$ 的补集 $X \setminus E$ |
| $E^\circ$ | 集合 $E$ 的内部, 即 $E$ 的内点的全体 |
| $E'$ | 集合 $E$ 的导集, 即 $E$ 的极限点 (聚点) 的全体 |
| $\overline{E}$ | 集合 $E$ 的闭包 |
| ∂E | 集合 $E$ 的边界 |
| $\alpha E + \beta F$ | 线性空间中集合的伸缩、代数和与代数差等, 表示集合 $\{ \alpha x + \beta y \| x \in E, y \in F \}$ |
| Σ, Π | 连加号, 连乘号 |
| [x], {x} | 实数 $x$ 的整数部分 (即不大于 $x$ 的最大整数) 与小数部分 (即 $x - [x]$) |
| $\overline{\lim}, \underline{\lim}$ | 上极限, 下极限 |
| ∫, ∫ | 上积分符号, 下积分符号 |
| $\mathcal{R}(I)$ | 区间 $I$ 上的 Riemann 可积函数全体 |
| $\mathcal{R}^p(I)$ | 区间 $I$ 上正部与负部均 $p$ 次 (广义) 可积的函数全体 |
| $C_n^k$ | 在 $n$ 个不同的元素中选取 $k$ 个的组合数 |

| $C^{\omega}(I)$ | 区间 $I \subseteq \mathbb{R}$ 上的实解析函数全体 |
| --- | --- |
| $C^{k}(\Omega)$ | 在 $\Omega$ 上有 $k$ 阶连续 (偏) 导数的函数全体 |
| $C_{c}^{k}(\Omega)$ | 在 $\Omega$ 上有紧致集且有 $k$ 阶连续 (偏) 导数的函数全体 |
| $C^{k,\alpha}(\Omega)$ | 在 $\Omega$ 上 $k$ 阶 (偏) 导数满足 $\alpha$ 次 Hölder 条件的函数全体 |
| $\mathscr{S}$ | 速降函数全体 |
| $\widehat{f},\widehat{f}$ | 函数 $f$ 的 Fourier 变换, Fourier 逆变换 |
| $f*g$ | 函数 $f$ 和 $g$ 的卷积 |
| $\ell_{\infty}$ | 有界实数数列的全体 |
| $\ell_{p}$ | $1 \leqslant p < +\infty, p$ 次可求和序列的全体 |