解 注意到

$$
x ^ {n} - 1 = (x - x _ {1}) (x - x _ {2}) \dots (x - x _ {n}), \tag {6.3.4}
$$

故有

$$
x _ {1} x _ {2} \dots x _ {n} = (- 1) ^ {n - 1}.
$$

在关系式 (6.3.4) 两端关于 $x$ 求导, 利用求导的四则运算法则, 可得

$$
n x ^ {n - 1} = \sum_ {i} (x - x _ {1}) \dots (x - x _ {i - 1}) (x - x _ {i + 1}) \dots (x - x _ {n}).
$$

在此等式中, 分别取  $x = x_{1}, x_{2}, \cdots, x_{n}$ , 然后将所得到的 n 个关系式相乘, 可得

$$
n ^ {n} (x _ {1} x _ {2} \dots x _ {n}) ^ {n - 1} = (- 1) ^ {n (n - 1) / 2} \prod_ {i <   j} (x _ {i} - x _ {j}) ^ {2}.
$$

结合等式 $x_{1}x_{2}\dots x_{n} = (-1)^{n - 1}$ ，从而有

$$
\prod_ {i <   j} (x _ {i} - x _ {j}) ^ {2} = (- 1) ^ {(n - 1) (n - 2) / 2} n ^ {n}.
$$

## 2. 复合函数求导的“链式法则”

对于复合函数求导, 成立下面所谓的链式法则:

定理 6.3.3 设函数  $\varphi(t)$  在  $t = t_{0}$  处可导, 函数  $f(x)$  在  $x_{0} = \varphi(t_{0})$  处可导, 则复合函数  $f \circ \varphi$  在  $t_{0}$  处可导, 且成立关系式

$$
(f \circ \varphi) ^ {\prime} (t _ {0}) = f ^ {\prime} (x _ {0}) \varphi^ {\prime} (t _ {0}). \tag {6.3.5}
$$

证明 我们先来分析一下复合函数 $f \circ \varphi$ 的差商

$$
\frac {f \circ \varphi (t _ {0} + \Delta t) - f \circ \varphi (t _ {0})}{\Delta t}.
$$

如果 $\varphi (t_0 + \Delta t) - \varphi (t_0)\neq 0$ ，则可将上式改写为

$$
\frac {f \circ \varphi (t _ {0} + \Delta t) - f \circ \varphi (t _ {0})}{\Delta t} = \frac {f \circ \varphi (t _ {0} + \Delta t) - f \circ \varphi (t _ {0})}{\varphi (t _ {0} + \Delta t) - \varphi (t _ {0})} \cdot \frac {\varphi (t _ {0} + \Delta t) - \varphi (t _ {0})}{\Delta t}. \tag {6.3.6}
$$

等式两边取 $\Delta t\to 0$ 的极限，即完成了定理的证明.事实上，这是因为左边的极限就是$(f\circ \varphi)^{\prime}(t_{0})$ 的定义，而右边的两个因子，其极限刚好分别为 $f^{\prime}(x_0)$ 和 $\varphi '(t_0)$

因此剩下的问题则是考虑 $\varphi(t_0 + \Delta t) - \varphi(t_0) = 0$ 的情况, 而这的确可以发生, 即使在 $t_0$ 的任意小邻域内也难以避免. 比如取 $\varphi$ 为例6.1.8中的函数. 则在0点的任意小邻域内, 只要 $n$ 足够大, 都有形如 $\frac{1}{n\pi}$ 的点, 使得 $\varphi\left(\frac{1}{n\pi}\right) - \varphi(0) = 0$.

为了克服这个问题, 注意到当 $\varphi(t_0 + \Delta t) - \varphi(t_0) = 0$ 时, (6.3.6) 式的左边显然也为 0 , 再看其右边, 第二个因子由于分子为 0 故整个因子也为 0 , 所以右边的问题出在第一个因子的分母上. 鉴于此, 我们对右边第一个因子处理如下:

引入函数

