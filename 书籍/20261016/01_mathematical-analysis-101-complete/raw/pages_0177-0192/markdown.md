数而言不再成立, 导数这个概念在一般的情况下不再出现: 当自变量是向量而不再是数域里的元素时, 导数定义中的自变量改变量作为除数已不再有意义, 但它的线性主部仍然具有明确的意义. 因此, 可微这个概念适用的范围更广, 它也将逐渐取代可导这个概念, 在后续课程中展现出微分巨大的威力.

根据可导与可微的关系以及等式(6.4.2)，对于给定的函数 $f(x)$ ，如果已知 $f(x_0)$ 和$f^{\prime}(x_{0})$ 的值，那么利用

$$
\Delta y = f (x _ {0} + \Delta x) - f (x _ {0}) \approx \mathrm{d} y = f ^ {\prime} (x _ {0}) \Delta x
$$

可知

$$
f (x _ {0} + \Delta x) \approx f (x _ {0}) + f ^ {\prime} (x _ {0}) \Delta x.
$$

这给我们提供了计算  $f(x)$  在点  $x_{0}$  附近近似估计的一种方法.

例 6.4.2 试求  $\sqrt{101}$  和  $\sqrt[4]{15}$  的近似值.

解 注意到所求值  $\sqrt{101} = \sqrt{100 + 1} = 10\sqrt{1 + 0.01}$ . 我们首先考察函数  $\sqrt{1 + x}$  在 x = 0 附近的估算.

由于 $(\sqrt{1 + x})' = \frac{1}{2\sqrt{1 + x}}, (\sqrt{1 + x})'|_{x=0} = \frac{1}{2}$. 所以当 $\Delta x$ 非常小时, 有

$$
\sqrt {1 + \Delta x} = 1 + \frac {1}{2} \Delta x + o (\Delta x) \qquad (\Delta x \to 0).
$$

或者说当  $\Delta x$  很小时,

$$
\sqrt {1 + \Delta x} \approx 1 + \frac {1}{2} \Delta x.
$$

取  $\Delta x = 0.01$  时, 可视为  $\Delta x$  比较小, 故有

$$
\sqrt {1 0 1} = 1 0 \sqrt {1 + 0 . 0 1} \approx 1 0 \times (1 + 0. 0 0 5) = 1 0. 0 5.
$$

对于 $\sqrt[4]{15}$ 的计算，我们有如下类似讨论:注意到所求值 $\sqrt[4]{15} = \sqrt[4]{16 - 1} = 2\sqrt[4]{1 - \frac{1}{16}}$。我们首先考察函数 $\sqrt[4]{1 + x}$ 在 $x = 0$ 附近的估算。

由于 $(\sqrt[4]{1 + x})' = \frac{1}{4\sqrt[4]{(1 + x)^3}}, (\sqrt[4]{1 + x})'|_{x=0} = \frac{1}{4}$. 所以当 $\Delta x$ 非常小时, 有

$$
\sqrt [ 4 ]{1 + \Delta x} \approx 1 + \frac {1}{4} \Delta x.
$$

取 $\Delta x = \frac{-1}{16}$ 时, 可视为 $\Delta x$ 比较小, 故有

$$
\sqrt [ 4 ]{1 5} = 2 \sqrt [ 4 ]{1 - \frac {1}{1 6}} \approx 2 \times \left(1 - \frac {1}{6 4}\right) \approx 1. 9 6 8 7 5
$$

(对比精确值 1.96798967 $\cdots$ ).

当然在精度要求比较高时, 上述估计还是比较粗略的. 而且上述讨论中, 我们也没有给出 $\Delta x$ 大小的一个标准, 即何时可以把它当作比较小, 何时又不可. 这些误差估计方面的问题在后面进一步的讨论中会逐渐得到解决. 但是, 在很多情况下通过微分给出的粗略预估还是很有益处的. 比如, 考虑下面的例子, 请先给出题目的一个朴素的、直觉上的猜测 (甚至非常粗略的感觉: 是较大的值还是较小的数), 再通过具体计算对比一下两个答案的吻合度.

例 6.4.3 将地球看成是一个半径为  $r = 6.4 \times 10^{6} \, m$  的理想球体.

(1) 在赤道上方围绕赤道拉一圈离地面高度为  $1 \, m$  的电线, 问电线的总长度比赤道的周长长多少米?
(2) 用一个厚度为 $1 \mathrm{~cm}$ 的地毯把地球铺满了, 问地毯外层的表面积比地球的表面积大多少?
(3) 用一个厚度为  $1 \, mm$  的薄膜把地球包起来, 问薄膜的总体积大约是多少? 换句话说, 问当地球的半径增加了  $1 \, mm$  时, 地球体积增加多少?

解 (1) 地球赤道的周长可以通过 $L = 2\pi r$ 来计算, 因此可以把电线离地面的高度当成是地球半径的改变量 $\Delta r = 1 \mathrm{~m}$. 相对于 $r$ 来说, 我们认为 $\Delta r$ 是一个非常小的量. 故电线的长度与赤道的长度的差的主部为

$$
\mathrm{d} L = 2 \pi \mathrm{d} r \approx 6. 2 8 (\mathrm{m}).
$$

考虑到地球之大, 这个差别是微不足道的.

(2) 地球的表面积 $S = 4\pi r^2$ 是 $r$ 的一个可微函数, $\Delta r = 1 \mathrm{~cm} = 0.01 \mathrm{~m}$, 因此所求改变量可以估计如下:

$$
\mathrm{d} S = 8 \pi r \mathrm{d} r = 8 \times 6. 4 \times 1 0 ^ {6} \times 0. 0 1 \pi \approx 1. 6 \times 1 0 ^ {6} (\mathrm{m} ^ {2}).
$$

这大致是说: 在现有的基础上, 如果地球半径增加 1 cm, 则表面积大概相当于增加了 224 个标准足球场 $^{①}$ .

(3) 地球的体积 $V = \frac{4}{3}\pi r^3$ 是 $r$ 的一个可微函数, $\Delta r = 1\mathrm{mm} = 0.001\mathrm{m}$, 因此所求误差量可以估计如下:

$$
\mathrm{d} V = 4 \pi r ^ {2} \mathrm{d} r = 4 \times 6. 4 ^ {2} \times 1 0 ^ {1 2} \times 0. 0 0 1 \pi \approx 5. 1 5 \times 1 0 ^ {1 1} (\mathrm{m} ^ {3}).
$$

这大致是说: 在现有的基础上, 如果地球半径增加 $1 \mathrm{~mm}$, 则地球的体积大概相当于增加了 $10^{10}$ (一百亿) 个容积为 $50 \mathrm{~m}^{3}$ 个集装箱. 相对于 $1 \mathrm{~mm}$ 而言, 这是一个相当可观的数字.

