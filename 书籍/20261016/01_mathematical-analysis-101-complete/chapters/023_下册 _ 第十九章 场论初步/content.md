# 下册 / 第十九章 场论初步

原始 PDF 第 738–751 页。

## 第十九章

## 场论初步

---

98

第十九章 场论初步

我们知道, 物理量大都可以表示为标量 (数量) 或矢量 (向量). 空间中分布的某种物理量在数学上可以表示为标量场 (函数) 或矢量场 (向量场). 例如, 物质的密度函数是标量场, 电场、磁场、重力场都是向量场. 在这一章里, 我们用数学方法讨论场的一些基本性质.

## 19.1 梯度场和保守场

物理中的向量场在数学中就是向量值函数. 为了直观地表示向量场的分布情况, 我们引进向量线的概念. 如果一条曲线 $\sigma$ 在每一点处的切线方向正好与向量场 $X$ 在该点的向量的方向重合, 则称 $\sigma$ 为向量场 $X$ 的向量线. 例如, 静电场的电力线和磁场的磁力线都是向量线.

设 $U$ 为 $\mathbb{R}^n$ 中的开集, $f$ 为定义在 $U$ 上的函数. 如果 $f$ 在 $U$ 上处处可微, 则可以得到 $U$ 上的向量场

$$
\nabla f: U \to \mathbb {R} ^ {n}, \boldsymbol {p} \mapsto \nabla f (\boldsymbol {p}), \forall \boldsymbol {p} \in U.
$$

$\nabla f$  称为 f 的梯度场, 也记为 gradf.

设 $c$ 为一个任意给定的常数, 考虑 $\mathbb{R}^n$ 的子集

$$
\{f = c \} = \{\boldsymbol {x} \in \mathbb {R} ^ {n} \mid f (\boldsymbol {x}) = c \},
$$

称为 $f$ 的一个等值面 $(n = 2$ 时常称为等值线). 若 $f$ 为 $C^1$ 函数且 $\nabla f$ 在等值面上的某一点 $\pmb{p}$ 处不等于零, 则由隐函数定理可知等值面在这一点附近可以表示为参数曲面, 且 $\nabla f(\pmb{p})$ 是该曲面在 $\pmb{p}$ 处的一个法向量. 一般来说梯度场的向量线垂直地穿越等值面.

设 $X$ 为向量场, 如果 $X$ 等于某个函数的梯度场, 则称 $X$ 为有势场, 该函数称为 $X$ 的一个势函数.

命题 19.1.1 设 X 为连续的有势场,  $\sigma$  为分段  $C^{1}$  的连续曲线, 则 X 沿  $\sigma$  的第二型曲线积分只与  $\sigma$  的起始位置和终点位置有关.

证明 取 $\sigma$ 的参数表示 $\sigma = \sigma(t)$, 其中 $t \in [\alpha, \beta]$. 设 $f$ 为 $\pmb{X}$ 的一个势函数, 则

$$
\begin{array}{l} \int_ {\sigma} \boldsymbol {X} \cdot \mathrm{d} \vec {s} = \int_ {\alpha} ^ {\beta} \nabla f (\sigma (t)) \cdot \sigma^ {\prime} (t) \mathrm{d} t \\ = \int_ {\alpha} ^ {\beta} (f \circ \sigma) ^ {\prime} (t) \mathrm{d} t = f (\sigma (\beta)) - f (\sigma (a)), \\ \end{array}
$$

其中我们用到了链式法则和 Newton-Leibniz 公式.

一般地, 若向量场沿曲线的第二型曲线积分只与曲线的两个端点有关, 而与曲线的具体形状无关, 则称这种向量场为保守场.

---

19.1 梯度场和保守场

99

命题 19.1.2 设 X 是定义在区域 D 上的连续向量场, 则 X 为保守场当且仅当它是有势场.

证明 命题19.1.1已经证明了充分性. 下面我们来看必要性, 以 $D \subseteq \mathbb{R}^2$ 为例, 固定一点 $\pmb{p}_0 \in D$. 由例14.5.5可知, 当 $(x, y) \in D$ 时, 在 $D$ 中存在连接 $\pmb{p}_0$ 和 $(x, y)$ 的分段 $C^1$ 的道路 $\sigma$. 定义

$$
\phi (x, y) = \int_ {\sigma} \boldsymbol {X} \cdot \mathrm{d} \vec {s}.
$$

由 $X$ 为保守场可知 $\phi$ 的定义与 $\sigma$ 的选取无关. 我们要说明 $X = \nabla \phi$. 记 $X = (P, Q)$. 设 $(x_0, y_0) \in D$, $\sigma$ 是连接 $p_0$ 和 $(x_0, y_0)$ 的道路. 当 $(x, y_0)$ 在 $(x_0, y_0)$ 附近时, 以直线段 $\tau$ 连接 $(x_0, y_0)$ 和 $(x, y_0)$, 则

$$
\phi (x, y _ {0}) = \int_ {\sigma \cup \tau} \boldsymbol {X} \cdot \mathrm{d} \vec {s} = \phi (x _ {0}, y _ {0}) + \int_ {(x _ {0}, y _ {0})} ^ {(x, y _ {0})} P \mathrm{d} x + Q \mathrm{d} y = \phi (x _ {0}, y _ {0}) + \int_ {x _ {0}} ^ {x} P (t, y _ {0}) \mathrm{d} t.
$$

由微积分基本定理可得 $\frac{\partial\phi}{\partial x} (x_0,y_0) = P(x_0,y_0)$ .同理可证 $\frac{\partial\phi}{\partial y} = Q,$ 因此 $\nabla \phi = \pmb {X}$ □

设 $X = (P, Q)$ 是平面区域 $D$ 上的 $C^1$ 向量场. 若 $X$ 为保守场, 则存在势函数 $\phi$, 此时

$$
Q _ {x} = \phi_ {y x} = \phi_ {x y} = P _ {y}.
$$

反之, 若 $Q_{x} = P_{y}$, 则 $\pmb{X}$ 未必是保守场. 事实上, 在 $\mathbb{R}^2 \setminus \{\mathbf{0}\}$ 上定义的向量场 $\pmb{X}(x, y) = \left(\frac{-y}{x^2 + y^2}, \frac{x}{x^2 + y^2}\right)$ 就是如此. 为了得到正面的结果, 我们引进单连通区域的概念.

