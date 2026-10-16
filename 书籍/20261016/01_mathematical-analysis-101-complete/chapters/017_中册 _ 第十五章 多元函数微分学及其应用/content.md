# 中册 / 第十五章 多元函数微分学及其应用

原始 PDF 第 544–618 页。

## 第十五章

## 多元函数微分学及其应用

---

240

第十五章 多元函数微分学及其应用

在上一章, 我们讨论了如何把一元函数的极限、连续等基本概念和内容推广到多元函数或映射. 从本章起, 我们将陆续把一元函数的微分和积分等概念以及相应的理论体系、思想方法、计算和应用也推广到多元函数或映射. 本章我们主要讨论微分学及其应用, 后面的章节再转向积分学.

本章大部分的内容和一元函数相应的内容平行，在结构上两者也有很多相似之处。比如，在本章我们也将讨论多元函数求导的四则运算法则、复合函数求导、高阶偏导数、链式法则、有限增量公式、一阶微分形式不变性、Taylor公式、微分的应用等；但同时我们也将特别指出一元与多元结论上本质的区别，比如多元函数关于连续与偏导数之间的逻辑关系，尤其多元函数中的隐函数存在定理、逆映射定理等几个重要的理论结果。这些结论对于深刻理解和揭示一元函数与多元函数在这些方面的差异是非常重要的，这也为后续课学习无穷元分析提供一些基本素材和案例。

## 15.1 偏导数与方向导数

我们回忆一下一元函数导数的定义: 若 $f$ 是一个一元函数, $x_0$ 是定义域中的内点, 则 $f$ 在 $x_0$ 处的导数定义为当极限 $\lim_{h\to 0}\frac{f(x_0 + h) - f(x_0)}{h}$ 存在有限时该极限的值.

对于多元函数的情形, 我们可以通过一元函数导数的定义来引入多元函数的偏导数.

定义 15.1.1 (偏导数) 设  $D \subseteq R^{n}$  是一开集,  $u = f(\boldsymbol{x}) = f(x_{1}, x_{2}, \cdots, x_{n})$  是在 D 上有定义的函数,  $\boldsymbol{x}_{0} = (x_{1}^{0}, x_{2}^{0}, \cdots, x_{n}^{0}) \in D$ . 对  $1 \leqslant i \leqslant n$ , 若一元函数

$$
\tilde {f} (x _ {i}) = f (x _ {1} ^ {0}, \dots , x _ {i - 1} ^ {0}, x _ {i}, x _ {i + 1} ^ {0}, \dots , x _ {n} ^ {0})
$$

在 $x_{i}^{0}$ 的导数 $\tilde{f}'(x_i^0)$ 存在, 则称 $f(x)$ 在 $x_0$ 处关于 $x_{i}$ 可偏导, 并称 $\tilde{f}'(x_i^0)$ 为 $f(x)$ 在 $x_0$ 关于 $x_{i}$ 的偏导数, 记为

$$
\frac {\partial f (\boldsymbol {x} _ {0})}{\partial x _ {i}}, \quad f _ {x _ {i}} (\boldsymbol {x} _ {0}), \quad \left. \frac {\partial u}{\partial x _ {i}} \right| _ {\boldsymbol {x} _ {0}}.
$$

若 $f(x)$ 在 $D$ 中的每一点关于 $x_{i}$ 都可偏导, 则将其偏导数记为

$$
\frac {\partial f (\boldsymbol {x})}{\partial x _ {i}}, \qquad f _ {x _ {i}} (\boldsymbol {x}), \qquad \frac {\partial u}{\partial x _ {i}}.
$$

可以看出, 若 $n$ 元函数 $f(\pmb{x})$ 关于每个分量都可偏导, 则 $f(\pmb{x})$ 具有 $n$ 个偏导数. 另一方面, 对每个固定的分量 $x_{i}, \frac{\partial f(\pmb{x})}{\partial x_{i}}$ 仍然是 $D$ 内的一个 $n$ 元函数. 进一步, 如果 $f_{x_i}(\pmb{x}) = \frac{\partial f(\pmb{x})}{\partial x_i}$ 关于 $x_{j}$ 仍然可偏导, 那么我们就把这样的偏导数 $\frac{\partial}{\partial x_j} \left( \frac{\partial f(\pmb{x})}{\partial x_i} \right)$ 称

---

15.1 偏导数与方向导数

241

为函数 $f(\pmb{x})$ 的二阶偏导数, 记为 $f_{x_i x_j}$ 或 $\frac{\partial^2 f(\pmb{x})}{\partial x_j \partial x_i}$. 需要注意的是, $i \neq j$ 时, $f_{x_j x_i}$ 和 $f_{x_i x_j}$ 统称为混合偏导数, 但它们是两个不同的二阶偏导数, 至于它们的值是否相等, 则是多元函数微分学中的基本问题之一, 我们在后面再加以讨论.

这样, 一个 $n$ 元函数共有 $n$ 个偏导数、$n^2$ 个二阶偏导数:

$$
\left\{\frac {\partial^ {2} f (\boldsymbol {x})}{\partial x _ {j} \partial x _ {i}} \right\} _ {1 \leqslant i, j \leqslant n},
$$

其中当 $i = j$ 时, 我们将采用记号:

$$
\frac {\partial}{\partial x _ {i}} \Big (\frac {\partial f}{\partial x _ {i}} \Big) = \frac {\partial^ {2} f}{\partial x _ {i} ^ {2}}.
$$

类似地可以定义更高阶偏导数.

定义15.1.2 给定 $n$ 元函数 $f(\pmb{x})$ ，其 $k$ 阶偏导数为

$$
f _ {x _ {i _ {1}} x _ {i _ {2}} \dots x _ {i _ {k}}} = \frac {\partial^ {k} f}{\partial x _ {i _ {k}} \partial x _ {i _ {k - 1}} \cdots \partial x _ {i _ {1}}} = \frac {\partial}{\partial x _ {i _ {k}}} \left(\frac {\partial^ {k - 1} f}{\partial x _ {i _ {k - 1}} \cdots \partial x _ {i _ {1}}}\right)
$$

必须注意, 高阶偏导数的值不但依赖于对哪些自变量求偏导, 还依赖于求偏导的次序. 以二元函数 $z = f(x, y)$ 为例, 它关于 $x$ 和 $y$ 均求二次偏导的四阶偏导数中, 就存在如下可能:

$$
f _ {x x y y}, f _ {x y x y}, f _ {y x x y}, f _ {y x y x}, f _ {y y x x}.
$$

在没有额外条件假设下,一般来说,它们可能彼此不等.后面我们还会返回到这个话题.

在具体问题讨论中, 我们常见的是二元函数和三元函数. 在不失一般性的条件下, 为了叙述和表达的简洁性, 我们经常以二元函数为主. 对于 $n = 2$, 设 $z = f(x, y)$ 在 $(x_0, y_0)$ 的某个邻域内有定义, 当 $y = y_0$ 固定不变, 而 $x$ 在 $x_0$ 处有增量 $\Delta x$ 时, 相应的函数增量为 $f(x_0 + \Delta x, y_0) - f(x_0, y_0)$. 函数 $z = f(x, y)$ 在点 $(x_0, y_0)$ 处对 $x$ 可偏导则是指极限

$$
\lim _ {\Delta x \to 0} \frac {f (x _ {0} + \Delta x , y _ {0}) - f (x _ {0} , y _ {0})}{\Delta x}
$$

存在有限, 记作 $\left.\frac{\partial z}{\partial x}\right|_{(x_0,y_0)}$, $\left.\frac{\partial f}{\partial x}\right|_{(x_0,y_0)}$, $z_x|_{(x_0,y_0)}$ 或 $f_x(x_0,y_0)$. 即

$$
f _ {x} \left(x _ {0}, y _ {0}\right) = \lim _ {\Delta x \to 0} \frac {f \left(x _ {0} + \Delta x , y _ {0}\right) - f \left(x _ {0} , y _ {0}\right)}{\Delta x}.
$$

类似地, 函数 $z = f(x, y)$ 在点 $(x_0, y_0)$ 处对 $y$ 可偏导则是指极限

$$
f _ {y} \left(x _ {0}, y _ {0}\right) = \lim _ {\Delta y \to 0} \frac {f \left(x _ {0} , y _ {0} + \Delta y\right) - f \left(x _ {0} , y _ {0}\right)}{\Delta y}
$$

存在有限.

---

242

第十五章 多元函数微分学及其应用

根据偏导数的定义, 在对某个变量求导时, 可暂时将其余变量视为常数. 因此, 偏导数的计算可以利用一元函数求导的所有法则和方法.

例 15.1.1 求  $f(x,y)=xy$  的一阶和二阶偏导数.

解 $f_{x} = y,$ $f_{y} = x,$ $f_{yx} = 1,$ $f_{xy} = 1,$ $f_{xx} = f_{yy} = 0.$

例 15.1.2 设  $abc \neq 0$ ,