我们换个角度再来讨论例6.4.3中更一般的场景.

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">① 世界杯决赛足球场尺寸为  $105 \, m \times 68 \, m = 7140 \, m^{2}$ .</span></small>

例 6.4.4 若已知 n 维空间中的半径为 r 的球体体积  $V_{n}$  为

$$
V _ {n} (r) = B _ {n} r ^ {n},
$$

其中 $B_{n}$ 是一个仅仅与 $n$ 有关的常数. 我们来考察当 $r$ 有微小改变时, 体积 $V_{n}(r)$ 的改变.

解 (i) 我们先看一下当 $n = 2$ 时的数学模型. 把比萨饼看成一个理想的半径为 1 的圆盘, 则面积为 $V_{2}(r) = \pi r^{2}|_{r=1} = \pi$. 假设比萨饼卷边宽度为 $\alpha$, 那么卷边占整个比萨的分量为 (假设卷边与内部有相同密度)

$$
\frac {V _ {2} (r) - V _ {2} (r - \alpha)}{V _ {2} (r)} = 2 \alpha - \alpha^ {2}.
$$

如果取  $\alpha = 10\%$ , 则比萨饼边占整个比萨饼大约为 20% (与精确值之间的误差为 1%).

(ii) 再看一下当 $n = 3$ 时的情景, 此时等同于上例中的 (3). 我们换个更通俗一些的场景: 把一个西瓜看成一个单位半径的理想球体, 假设西瓜皮的厚度占总厚度的 $\alpha$, 那么西瓜皮占据整个西瓜的分量为 (假设西瓜皮与西瓜瓤有相同的密度)

$$
3 \alpha - 3 \alpha^ {2} + \alpha^ {3}.
$$

其主部为  $3\alpha$ .

仍取  $\alpha = 10\%$ , 可知西瓜皮占整个西瓜的分量大概为 30%, 误差不超过为 3%. 可以看到, 西瓜皮所占分量还是很大的.

(iii) 对于一般的 n, 考虑 n 维空间中的单位球体, 当去掉一个厚度为  $\alpha$  的球皮时, 缩小的部分占原来整个球体体积的比例为  $\frac{\Delta V_{n}}{V_{n}}$ . 容易算出, 当  $\alpha$  很小时, 此比例的主部为  $n\alpha$ .

基于此, 一个朴素的结论呼之欲出:

思考并证明 对任意给定的 $0 < \delta_0 \ll 1$, 考虑 $n$ 维空间中的一个球皮厚度为 $\delta_0$、质量密度为 1 的单位球体, 则成立: $\forall \varepsilon > 0$, 只要空间维数 $n$ 足够大, 则球皮质量占整个球体质量 $V_n(1)$ 的比可以大于 $1 - \varepsilon$. 即在高维空间中, 球体质量几乎全部集中在球皮上.

有兴趣的读者可以作进一步的思考, 类似的表述还有: 高维球面的质量几乎全部集中在任意一条赤道附近 (注: $n$ 维空间中的半径为 $r$ 的球体的表面积 $S_{n}(r) = nB_{n}r^{n - 1}$).

## 6.4.2 微分法则

我们简要介绍一下微分法则. 所谓的微分法则是指计算微分时可以遵循的方法和规则. 因为从逻辑上我们已经知道函数的可微等价于可导, 我们还知道在函数可微时 $\mathrm{dy} = A\mathrm{dx}$ 中的系数 $A$ 就是 $f'(x)$, 所以前面讨论的几类初等函数的微分可以直接写出来, 在此不再一一列举. 下面先给出常见的微分的四则运算法则.

定理 6.4.2 设  $f(x)$ ,  $g(x)$  在点 x 处可微, 则有

(1)  $\mathrm{d}(f \pm g) = \mathrm{d}f \pm \mathrm{d}g;$
(2)  $\mathrm{d}(fg)=g\mathrm{d}f+f\mathrm{d}g;$
(3) $\mathrm{d}\left(\frac{f}{g}\right) = \frac{g\mathrm{d}f - f\mathrm{d}g}{g^2}$, 其中 $g \neq 0$.

例 6.4.5 计算  $y = \arctan x + \frac{1}{2} \ln \frac{1 + x}{1 - x}$  的微分.

解 由

$$
y ^ {\prime} = \frac {1}{1 + x ^ {2}} + \frac {1}{2} \left(\frac {1}{1 + x} + \frac {1}{1 - x}\right) = \frac {1}{1 + x ^ {2}} + \frac {1}{1 - x ^ {2}} = \frac {2}{1 - x ^ {4}}
$$

可得

$$
\mathrm{d} y = \frac {2}{1 - x ^ {4}} \mathrm{d} x.
$$

## 6.4.3 一阶微分的形式不变性

复合函数的求导运算成立特色鲜明的链式法则, 即如果函数 $y = f(u), u = g(x)$ 均在相应的点处可导, 则 $y = f(g(x))$ 也可导, 且

$$
\frac {\mathrm{d} y}{\mathrm{d} x} = (f (g (x))) ^ {\prime} = f ^ {\prime} (g (x)) g ^ {\prime} (x).
$$

所以, 一方面由定理 6.4.1 及等式 (6.4.3), 知

$$
\mathrm{d} y = (f (g (x))) ^ {\prime} \mathrm{d} x = f ^ {\prime} (g (x)) g ^ {\prime} (x) \mathrm{d} x.
$$

另一方面, 两个可导函数 $y = f(u)$ 和 $u = g(x)$ 的微分分别为

$$
\mathrm{d} y = f ^ {\prime} (u) \mathrm{d} u, \quad \mathrm{d} u = g ^ {\prime} (x) \mathrm{d} x.
$$

所以有

$$
\mathrm{d} y = f ^ {\prime} (u) \mathrm{d} u = f ^ {\prime} (u) g ^ {\prime} (x) \mathrm{d} x.
$$

这说明当把 $u$ 作为自变量时，函数 $y = f(u)$ 的微分为 $\mathrm{dy} = f'(u)\mathrm{du}$；而当把 $u$ 当成中间变量时，函数 $y = f(g(x))$ 的微分 $\mathrm{dy} = f'(g(x))g'(x)\mathrm{dx}$ 仍然满足 $\mathrm{dy} = f'(g(x))\mathrm{du} = f'(u)\mathrm{du}$. 这就是所谓的（一阶）微分形式的不变性. 用Leibniz表示导数的记号有

$$
\mathrm{d} y = \frac {\mathrm{d} f (u)}{\mathrm{d} u} \mathrm{d} u = \frac {\mathrm{d} f (g (x))}{\mathrm{d} x} \mathrm{d} x.
$$

下面我们通过一些例子来体会一下一阶微分的形式不变性的灵活应用.

例6.4.6 设

$$
y = \frac {x - a}{1 - a x} \quad (| a | <   1).
$$