设 $D$ 为 $\mathbb{R}^n$ 上的区域, 如果 $D$ 中任何连续闭曲线都可以在 $D$ 中连续地缩成一点, 则称 $D$ 为单连通区域. 换句话说, 如果从单位圆周 $S^1$ 到 $D$ 的连续映射均可以连续地延拓到单位圆盘上, 则称 $D$ 为单连通区域. 等价地说, 如果从矩形的边界到 $D$ 的连续映射均可以连续地延拓到整个矩形上, 则称 $D$ 为单连通区域.

定理 19.1.3 设 D 为  $R^{2}$  上的单连通区域,  $\boldsymbol{X} = (P, Q)$  为 D 上的  $C^{1}$  向量场. 如果  $Q_{x} = P_{y}$ ，则 X 为保守场.

证明 我们模仿上述命题的证明. 固定一点 $p_0 \in D$. 由例14.5.5可知, 当 $(x, y) \in D$ 时, 在 $D$ 中存在连接 $p_0$ 和 $(x, y)$ 的折线段 $\sigma$. 定义

$$
\phi (x, y) = \int_ {\sigma} \boldsymbol {X} \cdot \mathrm{d} \vec {s}.
$$

我们要说明 $\phi (x,y)$ 与道路 $\sigma$ 的选取无关，这样的话由上述命题的证明就可知 $\nabla \phi = X$

设 $\tau$ 是 $D$ 中连接 $\pmb{p}_0$ 和 $(x,y)$ 的另一折线段.由题设可知，存在连续映射 $\psi :[0,1]^2\to D,$ 使得 $\psi (0,\cdot) = \sigma ,\psi (1,\cdot) = \tau$ 且

$$
\psi (\cdot , 0) \equiv p _ {0}, \quad \psi (\cdot , 1) \equiv (x, y).
$$

---

100

第十九章 场论初步

我们要将 $\psi$ 改造成分片光滑的连续映射，从而便于应用Green公式.

由 $\psi ([0,1]^2)$ 为 $D$ 中的有界闭集可知，存在 $\delta >0$ ，使得

$$
\left\{\boldsymbol {u} \in \mathbb {R} ^ {2} \mid d (\boldsymbol {u}, \psi ([ 0, 1 ] ^ {2})) \leqslant \delta \right\} \subset D. \tag {19.1.1}
$$

由 $\psi$ 的一致连续性还可以知道, 当 $m$ 为充分大的正整数时, 每一个 $\psi(I_{ij})$ 的直径均小于 $\delta$, 其中

$$
I _ {i j} = [ s _ {i}, s _ {i + 1} ] \times [ t _ {j}, t _ {j + 1} ], s _ {i} = \frac {i}{m}, t _ {j} = \frac {j}{m}, i, j = 0, 1, \dots , m - 1.
$$

不妨设 $\sigma$ 和 $\tau$ 在每一个小区间 $[t_j, t_{j+1}]$ 上均为直线段. 记 $\pmb{v}_{i,j} = \psi(s_i, t_j)$, 当 $(s, t) \in I_{ij}$ ($0 \leqslant i, j \leqslant m-1$) 时, 令

$$
\begin{array}{l} \varphi (s, t) = m ^ {2} \left(s _ {i + 1} - s\right) \left(t _ {j + 1} - t\right) \boldsymbol {v} _ {i, j} + m ^ {2} \left(s _ {i + 1} - s\right) \left(t - t _ {j}\right) \boldsymbol {v} _ {i, j + 1} + \\ m ^ {2} (s - s _ {i}) \left(t _ {j + 1} - t\right) \boldsymbol {v} _ {i + 1, j} + m ^ {2} (s - s _ {i}) \left(t - t _ {j}\right) \boldsymbol {v} _ {i + 1, j + 1}, \\ \end{array}
$$

这样可以得到一个连续映射 $\varphi :[0,1]^2\to \mathbb{R}^2$ .利用(19.1.1)式容易验证 $\varphi ([0,1]^2)\subset D.$ 注意到 $\varphi (\cdot ,0)\equiv p_0,\varphi (\cdot ,1) = (x,y)$ 且

$$
\varphi (s _ {i}, t _ {j}) = \boldsymbol {v} _ {i, j} = \psi (s _ {i}, t _ {j}), \forall 0 \leqslant i, j \leqslant m.
$$

特别地, $\varphi(0,\cdot)=\sigma,\varphi(1,\cdot)=\tau$.

记 $\omega = P\mathrm{d}x + Q\mathrm{d}y$ ，由题设可知 $\mathrm{d}\omega = 0$ .在每一个小矩形 $I_{ij}$ 上 $\varphi$ 均为光滑映射，且

$$
\mathrm{d} (\varphi^ {*} \omega) = \varphi^ {*} (\mathrm{d} \omega) = 0.
$$

由Green公式可知

$$
\int_ {\partial I _ {i j}} \varphi^ {*} \omega = 0, \forall 0 \leqslant i, j \leqslant m - 1,
$$

其中 $\partial I_{ij}$ 均取逆时针方向. 在两个相邻小矩形的公共边上, 两个第二型积分相互抵消了, 于是有

$$
\int_ {\partial [ 0, 1 ] ^ {2}} \varphi^ {*} \omega = \sum_ {0 \leqslant i, j \leqslant m - 1} \int_ {\partial I _ {i j}} \varphi^ {*} \omega = 0.
$$

由 $\varphi^{*}\omega$ 在 $[0,1]\times \{0\}$ 和 $[0,1]\times \{1\}$ 上为零以及 $\varphi (0,\cdot) = \sigma ,\varphi (1,\cdot) = \tau$ 即可得到

$$
\int_ {\tau} \omega - \int_ {\sigma} \omega = \int_ {\partial [ 0, 1 ] ^ {2}} \varphi^ {*} \omega = 0,
$$

这就得到了欲证结论.

一个自然的问题就是: 已知 $Q_{x} = P_{y}$, 如何求出势函数 $\phi$? 根据上述定理的证明, 我们可以使用积分法, 即沿适当的路径对 $\pmb{X}$ 进行积分从而求出一个势函数. 我们也可以通过解方程组 $\phi_{x} = P, \phi_{y} = Q$ 去求出 $\phi$.

---

19.1 梯度场和保守场

101

例 19.1.1 验证  $\boldsymbol{X}=(3x^{2}-6xy,3y^{2}-3x^{2})$  是  $R^{2}$  上的有势场，并求其势函数.

