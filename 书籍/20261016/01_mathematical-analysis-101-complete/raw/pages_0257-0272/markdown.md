即

$$
G (x) = F (x) + c.
$$

由定理可知, 如果能求出  $f(x)$  的一个原函数, 则可以得到它所有的原函数, 任意两个原函数之间仅相差一个常数.

该定理有明确的几何直观: 设 $F$ 是给定函数 $f$ 的原函数, $\Gamma: y = F(x)$ 是这样一条曲线, 它在 $x = x_0$ 处有斜率为 $k = f(x_0)$ 的切线 $\ell$. 将 $\Gamma$ 沿着 $y$ 轴向上平移 $c$ 得到曲线 $\Gamma_c: y = F(x) + c$. 则 $\Gamma_c$ 在 $x = x_0$ 处的切线 $\ell_c$ 也对应着 $\ell$ 的平移, 即它们有完全相同的斜率 $k$, 所以 $y = F(x) + c$ 也是 $f(x)$ 的一个原函数. $\Gamma$ 和 $\Gamma_c$ 的切线方程分别为

$$
\ell : \quad y = f (x _ {0}) (x - x _ {0}) + F (x _ {0}), \qquad \ell_ {c}: \quad y = f (x _ {0}) (x - x _ {0}) + F (x _ {0}) + c.
$$

容易看出, 在这一族相互平行的曲线中, 如果要研究某一条过指定点 $(x_0, y_0)$ 的曲线 $\Gamma^*$, 则只需确定出相应的常数 $c = y_0 - F(x_0)$ 即可.

定理8.1.1的一个等价说法是, 如果函数 $f(x)$ 有一个原函数 $F(x)$, 则通过平移得到一族原函数; 反过来, 任何一个原函数都必须在此函数族中, 即 $\{F(x) + c : c \in \mathbb{R}\}$ 的集合恰好由 $f(x)$ 的所有原函数组成. 这样, 我们很自然地可以把这族由 $f(x)$ 生成的函数集合赋予它一个记号

$$
\int f (x) \mathrm{d} x,
$$

并称之为  $f(x)$  的不定积分,  $f(x)$  常称为被积函数.

这里我们需要注意两点: 一是原函数和不定积分是两个概念, 它们之间的关系是元素与集合的从属关系. 不定积分 $\int f(x) \mathrm{d}x$ 代表的不是一个函数, 而是一个由所有具有相同导函数的元素组成的集合, 这个集合中的每一个函数都称为 $f(x)$ 的一个原函数. 二是 $f(x)$ 的不定积分这个称呼以及记号 $\int f(x) \mathrm{d}x$ 现阶段看起来有点突兀, 它们的意义在学到定积分后将会看得更清楚和更深刻, 目前暂时当成一个术语理解即可.

例 8.1.1 求下列不定积分:

$$
\int \sin x \mathrm{d} x, \quad \int x ^ {2} \mathrm{d} x, \quad \int \mathrm{e} ^ {a x} \mathrm{d} x (a \neq 0).
$$

解 下面所有表达式中的 c 均为常数, 不再一一赘述.

由于 $(\cos x)' = -\sin x,$ 所以

$$
\int \sin x   \mathrm{d} x = - \cos x + c.
$$

同理, 我们可以写出另外两个不定积分:

$$
\int x ^ {2} \mathrm{d} x = \frac {1}{3} x ^ {3} + c, \quad \int \mathrm{e} ^ {a x} \mathrm{d} x = \frac {1}{a} \mathrm{e} ^ {a x} + c.
$$

例8.1.2 试讨论符号函数