证明: 当  $|x| < 1$  时,

$$
\frac {\mathrm{d} y}{1 - y ^ {2}} = \frac {\mathrm{d} x}{1 - x ^ {2}}.
$$

证明 一方面直接计算 $y$ 的微分, 有

$$
\mathrm{d} y = \frac {1 - a ^ {2}}{(1 - a x) ^ {2}} \mathrm{d} x.
$$

另一方面

$$
1 - y ^ {2} = 1 - \left(\frac {x - a}{1 - a x}\right) ^ {2} = \frac {(1 - a ^ {2}) (1 - x ^ {2})}{(1 - a x) ^ {2}},
$$

所以有

$$
(1 - y ^ {2}) \mathrm{d} x = \frac {(1 - a ^ {2}) (1 - x ^ {2})}{(1 - a x) ^ {2}} \mathrm{d} x = (1 - x ^ {2}) \mathrm{d} y.
$$

即

$$
\frac {\mathrm{d} y}{1 - y ^ {2}} = \frac {\mathrm{d} x}{1 - x ^ {2}}.
$$

这是一个形式上关于 $x$ 和 $y$ 很对称的微分关系, 在双曲几何等领域有重要作用.

例 6.4.7 设  $x \geqslant 0, y \geqslant 0,$

$$
x ^ {2} = 4 y ^ {2} + 4 y ^ {4}.
$$

证明:

$$
\frac {\mathrm{d} x}{\sqrt {1 + x ^ {2}}} = \frac {2 \mathrm{d} y}{\sqrt {1 + y ^ {2}}}.
$$

证明 由给定的关系式知

$$
x = 2 y \sqrt {1 + y ^ {2}}, \quad \sqrt {1 + x ^ {2}} = 1 + 2 y ^ {2}.
$$

另一方面, 对关系式两边微分, 有

$$
x \mathrm{d} x = 4 (y + 2 y ^ {3}) \mathrm{d} y = 4 y (1 + 2 y ^ {2}) \mathrm{d} y,
$$

故有

$$
2 y \sqrt {1 + y ^ {2}} \mathrm{d} x = 4 y (1 + 2 y ^ {2}) \mathrm{d} y = 4 y \sqrt {1 + x ^ {2}} \mathrm{d} y.
$$

即

$$
\frac {\mathrm{d} x}{\sqrt {1 + x ^ {2}}} = \frac {2 \mathrm{d} y}{\sqrt {1 + y ^ {2}}}.
$$

## 习题 6.4

1. 设 $x^{y} = y^{x}$ ($x > 0$, $y > 0$). 证明: $y(x \ln y - y) \mathrm{d}x = x(y \ln x - x) \mathrm{d}y$.
2. 证明: 如果 $y = \frac{x - a}{1 + ax}$，则 $\frac{\mathrm{d}x}{1 + x^2} = \frac{\mathrm{d}y}{1 + y^2}$.
3. 设 $xy = -1$. 证明: $\frac{\mathrm{d}y}{\sqrt{1 + y^4}} = \frac{\mathrm{d}x}{\sqrt{1 + x^4}}$.

4. 证明四次代数曲线 $x^{2} + y^{2} + x^{2}y^{2} = 1$ 满足微分方程 $\frac{\mathrm{dy}}{\sqrt{1 - y^4}} = \frac{\pm\mathrm{dx}}{\sqrt{1 - x^4}}.$
5. 证明四次代数曲线 $x^{2} + y^{2} + c^{2}x^{2}y^{2} = c^{2} + 2xy\sqrt{1 - c^{4}}$ (其中 $c$ 是常数) 满足微分方程 $\frac{\mathrm{dy}}{\sqrt{1 - y^4}} = \frac{\mathrm{dx}}{\sqrt{1 - x^4}}.$
6. 证明五次代数曲线 $(y^{4} - 2y^{2} - 1)x + y^{4} + 2y^{2} - 1 = 0$ 满足微分方程 $\frac{\mathrm{d}x}{\sqrt{1 - x^4}} = \frac{2\mathrm{dy}}{\sqrt{1 - y^4}}.$

(注 验证这些看起来很神奇的关系式成立是不难的, 但显然发现这些关系式应该是一件不平凡的事. 这类问题在经典的微积分发展过程中曾经起到过很重要的作用. 上述关系式中涉及的有关椭圆积分的问题, 等式两端的原函数都是积不出来的, 但它们之间的关系竟然有隐式解, 而且还是代数曲线.)

## 6.5 高阶导数

前面我们曾用质点位移函数 $s(t)$ 的导数 $s'(t)$ 来描述作直线变速运动的质点在 $t_0$ 时刻的瞬时速度. 它刻画的是路程 $s(t)$ 关于 $t$ 的变化率, 即 $s'(t)$. 在不同的点, 质点可能有不同的瞬时速度 $s'(t)$. 如果我们进一步研究瞬时速度的变化率, 那么物理上我们知道这个变化率称为质点的加速度, 而数学上则自然而然地称之为关于路程函数 $s(t)$ 的二阶导数 $(s'(t))'$. 完全类似地, 我们也可以按照 Leibniz 的几何模型来看这个问题: 对于平面曲线 $y = f(x)$, 它的一阶导数 $f'(x)$ 表示曲线上自变量为 $x$ 对应点处的切线斜率 $f'(x)$. 如果我们感兴趣曲线在不同点切线斜率的变化的快慢, 那么本质上我们遇到了和质点运动的加速度同样的数学问题, 即 $f(x)$ 的二阶导数 $(f'(x))'$. 比如, 直观告诉我们 $y = x$ 在不同点处的斜率相同, 而 $y = x^2$ 的斜率随着 $x$ 的增大而增大. 关于切线变化率的几何意义, 我们在后面适当的时候会作专门的讨论.

## 6.5.1 高阶导数的定义

下面我们给出二阶导数的定义. 根据一阶导数的定义, 如果一个函数在某点处可导, 则该函数不但要在该点有定义, 而且在包含该点的某邻域内都要有定义. 换句话说, 函数仅在一点有定义是不能定义该点导数的. 因此, 为了考虑函数 $f'(x)$ 在点 $x_0$ 处的导数, 必须要求函数 $f'(x)$ 在包含点 $x_0$ 的某邻域内有定义, 即 $f(x)$ 不能仅仅在点 $x_0$ 处可导, 而应该在包含点 $x_0$ 的某邻域内 (处处) 可导.

定义 6.5.1 设函数 $y = f\left( x\right)$ 在点 ${x}_{0}$ 附近的一个邻域内每一点可导,如果极限

$$
\lim _ {x \to x _ {0}} \frac {f ^ {\prime} (x) - f ^ {\prime} (x _ {0})}{x - x _ {0}} = A \tag {6.5.1}
$$