解 任给 $(x,y)\in \mathbb{R}^2$ ，考虑 $X$ 沿折线 $(0,0) - - -(x,0) - - -(x,y)$ 的积分.注意在第一段上 $y = 0$ ，在第二段上 $x$ 不变，因此

$$
\phi (x, y) = \int_ {(0, 0)} ^ {(x, 0)} (3 x ^ {2} - 0) \mathrm{d} x + \int_ {(x, 0)} ^ {(x, y)} (3 y ^ {2} - 3 x ^ {2}) \mathrm{d} y = x ^ {3} + y ^ {3} - 3 x ^ {2} y.
$$

容易验证这是 $X$ 的一个势函数. 一般的势函数可以写成

$$
u (x, y) = x ^ {3} + y ^ {3} - 3 x ^ {2} y + C,
$$

其中 C 是任意常数.

我们还可以使用凑全微分法去寻找势函数. 注意到 $\nabla \phi = (P, Q)$ 可以改写为

$$
\mathrm{d} \phi = P \mathrm{d} x + Q \mathrm{d} y.
$$

即若能将上式右边的微分形式凑成全微分, 也就可以得到一个势函数.

一般地, 设 $D$ 为 $\mathbb{R}^n$ 上的区域, $\pmb{X}$ 是 $D$ 上的向量场, 记为

$$
\boldsymbol {X} = (f _ {1}, f _ {2}, \dots , f _ {n}) = \sum_ {i = 1} ^ {n} f _ {i} \boldsymbol {e} _ {i},
$$

其中 $\{e_i\}_{i=1}^n$ 为 $\mathbb{R}^n$ 的标准正交基. 定义

$$
X ^ {\flat} = \sum_ {i = 1} ^ {n} f _ {i} \mathrm{d} x _ {i},
$$

称为 $X$ 的对偶1-形式. 例如, 若 $X = \nabla \phi$, 则 $X^{\flat} = \mathrm{d}\phi$. 如果 $X = \nabla \phi$ 为 $C^1$ 的保守场, 则

$$
\mathrm{d} \boldsymbol {X} ^ {\flat} = \mathrm{d} ^ {2} \phi = 0,
$$

即 $X^{\flat}$ 是闭形式. 若 $D$ 为单连通区域, 则用上述定理的证明方法可以证明 $H_{dR}^{1}(D) = \{0\}$, 即闭的 1-形式一定是恰当形式. 这说明在单连通区域上的向量场 $X$ 为保守场当且仅当 $X^{\flat}$ 为闭形式.

## 习题 19.1

1. 在  $R^{n}$  上记  $r = \|x\|$ ，计算  $\nabla r$  和  $\nabla r^{2}$ .

2. 设 f, g 为可微函数,  $\lambda, \mu$  为常数, 证明:

$$
\nabla (\lambda f + \mu g) = \lambda \nabla f + \mu \nabla g, \nabla (f g) = f \nabla g + g \nabla f.
$$

3. 设 $f$ 为可微函数, $\phi$ 为一元可微函数, 证明: $\nabla (\phi (f)) = \phi'(f)\nabla f$.

---

102

第十九章 场论初步

4. 设 $f, g$ 为可微函数, $g \neq 0$, 证明: $\nabla \left(\frac{f}{g}\right) = g^{-2}(g\nabla f - f\nabla g)$.

5. 验证 $X = (2x\cos y - y^2\sin x, 2y\cos x - x^2\sin y)$ 为 $\mathbb{R}^2$ 上的有势场, 并求其势函数.

6. 求函数 $\phi$, 使得 $\mathrm{d}\phi = (4x^3y^3 - 3y^2 + 5)\mathrm{d}x + (3x^4y^2 - 6xy - 4)\mathrm{d}y$.

7. 设 $X = (yz(2x + y + z), xz(x + 2y + z), xy(x + y + 2z))$，验证 $X$ 是 $\mathbb{R}^3$ 上的有势场，并求其势函数。

8. 验证下列积分与路径无关, 并计算其值:

(1) $\int_{\sigma}(x^2 - 2yz)\mathrm{d}x + (y^2 - 2zx)\mathrm{d}y + (z^2 - 2xy)\mathrm{d}z,$ 其中 $\sigma$ 是从 $(0,0,0)$ 到 $(a,b,c)$ 的曲线；

(2) $\int_{\sigma} \frac{x \, \mathrm{d}x + y \, \mathrm{d}y + z \, \mathrm{d}z}{\sqrt{x^2 + y^2 + z^2}}$, 其中 $\sigma$ 是 $\mathbb{R}^3 \setminus \{(0,0,0)\}$ 中从球面 $x^2 + y^2 + z^2 = 1$ 上一点到球面 $x^2 + y^2 + z^2 = 2$ 上一点的曲线.

9. 设 $\Omega$ 为 $\mathbb{R}^n$ 上的区域, $p_0 \in \Omega$, $f$ 为 $\Omega$ 上的 $C^1$ 函数, 证明:

$$
\nabla f (\boldsymbol {p} _ {0}) = \lim _ {r \to 0 ^ {+}} \frac {1}{\nu (B _ {r} (\boldsymbol {p} _ {0}))} \int_ {\partial B _ {r} (\boldsymbol {p} _ {0})} f   \mathrm{d} \vec {\sigma},
$$

其中  $d\vec{\sigma}=n\,d\sigma,\quad n$  为单位外法向量.

10. 设  $\{x_{i}\}_{i=1}^{n}$  为  $R^{n}$  上的直角坐标系, 考虑坐标变换  $\boldsymbol{x} = \varphi(\boldsymbol{u})$ , 其中  $\boldsymbol{u} = (u_{1}, u_{2}, \cdots, u_{n})$ . 设 f 为可微函数, 证明: 在坐标系  $\{u_{i}\}_{i=1}^{n}$  中梯度场  $\nabla f$  可以表示为

$$
\nabla f = \sum_ {i = 1} ^ {n} \frac {\partial f}{\partial u _ {i}} \nabla u _ {i}.
$$

## 19.2 散度和 Laplace 算子

我们首先回顾散度的定义. 设 U 为  $R^{n}$  中的开集,  $\boldsymbol{X} = (f_{1}, f_{2}, \cdots, f_{n})$  是 U 上的  $C^{1}$  向量场, 其散度  $\mathrm{div}(\boldsymbol{X})$  是 U 上的标量场, 在标准直角坐标系中的计算公式为

