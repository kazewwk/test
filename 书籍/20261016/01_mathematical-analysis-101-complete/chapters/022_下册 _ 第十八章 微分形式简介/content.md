# 下册 / 第十八章 微分形式简介

原始 PDF 第 708–737 页。

## 第十八章

## 微分形式简介

---

68

第十八章 微分形式简介

本章主要讨论曲线积分和曲面积分之间的联系, 得到重要的 Green $^{①}$  公式、Gauss $^{②}$  公式以及 Stokes $^{③}$  公式. 为了统一描述这些公式, 我们将引入微分形式这一新的研究对象, 它们是函数以及向量值函数的推广.

## 18.1 各类积分之间的联系

我们知道, 一元微积分中的 Newton-Leibniz 公式将微分和积分统一在一起, 从计算的角度来看, 它将被积区间上的函数导数的积分化成了区间边界上函数值的差 (代数和). 在多元微积分中也有类似的现象.

## 18.1.1 Gauss-Green 公式

设 $\Omega$ 是 $\mathbb{R}^n$ 中的有界开集, $X$ 是向量场 (向量值函数). 若 $X$ 在 $\bar{\Omega}$ 的某个开邻域上是 $C^1$ 的, 则记 $X \in C^1(\bar{\Omega})$. 类比于 Newton-Leibniz 公式, $X$ 沿 $\partial \Omega$ 的第二型积分应该可以化为 $X$ 的某种导数在 $\Omega$ 上的积分. 为此我们引进散度的概念.

任取 $p \in \Omega$, 当 $r > 0$ 且充分小时, $\overline{B_r(p)} \subset \Omega$. 在球面 $\partial B_r(p)$ 上取单位外法向量场 $n = \frac{1}{r} (x - p)$. 向量场 $X$ 沿该球面的第二型积分可以解释为流速为 $X$ 的流体流出球面的流量. 记

$$
\Phi (r) = \frac {1}{| B _ {r} (\boldsymbol {p}) |} \int_ {\partial B _ {r} (\boldsymbol {p})} \boldsymbol {X} \cdot \boldsymbol {n}   \mathrm{d} \sigma ,
$$

其中 $|B_r(\pmb {p})| = \omega_n r^n$ 是 $B_r(\pmb {p})$ 的容积. $\Phi (r)$ 称为平均流量(通量)密度.记 $\mathrm{div}(\mathbf{X}) =$ $\lim_{r\to 0^{+}}\varPhi (r)$ ，称为 $\pmb{X}$ 在 $\pmb{p}$ 处的流量(通量)密度或散度.我们有

引理 18.1.1 设  $X = (f_{1}, f_{2}, \cdots, f_{n})$  为  $C^{1}$  向量场，则

$$
\mathrm{div} (\boldsymbol {X}) (\boldsymbol {p}) = \mathrm{tr} J \boldsymbol {X} (\boldsymbol {p}) = \sum_ {i = 1} ^ {n} \frac {\partial f _ {i}}{\partial x _ {i}} (\boldsymbol {p}),
$$

其中 JX 是向量值函数 X 的 Jacobi 矩阵.

证明 不妨设 $p = 0$ . 由题设可知

$$
\boldsymbol {X} (\boldsymbol {x}) = \boldsymbol {X} (\boldsymbol {0}) + J \boldsymbol {X} (\boldsymbol {0}) \boldsymbol {x} + o (\| \boldsymbol {x} \|) \quad (\boldsymbol {x} \rightarrow \boldsymbol {0}).
$$

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">① Green, George, 1793 年 6 月—1841 年 5 月 31 日, 英国数学家.</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">② Gauss, Carolus Fridericus, 1777 年 4 月 30 日—1855 年 2 月 23 日, 德国数学家、物理学家、天文学家.</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">③ Stokes, George Gabriel, 1819 年 8 月 13 日—1903 年 2 月 1 日, 英国数学家、力学家.</span></small>

---

18.1 各类积分之间的联系

69

当 $r\to 0^{+}$ 时，就有

$$
\begin{array}{l} \int_ {\partial B _ {r} (\boldsymbol {p})} \boldsymbol {X} \cdot \boldsymbol {n} \mathrm{d} \sigma = \frac {1}{r} \int_ {\partial B _ {r} (\boldsymbol {0})} \boldsymbol {X} (\boldsymbol {0}) \cdot \boldsymbol {x} \mathrm{d} \sigma + \frac {1}{r} \int_ {\partial B _ {r} (\boldsymbol {0})} \boldsymbol {x} \cdot J \boldsymbol {X} (\boldsymbol {0}) \boldsymbol {x} \mathrm{d} \sigma + o (r ^ {n}) \\ = \sum_ {i = 1} ^ {n} \frac {f _ {i} (\mathbf {0})}{r} \int_ {\partial B _ {r} (\mathbf {0})} x _ {i} \mathrm{d} \sigma + \sum_ {i, j = 1} ^ {n} \frac {\partial_ {j} f _ {i} (\mathbf {0})}{r} \int_ {\partial B _ {r} (\mathbf {0})} x _ {i} x _ {j} \mathrm{d} \sigma + o (r ^ {n}). \\ \end{array}
$$

由球的对称性可知

$$
\int_ {\partial B _ {r} (\mathbf {0})} x _ {i} \mathrm{d} \sigma = 0, \quad \int_ {\partial B _ {r} (\mathbf {0})} x _ {i} x _ {j} \mathrm{d} \sigma = 0 (j \neq i).
$$

同理有

$$
\int_ {\partial B _ {r} (\mathbf {0})} x _ {i} ^ {2} \mathrm{d} \sigma = \frac {1}{n} \int_ {\partial B _ {r} (\mathbf {0})} \| \boldsymbol {x} \| ^ {2} \mathrm{d} \sigma = \omega_ {n} r ^ {n + 1}.
$$

这说明

$$
\int_ {\partial B _ {r} (\boldsymbol {p})} \boldsymbol {X} \cdot \boldsymbol {n} \mathrm{d} \sigma = \omega_ {n} r ^ {n} \sum_ {i = 1} ^ {n} \frac {\partial f _ {i}}{\partial x _ {i}} (\boldsymbol {0}) + o (r ^ {n}) (r \rightarrow 0 ^ {+}).
$$

由此即得欲证结论.

将上述引理中以 p 为中心的球换成以 p 为中心的方体时类似的结论也成立. 我们还可以猜测当 D 是以 p 为内点的小区域时, 也应有

$$
\int_ {\partial D} \boldsymbol {X} \cdot \boldsymbol {n}   \mathrm{d} \sigma \approx \nu (D) \mathrm{div} (\boldsymbol {X}) (\boldsymbol {p}).
$$

一般地, 若能将 $\Omega$ 分割为若干充分小的区域 $\{\Omega_i\}$, 取 $p_i \in \Omega_i$, 则

$$
\int_ {\Omega} \mathrm{div} (\boldsymbol {X}) \mathrm{d} \boldsymbol {x} \approx \sum_ {i} \nu (\varOmega_ {i}) \mathrm{div} (\boldsymbol {X}) (\boldsymbol {p} _ {i}) \approx \sum_ {i} \int_ {\partial \varOmega_ {i}} \boldsymbol {X} \cdot \boldsymbol {n} _ {i} \mathrm{d} \sigma ,
$$

其中 $n_i$ 均为单位外法向量场. 在相邻区域的公共边界上, 由于单位外法向量方向相反, 相应的两个第二型积分会互相抵消, 最终只剩下 $\partial \Omega$ 上的第二型曲面积分. 也就是说, 我们期望得到如下公式:

$$
\int_ {\Omega} \mathrm{div} (\boldsymbol {X}) \mathrm{d} \boldsymbol {x} = \int_ {\partial \Omega} \boldsymbol {X} \cdot \boldsymbol {n} \mathrm{d} \sigma . \tag {18.1.1}
$$

为了验证上式成立, 我们需要对  $\Omega$  施加适当的限制条件.

定义 18.1.1 ( $C^{k}$  边界) 设  $n \geqslant 2, \Omega$  为  $R^{n}$  中的开集. 如果任给  $x_{0} \in \partial \Omega$ , 均存在  $x_{0}$  的开邻域 U, 正数 r, h,  $C^{k}$  函数  $\phi: [-r, r]^{n-1} \rightarrow (-h, h)$ , 以及仿射变换  $\varphi(x) = A(x - x_{0})$ , 其中 A 是行列式为 1 的正交矩阵, 使得

(1) $\phi (\mathbf{0}) = 0$, $\varphi (U) = (-r,r)^{n - 1}\times (-h,h)$;
(2) $\varphi (U\cap \Omega) = D = \{(\pmb {x}^{\prime},x_{n})\mid \pmb{x}^{\prime}\in (-r,r)^{n - 1},\phi (\pmb{x}^{\prime}) <   x_{n} <   h\}$
(3) $\varphi(U \cap \partial\Omega) = \mathrm{graph}(\phi) = \{(\boldsymbol{x}', \phi(\boldsymbol{x}')) \mid \boldsymbol{x}' \in (-r, r)^{n-1}\}$,

则称  $\Omega$  具有  $C^{k}$  边界.

---

70

第十八章 微分形式简介

设 $\Omega$ 为具有 $C^k (k\geqslant 1)$ 边界的开集, 我们先在边界 $\partial \Omega$ 上定义单位外法向量场 $\pmb{n}$. 设 $\pmb{x}_0\in \partial \Omega$ ，记 $\pmb {n}(\pmb {x}_0) = \pmb{A}^{-1}\pmb{\nu}$ ，其中

$$
\nu = \frac {1}{\sqrt {1 + | \nabla \phi (\mathbf {0}) | ^ {2}}} \big (\nabla \phi (\mathbf {0}), - 1 \big).
$$