存在且有限, 则称 $f(x)$ 在点 $x_0$ 处二阶可导 (或二次可导), 记为

$$
A = f ^ {\prime \prime} (x _ {0}) = (f ^ {\prime}) ^ {\prime} (x _ {0}),
$$

或者

$$
y ^ {\prime \prime} = \frac {\mathrm{d} ^ {2} y}{\mathrm{d} x ^ {2}} = \frac {\mathrm{d}}{\mathrm{d} x} \Big (\frac {\mathrm{d} y}{\mathrm{d} x} \Big) \Big | _ {x = x _ {0}}, \quad \frac {\mathrm{d} ^ {2} f (x)}{\mathrm{d} x ^ {2}} = \frac {\mathrm{d}}{\mathrm{d} x} \Big (\frac {\mathrm{d} f (x)}{\mathrm{d} x} \Big) \Big | _ {x = x _ {0}}.
$$

类似地, 我们可以归纳定义函数 $f(x)$ 的三阶导数, $f'''(x) = (f''(x))'$, 以至 $f(x)$ 的 $n$ 阶导数. $f(x)$ 的 $n$ 阶导数定义为 $f(x)$ 的 $n - 1$ 阶导数的导数. 习惯上, 常用符号 $f^{(n)}(x)$ 或 $\frac{\mathrm{d}^n f(x)}{\mathrm{d}x^n}$ 表示, 尤其是当 $n \geqslant 4$ 时.

例6.5.1 设 $y = x^3$ ，求 $y^{(n)}$

解 容易计算出

$$
y ^ {\prime} = 3 x ^ {2}, \quad y ^ {\prime \prime} = (y ^ {\prime}) ^ {\prime} = 6 x, \quad y ^ {\prime \prime \prime} = 6, \quad y ^ {(n)} = 0 (n \geqslant 4).
$$

更一般地, 对于函数 $y = x^{k} (k \in \mathbb{N})$, 则当 $n \leqslant k$ 时, 有

$$
y ^ {(n)} = k (k - 1) \dots (k - n + 1) x ^ {k - n}, \qquad \text {特别地,} \quad y ^ {(k)} = k!.
$$

而当 $n > k$ 时, 有 $y^{(n)} = 0$.

在给出更多的常见函数的高阶导数之前, 我们强调一下用定义求高阶导数的重要性, 尤其对于分段定义的函数.

例6.5.2 设

$$
f (x) = \left\{ \begin{array}{l l} x ^ {2}, & x \in \mathbb {Q}, \\ - x ^ {2}, & x \not \in \mathbb {Q}. \end{array} \right.
$$

试讨论 $f(x)$ 在 $x = 0$ 处二阶导数的存在性.

解 若要考虑 $f''(0)$ 的存在性, 则必须先考虑 $f'(x)$. 根据 $f(x)$ 的具体情况, 这包括两种情况: $x = 0$ 处的导数和 $x \neq 0$ 处的导数.

首先, 根据定义可知 $f(x)$ 在 $x = 0$ 处可导, 且 $f'(0) = 0$. 而对于 $x \neq 0$, 显然 $f(x)$ 在该点处不连续, 因此 $f(x)$ 在 $x \neq 0$ 处不可导. 即在 $x = 0$ 的任何一个邻域内, $f'(x)$ 仅在 $x = 0$ 处有定义, 故 $f''(x)$ 在 $x = 0$ 处不存在.

例6.5.3 设

$$
f (x) = \left\{ \begin{array}{l l} x ^ {3} \sin \frac {1}{x}, & x \neq 0, \\ 0, & x = 0. \end{array} \right.
$$

试讨论 $f(x)$ 在 $x = 0$ 处二阶导数的存在性.

解 我们先考察 $f'(x)$ 的情况. 根据导数的定义, 函数在 $x = 0$ 处的导数

$$
f ^ {\prime} (0) = \lim _ {\Delta x \to 0} \frac {f (\Delta x) - f (0)}{\Delta x} = \lim _ {\Delta x \to 0} (\Delta x) ^ {2} \sin \frac {1}{\Delta x} = 0.
$$

在  $x \neq 0$  处  $f(x)$  是初等函数, 其导数为

$$
f ^ {\prime} (x) = 3 x ^ {2} \sin \frac {1}{x} - x \cos \frac {1}{x}.
$$

所以  $f(x)$  满足二阶导数定义的必要条件之一: 在 x=0 的某邻域内每一点均可导.

为了计算 $f(x)$ 在 $x = 0$ 处的二阶导数, 需要考虑极限

$$
\lim _ {\Delta x \to 0} \frac {f ^ {\prime} (\Delta x) - f ^ {\prime} (0)}{\Delta x} = \lim _ {\Delta x \to 0} \left(3 \Delta x \sin \frac {1}{\Delta x} - \cos \frac {1}{\Delta x}\right).
$$

显然, 该极限不存在. 因此虽然 $f'(x)$ 在 $x = 0$ 的某邻域内有定义, 但 $f''(x)$ 在 $x = 0$ 处不存在.

作为对比, 读者可以验证函数

$$
f (x) = \left\{ \begin{array}{l l} x ^ {4} \sin \frac {1}{x}, & x \neq 0, \\ 0, & x = 0. \end{array} \right.
$$

在 x = 0 处二阶可导但三阶不可导.

例6.5.4 考察函数

$$
f (x) = \left\{ \begin{array}{l l} {k _ {1} x ^ {2},} & {x \leqslant 0,} \\ {k _ {2} x ^ {2},} & {x \geqslant 0,} \end{array} \right. \text {其中} k _ {1}, k _ {2} \in \mathbb {R}, k _ {1} \neq k _ {2} \tag {6.5.2}
$$

在 x = 0 处二阶导数的存在性.

解 首先从定义可知该函数在 $x = 0$ 处一阶可导, 且导数 $f'(0) = 0$. 当 $x \neq 0$ 时, 有

$$
f ^ {\prime} (x) = \left\{ \begin{array}{l l} 2 k _ {1} x, & x <   0, \\ 2 k _ {2} x, & x > 0. \end{array} \right.
$$

由于

$$
\lim _ {x \to 0 ^ {-}} \frac {f ^ {\prime} (x) - f ^ {\prime} (0)}{x - 0} = \lim _ {x \to 0 ^ {-}} \frac {2 k _ {1} x}{x} = 2 k _ {1},
$$

$$
\lim _ {x \to 0 ^ {+}} \frac {f ^ {\prime} (x) - f ^ {\prime} (0)}{x - 0} = \lim _ {x \to 0 ^ {+}} \frac {2 k _ {2} x}{x} = 2 k _ {2} \neq 2 k _ {1},
$$

因此  $f''(x)$  在 x = 0 处不存在.

对照一下例 6.1.4 可以发现, 上例中的函数是一个分段抛物线, 在 x = 0 处看起来连续、一阶光滑 (一阶可导), 但它的导函数在 x = 0 处出现了尖点, 从而使得  $f'(x)$  不

再可导了. 又比如函数

$$
f (x) = \left\{ \begin{array}{l l} x ^ {4}, & x \leqslant 0, \\ 0, & x \geqslant 0, \end{array} \right.
$$

可以证明 $f'''(x)$ 存在, 但在 $x = 0$ 处已经出现由折线