$$
\operatorname{div} (\boldsymbol {X}) = \sum_ {i = 1} ^ {n} \frac {\partial f _ {i}}{\partial x _ {i}}.
$$

在物理中, 散度也称为通量密度, 它是不依赖于直角坐标系的量.

将梯度和散度结合起来可以得到重要的 Laplace $^{①}$ 算子. 设 U 为 $R^{n}$ 中的开集, f

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">① Laplace, Pierre-Simon, marquis de, 1749 年 3 月 23 日—1827 年 3 月 5 日, 法国数学家、天文学家.</span></small>

---

19.2 散度和 Laplace 算子

103

是 U 上的  $C^{2}$  函数 (标量场), f 的 Laplace 定义为

$$
\Delta f = \mathrm{div} (\nabla f).
$$

$\Delta$ 称为作用在标量场上的Laplace算子.在直角坐标系 $\{x_{i}\}_{i = 1}^{n}$ 中，显然有

$$
\Delta f = \sum_ {i = 1} ^ {n} \frac {\partial^ {2} f}{\partial x _ {i} ^ {2}}.
$$

如果  $\Delta f = 0$ ，则称 f 为 U 上的调和函数。

例如, 记 $r = \| \boldsymbol{x} \|$, 则当 $n = 2$ 时 $\ln r$ 是 $\mathbb{R}^2 \setminus \{\mathbf{0}\}$ 上的调和函数; $n \geqslant 3$ 时 $r^{2-n}$ 是 $\mathbb{R}^n \setminus \{\mathbf{0}\}$ 上的调和函数. 调和函数具有很多特别的性质, 我们用散度定理来给出所谓的平均值公式.

定理 19.2.1 (平均值公式) 设 f 为 U 上的调和函数, 如果  $\overline{B_{R}(x^{0})} \subset U$ , 则

$$
f (\pmb {x} ^ {0}) = \frac {1}{\nu (B _ {R} (\pmb {x} ^ {0}))} \int_ {B _ {R} (\pmb {x} ^ {0})} f (\pmb {x}) \mathrm{d} \pmb {x}.
$$

证明 不妨设 $x^0 = 0$. 当 $x \in B_R = B_R(0)$ 时, 利用 Newton-Leibniz 公式可得

$$
f (\boldsymbol {x}) - f (\boldsymbol {0}) = \int_ {0} ^ {1} \frac {\mathrm{d}}{\mathrm{d} t} f (t \boldsymbol {x}) \mathrm{d} t = \int_ {0} ^ {1} \nabla f (t \boldsymbol {x}) \cdot \boldsymbol {x} \mathrm{d} t.
$$

积分, 利用散度定理可得

$$
\begin{array}{l} \int_ {B _ {R}} f (\boldsymbol {x}) \mathrm{d} \boldsymbol {x} - \nu (B _ {R}) f (\boldsymbol {0}) \\ = \int_ {0} ^ {1} \mathrm{d} t \int_ {B _ {R}} \nabla f (t \boldsymbol {x}) \cdot \boldsymbol {x} \mathrm{d} \boldsymbol {x} \\ = \int_ {0} ^ {1} \mathrm{d} t \int_ {B _ {R}} \operatorname{div} \left[ \frac {\| \boldsymbol {x} \| ^ {2}}{2} \nabla f (t \boldsymbol {x}) \right] \mathrm{d} \boldsymbol {x} - \int_ {0} ^ {1} \mathrm{d} t \int_ {B _ {R}} \frac {\| \boldsymbol {x} \| ^ {2}}{2} t \Delta f (t \boldsymbol {x}) \mathrm{d} \boldsymbol {x} \\ = \int_ {0} ^ {1} \mathrm{d} t \frac {R ^ {2}}{2} \int_ {\partial B _ {R}} \nabla f (t \boldsymbol {x}) \cdot \boldsymbol {n} \mathrm{d} \sigma \\ = \int_ {0} ^ {1} \mathrm{d} t \frac {R ^ {2}}{2} \int_ {B _ {R}} t \Delta f (t \boldsymbol {x}) \mathrm{d} \boldsymbol {x} = 0, \\ \end{array}
$$

定理证毕.

推论 19.2.2 (Liouville 定理) 设 f 为  $R^{n}$  上的调和函数. 如果  $f \geqslant 0$ , 则 f 必为常值函数. 特别地,  $R^{n}$  上的有界调和函数必为常值函数.

证明 任取 $\pmb{p},\pmb{q}\in \mathbb{R}^n$ ，记 $d = \| \pmb {-}\pmb {q}\|$ .当 $R > 0$ 时，由三角不等式可知 $B_{R}(\pmb {p})\subseteq$ $B_{R + d}(\pmb {q})$ .由平均值不等式以及 $f\geqslant 0$ 可得

$$
f (\boldsymbol {p}) = \frac {1}{\nu (B _ {R} (\boldsymbol {p}))} \int_ {B _ {R} (\boldsymbol {p})} f (\boldsymbol {x}) \mathrm{d} \boldsymbol {x} \leqslant \frac {1}{\nu (B _ {R} (\boldsymbol {p}))} \int_ {B _ {R + d} (\boldsymbol {q})} f (\boldsymbol {x}) \mathrm{d} \boldsymbol {x}
$$

---

104

第十九章 场论初步

$$
= \frac {\nu (B _ {R + d} (\boldsymbol {q}))}{\nu (B _ {R} (\boldsymbol {p}))} f (\boldsymbol {q}) = \left(1 + \frac {d}{R}\right) ^ {n} f (\boldsymbol {q}).
$$

令 $R \to +\infty$ 可得 $f(\pmb{p}) \leqslant f(\pmb{q})$. 交换 $\pmb{p}, \pmb{q}$ 的位置可知 $f(\pmb{q}) \leqslant f(\pmb{p})$, 这说明 $f(\pmb{p}) = f(\pmb{q})$, 因此 $f$ 为常值函数. □

在实际应用中, 我们经常根据需要在空间中选取曲线坐标系. 下面我们来推导曲线坐标系中散度的计算公式. 我们首先利用微分形式重新表述散度: 设 X 如上, 记

$$
\omega = \sum_ {i = 1} ^ {n} (- 1) ^ {i - 1} f _ {i}   \mathrm{d} x _ {1} \wedge \dots \wedge \widehat {\mathrm{d} x _ {i}} \wedge \dots \wedge \mathrm{d} x _ {n},
$$