$$
\operatorname{sgn} (x) = \left\{ \begin{array}{l l} - 1, & x <   0, \\ 0, & x = 0, \\ 1, & x > 0 \end{array} \right.
$$

在 R 上是否有原函数.

解 我们假设 $\operatorname{sgn}(x)$ 有原函数 $F(x)$, 则

当 $x < 0$ 时, $F'(x) = -1$, 因此 $F(x) = -x + c_1$;

当 $x > 0$ 时, $F'(x) = 1$, 因此 $F(x) = x + c_2$.

由于  $F(x)$  是原函数, 故必须可导, 从而在 x = 0 处连续. 因而必须有  $c_{1} = c_{2} = c$ , 即

$$
F (x) = \left\{ \begin{array}{l l} - x + c, & x <   0, \\ c, & x = 0, \\ x + c, & x > 0. \end{array} \right.
$$

然而这样的  $F(x)$  在 x=0 处不可能可导, 从而  $\mathrm{sgn}(x)$  在 R 上没有原函数. 但请注意,  $\mathrm{sgn}(x)$  在任一不包含原点在内的区间上是有原函数的.

## 习题 8.1

1. 证明: 若 $\int f(x) \, \mathrm{d}x = F(x) + C$, 则

$$
\int f (a x + b) \mathrm{d} x = \frac {1}{a} F (a x + b) + C \quad (a \neq 0).
$$

2. 求下列不定积分:

(1) $\int (2^x + 3^x) \, \mathrm{d}x$;

(2) $\int \tan^2 x \, \mathrm{d}x$;

(3) $\int \frac{2x^2}{1 + x^2} \, \mathrm{d}x$;

(4) $\int \cos^2 x \, \mathrm{d}x$;

(5) $\int \cos x\cos 2x\mathrm{d}x;$

(6) $\int \frac{\cos 2x}{\cos^2 x \sin^2 x} \, \mathrm{d}x;$

(7) $\int \frac{\mathrm{e}^{3x} + 1}{\mathrm{e}^x + 1} \, \mathrm{d}x;$

(8) $\int \frac{\cos 2x}{\cos x - \sin x} \, \mathrm{d}x;$

(9) $\int \sqrt{1 - \sin 2x} \, \mathrm{d}x$.

3. 求下列不定积分:

(1) $\int \mathrm{e}^{-|x|}\mathrm{d}x;$

(2) $\int |x|\mathrm{d}x;$

(3) $\int \max \{1, x^2\} \, \mathrm{d}x$;

(4) $\int |\sin x| \, \mathrm{d}x$.

4. 设 $f$ 在 $(a, b)$ 内可导, 且 $|f'(x)| \leqslant M, \forall x \in (a, b)$. 证明: 极限 $\lim_{x \to a^+} f(x)$ 和 $\lim_{x \to b^-} f(x)$ 都存在且有限.
5. 设 $f$ 在 $[a, b]$ 上连续, 在 $(a, b)$ 内的左导数存在且恒为零, 证明: $f$ 为常值函数. 对于右导数有类似的结论.
6. 设 f 周期为 T. 则其原函数 F 以 T 为周期当且仅当  $F(T) = F(0)$ .
7. 设 $f$ 为奇函数. 则其原函数为偶函数; 设 $f$ 为偶函数. 则其原函数 $F$ 为奇函数当且仅当 $F(0) = 0$.

## 8.2 原函数的存在性

上节我们给出了原函数的概念和不定积分的定义, 本节我们将讨论不定积分的一个基本问题——原函数的存在性问题. 这个问题包含两个方面, 一是什么样的函数一定有原函数, 二是什么样的函数一定没有原函数. 对于问题的第一个方面, 我们有如下结论.

定理 8.2.1（原函数存在定理） 闭区间 I 上的连续函数必有原函数.

在给出定理证明之前, 我们简单分析一下. 首先, 连续函数原函数的存在性大都放到定积分引入之后, 通过变上限积分直接给出原函数 (见定理 9.3.6). 下面我们给出一个直接的证明.

回顾一下第六章例 6.1.7 中的函数  $g(x)$  和  $G(x)$ . 用原函数的语言重述该例的结论就是, 如果区间 I 上的逐段线性函数  $g(x)$  连续, 则  $g(x)$  有连续的逐段为抛物线的原函数  $G(x)$ . 本定理的证明将主要基于该结论.

给定区间 $I = [a,b]$ 和 $I$ 上的一组分点

$$
a = x _ {0} <   x _ {1} <   x _ {2} <   \dots <   x _ {n} <   x _ {n + 1} = b.
$$

设  $g(x)$  是区间 I 上的形如下式的逐段线性函数:

$$
g (x) = a _ {i} + k _ {i} (x - x _ {i}), \quad x \in [ x _ {i}, x _ {i + 1} ], \quad i = 0, 1, \dots , n.
$$

为了保证 $g(x)$ 的连续性, 有

$$
a _ {i} = a _ {i - 1} + k _ {i - 1} (x _ {i} - x _ {i - 1}) \quad i = 1, 2, \dots , n.
$$

例6.1.7直接给出了函数 $g(x)$ 满足 $G(a) = 0$ 的原函数

$$
G (x) = A _ {i} + a _ {i} (x - x _ {i}) + \frac {k _ {i}}{2} (x - x _ {i}) ^ {2}, \quad x \in [ x _ {i}, x _ {i + 1} ], \quad i = 0, 1, \dots , n,
$$

其中  $A_{0}=0,\quad A_{i}=A_{i-1}+a_{i-1}(x_{i}-x_{i-1})+\frac{k_{i-1}}{2}(x_{i}-x_{i-1})^{2},\quad i=1,2,\cdots,n.$

证明 不失一般性, 不妨假设 $I = [0,1]$. 设函数 $f(x)$ 是 $I$ 上的连续函数, 我们证明一定存在 $I$ 上的函数 $F(x)$ 使得 $F'(x) = f(x)$ (这里在区间端点处自然理解为单侧导数).

记

$$
\omega (r) = \max_{\substack{x,x^{\prime}\in [0,1]\\ |x - x^{\prime}|\leqslant r}}|f(x) - f(x^{\prime})|,\quad \forall r\geqslant 0.
$$

由于 $f(x)$ 在 $I$ 上连续, 故一致连续, 即 $\lim_{r\to 0^{+}}\omega (r) = \omega (0) = 0.$

任取 $n \geqslant 2$, 定义

$$
f _ {n} (x) = \left\{ \begin{array}{l l} f (0) + n \Big (f \Big (\frac {1}{n} \Big) - f (0) \Big) x, & x \in \left[ 0, \frac {1}{n}\right), \\ f \Big (\frac {1}{n} \Big) + n \Big (f \Big (\frac {2}{n} \Big) - f \Big (\frac {1}{n} \Big) \Big) \Big (x - \frac {1}{n} \Big), & x \in \left[ \frac {1}{n}, \frac {2}{n}\right), \\ \dots , \\ f \Big (\frac {n - 1}{n} \Big) + n \Big (f (1) - f \Big (\frac {n - 1}{n} \Big) \Big) \Big (x - \frac {n - 1}{n} \Big), & x \in \left[ \frac {n - 1}{n}, 1 \right]. \end{array} \right.
$$

则 $f_{n}(x)$ 是[0,1]上的连续的逐段线性函数.根据第六章例6.1.7的结论，知 $f_{n}(x)$ 在 $I$ 上有原函数 $F_{n}(x)$ 且 $F_{n}(0) = 0,F_{n}(x)$ 是一个连续的逐段抛物线函数

显然, $\forall x\in I$ ，有

$$
| f _ {n} (x) - f (x) | \leqslant \omega \Big (\frac {1}{n} \Big).
$$

由Lagrange中值定理, 知存在点 $\xi = \xi(m, n, x) \in (0, 1)$ 使得对任意的自然数 $m, n \geqslant 2$, 有

$$
\begin{array}{l} \left| F _ {m} (x) - F _ {n} (x) \right| = \left| \left(F _ {m} (x) - F _ {n} (x)\right) - \left(\left| F _ {m} (0) - F _ {n} (0) \right|\right) \right| \\ = \left| f _ {m} (\xi) - f _ {n} (\xi) \right| \cdot | x | \leqslant \left| f _ {m} (\xi) - f _ {n} (\xi) \right| \\ \leqslant \left| f _ {m} (\xi) - f (\xi) \right| + \left| f _ {n} (\xi) - f (\xi) \right| \\ \leqslant \omega \left(\frac {1}{m}\right) + \omega \left(\frac {1}{n}\right). \\ \end{array}
$$

由 Cauchy 收敛准则知当 $n \to +\infty$ 时, 有 $F_{n}(x)$ 收敛到某函数 $F(x)$.

对于 $n \geqslant 2$, 利用Lagrange中值定理, 考虑差商

$$
\begin{array}{l} \left| \frac {F _ {n} (x) - F _ {n} (x ^ {\prime})}{x - x ^ {\prime}} - f (x) \right| = | f _ {n} (x + \theta (x - x ^ {\prime})) - f (x) | \\ \leqslant \left| f _ {n} (x + \theta (x - x ^ {\prime})) - f (x + \theta (x - x ^ {\prime})) \right| + \\ \left| f \left(x + \theta \left(x - x ^ {\prime}\right)\right) - f (x) \right| \\ \end{array}
$$

$$
\leqslant \omega \left(\frac {1}{n}\right) + \omega (| x - x ^ {\prime} |),
$$

这意味着

$$
\left| \frac {F (x) - F (x ^ {\prime})}{x - x ^ {\prime}} - f (x) \right| \leqslant \omega (| x - x ^ {\prime} |).
$$

即  $\forall x \in I, F'(x) = f(x).$

对于本节开头时问题的第二个方面, 即什么样的函数一定没有原函数, 从例题 8.1.2 我们看到符号函数不可能有原函数. 事实上, 我们有下面更一般的结论.

定理 8.2.2 区间 I 上不具有介值性的函数一定不存在原函数.

证明 定理本质上是 Darboux 介值定理的应用: 任何一个可微函数的导函数必具有介值性, 因此不具有介值性的函数是不可能成为一个函数的导函数的. □

![](images/page_260_image_9.jpg)

注 8.2.1 上面两个定理合起来并没有给出连续函数是有原函数的充要条件。换句话说，我们并没有排除掉不连续函数一定没有原函数这种情况。事实上，下面的例子告诉我们，即使 $f(x)$ 在 $x = 0$ 处不连续，但它仍然可以有原函数。当然，此时的间断点一定不是第一类间断点。

例8.2.1 证明函数

$$
f (x) = \left\{ \begin{array}{l l} 2 x \sin \frac {1}{x ^ {2}} - \frac {2}{x} \cos \frac {1}{x ^ {2}}, & x \neq 0, \\ 0, & x = 0 \end{array} \right.
$$

有原函数

$$
F (x) = \left\{ \begin{array}{l l} x ^ {2} \sin \frac {1}{x ^ {2}}, & x \neq 0, \\ 0, & x = 0. \end{array} \right.
$$

证明 直接验证即可.

事实上, 我们可以利用连续函数必有原函数这一结论, 来给出构造不连续函数仍有原函数的稍微一般的方法. 参见本节习题题目 5.

## 习题8.2

1. 试讨论符号函数 $\operatorname{sgn}(x)$ 和 Dirichlet 函数有没有原函数？
2. 设 $a < c < b, f$ 在 $(a, b)$ 内连续, $F$ 在 $(a, c)$ 与 $(c, b)$ 内均为 $f$ 的原函数, 且 $F$ 在 $(a, b)$ 内连续. 证明: $F$ 是 $f$ 在 $(a, b)$ 内的原函数.
3. 设 $f$ 是区间 $[a, b]$ 上的实连续函数, $F$ 是 $f$ 在区间 $(a, b)$ 内的一个原函数. 证明: $F(a^{+})$ 与 $F(b^{-})$ 存在.
4. 设 $f(x)$ 在 $[a, b]$ 上有界且存在原函数, $g(x)$ 是 $[a, b]$ 上的连续函数. 求证: $f(x)g(x)$ 在 $[a, b]$ 上存在原函数.

5. 设函数 $f(x)$ 在 $(- \infty, + \infty)$ 上可导，$\lim_{x \to \infty} \frac{f(x)}{x} = 0$。求证:

$$
g (x) = \left\{ \begin{array}{l l} f ^ {\prime} \left(\frac {1}{x}\right), & x \neq 0, \\ 0, & x = 0 \end{array} \right.
$$

在 $(-\infty, +\infty)$ 上有原函数.

6. 在上面的题目 5 中, 特别地, 取 $f_{1}(x) = -\cos x$, $f_{2}(x) = \sin x$, 则满足 $\lim_{x \to \infty} \frac{f_{i}(x)}{x} = 0, i = 1, 2$. 因此, 下面结论成立: 函数

$$
g _ {1} (x) = \left\{ \begin{array}{l l} \sin \frac {1}{x}, & x \neq 0, \\ 0, & x = 0, \end{array} \right. \quad g _ {2} (x) = \left\{ \begin{array}{l l} \cos \frac {1}{x}, & x \neq 0, \\ 0, & x = 0 \end{array} \right.
$$

在 $\mathbb{R}$ 上有原函数. 试证明这个结论. 进一步, 证明 $g_2^2(x)$ 在 $\mathbb{R}$ 上没有原函数.

7. 试问函数

$$
f (x) = \left\{ \begin{array}{l l} \frac {1}{x} \sin \frac {1}{x}, & x > 0, \\ 0, & x = 0 \end{array} \right.
$$

在 $[0, +\infty)$ 上是否有原函数？

8. 设 $F(x)$ 是 $f(x)$ 在 $\mathbb{R}$ 上的一个有下界的原函数. 证明: $\inf_{x \in \mathbb{R}} |f(x)| = 0$.
9. 设函数 $f(x)$ 和 $g(x)$ 在区间 $I$ 上都有原函数. 问 $f(x)g(x)$ 是否在区间 $I$ 上也必有原函数?

## 8.3 不定积分的性质与计算

## 8.3.1 积出来和积不出来

定理 8.2.1告诉我们, 区间 I 上的连续函数一定有原函数, 那么随之而来的问题是: 如何计算一个给定的连续函数的原函数? 事实上, 一个前置的问题是: 一个函数如果有原函数, 原函数总能算出来吗? 这个问题逻辑上非常类同于一个奇数次多项式在实数域上至少有一个实数根和这个根总能算出来吗? 的确, 原函数的存在性和能否表示出来是两个层面的问题.

要回答连续函数的原函数能否表达出来, 首先要明确什么是表达出来. 一个通俗的说法是: 用什么方式表达出来的函数才能称之为被积函数算出来了? 比如, 当我们稍后理解到变上限的定积分也可以表示函数时, 那么 $\int_{a}^{x} \mathrm{e}^{-t^2} \mathrm{d}t$ 就是 $\mathrm{e}^{-t^2}$ 的一个原函数. 我们能说它的不定积分能表达出来并且就是 $\int_{a}^{x}\mathrm{e}^{-t^2}\mathrm{d}t + c$ 吗？再比如，如果原函数是由极限，或者由无穷多个函数之和(函数项级数)或之积表示，我们能称这个不定积分的原函数表示出来了吗？基于此，我们对一个函数的原函数能表示出来给一些基本的限定.

被积函数的原函数如果能用基本初等函数, 或者基本初等函数的有限次代数运算 (四则运算、复合运算、反函数运算等), 那么就称为该被积函数能积出来, 即上面所说的表示出来. 否则, 即使原函数存在, 我们通常也称该被积函数积不出来.

要判断一个具体的函数能否积出来不是一件容易的事, 17、18 世纪诸多数学家曾经一度发展了诸多方法和技巧, 直到发现即使是一些表达式非常简捷的初等函数, 也很难求出原函数的表示, 人们才渐渐意识到可能有些函数就是积不出来的!

从理论上考虑一个函数能否积出来的开创性工作是19世纪上半叶由Liouville提出并研究的，后被诸多数学家给以推广。系统的研究需要用到微分代数方面的知识，已经远超本课的范围。有兴趣的读者可以作进一步的延伸阅读，参见文献[60]或追溯一下教学研究方面的论文。

## 1. 几个能积出来的函数

下面我们先给出几个后面学习中经常遇到的能积出来的初等函数以及它们的不定积分, 其正确性可以直接从前面的导数运算中得以验证.

(1) $\int 0\mathrm{d}x = c;$
(2) $\int x^{\mu} \, \mathrm{d}x = \frac{1}{\mu + 1} x^{\mu + 1} + c (\mu \neq -1)$;
(3) $\int \mathrm{e}^{x} \, \mathrm{d}x = \mathrm{e}^{x} + c;$
(4) $\int \frac{1}{x} \, \mathrm{d}x = \ln |x| + c;$
(5) $\int\cos x\,\mathrm{d}x=\sin x+c;$
(6) $\int \sin x\mathrm{d}x = -\cos x + c;$
(7) $\int \sec^2 x \, \mathrm{d}x = \tan x + c;$
(8) $\int \csc^2 x \, \mathrm{d}x = -\cot x + c;$
(9) $\int \frac{1}{\sqrt{1 + x^2}}\mathrm{d}x = \ln (x + \sqrt{1 + x^2}) + c;$
(10) $\int \frac{1}{\sqrt{1 - x^2}}\mathrm{d}x = \arcsin x + c;$
(11) $\int \frac{1}{1 + x^2} \, \mathrm{d}x = \arctan x + c;$
(12) $\int \sinh x \, \mathrm{d}x = \cosh x + c.$

注意, 原函数的表达形式可能不是唯一的, 这种形式上的差别本质上是由于原函数之间可以相差一个常数造成的. 比如上面列表中的不定积分 $\int \frac{1}{\sqrt{1 - x^2}} \mathrm{d}x$ 有原函数 $\arcsin x$, 也可以取 $-\arccos x$ 为原函数. 而 $\int \frac{1}{1 + x^2} \mathrm{d}x$ 可以有原函数 $\arctan x$, 也可以取 $-\operatorname{arccot} x$ 为原函数. 又比如不定积分

$$
I = \int \frac {1}{1 + x ^ {4}} \mathrm{d} x = \frac {\sqrt {2}}{8} \ln \frac {x ^ {2} + \sqrt {2} x + 1}{x ^ {2} - \sqrt {2} x + 1} - \frac {\sqrt {2}}{4} \arctan \frac {\sqrt {2} x}{x ^ {2} - 1} + c,
$$

也可以表示为

$$
I = \frac {\sqrt {2}}{4} \ln \frac {x ^ {2} + \sqrt {2} x + 1}{\sqrt {1 + x ^ {4}}} + \frac {\sqrt {2}}{4} \left(\arctan (\sqrt {2} x + 1) + \arctan (\sqrt {2} x - 1)\right) + c.
$$

## 2. 几个积不出来的函数

我们下面给出几个著名的积不出来的初等函数, 供读者了解. 这些被积函数很多源于有关学科中的具体背景, 有着广泛的应用和影响, 而且大多数积分还曾被冠以数学家的名字. 也有一些被积函数是根据 Liouville 积不出来的结论刻意构造出来的, 意在营造一种效果: 这些形式上看似很简单的初等函数是根本就积不出来的.

Gauss 积分类型: $\int x^{2n} \mathrm{e}^{-x^2} \, \mathrm{d}x (n \in \mathbb{N})$.

Fresnel $^{①}$  积分:  $\int\sin(x^{2})\mathrm{d}x,\quad\int\cos(x^{2})\mathrm{d}x.$

正弦、余弦积分: $\int \frac{\sin x}{x^n} \, \mathrm{d}x$, $\int \frac{\cos x}{x^n} \, \mathrm{d}x$ ($n \in \mathbb{N}$).

对数积分:

$$
\int \frac {\mathrm{d} t}{\ln t}, \quad \int \frac {\ln t}{1 + x} \mathrm{d} t, \quad \int \frac {\ln x}{x (1 + x)} \mathrm{d} x, \quad \int \frac {\ln x}{1 + x ^ {2}} \mathrm{d} x,
$$

$$
\int \ln (\sin t) \mathrm{d} t, \quad \int \ln (\cos t) \mathrm{d} t, \quad \int \ln (1 + \sin t) \mathrm{d} t, \quad \int \ln (1 + \cos t) \mathrm{d} t.
$$

指数积分: $\int \frac{\mathrm{e}^x}{x}\mathrm{d}x,\quad \int \frac{\mathrm{e}^x}{1 + x}\mathrm{d}x,\quad \int \frac{\mathrm{e}^x}{1 + x^2}\mathrm{d}x,\quad \int \frac{\mathrm{e}^x}{x(1 + x)}\mathrm{d}x.$

椭圆积分: $\int \frac{\mathrm{d}x}{\sqrt{(1 - x^2)(1 - k^2x^2)}}, \quad \int \frac{x^2\mathrm{d}x}{\sqrt{(1 - x^2)(1 - k^2x^2)}} (0 < k^2 < 1).$

事实上, 可以根据一般性结论构造出很多形式简捷但积不出来的函数, 只不过要介绍这些一般性结论需要大量篇幅, 超出课程范围. 比如, Chebyshev 在 19 世纪中叶证明了下面的结论.

定理 8.3.1 形如  $\int x^{m}(a+bx^{n})^{p}\mathrm{d}x$  (m,n,p 均为有理数) 的不定积分能积出来的充要条件是 p,  $\frac{m+1}{n}$ ,  $p+\frac{m+1}{n}$  三者至少有一个是整数.

那么根据这个结论, 我们可以构造下面形式简捷但积不出来的函数 (椭圆积分):

$$
\int \frac {1}{\sqrt {1 - x ^ {3}}} \mathrm{d} x, \quad \int \frac {1}{\sqrt {1 - x ^ {4}}} \mathrm{d} x.
$$

另一方面, 通过调整 $m, n, p$, 又可以断定不定积分

$$
\int \frac {\sqrt {x}}{\sqrt {1 - x ^ {3}}} \mathrm{d} x
$$

是能积出来的, 剩下的就看如何把它积出来了.

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">① Fresnel, Augustin-Jean, 1788 年 5 月 10 日 — 1827 年 7 月 14 日, 法国物理学家.</span></small>

## 8.3.2 不定积分的基本性质

虽然求原函数的初等表示渐渐被直接定性分析原函数所取代, 并且把积不出来的函数当作一种全新的函数来接受并加以研究, 但是, 即使今天我们仍然把寻求原函数的显式表示当作数学分析学习中的基本方法和重要内容, 因为如果被积函数能用初等函数表示出来的话, 在进一步的研究中毕竟还是有其方便之处的. 这一点在学到定积分 Newton-Leibniz 公式时愈发能感悟到不定积分的重要性. 因此, 在本章我们还要详细讨论不定积分的性质以及计算不定积分的常用方法.

首先从微分的性质和不定积分的定义,可以直接推导和验证下面的结论:

(1) 函数 $f(x)$ 的原函数的导数还是 $f(x)$，即

$$
\frac {\mathrm{d}}{\mathrm{d} x} \left(\int f (x) \mathrm{d} x\right) = f (x).
$$

这条性质说明对一个函数先实施积分  $\int$  运算, 再实施微分 d 运算, 其效果刚好抵消, 相当于恒等运算:

$$
\mathrm{d} \circ \int = \mathrm{id}.
$$

(2) 设  $F(x)$  是  $F'(x)$  的一个原函数, 则有

$$
\int F ^ {\prime} (x) \mathrm{d} x = F (x) + c, \quad \int \mathrm{d} F (x) = F (x) + c.
$$

这条性质说明对一个函数先实施微分 d 运算, 再实施积分  $\int$  运算, 其效果是得到了这个函数所在的函数类:

$$
\int \circ \mathrm{d}: f \mapsto f + c.
$$

结合上一条, 我们看到, 微分和积分在抹掉一个常数的意义下是一对逆运算.

(3) 设 k 是常数 ( $k \neq 0$ ), 则

$$
\int k f (x) \mathrm{d} x = k \int f (x) \mathrm{d} x.
$$

(4) 设 $f(x)$ 和 $g(x)$ 在区间 $I$ 上均有原函数, 则 $f(x) + g(x)$ 在 $I$ 上也有原函数, 且

$$
\int (f (x) \pm g (x)) \mathrm{d} x = \int f (x) \mathrm{d} x \pm \int g (x) \mathrm{d} x.
$$

性质 (3) 和 (4) 表明了不定积分运算的线性性.

![](images/page_264_image_19.jpg)

注8.3.1 在上面式子中, 应该注意以下一点: 当等式两端都含不定积分时,由于每个不定积分都包含一个任意常数项, 所以这类等式应理解为等式左右两端相差一个常数. 也可以理解为其中有一个积分不再是任意原函数, 而是

在其他积分常数选定之后被确定了.

## 8.3.3 不定积分的运算法则之一: 分部积分法

下面我们介绍计算不定积分时常用的几个法则. 首先求不定积分的一个重要法则是分部积分法, 它的成立本质上是基于两个函数乘积的导数法则.

回顾一下两个函数 $u(x)$ 和 $v(x)$ 乘积的求导法则

$$
\mathrm{d} (u (x) v (x)) = v (x) \mathrm{d} u (x) + u (x) \mathrm{d} v (x),
$$

即

$$
u (x) \mathrm{d} v (x) = \mathrm{d} (u (x) v (x)) - v (x) \mathrm{d} u (x),
$$

从而

$$
\int u (x) \mathrm{d} v (x) = u (x) v (x) - \int v (x) \mathrm{d} u (x).
$$

这就是分部积分法. 我们给出严格的描述.

定理 8.3.2 设 $u\left( x\right)$ 和 $v\left( x\right)$ 均有连续的导函数, 则

$$
\int u (x) v ^ {\prime} (x) \mathrm{d} x = u (x) v (x) - \int u ^ {\prime} (x) v (x) \mathrm{d} x. \tag {8.3.1}
$$

公式 (8.3.1) 在自变量不产生歧义时, 也常简记为

$$
\int u v ^ {\prime} \mathrm{d} x = u v - \int u ^ {\prime} v \mathrm{d} x.
$$

分部积分法是求不定积分时使用频率最高的法则之一, 它特别适合于由两个不同类型函数乘积构成的被积函数的不定积分. 通常情况下, 可以试着先求其中一部分 $v'(x)$ 的积分 $v(x)$, 然后将 $\int u(x)v'(x) \mathrm{d}x$ 转化为求解 $\int v(x)u'(x) \mathrm{d}x$. 通过把 $u$ 和 $v$ 的角色对换, 使得原来不易处理的函数的不定积分对换成相对容易讨论的函数的不定积分. 选择合适的 $u$ 和 $v$ 直接影响计算的效果, 这一点可以通过适量的练习积累一些感觉.

当我们熟练掌握了这个法则后, 可以不必每次都标出函数 u 和 v, 只要心中记住相应函数的变动规则即可. 另外, 分部积分法则可以重复多次使用, 即有如下推广.

定理 8.3.3 设函数  $u(x)$  和  $v(x)$  在区间 I 上均有 n 阶连续的导函数  $u'(x)$ ， $u''(x)$ ， $\cdots$ ， $u^{(n)}(x)$  和  $v'(x)$ ， $v''(x)$ ， $\cdots$ ， $v^{(n)}(x)$ ，则

$$
\int u v ^ {(n)} \mathrm{d} x = u v ^ {(n - 1)} - u ^ {\prime} v ^ {(n - 2)} + u ^ {\prime \prime} v ^ {(n - 3)} + \dots + (- 1) ^ {n} \int u ^ {(n)} v \mathrm{d} x. \tag {8.3.2}
$$

证明 根据定理 8.3.3, 通过一次分部积分, 可得

$$
\int u v ^ {(n)} \mathrm{d} x = \int u \mathrm{d} v ^ {(n - 1)} = u v ^ {(n - 1)} - \int v ^ {(n - 1)} \mathrm{d} u = u v ^ {(n - 1)} - \int u ^ {\prime} v ^ {(n - 1)} \mathrm{d} x.
$$

类似地, 有

$$
\begin{array}{l} \int u ^ {\prime} v ^ {(n - 1)} \mathrm{d} x = u ^ {\prime} v ^ {(n - 2)} - \int u ^ {\prime \prime} v ^ {(n - 2)} \mathrm{d} x, \\ \int u ^ {\prime \prime} v ^ {(n - 2)} \mathrm{d} x = u ^ {\prime \prime} v ^ {(n - 3)} - \int u ^ {\prime \prime \prime} v ^ {(n - 3)} \mathrm{d} x, \\ \int u ^ {(n - 1)} v ^ {\prime} \mathrm{d} x = u ^ {(n - 1)} v - \int u ^ {(n)} v \mathrm{d} x. \\ \end{array}
$$

...，

整理这些关系式, 即得 (8.3.2) 式.

□

例 8.3.1 求不定积分

$$
I _ {1} = \int x \sin x \mathrm{d} x, \quad I _ {2} = \int \arctan x \mathrm{d} x.
$$

解 设 $v = \cos x, u = x,$ 则

$$
\begin{array}{l} I _ {1} = - \int x \mathrm{d} (\cos x) = - x \cos x + \int \cos x \mathrm{d} x \\ = - x \cos x + \sin x + c. \\ \end{array}
$$

为了计算 $I_{2}$, 可以设 $v = x, u = \arctan x$, 则有

$$
\begin{array}{l} I _ {2} = x \arctan x - \int x \mathrm{d} (\arctan x) \\ = x \arctan x - \int \frac {x}{1 + x ^ {2}} \mathrm{d} x \\ = x \arctan x - \frac {1}{2} \ln (1 + x ^ {2}) + c. \\ \end{array}
$$

例8.3.2 计算不定积分

$$
\int x ^ {n} \ln x \mathrm{d} x.
$$

解 可以取 $u = \ln x, \mathrm{d}v = x^n\mathrm{d}x.$ 于是

$$
\mathrm{d} u = \frac {\mathrm{d} x}{x}, \quad v = \frac {1}{n + 1} x ^ {n + 1}.
$$

因此

$$
\int x ^ {n} \ln x \mathrm{d} x = \frac {1}{n + 1} x ^ {n + 1} \ln x - \frac {1}{n + 1} \int x ^ {n} \mathrm{d} x = \frac {1}{n + 1} x ^ {n + 1} \ln x - \frac {1}{(n + 1) ^ {2}} x ^ {n + 1}.
$$

例 8.3.3 (反函数的原函数) 设  $f(x)$  有可微的反函数  $f^{-1}(x)$ ,  $F(x)$  为  $f(x)$  的一个原函数, 则

$$
\int f ^ {- 1} (x) \mathrm{d} x = x f ^ {- 1} (x) - F (f ^ {- 1} (x)) + c.
$$

证明 等式右端事实上是通过分部积分得到的, 下面我们给以验证. 为此, 在等式右端关于 $x$ 求导, 得

$$
\begin{array}{l} \frac {\mathrm{d}}{\mathrm{d} x} \left(x f ^ {- 1} (x) - F (f ^ {- 1} (x)) + c\right) \\ = f ^ {- 1} (x) + x \frac {\mathrm{d}}{\mathrm{d} x} f ^ {- 1} (x) - f (f ^ {- 1} (x)) \frac {\mathrm{d}}{\mathrm{d} x} f ^ {- 1} (x) \\ = f ^ {- 1} (x) + x \frac {\mathrm{d}}{\mathrm{d} x} f ^ {- 1} (x) - x \frac {\mathrm{d}}{\mathrm{d} x} f ^ {- 1} (x) = f ^ {- 1} (x). \\ \end{array}
$$

有很多重要的被积函数的不定积分需要多次使用分部积分求得,比如下面的例子.

例 8.3.4 计算不定积分

$$
I _ {n} = \int \frac {1}{(x ^ {2} + 1) ^ {n}} \mathrm{d} x.
$$

解 由

$$
\begin{array}{l} I _ {n} = \frac {x}{(x ^ {2} + 1) ^ {n}} + 2 n \int \frac {x ^ {2}}{(x ^ {2} + 1) ^ {n + 1}} \mathrm{d} x \\ = \frac {x}{(x ^ {2} + 1) ^ {n}} + 2 n I _ {n} - 2 n I _ {n + 1}, \\ \end{array}
$$

得

$$
I _ {n + 1} = \frac {x}{2 n (x ^ {2} + 1) ^ {n}} + \frac {2 n - 1}{2 n} I _ {n}.
$$

然后递推可得到 $I_{n}$ 的一般表达式. 特别地, 有

$$
I _ {2} = \int \frac {\mathrm{d} x}{\left(x ^ {2} + 1\right) ^ {2}} = \frac {x}{2 \left(x ^ {2} + 1\right)} + \frac {1}{2} \arctan x + c.
$$

## 8.3.4 不定积分的运算法则之二:换元积分法

换元积分法是计算不定积分时另一种常用的手法, 它本质上对应于复合函数的求导法则, 是基于一阶微分的形式不变性这一条性质的应用. 具体来说, 我们有

$$
f (u (x)) u ^ {\prime} (x) \mathrm{d} x = f (u) \mathrm{d} u,
$$

其中 $u = u(x)$ .因此，我们有

$$
\int f (u (x)) u ^ {\prime} (x) \mathrm{d} x = \int f (u) \mathrm{d} u. \tag {8.3.3}
$$

我们通过下面两个例子, 分别说明常见的两种换元积分方法. 它们分别对应关系式 (8.3.3) 中左端和右端之一的不定积分容易计算时的典型做法. 具体来说, 一种情况是左端的不定积分不是一下子能够看出来的, 而右端的不定积分相对容易求得. 此时, 我们需要做的是甄别出哪个因子是 $u'(x)$, 需要确定 $f(u(x))$. 由于我们看到的是乘积 $f(u(x))u'(x)$, 因此, 这种甄别并不平凡, 需要把若干因子 “打包” 成 $u(x)$.

另一种情况则是左端的不定积分容易计算, 而右端的不定积分难以计算. 此时, 我们需要寻找合适的  $u = u(x)$ , 使得右端关于 u 的积分转化为左端关于 x 的积分.

例8.3.5 若 $\int f(u)\mathrm{d}u = F(u) + c.$ 试求不定积分 $\int f(ax + b)\mathrm{d}x$ $(a\neq 0)$

解 初步观察可以发现, 如果把  $ax + b$  打包成复合函数求导中的  $u(x)$ , 那么  $f(ax + b)$  的问题形式上就得到了处理  $f(u(x))$ . 即令  $u = u(x) = ax + b$ , 则  $u'(x) \, dx = a \, dx$ . 由

$$
\int f (u (x)) u ^ {\prime} (x) \mathrm{d} x = \int f (u) \mathrm{d} u,
$$

得

$$
\int f (a x + b) \cdot a \mathrm{d} x = \int f (u) \mathrm{d} u = F (u) + c = F (a x + b) + c.
$$

所以

$$
\int f (a x + b) \mathrm{d} x = \frac {1}{a} F (a x + b) + \tilde {c}.
$$

特别地, 当  $a, b (a \neq 0)$  为某些特定值时, 如下关系式成立:

$$
\int f (a x) \mathrm{d} x = \frac {1}{a} F (a x) + c _ {1}, \quad \int f (x + b) \mathrm{d} x = F (x + b) + c _ {2}.
$$

例 8.3.6 求不定积分  $\int\frac{dx}{\sqrt{a^{2}+x^{2}}}$ ，其中 a>0.

解 这里从被积函数中不易看出哪些因子可以凑在一起打包成 $u(x)$。我们采取另一种尝试, 即能否造出一个 $u(x)$ 来, 同时考虑到 $\mathrm{d}u(x)$ 产生的效果, 使得被积函数变成我们熟悉的函数. 比如, 我们试着用 $x = a \tan t \left( |t| < \frac{\pi}{2} \right)$ 去替换被积函数中的 $x$, 这样一来, 有

$$
\frac {\mathrm{d} x}{\sqrt {a ^ {2} + x ^ {2}}} = \frac {\cos t}{a} \cdot \frac {a \mathrm{d} t}{\cos^ {2} t} = \frac {\mathrm{d} t}{\cos t}.
$$

因此, 我们有

$$
\int \frac {\mathrm{d} x}{\sqrt {a ^ {2} + x ^ {2}}} = \int \frac {\mathrm{d} t}{\cos t} = \int \frac {\cos t   \mathrm{d} t}{\cos^ {2} t} = \int \frac {\mathrm{d} \sin t}{1 - \sin^ {2} t}.
$$

最后这个式子的积分可以通过下面的方式计算出来: 令 $v = \sin t$,

$$
\begin{array}{l} \int \frac {\mathrm{d} \sin t}{1 - \sin^ {2} t} = \int \frac {\mathrm{d} v}{1 - v ^ {2}} = \frac {1}{2} \left(\int \frac {\mathrm{d} v}{1 - v} + \int \frac {\mathrm{d} v}{1 + v}\right) \\ = \frac {1}{2} \ln \left| \frac {1 + v}{1 - v} \right| + c. \\ \end{array}
$$

注意到  $v = \sin t = \frac{x}{\sqrt{a^{2} + x^{2}}}$ ，所以有

$$
\frac {1 + v}{1 - v} = \frac {1 + \sin t}{1 - \sin t} = \frac {\sqrt {a ^ {2} + x ^ {2}} + x}{\sqrt {a ^ {2} + x ^ {2}} - x} = \frac {1}{a ^ {2}} (x + \sqrt {a ^ {2} + x ^ {2}}) ^ {2}.
$$

最后得到

$$
\int \frac {\mathrm{d} x}{\sqrt {a ^ {2} + x ^ {2}}} = \ln (x + \sqrt {a ^ {2} + x ^ {2}}) + \tilde {c},
$$

其中  $\tilde{c}$  是把原来不定积分中的任意常数 c 和 a 考虑进去后的一个常数.

注8.3.2 形式上与上例中的被积函数相近的还有如下几个不定积分:

$$
\int \frac {\mathrm{d} x}{\sqrt {a ^ {2} - x ^ {2}}}, \quad \int \frac {\mathrm{d} x}{\sqrt {x ^ {2} - a ^ {2}}}, \quad \int \sqrt {a ^ {2} \pm x ^ {2}} \mathrm{d} x, \quad \int \sqrt {x ^ {2} - a ^ {2}} \mathrm{d} x.
$$

它们都是重要的被积函数, 建议读者试试相应的计算.

## 习题8.3

1. 求下列不定积分:

(1) $\int \frac{\mathrm{d}x}{1 + \cos x}$;
(3) $\int \frac{\mathrm{d}x}{\cos^3 x}$.
(5) $\int \sin mx\cos nx\mathrm{d}x;$

2. 求下列不定积分:

(1) $\int \frac{\mathrm{d}x}{\sqrt{x}(1 - x)};$
(3) $\int \sin^3 x\cos x\mathrm{d}x;$
(5) $\int \frac{\mathrm{d}x}{\sqrt{(x - a)(b - x)}};$
(7) $\int (a^2 - x^2)^{-\frac{3}{2}} \mathrm{~d}x;$
(9) $\int x^{5}(1 + x)^{-1}\mathrm{d}x;$

3. 求下列不定积分:

(1) $\int x^{2} \mathrm{e}^{-3x} \, \mathrm{d}x$;
(3) $\int x\sin^{-2}x\mathrm{d}x;$
(5) $\int \sqrt{x(1 - x^3)}\mathrm{d}x;$
(7) $\int x^{2}\arctan x\mathrm{d}x;$

(2) $\int \frac{\mathrm{d}x}{1 + \sin x}$;
(4) $\int \frac{\mathrm{d}x}{\cos^4 x}$.
(6) $\int \sin mx\sin nx\mathrm{d}x.$
(2) $\int x^{-\frac{1}{2}} (1 + x)^{-1} \, \mathrm{d}x$;
(4) $\int \frac{\mathrm{d}x}{a^2\sin^2 x + b^2\cos^2 x}$;
(6) $\int (x^{2} + a^{2})^{-\frac{3}{2}}\mathrm{d}x;$
(8) $\int (\arctan x)^2\mathrm{d}x;$
(10) $\int \frac{\mathrm{d}x}{a\sin x + b\cos x}.$
(2) $\int \cos (\ln x)\mathrm{d}x;$
(4) $\int x^{2}\sin 2x\mathrm{d}x;$
(6) $\int x^{2}\arccos x\mathrm{d}x;$
(8) $\int x^{2}(1 + x^{2})^{-2}\mathrm{d}x;$

(9) $\int x^{2}\sqrt{a^{2} + x^{2}}\mathrm{d}x;$
(10) $\int \sin x\ln (\tan x)\mathrm{d}x;$
(11) $\int \arctan \sqrt{x} \, \mathrm{d}x$;
(12) $\int \sin^{-2} x \ln (\sin x) \, \mathrm{d}x$;
(13) $\int x^{-2}\arcsin x\mathrm{d}x;$
(14) $\int x\ln \left(\frac{1 + x}{1 - x}\right)\mathrm{d}x;$
(15) $\int \ln (x + \sqrt{1 + x^2})\mathrm{d}x.$

4. 求下列不定积分的递推公式 (m, n 为非负整数):

(1) $\int \sin^n x \, \mathrm{d}x$;

(2) $\int \cos^n x\mathrm{d}x;$

(3) $\int \sin^{-n} x \, \mathrm{d}x$;

(4) $\int \cos^{-n} x \, \mathrm{d}x$;

(5) $\int (\arcsin x)^n\mathrm{d}x;$

(6) $\int (\ln x)^n\mathrm{d}x;$

(7) $\int x^{n} \mathrm{e}^{x} \, \mathrm{d}x$;

(8) $\int \sin^m x\cos^n x\mathrm{d}x;$

(9) $\int x^{n}(1 + x)^{-1}\mathrm{d}x.$

5. 计算  $\int xf''(x) \, dx$ .

## 8.4 几类能积出来的初等函数的不定积分

## 8.4.1 有理函数的不定积分

有理函数是为数不多的能确保积出来的函数类, 我们下面详细介绍一下有理函数类不定积分的求法.

首先, 所谓的有理函数是指形如 $f(x) = \frac{P(x)}{Q(x)}$ 的函数, 其中 $P(x)$ 和 $Q(x)$ 均为实系数多项式. 利用多项式的带余除法, 我们总可以把它写成如下形式:

$$
f (x) = \frac {P (x)}{Q (x)} = P _ {0} (x) + \frac {P _ {1} (x)}{Q (x)},
$$

其中 $P_{0}(x)$ 和 $P_{1}(x)$ 为实系数多项式, 且 $P_{1}(x)$ 的次数低于 $Q(x)$ 的次数. 由于多项式 $P_{0}(x)$ 的不定积分很容易求得, 因此我们仅需考虑 $\frac{P_{1}(x)}{Q(x)}$ 的不定积分. 所以下面我们不妨假设 $f(x) = \frac{P(x)}{Q(x)}$ 已经是既约真分式的有理函数, 即 $P(x)$ 的次数严格低于 $Q(x)$ 的次数, 且两者互素.

下面的定理是代数学中的一个结论, 其证明不难在高等代数教科书中找到, 在此不

再证明. 需要注意的是以下所有结论都是在实数域内.

定理 8.4.1 设  $f(x)=\frac{P(x)}{Q(x)}$  是一个真分式有理函数, 则

(1) $Q(x)$ 有不可约因子分解

$$
Q (x) = (x - a _ {1}) ^ {k _ {1}} \dots (x - a _ {r}) ^ {k _ {r}} (x ^ {2} + p _ {1} x + q _ {1}) ^ {\ell_ {1}} \dots (x ^ {2} + p _ {s} x + q _ {s}) ^ {\ell_ {s}},
$$

其中  $a_{i}, p_{j}, q_{j}$  为实数,  $k_{i}, \ell_{j}$  为正整数,  $p_{j}^{2} - 4q_{j} < 0, i = 1, 2, \cdots, r, j = 1, 2, \cdots, s.$

(2) $f(x)$ 有分解式

$$
\begin{array}{l} f (x) = \frac {A _ {1 1}}{x - a _ {1}} + \frac {A _ {1 2}}{(x - a _ {1}) ^ {2}} + \dots + \frac {A _ {1 k _ {1}}}{(x - a _ {1}) ^ {k _ {1}}} + \dots + \\ \frac {A _ {r 1}}{x - a _ {r}} + \frac {A _ {r 2}}{(x - a _ {r}) ^ {2}} + \dots + \frac {A _ {r k _ {r}}}{(x - a _ {r}) ^ {k _ {r}}} + \\ \frac {B _ {1 1} x + C _ {1 1}}{x ^ {2} + p _ {1} x + q _ {1}} + \frac {B _ {1 2} x + C _ {1 2}}{(x ^ {2} + p _ {1} x + q _ {1}) ^ {2}} + \dots + \frac {B _ {1 \ell_ {1}} x + C _ {1 \ell_ {1}}}{(x ^ {2} + p _ {1} x + q _ {1}) ^ {\ell_ {1}}} + \dots + \\ \frac {B _ {s 1} x + C _ {s 1}}{x ^ {2} + p _ {s} x + q _ {s}} + \frac {B _ {s 2} x + C _ {s 2}}{(x ^ {2} + p _ {s} x + q _ {s}) ^ {2}} + \dots + \frac {B _ {s \ell_ {s}} x + C _ {s \ell_ {s}}}{(x ^ {2} + p _ {s} x + q _ {s}) ^ {\ell_ {s}}}, \\ \end{array}
$$

其中所有参数  $A_{ij}, B_{ij}, C_{ij}$  均为唯一确定的实数.

根据这个定理容易看出, 所求函数  $f(x)$  的不定积分本质上就是两类函数的不定积分的线性组合:

$$
\frac {A}{(x - a) ^ {k}}, \qquad \frac {B x + C}{(x ^ {2} + p x + q) ^ {\ell}}, \quad \text {其中} p ^ {2} - 4 q <   0.
$$

所以, 我们只需处理这两类积分即可.

首先, 对于不定积分  $\int\frac{A}{(x-a)^{k}}\mathrm{d}x\ (k\in\mathbb{N})$ , 易见有如下结果:

(1) 当 k = 1 时,

$$
\int \frac {A}{(x - a) ^ {k}} \mathrm{d} x = \ln | x - a | + c.
$$

(2) 当 k > 1 时,

$$
\int \frac {A}{(x - a) ^ {k}} \mathrm{d} x = \frac {1}{1 - k} (x - a) ^ {1 - k} + c.
$$

其次, 对于不定积分  $\int\frac{Bx+C}{(x^{2}+px+q)^{\ell}}\mathrm{d}x\ (\ell\in\mathbb{N})$ , 我们作如下处理:

$$
x ^ {2} + p x + q = \left(x + \frac {p}{2}\right) ^ {2} + q - \frac {p ^ {2}}{4} = u ^ {2} + \mu^ {2},
$$

其中 $u = x + \frac{p}{2},\mu^2 = q - \frac{p^2}{4}$ .这样一来，

$$
\int \frac {B x + C}{(x ^ {2} + p x + q) ^ {\ell}} \mathrm{d} x = B \int \frac {u}{(u ^ {2} + \mu^ {2}) ^ {\ell}} \mathrm{d} u + \left(C - \frac {B p}{2}\right) \int \frac {1}{(u ^ {2} + \mu^ {2}) ^ {\ell}} \mathrm{d} u.
$$