$$
g (x) = f ^ {\prime \prime \prime} (x) = \left\{ \begin{array}{l l} 2 4 x, & x <   0, \\ 0, & x > 0 \end{array} \right.
$$

产生的尖点了. 所以 $f$ 在 $x = 0$ 处四阶导数不存在.

上面的三个例子为我们提供了二阶导数不存在的三种典型情况: 例 6.5.2 中的函数仅在 $x = 0$ 处有一阶导数, 在其他点函数本身都不连续更不可导; 例 6.5.3 中的函数虽然在 $x = 0$ 的某邻域内每点导数都存在, 但导函数不连续; 而例 6.5.4 中的函数每一点导数都存在, 导函数也连续, 但导函数在某点不再可导.

另外, 例 6.5.4 中的函数给我们一种强烈的暗示, 就是该函数在 x = 0 处的单侧二阶导数都存在, 只是两者不等. 因此, 有兴趣的读者可以就单侧高阶导数的定义和性质开展讨论.

事实上, 类似于一阶导数的多种推广, 读者也可以讨论高阶导数的几种推广, 比如单侧导数、Schwarz 型导数、Dini 导数等, 在此不再一一赘述.

犹如几类基本初等函数的一阶导数的计算和结论在整个数学分析的学习中非常重要, 同样, 很多初等函数的高阶导数也格外重要, 值得重视. 下面我们给出更多的例子, 目的在于熟悉这些函数的高阶导数, 而推导过程较为简捷. 高阶导数更多的计算方法, 在后续章节比如在 L'Hôpital 法则和 Taylor 展开式章节中, 还会有进一步的讨论.

例6.5.5 计算下列函数的 $n$ 阶导数 $y^{(n)}$:

$$
y = \mathrm{e} ^ {a x}, \quad y = \ln (1 + x), \quad y = \sin x, \quad y = \cos x, \quad y = \arctan x.
$$

解 对于 $y = \mathrm{e}^{ax}$ ，有

$$
y ^ {\prime} = a \mathrm{e} ^ {a x}, \quad y ^ {\prime \prime} = a ^ {2} \mathrm{e} ^ {a x}, \quad y ^ {(n)} = a ^ {n} \mathrm{e} ^ {a x}.
$$

对于 $y = \ln (1 + x)$ ，有

$$
y ^ {\prime} = \frac {1}{1 + x}, \quad y ^ {\prime \prime} = \frac {- 1}{(1 + x) ^ {2}}, \quad y ^ {\prime \prime \prime} = \frac {2 !}{(1 + x) ^ {3}}.
$$

不难归纳证明, 对于  $n \geqslant 1$ ,

$$
y ^ {(n)} = (- 1) ^ {n - 1} \frac {(n - 1) !}{(1 + x) ^ {n}}, \text {这里约定} 0! = 1.
$$

对于 $y = \sin x$ ，有

$$
y ^ {\prime} = \cos x, \quad y ^ {\prime \prime} = - \sin x, \quad y ^ {\prime \prime \prime} = - \cos x, \quad y ^ {(4)} = \sin x = y.
$$

我们看到  $\sin x$  的四阶导数又循环回到函数本身了, 故可以写出下面的关系:

$$
\sin^ {(n)} x = \sin \left(x + \frac {n \pi}{2}\right).
$$

同理可得

$$
\cos^ {(n)} x = \cos \left(x + \frac {n \pi}{2}\right).
$$

对于 $y = \arctan x$ ，有

$$
y ^ {\prime} = \frac {1}{1 + x ^ {2}} = \frac {1}{1 + \tan^ {2} y} = \cos^ {2} y = \cos y \sin \left(y + \frac {\pi}{2}\right).
$$

所以等式两端求导, 有

$$
y ^ {\prime \prime} = - 2 \cos y \sin y \cdot y ^ {\prime} = \cos^ {2} y \cdot \sin 2 \left(y + \frac {\pi}{2}\right).
$$

可以归纳证明

$$
y ^ {(n)} = (n - 1)! \cos^ {n} y \cdot \sin n \left(y + \frac {\pi}{2}\right).
$$

在结束本段之前, 我们引入一个重要的函数类—— $C^{k}$ 函数类.

定义 6.5.2( $C^{k}$ 函数类) 设 I 是 R 中一区间, f 为定义在 I 上的函数. 如果 $\forall x \in I$, f 在点 x 处 k 阶导数存在且连续, 则称 f 为 I 上的 $C^{k}$ 函数, 记为 $f \in C^{k}(I)$. I 上的连续函数全体记为 $C^{0}(I)$. 如果对任意 $k \geqslant 0$, f 均为 $C^{k}$ 函数, 则称 f 为无限次可微函数或无穷次光滑函数, 记为 $f \in C^{\infty}(I)$. 特别地, 如果 I = R, 有相应的 $f \in C^{k}(\mathbb{R})$.

## 6.5.2 高阶导数的求导法则

函数的高阶导数的计算也有相应的运算法则, 结构上类似于一阶导数的求导法则, 即包括四则运算下的求导法则、复合函数的求导法则、反函数的求导法则、参数方程的求导法则以及隐函数的求导法则等情况.

首先, 两个函数的四则运算下的高阶导数的计算, 成立如下结论: 两个函数和差的高阶导数具有线性叠加性, 乘积的高阶导数满足 Leibniz 公式, 而两个函数商的高阶求导不易写出具体表达式.

定理 6.5.1 设函数 $u\left( x\right) ,v\left( x\right)$ 在 ${x}_{0}$ 点处均 $n$ 次可导,则下面运算法则成立:

(1) $(u\pm v)^{(n)} = u^{(n)}\pm v^{(n)};$
(2) $(u\cdot v)^{(n)} = \sum_{k = 0}^{n}\mathrm{C}_n^k u^{(n - k)}\cdot v^{(k)}$ (Leibniz公式),

其中 $u^{(0)} = u, v^{(0)} = v.$

证明 我们只证明函数乘积的 Leibniz 公式, 和与差的情况请读者自己补充. 为此, 考虑数学归纳法.

首先, 当 $n = 1$ 时, 结论显然成立. 假设当 $n > 1$ 时, Leibniz 公式成立, 往证 $n + 1$ 时也成立. 事实上, 我们有

$$
\begin{array}{l} (u \cdot v) ^ {(n + 1)} = ((u \cdot v) ^ {(n)}) ^ {\prime} = \sum_ {k = 0} ^ {n} \mathrm{C} _ {n} ^ {k} \left(u ^ {(n - k)} \cdot v ^ {(k)}\right) ^ {\prime} \\ = \sum_ {k = 0} ^ {n} \mathrm{C} _ {n} ^ {k} \left(u ^ {(n - k + 1)} \cdot v ^ {(k)} + u ^ {(n - k)} \cdot v ^ {(k + 1)}\right) \\ = \mathrm{I} + \mathrm{II}, \\ \end{array}
$$

其中

$$
\mathrm{I} := \sum_ {k = 0} ^ {n} \mathrm{C} _ {n} ^ {k} u ^ {(n - k + 1)} \cdot v ^ {(k)}, \qquad \mathbb {I} := \sum_ {\ell = 0} ^ {n} \mathrm{C} _ {n} ^ {\ell} u ^ {(n - \ell)} \cdot v ^ {(\ell + 1)}.
$$

在Ⅱ中, 令 $\ell = k - 1$, 可得

$$
\mathbb {I} = \sum_ {k = 1} ^ {n + 1} \mathrm{C} _ {n} ^ {k - 1} u ^ {(n + 1 - k)} \cdot v ^ {(k)}.
$$

继续前面的计算, 有

$$
\begin{array}{l} (u \cdot v) ^ {(n + 1)} = \mathrm{I} + \mathrm{II} \\ = u ^ {(n + 1)} \cdot v + \sum_ {k = 1} ^ {n} \left(\mathrm{C} _ {n} ^ {k} + \mathrm{C} _ {n} ^ {k - 1}\right) u ^ {(n + 1 - k)} \cdot v ^ {(k)} + u \cdot v ^ {(n + 1)} \\ = \sum_ {k = 0} ^ {n + 1} \mathrm{C} _ {n + 1} ^ {k} u ^ {(n + 1 - k)} \cdot v ^ {(k)}. \\ \end{array}
$$

其中最后一步用到了恒等式

$$
\mathrm{C} _ {n} ^ {k} + \mathrm{C} _ {n} ^ {k - 1} = \mathrm{C} _ {n + 1} ^ {k}.
$$

注意, 两个函数商的二阶导数的计算可以按照一阶导数的法则进行,

$$
\left(\frac {g}{f}\right) ^ {\prime \prime} = \frac {g ^ {\prime \prime} f ^ {2} - f ^ {\prime \prime} f g - 2 f ^ {\prime} g ^ {\prime} f + 2 f ^ {2} g}{f ^ {3}},
$$

在满足可以形式运算的必要条件下, 表达式已经比较烦琐了.

(1) 复合函数高阶导数的求导法则 关于复合函数高阶导数的求导法则, 可以按照下面的运算法则逐步计算.

设 $f$ 和 $g$ 都是 $n$ 阶可导函数, 且 $g$ 与 $f$ 可以作复合运算 $g(f)$. 那么其复合函数 $h = g(f)$ 也是 $n$ 阶可导的, 且可以按如下方法计算:

$$
h ^ {\prime} (x) = g ^ {\prime} (f) f ^ {\prime} (x);
$$

$$
h ^ {\prime \prime} (x) = (h ^ {\prime}) ^ {\prime} = g ^ {\prime \prime} (f) f ^ {2} + g ^ {\prime} (f) f ^ {\prime \prime};
$$

$$
h ^ {\prime \prime \prime} (x) = \left(h ^ {\prime \prime}\right) ^ {\prime} = g ^ {\prime \prime \prime} (f) f ^ {\prime 3} + 3 g ^ {\prime \prime} (f) f ^ {\prime} f ^ {\prime \prime} + g ^ {\prime} (f) f ^ {\prime \prime \prime}.
$$

更高阶的导数可以类似计算, 也可以得到一个与 Leibniz 公式类似的表达式.

(2) 反函数高阶导数的求导法则 参见反函数的一阶求导法则推论 6.3.6.

设函数 $y = f(x)$ 在区间 $(a, b)$ 内严格单调、二阶可导且有非零的导数，那么它的反函数 $x = g(y)$ 在区间 $(\alpha, \beta)$ 内可导，其中

$$
\alpha = \min \left\{x (a ^ {+}), x (b ^ {-}) \right\}, \quad \beta = \max \left\{x (a ^ {+}), x (b ^ {-}) \right\}.
$$

我们已经知道

$$
\frac {\mathrm{d} g (y)}{\mathrm{d} y} = \frac {1}{f ^ {\prime} (x)}.
$$

对此式再次求导, 得

$$
\frac {\mathrm{d} ^ {2} g (y)}{\mathrm{d} y ^ {2}} = \frac {\mathrm{d}}{\mathrm{d} y} \left(\frac {1}{f ^ {\prime} (x)}\right) = \frac {\mathrm{d}}{\mathrm{d} x} \left(\frac {1}{f ^ {\prime} (x)}\right) \frac {\mathrm{d} x}{\mathrm{d} y} = - \frac {f ^ {\prime \prime} (x)}{f ^ {\prime 2} (x)} \cdot \frac {1}{f ^ {\prime} (x)} = - \frac {f ^ {\prime \prime} (x)}{f ^ {\prime 3} (x)}.
$$

反函数更高阶的导数可以类似讨论.

(3) 参数式表示的函数的高阶导数求导法则 设函数 $\varphi(t)$ 和 $\psi(t)$ 在区间 $I = (a, b)$ 内均二阶可导, $\varphi(t)$ 在 $I$ 内严格单调且有非零的导数, $\varphi'(t) \neq 0$. 因此 $\varphi(t)$ 在某区间 $J$ 上有可导的反函数 $t = \varphi^{-1}(x), x \in J$, 其中 $J$ 的定义可参见反函数求导法则中的描述, 而且有 $\frac{\mathrm{d}t}{\mathrm{d}x} = \frac{1}{\varphi'(t)}$.