它是 $U$ 上的 $(n - 1)$-形式, 求外微分可得

$$
\begin{array}{l} \mathrm{d} \omega = \sum_ {i = 1} ^ {n} (- 1) ^ {i - 1} \mathrm{d} f _ {i} \wedge \mathrm{d} x _ {1} \wedge \dots \wedge \widehat {\mathrm{d} x _ {i}} \wedge \dots \wedge \mathrm{d} x _ {n} \\ = \sum_ {i = 1} ^ {n} (- 1) ^ {i - 1} \sum_ {j = 1} ^ {n} \frac {\partial f _ {i}}{\partial x _ {j}} \mathrm{d} x _ {j} \wedge \mathrm{d} x _ {1} \wedge \dots \wedge \widehat {\mathrm{d} x _ {i}} \wedge \dots \wedge \mathrm{d} x _ {n} \\ = \sum_ {i = 1} ^ {n} (- 1) ^ {i - 1} \frac {\partial f _ {i}}{\partial x _ {i}} \mathrm{d} x _ {i} \wedge \mathrm{d} x _ {1} \wedge \dots \wedge \widehat {\mathrm{d} x _ {i}} \wedge \dots \wedge \mathrm{d} x _ {n} \\ = \sum_ {i = 1} ^ {n} \frac {\partial f _ {i}}{\partial x _ {i}} \mathrm{d} x _ {1} \wedge \dots \wedge \mathrm{d} x _ {n} = \operatorname{div} (\boldsymbol {X}) \mathrm{d} \boldsymbol {x}. \\ \end{array}
$$

考虑坐标变换 $x = \varphi(u)$, 其中 $\varphi: D \to U$ 为 $C^2$ 映射, $D$ 为 $\mathbb{R}^n$ 中的开集. 我们要求 $\det J\varphi$ 在 $D$ 上处处非零. 记

$$
\varphi (\boldsymbol {u}) = (\varphi_ {1} (\boldsymbol {u}), \dots , \varphi_ {n} (\boldsymbol {u})), \quad \boldsymbol {u} = (u _ {1}, \dots , u _ {n}) \in D.
$$

利用拉回映射可得

$$
\begin{array}{l} \varphi^ {*} \omega = \sum_ {i = 1} ^ {n} (- 1) ^ {i - 1} f _ {i} (\varphi) \mathrm{d} \varphi_ {1} \wedge \dots \wedge \widehat {\mathrm{d} \varphi_ {i}} \wedge \dots \wedge \mathrm{d} \varphi_ {n} \\ = \sum_ {i, j = 1} ^ {n} (- 1) ^ {i - 1} f _ {i} (\varphi) \frac {\partial \left(\varphi_ {1} \cdots \widehat {\varphi_ {i}} \cdots \varphi_ {n}\right)}{\partial \left(u _ {1} \cdots \widehat {u _ {j}} \cdots u _ {n}\right)} \mathrm{d} u _ {1} \wedge \dots \widehat {\mathrm{d} u _ {j}} \wedge \dots \wedge \mathrm{d} u _ {n} \\ = \sum_ {i, j = 1} ^ {n} (- 1) ^ {j - 1} f _ {i} (\varphi) \varphi_ {i j} \mathrm{d} u _ {1} \wedge \dots \widehat {\mathrm{d} u _ {j}} \wedge \dots \wedge \mathrm{d} u _ {n}, \\ \end{array}
$$

其中

$$
\varphi_ {i j} = (- 1) ^ {i + j} \frac {\partial (\varphi_ {1} \cdots \widehat {\varphi_ {i}} \cdots \varphi_ {n})}{\partial (u _ {1} \cdots \widehat {u _ {j}} \cdots u _ {n})},
$$

它是 Jacobi 矩阵 $J\varphi$ 在 $(i,j)$ 位置的代数余子式. 求外微分可得

$$
\mathrm{d} (\varphi^ {*} \omega) = \sum_ {i, j = 1} ^ {n} \frac {\partial}{\partial u _ {j}} \left[ f _ {i} (\varphi) \varphi_ {i j} \right] \mathrm{d} u _ {1} \wedge \dots \wedge \mathrm{d} u _ {n}.
$$

---

19.2 散度和Laplace算子

105

另一方面, 根据拉回映射与外微分运算可以交换次序可得

$$
\begin{array}{l} \mathrm{d} \left(\varphi^ {*} \omega\right) = \varphi^ {*} (\mathrm{d} \omega) = \varphi^ {*} (\operatorname{div} (\boldsymbol {X}) \mathrm{d} \boldsymbol {x}) \\ = \operatorname{div} (\boldsymbol {X}) (\varphi) \mathrm{d} \varphi_ {1} \wedge \dots \wedge \mathrm{d} \varphi_ {n} \\ = \operatorname{div} (\boldsymbol {X}) (\varphi) \det J \varphi \mathrm{d} u _ {1} \wedge \dots \wedge \mathrm{d} u _ {n}, \\ \end{array}
$$

这说明

$$
\operatorname{div} (\boldsymbol {X}) (\varphi) = \frac {1}{\det J \varphi} \sum_ {i, j = 1} ^ {n} \frac {\partial}{\partial u _ {j}} \left[ f _ {i} (\varphi) \varphi_ {i j} \right]. \tag {19.2.1}
$$

下面我们考虑一种常用的曲线坐标系. 若 $(J\varphi)^{\mathrm{T}}$ 的行向量 $\{\varphi_{u_j}\}_{j=1}^n$ 互相垂直, 则称 $\{u_i\}_{i=1}^n$ 为正交曲线坐标系. 此时

$$
(J \varphi) ^ {\mathrm{T}} J \varphi = \operatorname{diag} \left(h _ {1} ^ {2}, \dots , h _ {n} ^ {2}\right), \tag {19.2.2}
$$

其中

$$
h _ {j} = \| \varphi_ {u _ {j}} \|, j = 1, 2, \dots , n,
$$

$\{h_j\}_{j=1}^n$ 称为坐标系的 $\mathrm{Lamé}^{\text{①}}$ 系数. 由 (19.2.2) 式可知

$$
(J \varphi) ^ {- 1} = \mathrm{diag} \big (h _ {1} ^ {- 2}, \dots , h _ {n} ^ {- 2} \big) (J \varphi) ^ {\mathrm{T}}.
$$

