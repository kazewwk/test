$$
R (x) := \left\{ \begin{array}{l l} {1,} & {x = 0,} \\ {\frac {1}{q},} & {x = \frac {p}{q}} \\ {0,} & {x \in \mathbb {Q}.} \end{array} \right. (\text {其中} p, q \text {为既约整数}),
$$

证明 R 在有理点不连续, 在无理点连续.

3. 设 $S_{n} = \frac{1}{n^{2}}\sum_{k=0}^{n}\ln C_{n}^{k}$. 求 $\lim_{n\to+\infty} S_{n}$.

4. 设 $\lim_{x\to 0}f(x) = 0,\lim_{x\to 0}\frac{f(2x) - f(x)}{x} = 0.$ 证明 $\lim_{x\to 0}\frac{f(x)}{x} = 0.$

5. 称 $\mathbb{R}$ 上函数 $f$ 满足局部 Lipschitz$^{\text{①}}$ 条件, 是指对任何 $x \in \mathbb{R}$, 存在 $\delta > 0$ 以及 $M > 0$ 使得

$$
| f (y) - f (z) | \leqslant M | y - z |, \quad \forall y, z \in (x - \delta , x + \delta).
$$

证明: $f$ 在 $\mathbb{R}$ 上满足局部 Lipschitz 条件等价于对任何 $A > 0$, 存在 $M_A > 0$ 使得

$$
| f (x) - f (y) | \leqslant M _ {A} | x - y |, \quad \forall x, y \in [ - A, A ].
$$

6. 设 $f$ 为 $\mathbb{R}$ 上函数. 对任何 $x \in  \mathbb{R}$ ,存在 $\delta  > 0$ 以及 $M > 0$ 使得

$$
| f (y) - f (x) | \leqslant M | y - x |, \quad \forall y \in (x - \delta , x + \delta).
$$

问: f 是否一定满足局部 Lipschitz 条件?

7. 设 $f$ 是 $[a, b]$ 上的单调连续函数, $\{a_{n}\}$ 是 $[a, b]$ 中的点列. 证明:

(1) 若 $f$ 单增, 则 $\lim_{n\to +\infty}f(a_n) = f(\lim_{n\to +\infty}a_n), \lim_{n\to +\infty}f(a_n) = f(\lim_{n\to +\infty}a_n);$
(2) 若 $f$ 单减, 则 $\varlimsup_{n\to +\infty}f(a_n) = f(\varliminf_{n\to +\infty}a_n), \varliminf_{n\to +\infty}f(a_n) = f(\varlimsup_{n\to +\infty}a_n).$

8. 将习题 7 推广到广义实数系情形.

9. 证明区间 $I$ 上的单调函数的间断点均为跳跃间断点, 且间断点全体至多可列.

10. 设 $\{x_k\}_{k=1}^{\infty}$ 为 $\mathbb{R}$ 中点列, 定义 $f(x) := \sum_{k=1}^{\infty} \frac{1}{2^k} \chi_{(x_k, +\infty)}(x)$. 证明: $f$ 的间断点全体为 $\{x_k | k \geqslant 1\}$.

进一步, 若 $\{x_{k}\}$ 在 $\mathbb{R}$ 中稠密, 则 $f$ 在 $\mathbb{R}$ 上严格单增.

11. 将区间  $(0,1)$  内的实数用十进制小数  $0.a_{1}a_{2}a_{3}\cdots a_{n}\cdots$  表示, 约定不将 9 作为循环节. 定义

$$
f (0. a _ {1} a _ {2} a _ {3} \dots a _ {n} \dots) := 0. a _ {1} 0 a _ {2} 0 a _ {3} 0 \dots a _ {n} 0 \dots ,
$$

试问 $f$ 在 $(0,1)$ 内的哪些点连续，哪些点不连续？

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">① Lipschitz, Rudolf Otto Sigismund, 1832 年 5 月 14 日—1903 年 10 月 7 日, 德国数学家.</span></small>

12. 设正数列 $\{a_{n}\}$ 满足 $\lim_{n\to +\infty}a_{n} = 1, \overline{\lim}_{n\to +\infty}a_{n} = 2$ 及 $\lim_{n\to +\infty}\sqrt[n]{\prod_{k=1}^{n}a_{k}} = 1.$ 证明: $\lim_{n\to +\infty}\frac{1}{n}\sum_{k=1}^{n}a_{k} = 1.$

13. 证明: R 上实连续函数全体的势为 N.

14. 设 $f$ 在 $(0, +\infty)$ 上连续, 且对于任何 $a \in (0, +\infty)$, $\lim_{n \to +\infty} f(na) = 0$. 证明: $\lim_{x \to +\infty} f(x) = 0$.

## 5.2 基本初等函数的连续性

这一节要讨论的是初等函数在其定义域内的连续性. 关于初等函数, 这里不给出严格定义. 简单地讲, 初等函数是基本初等函数经过有限次的四则运算和复合运算得到的函数. 更确切一点, 在这种运算中需要把所谓代数函数包含进去. 函数 $f$ 称为代数函数, 是指满足一个代数方程的解析函数①, 具体地, 就是存在多项式 $a_{n}(\cdot), a_{n-1}(\cdot), \cdots, a_{0}(\cdot)$, 使得 $f$ 满足不可约方程

$$
a _ {n} (x) f ^ {n} (x) + a _ {n - 1} (x) f ^ {n - 1} (x) + \dots + a _ {1} (x) f (x) + a _ {0} (x) = 0,
$$

其中  $n \geqslant 1, a_{n}(\cdot) \neq 0.$

初等函数的连续性可由基本初等函数的连续性以及复合函数、反函数的连续性得到.因此,接下来主要建立基本初等函数的连续性以及有关复合函数连续性和反函数连续性的定理.

## 5.2.1 连续函数和、差、积、商的连续性

首先, 由极限的四则运算, 立即可得连续函数和、差、积、商的连续性.

定理 5.2.1 设  $\delta > 0$ ，函数 f 和 g 在  $(x_{0} - \delta, x_{0} + \delta)$  内有定义，且 f, g 在点  $x_{0}$  处连续.

(1) 设  $\alpha, \beta$  为常数, 则  $\alpha f + \beta g$  在点  $x_{0}$  处连续;
(2) fg 在点  $x_{0}$  处连续;
(3) 若  $g(x_{0}) \neq 0$ ，则  $\frac{f}{g}$  在点  $x_{0}$  处连续.

自然, 把定理中的连续改为左连续或右连续, 或在定义 5.1.4 意义下考虑连续性, 定理也成立.

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">① 这里的解析性可允许有个别例外点.</span></small>

## 5.2.2 复合函数的连续性

由于连续的本质是取极限和取函数值可以交换次序, 因此, 连续函数与连续函数复合得到的是连续函数. 具体地, 有如下定理.

定理 5.2.2 设 g 在区间  $(a, b)$  内有定义, 在点  $x_{0} \in (a, b)$  处连续. 又设  $g(a, b) \subseteq (c, d)$ , f 在  $(c, d)$  内有定义, 在点  $y_{0} = g(x_{0})$  处连续. 则  $f \circ g$  在点  $x_{0}$  处连续.

证明 由定理条件, $f \circ g$ 在 $(a, b)$ 内有定义.

任取 $(a, b)$ 内趋于 $x_0$ 的点列 $\{x_n\}$, 由 $g$ 的连续性以及 Heine 定理 5.1.1, 得到 $\lim_{n \to +\infty} g(x_n) = g(x_0)$. 于是, 由 $f$ 在点 $y_0 = g(x_0)$ 处的连续性, 并再次利用 Heine 定理 5.1.1, 得到 $\lim_{n \to +\infty} f(g(x_n)) = f(g(x_0))$. 这就是说 $f \circ g$ 在点 $x_0$ 处连续.

注 5.2.1 本质上, 定理 5.2.2 就是如下的关系式成立:

$$
\lim _ {x \to x _ {0}} f (g (x)) = f (\lim _ {x \to x _ {0}} g (x)) = f (g (\lim _ {x \to x _ {0}} x)) = f (g (x _ {0})). \tag {5.2.1}
$$

(5.2.1) 式自然是正确的, 也比较显然. 其推导过程可以视为使用了 Heine 定理 5.1.1 的一种推广:

设 $f$ 在 $(c,d)$ 内有定义，$y_0 \in (c,d)$，则 $\lim_{y \to y_0} f(y) = f(y_0)$ 当且仅当对任何取值于 $(c,d)$ 并满足 $\lim_{x \to x_0} g(x) = y_0$ 的函数 $g$，有 $\lim_{y \to y_0} f(g(x)) = f(y_0)$.

但初次使用就利用 (5.2.1) 式, 略微显得有点跳跃. 定理 5.2.2 的证明可以认为是 (5.2.1) 式的一个证明.

这里也可以看到, 极限运算中运用变量代换可以视为复合函数连续性的一个应用.

类似地, 可以给出复合函数左连续或右连续对应的相关定理.

在定理 5.2.2 中, $g(a,b) \subseteq (c,d)$, $f$ 在 $(c,d)$ 内有定义. 这样点 $x_0$ 是复合函数 $f \circ g$ 定义域的内点. 但时常两个函数的复合不是严格意义上定义域和值域匹配的复合, 例如基本初等函数复合过程中, 自然定义域就会产生变化. 一方面, 自然定义域有时候会出现左端点或右端点, 甚至出现孤立点. 这会给论证过程中的讨论带来一些麻烦. 利用定义 5.1.4 所定义的一般集合上函数的连续性, 则可以把各种情形都归并到一起.

定理 5.2.3 设 g 是 E 上的函数, 在点  $x_{0} \in E$  处连续. 又设  $y_{0} = g(x_{0}) \in F$ , 而 f 是 F 上的函数, 在点  $y_{0}$  处连续. 则  $f \circ g : E \cap g^{-1}(F) \to \mathbb{R}$  在点  $x_{0}$  处连续, 这里  $g^{-1}(F) = \{x | g(x) \in F\}$ .

## 5.2.3 反函数的连续性

现在, 我们来给出反函数的连续性.

定理 5.2.4 设 f 是  $[a, b]$  上严格单调的连续函数, 则 f 的反函数  $f^{-1}: f[a, b] \rightarrow R$  连续.

证明 由于 $f$ 严格单调, 因此它是单射, 从而反函数 $f^{-1}$ 存在. 不妨设 $f$ 严格单增. 任取 $y_0 \in f(a, b)$, 记 $x_0 = f^{-1}(y_0)$, 则 $x_0 \in (a, b)$.

对任何 $0 < \varepsilon < \min \{x_0 - a, b - x_0\}$, 令 $\delta := \min \{y_0 - f(x_0 - \varepsilon), f(x_0 + \varepsilon) - y_0\}$. 则当 $|y - y_0| < \delta$ 时,

$$
f (x _ {0} - \varepsilon) <   y <   f (x _ {0} + \varepsilon).
$$

从而

$$
f ^ {- 1} (y _ {0}) - \varepsilon = x _ {0} - \varepsilon <   f ^ {- 1} (y) <   x _ {0} + \varepsilon = f ^ {- 1} (y _ {0}) + \varepsilon .
$$

即 $f^{-1}$ 在点 $y_0 \in f(a, b)$ 处连续. 同理可证 $f^{-1}$ 在点 $f(a)$ 与 $f(b)$ 处连续.

细看定理 5.2.4 的证明, 可以发现没有用到 f 的连续性. 这里的问题在于我们没有说明满足  $|y - y_{0}| < \delta$  的 y 都在  $f^{-1}$  的定义域内, 即在 f 的值域内. 而要说明这一点, 需要下一节的介值定理 (参见定理 5.3.1). 另一方面, 如果按照一般集合上函数的连续性定义, 我们不要求  $f^{-1}$  的定义域为区间, 那么上述证明过程中, 追加  $y \in f[a, b]$  后就是正确的. 更确切地, 我们有如下结果.

定理5.2.5 设 $f$ 是 $[a,b]$ 上严格单调的函数，则 $f$ 的反函数 $f^{-1}:f[a,b]\to \mathbb{R}$ 连续.

易见 $f^{-1}$ 是 $f[a,b]$ 上严格单调的函数, 但它的反函数即 $f$ 不一定连续. 在此可以看到, 在保证 $f^{-1}$ 连续这个问题上, $f$ 的定义域为区间起到了重要的作用.

## 5.2.4 基本初等函数的连续性

有了前面各小节的理论基础, 我们来逐一讨论基本初等函数在其定义域内的连续性. 具体地, 我们要考察如下函数的连续性:

$$
x ^ {a}, a ^ {x}, \log_ {a} x, \sin x, \cos x, \tan x, \cot x, \sec x, \csc x, \arcsin x, \arccos x, \arctan x.
$$

## 1. 幂函数在其定义域内连续

根据 $a \neq 0$ 的不同情况，幂函数 $x^a$ 的定义域有四种情况:$(0, +\infty), [0, +\infty)$，$\mathbb{R} \setminus \{0\}$，$\mathbb{R}$。现设 $x^a$ 在点 $x_0$ 处有定义。

(1) $x_0 > 0$. 无论哪种情形, $x^a$ 在 $(0, +\infty)$ 内有定义. 对于, $x^a = \mathrm{e}^{a\ln x}$, 因此, $x^a$ 在 $(0, +\infty)$ 内的连续性可由指数函数和对数函数的连续性得到.

自然, 也可以直接通过以下不等式得到连续性: 记 $n = [|a|] + 1$, 则

$$
\left| x ^ {a} - x _ {0} ^ {a} \right| = x _ {0} ^ {a} \Big | \Big (\frac {x}{x _ {0}} \Big) ^ {a} - 1 \Big | \leqslant x _ {0} ^ {a} \Big (\Big | \Big (\frac {x}{x _ {0}} \Big) ^ {n} - 1 \Big | + \Big | \Big (\frac {x}{x _ {0}} \Big) ^ {- n} - 1 \Big | \Big), \quad \forall x > 0.
$$

另外, 也可以利用更精细的 (4.3.4) 式得到结论.

(2) $x_0 < 0$. 若 $x^a$ 在 $x_0 < 0$ 有定义, 则必在 $(- \infty, 0)$ 内有定义, 且此时

$$
x ^ {a} = (- 1) ^ {a} (- x) ^ {a}, \quad \forall x <   0.
$$

这样, 此种情形下, $x^{a}$ 在 $(- \infty, 0)$ 内的连续性可由 (1) 的结论得到.

(3) $x_0 = 0$. $x^a$ 在 $x_0 = 0$ 有定义当且仅当 $a > 0$. 此时, 直接从极限定义可得 $\lim_{x \to 0^+} x^a = 0$. 即此时 $x^a$ 在 0 点处右连续.

若进一步, $x^{a}$ 在整个 $\mathbb{R}$ 上有定义, 则利用 $|x^{a}| = |x|^{a}$, 可得此时有 $\lim_{x\to 0}x^a = 0$. 即此时 $x^{a}$ 在0点处连续.

总之, 幂函数在定义域内连续. 其中, 当 0 是 $x^{a}$ 定义域的左端点时, $x^{a}$ 在 0 点处右连续.

## 2. 指数函数在其定义域内连续

具体地, 对于 $a > 0, a \neq 1, a^x$ 在 $\mathbb{R}$ 内连续.

注意到 $a^x = a^{x_0}a^{x - x_0}$ ，我们只要证明 $a^x$ 在0点处的连续性.而在例4.3.1中，我们已经证明了 $\lim_{x\to 0}a^x = 1.$ 因此，指数函数在其定义域内连续

## 3. 对数函数在其定义域内连续

具体地, 对于 $a > 0, a \neq 1, \log_a x$ 在 $(0, +\infty)$ 内连续.

利用定理 5.2.4, 对数函数作为指数函数的反函数, 它在其定义域内连续.

自然也可以从定义出发直接证明.

## 4. 三角函数在其定义域内连续

(1) $\sin x$ 在 $\mathbb{R}$ 上连续.

首先, 由 $\lim_{x\to 0}\frac{\sin x}{x} = 1$ (参见(4.3.6)式) 可得 $\lim_{x\to 0}\sin x = 0$, 即 $\sin x$ 在0点处连续. 任取 $x_0\in \mathbb{R}$, 我们有

$$
\left| \sin x - \sin x _ {0} \right| = \left| 2 \cos \frac {x + x _ {0}}{2} \sin \frac {x - x _ {0}}{2} \right| \leqslant 2 \left| \sin \frac {x - x _ {0}}{2} \right|. \tag {5.2.2}
$$

结合 $\sin x$ 在0点处的连续性以及夹逼准则可得 $\lim_{x\to x_0}\sin x = \sin x_0$ 即 $\sin x$ 在 $\mathbb{R}$ 上连续.

(2) 由 $\cos x = \sin \left(x + \frac{\pi}{2}\right)$ 即得 $\cos x$ 在 $\mathbb{R}$ 上连续.

(3) 由连续函数四则运算的性质得到 $\tan x, \cot x, \sec x, \csc x$ 等函数在各自的定义域内连续.

## 5. 反三角函数在其定义域内连续

利用定理 5.2.4, 如下反三角函数均为连续函数:

$$
\begin{array}{l} \arcsin x: [ - 1, 1 ] \rightarrow \left[ - \frac {\pi}{2}, \frac {\pi}{2} \right], \\ \arccos x: [ - 1, 1 ] \rightarrow [ 0, \pi ], \\ \arctan x: (- \infty , + \infty) \rightarrow \left(- \frac {\pi}{2}, \frac {\pi}{2}\right). \\ \end{array}
$$

## 5.2.5 几个常用的重要极限

利用本节的定理, 尤其是复合函数的连续性, 可以大大丰富我们之前得到的极限关系式. 这里我们再次提请读者注意, 通过变量代换计算极限, 相当于利用复合函数的连续性来计算极限.

以下利用已知极限来推导出一些新的常用的重要极限.

1. $\lim_{x\to 0}(1 + x)^{\frac{1}{x}} = \mathrm{e}$ 的推论

(1) 两边取对数, 得到我们在 (4.3.3) 式中得到的

$$
\lim _ {x \to 0} \frac {\ln (1 + x)}{x} = 1. \tag {5.2.3}
$$

(2) 在 (5.2.3) 式中用 $\mathrm{e}^{x} - 1$ 代替 $x$, 得到

$$
\lim _ {x \to 0} \frac {\mathrm{e} ^ {x} - 1}{x} = 1. \tag {5.2.4}
$$

(3) 对于任何 $\alpha \in \mathbb{R}$, 下式给出了 (4.3.4) 式的又一推导过程:

$$
\lim _ {x \to 0} \frac {(1 + x) ^ {\alpha} - 1}{x} = \lim _ {x \to 0} \frac {\mathrm{e} ^ {\alpha \ln (1 + x)} - 1}{\ln (1 + x)} \lim _ {x \to 0} \frac {\ln (1 + x)}{x} = \alpha . \tag {5.2.5}
$$

2. $\lim_{x\to 0}\frac{\sin{x}}{x} = 1$ 的推论

(1) 结合  $\cos x$  在 0 点处的连续性, 得到

$$
\lim _ {x \to 0} \frac {\tan x}{x} = 1. \tag {5.2.6}
$$

(2) 在  $\lim_{x\to0}\frac{\sin x}{x}=1$  中以  $\arcsin x$  代替 x 得到

$$
\lim _ {x \to 0} \frac {\arcsin x}{x} = 1. \tag {5.2.7}
$$

(3) 在 (5.2.6) 式中以 $\arctan x$ 代替 $x$ 得到

$$
\lim _ {x \to 0} \frac {\arctan x}{x} = 1. \tag {5.2.8}
$$

3. $\lim_{x\to +\infty}x^{\frac{1}{x}} = 1$ 的推论

(1) 两端取对数得到

$$
\lim _ {x \to + \infty} \frac {\ln x}{x} = 0. \tag {5.2.9}
$$

对于任何 $\alpha > 0$ ，在(5.2.9)式中以 $x^{\alpha}$ 代替 $x$ 得到

$$
\lim _ {x \to + \infty} \frac {\ln x}{x ^ {\alpha}} = 0. \tag {5.2.10}
$$

由 (5.2.10) 式又得到对任何 $\alpha \in \mathbb{R}$ 以及 $\beta > 0$, 有

$$
\lim _ {x \to + \infty} \frac {(\ln x) ^ {\alpha}}{x ^ {\beta}} = 0. \tag {5.2.11}
$$

(2) 在 (5.2.11) 式中用 $\frac{1}{x}$ 代替 $x$ 得到对任何 $\alpha \in \mathbb{R}$ 以及 $\beta > 0$, 有

$$
\lim _ {x \to 0 ^ {+}} x ^ {\beta} | \ln x | ^ {\alpha} = 0. \tag {5.2.12}
$$

(3) 对于 $\alpha \in \mathbb{R}$ 以及 $\beta > 0$, 在 (5.2.11) 式中以 $\mathrm{e}^x$ 代替 $x$ 得到

$$
\lim _ {x \to + \infty} \frac {x ^ {\alpha}}{\mathrm{e} ^ {\beta x}} = 0. \tag {5.2.13}
$$

## 4. $\mathrm{e}^{x}$ 的无穷级数表示

类似于 (3.3.8) 式, 可以得到 $\mathrm{e}^{x}$ 的级数表示. 利用 (5.2.3) 式可得

$$
\lim _ {n \to + \infty} \left(1 + \frac {x}{n}\right) ^ {n} = \lim _ {n \to + \infty} \mathrm{e} ^ {n \ln (1 + \frac {x}{n})} = \mathrm{e} ^ {x}. \tag {5.2.14}
$$

另一方面, 对任何 $n \geqslant 1$, 我们有

$$
\left(1 + \frac {x}{n}\right) ^ {n} = 1 + x + \frac {x ^ {2}}{2 !} \left(1 - \frac {1}{n}\right) + \dots + \frac {x ^ {n}}{n !} \prod_ {k = 1} ^ {n - 1} \left(1 - \frac {k}{n}\right). \tag {5.2.15}
$$

由单调收敛定理易得级数 $\sum_{n=0}^{\infty} \frac{|x|^n}{n!}$ 收敛. 而由 Cauchy 收敛准则得到 $\sum_{n=0}^{\infty} \frac{x^n}{n!}$ 也收敛. 于是, 固定 $m \geqslant 2$, 当 $n \geqslant m$ 时, 有

$$
\left| \left(1 + \frac {x}{n}\right) ^ {n} - \left(1 + x + \frac {x ^ {2}}{2 !} \left(1 - \frac {1}{n}\right) + \dots + \frac {x ^ {m}}{m !} \prod_ {k = 1} ^ {m - 1} \left(1 - \frac {k}{n}\right)\right) \right| \leqslant \sum_ {k = m + 1} ^ {\infty} \frac {| x | ^ {k}}{k !}. \tag {5.2.16}
$$

上式中令 $n\to +\infty$ 可得

$$
\left| \mathrm{e} ^ {x} - \sum_ {k = 0} ^ {m} \frac {x ^ {k}}{k !} \right| \leqslant \sum_ {k = m + 1} ^ {\infty} \frac {| x | ^ {k}}{k !}. \tag {5.2.17}
$$

再令 $m\to +\infty$ 即得

$$
\mathrm{e} ^ {x} = \sum_ {n = 0} ^ {\infty} \frac {x ^ {n}}{n !}, \quad \forall x \in \mathbb {R}. \tag {5.2.18}
$$

## 习题5.2

1. 求  $\lim_{n\to+\infty}\left(\frac{n!}{n^n}\right)^{\frac{1}{n}}$ .
2. 设 $a > 0, b > 0$, 求证: $\lim_{n \to +\infty} \left(\frac{\sqrt[n]{a} + \sqrt[n]{b}}{2}\right)^n = \sqrt{ab}$.

3. 计算  $\lim_{x\to0}\frac{e^{x}-1-x}{x^{2}}$ .
4. 计算  $\lim_{x\to0}\frac{\ln(1+x)-x}{x^{2}}$ .
5. 设 $\alpha \in \mathbb{R}$, 计算 $\lim_{x\to 0}\frac{(1 + x)^{\alpha} - 1 - \alpha x}{x^{2}}$.

## 5.3 连续函数的基本性质

这一节介绍连续函数的基本性质, 包括介值性、最值性以及一致连续性等.

## 5.3.1 介值定理

首先, 引入如下的介值定理, 它常用于证明代数方程解的存在性.

定理 5.3.1 设 f 在  $[a, b]$  上连续， $f(a) < \eta < f(b)$ ，则存在  $\xi \in (a, b)$  使得  $f(\xi) = \eta$ .

证明 记 $E := \{x \in [a, b] | f(x) \leqslant \eta\}$. 则 $a \in E$. 因此, $E$ 非空有界, 从而 $\xi := \sup E$ 存在且 $a \leqslant \xi \leqslant b$.

由上确界的定义, 无论 $\xi$ 是否属于 $E$, 都可以找到 $E$ 中点列 $\{x_{n}\}$ 使得 $\lim_{n\to +\infty}x_{n} = \xi$. 于是由 $f$ 的连续性, $f(\xi) = \lim_{n\to +\infty}f(x_n)\leqslant \eta$. 特别地, $\xi < b$.

于是, 对任何 $x \in (\xi, b]$, 有 $f(x) > \eta$. 从而又有 $f(\xi) = \lim_{x \to \xi^{+}} f(x) \geqslant \eta$.

总之, 得到  $f(\xi)=\eta$ .

一般地, 对于区间 $I$, 我们称函数 $f: I \to \mathbb{R}$ 具有介值性, 是指对任何 $a, b \in I, a < b$, $f$ 在 $[a, b]$ 上 (而不仅仅是在 $I$ 上) 可取到任何介于 $f(a)$ 与 $f(b)$ 之间的值. 这等价于对 $I$ 的任何子区间 $J$, 它的像 $f(J)$ 也是区间或单点集.

例 5.3.1 设  $P(x)=x^{5}+a_{4}x^{4}+a_{3}x^{3}+a_{2}x^{2}+a_{1}x+a_{0}$ ，其中  $a_{0}, a_{1}, \cdots, a_{4} \in R$ .
证明:P 有实零点.

证明 显然 $P$ 是 $\mathbb{R}$ 上的连续函数. 记 $M = \sum_{k=0}^{4} |a_k| + 1$. 则

$$
\begin{array}{l} P (M) \geqslant M ^ {5} - \sum_ {k = 0} ^ {4} | a _ {k} | M ^ {k} \geqslant M ^ {5} - M ^ {4} \sum_ {k = 0} ^ {4} | a _ {k} | > 0, \\ P (- M) \leqslant - M ^ {5} + \sum_ {k = 0} ^ {4} | a _ {k} | M ^ {k} \leqslant - M ^ {5} + M ^ {4} \sum_ {k = 0} ^ {4} | a _ {k} | <   0. \\ \end{array}
$$

由介值定理即得 P 有零点  $\xi \in (-M, M)$ .

例 5.3.2 证明:  $\cos x = x$  有实零点.

证明 记 $f(x) = \cos x - x$. 则 $f$ 是 $\mathbb{R}$ 上的连续函数. 我们有

$$
f (0) = 1 - 0 > 0, \quad f (1) = \cos 1 - 1 <   0.
$$

由介值定理即得 f 有零点  $\xi \in (0,1)$ .

## 5.3.2 最值性与有界性

如下最值定理表明有界闭区间上连续函数具有最值, 进而是有界的.

定理 5.3.2 设 f 是有界闭区间  $[a, b]$  上的连续函数. 则 f 在  $[a, b]$  上有最大最小值, 即有  $\xi, \eta \in [a, b]$  使得

$$
f (\xi) = \sup _ {x \in [ a, b ]} f (x), \quad f (\eta) = \inf _ {x \in [ a, b ]} f (x).
$$

进而 f 在  $[a, b]$  上有界.

证明 记 $M = \sup_{x\in [a,b]}f(x)$ (这里的 $M$ 有可能为 $+\infty$ ). 而接下来的讨论要证明 $M$ 是有限的、可达的.

由上确界的定义, 有 $[a, b]$ 中点列 $\{x_{n}\}$ 使得 $\lim_{n \to +\infty} f(x_{n}) = M$. 这样的点列 $\{x_{n}\}$ 称为 $f$ 在 $[a, b]$ 上的极大化序列. 由致密性定理, $\{x_{n}\}$ 有收敛子列. 不妨设 $\{x_{n}\}$ 本身收敛, 其极限为 $\xi$. 则 $\xi \in [a, b]$,

$$
f (\xi) = \lim _ {n \to + \infty} f (x _ {n}) = M.
$$

这表明 $M$ 为 $f$ 的最大值, $\xi$ 为最大值点①. 同理, $f$ 有最小值. 进而 $f$ 有界.

把最值定理与介值定理结合, 可见  $[a,b]$  上的连续函数 f 把  $[a,b]$  映成区间  $[m,M]$  或单点集  $\{M\}=\{m\}$ , 其中 M,m 为 f 在  $[a,b]$  上的最大值和最小值.

仿定理 5.3.2 的证明, 自然可得如下结论: 设 f 是区间 I 上的连续函数,  $E \subseteq I$  是有界闭集, 则  $f(E)$  是有界闭集.

## 5.3.3 一致连续性

首先, 我们引入如下概念.

定义5.3.1 设 $f$ 是区间 $I$ 上的函数. 若 $\lim_{r\to 0^{+}}\sup_{\substack{x,y\in I\\ |x - y|\leqslant r}}|f(x) - f(y)| = 0,$ 则称 $f$ 在$I$ 上一致连续.

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">① 称函数取得最大 (小) 值的点为其最大 (小) 值点.</span></small>

易见, $f$ 在 $I$ 上一致连续等价于: $\forall \varepsilon > 0$, 存在 $\delta > 0$, 使得对任何满足 $|x - y| < \delta$ 的 $x, y \in I$, 有 $|f(x) - f(y)| < \varepsilon$.

若对于 $r \geqslant 0$ ，令

$$
\omega (r) \equiv \omega (r; f) := \sup_ {\substack {x, y \in I \\ | x - y | \leqslant r}} | f (x) - f (y) |. \tag{5.3.1}
$$

则 $f$ 在 $I$ 上一致连续当且仅当 $\lim_{r\to 0^{+}}\omega (r) = \omega (0) = 0.$

当 $f$ 在 $I$ 上一致连续时, 我们称由 (5.3.1) 式定义的 $\omega$ 为 $f$ 在 $I$ 上的连续模.

若 $f$ 在区间 $I$ 上一致连续, 则其连续模 $\omega$ 是 $[0, +\infty)$ 上一个单调增加的连续函数, 满足 $\omega(0) = 0$ 以及

$$
\omega (r + s) \leqslant \omega (r) + \omega (s), \quad \forall r, s \geqslant 0.
$$

一般地, 我们把满足  $\omega(0^{+}) = \omega(0) = 0$  的单调增加函数  $\omega : [0, +\infty) \to [0, +\infty]$  称为一个连续模.

易见, 一致连续蕴涵连续, 而反之不然.

例 5.3.3 在  $(0,+\infty)$  上考虑函数  $f(x):=\frac{1}{x}$ . 则 f 在  $(0,+\infty)$  上连续. 但对于 r>0,

$$
\sup_{\substack{x,y > 0\\ |x - y|\leqslant r}}|f(x) - f(y)|\geqslant \sup_{0 <   x <   r}|f(2x) - f(x)| = \sup_{0 <   x <   r}\frac{1}{2x} = +\infty .
$$

因此, $f$ 在 $(0, +\infty)$ 上非一致连续.

一致连续性是有界闭集上连续函数的重要性质.

## 定理 5.3.3 有界闭区间上的连续函数必一致连续.

证明 我们用两种方法证明.

证法1 任取 $\varepsilon > 0$, 由 $f$ 的连续性, 对任何 $x \in [a, b]$ 有 $\delta_x > 0$ 使得当 $|y - x| < \delta_x$ 且 $y \in [a, b]$ 时, 有 $|f(y) - f(x)| < \varepsilon$.

显然， $[a,b]\subset\bigcup_{x\in[a,b]}\left(x-\frac{\delta_{x}}{2},x+\frac{\delta_{x}}{2}\right)$ . 由有限覆盖定理, 存在  $x_{1},x_{2},\cdots,x_{n}\in[a,b]$ 
使得  $[a,b]\subset\bigcup_{k=1}^{n}\left(x_{k}-\frac{\delta_{x_{k}}}{2},x_{k}+\frac{\delta_{x_{k}}}{2}\right)$ .

取 $\delta = \frac{1}{2}\min_{1\leqslant k\leqslant n}\delta_{x_k}$ .则 $\delta >0$ .对于满足 $|x - y| <   \delta$ 的 $x,y\in [a,b]$ ，首先有 $1\leqslant k\leqslant n$ 使得 $x\in \left(x_{k} - \frac{\delta_{x_{k}}}{2},x_{k} + \frac{\delta_{x_{k}}}{2}\right)$ .进而又有 $x,y\in \left(x_{k} - \delta_{x_{k}},x_{k} + \delta_{x_{k}}\right)$ .从而

$$
| f (x) - f (y) | \leqslant | f (x) - f (x _ {k}) | + | f (y) - f (x _ {k}) | <   2 \varepsilon .
$$

于是, 由定义得到 $f$ 在 $[a, b]$ 上一致连续.

证法 2 若结论不真, 则存在  $\varepsilon_{0} > 0$  使得 (注意下式左端单增)

$$
\sup_{\substack{x,y\in [a,b]\\ |x - y|\leqslant r}}|f(x) - f(y)| > \varepsilon_{0},\qquad \forall   r > 0.
$$

特别地, 对于任何 $n \geqslant 1$, 有 $x_{n}, y_{n} \in [a, b]$ 使得 $|x_{n} - y_{n}| \leqslant \frac{1}{n}$ 且 $|f(x_{n}) - f(y_{n})| > \varepsilon_{0}$.

由致密性定理, $\{x_{n}\}$ 有子列收敛. 不妨设 $\{x_{n}\}$ 本身收敛到 $\xi$. 则必有 $\xi \in [a, b]$. 进一步, $\{y_{n}\}$ 必也收敛到 $\xi$. 于是, 由 $f$ 在 $\xi$ 的连续性,

$$
\varepsilon_ {0} \leqslant \lim _ {n \to + \infty} | f (x _ {n}) - f (y _ {n}) | = | f (\xi) - f (\xi) | = 0.
$$

得到矛盾. 定理得证.

例5.3.4 设 $f$ 在 $[a, +\infty)$ 上连续，$\lim_{x \to +\infty} f(x) = A$。证明:$f$ 在 $[a, +\infty)$ 上一致连续。

证明 任取 X > a. 则对任意  $r \in (0,1)$ ,

$$
\sup_{\substack{x,y\geqslant a\\ |x - y| <   r}}|f(x) - f(y)|\leqslant \sup_{\substack{x,y\in [a,X + 1]\\ |x - y| <   r}}|f(x) - f(y)| + 2\sup_{x\geqslant X}|f(x) - A|.
$$

由定理 5.3.3,

$$
\varlimsup_ {r \to 0 ^ {+}} \sup_ {\substack {x, y \geqslant a \\ | x - y | <   r}} | f (x) - f (y) | \leqslant 2 \sup_ {x \geqslant X} | f (x) - A |, \quad \forall   X > a.
$$

由题设条件, 上式中令  $X \rightarrow +\infty$  即得

$$
\lim_{r\to 0^{+}}\sup_{\substack{x,y\geqslant a\\ |x - y| <   r}}|f(x) - f(y)| = 0.
$$

即 f 在  $[a, +\infty)$  上一致连续.

例5.3.5 设 $f$ 在 $[a, +\infty)$ 上一致连续， $\lim_{n\to +\infty}f(\sqrt{n}) = A.$ 证明: $\lim_{x\to +\infty}f(x) = A.$

证明 设 $\omega$ 为 $f$ 在 $[a, +\infty)$ 上的连续模. 对于 $x > |a| + 1$, 记 $n_x = [x^2]$. 则

$$
| x - \sqrt {n _ {x}} | \leqslant x - \sqrt {x ^ {2} - 1} = \frac {1}{x + \sqrt {x ^ {2} - 1}} <   \frac {1}{x}.
$$

从而

$$
\begin{array}{l} \left| f (x) - A \right| \leqslant \left| f (x) - f (\sqrt {n _ {x}}) \right| + \left| f (\sqrt {n _ {x}}) - A \right| \\ \leqslant \omega \big (\left| x - \sqrt {n _ {x}} \right| \big) + \left| f (\sqrt {n _ {x}}) - A \right| \\ \leqslant \omega \Big (\frac {1}{x} \Big) + \big | f (\sqrt {n _ {x}}) - A \big |. \\ \end{array}
$$

由题设条件和夹逼准则立即得到  $\lim_{x\to+\infty}f(x)=A.$

□

## 5.3.4 摄动法

利用函数的连续性, 可以把非退化、非奇异情形下的一些结果推广到退化或奇异情形. 典型的是线性代数问题中, 可利用摄动法简化一些退化矩阵或矩阵特征值有重根情形的问题的处理.

例5.3.6 设 A, B 均为 n 阶方阵, 且  $A + B$  非奇异, 证明:  $A(A + B)^{-1}B = B(A + B)^{-1}A$ .

证明 若 $A, B$ 可逆, 则

$$
A (A + B) ^ {- 1} B = \left(B ^ {- 1} (A + B) A ^ {- 1}\right) ^ {- 1} = \left(A ^ {- 1} + B ^ {- 1}\right) ^ {- 1} = B (A + B) ^ {- 1} A.
$$

一般地, 由于 $\pmb{A}, \pmb{B}, \pmb{A} + \pmb{B}$ 的特征值的个数有限, 因此有 $\delta > 0$ 使得当 $0 < s < \delta$ 时, $s$ 不是 $\pmb{A}, \pmb{B}$ 的特征值, $2s$ 不是 $\pmb{A} + \pmb{B}$ 的特征值. 从而 $\pmb{A}_s := \pmb{A} - s\pmb{I}, \pmb{B}_s := \pmb{B} - s\pmb{I}$ 和 $\pmb{A}_s + \pmb{B}_s$ 可逆. 此时,

$$
A _ {s} (A _ {s} + B _ {s}) ^ {- 1} B _ {s} = B _ {s} (A _ {s} + B _ {s}) ^ {- 1} A _ {s}.
$$

上式中令 $s\to 0^{+}$ 即得 $\pmb {A}(\pmb {A} + \pmb {B})^{-1}\pmb {B} = \pmb {B}(\pmb {A} + \pmb {B})^{-1}\pmb{A}$

□

## 习题5.3

1. 设 $f$ 为有界区间 $(a, b)$ 内的连续函数, $f(a^{+}), f(b^{-})$ 都存在且 $f(a^{+}) < 0, f(b^{-}) > 0$. 证明: 存在 $\xi \in (a, b)$ 使得 $f(\xi) = 0$.

2. 设 $f$ 在 $(0, +\infty)$ 内连续, 且满足 $f(x^{2}) = f(x) (\forall x > 0)$. 证明: $f$ 在 $(0, +\infty)$ 内为常数.

3. 设 $f$ 为区间 $(a, +\infty)$ 上的连续函数, $f(a^{+})$ 存在且为负数, $f(+\infty) = +\infty$. 证明: 存在 $\xi \in (a, +\infty)$ 使得 $f(\xi) = 0$.

4. 设 $f$ 是 $\mathbb{R}$ 上的连续周期函数. 若 $f$ 不为常数, 证明它一定有最小正周期.

5. 试用闭区间套定理证明介值定理.

6. 设 $f$ 在有界区间 $(a, b)$ 内连续. 证明: $f$ 在 $(a, b)$ 内一致连续当且仅当 $f(a^{+})$ 和 $f(b^{-})$ 都存在.

7. 设 $f$ 在 $[0, +\infty)$ 上连续，$\lim_{n \to +\infty} f(\sqrt{n} \ln n) = 0$。证明:$\lim_{x \to +\infty} f(x)$ 存在的充要条件是 $f$ 在 $[0, +\infty)$ 上一致连续。

8. 证明: $f(x) = \sin^2 x + \sin x^2$ 不是周期函数.

9. 设 $f$ 在 $\mathbb{R}$ 上一致连续. 证明: 存在常数 $a, b$ 使得对任何 $x \in \mathbb{R}$, 有 $|f(x)| \leqslant a + b|x|$.

10. 设 $a > 0, a^2 + 4b < 0$. 求证: 不存在 $\mathbb{R}$ 上具有介值性的函数 $f$ 满足 $f(f(x)) = af(x) + bx$.

11. 设 $\mathbb{R}$ 上连续函数列 $\{f_n\}$ 对于每一个 $x \in \mathbb{R}$ 都是有界的 (称为“逐点有界”). 证明: 存在区间 $(a, b)$ 使得 $\{f_n\}$ 在 $(a, b)$ 内一致有界. 即存在与 $n$ 无关的常数 $M > 0$ 使得

$$
| f _ {n} (x) | \leqslant M, \quad \forall n \geqslant 1, x \in (a, b).
$$

12. 设函数 $f$ 在区间 $\left( {{x}_{0}, + \infty }\right)$ 上连续并有界. 证明: 对任何实数 $T$ ,存在趋于 $+ \infty$ 的序列 $\left\{  {x}_{n}\right\}$ 使得

$$
\lim _ {n \to + \infty} (f (x _ {n} + T) - f (x _ {n})) = 0.
$$

13. 设 $f$ 是区间 $(a, b)$ 内的函数, 若 $\forall n \in \mathbb{N}_{+}$, $\frac{|f + n| - |f - n|}{2}$ 连续, 证明 $f$ 连续.

14. 设 $f$ 在 $\mathbb{R}$ 上连续, 且对任何 $x, y \in \mathbb{R}$ 均有 $f(x + y) = f(x) + f(y)$. 证明: $f$ 必为齐次线性函数.

15. 在习题 14 中, $f$ 的连续性可以用 $f$ 在 0 点的连续性来代替. 进一步证明: $f$ 的连续性用局部有界性代替时, 结论仍然成立.

16. $\mathbb{R}$ 上的函数 $f$ 满足 $f(x + y) = f(x)f(y)$, 设 $f$ 局部有界.

(1) 证明: 存在常数 $A$, 使得

$$
f (x) = A ^ {x}, \quad \forall x \in \mathbb {R};
$$

(2) 若 $f$ 是复值函数, 情况又如何?

17. 设 $f, g$ 在闭区间 $[a, b]$ 上连续, 且存在 $x_{n} \in [a, b]$, 使得

$$
f (x _ {n}) = g (x _ {n + 1}), \quad \forall n = 1, 2, \dots .
$$

证明:存在 $\xi \in [a,b]$ 使得， $f(\xi) = g(\xi)$

18. 证明不存在 $\mathbb{R}$ 上的连续函数 $f$ 使得对任何 $\alpha \in \mathbb{R}$, 方程 $f(x) = \alpha$ 恰好有两个根.
19. 设 $n$ 为正整数, $f$ 在 $[0, n]$ 上连续, 且 $f(0) = f(n)$. 证明存在 $n$ 组不同的 $\{x, y\}$ 使得 $f(x) = f(y)$ 且 $x - y$ 为非零整数.
20. 设定义在区间 $[a, b]$ 内的函数 $f$ 具有介值性. 证明 $f$ 在 $[a, b]$ 上连续当且仅当对任何有理数 $q$, $\{x \in [a, b] | f(x) = q\}$ 是闭集.
21. 设 $f(x), g(x)$ 和 $xf(x)$ 均在 $\mathbb{R}$ 上一致连续. 证明 $f(x)g(x)$ 在 $\mathbb{R}$ 上一致连续.
22. 设 $f$ 在 $[a, b]$ 上连续, 但不为常数. 求证: $\exists \xi \in (a, b)$ 使 $f$ 在点 $\xi$ 不取极值. 即对任何 $\delta > 0$, 都有 $x \in (\xi - \delta, \xi)$ 以及 $y \in (\xi, \xi + \delta)$ 使得 $\left(f(x) - f(\xi)\right)(f(y) - f(\xi)) < 0$.
23. 设 A, B 均为 n 阶方阵, 证明  $\det\begin{pmatrix}A & B \\ B & A\end{pmatrix} = \det(A + B) \det(A - B).$

## 5.4 Lipschitz 连续、Hölder 连续和单调函数

在今后的研究中有几类连续函数将受到特别的关注. 首先, 我们引入如下概念.

定义 5.4.1 设 f 是区间 I 上的函数, 若存在常数 M 使得

$$
\(| f (x) - f (y) | \leqslant M | x - y |, \quad \forall x, y \in I, \tag {5.4.1}
$$

则称 $f$ 在 $I$ 上满足Lipschitz条件，或称 $f$ 在 $I$ 上Lipschitz连续.(5.4.1)式中的常数 $M$ 称为Lipschitz常数.

若存在 $\alpha \in (0,1)$ 以及常数 $M$ 使得

$$
\(| f (x) - f (y) | \leqslant M | x - y | ^ {\alpha}, \quad \forall x, y \in I, \tag {5.4.2}
$$

则称 $f$ 在 $I$ 上满足 $\mathbf{Hölder}^{\text{①}}$ 条件, 或称 $f$ 在 $I$ 上 $\mathbf{Hölder}$ 连续, (5.4.2) 式也常称为 $\mathrm{Lip - }\alpha$ 条件.

易见 Lipschitz 连续或 Hölder 连续蕴涵一致连续. 在有界区间 Lipschitz 连续蕴涵 Hölder 连续.

例 5.4.1 设 f 为区间  $(a, b)$  内的函数, 且有  $\alpha > 1$  以及常数 M > 0 使得

$$
| f (x) - f (y) | \leqslant M | x - y | ^ {\alpha}, \quad \forall   x, y \in (a, b).
$$

证明: $f$ 在 $(a, b)$ 内恒为常数.

证明 任取 $x, y \in (a, b)$. 由题设条件, 对于 $n \geqslant 2$, 有

$$
\begin{array}{l} \left| f (y) - f (x) \right| \leqslant \sum_ {k = 1} ^ {n} \left| f \left(x + \frac {k (y - x)}{n}\right) - f \left(x + \frac {(k - 1) (y - x)}{n}\right) \right| \\ \leqslant M \sum_ {k = 1} ^ {n} \frac {| y - x | ^ {\alpha}}{n ^ {\alpha}} = \frac {M | y - x | ^ {\alpha}}{n ^ {\alpha - 1}}. \\ \end{array}
$$

令  $n \rightarrow +\infty$  即得  $f(y) = f(x)$ ，即 f 在  $(a, b)$  内恒为常数.

当 Lipschitz 常数小于 1 时, 我们有如下的结果.

例5.4.2 设 $f:\mathbb{R}\to \mathbb{R}$ 满足

$$
\left| f (x) - f (y) \right| \leqslant k | x - y |, \quad \forall x, y \in \mathbb {R}, \tag {5.4.3}
$$

其中常数 0 < k < 1. 证明: f 有唯一的不动点, 即方程  $f(x) = x$  有唯一解.

进一步，设  $\xi$  为该不动点，则对任何  $x_{0} \in R, \{f_{n}(x_{0})\}$  收敛到  $\xi$ ，其中  $f_{n} = \overbrace{f \circ f \circ \cdots \circ f}^{n个}$ .

证明 由题设条件, $f$ 连续. 进一步, 有

$$
\begin{array}{l} \left| f _ {2} \left(x _ {0}\right) - f _ {1} \left(x _ {0}\right) \right| = \left| f \left(f \left(x _ {0}\right)\right) - f \left(x _ {0}\right) \right| \leqslant k \left| f \left(x _ {0}\right) - x _ {0} \right|, \\ \left| f _ {3} \left(x _ {0}\right) - f _ {2} \left(x _ {0}\right) \right| = \left| f \left(f _ {2} \left(x _ {0}\right)\right) - f \left(f _ {1} \left(x _ {0}\right)\right) \right| \leqslant k \left| f _ {2} \left(x _ {0}\right) - f _ {1} \left(x _ {0}\right) \right| \leqslant k ^ {2} \left| f \left(x _ {0}\right) - x _ {0} \right|, \\ \end{array}
$$

...，

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">① Hölder, Otto Ludwig, 1859 年 12 月 22 日—1937 年 8 月 29 日, 德国数学家.</span></small>

$$
| f _ {n + 1} (x _ {0}) - f _ {n} (x _ {0}) | \leqslant k ^ {n} | f (x _ {0}) - x _ {0} |,
$$

...

从而, 对于任何 $m > n \geqslant 1$, 有

$$
| f _ {m} (x _ {0}) - f _ {n} (x _ {0}) | \leqslant \sum_ {j = n} ^ {m - 1} k ^ {j} | f (x _ {0}) - x _ {0} | \leqslant \frac {k ^ {n}}{1 - k} | f (x _ {0}) - x _ {0} |.
$$

因此， $\{f_{n}(x_{0})\}$ 是 Cauchy 列，从而有极限，设其极限为 $\xi$。则对 $f_{n+1}(x_{0}) = f(f_{n}(x_{0}))$ 取极限得到 $f(\xi) = \xi$。这样就证明了 $\{f_{n}(x_{0})\}$ 收敛到 $f$ 的不动点。

另一方面, 若 $\eta$ 也是 $f$ 的不动点, 则

$$
| \eta - \xi | = | f (\eta) - f (\xi) | \leqslant k | \eta - \xi |.
$$

于是由 $0 < k < 1$ 得到 $\eta = \xi$, 即 $f$ 的不动点唯一.

上例是压缩映射原理的特例. 压缩映射原理在一般的完备度量空间中成立, 其证明与例题中的证明大同小异. 易见, 在例 5.4.2 中把 $f: \mathbb{R} \to \mathbb{R}$ 改成 $f: I \to I$, 其中 $I$ 为 (有界或无界的) 闭区间, 而其他条件不变, 则结论依然成立.

若  $f:[a,b]\rightarrow[a,b]$  是连续函数, 则由介值定理可得 f 有不动点.

在今后的讨论中, 单调函数经常起着重要的作用. 以下是单调函数一个有趣的性质.

定理 5.4.1 设 f 是  $(a, b)$  内的单调函数. 则 f 的不连续点至多可列.

证明 不妨设 $f$ 单增. 由单调收敛定理, 对任何 $x \in (a, b)$, $f(x^{+})$ 与 $f(x^{-})$ 都存在, 且 $f(x^{-}) \leqslant f(x^{+})$. 考虑集合 $E := \{x \in (a, b) | f(x^{-}) < f(x^{+})\}$. 则 $E$ 为 $f$ 的不连续点全体. 而对于 $x \in E$ 均可以取到有理数 $q_{x} \in (f(x^{-}), f(x^{+}))$. 注意到对于不同的 $x, y \in E$, $y > x$, 有 $q_{y} > f(y^{-}) \geqslant f(x^{+}) > q_{x}$, 因此 $x \mapsto q_{x}$ 是 $E$ 到有理数集的一个单射. 这表明 $E$ 至多可列, 即 $f$ 的不连续点全体至多可列. □

下例表明单调函数的不连续点可以是任意可列集.

例 5.4.3 设有点列  $\{x_{n}\}_{n=1}^{\infty}$ . 证明: 存在 R 的单增函数 f, 其不连续点全体恰好为  $\{x_{n}|n\geqslant1\}$ .

证明 不妨设 $x_{n}$ 两两不同. 记

$$
h (\cdot) = \chi_ {(0, + \infty)} (\cdot), \qquad i (\cdot) = \chi_ {\{0 \}} (\cdot).
$$

定义

$$
f (x) = \sum_ {x _ {n} <   x} \frac {1}{2 ^ {n}} = \sum_ {n = 1} ^ {\infty} \frac {1}{2 ^ {n}} h (x - x _ {n}), \qquad x \in \mathbb {R}.
$$

则对任何 $x \in \mathbb{R}$, 级数 $\sum_{n=1}^{\infty} \frac{1}{2^n} h(x - x_n)$ 的部分和单调有界, 从而级数收敛. 即 $f(x)$ 是合理定义的.

易见 f 是单调增加的函数.

另一方面, 固定 $x_0 \in \mathbb{R}$, 对任何 $m \geqslant 2$, 取 $\delta = \min \left\{|x_n - x_0||1 \leqslant n \leqslant m, x_n \neq x_0\right\}$. 则 $\delta > 0$, 且当 $x_0 < x < x_0 + \delta$ 时,

$$
\sum_ {n = 1} ^ {m} \frac {1}{2 ^ {n}} h (x - x _ {n}) = \sum_ {n = 1} ^ {m} \frac {1}{2 ^ {n}} \big (h (x _ {0} - x _ {n}) + i (x _ {0} - x _ {n}) \big).
$$

因此，

$$
0 \leqslant f (x) - \sum_ {n = 1} ^ {\infty} \frac {1}{2 ^ {n}} \big (h (x _ {0} - x _ {n}) + i (x _ {0} - x _ {n}) \big) \leqslant \sum_ {n = m + 1} ^ {\infty} \frac {1}{2 ^ {n}}.
$$

由此即得

$$
\lim _ {x \to x _ {0} ^ {+}} f (x) = \sum_ {n = 1} ^ {\infty} \frac {1}{2 ^ {n}} \big (h (x _ {0} - x _ {n}) + i (x _ {0} - x _ {n}) \big).
$$

即 $f$ 在点 $x_0$ 处右连续当且仅当 $x_0 \notin \{x_n | n \geqslant 1\}$.

同理可证

$$
\lim _ {x \to x _ {0} ^ {-}} f (x) = \sum_ {n = 1} ^ {\infty} \frac {1}{2 ^ {n}} h (x _ {0} - x _ {n}) = f (x _ {0}).
$$

即 f 在点  $x_{0}$  处左连续.

总之，f 的不连续点全体是集合  $\{x_{n}|n\geqslant1\}$ .

在上例中, $f$ 是左连续的. 如果取 $\{x_{n}\}$ 为 $\mathbb{R}$ 的稠密子列, 比如所有有理数的一个排列, 则 $f$ 的不连续点全体是 $\mathbb{R}$ 的稠密子集. 而且此时 $f$ 是严格单增的.

例 5.4.4 设区间 I 上函数 f 具有介值性, 且是两个单调函数之和. 证明: f 在 I 上连续.

证明 只要证明对任何有界闭区间 $[a, b] \subseteq I$, $f$ 在 $[a, b]$ 上连续. 由于 $f$ 为两个单调函数之和, 因此对任何 $x_0 \in [a, b)$, $f$ 在点 $x_0$ 处的右极限 $f(x_0^+)$ 存在.

若 $\varepsilon_0 = |f(x_0^+) - f(x_0)| > 0$，则不妨设 $\varepsilon_0 = f(x_0^+) - f(x_0) > 0$。此时，存在 $\delta \in (0, b - x_0)$ 使得当 $0 < x - x_0 < \delta$ 时有 $f(x) > f(x_0^+) - \frac{\varepsilon_0}{2} > f(x_0) + \frac{\varepsilon_0}{2}$。从而 $f$ 在 $[x_0, x_0 + \delta)$ 上取到 $f(x_0)$ 以及大于 $f(x_0) + \frac{\varepsilon_0}{2}$ 的某个值，但取不到介于这两者之间的值 $f(x_0) + \frac{\varepsilon_0}{2}$。与题设的介值性矛盾。因此 $\varepsilon_0 = 0$。即 $f$ 在点 $x_0$ 处右连续。

由  $x_{0} \in [a, b)$  的任意性, f 在  $[a, b)$  上右连续. 同理, f 在  $(a, b]$  上左连续.

总之, $f$ 在 $I$ 上连续.