现在我们计算由参数表达式

$$
x = \varphi (t), \qquad y = \psi (t), \qquad t \in I,
$$

所定义的函数

$$
y = \psi (t) = \psi (\varphi^ {- 1} (x)) = f (x), \quad x \in J
$$

的二阶导数.

我们知道, 该函数的一阶导数由下式给出:

$$
\frac {\mathrm{d} y}{\mathrm{d} x} = f ^ {\prime} (x) = \frac {\psi^ {\prime} (t)}{\varphi^ {\prime} (t)}.
$$

因此

$$
\begin{array}{l} \frac {\mathrm{d} ^ {2} y}{\mathrm{d} x ^ {2}} = \frac {\mathrm{d}}{\mathrm{d} x} \left(\frac {\psi^ {\prime} (t)}{\varphi^ {\prime} (t)}\right) = \frac {\mathrm{d}}{\mathrm{d} t} \left(\frac {\psi^ {\prime} (t)}{\varphi^ {\prime} (t)}\right) \cdot \frac {\mathrm{d} t}{\mathrm{d} x} \\ = \frac {\psi^ {\prime \prime} (t) \varphi^ {\prime} (t) - \psi^ {\prime} (t) \varphi^ {\prime \prime} (t)}{(\varphi^ {\prime} (t)) ^ {2}} \cdot \frac {1}{\varphi^ {\prime} (t)} \\ = \frac {\psi^ {\prime \prime} (t) \varphi^ {\prime} (t) - \psi^ {\prime} (t) \varphi^ {\prime \prime} (t)}{(\varphi^ {\prime} (t)) ^ {3}}. \\ \end{array}
$$