另一方面, 在线性代数中我们知道 $(J\varphi)^{-1} = (\det J\varphi)^{-1}(J\varphi)^*$, 其中 $(J\varphi)^*$ 在 $(i,j)$ 位置的元素等于 $\varphi_{ji}$, 这说明

$$
\varphi_ {i j} = \frac {\det J \varphi}{h _ {j} ^ {2}} \frac {\partial \varphi_ {i}}{\partial u _ {j}}.
$$

代入 (19.2.1) 式可得

$$
\mathrm{div} (\boldsymbol {X}) (\varphi) = \frac {1}{\det J \varphi} \sum_ {j = 1} ^ {n} \frac {\partial}{\partial u _ {j}} \big [ X _ {j} \det J \varphi \big ],
$$

其中

$$
X _ {j} = \frac {1}{h _ {j} ^ {2}} \sum_ {i = 1} ^ {n} f _ {i} (\varphi) \frac {\partial \varphi_ {i}}{\partial u _ {j}}.
$$

注意到  $\det J\varphi = \pm h_{1} \cdots h_{n}$ ，因此也有

$$
\operatorname{div} (\boldsymbol {X}) (\varphi) = \frac {1}{h _ {1} \cdots h _ {n}} \sum_ {j = 1} ^ {n} \frac {\partial}{\partial u _ {j}} \left[ X _ {j} h _ {1} \dots h _ {n} \right]. \tag {19.2.3}
$$

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">① Lamé, Gabriel, 1795 年 7 月 22 日—1870 年 5 月 1 日, 法国数学家.</span></small>

---

106

第十九章 场论初步

我们断言: 在正交曲线坐标系中 $X$ 可以表示为

$$
\boldsymbol {X} (\varphi) = \sum_ {j = 1} ^ {n} X _ {j} \varphi_ {u _ {j}}. \tag {19.2.4}
$$

事实上，记

$$
\hat {e} _ {j} = \frac {1}{h _ {j}} \varphi_ {u _ {j}}, j = 1, \dots , n,
$$

则 $\{\hat{e}_j\}_{j = 1}^n$ 为标准正交基.由链式法则可得

$$
\boldsymbol {X} (\varphi) \cdot \hat {\boldsymbol {e}} _ {j} = \frac {1}{h _ {j}} \sum_ {i = 1} ^ {n} f _ {i} (\varphi) \boldsymbol {e} _ {i} \cdot \varphi_ {u _ {j}} = \frac {1}{h _ {j}} \sum_ {i = 1} ^ {n} f _ {i} (\varphi) \frac {\partial \varphi_ {i}}{\partial u _ {j}} = h _ {j} X _ {j},
$$

于是

$$
\boldsymbol {X} (\varphi) = \sum_ {j = 1} ^ {n} \big [ \boldsymbol {X} (\varphi) \cdot \hat {\boldsymbol {e}} _ {j} \big ] \hat {\boldsymbol {e}} _ {j} = \sum_ {j = 1} ^ {n} X _ {j} \varphi_ {u _ {j}}.
$$

在正交曲线坐标系中, 我们有

$$
\begin{array}{l} \nabla f (\varphi) = \sum_ {j = 1} ^ {n} \left[ \nabla f (\varphi) \cdot \hat {\boldsymbol {e}} _ {j} \right] \hat {\boldsymbol {e}} _ {j} = \sum_ {j = 1} ^ {n} \frac {1}{h _ {j} ^ {2}} [ \nabla f (\varphi) \cdot \varphi_ {u _ {j}} ] \varphi_ {u _ {j}} \\ = \sum_ {j = 1} ^ {n} \frac {1}{h _ {j} ^ {2}} \frac {\partial f (\varphi)}{\partial u _ {j}} \varphi_ {u _ {j}}. \\ \end{array}
$$

由(19.2.3)式可得

$$
\Delta f (\varphi) = \frac {1}{h _ {1} \cdots h _ {n}} \sum_ {j = 1} ^ {n} \frac {\partial}{\partial u _ {j}} \left[ \frac {h _ {1} \cdots h _ {n}}{h _ {j} ^ {2}} \frac {\partial f (\varphi)}{\partial u _ {j}} \right]. \tag {19.2.5}
$$

这就得到了 Laplace 算子在正交曲线坐标下的表达式.

例 19.2.1 求梯度和 Laplace 算子在平面极坐标下的表达式.

解 平面直角坐标 $(x,y)$ 和极坐标 $(r,\theta)$ 之间的变换关系为

$$
(x, y) = \varphi (r, \theta) = (r \cos \theta , r \sin \theta).
$$

求导可得

$$
\varphi_ {r} = (\cos \theta , \sin \theta), \varphi_ {\theta} = (- r \sin \theta , r \cos \theta).
$$

由此可见极坐标是正交曲线坐标. 其 Lamé 系数为

$$
h _ {1} = \| \varphi_ {r} \| = 1, h _ {2} = \| \varphi_ {\theta} \| = r,
$$

其中设 $f = f(x,y)$ 为平面上的 $C^2$ 函数，其梯度在极坐标中可以表示为

$$
\nabla f = \frac {\partial f}{\partial r} \varphi_ {r} + \frac {1}{r ^ {2}} \frac {\partial f}{\partial \theta} \varphi_ {\theta}.
$$

---

19.2 散度和 Laplace 算子

107

由(19.2.5)式可得

$$
\Delta f = \frac {1}{r} \frac {\partial}{\partial r} \left(r \frac {\partial f}{\partial f}\right) + \frac {1}{r ^ {2}} \frac {\partial^ {2} f}{\partial \theta^ {2}}.
$$

这是平面 Laplace 算子在极坐标下的表达式.

## 习题 19.2

1. 求向量场 $X = (y, zx, xy)$ 通过方体 $[-1, 1]^3$ 的表面的通量, 其中方体表面的方向为外侧.

2. 求向量场 $X = (x^{2}, y^{2}, z^{2})$ 通过球面 $x^{2} + y^{2} + z^{2} = 1, x > 0, y > 0, z > 0$ 的部分的通量, 其中球面的方向为外侧.

3. 求引力场  $F = \kappa r^{-3} r$  的散度, 其中  $\kappa$  为常数,  $\boldsymbol{r} = (x, y, z)$ ,  $r = \sqrt{x^{2} + y^{2} + z^{2}}$ .