$$
f (x, y) = \left\{ \begin{array}{l l} {a x + b y,} & {x = 0 \text {或} y = 0,} \\ {c,} & {\text {其他点}.} \end{array} \right.
$$

可以直接验证, 两个偏导数 $f_{x}(0,0)$ 和 $f_{y}(0,0)$ 都存在, 这是因为

$$
f _ {x} (0, 0) = \lim _ {x \to 0} \frac {f (x , 0) - f (0 , 0)}{x - 0} = \lim _ {x \to 0} \frac {a x}{x} = a.
$$

同理有 $f_{y}(0,0) = b.$

注意, 虽然函数的两个偏导数都存在, 但显然 $f(x,y)$ 在 $(0,0)$ 不连续.

例 15.1.3 设  $D(y)$  是关于 y 的 Dirichlet 函数, 求  $f(x,y)=x+D(y)$  在  $(x_{0},y_{0})=(0,0)$  处的偏导数  $\frac{\partial f}{\partial x}$  和  $\frac{\partial}{\partial y}\left(\frac{\partial f}{\partial x}\right)$ .

解 直接的计算表明

$$
\frac {\partial f}{\partial x} (0, 0) = 1, \quad \frac {\partial}{\partial y} \left(\frac {\partial f}{\partial x}\right) (0, 0) = 0.
$$

此例告诉我们, 虽然函数 $f(x, y)$ 关于 $y$ 处处不连续, 但二元函数仍然有可能关于另一个变量可偏导, 甚至有高阶偏导数, 这是多元函数与一元函数不同之处.

当然, 多元函数在某点连续一般来说逻辑上也得不到在该点可偏导的结论, 这只要把具有这种特点的一元函数看成多元函数即可. 比如 $\forall y_0, f(x,y) = g(x) = |x|$ 在 $(0,y_0)$ 关于 $x$ 就不可偏导.

我们知道, 导数是函数的变化率. 对于一元函数来说, 如果导数恒为零, 则该函数变化率为零, 即函数为常值函数. 对于多元函数来说, 我们有

命题15.1.1 设函数 $f: \mathbb{R}^n \to \mathbb{R}$ 的偏导数恒为零, 则 $f$ 为常值函数.

证明 以二元函数为例. 设 $\frac{\partial f}{\partial x} = \frac{\partial f}{\partial y} = 0$. 我们有

$$
f (x, y) - f (0, 0) = (f (x, y) - f (0, y)) + (f (0, y) - f (0, 0)).
$$

对上式右边括号中的项分别关于变量 $x$ 和 $y$ 应用一元函数的微分中值定理, 可得

$$
f (x, y) - f (0, 0) = \frac {\partial f}{\partial x} (\xi , y) (x - 0) + \frac {\partial f}{\partial y} (0, \zeta) (y - 0) = 0,
$$

即 $f(x,y)\equiv f(0,0)$

□

---

15.1 偏导数与方向导数

243

事实上, 无论从证明过程中还是从一元函数的结论中, 我们看到了更一般的结论: 如果定义在凸域上的 $n$ 元函数 $f$ 关于某一个变量的偏导数恒为零, 那么 $f$ 本质上是一个 $n - 1$ 元函数.

由一元函数导数的几何意义, 可得多元函数偏导数的几何意义. 例如二元函数 $z = f(x,y), (x,y) \in D$, 给出了 $\mathbb{R}^3$ 中的一个曲面 $S$. 设 $z_0 = f(x_0,y_0)$, 点 $P_0(x_0,y_0,z_0)$ 为曲面 $S$ 上一点. 考察曲面 $S$ 与平面 $y = y_0$ 的交线 $\Gamma$. 偏导数 $f_x(x_0,y_0)$ 即表示交线 $\Gamma$ 在 $P_0$ 点的切线斜率, 交线在 $P_0$ 点的切向量为 $(1,0,f_x(x_0,y_0))$.

同理， $f_{y}(x_0,y_0)$ 表示曲面 $S$ 与平面 $x = x_0$ 的交线 $\Sigma$ 在 $P_0$ 点的切线斜率，交线 $\Sigma$ 在 $P_0$ 点的切向量为 $(0,1,f_y(x_0,y_0))$

我们看到, 偏导数 $f_{x_i}$ 描述的是函数 $f$ 沿着 $x_i$ 轴方向的变化率. 完全类似, 我们可以考虑函数沿着任一给定方向 $\pmb{u}$ 的变化率. 具体来说, 考虑定义在开集 $D \subseteq \mathbb{R}^n$ 上的 $n$ 元函数 $z = f(\pmb{x}), \pmb{x}_0 \in D$. 在以 $\pmb{x}_0$ 为始点, 以 $\pmb{u}$ 的正向为方向向量的射线 $\ell$ 上任取一点 $\pmb{x} \in D \cap \ell$, 则有 $\pmb{x} = \pmb{x}_0 + \pmb{x} - \pmb{x}_0 = \pmb{x}_0 + h\pmb{u}, h > 0$.

定义 15.1.3 设  $z = f(x)$  是定义在开集  $D \subseteq R^{n}$  上的 n 元函数.  $x_{0} \in D$ ,  $\boldsymbol{u} = (u_{1}, u_{2}, \cdots, u_{n})$  是一个 n 维单位向量, 即  $\|u\| = 1$ . 如果极限

$$
\frac {\partial f}{\partial \boldsymbol {u}} (\boldsymbol {x} _ {0}) := \lim _ {h \to 0 ^ {+}} \frac {f (\boldsymbol {x} _ {0} + h \boldsymbol {u}) - f (\boldsymbol {x} _ {0})}{h} \tag {15.1.1}
$$

存在有限, 则称函数 $f$ 在 $\pmb{x}_0$ 处沿着方向 $\pmb{u}$ 是方向可导的, 并称该极限为函数 $f$ 在 $\pmb{x}_0$ 处沿着方向 $\pmb{u}$ 的方向导数.

我们来解释一下上述定义中, 为何要取 $\pmb{u} = (u_{1}, u_{2}, \dots, u_{n})$ 为单位向量. 事实上, 我们知道, 当初引入方向导数的目的就是考察函数沿着一个给定方向 $\pmb{u}$ 的变化情况. 但众所周知, 对于一个给定方向 $\pmb{u}$ 和任意实数 $\lambda > 0$, 向量 $\pmb{v} := \lambda \pmb{u}$ 是一个与 $\pmb{u}$ 同向的向量, 因此我们一方面有理由根据定义 (15.1.1) 计算相应的极限 $\frac{\partial f}{\partial \pmb{v}} (\pmb{x}_{0})$, 另一方面, 还希望这两个极限值 $\frac{\partial f(\pmb{x}_{0})}{\partial \pmb{u}}$ 和 $\frac{\partial f(\pmb{x}_{0})}{\partial \pmb{v}}$ 相等, 因为这样更吻合方向导数中“方向”的直觉.

我们设想一下, 假如情况并非如此, 即在极限 (15.1.1) 中不要求 $\pmb{u}$ 为单位向量, 我们分别来计算一下函数 $f$ 沿方向 $\pmb{u}$ 与沿方向 $\pmb{v}$ 给出的极限 (15.1.1). 为此, 我们计算 $f$ 沿 $\pmb{v} = \lambda \pmb{u}$ 的变化率:

$$
\begin{array}{l} \frac {\partial f (\boldsymbol {x} _ {0})}{\partial \boldsymbol {v}} = \lim _ {h \to 0 ^ {+}} \frac {f (\boldsymbol {x} _ {0} + h \boldsymbol {v}) - f (\boldsymbol {x} _ {0})}{h} \\ = \lambda \cdot \lim _ {h \rightarrow 0 ^ {+}} \frac {f \left(\boldsymbol {x} _ {0} + h \lambda \boldsymbol {u}\right) - f \left(\boldsymbol {x} _ {0}\right)}{h \lambda} \tag {15.1.2} \\ = \lambda \frac {\partial f (\boldsymbol {x} _ {0})}{\partial \boldsymbol {u}}. \\ \end{array}
$$

---

244

第十五章 多元函数微分学及其应用

这样一来, 我们看出在定义式 (15.1.1) 中如果没有单位向量的假设, 那么即使沿着同一方向的方向导数, 其结果也将因 $\lambda$ 的不同而导致计算结果的千差万别, 这在实际应用中会带来诸多不便. 这一场景犹如在考察一个二维山坡在某点处沿东北方向变化快慢时,不应该依赖于指向东北方向的手臂长短不同而不同.

还有一点值得注意, 如果 $\lambda < 0$, 比如 $\lambda = -1$, 在定义 15.1.3 中, 一般来说, $f$ 沿 $u$ 的方向导数并不等同于沿 $-u$ 的方向导数. 即, 如果令 $v = -u$, 则有

$$
\begin{array}{l} \frac {\partial f (\boldsymbol {x} _ {0})}{\partial \boldsymbol {v}} = \lim _ {h \to 0 ^ {+}} \frac {f (\boldsymbol {x} _ {0} + h \boldsymbol {v}) - f (\boldsymbol {x} _ {0})}{h} \\ = \lim _ {h \to 0 ^ {+}} \frac {f (\boldsymbol {x} _ {0} - h \boldsymbol {u}) - f (\boldsymbol {x} _ {0})}{h} \\ = - \lim _ {t \to 0 ^ {-}} \frac {f (\boldsymbol {x} _ {0} + t \boldsymbol {u}) - f (\boldsymbol {x} _ {0})}{t} \\ \neq - \frac {\partial f (\boldsymbol {x} _ {0})}{\partial \boldsymbol {u}}. \\ \end{array}
$$

所以, 沿 $\pmb{u}$ 的负方向 $-\pmb{u}$ 的方向导数 $\frac{\partial f(\pmb{x}_0)}{\partial(-\pmb{u})}$ 和沿 $\pmb{u}$ 的方向导数的负值 $-\frac{\partial f(\pmb{x}_0)}{\partial\pmb{u}}$, 一般来说, 是不相等的.

![](../../raw/pages_0545-0560/images/page_548_image_6.jpg)

注 15.1.1 不同的教材或参考书中, 方向导数的定义可能有所不同. 两种常见的方式为: 在 (15.1.1) 式中, 一种是  $h \rightarrow 0^{+}$  的极限, 另一种是  $h \rightarrow 0$  的极限. 本书采用的是第一种形式下的定义.

在我们采用的定义下, 方向导数与偏导数之间有如下关系, 读者可自行验证.

命题 15.1.2 设 $z = f\left( x\right)$ 是定义在开集 $D \subseteq  {\mathbb{R}}^{n}$ 上的 $n$ 元函数. ${x}_{0} \in  D$ .

$$
\boldsymbol {u} = \boldsymbol {e} _ {i} = (0, \dots , 0, 1, 0, \dots , 0), \quad \boldsymbol {v} = - \boldsymbol {e} _ {i} = (0, \dots , 0, - 1, 0, \dots , 0),
$$

其中向量中为 $\pm 1$ 的分量位于第 $i$ 个位置. 则偏导数 $\frac{\partial f(x_0)}{\partial x_i}$ 存在的充要条件是 $\frac{\partial f(x_0)}{\partial u}$ 和 $\frac{\partial f(x_0)}{\partial v}$ 都存在有限, 且

$$
\frac {\partial f (\boldsymbol {x} _ {0})}{\partial x _ {i}} = \frac {\partial f (\boldsymbol {x} _ {0})}{\partial \boldsymbol {u}} = - \frac {\partial f (\boldsymbol {x} _ {0})}{\partial \boldsymbol {v}}.
$$

我们给出几个关于偏导数、方向导数以及它们之间关系的例子. 首先, 下面的例子说明, 即使函数在某点处所有方向的方向导数都存在, 也不一定可偏导.

例 15.1.4 证明: 二元函数  $z = f(x, y) = \sqrt{x^{2} + y^{2}}$  在  $(0, 0)$  点沿任意方向的方向导数都存在, 但偏导数不存在.

证明 任取单位向量 $\pmb{u} = (u_{1}, u_{2})$，可得

$$
\frac {\partial f}{\partial \boldsymbol {u}} (0, 0) = \lim _ {h \to 0 ^ {+}} \frac {f (h \boldsymbol {u})}{h} = \frac {f (h u _ {1} , h u _ {2})}{h} = \lim _ {h \to 0 ^ {+}} \frac {h}{h} = 1.
$$

---

15.1 偏导数与方向导数

245

所以函数沿任一方向的方向导数都存在且相等.

另一方面, 根据定义, 有

$$
\frac {\partial f}{\partial x} (0, 0) = \lim _ {x \to 0} \frac {f (x , 0) - f (0 , 0)}{x - 0} = \lim _ {x \to 0} \frac {| x |}{x},
$$

所以 $f_{x}(0,0)$ 不存在. 同理, $f_{y}(0,0)$ 也不存在.

如果应用命题 15.1.2, 也可以得到 f 的偏导数不存在.

当然, 反过来, 如果函数 $f$ 在 $\pmb{x}_0$ 处的偏导数存在, 除了能保证沿着平行于坐标轴方向的方向导数存在外, 并不能保证其他方向的方向导数存在. 为此, 读者可以自行验证下面的例子:

例15.1.5 证明:二元函数

$$
f (x, y) = \left\{ \begin{array}{l l} \frac {x y}{x ^ {2} + y ^ {2}}, & (x, y) \neq (0, 0), \\ 0, & (x, y) = (0, 0), \end{array} \right.
$$

在 $(0,0)$ 点偏导数存在,但沿任意非坐标轴方向的方向导数都不存在.

读者还可验证下面的结论:

例 15.1.6 一个在  $(0,0)$  点连续，但在该点沿任何方向的方向导数都不存在的例子:

$$
f (x, y) = x ^ {2 / 3} + y ^ {2 / 3}.
$$

例15.1.7 证明:二元函数

$$
f (x, y) = \left\{ \begin{array}{l l} {1,} & {y = x ^ {2}, x \neq 0,} \\ {0,} & {\text {其他点}} \end{array} \right.
$$

在 $(0,0)$ 处沿任意方向的方向导数都为0，但函数并非常值函数，事实上，该函数在原点并不连续.

和一元函数不同, 对于一个多元函数, 它在某点处的偏导数或方向导数存在, 只是反映了函数沿特定方向的变化性质, 所以偏导数和方向导数的存在都不能保证多元函数的连续性.

为了更好地研究多元函数的性质, 更系统地对比偏导、方向导数、连续、可微之间的关系, 我们引入下面的一个重要的基本概念: 微分.

定义 15.1.4(微分、导数) 设  $D \subseteq R^{n}$  为一开集,  $f: D \to R$  为多元函数,  $x_{0} \in D$ . 如果存在 n 维向量  $L_{x_{0}} = (A_{1}, A_{2}, \cdots, A_{n})$ , 使得在  $x_{0}$  附近成立

$$
f (\boldsymbol {x}) - f (\boldsymbol {x} _ {0}) = \langle \boldsymbol {L} _ {\boldsymbol {x} _ {0}}, \Delta \boldsymbol {x} \rangle + o (\| \Delta \boldsymbol {x} \|) \quad (\boldsymbol {x} \rightarrow \boldsymbol {x} _ {0}),
$$

则称 $f$ 在 $\pmb{x}_0$ 处可微, $\Delta \pmb{x} = \pmb{x} - \pmb{x}_0$ 称为自变量 $\pmb{x}$ 的全增量, 向量 $L_{\pmb{x}_0}$ 称为函数 $f$ 在 $\pmb{x}_0$ 处的导数, 也记为

$$
L _ {\boldsymbol {x} _ {0}} = f ^ {\prime} (\boldsymbol {x} _ {0}).
$$

---

246

第十五章 多元函数微分学及其应用

向量 $L_{\pmb{x_0}}$ 与 $\Delta \pmb{x}$ 的内积 $\langle L_{\pmb{x_0}},\Delta \pmb{x}\rangle = \sum_{i = 1}^{n}A_i\Delta x_i$ 称为 $f$ 在 $\pmb{x}_0$ 处的全微分，或简称微分，并记作 $\mathrm{df}(\pmb{x}_0)$，即

$$
\mathrm{d} f (\boldsymbol {x} _ {0}) = \langle \boldsymbol {L} _ {\boldsymbol {x} _ {0}}, \Delta \boldsymbol {x} \rangle = \sum_ {i = 1} ^ {n} A _ {i} \Delta x _ {i}.
$$

如果 $\forall x\in D$ ， $f$ 在 $\pmb{x}$ 处都可微，则称 $f$ 在 $D$ 上可微.

由于当 $1 \leqslant i \leqslant n, x_{i}$ 是自变量时，可定义 $\mathrm{dx}_i = \Delta x_i$ ，因此 $f(\pmb{x})$ 在 $\pmb{x_0}$ 处的微分又更自然地记为

$$
\mathrm{d} f (\pmb {x} _ {0}) = \langle \pmb {L} _ {\pmb {x} _ {0}}, \mathrm{d} \pmb {x} \rangle = \sum_ {i = 1} ^ {n} A _ {i} \mathrm{d} x _ {i}.
$$

函数 $f$ 的全微分有明确的几何意义. 图15.1给出了长和宽分别为 $x$ 和 $y$ 的矩形面积 $S(x,y) = xy$ 的全微分的几何意义 (可对比一元函数微分章节中的图6.6). 考虑函数 $S$ 在 $(x_0,y_0)$ 处的增量 $\Delta S$

$$
\Delta S = y _ {0} \Delta x + x _ {0} \Delta y + \Delta x \cdot \Delta y = (y _ {0}, x _ {0}) \cdot (\Delta x, \Delta y) + \Delta x \cdot \Delta y,
$$

即  $\Delta S$  由三部分组成: 两个浅色矩形的面积  $x_{0}\Delta y$  和  $y_{0}\Delta x$ , 以及一个边长为  $\Delta x$  和  $\Delta y$  的深色矩形的面积  $\Delta x \cdot \Delta y$ , 后者是自变量增量  $(\Delta x, \Delta y)$  的高阶无穷小量.

![](../../raw/pages_0545-0560/images/page_550_image_10.jpg)

<details>
<summary>text_image</summary>

y
Δy
Δx·Δy
y₀
S(x₀, y₀)
O
x₀
x
</details>

图15.1 微分的几何意义

微分也称为函数 $f$ 的线性化. 微分学的基本思想就是对各种研究对象做线性化 (以直代曲). 显然, 当 $f$ 在 $\pmb{x}_0$ 处可微时, $f$ 也在 $\pmb{x}_0$ 处连续, 具体来说, 我们有

命题 15.1.3 (可微必可导) 设 f 在  $x_{0}$  处可微, 其微分为  $\mathrm{d}f(x_{0})=\sum_{i=1}^{n}A_{i}\mathrm{d}x_{i}$ ,
则

(1) f 在  $x_{0}$  处连续.
(2) 对 $1 \leqslant i \leqslant n$, 有 $\frac{\partial f}{\partial x_i} (\pmb{x}_0) = A_i$.

---

15.1 偏导数与方向导数

247

证明 可以由偏导和可微的定义直接得到, 证明从略.

值得注意的是, 命题反方向的结论不成立. 即函数可偏导、可导都不能得出可微.

根据命题 15.1.3 可知, 当 f 在  $x_{0}$  处可微时, 导数  $f^{\prime}(x_{0})$ , 偏导数  $f_{x_{i}}(x_{0})$  都存在, 称向量  $(f_{x_{1}}(x_{0}),\cdots,f_{x_{n}}(x_{0}))$  为  $f(x)$  在  $x_{0}$  处的梯度, 记为  $\operatorname{grad} f(x_{0})$ , 也记为

$$
\nabla f \left(\boldsymbol {x} _ {0}\right) = \operatorname{grad} f \left(\boldsymbol {x} _ {0}\right) = f ^ {\prime} \left(\boldsymbol {x} _ {0}\right) = \left(f _ {x _ {1}} \left(\boldsymbol {x} _ {0}\right), \dots , f _ {x _ {n}} \left(\boldsymbol {x} _ {0}\right)\right). \tag {15.1.3}
$$

注意对多元函数而言, 大家最常见到的是偏导数这个概念, 而在定义 15.1.4 中我们采用了 “导数” 这个字眼, 很大程度上是借用一元函数 “导数” 的语境, 只需注意这是一个说法而已: 对于多元函数, “导数” 给出的是一个向量. 另外, 我们已经赋予 “导数” 多种称呼和记号: 比如线性映射、微分算子, 以及在场论中常见到的梯度, 等等.

在函数可微的条件下, 下面几种表示都是在说多元函数  $f(x)$  的同一件事:

$$
f ^ {\prime} (\boldsymbol {x}), \qquad \nabla f (\boldsymbol {x}), \qquad \operatorname{grad} f (\boldsymbol {x}), \qquad \boldsymbol {L} _ {\boldsymbol {x}} = \left(f _ {x _ {1}} (\boldsymbol {x}), \dots , f _ {x _ {n}} (\boldsymbol {x})\right),
$$

在后面的章节中, 我们经常在这些不同的表示中自由切换.

关于多元函数可微与方向导数之间的关系, 有下面的结论:

命题 15.1.4 (可微必方向可导) 设 f 在  $x_{0}$  处可微,  $u = \sum_{i=1}^{n} u_{i} e_{i}$  为任一 n 维单位向量, 则 f 在  $x_{0}$  处沿 u 的方向导数都存在, 并且有

$$
\frac {\partial f}{\partial \boldsymbol {u}} (\boldsymbol {x} _ {0}) = \mathrm{d} f (\boldsymbol {x} _ {0}) (\boldsymbol {u}) = \nabla f (\boldsymbol {x} _ {0}) \cdot \boldsymbol {u}. \tag {15.1.4}
$$

证明 设 u 为单位向量. 根据假设, 有

$$
f (\boldsymbol {x} _ {0} + t \boldsymbol {u}) - f (\boldsymbol {x} _ {0}) = L (t \boldsymbol {u}) + o (\| t \boldsymbol {u} \|) = t L (\boldsymbol {u}) + o (| t |) \quad (t \rightarrow 0).
$$

故

$$
\frac {\partial f}{\partial \boldsymbol {u}} (\boldsymbol {x} _ {0}) = \lim _ {t \to 0} \frac {f (\boldsymbol {x} _ {0} + t \boldsymbol {u}) - f (\boldsymbol {x} _ {0})}{t} = L (\boldsymbol {u}) = L \left(\sum_ {i = 1} ^ {n} u _ {i} \boldsymbol {e} _ {i}\right) = \nabla f (\boldsymbol {x} _ {0}) \cdot \boldsymbol {u}.
$$

即 (15.1.4) 式成立.

注 15.1.2 人们习惯于把方向导数中的单位向量 u 用方向余弦表示, 即

$$
\boldsymbol {u} = (\cos \alpha_ {1}, \cos \alpha_ {2}, \dots , \cos \alpha_ {n}), \quad \sum_ {i = 1} ^ {n} \cos^ {2} \alpha_ {i} = 1,
$$

其中  $\alpha_{i}(i=1,2,\cdots,n)$  表示向量 u 与坐标轴  $x_{i}$  正向的夹角，那么当 f 在  $x_{0}$  处可微时，f 的导数和沿方向 u 的方向导数之间有如下的关系:

$$
\frac {\partial f}{\partial \boldsymbol {u}} (\boldsymbol {x} _ {0}) = f ^ {\prime} (\boldsymbol {x} _ {0}) \cdot \boldsymbol {u} = \nabla f (\boldsymbol {x} _ {0}) \cdot \boldsymbol {u} = f _ {x _ {1}} \cos \alpha_ {1} + f _ {x _ {2}} \cos \alpha_ {2} + \dots + f _ {x _ {n}} \cos \alpha_ {n}.
$$

显然, 这一方向导数只有在向量 u 与梯度向量  $\nabla f(x_{0})$  同向时达到最大

---

248

第十五章 多元函数微分学及其应用

值, 即, 当  $\nabla f(\boldsymbol{x}_{0}) = \lambda \boldsymbol{u} (\lambda > 0)$  时,

$$
\| \nabla f \| = \sqrt {f _ {x _ {1}} ^ {2} + f _ {x _ {2}} ^ {2} + \cdots + f _ {x _ {n}} ^ {2}}.
$$

因此, 梯度方向是与具体的坐标系选取无关的: 一个纯量函数 $f$ 的梯度 $\nabla f$ 是一个向量, 其大小和方向是 $f$ 等高线变化最快的方向.

定义 15.1.5 设 $D \subseteq \mathbb{R}^n$ 为一开集, 如果 $\forall x \in D$, 定义在 $D$ 上的 $n$ 元函数 $f$ 在 $x$ 附近偏导数都存在, 且偏导数在点 $x$ 处连续, 则称 $f$ 在 $D$ 上是 $C^1$ 的, 记为 $f \in C^1(D)$. 即, $C^1(D)$ 是指 $D$ 上所有偏导数都存在且连续的函数的全体.

下面的结果给出了多元函数可微的充分条件.

命题 15.1.5 若  $f \in C^{1}(D)$ ，则 f 在 D 上必可微.

证明 以二元函数为例, 记 $\pmb{x} = (x, y)$, $\pmb{x}_0 = (x_0, y_0)$. 当 $\pmb{x} \to \pmb{x}_0$ 时, 有

$$
\begin{array}{l} f (\boldsymbol {x}) - f (\boldsymbol {x} _ {0}) = (f (x, y) - f (x _ {0}, y)) + (f (x _ {0}, y) - f (x _ {0}, y _ {0})) \\ = \frac {\partial f}{\partial x} (\xi , y) \Delta x + \frac {\partial f}{\partial y} (x _ {0}, \zeta) \Delta y \\ = \left(\frac {\partial f}{\partial x} (\boldsymbol {x} _ {0}) + o (1)\right) \Delta x + \left(\frac {\partial f}{\partial y} (\boldsymbol {x} _ {0}) + o (1)\right) \Delta y \\ = \frac {\partial f}{\partial x} (\boldsymbol {x} _ {0}) \Delta x + \frac {\partial f}{\partial y} (\boldsymbol {x} _ {0}) \Delta y + o \big (\| \boldsymbol {x} - \boldsymbol {x} _ {0} \| \big), \\ \end{array}
$$

故 $f$ 在 $\pmb{x}_0 = (x_0, y_0)$ 处可微.

综合命题 15.1.3 与命题 15.1.5 以及前面的讨论, 我们得到下面的逻辑关系:

$f$ 在 $D$ 上方向导数存在

$$
f \in C ^ {1} (D) \Rightarrow \quad \begin{array}{c} \uparrow \\ f \text {在} D \text {上可微} \\ \Downarrow \end{array} \quad \Rightarrow f \text {在} D \text {上连续}.
$$

$f$ 在 $D$ 上偏导数存在

例15.1.8 例15.1.5中的函数

$$
f (x, y) = \left\{ \begin{array}{l l} \frac {x y}{x ^ {2} + y ^ {2}}, & (x, y) \neq (0, 0), \\ 0, & (x, y) = (0, 0) \end{array} \right.
$$

在 $(0,0)$ 点偏导数存在,但在 $(0,0)$ 点不连续(在该点非坐标轴方向上的方向导数也不存在),故在该点不可微.

---

15.1 偏导数与方向导数

249

例15.1.9 证明:函数

$$
f (x, y) = \left\{ \begin{array}{l l} \left(x ^ {2} + y ^ {2}\right) \sin \frac {1}{\sqrt {x ^ {2} + y ^ {2}}}, & (x, y) \neq (0, 0), \\ 0, & (x, y) = (0, 0) \end{array} \right.
$$

在 $(0,0)$ 处可微,但偏导数不连续.

证明 $f$ 的可微性易证, 下面我们只考虑 $f$ 偏导数的不连续性. 由于

$$
f _ {x} (x, y) = \left\{ \begin{array}{l l} 2 x \sin \frac {1}{\sqrt {x ^ {2} + y ^ {2}}} - \frac {x}{\sqrt {x ^ {2} + y ^ {2}}} \cos \frac {1}{\sqrt {x ^ {2} + y ^ {2}}}, & (x, y) \neq (0, 0), \\ 0, & (x, y) = (0, 0), \end{array} \right.
$$

令 $x_{k} = y_{k} = \frac{\sqrt{2}}{4k\pi}$ ，则有

$$
\lim _ {k \to + \infty} f _ {x} (x _ {k}, y _ {k}) = - \frac {\sqrt {2}}{2}.
$$

另一方面，由定义直接计算可得 $f_{x}(0,0) = 0$ ，故 $f_{x}$ 在 $(0,0)$ 点不连续.同理可证 $f_{y}$ 在 $(0,0)$ 点也不连续. □

## $C^{k}$  函数类, 混合偏导数的次序

上面我们看到一阶偏导数的连续性是一个较强的条件, 也就是说, 如果 $f$ 是 $C^1$ 的, 那么它将蕴涵着可微性、偏导数和方向导数的存在性等结论. 对于高阶偏导数, 也有类似的结论. 为此, 我们先把前面介绍过的 $C^1$ 概念一般化:

定义 15.1.6 $\left( {{C}^{k}\text{函数类}}\right)$ 设 $f : D \rightarrow  \mathbb{R}$ 为多元函数. 如果 $f$ 连续,且直到 $k$ 阶的各种偏导数都存在且连续,则称 $f$ 为 ${C}^{k}$ 函数,记为 $f \in  {C}^{k}\left( D\right)$ . 如果对任意 $k \geq  0,f$ 均为 ${C}^{k}$ 函数,则称 $f$ 为无限次可导函数或光滑函数,记为 $f \in  {C}^{\infty }\left( D\right)$ .

值得注意的是, 一元函数 $C^k$ 的定义 (见定义6.5.2) 只要求 $k$ 阶导数连续即可, 无须要求更低阶的导数存在且连续, 这是因为对于一元函数而言, 高阶可导必然有低阶可导成立. 这一断言对于多元函数来说, 应该明确如下: 如果定义域 $D$ 不是区域, 那么上述偏导和高阶偏导的定义有些复杂和麻烦, 高阶可偏导通常也不自动蕴涵低阶可偏导, 比如下面的例子. 因此为了避免这种极其复杂的定义域带来的技术上的繁文缛节, 我们的讨论限于 $D$ 是 $\mathbb{R}^n$ 中的区域, 在这种基本假设下, 多元函数的 $C^k(D)$ 类可以定义为区域 $D$ 上的所有 $k$ 阶偏导数均连续的函数的全体.

例15.1.10 函数

$$
f (x, y) = \left\{ \begin{array}{l l} \mathrm{e} ^ {- x ^ {2} / y ^ {2} - y ^ {2} / x ^ {2}}, & x y \neq 0, \\ 0, & x y = 0 \end{array} \right.
$$

---

250

第十五章 多元函数微分学及其应用

在 $(0,0)$ 点不连续,但其各阶偏导数处处存在. $^{①}$

下面的定理表明, 对于  $C^{2}$  函数, 虽然它的任意两个混合偏导数  $f_{x_{i}x_{j}}$  和  $f_{x_{j}x_{i}}$  都是以二元函数陈述的, 但显然结论对于 n 元函数均成立.

定理 15.1.6（求导次序的可交换性） 设  $f: D \rightarrow R$  为二元函数,  $(x_{0}, y_{0}) \in D$ . 如果  $f \in C^{2}(D)$ ，则  $f_{yx}(x_{0}, y_{0}) = f_{xy}(x_{0}, y_{0})$ .

证明 对于充分小的 $k \neq 0, h \neq 0$, 考虑函数

$$
\varphi (y) = f (x _ {0} + h, y) - f (x _ {0}, y), \quad \psi (x) = f (x, y _ {0} + k) - f (x, y _ {0}).
$$

由微分中值定理, 存在  $\theta_{1}, \theta_{2} \in (0,1)$ , 使得

$$
\begin{array}{l} \varphi (y _ {0} + k) - \varphi (y _ {0}) = \varphi_ {y} (y _ {0} + \theta_ {1} k) k \\ = \left(f _ {y} (x _ {0} + h, y _ {0} + \theta_ {1} k) - f _ {y} (x _ {0}, y _ {0} + \theta_ {1} k)\right) k \\ = f _ {y x} (x _ {0} + \theta_ {2} h, y _ {0} + \theta_ {1} k) k h. \\ \end{array}
$$

同理, 存在  $\theta_{3}, \theta_{4} \in (0,1)$ , 使得

$$
\psi (x _ {0} + h) - \psi (x _ {0}) = f _ {x y} (x _ {0} + \theta_ {3} h, y _ {0} + \theta_ {4} k) h k.
$$

易见 $\varphi (y_0 + k) - \varphi (y_0) = \psi (x_0 + h) - \psi (x_0)$，这说明

$$
f _ {y x} (x _ {0} + \theta_ {2} h, y _ {0} + \theta_ {1} k) = f _ {x y} (x _ {0} + \theta_ {3} h, y _ {0} + \theta_ {4} k).
$$

令  $k, h \rightarrow 0$ ，由  $f_{yx}, f_{xy}$  在  $(x_{0}, y_{0})$  处连续即得欲证等式.

上述结果对于更一般的情况也成立, 读者可以自行证明: 对于多元函数 $f$, 如果 $f \in C^{k}(D)$, $k \geqslant 2$, 那么它的任意 $k$ 阶偏导数 $f_{x_{i_1}x_{i_2}\cdots x_{i_k}}$ 与求偏导次序无关.

下面的例子告诉我们, 如果函数不是  $C^{2}$  的, 那么二阶混合偏导数的值可能与求导次序有关.

例15.1.11 考虑函数

$$
f (x, y) = \left\{ \begin{array}{l l} x y \frac {x ^ {2} - y ^ {2}}{x ^ {2} + y ^ {2}}, & (x, y) \neq (0, 0), \\ 0, & (x, y) = (0, 0). \end{array} \right.
$$

试求函数在 $(0,0)$ 处的两个二阶混合偏导数 $f_{xy}(0,0)$ 和 $f_{yx}(0,0)$.

解 直接计算可得如下表示:

$$
f _ {x} (x, y) = \left\{ \begin{array}{l l} \frac {x ^ {4} y + 4 x ^ {2} y ^ {3} - y ^ {5}}{(x ^ {2} + y ^ {2}) ^ {2}}, & (x, y) \neq (0, 0), \\ 0, & (x, y) = (0, 0) \end{array} \right.
$$

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">① N. Kimura, J. Burr. Discontinuous function with partial derivatives everywhere. Amer. Math. Monthly, 1960(8): 813-814.</span></small>

---

15.1 偏导数与方向导数

251

和

$$
f _ {y} (x, y) = \left\{ \begin{array}{l l} \frac {x ^ {5} - 4 x ^ {3} y ^ {2} - x y ^ {4}}{(x ^ {2} + y ^ {2}) ^ {2}}, & (x, y) \neq (0, 0), \\ 0, & (x, y) = (0, 0), \end{array} \right.
$$

从而可得

$$
f _ {x y} (0, 0) = 1, \quad f _ {y x} (0, 0) = - 1.
$$

作为不能随意交换求偏导次序的反例, 上面例中的函数构思巧妙, 为绝大多数教材或参考书所采用, 甚至都鲜见其他反例. 下面我们对这个函数的构造做一些进一步的讨论.

为了看清楚这个例子的来龙去脉以及它的几何意义, 我们将函数用极坐标表示, 代之以 $f(x, y)$, 我们考虑 $4f(x, y)$ 并且还把它记为 $f(x, y)$, 显然这丝毫不影响结论. 令

$$
x = r \cos \theta , \quad y = r \sin \theta , \quad r > 0, \quad \theta \in [ 0, 2 \pi).
$$

则有

$$
f (x, y) = r ^ {2} \sin 4 \theta .
$$

该函数图像见本节后面图15.6.

利用这个有趣的观察, 读者就不难发现下面诸多二阶混合偏导数各具特色的例子. 我们把这些结论的验证留给读者, 有兴趣的读者可以从这些素材中提炼出一般性结论.

例 15.1.12 下列结论成立:

(1) 函数 $f(x, y) = x^2 + y^2$ 是 $C^\infty(\mathbb{R}^2)$ 的, 特别地, 两个混合偏导数 $f_{xy}(0, 0)$ 和 $f_{yx}(0, 0)$ 存在且相等.
(2) 函数 $f(x, y) = 2xy$ 是 $C^\infty(\mathbb{R}^2)$ 的，特别地，两个混合偏导数 $f_{xy}(0, 0)$ 和 $f_{yx}(0, 0)$ 存在且相等.
(3) 重述例 15.1.11 中的函数

$$
f (x, y) = \left\{ \begin{array}{l l} 4 x y \frac {x ^ {2} - y ^ {2}}{x ^ {2} + y ^ {2}}, & (x, y) \neq (0, 0), \\ 0, & (x, y) = (0, 0). \end{array} \right.
$$

它在 $(0,0)$ 处的两个二阶混合偏导数 $f_{xy}(0,0)$ 和 $f_{yx}(0,0)$ 存在但不相等.

(4) 函数

$$
f (x, y) = \left\{ \begin{array}{l l} 2 x y \frac {(3 x ^ {2} - y ^ {2}) (x ^ {2} - 3 y ^ {2})}{(x ^ {2} + y ^ {2}) ^ {2}}, & (x, y) \neq (0, 0), \\ 0, & (x, y) = (0, 0) \end{array} \right.
$$

在 $(0,0)$ 处的两个二阶混合偏导数 $f_{xy}(0,0)$ 和 $f_{yx}(0,0)$ 存在且相等，均为0.

---

252

第十五章 多元函数微分学及其应用

(5) 函数

$$
f (x, y) = y \sqrt {x ^ {2} + y ^ {2}} \tag {15.1.5}
$$

的两个混合偏导数  $f_{xy}(0,0)$  和  $f_{yx}(0,0)$ ，一个存在，一个不存在.

(6) 函数

$$
f (x, y) = \left\{ \begin{array}{l l} y \frac {3 x ^ {2} - y ^ {2}}{\sqrt {x ^ {2} + y ^ {2}}}, & (x, y) \neq (0, 0), \\ 0, & (x, y) = (0, 0) \end{array} \right.
$$

的两个混合偏导数  $f_{xy}(0,0)$  和  $f_{yx}(0,0)$ ，一个存在，一个不存在.

(7) 函数

$$
f (x, y) = \left\{ \begin{array}{l l} \frac {5 x ^ {4} y - 1 0 x ^ {2} y ^ {3} + y ^ {5}}{(\sqrt {x ^ {2} + y ^ {2}}) ^ {3}}, & (x, y) \neq (0, 0), \\ 0, & (x, y) = (0, 0) \end{array} \right.
$$

的两个混合偏导数 $f_{xy}(0,0)$ 和 $f_{yx}(0,0)$, 一个存在, 一个不存在.

初看起来, 这些函数要么结论过于平凡, 比如 (1) 和 (2), 要么感觉人为构造痕迹明显, 比如 (3)—(7), 甚至我们还能构造出形式更 “诡异” 且符合我们预期的函数. 其实, 如果把这些函数用极坐标系表达, 从 (1) 到 (7), 我们还是能看出它们的分析性质和几何特点的. 比如, 它们分别具有如下形式:

(1) $z = r^2$;
(2) $z = r^{2}\sin 2\theta$
(3) $z = r^{2}\sin 4\theta$
(4) $z = r^{2}\sin 6\theta$
(5) $z = r^{2}\sin \theta$
(6) $z = r^{2}\sin 3\theta$
(7) $z = r^{2}\sin 5\theta$

图 15.2—图 15.7 是相应函数的图像.

![](../../raw/pages_0545-0560/images/page_556_chart_21.jpg)

<details>
<summary>surface_3d</summary>

| x | y | \(\xi\) |
| --- | --- | --- |
| -1 | -1 | ~0 |
| -1 | 0 | ~0 |
| -1 | 1 | ~0 |
| 0 | -1 | ~0 |
| 0 | 0 | ~0 |
| 0 | 1 | ~0 |
| 1 | -1 | ~0 |
| 1 | 0 | ~0 |
| 1 | 1 | ~0 |
</details>

图15.2 $z = r^2$

---

15.1 偏导数与方向导数

253

![](../../raw/pages_0545-0560/images/page_557_chart_2.jpg)

<details>
<summary>surface_3d</summary>

| x | y | z |
| --- | --- | --- |
| -1~1 | -1~1 | -1~1 |
</details>

图15.3 $z = r^2\sin \theta$

![](../../raw/pages_0545-0560/images/page_557_chart_4.jpg)

<details>
<summary>surface_3d</summary>

| x | y | z |
| --- | --- | --- |
| -1~1 | -1~1 | -1~0.5 |
</details>

图15.4 $z = r^2\sin 2\theta$

![](../../raw/pages_0545-0560/images/page_557_chart_6.jpg)

<details>
<summary>surface_3d</summary>

| x | y | z |
| --- | --- | --- |
| -1~1 | -1~1 | ~-0.8 ~0.8 |
</details>

图15.5 $z = r^2\sin 3\theta$

---

254

第十五章 多元函数微分学及其应用

![](../../raw/pages_0545-0560/images/page_558_chart_2.jpg)

<details>
<summary>surface_3d</summary>

| x | y | z |
| --- | --- | --- |
| -1~1 | -1~1 | -1~1 |
</details>

图15.6 $z = r^2\sin 4\theta$

![](../../raw/pages_0545-0560/images/page_558_chart_4.jpg)

<details>
<summary>surface_3d</summary>

| x | y | z |
| --- | --- | --- |
| -1~1 | -1~1 | -1~0.5 |
</details>

图15.7 $z = r^2\sin 5\theta$

当然, 经过适量的计算, 还可以继续考虑  $z = r^{2} \sin 8\theta$  的情况. 此时, 所对应的直角坐标下的函数  $f(x, y)$  具有形式

$$
f (x, y) = \left\{ \begin{array}{l l} x y \frac {(x ^ {2} - y ^ {2}) (x ^ {4} - 6 x ^ {2} y ^ {2} + y ^ {4})}{(x ^ {2} + y ^ {2}) ^ {3}}, & (x, y) \neq (0, 0), \\ 0, & (x, y) = (0, 0). \end{array} \right.
$$

有兴趣的读者可以证明 $f(x,y)$ 在 $(0,0)$ 点的两个混合偏导数 $f_{xy}(0,0)$ 和 $f_{yx}(0,0)$ 都存在但不相等.

显然, 读者可能很自然提出如下问题: 函数 $z = r^{2} \sin k\theta$ 在直角坐标表示下, 相应的函数的二阶混合偏导数 $f_{xy}$ 和 $f_{yx}$ 的存在性和相等性如何依赖于 $k$ 的取值? 读者可以通过讨论 $k \in \{4p + 2, 4p, 2p + 1\}, p > 0$ 来进行分类.

现在我们不妨再啰唆几句, 考虑下面的函数, 并返回去考虑一阶偏导数的存在性:

---

15.1 偏导数与方向导数

255

例15.1.13 证明:函数

$$
f (x, y) = \left\{ \begin{array}{l l} \frac {2 x y}{\sqrt {x ^ {2} + y ^ {2}}}, & (x, y) \neq (0, 0), \\ 0, & (x, y) = (0, 0) \end{array} \right.
$$

和函数

$$
g (x, y) = \left\{ \begin{array}{l l} \frac {3 x ^ {2} y - y ^ {3}}{x ^ {2} + y ^ {2}}, & (x, y) \neq (0, 0), \\ 0, & (x, y) = (0, 0) \end{array} \right.
$$

的两个偏导数 $f_{x}(0,0), f_{y}(0,0)$ 和 $g_{x}(0,0), g_{y}(0,0)$ 都存在. 沿任意方向的方向导数也存在. 但 $f_{x}$ 和 $f_{y}$ 在 $(0,0)$ 点都不连续, $f$ 在原点也不可微. 同理, $g_{x}$ 和 $g_{y}$ 在 $(0,0)$ 点也都不连续, $g$ 在原点也不可微.

例子结论的正确性可以通过计算直接得以验证, 从略. 下面我们也从极坐标的角度来分析这两个函数, 同时再回顾和对比一下例 15.1.4 中的函数 $z = f(x, y) = \sqrt{x^2 + y^2} = r$.

事实上, 这三个函数的表达式为

$$
(1) z = r; \quad (2) z = r \sin 2 \theta ; \quad (3) z = r \sin 3 \theta.
$$

结论是它们的方向导数都存在, 偏导数 (1) 不存在, (2) 和 (3) 存在, 但不连续. 所有的情况在 $(0,0)$ 点都不可微.

一个稍微一般性的问题是, 如果函数  $f(x,y)$  在极坐标下表达式为

$$
f (x, y) = \left\{ \begin{array}{l l} r \sin k \theta , & (x, y) \neq (0, 0), k \geqslant 2, \\ 0, & (x, y) = (0, 0). \end{array} \right.
$$

考虑函数 $f$ 在 $(0,0)$ 点处的方向导数、偏导数的存在性，以及可微性. 我们留给读者做进一步的思考.

如果不厌其烦的话, 还可以回顾和对比例 15.1.5 中的函数. 在极坐标表示下, 该函数具有表示 $z = \sin 2\theta$, 注意此函数在原点不连续.

把上面的内容综合起来, 我们可以提出一个更一般些的思考题: 函数

$$
f (x, y) = r ^ {m} \sin n \theta , \quad m \geqslant 0,   n \in \mathbb {N}
$$

的 $m$ 阶混合偏导数的存在性、混合偏导数次序的可交换性如何？

下面我们再回到定理 15.1.6 中的话题, 我们知道, 函数 $f \in C^{2}(D)$ 是保证两个二阶混合偏导数 $f_{xy} f_{yx}$ 相等的充分条件. 事实上, 关于两个混合偏导数何时相等的问题, Bernoulli, Euler, Lagrange, Cauchy, Schwarz, Young 等诸多数学家对此开展过讨论, 得到若干弱化条件下的结论. 下面我们介绍两个有代表性的结论, 其证明留作练习.

---

256

第十五章 多元函数微分学及其应用

定理 15.1.7 (Young 定理) 设 $f: D \to \mathbb{R}$ 为二元函数, $(x_0, y_0) \in D$. 如果 $f$ 在 $(x_0, y_0)$ 附近偏导数 $f_x$ 和 $f_y$ 存在, 并且它们在 $(x_0, y_0)$ 都可微, 那么 $f_{yx}(x_0, y_0) = f_{xy}(x_0, y_0)$.

定理 15.1.8 (Schwarz 定理) 设 $f: D \to \mathbb{R}$ 为二元函数, $(x_0, y_0) \in D$. 如果 $f$ 在 $(x_0, y_0)$ 附近偏导数 $f_x, f_y$ 和 $f_{xy}$ (或 $f_{yx}$) 存在, 且 $f_{xy}$ (或 $f_{yx}$) 在 $(x_0, y_0)$ 连续, 那么 $f_{yx}$ (或 $f_{xy}$) 也存在, 且 $f_{yx}(x_0, y_0) = f_{xy}(x_0, y_0)$.

## 习题 15.1

1. 设 $f$ 为多元函数, 证明: 如果 $\pmb{u}, \pmb{v}$ 为单位向量, 且 $\pmb{u} = -\pmb{v}$, 则 $\frac{\partial f}{\partial \pmb{u}} = -\frac{\partial f}{\partial \pmb{v}}$.

2. 计算偏导数:

(1) $f(x,y) = x + y + \sqrt{x^2 + y^2}$, 求 $f_x(3,4), f_y(0,1)$.
(2) $f(x,y,z) = (\cos x / \sin y)\mathrm{e}^z$ ，求 $\left(\pi ,\frac{\pi}{2},\ln 3\right)$ 处的一阶偏导数.
(3) $f(x,y) = \sin (x^2 y)$, 求 (1,1) 处的一阶偏导数.

3. 求下列函数的一阶偏导数:

(1) $xy + \frac{x}{y};$

(2) $\tan \frac{x^2}{y}$;

(3) $\ln \left(x + \frac{y}{x^2}\right)$;

(4) $\mathrm{e}^{xy + yz + zx}$;

(5) arctan  $\frac{y}{x}$ ;

(6)  $\ln(x_{1} + x_{2} + \cdots + x_{n})$ .

4. 求下列函数的一阶和二阶偏导数:

(1) $(xy)^{yz}$;

(2)  $\arcsin(x_{1}^{2}+\cdots+x_{n}^{2});$

(3) $x^{y^{z}}$;

(4) $\tan (\arctan x + \arctan y)$.

5. 设多元函数 $f$ 的偏导数都存在且有界, 证明: $f$ 连续.

6. 设 $f(x, y, z)$ 在区域 $D \subseteq \mathbb{R}^3$ 上有定义, $f_x(x, y, z)$ 与 $f_y(x, y, z)$ 在 $D$ 上有界, 且对固定的 $(x, y)$, $f(x, y, z)$ 是 $z$ 的连续函数, 证明: $f(x, y, z)$ 在 $D$ 上连续.

7. 试将例 15.1.5 中的函数写成极坐标形式, 然后类似写出函数 $z = \sin 3\theta$, $z = \sin 4\theta$ 的直角坐标形式, 并讨论它们在 $(0,0)$ 点的连续性、偏导数以及方向导数的存在性.

8. 设 $u = \mathrm{e}^{x}\cos y, v = \mathrm{e}^{x}\sin y$, 证明: $u_{x} = v_{y}, u_{y} = -v_{x}$.

9. 记 $\Delta = \frac{\partial^2}{\partial x^2} + \frac{\partial^2}{\partial y^2}$, 称为平面 $\mathbb{R}^2$ 上的 Laplace 算子, 证明: 上题中的 $u, v$ 满足方程 $\Delta u = u_{xx} + u_{yy} = 0, \quad \Delta v = v_{xx} + v_{yy} = 0$.

10. 记 $r = \left((x - x_0)^2 + (y - y_0)^2 + (z - z_0)^2\right)^{1/2}$, 证明: $\Delta r^{-1} = 0$, 其中 $\Delta$ 为 $\mathbb{R}^3$ 中的 Laplace 算子, $\Delta u = u_{xx} + u_{yy} + u_{zz}$.

11. 设 $f(x, y)$ 分别关于变量 $x, y$ 为连续函数, 证明: 如果 $f$ 关于其中一个变量是单调函数 (比如偏导数存在且非负), 则 $f$ 为二元连续函数.

12. 试讨论方向导数的介值性, 即: 设 $f(x,y)$ 在区域 $D \subseteq \mathbb{R}^2$ 内可微, $P_1$ 和

---

15.1 偏导数与方向导数

257

$P_{2}$ 是 $D$ 内两点. 如果 $f(x,y)$ 在 $P_{i}$ 沿方向 $\ell_{i}$ 的方向导数为 $d_{i} (i = 1,2)$, 对于任意 $d$, $d_{1} < d < d_{2}$, 是否一定存在一点 $P \in D$ 及某个方向 $\ell$, 使得 $f(x,y)$ 在 $P$ 沿 $\ell$ 的方向导数为 $d$? 请说明理由.

13. 设 $P(x, y)$ 和 $Q(x, y)$ 均为 $s$ 次齐次可微函数, 证明有下面的关系式:

$$
\frac {\partial}{\partial y} \bigg (\frac {P (x , y)}{x P (x , y) + y Q (x , y)} \bigg) = \frac {\partial}{\partial x} \bigg (\frac {Q (x , y)}{x P (x , y) + y Q (x , y)} \bigg). \tag {*}
$$

14. 设 $M(x, y)$ 和 $N(x, y)$ 分别为 $(m, n)-s + n$ 和 $(m, n)-s + m$ 次拟齐次可微函数 (定义见 (15.3.8) 式), 试着给出相应于 (\*) 式的关系式.

15. 求方向导数:

(1) 设函数 $f(x, y) = xy$，计算函数 $f$ 在点 (1, 1) 处沿方向 $\boldsymbol{u} = \left(\frac{1}{\sqrt{2}}, \frac{1}{\sqrt{2}}\right)$ 的方向导数；

(2) 设 $f(x, y) = (x - 1)^2 - y^2$，方向 $\boldsymbol{u} = \left(\frac{3}{5}, -\frac{4}{5}\right)$. 求 $f$ 在点 (0,1) 处沿方向 $\boldsymbol{u}$ 的方向导数.

16. 设函数 $f(x, y) = \sqrt{|x^2 - y^2|}$. 问:在坐标原点处沿哪些方向 $f$ 的方向导数存在？

17. 设

$$
f (x, y) = \left\{ \begin{array}{l l} \frac {x y}{\sqrt {x ^ {2} + y ^ {2}}}, & x ^ {2} + y ^ {2} > 0, \\ 0, & x ^ {2} + y ^ {2} = 0. \end{array} \right.
$$

问: 在坐标原点处沿哪些方向 f 的方向导数存在?

18. 设函数 $f(x, y, z) = 1 + x + y + z$. 问在平面 $x + y + z = 0$ 上的每一点处, 沿怎样的方向 $f$ 存在方向导数?

19. 设函数  $f(x,y)$  在点  $(x_{0},y_{0})$  可微,  $\{\ell_{1},\ell_{2},\cdots,\ell_{n}\}$  是给定的 n 个单位向量, 相邻两个向量之间的夹角为  $\frac{2\pi}{n}$ . 证明:  $\sum_{i=1}^{n}\frac{\partial f}{\partial\ell_{i}}=0$ .

20. 设  $\{\ell_{1},\ell_{2},\cdots,\ell_{n}\}$  是给定的 n 个线性无关的单位向量,  $f(\boldsymbol{x})$  是区域  $D \subseteq R^{n}$  上的可微函数, 如果  $\frac{\partial f}{\partial\ell_{i}} = 0$  对于  $i = 1, 2, \cdots, n$  都成立, 证明:  $f(\boldsymbol{x})$  在区域 D 上为常数.

21. 如果 $f(x, y)$ 和 $f_x(x, y)$ 均在 $[a, b] \times [c, d]$ 上连续，$g(x) = \int_{c}^{d} f(x, y) \, \mathrm{d}y$. 证明:$g(x)$ 可导且 $g'(x) = \int_{c}^{d} f_x(x, y) \, \mathrm{d}y$.

---

258

第十五章 多元函数微分学及其应用

## 15.2 映射的微分

前面我们讨论了 n 元函数的微分, 那里的多元函数, 具体指形如  $f: D \rightarrow R$ , 其中 D 是  $R^{n}$  中的开集. 下面我们把函数的微分推广到更广的情形, 即映射的微分. 这里所说的映射仍然是有限维欧氏空间之间的映射, 即  $R^{n}$  中的开集 D 到  $R^{m}$  的对应: 设开集  $D \subseteq R^{n}$ ,  $f: D \rightarrow R^{m}$ , f 的分量依次为  $f_{1}, f_{2}, \cdots, f_{m}$ , 它们均为 n 元函数.

在本书中, 我们也把上述意义下的映射称为向量值函数, 并经常在这两种称呼之间来回切换.

设  $\boldsymbol{x}=(x_{1},x_{2},\cdots,x_{n})\in D,$

$$
\boldsymbol {u} = \boldsymbol {f} (\boldsymbol {x}) = (f _ {1} (\boldsymbol {x}), f _ {2} (\boldsymbol {x}), \dots , f _ {m} (\boldsymbol {x})) ^ {\mathrm{T}} = \left( \begin{array}{c} f _ {1} (\boldsymbol {x}) \\ f _ {2} (\boldsymbol {x}) \\ \vdots \\ f _ {m} (\boldsymbol {x}) \end{array} \right)
$$

是开集 $D \subseteq \mathbb{R}^n$ 中一个 $m$ 维向量值函数, 我们常用行向量或者列向量来表示向量值函数, 至于是用行向量还是列向量, 通常可由上下文作出简单判断, 应该不会产生歧义.

下面设  $x_{0} \in D, h \in R^{n}$ ，由于  $x_{0}$  是 D 的内点，故只要  $\|h\| \ll 1$ ，就有  $x_{0} + h \in D$ .

定义 15.2.1 设  $\boldsymbol{u} = \boldsymbol{f}(\boldsymbol{x})$  定义在开集  $D \subseteq R^{n}$  上， $x_{0} \in D$ . 如果存在  $m \times n$  常数矩阵

$$
\boldsymbol {A} = \left(a _ {i j}\right) _ {m \times n} = \left( \begin{array}{c c c} a _ {1 1} & \dots & a _ {1 n} \\ \vdots & & \vdots \\ a _ {m 1} & \dots & a _ {m n} \end{array} \right),
$$

其中 $\pmb{A}$ 的元素 $a_{ij}$ 仅依赖于 $\pmb{x}_0$ 但不依赖于 $\pmb{h}$, 使得当 $\| \pmb{h} \| \to 0$ 时, 如下关系式成立:

$$
\Delta f (x _ {0}) = f (x _ {0} + h) - f (x _ {0}) = A h + r (h),
$$

其中

$$
\lim _ {\boldsymbol {h} \to 0} \frac {\| \boldsymbol {r} (\boldsymbol {h}) \|}{\| \boldsymbol {h} \|} = 0, \tag {15.2.1}
$$

则称映射 $f$ 在点 $\pmb{x}_0$ 处可微, 又称可导, $A$ 称 $f$ 在点 $\pmb{x}_0$ 处的 Fréchet 导数或简称导数, 记为 $f'(x_0)$ 或 $Df(x_0)$, $Ah$ 称 $f$ 在点 $\pmb{x}_0$ 处的微分, 记为

$$
\mathrm{d} \boldsymbol {f} (\boldsymbol {x} _ {0}) = \boldsymbol {A} \boldsymbol {h} = \boldsymbol {f} ^ {\prime} (\boldsymbol {x} _ {0}) \boldsymbol {h} = D \boldsymbol {f} (\boldsymbol {x} _ {0}) \boldsymbol {h}.
$$

鉴于习惯上将 h 理解为自变量的差  $\Delta x$ ，所以把微分也常记为

$$
\mathrm{d} \boldsymbol {f} (\boldsymbol {x} _ {0}) = \boldsymbol {f} ^ {\prime} (\boldsymbol {x} _ {0}) \mathrm{d} \boldsymbol {x} = D \boldsymbol {f} (\boldsymbol {x} _ {0}) \mathrm{d} \boldsymbol {x}.
$$

---

15.2 映射的微分

259

如果 f 在 D 中任意一点处都可微, 则称 f 在 D 中可微.

可以看出, 如果 $m = 1$, 映射的微分就是多元函数的微分.

需要注意的是, 极限式 (15.2.1) 中分子  $\boldsymbol{r}(\boldsymbol{h})$  的范数是 m 维欧氏空间中的范数, 而分母 h 的范数是 n 维欧氏空间中的范数.

由映射可微的定义看出, 在可微点处, 映射增量的主要部分是一个线性映射 A 作用于向量 h. 下面我们具体讨论一下, 当 f 可微时, 矩阵 A 元素的确定. 下面的定理成立:

定理 15.2.1 设 D 是  $R^{n}$  中的开集,  $\boldsymbol{x}_{0} \in D$ ,  $\boldsymbol{f}(\boldsymbol{x}) = (f_{1}(\boldsymbol{x}), f_{2}(\boldsymbol{x}), \cdots, f_{m}(\boldsymbol{x}))^{\mathrm{T}}$  是在 D 上有定义的映射. 则  $\boldsymbol{f}(\boldsymbol{x})$  在点  $x_{0}$  处可微的充要条件是  $\forall j, 1 \leqslant j \leqslant m$ ,  $f_{j}(\boldsymbol{x})$  在点  $x_{0}$  处可微. 记

$$
J \boldsymbol {f} (\boldsymbol {x} _ {0}) = \left( \begin{array}{c c c c} \frac {\partial f _ {1} (\boldsymbol {x} _ {0})}{\partial \boldsymbol {x} _ {1}} & \frac {\partial f _ {1} (\boldsymbol {x} _ {0})}{\partial \boldsymbol {x} _ {2}} & \dots & \frac {\partial f _ {1} (\boldsymbol {x} _ {0})}{\partial \boldsymbol {x} _ {n}} \\ \frac {\partial f _ {2} (\boldsymbol {x} _ {0})}{\partial \boldsymbol {x} _ {1}} & \frac {\partial f _ {2} (\boldsymbol {x} _ {0})}{\partial \boldsymbol {x} _ {2}} & \dots & \frac {\partial f _ {2} (\boldsymbol {x} _ {0})}{\partial \boldsymbol {x} _ {n}} \\ \vdots & \vdots & & \vdots \\ \frac {\partial f _ {m} (\boldsymbol {x} _ {0})}{\partial \boldsymbol {x} _ {1}} & \frac {\partial f _ {m} (\boldsymbol {x} _ {0})}{\partial \boldsymbol {x} _ {2}} & \dots & \frac {\partial f _ {m} (\boldsymbol {x} _ {0})}{\partial \boldsymbol {x} _ {n}} \end{array} \right), \tag {15.2.2}
$$

则当 $f(x)$ 在 $\pmb{x}_0$ 处可微时，有

$$
\mathrm{d} \boldsymbol {f} (\boldsymbol {x}) = J \boldsymbol {f} (\boldsymbol {x} _ {0}) \mathrm{d} \boldsymbol {x},
$$

或者说

$$
\boldsymbol {f} ^ {\prime} (\boldsymbol {x} _ {0}) = J \boldsymbol {f} (\boldsymbol {x} _ {0}).
$$

定理的证明, 只需考虑到映射可微的定义与 $m$ 个 $n$ 元分量函数可微的定义之间的关系, 以及多元函数可微的充要条件即可得知矩阵 $\mathbf{A}$ 的元素必满足 $a_{ij} = \frac{\partial f_i}{\partial x_j} (\pmb{x}_0)$.

矩阵 (15.2.2) 称为映射 $f$ 在 $x_0$ 处的 Jacobi 矩阵$^{①}$, 这是一个 $m \times n$ 的矩阵. 所以对于一个可微映射, 它的导数就是它的 Jacobi 矩阵. 特别地, 多元函数作为向量值函数 $m = 1$ 的特殊情况, 此时的 Jacobi 矩阵就是多元函数的导数, 即梯度向量. 映射的另一个特殊情况是 $m = n$, 此时的 Jacobi 矩阵是一个 $n \times n$ 方阵, 对应的行列式称为映射的 Jacobi 行列式, 常记为

$$
\frac {\partial (f _ {1} , \cdots , f _ {n})}{\partial (x _ {1} , \cdots , x _ {n})}.
$$

类似于多元函数的结论: 偏导数连续蕴涵着可微. 对于映射的可微性, 下面定理成立, 证明完全类似于多元函数的情形, 故略之.

定理 15.2.2 如果定义在开集 $D \subseteq \mathbb{R}^n$ 上的映射 $f: D \to \mathbb{R}^m$ 的 Jacobi 矩阵 $Jf(x)$ 存在, 且 $Jf(x)$ 的各元素在点 $x_0$ 处连续, 则映射 $f$ 在点 $x_0$ 处可微.

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">① Jacobi, Carl Gustav Jacob, 1804 年 12 月 10 日—1851 年 2 月 18 日, 德国数学家.</span></small>

---

260

第十五章 多元函数微分学及其应用

类似于函数的光滑分类, 我们也可以引入映射的分类:

定义 15.2.2 设开集  $D \subseteq R^{n}$ ，映射  $f : D \to R^{m}$ 。如果 f 在 D 上的每一点都连续，则记  $f \subseteq C^{0}(D)$ ；如果 Jf 在 D 上的每一点都连续，则记  $f \subseteq C^{1}(D)$ 。

行文至此, 我们以下面的思考题结束本节: 设 $D \subseteq \mathbb{R}^n$ 是连通区域, $f: D \to \mathbb{R}^n$ 是可微映射, 问是否有类似一元函数导数的 Darboux 介值定理成立: 如果可微映射 $f$ 的 Jacobi 行列式在 $D$ 内处处不为零, 则它必在整个 $D$ 上是定号的 (注意, 这一结论对 $C^1$ 映射自然成立).

## 习题 15.2

1. 设

$$
f (x, y) = \left\{ \begin{array}{l l} \frac {x ^ {2} y}{x ^ {4} + y ^ {2}}, & x ^ {2} + y ^ {2} > 0, \\ 0, & x = y = 0. \end{array} \right.
$$

求证: 函数 $f$ 在原点处的各个方向导数存在, 但在原点处 $f$ 不可微.

2. 求证: 函数 $f(x, y) = \sqrt{|xy|}$ 在原点处不可微.

3. 求下列函数在指定点处的微分:

(1) $f(x,y) = x^{2} + 2xy - y^{2}$ 在点 $(1,2)$ 处.
(2) $f(x,y,z) = \ln (x + y - z) + \mathrm{e}^{x + y}\sin z$ 在点 $(1,2,1)$ 处.
(3) $u = \sqrt{t_1^2 + t_2^2 + \cdots + t_n^2}$ 在点 $(t_1, t_2, \cdots, t_n)$ 处, 其中 $t_1^2 + t_2^2 + \cdots + t_n^2 > 0$.
(4)  $u = \sin(x_{1}^{2} + x_{2}^{2} + \cdots + x_{n}^{2})$  在点  $(x_{1}, x_{2}, \cdots, x_{n})$  处.

4. 计算函数 $f$ 的 Jacobi 矩阵 $Jf$, 设:

(1) $f(x,y)=x^{2}y^{3}.$
(2) $f(x,y,z) = x^{2}y\sin (yz)$.
(3)  $f(x, y, z) = x \cos(y - 3z) + a \arcsin(xy).$
(4)  $f(x_{1}, x_{2}, \cdots, x_{n}) = (x_{1}^{2} + x_{2}^{2} + \cdots + x_{n}^{2})^{1/2}.$

5. 在指定点处计算下列映射的 Jacobi 矩阵和微分:

(1) $f(x,y)=(xy^{2}-3x^{2},3x-5y^{2})$, 在点 (1,-1) 处.
(2) $f(x,y,z)=(xy^{2}-4yz,3xy^{2}-y^{2}z)$ ，在点 $(1,-2,3)$ 处.
(3) $f(x,y)=(\mathrm{e}^{x}\cos(xy),\mathrm{e}^{x}\sin(xy))$, 在点 $\left(1,\frac{\pi}{2}\right)$ 处.

6. 计算下列映射的 Jacobi 矩阵:

(1)  $\boldsymbol{f}(r,\theta)=(r\cos\theta,r\sin\theta).$
(2)  $f(r, \theta, z) = (r \cos \theta, r \sin \theta, z).$
(3) $\boldsymbol{f}(r,\theta,\varphi)=(r\sin\theta\cos\varphi,r\sin\theta\sin\varphi,r\cos\theta).$

7. 设 $f: [a, b] \to \mathbb{R}^n$, 并且对一切 $t \in [a, b]$, 有 $\|f(t)\| =$ 常数. 求证 $\langle Jf, f \rangle = 0$,

---

15.3 多元函数求导 复合函数链式法则

261

并对此条件作几何解释.

8. 设 $\alpha, \beta, \gamma$ 为 $\mathbb{R}$ 上的连续函数, 求出一个由 $\mathbb{R}^3$ 到 $\mathbb{R}^3$ 的可微映射 $f$, 使得

$$
J \boldsymbol {f} (x, y, z) = \left( \begin{array}{c c c} \alpha (x) & 0 & 0 \\ 0 & \beta (y) & 0 \\ 0 & 0 & \gamma (z) \end{array} \right).
$$

9. 映射 $f: \mathbb{R}^n \to \mathbb{R}^m$，如果条件

$$
\boldsymbol {f} (\lambda \boldsymbol {x} + \mu \boldsymbol {y}) = \lambda \boldsymbol {f} (\boldsymbol {x}) + \mu \boldsymbol {f} (\boldsymbol {y})
$$

对一切 $x, y \in \mathbb{R}^n$ 和一切 $\lambda, \mu \in \mathbb{R}$ 成立, 则称 $f$ 是线性映射. 证明:

(1) $f(0)=0.$
(2) $f(-x) = -f(x), x \in \mathbb{R}^n.$
(3) 映射 f 由  $f(e_{1}), f(e_{2}), \cdots, f(e_{n})$  完全确定, 其中  $e_{1}, e_{2}, \cdots, e_{n}$  是  $R^{n}$  中的单位坐标向量.

10. 设  $f: R^{n} \rightarrow R^{m}$  为线性映射, 试求 Jf.

11. 设 $E: \mathbb{R}^n \to \mathbb{R}^n$ 满足: 对一切 $x \in \mathbb{R}^n$ 有 $E(x) = x$, 称 $E$ 为 $\mathbb{R}^n$ 中的恒同映射. 求证: $E$ 是一个线性映射, 并且 $JE = I_n$, 这里 $I_n$ 表示 $n$ 阶单位矩阵.

## 15.3 多元函数求导 复合函数链式法则

## 多元函数导数的四则运算

本节我们主要讨论多元函数或映射求偏导数的一些基本法则, 因此我们总假设所涉及的多元函数或映射的各个偏导数都存在. 我们以多元函数为主, 映射的情形读者可以根据具体情形给予类似的讨论. 根据前面的讨论, 我们知道, 多元函数的导数是一个向量, 映射的导数是一个矩阵. 我们有如下的求导法则.

定理 15.3.1 设  $f(\boldsymbol{x}), g(\boldsymbol{x})$  是在开集  $D \subseteq R^{n}$  上的两个可微的多元函数, 则  $\forall x \in D$ , 成立

(1) $(f(\pmb{x})\pm g(\pmb{x}))' = f'(\pmb{x})\pm g'(\pmb{x}).$
(2) $(f(\pmb {x})g(\pmb {x}))' = f(\pmb {x})g'(\pmb {x}) + f'(\pmb {x})g(\pmb {x}).$
(3) $\left(\frac{f(\boldsymbol{x})}{g(\boldsymbol{x})}\right)' = \frac{f'(\boldsymbol{x})g(\boldsymbol{x}) - f(\boldsymbol{x})g'(\boldsymbol{x})}{g^2(\boldsymbol{x})}\quad (g(\boldsymbol{x})\neq 0).$\]

上面 (1) 和 (2) 中, 如果 $f(x)$ 和 $g(x)$ 是 $D \subseteq \mathbb{R}^n$ 到 $\mathbb{R}^m$ 的可微映射, 则有

$(1') (f(x) \pm g(x))' = f'(x) \pm g'(x)$.

---

262

第十五章 多元函数微分学及其应用

$(2')\left(\boldsymbol{f}(\boldsymbol{x})\boldsymbol{g}(\boldsymbol{x})^{\mathrm{T}}\right)' = \boldsymbol{f}(\boldsymbol{x})(\boldsymbol{g}(\boldsymbol{x})^{\mathrm{T}})' + \boldsymbol{g}(\boldsymbol{x})(\boldsymbol{f}(\boldsymbol{x})^{\mathrm{T}})'$.

证明 我们以 (3) 为例给出证明, 其他法则的证明可以类似给出. 由定义知

$$
\left(\frac {f (\boldsymbol {x})}{g (\boldsymbol {x})}\right) ^ {\prime} = \left(\frac {\partial}{\partial x _ {1}} \left(\frac {f (\boldsymbol {x})}{g (\boldsymbol {x})}\right), \frac {\partial}{\partial x _ {2}} \left(\frac {f (\boldsymbol {x})}{g (\boldsymbol {x})}\right), \dots , \frac {\partial}{\partial x _ {n}} \left(\frac {f (\boldsymbol {x})}{g (\boldsymbol {x})}\right)\right). \tag {15.3.1}
$$

考虑到

$$
\frac {\partial}{\partial x _ {i}} \left(\frac {f (\boldsymbol {x})}{g (\boldsymbol {x})}\right) = \frac {1}{g ^ {2} (\boldsymbol {x})} \left(\frac {\partial f (\boldsymbol {x})}{\partial x _ {i}} g (\boldsymbol {x}) - f (\boldsymbol {x}) \frac {\partial g (\boldsymbol {x})}{\partial x _ {i}}\right) \quad (i = 1, 2, \dots , n),
$$

将上式代入 (15.3.1) 式即得 (3).

## 复合函数求导法则

我们可以利用微分研究向量值函数的复合求导.

定理 15.3.2 (复合求导) 设 D 和  $\Delta$  分别为  $R^{n}$  和  $R^{m}$  中的开集,  $f: D \rightarrow R^{m}$  和  $g: \Delta \rightarrow R^{l}$  为向量值函数, 且  $f(D) \subseteq \Delta$ . 如果 f 在  $x_{0} \in D$  处可微, g 在  $y_{0} = f(x_{0})$  处可微, 则复合函数  $h = g \circ f$  在  $x_{0}$  处可微, 且

$$
J \boldsymbol {h} (\boldsymbol {x} _ {0}) = J \boldsymbol {g} \circ \boldsymbol {f} (\boldsymbol {x} _ {0}) = J \boldsymbol {g} (\boldsymbol {y} _ {0}) \cdot J \boldsymbol {f} (\boldsymbol {x} _ {0}). \tag {15.3.2}
$$

证明 由 $f$ 在 $\pmb{x}_0$ 处可微可知, 在 $\pmb{x}_0$ 附近成立

$$
\boldsymbol {f} (\boldsymbol {x}) - \boldsymbol {f} \left(\boldsymbol {x} _ {0}\right) = J \boldsymbol {f} \left(\boldsymbol {x} _ {0}\right) \left(\boldsymbol {x} - \boldsymbol {x} _ {0}\right) + o \left(\| \boldsymbol {x} - \boldsymbol {x} _ {0} \|\right). \tag {15.3.3}
$$

这说明存在常数 $C$，使得 $\| \pmb{f}(\pmb{x}) - \pmb{f}(\pmb{x}_0) \| \leqslant C \| \pmb{x} - \pmb{x}_0\|$. 特别地，当 $\pmb{x} \to \pmb{x}_0$ 时 $\pmb{f}(\pmb{x}) \to \pmb{f}(\pmb{x}_0)$. 同理，$\pmb{g}$ 在 $\pmb{y}_0$ 处可微，故

$$
\boldsymbol {g} (\boldsymbol {y}) - \boldsymbol {g} \left(\boldsymbol {y} _ {0}\right) = J \boldsymbol {g} \left(\boldsymbol {y} _ {0}\right) \left(\boldsymbol {y} - \boldsymbol {y} _ {0}\right) + o \left(\| \boldsymbol {y} - \boldsymbol {y} _ {0} \|\right). \tag {15.3.4}
$$

在上式中代入 $\pmb{y} = \pmb{f}(\pmb{x})$ 可得

$$
\begin{array}{l} \boldsymbol {h} (\boldsymbol {x}) - \boldsymbol {h} \left(\boldsymbol {x} _ {0}\right) = J \boldsymbol {g} \left(\boldsymbol {y} _ {0}\right) \left(\boldsymbol {f} (\boldsymbol {x}) - \boldsymbol {f} \left(\boldsymbol {x} _ {0}\right)\right) + o \left(\| \boldsymbol {f} (\boldsymbol {x}) - \boldsymbol {f} \left(\boldsymbol {x} _ {0}\right) \|\right) \\ = \left(J \boldsymbol {g} \left(\boldsymbol {y} _ {0}\right) \cdot J \boldsymbol {f} \left(\boldsymbol {x} _ {0}\right)\right) \left(\boldsymbol {x} - \boldsymbol {x} _ {0}\right) + J \boldsymbol {g} \left(\boldsymbol {y} _ {0}\right) o \left(\| \boldsymbol {x} - \boldsymbol {x} _ {0} \|\right) + o \left(\| \boldsymbol {x} - \boldsymbol {x} _ {0} \|\right) \\ = \left(J \boldsymbol {g} (\boldsymbol {y} _ {0}) \cdot J \boldsymbol {f} (\boldsymbol {x} _ {0})\right) (\boldsymbol {x} - \boldsymbol {x} _ {0}) + o \left(\| \boldsymbol {x} - \boldsymbol {x} _ {0} \|\right), \\ \end{array}
$$

这说明 h 在  $x_{0}$  处可微, 且 (15.3.2) 式成立.

关系式(15.3.2) 可以写成分量的形式:

$$
\frac {\partial h _ {i}}{\partial x _ {j}} \left(\boldsymbol {x} _ {0}\right) = \sum_ {k = 1} ^ {m} \frac {\partial g _ {i}}{\partial y _ {k}} \left(\boldsymbol {y} _ {0}\right) \cdot \frac {\partial f _ {k}}{\partial x _ {j}} \left(\boldsymbol {x} _ {0}\right), i = 1, 2, \dots , l, j = 1, 2, \dots , n. \tag {15.3.5}
$$

这也就是所谓的链式法则.

如果在复合求导的定理 15.3.2 中, 有  $m = n = \ell$ , 那么所有环节中涉及的 Jacobi 矩阵均为方阵, 因此可以考虑 Jacobi 行列式, 我们可以得到下面分量形式的表述.

---

15.3 多元函数求导 复合函数链式法则

263

推论 15.3.3 若  $f_{1}, f_{2}, \cdots, f_{n}$  关于变量  $y_{1}, y_{2}, \cdots, y_{n}$  连续可微，而变量  $y_{1}, y_{2}, \cdots, y_{n}$  关于变量  $x_{1}, x_{2}, \cdots, x_{n}$  连续可微，则  $f_{1}, f_{2}, \cdots, f_{n}$  关于变量  $x_{1}, x_{2}, \cdots, x_{n}$  也连续可微，且成立

$$
\frac {\partial (f _ {1} , f _ {2} , \cdots , f _ {n})}{\partial (x _ {1} , x _ {2} , \cdots , x _ {n})} = \frac {\partial (f _ {1} , f _ {2} , \cdots , f _ {n})}{\partial (y _ {1} , y _ {2} , \cdots , y _ {n})} \cdot \frac {\partial (y _ {1} , y _ {2} , \cdots , y _ {n})}{\partial (x _ {1} , x _ {2} , \cdots , x _ {n})}.
$$

推论 15.3.4 设  $\sigma:(a,b)\to\mathbb{R}^{n}$  为向量值函数, 写成分量的形式为

$$
\boldsymbol {\sigma} (t) = \left(x _ {1} (t), \dots , x _ {n} (t)\right), \quad t \in (a, b).
$$

设 $\sigma(t)$ 的每一个分量都在 $t_0$ 处可导, 且多元函数 $f$ 在 $x_0 = \sigma(t_0)$ 处可微, 则复合函数 $f \circ \sigma$ 在 $t_0$ 处可导, 且

$$
\left(f \circ \boldsymbol {\sigma}\right) ^ {\prime} (t _ {0}) = \nabla f (\boldsymbol {x} _ {0}) \cdot \boldsymbol {\sigma} ^ {\prime} (t _ {0}), \tag {15.3.6}
$$

其中  $\boldsymbol{\sigma}^{\prime}(t_{0})=\left(x_{1}^{\prime}(t_{0}),\cdots,x_{n}^{\prime}(t_{0})\right)$ .

例 15.3.1 设  $f(x,y)$  可微,  $\varphi(x)$  可微, 求  $u = f(x, \varphi(x))$  关于 x 的导数.

解 由链式法则，

$$
\begin{array}{l} u _ {x} = f _ {x} (x, \varphi (x)) \cdot x _ {x} + f _ {y} (x, \varphi (x)) \cdot \varphi^ {\prime} (x) \\ = f _ {x} (x, \varphi (x)) + f _ {y} (x, \varphi (x)) \cdot \varphi^ {\prime} (x). \\ \end{array}
$$

![](../../raw/pages_0561-0576/images/page_567_image_12.jpg)

注 15.3.1 例 15.3.1 中的二元函数 $u = f(s, t)$ 经过复合 $s = s(x), t = t(x)$ 后, 最终得到的本质上是 $x$ 的一元函数, 此时 $u$ 关于 $x$ 的导数 (如果中间每个环节均可导的话), 常称为 $u$ 对 $x$ 的全导数. 全导数可以理解为对一元函数导数概念的完善, 它反映出所有中间变量对函数做出的总贡献这一基本思想.

例 15.3.2 设  $u = f(x, y)$  可微,  $x = r \cos \theta$ ,  $y = r \sin \theta$ , 证明:

$$
\left(\frac {\partial u}{\partial x}\right) ^ {2} + \left(\frac {\partial u}{\partial y}\right) ^ {2} = \left(\frac {\partial u}{\partial r}\right) ^ {2} + \frac {1}{r ^ {2}} \left(\frac {\partial u}{\partial \theta}\right) ^ {2}.
$$

证明 由链式法则，

$$
\begin{array}{l} \frac {\partial u}{\partial r} = \frac {\partial u}{\partial x} \cdot \frac {\partial x}{\partial r} + \frac {\partial u}{\partial y} \cdot \frac {\partial y}{\partial r} = \frac {\partial u}{\partial x} \cos \theta + \frac {\partial u}{\partial y} \sin \theta , \\ \frac {\partial u}{\partial \theta} = \frac {\partial u}{\partial x} \cdot \frac {\partial x}{\partial \theta} + \frac {\partial u}{\partial y} \cdot \frac {\partial y}{\partial \theta} = - r \frac {\partial u}{\partial x} \sin \theta + r \frac {\partial u}{\partial y} \cos \theta. \\ \end{array}
$$

这说明

$$
\begin{array}{l} \left(\frac {\partial u}{\partial r}\right) ^ {2} + \frac {1}{r ^ {2}} \left(\frac {\partial u}{\partial \theta}\right) ^ {2} = \left(\frac {\partial u}{\partial x} \cos \theta + \frac {\partial u}{\partial y} \sin \theta\right) ^ {2} + \left(- \frac {\partial u}{\partial x} \sin \theta + \frac {\partial u}{\partial y} \cos \theta\right) ^ {2} \\ = \left(\frac {\partial u}{\partial x}\right) ^ {2} + \left(\frac {\partial u}{\partial y}\right) ^ {2}. \\ \end{array}
$$

![](../../raw/pages_0561-0576/images/page_567_image_20.jpg)

---

264

第十五章 多元函数微分学及其应用

例15.3.3 设 $z = f(u, v, w)$, $v = \varphi(u, s)$, $s = \psi(u, w)$, 求 $\frac{\partial z}{\partial u}, \frac{\partial z}{\partial w}$.

解 按照定义,

$$
z = f (u, v, w) = f (u, \varphi (u, s), w) = f (u, \varphi (u, \psi (u, w)), w).
$$

由链式法则，

$$
\begin{array}{l} \frac {\partial z}{\partial u} = \frac {\partial f}{\partial u} + \frac {\partial f}{\partial v} \cdot \frac {\partial v}{\partial u} = \frac {\partial f}{\partial u} + \frac {\partial f}{\partial v} \cdot \left(\frac {\partial \varphi}{\partial u} + \frac {\partial \varphi}{\partial s} \cdot \frac {\partial s}{\partial u}\right) \\ = \frac {\partial f}{\partial u} + \frac {\partial f}{\partial v} \cdot \frac {\partial \varphi}{\partial u} + \frac {\partial f}{\partial v} \cdot \frac {\partial \varphi}{\partial s} \cdot \frac {\partial \psi}{\partial u}, \\ \frac {\partial z}{\partial w} = \frac {\partial f}{\partial w} + \frac {\partial f}{\partial v} \cdot \frac {\partial v}{\partial w} = \frac {\partial f}{\partial w} + \frac {\partial f}{\partial v} \left(\frac {\partial \varphi}{\partial s} \cdot \frac {\partial s}{\partial w}\right) \\ = \frac {\partial f}{\partial w} + \frac {\partial f}{\partial v} \cdot \frac {\partial \varphi}{\partial s} \cdot \frac {\partial \psi}{\partial w}. \\ \end{array}
$$

$$
\begin{array}{l} \frac {\partial z}{\partial w} = \frac {\partial f}{\partial w} + \frac {\partial f}{\partial v} \cdot \frac {\partial v}{\partial w} = \frac {\partial f}{\partial w} + \frac {\partial f}{\partial v} \left(\frac {\partial \varphi}{\partial s} \cdot \frac {\partial s}{\partial w}\right) \\ = \frac {\partial f}{\partial w} + \frac {\partial f}{\partial v} \cdot \frac {\partial \varphi}{\partial s} \cdot \frac {\partial \psi}{\partial w}. \\ \end{array}
$$

定理 15.3.2 有如下  $C^{1}$  版本的结论. 我们仅以二元函数为例, 显然结论对 n 元复合函数也成立.

定理 15.3.5 如果函数  $\varphi(s,t)$ ,  $\psi(s,t)$  关于 s, t 连续可微, 并且函数  $f(x,y)$  在 D 上关于 x, y 连续可微, 那么复合函数  $f(\varphi(s,t),\psi(s,t))$  关于 s, t 连续可微.

证明 由定理15.3.2知 $f(\varphi (s,t),\psi (s,t))$ 关于 $s,t$ 都可求偏导，且

$$
\begin{array}{l} \frac {\partial}{\partial s} f (\varphi , \psi) = f _ {x} (\varphi , \psi) \varphi_ {s} (s, t) + f _ {y} (\varphi , \psi) \psi_ {s} (s, t), \\ \frac {\partial}{\partial t} f (\varphi , \psi) = f _ {x} (\varphi , \psi) \varphi_ {t} (s, t) + f _ {y} (\varphi , \psi) \psi_ {t} (s, t), \\ \end{array}
$$

其中 $\varphi = \varphi(s, t), \psi = \psi(s, t)$. 根据假设, $f_x(x, y)$ 和 $f_y(x, y)$ 是变量 $x, y$ 的连续函数, 故 $f_x(\varphi(s, t), \psi(s, t))$ 和 $f_y(\varphi(s, t), \psi(s, t))$ 是 $s, t$ 的连续函数, 又由于 $\varphi_s(s, t), \psi_s(s, t), \varphi_t(s, t), \psi_t(s, t)$ 都是连续函数, 因此 $\frac{\partial f}{\partial s}(\varphi, \psi), \frac{\partial f}{\partial t}(\varphi, \psi)$ 是变量 $x, y$ 的连续函数, 即 $f(\varphi, \psi)$ 是 $C^1$ 的.

## 复合函数的高阶偏导数

理论上我们可以把定理 15.3.5 关于复合函数  $C^{1}$  版本的结论推广到更一般的情形. 我们还是以二元函数为例, 不加证明地提供下面的结论.

定理 15.3.6 如果函数  $\varphi(s,t)$ ,  $\psi(s,t)$  关于 s, t 是 n 阶连续可微的, 并且函数  $f(x,y)$  在 D 上关于 x, y 是 n 阶连续可微的, 那么复合函数  $f(\varphi(s,t),\psi(s,t))$  关于 s, t 也是 n 阶连续可微的.

推论15.3.7 如果函数 $\varphi(s, t)$, $\psi(s, t)$ 是关于 $s, t$ 的 $C^\infty$ 连续可微函数, 并且函数 $f(x, y)$ 是 $D$ 上关于 $x, y$ 的 $C^\infty$ 连续可微函数, 那么复合函数 $f(\varphi(s, t), \psi(s, t))$ 也是关于 $s, t$ 的 $C^\infty$ 连续可微函数.

复合函数的高阶偏导数的计算, 可以依据求偏导的法则逐步递推, 然而很难给出一般性的公式或者表达. 我们仅以例子来演示一下高阶偏导数的求法.

---

15.3 多元函数求导 复合函数链式法则

265

我们以二元函数为例. 设 $u = f(x, y)$, $x = \varphi(s, t)$, $y = \psi(s, t)$, 并设所有涉及的函数均具有二阶连续偏导数. 则有

$$
\frac {\partial u}{\partial s} = \frac {\partial f}{\partial x} \frac {\partial \varphi}{\partial s} + \frac {\partial f}{\partial y} \frac {\partial \psi}{\partial s},
$$

$$
\frac {\partial^ {2} u}{\partial s ^ {2}} = \frac {\partial^ {2} f}{\partial x ^ {2}} \left(\frac {\partial \varphi}{\partial s}\right) ^ {2} + 2 \frac {\partial^ {2} f}{\partial x \partial y} \frac {\partial \varphi}{\partial s} \frac {\partial \psi}{\partial s} + \frac {\partial f}{\partial x} \frac {\partial^ {2} \varphi}{\partial s ^ {2}} + \frac {\partial^ {2} f}{\partial y ^ {2}} \left(\frac {\partial \psi}{\partial s}\right) ^ {2} + \frac {\partial f}{\partial y} \frac {\partial^ {2} \psi}{\partial s ^ {2}}.
$$

类似可以计算  $\frac{\partial u}{\partial t}, \frac{\partial^{2}u}{\partial t^{2}}, \frac{\partial^{2}u}{\partial s\partial t}$  等.

例15.3.4 设 $u = f(r), r = \sqrt{x^2 + y^2 + z^2}$, 假设 $u$ 满足Laplace方程

$$
\Delta u := \frac {\partial^ {2} u}{\partial x ^ {2}} + \frac {\partial^ {2} u}{\partial y ^ {2}} + \frac {\partial^ {2} u}{\partial z ^ {2}} = 0,
$$

试求  $f(r)$ .

解 由 $\frac{\partial u}{\partial x} = f'(r)\frac{x}{r}$, 可得 $\frac{\partial^2u}{\partial x^2} = f''(r)\frac{x^2}{r^2} + f'(r)\frac{r^2 - x^2}{r^3}$. 同理可得

$$
\frac {\partial^ {2} u}{\partial y ^ {2}} = f ^ {\prime \prime} (r) \frac {y ^ {2}}{r ^ {2}} + f ^ {\prime} (r) \frac {r ^ {2} - y ^ {2}}{r ^ {3}}, \quad \frac {\partial^ {2} u}{\partial z ^ {2}} = f ^ {\prime \prime} (r) \frac {z ^ {2}}{r ^ {2}} + f ^ {\prime} (r) \frac {r ^ {2} - z ^ {2}}{r ^ {3}}.
$$

因此有

$$
\Delta u = f ^ {\prime \prime} (r) + \frac {2}{r} f ^ {\prime} (r) = 0,
$$

即

$$
\left(r ^ {2} f ^ {\prime} (r)\right) ^ {\prime} = r ^ {2} f ^ {\prime \prime} (r) + 2 r f ^ {\prime} (r) = r ^ {2} \Delta u = 0.
$$

故有

$$
f ^ {\prime} (r) = \frac {c}{r ^ {2}},
$$

其中 $c$ 是常数. 两端求不定积分得

$$
f (r) = \frac {c}{r} + c _ {1},
$$

因此

$$
u = \frac {c}{\sqrt {x ^ {2} + y ^ {2} + z ^ {2}}} + c _ {1},
$$

其中 c 和  $c_{1}$  均为常数.

## 多元函数一阶微分形式不变性

我们知道对于一元函数, 在函数的复合运算中, 一阶微分具有形式不变性. 下面我们指出, 对于多元函数, 仍然成立一阶微分形式不变性, 即在计算函数的全微分时, 无论该函数的自变量、因变量还是中间变量是什么, 其全微分的形式保持不变. 这是数学分析中的一条极其重要的性质, 它使得我们不必区分变量的类型, 即自变量、因变量或中

---

266

第十五章 多元函数微分学及其应用

间变量, 而直接利用一元函数的微分性质进行计算, 从而简化了多元函数微分学的处理过程.

设  $f(\boldsymbol{u}) = f(u_{1}, u_{2}, \cdots, u_{m})$  在开集  $D \subseteq R^{m}$  可微，则  $f(\boldsymbol{u})$  的微分为

$$
\mathrm{d} f (\boldsymbol {u}) = f ^ {\prime} (\boldsymbol {u}) \mathrm{d} \boldsymbol {u}.
$$

此时, $u$ 是自变量. 现在设

$$
\boldsymbol {u} = (u _ {1} (\boldsymbol {x}), u _ {2} (\boldsymbol {x}), \dots , u _ {m} (\boldsymbol {x})) ^ {\mathrm{T}}
$$

是开集 $\Delta \subseteq \mathbb{R}^n$ 内的一个 $n$ 元可微向量值函数, 并且 $\pmb{u}(\Delta) \subseteq D$, 则复合函数 $f(\pmb{u}(\pmb{x}))$ 在 $\Delta$ 中可微, 从而有

$$
\mathrm{d} f (\boldsymbol {u} (\boldsymbol {x})) = f ^ {\prime} (\boldsymbol {u} (\boldsymbol {x})) \boldsymbol {u} ^ {\prime} (\boldsymbol {x}) \mathrm{d} \boldsymbol {x}.
$$

注意到

$$
\mathrm{d} \boldsymbol {u} = (u _ {1} ^ {\prime} (\boldsymbol {x}), u _ {2} ^ {\prime} (\boldsymbol {x}), \dots , u _ {m} ^ {\prime} (\boldsymbol {x})) ^ {\mathrm{T}} \mathrm{d} \boldsymbol {x} = \boldsymbol {u} ^ {\prime} (\boldsymbol {x}) \mathrm{d} \boldsymbol {x},
$$

因此, 当 u 为中间变量时, 仍然有

$$
\mathrm{d} f (\boldsymbol {u}) = f ^ {\prime} (\boldsymbol {u} (\boldsymbol {x})) \boldsymbol {u} ^ {\prime} (\boldsymbol {x}) \mathrm{d} \boldsymbol {x} = f ^ {\prime} (\boldsymbol {u}) \mathrm{d} \boldsymbol {u}.
$$

例15.3.5 若 $m$ 元函数 $f$ 满足

$$
f \left(t x _ {1}, t x _ {2}, \dots , t x _ {m}\right) = t ^ {n} f \left(x _ {1}, x _ {2}, \dots , x _ {m}\right), \tag {15.3.7}
$$

则称 f 为 n 次齐次函数.

证明: 若 m 元函数  $f(x_{1}, x_{2}, \cdots, x_{m})$  是开集  $D \subseteq R^{m}$  上的可微函数, 则 f 满足 Euler 方程

$$
\sum_ {k = 1} ^ {m} \frac {\partial f}{\partial x _ {k}} \cdot x _ {k} = n f.
$$

证明 根据齐次函数的定义,

$$
f \left(t x _ {1}, t x _ {2}, \dots , t x _ {m}\right) = f \left(u _ {1}, u _ {2}, \dots , u _ {m}\right) = t ^ {n} f \left(x _ {1}, x _ {2}, \dots , x _ {m}\right).
$$

对其定义关系式两边关于 t 求导, 有

$$
\sum_ {k = 1} ^ {m} \frac {\partial f (t x _ {1} , t x _ {2} , \cdots , t x _ {m})}{\partial u _ {k}} \cdot x _ {k} = n t ^ {n - 1} f (x _ {1}, x _ {2}, \dots , x _ {m}).
$$

令 $t = 1$ ，有

$$
\sum_ {k = 1} ^ {m} \frac {\partial f}{\partial x _ {k}} \cdot x _ {k} = n f,
$$

---

15.3 多元函数求导 复合函数链式法则

267

得证.

有兴趣的读者可以进一步证明下面结论成立:

如果 n 次齐次函数  $f(x_{1}, x_{2}, \cdots, x_{m})$  是  $C^{2}$  的, 则对所有的  $k = 1, 2, \cdots, m$ , 都有  $f_{x_{k}}$  是 n - 1 次齐次函数, 满足

$$
\sum_ {i = 1} ^ {m} \frac {\partial}{\partial x _ {i}} (f _ {x _ {k}}) \cdot x _ {i} = (n - 1) f _ {x _ {k}}.
$$

即, n 次齐次函数的每一项偏导数都是 n-1 次齐次函数.

试问,能否给出进一步的递推?

齐次函数的概念还可以推广到拟齐次或加权齐次, 即权重不同的齐次. 以二元函数为例, 若函数  $f(x_{1}, x_{2})$  满足

$$
f \left(t ^ {p} x _ {1}, t ^ {q} x _ {2}\right) = t ^ {n} f \left(x _ {1}, x _ {2}\right), \tag {15.3.8}
$$

则称 $f$ 为 $(p,q)$-$n$ 次拟齐次函数. 那么, 可以证明: 若可微函数 $f(x_1, x_2)$ 是开集 $D \subseteq \mathbb{R}^2$ 上的 $(p,q)$-$n$ 次拟齐次函数, 则 $f$ 满足 Euler 方程

$$
p x _ {1} \frac {\partial f}{\partial x _ {1}} + q x _ {2} \frac {\partial f}{\partial x _ {2}} = n f (x _ {1}, x _ {2}). \tag {15.3.9}
$$

## 高阶微分

设 $D \subseteq \mathbb{R}^n$ 为开集, 函数 $f(\pmb{x})$ 在 $\pmb{x} \in D$ 可微, 即有

$$
\mathrm{d} f (\boldsymbol {x}) = \sum_ {i = 1} ^ {n} \frac {\partial f (\boldsymbol {x})}{\partial x _ {i}} \mathrm{d} x _ {i}.
$$

若 $\forall i, 1 \leqslant i \leqslant n, f_{x_i}$ 仍是可微函数, 则称

$$
\sum_ {i = 1} ^ {n} \Big (\sum_ {k = 1} ^ {n} \frac {\partial^ {2} f (\boldsymbol {x})}{\partial x _ {k} \partial x _ {i}} \mathrm{d} x _ {k} \Big) \mathrm{d} x _ {i}
$$

为 $f(\pmb{x})$ 的二阶微分, 并记为 $\mathrm{d}^2 f(\pmb{x})$, 即

$$
\mathrm{d} ^ {2} f (\boldsymbol {x}) = \sum_ {i = 1} ^ {n} \sum_ {k = 1} ^ {n} \frac {\partial^ {2} f (\boldsymbol {x})}{\partial x _ {k} \partial x _ {i}} \mathrm{d} x _ {k} \mathrm{d} x _ {i}.
$$

类似地, 我们可以引入函数 $f$ 的 $k$ 阶微分. 并且, 如果引入形式上的记号

$$
\mathrm{d} f (\boldsymbol {x}) = \Big (\sum_ {i = 1} ^ {n} \mathrm{d} x _ {i} \frac {\partial}{\partial x _ {i}} \Big) f (\boldsymbol {x}),
$$

$$
\mathrm{d} ^ {2} f (\boldsymbol {x}) = \sum_ {i = 1} ^ {n} \sum_ {k = 1} ^ {n} \mathrm{d} x _ {k} \mathrm{d} x _ {i} \frac {\partial^ {2}}{\partial x _ {k} \partial x _ {i}} f (\boldsymbol {x}) = \left(\sum_ {i = 1} ^ {n} \mathrm{d} x _ {i} \frac {\partial}{\partial x _ {i}}\right) ^ {2} f (\boldsymbol {x}),
$$

---

268

第十五章 多元函数微分学及其应用

等等, 那么, 当 $f(\pmb{x}) \in C^{k}(D)$ 时, 可以将 $k$ 阶微分记为

$$
\mathrm{d} ^ {k} f (\boldsymbol {x}) = \Big (\sum_ {i = 1} ^ {n} \mathrm{d} x _ {i} \frac {\partial}{\partial x _ {i}} \Big) ^ {k} f (\boldsymbol {x}).
$$

上述记号对于高阶微分来说很方便记忆, 因为这个记号形式上对应着二项式定理推广时的表达式. 请对比下面的多项式展开, 读者可以自行补充其证明.

命题 15.3.8 对于两个自然数 k 和 n, 成立

$$
(x _ {1} + \dots + x _ {n}) ^ {k} = \sum_ {\alpha_ {1} + \dots + \alpha_ {n} = k} \frac {k !}{\alpha_ {1} ! \cdots \alpha_ {n} !} x _ {1} ^ {\alpha_ {1}} \dots x _ {n} ^ {\alpha_ {n}},
$$

其中  $x_{i}$  为实数,  $\alpha_{i}$  为非负整数.

在本节最后, 也可以考虑多元函数复合函数的高阶微分, 但是我们知道在一元函数微分中, 二阶以上的微分已不再具有形式不变性, 因此多元函数情形也不可能具有高阶微分的形式不变性.

## 习题15.3

1. 设 $f(x, y, z) = F(u, v, w)$，其中 $x^2 = vw, y^2 = wu, z^2 = uv$. 求证:

$$
x \frac {\partial f}{\partial x} + y \frac {\partial f}{\partial y} + z \frac {\partial f}{\partial z} = u \frac {\partial F}{\partial u} + v \frac {\partial F}{\partial v} + w \frac {\partial F}{\partial w}.
$$

2. 设有函数 $f(x, y, z)$, $u$ 是一个方向, 函数 $f$ 沿方向 $u$ 的方向导数记作 $\frac{\partial f}{\partial u}$, 设 $e_1, e_2, e_3$ 是 $\mathbb{R}^3$ 中的三个互相垂直的方向, 求证:

$$
\left(\frac {\partial f}{\partial \boldsymbol {e} _ {1}}\right) ^ {2} + \left(\frac {\partial f}{\partial \boldsymbol {e} _ {2}}\right) ^ {2} + \left(\frac {\partial f}{\partial \boldsymbol {e} _ {3}}\right) ^ {2} = \left(\frac {\partial f}{\partial x}\right) ^ {2} + \left(\frac {\partial f}{\partial y}\right) ^ {2} + \left(\frac {\partial f}{\partial z}\right) ^ {2}.
$$

3. 求复合函数 $f \circ g$ 在指定点的 Jacobi 矩阵:

(1) $\boldsymbol{f}(x,y)=(xy,x^{2}y),\boldsymbol{g}(s,t)=(s+t,s^{2}-t^{2})$ ，在点 $(s,t)=(2,1)$ .
(2) $\boldsymbol{f}(x,y)=(\mathrm{e}^{x+2y},\sin(y+2x))$, $\boldsymbol{g}(u,v,w)=(u+2v^{2}+3w^{3},2v-u^{2})$, 在点 $(u,v,w)=(1,-1,1)$.
(3) $\boldsymbol{f}(x,y,z)=(x+y+z,xy,x^{2}+y^{2}+z^{2}),\boldsymbol{g}(u,v,w)=(\mathrm{e}^{v^{2}+u^{2}},\sin(uw),\sqrt{uv})$，在点 $(u,v,w)=(2,1,3)$.

4. 设 $D$ 为 $\mathbb{R}^n$ 中的区域, $f$ 在 $D$ 中处处可微. 如果 $\mathrm{d}f = 0$, 证明: $f$ 为常值函数.

5. 证明: 如果 $u(x, y)$ 满足方程 $\Delta u = \frac{\partial^2 u}{\partial x^2} + \frac{\partial^2 u}{\partial y^2} = 0$, 则 $v(x, y) = u(x^2 - y^2, 2xy)$ 和 $w(x, y) = u\left(\frac{x}{x^2 + y^2}, \frac{y}{x^2 + y^2}\right)$ 也满足此方程.

---

15.4 微分中值定理

269

6. 证明: 函数

$$
u (x, t) = \frac {1}{2 a \sqrt {\pi t}} \mathrm{e} ^ {- \frac {(x - b) ^ {2}}{4 a ^ {2} t}}
$$

满足方程

$$
\frac {\partial u}{\partial t} = a ^ {2} \frac {\partial^ {2} u}{\partial x ^ {2}}.
$$

7. 设 $F(x, y) \in C^{1}(\mathbb{R}^{2})$, 具有形式 $F(x, y) = f(x)g(y)$. 假设在极坐标系中 $F$ 可写为 $F(r\cos \theta, r\sin \theta) = h(r)$. 又假设若 $F(x, y)$ 无零点, 试求 $F(x, y)$.

8. 设 $\varphi, \psi$ 均为 $C^2$ 函数, 验证: $u = \varphi\left(\frac{y}{x}\right) + y\psi\left(\frac{y}{x}\right)$ 满足微分方程

$$
x ^ {2} \frac {\partial^ {2} u}{\partial x ^ {2}} + 2 x y \frac {\partial^ {2} u}{\partial x \partial y} + y ^ {2} \frac {\partial^ {2} u}{\partial y ^ {2}} = 0.
$$

9. 设 $f$ 为多元函数, 其偏导数均连续, 求在给定的任何一点处方向导数的最大值和最小值.

10. 设 $f_{x}$ 和 $f_{y}$ 在 $(x_0, y_0)$ 处可微, 证明: $f_{xy}(x_0, y_0) = f_{yx}(x_0, y_0)$.

## 15.4 微分中值定理

一元函数微分学中的一个重要性质是微分中值定理, 它们在数学分析中有深刻的影响和广泛的应用. 对于多元函数, 也有相应的结论. 我们先简要回顾一下 $\mathbb{R}^n$ 中凸集的概念:

设开集 $D \subseteq \mathbb{R}^n$, 如果 $\forall x, y \in D$, 都有 $\overline{xy} = \{\theta x + (1 - \theta)y | \theta \in [0,1]\} \subseteq D$, 则称 $D$ 是 $\mathbb{R}^n$ 中的开的凸集, 又称凸域.

定理 15.4.1 (多元函数微分中值定理) 设  $D \subseteq R^{n}$  为凸域, 函数  $f : D \to R$  在 D 中处处可微. 则任给  $x, y \in D$ , 存在  $\theta \in (0,1)$ , 使得

$$
f (\boldsymbol {x}) - f (\boldsymbol {y}) = \nabla f (\boldsymbol {\xi}) \cdot (\boldsymbol {x} - \boldsymbol {y}), \quad \boldsymbol {\xi} = \theta \boldsymbol {x} + (1 - \theta) \boldsymbol {y}. \tag {15.4.1}
$$

证明 令 $\sigma(t) = t\boldsymbol{x} + (1 - t)\boldsymbol{y}$, 由 $D$ 为凸域可知当 $t \in [0,1]$ 时 $\sigma(t) \in D$. 对一元函数 $\varphi(t) = f \circ \sigma(t)$, 一方面显然有 $\varphi(1) = f(\boldsymbol{x}), \varphi(0) = f(\boldsymbol{y})$, 另一方面, 由微分中值定理可知存在 $\theta \in (0,1)$, 使得 $\varphi(1) - \varphi(0) = \varphi'(\theta)$. 再由 (15.3.6) 式可得

$$
\varphi (1) - \varphi (0) = \nabla f (\boldsymbol {\xi}) \cdot \boldsymbol {\sigma} ^ {\prime} (\theta) = \nabla f (\boldsymbol {\xi}) \cdot (\boldsymbol {x} - \boldsymbol {y}),
$$

其中  $\boldsymbol{\xi}=\boldsymbol{\sigma}(\theta)=\theta\boldsymbol{x}+(1-\theta)\boldsymbol{y}$ . 结论得证.

如果把定理 15.4.1 类比于 Lagrange 微分中值定理的话, 那么下面的推论则对应着一元函数的 Rolle 微分中值定理, 而证明的基本思想与一元函数的 Fermat 引理如出一

---

270

第十五章 多元函数微分学及其应用

辙: 有界闭区域上的连续函数必能取到最大、最小值, 而且在极值点处函数如果可微, 则梯度为零. 作为练习, 详细证明留给读者.

设 $r > 0$ ，记

$$
\overline {{B _ {r} (\boldsymbol {x} _ {0})}} = \{\boldsymbol {x} \in \mathbb {R} ^ {n} | \| \boldsymbol {x} - \boldsymbol {x} _ {0} \| \leqslant r \},
$$

$$
B _ {r} (\boldsymbol {x} _ {0}) = \{\boldsymbol {x} \in \mathbb {R} ^ {n} | \| \boldsymbol {x} - \boldsymbol {x} _ {0} \| <   r \},
$$

$$
\partial \overline {{B _ {r} \left(\boldsymbol {x} _ {0}\right)}} = \left\{\boldsymbol {x} \in \mathbb {R} ^ {n} \mid \| \boldsymbol {x} - \boldsymbol {x} _ {0} \| = r \right\}.
$$

推论 15.4.2 设  $x_{0} \in R^{n}, u = f(x)$  是定义在  $\overline{B_{r}(x_{0})}$  上的 n 元函数, 满足下列条件:

(1) $f(\pmb{x})$ 在 $\overline{B_r(\pmb{x_0})}$ 上连续.
(2) $f(\pmb{x})$ 在 $\overline{B_r(\pmb{x_0})}$ 的内部 $B_{r}(\pmb{x}_{0})$ 可微.
(3) $f(\pmb{x})$ 在 $\overline{B_r(\pmb{x_0})}$ 的边界 $\partial \overline{B_r(\pmb{x_0})}$ 上取常值.

则 f 在  $\overline{B_{r}(\boldsymbol{x}_{0})}$  内部至少存在一点  $\xi$  使得  $f'(\boldsymbol{\xi}) = 0$ .

该推论有明确的几何意义.比如以 $n = 2$ 为例，则推论说明如果二元函数 $f(x,y)$ 给出的曲面 $z = f(x,y)$ 在自变量取值的圆盘上连续，圆盘内可微，边界上的值相等，则圆盘内一定有一点，在此点处曲面的切平面平行于 $xOy$ 坐标平面.从几何上看，下面的结论是推论15.4.2的一般化，也是定理15.4.1的特殊情况.

推论 15.4.3 设  $u = f(x, y)$  是定义在  $\overline{B_{r}(\boldsymbol{x}_{0})} (r > 0)$  上的二元函数，其中  $\boldsymbol{x}_{0} = (x_{0}, y_{0})$ ，满足下列条件:

(1)  $f(x,y)$  在  $\overline{B_{r}(\boldsymbol{x}_{0})}$  上连续.
(2)  $f(x,y)$  在  $B_{r}(\boldsymbol{x}_{0})$  内可微.
(3) 曲面 $z = f(x, y)$ 在 $\partial \overline{B_r(x_0)}$ 上的点都落在同一个平面 $\pi: z = ax + by + c$ 上. 则 $f$ 在 $\overline{B_r(x_0)}$ 内部至少存在一点 $\xi$ 使得 $f'(\xi) = (a, b)$.

下面我们讨论一下多元函数的微分中值定理能否推广到更一般的映射. 首先, 下面的例子表明, 推论 15.4.2 的形式上的结论对于映射来讲, 一般不再成立.

例 15.4.1 设  $f: \overline{B_{1}(0)} \rightarrow R^{2}$ ，其中  $\mathbf{0} = (0, 0)$ ，具有形式

$$
\boldsymbol {f} (x, y) = \big (x (x ^ {2} + y ^ {2} - 1), y (x ^ {2} + y ^ {2} - 1) \big).
$$

则 $f$ 满足推论15.4.2中的三个相应的条件:

(1)  $f(x,y)$  在  $\overline{B_{1}(\mathbf{0})}$  上连续.
(2)  $f(x,y)$  在  $\overline{B_{1}(\mathbf{0})}$  的内部  $B_{1}(\mathbf{0})$  可微.

(3) $f(x,y)$ 在 $\overline{B_1(\mathbf{0})}$ 的边界 $\partial \overline{B_1(\mathbf{0})}$ 上取常向量 $\mathbf{0} = (0,0)$. 但是, $f(x,y)$ 的导数 $f'(x,y)$, 即 Jacobi 矩阵

$$
\boldsymbol {f} ^ {\prime} (x, y) = \left( \begin{array}{c c} 3 x ^ {2} + y ^ {2} - 1 & 2 x y \\ 2 x y & x ^ {2} + 3 y ^ {2} - 1 \end{array} \right)
$$

---

15.4 微分中值定理

271

对于任意的  $(x,y)\in B_{1}(\mathbf{0})$  都不可能为零矩阵.

此例说明, 对于映射而言, 微分中值定理纯形式的照搬是不成立的. 事实上, 简单的分析可以看出下面的情景:

设 $D \subseteq \mathbb{R}^n$ 为凸域, $\pmb{f}: D \to \mathbb{R}^m$ 为一映射. 又设 $\pmb{x}, \pmb{y} \in D$. 对 $\pmb{f}$ 的每一个分量 $f_i$, 应用微分中值定理可得 $\pmb{\xi}_i \in D$, 使得

$$
f _ {i} (\boldsymbol {x}) - f _ {i} (\boldsymbol {y}) = \nabla f _ {i} (\boldsymbol {\xi} _ {i}) \cdot (\boldsymbol {x} - \boldsymbol {y}).
$$

因此, 对于不同的 $i$, 这些 $\xi_{i}$ 有可能不同. 比如:

例 15.4.2 考虑映射  $f: R \rightarrow R^{2}, f(t) = (t^{2}, t^{3})$ . 取  $t_{1} = 1, t_{2} = 0$ , 则

$$
\boldsymbol {f} (1) = (1, 1), \quad \boldsymbol {f} (0) = (0, 0).
$$

这表明 $\xi_1 = 1 / 2, \xi_2 = \pm 1 / \sqrt{3}$, 因此 $\xi_1 \neq \xi_2$.

所以对于映射, 一般我们不能指望

$$
f (x) - f (y) = J f (\xi) (x - y).
$$

对某个  $\xi$  成立. 然而, 我们有下面的结论:

定理 15.4.4（拟微分中值定理） 设  $D \subseteq R^{n}$  为凸域,  $f : D \to R^{m}$  在 D 中处处可微. 则任给  $x, y \in D$ , 存在  $\xi \in D$ , 使得

$$
\| f (x) - f (y) \| \leqslant \| J f (\xi) \| \cdot \| x - y \|\cdot
$$

证明 基本的想法是对 f 的分量的线性组合应用微分中值定理. 为此, 不妨设  $f(x) \neq f(y)$ . 任意取定  $R^{m}$  中的单位向量  $\boldsymbol{u} = (u_{1}, \cdots, u_{m})$ , 记

$$
g = \boldsymbol {u} \cdot \boldsymbol {f} = \sum_ {i = 1} ^ {m} u _ {i} f _ {i},
$$

则 g 为 D 中可微函数. 根据微分中值定理, 存在  $\xi \in D$ , 使得

$$
g (\boldsymbol {x}) - g (\boldsymbol {y}) = \nabla g (\boldsymbol {\xi}) \cdot (\boldsymbol {x} - \boldsymbol {y}).
$$

注意到 $\nabla g(\pmb {\xi}) = \sum_{i = 1}^{m}u_{i}\nabla f_{i}(\pmb {\xi})$ .利用Cauchy-Schwarz不等式可得

$$
\begin{array}{l} \| \nabla g (\boldsymbol {\xi}) \| \leqslant \sum_ {i = 1} ^ {m} | u _ {i} | \cdot \| \nabla f _ {i} (\boldsymbol {\xi}) \| \\ \leqslant \| \boldsymbol {u} \| \cdot \left(\sum_ {i = 1} ^ {m} \| \nabla f _ {i} (\boldsymbol {\xi}) \| ^ {2}\right) ^ {1 / 2} = \| J \boldsymbol {f} (\boldsymbol {\xi}) \|\cdot \\ \end{array}
$$

由 $g(\pmb {x}) - g(\pmb {y}) = \pmb {u}\cdot (\pmb {f}(\pmb {x}) - \pmb {f}(\pmb {y}))$ 可得

---

272

第十五章 多元函数微分学及其应用

$$
\left| \boldsymbol {u} \cdot (\boldsymbol {f} (\boldsymbol {x}) - \boldsymbol {f} (\boldsymbol {y})) \right| \leqslant \| \nabla g (\boldsymbol {\xi}) \| \cdot \| \boldsymbol {x} - \boldsymbol {y} \| \leqslant \| J \boldsymbol {f} (\boldsymbol {\xi}) \| \cdot \| \boldsymbol {x} - \boldsymbol {y} \|\.
$$

在上式中取  $\boldsymbol{u}=(\boldsymbol{f}(\boldsymbol{x})-\boldsymbol{f}(\boldsymbol{y}))/\|\boldsymbol{f}(\boldsymbol{x})-\boldsymbol{f}(\boldsymbol{y})\|$  即可.

利用拟微分中值定理, 不难证明下面的结论:

推论15.4.5 设 $D \subseteq \mathbb{R}^n$ 为凸域, $f: D \to \mathbb{R}^m$ 在 $D$ 中可微, 且其Jacobi矩阵处处为零矩阵, 则 $f$ 是常向量值映射.

例 15.4.3 设二元函数  $f(x,y)$  在圆盘  $\overline{B_{10}(0)}$  上连续, 在其内可微,  $f(0,0)=0$ ,  $\|\operatorname{grad} f\| \leqslant 2$ , 证明:  $|f(2,2)| \leqslant 4\sqrt{2}$ .

证明 多元函数作为映射的特殊情况, 也有拟微分中值定理成立. 因此存在 $\theta \in (0,1)$ 使得

$$
\begin{array}{l} | f (2, 2) - f (0, 0) | = | f _ {x} (2 \theta , 2 \theta) \cdot 2 + f _ {y} (2 \theta , 2 \theta) \cdot 2 | = | \langle \mathrm{grad} f, (2, 2) \rangle | \\ \leqslant \| \mathrm{grad} f \| \cdot \| (2, 2) \| \leqslant 2 \cdot \sqrt {8} = 4 \sqrt {2}. \\ \end{array}
$$

## 习题 15.4

1. 考虑向量值函数 $f: \mathbb{R} \to \mathbb{R}^2$, $f(x) = (\sin x, \cos x)$. 证明: 不存在 $\xi \in (0,1)$ 使得

$$
\boldsymbol {f} (\pi) - \boldsymbol {f} (0) = \pi \boldsymbol {f} ^ {\prime} (\xi).
$$

2. 试讨论映射 $f: \mathbb{R}^n \to \mathbb{R}^n$,

$$
f (\boldsymbol {x}) = \| \boldsymbol {x} \| \boldsymbol {x}
$$

在原点的可微性. 如果可微, 求其导数.

3. 设 $f: D \subseteq \mathbb{R}^n \to \mathbb{R}^m, x_0 \in D$, 存在矩阵 $A$, 使得在 $x_0$ 的邻域内有

$$
\boldsymbol {f} (\boldsymbol {x}) = \boldsymbol {f} (\boldsymbol {x} _ {0}) + \boldsymbol {A} (\boldsymbol {x} - \boldsymbol {x} _ {0}) + o (\boldsymbol {x} - \boldsymbol {x} _ {0}),
$$

其中 $o(\pmb{x} - \pmb{x}_0)$ 表示当 $\| \pmb{x} - \pmb{x}_0\| \to 0$ 时，模为高阶无穷小量的向量.证明: $\pmb{f}$ 在 $\pmb{x}_0$ 处可微，且 $Jf(x_0) = A$

4. 设 $f: \mathbb{R} \to \mathbb{R}^3$ 是可微映射, 满足 $\| f(t) \| = 1 (\forall t \in \mathbb{R})$. 证明:

$$
\boldsymbol {f} ^ {\prime} (t) \cdot \boldsymbol {f} (t) = 0.
$$

试给出这一关系式的几何解释.

5. 设 $u(x, y)$, $v(x, y)$ 是 $\mathbb{R}^2$ 上的 $C^1$ 函数, 且存在 $M > 0$, 使得对任意的 $(x_i, y_i) \in \mathbb{R}^2 (i = 1, 2)$ 均成立

$$
(u _ {1} - u _ {2}) ^ {2} + (v _ {1} - v _ {2}) ^ {2} \geqslant M \big ((x _ {1} - x _ {2}) ^ {2} + (y _ {1} - y _ {2}) ^ {2} \big),
$$

---

15.5 Taylor 公式

273

其中 $u_{i} = u(x_{i},y_{i}),v_{i} = v(x_{i},y_{i})$ $(i = 1,2)$ .证明: $\forall (x,y)\in \mathbb{R}^2$ 有

$$
\frac {\partial (u , v)}{\partial (x , y)} \neq 0.
$$

6. 设 $f(x, y)$ 在点 $(x_0, y_0)$ 的邻域 $U$ 上有定义. 如果 $f(x, y_0)$ 在点 $x = x_0$ 处连续，且存在 $M > 0, |f_y(x, y)| \leqslant M ((x, y) \in U)$，证明:$f(x, y)$ 在点 $(x_0, y_0)$ 处连续.

7. 设 $D = \{(x, y, z) | x^2 + y^2 + z^2 < 1\}$, $f(x, y, z)$ 在 $D$ 上的偏导数存在, 且有

$$
| f _ {x} (x, y, z) | \leqslant 1, \quad | f _ {y} (x, y, z) | \leqslant 1, \quad (x, y, z) \in D.
$$

若对取定的点 $(x,y):x^{2} + y^{2}\leqslant 1$ ，有 $f(x,y,z)$ 是 $z$ 的连续函数，证明: $f\in C(D)$

8. 设映射 $\pmb{f}: [a, b] \to \mathbb{R}^n$ 和函数 $g: [a, b] \to \mathbb{R}$ 在 $[a, b]$ 上连续，在 $(a, b)$ 内可微. 如果 $\| \pmb{f}'(t) \| \leqslant g'(t) (t \in (a, b))$, 证明: $\| \pmb{f}(b) - \pmb{f}(a) \| \leqslant g(b) - g(a)$.

9. 设 $f(x, y)$, $g(x, y)$ 在区域 $D$ 上偏导数存在, 满足

$$
f _ {x} = g _ {y}, \quad f _ {y} = - g _ {x}, \quad f ^ {2} (x, y) + g ^ {2} (x, y) \equiv 1, \quad (x, y) \in D.
$$

证明: $f(x,y)$ 和 $g(x,y)$ 在 $D$ 上均为常值函数.

10. 设 $f(\pmb{y}) \in C^2(\mathbb{R}^n)$, 矩阵 $\pmb{A} = (a_{ij})_{n \times n}$ 是正交矩阵, $F(\pmb{x}) = f(\pmb{A}\pmb{x})$. 证明: 当 $\pmb{y} = \pmb{A}\pmb{x}$ 时, 有

$$
\begin{array}{l} \sum_ {i = 1} ^ {n} \left(\frac {\partial f}{\partial y _ {i}}\right) ^ {2} = \sum_ {i = 1} ^ {n} \left(\frac {\partial F}{\partial x _ {i}}\right) ^ {2}, \\ \sum_ {i = 1} ^ {n} \frac {\partial^ {2} f}{\partial y _ {i} ^ {2}} = \sum_ {i = 1} ^ {n} \frac {\partial^ {2} F}{\partial x _ {i} ^ {2}}. \\ \end{array}
$$

11. 设 $f$ 是 $\mathbb{R}^n \to \mathbb{R}^n$ 的可微映射, 如果存在 $k \in (0,1)$ 使得 $\| f'(x) - id \| \leqslant k (\forall x \in \mathbb{R}^n)$, 其中 $id$ 是恒同映射. 证明: $f$ 是单射, 并且有界集的逆像是有界的.

12. (映射的导数极限定理) 设 $E \subseteq \mathbb{R}^n$ 是一开集, $\pmb{a} \in E$. $\pmb{f}$ 是 $E \to \mathbb{R}^n$ 的连续映射, 且在 $\pmb{x} \neq \pmb{a}$ 点可微. 设 $\pmb{L}$ 是 $E \to \mathbb{R}^n$ 的线性映射, 满足

$$
\lim _ {\boldsymbol {x} \to \boldsymbol {a}} \| \boldsymbol {f} ^ {\prime} (\boldsymbol {x}) - \boldsymbol {L} \| = 0.
$$

证明: $f$ 在 $\pmb{a}$ 处可微, 且 $f'(a) = L$.

## 15.5 Taylor 公式

## Taylor 多项式

我们回忆一下一元函数时的场景. 设一元实函数 $f$ 在 ${x}_{0}$ 点有 $m$ 阶导数,则称

$$
T _ {m} (x) := \sum_ {k = 0} ^ {m} \frac {f ^ {(k)} (x _ {0})}{k !} (x - x _ {0}) ^ {k}
$$

---

274

第十五章 多元函数微分学及其应用

为 $f$ 在 $x_0$ 点的 $m$ 阶Taylor多项式, $f - T_{m}$ 称为Taylor展式的余项. 显然, 函数 $f$ 在 $x_0$ 点的 $m$ 阶Taylor多项式 $T_{m}$ 是一个阶数不高于 $m$ 的多项式, 它与 $f$ 在 $x_0$ 处的所有不高于 $m$ 阶的导数都相等. 因此, 如果把这一定义推广到多元函数, 我们不仅需要函数在给定点的直到 $m$ 阶的偏导数都存在, 而且需要相应的混合偏导数不依赖于求导次序. 而能保证后者成立的使用起来比较方便的充分条件就是假设 $f$ 是 $C^{m}$ 函数.

我们先引入一些记号. 设 $\alpha_{i}$ 均为非负整数, $1 \leqslant i \leqslant n$. 引入如下多重指标和记号:

$$
\boldsymbol {\alpha} = (\alpha_ {1}, \dots , \alpha_ {n}), \quad | \boldsymbol {\alpha} | = \sum_ {i = 1} ^ {n} \alpha_ {i}, \quad \boldsymbol {\alpha}! = \alpha_ {1}! \cdot \alpha_ {2}! \dots \alpha_ {n}!.
$$

如果  $\boldsymbol{x}=(x_{1},\cdots,x_{n})\in\mathbb{R}^{n}$ ，则记  $x^{\alpha}=x_{1}^{\alpha_{1}}\cdot x_{2}^{\alpha_{2}}\cdots x_{n}^{\alpha_{n}}$ 。对于多元函数 f，我们也用下面的记号表示  $|\alpha|$  阶偏导数:

$$
D ^ {\alpha} f (\boldsymbol {x} _ {0}) = \frac {\partial^ {| \alpha |} f (\boldsymbol {x} _ {0})}{\partial x _ {1} ^ {\alpha_ {1}} \cdots \partial x _ {n} ^ {\alpha_ {n}}} = \frac {\partial^ {| \alpha |} f (\boldsymbol {x} _ {0})}{\partial \boldsymbol {x} ^ {\alpha}}.
$$

定义 15.5.1 设 n 元实函数 f 在  $x_{0}$  点有直到 m 阶的各阶连续的偏导数, 则称

$$
T _ {m} (\boldsymbol {x}) \equiv T _ {m} (\boldsymbol {x}; f) := \sum_ {k = 0} ^ {m} \sum_ {| \boldsymbol {\alpha} | = k} \frac {1}{\boldsymbol {\alpha} !} \frac {\partial^ {k} f (\boldsymbol {x} _ {0})}{\partial \boldsymbol {x} ^ {\boldsymbol {\alpha}}} (\boldsymbol {x} - \boldsymbol {x} _ {0}) ^ {\boldsymbol {\alpha}} \tag {15.5.1}
$$

为 f 在  $x_{0}$  点的 m 阶 Taylor 多项式.

定理 15.5.1 (Taylor 公式) 设  $D \subseteq R^{n}$  为凸域,  $f \in C^{m+1}(D)$ ,  $a \in D$ . 则任给  $x \in D$ , 存在  $\theta \in (0,1)$ , 使得

$$
f (\boldsymbol {x}) = \sum_ {k = 0} ^ {m} \sum_ {| \alpha | = k} \frac {D ^ {\alpha} f (\boldsymbol {a})}{\alpha !} (\boldsymbol {x} - \boldsymbol {a}) ^ {\alpha} + \sum_ {| \alpha | = m + 1} \frac {D ^ {\alpha} f (\boldsymbol {a} + \theta (\boldsymbol {x} - \boldsymbol {a}))}{\alpha !} (\boldsymbol {x} - \boldsymbol {a}) ^ {\alpha}.
$$

证明 考虑一元函数 $\varphi(t) = f(\boldsymbol{a} + t(\boldsymbol{x} - \boldsymbol{a}))$, $t \in [0,1]$. $\varphi$ 具有 $m + 1$ 阶连续导数，故由一元函数的 Taylor 公式, 存在 $\theta \in (0,1)$, 使得

$$
\varphi (1) = \varphi (0) + \varphi^ {\prime} (0) + \frac {1}{2 !} \varphi^ {\prime \prime} (0) + \dots + \frac {1}{m !} \varphi^ {(m)} (0) + \frac {1}{(m + 1) !} \varphi^ {(m + 1)} (\theta). \tag {15.5.2}
$$

利用数学归纳法不难证明

$$
\varphi^ {(k)} (t) = \sum_ {| \alpha | = k} \frac {k !}{\alpha !} D ^ {\alpha} f (\boldsymbol {a} + t (\boldsymbol {x} - \boldsymbol {a})) (\boldsymbol {x} - \boldsymbol {a}) ^ {\alpha}.
$$

特别地, t = 0 时, 有

$$
\varphi^ {(k)} (0) = \sum_ {| \alpha | = k} \frac {k !}{\alpha !} D ^ {\alpha} f (\boldsymbol {a}) (\boldsymbol {x} - \boldsymbol {a}) ^ {\alpha},
$$

将上式代入 (15.5.2) 式即得欲证公式.

□

---

15.5 Taylor 公式

275

记

$$
R _ {m} (\boldsymbol {x}) = f (\boldsymbol {x}) - \sum_ {k = 0} ^ {m} \sum_ {| \boldsymbol {\alpha} | = k} \frac {D ^ {\boldsymbol {\alpha}} f (\boldsymbol {a})}{\boldsymbol {\alpha} !} (\boldsymbol {x} - \boldsymbol {a}) ^ {\boldsymbol {\alpha}}.
$$

由 Taylor 公式, 当  $f \in C^{m+1}(D)$  时,

$$
R _ {m} (\pmb {x}) = \sum_ {| \pmb {\alpha} | = m + 1} \frac {D ^ {\pmb {\alpha}} f (\pmb {a} + \theta (\pmb {x} - \pmb {a}))}{\pmb {\alpha} !} (\pmb {x} - \pmb {a}) ^ {\pmb {\alpha}}. \qquad (\mathrm{Lagrange} \text {余项})
$$

推论 15.5.2 在上述定理的条件下，当  $\|x - a\|$  充分小时， $R_{m}(x) = O(\|\boldsymbol{x} - \boldsymbol{a}\|^{m+1})$ .

证明 取 $\delta > 0$, 使得 $\overline{B_{\delta}(\boldsymbol{a})} \subset D$. 由于 $f \in C^{m+1}(D)$, $\overline{B_{\delta}(\boldsymbol{a})}$ 紧致, 故存在 $M > 0$ 使得

$$
| D ^ {\alpha} f (\boldsymbol {x}) | \leqslant M, \quad \forall \boldsymbol {x} \in \overline {{B _ {\delta} (\boldsymbol {a})}}, | \boldsymbol {\alpha} | \leqslant m + 1.
$$

因此

$$
\begin{array}{l} | R _ {m} (\boldsymbol {x}) | \leqslant M \sum_ {| \boldsymbol {\alpha} | = m + 1} \frac {1}{\boldsymbol {\alpha} !} | (\boldsymbol {x} - \boldsymbol {a}) ^ {\boldsymbol {\alpha}} | \\ \leqslant M \sum_ {| \alpha | = m + 1} \frac {1}{\alpha !} \| \boldsymbol {x} - \boldsymbol {a} \| ^ {| \alpha |} = C \| \boldsymbol {x} - \boldsymbol {a} \| ^ {m + 1}. \\ \end{array}
$$

推论得证.

![](../../raw/pages_0577-0592/images/page_579_image_12.jpg)

注 15.5.1 如果 $f \in  {C}^{m}\left( D\right)$ ,则 Taylor 公式可写为

$$
\begin{array}{l} f (x) = \sum_ {k = 0} ^ {m - 1} \sum_ {| \alpha | = k} \frac {D ^ {\alpha} f (\boldsymbol {a})}{\alpha !} (\boldsymbol {x} - \boldsymbol {a}) ^ {\alpha} + \sum_ {| \alpha | = m} \frac {D ^ {\alpha} f (\boldsymbol {a} + \theta (\boldsymbol {x} - \boldsymbol {a}))}{\alpha !} (\boldsymbol {x} - \boldsymbol {a}) ^ {\alpha} \\ = \sum_ {k = 0} ^ {m} \sum_ {| \boldsymbol {\alpha} | = k} \frac {D ^ {\boldsymbol {\alpha}} f (\boldsymbol {a})}{\boldsymbol {\alpha} !} (\boldsymbol {x} - \boldsymbol {a}) ^ {\boldsymbol {\alpha}} + R _ {m} (\boldsymbol {x}), \\ \end{array}
$$

其中

$$
R _ {m} (\boldsymbol {x}) = \sum_ {| \alpha | = m} \frac {1}{\alpha !} \big (D ^ {\alpha} f (\boldsymbol {a} + \theta (\boldsymbol {x} - \boldsymbol {a})) - D ^ {\alpha} f (\boldsymbol {a}) \big) (\boldsymbol {x} - \boldsymbol {a}) ^ {\alpha}.
$$

用推论的证明方法可得如下估计:

$$
R _ {m} (\boldsymbol {x}) = o \big (\| \boldsymbol {x} - \boldsymbol {a} \| ^ {m} \big) (\boldsymbol {x} \rightarrow \boldsymbol {a}). \quad (\text {Peano 余项})
$$

Taylor 公式的常数项  $f(\boldsymbol{a})$  自然是  $f(\boldsymbol{x})$  的最粗逼近, 属于常数函数类中的零次逼近, 更精确的逼近则要考虑其一次逼近、二次逼近等. 它们是极其重要的逼近, 并且分别具有明确的几何意义: 高维空间的平面和二次曲面.

---

276

第十五章 多元函数微分学及其应用

Taylor 公式中的线性项和二次项分别具有形式

$$
\nabla f (\pmb {a}) \cdot (\pmb {x} - \pmb {a}) \quad \text {和} \quad \frac {1}{2} (\pmb {x} - \pmb {a}) \nabla^ {2} f (\pmb {a}) (\pmb {x} - \pmb {a}) ^ {\mathrm{T}},
$$

其中  $\nabla f(a)$  是前面曾经引入过的函数在点 a 处的梯度, 而

$$
\nabla^ {2} f := \left(\frac {\partial^ {2} f}{\partial x _ {j} \partial x _ {i}}\right) _ {n \times n}
$$

称为 $f$ 的Hesse矩阵，记为 $\operatorname{Hess}(f)$ 或 $\pmb{H}_f$ ，该矩阵的迹 $\mathrm{tr}\nabla^2 f$ 常被记为 $\Delta f$ ，即

$$
\Delta = \mathrm{tr} \nabla^ {2} = \sum_ {i = 1} ^ {n} \frac {\partial^ {2}}{\partial x _ {i} ^ {2}}
$$

称为 Laplace 算子.

## 多元凸函数

作为 Taylor 公式的应用, 我们来讨论多元函数凸性的一些结果. 由于研究凸性需要考虑任意两点之间线段上的函数值与端点函数值之间的关系, 因此我们总是假定 $D \subseteq \mathbb{R}^n$ 是一个凸域. 在凸域 $D$ 内, 若 $f(\pmb{x})$ 有直到 $k$ 阶的连续偏导数, 则 $\forall \pmb{x}_0 \in D, f(\pmb{x})$ 总可以在 $\pmb{x}_0$ 处展成 $k$ 阶 Taylor 公式.

定义 15.5.2 (凸函数) 设  $D \subseteq R^{n}$  为凸域,  $f : D \to R$  为多元函数. 如果任给  $x, y \in D, x \neq y$ , 均有

$$
f (t \boldsymbol {x} + (1 - t) \boldsymbol {y}) \leqslant t f (\boldsymbol {x}) + (1 - t) f (\boldsymbol {y}), \forall t \in (0, 1),
$$

则称 $f$ 为 $D$ 中的凸函数. 上式中“$\leqslant$”换成“<”时, 称为严格凸函数.

从凸函数的定义出发研究其性质是最自然和最基本的出发点, 没有额外的假设. 但是当我们试图应用 Taylor 公式来研究多元凸函数的时候, 自然要求函数满足 Taylor 公式的条件. 通常, 随着函数条件的加强, 研究的工具和手法也会多一些. 比如, 对于一元函数 $f(x)$, 如果 $f'(x)$ 存在, 那么我们可以通过讨论导函数的单调性来确定 $f(x)$ 的凹凸性. 如果再加上 $f$ 二阶可导, 那么可以通过讨论二阶导数的定号性来判别 $f(x)$ 的凹凸性. 对于多元函数 $f(x)$, 其导数 $f'(x)$ 在很多情形下也可以类比为一元函数 $f'(x)$ 的作用. 而如果它二阶可微的话, 那么它的 Hesse 矩阵 $H_f$ 将扮演着一元函数 $f''(x)$ 类似的角色. 另外, 我们知道, 几何上, 凸函数具有非常明确的几何特点: $f(x)$ 是凸的充要条件是曲线 $y = f(x)$ 上任一点都在曲线该点切线的上方. 对应于多元函数, 几何上则表现为曲面上的点与切平面之间的位置关系. 具体来说, 对于多元函数, 我们有下面的结论:

命题 15.5.3 设函数 f 在凸域 D 上有定义.

(1) 如果 $f$ 在 $D$ 内处处可微, 则

$$
f \text {为凸函数} \iff f (\pmb {y}) \geqslant f (\pmb {x}) + \nabla f (\pmb {x}) \cdot (\pmb {y} - \pmb {x}), \forall \pmb {x}, \pmb {y} \in D. \tag {15.5.3}
$$

---

15.5 Taylor 公式

277

(2) 如果 $f \in C^2(D)$, 则

$$
f \text {为凸函数} \iff \nabla^ {2} f \geqslant 0 (\text {半正定}).
$$

证明 (1) “$\Longrightarrow$” 任给 $\pmb{x}, \pmb{y} \in D, t \in (0,1)$, 有

$$
\begin{array}{l} t \big (f (\boldsymbol {y}) - f (\boldsymbol {x}) \big) \geqslant f (\boldsymbol {x} + t (\boldsymbol {y} - \boldsymbol {x})) - f (\boldsymbol {x}) \\ = \nabla f (\boldsymbol {x}) \cdot t (\boldsymbol {y} - \boldsymbol {x}) + o (t \| \boldsymbol {y} - \boldsymbol {x} \|), \\ \end{array}
$$

上式两边除以 t, 然后令  $t \rightarrow 0^{+}$  即得 (15.5.3) 式.

“$\Longleftarrow$”任给 $\pmb{x}, \pmb{y} \in D, t \in (0,1)$, 记 $z = t\pmb{x} + (1 - t)\pmb{y}$, 则

$$
f (\boldsymbol {x}) \geqslant f (\boldsymbol {z}) + \nabla f (\boldsymbol {z}) \cdot (\boldsymbol {x} - \boldsymbol {z}), \quad f (\boldsymbol {y}) \geqslant f (\boldsymbol {z}) + \nabla f (\boldsymbol {z}) \cdot (\boldsymbol {y} - \boldsymbol {z}).
$$

这说明

$$
t f (\boldsymbol {x}) + (1 - t) f (\boldsymbol {y}) \geqslant f (\boldsymbol {z}) + \nabla f (\boldsymbol {z}) \cdot \left(t (\boldsymbol {x} - \boldsymbol {z}) + (1 - t) (\boldsymbol {y} - \boldsymbol {z})\right) = f (\boldsymbol {z}).
$$

(2) “$\Longleftarrow$” 设 $f \in C^{2}(D)$, 由 Taylor 公式, 任给 $\boldsymbol{x}, \boldsymbol{y} \in D$, 存在 $\boldsymbol{\xi} \in D$ 使得

$$
f (\boldsymbol {y}) = f (\boldsymbol {x}) + \nabla f (\boldsymbol {x}) \cdot (\boldsymbol {y} - \boldsymbol {x}) + \frac {1}{2} (\boldsymbol {y} - \boldsymbol {x}) \nabla^ {2} f (\boldsymbol {\xi}) (\boldsymbol {y} - \boldsymbol {x}) ^ {\mathrm{T}}.
$$

由  $\nabla^{2}f\geqslant0$  知 (15.5.3) 式成立, 再由 (1) 知 f 为凸函数.

“$\Longrightarrow$”(反证法). 如果 $\nabla^2 f(\boldsymbol{x})$ 不是半正定的, 则存在 $\mathbb{R}^n$ 中的单位向量 $\boldsymbol{h}$, 使得 $\boldsymbol{h}\nabla^2 f(\boldsymbol{x})\boldsymbol{h}^\mathrm{T} < 0$. 对一元函数 $\varphi(t) = f(\boldsymbol{x} + t\boldsymbol{h})$ 应用 Taylor 公式可得

$$
f (\boldsymbol {x} + t \boldsymbol {h}) = f (\boldsymbol {x}) + t \nabla f (\boldsymbol {x}) \cdot \boldsymbol {h} + \frac {1}{2} t ^ {2} \boldsymbol {h} \nabla^ {2} f (\boldsymbol {x}) \boldsymbol {h} ^ {\mathrm{T}} + o (t ^ {2}) (t \rightarrow 0).
$$

当 $t \neq 0$ 充分小时, 上式右端第三项小于零, 这与 (15.5.3) 式相矛盾.

例 15.5.1 设  $y = g(x)$  是  $(a, b)$  上的一元凸函数，二阶可导.证明: $f(\boldsymbol{x}) = g(x_{1}) + \cdots + g(x_{n})$  是  $D = (a, b)^{n} \subseteq R^{n}$  内的 n 元凸函数.

证明 因为  $f'(x) = (g'(x_1), \cdots, g'(x_n))$ ，所以

$$
\boldsymbol {H} _ {f} (\boldsymbol {x}) = \mathrm{diag} \big (g ^ {\prime \prime} (x _ {1}), \dots , g ^ {\prime \prime} (x _ {n}) \big).
$$

由于  $g''(x_{i}) \geqslant 0 (i = 1, 2, \cdots, n)$ ，故  $H_{f}(\boldsymbol{x})$  是半正定矩阵。根据上述命题知  $f(\boldsymbol{x})$  是 D 内的凸函数。

## 最值与极值

函数的最值和极值通常放在一起讨论. 我们知道, 极值是一个局部概念, 关注的是函数在某点邻域内取值的大小比较, 所以一个函数在一点处的极大值很有可能不如该函数在另一点处的极小值来得大. 最值是一个全局概念, 研究的是函数在整个定义域或在

---

278

第十五章 多元函数微分学及其应用

指定点集上的最大 (小) 值. 然而两者又有密切的联系. 最值的讨论一般是在考虑了所有的极值点、边界点和一些特殊点处的函数值后, 加以比较, 再从中考虑其最大或最小值.

本小节我们也是采用这个基本思路来讨论多元函数的最值和极值问题, 即: 我们以多元微分为工具, 重点讨论函数极值的性质和特点, 然后再通过比较函数在给定集合边界点处的取值来讨论最值.

类似于一元函数的 Taylor 公式可以用来研究一元函数的最值和极值, 我们也将应用多元函数的 Taylor 公式来研究多元函数的极值. 只不过相比一元函数, 多元函数的极值大致有如下两类: 无条件极值和有条件极值, 前者就是我们所说的普通极值; 而后者则是指在额外限制条件下的极值问题. 我们先讨论无条件极值. 在和一元函数相似之处, 我们将视情况省去某些重复度较高的技术细节.

定义 15.5.3 (极值) 设  $D \subseteq R^{n}$ ,  $f : D \to R$  为多元函数,  $x_{0} \in D$ . 如果存在  $\delta > 0$ , 使得

$$
f (\pmb {x} _ {0}) \geqslant f (\pmb {x}) \quad (\text {或} f (\pmb {x} _ {0}) \leqslant f (\pmb {x})), \forall \pmb {x} \in D \cap \stackrel {\circ} {B} _ {\delta} (\pmb {x} _ {0}),
$$

则称 $x_0$ 为 $f$ 的极大（小）值点，$f(x_0)$ 为 $f$ 的极大（小）值。如果上式中严格的不等号“>”（“<”）成立，则相应地称 $x_0$ 为严格极值点，而 $f(x_0)$ 为严格极值。

如果 $\forall \delta > 0$, 都存在 $x_{1}, x_{2} \in \overset{\circ}{B}_{\delta}(x_{0})$, 使得

$$
f (\boldsymbol {x} _ {1}) > f (\boldsymbol {x} _ {0}), \quad f (\boldsymbol {x} _ {2}) <   f (\boldsymbol {x} _ {0}),
$$

则称  $x_{0}$  为 f 的鞍点.

例15.5.2 点 $(0,0)$ 分别是函数

$$
f _ {1} (x, y) = x ^ {4} + y ^ {4}, \quad f _ {2} (x, y) = - x ^ {2} - y ^ {4}, \quad f _ {3} (x, y) = x ^ {4} - y ^ {4}
$$

的极小值点、极大值点和鞍点.

同 Fermat 引理一样, 我们有如下关于极值的一阶必要条件.

定理 15.5.4（极值的必要条件） 设  $x_{0}$  为 f 的极值点, 如果  $x_{0}$  为 D 的内点, 且 f 在  $x_{0}$  处可微, 则  $\nabla f(x_{0}) = 0$ .

证明 任取单位向量 $e \in S^{n-1}$，考虑一元函数 $\varphi(t) = f(x_0 + te)$。因为 $x_0$ 为内点，当 $|t|$ 充分小时 $x_0 + te \in D$。于是 $t = 0$ 为 $\varphi$ 的极值点。根据一元函数的 Fermat 引理和 (15.3.6) 式可得

$$
0 = \varphi^ {\prime} (0) = \nabla f (\boldsymbol {x} _ {0}) \cdot \boldsymbol {e},
$$

由 e 的任意性可知  $\nabla f(\boldsymbol{x}_{0}) = \boldsymbol{0}$ .

梯度为零的点称为函数的驻点或临界点, 也称可疑点. 求函数极值时, 也可以比较形象地说成: 一般先找出函数的可疑点, 然后再做进一步的判定. 如果一个点连可疑点都不是, 自然不用去理会它的极值性. 但如果它是可疑点, 至于它是不是真正的极值点, 则需要进一步讨论, 下面的定理就是做进一步研判的模式之一: 极值的二阶必要条件.

---

15.5 Taylor 公式

279

定理 15.5.5 设 n 元实函数 f 在  $x_{0}$  取到极小（大）值，且 f 在  $x_{0}$  的一个邻域内可微，其一阶偏导均在  $x_{0}$  点可微。则其 Hesse 矩阵  $H_{f}(x_{0})$  半正（负）定。

证明 我们只考虑极小值的情况, 极大值的情况完全类似讨论. 由定理 15.5.4 知, $f_{\pmb{x}}(\pmb{x}_{0}) = \mathbf{0}$. 由带 Peano 余项的 Taylor 公式, 可得

$$
f (\boldsymbol {x} + \boldsymbol {x} _ {0}) = f (\boldsymbol {x} _ {0}) + \frac {1}{2} \boldsymbol {x} \boldsymbol {H} _ {f} (\boldsymbol {x} _ {0}) \boldsymbol {x} ^ {\mathrm{T}} + o \big (\| \boldsymbol {x} \| ^ {2} \big) \quad (\boldsymbol {x} \rightarrow \boldsymbol {0}). \tag {15.5.4}
$$

由此立即得到对任何单位向量  $e \in S^{n-1}$ ,

$$
\frac {1}{2} \boldsymbol {e} \boldsymbol {H} _ {f} (\boldsymbol {x} _ {0}) \boldsymbol {e} ^ {\mathrm{T}} = \lim _ {t \to 0} \frac {f (t \boldsymbol {e} + \boldsymbol {x} _ {0}) - f (\boldsymbol {x} _ {0})}{t ^ {2}} \geqslant 0.
$$

因此  $H_{f}(x_{0})$  半正定.

需要强调指出的是: 上面两个定理对极值点的判定都有预设门槛, 那就是假设了函数可微. 换句话说, 在寻求一个函数的极值点时, 如果只关注梯度为零试图找到所有的可疑点, 那么仍有可能有漏网之鱼: 那些不可微的点! 这一点从一元函数 $y = |x|$ 便可一目了然: 该函数通过寻求导数为零的点, 并没有发现“可疑点”, 但恰恰在不可导的点 $x_0 = 0$ 处, 函数取到极值.

定理 15.5.5 的必要性而非充分性是显然的, 比如  $(0,0)$  是函数  $f(x,y)=x^{2}-y^{4}$  的鞍点, 但 f 的 Hesse 矩阵  $H_{f}(0,0)$  是半正定的.

利用 Taylor 展式, 我们还可以得到多元函数取得极值的充分条件. 为此, 先给出如下定义和引理:

定义 15.5.4 设多元函数 $f\left( x\right)$ 在点 ${x}_{0}$ 的某邻域内有二阶连续偏导数, ${x}_{0}$ 是 $f\left( x\right)$ 的驻点. 记 $f\left( x\right)$ 在 ${x}_{0}$ 处的 Hesse 矩阵为 ${H}_{f}\left( {x}_{0}\right)$ . 如果

$$
\det \boldsymbol {H} _ {f} (\boldsymbol {x} _ {0}) \neq 0,
$$

则称  $x_{0}$  为 f 的非退化驻点. 否则, 称  $x_{0}$  为 f 的退化驻点.

引理 15.5.6 设  $f(\boldsymbol{x}) = f(x_{1}, \cdots, x_{n})$  在区域  $D \subseteq R^{n}$  内有二阶连续偏导数，设  $f(\boldsymbol{x})$  在  $x_{0}$  处的 Hesse 矩阵为  $\boldsymbol{H}_{f}(\boldsymbol{x}_{0}) = (f_{x_{i}x_{j}})_{\boldsymbol{x}_{0}}$ . 则存在实数 m, M 使得对任意的单位向量  $u \in S^{n-1}$ ，成立

$$
m \leqslant \boldsymbol {u} \boldsymbol {H} _ {f} (\boldsymbol {x} _ {0}) \boldsymbol {u} ^ {\mathrm{T}} \leqslant M.
$$

证明 注意到  $\boldsymbol{u}\boldsymbol{H}_{f}(\boldsymbol{x}_{0})\boldsymbol{u}^{\mathrm{T}}$  是紧致集  $S^{n-1}$  上的连续函数, 从而可以取到最大值 M 和最小值 m. □

定理 15.5.7 设 n 元函数 f 在  $x_{0}$  的一个邻域内有二阶连续偏导数,  $x_{0}$  为 f 的非退化驻点, 即  $f_{x}(\boldsymbol{x}_{0}) = \boldsymbol{0}$ , 且  $\det H_{f}(\boldsymbol{x}_{0}) \neq 0$ . 此时矩阵  $H_{f}(\boldsymbol{x}_{0})$  必为且仅为正定、负定或不定三者之一. 进一步, 有

(1) 若  $H_{f}(x_{0})$  正定, 则 f 在  $x_{0}$  取得严格极小值.

---

280

第十五章 多元函数微分学及其应用

(2) 若  $H_{f}(x_{0})$  负定, 则 f 在  $x_{0}$  取得严格极大值.
(3) 若  $H_{f}(x_{0})$  不定, 则 f 在  $x_{0}$  点一定取不到极值.

证明 我们只证 (1) 和 (3), 因为 (2) 的证明与 (1) 完全类同.

在  $x_{0}$  的充分小邻域内, 考虑  $f(x)$  在  $x_{0}$  处的 Taylor 公式, 记  $\Delta x = x - x_{0}$ ,

$$
\begin{array}{l} f (\boldsymbol {x}) = f (\boldsymbol {x} _ {0}) + f ^ {\prime} (\boldsymbol {x} _ {0}) (\Delta \boldsymbol {x}) ^ {\mathrm{T}} + \frac {1}{2} \Delta \boldsymbol {x} \boldsymbol {H} _ {f} (\boldsymbol {x} _ {0}) (\Delta \boldsymbol {x}) ^ {\mathrm{T}} + o (\| \Delta \boldsymbol {x} \| ^ {2}) \\ = f (\boldsymbol {x} _ {0}) + \frac {1}{2} \frac {\Delta \boldsymbol {x}}{\| \Delta \boldsymbol {x} \|} \boldsymbol {H} _ {f} (\boldsymbol {x} _ {0}) \frac {(\Delta \boldsymbol {x}) ^ {\mathrm{T}}}{\| \Delta \boldsymbol {x} \|} (\| \Delta \boldsymbol {x} \| ^ {2}) + o (\| \Delta \boldsymbol {x} \| ^ {2}) (\boldsymbol {x} - \boldsymbol {x} _ {0} \rightarrow \boldsymbol {0}). \\ \end{array}
$$

注意到  $u := \frac{\Delta x}{\|\Delta x\|} \in S^{n-1}$ ，故上式第二项  $\boldsymbol{u}\boldsymbol{H}_{f}(\boldsymbol{x}_{0})\boldsymbol{u}^{\mathrm{T}}$  是  $S^{n-1}$  上的连续函数。由  $S^{n-1}$  的紧致性，知  $\boldsymbol{u}\boldsymbol{H}_{f}(\boldsymbol{x}_{0})\boldsymbol{u}^{\mathrm{T}}$  在  $S^{n-1}$  上有最大值 M 和最小值 m。

(1) 当  $H_{f}(x_{0})$  正定时, 这意味着上述最小值 m > 0. 所以

$$
\begin{array}{l} f (\boldsymbol {x}) = f (\boldsymbol {x} _ {0}) + \frac {1}{2} \boldsymbol {u} \boldsymbol {H} _ {f} (\boldsymbol {x} _ {0}) \boldsymbol {u} ^ {\mathrm{T}} (\| \boldsymbol {x} - \boldsymbol {x} _ {0} \| ^ {2}) + o (\| \boldsymbol {x} - \boldsymbol {x} _ {0} \| ^ {2}) \\ > f (\boldsymbol {x} _ {0}) + \frac {m}{4} \| \boldsymbol {x} - \boldsymbol {x} _ {0} \| ^ {2} > f (\boldsymbol {x} _ {0}). \\ \end{array}
$$

故  $f(x)$  在  $x_{0}$  取极小值.

(3) 当  $H_{f}(x_{0})$  不定时, 这意味着存在  $u_{1}, u_{2} \in S^{n-1}$ , 使得

$$
\boldsymbol {u} _ {1} \boldsymbol {H} _ {f} (\boldsymbol {x} _ {0}) \boldsymbol {u} _ {1} ^ {\mathrm{T}} = m <   0, \quad \boldsymbol {u} _ {2} \boldsymbol {H} _ {f} (\boldsymbol {x} _ {0}) \boldsymbol {u} _ {2} ^ {\mathrm{T}} = M > 0.
$$

易知对充分小的 t > 0, 有

$$
f (\boldsymbol {x} _ {0} + t \boldsymbol {u} _ {1}) = f (\boldsymbol {x} _ {0}) + \frac {1}{2} m t ^ {2} + o (t ^ {2}) <   f (\boldsymbol {x} _ {0}) + \frac {1}{4} m t ^ {2} <   f (\boldsymbol {x} _ {0}).
$$

$$
f (\boldsymbol {x} _ {0} + t \boldsymbol {u} _ {2}) = f (\boldsymbol {x} _ {0}) + \frac {1}{2} M t ^ {2} + o (t ^ {2}) > f (\boldsymbol {x} _ {0}) + \frac {1}{4} M t ^ {2} > f (\boldsymbol {x} _ {0}).
$$

这说明  $f(x)$  在  $x_{0}$  取不到极值.

函数在退化驻点处的极值判定比较复杂, 通常要另行讨论. 需要注意的是, 设 $x_0$ 是 $f$ 的退化驻点, 那么即使 Hesse 矩阵 $H_f(x_0)$ 是半正 (负) 定, 也得不到函数的极值性. 这只要对比一下这几个函数在 $(0,0)$ 点处的情况即知: $f = \pm x^2 \pm y^4$.

但是, 如果  $H_{f}(x)$  在退化驻点  $x_{0}$  的某一个邻域内都是半正定的, 那么还是可以得到极值性结论的. 只不过此时的极值不一定是严格极值. 即, 我们有下面的结论:

定理 15.5.8 设 n 元函数 f 在  $x_{0}$  的一个邻域内有二阶连续偏导数,  $f_{\boldsymbol{x}}(\boldsymbol{x}_{0}) = \boldsymbol{0}$ . 记  $f(\boldsymbol{x})$  在 x 处的 Hesse 矩阵为  $\boldsymbol{H}_{f}(\boldsymbol{x})$ .

(1) 若  $H_{f}(x)$  在  $x_{0}$  的某邻域内都是半正定的，则 f 在  $x_{0}$  处取得极小值.
(2) 若  $H_{f}(x)$  在  $x_{0}$  的某邻域内都是半负定的，则 f 在  $x_{0}$  处取得极大值.

---

15.5 Taylor 公式

281

证明 我们只给出 (1) 的证明, (2) 的证明完全类似.

由假设, 对于某个 $\delta > 0$, 当 $\| \boldsymbol{x} \| < \delta$ 时, 根据 Taylor 公式的 Lagrange 余项表示, 我们有 $\theta = \delta_{\boldsymbol{x}} \in (0,1)$ 使得

$$
f (\boldsymbol {x} + \boldsymbol {x} _ {0}) = f (\boldsymbol {x} _ {0}) + \frac {1}{2} \boldsymbol {x} \boldsymbol {H} _ {f} (\boldsymbol {x} _ {0} + \theta \boldsymbol {x}) \boldsymbol {x} ^ {\mathrm{T}} \geqslant f (\boldsymbol {x} _ {0}). \tag {15.5.5}
$$

这就是说  $x_{0}$  为 f 的极小值点.

注 15.5.2 需要注意的是, 当 $x_0$ 是退化驻点时, 即使 $H_f(x)$ 在 $x_0$ 的任一邻域内都是不定的, 也得不到 $f$ 在 $x_0$ 处不是极值点的结论. 这是因为即使当 $x$ 在邻域内任意取值时, 我们也并不能保证关系式(15.5.5) 中, 总能取到既有不小于 $f(x_0)$ 的 $\theta$ 又有不大于 $f(x_0)$ 的 $\theta$.

事实上, 我们可以回顾一下一元函数时的例 7.5.1. 当然, 必要的话也可以由此例子中的函数 $f(x)$ 组装出一个二元函数 $f(x) + f(y)$ 或者 $f(\sqrt{x^2 + y^2})$.

例 15.5.3 考虑函数  $f(x,y)=x^{4}+y^{4}$ ，易知  $(0,0)$  是其退化驻点，在  $(0,0)$  的邻域内，有

$$
\boldsymbol {H} _ {f} (x, y) = \left( \begin{array}{c c} 1 2 x ^ {2} & 0 \\ 0 & 1 2 y ^ {2} \end{array} \right)
$$

是半正定的, 故  $(0,0)$  是 f 的极小值点.

例 15.5.4 求  $f(x,y)=x^{4}+y^{4}-(x+y)^{2}$  的极值点和极值.

解 先求 $f(x,y)$ 的驻点. 为此, 考虑

$$
0 = \frac {\partial f}{\partial x} = 4 x ^ {3} - 2 x - 2 y, \quad 0 = \frac {\partial f}{\partial y} = 4 y ^ {3} - 2 x - 2 y.
$$

上式有三个解

$$
P _ {0} = (0, 0), \quad P _ {1} = (1, 1), \quad P _ {2} = (- 1, - 1).
$$

为了判断它们的极值性, 考虑驻点处的 Hesse 矩阵:

$$
\boldsymbol {H} _ {f} (x, y) = \left( \begin{array}{c c} 1 2 x ^ {2} - 2 & - 2 \\ - 2 & 1 2 y ^ {2} - 2 \end{array} \right).
$$

易知在  $P_{1}, P_{2}$  处,  $H_{f}$  正定, 从而  $P_{1}, P_{2}$  为极小值点. 此时  $f(P_{1}) = f(P_{2}) = -2$ .

由于在 $P_0$ 处 $\pmb{H}_f$ 为退化矩阵, 即 $P_0$ 是退化驻点. 容易看出, 在 $(0,0)$ 的充分小邻域内, 总可以取到 $(x,0), |x| \ll 1$, 使得 $f(x,0) < 0$; 又总可以取 $(x, -x), |x| \ll 1$, 使得 $f(x, -x) = 2x^4 > 0$. 这说明 $P_0$ 不是极值点.

例 15.5.5 试在点集  $D := \{(x, y) | 0 \leqslant y \leqslant x, 0 \leqslant x \leqslant 3\}$  (图 15.8) 上讨论下面函数的取值范围:

$$
f (x, y) := 4 x ^ {3} - 8 x ^ {2} y + 1 6 x y ^ {2} - 3 3 x - 4 8 y.
$$

---

282

第十五章 多元函数微分学及其应用

![](../../raw/pages_0577-0592/images/page_586_image_2.jpg)

<details>
<summary>text_image</summary>

y
3
ℓ₃
D
ℓ₂
O
ℓ₁
3
x
</details>

图15.8

解 我们只要求出 $f$ 在 $D$ 上的最大值和最小值. 由于 $f$ 连续可微, 其最大值和最小值在边界或驻点取得.

(1) 在边界 $\ell_1: y = 0, 0 \leqslant x \leqslant 3$ 上, 有 $f(x,0) = 4x^3 - 33x$. 该函数在 $[0,3]$ 上有驻点 $\frac{\sqrt{11}}{2}$. 因此, $f$ 在 $\ell_1$ 上可能的最值点为 $(0,0)$, $\left(\frac{\sqrt{11}}{2}, 0\right)$ 以及 $(3,0)$.
(2) 在边界 $\ell_2: x = 3, 0 \leqslant y \leqslant 3$ 上, 有 $f(3, y) = 9 - 120y + 48y^2$. 该函数在 $[0, 3]$ 上有驻点 $\frac{5}{4}$. 因此, $f$ 在 $\ell_2$ 上可能的最值点为 $(3, 0)$, $\left(3, \frac{5}{4}\right)$ 以及 $(3, 3)$.
(3) 在边界 $\ell_3: y = x, 0 \leqslant x \leqslant 3$ 上, 有 $f(x, x) = 12x^3 - 81x$. 该函数在 $[0, 3]$ 上有驻点 $\frac{3}{2}$. 因此, $f$ 在 $\ell_3$ 上可能的最值点为 $(0, 0)$, $\left(\frac{3}{2}, \frac{3}{2}\right)$ 和 $(3, 3)$.
(4) 在 $f$ 定义域的内部, $f$ 可能的最值点必为驻点, 它为以下方程的解:

$$
\left\{ \begin{array}{l} f _ {x} (x, y) = 1 2 x ^ {2} - 1 6 x y + 1 6 y ^ {2} - 3 3 = 0, \\ f _ {y} (x, y) = - 8 x ^ {2} + 3 2 x y - 4 8 = 0. \end{array} \right.
$$

求得 $D$ 内的驻点有 $\left(2, \frac{5}{4}\right)$.

计算得到

$$
f (0, 0) = 0, \quad f (3, 0) = 9, \quad f (3, 3) = 8 1,
$$

$$
f \left(\frac {\sqrt {1 1}}{2}, 0\right) = - 1 1 \sqrt {1 1}, \quad f \left(3, \frac {5}{4}\right) = - 6 6, \quad f \left(\frac {3}{2}, \frac {3}{2}\right) = - 8 1, \quad f \left(2, \frac {5}{4}\right) = - 8 4.
$$

因此, $f$ 在 $D$ 上的取值范围是 $[-84, 81]$.

例 15.5.6 试求下面函数的极值:

(1) $f(x,y)=x^{2}+y^{3}-3y;$

(2) $g(x,y) = (y - x^2)(y - 2x^2)$.

解 (1) 容易算出 $f$ 的驻点: $(0,1), (0,-1)$. 又可以计算其 Hesse 矩阵:

$$
\boldsymbol {H} _ {f} (0, 1) = \left( \begin{array}{c c} 2 & 0 \\ 0 & 6 \end{array} \right), \quad \boldsymbol {H} _ {f} (0, - 1) = \left( \begin{array}{c c} 2 & 0 \\ 0 & - 6 \end{array} \right).
$$

---

15.5 Taylor 公式

283

故 $(0, -1)$ 不是极值点而 $(0, 1)$ 为极小值点, 极小值为 $f(0, 1) = -2$.

(2) 容易算出 $(0,0)$ 是 $g$ 的唯一驻点. 在每一条经过 $(0,0)$ 的直线上, $(0,0)$ 都是极小值点, 但它不是 $g$ 在平面上的极值点.

注意曲面 $z = g(x,y)$ 的几何特点对进一步理解题目结论是有益的.

例 15.5.7 求  $f(x,y)=x^{2}+y^{2}(1+x)^{3}$  的极值.

解 容易求得 $(0,0)$ 为 $f$ 的唯一驻点, 且为极小值点, 但 $f(-2,3) = -5 < f(0,0) = 0$, 因此 $(0,0)$ 不是最小值点. □

本例揭示了多元函数和一元函数不同之处: 一元函数的唯一极值点必为最值点.

例 15.5.8 存在有多个 (甚至无穷多个) 极大值点, 但可能无极小值点的多元函数.

解 可以考察例子 $f(x, y) = (1 + \mathrm{e}^y) \cos x - y \mathrm{e}^y$，直接验证.

例 15.5.9 设  $f \in C^{2}(\mathbb{R}^{n})$ ，如果  $H_{f} \geqslant I_{n}$  总成立，其中  $I_{n}$  为 n 阶单位方阵，证明:f 有唯一的最小值点.

证明 根据 Taylor 公式, f 可在原点处展开为

$$
f (\boldsymbol {x}) = f (\boldsymbol {0}) + \nabla f (\boldsymbol {0}) \cdot \boldsymbol {x} + \frac {1}{2} \boldsymbol {x} \boldsymbol {H} _ {f} (\boldsymbol {\xi}) \boldsymbol {x} ^ {\mathrm{T}}.
$$

由假设得

$$
f (\boldsymbol {x}) \geqslant f (\boldsymbol {0}) + \nabla f (\boldsymbol {0}) \cdot \boldsymbol {x} + \frac {1}{2} \| \boldsymbol {x} \| ^ {2}, \quad \forall \boldsymbol {x} \in \mathbb {R} ^ {n}.
$$

特别地, 当 $\| \pmb{x} \| \to \infty$ 时, $f(\pmb{x}) \to \infty$, 这说明 $f$ 的最小值存在. 设 $\pmb{x}_0$ 为最小值点. 在 $\pmb{x}_0$ 处, $\nabla f(\pmb{x}_0) = 0$, 且 $f$ 的 Taylor 公式形如

$$
f (\boldsymbol {x}) = f (\boldsymbol {x} _ {0}) + \frac {1}{2} (\boldsymbol {x} - \boldsymbol {x} _ {0}) \boldsymbol {H} _ {f} (\boldsymbol {\zeta}) (\boldsymbol {x} - \boldsymbol {x} _ {0}) ^ {\mathrm{T}},
$$

由已知条件得 $f(\pmb {x})\geqslant f(\pmb {x}_0) + \frac{1}{2}\| \pmb {x} - \pmb {x}_0\| ^2$ ，特别地， $\pmb{x_0}$ 为唯一的最小值点.

例 15.5.10 (最小二乘法) 设  $(x_{i}, y_{i})$  ( $i = 1, 2, \cdots, n$ ) 为平面  $R^{2}$  上 n 个互异点，求一条直线  $y = ax + b$ ，使得  $F(a, b) = \sum_{i=1}^{n} (ax_{i} + b - y_{i})^{2}$  最小.

解 $F(a,b)$ 是关于 $(a,b)$ 的光滑函数，其驻点必满足

$$
\frac {\partial F}{\partial a} = 2 \sum_ {i = 1} ^ {n} x _ {i} (a x _ {i} + b - y _ {i}) = 0,
$$

$$
\frac {\partial F}{\partial b} = 2 \sum_ {i = 1} ^ {n} (a x _ {i} + b - y _ {i}) = 0,
$$

可得唯一驻点

$$
a = c ^ {- 1} \left(n \sum_ {i = 1} ^ {n} x _ {i} y _ {i} - \sum_ {i = 1} ^ {n} x _ {i} \sum_ {i = 1} ^ {n} y _ {i}\right),
$$

$$
b = c ^ {- 1} \left(\sum_ {i = 1} ^ {n} x _ {i} ^ {2} \sum_ {i = 1} ^ {n} y _ {i} - \sum_ {i = 1} ^ {n} x _ {i} \sum_ {i = 1} ^ {n} x _ {i} y _ {i}\right),
$$

---

284

第十五章 多元函数微分学及其应用

其中

$$
c = n \sum_ {i = 1} ^ {n} x _ {i} ^ {2} - \left(\sum_ {i = 1} ^ {n} x _ {i}\right) ^ {2} = \frac {1}{2} \sum_ {i \neq j} (x _ {i} - x _ {j}) ^ {2} > 0.
$$

由于当 $\| (a,b)\| \to \infty$ 时 $F(a,b)\to \infty ,F$ 有最小值，从而求出的唯一驻点必为最小值点.此时，所求直线方程可写为

$$
\left| \begin{array}{c c c} x & y & 1 \\ \sum_ {i = 1} ^ {n} x _ {i} & \sum_ {i = 1} ^ {n} y _ {i} & n \\ \sum_ {i = 1} ^ {n} x _ {i} ^ {2} & \sum_ {i = 1} ^ {n} x _ {i} y _ {i} & \sum_ {i = 1} ^ {n} x _ {i} \end{array} \right| = 0.
$$

## 习题 15.5

1. 利用微分作近似计算:

(1) $1.002^{2} \times 2.003^{2} \times 3.004^{3}$; (2) $0.97^{1.05}$.

2. 设 $f$ 为 $C^k$ 函数, 记 $\varphi(t) = f(\boldsymbol{a} + t(\boldsymbol{x} - \boldsymbol{a}))$, 利用数学归纳法证明:

$$
\varphi^ {(k)} (t) = \sum_ {| \alpha | = k} \frac {k !}{\alpha !} D ^ {\alpha} f (\boldsymbol {a} + t (\boldsymbol {x} - \boldsymbol {a})) (\boldsymbol {x} - \boldsymbol {a}) ^ {\alpha}.
$$

3. 求下列函数在指定点处的 Taylor 展开:

(1) $f(x,y) = 2x^{2} - xy - y^{2} - 6x - 3y + 5, (x,y) = (1, -2)$.
(2) $f(x,y,z) = x^{3} + y^{3} + z^{3} - 3xyz,\quad (x,y,z) = (1,1,1).$
(3) $f(x,y) = (1 + x)^{m}(1 + y)^{n},\quad m,n$ 为正整数， $(x,y) = (0,0)$
(4) $f(x,y) = \mathrm{e}^{x + y},\quad (x,y) = (0,0).$

4. 设函数 $f$ 的直到 $m$ 阶的各种偏导数都在 $a$ 处连续, 且在 $a$ 附近, 有

$$
f (x) = \sum_ {k = 0} ^ {m} \sum_ {| \alpha | = k} c _ {\alpha} (\boldsymbol {x} - \boldsymbol {a}) ^ {\alpha} + o (\| \boldsymbol {x} - \boldsymbol {a} \| ^ {m}).
$$

证明: $c_{\alpha} = \frac{1}{\alpha!} D^{\alpha}f(\pmb {a}),\forall |\pmb {\alpha}|\leqslant m.$

5. 对下列函数作 Taylor 展开到指定项:

(1) $f(x,y)=x^{y}$ ，在(1,1)处展开到二次项.
(2) $f(x,y) = \frac{\cos x}{\cos y}$, 在 $(0,0)$ 处展开到二次项.
(3) $f(x,y)=\sin(x^{2}+y^{2})$ ，在(0,0)处展开到六次项.
(4) $f(x,y) = \arctan \frac{y}{1 + x^2}$, 在 $(0,0)$ 处展开到四次项.

6. 将下列多项式在指定点处展开成 Taylor 多项式:

---

15.5 Taylor公式

285

(1) $2x^{2}-xy-y^{2}-6x-3y+5$ 在点 $(1,-2)$ 处.
(2) $x^{3}+y^{3}+z^{3}-3xyz$ 在点 $(1,1,1)$ 处.

7. 考察二次多项式

$$
f (x, y, z) = \left( \begin{array}{c c c} x & y & z \end{array} \right) \left( \begin{array}{c c c} A & D & F \\ D & B & E \\ F & E & C \end{array} \right) \left( \begin{array}{c} x \\ y \\ z \end{array} \right),
$$

将 $f(x + \Delta x, y + \Delta y, z + \Delta z)$ 按 $\Delta x, \Delta y, \Delta z$ 的正整数幂展开.

8. 将  $x^{r}$  (r > 0) 在点 (1, 1) 作 Taylor 展开, 写到二次项.

9. 设函数  $F(x,y)$  在  $(x_{0},y_{0})$  的某邻域内二阶连续可微, 且

$$
\frac {\partial F \left(x _ {0} , y _ {0}\right)}{\partial x} = 0, \quad \frac {\partial F \left(x _ {0} , y _ {0}\right)}{\partial y} > 0, \quad \frac {\partial^ {2} F \left(x _ {0} , y _ {0}\right)}{\partial x ^ {2}} <   0.
$$

设 $y = y(x)$ 是由 $F(x,y) = 0$ 确定的函数. 试讨论上述条件下 $y = y(x)$ 在 $x_0$ 处的极值性.

10. 设 $f$ 为凸域 $D$ 中的可微函数. 证明: $f$ 为凸函数当且仅当

$$
(\nabla f (\boldsymbol {x}) - \nabla f (\boldsymbol {y})) \cdot (\boldsymbol {x} - \boldsymbol {y}) \geqslant 0, \quad \forall \boldsymbol {x}, \boldsymbol {y} \in D.
$$

11. 求下列函数的驻点, 并判断是否为极值点, 是什么类型的极值点:

(1) $f(x,y)=y^{2}(\sin x-x/2);$

(2) $f(x,y)=\cos(x+y)+\sin(x-y);$

(3) $f(x,y)=y^{x};$

(4) $f(x,y)=x/y-xy;$

(5) $f(x,y)=(x^{2}+y^{2})\mathrm{e}^{-x^{2}-y^{2}};$

(6) $f(x,y) = y\mathrm{e}^{-x^2}$

12. 求下列函数的极值:

(1) $f(x,y)=4(x-y)-x^{2}-y^{2};$

(2) $f(x,y)=x^{2}+(y-1)^{2};$

(3) $f(x,y)=x^{2}+xy+y^{2}+x-y+1;$

(4) $f(x,y) = x^{3} + y^{3} - 3xy.$

13. 设 $f(x, y) = 4x^2y - x^4 - 2y^2$，证明 (0,0) 是鞍点。但点 (0,0) 是一元函数 $g(t) = f(t\cos \theta, t\sin \theta)$ 的极大值点。

14. 设 $D \subseteq \mathbb{R}^n$ 为区域, $f \in C^2(D)$. 如果 $\Delta f \geqslant 0$, 证明: $f$ 在 $D$ 内无极大值点, 除非 $f$ 为常值函数.

15. 设  $x^{1}, \cdots, x^{k}$  为  $R^{n}$  中的有限个点. 记  $\varphi(x) = \sum_{i=1}^{k} \|x - x^{i} \|, \psi(x) = \sum_{i=1}^{k} \|x - x^{i} \|^{2}$ . 证明  $\varphi, \psi$  为凸函数, 并求  $\psi$  的最小值点.

16. 求函数 $f(x, y) = xy \sqrt{1 - \frac{x^2}{a^2} - \frac{y^2}{b^2}}$ ($a > 0, b > 0$) 的极值.

17. 设函数 $z(x, y)$ 是有界闭区域 $D$ 上的连续函数, 在 $D$ 内部偏导数存在, 在 $D$ 的边界上其值为 0 , 在 $D$ 的内部满足 $z_{x} + z_{y} = f(z)$, 其中 $f$ 是一个严格单调函数, $f(0) = 0$. 证明: $z(x, y) \equiv 0 ((x, y) \in D)$.

---

286

第十五章 多元函数微分学及其应用

18. 设 $z = f(x, y)$ 是定义在整个平面上的光滑函数, 对每一个 $\alpha$, 定义一元函数 $g_{\alpha}(t) = f(t \cos \alpha, t \sin \alpha)$. 若对任何的 $\alpha$, 有 $\frac{\mathrm{d}g_{\alpha}(0)}{\mathrm{d}t} = 0$, $\frac{\mathrm{d}^2 g_{\alpha}(0)}{\mathrm{d}t^2} > 0$. 证明: 点 $(0, 0)$ 是 $f(x, y)$ 的极小值点.

19. 设 $z = f(x, y)$ 是定义在整个平面上的光滑函数, 对每一个 $\alpha$, 定义一元函数 $g_{\alpha}(t) = f(t \cos \alpha, t \sin \alpha)$. 若对任何的 $\alpha$, 函数 $g_{\alpha}(x)$ 在 $x = 0$ 处都取到极小值. 问: 点 $(0, 0)$ 一定是 $f(x, y)$ 的极小值点吗?

20. 证明: (1) 定义在凸域上的多元凸函数一定是连续函数.

(2) 凸函数的局部极小必为整体极小. 即: 如果 $f(\pmb{x})$ 是开区域 $D \subseteq \mathbb{R}^n$ 上的凸函数, $P_0 \in D$ 是 $f(\pmb{x})$ 的极小值点, 那么它也是 $f(\pmb{x})$ 在 $D$ 上的最小值点.

21. 设点  $\boldsymbol{a}=(a_{1},a_{2},\cdots,a_{n})$  是多元函数  $y=f(x_{1},x_{2},\cdots,x_{n})$  的极大值点，且在点 a 处二阶偏导数  $f_{x_{i}x_{i}}, i=1,2,\cdots,n$  都存在。证明:

$$
\Delta f (a _ {1}, a _ {2}, \dots , a _ {n}) = \sum_ {i = 1} ^ {n} \frac {\partial^ {2} f}{\partial x _ {i} ^ {2}} (a _ {1}, a _ {2}, \dots , a _ {n}) \leqslant 0.
$$

22. 设 $f(x, y, z)$ 是 $C^2$ 的 $n$ 次齐次函数, 证明:

$$
\left(x \frac {\partial}{\partial x} + y \frac {\partial}{\partial y} + z \frac {\partial}{\partial z}\right) ^ {n} f (x, y, z) = n! f (x, y, z).
$$

23. 设有界区域 $D \subset \mathbb{R}^n$ 有光滑边界, 如果 $f(\pmb{x})$ 是 $\overline{D}$ 上的 $C^2$ 函数, 满足 $\Delta f(\pmb{x}) > 0$, 证明: $f(\pmb{x})$ 不可能在 $D$ 的内部达到最大值.

24. 设 $D \subset \mathbb{R}^n$ 是有界闭区域, $u = u(\pmb{x})$ 是 $D$ 内的 $C^2$ 函数, 满足

$$
\Delta u + c u = 0, \quad \text {其中} c <   0 \text {为常数}.
$$

证明: $u$ 在 $D$ 上的正的最大值 (负的最小值) 不可能在 $D$ 的内部达到. 而且, 如果 $u$ 在 $D$ 上连续, 在 $D$ 的边界 $\partial D$ 上为零, 则 $u$ 在 $D$ 上恒为零.

## 15.6 隐函数存在定理

本节考虑由方程 $F(\pmb {x},\pmb {y}) = 0$ 确定的隐函数 $\pmb {y} = \pmb {y}(\pmb {x})$ 的存在性问题以及相应的分析性质.主要包括三个基本定理，隐函数存在定理、隐函数方程组存在定理(隐映射定理)，逆映射存在定理(逆映射定理).三者紧密相关，在数学分析中都具有极其重要的地位和理论意义，同时在相关分支中，有着广泛的应用.

---

15.6 隐函数存在定理

287

## 1. 单个方程的情形

首先, 我们讨论单个方程时隐函数存在的充分条件. 为此, 我们先 “掩耳盗铃” 一下, 分析下面这个夸张的例子:

考虑隐函数 $F(x, y) = ax + by + c = 0$，问何时可由此方程确定出 $y$ 是 $x$ 的函数关系 $y = y(x)$? 即，在 $F = 0$ 限定条件下，在使得 $F$ 有意义的范围内，任给一个 $x$，都能断定存在唯一的一个 $y$ 使得 $F = 0$ 成立.

对于这个具体问题, 答案是显而易见的. 即, 如果 $b \neq 0$, 则可以唯一确定一个函数关系 $y = y(x)$. 而且, 至于 $x$ 是一元变量还是多元变量, 都丝毫不影响 $y$ 是 $x$ 的函数关系. 那么 $b \neq 0$ 这个条件, 在稍微更一般的表达式 $F(x, y) = 0$ 中, 又是如何表现的呢? 事实上, 稍微分析一下可解的本质, 即可发现, 当 $x$ 做微小改变时, 要使得 $y$ 以函数关系依赖于 $x$, 必须导致 $y$ 也产生变动. 把这个表现抽取出来, 即为 $F_y(x, y) \neq 0$.

定理 15.6.1 (隐函数存在定理) 设  $\Omega \subseteq R^{n}$  为区域, F 是定义在  $\Omega \times (a, b)$  上的  $C^{1}$  函数, 设  $x_{0} \in \Omega, y_{0} \in (a, b)$ , 满足

(1) $F(\boldsymbol{x}_{0},y_{0})=0.$
(2) $F_{y}(\boldsymbol{x}_{0}, y_{0}) \neq 0.$

则存在 $\delta > 0$ 以及 $\eta > 0$, 使得对任何 $\pmb{x} \in B_{\delta}(\pmb{x}_0)$, 存在唯一的 $y = \varphi(\pmb{x}) \in (y_0 - \eta, y_0 + \eta)$ 使得

$$
F (\boldsymbol {x}, \varphi (\boldsymbol {x})) \equiv 0.
$$

进一步， $\varphi (\pmb {x})$ 在 $B_{\delta}(\pmb{x}_0)$ 内连续可微，且

$$
\varphi_ {\boldsymbol {x}} (\boldsymbol {x}) = - \frac {F _ {\boldsymbol {x}} (\boldsymbol {x} , \varphi (\boldsymbol {x}))}{F _ {y} (\boldsymbol {x} , \varphi (\boldsymbol {x}))}, \quad \forall \boldsymbol {x} \in B _ {\delta} (\boldsymbol {x} _ {0}). \tag {15.6.1}
$$

注意, 定理中的符号  $\varphi_{\boldsymbol{x}}(\boldsymbol{x})$  和  $F_{\boldsymbol{x}}(\boldsymbol{x}, \varphi(\boldsymbol{x}))$  的含义是指偏导数对应的分量相等. 用分量表示则为:

设  $F(\boldsymbol{x},y)=F(x_{1},x_{2},\cdots,x_{n},y)$ ,  $y=\varphi(\boldsymbol{x})=\varphi(x_{1},x_{2},\cdots,x_{n})$ . 关系式 (15.6.1) 等价于

$$
\frac {\partial y}{\partial x _ {i}} = \varphi_ {x _ {i}} (\boldsymbol {x}) = - \frac {F _ {x _ {i}} (\boldsymbol {x} , \varphi (\boldsymbol {x}))}{F _ {y} (\boldsymbol {x} , \varphi (\boldsymbol {x}))}, \quad i = 1, 2, \dots , n, \forall \boldsymbol {x} \in B _ {\delta} (\boldsymbol {x} _ {0}).
$$

证明 不妨设 $\gamma \equiv F_y(x_0, y_0) > 0$. 由 $F_y$ 的连续性, 存在 $\delta_0 > 0, \eta > 0$ 使得

$$
F _ {y} (\boldsymbol {x}, y) > \frac {\gamma}{2} > 0, \quad \forall (\boldsymbol {x}, y) \in B _ {\delta_ {0}} (\boldsymbol {x} _ {0}) \times [ y _ {0} - \eta , y _ {0} + \eta ]. \tag {15.6.2}
$$

因此， $F(\pmb{x}_0,y_0 + \eta) > F(\pmb{x}_0,y_0) = 0 > F(\pmb{x}_0,y_0 - \eta)$ 进一步，由 $F$ 的连续性，存在$\delta \in (0,\delta_0)$ 使得

$$
F (\boldsymbol {x}, y _ {0} + \eta) > 0 > F (\boldsymbol {x}, y _ {0} - \eta), \quad \forall \boldsymbol {x} \in B _ {\delta} (\boldsymbol {x} _ {0}). \tag {15.6.3}
$$

---

288

第十五章 多元函数微分学及其应用

对于固定的  $\boldsymbol{x} \in B_{\delta}(\boldsymbol{x}_{0})$ ，由介值定理，并注意到  $F(\boldsymbol{x}, y)$  关于 y 在  $[y_{0} - \eta, y_{0} + \eta]$  上严格单增，我们知有唯一的  $\varphi(\boldsymbol{x}) \in (y_{0} - \eta, y_{0} + \eta)$  满足  $F(\boldsymbol{x}, \varphi(\boldsymbol{x})) = 0$ 。进一步，对于  $x_{1}, x_{2} \in B_{\delta}(\boldsymbol{x}_{0})$ ，由 (15.6.2) 式，我们有

$$
\begin{array}{l} \frac {\gamma}{2} | \varphi (\boldsymbol {x} _ {1}) - \varphi (\boldsymbol {x} _ {2}) | \leqslant \left| F (\boldsymbol {x} _ {1}, \varphi (\boldsymbol {x} _ {1})) - F (\boldsymbol {x} _ {1}, \varphi (\boldsymbol {x} _ {2})) \right| \\ = \big | F (\pmb {x} _ {2}, \varphi (\pmb {x} _ {2})) - F (\pmb {x} _ {1}, \varphi (\pmb {x} _ {2})) \big |. \tag {15.6.4} \\ \end{array}
$$

从而由 $F$ 的连续性即得 $\varphi$ 在 $\pmb{x} \in B_{\delta}(\pmb{x}_0)$ 内连续。另一方面，固定 $\pmb{x} \in B_{\delta}(\pmb{x}_0)$，当 $0 < |\Delta \pmb{x}| < \delta - |\pmb{x} - \pmb{x}_0|$ 时，由微分中值定理，存在 $\theta \equiv \theta_{\pmb{x}, \Delta \pmb{x}} \in (0,1)$ 使得

$$
\begin{array}{l} 0 = F (\boldsymbol {x} + \Delta \boldsymbol {x}, \varphi (\boldsymbol {x} + \Delta \boldsymbol {x})) - F (\boldsymbol {x}, \varphi (\boldsymbol {x})) \\ = F _ {\boldsymbol {x}} (\boldsymbol {x} + \theta \Delta \boldsymbol {x}, \varphi (\boldsymbol {x}) + \theta \Delta y) \Delta \boldsymbol {x} + F _ {y} (\boldsymbol {x} + \theta \Delta \boldsymbol {x}, \varphi (\boldsymbol {x}) + \theta \Delta y) \Delta y, \tag {15.6.5} \\ \end{array}
$$

其中  $\Delta y := \varphi(\boldsymbol{x} + \Delta\boldsymbol{x}) - \varphi(\boldsymbol{x})$ . 因此,

$$
\begin{array}{l} \varphi (\boldsymbol {x} + \Delta \boldsymbol {x}) - \varphi (\boldsymbol {x}) = - \frac {F _ {\boldsymbol {x}} (\boldsymbol {x} + \theta \Delta \boldsymbol {x} , \varphi (\boldsymbol {x}) + \theta \Delta y)}{F _ {y} (\boldsymbol {x} + \theta \Delta \boldsymbol {x} , \varphi (\boldsymbol {x}) + \theta \Delta y)} \Delta \boldsymbol {x} \\ = - \frac {F _ {\boldsymbol {x}} (\boldsymbol {x} , \varphi (\boldsymbol {x}))}{F _ {y} (\boldsymbol {x} , \varphi (\boldsymbol {x}))} \Delta \boldsymbol {x} + r (\boldsymbol {x}, \Delta \boldsymbol {x}), \tag {15.6.6} \\ \end{array}
$$

其中

$$
\lim _ {\Delta \boldsymbol {x} \to 0} \frac {| r (\boldsymbol {x} , \Delta \boldsymbol {x}) |}{| \Delta \boldsymbol {x} |} = \lim _ {\Delta \boldsymbol {x} \to 0} \frac {1}{| \Delta \boldsymbol {x} |} \left| \left(\frac {F _ {\boldsymbol {x}} (\boldsymbol {x} + \theta \Delta \boldsymbol {x} , \varphi (\boldsymbol {x}) + \theta \Delta y)}{F _ {y} (\boldsymbol {x} + \theta \Delta \boldsymbol {x} , \varphi (\boldsymbol {x}) + \theta \Delta y)} - \frac {F _ {\boldsymbol {x}} (\boldsymbol {x} , \varphi (\boldsymbol {x}))}{F _ {y} (\boldsymbol {x} , \varphi (\boldsymbol {x}))}\right) \Delta \boldsymbol {x} \right| = 0. \tag {15.6.7}
$$

故 $\varphi$ 在 $B_{\delta}(\pmb{x}_0)$ 内连续可微且(15.6.1)式成立.

注15.6.1 定理的结果表明方程 $F(\pmb{x},y) = 0$ 在 $(\pmb{x}_0,y_0)$ 附近确定（唯一的）一个隐函数 $y = \varphi (\pmb {x})$ .需要强调这里的唯一性是指 $\varphi (\pmb {x})$ 的取值是限制在 $y_{0}$ 的一个邻域内的.在更大的范围内，唯一性自然不一定成立.因此，我们不能说方程 $F(\pmb {x},y) = 0$ 在 $\pmb{x}_0$ 附近唯一地确定了一个隐函数.

例如, 对于方程 $F(x,y) \equiv x^{2} + y^{2} - 1 = 0$, 以及 $(x_0,y_0) = \left(\frac{\sqrt{2}}{2},\frac{\sqrt{2}}{2}\right)$, 可得 $F(x_0,y_0) = 0$ 以及 $F_y(x_0,y_0) \neq 0$. 该方程在 $(x_0,y_0)$ 附近, $x \in (x_0 - \delta, x_0 + \delta)$, 确定一个隐函数 $y(x) = \sqrt{1 - x^2}$. 而方程 $F = 0$ 本身对应于 $x \in (x_0 - \delta, x_0 + \delta)$ 的解并不唯一: $y(x) = \pm \sqrt{1 - x^2}$. 所以如果考虑 $(x_0,y_0)$ 附近的函数关系, 则把 $y(x) = -\sqrt{1 - x^2}$ 排除在外了.

注 15.6.2 当 F 的光滑性不同时, 定理有多种不同的版本. 粗略说来, 如果定理中 F 是  $C^{k}$  光滑函数  $(k=1,2,\cdots,\infty)$ , 那么定理中的  $\varphi(\boldsymbol{x})$  也将是  $C^{k}$  光滑的.

---

15.6 隐函数存在定理

289

另外, 从定理的证明可以看出, 如果仅要求函数 $y = \varphi(\boldsymbol{x})$ 的 (局部) 存在性, 而不关心 $\varphi(\boldsymbol{x})$ 的导数的话, 那么在其他条件不变的情况下, 条件 $F: \Omega \times (a, b) \to \mathbb{R}$ 是 $C^1(\Omega \times (a, b))$ 函数, 可以不要求 $F_{\boldsymbol{x}}(\boldsymbol{x}, y)$ 连续, 甚至可以不存在.

进一步, 定理还可以有相应的 $C^0$ 版本. 即, 如果定理中 $F$ 是 $C^0$ 连续函数, 而且关于 $y$ 严格单调, 则 $\varphi(x)$ 存在且也是连续的. 这里关于 $y$ 严格单调的假设起到 $C^1$ 框架下 $F_y \neq 0$ 的作用.

定理中的条件 $F_{y}(\pmb{x}_{0},y_{0})\neq 0$ 是充分而非必要的.例如，考虑隐函数 $F(x,y) = y^{3} - x^{3} = 0$ 在点 $(x_0,y_0) = (0,0)$ 附近，我们一方面有 $F_{y}(0,0) = 0$ ，但另一方面，方程显然可以确定唯一的函数关系 $y = x$

例 15.6.1 设  $x = x(y, z)$ ,  $y = y(x, z)$ ,  $z = z(x, y)$  都是由  $F(x, y, z) = 0$  确定的隐函数, 假设它们具有连续的偏导数, 试证明:

$$
\frac {\partial x}{\partial y} \frac {\partial y}{\partial z} \frac {\partial z}{\partial x} = - 1, \quad \frac {\partial x}{\partial y} \frac {\partial x}{\partial z} \frac {\partial y}{\partial x} \frac {\partial y}{\partial z} \frac {\partial z}{\partial x} \frac {\partial z}{\partial y} = 1.
$$

证明 由隐函数存在定理, 得

$$
\frac {\partial x}{\partial y} = - \frac {F _ {y}}{F _ {x}}, \quad \frac {\partial y}{\partial z} = - \frac {F _ {z}}{F _ {y}}, \quad \frac {\partial z}{\partial x} = - \frac {F _ {x}}{F _ {z}},
$$

代入即可. 同理可证第二个关系式.

例15.6.2 考虑Kepler方程

$$
y - x - \varepsilon \sin y = 0, \quad 0 <   \varepsilon <   1,
$$

确定的隐函数  $y = f(x)$ ，求  $f'(x)$ .

解 把 $y$ 视为 $x$ 的函数 $y = f(x)$, 即 $f(x) - x - \varepsilon \sin f(x) \equiv 0$. 方程两端对 $x$ 求导数, 得

$$
f ^ {\prime} (x) (1 - \varepsilon \cos f (x)) - 1 = 0.
$$

即

$$
f ^ {\prime} (x) = \frac {1}{1 - \varepsilon \cos f (x)}.
$$

## 2. 方程组的情形

上面对单个方程的隐函数讨论可以推广到多个方程, 即方程组的情况, 或者说向量值函数 (即映射) 的情况. 为了更深刻理解更一般的情况, 我们以线性代数中的方程组为例来说明其基本思想.

---

290

第十五章 多元函数微分学及其应用

考虑由两个方程组成的方程组的求解问题:

$$
\left\{ \begin{array}{l} F (x, u, v) = 0, \\ G (x, u, v) = 0. \end{array} \right.
$$

对比前面讨论的单个方程的情形, 如果我们希望由 $F(x,y) = 0$ 解出 $y$ 关于 $x$ 的函数, 则是通过假设 $F_{y}(x,y) \neq 0$ 来保证的. 现在在多个方程时, $F_{y}(x,y) \neq 0$ 的表现形式如何?

为此, 我们仍然返回到更简单的情况: 设

$$
\left\{ \begin{array}{l} F (x, u, v) = f _ {x} x + a _ {u} u + a _ {v} v, \\ G (x, u, v) = g _ {x} x + b _ {u} u + b _ {v} v, \end{array} \right.
$$

其中 $a_{u}, a_{v}, b_{u}, b_{v}, f_{x}, g_{x}$ 均为常数. 此时我们的问题无异于求解方程组

$$
\left\{ \begin{array}{l} a _ {u} u + a _ {v} v = - f _ {x} x, \\ b _ {u} u + b _ {v} v = - g _ {x} x. \end{array} \right.
$$

由线性代数的理论知, 这个方程组有唯一解的充要条件是其系数行列式

$$
\left| \begin{array}{c c} a _ {u} & a _ {v} \\ b _ {u} & b _ {v} \end{array} \right| = a _ {u} b _ {v} - a _ {v} b _ {u} \neq 0.
$$

注意到

$$
F _ {u} = a _ {u}, \quad F _ {v} = a _ {v}, \quad G _ {u} = b _ {u}, \quad G _ {v} = b _ {v}.
$$

因此我们猜测对于一般的 $F$ 和 $G$, 条件

$$
\left| \begin{array}{c c} F _ {u} & F _ {v} \\ G _ {u} & G _ {v} \end{array} \right| \neq 0
$$

可以保证隐函数方程组的可解性. 自然, 由于是非线性情况, 这里的可解很有可能是局部的. 另外, 我们也看出, 这里的 $x$ 是一元变量还是多元变量, 丝毫不影响 $u, v$ 的可解性. 换句话说, 这里的关键是上面行列式的非零性.

给定可微函数 $F(x,y),G(x,y)$ ，我们称行列式

$$
\left| \begin{array}{c c} F _ {u} & F _ {v} \\ G _ {u} & G _ {v} \end{array} \right|
$$

为 $F, G$ 的 Jacobi 行列式, 记作

$$
J = \frac {\partial (F , G)}{\partial (u , v)} = \left| \begin{array}{c c} F _ {u} & F _ {v} \\ G _ {u} & G _ {v} \end{array} \right|.
$$

---

15.6 隐函数存在定理

291

更一般地, $n$ 个可微函数 $F_{i}(x_{1}, x_{2}, \cdots, x_{n}), i = 1, 2, \cdots, n$ 的 Jacobi 行列式是一个 $n \times n$ 矩阵给出的行列式, 定义为

$$
J = \frac {\partial (F _ {1} , F _ {2} , \cdots , F _ {n})}{\partial (x _ {1} , x _ {2} , \cdots , x _ {n})} = \det \left(\frac {\partial F _ {i}}{\partial x _ {j}}\right).
$$

我们有下面的定理:

定理 15.6.2（隐映射定理） 设  $W \subseteq R^{n} \times R^{m}$  为开集, W 中的点用  $(x, y)$  表示, 其中  $\boldsymbol{x} = (x_{1}, x_{2}, \cdots, x_{n})$ ,  $\boldsymbol{y} = (y_{1}, y_{2}, \cdots, y_{m})$ . 设

$$
\boldsymbol {F} (\boldsymbol {x}, \boldsymbol {y}) = (F _ {1} (\boldsymbol {x}, \boldsymbol {y}), F _ {2} (\boldsymbol {x}, \boldsymbol {y}), \dots , F _ {m} (\boldsymbol {x}, \boldsymbol {y}))
$$

是 $W$ 到 $\mathbb{R}^m$ 的 $C^1$ 映射， $(\pmb{x}_0,\pmb{y}_0)\in W$ ，满足

(i)  $\boldsymbol{F}(\boldsymbol{x}_{0}, \boldsymbol{y}_{0}) = \boldsymbol{0}.$
(ii)  $\det J_{\mathbf{y}}\mathbf{F}(\mathbf{x}_{0},\mathbf{y}_{0})\neq0,$  其中  $J_{\mathbf{y}}\mathbf{F}(\mathbf{x},\mathbf{y})=\left(\frac{\partial F_{i}}{\partial y_{j}}(\mathbf{x},\mathbf{y})\right)_{m\times m}.$

则存在  $x_{0}$  的开邻域  $V \subseteq R^{n}$  以及唯一的  $C^{1}$  映射  $\psi: V \to R^{m}$ ，使得

(1) $\boldsymbol{y}_{0}=\psi(\boldsymbol{x}_{0}),\boldsymbol{F}(\boldsymbol{x},\psi(\boldsymbol{x}))=\boldsymbol{F}(\boldsymbol{x}_{0},\boldsymbol{y}_{0}),\forall\boldsymbol{x}\in V.$
(2) $J\psi (\pmb {x}) = -\left(J_{\pmb{y}}\pmb {F}(\pmb {x},\psi (\pmb {x}))\right)^{-1}J_{\pmb{x}}\pmb {F}(\pmb {x},\psi (\pmb {x}))$ ，其中 $J_{\pmb{x}}\pmb {F}(\pmb {x},\pmb {y}) = \left(\frac{\partial F_i}{\partial x_j} (\pmb {x},\pmb {y})\right)_{m\times n}$

类似于隐函数存在定理, 隐映射定理同样也有  $C^{k}$  版本,  $k = 1, 2, \cdots, \infty$ . 即, 如果  $\boldsymbol{F}(\boldsymbol{x}, \boldsymbol{y}) \in C^{k}$ , 则定理中的映射  $\psi: V \to R^{m}$  也是  $C^{k}$  的.

隐映射定理的证明有多种方法, 常见的有: 对空间维数 $m$ 用数学归纳法, 讨论函数 $\| \boldsymbol{F} \|$ 的极值法、不动点法, 以及先证明逆映射定理然后应用逆映射定理的方法. 我们采用数学归纳法证明, 其特点是相对而言较为初等和直接.

证明 我们对 $m$ 作归纳证明. 事实上, 整个证明的核心思想将在 $m = 2$ 时充分体现, 所以 $m = 2$ 的证明是最本质的. 至于 $m \geqslant 3$ 的证明则仅仅是形式上的复杂和重复. 因此我们只给出 $m = 2$ 的证明.

注意 $m = 2$ 时, 有 $\pmb{y} = (y_{1}, y_{2})$. 记 $\pmb{y}_{0} = (y_{1}^{0}, y_{2}^{0})$. 由于

$$
\frac {\partial (F _ {1} , F _ {2})}{\partial (y _ {1} , y _ {2})} \bigg | _ {(\boldsymbol {x} _ {0}, \boldsymbol {y} _ {0})} \neq 0.
$$

不妨假设 $\frac{\partial F_2}{\partial y_2} (\pmb{x}_0,\pmb{y}_0)\neq 0.$ 由单个方程的隐函数存在定理知， $\exists \delta_1 > 0$ ，方程

$$
F _ {2} (\boldsymbol {x}, y _ {1}, y _ {2}) = 0
$$

在 $B_{\delta_1}(\pmb{x}_0)\times (y_1^0 -\delta_1,y_1^0 +\delta_1)$ 内唯一确定一个函数

$$
y _ {2} = g (\boldsymbol {x}, y _ {1}),
$$

使得满足

$$
\boldsymbol {F} (\boldsymbol {x}, y _ {1}, g (\boldsymbol {x}, y _ {1})) = 0, \quad y _ {2} ^ {0} = g (\boldsymbol {x} _ {0}, y _ {1} ^ {0})
$$

---

292

第十五章 多元函数微分学及其应用

且 $g(\pmb {x},y_1)$ 在该邻域内具有连续偏导数.将 $y_{2} = g(\pmb {x},y_{1})$ 代入

$$
F _ {1} (\boldsymbol {x}, y _ {1}, y _ {2}) = 0,
$$

得到一个关于 $(\pmb{x},y_{1})$ 的方程

$$
H (\boldsymbol {x}, y _ {1}) = F _ {1} (\boldsymbol {x}, y _ {1}, g (\boldsymbol {x}, y _ {1})) = 0.
$$

由于

$$
\begin{array}{l} \frac {\partial H}{\partial y _ {1}} = \frac {\partial F _ {1}}{\partial y _ {1}} + \frac {\partial F _ {1}}{\partial y _ {2}} \cdot \frac {\partial g (\boldsymbol {x} , y _ {1})}{\partial y _ {1}} = \frac {\partial F _ {1}}{\partial y _ {1}} + \frac {\partial F _ {1}}{\partial y _ {2}} \cdot \left(- \frac {\partial F _ {2}}{\partial y _ {1}} / \frac {\partial F _ {2}}{\partial y _ {2}}\right) \\ = \frac {\partial (F _ {1} , F _ {2})}{\partial (y _ {1} , y _ {2})} \cdot \left(\frac {\partial F _ {2}}{\partial y _ {2}}\right) ^ {- 1}. \\ \end{array}
$$

故有

$$
\frac {\partial H (\boldsymbol {x} _ {0} , y _ {1} ^ {0})}{\partial y _ {1}} = \frac {\partial (F _ {1} , F _ {2})}{\partial (y _ {1} , y _ {2})} \cdot \left(\frac {\partial F _ {2}}{\partial y _ {2}}\right) ^ {- 1} \Bigg | _ {(\boldsymbol {x} _ {0}, \boldsymbol {y} _ {0})} \neq 0.
$$

因此 $\exists \delta_0, 0 < \delta_0 < \delta_1$，使得 $H(\pmb{x}, y_1) = 0$ 在 $B_{\delta_0}(\pmb{x}_0)$ 内唯一确定一个函数 $y_1 = f_1(\pmb{x})$ 满足 $y_1^0 = f_1(\pmb{x}_0)$ 且

$$
F _ {1} \big (\boldsymbol {x}, f _ {1} (\boldsymbol {x}), g \big (\boldsymbol {x}, f _ {1} (\boldsymbol {x}) \big) \big) = 0.
$$

记

$$
y _ {1} = f _ {1} (\boldsymbol {x}), \quad y _ {2} = f _ {2} (\boldsymbol {x}) = g (\boldsymbol {x}, f _ {1} (\boldsymbol {x})),
$$

则在 $B_{\delta_0}(\pmb{x}_0)$ 内，成立

$$
\left\{ \begin{array}{l} F _ {1} \big (\boldsymbol {x}, f _ {1} (\boldsymbol {x}), f _ {2} (\boldsymbol {x}) \big) = 0, \\ F _ {2} \big (\boldsymbol {x}, f _ {1} (\boldsymbol {x}), f _ {2} (\boldsymbol {x}) \big) = 0, \end{array} \right.
$$

且  $\boldsymbol{y}_{0}=(f_{1}(\boldsymbol{x}_{0}),f_{2}(\boldsymbol{x}_{0}))$ . 再由  $\boldsymbol{F}(\boldsymbol{x},\boldsymbol{y})$  具有连续的偏导数, 可得  $f_{1}(\boldsymbol{x}), f_{2}(\boldsymbol{x})$  在  $B_{\delta_{0}}(\boldsymbol{x}_{0})$  内具有连续的偏导数.

利用复合函数求导法则, 可得

$$
\left\{ \begin{array}{l} \frac {\partial F _ {1}}{\partial x _ {i}} + \frac {\partial F _ {1}}{\partial y _ {1}} \frac {\partial f _ {1}}{\partial x _ {i}} + \frac {\partial F _ {1}}{\partial y _ {2}} \frac {\partial f _ {2}}{\partial x _ {i}} = 0, \\ \frac {\partial F _ {2}}{\partial x _ {i}} + \frac {\partial F _ {2}}{\partial y _ {1}} \frac {\partial f _ {1}}{\partial x _ {i}} + \frac {\partial F _ {2}}{\partial y _ {2}} \frac {\partial f _ {2}}{\partial x _ {i}} = 0, \end{array} \right.
$$

写成向量形式, 有

$$
\left. \left( \begin{array}{c c c c} \frac {\partial f _ {1}}{\partial x _ {1}} & \frac {\partial f _ {1}}{\partial x _ {2}} & \dots & \frac {\partial f _ {1}}{\partial x _ {n}} \\ \frac {\partial f _ {2}}{\partial x _ {1}} & \frac {\partial f _ {2}}{\partial x _ {2}} & \dots & \frac {\partial f _ {2}}{\partial x _ {n}} \end{array} \right) \right| _ {\boldsymbol {x}} = - \left. \left( \begin{array}{c c} \frac {\partial F _ {1}}{\partial y _ {1}} & \frac {\partial F _ {1}}{\partial y _ {2}} \\ \frac {\partial F _ {2}}{\partial y _ {1}} & \frac {\partial F _ {2}}{\partial y _ {2}} \end{array} \right) ^ {- 1} \right| _ {(\boldsymbol {x}, \boldsymbol {y})} \left. \left( \begin{array}{c c c c} \frac {\partial F _ {1}}{\partial x _ {1}} & \frac {\partial F _ {1}}{\partial x _ {2}} & \dots & \frac {\partial F _ {1}}{\partial x _ {n}} \\ \frac {\partial F _ {2}}{\partial x _ {1}} & \frac {\partial F _ {2}}{\partial x _ {2}} & \dots & \frac {\partial F _ {2}}{\partial x _ {n}} \end{array} \right) \right| _ {\boldsymbol {x}}
$$

---

15.6 隐函数存在定理

293

下面证明隐函数解的唯一性. 假设不然, 由 $F(x, y) = 0$ 在 $B_{\delta_0}(x_0)$ 内还有另外一组方程

$$
y _ {1} = \tilde {f} _ {1} (\boldsymbol {x}), \quad y _ {2} = \tilde {f} _ {2} (\boldsymbol {x})
$$

也满足定理要求和结论, 则有 $f_{i}$ 和 $\tilde{f}_{i} (i = 1,2)$ 有相同的偏导数. 从而它们的差 $f_{i} - \tilde{f}_{i}$ 必为常数, 易知此常数必为零. 因此可得 $f_{i} = \tilde{f}_{i}$. □

例 15.6.3 设  $x^{2} + 2y^{2} + 3z^{2} + xy - z - 9 = 0$ ，求 x = 1, y = -2, z = 1 时  $\frac{\partial z}{\partial x}$ ,  $\frac{\partial z}{\partial y}$ ,  $\frac{\partial^{2}z}{\partial y\partial x}$  的值.

解 令 $F(x,y,z) = x^{2} + 2y^{2} + 3z^{2} + xy - z - 9,$ 则

$$
F (1, - 2, 1) = 0, \quad F _ {z} (1, - 2, 1) = (6 z - 1) | _ {z = 1} = 5 \neq 0,
$$

故 $z$ 可局部地表示为 $x, y$ 的函数, 记为 $z = z(x, y)$. 由隐映射定理, 在 $(1, -2, 1)$ 处, 有

$$
\begin{array}{l} (z _ {x}, z _ {y}) = - F _ {z} ^ {- 1} \cdot (F _ {x}, F _ {y}) \\ = - \left. \frac {1}{5} (2 x + y, 4 y + x) \right| _ {(x, y, z) = (1, - 2, 1)} = \left(0, \frac {7}{5}\right). \\ \end{array}
$$

又因为

$$
z _ {y} = - F _ {z} ^ {- 1} \cdot F _ {y} = - \frac {1}{6 z - 1} (4 y + x),
$$

所以

$$
\frac {\partial^ {2} z}{\partial y \partial x} = \frac {6}{(6 z - 1) ^ {2}} \cdot z _ {x} (4 y + x) - \frac {1}{6 z - 1},
$$

从而 $\frac{\partial^2z}{\partial y\partial x} (1, - 2,1) = -\frac{1}{5}.$

## 3. 逆映射定理

回忆一下:对于一元函数，如果它可微且导数处处非零，则该函数可逆且其逆仍可微。下面我们考虑多元向量值函数类似的问题。

例 15.6.4 设 A 为 n 阶方阵, 如果  $\|A\| < 1$ , 则  $I_{n} - A$  可逆.

事实上, 设  $u \in R^{n}$ , 如果  $(I_{n} - A)u = 0$ , 则  $\|u\| = \|Au\| \leqslant \|A\|\cdot\|u\|$ , 由  $\|A\| < 1$  可知 u = 0. 根据线性代数可知  $I_{n} - A$  可逆.

我们也可从分析学观点来看. 给定  $v \in R^{n}$ ，我们解方程

$$
(I _ {n} - A) \pmb {x} = \pmb {v}, \text {即} \pmb {x} = A \pmb {x} + \pmb {v}.
$$

考虑映射 $\varphi (\pmb {x}) = \pmb {A}\pmb {x} + \pmb{v}$ ，当 $x,y\in \mathbb{R}^n$ 时

$$
\| \varphi (\boldsymbol {x}) - \varphi (\boldsymbol {y}) \| = \| \boldsymbol {A} (\boldsymbol {x} - \boldsymbol {y}) \| \leqslant \| \boldsymbol {A} \| \cdot \| \boldsymbol {x} - \boldsymbol {y} \|,
$$

---

294

第十五章 多元函数微分学及其应用

这说明 $\varphi$ 是 $\mathbb{R}^n$ 到自身的压缩映射. 根据压缩映射原理, $\varphi$ 有唯一的不动点, 即 $I_{n} - A$ 可逆.

这个例子意味着, 恒同映射这样一个可逆映射作一个小的扰动以后仍然为可逆映射. 一般地, 任何可逆线性映射在微扰下仍为可逆映射. 对于向量值函数来说, 要知道它在某一点附近是否可逆, 只要在这一点将它线性化, 看看其微分是否可逆. 这里我们需要对函数加一定的可微性条件. 回顾一下, 一个向量值函数称为 $C^k$ 的是指它的每一个分量都是 $C^k$ 函数. 下面的重要结果也称为向量值函数的反函数定理.

定理 15.6.3 (逆映射定理) 设 $D \subseteq \mathbb{R}^n$ 为开集, $f: D \to \mathbb{R}^n$ 为 $C^k (k \geqslant 1)$ 映射, $x_0 \in D$. 如果 $\det J f(x_0) \neq 0$, 则存在 $x_0$ 的开邻域 $U \subseteq D$ 以及 $y_0 = f(x_0)$ 的开邻域 $V \subseteq \mathbb{R}^n$, 使得 $f|_{U}: U \to V$ 是可逆映射, 且其逆映射 $h: V \to U$, $h(y) = x$ 也是 $C^k$ 的, 并且满足

$$
J \boldsymbol {h} (\boldsymbol {y}) = \left(J \boldsymbol {f} (\boldsymbol {h} (\boldsymbol {y}))\right) ^ {- 1}, \forall \boldsymbol {y} \in V.
$$

证明 不失一般性, 可设 $x_0 = 0, y_0 = 0$. 以 $L$ 记 $\pmb{f}$ 在 $x_0 = 0$ 处的微分, 则 $L$ 可逆, 且 $L^{-1} \circ \pmb{f}$ 在 $x_0$ 处的微分为恒同映射. 如果欲证结论对 $L^{-1} \circ \pmb{f}$ 成立, 则对 $\pmb{f}$ 也成立. 因此, 不妨从一开始就假设 $J\pmb{f}(\pmb{x}_0) = \pmb{I}_n$.

在 $x_0 = 0$ 附近, $\pmb{f}$ 是恒同映射的小扰动:

$$
\boldsymbol {f} (\boldsymbol {x}) = \boldsymbol {x} + \boldsymbol {g} (\boldsymbol {x}), \quad J \boldsymbol {g} (\boldsymbol {0}) = \boldsymbol {0}.
$$

扰动项 $g(x) = f(x) - x$ 为 $C^k$ 映射. 因此, 存在 $\delta > 0$ 使得

$$
\| J \boldsymbol {g} (\boldsymbol {x}) \| \leqslant \frac {1}{2}, \forall \boldsymbol {x} \in \overline {{B _ {\delta} (\boldsymbol {0})}} \subseteq D.
$$

由拟微分中值定理可知

$$
\| \boldsymbol {g} (\boldsymbol {x} _ {1}) - \boldsymbol {g} (\boldsymbol {x} _ {2}) \| \leqslant \frac {1}{2} \| \boldsymbol {x} _ {1} - \boldsymbol {x} _ {2} \|, \forall \boldsymbol {x} _ {1}, \boldsymbol {x} _ {2} \in \overline {{B _ {\delta} (\mathbf {0})}}.
$$

给定 $\pmb{y} \in B_{\delta / 2}(\mathbf{0})$ ，我们在 $B_{\delta}(\mathbf{0})$ 中解方程

$$
\pmb {f} (\pmb {x}) = \pmb {y}, \text {即} \pmb {x} = \pmb {y} - \pmb {g} (\pmb {x}). \tag {15.6.8}
$$

记 $\varphi (\pmb {x}) = \pmb {y} - \pmb {g}(\pmb {x})$ .当 $\pmb {x}\in \overline{B_{\delta}(\mathbf{0})}$ 时

$$
\| \varphi (\boldsymbol {x}) \| \leqslant \| \boldsymbol {y} \| + \| \boldsymbol {g} (\boldsymbol {x}) \| <   \frac {\delta}{2} + \frac {1}{2} \| \boldsymbol {x} \| \leqslant \delta . \tag {15.6.9}
$$

这说明 $\varphi (\overline{B_{\delta}(\mathbf{0})})\subset B_{\delta}(\mathbf{0})$ .当 $x_{1},x_{2}\in \overline{B_{\delta}(\mathbf{0})}$ 时

$$
\| \varphi (\boldsymbol {x} _ {1}) - \varphi (\boldsymbol {x} _ {2}) \| = \| \boldsymbol {g} (\boldsymbol {x} _ {2}) - \boldsymbol {g} (\boldsymbol {x} _ {1}) \| \leqslant \frac {1}{2} \| \boldsymbol {x} _ {1} - \boldsymbol {x} _ {2} \|\cdot
$$

根据压缩映射原理, 方程 (15.6.8) 在 $\overline{B_{\delta}(\mathbf{0})}$ 中有唯一解, 记为 $x_{y}$. 由 (15.6.9) 式可知 $x_{y} \in B_{\delta}(\mathbf{0})$. 令

$$
U = \boldsymbol {f} ^ {- 1} \big (B _ {\delta / 2} (\boldsymbol {0}) \big) \cap B _ {\delta} (\boldsymbol {0}), V = B _ {\delta / 2} (\boldsymbol {0}),
$$

---

15.6 隐函数存在定理

295

则我们已经证明了  $f|_{U}: U \rightarrow V$  是一一映射, 其逆映射  $h(y) = x_{y}$  满足

$$
\boldsymbol {y} - \boldsymbol {g} (\boldsymbol {h} (\boldsymbol {y})) = \boldsymbol {h} (\boldsymbol {y}). \tag {15.6.10}
$$

(1) $h:V\to U$ 是连续映射: 当 $y_{1},y_{2}\in V$ 时

$$
\begin{array}{l} \| \boldsymbol {h} (\boldsymbol {y} _ {1}) - \boldsymbol {h} (\boldsymbol {y} _ {2}) \| \leqslant \| \boldsymbol {y} _ {1} - \boldsymbol {y} _ {2} \| + \| \boldsymbol {g} (\boldsymbol {h} (\boldsymbol {y} _ {1})) - \boldsymbol {g} (\boldsymbol {h} (\boldsymbol {y} _ {2})) \| \\ \leqslant \| \boldsymbol {y} _ {1} - \boldsymbol {y} _ {2} \| + \frac {1}{2} \| \boldsymbol {h} (\boldsymbol {y} _ {1}) - \boldsymbol {h} (\boldsymbol {y} _ {2}) \|, \\ \end{array}
$$

这说明 $\| \pmb {h}(\pmb{y}_1) - \pmb {h}(\pmb{y}_2)\| \leqslant 2\| \pmb {y}_1 - \pmb {y}_2\|$, $\forall \pmb{y}_1, \pmb{y}_2 \in V$.

(2) $h:V\to U$ 是可微映射: 设 $y_{0}\in V$, 则对 $y\in V$, 有

$$
\begin{array}{l} \boldsymbol {h} (\boldsymbol {y}) - \boldsymbol {h} \left(\boldsymbol {y} _ {0}\right) = \left(\boldsymbol {y} - \boldsymbol {y} _ {0}\right) - \left(\boldsymbol {g} \left(\boldsymbol {h} (\boldsymbol {y})\right) - \boldsymbol {g} \left(\boldsymbol {h} \left(\boldsymbol {y} _ {0}\right)\right)\right) \\ = (\boldsymbol {y} - \boldsymbol {y} _ {0}) - J \boldsymbol {g} (\boldsymbol {h} (\boldsymbol {y} _ {0})) \cdot (\boldsymbol {h} (\boldsymbol {y}) - \boldsymbol {h} (\boldsymbol {y} _ {0})) + o \left(\| \boldsymbol {h} (\boldsymbol {y}) - \boldsymbol {h} (\boldsymbol {y} _ {0}) \|\right). \\ \end{array}
$$

利用 $Jf = I_n + Jg$ 和(1)，上式可改写为

$$
J \boldsymbol {f} (\boldsymbol {h} (\boldsymbol {y} _ {0})) \cdot (\boldsymbol {h} (\boldsymbol {y}) - \boldsymbol {h} (\boldsymbol {y} _ {0})) = (\boldsymbol {y} - \boldsymbol {y} _ {0}) + o \big (\| \boldsymbol {y} - \boldsymbol {y} _ {0} \| \big),
$$

因而

$$
\boldsymbol {h} (\boldsymbol {y}) - \boldsymbol {h} (\boldsymbol {y} _ {0}) = \left[ J \boldsymbol {f} (\boldsymbol {h} (\boldsymbol {y} _ {0})) \right] ^ {- 1} \cdot (\boldsymbol {y} - \boldsymbol {y} _ {0}) + o \big (\| \boldsymbol {y} - \boldsymbol {y} _ {0} \| \big).
$$

这说明 h 在  $y_{0}$  处可微.

(3) $h:V\to U$ 为 $C^{k}$ 映射:由(2)可知

$$
J \boldsymbol {h} (\boldsymbol {y}) = \left(J \boldsymbol {f} (\boldsymbol {h} (\boldsymbol {y}))\right) ^ {- 1}, \forall \boldsymbol {y} \in V. \tag {15.6.11}
$$

由  $f \in C^{k}$  知  $Jf \in C^{k-1}$ . 由 (2) 及 (15.6.11) 式可推出 Jh 连续, 即  $h \in C^{1}$ . 再由  $Jf \in C^{k-1}, h \in C^{1}$  及 (15.6.11) 式可推出  $Jh \in C^{1}$  即  $h \in C^{2}$ . 以此类推, 最后我们就得到  $h \in C^{k}$ . □

需要特别强调的是逆映射定理一般来说仅有局部性, 也就是说, 只是在点 $f(x_0)$ 附近才存在逆映射. 换句话说, 即使 $\det J f$ 在 $D$ 上处处非零, 我们也只能断言在 $f(D)$ 中的每一个点的一个局部范围内存在逆映射, 一般不能保证在大范围内成为 $f$ 在 $f(D)$ 上的逆映射, 这与一元函数不同.

例 15.6.5 研究  $f: R^{2} \rightarrow R^{2}$ ,  $f(x, y) = (\mathrm{e}^{x} \cos y, \mathrm{e}^{x} \sin y)$  的逆映射.

解 注意到

$$
\det J \boldsymbol {f} (x, y) = \left| \begin{array}{c c} \mathrm{e} ^ {x} \cos y & - \mathrm{e} ^ {x} \sin y \\ \mathrm{e} ^ {x} \sin y & \mathrm{e} ^ {x} \cos y \end{array} \right| = \mathrm{e} ^ {2 x} \neq 0,
$$

这说明 f 局部可逆. 但 f 不是单射, 因此整体不可逆.

另一方面, 当映射的 Jacobi 矩阵退化时, 映射本身也可能可逆.

---

296

第十五章 多元函数微分学及其应用

例 15.6.6 研究  $f: R^{2} \rightarrow R^{2}$ ,  $f(x, y) = (x^{3}, y^{3})$  的逆映射.

解 显然, $f$ 为光滑映射, 它也是可逆映射. 注意到 $f$ 的逆映射在 $(0,0)$ 处不可微, 这是由 $Jf$ 在 $(0,0)$ 处的退化性所造成的. □

例 15.6.7 设  $f: R^{2} \rightarrow R$  为  $C^{k}(k \geqslant 1)$  函数,  $\frac{\partial f}{\partial y}(x_{0}, y_{0}) \neq 0$ , 在  $(x_{0}, y_{0})$  附近解方程  $f(x, y) = f(x_{0}, y_{0})$ .

解 显然, $(x_0, y_0)$ 是方程的解. 利用逆映射定理, 我们可以在 $(x_0, y_0)$ 附近找到别的解. 为此, 令

$$
\boldsymbol {F}: \mathbb {R} ^ {2} \to \mathbb {R} ^ {2}, \quad \boldsymbol {F} (x, y) = (x, f (x, y)).
$$

在 $(x_{0},y_{0})$ 处,有

$$
\det J \boldsymbol {F} (x _ {0}, y _ {0}) = \left| \begin{array}{c c} 1 & 0 \\ \frac {\partial f}{\partial x} & \frac {\partial f}{\partial y} \end{array} \right| _ {(x _ {0}, y _ {0})} = \frac {\partial f}{\partial y} (x _ {0}, y _ {0}) \neq 0.
$$

由逆映射定理, 在  $(x_{0}, y_{0})$  附近 F 为可逆映射. 于是当 x 在  $x_{0}$  附近时, 记

$$
\boldsymbol {F} ^ {- 1} \big (x, f (x _ {0}, y _ {0}) \big) = \big (\varphi (x), \psi (x) \big),
$$

$\varphi (x),\psi (x)$ 均为 $C^k$ 函数.根据 $\pmb{F}$ 的定义可得

$$
\big (\varphi (x), f (\varphi (x), \psi (x)) \big) = \big (x, f (x _ {0}, y _ {0}) \big),
$$

这说明 $\varphi (x) = x, f(x,\psi (x)) = f(x_0,y_0)$. 对 $x$ 求导还可得到

$$
\frac {\partial f}{\partial x} (x, \psi (x)) + \frac {\partial f}{\partial y} (x, \psi (x)) \cdot \psi^ {\prime} (x) = 0,
$$

从而有

$$
\psi^ {\prime} (x) = - \left(\frac {\partial f}{\partial y} (x, \psi (x))\right) ^ {- 1} \frac {\partial f}{\partial x} (x, \psi (x)).
$$

$y = \psi (x)$ 是由 $f(x,y) = f(x_0,y_0)$ 所决定的隐函数.

关于大范围内逆映射的存在性问题, 我们简单介绍以下一个全局结论. 首先我们给出正则映射的定义.

定义 15.6.1 设开集 $D \subseteq \mathbb{R}^n$, 如果映射 $f: D \to \mathbb{R}^n$ 满足

(1) $f \in C^{1}(D).$
(2) f 是 D 上的单射.
(3)  $\forall x \in D, \det Jf(x) \neq 0,$

则称 f 是 D 上的一个正则映射.

下面的定理表明,正则映射的逆映射也是正则映射.

---

15.6 隐函数存在定理

297

定理 15.6.4 设开集 $D \subseteq \mathbb{R}^n$, 如果映射 $f: D \to \mathbb{R}^n$ 是 $D$ 上的一个正则映射, 则 $\Omega = f(D)$ 是一开集, 且存在由 $\Omega$ 到 $D$ 上的映射 $f^{-1}$ 满足: 对一切 $y \in \Omega$, 有

$$
\boldsymbol {f} \circ \boldsymbol {f} ^ {- 1} (\boldsymbol {y}) = \boldsymbol {y},
$$

并且  $f^{-1} \in C^{1}(\Omega)$ ,

$$
J \boldsymbol {f} ^ {- 1} (\boldsymbol {y}) = \left(J \boldsymbol {f} (\boldsymbol {x})\right) ^ {- 1}, \tag {15.6.12}
$$

其中  $\boldsymbol{x}=\boldsymbol{f}^{-1}(\boldsymbol{y})$ .

证明 由于 f 是单射, 故逆映射  $f^{-1}$  存在, 即下式成立:

$$
\boldsymbol {f} \circ \boldsymbol {f} ^ {- 1} (\boldsymbol {y}) = \boldsymbol {y}.
$$

因为逆映射定理保证了局部逆映射的存在唯一性, 而整体逆映射必然是局部逆映射, 所以 $\pmb{f}^{-1} \in C^{1}(\Omega)$ 和 (15.6.12) 式也都必然成立. 为了证明 $\pmb{f}(D)$ 是开集, 任取 $\pmb{y} \in \Omega$, 存在 $\pmb{x} \in D$ 使得 $\pmb{y} = \pmb{f}(\pmb{x})$, 由定理 15.6.3, 存在 $\pmb{x}$ 的邻域 $U$ 和 $\pmb{y}$ 的邻域 $V$ 满足 $V = \pmb{f}(U)$, 因此 $V = \pmb{f}(U) \subseteq \pmb{f}(D) = \Omega$, 因此 $\pmb{y}$ 是 $\Omega$ 的内点. 由 $\pmb{y}$ 的任意性, 知 $\Omega$ 是开的.

把关系式 (15.6.12) 写成熟悉的矩阵形式, 则有

$$
\left( \begin{array}{c c c} \frac {\partial x _ {1}}{\partial y _ {1}} & \dots & \frac {\partial x _ {1}}{\partial y _ {n}} \\ \vdots & & \vdots \\ \frac {\partial x _ {n}}{\partial y _ {1}} & \dots & \frac {\partial x _ {n}}{\partial y _ {n}} \end{array} \right) = \left( \begin{array}{c c c} \frac {\partial y _ {1}}{\partial x _ {1}} & \dots & \frac {\partial y _ {1}}{\partial x _ {n}} \\ \vdots & & \vdots \\ \frac {\partial y _ {n}}{\partial x _ {1}} & \dots & \frac {\partial y _ {n}}{\partial x _ {n}} \end{array} \right) ^ {- 1}. \tag {15.6.13}
$$

回忆一下前面关于 Jacobi 行列式的记号:

$$
\frac {\partial (y _ {1} , \cdots , y _ {n})}{\partial (x _ {1} , \cdots , x _ {n})} = \det \left( \begin{array}{c c c} \frac {\partial y _ {1}}{\partial x _ {1}} & \dots & \frac {\partial y _ {1}}{\partial x _ {n}} \\ \vdots & & \vdots \\ \frac {\partial y _ {n}}{\partial x _ {1}} & \dots & \frac {\partial y _ {n}}{\partial x _ {n}} \end{array} \right),
$$

我们在 (15.6.13) 式两端取行列式, 可得

$$
\frac {\partial (y _ {1} , \cdots , y _ {n})}{\partial (x _ {1} , \cdots , x _ {n})} = \left(\frac {\partial (x _ {1} , \cdots , x _ {n})}{\partial (y _ {1} , \cdots , y _ {n})}\right) ^ {- 1}. \tag {15.6.14}
$$

例 15.6.8 设  $u=\frac{y^{2}}{x}$ ,  $v=\frac{x^{2}}{y}$ . 试计算  $\frac{\partial(x,y)}{\partial(u,v)}$ .

解 由方程组可以直接计算得到 $\frac{\partial(u,v)}{\partial(x,y)} = \left| \begin{array}{cc}u_x & u_y\\ v_x & v_y \end{array} \right| = -3.$ 根据公式(15.6.14) 可得 $\frac{\partial(x,y)}{\partial(u,v)} = -\frac{1}{3}.$ □

---

298

第十五章 多元函数微分学及其应用

当然, 这是一道可以直接计算的题目, 读者可以通过直接计算和利用公式两种做法来对比一下结果. 进一步, 读者可从上面的讨论中体会一下逆映射的内容与反函数相应内容之间的一般与特殊的关系.

逆映射定理在分析学和其他专业方向上有着深刻的影响和广泛的应用. 我们仅举一些变量替换方面的例子来体会一下它在简化偏微分方程方面的威力.

例15.6.9 设函数 $u = u(t,x)\in C^2$ ，试作变量替换

$$
\xi = x - a t, \quad \eta = x + a t.
$$

将波动方程 $u_{tt} = a^2 u_{xx}$ $(a\neq 0)$ 转化成 $u$ 关于 $\xi ,\eta$ 所满足的方程.

解 直接计算得

$$
\frac {\partial (\xi , \eta)}{\partial (t , x)} = \det \left( \begin{array}{c c} - a & 1 \\ a & 1 \end{array} \right) = - 2 a \neq 0.
$$

从而变量替换是可逆的 (逆映射存在). 易知

$$
\left\{ \begin{array}{l} u _ {x} = u _ {\xi} \xi_ {x} + u _ {\eta} \eta_ {x} = u _ {\xi} + u _ {\eta}, \\ u _ {t} = u _ {\xi} \xi_ {t} + u _ {\eta} \eta_ {t} = a (u _ {\eta} - u _ {\xi}), \end{array} \right.
$$

以及

$$
\left\{ \begin{array}{l} u _ {x x} = u _ {\xi \xi} + u _ {\eta \eta} + 2 u _ {\xi \eta}, \\ u _ {t t} = a ^ {2} (u _ {\xi \xi} + u _ {\eta \eta}) - 2 a ^ {2} u _ {\xi \eta}. \end{array} \right.
$$

因此由 $u_{tt} = a^2 u_{xx}$ 得到 $u_{\xi \eta} = 0$ .后者很容易求得通解:

$$
u (\xi , \eta) = \varphi (\xi) + \psi (\eta),
$$

其中 $\varphi, \psi \in C^2$. 故波动方程 $u_{tt} = a^2 u_{xx}, u \in C^2$, 的通解为

$$
u (t, x) = \varphi (x - a t) + \eta (x + a t).
$$

例15.6.10 假设二元函数 $z = z(x,y)\in C^2$ 且满足二阶偏微分方程

$$
z _ {x x} + 2 z _ {x y} + z _ {y y} = 0.
$$

试通过变量替换

$$
u = x + y, \quad v = x - y,
$$

来计算 w := xy - z 关于 u, v 所满足的微分方程.

解 直接计算可得

$$
\frac {\partial (u , v)}{\partial (x , y)} = \det \left( \begin{array}{c c} 1 & 1 \\ 1 & - 1 \end{array} \right) = - 2.
$$

---

15.6 隐函数存在定理

299

从而变量替换是可逆的, 根据

$$
\left\{ \begin{array}{l} z _ {x} = y - w _ {x} = y - (w _ {u} + w _ {v}), \\ z _ {y} = x - w _ {y} = x - (w _ {u} - w _ {v}) \end{array} \right.
$$

和

$$
\left\{ \begin{array}{l} z _ {x x} = - (w _ {u u} + 2 w _ {u v} + w _ {v v}), \\ z _ {x y} = 1 - (w _ {u u} - w _ {v v}), \\ z _ {y y} = - (w _ {u u} - 2 w _ {u v} + w _ {v v}), \end{array} \right.
$$

可得 $w_{uu} = \frac{1}{2}$

![](../../raw/pages_0593-0608/images/page_603_image_7.jpg)

## 习题 15.6

1. 研究下列函数在指定点的邻域内是否可以将 $y$ 解为 $x$ 的函数:

(1) $f(x,y) = x^{2} - y^{2},\quad (x,y) = (0,0).$
(2)  $f(x,y) = \sin(\pi(x+y)) - 1, \quad (x,y) = (1/4,1/4).$
(3) $f(x,y) = xy + \ln (xy) - 1, \quad (x,y) = (1,1)$.
(4) $f(x,y) = x^{5} + y^{5} + xy - 3, (x,y) = (1,1)$.

2. 计算指定点处的偏导数:

(1) $y^{z} - xz^{3} - 1 = 0, \quad \frac{\partial z}{\partial y}(1,2,1).$
(2) $x^{2} + 2y^{2} + 3z^{2} + xy - z = 9,\quad \frac{\partial^{2}z}{\partial x^{2}} (1, - 2,1).$

3. 方程组

$$
x v - 4 y + 2 \mathrm{e} ^ {u} + 3 = 0, \quad 2 x - z - 6 u + v \cos u = 0
$$

在点 $x = -1, y = 1, z = -1, u = 0, v = 1$ 处确定了隐函数 $u = u(x, y, z), v = v(x, y, z)$. 求 $u, v$ 在该点处的 Jacobi 矩阵.

4. 设 $U, V$ 为 $\mathbb{R}^n$ 中的开集, $\pmb{f}: U \to V$ 为可微映射, 且 $\det J\pmb{f}(\pmb{x}) \neq 0, \forall \pmb{x} \in U$. 如果 $\pmb{f}$ 的逆映射存在且连续, 证明: 其逆映射一定也是可微的.

5. 设 $f: \mathbb{R}^n \to \mathbb{R}^n$ 为连续可微的映射, 且

$$
\| \boldsymbol {f} (\boldsymbol {x}) - \boldsymbol {f} (\boldsymbol {y}) \| \geqslant \| \boldsymbol {x} - \boldsymbol {y} \|, \quad \forall \boldsymbol {x}, \boldsymbol {y} \in \mathbb {R} ^ {n}.
$$

证明: $f$ 可逆, 且其逆映射也是连续可微的.

6. 下列方程确定隐函数  $y(x)$ ，计算  $\frac{\mathrm{d}y}{\mathrm{d}x}$ :

(1) $x^{2} + 2xy - y^{2} = a^{2}$.
(2)  $xy - \ln y = 0,$  在点 (0,1) 处.

---

300

第十五章 多元函数微分学及其应用

(3)  $y - \varepsilon \sin y = x,$  常数  $\varepsilon \in (0,1)$ .

7. 从下列方程中计算  $\frac{\partial z}{\partial x}$  和  $\frac{\partial z}{\partial y}$ :

(1) $\mathrm{e}^z - xyz = 0$.

(2) $\frac{x}{z} = \ln \frac{z}{y}$.

(3) $x + y + z = \mathrm{e}^{-(x + y + z)}$, 并对计算的结果作出解释.

(4) $z^{2}y - xz^{3} - 1 = 0$, 在点 (1,2,1) 处.

8. 设 $x = x(y, z)$, $y = y(x, z)$, $z = z(x, y)$ 都是由 $f(x, y, z) = 0$ 确定的隐函数, 并且都具有连续的偏导数. 求证:

$$
\frac {\partial x}{\partial y} \frac {\partial y}{\partial z} \frac {\partial z}{\partial x} = - 1.
$$

9. 将上题推广到 n 元函数, 探讨有没有相应的结论.

10. 设 $F(x - y, y - z, z - x) = 0$, 计算 $\frac{\partial z}{\partial x}$ 和 $\frac{\partial z}{\partial y}$.

11. 设 $F(x + y + z, x^2 + y^2 + z^2) = 0$, 计算 $\frac{\partial z}{\partial x}$ 和 $\frac{\partial z}{\partial y}$.

12. 二元函数 $F$ 在 $\mathbb{R}^2$ 上二次连续可微. 已知曲线 $F(x, y) = 0$ 是“8”字形. 问方程组

$$
\frac {\partial F}{\partial x} (x, y) = 0, \quad \frac {\partial F}{\partial y} (x, y) = 0
$$

在 $\mathbb{R}^2$ 中至少有几组解？

13. 设 $F(x, y) = 0$ 满足隐函数存在定理的条件，即 $F$ 有一阶连续偏导数，$F(x_0, y_0) = 0$，$F_y(x_0, y_0) \neq 0$. 设 $y = y(x)$ 是由此该方程确定的隐函数，满足 $y(x_0) = y_0$，证明:$x_0$ 是 $y(x)$ 的极值点的必要条件是 $F_x(x_0, y_0) = 0$; 如果 $F_{xx}(x_0, y_0) \neq 0$，则 $x_0$ 一定是 $y(x)$ 的极值点.

具体来说, 如果

$$
- \frac {F _ {x x} (x _ {0} , y _ {0})}{F _ {y} (x _ {0} , y _ {0})} > 0,
$$

则 $x_0$ 是隐函数 $y = y(x)$ 的极小值点；如果

$$
- \frac {F _ {x x} (x _ {0} , y _ {0})}{F _ {y} (x _ {0} , y _ {0})} <   0,
$$

则  $x_{0}$  是隐函数  $y = y(x)$  的极大值点.

---

15.7 Lagrange 乘数法 条件极值

301

## 15.7 Lagrange 乘数法 条件极值

下面我们讨论条件极值问题. 所谓条件极值, 通常是指在目标函数的自变量受到某些约束, 只能在定义域的某一范围内变化. 我们先通过简单的场景来推演一下一般情况的处理方法.

给定平面上的一条曲线 $\Sigma$，设其解析式为 $\varphi(x, y) = 0$，我们暂时假设它的条件足够好，使得讨论得以进行。我们的问题是求给定函数 $z = f(x, y)$ 的极值，其中 $(x, y)$ 不能任意选取，必须受限于 $\Sigma$ 上，即必须满足 $\varphi(x, y) = 0$。

一种自然的处理思路是这样的: 如果 $(x_0, y_0) \in \Sigma$ 且是函数 $z = f(x, y)$ 的极值点, 又假设在 $(x_0, y_0)$ 附近从条件 $\varphi(x, y) = 0$ 中能解出 $y = y(x)$ (或者 $x = x(y)$), 那么将 $y = y(x)$ 代入 $z = f(x, y) = f(x, y(x)) = \tilde{f}(x)$, 则 $x_0$ 应该是函数 $\tilde{f}(x)$ 在通常意义下的极值点, 因而满足极值点处的必要条件

$$
\tilde {f} ^ {\prime} (x _ {0}) = \frac {\partial f}{\partial x} + \frac {\partial f}{\partial y} y ^ {\prime} (x _ {0}) = 0. \tag {15.7.1}
$$

由前面的隐函数存在定理我们知道, 要使得能从隐函数 $\varphi(x,y)=0$ 中确定函数关系 $y=y(x)$ 或者 $x=x(y)$, 除了 $\varphi(x,y)$ 满足一定的光滑性外 (比如 $C^{1}$), 还要假设 $\varphi_{y}(x_{0},y_{0})\neq0$ 或者 $\varphi_{x}(x_{0},y_{0})\neq0$. 由于 $x,y$ 角色的完全对等性, 因此上面两者只要有一个成立即可, 而这等价于条件 $(\varphi_{x},\varphi_{y})\neq0$ 即可. 不妨假设 $\varphi_{y}(x_{0},y_{0})\neq0$. 根据隐函数存在定理, $\exists\delta>0$, 使得在 $(x_{0}-\delta,x_{0}+\delta)$ 内存在 $y=y(x)$, 满足 $y_{0}=y(x_{0})$, $\varphi(x,y(x))\equiv0$, 且 $y'(x_{0})=-\frac{\varphi_{x}(x_{0},y_{0})}{\varphi_{y}(x_{0},y_{0})}$.

我们继续上面的分析, 又由 (15.7.1) 式, 知 $y'(x_0) = -\frac{f_x(x_0, y_0)}{f_y(x_0, y_0)}$. 这样一来, 我们得到如下关系式:

$$
\frac {f _ {x} (x _ {0} , y _ {0})}{\varphi_ {x} (x _ {0} , y _ {0})} = \frac {f _ {y} (x _ {0} , y _ {0})}{\varphi_ {y} (x _ {0} , y _ {0})} \quad \Longleftrightarrow \quad \left| \begin{array}{c c} f _ {x} (x _ {0}, y _ {0}) & f _ {y} (x _ {0}, y _ {0}) \\ \varphi_ {x} (x _ {0}, y _ {0}) & \varphi_ {y} (x _ {0}, y _ {0}) \end{array} \right| = 0.
$$

故 $\operatorname{grad} f(x_0, y_0)$ 与 $\operatorname{grad} \varphi(x_0, y_0)$ 线性相关, 即存在 $-\lambda \in \mathbb{R}$, 使得

$$
\mathrm{grad} f (x _ {0}, y _ {0}) = - \lambda \mathrm{grad} \varphi (x _ {0}, y _ {0}).
$$

将其改写为

$$
\left\{ \begin{array}{l} f _ {x} (x _ {0}, y _ {0}) + \lambda \varphi_ {x} (x _ {0}, y _ {0}) = 0, \\ f _ {y} (x _ {0}, y _ {0}) + \lambda \varphi_ {y} (x _ {0}, y _ {0}) = 0. \end{array} \right. \tag {15.7.2}
$$

注意, $(x_{0},y_{0})$ 同时还需要满足 $\varphi(x_{0},y_{0})=0$ .

---

302

第十五章 多元函数微分学及其应用

上述场景有明确的几何意义: 如图 15.9. 从几何上看, 就是在曲线 $\Sigma: \varphi(x, y) = 0$ 上求曲面 $z = f(x, y)$ 的最高点或者最低点. 考虑由曲面定义出的等高线族 $f(x, y) = c$ 与曲线 $\Sigma: \varphi(x, y) = 0$ 的交点, 我们需要寻找的就是使得 $c$ 成为最大或最小的那条等高线. 由于一般来说, 等高线的分布依单参数 $c$ 单调变化, 几何上看, 只有与曲线 $\Sigma$ 相切的那条等高线才有可能是最值曲线. 设切点为 $(x_0, y_0)$, 则切点才有可能是约束条件下函数 $f(x, y)$ 的最值点. 另一方面, 切点的寻求可以考虑两条曲线的法向量, 并令两者成比例得到:

$$
\begin{array}{l} \boldsymbol {n} _ {\varphi} = (\varphi_ {x} (x _ {0}, y _ {0}), \varphi_ {y} (x _ {0}, y _ {0})), \\ \boldsymbol {n} _ {f} = (f _ {x} (x _ {0}, y _ {0}), f _ {y} (x _ {0}, y _ {0})). \\ \end{array}
$$

即

$$
\frac {f _ {x} (x _ {0} , y _ {0})}{\varphi_ {x} (x _ {0} , y _ {0})} = \frac {f _ {y} (x _ {0} , y _ {0})}{\varphi_ {y} (x _ {0} , y _ {0})} = - \lambda .
$$

这就是前面的式子(15.7.2)几何上的解释.

![](../../raw/pages_0593-0608/images/page_606_image_7.jpg)

<details>
<summary>text_image</summary>

Σ: φ(x,y) = 0
(c₀, y₀)
c₄
c₃
c₂
c₁
f(x,y) = c
</details>

图15.9 条件极值

我们将上述场景一般化, 可以考虑如下场景下的条件极值问题:

设 $U \subseteq \mathbb{R}^n$ 为开集, $f: U \to \mathbb{R}$ 为可微函数, $\Phi: U \to \mathbb{R}^m (n > m)$ 为 $C^k (k \geqslant 1)$ 映射. 记

$$
\Sigma = \boldsymbol {\Phi} ^ {- 1} (\mathbf {0}) = \{\boldsymbol {x} \in U   |   \boldsymbol {\Phi} (\boldsymbol {x}) = \mathbf {0} \}, \qquad \boldsymbol {\Phi} = (\varphi_ {1}, \dots , \varphi_ {m}).
$$

$f$ 在 $\Sigma$ 上的极值称为条件极值, 方程 $\Phi(x) = 0$ 称为约束条件.

如果对任意  $x \in \Sigma$ ，矩阵  $J\Phi(x)$  的秩均为 m，则称  $\Sigma$  上的点满足 m 个独立的约束条件。此时，利用隐函数存在定理可知  $\Sigma$  为  $R^{n}$  中 n - m 维曲面，且  $\Sigma$  在 x 处的法空间由  $\{\nabla\varphi_{1}(x), \cdots, \nabla\varphi_{m}(x)\}$  张成（必要时，可参考下节多元微分学在几何上的应用），其中  $\varphi_{i}$  是  $\Phi$  的第 i 个分量。如果  $x_{0} \in \Sigma$  为 f 的极值点，则  $\nabla f(x_{0})$  必为  $\Sigma$  在  $x_{0}$  处的法向量。事实上，设  $\gamma(t)$  是  $\Sigma$  上的可微参数曲线， $\gamma(0) = x_{0}$ 。则  $t = t_{0}$  是  $f \circ \gamma(t)$  的极值点，从而是驻点。由 Fermat 引理，成立

$$
\begin{array}{l} \left(f \circ \gamma\right) ^ {\prime} (t _ {0}) = \frac {\mathrm{d}}{\mathrm{d} t} f \Big (x _ {1} (t), \dots , x _ {n} (t) \Big) \Big | _ {t = t _ {0}} \\ = f _ {x _ {1}} (\boldsymbol {x} _ {0}) x _ {1} ^ {\prime} (t _ {0}) + \dots + f _ {x _ {n}} (\boldsymbol {x} _ {0}) x _ {n} ^ {\prime} (t _ {0}) = \nabla f (\boldsymbol {x} _ {0}) \cdot \boldsymbol {\gamma} ^ {\prime} (t _ {0}) = 0. \\ \end{array}
$$

---

15.7 Lagrange 乘数法 条件极值

303

注意到  $\gamma'(t_{0})$  为  $\Sigma$  在  $x_{0}$  处的切向量. 由  $\gamma$  的任意性即知  $\nabla f(x_{0})$  为  $\Sigma$  在  $x_{0}$  处的法向量. 因此, 存在  $\lambda_{1}, \cdots, \lambda_{m} \in R$ , 使得

$$
\nabla f (\boldsymbol {x} _ {0}) = \sum_ {i = 1} ^ {m} \lambda_ {i} \nabla \varphi_ {i} (\boldsymbol {x} _ {0}). \tag {15.7.3}
$$

称  $\boldsymbol{\lambda}=(\lambda_{1},\cdots,\lambda_{m})$  为 Lagrange 乘数.

定理 15.7.1 (Lagrange 乘数法) 设 $f, \Phi$ 如上, $x_0 \in \Sigma$ 为 $f$ 的条件极值点. 如果 $J\Phi(x_0)$ 的秩为 $m$, 则存在 $\lambda = (\lambda_1, \cdots, \lambda_m) \in \mathbb{R}^m$, 使得

$$
\nabla f (\boldsymbol {x} _ {0}) - \boldsymbol {\lambda} \cdot J \boldsymbol {\Phi} (\boldsymbol {x} _ {0}) = \boldsymbol {0}. \tag {15.7.4}
$$

用分量形式表示的话, 即为

$$
\nabla f (\boldsymbol {x} _ {0}) = \lambda_ {1} \nabla \varphi_ {1} (\boldsymbol {x} _ {0}) + \dots + \lambda_ {m} \nabla \varphi_ {m} (\boldsymbol {x} _ {0}). \tag {15.7.5}
$$

证明 不妨设

$$
\frac {\partial (\varphi_ {1} , \cdots , \varphi_ {m})}{\partial (x _ {1} , \cdots , x _ {m})} (\boldsymbol {x} _ {0}) \neq 0.
$$

由隐映射定理, 存在点  $\boldsymbol{z}_{0} = (x_{m+1}^{0}, \cdots, x_{n}^{0})$  的开邻域 V 以及  $C^{k}$  映射  $\psi : V \to R^{m}$  使得

$$
y _ {0} = \psi (z _ {0}), \quad \Phi (\psi (z), z) = 0, \quad \forall   z \in V.
$$

其中  $\boldsymbol{y}_{0}=(x_{1}^{0},\cdots,x_{m}^{0})$ ,  $\boldsymbol{y}=(x_{1},\cdots,x_{m})$ ,  $\boldsymbol{z}=(x_{m+1},\cdots,x_{n})$ ,  $\boldsymbol{x}=(\boldsymbol{y},\boldsymbol{z})\in U.$ 
在  $x_{0}=(y_{0},z_{0})$  处求导, 有

$$
J \psi (\boldsymbol {z} _ {0}) = - (J _ {\boldsymbol {y}} \boldsymbol {\Phi}) ^ {- 1} (\boldsymbol {x} _ {0}) \cdot J _ {\boldsymbol {z}} \boldsymbol {\Phi} (\boldsymbol {x} _ {0}). \tag {15.7.6}
$$

由于 $x_0$ 为 $f$ 的条件极值点, 故 $z_0$ 为 $f(\psi(z), z)$ 的极值点 (驻点), 在 $z_0$ 处求导, 得

$$
J _ {\boldsymbol {y}} f (\boldsymbol {x} _ {0}) \cdot J \psi (\boldsymbol {z} _ {0}) + J _ {\boldsymbol {z}} f (\boldsymbol {x} _ {0}) = \boldsymbol {0}. \tag {15.7.7}
$$

将 (15.7.6) 式代入上式, 得

$$
J _ {z} f (\boldsymbol {x} _ {0}) = J _ {\boldsymbol {y}} f (\boldsymbol {x} _ {0}) \cdot (J _ {\boldsymbol {y}} \boldsymbol {\Phi}) ^ {- 1} (\boldsymbol {x} _ {0}) \cdot J _ {z} \boldsymbol {\Phi} (\boldsymbol {x} _ {0}). \tag {15.7.8}
$$

记 $\lambda = J_{\pmb{y}}f(\pmb{x}_0)\cdot (J_{\pmb{y}}\pmb {\Phi})^{-1}(\pmb {x}_0)$ ，即

$$
J _ {\boldsymbol {y}} f (\boldsymbol {x} _ {0}) = \boldsymbol {\lambda} \cdot J _ {\boldsymbol {y}} \boldsymbol {\Phi} (\boldsymbol {x} _ {0}). \tag {15.7.9}
$$

(15.7.8) 式可用  $\lambda$  改写为

$$
J _ {z} f (\boldsymbol {x} _ {0}) = \boldsymbol {\lambda} \cdot J _ {z} \boldsymbol {\Phi} (\boldsymbol {x} _ {0}). \tag {15.7.10}
$$

(15.7.9) 式和 (15.7.10) 式结合起来就得到 (15.7.4) 式.

□

---

304

第十五章 多元函数微分学及其应用

在实际应用中, (15.7.4) 式通常解释为: 如果  $x_{0}$  为条件极值点, 则  $(\boldsymbol{x}_{0}, \boldsymbol{\lambda})$  为如下辅助函数的驻点:

$$
F (\boldsymbol {x}, \boldsymbol {\lambda}) = f (\boldsymbol {x}) - \sum_ {i = 1} ^ {m} \lambda_ {i} \cdot \varphi_ {i} (\boldsymbol {x}).
$$

例15.7.1 求圆周 $(x - 1)^2 + y^2 = 1$ 上的点与固定点(0,1)的距离的最大值和最小值.

解 在约束条件 $(x - 1)^2 + y^2 - 1 = 0$ 下求距离函数 $d = \sqrt{x^2 + (y - 1)^2}$ 的最大值和最小值. 考虑辅助函数

$$
F (x, y, \lambda) = x ^ {2} + (y - 1) ^ {2} - \lambda ((x - 1) ^ {2} + y ^ {2} - 1),
$$

求其驻点:

$$
F _ {x} = F _ {y} = F _ {\lambda} = 0 \Longleftrightarrow \left\{ \begin{array}{l l} x - \lambda (x - 1) = 0, \\ y - 1 - \lambda y = 0, \\ (x - 1) ^ {2} + y ^ {2} - 1 = 0 \end{array} \right. \Longrightarrow \left\{ \begin{array}{l l} x = \frac {- \lambda}{1 - \lambda}, \\ y = \frac {1}{1 - \lambda}, \\ \lambda = 1 \pm \sqrt {2}. \end{array} \right.
$$

在驻点处 $d^2 = \lambda^2$ ，即 $d = |\lambda|$ .由于 $d$ 在圆周上达到最大值和最小值，故其最大值必为 $\sqrt{2} +1$ ，最小值必为 $\sqrt{2} -1$ □

例 15.7.2 设  $\alpha_{i}>0, x_{i}>0, i=1,\cdots,n.$  证明:

$$
x _ {1} ^ {\alpha_ {1}} \dots x _ {n} ^ {\alpha_ {n}} \leqslant \left(\frac {\alpha_ {1} x _ {1} + \cdots + \alpha_ {n} x _ {n}}{\alpha_ {1} + \cdots + \alpha_ {n}}\right) ^ {\alpha_ {1} + \dots + \alpha_ {n}},
$$

等号成立当且仅当  $x_{1}=x_{2}=\cdots=x_{n}$ .

证明 考虑函数 $f(x_{1},\dots ,x_{n}) = \ln (x_{1}^{\alpha_{1}}\dots x_{n}^{\alpha_{n}}) = \sum_{i = 1}^{n}\alpha_{i}\ln x_{i}$ 在约束条件 $\sum_{i = 1}^{n}\alpha_{i}x_{i} = c(c > 0)$ 下的条件极值.令

$$
F (x, \lambda) = \sum_ {i = 1} ^ {n} \alpha_ {i} \ln x _ {i} - \lambda \Big (\sum_ {i = 1} ^ {n} \alpha_ {i} x _ {i} - c \Big),
$$

求驻点:

$$
F _ {x _ {i}} = F _ {\lambda} = 0 \quad \Longrightarrow \quad \frac {\alpha_ {i}}{x _ {i}} = \lambda \alpha_ {i}, \quad \sum_ {i = 1} ^ {n} \alpha_ {i} x _ {i} - c = 0,
$$

即  $x_{i}=c\left(\sum_{i=1}^{n}\alpha_{i}\right)^{-1}, i=1,2,\cdots,n.$  因为在集合  $D: x_{i} \geqslant 0, \sum_{i=1}^{n} \alpha_{i} x_{i}=c$  的边界上，f 取值为  $-\infty,$  因此 f 在 D 的内部取到最大值，上述唯一驻点必为最大值点，从而

$$
\ln (x _ {1} ^ {\alpha_ {1}} \dots x _ {n} ^ {\alpha_ {n}}) \leqslant \sum_ {i = 1} ^ {n} \alpha_ {i} \ln c \Big (\sum_ {i = 1} ^ {n} \alpha_ {i} \Big) ^ {- 1},
$$

---

15.7 Lagrange 乘数法 条件极值

305

整理以后即得欲证不等式.

由于在Lagrange乘数法中，条件极值问题转化为

$$
F (\boldsymbol {x}) = f (\boldsymbol {x}) - \sum_ {j = 1} ^ {m} \lambda_ {j} \varphi_ {j} (\boldsymbol {x})
$$

的普通极值问题. 当  $x_{0}$  是驻点时,  $\lambda_{j}, j=1,2,\cdots,m$  是 m 个常数, 因此我们利用  $F(\boldsymbol{x})$  在  $x_{0}$  处的 Hesse 矩阵  $\boldsymbol{H}_{F}(\boldsymbol{x}_{0})$  来判定  $x_{0}$  是否为极值点: 可以证明, 当  $\boldsymbol{H}_{F}(\boldsymbol{x}_{0})$  正定时, 条件极值点为极小值点;  $\boldsymbol{H}_{F}(\boldsymbol{x}_{0})$  负定时, 条件极值为极大值点. 值得注意的是当  $\boldsymbol{H}_{F}(\boldsymbol{x}_{0})$  不定时, 对于无条件极值, 此时  $x_{0}$  的极值性不可得知, 但是, 对于条件极值仍可能取到.

例如, 设 $f(x,y) = x^{2} - y^{2}, \varphi(x,y) = y \equiv 0$, 则 $\varphi(x,y) = 0$ 确定直线方程 $y = 0$, 显然 $f(x,0) = x^{2}$ 在 $(0,0)$ 处取极小值 0. 容易算出 $F(x,y) = x^{2} - y^{2} - \lambda y$ 的 Hesse 矩阵在 $(0,0)$ 处为对角矩阵 $\mathrm{diag}(2,-2)$, 这是一个不定矩阵.

另外, 如果约束条件中有不可微点或者退化点, 那么在这些点上, 条件极值要单独考虑. 例如, 考虑函数 $f(x, y) = x^2 + y^2$ 在条件 $\varphi(x, y) = (x - 1)^3 - y^2 = 0$ 限制下的最小值.

记 $F(x,y,\lambda) = f(x,y) - \lambda \varphi (x,y)$ .直接计算可以发现，方程组

$$
F _ {x} (x, y) = 0, \quad F _ {y} (x, y) = 0, \quad \varphi (x, y) = 0
$$

没有解.但是注意到 $f(x,y)$ 本质上是原点到曲线 $\Sigma : \varphi (x,y) = 0$ 上点 $(x,y)$ 的距离（的平方），所以 $f(x,y)$ 显然在曲线 $\Sigma$ 上的尖点(1,0)处有最小值（注意(1,0)处$F_{x}(1,0)\neq 0)$ .见图15.10.

![](../../raw/pages_0609-0624/images/page_609_image_11.jpg)

<details>
<summary>text_image</summary>

y
y² = (x - 1)³
O
(1,0)
x
</details>

图15.10 条件极值退化点的情况

## 习题 15.7

1. 求下列函数在指定约束条件下的极值  $(a, b, c > 0)$ :

(1) $f(x,y) = xy, \quad x + y = 1.$

---

306

第十五章 多元函数微分学及其应用

(2)  $f(x,y)=x/a+y/b,\quad x^{2}+y^{2}=1.$
(3) $f(x,y)=x^{2}+y^{2},\quad x/a+y/b=1.$
(4) $f(x,y) = \cos \pi (x + y),\quad x^{2} + y^{2} = 1.$
(5) $f(x,y,z) = x - 2y + 2z, \quad x^2 + y^2 + z^2 = 1.$
(6) $f(x,y,z) = 3x^{2} + 3y^{2} + z^{2},\quad x + y + z = 1.$
(7) $f(x,y,z) = x^{a}y^{b}z^{c},\quad x,y,z\geqslant 0,\quad x + y + z = 1.$

2. 求周长为  $2\ell$  的平面三角形的最大面积.

3. 求圆内接三角形面积最大者.

4. 称一个三角形内接于正方形是指三角形的三个顶点均落在正方形的边界上. 给定一个单位正方形, 试在所有的内接等边三角形中, 求出边长最大和边长最小的等边三角形.

5. 求原点到直线  $2x + 2y + z + 9 = 0,\quad 2x - y - 2z - 18 = 0$  的距离.

6. 求椭圆  $x^{2} + 4y^{2} = 4$  到直线  $x + y = 4$  的距离.

7. 求抛物线  $y = x^{2}$  与直线 x - y - 2 = 0 之间的最短距离.

8. 设 $a > 0$, 求曲线

$$
\left\{ \begin{array}{l} x ^ {2} + y ^ {2} = 2 a x, \\ x ^ {2} + y ^ {2} + x y = a ^ {2} \end{array} \right.
$$

上的点到 xOy 平面的最小距离和最大距离.

9. 求包含在椭圆  $\frac{x^{2}}{a^{2}} + \frac{y^{2}}{b^{2}} = 1$  内各边与坐标轴平行的矩形的最大周长.

10. 求包含在椭球 $\frac{x^2}{a^2} + \frac{y^2}{b^2} + \frac{z^2}{c^2} = 1$ 内各面与坐标面平行的长方体的最大体积、所有这样的长方体的最大表面积, 以及所有这样的长方体的最大棱长.

思考与对比: 它们是同一个长方体吗?

又问: 如果去掉“各面与坐标面平行的长方体”这一假设限制, 上述问题的结论如何?

11. 设 a > 0, 试将 a 分解为 n 个正因子, 使得其倒数之和最小.
12. 给定一个凸四边形, 试在其内求一点 $P$, 使得 $P$ 到四个顶点的距离之平方和最小.

13. 设  $a_{1}, a_{2}, \cdots, a_{n} \geqslant 0$ ，求  $u = \sum_{i=1}^{n} a_{i} x_{i}$  在高维球面  $\sum_{i=1}^{n} x_{i}^{2} = r^{2}$  上的最大值和最小值.

14. 设 $D$ 是由两抛物线 $y = x^{2} - 1, y = -x^{2} + 1$ 所围成的闭域. 试在 $D$ 内求一形如 $\frac{x^2}{a^2} + \frac{y^2}{b^2} = 1$ 的椭圆, 使其面积最大.

15. 设  $a_{1}, a_{2}, \cdots, a_{n}$  均为正实数,  $a_{1} + \cdots + a_{n} = 2000$ . 试确定合适的 n 使得  $a_{1} \cdots a_{n}$  达到最大值. 又若要求所有的  $a_{i}$  均为自然数, 再考虑这个问题.

---

15.8 多元微分学在几何上的应用

307

16. 设 $p > 1$, $\frac{1}{p} + \frac{1}{q} = 1$, 用求条件极值的办法证明 Hölder 不等式

$$
\sum_ {i = 1} ^ {n} u _ {i} v _ {i} \leqslant \left(\sum_ {i = 1} ^ {n} u _ {i} ^ {p}\right) ^ {\frac {1}{p}} \left(\sum_ {i = 1} ^ {n} v _ {i} ^ {q}\right) ^ {\frac {1}{q}}, \quad \forall u _ {i}, v _ {i} \geqslant 0, i = 1, \dots , n.
$$

17. 设  $\boldsymbol{A}=(a_{ij})_{n\times n}$  为 n 阶方阵,  $\boldsymbol{b}=(b_{1},b_{2},\cdots,b_{n})\in\mathbb{R}^{n}$ , 令

$$
f (\boldsymbol {x}) = \boldsymbol {x} \boldsymbol {A} \boldsymbol {x} ^ {\mathrm{T}} + \boldsymbol {b} \boldsymbol {x} = \sum_ {i, j = 1} ^ {n} a _ {i j} x _ {i} x _ {j} + \sum_ {i = 1} ^ {n} b _ {i} x _ {i}, \quad \boldsymbol {x} \in \mathbb {R} ^ {n}.
$$

(1) 分析 f 在  $R^{n}$  上的极值.
(2) 分析 $f$ 在约束条件 $\sum_{i=1}^{n} x_i^2 = 1$ 下的极值.

18. 求函数 $f(x, y) = \sin x + \cos y + \cos (x - y)$ 在正方形 $\left[0, \frac{\pi}{2}\right]^2$ 上的极值.

19. 设 $f(x, y) = 3x^4 - 4x^2y + y^2$. 证明: 限制在每一条过原点的直线上, 原点是 $f$ 的极小值点, 但是函数 $f$ 在原点处不取极小值. 在 $xOy$ 平面上, 画出点集

$$
P = \{(x, y) | f (x, y) > 0 \}, \quad Q = \{(x, y) | f (x, y) <   0 \}.
$$

20. 求由隐函数 $2x^{2} + y^{2} + z^{2} + 2xy - 2x - 2y - 4z + 4 = 0$ 所确定的函数 $z = z(x,y)$ 的极值.

21. (一般情况下的最小二乘法) 设  $(x_{i}, y_{i}) (i = 0, 1, 2, \cdots, n)$  为平面  $R^{2}$  上  $n + 1$  个互异点, 求一个 m (m < n) 次多项式  $Y = a_{0} + a_{1}x + \cdots + a_{m}x^{m}$ , 使得  $F(\boldsymbol{a}) = \sum_{i=0}^{n} (Y_{i} - y_{i})^{2}$  最小, 其中  $\boldsymbol{a} = (a_{0}, \cdots, a_{m}), Y_{i} = a_{0} + a_{1}x_{i} + \cdots + a_{m}x_{i}^{m} (i = 0, 1, \cdots, n)$ .

22. (1) 求把一个等边三角形面积二等分的所有直线段的最短长度.

(2) 求把一个等边三角形面积二等分的所有二折线段的最短长度.
(3) 求把一个等边三角形面积二等分的所有曲线的最短长度.

## 15.8 多元微分学在几何上的应用

在本章最后一节, 我们来讨论一下多元微分学在几何上的应用. 主要包括用解析的方法讨论空间曲线的切线和法平面, 以及曲面的切平面和法线.

## 空间曲线的切线和法平面

$\mathbb{R}^n$ 空间中的一条曲线 $\Gamma$ 是指 $[0,1] \to \mathbb{R}^n$ 的一个连续映射

$$
\Gamma : \gamma (t) = (x _ {1} (t), x _ {2} (t), \dots , x _ {n} (t)), \quad t \in [ 0, 1 ], \tag {15.8.1}
$$

---

308

第十五章 多元函数微分学及其应用

$t$ 称为参数. 当 $n = 2,3$ 时, 即我们熟悉的平面曲线和三维空间曲线.

我们知道, 一般来说, 如果仅仅要求 $\gamma(t)$ 是一个连续映射, 则几何上我们称为连续曲线. 连续曲线有可能是非常复杂的, 比如, 它可以是不可求长的, 可以如 Peano 曲线那样充满平面或空间中某个区域. 不可求长曲线一定是其光滑性不够好, 比如 $\gamma(t)$ 不可能是逐段 $C^1[0,1]$ 的, Peano 曲线中的映射 $\gamma(t)$ 不可能是 $1 - 1$ 的.

由于我们的目的是探讨多元微分学在几何上的应用, 因此在下面的讨论中, 我们约定: 由连续映射 (15.8.1) 给出的曲线 $\Gamma$ 是简单的和可微的. $\Gamma$ 称为简单的是指, $\forall t_1 \in (0,1), t_2 \in [0,1]$, 当 $t_1 \neq t_2$ 时, 都有 $\gamma(t_1) \neq \gamma(t_2)$. 进一步, 若对 $t_1 \neq t_2$, 有 $\gamma(t_1) \neq \gamma(t_2)$, 同时还有 $\gamma(0) = \gamma(1)$, 则 $\Gamma$ 称为一条 Jordan 闭曲线; $\Gamma$ 称为可微的是指 $\gamma(t)$ 作为映射是可微的, 这等价于 $x_i(t) (i=1,2,\cdots,n)$ 是可微函数.

下面我们考虑如何寻求由(15.8.1)给出的曲线 $\Gamma$ 在点 $P_0 = \gamma (t_0)$ 处的切线.由于切线是通过割线的极限状态来定义的，因此，在曲线 $\Gamma$ 上任取一点 $P = \gamma (t)$ ，考虑由 $P$ 与 $P_{0}$ 两点确定的割线 $L_{P_0P}$

$$
\frac {x _ {1} - x _ {\mathrm{i}} (t _ {0})}{x _ {1} (t) - x _ {1} (t _ {0})} = \dots = \frac {x _ {n} - x _ {n} (t _ {0})}{x _ {n} (t) - x _ {n} (t _ {0})},
$$

其中  $(x_{1}, x_{2}, \cdots, x_{n})$  是  $L_{P_{0}P}$  上的动点坐标. 在上式中分母同除以  $t - t_{0}$  并取  $t \rightarrow t_{0}$  的极限, 根据  $\Gamma$  的可微性假设, 有下式成立:

$$
\frac {x _ {1} - x _ {1} (t _ {0})}{x _ {1} ^ {\prime} (t _ {0})} = \dots = \frac {x _ {n} - x _ {n} (t _ {0})}{x _ {n} ^ {\prime} (t _ {0})}.
$$

这就是曲线  $\Gamma$  在  $P_{0}$  处的切线方程.

可以看出

$$
\gamma^ {\prime} (t _ {0}) = (x _ {1} ^ {\prime} (t _ {0}), x _ {2} ^ {\prime} (t _ {0}), \dots , x _ {n} ^ {\prime} (t _ {0}))
$$

恰好为曲线 $\Gamma$ 在 $P_0$ 处的切向量.

我们同时也得到了曲线 $\Gamma$ 在 $P_0$ 处的法平面方程:即过 $P_0$ 点以切向量为法向的平面方程

$$
\gamma^ {\prime} (t _ {0}) \cdot (\boldsymbol {x} - \boldsymbol {x} (t _ {0})) = 0.
$$

例 15.8.1 一元函数图像的切线.设 f 为一元可微函数，令  $\gamma(t)=(t,f(t))$ ，则  $\gamma'(t_{0})=(1,f'(t_{0}))$ ， $\gamma(t)$  在  $t_{0}$  处切线方程为

$$
\frac {x - t _ {0}}{1} = \frac {y - f (t _ {0})}{f ^ {\prime} (t _ {0})},
$$

即 $y = f(t_0) + f'(t_0)(x - t_0)$，这也就是一元函数图像的切线。此时的法平面表现为法线，其表达式为

$$
x - t _ {0} + f ^ {\prime} (t _ {0}) (y - f (t _ {0})) = 0.
$$

---

15.8 多元微分学在几何上的应用

309

例 15.8.2 设 a > 0, 求螺旋线  $\gamma(t) = (a \cos t, a \sin t, t)$  的切线和法平面方程.

解 在 $t = t_0$ 处, $\gamma'(t_0) = (-a\sin t_0, a\cos t_0, 1)$, 故切线方程为

$$
\frac {x - a \cos t _ {0}}{- a \sin t _ {0}} = \frac {y - a \sin t _ {0}}{a \cos t _ {0}} = \frac {z - t _ {0}}{1},
$$

法平面方程化简后为 $z = (a\sin t_0)x - (a\cos t_0)y + t_0.$

作为一种特殊情况, 下面我们讨论三维空间中由两个曲面交线形成的曲线的切线方程. 假设  $F_{1}$  与  $F_{2}$  均为区域  $D \subseteq R^{3}$  上的可微函数, 考虑由方程组

$$
F _ {1} (x, y, z) = 0, \quad F _ {2} (x, y, z) = 0, \quad (x, y, z) \in D
$$

定义的点集.

我们知道, 当

$$
\boldsymbol {F} ^ {\prime} (\boldsymbol {x} _ {0}) = \binom{F _ {1} ^ {\prime} (\boldsymbol {x} _ {0})}{F _ {2} ^ {\prime} (\boldsymbol {x} _ {0})} = \left( \begin{array}{c c c} \frac {\partial F _ {1}}{\partial x} & \frac {\partial F _ {1}}{\partial y} & \frac {\partial F _ {1}}{\partial z} \\ \frac {\partial F _ {2}}{\partial x} & \frac {\partial F _ {2}}{\partial y} & \frac {\partial F _ {2}}{\partial z} \end{array} \right) _ {\boldsymbol {x} _ {0}}
$$

的秩为2时，由隐函数组存在定理，在 $x_0 = (x_0, y_0, z_0)$ 附近，存在两个变量可确定为第三个变量的函数，从而该方程组能确定一条过 $x_0 = (x_0, y_0, z_0)$ 的曲线 $\Gamma$ ，且在 $x_0$ 附近 $\Gamma$ 可以表示为参数形式 $\gamma(t) = (x(t), y(t), z(t)), t \in (a, b)$，其中

$$
\boldsymbol {x} _ {0} = (x _ {0}, y _ {0}, z _ {0}) = \boldsymbol {\gamma} (t _ {0}) = (x (t _ {0}), y (t _ {0}), z (t _ {0})).
$$

一方面我们知道曲线 $\Gamma$ 在点 $x_0$ 处的切向量为 $\gamma'(t_0) = (x'(t_0), y'(t_0), z'(t_0))$, 另一方面, 曲线 $\Gamma$ 是由方程组

$$
F _ {1} (x (t), y (t), z (t)) = 0, \quad F _ {2} (x (t), y (t), z (t)) = 0
$$

确定, 所以, 对方程组关于 t 求导, 可得  $\nabla F_{1}(\boldsymbol{x}_{0}) \cdot \boldsymbol{\gamma}'(t_{0}) = 0$ , 即

$$
\left(\frac {\partial F _ {1} (\boldsymbol {x} _ {0})}{\partial x}, \frac {\partial F _ {1} (\boldsymbol {x} _ {0})}{\partial y}, \frac {\partial F _ {1} (\boldsymbol {x} _ {0})}{\partial z}\right) (x ^ {\prime} (t _ {0}), y ^ {\prime} (t _ {0}), z ^ {\prime} (t _ {0})) = 0.
$$

同理

$$
\left(\frac {\partial F _ {2} (\boldsymbol {x} _ {0})}{\partial x}, \frac {\partial F _ {2} (\boldsymbol {x} _ {0})}{\partial y}, \frac {\partial F _ {2} (\boldsymbol {x} _ {0})}{\partial z}\right) (x ^ {\prime} (t _ {0}), y ^ {\prime} (t _ {0}), z ^ {\prime} (t _ {0})) = 0.
$$

因此 $\Gamma$ 在点 $x_0$ 处的切向量 $\gamma'(t_0)$ 应该与向量 $F_{1}^{\prime}(x_{0})\times F_{2}^{\prime}(x_{0})$ 平行.直接计算可得

$$
F _ {1} ^ {\prime} (\boldsymbol {x} _ {0}) \times F _ {2} ^ {\prime} (\boldsymbol {x} _ {0}) = (A, B, C) = \left(\frac {\partial (F _ {1} , F _ {2})}{\partial (y , z)}, \frac {\partial (F _ {1} , F _ {2})}{\partial (z , x)}, \frac {\partial (F _ {1} , F _ {2})}{\partial (x , y)}\right) _ {\boldsymbol {x} _ {0}}.
$$

---

310

第十五章 多元函数微分学及其应用

所以曲线 $\Gamma$ 在 $x_0$ 处的切线方程为

$$
\frac {x - x _ {0}}{A} = \frac {y - y _ {0}}{B} = \frac {z - z _ {0}}{C},
$$

而法平面方程为

$$
A (x - x _ {0}) + B (y - y _ {0}) + C (z - z _ {0}) = 0.
$$

## 曲面的切平面和法线

下面我们讨论一下三维空间中两种常见情形的曲面的切平面和法线.

## 1. 形如 $F(x, y, z) = 0$ 的曲面

设 $\mathbb{R}^3$ 中的曲面 $S$ 是由方程 $F(x,y,z) = 0$ 给出, 其中函数 $F(x,y,z)$ 是区域 $D \subseteq \mathbb{R}^3$ 上的连续可微函数. 设 $\pmb{x}_0 = (x_0, y_0, z_0) \in D$ 且在曲面 $S$ 上, 即 $F(x_0, y_0, z_0) = 0$. 我们来求过点 $\pmb{x}_0$ 的切平面方程和法线方程.

为此, 在 $S$ 上任取一条过 $\pmb{x}_0$ 的空间光滑曲线 $\Gamma: \gamma(t) = (x(t), y(t), z(t)), t \in (a, b)$. 设 $t_0 \in (a, b)$ 满足 $\gamma(t_0) = \pmb{x}_0$. 故有

$$
F (\gamma (t)) = F (x (t), y (t), z (t)) \equiv 0, \quad \forall t \in (a, b).
$$

将该方程在 $t_0$ 处求导, 可得

$$
\nabla F (\boldsymbol {x} _ {0}) \cdot \boldsymbol {\gamma} ^ {\prime} (t _ {0}) = 0.
$$

这说明满足上述条件的任何一条曲线 $\Gamma$ 在 $x_0$ 处的切向量都与固定向量 $\nabla F(x_0)$ 正交. 如果 $\nabla F(x_0)$ 是非零向量, 那么上式表明曲面 $S$ 过 $x_0$ 的任何光滑曲线的切向量与固定向量 $\nabla F(x_0)$ 正交. 因此, $S$ 上过 $x_0$ 点的任何光滑曲线在该点处的切线都在平面

$$
\pi : \quad \nabla F (\boldsymbol {x} _ {0}) \cdot (\boldsymbol {x} - \boldsymbol {x} _ {0}) = 0
$$

上. 平面 $\pi$ 很自然地被称为曲面 $S$ 在 $\pmb{x}_0$ 处的切平面, 而直线

$$
\ell : \quad \frac {x - x _ {0}}{F _ {x} (\boldsymbol {x} _ {0})} = \frac {y - y _ {0}}{F _ {y} (\boldsymbol {x} _ {0})} = \frac {z - z _ {0}}{F _ {z} (\boldsymbol {x} _ {0})}
$$

称为 S 在  $x_{0}$  处的法线.

## 2. 由参数方程给出的曲面

考虑 $\mathbb{R}^3$ 中由双参数 $(u,v)\in D\subseteq \mathbb{R}^2$ 给出的曲面 $S:\pmb {x} = \pmb {x}(u,v)$ ，其分量形式为

$$
S: \quad x = x (u, v), \quad y = y (u, v), \quad z = z (u, v),
$$

其中 $D$ 是 $\mathbb{R}^2$ 中的区域. 假设所有的分量函数 $x(u,v), y(u,v)$ 和 $z(u,v)$ 都是 $D$ 上的 $C^1(D)$ 函数, 我们来求曲面 $S$ 在点

$$
\boldsymbol {x} _ {0} = (x _ {0}, y _ {0}, z _ {0}) = (x (u _ {0}, v _ {0}), y (u _ {0}, v _ {0}), z (u _ {0}, v _ {0})), \quad (u _ {0}, v _ {0}) \in D
$$

---

15.8 多元微分学在几何上的应用

311

处的切平面与法线方程. 为此, 在 S 上取两条特别的曲线:

$$
\Gamma_ {1}:   \pmb {x} = \pmb {x} (u, v _ {0}) \quad {\text {和}} \quad \Gamma_ {2}:   \pmb {x} = \pmb {x} (u _ {0}, v).
$$

它们在 $x_0$ 处的切向量分别为

$$
\pmb {x} _ {u} ^ {0} = (x _ {u} (u _ {0}, v _ {0}), y _ {u} (u _ {0}, v _ {0}), z _ {u} (u _ {0}, v _ {0})) \quad \text {和} \quad \pmb {x} _ {v} ^ {0} = (x _ {v} (u _ {0}, v _ {0}), y _ {v} (u _ {0}, v _ {0}), z _ {v} (u _ {0}, v _ {0})).
$$

如果它们不平行, 则它们对应的切线将确定 $S$ 在 $\pmb{x}_0$ 处的切平面 $\pi$ 和法向量 $\pmb{n}$.

$$
\boldsymbol {n} = \boldsymbol {x} _ {u} ^ {0} \times \boldsymbol {x} _ {v} ^ {0} = \left| \begin{array}{c c c} \boldsymbol {i} & \boldsymbol {j} & \boldsymbol {k} \\ x _ {u} & y _ {u} & z _ {u} \\ x _ {v} & y _ {v} & z _ {v} \end{array} \right| _ {(u _ {0}, v _ {0})}.
$$

故当

$$
\left( \begin{array}{c c c} x _ {u} & y _ {u} & z _ {u} \\ x _ {v} & y _ {v} & z _ {v} \end{array} \right) _ {(u _ {0}, v _ {0})}
$$

的秩为 2 时, 记

$$
A = \frac {\partial (y , z)}{\partial (u , v)} \Big | _ {(u _ {0}, v _ {0})}, \quad B = \frac {\partial (z , x)}{\partial (u , v)} \Big | _ {(u _ {0}, v _ {0})}, \quad C = \frac {\partial (x , y)}{\partial (u , v)} \Big | _ {(u _ {0}, v _ {0})},
$$

则曲面 $S$ 在 $\pmb{x}_0$ 处的切平面 $\pi$ 的方程与法线 $L$ 的方程分别为

$$
\pi : \quad (A, B, C) \cdot (\boldsymbol {x} - \boldsymbol {x} _ {0}) = A (x - x _ {0}) + B (y - y _ {0}) + C (z - z _ {0}) = 0
$$

和

$$
L: \quad \frac {x - x _ {0}}{A} = \frac {y - y _ {0}}{B} = \frac {z - z _ {0}}{C}.
$$

通常我们又把切平面 $\pi$ 的方程改写为下面行列式的表示形式:

$$
\left| \begin{array}{c c c} x - x _ {0} & y - y _ {0} & z - z _ {0} \\ x _ {u} & y _ {u} & z _ {u} \\ x _ {v} & y _ {v} & z _ {v} \end{array} \right| _ {(u _ {0}, v _ {0})} = 0.
$$

例15.8.3 考虑一种特殊的由显式方程给出的曲面 $S: z = f(x, y), (x, y) \in D \subseteq \mathbb{R}^2$，其中 $f(x, y) \in C^1(D)$. 将其写成参数形式

$$
x = x, \quad y = y, \quad z = f (x, y), \quad (x, y) \in D.
$$

则曲面 $S$ 过点 $P_{0}(x_{0},y_{0},z_{0})$ 的切平面方程可以写成

$$
\left| \begin{array}{c c c} x - x _ {0} & y - y _ {0} & z - z _ {0} \\ 1 & 0 & f _ {x} (x _ {0}, y _ {0}) \\ 0 & 1 & f _ {y} (x _ {0}, y _ {0}) \end{array} \right| = 0,
$$

---

312

第十五章 多元函数微分学及其应用

即

$$
z = z _ {0} + f _ {x} (x _ {0}, y _ {0}) (x - x _ {0}) + f _ {y} (x _ {0}, y _ {0}) (y - y _ {0}).
$$

曲面 $S$ 过点 $P_{0}(x_{0},y_{0},z_{0})$ 的法线方程可以表示为

$$
\frac {x - x _ {0}}{- f _ {x} (x _ {0} , y _ {0})} = \frac {y - y _ {0}}{- f _ {y} (x _ {0} , y _ {0})} = \frac {z - z _ {0}}{1}.
$$

## 习题 15.8

1. 求下列曲线在指定点的切线和法平面方程:

(1) $\sigma(t) = (a\cos t\sin t, b\sin^2 t, c\cos t), \quad t = \frac{\pi}{4}$.
(2)  $\boldsymbol{\sigma}(t)=(t,t^{2},t^{3}),\quad t=t_{0}.$
(3)  $\boldsymbol{\sigma}(t)=(a\cos t,a\sin t),\quad t=t_{0}.$

2. 求下列曲面在指定点的切平面和法线方程:

(1)  $r(u, v) = (u, a \cos v, a \sin v), \quad (u, v) = (u_0, v_0).$
(2) $z = x^{2} + y^{2},\quad (x,y,z) = (1,2,5)$
(3)  $r(u,v) = (a \sin u \cos v, b \sin u \sin v, c \cos u), \quad (u,v) = (u_{0}, v_{0}).$

3. 求下列曲面在指定点的切平面:

(1) $x^{3} + 2xy^{2} - 7z^{3} + 3y + 1 = 0, (x,y,z) = (1,1,1)$.
(2) $(x^{2} + y^{2})^{2} + x^{2} - yz + 7xy + 3x + z^{4} - z = 14,\quad (x,y,z) = (1,1,1).$
(3) $\sin^2 x + \cos (y + z) = \frac{3}{4},\quad (x,y,z) = \left(\frac{\pi}{6},\frac{\pi}{3},0\right)$.
(4) $x^{2} + y^{2} = z^{2} + \sin z, (x,y,z) = (0,0,0)$.

4. 求下列曲线在指定点的切线:

(1) $x^{2} + y^{2} + z^{2} = 3x, \quad 2x - 3y + 5z = 4, \quad (x,y,z) = (1,1,1)$.
(2) $x^{2} + z^{2} = 10, \quad y^{2} + z^{2} = 10, \quad (x,y,z) = (1,1,3)$.
(3) $3x^{2} + 3y^{2} - z^{2} = 32, \quad x^{2} + y^{2} = z^{2}, \quad (x,y,z) = (\sqrt{7},3,4)$.

5. 求出下列曲面在指定点处的法向量和切平面方程:

(1) $x^{2} + y^{2} + z^{2} = 4, \quad P_{0}(1,1,\sqrt{2}).$
(2) $z = \arctan \frac{y}{x},\quad P_0\left(1,1,\frac{\pi}{4}\right).$
(3) $3x^{2}+2y^{2}-2z-1=0,\quad P_{0}(1,1,2).$
(4) $z = y + \ln \frac{x}{z},\quad P_0(1,1,1).$

6. 求出椭球面 $x^{2} + 2y^{2} + 3z^{2} = 21$ 上所有平行于平面 $x + 4y + 6z = 0$ 的切平面.

7. 证明: 曲面  $z = x e^{x/y}$  上所有切平面都通过原点.

8. 定出常数 $\lambda$, 使曲面 $xyz = \lambda$ 与椭球面

$$
\frac {x ^ {2}}{a ^ {2}} + \frac {y ^ {2}}{b ^ {2}} + \frac {z ^ {2}}{c ^ {2}} = 1
$$

---

15.8 多元微分学在几何上的应用

313

在某一点相切, 即有共同的切平面.

9. 两相交曲面在交点处的法向量所夹的角称为这两曲面在该点的夹角. 求柱面 $x^{2} + y^{2} = a^{2}$ 与曲面 $bz = xy$ 的夹角.

10. 求椭球面

$$
\frac {x ^ {2}}{a ^ {2}} + \frac {y ^ {2}}{b ^ {2}} + \frac {z ^ {2}}{c ^ {2}} = 1
$$

上点的法向量与 x 轴和 z 轴夹成等角的点的全体.

11. 求曲面 $x^{2} + y^{2} + z^{2} = x$ 的切平面, 使其垂直于平面 $x - y - z = 2$ 和 $x - y - \frac{z}{2} = 2$.

12. 证明: 曲面 $\sqrt{x + \sqrt{y + \sqrt{z}}} = \sqrt{a} (a > 0)$ 的切平面在各坐标轴上割下的诸线段之和为常数.

13. 证明: 曲面 $F(x - ax, y - bz) = 0$ 的所有切平面与某一直线平行, 其中 $a, b$ 为常数.

14. 证明: 曲面

$$
F \left(\frac {x - a}{z - c}, \frac {y - b}{z - c}\right) = 0
$$

的切平面通过一定点, 其中 a, b, c 为常数.

15. 设  $R^{3}$  中的曲面在柱面坐标下的方程为  $F(r,\theta,z)=0$ ，其中 F 是可微函数。试求  $(r_{0},\theta_{0},z_{0})$  所对应曲面上的点处的切平面与法线方程。

16. 设曲面 $S$ 由 $F(x, y, z) = 0$ 给出, 其中 $F(x, y, z)$ 是区域 $D \subseteq \mathbb{R}^3$ 内的连续可微函数并且当 $(x_0, y_0, z_0) \in D$ 时, $F'(x_0, y_0, z_0) \neq \mathbf{0}$. 证明: 曲面 $S$ 在 $(x_0, y_0, z_0)$ 处的切平面上过 $(x_0, y_0, z_0)$ 的任何一条直线都是曲面上某光滑曲线的切线.