需要提醒的是, 参数形式下函数的二阶导数 $\frac{\mathrm{d}^2y}{\mathrm{d}x^2}$ 的最终表达式并不是 $\frac{\psi''(t)}{\varphi''(t)}$. 同时也注意分母不是 $(\varphi'(t))^2$ 而是 $(\varphi'(t))^3$, 这一点很容易出现错误.

有兴趣的读者可以尝试推导一下参数形式下三阶甚至更高阶导数的计算.

(4) 隐函数的高阶导数的求导法则 我们通过一个具体例子来展示一下隐函数方程的高阶导数的计算, 对于隐函数可否确定一个函数关系以及可导的一般性条件, 我们将在多元函数章节详细讨论.

例 6.5.6 设函数  $y = y(x)$  由隐函数方程  $x^{2} + y^{2} = 1 (y > 0)$  给出, 试求  $y'''$ .

解 由一阶微分的方法, 得

$$
x \mathrm{d} x + y \mathrm{d} y = 0.
$$

所以

$$
y ^ {\prime} = - \frac {x}{y}.
$$

在上式两端分别求导, 可得

$$
y ^ {\prime \prime} = - \frac {\mathrm{d}}{\mathrm{d} x} \left(\frac {x}{y}\right) = - \frac {y - x y ^ {\prime}}{y ^ {2}} = - \frac {1}{y ^ {2}} \left(y + \frac {x ^ {2}}{y}\right) = - \frac {1}{y ^ {3}}.
$$

进一步有

$$
y ^ {\prime \prime \prime} = \frac {3 y ^ {\prime}}{y ^ {4}} = - \frac {3 x}{y ^ {5}}.
$$

## 6.5.3 高阶微分

若函数 $y = f(x)$ 在区间 $(a, b)$ 内可微, 则有微分关系 $\mathrm{dy} = f'(x) \mathrm{dx}$, 其中 $f'(x)$ 仍然为 $x$ 的函数, 而 $\mathrm{dx}$ 是一个与 $x$ 无关的量. 因此, 我们仍然可以把 $\mathrm{dy}$ 视为 $x$ 的函数. 如果 $\mathrm{dy}$ 在某点 $x$ 处可微, 那么我们可以继续计算它的一阶微分 $\mathrm{d}(\mathrm{dy})$. 为此, 取自变量的改变量 $\Delta x$ 与原来的改变量相同, 即 $\Delta x = \mathrm{dx}$, 并称为 $y = f(x)$ 的二阶微分, 记为 $\mathrm{d}^2 y$, 即

$$
\mathrm{d} ^ {2} y = \mathrm{d} (\mathrm{d} y) = (f ^ {\prime} (x) \mathrm{d} x) ^ {\prime} \mathrm{d} x = f ^ {\prime \prime} (x) \mathrm{d} x \mathrm{d} x = f ^ {\prime \prime} (x) (\mathrm{d} x) ^ {2} = f ^ {\prime \prime} (x) \mathrm{d} x ^ {2},
$$

其中 $\mathrm{dx}^2 = (\mathrm{dx})^2$

需要注意的是这里的 $\mathrm{dx}$ 与 $x$ 无关, 所以 $(\mathrm{dx})' = 0$, 另外记号 $\mathrm{dx}^2$ 也有点怪异, 它表示 $(\mathrm{dx})^2$ 而不是 $x^2$ 的微分, 如果要表达 $x^2$ 的微分, 必要时采用符号 $\mathrm{d}(x^2) = 2x\mathrm{dx}$.

类似地我们可以定义函数的三阶微分, 即如果函数 $y = f(x)$ 的二阶微分 $\mathrm{d}^2 y$ 在点 $x \in (a, b)$ 处可微, 那么我们就可以计算它的一阶微分 $\mathrm{d}(\mathrm{d}^2 y)$, 特别地, 我们取自变量 $x$ 的改变量与原来的改变量相同, 即 $\Delta x = \mathrm{d}x$, 并称为 $y = f(x)$ 的三阶微分, 记为 $\mathrm{d}^3 y$,

即

$$
\mathrm{d} ^ {3} y = \mathrm{d} (\mathrm{d} ^ {2} y) = f ^ {\prime \prime \prime} (x) (\mathrm{d} x) ^ {3} = f ^ {\prime \prime \prime} (x) \mathrm{d} x ^ {3},
$$

其中 $\mathrm{dx}^3 = (\mathrm{dx})^3$

不难看出, 应用数学归纳法, 当 $\mathrm{d}^{n-1}y$ 在点 $x \in (a, b)$ 处可微时, 我们可以作 $\mathrm{d}^{n-1}y$ 的一阶微分, 并取 $x$ 的改变量与原来的改变量相同, 即 $\Delta x = \mathrm{d}x$, 记为 $\mathrm{d}^n y = \mathrm{d}(\mathrm{d}^{n-1}y)$, 称为 $y = f(x)$ 在点 $x$ 处的 $n$ 阶微分. 即

$$
\mathrm{d} ^ {n} y = \mathrm{d} (\mathrm{d} ^ {n - 1} y) = (f ^ {(n - 1)} (x) \mathrm{d} x ^ {n - 1}) ^ {\prime} \mathrm{d} x = f ^ {(n)} (x) \mathrm{d} x ^ {n - 1} \mathrm{d} x = f ^ {(n)} (x) \mathrm{d} x ^ {n},
$$

其中 $\mathrm{dx}^n = (\mathrm{dx})^n$

从上述表达式可以看出高阶微分与高阶导数的关系

$$
\frac {\mathrm{d} ^ {n} y}{\mathrm{d} x ^ {n}} = y ^ {(n)} = f ^ {(n)} (x).
$$

由此也可看出, 计算高阶微分和计算高阶导数本质上的相同之处. 因此, 关于函数 $u(x)$ 和 $v(x)$ 高阶导数的运算法则也同样适用于高阶微分, 我们有下面的定理:

定理 6.5.2 设函数 $u\left( x\right)$ 和 $v\left( x\right)$ 在点 $x$ 处存在 $n$ 阶微分,则下面的关系式成立:

(1) $\mathrm{d}^n (u\pm v) = \mathrm{d}^nu\pm \mathrm{d}^nv;$
(2) $\mathrm{d}^n (u\cdot v) = \sum_{k = 0}^{n}\mathrm{C}_n^k\mathrm{d}^{n - k}u\cdot \mathrm{d}^k v$ (Leibniz公式),

其中 $\mathrm{d}^0 u = u,\quad \mathrm{d}^0 v = v.$

读者可以补充两个函数商的二阶微分表示.

关于复合函数的微分, 我们知道复合函数的一阶微分具有一个极其重要的性质, 即一阶微分的形式不变性. 我们需要强调的是, 对于复合函数的高阶微分形式不变性不再成立.

事实上, 设 $y = f(u)$, 如果 $u$ 是自变量, 则有 $\mathrm{d}^2 y = f''(u) \mathrm{d}^2 u$; 但是如果 $u$ 是中间变量, 当 $u = g(x)$ 时, 一阶微分给出

$$
\mathrm{d} f = f ^ {\prime} (u) \mathrm{d} u = f ^ {\prime} (u) g ^ {\prime} (x) \mathrm{d} x,
$$

而二阶微分有

$$
\mathrm{d} ^ {2} f = \mathrm{d} (f ^ {\prime} (u) \mathrm{d} u) = f ^ {\prime \prime} (u) (g ^ {\prime} (x)) ^ {2} \mathrm{d} x ^ {2} + f ^ {\prime} (u) g ^ {\prime \prime} (x) \mathrm{d} x ^ {2} = f ^ {\prime \prime} (u) \mathrm{d} u ^ {2} + f ^ {\prime} (u) \mathrm{d} ^ {2} u.
$$

等式最右端多出一项 $f'(u)\mathrm{d}^2 u$ 所以当 $\mathrm{d}^2 u\neq 0$ ，即 $g''(x)\neq 0$ 时，二阶微分已经不具有形式不变性了.当然，当 $u$ 是自变量时(本质上是 $u = x$ )， $g^{\prime \prime}(x) = 0$ ，就又回到了$\mathrm{d}^2 y = f''(u)\mathrm{d}u^2$ 了.

## 习题 6.5

1. 求下列函数指定阶的导数:

(1) $f(x) = \mathrm{e}^{x}\cos x$ ，求 $f^{(5)}$

(2) $f(x)=x^{2}\ln x+x\ln^{2}x,$ 求 $f'';$

(3) $f(x) = x^{2}\mathrm{e}^{x}$, 求 $f^{(10)}$;

(4) $f(x) = x^{5}\cos x$ ，求 $f^{(50)}$

2. 通过对  $(1+x)^{n}$  求导并利用二项式定理证明:

(1) $\sum_{k=0}^{n} C_n^k k = n 2^{n-1}$;

(2) $\sum_{k=0}^{n} C_n^k k^2 = n(n+1) 2^{n-2}$.

3. 证明: 函数 $y = \cos (n\arccos x)$ 满足

$$
\frac {n \mathrm{d} x}{\sqrt {1 - x ^ {2}}} = \frac {\mathrm{d} y}{\sqrt {1 - y ^ {2}}},
$$

$$
(1 - x ^ {2}) y ^ {\prime \prime} - x y ^ {\prime} + n ^ {2} y = 0.
$$

4. 证明: 任一圆周 $(x - a)^{2} + (y - b)^{2} = c^{2}$ 上的任意一点 $(x, y), y \neq b$ 处的导数、二阶导数和三阶导数都满足关系式:

(1) $\frac{y''}{(\sqrt{1 + y'^2})^3} = c$ ( $c$ 为常数);

(2) $y'''(1+(y')^{2})=3y'(y'')^{2}$.

5. 函数 $y = f(x)$ 的极坐标表示为 $r^2 = \cos 2\theta \left(0 < \theta < \frac{\pi}{4}\right)$，计算 $\frac{\mathrm{d}^2y}{\mathrm{d}x^2}$.

6. 设 $f(x) = x \ln (2^{\frac{1}{x}} + 3^{\frac{1}{x}})$, $x > 0$. 证明: $f'(x) > 0$, $f''(x) > 0$.

7. 设 $P(x)$ 是有 $n$ 个单根的 $n$ 次多项式. 证明: $P'(x)^2 \geqslant P(x)P''(x)$.

8.  $\forall n \geqslant 1$ , 证明下列等式成立:

(1) $(\ln x)^{(n)} = \frac{(-1)^{n - 1}(n - 1)!}{x^n}$;

(2) $(\sin^4 x + \cos^4 x)^{(n)} = 4^{n - 1}\cos \left(4x + \frac{\pi}{2} n\right)$;

(3) $(\mathrm{e}^{ax}\sin bx)^{(n)} = (a^2 +b^2)^{\frac{n}{2}}\mathrm{e}^{ax}\sin (bx + n\varphi)$, 其中 $\varphi$ 满足条件

$$
\sin \varphi = \frac {b}{\sqrt {a ^ {2} + b ^ {2}}}, \quad \cos \varphi = \frac {a}{\sqrt {a ^ {2} + b ^ {2}}}.
$$

9. 设函数 $y = f(x)$ 在点 $x$ 处三阶可导, 且 $f'(x) \neq 0$. 若 $f(x)$ 存在反函数 $x = f^{-1}(y)$, 试用 $f'(x), f''(x)$ 以及 $f'''(x)$ 表示 $(f^{-1})'''(y)$.

10. 设函数

$$
y = x ^ {\alpha} \sin \frac {1}{x ^ {\beta}} \quad (x \neq 0), \qquad y (0) = 0, \qquad \alpha , \beta \in \mathbb {R}.
$$

试讨论函数的连续性、一致连续性、L-连续性、可导性与高阶可导性.

11. 考虑习题 6.3 中的题目 14: 设  $y(x)=(x-x_{1})(x-x_{2})\cdots(x-x_{n})$ ，其中  $x_{1}, x_{2}, \cdots, x_{n}$  是 n 个两两互异的实数。又设  $\xi_{1}, \xi_{2}, \cdots, \xi_{n-1}$  是  $y'(x)=0$  的 n-1 个实根

(其存在性下一章将会讨论). 试计算并化简

$$
\sum_ {k = 1} ^ {n - 1} \frac {1}{y ^ {\prime \prime} (\xi_ {k})}.
$$

进一步, 设  $\eta_{1}, \eta_{2}, \cdots, \eta_{n-2}$  是  $y''(x) = 0$  的 n - 2 个实根, 试计算并化简

$$
\sum_ {k = 1} ^ {n - 2} \frac {1}{y ^ {\prime \prime \prime} (\eta_ {k})}.
$$

请给出更一般情况下的描述和讨论.