4. 求电场  $E = \kappa r^{-3} r$  穿过围绕  $R^{3}$  的坐标原点的任一光滑封闭曲面的电通量, 其中  $\kappa$  为常数.

5. 在  $R^{n}$  上记  $\boldsymbol{r} = (x_{1}, x_{2}, \cdots, x_{n})$ ，求  $\mathrm{div}(\boldsymbol{r})$  和  $\mathrm{div}(r^{-1}\boldsymbol{r})$ .

6. 设 f 为  $C^{1}$  函数, X 为  $C^{1}$  向量场, 证明:

$$
\mathrm{div} (f \boldsymbol {X}) = f \mathrm{div} (\boldsymbol {X}) + \nabla f \cdot \boldsymbol {X}.
$$

7. 验证: 当 $n = 2$ 时, $\ln r$ 是 $\mathbb{R}^2 \setminus \{\mathbf{0}\}$ 上的调和函数; 当 $n \geqslant 3$ 时, $r^{2-n}$ 是 $\mathbb{R}^n \setminus \{\mathbf{0}\}$ 上的调和函数.

8. 设 $f, g$ 为 $C^2$ 函数, 证明:

$$
\operatorname{div} (f \nabla g) = \nabla f \cdot \nabla g + f \Delta g, \Delta (f g) = f \Delta g + g \Delta f + 2 \nabla f \cdot \nabla g.
$$

9. 设 $D \subset \mathbb{R}^n$ 为具有 $C^1$ 边界的有界开集, $\pmb{n}$ 是边界上的单位外法向量. 若 $f, g \in C^2(\bar{D})$, 证明:

$$
\int_ {D} (f \Delta g - g \Delta f) \mathrm{d} x = \int_ {\partial D} \left(f \frac {\partial g}{\partial \boldsymbol {n}} - g \frac {\partial f}{\partial \boldsymbol {n}}\right) \mathrm{d} \sigma .
$$

10. 设 $D \subset \mathbb{R}^n$ 为具有 $C^1$ 边界的有界开集, $f, g \in C^2(\bar{D})$ 且均为调和函数. 若在 $\partial D$ 上 $f = g$, 证明: $f \equiv g$.

11. 设 $D \subset \mathbb{R}^n$ 为具有 $C^1$ 边界的有界区域, $f \in C^2(\bar{D})$ 且为调和函数. 证明: $f$ 在 $D$ 的内部达不到最大值或最小值, 除非 $f$ 恒为常数.

12. 设 $p(z)$ 是复平面上的多项式. 如果 $p(z)$ 没有零点, 则 $\frac{1}{p(z)}$ 的实部和虚部均为有界调和函数, 从而必为常数. 由此推出代数基本定理.

13. 在  $R^{3}$  的球坐标系和柱坐标系中求散度的计算公式.

---

108

第十九章 场论初步

## 19.3 旋度场

设 $U$ 是 $\mathbb{R}^3$ 中的开集, $\pmb{X} = (P, Q, R)$ 为 $U$ 上的 $C^1$ 向量场, 记

$$
\mathrm{rot} (\boldsymbol {X}) = (R _ {y} - Q _ {z}, P _ {z} - R _ {x}, Q _ {x} - P _ {y}),
$$

称为 $X$ 的旋度, 也记为 $\operatorname{curl}(X)$. 为了便于记忆, 上式形式上可以写为

$$
\mathrm{rot} (\boldsymbol {X}) = \nabla \times \boldsymbol {X} = \left| \begin{array}{c c c} \mathbf {i} & \mathbf {j} & \mathbf {k} \\ \partial_ {x} & \partial_ {y} & \partial_ {z} \\ P & Q & R \end{array} \right|,
$$

其中 $\{\mathbf{i},\mathbf{j},\mathbf{k}\} = \{\pmb{e}_1,\pmb{e}_2,\pmb{e}_3\}$ 是 $\mathbb{R}^3$ 的标准正交基， $\nabla = \mathrm{i}\partial_x + \mathrm{j}\partial_y + \mathrm{k}\partial_z$ 称为Hamilton算子，又称Nabla算子.

在物理中, 旋度与环流量的面密度密切相关. 设 $\sigma$ 是 $U$ 中的一条给定方向的闭曲线, 我们称第二型曲线积分

$$
\oint_ {\sigma} \boldsymbol {X} \cdot \mathrm{d} \vec {s}
$$

为向量场 $X$ 沿 $\sigma$ 的环流量. 设 $p_0 \in U, n$ 为单位向量, 以 $p_0$ 为中心, $r$ 为半径作一个垂直于 $n$ 的小圆盘 $D_r$. $D_r$ 的方向由法向量 $n$ 决定, $\partial D_r$ 的方向为诱导定向. 此时, $X$ 沿 $\partial D_r$ 的环流量与 $D_r$ 的面积的比值

$$
\frac {1}{\nu (D _ {r})} \oint_ {\partial D _ {r}} \boldsymbol {X} \cdot \mathrm{d} \vec {s}
$$

表示向量场 $X$ 绕 $\pmb{n}$ 轴旋转的环流量对面积的平均变换率. 当 $r \to 0^{+}$ 时, 此比值的极限反映了向量场 $X$ 绕 $\pmb{n}$ 轴的旋转状况. 为了计算这一极限, 利用Stokes公式和积分中值公式可得

$$
\frac {1}{\nu (D _ {r})} \oint_ {\partial D _ {r}} \boldsymbol {X} \cdot \mathrm{d} \vec {s} = \frac {1}{\nu (D _ {r})} \iint_ {D _ {r}} \mathrm{rot} (\boldsymbol {X}) \cdot \boldsymbol {n} \mathrm{d} \sigma = \mathrm{rot} (\boldsymbol {X}) (\boldsymbol {p}) \cdot \boldsymbol {n},
$$

其中 $\pmb{p} \in \overline{D_r}$. 当 $r \to 0^+$ 时, $\pmb{p} \to \pmb{p}_0$, 于是

$$
\lim _ {r \to 0 ^ {+}} \frac {1}{\nu (D _ {r})} \oint_ {\partial D _ {r}} \boldsymbol {X} \cdot \mathrm{d} \vec {s} = \mathrm{rot} (\boldsymbol {X}) (\boldsymbol {p} _ {0}) \cdot \boldsymbol {n},
$$

这是旋度  $\mathrm{rot}(X)$  在 n 上的投影.