$$
\psi (x) = \left\{ \begin{array}{l l} \frac {f (x) - f (\varphi (t _ {0}))}{x - \varphi (t _ {0})}, & x \neq \varphi (t _ {0}), \\ f ^ {\prime} (\varphi (t _ {0})), & x = \varphi (t _ {0}). \end{array} \right. \tag {6.3.7}
$$

根据 $\psi (x)$ 的定义，注意到 $x_0 = \varphi (t_0)$，显然该函数在点 $x_0$ 处连续，即

$$
\lim _ {x \to x _ {0}} \psi (x) = f ^ {\prime} (x _ {0}) = \psi (x _ {0}).
$$

通过引入上述函数 $\psi (x)$ ，无论 $\varphi (t_0 + \Delta t) - \varphi (t_0)$ 是否为0,(6.3.6)式总可以写为

$$
\frac {f \circ \varphi (t _ {0} + \Delta t) - f \circ \varphi (t _ {0})}{\Delta t} = \psi (\varphi (t)) \cdot \frac {\varphi (t _ {0} + \Delta t) - \varphi (t _ {0})}{\Delta t}.
$$

上式两边令 $t \to t_0$，即得等式 (6.3.5).

复合函数的求导法则常常被称为“链式法则”，但从表达式(6.3.5)中也许并没有体会到它的形象之处。事实上，当我们求任意有限多个函数的复合时，下面推论给出的求导公式就像链条似的，一环套一环，非常形象。另外，在多元函数求导运算时，我们也有相应的链式法则，那里我们越发能体会到这一称呼的直观性。

作为练习, 读者可以证明下面的结论:

推论 6.3.4 设有 n 个函数  $\varphi_{k}(t_{k})\ (k=1,2,\cdots,n)$  满足: $\varphi_{1}(t_{1})$  在  $t_{1}=t_{1,0}$  处可导， $\varphi_{k}(t_{k})$  在  $t_{k,0}=\varphi_{k-1}(t_{k-1,0})\ (k=2,3,\cdots,n)$  处可导。则复合函数  $f=\varphi_{n}\circ\varphi_{n-1}\circ\cdots\circ\varphi_{1}$  在  $t_{1,0}$  处可导，且

$$
f ^ {\prime} (t _ {1, 0}) = (\varphi_ {n} \circ \varphi_ {n - 1} \circ \dots \circ \varphi_ {1}) ^ {\prime} | _ {t _ {1, 0}} = \varphi_ {n} ^ {\prime} (t _ {n, 0}) \varphi_ {n - 1} ^ {\prime} (t _ {n - 1, 0}) \dots \varphi_ {1} ^ {\prime} (t _ {1, 0}).
$$

如果采用 Leibniz 引入的导数符号的话, 上述求导法则可以更形象地写成

$$
\left. \frac {\mathrm{d} f}{\mathrm{d} t _ {1}} \right| _ {t _ {1} = t _ {1, 0}} = \frac {\mathrm{d} \varphi_ {n}}{\mathrm{d} \varphi_ {n - 1}} \cdot \frac {\mathrm{d} \varphi_ {n - 1}}{\mathrm{d} \varphi_ {n - 2}} \dots \frac {\mathrm{d} \varphi_ {2}}{\mathrm{d} \varphi_ {1}} \cdot \left. \frac {\mathrm{d} \varphi_ {1}}{\mathrm{d} t _ {1}} \right| _ {t _ {1} = t _ {1, 0}}
$$

对于等式右边的表达式, 也许对分子分母产生跃跃欲试 “约分” 的想法了. 这的确是 Leibniz 符号的好处之一, 我们在后面讨论函数微分时还将返回这个话题, 并且把这种想法合理化、严谨化.

在实际情况中, 复合函数链式法则可能是所有求导问题中应用频率最高的法则之一. 利用这个法则, 可以极大简便复杂函数的求导. 在具体计算时, 只要分清把哪些变量打包成中间变量, 则不必每次都引入新的中间变量符号了. 在情况复杂时, 可能要层层打包, 操作时把这些包像剥洋葱似的层层解开. 熟练掌握这一方法可以极大缩短计算过程提高求导速度.

例 6.3.5 求下列函数的导数:

$$
a ^ {x} (a > 0), \quad \sin^ {2} x, \quad \tan (2 x + 1), \quad \mathrm{e} ^ {- x ^ {2}}, \quad \ln (x + \sqrt {1 + x ^ {2}}).
$$

解 直接应用复合函数求导的链式法则, 可得

$$
(a ^ {x}) ^ {\prime} = (\mathrm{e} ^ {x \ln a}) ^ {\prime} = (\mathrm{e} ^ {x \ln a}) \cdot (x \ln a) ^ {\prime} = a ^ {x} \ln a.
$$

$$
(\sin^ {2} x) ^ {\prime} = 2 \sin x \cdot (\sin x) ^ {\prime} = \sin 2 x.
$$

$$
(\tan (2 x + 1)) ^ {\prime} = \frac {1}{\cos^ {2} (2 x + 1)} \cdot (2 x + 1) ^ {\prime} = \frac {2}{\cos^ {2} (2 x + 1)}.
$$

$$
(\mathrm{e} ^ {- x ^ {2}}) ^ {\prime} = \mathrm{e} ^ {- x ^ {2}} \cdot (- x ^ {2}) ^ {\prime} = - 2 x \mathrm{e} ^ {- x ^ {2}}.
$$

$$
\begin{array}{l} \left(\ln (x + \sqrt {1 + x ^ {2}})\right) ^ {\prime} = \frac {1}{x + \sqrt {1 + x ^ {2}}} \cdot (x + \sqrt {1 + x ^ {2}}) ^ {\prime} \\ = \frac {1}{x + \sqrt {1 + x ^ {2}}} \cdot \left(1 + \frac {x}{\sqrt {1 + x ^ {2}}}\right) \\ = \frac {1}{\sqrt {1 + x ^ {2}}}. \\ \end{array}
$$

## 3. 反函数的求导法则

定理 6.3.5 设函数  $y = f(x)$  在包含点  $x_{0}$  的开区间 I 上严格单调并且连续. 如果  $f(x)$  在点  $x_{0}$  处可导, 且导数  $f'(x_{0}) \neq 0$ , 那么它的反函数  $x = f^{-1}(y)$  在点  $y_{0} = f(x_{0})$  处可导, 并且有

$$
(f ^ {- 1}) ^ {\prime} (y _ {0}) = \frac {1}{f ^ {\prime} (x _ {0})}.
$$

证明 由条件假设知函数 $x = f^{-1}(y)$ 也严格单调并且连续. 于是, 条件“$y \neq y_0$ 且 $y \to y_0$”等价于条件“$x \neq x_0$ 且 $x \to x_0$”, 因此下式成立:

$$
\lim _ {y \to y _ {0}} \frac {f ^ {- 1} (y) - f ^ {- 1} (y _ {0})}{y - y _ {0}} = \lim _ {x \to x _ {0}} \frac {x - x _ {0}}{f (x) - f (x _ {0})} = \lim _ {x \to x _ {0}} \frac {1}{\frac {f (x) - f (x _ {0})}{x - x _ {0}}} = \frac {1}{f ^ {\prime} (x _ {0})}. \quad \square
$$

注 6.3.1 对比一下连续函数章节的内容, 由定理 5.2.4 我们知道: 严格单调的连续函数存在反函数, 且反函数也连续. 现在定理 6.3.5 告诉我们, 一个严格单调的连续函数, 如果它可导, 并且如果它的导数非零, 那么其反函数存在、连续, 并且也可导. 进一步不难证明, 如果原来的函数导函数连续, 那么其反函数的导函数也连续.

我们特意指出这两种情况 (可以形象地描述为一种是  $C^{0}$  情况, 一种是  $C^{1}$  情况), 目的是提醒读者关注以下几点: 一是对高阶导数存在时的相应结论的成立性; 一是在后面多元函数章节, 一些结构上非常相似的结论的成立性.

需要注意的是, 定理中的条件 $f'(x_0) \neq 0$ 不可缺少, 即使 $y = f(x)$ 在包含点 $x_0$ 的开区间 $I$ 上严格单调、连续、可导也不够. 函数 $y = x^3$ 在 0 点就是一个反例: 其反函数在 0 点附近存在、连续, 但反函数在此点不可导.

显然, 如果上面的条件不但在点 $x_0$ 成立, 而且在区间 $(a, b)$ 内都成立的话, 结论自然对整个区间上的每一个点都成立. 即

推论 6.3.6 如果函数  $y = f(x)$  在区间  $(a, b)$  内严格单调、可导且有非零的导数, 那么它的反函数  $x = f^{-1}(y)$  将在区间  $(\alpha, \beta)$  内可导, 其中

$$
\alpha = \min \left\{x (a ^ {+}), x (b ^ {-}) \right\}, \qquad \beta = \max \left\{x (a ^ {+}), x (b ^ {-}) \right\}.
$$

且有

$$
\frac {\mathrm{d} f ^ {- 1} (y)}{\mathrm{d} y} = \frac {1}{f ^ {\prime} (x)}.
$$

反函数的导数有明确的几何意义. 由于在同一个坐标系里 $y = f(x)$ 和 $x = f^{-1}(y)$ 对应同一条曲线 $C$, 因此在给定点其切线对应同一条直线 $\ell$, 而导数描述的是切线的斜率, 后者是因变量与自变量的比值. 因此当考虑反函数的导数时, 无非就是在计算斜率时把自变量和因变量的角色交换了一下, 而这刚好产生倒数关系. 换句话说, 假设曲线 $C$ 在点 $(x_0, y_0)$ 处的切线 $\ell$ 与 $x$ 轴正向和 $y$ 轴正向的夹角分别为 $\alpha$ 和 $\beta$ 的话, 显然有 $\alpha + \beta = \frac{\pi}{2}$ (见图6.4). 因此有

$$
\tan \alpha = {\frac {1}{\tan \beta}}, \qquad {\text {即}} \quad f ^ {\prime} (x _ {0}) = {\frac {1}{(f ^ {- 1}) ^ {\prime} (y _ {0})}}.
$$

![](images/page_163_image_10.jpg)

<details>
<summary>text_image</summary>

y
x=f⁻¹(y)
y=f(x)
l
O
α
(x₀, y₀)
β
x
</details>

图6.4 反函数的导数

例 6.3.6 计算下列函数的导数:

$$
\ln x, \quad \arcsin x, \quad \arccos x, \quad \arctan x, \quad \operatorname{arccot} x.
$$

解 我们知道 $f(x) = \mathrm{e}^x$ 与 $g(y) = \ln y$ 互为反函数, 因此从 $f'(x) = \mathrm{e}^x$, 由反函数求导法则, 可得

$$
g ^ {\prime} (y) = \frac {1}{f ^ {\prime} (g (y))} = \frac {1}{\mathrm{e} ^ {\ln y}} = \frac {1}{y}.
$$

把 $x, y$ 的符号对换一下, 写成更熟悉的表述, 即得

$$
(\ln x) ^ {\prime} = \frac {1}{x}.
$$

道理同上, 注意到 $f(x) = \arcsin x$ 和 $g(y) = \sin y$ 互为反函数, 因此有

$$
f ^ {\prime} (x) = \frac {1}{g ^ {\prime} (f (x))} = \frac {1}{\cos (\arcsin x)} = \frac {1}{\sqrt {1 - x ^ {2}}}.
$$

即

$$
(\arcsin x) ^ {\prime} = \frac {1}{\sqrt {1 - x ^ {2}}}
$$

同理有如下结论:

$$
(\arccos x) ^ {\prime} = - \frac {1}{\sqrt {1 - x ^ {2}}}.
$$

$$
(\arctan x) ^ {\prime} = \frac {1}{1 + x ^ {2}}.
$$

$$
(\operatorname{arccot} x) ^ {\prime} = - \frac {1}{1 + x ^ {2}}.
$$

行文至此, 我们觉得很有必要把前面讨论过的基本初等函数导数给出个列表. 这些函数的导数在数学各个分支中高频出现, 其地位和作用类似于小学里的九九乘法表, 因此有必要熟练记住它们, 这是数学分析课程中为数不多的既要理解、又要熟记的内容.

初等函数导数表

| f | $f'$ | f | $f'$ | f | $f'$ |
| --- | --- | --- | --- | --- | --- |
| c | 0 | $x^{\mu}$ | $\mu x^{\mu-1}$ | $e^{x}$ | $e^{x}$ |
| $a^{x}$ | $a^{x} \ln a$ | $\ln x$ | $\frac{1}{x}$ | $\log_{a} x$ | $\frac{1}{x \ln a}$ |
| $\sin x$ | $\cos x$ | $\cos x$ | $-\sin x$ | $\tan x$ | $\frac{1}{\cos^{2} x}$ |
| $\cot x$ | $-\frac{1}{\sin^{2} x}$ | $\arcsin x$ | $\frac{1}{\sqrt{1-x^{2}}}$ | $\arccos x$ | $-\frac{1}{\sqrt{1-x^{2}}}$ |
| $\arctan x$ | $\frac{1}{1+x^{2}}$ | $\operatorname{arccot} x$ | $-\frac{1}{1+x^{2}}$ |  |  |

## 4. 隐函数的求导

隐函数这个概念是相对显函数而言的. 所谓的显函数, 通常是指因变量 $y$ 可以用自变量 $x$ 的形如 $y = f(x)$ 的表达式给出, 其中 $f$ 是 $x, y$ 间的对应关系. 因此, 顾名思义, 隐函数就是指变量 $x, y$ 之间虽然也存在某种函数关系, 但这个对应关系只能通过形如 $F(x, y) = 0$ 的方程给出, 而不能或不便用显式表出. 比如平面上单位圆周上的点 $(x, y)$ 满足 $x^2 + y^2 = 1$, 比如 $\sin x + \sin xy = \ln y$, 等等.

这里自然涉及一个基本问题: 既然 $x, y$ 只是通过方程 $F(x, y) = 0$ 给出, 同时又由于我们不能用显式表述出 $y = f(x)$ 的形式, 那么如何得知这个约束条件蕴涵着函数关系? 目前, 我们从理论上还不能给这个问题一个满意回答, 需要把这个基本问题推迟到多元微积分章节去讨论, 在那里我们将给出确定函数关系的条件, 以及函数关系成立的范围.

在本节, 我们的重点是假定通过其他方式已经得知隐式 $F(x, y) = 0$ 确定了一个函数关系 $y = f(x) (x \in I)$, 并且还知道这个函数在点 $x_0$ 处可导, 我们仅仅试图求出这个函数的导数.

这是一个听起来有点天方夜谭的问题: 我们甚至连函数关系都不能显式确定, 又如何谈起计算它的导数. 为此, 我们先考虑一道 “假的隐函数” 题目, 就是说本来可以把 y 用显式表示, 但我们先 “掩耳盗铃” 一番. 这样做的目的是希望从中获取一些感觉, 为后期的一般性讨论提供一些素材.

考虑隐函数 $x^{2} + y^{2} = 1$ ，其中 $x\in (-1,1),y > 0.$ 由于限定了 $y > 0,$ 那么可知这个约束关系的确给出了一个函数关系 $y = f(x)$ .我们欲求 $y = f(x)$ 在点 $x_0$ 的导数$f^{\prime}(x_0)$ .为此，记 $y_{0} = f(x_{0})$ ，即使不知道 $f(x)$ 的表达式， $y_{0}$ 的信息可以从 $F(x_0,y_0) = 0$ 中提取.比如，我们知道 $\left(\frac{3}{5},\frac{4}{5}\right)$ 满足隐函数关系，并不需要知道 $f(x)$ 的表达式

一方面, 我们将 $y = f(x)$ 代入到 $x^{2} + f^{2}(x) = 1$, 两端对其求导, 得

$$
2 x + 2 f (x) f ^ {\prime} (x) = 0.
$$

故

$$
f ^ {\prime} (x _ {0}) = - \frac {x _ {0}}{f (x _ {0})} = - \frac {x _ {0}}{y _ {0}}.
$$

我们强调的是: 在这样一个求导过程中, 并没有用到 $f$ 的具体表示, 却最终得到了一个并没有写出来的函数的导数值. 比如, 在点 $\left(\frac{3}{5}, \frac{4}{5}\right)$ 处, 我们就有 $y'\left(\frac{3}{5}\right) = -\frac{3}{4}$.

现在我们作一个验算: 从原来的“假隐函数”中, 解得 $y = f(x) = \sqrt{1 - x^2}$, 因此

$$
y ^ {\prime} = - \frac {x}{\sqrt {1 - x ^ {2}}} = - \frac {x}{y}.
$$

的确与我们不具体给出 $f(x)$ 的计算结果吻合.

采用上面的思路, 我们再考虑一个由隐函数确定的关系式的求导问题, 此时 $y$ 的确不易用 $x$ 的初等函数表示.

例6.3.7 考虑Kepler方程

$$
y - x - \varepsilon \sin y = 0, \quad 0 <   \varepsilon <   1.
$$

我们用到后面章节的一个断言: 该方程可以确定一个函数关系 $y = y(x)$, 而且 $y(x)$ 可导. 我们的问题是: 试求出 $y'(x)$.

解 由假设知

$$
y (x) - x - \varepsilon \sin y (x) = 0,
$$

两端对 x 求导, 得

$$
y ^ {\prime} (x) - 1 - \varepsilon y ^ {\prime} (x) \cos y (x) = 0,
$$

因此有

$$
y ^ {\prime} (x) = \frac {1}{1 - \varepsilon \cos y (x)}.
$$

比如在 $x_0 = 0$ 处, 该隐函数所对应的 $y_0 = 0$, 因此 0 点处的导数为 $y'(0) = \frac{1}{1 - \varepsilon}$.

## 5. 更多的求导法则

利用上面介绍的复合函数和反函数求导法则, 我们给出这些法则的几个具体应用, 主要包括所谓的对数求导法则、参数方程求导法则以及极坐标形式下的求导法则.

## (1) 对数求导法则

对数求导法作为求导的一种具体手法, 主要针对某些特定形式的函数求导. 比如形如 $u(x)^{v(x)}$ 的函数、若干因子相乘或相除的函数或含指数或幂次的函数, 当然还有这些函数的复合或组合. 这一手法最基本的出发点是利用了对数函数的性质: 将乘、除转化为加、减, 幂函数、指数函数转化为乘法, 而后者的计算量通常要小很多. 当然, 也不排除这些函数与前面的隐函数求导等结合起来, 甚至有可能多次取对数.

我们仅举几个例子领略一下这一方法.

例 6.3.8 求下列函数的导数:

$$
f (x) = x ^ {x} (x > 0), \quad g (x) = (\ln x) ^ {\ln x} (x > 1).
$$

解 两端取对数得

$$
\ln f (x) = x \ln x,
$$

两端再关于 $x$ 求导, 得

$$
\frac {f ^ {\prime} (x)}{f (x)} = 1 + \ln x,
$$

从而

$$
(x ^ {x}) ^ {\prime} = x ^ {x} (1 + \ln x).
$$

在等式 $g(x) = (\ln x)^{\ln x}$ 两端取对数，有

$$
\ln g (x) = (\ln x) \cdot \ln (\ln x),
$$

两端求导得

$$
\frac {g ^ {\prime} (x)}{g (x)} = \frac {1}{x} \cdot \ln (\ln x) + \ln x \cdot \frac {1}{\ln x} \cdot \frac {1}{x} = \frac {1}{x} \left(1 + \ln (\ln x)\right),
$$

所以有

$$
g ^ {\prime} (x) = \frac {1}{x} (\ln x) ^ {\ln x} \left(1 + \ln (\ln x)\right).
$$

作为练习,读者可以通过计算下面函数的导数体会对数求导法的使用场合.

例6.3.9 求函数

$$
y = \frac {(x + a _ {1}) ^ {\alpha_ {1}} (x + a _ {2}) ^ {\alpha_ {2}} \cdots (x + a _ {n}) ^ {\alpha_ {n}}}{(x ^ {2} + b _ {1} x + c _ {1}) ^ {\beta_ {1}} (x ^ {2} + b _ {2} x + c _ {2}) ^ {\beta_ {2}} \cdots (x ^ {2} + b _ {m} x + c _ {m}) ^ {\beta_ {m}}}
$$

的导数.

下面的问题是隐函数与对数求导相结合的例子.

例6.3.10 假设函数 $y = f(x)$ 是由隐函数

$$
x ^ {y} - y ^ {x} + 1 = 0
$$

确定的一个可导函数. 试求 $f'(2)$.

解 方程两端对 $x$ 求导, 得

$$
(\mathrm{e} ^ {y \ln x}) ^ {\prime} - (\mathrm{e} ^ {x \ln y}) ^ {\prime} = 0,
$$

$$
x ^ {y} \left(y ^ {\prime} \ln x + \frac {y}{x}\right) - y ^ {x} \left(\ln y + \frac {x}{y} y ^ {\prime}\right) = 0,
$$

故

$$
y ^ {\prime} = \frac {y ^ {x} \ln y - x ^ {y - 1} y}{x ^ {y} \ln x - y ^ {x - 1} x}.
$$

由于隐函数能够确定一个函数关系 $y = f(x)$，而当 $x = 2$ 时，显然 $y = 3$ 满足隐式关系，因此只能有唯一的 $y = 3$. 所以我们有

$$
f ^ {\prime} (2) = \frac {9 \ln 3 - 1 2}{8 \ln 2 - 6}.
$$

## (2) 参数方程求导法则

我们知道在一定条件下, 参数方程

$$
\left\{ \begin{array}{l l} x = x (t), \\ y = y (t), \end{array} \right. \quad t \in (\alpha , \beta),
$$

可以通过参数 $t$ 来确定 $x, y$ 之间的函数关系 $y = f(x)$. 下面我们对参数方程求导问题作一简要讨论.

首先, 在前面讨论反函数导数时曾经讨论过, 如果 $x(t), y(t)$ 在 $t \in (\alpha, \beta)$ 内严格单调、可导, 且 $\frac{\mathrm{d}}{\mathrm{d}t} x(t) \neq 0$, 则 $x = x(t)$ 在区间 $x \in (a, b)$ 内存在反函数 $t = t(x)$, 其中

$$
a = \min \left\{x (\alpha^ {+}), x (\beta^ {-}) \right\}, \quad b = \max \left\{x (\alpha^ {+}), x (\beta^ {-}) \right\}.
$$

将 $t = t(x)$ 代入 $y = y(t)$ 可得函数

$$
y = y (t) = y (t (x)), \quad x \in (a, b).
$$

由复合函数求导法则, 我们有

$$
\frac {\mathrm{d} y}{\mathrm{d} x} = \frac {\mathrm{d} y}{\mathrm{d} t} \cdot \frac {\mathrm{d} t}{\mathrm{d} x} = \frac {y ^ {\prime} (t)}{x ^ {\prime} (t)}.
$$

例6.3.11 求由参数方程 $x = t, y = t^2$ 所确定的函数在 $t = 1$ 处的导数 $\frac{\mathrm{dy}}{\mathrm{dx}}$.

解 考虑到 $x'(t) = 1 \neq 0, y'(t) = 2t$，所以该参数方程确定 $x, y$ 之间的一个函数 $y = y(t(x))$，且

$$
\frac {\mathrm{d} y}{\mathrm{d} x} \bigg | _ {t = 1} = \left. \frac {y ^ {\prime} (t)}{x ^ {\prime} (t)} \right| _ {t = 1} = 2.
$$

当然, 本例中的参数方程非常简单, 故直接得到函数的显式表示 $y = x^2$ 并作验证.

例6.3.12 求由参数方程 $x = \sin t, y = \mathrm{e}^t$ 所确定的函数在 $t = 0$ 处的导数 $\frac{\mathrm{dy}}{\mathrm{dx}}$.

解 考虑到在 $t = 0$ 附近, $x'(t) = \cos t \neq 0$, $y'(0) = 1$, 所以该参数方程确定 $x, y$ 之间的一个函数 $y = y(t(x))$, 且

$$
\left. \frac {\mathrm{d} y}{\mathrm{d} x} \right| _ {t = 0} = \left. \frac {y ^ {\prime} (t)}{x ^ {\prime} (t)} \right| _ {t = 0} = 1.
$$

## (3) 极坐标形式下求导法则

考虑一类特殊的参数方程的求导问题: 设 $r = r(\theta), \theta \in (\alpha, \beta)$ 是一给定的函数, 由此函数可以诱导出参数方程

$$
\left\{ \begin{array}{l l} x = r (\theta) \cos \theta , & \theta \in (\alpha , \beta). \\ y = r (\theta) \sin \theta , \end{array} \right.
$$

假设 $r(\theta)$ 作为 $\theta$ 的函数其导数 $r'(\theta)$ 存在, 在 $\theta_0$ 附近

$$
x ^ {\prime} (\theta_ {0}) = r ^ {\prime} (\theta_ {0}) \cos \theta_ {0} - r (\theta_ {0}) \sin \theta_ {0} \neq 0.
$$

由前面的讨论, 知此时有反函数关系 $\theta = \theta(x)$, 代入 $y = y(\theta) = y(\theta(x))$, 可以进一步计算 $y$ 关于 $x$ 的导数了.

$$
\frac {\mathrm{d} y}{\mathrm{d} x} = \frac {r ^ {\prime} (\theta) \sin \theta + r (\theta) \cos \theta}{r ^ {\prime} (\theta) \cos \theta - r (\theta) \sin \theta},
$$

这就是极坐标形式下函数的求导公式. 我们对等式作一些形式处理:

$$
\frac {\mathrm{d} y}{\mathrm{d} x} = \frac {\tan \theta + \frac {r (\theta)}{r ^ {\prime} (\theta)}}{1 - \tan \theta \frac {r (\theta)}{r ^ {\prime} (\theta)}}.
$$

注意到导数的几何意义 (见图 6.5) $\frac{dy}{dx}$ 是切线与 x 轴正向的夹角 $\alpha$ 的正切, 即

$$
\frac {\mathrm{d} y}{\mathrm{d} x} = \tan \alpha = \frac {\tan \theta + \frac {r (\theta)}{r ^ {\prime} (\theta)}}{1 - \tan \theta \frac {r (\theta)}{r ^ {\prime} (\theta)}}.
$$

因此, 由此可解出

$$
\frac {r (\theta)}{r ^ {\prime} (\theta)} = \frac {\tan \alpha - \tan \theta}{1 + \tan \alpha \tan \theta} = \tan (\alpha - \theta).
$$

![](images/page_169_image_6.jpg)

<details>
<summary>text_image</summary>

y
r=r(θ)
β
θ
O
x
α
</details>

图6.5 极坐标的导数

例 6.3.13 考虑 Archimedes 螺线在极坐标下的表示

$$
r = \frac {1}{2 \pi} \theta .
$$

容易求得 $\frac{\mathrm{d}r}{\mathrm{d}\theta} = \frac{1}{2\pi}$ 是个常数. 考虑到极坐标的内涵, 这说明在极坐标下 $r$ 关于 $\theta$ 的导数为常数的几何意义就是, 每当 $\theta$ 改变 $\Delta \theta$ 时, $r$ 的改变量都是 $k\Delta \theta$. 特别地, 每当 $\theta$ 逆时针旋转一周增加 $2\pi$ 时, $r$ 便增加 1. 这深刻刻画了 Archimedes 螺线的特点.

如果用直角坐标

$$
\sqrt {x ^ {2} + y ^ {2}} = k \mathrm{e} ^ {\arctan {\frac {y}{x}}}
$$

表述 Archimedes 螺线的话, 形式上要复杂得多. 而此时 $y$ 关于 $x$ 的导数为

$$
\frac {\mathrm{d} y}{\mathrm{d} x} = \frac {x + y}{x - y}.
$$

例6.3.14 考虑双纽线 $r^2 = a^2\cos 2\theta \left(0 < \theta < \frac{\pi}{4}\right)$. 证明: 双纽线的向径与切线的夹角与极角两倍的差是常数.

证明 设向径与切线的夹角为 $\beta$. 则

$$
\tan \beta = \frac {r (\theta)}{r ^ {\prime} (\theta)} = \frac {r ^ {2} (\theta)}{r (\theta) r ^ {\prime} (\theta)} = - \frac {\cos 2 \theta}{\sin 2 \theta} = \tan \left(2 \theta + \frac {\pi}{2}\right).
$$

注意到 $0 < \theta < \frac{\pi}{4}$, 故有 $\beta - 2\theta = \frac{\pi}{2}$.

## 习题6.3

1. 求下列函数的导数:

(1) $f(x) = (x + 1)(x + 2)^{2}(x + 3)^{3}$;
(2) $f(x) = (1 + nx^{m})(1 + mx^{n})$;
(3) $f(x) = (ax^{m} + b)^{n}(cx^{n} + d)^{m}$.

2. 求下列函数的导数:

(1) $f(x)=\sqrt{\sin^{2}x};$

(2) $f(x) = \frac{x}{(1 - x)^2(1 + x)}$;
(4) $f(x) = \frac{x \sin x + \cos x}{x \sin x - \cos x}$.

(3) $f(x) = \frac{x^p(1 - x)^q}{1 + x}$;

3. 求下列函数的导数:

(1) $f(x)=\frac{x}{\sqrt{a^{2}+x^{2}}}$;

(2) $f(x) = \arcsin (\cos^2 x)$;

(3) $f(x) = \arcsin x\sqrt{1 - x^2};$

(4) $f(x)=\sqrt{x+\sqrt{x+\sqrt{x}}};$

(5) $f(x) = \mathrm{e}^{ax}\sin bx.$

4. 求下列函数的导数:

(1) $f(x) = (x \sin x)^x$;

(2) $f(x) = x\sqrt{\frac{1 - x}{1 + x}};$

(3) $f(x) = (x)^{a^x}$;

(4) $f(x) = a^{x^n}$;

(5) $f(x) = (\cos x)^{\sin x} + (\sin x)^{\cos x};$

(6) $f(x) = (x + \sqrt{1 + x^2})^n$.

5. 设

$$
f (x) = \cos \left(2 \arctan \left(\sin \left(\operatorname{arccot} \sqrt {\frac {1 - x}{x}}\right)\right)\right),
$$

证明下面四个关系式中有一个成立:

(1) $(1 - x)^{2}f^{\prime}(x) - 2(f(x))^{2} = 0;$
(2) $(1 - x)^{2}f^{\prime}(x) + 2(f(x))^{2} = 0;$
(3) $(1 + x)^{2}f^{\prime}(x) - 2(f(x))^{2} = 0;$
(4) $(1 + x)^{2}f^{\prime}(x) + 2(f(x))^{2} = 0.$

6. 设

$$
y = \frac {1}{4 \sqrt {2}} \ln \frac {x ^ {2} + \sqrt {2} x + 1}{x ^ {2} - \sqrt {2} x + 1} - \frac {1}{2 \sqrt {2}} \arctan \frac {\sqrt {2} x}{x ^ {2} - 1},
$$

求  $y'(x)$ .

7. 求下列由参数方程所确定的函数的导数  $\frac{dy}{dx}$ :

(1) $\left\{\begin{aligned}x&=\cos^{4}t,\\ y&=\sin^{4}t\end{aligned}\right.$ 在 $t=\frac{\pi}{3}$ 处;

(2) 设  $\left\{\begin{aligned} x &= a(t - \sin t), \\ y &= a(1 - \cos t), \end{aligned}\right.$  求  $\left.\frac{dy}{dx}\right|_{t=\frac{\pi}{2}}, \left.\frac{dy}{dx}\right|_{t=\pi}.$

8. 设 $f(x)$ 可导，求 $y'$:

(1) $y = f(x \sin x)$;

(2) $y = f(\mathrm{e}^x)\mathrm{e}^{f(x)}$;

(3) $y = f(\cos x) \sin x;$

(4) $y = f(f(f(x)))$;

(5)  $y = f(\tan x)$ ;

(6) $y = [f(\ln x)]^n$.

9. 设  $u(x)$ ,  $v(x)$  可导, 求  $y'$ :

(1) $y = \sqrt{u^2(x) + v^2(x)}$;

(2) $y = \sqrt[u]$;

(3) $y = \arctan \frac{u(x)}{v(x)}$;

(4) $y = \frac{u}{v^2}$;

(5) $y = \frac{1}{\sqrt{u^2 + v^2}}$;

(6) $y = u^{\mathrm{e}^{v}}$.

10. 设 $a_{ij}(x)$ 均为可导函数, 试求行列式 $\det(a_{ij}(x))_{n \times n}$ 的导数.

11. 将区间  $(0,1)$  内的实数 x 用十进制无限小数表示为  $x = 0.x_{1}x_{2}x_{3}\cdots, x_{i} \in \{0,1,\cdots,9\}$ . 比如 x = 0.5, 则记为  $x = 0.4999\cdots$ . 定义  $f(x) = 0.x_{1}0x_{2}00x_{3}\cdots$ , 试讨论  $f(x)$  是否有可导的点.

12. 前面曾经引入过 [0,1] 上的 Riemann 函数 (参见习题 5.1 中的题目 2):

$$
R (x) := \left\{ \begin{array}{l l} {1,} & {x = 0,} \\ {\frac {1}{q},} & {x = \frac {p}{q}, \quad \text {其中} p, q \text {为既约整数},} \\ {0,} & {x \text {为无理数}.} \end{array} \right. \tag {6.3.8}
$$

证明 Riemann 函数 $R(x)$ 虽然在无理点连续, 但处处不可导.

13. 设 $R(x)$ 是由 (6.3.8) 式定义的 Riemann 函数. 记 $R_{2}(x) = R^{2}(x), R_{3}(x) = R^{3}(x)$. 证明:

(1)  $R_{2}(x)$  在 [0,1] 上仍然处处不可导;

\*(2) $R_{3}(x)$ 在[0,1]上存在可导的点.

14. 设  $x_{1}, x_{2}, \cdots, x_{n}$  是 n 个两两互异的实数， $y(x) = (x - x_{1})(x - x_{2}) \cdots (x - x_{n})$ ，计算并化简

$$
\sum_ {k = 1} ^ {n} \frac {1}{y ^ {\prime} (x _ {k})}.
$$

进一步, 当  $x_{1}, x_{2}, \cdots, x_{n}$  有相等的情况时, 有可能  $y'(x_{k}) = 0$ , 试给出一个与上面求和式类似的求和表达式.

15. 设  $x_{1}, x_{2}, \cdots, x_{n}$  是 n 个两两互异的实数, 考虑 Vandermonde 行列式

$$
y (x) = \left| \begin{array}{c c c c c} 1 & 1 & \dots & 1 & 1 \\ x _ {1} & x _ {2} & \dots & x _ {n} & x \\ x _ {1} ^ {2} & x _ {2} ^ {2} & \dots & x _ {n} ^ {2} & x ^ {2} \\ \vdots & \vdots & & \vdots & \vdots \\ x _ {1} ^ {n} & x _ {2} ^ {n} & \dots & x _ {n} ^ {n} & x ^ {n} \end{array} \right|.
$$

试计算

$$
\sum_ {k = 1} ^ {n} \frac {1}{y ^ {\prime} (x _ {k})}.
$$

16. 证明: 椭圆 $x^{2} + 2y^{2} = C^{2}$ 与抛物线 $y = px^{2}$ 在任一交点处的切线都相互垂直.
17. 证明: 对任意的实数 $a, b, 0 < |a| < 1, |b| > 1$, 椭圆 $\frac{x^2}{a^2} + \frac{y^2}{1 - a^2} = 1$ 与双曲线 $\frac{x^2}{b^2} + \frac{y^2}{1 - b^2} = 1$ 在交点处的切线相互垂直.
18. 证明: 对于任意实数 $c_{1}, c_{2}$, 曲线 $xy = c_{1}$ 与 $x^{2} - y^{2} + 2xy = c_{2}$ 在交点处两曲线切线的夹角是定值 $\frac{\pi}{4}$.
19. 设 $f(x_0) = g(x_0)$, $f(x), g(x)$ 在点 $x_0$ 处均可导, 且有相同的导数 $k$, 证明对于满足条件

$$
\min \{f (x), g (x) \} \leqslant h (x) \leqslant \max \{f (x), g (x) \}
$$

的任一函数  $h(x)$  在  $x_{0}$  处也是可导的, 且导数值等于 k. 试给出其几何直观理解.

20. 设 $f(x)$ 在 $x = 0$ 处可导. 问极限 $\lim_{x \to 0} \frac{f(x) - f(x - x^3)}{x^3}$ 是否一定存在?

21. 设 $f(x)$ 在 $x = 0$ 处连续. 问两极限 $\lim_{x \to 0} \frac{f(x) - f(0)}{x}$ 和 $\lim_{x \to 0} \frac{f(x^3) - f(x^3 - x^5)}{x^5}$ 之间的存在性有没有逻辑关系？

22. 证明在 $\mathbb{R}$ 上不存在可微函数 $f$ 满足

$$
f \circ f (x) = - x ^ {3} + x ^ {2} + 1.
$$

23. 证明在 $\mathbb{R}$ 上不存在可微函数 $f$ 满足

$$
f \circ f (x) = x ^ {2} - 3 x + 3.
$$

## 6.4 函数的微分

## 6.4.1 微分的定义 可导与可微的关系

前面我们引入了函数的导数这一基本概念. 函数 $f(x)$ 在点 $x_0$ 处可导是指当自变量作微小改变 $\Delta x = x - x_0$ 时, 函数值的改变量 $\Delta y = f(x) - f(x_0)$ 与自变量改变量 $\Delta x$ 差商 $\Delta y / \Delta x$ 的极限存在且有限. 因此函数可导是指这一差商的极限有一个明确趋势.

微分是与导数紧密相关的另一个概念, 在上述符号和语境下, 微分更侧重于考察当 x 改变  $\Delta x$  时引起的 y 的改变量  $\Delta y$  的大小, 以及特别关注  $\Delta y$  的大小是否与  $\Delta x$  的大小大致稳定在一个比例关系上. 具体来说就是, 对于不同的  $\Delta x$ ,  $\Delta y$  自然可以不同, 但是当  $\Delta x$  比较小时,  $\Delta y$  能否总能 “粗线条” 近似等于  $A\Delta x$ , 其中 A 是常数, “粗线条” 是指两者的误差  $\Delta y - A\Delta x$  相对于基本无穷小量  $\Delta x$  而言, 是可以 “忽略不计” 的高阶无穷小量. 若如此, 则称  $y = f(x)$  在  $x_{0}$  处可微. 我们给出如下严格的定义:

定义 6.4.1 设  $y = f(x)$  在点  $x_{0}$  附近有定义, 如果存在常数 A, 使得

$$
\Delta y = f (x _ {0} + \Delta x) - f (x _ {0}) = A \Delta x + o (\Delta x) \quad (\Delta x \rightarrow 0),
$$

则称 $f(x)$ 在点 $x_0$ 处可微. $A\Delta x$ 构成了 $\Delta y$ 主要部分, 简称 $\Delta y$ 的主部, 常称之为 $y$ 的微分, 记为 $\mathrm{dy}$ 或 $\mathrm{df}(x_0)$. 即当函数 $y = f(x)$ 在点 $x_0$ 处可微时, 有 $\mathrm{dy} = A\Delta x$.

![](images/page_173_image_9.jpg)

<details>
<summary>natural_image</summary>

Blank white image with a thin blue horizontal line at the top (no text or symbols)
</details>

注 6.4.1 (1) 定义中所说的 A 是常数, 是指它相对于  $\Delta x$  而言是常数, 不依赖于  $\Delta x$  的改变而改变. 显然, A 的值是依赖于  $x_{0}$  点的, 即  $A = A(x_{0})$ , 当不刻意强调  $x_{0}$  时, 常写为  $A = A(x)$ .

(2) 考虑到取特殊函数 $y = f(x) = x$ 时, 显然有 $\Delta y = \Delta x$, 所以又有 $\mathrm{dx} = \Delta x$. 因此在微分记号中, 常约定把 $\Delta x$ 记成 $\mathrm{dx}$, 而把一个可微函数的微分记为 $\mathrm{dy} = A\mathrm{dx}$.

我们通过下面具体例子来体会一下微分的几何直观.

例 6.4.1 考虑边长为  $x_{0}$  的正方形的面积  $S = x_{0}^{2}$ ，当边长  $x_{0}$  作一微小改变  $\Delta x$  时，则正方形的面积改变量为

$$
\Delta S = (x _ {0} + \Delta x) ^ {2} - x _ {0} ^ {2} = 2 x _ {0} \Delta x + (\Delta x) ^ {2}. \tag {6.4.1}
$$

从解析式(6.4.1)可以看出, $\Delta S$ 包含两部分, $2x_0\Delta x$ 和 $(\Delta x)^2$. 当 $\Delta x \to 0$ 时, $\Delta S$ 的主部 $\mathrm{d}S = 2x_0\Delta x$, 而误差 $\Delta S - \mathrm{d}S$ 为 $(\Delta x)^2$, 是 $\Delta x$ 的高阶无穷小量. 根据定义, 这说明正方形的面积 $S = x^2$ 是边长 $x$ 的可微函数, 且 $\mathrm{d}S = 2x\mathrm{d}x$.

解析式 (6.4.1) 有明确的几何直观, 从图 6.6 中可以看出 $\Delta S$ 两部分的几何意义: $2x_{0}\Delta x$ 对应的是两个长为 $x_{0}$, 宽为 $\Delta x$ 的浅蓝色长方形的面积, $(\Delta x)^{2}$ 对应的是一个边长为  $\Delta x$  的深蓝色正方形的面积, 它是自变量的改变量  $\Delta x$  的高阶无穷小量.

![](images/page_174_image_3.jpg)

<details>
<summary>text_image</summary>

y
Δx
x₀
(Δx)²
S
Δx
O
x₀
x
</details>

图6.6

关于可微与可导之间的关系, 成立下面的重要定理:

定理 6.4.1 函数 $y = f\left( x\right)$ 在点 ${x}_{0}$ 处可微的充要条件是它在该点处可导.

证明 (必要性) 若 $f(x)$ 在 $x_0$ 处可微, 即存在常数 $A$ 使得

$$
\Delta y = f (x _ {0} + \Delta x) - f (x _ {0}) = A \Delta x + o (\Delta x) \quad (\Delta x \rightarrow 0) \tag {6.4.2}
$$

成立. 从而

$$
\frac {\Delta y}{\Delta x} = A + o (1) \qquad (\Delta x \to 0),
$$

即

$$
\lim _ {\Delta x \to 0} f ^ {\prime} (x _ {0}) = \lim _ {\Delta x \to 0} \frac {\Delta y}{\Delta x} = A.
$$

这表明 $f(x)$ 不但在点 $x_0$ 处可导, 而且其导数值为 $f'(x_0) = A$.

(充分性) 如果  $f(x)$  在  $x_{0}$  处可导, 即

$$
\lim _ {\Delta x \to 0} \frac {f (x _ {0} + \Delta x) - f (x _ {0})}{\Delta x} = f ^ {\prime} (x _ {0}).
$$

用无穷小等价的语言表示, 有

$$
\frac {f (x _ {0} + \Delta x) - f (x _ {0})}{\Delta x} = f ^ {\prime} (x _ {0}) + o (1) \quad (\Delta x \to 0),
$$

从而有关系式 (6.4.2) 成立, 其中 $A = f'(x_0)$, 即

$$
\Delta y = f (x _ {0} + \Delta x) - f (x _ {0}) = f ^ {\prime} (x _ {0}) \Delta x + o (\Delta x) \quad (\Delta x \rightarrow 0).
$$

从而

$$
\mathrm{d} y = f ^ {\prime} (x) \mathrm{d} x. \tag {6.4.3}
$$

□

类似于导数值刻画的是切线的斜率, 微分也有相应的几何意义: 给定函数 $y = f(x)$ 以及它对应的曲线 $C$, 设曲线 $C$ 在 $P_0(x_0, f(x_0))$ 处存在切线 $\ell, P(x_0 + \Delta x, f(x_0 + \Delta x))$ 是曲线 $C$ 上 $P_0$ 附近的另一点, 点 $Q(x_0 + \Delta x, f(x_0))$ 和点 $T(x_0 + \Delta x, f(x_0) + f'(x_0)\Delta x)$ 如图 6.7 所示. 则

$$
Q T = \mathrm{d} y = f ^ {\prime} (x _ {0})) \Delta x, \qquad T P = \Delta y - \mathrm{d} y = o (\Delta x) \quad (\Delta x \to 0).
$$

![](images/page_175_chart_4.jpg)

<details>
<summary>line</summary>

| Point | x-coordinate | y-coordinate |
| --- | --- | --- |
| P0 | \(x_0\) | \(y_0\) |
| Q | \(x_0+\Delta x\) | \(y_0+\Delta y\) |
| T | N/A | N/A |
</details>

图6.7

所以我们看到如下事实:

(1)  $dx = \Delta x = P_{0}Q$  是自变量的增量;
(2)  $\Delta y = QP$  是函数的增量;
(3)  $\mathrm{d}y = f'(x_{0})\mathrm{d}x = QT$  几何上是切线的增量, 代数上是函数增量的线性主部, 即微分;
(4)  $\Delta y - \mathrm{d}y = o(\Delta x) = TP$  是函数增量与其切线增量的差.

我们知道, Leibniz 引入的导数符号  $\frac{dy}{dx}$  是一个整体记号, 引入微分概念后, 我们可以给导数符号赋予新的内涵: 即可以把它看成分子 dy 与分母 dx 的商从而可以单独参与运算, 类似于  $\frac{3}{5}$  中的 3 和 5. 这一形式上的解脱为我们提供了极大的方便:

$$
\frac {\mathrm{d} y}{\mathrm{d} x} = A \quad \Longleftrightarrow \quad \mathrm{d} y = A \mathrm{d} x.
$$

当然, 如果从形式上来理解微分仅仅是把导数两端乘 dx 得来就过于表象化了. 在后期众多的课程中, 我们将渐渐意识到微分适用的场景将远远超过导数, 具有更强大的威力和更广泛的应用.

微分强调的是在某点附近, 函数的改变量能否剥离出自变量改变量的一个线性主部, 而导数强调的是两个改变量的比值. 可微和可导似乎是看待同一事情 $\Delta y$ 的两个不同角度, 差别不大. 对于一元函数而言的确如此, 即可微等价于可导. 这一等价性对于多元函