断言: 存在 $\delta > 0$, 使得当 $0 < t \leqslant \delta$ 时, $t\nu \notin \bar{D}$; 当 $-\delta \leqslant t < 0$ 时 $t\nu \in D$. 事实上, 记 $t\nu = (x', x_n)$, 由 $\phi(0) = 0$ 可得

$$
\begin{array}{l} x _ {n} - \phi (\boldsymbol {x} ^ {\prime}) = x _ {n} - \nabla \phi (\boldsymbol {0}) \cdot \boldsymbol {x} ^ {\prime} + o (t) = (\boldsymbol {x} ^ {\prime}, x _ {n}) \cdot (- \nabla \phi (\boldsymbol {0}), 1) + o (t) \\ = - t \sqrt {1 + | \nabla \phi (\mathbf {0}) | ^ {2}} + o (t) (t \to 0), \\ \end{array}
$$

由此可见上述断言成立.这说明当 $0 < t \leqslant \delta$ 时，$x_0 + tn \notin \bar{\Omega}$；当 $-\delta \leqslant t < 0$ 时，$x_0 + tn \in \Omega$.正是因为如此我们才称法向量 $n$ 指向 $\Omega$ 的外侧方向.由此还可以看出 $n$ 不依赖于 $\varphi$ 的选取.

设 $\Omega$ 是具有 $C^1$ 边界的有界开集, $f \in C^1(\bar{\Omega})$, 为了验证 (18.1.1) 式成立, 我们再来说明 (18.1.1) 式在 $\mathbb{R}^n$ 的平移和旋转变换下具有形式不变性. 以旋转变换 $\psi(x) = Ax$ 为例, 设 $\psi(\Omega') = \Omega$, 由变量替换公式可得

$$
\int_ {\partial \Omega} \boldsymbol {X} \cdot \boldsymbol {n} \mathrm{d} \sigma = \int_ {\partial \Omega^ {\prime}} \boldsymbol {X} (\psi) \cdot \boldsymbol {n} (\psi) \mathrm{d} \sigma^ {\prime} = \int_ {\partial \Omega^ {\prime}} \boldsymbol {X} (\psi) \cdot \psi (\boldsymbol {n} ^ {\prime}) \mathrm{d} \sigma^ {\prime},
$$

其中 $n' = \psi^{-1}(n(\psi))$ 是 $\Omega'$ 在边界上的单位外法向量场. 由于旋转变换保持内积, 我们就有

$$
\int_ {\partial \Omega} \boldsymbol {X} \cdot \boldsymbol {n}   \mathrm{d} \sigma = \int_ {\partial \Omega^ {\prime}} \boldsymbol {X} ^ {\prime} \cdot \boldsymbol {n} ^ {\prime}   \mathrm{d} \sigma^ {\prime},
$$

其中 $X^{\prime} = \psi^{-1}\circ X\circ \psi$ .由链式法则可知

$$
\mathrm{div} (\boldsymbol {X} ^ {\prime}) = \mathrm{tr} J \boldsymbol {X} ^ {\prime} = \mathrm{tr} \left[ \psi^ {- 1} \circ (J \boldsymbol {X}) (\psi) \circ \psi \right] = \mathrm{tr} (J \boldsymbol {X}) (\psi) = \mathrm{div} (\boldsymbol {X}) (\psi).
$$

由变量替换公式可得

$$
\int_ {\Omega} \mathrm{div} (\boldsymbol {X}) \mathrm{d} \boldsymbol {x} = \int_ {\Omega^ {\prime}} \mathrm{div} (\boldsymbol {X} ^ {\prime}) \mathrm{d} \boldsymbol {x} ^ {\prime}.
$$

这说明 (18.1.1) 式对 $\Omega$ 成立当且仅当它对 $\Omega'$ 成立.

由定义 18.1.1 可知  $\partial\Omega$  在局部上为参数超曲面. 为了将局部上的积分整合成  $\Omega$  上的积分, 我们需要用到一个方便的工具, 叫做单位分解.

所谓单位分解, 就是将 1 分解为若干个具有紧支集的函数之和. 其中, 函数 $f$ 的支集 $\operatorname{supp} f$ 定义为

$$
\mathrm{supp} f = \overline {{\{x \mid f (x) \neq 0 \}}}
$$

---

18.1 各类积分之间的联系

71

我们在 $\mathbb{R}$ 上定义偶函数 $\phi(t)$ 如下:

$$
\phi (t) = 1, t \in [ 0, 0. 5 ]; \phi (t) = \frac {(1 - t) ^ {3}}{(t - 0 . 5) ^ {3} + (1 - t) ^ {3}}, 0. 5 <   t \leqslant 1; \phi (t) = 0, t \geqslant 1. \tag {18.1.2}
$$

当 $t < 0$ 时令 $\phi(t) = \phi(-t)$. 容易验证 $\phi$ 是 $C^2$ 函数, 称为 $\mathbb{R}$ 上的鼓包函数.

引理 18.1.2 (单位分解) 设 K 为  $R^{n}$  中的有界闭集,  $\{V_{\alpha}\}$  为 K 的有限开覆盖, 则存在  $R^{n}$  上的非负  $C^{2}$  函数  $\{\phi_{\alpha}\}$ , 使得

$$
0 \leqslant \sum_ {\alpha} \phi_ {\alpha} (\boldsymbol {x}) \leqslant 1, \forall \boldsymbol {x} \in \mathbb {R} ^ {n}; \sum_ {\alpha} \phi_ {\alpha} (\boldsymbol {x}) = 1, \forall \boldsymbol {x} \in K; \operatorname{supp} \phi_ {\alpha} \subset V _ {\alpha}.
$$

$\{\phi_{\alpha}\}$  称为从属于开覆盖  $\{V_{\alpha}\}$  的一个单位分解.

证明 由题设可知, 任给 $\pmb{x} \in K$, 存在 $\alpha$, 使得 $\pmb{x} \in V_{\alpha}$. 取 $\varepsilon_{\pmb{x}} > 0$, 使得 $B_{2\varepsilon_{\pmb{x}}}(\pmb{x}) \subset V_{\alpha}$. 根据有限覆盖定理, 存在有限个小球, 记为 $\{B_{\varepsilon_i / 2}(\pmb{x}^i)\}_{i=1}^k$, 使得它们覆盖了 $K$, 其中 $\pmb{x}^i \in K, \varepsilon_i = \varepsilon_{\pmb{x}^i}$. 记

$$
\phi_ {i} (\boldsymbol {x}) = \phi \big (\varepsilon_ {i} ^ {- 1} \| \boldsymbol {x} - \boldsymbol {x} ^ {i} \| \big), i = 1, 2, \dots , k,
$$

其中 $\phi$ 为上面的一元鼓包函数. 令

$$
\psi_ {1} = \phi_ {1}, \quad \psi_ {i} = (1 - \phi_ {1}) (1 - \phi_ {2}) \dots (1 - \phi_ {i - 1}) \phi_ {i}, \quad i = 2, 3, \dots , k.
$$

显然有

$$
\mathrm{supp}   \psi_ {i} \subset B _ {2 \varepsilon_ {i}} (\boldsymbol {x} ^ {i}), i = 1, 2, \dots , k.
$$

注意到

$$
\psi_ {1} + \psi_ {2} + \dots + \psi_ {k} = 1 - (1 - \phi_ {1}) (1 - \phi_ {2}) \dots (1 - \phi_ {k}).
$$

由 $\{B_{\varepsilon_i / 2}(\pmb{x}^i)\}_{i = 1}^k$ 为 $K$ 的覆盖可知，当 $\pmb {x}\in K$ 时，至少有一个 $\phi_i$ 满足 $\phi_i(\pmb {x}) = 1.$ 于是

$$
\psi_ {1} (\boldsymbol {x}) + \psi_ {2} (\boldsymbol {x}) + \dots + \psi_ {k} (\boldsymbol {x}) = 1, \forall \boldsymbol {x} \in K.
$$

将支集含于 $V_{\alpha}$ 的那些 $\psi_{i}$ 的和记为 $\phi_{\alpha}$ (不重复求和), 则 $\{\phi_{\alpha}\}$ 为满足定理要求的单位分解.

定理 18.1.3 (散度定理) 设  $\Omega$  是  $R^{n}$  中具有  $C^{1}$  边界的有界开集, X 是  $\bar{\Omega}$  上的  $C^{1}$  向量场, n 是  $\Omega$  在边界上的单位外法向量场, 则 (18.1.1) 式成立.

证明 由题设可知 $\partial \Omega$ 是有界闭集, 于是存在有限个满足定义18.1.1中要求的开集 $\{U_k\}_{k=1}^m$, 使得 $\{\Omega, U_k \mid 1 \leqslant k \leqslant m\}$ 为 $\bar{\Omega}$ 的开覆盖. 对此开覆盖应用单位分解引理可以将欲证结论约化为如下两种情形:

---

72

第十八章 微分形式简介

(1) $\operatorname{supp} X \subset \Omega$, 其中 $\operatorname{supp} X = \overline{\{x \mid X(x) \neq 0\}}$, 称为 $X$ 的支集. 在这种情形下, 取 $R > 0$, 使得 $\bar{\Omega} \subset [-R, R]^n$, 我们规定 $X$ 在 $[-R, R]^n \setminus \bar{\Omega}$ 上为零. 此时 $X \in C^1([-R, R]^n)$. 记 $X = (f_1, f_2, \cdots, f_n)$, 由重积分化累次积分可得

$$
\int_ {\Omega} \frac {\partial f _ {i}}{\partial x _ {i}} \mathrm{d} \boldsymbol {x} = \int_ {[ - R, R ] ^ {n}} \frac {\partial f _ {i}}{\partial x _ {i}} \mathrm{d} \boldsymbol {x} = \int_ {[ - R, R ] ^ {n - 1}} f _ {i} | _ {x _ {i} = - R} ^ {x _ {i} = R} \mathrm{d} x _ {1} \dots \widehat {\mathrm{d} x _ {i}} \dots \mathrm{d} x _ {n} = 0.
$$

由此可见 (18.1.1) 式左右两边都等于零.

(2) suppX 包含于某个  $U_{k}$ . 根据 (18.1.1) 式在  $R^{n}$  的平移和旋转变换下的形式不变性, 不妨设  $U_{k}=D$ , 其中 D 如定义 18.1.1 所述. 当  $x_{n}\geqslant h$  时我们规定  $\boldsymbol{X}(\boldsymbol{x})=\boldsymbol{0}$ , 其中  $\boldsymbol{x}=(\boldsymbol{x}^{\prime},x_{n}),\boldsymbol{x}^{\prime}=(x_{1},x_{2},\cdots,x_{n-1})$ .

当 $1 \leqslant i \leqslant n - 1$ 时, 由重积分化累次积分可得

$$
\begin{array}{l} \int_ {\Omega} \frac {\partial f _ {i}}{\partial x _ {i}} \mathrm{d} \boldsymbol {x} = \int_ {D} \frac {\partial f _ {i}}{\partial x _ {i}} \mathrm{d} \boldsymbol {x} = \int_ {[ - R, R ] ^ {n - 1}} \int_ {\phi (\boldsymbol {x} ^ {\prime})} ^ {h} \frac {\partial f _ {i}}{\partial x _ {i}} \mathrm{d} \boldsymbol {x} \\ = \int_ {[ - R, R ] ^ {n - 1}} \int_ {0} ^ {h - \phi (\boldsymbol {x} ^ {\prime})} \frac {\partial f _ {i}}{\partial x _ {i}} (\boldsymbol {x} ^ {\prime}, y + \phi (\boldsymbol {x} ^ {\prime})) \mathrm{d} \boldsymbol {x} ^ {\prime} \mathrm{d} y \\ = \int_ {[ - R, R ] ^ {n - 1}} \int_ {0} ^ {2 h} \frac {\partial f _ {i}}{\partial x _ {i}} (\boldsymbol {x} ^ {\prime}, y + \phi (\boldsymbol {x} ^ {\prime})) \mathrm{d} \boldsymbol {x} ^ {\prime} \mathrm{d} y \\ = \int_ {[ - R, R ] ^ {n - 1}} \int_ {0} ^ {2 h} [ f _ {i} (\boldsymbol {x} ^ {\prime}, y + \phi (\boldsymbol {x} ^ {\prime})) ] _ {x _ {i}} \mathrm{d} \boldsymbol {x} ^ {\prime} \mathrm{d} y - \\ \int_ {[ - R, R ] ^ {n - 1}} \int_ {0} ^ {2 h} [ f _ {i} (\boldsymbol {x} ^ {\prime}, y + \phi (\boldsymbol {x} ^ {\prime})) ] _ {y} \phi_ {x _ {i}} \mathrm{d} \boldsymbol {x} ^ {\prime} \mathrm{d} y \\ = \int_ {[ - R, R ] ^ {n - 2}} \int_ {0} ^ {2 h} [ f _ {i} (\boldsymbol {x} ^ {\prime}, y + \phi (\boldsymbol {x} ^ {\prime})) ] | _ {x _ {i} = - R} ^ {x _ {i} = R} \mathrm{d} x _ {1} \dots \widehat {\mathrm{d} x _ {i}} \dots \mathrm{d} x _ {n - 1} \mathrm{d} y - \\ \int_ {[ - R, R ] ^ {n - 1}} [ f _ {i} (\boldsymbol {x} ^ {\prime}, y + \phi (\boldsymbol {x} ^ {\prime})) ] \big | _ {y = 0} ^ {y = 2 h} \phi_ {x _ {i}} \mathrm{d} \boldsymbol {x} ^ {\prime} \\ = \int_ {[ - R, R ] ^ {n - 1}} f _ {i} (\boldsymbol {x} ^ {\prime}, \phi (\boldsymbol {x} ^ {\prime})) \phi_ {x _ {i}} \mathrm{d} \boldsymbol {x} ^ {\prime}. \\ \end{array}
$$

同理可得

$$
\int_ {\Omega} \frac {\partial f _ {n}}{\partial x _ {n}} \mathrm{d} x = - \int_ {[ - R, R ] ^ {n - 1}} f _ {n} (\boldsymbol {x} ^ {\prime}, \phi (\boldsymbol {x} ^ {\prime})) \mathrm{d} \boldsymbol {x} ^ {\prime}.
$$

由上述计算可得

$$
\begin{array}{l} \int_ {\Omega} \mathrm{div} (\boldsymbol {X}) \mathrm{d} \boldsymbol {x} = \int_ {[ - R, R ] ^ {n - 1}} \boldsymbol {X} (\boldsymbol {x} ^ {\prime}, \phi (\boldsymbol {x} ^ {\prime})) \cdot (\nabla \phi (\boldsymbol {x} ^ {\prime}), - 1) \mathrm{d} \boldsymbol {x} ^ {\prime} \\ = \int_ {[ - R, R ] ^ {n - 1}} \boldsymbol {X} (\boldsymbol {x} ^ {\prime}, \phi (\boldsymbol {x} ^ {\prime})) \cdot \boldsymbol {n} \sqrt {1 + | \nabla \phi (\boldsymbol {x} ^ {\prime}) | ^ {2}} \mathrm{d} \boldsymbol {x} ^ {\prime} \\ = \int_ {\mathrm{graph} (\phi)} \boldsymbol {X} \cdot \boldsymbol {n}   \mathrm{d} \sigma = \int_ {\partial \Omega} \boldsymbol {X} \cdot \boldsymbol {n}   \mathrm{d} \sigma , \\ \end{array}
$$

---

18.1 各类积分之间的联系

73

定理证毕.

散度定理在平面上可以改写为所谓的 Green 公式. 考虑平面  $R^{2}$  上具有  $C^{1}$  边界的有界开集  $\Omega$ .  $R^{2}$  上的标准定向限制在  $\Omega$  上就得到  $\Omega$  的定向.  $\Omega$  的边界  $\partial\Omega$  有所谓的诱导定向. 这个诱导定向定义如下: 设  $(x(t), y(t))$  为  $\partial\Omega$  的一段参数曲线, 则  $(x'(t), y'(t))$  为切向量,  $(y'(t), -x'(t))$  为法向量. 如果  $(y'(t), -x'(t))$  为相对于区域  $\Omega$  的外法向量, 则参数 t 决定的边界方向称为诱导定向, 也称为正向. 直观上看, 从外法向到切向的旋转方向是逆时针的, 这种确定边界定向的方法又称为 “右手法则” (图 18.1(a)).

![](../../raw/pages_0705-0720/images/page_713_image_4.jpg)

图 18.1 诱导定向

例 18.1.1 环形区域边界上正向.

如图 18.1(b) 所示, 设 b > a > 0, 平面区域  $\{a^{2} \leqslant x^{2} + y^{2} \leqslant b^{2}\}$  是半径为 b 的大圆盘中挖去一个半径为 a 的小圆盘形成的环形区域. 它的边界由圆周  $\{x^{2} + y^{2} = b^{2}\}$  和  $\{x^{2} + y^{2} = a^{2}\}$  组成. 按照诱导定向的定义, 在大圆  $\{x^{2} + y^{2} = b^{2}\}$  上, 方向是逆时针的; 而在小圆  $\{x^{2} + y^{2} = a^{2}\}$  上, 方向应是顺时针的. □

下面的结果将二重积分和第二型曲线积分联系起来了, 它常称为 Green 公式.

定理 18.1.4 (Green 公式) 设  $\Omega$  为平面上具有  $C^{1}$  边界的有界开集, 边界的定向为诱导定向. 如果 P, Q 为  $\bar{\Omega}$  上的  $C^{1}$  函数, 则

$$
\int_ {\Omega} \left(\frac {\partial Q}{\partial x} - \frac {\partial P}{\partial y}\right) \mathrm{d} x \mathrm{d} y = \int_ {\partial \Omega} P \mathrm{d} x + Q \mathrm{d} y.
$$

证明 取  $\boldsymbol{X}=(Q,-P)$ ，则  $\mathrm{div}(\boldsymbol{X})=\frac{\partial Q}{\partial x}-\frac{\partial P}{\partial y}$ 。若在边界曲线上取弧长参数 s，则单位外法向量可以表示  $\boldsymbol{n}=(y'(s),-x'(s))$ ，此时

$$
P \mathrm{d} x + Q \mathrm{d} y = [ P x ^ {\prime} (s) + Q y ^ {\prime} (s) ] \mathrm{d} s = \boldsymbol {X} \cdot \boldsymbol {n} \mathrm{d} s,
$$

这样散度定理就可以改写成 Green 公式.

![](../../raw/pages_0705-0720/images/page_713_image_14.jpg)

注 18.1.1 Green 公式对于那些类似于矩形区域的具有分段  $C^{1}$  边界的区域仍成立.

例 18.1.2 平面简单闭曲线所围区域的面积.

---

74

第十八章 微分形式简介

设 $\gamma(t) = (x(t), y(t))$ ($t \in [\alpha, \beta]$) 为 $\mathbb{R}^2$ 上分段 $C^1$ 的简单闭曲线, 它围成的区域记为 $\Omega$. 在 Green 公式中取 $P(x, y) = -y$, $Q(x, y) = x$, 可得如下面积公式:

$$
\begin{array}{l} \nu (\Omega) = \frac {1}{2} \int_ {\Omega} \left(\frac {\partial Q}{\partial x} - \frac {\partial P}{\partial y}\right) \mathrm{d} x \mathrm{d} y = \frac {1}{2} \int_ {\partial \Omega} P \mathrm{d} x + Q \mathrm{d} y \\ = \frac {1}{2} \int_ {\alpha} ^ {\beta} [ x (t) y ^ {\prime} (t) - x ^ {\prime} (t) y (t) ] \mathrm{d} t, \\ \end{array}
$$

其中, 参数 t 选取的方向是逆时针的.

作为例子, 考虑椭圆  $\frac{x^{2}}{a^{2}} + \frac{y^{2}}{b^{2}} = 1$  所围成的面积. 椭圆的参数方程为

$$
x (t) = a \cos t, y (t) = b \sin t, t \in [ 0, 2 \pi ],
$$

于是其面积为

$$
\nu = \frac {1}{2} \int_ {0} ^ {2 \pi} (a \cos t b \cos t + a \sin t b \sin t) \mathrm{d} t = \pi a b.
$$

例 18.1.3 计算积分  $I = \int_{C} x^{2} y \, dx - xy^{2} \, dy$ ，其中 C 是上半圆  $x^{2} + y^{2} = a^{2}$ ， $y \geqslant 0$ ，取逆时针方向 (图 18.2).

![](../../raw/pages_0705-0720/images/page_714_image_10.jpg)

<details>
<summary>text_image</summary>

y
a
-a O a x
</details>

图18.2 上半圆

解 考虑上半圆的边界, 它由 $C$ 以及 $(x,0)$ ($x \in [-a,a]$) 组成, 在上半圆区域上用 Green 公式, 得

$$
I = \int_ {\{x ^ {2} + y ^ {2} \leqslant a ^ {2}, y \geqslant 0 \}} (- x ^ {2} - y ^ {2}) \mathrm{d} x \mathrm{d} y = - \int_ {0} ^ {\pi} \mathrm{d} \theta \int_ {0} ^ {a} r ^ {3} \mathrm{d} r = - \frac {\pi}{4} a ^ {4}.
$$

例 18.1.4 设  $\Omega$  为包含原点的平面有界区域, 其边界为  $C^{1}$  曲线, 取逆时针方向 (图 18.3). 计算积分

$$
I = \int_ {\partial \Omega} \frac {- y \mathrm{d} x}{x ^ {2} + y ^ {2}} + \frac {x \mathrm{d} y}{x ^ {2} + y ^ {2}}.
$$

解 取中心为原点的小圆 $x^{2} + y^{2} = \varepsilon^{2}$, 使得 $B_{\varepsilon}(\mathbf{0}) \subset \Omega$. 小圆上的定向规定为逆时针方向 (从而与诱导定向相反), 其参数表示为 $x = \varepsilon \cos \theta, y = \varepsilon \sin \theta$. 注意到

$$
\frac {\partial}{\partial x} \left(\frac {x}{x ^ {2} + y ^ {2}}\right) + \frac {\partial}{\partial y} \left(\frac {y}{x ^ {2} + y ^ {2}}\right) = 0.
$$

---

18.1 各类积分之间的联系

75

在区域 $\Omega \setminus B_{\varepsilon}(\mathbf{0})$ 中利用Green公式可得

$$
\begin{array}{l} 0 = \int_ {\Omega \backslash B _ {\varepsilon} (\mathbf {0})} \left[ \frac {\partial}{\partial x} \left(\frac {x}{x ^ {2} + y ^ {2}}\right) + \frac {\partial}{\partial y} \left(\frac {y}{x ^ {2} + y ^ {2}}\right) \right] \mathrm{d} x \mathrm{d} y \\ = I - \int_ {\left\{x ^ {2} + y ^ {2} = \varepsilon^ {2} \right\}} \left(\frac {- y \mathrm{d} x}{x ^ {2} + y ^ {2}} + \frac {x \mathrm{d} y}{x ^ {2} + y ^ {2}}\right) \\ = I - \int_ {0} ^ {2 \pi} \mathrm{d} \theta = I - 2 \pi . \\ \end{array}
$$

这说明  $I = 2\pi$ .

![](../../raw/pages_0705-0720/images/page_715_image_5.jpg)

<details>
<summary>text_image</summary>

y
Ω
-ε O ε x
</details>

图18.3 有界区域

在三维空间中, 散度定理可以改写为所谓的 Gauss 公式. 设  $\Omega$  为  $R^{3}$  中具有  $C^{1}$  边界的有界开集, 边界的定向取为诱导定向, 即外侧方向. 如下 Gauss 公式将三重积分与第二型曲面积分联系起来了.

定理 18.1.5 (Gauss 公式) 设  $\Omega$  为  $R^{3}$  中具有  $C^{1}$  边界的有界开集, 其边界的定向取为诱导定向. 如果 P, Q, R 为  $\bar{\Omega}$  上的  $C^{1}$  函数, 则

$$
\int_ {\Omega} \left(\frac {\partial P}{\partial x} + \frac {\partial Q}{\partial y} + \frac {\partial R}{\partial z}\right) \mathrm{d} x \mathrm{d} y \mathrm{d} z = \int_ {\partial \Omega} P \mathrm{d} y \wedge \mathrm{d} z + Q \mathrm{d} z \wedge \mathrm{d} x + R \mathrm{d} x \wedge \mathrm{d} y.
$$

证明 在散度定理中取  $\boldsymbol{X}=(P,Q,R)$  即可.

例 18.1.5 曲面所围区域的体积.

设有界区域 $\Omega$ 具有 $C^1$ 边界, 在 Gauss 公式中取 $P = x, Q = y, R = z$ 就得到了如下体积公式

$$
\nu (\varOmega) = \frac {1}{3} \int_ {\partial \varOmega} x   \mathrm{d} y \wedge \mathrm{d} z + y   \mathrm{d} z \wedge \mathrm{d} x + z   \mathrm{d} x \wedge \mathrm{d} y.
$$

例18.1.6 在 $\mathbb{R}^3$ 上, 记 $r = \sqrt{x^2 + y^2 + z^2}$, 计算积分

$$
I = \int_ {\partial \Omega} \frac {x}{r ^ {3}} \mathrm{d} y \wedge \mathrm{d} z + \frac {y}{r ^ {3}} \mathrm{d} z \wedge \mathrm{d} x + \frac {z}{r ^ {3}} \mathrm{d} x \wedge \mathrm{d} y,
$$

其中  $\Omega$  是包含原点在内的有界区域, 其边界取外侧方向.

---

76

第十八章 微分形式简介

解 记 $P = x / r^3, Q = y / r^3, R = z / r^3$，则易验证

$$
\frac {\partial P}{\partial x} + \frac {\partial Q}{\partial y} + \frac {\partial R}{\partial z} = 0.
$$

取以原点为中心的且完全包含于 $\Omega$ 的小球 $B_{\varepsilon} = \{x^{2} + y^{2} + z^{2}\leqslant \varepsilon^{2}\}$ ，小球面的定向取相对于小球体的外侧方向.分别在 $\Omega \setminus B_{\varepsilon}$ 和 $B_{\varepsilon}$ 中应用Gauss公式可得

$$
\begin{array}{l} I = \int_ {\partial B _ {\varepsilon}} \frac {x}{r ^ {3}} \mathrm{d} y \wedge \mathrm{d} z + \frac {y}{r ^ {3}} \mathrm{d} z \wedge \mathrm{d} x + \frac {z}{r ^ {3}} \mathrm{d} x \wedge \mathrm{d} y \\ = \varepsilon^ {- 3} \int_ {\partial B _ {\epsilon}} x \mathrm{d} y \wedge \mathrm{d} z + y \mathrm{d} z \wedge \mathrm{d} x + z \mathrm{d} x \wedge \mathrm{d} y \\ = \varepsilon^ {- 3} 3 \nu (B _ {\varepsilon}) = 4 \pi . \\ \end{array}
$$

![](../../raw/pages_0705-0720/images/page_716_image_6.jpg)

例 18.1.7 设  $\Omega$  是  $R^{3}$  上包含原点在内的有界区域, 其边界取外侧方向. 在原点处有电荷 q, 求它生成的电场通过  $\partial\Omega$  的电通量.

解 由库仑定律，电荷所生成的电场为 $F = \kappa \frac{q}{r^3} r$，其中 $r = (x, y, z)$，$r = \sqrt{x^2 + y^2 + z^2}$。计算表明，$\operatorname{div}(F)$ 在原点之外为零。于是，当 $\varepsilon > 0$ 且充分小时，在 $\Omega \setminus B_{\varepsilon}(0)$ 中应用散度定理可得

$$
0 = \int_ {\Omega \setminus B _ {\varepsilon} (\mathbf {0})} \mathrm{div} (\boldsymbol {F})   \mathrm{d} x   \mathrm{d} y   \mathrm{d} z = \int_ {\partial \Omega} \boldsymbol {F} \cdot \boldsymbol {n}   \mathrm{d} \sigma - \int_ {\partial B _ {\varepsilon} (\mathbf {0})} \boldsymbol {F} \cdot \boldsymbol {n}   \mathrm{d} \sigma ,
$$

注意到在球面上, $n=\frac{r}{r}$ ，于是电场F通过曲面 $\partial\Omega$ 的电通量为

$$
\int_ {\partial \Omega} \boldsymbol {F} \cdot \boldsymbol {n} \mathrm{d} \sigma = \int_ {\partial B _ {\varepsilon (\mathbf {0})}} \kappa \frac {q}{\varepsilon^ {2}} \mathrm{d} \sigma = 4 \kappa \pi q.
$$

![](../../raw/pages_0705-0720/images/page_716_image_12.jpg)

## 18.1.2 Stokes 公式

设 $\Sigma$ 为 $\mathbb{R}^3$ 中的 $C^2$ 有向曲面, 其边界 $\partial \Sigma$ 由有限条分段 $C^1$ 的简单闭曲线所组成. 我们用“右手法则”在边界上定义诱导定向如下: 边界在曲面上的外法向量与边界的切向量的外积得到的曲面法向量与决定曲面方向的法向量同向. 即如果用右手从曲线外法向到切向作旋转, 则大拇指所指方向为曲面的正法向 (图18.4).

![](../../raw/pages_0705-0720/images/page_716_image_15.jpg)

<details>
<summary>text_image</summary>

Ω
Σ
</details>

图18.4 曲面区域

---

18.1 各类积分之间的联系

77

下面的 Stokes 公式将第二型曲面积分与第二型曲线积分联系起来了, 它是平面区域上 Green 公式的推广.

定理 18.1.6 (Stokes 公式) 设  $\Sigma$  为定向曲面, 其边界取诱导定向. 如果 P, Q, R 为  $\bar{\Sigma}$  上的  $C^{1}$  函数, 则

$$
\begin{array}{l} \int_ {\Sigma} \left(\frac {\partial R}{\partial y} - \frac {\partial Q}{\partial z}\right) \mathrm{d} y \wedge \mathrm{d} z + \left(\frac {\partial P}{\partial z} - \frac {\partial R}{\partial x}\right) \mathrm{d} z \wedge \mathrm{d} x + \left(\frac {\partial Q}{\partial x} - \frac {\partial P}{\partial y}\right) \mathrm{d} x \wedge \mathrm{d} y \\ = \int_ {\partial \Sigma} P \mathrm{d} x + Q \mathrm{d} y + R \mathrm{d} z. \\ \end{array}
$$

我们只讨论一个特殊情形: 假定 $r(u, v)$ 是有向曲面 $\Sigma$ 的参数表示, 其中 $(u, v) \in D \subseteq \mathbb{R}^2$. 我们来讨论在参数表示下 Stokes 公式中的两个积分如何变化. 为了方便起见, Stokes 公式的左右两边分别记为 I, II.

记 $r(u,v) = (x(u,v),y(u,v),z(u,v))$ ，则

$$
\mathrm{II} = \int_ {\partial D} S \mathrm{d} u + T \mathrm{d} v,
$$

其中 $S = Px_{u} + Qy_{u} + Rz_{u}, T = Px_{v} + Qy_{v} + Rz_{v}$. 由 Green 公式可得

$$
\mathrm{II} = \iint_ {D} (T _ {u} - S _ {v})   \mathrm{d} u   \mathrm{d} v.
$$

计算表明

$$
T _ {u} - S _ {v} = (P _ {u} x _ {v} - P _ {v} x _ {u}) + (Q _ {u} y _ {v} - Q _ {v} y _ {u}) + (R _ {u} z _ {v} - R _ {v} z _ {u}).
$$

根据复合求导的链式法则, 有

$$
P _ {u} = P _ {x} x _ {u} + P _ {y} y _ {u} + P _ {z} z _ {u}, P _ {v} = P _ {x} x _ {v} + P _ {y} y _ {v} + P _ {z} z _ {v},
$$

关于 $Q, R$ 有完全类似的等式, 将它们代入前式可得

$$
\begin{array}{l} T _ {u} - S _ {v} = P _ {y} \left(y _ {u} x _ {v} - x _ {u} y _ {v}\right) + P _ {z} \left(z _ {u} x _ {v} - x _ {u} z _ {v}\right) + Q _ {x} \left(x _ {u} y _ {v} - y _ {u} x _ {v}\right) + \\ Q _ {z} (z _ {u} y _ {v} - y _ {u} z _ {v}) + R _ {x} (x _ {u} z _ {v} - z _ {u} x _ {v}) + R _ {y} (y _ {u} z _ {v} - z _ {u} y _ {v}), \\ \end{array}
$$

或改写为

$$
T _ {u} - S _ {v} = (R _ {y} - Q _ {z}) \frac {\partial (y , z)}{\partial (u , v)} + (P _ {z} - R _ {x}) \frac {\partial (z , x)}{\partial (u , v)} + (Q _ {x} - P _ {y}) \frac {\partial (x , y)}{\partial (u , v)}.
$$

根据第二型曲面积分的定义可得

$$
\mathrm{I} = \iint_ {D} (T _ {u} - S _ {v})   \mathrm{d} u   \mathrm{d} v.
$$

这说明 I = II, 即 Stokes 公式成立.

---

78

第十八章 微分形式简介

例18.1.8 计算积分 $I = \oint_{C}(x^{2} - y)\mathrm{d}x + (2x + y^{2})\mathrm{d}y + z^{2}\mathrm{d}z,$ 其中 $C = \{|x| + |y| = 1,z = \arctan (x + y)\}$，从 $z$ 轴正向往 $z$ 轴负向看，$C$ 的方向是逆时针的。

解 如果取 $C$ 的参数表示代入表达式进行计算可能会比较复杂. 这里使用一个小技巧: 把 $C$ 视为曲面 $\Sigma = \{z = \arctan (x + y) \mid (x, y) \in D\}$ 的边界, 其中 $D = \{(x, y) \mid |x| + |y| \leqslant 1\}$, 然后利用 Stokes 公式: 取 $P = x^2 - y$, $Q = 2x + y^2$, $R = z^2$, 计算表明

$$
R _ {y} - Q _ {z} = 0, P _ {z} - R _ {x} = 0, Q _ {x} - P _ {y} = 3.
$$

于是

$$
I = \iint_ {\Sigma} 3   \mathrm{d} x \wedge \mathrm{d} y = \iint_ {D} 3   \mathrm{d} x   \mathrm{d} y = 3 \nu (D) = 6.
$$

## 习题18.1

1. 验证由 (18.1.2) 式定义的鼓包函数的确是  $C^{2}$  函数.
2. 能否将  $C^{2}$  的鼓包函数改造成  $C^{3}$  的鼓包函数？请说明如何改造.
3. 设  $(a, b) \subset \mathbb{R}$ ，考虑如下一元函数:

$$
\rho (t) = \left\{ \begin{array}{l l} \mathrm{e} ^ {\frac {1}{(t - a) (b - t)}}, & t \in (a, b), \\ 0, & t \in (- \infty , a ] \cup [ b, + \infty), \end{array} \right.
$$

验证  $\rho\in C^{\infty}(\mathbb{R})$ .

4. 利用 Green 公式计算下列积分:

(1) $\int_{C} xy^{2} \, \mathrm{d}x - x^{2}y \, \mathrm{d}y, C$ 为圆周 $x^{2} + y^{2} = a^{2}$, 取逆时针方向;
(2) $\int_{C}(x + y)\mathrm{d}x - (x - y)\mathrm{d}y, C$ 为椭圆 $\frac{x^2}{a^2} +\frac{y^2}{b^2} = 1,$ 取逆时针方向；
(3) $\int_{C}(x^{2} + y)\mathrm{d}x - (x + y^{2})\mathrm{d}y, C$ 是从(1,1)经过(3,2)到(2,5)再回到(1,1)的三角形边界；
(4) $\int_{C} \mathrm{e}^{x} \sin y \, \mathrm{d}x + \mathrm{e}^{x} \cos y \, \mathrm{d}y$, $C$ 是上半圆周 $x^{2} + y^{2} = ax (y \geqslant 0)$, 取逆时针方向.

5. 利用 Green 公式计算下列曲线所围成的面积 $\left( {a > 0}\right)$ :

(1) 抛物线  $(x+y)^{2}=ax$  和 x 轴;
(2) 双纽线  $(x^{2}+y^{2})^{2}=a^{2}(x^{2}-y^{2})$ ;
(3) $x^{3} + y^{3} = 3axy$.

6. 设 $\Omega$ 为 $\mathbb{R}^n$ 中具有 $C^1$ 边界的有界开集, $\pmb{v}$ 为任意一个固定的向量, 证明:

$$
\int_ {\partial \Omega} \boldsymbol {v} \cdot \boldsymbol {n}   \mathrm{d} \sigma = 0,
$$

其中 n 为  $\partial\Omega$  的单位外法向量.

---

18.1 各类积分之间的联系

79

7. 设 $\Omega$ 为 $\mathbb{R}^n$ 中具有 $C^1$ 边界的有界开集, $u, v$ 为 $\bar{\Omega}$ 上的 $C^2$ 函数. 证明 Green 第一公式:

$$
\int_ {\Omega} v \Delta u \mathrm{d} x = \int_ {\partial \Omega} v \frac {\partial u}{\partial \boldsymbol {n}} \mathrm{d} \sigma - \int_ {\Omega} \nabla u \cdot \nabla v \mathrm{d} x,
$$

其中  $\Delta u = tr \nabla^{2}u, n$  为边界  $\partial\Omega$  上的单位外法向量.

8. 设 $\Omega$ 为 $\mathbb{R}^n$ 中具有 $C^1$ 边界的有界开集, $u, v$ 为 $\bar{\Omega}$ 上的 $C^2$ 函数. 证明 Green 第二公式:

$$
\int_ {\Omega} (v \Delta u - u \Delta v) \mathrm{d} x = \int_ {\partial \Omega} \left(v \frac {\partial u}{\partial \boldsymbol {n}} - u \frac {\partial v}{\partial \boldsymbol {n}}\right) \mathrm{d} \sigma ,
$$

其中 n 为边界  $\partial\Omega$  上的单位外法向量.

9. 设 $u$ 为闭圆盘 $D = \{x^{2} + y^{2} \leqslant 1\}$ 上的 $C^2$ 函数, 且 $\Delta u(x,y) = \mathrm{e}^{-(x^2 +y^2)}$, 证明:

$$
\iint_ {D} \left(x \frac {\partial u}{\partial x} + y \frac {\partial u}{\partial y}\right) \mathrm{d} x \mathrm{d} y = \frac {\pi}{2 \mathrm{e}}.
$$

10. 设 $\Omega$ 为 $\mathbb{R}^3$ 中具有 $C^1$ 边界的有界开集, $(x_0, y_0, z_0) \notin \partial \Omega$. 证明:

$$
\iiint_ {\Omega} \frac {\mathrm{d} x \mathrm{d} y \mathrm{d} z}{r} = \frac {1}{2} \iint_ {\partial \Omega} \frac {\boldsymbol {r} \cdot \mathrm{d} \vec {\sigma}}{r},
$$

其中  $\boldsymbol{r}=(x-x_{0},y-y_{0},z-z_{0}),\boldsymbol{r}=\sqrt{(x-x_{0})^{2}+(y-y_{0})^{2}+(z-z_{0})^{2}}$ ，对下列两种情况进行讨论:

(1) $(x_{0},y_{0},z_{0})\notin\Omega;$

(2) $(x_{0},y_{0},z_{0})\in\Omega$ ，此时令

$$
\iiint_ {\Omega} \frac {\mathrm{d} x \mathrm{d} y \mathrm{d} z}{r} = \lim _ {r \to 0 ^ {+}} \iiint_ {\Omega \setminus B _ {r}} \frac {\mathrm{d} x \mathrm{d} y \mathrm{d} z}{r},
$$

其中  $B_{r}$  是以  $(x_{0}, y_{0}, z_{0})$  为中心，以 r 为半径的球.

11. 利用 Gauss 公式计算下列积分:

(1) $\int_{\Sigma} x^{3} \mathrm{~d}y \wedge \mathrm{d}z + y^{3} \mathrm{~d}z \wedge \mathrm{d}x + z^{3} \mathrm{~d}x \wedge \mathrm{d}y, \Sigma$ 为球面 $x^{2} + y^{2} + z^{2} = a^{2}$, 方向为外侧;

(2) $\int_{\Sigma} x^{2} \mathrm{~d}y \wedge \mathrm{d}z + y^{2} \mathrm{~d}z \wedge \mathrm{d}x + z^{2} \mathrm{~d}x \wedge \mathrm{d}y, \Sigma$ 为矩形区域 $[0, a]^{3}$ 的边界, 方向为外侧;

(3) $\int_{\Sigma}(x - y)\mathrm{d}y\wedge \mathrm{d}z + (y - z)\mathrm{d}z\wedge \mathrm{d}x + (z - x)\mathrm{d}x\wedge \mathrm{d}y,\Sigma$ 为曲面 $z = x^{2} + y^{2}$ $(z\leqslant 1)$ ，方向向下.

12. 计算下列曲面积分:

(1) 设  $\Sigma$  为  $\frac{x^{2}}{a^{2}} + \frac{y^{2}}{b^{2}} + \frac{z^{2}}{c^{2}} = 1 (z \geqslant 0)$ ，方向为下侧，

$$
\iint_ {\Sigma} (x ^ {2} - y ^ {2}) \mathrm{d} y \wedge \mathrm{d} z + (y ^ {2} - z ^ {2}) \mathrm{d} z \wedge \mathrm{d} x + 2 z (y - x) \mathrm{d} x \wedge \mathrm{d} y;
$$

---

80

第十八章 微分形式简介

(2) 设 $\Sigma$ 是由平面 $x + y + z = 1$, $x = 0$, $y = 0$ 和 $z = 0$ 所围成的区域 $\Omega$ 的表面, 方向为外侧,

$$
\iint_ {\Sigma} (x + \cos y) \mathrm{d} y \wedge \mathrm{d} z + (y + \cos z) \mathrm{d} z \wedge \mathrm{d} x + (z + \cos x) \mathrm{d} x \wedge \mathrm{d} y;
$$

(3) 设 $\Sigma$ 为 $\frac{x^2}{a^2} + \frac{y^2}{b^2} + \frac{z^2}{c^2} = 1 (x \geqslant 0)$, 方向为后侧 (即法向量与 $x$ 轴夹角大于或等于 $\frac{\pi}{2}$),

$$
\iint_ {\Sigma} \left(\frac {x ^ {3}}{a ^ {2}} + y z\right) \mathrm{d} y \wedge \mathrm{d} z + \left(\frac {y ^ {3}}{b ^ {2}} + z ^ {3} x ^ {2}\right) \mathrm{d} z \wedge \mathrm{d} x + \left(\frac {z ^ {3}}{c} + x ^ {3} y ^ {3}\right) \mathrm{d} x \wedge \mathrm{d} y.
$$

13. 利用 Stokes 公式计算下列积分:

(1) $\int_{C} y \, \mathrm{d}x + z \, \mathrm{d}y + x \, \mathrm{d}z, C$ 是圆周 $x^{2} + y^{2} + z^{2} = a^{2}, x + y + z = 0$, 从 $x$ 轴看上去圆周的方向是逆时针的;
(2) $\int_{C} y^{2} \mathrm{~d} x + z^{2} \mathrm{~d} y + x^{2} \mathrm{~d} z, C$ 是圆周 $x^{2} + y^{2} + z^{2} = a^{2}, x + y + z = a,$ 从 $x$ 轴看上去圆周的方向是逆时针的;
(3) $\int_{C}(z - y)\mathrm{d}x + (x - z)\mathrm{d}y + (y - x)\mathrm{d}z, C$ 是从 $(a,0,0)$ 经过 $(0,a,0)$ 到 $(0,0,a)$ 再回到 $(a,0,0)$ 的三角形边界；

14. 利用 Stokes 公式计算如下积分:

$$
\oint_ {C} (y ^ {2} + z ^ {2}) \mathrm{d} x + (z ^ {2} + x ^ {2}) \mathrm{d} y + (x ^ {2} + y ^ {2}) \mathrm{d} z,
$$

其中 C 是曲面  $x^{2} + y^{2} + z^{2} = 4x$  与  $x^{2} + y^{2} = 2x$  的交线在  $z \geqslant 0$  的部分, 方向规定为从原点进入第一卦限.

15. 利用 Stokes 公式求力场 $\mathbf{F} = (x + 2y + 4, 4x - 2y, 3x + z)$ 沿椭圆

$$
C: (3 x + 2 y - 5) ^ {2} + (x - y + 1) ^ {2} = a ^ {2} (a > 0), \quad z = 4
$$

所做的功, 其中从 z 轴正轴看去 C 为逆时针方向.

## 18.2 外代数和微分形式

在第二型曲线积分和第二型曲面积分中, 我们遇到了形如 $A \mathrm{~d} x + B \mathrm{~d} y$, $A \mathrm{~d} y \mathrm{~d} z + B \mathrm{~d} z \mathrm{~d} x + C \mathrm{~d} x \mathrm{~d} y$ 之类的表示式. 在微积分发展的早期, 这些表达式被视为 “出现在积分号下面的东西”, 没有赋予它们实在的含义. 它们后来被称为微分形式, 满足特定的运算规则. 为了解释这些运算规则, 我们简要地介绍一下外代数的基本概念.

---

18.2 外代数和微分形式

81

设 $V$ 是实数域上的 $n$ 维向量空间, 其对偶空间 $V^{*}$ 定义为

$$
V ^ {*} = \{\phi : V \to \mathbb {R} \mid \phi \text {为线性函数} \}.
$$

显然, $V^{*}$ 成为实数域上的向量空间, 其维数也等于 $n$. 在 $V$ 中取一组基 $\{\boldsymbol{v}_i\}_{i=1}^n$, 定义 $\{\phi^j\}_{j=1}^n \subset V^{*}$ 为

$$
\phi^ {j} \left(\sum_ {i = 1} ^ {n} \lambda_ {i} \pmb {v} _ {i}\right) = \lambda_ {j}, \text {其中} \lambda_ {i} \in \mathbb {R}, i = 1, 2, \dots , n.
$$

容易验证 $\{\phi^j\}_{j=1}^n$ 是 $V^{*}$ 的一组基, 称为 $\{\pmb{v}_i\}_{i=1}^n$ 的对偶基. 当 $\pmb{v} \in V$, $\phi \in V^{*}$ 时, 我们有

$$
\boldsymbol {v} = \sum_ {i = 1} ^ {n} \phi^ {i} (\boldsymbol {v}) \boldsymbol {v} _ {i}, \quad \phi = \sum_ {j = 1} ^ {n} \phi (\boldsymbol {v} _ {j}) \phi^ {j}. \tag {18.2.1}
$$

设 $\phi, \psi \in V^{*}$, 在 $V$ 上定义二次型 (双线性型) $\phi \otimes \psi$ 如下:

$$
\phi \otimes \psi (\boldsymbol {v}, \boldsymbol {w}) = \phi (\boldsymbol {v}) \psi (\boldsymbol {w}), \forall \boldsymbol {v}, \boldsymbol {w} \in V.
$$

利用上述记号, V 上的任意一个二次型  $\Phi$  都可以表示为

$$
\varPhi = \sum_ {i, j = 1} ^ {n} \varPhi_ {i j} \phi^ {i} \otimes \phi^ {j}, \tag {18.2.2}
$$

其中 $\Phi_{ij} = \Phi (v_i,v_j)$ .内积是我们比较熟悉的二次型，我们知道 $\varPhi$ 为 $V$ 上的内积当且仅当 $\left(\varPhi_{ij}\right)_{n\times n}$ 为正定对称方阵.另一类重要的二次型是反对称(斜对称)二次型.若

$$
\varPhi (\boldsymbol {w}, \boldsymbol {v}) = - \varPhi (\boldsymbol {v}, \boldsymbol {w}), \forall \boldsymbol {v}, \boldsymbol {w} \in V,
$$

则称 $\Phi$ 是反对称的. 此时

$$
\varPhi_ {j i} = - \varPhi_ {i j}, \forall i, j \in \{1, 2, \dots , n \}.
$$

特别地, $\Phi_{ii}=0,\forall i\in\{1,2,\cdots,n\}$ .于是 $\Phi$ 可以表示为

$$
\varPhi = \sum_ {1 \leqslant i <   j \leqslant n} \varPhi_ {i j} \phi^ {i} \wedge \phi^ {j}, \tag {18.2.3}
$$

其中

$$
\phi^ {i} \wedge \phi^ {j} = \phi^ {i} \otimes \phi^ {j} - \phi^ {j} \otimes \phi^ {i}.
$$

$V$ 上反对称二次型的全体构成了一个向量空间, 记为 $\wedge^2 V^*$, 其维数为 $C_n^2$.

---

82

第十八章 微分形式简介

一般地, 若 $2 \leqslant q \leqslant n$, 考虑 $V$ 上的 $q$ 次型, 它们是定义在乘积空间 $V \times \cdots \times V (q$ 个 $V$ 的乘积) 上的函数且关于每一个分量都满足线性性. 例如, 当 $\{\psi^i\}_{i=1}^q \subset V^*$ 时, 定义 $q$ 次型 $\psi^1 \otimes \cdots \otimes \psi^q$ 如下:

$$
\psi^ {1} \otimes \dots \otimes \psi^ {q} (\boldsymbol {w} _ {1}, \dots , \boldsymbol {w} _ {q}) = \psi^ {1} (\boldsymbol {w} _ {1}) \dots \psi^ {q} (\boldsymbol {w} _ {q}), \forall \boldsymbol {w} _ {1}, \dots , \boldsymbol {w} _ {q} \in V.
$$

若 $\Theta$ 为 $V$ 上的 $q$ 次型, 则它可以表示为

$$
\Theta = \sum_ {i _ {1}, \dots , i _ {q} = 1} ^ {n} \Theta_ {i _ {1} \dots i _ {q}} \phi^ {i _ {1}} \otimes \dots \otimes \phi^ {i _ {q}}, \tag {18.2.4}
$$

其中

$$
\Theta_ {i _ {1} \dots i _ {q}} = \Theta (\boldsymbol {v} _ {i _ {1}}, \dots , \boldsymbol {v} _ {i _ {q}}).
$$

若 $\Theta$ 满足反对称性, 即

$$
\Theta (\dots , \boldsymbol {w}, \dots , \boldsymbol {v}, \dots) = - \Theta (\dots , \boldsymbol {v}, \dots , \boldsymbol {w}, \dots), \forall \boldsymbol {v}, \boldsymbol {w} \in V,
$$

则只有  $\{i_{1},\cdots,i_{q}\}$  互不相同时， $\Theta_{i_{1}\cdots i_{q}}$  才可能不为零，且当  $\tau$  为  $\{1,2,\cdots,q\}$  的置换时，有

$$
\Theta_ {i _ {\tau (1)} \dots i _ {\tau (q)}} = (- 1) ^ {\tau} \Theta_ {i _ {1} \dots i _ {q}},
$$

其中当 $\tau$ 为偶置换时 $(-1)^{\tau} = 1$; 当 $\tau$ 为奇置换时 $(-1)^{\tau} = -1$. 于是 $\Theta$ 可以表示为

$$
\Theta = \sum_ {i _ {1} <   \dots <   i _ {q}} \Theta_ {i _ {1} \dots i _ {q}} \phi^ {i _ {1}} \wedge \dots \wedge \phi^ {i _ {q}}, \tag {18.2.5}
$$

其中

$$
\phi^ {i _ {1}} \wedge \dots \wedge \phi^ {i _ {q}} = \sum_ {\tau \in S _ {q}} (- 1) ^ {\tau} \phi^ {i _ {\tau (1)}} \otimes \dots \otimes \phi^ {i _ {\tau (q)}}, \forall i _ {1}, \dots , i _ {q}. \tag {18.2.6}
$$

这里  $S_{q}$  表示  $\{1,2,\cdots,q\}$  的置换群.

$V$ 上具有反对称性的 $q$ 次型的全体构成了一个向量空间, 记为 $\wedge^q V^*$, 其维数为 $\mathrm{C}_n^q$. 为了方便起见, 记 $\wedge^0 V^* = \mathbb{R}, \wedge^1 V^* = V^*$. 记 $\wedge^* V^* = \oplus_{q=0}^n \wedge^q V^*$, 这是一个维数为 $2^n$ 的向量空间, 它上面还有一个外乘法运算 $\wedge$: 若 $\Theta^1 \in \wedge^p V^*, \Theta^2 \in \wedge^q V^*$, 则定义 $\Theta^1 \wedge \Theta^2 \in \wedge^{p+q} V^*$ 为

$$
\Theta^ {1} \wedge \Theta^ {2} = \sum_ {i _ {1} <   \dots <   i _ {p}} \sum_ {j _ {1} <   \dots <   j _ {q}} \Theta_ {i _ {1} \dots i _ {p}} ^ {1} \Theta_ {j _ {1} \dots j _ {q}} ^ {2} \phi^ {i _ {1}} \wedge \dots \wedge \phi^ {i _ {p}} \wedge \phi^ {j _ {1}} \wedge \dots \wedge \phi^ {j _ {q}}. \tag {18.2.7}
$$

从上式可以看出

$$
\Theta^ {1} \wedge \Theta^ {2} = (- 1) ^ {p q} \Theta^ {2} \wedge \Theta^ {1}, \tag {18.2.8}
$$

---

18.2 外代数和微分形式

83

这说明外乘法运算一般不满足交换律. 不过, 外乘法运算满足结合律:

$$
(\Theta^ {1} \wedge \Theta^ {2}) \wedge \Theta^ {3} = \Theta^ {1} \wedge (\Theta^ {2} \wedge \Theta^ {3}),
$$

因此在进行多次外乘法运算时一般省略括号. 当  $\{\psi^{i}\}_{i=1}^{q} \subset V^{*}, \{w_{i}\}_{i=1}^{q} \subset V$  时, 我们有如下计算公式:

$$
(\psi^ {1} \wedge \dots \wedge \psi^ {q}) (\boldsymbol {w} _ {1}, \dots , \boldsymbol {w} _ {q}) = \det \left(\psi^ {i} (\boldsymbol {w} _ {j})\right) _ {q \times q}. \tag {18.2.9}
$$

$^{*}V^{*}$  连同外乘法运算构成了一个代数, 称为 V 上的外代数. 外代数是 Grassmann $^{①}$  在 1844 年所发明的, 不过在之后相当长的一段时间内被忽视了, 很久以后人们才发现它在数学和物理中都有重要的应用.

下面我们将向量空间 $V$ 取为欧氏空间 $\mathbb{R}^n$. 首先有

命题 18.2.1 取  $V = R^{n}$ ，则  $V^{*} = \operatorname{span}\{\mathrm{d}x_{j}(\boldsymbol{p})\}_{j=1}^{n}$ ，其中  $x_{j}$  是  $R^{n}$  上的第 j 个坐标函数，p 是  $R^{n}$  上任意一点.

证明 我们来说明  $\{\mathrm{d}x_{j}(\boldsymbol{p})\}_{j=1}^{n}$  是标准正交基  $\{e_{i}\}_{i=1}^{n}$  的对偶基. 首先我们回顾, 当 f 是  $R^{n}$  上在 p 处可微的函数时, 它在 p 处的梯度  $\nabla f(\boldsymbol{p})$  定义为

$$
\nabla f (\boldsymbol {p}) = \left(\frac {\partial f}{\partial x _ {1}} (\boldsymbol {p}), \dots , \frac {\partial f}{\partial x _ {n}} (\boldsymbol {p})\right).
$$

此时，f 在 p 处的微分  $\mathrm{d}f(\boldsymbol{p})$  可以用梯度表示为

$$
\mathrm{d} f (\boldsymbol {p}): \mathbb {R} ^ {n} \to \mathbb {R}, \boldsymbol {u} \mapsto \nabla f (\boldsymbol {p}) \cdot \boldsymbol {u}.
$$

注意 $\nabla x_{j}\equiv e_{j}$ ，上式表明

$$
\mathrm{d} x _ {j} (\boldsymbol {p}) (\boldsymbol {e} _ {i}) = \boldsymbol {e} _ {j} \cdot \boldsymbol {e} _ {i} = \delta_ {j i} = \left\{ \begin{array}{l l} 1, & i = j, \\ 0, & i \neq j, \end{array} \right.
$$

这说明  $\{\mathrm{d}x_{j}(\boldsymbol{p})\}_{j=1}^{n}$  的确是标准正交基  $\{e_{i}\}_{i=1}^{n}$  的对偶基.

注 18.2.1 从上述证明可以看出  $\mathrm{d}x_{j}(\boldsymbol{p})$  与 p 无关, 下面我们将  $\mathrm{d}x_{j}(\boldsymbol{p})$  简记为  $dx_{j}$ .

由上述讨论可知

$$
\wedge^ {*} \left(\mathbb {R} ^ {n}\right) ^ {*} = \operatorname{span} \{1, \mathrm{d} x _ {i _ {1}} \wedge \dots \wedge \mathrm{d} x _ {i _ {q}} \mid 1 \leqslant i _ {1} <   \dots <   i _ {q} \leqslant n, 1 \leqslant q \leqslant n \}.
$$

为了方便起见, 记  $dx_{I} = dx_{i_{1}} \wedge \cdots \wedge dx_{i_{q}}$ , 其中  $I = \{i_{1}, \cdots, i_{q}\}$ ,  $i_{1} < \cdots < i_{q}$ . 当  $I = \varnothing$  时规定  $dx_{I} = 1$ . 设  $D \subseteq R^{n}$ , 从 D 到  $\wedge^{q}(\mathbb{R}^{n})^{*}$  的映射称为 D 上的 q-形式或 q 次微分形式. 显然, 0-形式就是 D 上的函数.

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">① Grassmann, Hermann Günther, 1809 年 4 月 15 日—1877 年 9 月 26 日, 德国数学家.</span></small>

---

84

第十八章 微分形式简介

例 18.2.1 可微函数的全微分.

设 f 为 D 上的可微函数, 其全微分 df 定义为

$$
\mathrm{d} f: U \to \left(\mathbb {R} ^ {n}\right) ^ {*}, \boldsymbol {p} \mapsto \mathrm{d} f (\boldsymbol {p}),
$$

这说明 $\mathrm{df}$ 是 $D$ 上的1-形式.由(18.2.1)式可知

$$
\mathrm{d} f (\boldsymbol {p}) = \sum_ {j = 1} ^ {n} \mathrm{d} f (\boldsymbol {p}) (\boldsymbol {e} _ {j}) \mathrm{d} x _ {j} = \sum_ {j = 1} ^ {n} \nabla f (\boldsymbol {p}) \cdot \boldsymbol {e} _ {j} \mathrm{d} x _ {j} = \sum_ {j = 1} ^ {n} \frac {\partial f}{\partial x _ {j}} (\boldsymbol {p}) \mathrm{d} x _ {j},
$$

即 $\mathrm{df}$ 可以表示为

$$
\mathrm{d} f = \sum_ {j = 1} ^ {n} \frac {\partial f}{\partial x _ {j}} \mathrm{d} x _ {j}.
$$

一般地, 设  $\omega$  为 q-形式, 当  $I=\{i_{1},\cdots,i_{q}\}$  时, 记

$$
\omega_ {I} = \omega (\boldsymbol {e} _ {i _ {1}}, \dots , \boldsymbol {e} _ {i _ {q}}),
$$

则 $\omega$ 可以表示为

$$
\omega = \sum_ {I} \omega_ {I} \mathrm{d} x _ {I} = \sum_ {i _ {1} <   \dots <   i _ {q}} \omega_ {i _ {1} \dots i _ {q}} \mathrm{d} x _ {i _ {1}} \wedge \dots \wedge \mathrm{d} x _ {i _ {q}}, \tag {18.2.10}
$$

当  $\omega_{I}$  均为  $C^{k}$  函数时, 称  $\omega$  为  $C^{k}$  的 q-形式.

设 $\omega, \eta$ 为 $q$-形式, 它们逐点相加的和 $\omega + \eta$ 也是 $q$-形式. 类似地, 设 $f, g$ 为函数, 则 $f\omega + g\eta$ 为 $q$-形式, 它在 $x$ 处的值为 $f(x)\omega(x) + g(x)\eta(x)$.

设 $\omega, \eta$ 分别为 $p$-形式和 $q$-形式, 它们可以表示为

$$
\omega = \sum_ {I} \omega_ {I} \mathrm{d} x _ {I}, \eta = \sum_ {J} \eta_ {J} \mathrm{d} x _ {J}.
$$

令

$$
\omega \wedge \eta = \sum_ {I} \sum_ {J} \omega_ {I} \eta_ {J} \mathrm{d} x _ {I} \wedge \mathrm{d} x _ {J},
$$

则 $\omega \wedge \eta$ 为 $(p + q)$ -形式. 下列性质可以直接验证:

\- 设 $\omega_{1},\omega_{2}$ 为 $p$ -形式, $\eta$ 为 $q$ -形式, $f_{1},f_{2}$ 为函数, 则

$$
(f _ {1} \omega_ {1} + f _ {2} \omega_ {2}) \wedge \eta = f _ {1} (\omega_ {1} \wedge \eta) + f _ {2} (\omega_ {2} \wedge \eta).
$$

\- 设 $\omega, \eta$ 分别为 $p$-形式和 $q$-形式, 则

$$
\omega \wedge \eta = (- 1) ^ {p q} \eta \wedge \omega .
$$

---

18.2 外代数和微分形式

85

\- 设 $\omega, \eta, \zeta$ 分别为 $p$-形式, $q$-形式和 $r$-形式, 则

$$
(\omega \land \eta) \land \zeta = \omega \land (\eta \land \zeta),
$$

因此, 上式中的括号通常可以省略.

例 18.2.2 体积形式和坐标变换.

在  $R^{n}$  上, 记  $dx = dx_{1} \wedge \cdots \wedge dx_{n}$ . dx 为 n-形式, 称为  $R^{n}$  的体积形式. 设  $D \subseteq R^{n}$  为开集,  $\varphi : D \to R^{n}$  为可微映射, 它的第 i 个分量记为  $\varphi_{i}$ . 我们有

$$
\begin{array}{l} \mathrm{d} \varphi_ {1} \wedge \dots \wedge \mathrm{d} \varphi_ {n} = \left(\sum_ {j = 1} ^ {n} \frac {\partial \varphi_ {1}}{\partial x _ {j}} \mathrm{d} x _ {j}\right) \wedge \dots \wedge \left(\sum_ {j = 1} ^ {n} \frac {\partial \varphi_ {n}}{\partial x _ {j}} \mathrm{d} x _ {j}\right) \\ = \sum_ {1 \leqslant j _ {1}, \dots , j _ {n} \leqslant n} \frac {\partial \varphi_ {1}}{\partial x _ {j _ {1}}} \dots \frac {\partial \varphi_ {n}}{\partial x _ {j _ {n}}} \mathrm{d} x _ {j _ {1}} \wedge \dots \wedge \mathrm{d} x _ {j _ {n}}. \\ \end{array}
$$

注意到只有  $j_{1},\cdots,j_{n}$  互不相同时  $dx_{j_{1}}\wedge\cdots\wedge dx_{j_{n}}$  才不等于零. 若用  $S_{n}$  表示  $\{1,2,\cdots,n\}$  的置换群, 则

$$
\begin{array}{l} \mathrm{d} \varphi_ {1} \wedge \dots \wedge \mathrm{d} \varphi_ {n} = \sum_ {\tau \in S _ {n}} \frac {\partial \varphi_ {1}}{\partial x _ {\tau (1)}} \dots \frac {\partial \varphi_ {n}}{\partial x _ {\tau (n)}} \mathrm{d} x _ {\tau (1)} \wedge \dots \wedge \mathrm{d} x _ {\tau (n)} \\ = \sum_ {\tau \in S _ {n}} (- 1) ^ {\tau} \frac {\partial \varphi_ {1}}{\partial x _ {\tau (1)}} \dots \frac {\partial \varphi_ {n}}{\partial x _ {\tau (n)}} \mathrm{d} x _ {1} \wedge \dots \wedge \mathrm{d} x _ {n} \\ = \frac {\partial (\varphi_ {1} , \cdots , \varphi_ {n})}{\partial (x _ {1} , \cdots , x _ {n})} \mathrm{d} x _ {1} \wedge \dots \wedge \mathrm{d} x _ {n}. \\ \end{array}
$$

上式和重积分的变量替换公式很像, 区别在于这里的 Jacobi 行列式没有绝对值. □

设 $U \subseteq \mathbb{R}^n$, $\omega$ 是 $U$ 上的 $n$-形式, 它可以表示为

$$
\omega = f (\boldsymbol {x}) \mathrm{d} x _ {1} \wedge \dots \wedge \mathrm{d} x _ {n},
$$

其中 $f$ 是定义在 $U$ 上的函数. 我们规定 $\omega$ 在 $U$ 上的积分等于函数 $f$ 在 $U$ 上的 (广义) Riemann 积分 (假定此积分有意义), 记为

$$
\int_ {U} \omega = \int_ {U} f (\pmb {x}) \mathrm{d} \pmb {x} = \int_ {U} f (\pmb {x}) \mathrm{d} x _ {1} \dots \mathrm{d} x _ {n}.
$$

如果 $\varphi : D \to U$ 是保定向 (Jacobi行列式恒为正) 的微分同胚, 则由变量替换公式可得

$$
\int_ {D} \varphi^ {*} \omega = \int_ {\varphi (D)} \omega = \int_ {U} \omega ,
$$

这称为积分的形式不变性.

---

86

第十八章 微分形式简介

## 习题18.2

1. 设 $V$ 是实数域上的 $n$ 维向量空间, 在 $V$ 中取两组基 $\{\pmb{v}_i\}_{i=1}^n, \{\pmb{w}_j\}_{j=1}^n$, 相应的对偶基分别为 $\{\phi^i\}_{i=1}^n, \{\psi^j\}_{j=1}^n$. 设 $\pmb{w}_j = \sum_{i=1}^{n} a_j^i \pmb{v}_i$, 求两组对偶基之间的转换关系.

2. 沿用上一题中的记号, 设 $\Theta \in \wedge^q V^*$ 可以表示为

$$
\Theta = \sum_ {i _ {1} <   \dots <   i _ {q}} \Theta_ {i _ {1} \dots i _ {q}} \phi^ {i _ {1}} \wedge \dots \wedge \phi^ {i _ {q}}, \quad \Theta = \sum_ {j _ {1} <   \dots <   j _ {q}} \tilde {\Theta} _ {j _ {1} \dots j _ {q}} \psi^ {j _ {1}} \wedge \dots \wedge \psi^ {j _ {q}},
$$

求系数  $\tilde{\Theta}_{j_{1}\cdots j_{q}}$  和  $\Theta_{i_{1}\cdots i_{q}}$  之间的转换关系式.

3. 验证外代数的外乘积运算与向量空间中基的选取无关.

4. 设  $\phi^{1},\cdots,\phi^{q}\in(\mathbb{R}^{n})^{*},\phi^{i}=\sum_{j=1}^{n}a_{j}^{i}\mathrm{d}x_{j}$ . 证明:

$$
\phi^ {1} \wedge \dots \wedge \phi^ {q} = \sum_ {1 \leqslant k _ {1} <   \dots <   k _ {q} \leqslant n} \det \left(a _ {k _ {j}} ^ {i}\right) _ {q \times q} \mathrm{d} x _ {k _ {1}} \wedge \dots \wedge \mathrm{d} x _ {k _ {q}}.
$$

5. 化简下列表达式:

(1) $(x\mathrm{d}x+y\mathrm{d}y)\wedge(z\mathrm{d}z-z\mathrm{d}x);$
(2) $(\mathrm{dx} + \mathrm{dy} + \mathrm{dz}) \wedge (x\mathrm{dx} \wedge \mathrm{dy} - y\mathrm{dy} \wedge \mathrm{dz})$.

6. 设  $\omega = dx_{1} \wedge dx_{2} + dx_{3} \wedge dx_{4}.$

(1) 化简  $\omega \wedge \omega;$
(2) 证明: 不存在两个 1-形式 $\alpha, \beta$, 使得 $\alpha \wedge \beta = \omega$.

7. 设

$$
\begin{array}{l} \omega = x _ {1} \mathrm{d} x _ {2} + x _ {2} \mathrm{d} x _ {3} + x _ {3} \mathrm{d} x _ {1}, \\ \eta = x _ {1} x _ {2} \mathrm{d} x _ {1} \wedge \mathrm{d} x _ {2} + x _ {2} x _ {3} \mathrm{d} x _ {2} \wedge \mathrm{d} x _ {3} + x _ {3} x _ {1} \mathrm{d} x _ {3} \wedge \mathrm{d} x _ {1}. \\ \end{array}
$$

通过计算判断  $\omega \wedge \eta$  与  $\eta \wedge \omega$  是否相同.

8. 设  $(x,y)$  为  $R^{2}$  上的直角坐标,  $(r,\theta)$  为极坐标, 证明:  $dx \wedge dy = r dr \wedge d\theta$ .

9. 设  $(x, y, z)$  为  $R^{3}$  上的直角坐标,  $(r, \theta, \varphi)$  为球坐标, 其中

$$
x = r \sin \theta \cos \varphi , y = r \sin \theta \sin \varphi , z = r \cos \theta,
$$

通过计算证明: $\mathrm{dx} \wedge \mathrm{dy} \wedge \mathrm{dz} = r^{2} \sin \theta \mathrm{dr} \wedge \mathrm{d}\theta \wedge \mathrm{d}\varphi$.

10. 设  $\{f_{i}\}_{i=1}^{n-1}$  为  $R^{n}$  上的  $C^{1}$  函数, 证明:

$$
\mathrm{d} f _ {1} \wedge \dots \wedge \mathrm{d} f _ {n - 1} = \sum_ {j = 1} ^ {n} \frac {\partial (f _ {1} , \cdots , f _ {n - 1})}{\partial (x _ {1} , \cdots , \widehat {x _ {j}} , \cdots , x _ {n})} \mathrm{d} x _ {1} \wedge \dots \wedge \widehat {\mathrm{d} x _ {j}} \wedge \dots \wedge \mathrm{d} x _ {n}.
$$

---

18.3 拉回映射和外微分运算

87

## 18.3 拉回映射和外微分运算

微分形式在坐标变换下的变换规律可以用所谓的拉回映射来描述. 我们仍然从线性代数开始讨论. 设 $L: \mathbb{R}^n \to \mathbb{R}^m$ 为线性映射, 它诱导了相应的对偶空间之间的线性映射 $L^*: (\mathbb{R}^m)^* \to (\mathbb{R}^n)^*$: 当 $\phi \in (\mathbb{R}^m)^*$ 时令 $L^*\phi = \phi \circ L$. 一般地, 设 $\Theta \in \wedge^q(\mathbb{R}^m)^*$, 则定义 $L^*\Theta \in \wedge^q(\mathbb{R}^n)^*$ 为

$$
\boldsymbol {L} ^ {*} \Theta (\boldsymbol {u} ^ {1}, \dots , \boldsymbol {u} ^ {q}) = \Theta \big (\boldsymbol {L} (\boldsymbol {u} ^ {1}), \dots , \boldsymbol {L} (\boldsymbol {u} ^ {q}) \big), \forall \boldsymbol {u} ^ {1}, \dots , \boldsymbol {u} ^ {q} \in \mathbb {R} ^ {n}.
$$

$L^{*}$  称为由 L 所诱导的拉回映射. 当  $\phi^{1},\cdots,\phi^{q}\in\left(\mathbb{R}^{m}\right)^{*}$  时, 显然有

$$
\boldsymbol {L} ^ {*} (\phi^ {1} \otimes \dots \otimes \phi^ {q}) = \boldsymbol {L} ^ {*} \phi^ {1} \otimes \dots \otimes \boldsymbol {L} ^ {*} \phi^ {q}.
$$

由(18.2.6)式可得

$$
\boldsymbol {L} ^ {*} (\phi^ {1} \wedge \dots \wedge \phi^ {q}) = \boldsymbol {L} ^ {*} \phi^ {1} \wedge \dots \wedge \boldsymbol {L} ^ {*} \phi^ {q}.
$$

设 $U \subseteq \mathbb{R}^n$ 为开集, $\varphi: U \to \mathbb{R}^m$ 为可微映射, 它在 $x \in U$ 处的微分记为 $\varphi_{*x} = \mathrm{d}\varphi(x)$. 如果 $\omega$ 为 $\mathbb{R}^m$ 上的 $q$-形式, 则 $\varphi^{*}\omega$ 为 $U$ 上的 $q$-形式, 它在 $x$ 处的值定义为

$$
\varphi_ {* \boldsymbol {x}} ^ {*} [ \omega (\varphi (\boldsymbol {x})) ] \in \wedge^ {q} \left(\mathbb {R} ^ {n}\right) ^ {*}.
$$

$\varphi^{*}$ 称为由 $\varphi$ 所诱导的拉回映射, 它具有下列性质:

- 设 $\omega, \eta$ 均为 $q$-形式, 则 $\varphi^{*}(\omega + \eta) = \varphi^{*}\omega + \varphi^{*}\eta$.
- 设 $\omega$ 为 $q$-形式, $f$ 为函数, 则 $\varphi^{*}(f\omega) = f(\varphi)\varphi^{*}\omega$.
- 设 $f$ 为可微函数, 则 $\varphi^{*}(\mathrm{d}f) = \mathrm{d}[f(\varphi)]$. 事实上, 在任意一点 $\pmb{x}$ 处, 成立

$$
\varphi^ {*} (\mathrm{d} f) (\boldsymbol {x}) = \mathrm{d} f (\varphi (\boldsymbol {x})) \circ \varphi_ {* \boldsymbol {x}} = \mathrm{d} f (\varphi (\boldsymbol {x})) \circ \mathrm{d} \varphi (\boldsymbol {x}) = \mathrm{d} [ f (\varphi) ] (\boldsymbol {x}),
$$

其中我们用到了链式法则.特别地， $\varphi^{*}(\mathrm{d}x_{i})=\mathrm{d}\varphi_{i}$ ，其中  $\varphi_{i}=x_{i}\circ\varphi$  是  $\varphi$  的第 i 个分量.

\- 设 $\omega$ 为 $q$-形式, 由 (18.2.10) 式所表示, 则

$$
\varphi^ {*} \omega = \sum_ {i _ {1} <   \dots <   i _ {q}} \omega_ {i _ {1} \dots i _ {q}} (\varphi) \mathrm{d} \varphi_ {i _ {1}} \wedge \dots \wedge \mathrm{d} \varphi_ {i _ {q}}.
$$

- 设 $\omega, \eta$ 分别为 $p$-形式和 $q$-形式, 则 $\varphi^{*}(\omega \wedge \eta) = \varphi^{*}\omega \wedge \varphi^{*}\eta$.
- 设 $\varphi$ 如上, $\psi: \mathbb{R}^m \to \mathbb{R}^k$ 也为可微映射, $\omega$ 为 $\mathbb{R}^k$ 上的 $q$-形式, 则 $(\psi \circ \varphi)^*\omega = \varphi^*(\psi^*\omega)$.

利用拉回映射, 例 18.2.2 的结果可以简单地写为 $\varphi^{*}(\mathrm{d}\boldsymbol{x}) = (\det J\varphi)\mathrm{d}\boldsymbol{x}$. 特别地, 如果 $\varphi, \psi$ 均为 $\mathbb{R}^n$ 到自身的线性变换, 其矩阵表示分别为 $A, B$, 则

$$
\varphi^ {*} (\mathrm{d} \boldsymbol {x}) = (\det \boldsymbol {A}) \mathrm{d} \boldsymbol {x}, \quad \psi^ {*} (\mathrm{d} \boldsymbol {x}) = (\det \boldsymbol {B}) \mathrm{d} \boldsymbol {x}.
$$

---

88

第十八章 微分形式简介

复合映射  $\psi\circ\varphi$  的矩阵表示为 BA, 因此有

$$
\det (\boldsymbol {B} \boldsymbol {A}) \mathrm{d} \boldsymbol {x} = (\psi \circ \varphi) ^ {*} (\mathrm{d} \boldsymbol {x}) = \varphi^ {*} (\psi^ {*} (\mathrm{d} \boldsymbol {x})) = (\det \boldsymbol {B}) \varphi^ {*} (\mathrm{d} \boldsymbol {x}) = (\det \boldsymbol {B}) (\det \boldsymbol {A}) \mathrm{d} \boldsymbol {x},
$$

这就得到了线性代数中熟知的等式  $\det(B\boldsymbol{A})=(\det\boldsymbol{B})(\det\boldsymbol{A})$ .

我们知道, 给定可微函数 $f$, 它的全微分 $\mathrm{d}f$ 为 1-形式. 给定 $\mathbb{R}^n$ 上的 $q$-形式 $\omega$, 我们要定义一个 $(q + 1)$-形式, 它由 $\omega$ 求导得到, 记为 $\mathrm{d}\omega$.

设 $\omega$ 为 $C^k (k\geqslant 1)$ 的 $q-$ 形式，它可以表示为

$$
\omega = \sum_ {1 \leqslant i _ {1} <   \dots <   i _ {q} \leqslant n} \omega_ {i _ {1} \dots i _ {q}} \mathrm{d} x _ {i _ {1}} \wedge \dots \wedge \mathrm{d} x _ {i _ {q}},
$$

我们定义

$$
\mathrm{d} \omega = \sum_ {1 \leqslant i _ {1} <   \dots <   i _ {q} \leqslant n} \mathrm{d} \omega_ {i _ {1} \dots i _ {q}} \wedge \mathrm{d} x _ {i _ {1}} \wedge \dots \wedge \mathrm{d} x _ {i _ {q}}.
$$

显然, $\mathrm{d}\omega$ 为 $(q + 1)$-形式, 称为 $\omega$ 的外微分. 注意, 当 $q = n$ 时, 规定 $\mathrm{d}\omega = 0$.

例 18.3.1  $R^{2}$  上 1-形式的外微分.

设  $\omega = P(x, y) \, dx + Q(x, y) \, dy$  为  $R^{2}$  上的 1-形式, 则

$$
\begin{array}{l} \mathrm{d} \omega = \mathrm{d} P \wedge \mathrm{d} x + \mathrm{d} Q \wedge \mathrm{d} y \\ = (P _ {x} \mathrm{d} x + P _ {y} \mathrm{d} y) \wedge \mathrm{d} x + (Q _ {x} \mathrm{d} x + Q _ {y} \mathrm{d} y) \wedge \mathrm{d} y \\ = (Q _ {x} - P _ {y}) \mathrm{d} x \wedge \mathrm{d} y, \\ \end{array}
$$

其中我们用到了

$$
\mathrm{d} x \wedge \mathrm{d} x = \mathrm{d} y \wedge \mathrm{d} y = 0, \mathrm{d} y \wedge \mathrm{d} x = - \mathrm{d} x \wedge \mathrm{d} y.
$$

例 18.3.2  $R^{3}$  上 1-形式的外微分.

设 $\omega = P(x,y,z)\mathrm{d}x + Q(x,y,z)\mathrm{d}y + R(x,y,z)\mathrm{d}z$ 为1-形式,则

$$
\begin{array}{l} \mathrm{d} \omega = \mathrm{d} P \wedge \mathrm{d} x + \mathrm{d} Q \wedge \mathrm{d} y + \mathrm{d} R \wedge \mathrm{d} z \\ = (P _ {x} \mathrm{d} x + P _ {y} \mathrm{d} y + P _ {z} \mathrm{d} z) \wedge \mathrm{d} x + (Q _ {x} \mathrm{d} x + Q _ {y} \mathrm{d} y + Q _ {z} \mathrm{d} z) \wedge \mathrm{d} y + \\ (R _ {x} \mathrm{d} x + R _ {y} \mathrm{d} y + R _ {z} \mathrm{d} z) \wedge \mathrm{d} z \\ = (R _ {y} - Q _ {z}) \mathrm{d} y \wedge \mathrm{d} z + (P _ {z} - R _ {x}) \mathrm{d} z \wedge \mathrm{d} x + (Q _ {x} - P _ {y}) \mathrm{d} x \wedge \mathrm{d} y. \\ \end{array}
$$

例 18.3.3  $R^{3}$  上 2-形式的外微分.

设  $R^{3}$  上的 2-形式可以表示为

$$
\omega = P (x, y, z) \mathrm{d} y \wedge \mathrm{d} z + Q (x, y, z) \mathrm{d} z \wedge \mathrm{d} x + R (x, y, z) \mathrm{d} x \wedge \mathrm{d} y,
$$

---

18.3 拉回映射和外微分运算

89

则

$$
\begin{array}{l} \mathrm{d} \omega = \mathrm{d} P \wedge \mathrm{d} y \wedge \mathrm{d} z + \mathrm{d} Q \wedge \mathrm{d} z \wedge \mathrm{d} x + \mathrm{d} R \wedge \mathrm{d} x \wedge \mathrm{d} y \\ = P _ {x} \mathrm{d} x \wedge \mathrm{d} y \wedge \mathrm{d} z + Q _ {y} \mathrm{d} y \wedge \mathrm{d} z \wedge \mathrm{d} x + R _ {z} \mathrm{d} z \wedge \mathrm{d} x \wedge \mathrm{d} y \\ = (P _ {x} + Q _ {y} + R _ {z}) \mathrm{d} x \wedge \mathrm{d} y \wedge \mathrm{d} z. \\ \end{array}
$$

从上述例子可以看出, Green 公式、Gauss 公式和 Stokes 公式可以写成统一的形式:

$$
\int_ {D} \mathrm{d} \omega = \int_ {\partial D} \omega .
$$

我们将 d 称为外微分算子, 它具有以下性质:

- 设 $\omega, \eta$ 为 $q$-形式, $\lambda, \mu \in \mathbb{R}$, 则 $\mathrm{d}(\lambda \omega + \mu \eta) = \lambda \mathrm{d}\omega + \mu \mathrm{d}\eta$.
- 设 $f$ 为函数, $\omega$ 为 $q$-形式, 则 $\mathrm{d}(f\omega) = \mathrm{d}f \wedge \omega + f \mathrm{d}\omega$.
- 设 $\omega, \eta$ 分别为 $p$-形式和 $q$-形式, 则

$$
\mathrm{d} (\omega \wedge \eta) = \mathrm{d} \omega \wedge \eta + (- 1) ^ {p} \omega \wedge \mathrm{d} \eta.
$$

\- $\mathrm{d}^2 = 0$ ，即 $\mathrm{d}(\mathrm{d}\omega) = 0$ 。先考虑0-形式。设 $f$ 为 $C^k (k\geqslant 2)$ 函数，则

$$
\begin{array}{l} \mathrm{d} ^ {2} f = \mathrm{d} (\mathrm{d} f) = \mathrm{d} \left(\sum_ {i = 1} ^ {n} \frac {\partial f}{\partial x _ {i}} \mathrm{d} x _ {i}\right) \\ = \sum_ {i = 1} ^ {n} \mathrm{d} \left(\frac {\partial f}{\partial x _ {i}}\right) \wedge \mathrm{d} x _ {i} = \sum_ {i, j = 1} ^ {n} \frac {\partial^ {2} f}{\partial x _ {i} \partial x _ {j}} \mathrm{d} x _ {j} \wedge \mathrm{d} x _ {i} \\ = \sum_ {i <   j} \left(\frac {\partial^ {2} f}{\partial x _ {i} \partial x _ {j}} - \frac {\partial^ {2} f}{\partial x _ {j} \partial x _ {i}}\right) \mathrm{d} x _ {j} \wedge \mathrm{d} x _ {i} = 0, \\ \end{array}
$$

其中我们用到了求导次序的可交换性.对于 q-形式，以  $\omega = f \, dx_{i_1} \wedge \cdots \wedge dx_{i_q}$  为例，此时

$$
\mathrm{d} \omega = \mathrm{d} f \wedge \mathrm{d} x _ {i _ {1}} \wedge \dots \wedge \mathrm{d} x _ {i _ {q}}.
$$

根据  $d^{2}f=0$  和前一条性质可知  $d^{2}\omega=0$ .

\- $\mathrm{d}(\varphi^{*}\omega) = \varphi^{*}\mathrm{d}\omega$. 仍设 $\omega = f\mathrm{d}x_{i_1}\wedge \dots \wedge \mathrm{d}x_{i_q}$, 则

$$
\mathrm{d} (\varphi^ {*} \omega) = \mathrm{d} (f (\varphi) \mathrm{d} \varphi_ {i _ {1}} \wedge \dots \wedge \mathrm{d} \varphi_ {i _ {q}}) = \mathrm{d} (f (\varphi)) \wedge \mathrm{d} \varphi_ {i _ {1}} \wedge \dots \wedge \mathrm{d} \varphi_ {i _ {q}}.
$$

根据拉回映射的性质,  $\mathrm{d}(f(\varphi))=\varphi^{*}(\mathrm{d}f)$ , 代入上式即得欲证等式.

如果 $\mathrm{d}\omega = 0$ ，则称 $\omega$ 为闭形式；如果 $\omega = \mathrm{d}\eta$ ，则称 $\omega$ 为恰当形式.由 $\mathrm{d}^2 = 0$ 可知恰当形式必为闭形式，反之不然.

例 18.3.4  $R^{2} \setminus \{0\}$  上的一个非恰当的闭形式.

---

90

第十八章 微分形式简介

考虑 $\mathbb{R}^2\setminus \{\mathbf{0}\}$ 上的如下1-形式

$$
\omega = \frac {x}{x ^ {2} + y ^ {2}} \mathrm{d} y - \frac {y}{x ^ {2} + y ^ {2}} \mathrm{d} x,
$$

直接的计算表明 $\mathrm{d}\omega = 0$ ，即 $\omega$ 为闭形式.如果用极坐标 $(r,\theta)$ 表示，则由

$$
\mathrm{d} x = \cos \theta \mathrm{d} r - r \sin \theta \mathrm{d} \theta , \quad \mathrm{d} y = \sin \theta \mathrm{d} r + r \cos \theta \mathrm{d} \theta
$$

可得 $\omega = \mathrm{d}\theta$. 不过, 这个等式并不表明 $\omega$ 是恰当形式, 因为 $\theta$ 不能定义在整个 $\mathbb{R}^2 \setminus \{\mathbf{0}\}$ 上. 事实上, 不存在 $\mathbb{R}^2 \setminus \{\mathbf{0}\}$ 上的函数 $f$, 使得 $\omega = \mathrm{d}f$. (反证法) 如果这样的 $f$ 存在, 则 $\omega$ 沿单位圆周 (逆时针方向) 积分为零. 另一方面, 直接的计算表明此积分等于 $2\pi$. □一般地, 设 $U \subseteq \mathbb{R}^n$ 为开集, 考虑商空间

$$
H _ {d R} ^ {q} (U) = \{U \text {上的} q \text {次闭形式} \} / \{U \text {上的} q \text {次恰当形式} \},
$$

它是实数域上的向量空间 (因而是加法群), 称为 $U$ 的 $q$ 次 de Rham 上同调群. de Rham 上同调群刻画了 $U$ 是否连通或里面有没有洞. 例如, $H_{dR}^{1}(\mathbb{R}^{2} \setminus \{\mathbf{0}\}) = \mathbb{R}$, 这代表着平面上被挖去了一个点. 再如, 虽然 $H_{dR}^{1}(\mathbb{R}^{3} \setminus \{\mathbf{0}\}) = 0$, 但 $H_{dR}^{2}(\mathbb{R}^{3} \setminus \{\mathbf{0}\}) = \mathbb{R}$, 说明空间里面确实有洞.

## 习题18.3

1. 在 $\mathbb{R}^{2n}$ 中定义 2-形式 $\omega$ 为

$$
\omega = \sum_ {i = 1} ^ {n} \mathrm{d} x _ {i} \wedge \mathrm{d} x _ {n + i}.
$$

记  $\omega^{n}=\omega\wedge\cdots\wedge\omega$  (n 个  $\omega$ ), 证明:

$$
\omega^ {n} = (- 1) ^ {\frac {n (n - 1)}{2}} n! \mathrm{d} x _ {1} \wedge \mathrm{d} x _ {2} \wedge \dots \wedge \mathrm{d} x _ {2 n}.
$$

2. 沿用上一题中的记号. 设 $\varphi: \mathbb{R}^{2n} \to \mathbb{R}^{2n}$ 为线性变换, 若 $\varphi^{*}\omega = \omega$, 则称 $\varphi$ 为辛变换. 证明: 辛变换的行列式等于 1.

3. 计算下列微分形式的外微分:

(1) $\omega = y\mathrm{d}x + x\mathrm{d}z;$

(2) $\omega = x^{2}y\mathrm{d}x - yze^{x}\mathrm{d}y;$

(3) $\omega = xy\mathrm{d}y\wedge \mathrm{d}z + yz\mathrm{d}z\wedge \mathrm{d}x + zx\mathrm{d}x\wedge \mathrm{d}y.$

4. 利用 $\mathrm{df} = 0$ 当且仅当 $f$ 为局部常值函数解下列方程:

(1)  $e^{y} \, dx + (xe^{y} + 2y) \, dy = 0;$

(2) $(7x + 3y)\mathrm{d}x + (3x - 5y)\mathrm{d}y = 0.$

5. 设 $\omega$ 为 $p$-形式, $\eta$ 为 $q$-形式, 则

$$
\mathrm{d} (\omega \wedge \eta) = \mathrm{d} \omega \wedge \eta + (- 1) ^ {p} \omega \wedge \mathrm{d} \eta .
$$

---

18.4 Brouwer 不动点定理

91

6. 设 P, Q 是平面区域上的  $C^{2}$  函数且  $P^{2} + Q^{2} \equiv 1$ . 证明: P dQ 是闭的 1-形式.

7. 设  $\{f_{i}\}_{i=1}^{q}$  为  $R^{n}$  上的  $C^{2}$  函数, 证明:  $df_{1} \wedge \cdots \wedge df_{g}$  是闭形式.

8. 构造一个  $(n-1)$ -形式  $\omega$ ，使得

$$
\mathrm{d} \omega = \mathrm{d} x _ {1} \wedge \mathrm{d} x _ {2} \wedge \dots \wedge \mathrm{d} x _ {n}.
$$

9. 设  $\omega = yzdy \wedge dz + zxyzdz \wedge dz + xydx \wedge dy.$

(1) 证明: $\omega$ 是 $\mathbb{R}^3$ 中的闭形式;
(2) 构造一个 1-形式  $\eta$ ，使得  $\omega = d\eta$ .

10. 设  $f: R^{2} \rightarrow R$  为  $C^{2}$  函数, 且  $\Delta f = 0$ . 证明:

(1)  $\omega = \frac{\partial f}{\partial x} dy - \frac{\partial f}{\partial y} dx$  为闭形式;

(2) 存在函数  $g: R^{2} \rightarrow R$ ，使得

$$
\frac {\partial f}{\partial x} = \frac {\partial g}{\partial y}, \quad \frac {\partial f}{\partial y} = - \frac {\partial g}{\partial x}.
$$

## 18.4 Brouwer 不动点定理

我们知道, Green 公式和 Gauss 公式都可以写成散度定理的形式, 它们也可以用微分形式来描述. 下面我们用微分形式的积分来重新表述  $R^{n}$  中的散度定理.

我们先回顾参数超曲面上的积分. 设 $U \subseteq \mathbb{R}^{n-1}$ 为开集, $\psi: U \to \mathbb{R}^n$ 是 $C^1$ 映射. 若 $\psi$ 为单射且 $\operatorname{rank} J\psi \equiv n-1$, 则称 $\Sigma = \psi(U)$ 为参数超曲面, $\psi$ 称为 $\Sigma$ 的一个参数化映射 (参数表示). 若 $\eta$ 在 $\Sigma$ 的某个开邻域中有定义的 $(n-1)$-形式, 则记

$$
\int_ {\Sigma} \eta = \int_ {U} \psi^ {*} \eta .
$$

具体来说, 记  $\eta=\sum_{i=1}^{n}(-1)^{i-1}f_{i}\mathrm{d}x_{1}\wedge\cdots\wedge\widehat{\mathrm{d}x_{i}}\wedge\cdots\wedge\mathrm{d}x_{n}$ , 则

$$
\int_ {\Sigma} \eta = \int_ {U} \sum_ {i = 1} ^ {n} (- 1) ^ {i - 1} f _ {i} (\psi) \frac {\partial (\psi_ {1} , \cdots , \widehat {\psi} _ {i} , \cdots , \psi_ {n})}{\partial (u _ {1} , \cdots , u _ {n - 1})} \mathrm{d} u _ {1} \dots \mathrm{d} u _ {n - 1}, \tag {18.4.1}
$$

其中

$$
\boldsymbol {\psi} (\boldsymbol {u}) = (\psi_ {1} (\boldsymbol {u}), \dots , \psi_ {n} (\boldsymbol {u})), \quad \boldsymbol {u} = (u _ {1}, \dots , u _ {n - 1}) \in U.
$$

记  $\boldsymbol{X}=(f_{1},\cdots,f_{n}),\boldsymbol{N}_{\psi}=\boldsymbol{\psi}_{u_{1}}\times\cdots\times\boldsymbol{\psi}_{u_{n-1}}$ ，则 (18.4.1) 式可以改写为

$$
\int_ {\Sigma} \eta = \int_ {U} \boldsymbol {X} (\psi) \cdot \boldsymbol {N} _ {\psi} \mathrm{d} u _ {1} \dots \mathrm{d} u _ {n - 1}. \tag {18.4.2}
$$

---

92

第十八章 微分形式简介

不过, 上式右边的积分可能会依赖于参数化映射 $\psi$ 的选取. 若 $\phi: D \to U$ 为微分同胚, 记 $\varphi = \psi \circ \phi$, 则由链式法则可知 $N_{\varphi} = N_{\psi} \det J \phi$. 由变量替换公式可知, 当 $\phi$ 保定向时上述积分才具有不变性. 为了让微分形式 $\eta$ 在 $\Sigma$ 上的积分有意义, 我们必须给 $\Sigma$ 规定一个所谓的方向, 它由单位法向量 $n$ 给出. 在利用参数化映射 $\psi$ 定义微分形式的积分时, 我们要求法向量 $N_{\psi}$ 与给定的单位法向量 $n$ 同向, 即 $n = N_{\psi} \| N_{\psi} \|^{-1}$. 否则微分形式的积分会多出一个负号. 当 $N_{\psi}$ 与 $n$ 同向时, (18.4.2) 式可以表示为

$$
\int_ {\Sigma} \eta = \int_ {U} \boldsymbol {X} (\psi) \cdot \boldsymbol {n} (\psi) \| \boldsymbol {N} _ {\psi} \| \mathrm{d} u _ {1} \dots \mathrm{d} u _ {n - 1} = \int_ {\Sigma} \boldsymbol {X} \cdot \boldsymbol {n} \mathrm{d} \sigma , \tag {18.4.3}
$$

其中  $d\sigma$  是  $\Sigma$  上的面积元.

设 $\Omega$ 是 $\mathbb{R}^n$ 中具有 $C^1$ 边界的有界开集, 我们要在 $\partial \Omega$ 上定义微分形式的积分. 由定义18.1.1可知 $\partial \Omega$ 在局部上均为参数超曲面. 利用单位分解可以将局部上的积分整合成 $\Omega$ 上的积分. 设 $\{U_i\}_{i=1}^k$ 为 $\partial \Omega$ 是开覆盖, 使得每一个 $U_i \cap \partial \Omega$ 均为参数超曲面. 此时 $\{\Omega, U_i \mid 1 \leqslant i \leqslant k\}$ 是 $\bar{\Omega}$ 的开覆盖, 取从属于此开覆盖的单位分解 $\{\phi_0, \phi_i \mid 1 \leqslant i \leqslant k\}$. 设 $\eta$ 是在 $\bar{\Omega}$ 的某个开邻域上有定义的 $(n-1)$-形式, 记

$$
\int_ {\partial \Omega} \eta = \sum_ {i = 1} ^ {k} \int_ {U _ {i} \cap \partial \Omega} \phi_ {i} \eta ,
$$

其中 $\Omega$ 的方向由单位外法向量决定. 注意 $\phi_0\eta$ 在 $\partial \Omega$ 上为零, 因此对积分没有贡献. 可以说明, 上述积分不依赖于开覆盖或单位分解的选取.

定理 18.4.1 (Gauss-Green 公式) 设  $\Omega$  是  $R^{n}$  中具有  $C^{1}$  边界的有界开集,  $\eta$  是在  $\bar{\Omega}$  的某个开邻域上的定义的  $C^{1}$  的  $(n-1)$ -形式, 则

$$
\int_ {\Omega} \mathrm{d} \eta = \int_ {\partial \Omega} \eta ,
$$

其中  $\partial\Omega$  的方向由单位外法向量 n 所决定.

证明 记  $\eta=\sum_{i=1}^{n}(-1)^{i-1}f_{i}\mathrm{d}x_{1}\wedge\cdots\wedge\widehat{\mathrm{d}x_{i}}\wedge\cdots\wedge\mathrm{d}x_{n}$ ，则

$$
\mathrm{d} \eta = \mathrm{div} (\boldsymbol {X}) \mathrm{d} x _ {1} \wedge \dots \wedge \mathrm{d} x _ {n},
$$

其中  $\boldsymbol{X}=(f_{1},\cdots,f_{n})$ . 这说明

$$
\int_ {\Omega} \mathrm{d} \eta = \int_ {\Omega} \mathrm{div} (\boldsymbol {X}) \mathrm{d} \boldsymbol {x}.
$$

另一方面，由(18.4.3)式可知

$$
\int_ {\partial \Omega} \eta = \int_ {\partial \Omega} \boldsymbol {X} \cdot \boldsymbol {n}   \mathrm{d} \sigma ,
$$

于是欲证结论化成了散度定理.

□

---

18.4 Brouwer 不动点定理

93

注18.4.1 利用微分形式的积分表述散度定理的好处是容易看出相关积分公式的形式不变性. 若 $\phi : \bar{D} \to \bar{\Omega}$ 为保定向的微分同胚, 则由变量替换公式可知

$$
\int_ {D} \phi^ {*} (\mathrm{d} \eta) = \int_ {\Omega} \mathrm{d} \eta , \quad \int_ {\partial D} \phi^ {*} (\eta) = \int_ {\partial \Omega} \eta ,
$$

利用拉回映射与外微分可以交换次序可知, Gauss-Green 公式在  $\Omega$  上成立当且仅当它在 D 上成立.

下面我们来介绍 Gauss-Green 公式的一个应用. 我们知道, 数学中的很多问题经常转化为解方程, 解方程往往又转化为求不动点. 下面我们利用 Gauss-Green 公式来证明一个重要的不动点定理. 为了便于利用微分学的手段, 我们要用 $C^2$ 函数逼近连续函数. 这里我们用单位分解来做. 以下记 $D$ 为 $\mathbb{R}^n$ 中的单位闭球.

引理18.4.2 设 $\psi : D \to \mathbb{R}^n$ 为连续的向量值函数, 且当 $\pmb{x} \in S^{n-1} = \partial D$ 时 $\psi(\pmb{x}) = \pmb{x}$, 则任给 $\varepsilon > 0$, 存在 $C^2$ 的向量值函数 $\rho: \mathbb{R}^n \to \mathbb{R}^n$, 使得

$$
\rho (\boldsymbol {x}) = \boldsymbol {x}, \forall \| \boldsymbol {x} \| \geqslant 1; \| \rho (\boldsymbol {x}) - \psi (\boldsymbol {x}) \| <   \varepsilon , \forall \boldsymbol {x} \in D.
$$

证明 记 $f(\pmb{x}) = \psi (\pmb {x}) - \pmb{x}$, 则 $f|_{S^{n - 1}} \equiv 0$. 任给 $\varepsilon > 0$, 由 $f$ 在 $D$ 中一致连续可知, 存在 $\delta > 0$, 使得只要 $\| \pmb {x} - \pmb {y} \| \leqslant \delta$, 就有 $\| f(\pmb {x}) - f(\pmb {y}) \| < \frac{\varepsilon}{2}$. 令

$$
g (\boldsymbol {x}) = \left\{ \begin{array}{l l} f ((1 + \delta) \boldsymbol {x}), & \| \boldsymbol {x} \| \leqslant \frac {1}{1 + \delta}, \\ 0, & \| \boldsymbol {x} \| > \frac {1}{1 + \delta}. \end{array} \right.
$$

则当 $\pmb{x} \in D$ 时 $\|g(\pmb{x}) - f(\pmb{x})\| < \frac{\varepsilon}{2}$; 当 $\| \pmb{x} - \pmb{y} \| \leqslant \eta = \frac{\delta}{1 + \delta}$ 时, $\|g(\pmb{x}) - g(\pmb{y})\| < \frac{\varepsilon}{2}$.

根据单位分解引理, 存在有限点集  $\{\boldsymbol{x}^{i}\}_{i=1}^{k} \subset \overline{B_{1-\eta}(0)}$ , 以及相应的  $C^{2}$  函数  $\{\phi_{i}\}$ , 使得 supp  $\phi_{i} \subset B_{\eta}(\boldsymbol{x}^{i})$ , 且

$$
0 \leqslant \sum_ {i = 1} ^ {k} \phi_ {i} \leqslant 1; \quad \sum_ {i = 1} ^ {k} \phi_ {i} (\boldsymbol {x}) = 1, \forall \boldsymbol {x} \in \overline {{B _ {1 - \eta} (0)}}.
$$

令 $h(\pmb {x}) = \sum_{i = 1}^{k}g(\pmb{x}^{i})\phi_{i}(\pmb {x})$ ，则当 $\| \pmb {x}\| \geqslant 1$ 时 $h(\pmb {x}) = 0,$ 且当 $\pmb {x}\in D$ 时

$$
h (\boldsymbol {x}) - g (\boldsymbol {x}) = \sum_ {i = 1} ^ {k} \left[ g (\boldsymbol {x} ^ {i}) - g (\boldsymbol {x}) \right] \phi_ {i} (\boldsymbol {x}).
$$

于是

$$
\| h (\boldsymbol {x}) - g (\boldsymbol {x}) \| \leqslant \sum_ {i = 1} ^ {k} \| g (\boldsymbol {x} ^ {i}) - g (\boldsymbol {x}) \| \phi_ {i} (\boldsymbol {x}).
$$

---

94

第十八章 微分形式简介

上式右端只需要考虑 $\phi_i(\pmb{x}) > 0$ 的项, 此时 $\pmb{x} \in B_{\eta}(\pmb{x}^i)$, 因此 $\|g(\pmb{x}^i) - g(\pmb{x})\| < \frac{\varepsilon}{2}$, 这表明 $\|h(\pmb{x}) - g(\pmb{x})\| < \frac{\varepsilon}{2}$. 记 $\rho(\pmb{x}) = \pmb{x} + h(\pmb{x})$, 则 $\rho$ 是满足要求的 $C^2$ 映射.

引理18.4.3 设 $\rho: D \to \mathbb{R}^n$ 为 $C^2$ 的向量值函数, 如果当 $x \in S^{n-1}$ 时 $\rho(x) = x$, 则 $\rho$ 必有零点.

证明 (反证法) 设 $\rho$ 没有零点. 在 $\mathbb{R}^n \setminus \{0\}$ 上考虑 $(n - 1)$-形式

$$
\Theta_ {0} = \sum_ {i = 1} ^ {n} (- 1) ^ {i - 1} \| \boldsymbol {x} \| ^ {- n} x _ {i}   \mathrm{d} x _ {1} \wedge \dots \wedge \mathrm{d} x _ {i - 1} \wedge \mathrm{d} x _ {i + 1} \wedge \dots \wedge \mathrm{d} x _ {n},
$$

直接的计算表明 $\mathrm{d}\Theta_0 = 0$ 记

$$
\Theta = \boldsymbol {\rho} ^ {*} \Theta_ {0} = \sum_ {i = 1} ^ {n} (- 1) ^ {i - 1} \| \boldsymbol {\rho} \| ^ {- n} \rho_ {i} \mathrm{d} \rho_ {1} \wedge \dots \wedge \mathrm{d} \rho_ {i - 1} \wedge \mathrm{d} \rho_ {i + 1} \wedge \dots \wedge \mathrm{d} \rho_ {n},
$$

其中  $\rho_{i}$  是  $\rho$  的第 i 个分量, 则仍有  $d\Theta = 0$ .

利用 Gauss-Green 公式 (边界取外法向) 以及 $\pmb{\rho}(x) = x$ ($x \in S^{n-1}$) 可得

$$
\begin{array}{l} 0 = \int_ {D} \mathrm{d} \Theta = \int_ {S ^ {n - 1}} \Theta = \int_ {S ^ {n - 1}} \Theta_ {0} \\ = \int_ {S ^ {n - 1}} \sum_ {i = 1} ^ {n} (- 1) ^ {i - 1} x _ {i} \mathrm{d} x _ {1} \wedge \dots \wedge \mathrm{d} x _ {i - 1} \wedge \mathrm{d} x _ {i + 1} \wedge \dots \wedge \mathrm{d} x _ {n} \\ = \int_ {D} n \mathrm{d} x _ {1} \dots \mathrm{d} x _ {n} = n \nu (D) > 0, \\ \end{array}
$$

这就得出了矛盾.

定理 18.4.4 (Brouwer 不动点定理) 设 B 为  $R^{n}$  中的闭球,  $\varphi: B \rightarrow B$  为连续映射, 则  $\varphi$  必有不动点.

证明 (反证法) 不妨设 $B = D$ 为单位闭球. 设 $\varphi$ 没有不动点. 用直线段连接 $\varphi(x)$ 和 $x$, 其延长线交球面于 $\psi(x)$. 容易看出 $\psi: D \to S^{n-1}$ 为连续映射, 且当 $x \in S^{n-1}$ 时 $\psi(x) = x$.

根据引理18.4.2, 存在 $C^2$ 映射 $\rho: D \to \mathbb{R}^n$, 使得

$$
\rho (\boldsymbol {x}) = \boldsymbol {x}, \forall \boldsymbol {x} \in S ^ {n - 1}; \| \rho (\boldsymbol {x}) - \psi (\boldsymbol {x}) \| <   1, \forall \boldsymbol {x} \in D.
$$

根据引理 18.4.3,  $\rho$  有零点, 但这与上面的不等式以及  $\|\psi\| \equiv 1$  相矛盾.

例 18.4.1 设  $\boldsymbol{A} = (a_{ij})_{n \times n}$  为 n 阶实方阵, 如果它的每一元素  $a_{ij}$  都大于零, 则称 A 为正矩阵. 证明: 正矩阵必有正特征值.

证明 当  $\boldsymbol{x}=(x_{1},x_{2},\cdots,x_{n})\in\mathbb{R}^{n}$  时, 记  $|\boldsymbol{x}|_{1}=\sum_{i=1}^{n}|x_{i}|$ . 考虑 n-1 维单形

$$
\Delta_ {n} = \{\boldsymbol {x} \in \mathbb {R} ^ {n} \mid | \boldsymbol {x} | _ {1} = 1, x _ {i} \geqslant 0, i = 1, 2, \dots , n \}.
$$

---

18.4 Brouwer 不动点定理

95

显然, 当  $x \in \Delta_{n}$  时  $|Ax|_{1} > 0$ . 考虑连续映射

$$
\varphi : \Delta_ {n} \to \Delta_ {n}, \quad \boldsymbol {x} \mapsto \boldsymbol {A} \boldsymbol {x} / | \boldsymbol {A} \boldsymbol {x} | _ {1}.
$$

因为 $\Delta_{n}$ 和 $n - 1$ 维单位闭球同胚 (即它们之间存在互逆的连续映射), 我们仍然可以应用 Brouwer 不动点定理得到 $\varphi$ 的不动点, 将此不动点记为 $\xi$, 则 $\xi$ 是 $A$ 的特征向量, $|A\xi|_1$ 就是 $A$ 的正特征值.

## 习题 18.4

1. 在 $\mathbb{R}^n \setminus \{0\}$ 上考虑 $(n - 1)$-形式

$$
\Theta_ {0} = \sum_ {i = 1} ^ {n} (- 1) ^ {i - 1} \| \boldsymbol {x} \| ^ {- n} x _ {i}   \mathrm{d} x _ {1} \wedge \dots \wedge \mathrm{d} x _ {i - 1} \wedge \mathrm{d} x _ {i + 1} \wedge \dots \wedge \mathrm{d} x _ {n},
$$

验证  $d\Theta_{0}=0.$

2. 设 $\Omega$ 是 $\mathbb{R}^n$ 中具有 $C^1$ 边界的有界开集且 $0 \in \Omega$. 计算上一题中的微分形式 $\Theta_0$ 在 $\partial \Omega$ 上的积分, 其中方向取外法向.

3. 设 $f$ 为 $\mathbb{R}^n$ 上具有紧支集的连续函数. 证明: 任给 $\varepsilon, \eta > 0$, 存在 $\mathbb{R}^n$ 上具有紧支集的 $C^2$ 函数 $g$, 使得

$$
| g (\boldsymbol {x}) - f (\boldsymbol {x}) | <   \varepsilon , \forall \boldsymbol {x} \in \mathbb {R} ^ {n}; \operatorname{supp} g \subset \{\boldsymbol {x} \mid d (\boldsymbol {x}, \operatorname{supp} f) <   \eta \}.
$$

4. 设 $f, h$ 为 $\mathbb{R}^n$ 上的连续函数, 且 $h$ 处处为正. 证明: 存在 $\mathbb{R}^n$ 上的 $C^2$ 函数 $g$, 使得 $|g(\pmb{x}) - f(\pmb{x})| < h(\pmb{x}), \forall \pmb{x} \in \mathbb{R}^n$.

5. 设 $D$ 是 $\mathbb{R}^n$ 中的单位闭球, $f: D \to \mathbb{R}^n$ 为连续的向量值函数. 如果 $f(\partial D) \subseteq D$, 证明: $f$ 必有不动点.

6. 设 $U \subseteq \mathbb{R}^n$ 为开集, $\varphi: U \to \mathbb{R}^n$ 在 $\pmb{x}^0$ 处可微. 如果 $\det J\varphi(\pmb{x}^0) \neq 0$, 证明: $\varphi(\pmb{x}^0)$ 是 $\varphi(U)$ 的内点.

7. 设 $D$ 为 $\mathbb{R}^n$ 中的单位闭球, $\rho: D \to \mathbb{R}^n$ 为连续的向量值函数. 如果 $\rho(x) \cdot x \geqslant 0$, $\forall x \in S^{n-1}$, 证明: $\rho$ 必有零点.

8. 设 $\overline{B_r(0)}$ 是 $\mathbb{R}^n$ 中以原点为中心, $r$ 为半径的闭球, $\varphi: \overline{B_r(0)} \to \mathbb{R}^n$ 为连续映射. 如果存在 $\delta \in (0,1)$, 使得只要 $\|x\| = r$, 就有 $\|\varphi(x) - x\| \leqslant \delta r$, 证明:

$$
\varphi (\overline {{B _ {r} (\mathbf {0})}}) \supseteq \overline {{B _ {(1 - \delta) r} (\mathbf {0})}}.
$$

9. 设  $\rho: R^{n} \rightarrow R^{n}$  连续, 且

$$
\lim _ {\boldsymbol {x} \to \infty} \frac {\rho (\boldsymbol {x}) \cdot \boldsymbol {x}}{\| \boldsymbol {x} \|} = + \infty .
$$

证明: $\rho$ 为满射.

---

96

第十八章 微分形式简介

10. 设 $\rho: \mathbb{R}^{n} \to \mathbb{R}^{n}$ 连续, 且存在常数 $C$, 使得

$$
\| \boldsymbol {\rho} (\boldsymbol {x}) - \boldsymbol {x} \| \leqslant C, \forall \boldsymbol {x} \in \mathbb {R} ^ {n},
$$

证明:  $\rho$  为满射.

11. 设  $\varphi: R^{n} \rightarrow R^{n}$  为  $C^{1}$  映射, 且

(1)  $\det J\varphi(\boldsymbol{x}) \neq 0, \forall \boldsymbol{x} \in \mathbb{R}^{n};$
(2) 当  $x \to \infty$  时  $\varphi(x) \to \infty,$

证明: $\varphi$ 为可逆映射, 且其逆映射为 $C^1$ 映射.