从上述讨论可以看出, 将小圆盘换成一列收缩到  $p_{0}$  的平面小区域时类似的结论也成立. 同时也可以看出, 旋度的定义其实不依赖于直角坐标系 (但依赖于空间的定向). 下面我们在曲线正交坐标系中计算旋度场的表达式.

---

19.3 旋度场

109

引理 19.3.1 设 f 为  $C^{1}$  函数, X 为  $C^{1}$  向量场, 则

$$
\mathrm{rot} (f \boldsymbol {X}) = \nabla f \times \boldsymbol {X} + f \mathrm{rot} (\boldsymbol {X}).
$$

证明 这可以通过直接计算得到, 留作练习.

设  $\{u_{i}\}_{i=1}^{n}$  为曲线正交坐标系, 相应的坐标变换为  $\varphi = \varphi(u)$ , 我们要求  $\det J\varphi > 0$ . 在此曲线坐标系中, 设向量场 X 可以表示为

$$
X = \sum_ {i = 1} ^ {3} X _ {i} \varphi_ {u _ {i}}.
$$

由前一节关于梯度的计算公式可知  $\nabla u_{i}=h_{i}^{-2}\varphi_{u_{i}}$ ，因此有

$$
X = \sum_ {i = 1} ^ {3} X _ {i} h _ {i} ^ {2} \nabla u _ {i},
$$

其中 $\{h_i\}_{i=1}^3$ 为 Lamé 系数. 注意到 $\mathrm{rot}(\nabla u_i) = 0$, 由上述引理可得

$$
\mathrm{rot} (\boldsymbol {X}) = \sum_ {i = 1} ^ {3} \nabla (X _ {i} h _ {i} ^ {2}) \times \nabla u _ {i} = \sum_ {i, j = 1} ^ {3} \frac {\partial (X _ {i} h _ {i} ^ {2})}{\partial u _ {j}} \nabla u _ {j} \times \nabla u _ {i}.
$$

利用 $\{\nabla u_i\}_{i=1}^3$ 互相正交以及 $\det J\varphi > 0$ 不难得出

$$
\nabla u _ {1} \times \nabla u _ {2} = \lambda \varphi_ {u _ {3}}, \nabla u _ {2} \times \nabla u _ {3} = \lambda \varphi_ {u _ {1}}, \nabla u _ {3} \times \nabla u _ {1} = \lambda \varphi_ {u _ {2}},
$$

其中

$$
\lambda = h _ {1} ^ {- 2} h _ {2} ^ {- 2} h _ {3} ^ {- 2} \det J \varphi = (h _ {1} h _ {2} h _ {3}) ^ {- 1}.
$$

这说明

$$
\begin{array}{l} \mathrm{rot} (\boldsymbol {X}) = \frac {\partial_ {u _ {2}} (X _ {3} h _ {3} ^ {2}) - \partial_ {u _ {3}} (X _ {2} h _ {2} ^ {2})}{h _ {1} h _ {2} h _ {3}} \varphi_ {u _ {1}} + \frac {\partial_ {u _ {3}} (X _ {1} h _ {1} ^ {2}) - \partial_ {u _ {1}} (X _ {3} h _ {3} ^ {2})}{h _ {1} h _ {2} h _ {3}} \varphi_ {u _ {2}} + \\ \frac {\partial_ {u _ {1}} (X _ {2} h _ {2} ^ {2}) - \partial_ {u _ {2}} (X _ {1} h _ {1} ^ {2})}{h _ {1} h _ {2} h _ {3}} \varphi_ {u _ {3}}. \\ \end{array}
$$

上式形式上可以写成

$$
\mathrm{rot} (\boldsymbol {X}) = \frac {1}{h _ {1} h _ {2} h _ {3}} \left| \begin{array}{c c c} \varphi_ {u _ {1}} & \varphi_ {u _ {2}} & \varphi_ {u _ {3}} \\ \partial_ {u _ {1}} & \partial_ {u _ {2}} & \partial_ {u _ {3}} \\ X _ {1} h _ {1} ^ {2} & X _ {2} h _ {2} ^ {2} & X _ {3} h _ {3} ^ {2} \end{array} \right|.
$$

---

110

第十九章 场论初步

## 习题 19.3

1. 求下列向量场的旋度:

(1) $X=(y^{2}+z^{2},z^{2}+x^{2},x^{2}+y^{2});$

(2) $X = (2xy, \mathrm{e}^z \sin y, x^2 + y^2 + z^2)$.

2. 给出引理 19.3.1 的详细证明.

3. 设 f 为  $C^{2}$  函数, 证明:  $\mathrm{rot}(\nabla f)=0$ .

4. 设 X 为  $C^{2}$  向量场, 证明:  $\text{div}(\text{rot}(X)) = 0$ .

5. 设 $X, Y$ 为 $C^1$ 向量场, 证明: $\operatorname{div}(\boldsymbol{X} \times \boldsymbol{Y}) = \boldsymbol{Y} \cdot \operatorname{rot}(\boldsymbol{X}) - \boldsymbol{X} \cdot \operatorname{rot}(\boldsymbol{Y})$.

6. 设  $\boldsymbol{X} = (P, Q, R)$  为  $C^{2}$  向量场, 证明:

$$
\mathrm{rot} \big (\mathrm{rot} (\boldsymbol {X}) \big) = \nabla \big (\mathrm{div} (\boldsymbol {X}) \big) - \Delta \boldsymbol {X},
$$

其中  $\Delta X = (\Delta P, \Delta Q, \Delta R)$ .

7. 写出柱面坐标系和球面坐标系中旋度场的计算公式.

8. 设 $\Omega$ 为 $\mathbb{R}^3$ 上的区域, $p_0 \in \Omega$, $X$ 是定义在 $\Omega$ 上的 $C^1$ 向量场. 证明:

$$
\mathrm{rot} (\boldsymbol {X}) (\boldsymbol {p} _ {0}) = \lim _ {r \to 0 ^ {+}} \frac {1}{\nu (B _ {r} (\boldsymbol {p} _ {0}))} \int_ {\partial B _ {r} (\boldsymbol {p} _ {0})} \boldsymbol {n} \times \boldsymbol {X}   \mathrm{d} \sigma ,
$$

其中 n 表示单位外法向量场.

9. 散度为零的场称为无源场. 证明: 矩形区域中的无源场必为旋度场.

10. 旋度为零的场称为无旋场. 证明: 在单连通区域上, 无旋场必为保守场.
