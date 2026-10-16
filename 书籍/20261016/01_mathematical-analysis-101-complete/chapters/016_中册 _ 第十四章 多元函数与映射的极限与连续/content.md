# 中册 / 第十四章 多元函数与映射的极限与连续

原始 PDF 第 518–543 页。

## 第十四章

## 多元函数与映射的极限与连续

---

214

第十四章 多元函数与映射的极限与连续

从这一章开始我们要研究多个变量的函数. 我们知道, 一元函数的诸多性质都依赖于实数的性质. 为了研究多个变量的函数, 我们要首先研究其定义域的基本性质.

## 14.1 欧氏空间上的内积和外积

一元函数是指以 $\mathbb{R}$ 的子集为定义域的函数. 当变化因素不止一个时, 我们就要考虑定义在一般欧氏空间中的函数. 设 $n$ 为正整数, 记

$$
\mathbb {R} ^ {n} = \{(a _ {1}, a _ {2}, \dots , a _ {n}) \mid a _ {i} \in \mathbb {R}, i = 1, 2, \dots , n \},
$$

它是由 n 元有序实数组构成的集合. 以显然的方式,  $R^{n}$  成为 R 上的向量空间, 称为 n 维欧氏空间.  $a_{i}$  称为向量  $(a_{1}, a_{2}, \cdots, a_{n})$  的第 i 个坐标.

以 $\mathbb{R}^n$ 的子集为定义域的函数称为 $n$ 元函数, $n > 1$ 时统称多元函数. 为了研究多元函数, 我们首先要研究 $\mathbb{R}^n$ 的性质, 这可以与 $\mathbb{R}$ 的性质做对比. 比如, 为了比较两个实数的大小, 我们可以考虑它们之间差的绝对值. 从几何上看, 这个绝对值可以认为是这两个实数在直线上所代表的两个点之间的距离. 为了方便起见, $\mathbb{R}^n$ 中的向量 ($n$ 元实数组) 也称为 $\mathbb{R}^n$ 中的点. 给定 $\mathbb{R}^n$ 中的两个点 (向量), 怎样定义它们之间的距离 (夹角)? 为了定义距离和夹角, 我们引入如下概念.

定义 14.1.1 (内积) 设 V 是实数域 R 上的向量空间, 如果函数  $g: V \times V \rightarrow R$  满足以下条件:

(1) 任给  $v \in V$ ，均有  $g(v, v) \geqslant 0$ ，且  $g(v, v) = 0 \Longleftrightarrow v = 0$ （正定性）.
(2) 任给  $u, v \in V$ ，均有  $g(u, v) = g(v, u)$  （对称性）.
(3) 任给 $\alpha, \beta \in \mathbb{R}, \pmb{u}, \pmb{v}, \pmb{w} \in V$, 均有

$$
g (\alpha \pmb {u} + \beta \pmb {v}, \pmb {w}) = \alpha g (\pmb {u}, \pmb {w}) + \beta g (\pmb {v}, \pmb {w}) (\text {线性性}),
$$

则称 g 为 V 上的内积,  $(V, g)$  称为内积空间.

我们常用 $\langle ,\rangle$ 表示内积, 比如 $\langle \pmb {u},\pmb {v}\rangle = g(\pmb {u},\pmb {v})$ 表示 $\pmb {u},\pmb{v}$ 之间的内积. 有了内积就可以定义向量的长度和向量之间的夹角. 设 $\pmb {u}\in V$, 记 $\| \pmb {u}\| = \sqrt{\langle\pmb{u},\pmb{u}\rangle}$, 称为 $\pmb{u}$ 的范数或长度.

定理 14.1.1 (Schwarz $^{①}$ 不等式) 设 $(V, \langle, \rangle)$ 为内积空间, $u, v \in V$, 则

$$
| \langle \boldsymbol {u}, \boldsymbol {v} \rangle | \leqslant \| \boldsymbol {u} \| \cdot \| \boldsymbol {v} \|,
$$

等号成立当且仅当 u, v 线性相关.

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">① Schwarz, Hermann Amandus, 1843 年 1 月 25 日—1921 年 11 月 30 日, 德国数学家.</span></small>

---

14.1 欧氏空间上的内积和外积

215

证明 当 u = 0 (或 v = 0) 时, 由内积的线性性可得

$$
\langle \mathbf {0}, \boldsymbol {v} \rangle = \langle 0 \cdot \mathbf {0}, \boldsymbol {v} \rangle = 0 \langle \mathbf {0}, \boldsymbol {v} \rangle = 0,
$$

此时不等式自然成立. 下设  $u, v \neq 0$ , 当  $t \in R$  时, 根据内积的定义, 我们有

$$
\langle \boldsymbol {u}, \boldsymbol {u} \rangle - 2 t \langle \boldsymbol {u}, \boldsymbol {v} \rangle + t ^ {2} \langle \boldsymbol {v}, \boldsymbol {v} \rangle = \langle \boldsymbol {u} - t \boldsymbol {v}, \boldsymbol {u} - t \boldsymbol {v} \rangle \geqslant 0,
$$

上式是关于 $t$ 的一元二次函数, 因此其判别式非正:

$$
\Delta = 4 \langle \boldsymbol {u}, \boldsymbol {v} \rangle^ {2} - 4 \langle \boldsymbol {u}, \boldsymbol {u} \rangle \langle \boldsymbol {v}, \boldsymbol {v} \rangle \leqslant 0,
$$

等号成立的条件留作练习.

![](../../raw/pages_0513-0528/images/page_519_image_9.jpg)

注 14.1.1 当  $\langle v, v \rangle \geqslant 0$  恒成立时 Schwarz 不等式成立.

根据 Schwarz 不等式, 当 u, v 为非零向量时, 可以取  $\theta(u, v) \in [0, \pi]$ , 使得

$$
\cos \theta (\boldsymbol {u}, \boldsymbol {v}) = \frac {\langle \boldsymbol {u} , \boldsymbol {v} \rangle}{\| \boldsymbol {u} \| \| \boldsymbol {v} \|},
$$

$\theta(\boldsymbol{u},\boldsymbol{v})$  称为 u,v 之间的夹角, 也记为  $\angle(\boldsymbol{u},\boldsymbol{v})$ .

例 14.1.1  $R^{n}$  中的标准内积和范数.

设  $u, v \in R^{n}$ ，记  $\boldsymbol{u} = (u_{1}, u_{2}, \cdots, u_{n})$ ， $\boldsymbol{v} = (v_{1}, v_{2}, \cdots, v_{n})$ ，定义

$$
\langle \boldsymbol {u}, \boldsymbol {v} \rangle = \boldsymbol {u} \cdot \boldsymbol {v} = \sum_ {i = 1} ^ {n} u _ {i} v _ {i},
$$

容易看出 $\langle ,\rangle$ 为 $\mathbb{R}^n$ 中的内积, 称为标准内积或欧氏内积. 此时, $\pmb{u}$ 的范数为

$$
\| \boldsymbol {u} \| = \sqrt {u _ {1} ^ {2} + u _ {2} ^ {2} + \cdots + u _ {n} ^ {2}}.
$$

当 n=1 时, 范数也就是绝对值.

![](../../raw/pages_0513-0528/images/page_519_image_20.jpg)

例 14.1.2 矩阵空间中的内积和范数.

用 $M_{m \times n}$ 表示 $m \times n$ 实矩阵的全体构成的向量空间. 设 $\mathbf{A}, \mathbf{B} \in M_{m \times n}$, 定义

$$
\langle \boldsymbol {A}, \boldsymbol {B} \rangle = \mathrm{tr} \big (\boldsymbol {A} \boldsymbol {B} ^ {\mathrm{T}} \big),
$$

不难验证 $\langle ,\rangle$ 为 $M_{m\times n}$ 中的内积.若 $\pmb {A} = (a_{ij})_{m\times n}$ ，则其范数可以表示为

$$
\| \boldsymbol {A} \| = \left(\sum_ {i = 1} ^ {m} \sum_ {j = 1} ^ {n} a _ {i j} ^ {2}\right) ^ {\frac {1}{2}}.
$$

![](../../raw/pages_0513-0528/images/page_519_image_26.jpg)

需要注意的是, 在参与矩阵的乘法运算时, 我们经常把  $R^{n}$  中的向量视为列向量. 下面的结果建立了矩阵的范数和向量的范数之间的联系.

---

216

第十四章 多元函数与映射的极限与连续

引理 14.1.2 (范数不等式) 设  $b \in R^{n}$ ,  $A = (a_{ij})_{m \times n}$ ，则  $\|Ab\| \leqslant \|A\| \|b\|$ .

证明 我们把矩阵 A 的第 i 行记为  $a^{i}$ ，则 Ab 用列向量表示为

$$
\boldsymbol {A} \boldsymbol {b} = \left(\boldsymbol {a} ^ {1} \cdot \boldsymbol {b}, \boldsymbol {a} ^ {2} \cdot \boldsymbol {b}, \dots , \boldsymbol {a} ^ {m} \cdot \boldsymbol {b}\right) ^ {\mathrm{T}}.
$$

根据 Schwarz 不等式可得

$$
\| \boldsymbol {A} \boldsymbol {b} \| ^ {2} = \sum_ {i = 1} ^ {m} \left(\boldsymbol {a} ^ {i} \cdot \boldsymbol {b}\right) ^ {2} \leqslant \sum_ {i = 1} ^ {m} \| \boldsymbol {a} ^ {i} \| ^ {2} \| \boldsymbol {b} \| ^ {2} = \| \boldsymbol {A} \| ^ {2} \| \boldsymbol {b} \| ^ {2}.
$$

将上式两边开方即得欲证结论.

有了范数就可以定义距离. 设  $(V, \langle, \rangle)$  为内积空间,  $u, v \in V$ . 记  $d(u, v) = \|u - v\|$ , 称为 u, v 之间的距离.

命题 14.1.3 (三角不等式) 设  $(V, \langle, \rangle)$  为内积空间,  $x, y, z \in V$ , 则有

$$
d (\boldsymbol {x}, \boldsymbol {z}) \leqslant d (\boldsymbol {x}, \boldsymbol {y}) + d (\boldsymbol {y}, \boldsymbol {z}).
$$

证明 我们先证明绝对值不等式: 任给 $\pmb{u}, \pmb{v} \in V$, 均有

$$
\| \boldsymbol {u} + \boldsymbol {v} \| \leqslant \| \boldsymbol {u} \| + \| \boldsymbol {v} \|. \tag {14.1.1}
$$

事实上, 根据 Schwarz 不等式, 有

$$
\begin{array}{l} \| \boldsymbol {u} + \boldsymbol {v} \| ^ {2} = \langle \boldsymbol {u} + \boldsymbol {v}, \boldsymbol {u} + \boldsymbol {v} \rangle = \langle \boldsymbol {u}, \boldsymbol {u} \rangle + 2 \langle \boldsymbol {u}, \boldsymbol {v} \rangle + \langle \boldsymbol {v}, \boldsymbol {v} \rangle \\ \leqslant \| \boldsymbol {u} \| ^ {2} + 2 \| \boldsymbol {u} \| \| \boldsymbol {v} \| + \| \boldsymbol {v} \| ^ {2} = (\| \boldsymbol {u} \| + \| \boldsymbol {v} \|) ^ {2}. \\ \end{array}
$$

将上式两边开方即得绝对值不等式. 当 $x, y, z \in V$ 时, 利用绝对值不等式可得

$$
\begin{array}{l} d (\boldsymbol {x}, \boldsymbol {z}) = \| \boldsymbol {x} - \boldsymbol {z} \| = \| (\boldsymbol {x} - \boldsymbol {y}) + (\boldsymbol {y} - \boldsymbol {z}) \| \\ \leqslant \| \boldsymbol {x} - \boldsymbol {y} \| + \| \boldsymbol {y} - \boldsymbol {z} \| = d (\boldsymbol {x}, \boldsymbol {y}) + d (\boldsymbol {y}, \boldsymbol {z}). \\ \end{array}
$$

设 $\pmb{u},\pmb{v}\in \mathbb{R}^n$ ，若 $\pmb {u}\cdot \pmb {v} = 0$ ，则称 $\pmb {u},\pmb{v}$ 互相垂直(正交)，记为 $\pmb {u}\perp \pmb{v}$ .第 $i$ 个坐标为1,其余坐标为零的向量记为 $e_i$ ，我们将 $\{e_i\}_{i = 1}^n$ 称为 $\mathbb{R}^n$ 中的标准正交基.

在  $R^{n}$  中给定 n-1 个向量  $v^{1}, v^{2}, \cdots, v^{n-1}$ ，我们要构造另一个向量 w，使得 w 与  $v^{i}$  均垂直。为此，记  $\boldsymbol{v}^{i} = (v_{1}^{i}, \cdots, v_{n}^{i})$ ，考虑线性函数  $\ell: R^{n} \to R$ :

$$
\ell (\boldsymbol {x}) = \left| \begin{array}{c c c} x _ {1} & \dots & x _ {n} \\ v _ {1} ^ {1} & \dots & v _ {n} ^ {1} \\ \vdots & & \vdots \\ v _ {1} ^ {n - 1} & \dots & v _ {n} ^ {n - 1} \end{array} \right|, \quad \forall \boldsymbol {x} = (x _ {1}, x _ {2}, \dots , x _ {n}).
$$

---

14.1 欧氏空间上的内积和外积

217

按照行列式的定义, $\ell (\pmb {x})$ 可以表示为

$$
\ell (\boldsymbol {x}) = \boldsymbol {x} \cdot \boldsymbol {w} = \sum_ {i = 1} ^ {n} x _ {i} w _ {i}, \tag {14.1.2}
$$

其中  $\boldsymbol{w}=(w_{1},w_{2},\cdots,w_{n})$ ，且

$$
w _ {i} = (- 1) ^ {i - 1} \left| \begin{array}{c c c c c c} v _ {1} ^ {1} & \dots & v _ {i - 1} ^ {1} & v _ {i + 1} ^ {1} & \dots & v _ {n} ^ {1} \\ \vdots & & \vdots & \vdots & & \vdots \\ v _ {1} ^ {n - 1} & \dots & v _ {i - 1} ^ {n - 1} & v _ {i + 1} ^ {n - 1} & \dots & v _ {n} ^ {n - 1} \end{array} \right|, i = 1, 2, \dots , n. \tag {14.1.3}
$$

由  $\ell(\boldsymbol{x})$  的定义易见  $\ell(\boldsymbol{v}^{i})=0\ (1\leqslant i\leqslant n-1)$ . 再由 (14.1.2) 可知 w 的确与  $v^{i}$  都垂直.
我们称 w 是  $v^{1}, v^{2}, \cdots, v^{n-1}$  的外积, 记为

$$
\boldsymbol {w} = \boldsymbol {v} ^ {1} \times \boldsymbol {v} ^ {2} \times \dots \times \boldsymbol {v} ^ {n - 1}.
$$

外积还具有下列性质:

\- $\{\pmb{v}^i\}_{i=1}^{n-1}$ 线性相关当且仅当 $\pmb{v}^1 \times \pmb{v}^2 \times \dots \times \pmb{v}^{n-1} = \mathbf{0}$. 事实上, 如果 $\{\pmb{v}^i\}_{i=1}^{n-1}$ 线性相关, 则 $\ell(\pmb{x}) \equiv 0$, 从而 $\| \pmb{w} \|^2 = \ell(\pmb{w}) = 0$; 另一方面, 如果 $\{\pmb{v}^i\}_{i=1}^{n-1}$ 线性无关, 则可以将它们扩充为 $\mathbb{R}^n$ 中的一组基 $\{\pmb{u}, \pmb{v}_i \mid 1 \leqslant i \leqslant n-1\}$. 此时 $\ell(\pmb{u}) \neq 0$, 即 $\pmb{u} \cdot \pmb{w} \neq 0$, 特别地 $\pmb{w} \neq \mathbf{0}$.

\- 外积关于每一个分量 $\pmb{v}^i$ 都是线性的, 即任给 $\lambda, \mu \in \mathbb{R}$ 以及向量 $\pmb{v}^i, \tilde{\pmb{v}}^i$, 有

$$
\boldsymbol {v} ^ {1} \times \dots \times \left(\lambda \boldsymbol {v} ^ {i} + \mu \tilde {\boldsymbol {v}} ^ {i}\right) \times \dots \times \boldsymbol {v} ^ {n - 1} = \lambda \boldsymbol {v} ^ {1} \times \dots \times \boldsymbol {v} ^ {i} \times \dots \times \boldsymbol {v} ^ {n - 1} +
$$

$$
\mu \boldsymbol {v} ^ {1} \times \dots \times \tilde {\boldsymbol {v}} ^ {i} \times \dots \times \boldsymbol {v} ^ {n - 1}
$$

\- 当 $i < j$ 时, 交换 $\pmb{v}^i$ 和 $\pmb{v}^j$ 的位置以后外积变一个符号, 即

$$
\boldsymbol {v} ^ {1} \times \dots \times \boldsymbol {v} ^ {j} \times \dots \times \boldsymbol {v} ^ {i} \times \dots \times \boldsymbol {v} ^ {n - 1} = - \boldsymbol {v} ^ {1} \times \dots \times \boldsymbol {v} ^ {i} \times \dots \times \boldsymbol {v} ^ {j} \times \dots \times \boldsymbol {v} ^ {n - 1}.
$$

一般地, 设  $\sigma$  为  $\{1,\cdots,n-1\}$  的置换, 则

$$
\boldsymbol {v} ^ {\sigma (1)} \times \dots \times \boldsymbol {v} ^ {\sigma (n - 1)} = (- 1) ^ {\sigma} \boldsymbol {v} ^ {1} \times \dots \times \boldsymbol {v} ^ {n - 1},
$$

其中 $\sigma$ 为偶置换时 $(-1)^{\sigma} = 1, \sigma$ 为奇置换时 $(-1)^{\sigma} = -1$.

\- $\| \pmb{v}^{1}\times \dots \times \pmb{v}^{n - 1}\| = \left(\det \left(\pmb{v}^{i}\cdot \pmb{v}^{j}\right)_{(n - 1)\times (n - 1)}\right)^{\frac{1}{2}}$ .事实上，当 $\{\pmb{v}^i\}_{i = 1}^{n - 1}$ 线性相关时 $\pmb {w} = \mathbf{0},\det \left(\pmb {v}^{i}\cdot \pmb{v}^{j}\right)_{(n - 1)\times (n - 1)} = 0;$ 当 $\{\pmb{v}^i\}_{i = 1}^{n - 1}$ 线性无关时，利用 $\| \pmb {w}\| ^2 = \ell (\pmb {w})$ 以

---

218

第十四章 多元函数与映射的极限与连续

及 $\pmb{v}^i\cdot \pmb {w} = 0$ 可得

$$
\begin{array}{l} \| \boldsymbol {w} \| ^ {4} = \det \left(\left( \begin{array}{c} \boldsymbol {w} \\ \boldsymbol {v} ^ {1} \\ \vdots \\ \boldsymbol {v} ^ {n - 1} \end{array} \right) \left( \begin{array}{c} \boldsymbol {w} \\ \boldsymbol {v} ^ {1} \\ \vdots \\ \boldsymbol {v} ^ {n - 1} \end{array} \right) ^ {\mathrm{T}}\right) = \det \left( \begin{array}{c c} \boldsymbol {w} \cdot \boldsymbol {w} & 0 \\ 0 & (\boldsymbol {v} ^ {i} \cdot \boldsymbol {v} ^ {j}) _ {(n - 1) \times (n - 1)} \end{array} \right) \\ = \| \boldsymbol {w} \| ^ {2} \det \left(\boldsymbol {v} ^ {i} \cdot \boldsymbol {v} ^ {j}\right) _ {(n - 1) \times (n - 1)}, \\ \end{array}
$$

这说明  $\left\|w\right\|^{2}=\det\left(v^{i}\cdot v^{j}\right)_{(n-1)\times(n-1)}$ .

\- 若  $\{e_{i}\}_{i=1}^{n}$  为  $R^{n}$  中的标准正交基, 则  $e_{1} \times \cdots \times e_{i-1} \times e_{i+1} \times \cdots \times e_{n} = (-1)^{i-1} e_{i}$ .

## 习题 14.1

1. 我们用 $C[a, b]$ 表示 $[a, b]$ 上连续函数的全体构成的空间. 设 $f, g \in C[a, b]$, 定义

$$
\langle f, g \rangle = \int_ {a} ^ {b} f (x) g (x) \mathrm{d} x,
$$

验证 $\langle,\rangle$ 是 $C[a,b]$ 上的内积.

2. 设 $\langle ,\rangle$ 为向量空间 $V$ 上的内积, $\pmb{u}, \pmb{v} \in V, \pmb{v} \neq \mathbf{0}$. 在不等式

$$
\langle \boldsymbol {u} - t \boldsymbol {v}, \boldsymbol {u} - t \boldsymbol {v} \rangle \geqslant 0
$$

中代入  $t=\frac{\langle u,v\rangle}{\langle v,v\rangle}$  从而证明 Schwarz 不等式.

3. 设 $(V, \langle, \rangle)$ 为内积空间, 证明如下的余弦公式:

$$
\| \boldsymbol {u} - \boldsymbol {v} \| ^ {2} = \| \boldsymbol {u} \| ^ {2} + \| \boldsymbol {v} \| ^ {2} - 2 \| \boldsymbol {u} \| \| \boldsymbol {v} \| \cos \theta (\boldsymbol {u}, \boldsymbol {v}), \forall \boldsymbol {u}, \boldsymbol {v} \in V.
$$

4. 设 $(V, \langle , \rangle)$ 为内积空间, 证明如下的平行四边形公式:

$$
\| \boldsymbol {u} + \boldsymbol {v} \| ^ {2} + \| \boldsymbol {u} - \boldsymbol {v} \| ^ {2} = 2 \big (\| \boldsymbol {u} \| ^ {2} + \| \boldsymbol {v} \| ^ {2} \big), \forall \boldsymbol {u}, \boldsymbol {v} \in V.
$$

5. 设 $\pmb{u} \in \mathbb{R}^n$, 证明: $\| \pmb{u} \| = \max \{\pmb{u} \cdot \pmb{v} \mid \pmb{v} \in S^{n-1}\}$, 其中 $S^{n-1} = \{\pmb{x} \in \mathbb{R}^n \mid \| \pmb{x} \| = 1\}$.

6. 设  $\boldsymbol{x}=(x_{1},x_{2},\cdots,x_{n})\in\mathbb{R}^{n}$ ，证明:

(1) 存在常数  $K_{1}, K_{2} > 0$ , 使得

$$
K _ {1} \sum_ {i = 1} ^ {n} | x _ {i} | \leqslant \| \boldsymbol {x} \| \leqslant K _ {2} \sum_ {i = 1} ^ {n} | x _ {i} |.
$$

(2) 存在常数 $M_{1}, M_{2} > 0$, 使得

$$
M _ {1} \max _ {1 \leqslant i \leqslant n} | x _ {i} | \leqslant \| \boldsymbol {x} \| \leqslant M _ {2} \max _ {1 \leqslant i \leqslant n} | x _ {i} |.
$$

---

14.2 欧氏空间的拓扑

219

7. 设 $A, B$ 为 $n$ 阶实方阵, 证明: $\|AB\| \leqslant \|A\| \|B\|$.
8. 设 A 为 n 阶实方阵. 若  $\|A\| < 1$ , 证明:  $I_{n} - A$  可逆, 其中  $I_{n}$  是 n 阶单位矩阵.
9. 设  $u, v, w \in R^{3}$ ，证明: $(\boldsymbol{u} \times \boldsymbol{v}) \times \boldsymbol{w} + (\boldsymbol{v} \times \boldsymbol{w}) \times \boldsymbol{u} + (\boldsymbol{w} \times \boldsymbol{u}) \times \boldsymbol{v} = \boldsymbol{0}$ .

10. 当 $f \in C[0,1]$ 时, 记 $|f|_{\infty} = \max \{|f(x)| \mid x \in [0,1]\}$. 问: $|\cdot|_{\infty}$ 是否为某个内积的范数? 请说明理由.

## 14.2 欧氏空间的拓扑

通过一元函数的学习, 我们知道无论是函数的极限还是连续性等性质都与实数的基本性质密切相关. 类似地, 多元函数的性质和欧氏空间的基本性质密切相关, 下面我们就来介绍欧氏空间的基本拓扑性质.

设 $\pmb{x} \in \mathbb{R}^n, r > 0$. 记 $B_r(\pmb{x}) = \{\pmb{y} \in \mathbb{R}^n \mid d(\pmb{y}, \pmb{x}) < r\}$, 称为以 $\pmb{x}$ 为中心 (球心), $r$ 为半径的开球.

开集: 设 $U \subseteq \mathbb{R}^n$. 如果任给 $\pmb{x} \in U$, 均存在 $r > 0$, 使得 $B_r(\pmb{x}) \subseteq U$, 则称 $U$ 为 $\mathbb{R}^n$ 中的开集. 注意, 空集是开集. 当然, 整个 $\mathbb{R}^n$ 也是开集.

闭集: 如果一个集合在  $R^{n}$  中的补集是开集, 则称该集合为  $R^{n}$  中的闭集. 空集以及整个  $R^{n}$  都是闭集.

例 14.2.1 开集的简单例子.

我们先来说明开球 $B_r(\pmb{x})$ 是开集.事实上，若 $\pmb{y} \in B_r(\pmb{x})$ ，记 $r' = r - d(\pmb{y}, \pmb{x})$ 则 $r' > 0$ 当 $\pmb{z} \in B_{r'}(\pmb{y})$ 时，由三角不等式可得

$$
d (\boldsymbol {z}, \boldsymbol {x}) \leqslant d (\boldsymbol {z}, \boldsymbol {y}) + d (\boldsymbol {y}, \boldsymbol {x}) <   r ^ {\prime} + d (\boldsymbol {y}, \boldsymbol {x}) = r,
$$

即 $z \in B_r(x)$, 这说明 $B_{r'}(y) \subseteq B_r(x)$, 由开集的定义即知 $B_r(x)$ 是开集.

设 $(a_{i},b_{i})\ (i=1,2,\cdots,n)$ 均为 R 中的开区间, 记

$$
I = \prod_ {i = 1} ^ {n} (a _ {i}, b _ {i}) = \{(x _ {1}, x _ {2}, \dots , x _ {n}) \in \mathbb {R} ^ {n} \mid a _ {i} <   x _ {i} <   b _ {i}, 1 \leqslant i \leqslant n \},
$$

称为 $n$ 维开矩形. 我们来说明开矩形是开集. 事实上, 若 $\pmb{x} \in I$, 记

$$
r = \min \{x _ {i} - a _ {i}, b _ {i} - x _ {i} \mid 1 \leqslant i \leqslant n \},
$$

则 r > 0. 当  $\boldsymbol{y} = (y_{1}, y_{2}, \cdots, y_{n}) \in B_{r}(\boldsymbol{x})$  时, 由

$$
| y _ {i} - x _ {i} | \leqslant d (\boldsymbol {y}, \boldsymbol {x}) <   r \leqslant \min \{x _ {i} - a _ {i}, b _ {i} - x _ {i} \}
$$

---

220

第十四章 多元函数与映射的极限与连续

可知 $a_{i} < y_{i} < b_{i}, \forall 1 \leqslant i \leqslant n$. 这说明 $\pmb{y} \in I$, 即 $B_{r}(\pmb{x}) \subseteq I$, 于是由开集的定义即知 $I$ 是开集.

例14.2.2 闭集的简单例子.

设 $x \in \mathbb{R}^n, r > 0$. 记 $\overline{B_r(x)} = \{\boldsymbol{y} \in \mathbb{R}^n \mid d(\boldsymbol{y}, \boldsymbol{x}) = \| \boldsymbol{y} - \boldsymbol{x} \| \leqslant r\}$, 称为以 $x$ 为中心 (球心), $r$ 为半径的闭球. 我们来说明闭球是闭集. 事实上, 若 $y \notin \overline{B_r(x)}$, 记 $r' = d(\boldsymbol{y}, \boldsymbol{x}) - r$, 则 $r' > 0$, 由三角不等式可知 $B_{r'}(\boldsymbol{y}) \subseteq \mathbb{R}^n \setminus \overline{B_r(x)}$, 由定义可知 $\mathbb{R}^n \setminus \overline{B_r(x)}$ 为开集, 即 $\overline{B_r(x)}$ 是闭集.

设 $[a_i, b_i]$ ($i = 1, 2, \dots, n$) 均为 $\mathbb{R}$ 中的闭区间，记

$$
I = \prod_ {i = 1} ^ {n} [ a _ {i}, b _ {i} ] = \{(x _ {1}, x _ {2}, \dots , x _ {n}) \in \mathbb {R} ^ {n} \mid a _ {i} \leqslant x _ {i} \leqslant b _ {i}, 1 \leqslant i \leqslant n \},
$$

称为 $n$ 维(闭)矩形. 记 $\nu (I) = \prod_{i = 1}^{n}(b_i - a_i)$, 称为 $I$ 的容积. 记

$$
d (I) = \left[ (b _ {1} - a _ {1}) ^ {2} + (b _ {2} - a _ {2}) ^ {2} + \dots + (b _ {n} - a _ {n}) ^ {2} \right] ^ {\frac {1}{2}},
$$

称为 $I$ 的直径. 容易验证 $d(I) = \max \{d(\pmb{x},\pmb{y})\mid \pmb {x},\pmb {y}\in I\}$.

我们来说明 $I$ 是闭集. 事实上, 若 $\pmb{y} = (y_1, y_2, \dots, y_n) \notin I$, 则存在 $i$, 使得 $y_i \notin [a_i, b_i]$. 不妨设 $y_i < a_i$, 记 $r = a_i - y_i$, 则 $r > 0$. 当 $\pmb{z} = (z_1, z_2, \dots, z_n) \in B_r(\pmb{y})$ 时,

$$
a _ {i} - z _ {i} = r + y _ {i} - z _ {i} \geqslant r - \| \boldsymbol {y} - \boldsymbol {z} \| > 0,
$$

即 $z \notin I$, 这说明 $B_r(y) \subseteq \mathbb{R}^n \setminus I$, 因此 $\mathbb{R}^n \setminus I$ 是开集, $I$ 是闭集.

为了刻画开集和闭集, 我们引进点列极限的概念: 设 $\{\pmb{u}_i\}_{i=1}^{+\infty} \subseteq \mathbb{R}^n$, $\pmb{u} \in \mathbb{R}^n$. 如果 $\lim_{i \to +\infty} d(\pmb{u}_i, \pmb{u}) = \lim_{i \to +\infty} \| \pmb{u}_i - \pmb{u} \| = 0$, 则称点列 $\{\pmb{u}_i\}$ 收敛于 $\pmb{u}$, 或 $\{\pmb{u}_i\}$ 以 $\pmb{u}$ 为极限. 由三角不等式可知, 极限具有唯一性. 若 $\{\pmb{u}_i\}$ 为收敛点列, 其极限可记为 $\lim_{i \to +\infty} \pmb{u}_i$.

命题 14.2.1 (1) 设  $\{u_{i}\}$  收敛于 u. 若 u 属于开集 U, 则存在 N, 使得当 i > N 时  $u_{i}$  均属于 U.

(2) C 为闭集  $\Longleftrightarrow$  C 中任何收敛点列的极限仍属于 C.

证明 (1) 由 $U$ 为开集可知, 存在 $r > 0$, 使得 $B_r(\pmb{u}) \subseteq U$. 由极限的定义可知, 存在 $N$, 使得当 $i > N$ 时 $d(\pmb{u}_i, \pmb{u}) < r$, 即 $\pmb{u}_i \in B_r(\pmb{u}) \subseteq U$.

(2) “$\Longrightarrow$” 设 $\{\pmb{u}_i\}$ 为闭集 $C$ 中的收敛点列, 其极限为 $\pmb{u}$. 若 $\pmb{u} \notin C$, 则由 $C$ 为闭集可知, 存在 $r > 0$, 使得 $B_r(\pmb{u}) \subseteq \mathbb{R}^n \setminus C$. 由 (1) 可知, 当 $i$ 充分大时 $\pmb{u}_i \in \mathbb{R}^n \setminus C$, 这与 $\{\pmb{u}_i\} \subseteq C$ 相矛盾.

“$\Longleftarrow$”我们来说明 $\mathbb{R}^n \setminus C$ 是开集. 设 $\pmb{u} \in \mathbb{R}^n \setminus C$, 我们要说明存在 $i \geqslant 1$, 使得 $B_{\frac{1}{i}}(\pmb{u}) \subseteq \mathbb{R}^n \setminus C$. (反证法) 若不然, 则对每一个正整数 $i$, 均存在 $\pmb{u}_i \in B_{\frac{1}{i}}(\pmb{u}) \cap C$. 此时 $\{\pmb{u}_i\}$ 收敛于 $\pmb{u}$, 这与题设相矛盾.

---

14.2 欧氏空间的拓扑

221

下面我们将数列极限的重要结果推广到点列极限的情形.

定理 14.2.2 (Bolzano) 设  $\{u_{i}\} \subseteq R^{n}$ ，如果  $\{\|u_{i}\|\}$  有界，则  $\{u_{i}\}$  必有收敛子列.

证明 以 $n = 2$ 为例. 记 $\pmb{u}_i = (x_i, y_i)$, 则由 $|x_i|, |y_i| \leqslant \| \pmb{u}_i\|$ 可知 $\{x_i\}, \{y_i\}$ 均为有界数列. 于是 $\{x_i\}$ 存在收敛子列, 不妨设它本身收敛于 $x_0$. 注意 $\{y_i\}$ 也有收敛子列, 比如 $\{y_{ij}\}$ 收敛于 $y_0$. 记 $\pmb{u}_0 = (x_0, y_0)$, 由

$$
\| \boldsymbol {u} _ {i _ {j}} - \boldsymbol {u} _ {0} \| = \sqrt {(x _ {i _ {j}} - x _ {0}) ^ {2} + (y _ {i _ {j}} - y _ {0}) ^ {2}} \leqslant | x _ {i _ {j}} - x _ {0} | + | y _ {i _ {j}} - y _ {0} |
$$

即知  $\{u_{i_{j}}\}$  收敛于  $u_{0}$ .

引理 14.2.3 (Lebesgue 覆盖引理) 设  $\{U_{\alpha}\}$  为  $R^{n}$  中的一族开集, 若它们的并集包含闭矩形 I, 则存在  $\lambda > 0$ , 使得每一个包含于 I 且直径小于  $\lambda$  的矩形均包含于某一个  $U_{\alpha}$  中.

证明 (反证法) 若结论不对, 则对每一个正整数 $i$, 均存在直径小于 $\frac{1}{i}$ 矩形 $I_i \subseteq I$, 使得 $I_i$ 不包含于任何一个 $U_\alpha$ 中. 取 $\boldsymbol{u}_i \in I_i$, 则 $\{\boldsymbol{u}_i\} \subseteq I$, 从而存在收敛子列. 不妨设它本身收敛于 $\boldsymbol{u}_0$, 则 $\boldsymbol{u}_0 \in I$. 由题设, $\boldsymbol{u}_0$ 属于某个 $U_\alpha$. 由于 $U_\alpha$ 为开集, 故存在 $r > 0$, 使得 $B_r(\boldsymbol{u}_0) \subseteq U_\alpha$. 取 $N > \frac{2}{r}$, 使得当 $i > N$ 时, $d(\boldsymbol{u}_i, \boldsymbol{u}_0) < \frac{r}{2}$. 此时, 任给 $\boldsymbol{u} \in I_i$, 有

$$
d (\pmb {u}, \pmb {u} _ {0}) \leqslant d (\pmb {u}, \pmb {u} _ {i}) + d (\pmb {u} _ {i}, \pmb {u} _ {0}) \leqslant d (I _ {i}) + \frac {r}{2} <   \frac {1}{i} + \frac {r}{2} <   r,
$$

即 $\pmb{u} \in B_r(\pmb{u}_0)$, 从而 $I_i \subseteq B_r(\pmb{u}_0) \subseteq U_\alpha$, 这与 $I_i$ 的选取相矛盾.

为了叙述起来方便起见, 我们引进覆盖的概念. 若一族集合 $\{U_{\alpha}\}$ 的并集包含集合 $S$, 则称 $\{U_{\alpha}\}$ 是 $S$ 的一个覆盖; 每一个 $U_{\alpha}$ 都是开集的覆盖称为开覆盖.

定理 14.2.4 (有限覆盖定理) 设 $\{U_{\alpha}\}$ 为闭矩形 $I$ 的开覆盖, 则可以从这一族开集中选取有限个 $U_{\alpha}$, 使得它们的并集仍然包含 $I$.

证明 设 $\lambda$ 是前一引理中的正数 (称为 Lebesgue 数). 取正整数 $m > \frac{d(I)}{\lambda}$. 将 $I$ 等分为 $m^n$ 个小矩形, 每一个的直径均为 $\frac{d(I)}{m}$, 它小于 $\lambda$. 于是由前一引理可知, 每一个小矩形均包含于某一个 $U_\alpha$ 中, 因此 $I$ 包含于不超过 $m^n$ 个 $U_\alpha$ 的并集中. $\square$

设 $S \subseteq \mathbb{R}^n$ 为非空子集, 记 $d(S) = \sup \{d(\pmb{x}, \pmb{y}) \mid \pmb{x}, \pmb{y} \in S\}$, 称为 $S$ 的直径. 当 $d(S) < +\infty$ 时称 $S$ 为有界子集.

定理 14.2.5 (闭集套定理) 设  $\{C_{i}\}$  是  $R^{n}$  中一列非空有界闭集，如果  $C_{i} \supseteq C_{i+1}$  对每一个  $i \geqslant 1$  都成立，则  $\{C_{i}\}$  必有公共点。进一步，如果  $\lim_{i \to +\infty} d(C_{i}) = 0$ ，则  $\{C_{i}\}$  有且仅有一个公共点。

证明 先来说明 $\{C_i\}$ 必有公共点. (反证法) 若不然, 记 $U_i = \mathbb{R}^n \setminus C_i$, 则开集族 $\{U_i\}$ 的并集是整个 $\mathbb{R}^n$. 取矩形 $I \supseteq C_1$, 由前一定理, 存在 $m$, 使得

$$
I \subseteq \bigcup_ {i = 1} ^ {m} U _ {i} = U _ {m},
$$

---

222

第十四章 多元函数与映射的极限与连续

这与 $C_m \subseteq C_1 \subseteq I$ 相矛盾.

如果 $\lim_{i\to +\infty}d(C_i) = 0$ ，且 $\pmb {x},\pmb{y}$ 均为 $\{C_i\}$ 的公共点，则 $d(\pmb {x},\pmb {y})\leqslant d(C_i)$ 对每一 $i$ 都成立，令 $i\to \infty$ 可知 $d(\pmb {x},\pmb {y}) = 0$ ，即 $\pmb {x} = \pmb{y}$ □

研究数列极限时可以考虑单调性. 在一般的欧氏空间中没有单调点列的概念, 不过 Cauchy 准则仍然成立.

Cauchy 列: 设  $\{u_{i}\}$  为  $R^{n}$  中的点列. 如果任给  $\varepsilon > 0$ , 均存在 N, 使得当 i, j > N 时  $d(\boldsymbol{u}_{i}, \boldsymbol{u}_{j}) < \varepsilon$ , 则称  $\{u_{i}\}$  为 Cauchy 列或基本列.

例 14.2.3 设  $A \in M_{n \times n}$ ，记  $e_{i}(A) = \sum_{k=0}^{i} \frac{A^{k}}{k!}$ ，其中  $A^{0} = I_{n}$ ，证明: $\{e_{i}(A)\}$  为 Cauchy 列.

证明 $M_{n\times n}$ 可视为 $n^2$ 维的欧氏空间.当 $j > i$ 时，根据矩阵范数的性质可得

$$
d \big (e _ {j} (\boldsymbol {A}), e _ {i} (\boldsymbol {A}) \big) = \| e _ {j} (\boldsymbol {A}) - e _ {i} (\boldsymbol {A}) \| \leqslant \sum_ {k = i + 1} ^ {j} \frac {\| \boldsymbol {A} \| ^ {k}}{k !} \leqslant \frac {\| \boldsymbol {A} \| ^ {i + 1}}{(i + 1) !} \mathrm{e} ^ {\| \boldsymbol {A} \|},
$$

再由  $\lim_{i\to+\infty}\frac{\|\boldsymbol{A}\|^{i}}{i!}=0$  即知  $\{e_{i}(\boldsymbol{A})\}$  为 Cauchy 列.

定理 14.2.6 (Cauchy 准则) 设  $\{u_{i}\}$  为  $R^{n}$  中的点列. 则  $\{u_{i}\}$  收敛  $\Longleftrightarrow\{u_{i}\}$  为 Cauchy 列.

证明 若 $\{\pmb{u}_i\}$ 收敛于 $\pmb{u}$, 则利用三角不等式 $d(\pmb{u}_i, \pmb{u}_j) \leqslant d(\pmb{u}_i, \pmb{u}) + d(\pmb{u}_j, \pmb{u})$ 易见 $\{\pmb{u}_i\}$ 为 Cauchy 列.

反之, 若 $\{\pmb{u}_i\}$ 为 Cauchy 列, 则与 Cauchy 数列类似, $\{\pmb{u}_i\}$ 必为有界点列, 从而存在收敛子列. 与数列的情形类似, 容易看出 $\{\pmb{u}_i\}$ 本身也是收敛的. □

设 $\mathbf{A}$ 为 $n$ 阶实方阵, 根据前例我们就知道 $\{e_i(A)\}$ 收敛, 其极限记为 $\exp(A)$ 或 $\mathrm{e}^A$. 称 $\exp$ 为矩阵的指数映射, 关于它的进一步讨论可参见本节习题.

定理 14.2.7 (压缩映射原理) 设 C 为  $R^{n}$  中的闭集,  $f: C \rightarrow C$  为映射. 如果存在常数  $\lambda \in [0,1)$ , 使得

$$
d \big (f (\boldsymbol {x}), f (\boldsymbol {y}) \big) \leqslant \lambda d (\boldsymbol {x}, \boldsymbol {y}), \forall \boldsymbol {x}, \boldsymbol {y} \in C,
$$

则存在唯一的 $c \in C$，使得 $f(c) = c$.

证明 任取 $c_{0} \in C$, 当 $i \geqslant 1$ 时用 $c_{i} = f(c_{i-1})$ 递归地定义 $C$ 中一列点 $\{c_{i}\}$, 我们来说明它是 Cauchy 列.

事实上, 当 $i \geqslant 1$ 时, 根据题设可得

$$
d (\boldsymbol {c} _ {i + 1}, \boldsymbol {c} _ {i}) = d \big (f (\boldsymbol {c} _ {i}), f (\boldsymbol {c} _ {i - 1}) \big) \leqslant \lambda   d \big (\boldsymbol {c} _ {i}, \boldsymbol {c} _ {i - 1} \big),
$$

---

14.2 欧氏空间的拓扑

223

由数学归纳法可以得出 $d(\pmb{c}_{i + 1},\pmb{c}_i)\leqslant \lambda^i d(\pmb{c}_1,\pmb{c}_0)$ 因此，当 $j > i$ 时，由三角不等式可得

$$
d (\boldsymbol {c} _ {j}, \boldsymbol {c} _ {i}) \leqslant \sum_ {k = i + 1} ^ {j} d (\boldsymbol {c} _ {k}, \boldsymbol {c} _ {k - 1}) \leqslant \sum_ {k = i + 1} ^ {j} \lambda^ {k - 1} d (\boldsymbol {c} _ {1}, \boldsymbol {c} _ {0}) \leqslant \frac {\lambda^ {i}}{1 - \lambda} d (\boldsymbol {c} _ {1}, \boldsymbol {c} _ {0}),
$$

由 $\lambda \in [0,1)$ 可知 $\lim_{i\to +\infty}\lambda^i = 0$ ，这说明 $\{\pmb{c}_i\}$ 为Cauchy列，其极限记为 $c$ ，由 $C$ 为闭集可知 $c\in C$ .由 $c_{i} = f(c_{i - 1})$ 和三角不等式可得

$$
d \big (f (\boldsymbol {c}), \boldsymbol {c} \big) \leqslant d \big (f (\boldsymbol {c}), f (\boldsymbol {c} _ {i - 1}) \big) + d (\boldsymbol {c} _ {i}, \boldsymbol {c}) \leqslant \lambda   d (\boldsymbol {c}, \boldsymbol {c} _ {i - 1}) + d (\boldsymbol {c} _ {i}, \boldsymbol {c}),
$$

令 $i \to +\infty$ 可知 $d(f(\pmb{c}), \pmb{c}) = 0$, 即 $f(\pmb{c}) = \pmb{c}$.

若另有 $c' \in C$，使得 $f(c') = c'$，则

$$
d (\boldsymbol {c} ^ {\prime}, \boldsymbol {c}) = d \big (f (\boldsymbol {c} ^ {\prime}), f (\boldsymbol {c}) \big) \leqslant \lambda   d (\boldsymbol {c} ^ {\prime}, \boldsymbol {c}),
$$

由  $\lambda\in[0,1)$  可知  $d(\boldsymbol{c}^{\prime},\boldsymbol{c})=0$  ，即  $c^{\prime}=c$

□

满足上述定理要求的映射 f 称为压缩映射, c 称为 f 的不动点.

例14.2.4 设 $A \in M_{n \times n}$, 若 $\| A \| < 1$, 证明: 存在 $A_* \in M_{n \times n}$, 使得 $A_*^2 = I_n - A$. 证明 记 $\alpha = 1 - \sqrt{1 - \| A \|}$, 则 $\alpha \in [0,1)$. 记 $C = \{X \in M_{n \times n} \mid \| X \| \leqslant \alpha\}$, 则 $C$ 为 $M_{n \times n}$ 中的闭集. 当 $X \in C$ 时, 令 $f(X) = \frac{1}{2}(A + X^2)$. 由矩阵范数的性质可得

$$
\| f (\boldsymbol {X}) \| \leqslant \frac {1}{2} \big (\| \boldsymbol {A} \| + \| \boldsymbol {X} \| ^ {2} \big) \leqslant \frac {1}{2} \big (\| \boldsymbol {A} \| + \alpha^ {2} \big) = \alpha ,
$$

这说明 $f(\pmb {X})\in C$ .当 $\pmb {X},\pmb {Y}\in C$ 时，有

$$
\| f (\boldsymbol {X}) - f (\boldsymbol {Y}) \| = \frac {1}{2} \| (\boldsymbol {X} - \boldsymbol {Y}) \boldsymbol {X} + \boldsymbol {Y} (\boldsymbol {X} - \boldsymbol {Y}) \| \leqslant \frac {1}{2} \| \boldsymbol {X} - \boldsymbol {Y} \| (\| \boldsymbol {X} \| + \| \boldsymbol {Y} \|) \leqslant \alpha \| \boldsymbol {X} - \boldsymbol {Y} \|,
$$

这说明 $f:C \rightarrow  C$ 为压缩映射. $f$ 的不动点记为 $B$ ,则 ${A}_{ * }^{2} = {I}_{n} - A$ ,其中 ${A}_{ * } = {I}_{n} - B$ . $\square$

## 习题14.2

1. 证明: $\mathbb{R}^n$ 中的有限点集是闭集; 坐标均为整数的点构成的集合 $\mathbb{Z}^n$ 是闭集; 坐标均为有理数的点构成的集合 $\mathbb{Q}^n$ 既不是开集, 也不是闭集.
2. 证明: 一族开集的并集仍为开集, 有限个开集的交集仍为开集; 一族闭集的交集仍为闭集, 有限个闭集的并集仍为闭集.
3. 设 $A, B \subseteq \mathbb{R}$ 且不是空集. 证明: $A \times B$ 为有界闭集当且仅当 $A, B$ 均为有界闭集.

4. 设  $u \in R^{n}, c \in R,$  证明:

(1) 半空间  $\left\{x \in R^{n} \mid x \cdot u > c\right\}$  是开集.
(2) $\left\{x\in\mathbb{R}^{n}\mid x\cdot u\geqslant c\right\}$ 是闭集.

---

224

第十四章 多元函数与映射的极限与连续

5. 设  $\{u_{i}\} \subset R^{n}$  为收敛点列, 证明:  $\{\|u_{i}\|\}$  为收敛数列, 从而有界.

6. 设  $\{u_{i}\}$  和  $\{v_{i}\}$  为  $R^{n}$  中的点列且分别收敛于 u, v. 设  $\lambda, \mu$  为实数, 证明:

$$
\lim _ {i \to \infty} (\lambda \boldsymbol {u} _ {i} + \mu \boldsymbol {v} _ {i}) = \lambda \boldsymbol {u} + \mu \boldsymbol {v}.
$$

7. 设  $\{u_{i}\}$  为  $R^{n}$  中的点列, 证明:  $\{u_{i}\}$  为收敛点列当且仅当对每一个  $j=1,2,\cdots,n$ , 由  $\{u_{i}\}$  的第 j 个坐标构成的数列均收敛.

8. 设  $\{u_{i}\}$  和  $\{v_{i}\}$  为  $R^{n}$  中的点列且分别收敛于 u, v. 证明:

$$
\lim _ {i \to \infty} \boldsymbol {u} _ {i} \cdot \boldsymbol {v} _ {i} = \boldsymbol {u} \cdot \boldsymbol {v}.
$$

9. 证明: 有限覆盖定理中的矩形 $I$ 换成 $\mathbb{R}^n$ 的有界闭集时, 结论仍然成立. (提示: 设 $C$ 为有界闭集, 取矩形 $I \supseteq C$, 则 $\mathbb{R}^n \setminus C$ 和给定的 $U_{\alpha}$ 一起成为 $I$ 的开覆盖.)

10. 设  $\{u_{i}\}$  为  $R^{n}$  中的点列, 如果  $\sum_{i=1}^{+\infty}\|u_{i+1}-u_{i}\|$  收敛, 证明:  $\{u_{i}\}$  为收敛点列.

11. 设 $A \in M_{n \times n}$, $P$ 是 $n$ 阶可逆矩阵, 证明: $P \exp(A) P^{-1} = \exp(P A P^{-1})$.

12. 设  $A \in M_{n \times n}$ ，证明: $\det \exp(A) = \exp(\operatorname{tr}A)$ .

13. 设 $A \in M_{n \times n}$, 当 $t \in \mathbb{R}$ 时记 $\tau(t) = \exp(tA)$, 证明: $\tau'(t) = A\tau(t) = \tau(t)A$.

14. 本题研究如下常系数线性常微分方程:

$$
x ^ {(n)} (t) + a _ {n - 1} x ^ {(n - 1)} (t) + \dots + a _ {1} x ^ {\prime} (t) + a _ {0} x (t) = 0
$$

在初值条件  $x(t_{0})=c_{0}, x'(t_{0})=c_{1}, \cdots, x^{(n-1)}(t_{0})=c_{n-1}$  下解的存在性.

(1) 记  $\boldsymbol{X}(t)=\left(x(t),x'(t),\cdots,x^{(n-1)}(t)\right)^{\mathrm{T}}$ ，证明:上述方程可以转化为

$$
\boldsymbol {X} ^ {\prime} (t) = \boldsymbol {A} \boldsymbol {X} (t), \text {其中} \boldsymbol {A} \in M _ {n \times n}.
$$

(2) 证明:  $\boldsymbol{X}(t)=\exp\left((t-t_{0})\boldsymbol{A}\right)(c_{0},c_{1},\cdots,c_{n-1})^{\mathrm{T}}$  满足  $\boldsymbol{X}^{\prime}(t)=\boldsymbol{A}\boldsymbol{X}(t)$ .

15. 设 $A \in M_{n \times n}$ 且 $\|A\| < 1$。递归地定义一列方阵 $\{B_i\}$: $B_0 = I_n, i \geqslant 1$ 时 $B_i = I_n + AB_{i-1}$。证明: $\{B_i\}$ 收敛, 且其极限 $B$ 满足 $(I_n - A)B = B(I_n - A) = I_n$.

16. 设 C 为  $R^{n}$  中的闭集,  $f: C \rightarrow C$  为映射. 如果存在正整数 m, 使得 f 和自身复合 m 次以后是压缩映射, 证明: f 有唯一的不动点.

## 14.3 多元函数的极限

自然界中变化的量在数学中经常表示为函数. 多元函数是指依赖于多个变化量的函数. 比如, 地球表面的温度依赖于时间、经度、纬度等. 下面我们来研究多元函数随变量变化的规律, 先从函数极限的概念开始.

---

14.3 多元函数的极限

225

设 $\pmb{u}_0\in \mathbb{R}^n,r > 0$ ，记

$$
\stackrel {\circ} {B} _ {r} (\boldsymbol {u} _ {0}) = B _ {r} (\boldsymbol {u} _ {0}) \setminus \{\boldsymbol {u} _ {0} \} = \left\{\boldsymbol {u} \in \mathbb {R} ^ {n} \mid 0 <   \| \boldsymbol {u} - \boldsymbol {u} _ {0} \| <   r \right\},
$$

称为  $u_{0}$  的去心 r 邻域.

设 $S \subseteq \mathbb{R}^n$, $\pmb{u}_0 \in \mathbb{R}^n$. 如果 $\pmb{u}_0$ 的任何去心邻域中均含有 $S$ 中的点, 即

$$
\stackrel {\circ} {B} _ {r} (\boldsymbol {u} _ {0}) \cap S \neq \varnothing , \forall r > 0,
$$

则称  $u_{0}$  为 S 的一个聚点. 注意, S 的聚点可以属于 S, 也可以不属于 S. 设  $f: S \rightarrow R^{m}$  为映射. f 常称为向量值函数, m = 1 时简称函数.

定义 14.3.1 (向量值函数的极限) 设  $S \subseteq R^{n}$ ,  $f : S \to R^{m}$  为向量值函数,  $u_{0}$  为 S 的一个聚点,  $v_{0} \in R^{m}$ . 如果任给  $\varepsilon > 0$ , 均存在  $\delta > 0$ , 使得

$$
\boldsymbol {f} \left(\stackrel {\circ} {B} _ {\delta} (\boldsymbol {u} _ {0}) \cap S\right) \subseteq B _ {\varepsilon} (\boldsymbol {v} _ {0}),
$$

则称 f 在  $u_{0}$  处以  $v_{0}$  为极限, 记为

$$
\lim _ {\boldsymbol {u} \to \boldsymbol {u} _ {0}} \boldsymbol {f} (\boldsymbol {u}) = \boldsymbol {v} _ {0}.
$$

若不存在满足上述条件的  $v_{0}$ ，则称 f 在  $u_{0}$  处的极限不存在.

向量值函数极限的四则运算性质、复合性质以及判断极限是否存在的 Cauchy 准则、Heine 定理等与一元函数类似, 我们留给读者完成.

例14.3.1 用定义证明: $\lim_{(x,y)\to (0,0)}\frac{x^2y}{x^2 + y^2} = 0.$

证明 任给 $\varepsilon > 0$, 取 $\delta = \varepsilon$, 当 $(x, y) \in \mathring{B}_{\delta}(\mathbf{0})$ 时,

$$
\left| \frac {x ^ {2} y}{x ^ {2} + y ^ {2}} - 0 \right| \leqslant | y | \leqslant \sqrt {x ^ {2} + y ^ {2}} <   \delta = \varepsilon ,
$$

由极限的定义即得欲证结论.

例 14.3.2 证明: 二元函数  $f(x,y)=\frac{xy}{x^{2}+y^{2}}$  在  $(0,0)$  处不存在极限.

证明 若 $\lambda$ 是常数, 则在直线 $y = \lambda x$ 上, $f(x,y) = \frac{\lambda}{1 + \lambda^2}$. 特别地, 考虑点列

$$
\boldsymbol {u} _ {k} = (1 / k, 1 / k), \quad \boldsymbol {u} _ {k} ^ {\prime} = (1 / k, - 1 / k), \quad k = 1, 2, \dots ,
$$

则 $\pmb{u}_k\to (0,0),\pmb{u}_k^{\prime}\rightarrow (0,0)(k\to \infty)$ ，但

$$
f (\boldsymbol {u} _ {k}) = \frac {1}{2}, f (\boldsymbol {u} _ {k} ^ {\prime}) = - \frac {1}{2},
$$

根据 Heine 定理可知 $f(x,y)$ 在 $(0,0)$ 处不存在极限.

---

226

第十四章 多元函数与映射的极限与连续

按照定义, 二元函数 $f(x,y)$ 在 $(x_0,y_0)$ 处以 $\alpha$ 为极限, 是指当坐标 $x,y$ 同时趋于 $x_0,y_0$ 时 $f(x,y)$ 趋于 $\alpha$. 如果 $x,y$ 不是同时而是分别有次序地趋于 $x_0,y_0$, 则会引出另一种极限.

如果对于每一个固定的 $y \neq y_0$，极限 $\lim_{x \to x_0} f(x, y) = \varphi(y)$ 都存在，则可以定义极限

$$
\lim _ {y \to y _ {0}} \lim _ {x \to x _ {0}} f (x, y) = \lim _ {y \to y _ {0}} \varphi (y).
$$

类似地, 可以定义  $\lim_{x\to x_{0}}\lim_{y\to y_{0}}f(x,y)$ , 它们称为累次极限. 累次极限也可以对三元以及更多元的函数定义. 为了区别起见, 将之前定义的极限称为重极限.

例 14.3.3 求函数  $f(x,y)=\frac{xy}{x^{2}+y^{2}}$  在  $(0,0)$  处的累次极限.

解 当 $y \neq 0$ 时, 由一元函数的连续性质可知

$$
\lim _ {x \to 0} f (x, y) = \frac {0 \cdot y}{0 ^ {2} + y ^ {2}} = 0,
$$

这说明 $\lim_{y\to 0}\lim_{x\to 0}f(x,y) = 0.$ 同理可知 $\lim_{x\to 0}\lim_{y\to 0}f(x,y) = 0.$

上面的例子说明了累次极限存在不意味着重极限存在. 下面的例子表明, 重极限存在时, 累次极限未必存在.

例 14.3.4 研究函数  $f(x,y)=x\sin\frac{1}{y}$  在  $(0,0)$  处的重极限和累次极限.

解 由 $|f(x,y)| \leqslant |x|$ 可知 $\lim_{(x,y) \to (0,0)} f(x,y) = 0$. 当 $x \neq 0$ 时, 由于 $\lim_{y \to 0} f(x,y)$ 不存在, 故累次极限 $\lim_{x \to 0} \lim_{y \to 0} f(x,y)$ 不存在.

下面的定理给出了重极限和累次极限之间关系的一个结果.

定理 14.3.1 设  $\lim_{(x,y)\to(x_{0},y_{0})}f(x,y)=\alpha,$  且对任意  $y\neq y_{0},\quad\lim_{x\to x_{0}}f(x,y)=\varphi(y)$ 
均存在，则

$$
\lim _ {y \to y _ {0}} \lim _ {x \to x _ {0}} f (x, y) = \lim _ {y \to y _ {0}} \varphi (y) = \alpha;
$$

进一步, 若对任意 $x \neq x_0$, $\lim_{y \to y_0} f(x, y)$ 也存在, 则

$$
\lim _ {x \to x _ {0}} \lim _ {y \to y _ {0}} f (x, y) = \alpha = \lim _ {y \to y _ {0}} \lim _ {x \to x _ {0}} f (x, y).
$$

证明 由题设可知, 任给 $\varepsilon > 0$, 存在 $\delta > 0$, 当

$$
0 <   \sqrt {(x - x _ {0}) ^ {2} + (y - y _ {0}) ^ {2}} <   \delta
$$

时， $|f(x,y) - \alpha | < \varepsilon$ 固定 $y$ ，使之满足 $0 < |y - y_0| < \delta$ ，令 $x \to x_0$ 可得

$$
| \varphi (y) - \alpha | \leqslant \varepsilon .
$$

这说明  $\lim_{y\to y_{0}}\varphi(y)=\alpha.$  余下的证明类似, 略.

□

---

14.3 多元函数的极限

227

定义 14.3.2 (向量值函数的连续性) 设  $S \subseteq R^{n}$ ,  $f : S \to R^{m}$  为向量值函数,  $u_{0} \in S$ . 如果任给  $\varepsilon > 0$ , 均存在  $\delta > 0$ , 使得

$$
\boldsymbol {f} \left(B _ {\delta} (\boldsymbol {u} _ {0}) \cap S\right) \subseteq B _ {\varepsilon} \left(\boldsymbol {f} (\boldsymbol {u} _ {0})\right), \tag {14.3.1}
$$

则称 $\pmb{f}$ 在 $\pmb{u}_0$ 处连续. 如果 $\pmb{f}$ 处处连续, 则称 $\pmb{f}$ 为 $S$ 上的连续映射, 记为 $\pmb{f} \in C(S, \mathbb{R}^m)$.

命题14.3.2 映射 $f$ 在 $\pmb{u}_0$ 处连续 $\Longleftrightarrow$ 任给 $S$ 中收敛于 $\pmb{u}_0$ 的点列 $\{\pmb{u}_i\}$，均有 $\lim_{i\to +\infty}f(\pmb{u}_i) = f(\pmb{u}_0)$.

证明 “$\Longrightarrow$” 若 $f$ 在 $u_0$ 处连续, 则任给 $\varepsilon > 0$, 存在 $\delta > 0$ 使得 (14.3.1) 式成立. 当 $S$ 中的点列 $\{u_i\}$ 收敛于 $u_0$ 时, 存在 $N$, 使得当 $i > N$ 时 $u_i \in B_{\delta}(u_0)$. 此时 $f(u_i) \in B_{\varepsilon}(f(u_0))$. 这说明 $\{f(u_i)\}$ 收敛于 $f(u_0)$.

“$\Longleftarrow$”（反证法）若 $f$ 在 $\pmb{u}_0$ 处不连续，则存在 $\varepsilon_0 > 0$ 以及点列 $\{\pmb{u}_i\} \subseteq S$，使得

$$
d (\pmb {u} _ {i}, \pmb {u} _ {0}) <   \frac {1}{i}, d \big (\pmb {f} (\pmb {u} _ {i}), \pmb {f} (\pmb {u} _ {0}) \big) \geqslant \varepsilon_ {0},
$$

此时  $\{u_{i}\}$  收敛于  $u_{0}$ ，但  $\{f(u_{i})\}$  不收敛于  $f(u_{0})$ ，这就导出了矛盾.

□

下面命题的证明与一元函数类似, 我们略去证明.

命题 14.3.3 (连续函数的四则运算性质) 设  $f, g: S \rightarrow R$  为连续函数, 则

(1) 当  $\lambda, \mu \in R$  时,  $\lambda f + \mu g$  也是连续函数.
(2) fg 为连续函数.
(3) 当  $g \neq 0$  时,  $\frac{f}{g}$  为连续函数.

为了更好地刻画连续映射, 我们引进相对开集和相对闭集的概念. 设 $\pmb{u} \in S, r > 0$, 记 $B_r^S(\pmb{u}) = B_r(\pmb{u}) \cap S$, 称为 $S$ 中的相对开球. 设 $U \subseteq S$, 如果任给 $\pmb{u} \in U$, 均存在 $r > 0$, 使得 $B_r^S(\pmb{u}) \subseteq U$, 则称 $U$ 为 $S$ 中的相对开集. 设 $C \subseteq S$, 若 $S \setminus C$ 为 $S$ 中的相对开集, 则称 $C$ 为 $S$ 中的相对闭集.

命题 14.3.4 (连续映射的刻画) 映射  $f: S \rightarrow R^{m}$  连续  $\Longleftrightarrow$  开集的原像为 S 中的相对开集  $\Longleftrightarrow$  闭集的原像为 S 中的相对闭集.

证明 以开集为例. “$\Longrightarrow$” 设 $\pmb{f}$ 连续, $V$ 为 $\mathbb{R}^m$ 中的开集. 任取 $\pmb{u}_0 \in \pmb{f}^{-1}(V)$, 则 $\pmb{f}(\pmb{u}_0) \in V$, 由于 $V$ 为开集, 故存在 $\varepsilon > 0$, 使得 $B_{\varepsilon}(\pmb{f}(\pmb{u}_0)) \subseteq V$. 由 $\pmb{f}$ 在 $\pmb{u}_0$ 处连续可知, 存在 $\delta > 0$, 使得 (14.3.1) 式成立. 这说明 $B_{\delta}^{S}(\pmb{u}_0) \subseteq \pmb{f}^{-1}(V)$, 因此 $\pmb{f}^{-1}(V)$ 为 $S$ 中的相对开集.

“$\Longleftarrow$”任取 $\pmb{u}_0 \in S$ 以及 $\varepsilon > 0$. 于是 $U = \pmb{f}^{-1}\big(B_{\varepsilon}(\pmb{f}(\pmb{u}_0))\big)$ 为 $S$ 中包含 $\pmb{u}_0$ 的相对开集, 从而存在 $\delta > 0$, 使得 $B_{\delta}^{S}(\pmb{u}_0) \subseteq U$. 即 $\pmb{f}\big(B_{\delta}^{S}(\pmb{u}_0)\big) \subseteq B_{\varepsilon}(\pmb{f}(\pmb{u}_0))$, 于是 $\pmb{f}$ 在 $\pmb{u}_0$ 处连续.

利用连续映射的刻画可以得出连续映射的复合仍为连续映射, 我们略去证明.

命题 14.3.5 (连续映射的复合性质) 设  $f: S \rightarrow R^{m}, g: T \rightarrow R^{k}$  均为连续映射，其中  $f(S) \subseteq T \subseteq \mathbb{R}^{m}$ ，则  $g \circ f: S \rightarrow R^{k}$  也是连续映射.

---

228

第十四章 多元函数与映射的极限与连续

例 14.3.5 行列式函数.

$M_{n\times n}$  可视为  $n^{2}$  维的欧氏空间, 此时矩阵的行列式 det :  $M_{n\times n} \rightarrow R$  是多元函数, 它是具有  $n^{2}$  个变量的多元多项式, 由连续函数的四则运算性质可知 det 是连续函数. □

记 $GL(n, \mathbb{R}) = \{\boldsymbol{A} \in M_{n \times n} \mid \det \boldsymbol{A} \neq 0\}$, 则 $GL(n, \mathbb{R}) = \det^{-1}(\mathbb{R} \setminus \{0\})$. 因为 $\mathbb{R} \setminus \{0\}$ 为 $\mathbb{R}$ 中的开集, 由 $\det$ 连续可知 $GL(n, \mathbb{R})$ 是 $M_{n \times n}$ 中的开集. 直观地看, 若 $\boldsymbol{A}$ 是非退化方阵, 则 $\boldsymbol{A}$ 附近的方阵也是非退化的.

## 习题 14.3

1. 设 $S \subseteq \mathbb{R}^n$, $\boldsymbol{u}_0 \in \mathbb{R}^n$. 证明: $\boldsymbol{u}_0$ 是 $S$ 的聚点当且仅当存在点列 $\{\boldsymbol{u}_i\} \subseteq S \setminus \{\boldsymbol{u}_0\}$, 使得 $\lim_{i \to +\infty} \boldsymbol{u}_i = \boldsymbol{u}_0$.

2. 设 $S \subseteq \mathbb{R}^n$, $\pmb{u}_0$ 是 $S$ 的聚点, $\pmb{f}: S \to \mathbb{R}^m$ 为向量值函数, 请给出 $\lim_{\pmb{u} \to \pmb{u}_0} \pmb{f}(\pmb{u}) = \infty$ 的定义.

3. 设 $f$ 是定义在 $\mathbb{R}^n$ 上的向量值函数, 请给出 $\lim_{x\to \infty}f(x)$ 的定义.

4. 按照定义证明下列极限的等式:

(1) $\lim_{(x,y)\to (2,1)}(2x - 3y) = 1;$

(2) $\lim_{(x,y)\to (1,1)}(x^2 +y^2) = 2.$

5. 求下列极限:

(1) $\lim_{(x,y)\to (0,0)}\frac{\mathrm{e}^x + \mathrm{e}^y}{\cos x - \sin y};$

(2) $\lim_{(x,y)\to (0,0)}\frac{x^2y^{\frac{3}{2}}}{x^4 + y^2};$

(3) $\lim_{(x,y)\to (0,0)}xy\ln (x^2 +y^2);$

(4) $\lim_{(x,y)\to (0,0)}\frac{\sin(x^3 + y^3)}{x^2 + y^2}.$

6. 研究下列函数在  $(0,0)$  处的重极限:

(1) $f(x,y) = \frac{x^2}{x^2 + y^2}$;

(2) $f(x,y) = \frac{x^3 + y^3}{x^2 + y}$;

(3) $f(x,y) = \frac{x^2y^2}{x^3 + y^3}$;

(4) $f(x,y) = \frac{x^4y^4}{(x^2 + y^4)^3}.$

7. 叙述并证明向量值函数极限的 Heine 定理和 Cauchy 准则.

8. 研究二元函数 $f(x, y) = \frac{x - y + x^2 + y^2}{x + y}$ 在 (0,0) 处的两个累次极限.

9. 研究二元函数  $f(x,y)=(x+y)\sin\frac{1}{x}\sin\frac{1}{y}$  在  $(0,0)$  处的重极限和两个累次极限.

10. 证明: 多元向量值函数为连续映射当且仅当它的每一个分量均为连续函数.

11. 证明: 连续映射复合以后仍为连续映射.

12. 设 $S \subseteq \mathbb{R}^n$, $\boldsymbol{u}_0 \in S$, $\boldsymbol{f}: S \to \mathbb{R}^m$ 为向量值函数. 证明: $\boldsymbol{f}$ 在 $\boldsymbol{u}_0$ 处连续当且仅当任给 $S$ 中以 $\boldsymbol{u}_0$ 为极限的点列 $\{\boldsymbol{u}_i\}$, 均有 $\{\boldsymbol{f}(\boldsymbol{u}_i)\}$ 以 $\boldsymbol{f}(\boldsymbol{u}_0)$ 为极限.

13. 设 $S \subseteq \mathbb{R}^n$. 证明: 若 $U$ 为 $S$ 中的相对开集, 则存在 $\mathbb{R}^n$ 中的开集 $W$, 使

---

14.4 连续映射的整体性质

229

得 $U = W \cap S$; 若 $C$ 为 $S$ 中的相对闭集, 则存在 $\mathbb{R}^n$ 中的闭集 $D$, 使得 $C = D \cap S$.

14. 记 $SL(n, \mathbb{R}) = \{\boldsymbol{A} \in M_{n \times n} \mid \det \boldsymbol{A} = 1\}$. 证明: $SL(n, \mathbb{R})$ 是 $M_{n \times n}$ 中的闭集.

## 14.4 连续映射的整体性质

下面我们来研究连续映射的整体性质, 先看介值性, 它与集合的道路连通性密切相关.

设 $S \subseteq \mathbb{R}^n$. 如果任给 $\pmb{u}_0, \pmb{u}_1 \in S$, 均存在连续映射 $\sigma: [0,1] \to \mathbb{R}^n$, 使得 $\sigma(0) = \pmb{u}_0$, $\sigma(1) = \pmb{u}_1$, 且 $\sigma([0,1]) \subseteq S$, 则称 $S$ 是道路连通子集. 此时 $\sigma$ 称为 $S$ 中连接 $\pmb{u}_0$ 和 $\pmb{u}_1$ 的一条道路. 如果 $\sigma$ 的每一分量均为 $C^1$ 函数, 则称 $\sigma$ 为 $C^1$ 的道路. 如果存在 $[0,1]$ 的分割, 使得在每一个小区间上 $\sigma$ 都是 $C^1$ 的, 则称 $\sigma$ 是分段 $C^1$ 的道路.

例 14.4.1 设  $n \geqslant 2$ ，证明: $R^{n} \setminus \{0\}$  是  $R^{n}$  中的道路连通子集.

证明 设 $u_0, u_1$ 都不是原点. 若连接 $u_0$ 和 $u_1$ 的直线不经过原点, 则令

$$
\boldsymbol {\sigma} (t) = (1 - t) \boldsymbol {u} _ {0} + t \boldsymbol {u} _ {1}, \quad t \in [ 0, 1 ],
$$

此时  $\sigma$  是平面上连接  $u_{0}$  和  $u_{1}$  的一条道路, 且不经过原点.

若连接  $u_{0}$  和  $u_{1}$  的直线经过原点, 由于  $n \geqslant 2$ , 我们就可以在该直线之外任取一点 u. 令

$$
\boldsymbol {\sigma} (t) = \left\{ \begin{array}{l l} (1 - 2 t) \boldsymbol {u} _ {0} + 2 t \boldsymbol {u}, & 0 \leqslant t \leqslant \frac {1}{2}, \\ 2 (1 - t) \boldsymbol {u} + (2 t - 1) \boldsymbol {u} _ {1}, & \frac {1}{2} <   t \leqslant 1, \end{array} \right.
$$

则  $\sigma$  是平面上连接  $u_{0}$  和  $u_{1}$  的一条道路, 且不经过原点.

定理 14.4.1（介值定理） 设 S 为  $R^{n}$  中的道路连通子集,  $f: S \rightarrow R^{m}$  为连续映射, 则  $f(S)$  为  $R^{m}$  中的道路连通子集.

证明 任取 $v_{0}, v_{1} \in f(S)$, 则存在 $u_{0}, u_{1} \in S$, 使得 $f(u_{0}) = v_{0}, f(u_{1}) = v_{1}$. 设 $\sigma : [0,1] \to \mathbb{R}^{n}$ 是 $S$ 中连接 $u_{0}, u_{1}$ 的道路, 记 $\tau(t) = f(\sigma(t))$, 则 $\tau$ 就是 $f(S)$ 中连接 $v_{0}, v_{1}$ 的道路, 这说明 $f(S)$ 是道路连通子集.

定理 14.4.2 (零值定理) 设 S 为  $R^{n}$  中道路连通子集,  $f: S \rightarrow R$  为连续函数. 若  $f(\boldsymbol{u}_{0}) < 0$ ,  $f(\boldsymbol{u}_{1}) > 0$ , 则存在  $\zeta \in S$ , 使得  $f(\zeta) = 0$ .

证明 设 $\sigma : [0,1] \to \mathbb{R}^n$ 是 $S$ 中连接 $u_0, u_1$ 的道路, 记 $\tau(t) = f(\sigma(t))$, 则 $\tau : [0,1] \to \mathbb{R}$ 为连续函数, 且 $\tau(0) < 0$, $\tau(1) > 0$. 根据一元连续函数的零值定理, 存在 $\xi \in (0,1)$, 使得 $\tau(\xi) = 0$. 记 $\zeta = \sigma(\xi)$, 则 $f(\zeta) = 0$.

例 14.4.2 设  $f: S^{1} \rightarrow R$  为定义在单位圆周上的连续函数, 证明: 存在  $u \in S^{1}$ , 使得  $f(-u) = f(u)$ .

---

230

第十四章 多元函数与映射的极限与连续

证明 显然, 单位圆周是道路连通子集. 考虑函数 $g(\pmb{x}) = f(\pmb{x}) - f(-\pmb{x})$, 则 $g$ 也是 $S^1$ 上的连续函数, 且

$$
g (\boldsymbol {x}) g (- \boldsymbol {x}) = (f (\boldsymbol {x}) - f (- \boldsymbol {x})) (f (- \boldsymbol {x}) - f (\boldsymbol {x})) = - (f (\boldsymbol {x}) - f (- \boldsymbol {x})) ^ {2} \leqslant 0,
$$

根据零值定理, 存在  $u \in S^{1}$ , 使得  $g(u) = 0$ , 此时  $f(-u) = f(u)$ .

我们再看连续映射的一致连续性质和最值性质，它们都与有界闭集密切相关。设 $S \subseteq \mathbb{R}^n$ ，$\pmb{f}: S \to \mathbb{R}^m$ 为映射。如果任给 $\varepsilon > 0$ ，均存在 $\delta > 0$ ，使得对每一个 $\pmb{u} \in S$ ，均有

$$
\boldsymbol {f} \big (B _ {\delta} ^ {S} (\boldsymbol {u}) \big) \subseteq B _ {\varepsilon} \big (\boldsymbol {f} (\boldsymbol {u}) \big),
$$

则称 $f$ 一致连续. 显然, 一致连续意味着连续.

定理 14.4.3 (一致连续性) 设 $f: S \to \mathbb{R}^m$ 为连续映射. 若 $S$ 为有界闭集, 则 $f$ 一致连续.

证明 (反证法) 若不然, 则存在 $\varepsilon_0 > 0$, 使得对每一个正整数 $i$, 均存在 $\pmb{u}_i, \pmb{v}_i \in S$, 满足

$$
d (\boldsymbol {u} _ {i}, \boldsymbol {v} _ {i}) <   \frac {1}{i}, d \big (\boldsymbol {f} (\boldsymbol {u} _ {i}), \boldsymbol {f} (\boldsymbol {v} _ {i}) \big) \geqslant \varepsilon_ {0}.
$$

因为 $S$ 为有界闭集, 所以 $\{\pmb{u}_i\}$ 存在收敛子列. 不妨设它本身收敛于 $\pmb{u}_0$, 则 $\pmb{u}_0 \in S$. 由三角不等式可知 $\{\pmb{v}_i\}$ 也收敛于 $\pmb{u}_0$, 且

$$
\varepsilon_ {0} \leqslant d \big (\boldsymbol {f} (\boldsymbol {u} _ {i}), \boldsymbol {f} (\boldsymbol {u} _ {0}) \big) + d \big (\boldsymbol {f} (\boldsymbol {u} _ {0}), \boldsymbol {f} (\boldsymbol {v} _ {i}) \big).
$$

令 $i\to \infty$ ，由 $\pmb{f}$ 连续可知上式右边趋于零，这就导出了矛盾

定理 14.4.4（最值定理）设 $f: S \to \mathbb{R}^m$ 为连续映射。若 $S$ 为有界闭集，则 $f(S)$ 为 $\mathbb{R}^m$ 中的有界闭集。特别地，当 $m = 1$ 时，$f$ 达到最小值和最大值。

证明 先证明 $f(S)$ 有界. (反证法) 若不然, 则对每一个正整数 $i$, 均存在 $u_i \in S$, 使得 $\| f(u_i) \| > i$. 因为 $S$ 为有界闭集, 所以 $\{u_i\}$ 存在收敛子列. 不妨设它本身收敛于 $u_0$, 则 $u_0 \in S$. 由 $f$ 连续可知 $\{f(u_i)\}$ 收敛于 $f(u_0)$, 则 $\{f(u_i)\}$ 为有界点列, 这就导出了矛盾.

我们用命题14.2.1来说明 $f(S)$ 是闭集. 设 $\{f(u_i)\}$ 收敛于 $v_0$, 我们要说明 $v_0 \in f(S)$. 类似于前一段的论证, 不妨设 $\{u_i\}$ 收敛于 $u_0 \in S$. 由 $f$ 连续可知 $\{f(u_i)\}$ 收敛于 $f(u_0)$. 由极限的唯一性即知 $v_0 = f(u_0) \in f(S)$.

当 $m = 1$ 时, $f(S)$ 是 $\mathbb{R}^1$ 中的有界闭集, 其下确界和上确界分别记为 $\alpha, \beta$. 因为 $\alpha$ 是最大下界, 对每一个正整数 $i$, 就存在 $\alpha_i \in f(S)$, 使得

$$
\alpha \leqslant \alpha_ {i} <   \alpha + \frac {1}{i}.
$$

这说明  $\{\alpha_{i}\}$  是  $f(S)$  中收敛点列, 由  $f(S)$  为闭集即知其极限  $\alpha \in f(S)$ . 同理,  $\beta \in f(S)$ . 这说明 f 达到了最小值  $\alpha$  和最大值  $\beta$ . □

---

14.4 连续映射的整体性质

231

下面我们介绍最值定理的简单应用. 设  $\boldsymbol{A} = (a_{ij})_{n \times n}$  为 n 阶对称实方阵, 考虑函数  $Q : R^{n} \rightarrow R$ ,

$$
Q (\boldsymbol {x}) = \langle \boldsymbol {x}, \boldsymbol {A} \boldsymbol {x} \rangle = \sum_ {i, j = 1} ^ {n} a _ {i j} x _ {i} x _ {j}.
$$

若 $Q(\pmb{x})\geqslant 0$ 恒成立, 则称 $\mathbf{A}$ 半正定; 若 $\mathbf{A}$ 半正定, 且 $Q(\pmb {x}) = 0$ 仅在 $\pmb {x} = \mathbf{0}$ 处成立, 则称 $\mathbf{A}$ 正定.

例 14.4.3 设 A 为 n 阶正定矩阵, 证明: 存在正数  $\lambda, \mu$ , 使得

$$
\lambda \| \boldsymbol {x} \| ^ {2} \leqslant Q (\boldsymbol {x}) \leqslant \mu \| \boldsymbol {x} \| ^ {2}, \forall \boldsymbol {x} \in \mathbb {R} ^ {n}.
$$

证明 记 $S^{n-1} = \{\boldsymbol{x} \in \mathbb{R}^n \mid \| \boldsymbol{x} \| = 1\}$. 由题设可知 $Q(\boldsymbol{x})$ 在 $S^{n-1}$ 上恒为正. 注意到 $Q(\boldsymbol{x})$ 是连续函数, $S^{n-1}$ 是有界闭集, 由最值定理, $Q(\boldsymbol{x})$ 在 $S^{n-1}$ 上达到 (正的) 最小值 $\lambda$ 和最大值 $\mu$. 当 $\boldsymbol{x} \neq \boldsymbol{0}$ 时, 记 $\boldsymbol{x}' = \frac{\boldsymbol{x}}{\|\boldsymbol{x}\|}$, 则 $Q(\boldsymbol{x}) = \| \boldsymbol{x} \|^2 Q(\boldsymbol{x}')$, 于是

$$
\lambda \leqslant \frac {Q (\boldsymbol {x})}{\| \boldsymbol {x} \| ^ {2}} = Q (\boldsymbol {x} ^ {\prime}) \leqslant \mu .
$$

这就得到了欲证结论.

□

事实上, $\lambda, \mu$ 分别是 $\mathbf{A}$ 的最小特征值和最大特征值.

命题 14.4.5 $Q(x)$ 在 $S^{n-1}$ 上的最小值必为矩阵 $\mathbf{A}$ 的特征值.

证明 根据最值定理, 存在 $\pmb{u} \in S^{n-1}$, 使得 $Q(\pmb{u}) = \lambda$. 此时 $Q(\pmb{x}) \geqslant \lambda \| \pmb{x} \|^2$, $\forall \pmb{x} \in \mathbb{R}^n$. 特别地, 对任意 $\pmb{y} \in \mathbb{R}^n$, $t \in \mathbb{R}$, 有

$$
\varphi (t) = Q (\boldsymbol {u} + t \boldsymbol {y}) - \lambda \| \boldsymbol {u} + t \boldsymbol {y} \| ^ {2} \geqslant 0.
$$

$\varphi (t)$ 关于 $t$ 为光滑函数, $t = 0$ 时取到最小值0, 由Fermat引理可知 $\varphi^{\prime}(0) = 0$. 即

$$
\langle \boldsymbol {y}, \boldsymbol {A} \boldsymbol {u} \rangle + \langle \boldsymbol {u}, \boldsymbol {A} \boldsymbol {y} \rangle - \lambda \big (\langle \boldsymbol {u}, \boldsymbol {y} \rangle + \langle \boldsymbol {y}, \boldsymbol {u} \rangle \big) = 0.
$$

由 $\mathbf{A}$ 为对称方阵可得 $\langle y, Au - \lambda u \rangle = 0$. 取 $y = Au - \lambda u$, 由内积的正定性可得 $Au - \lambda u = 0$. 这说明 $\lambda$ 为 $\mathbf{A}$ 的特征值.

注 14.4.1 利用上述方法可以证明, 实对称矩阵的特征值全为实数.

## 习题14.4

1. 记 $S^{n-1} = \{\boldsymbol{x} \in \mathbb{R}^n \mid \| \boldsymbol{x} \| = 1\}$. 证明: 当 $n \geqslant 2$ 时 $S^{n-1}$ 是道路连通子集.
2. 记 $O(n) = \{\mathbf{A} \in M_{n \times n} \mid \mathbf{A}\mathbf{A}^{\mathrm{T}} = \mathbf{I}_n\}$. 证明:

(1)  $O(n)$  是  $M_{n \times n}$  中的有界闭集.
(2)  $O(n)$  不是道路连通的.

---

232

第十四章 多元函数与映射的极限与连续

3. 设 $S \subseteq \mathbb{R}^n$ 既是开集又是闭集, 证明: $S = \varnothing$ 或 $S = \mathbb{R}^n$.
4. 设 $f: \mathbb{R}^2 \to \mathbb{R}$ 为连续函数, 证明: 存在 $\pmb{u}_0 \neq \pmb{u}_1$, 使得 $f(\pmb{u}_0) = f(\pmb{u}_1)$.
5. 记 $f(x, y) = \cos(xy)$. 证明: $f$ 在 $\mathbb{R}^2$ 上不一致连续.
6. 设 $S$ 为 $\mathbb{R}^n$ 中的非空闭集, $\pmb{u}_0 \in \mathbb{R}^n$. 证明: 存在 $\pmb{u}_1 \in S$, 使得

$$
d (\boldsymbol {u} _ {0}, \boldsymbol {u} _ {1}) = \inf \{d (\boldsymbol {u} _ {0}, \boldsymbol {u}) \mid \boldsymbol {u} \in S \}.
$$

7. 设 $S$ 为 $\mathbb{R}^n$ 中的非空有界闭集, 证明: 存在 $\pmb{u}_0, \pmb{u}_1 \in S$, 使得

$$
d (\boldsymbol {u} _ {0}, \boldsymbol {u} _ {1}) = \sup \{d (\boldsymbol {u}, \boldsymbol {v}) \mid \boldsymbol {u}, \boldsymbol {v} \in S \}.
$$

8. 设 $\mathbf{A}$ 是 $n$ 阶实方阵且 $\det \mathbf{A} \neq 0$. 证明: 存在常数 $\lambda > 0$, 使得

$$
\| \boldsymbol {A} \boldsymbol {x} \| \geqslant \lambda \| \boldsymbol {x} \|, \forall \boldsymbol {x} \in \mathbb {R} ^ {n}.
$$

9. 设 $\pmb{A}$ 是 $n$ 阶正定矩阵, $\pmb{u} \in \mathbb{R}^n$, $c \in \mathbb{R}$. 记

$$
f (\boldsymbol {x}) = \langle \boldsymbol {x}, \boldsymbol {A} \boldsymbol {x} \rangle + \langle \boldsymbol {u}, \boldsymbol {x} \rangle + c, \forall \boldsymbol {x} \in \mathbb {R} ^ {n}.
$$

证明: $\lim_{x\to\infty}f(x)=+\infty,$  并求 f 的最小值.

10. 记 $SO(n) = \{\mathbf{A} \in O(n) \mid \det \mathbf{A} = 1\}$. 证明: 当 $n \geqslant 2$ 时 $SO(n)$ 是 $M_{n \times n}$ 中的道路连通子集.

## 14.5 Lipschitz 映射和零测集

我们知道, 定义在闭区间中的一元有界函数可积当且仅当其间断点集为零测集. 在研究多元函数的积分时, 我们将首先研究定义在 n 维闭矩形上的有界函数, 同样地要给出可积函数间断点集的刻画.

我们先看一类非常特殊的函数. 设 $S \subseteq \mathbb{R}^n$, 定义函数 $\chi_S: \mathbb{R}^n \to \mathbb{R}$ 如下:

$$
\chi_ {S} (\boldsymbol {x}) = \left\{ \begin{array}{l l} 1, & \boldsymbol {x} \in S, \\ 0, & \boldsymbol {x} \in \mathbb {R} ^ {n} \setminus S. \end{array} \right.
$$

$\chi_S$ 称为子集 $S$ 的特征函数. 不难看出, $\chi_S$ 在 $\pmb{u}$ 处连续时, 若 $\pmb{u} \in S$, 则存在 $r > 0$, 使得 $B_r(\pmb{u}) \subseteq S$; 若 $\pmb{u} \notin S$, 则存在 $r > 0$, 使得 $B_r(\pmb{u}) \subseteq \mathbb{R}^n \setminus S$. 为了方便起见, 我们再引进几个与子集有关的概念.

内点: 设  $u \in S$ . 如果存在 r > 0, 使得  $B_{r}(\boldsymbol{u}) \subseteq S$ , 则称 u 为 S 的内点. 内点的全体记为 intS 或  $S^{\circ}$ , 称为 S 的内部.

---

14.5 Lipschitz 映射和零测集

233

外点: 设 $\pmb{u} \notin S$. 如果存在 $r > 0$, 使得 $B_r(\pmb{u}) \subseteq \mathbb{R}^n \setminus S$, 则称 $\pmb{u}$ 为 $S$ 的外点. 外点的全体记为 $\operatorname{ext} S$, 称为 $S$ 的外部.

边界点: 设 $\pmb{u} \in \mathbb{R}^n$. 如果任给 $r > 0$, $B_r(\pmb{u})$ 中既有属于 $S$ 中的点, 也有不属于 $S$ 中的点, 则称 $\pmb{u}$ 为 $S$ 的边界点. 边界点的全体记为 $\partial S$, 称为 $S$ 的边界. $\partial S$ 就是特征函数 $\chi_S$ 的间断点 (不连续点) 集.

从定义不难看出, intS 是包含于 S 的 “最大” 开集, S 的外点就是  $R^{n} \setminus S$  的内点. 整个空间  $R^{n}$  可以分解为

$$
\mathbb {R} ^ {n} = \mathrm{int} S \cup \partial S \cup \mathrm{ext} S,
$$

上式右边的三个子集互不相交. 我们再列举几条今后会用到的性质:

- $\partial S$ 为闭集, 这是因为它的补集等于 intS ∪ extS.
- $\operatorname{int} S \cup \partial S$ 也是闭集, 记为 $\bar{S}$, 称为 $S$ 的闭包. 此外, $\bar{S} = S \cup \partial S$ 也成立. 这是因为

$$
\bar {S} \subseteq S \cup \partial S \subseteq (\mathrm{int} S \cup \partial S) \cup \partial S = \bar {S}.
$$

- $S$ 为闭集当且仅当 $\partial S \subseteq S$, 即 $S = \bar{S}$. 事实上, 若 $S$ 是闭集, 则 $\mathbb{R}^n \setminus S$ 为开集, 它里面的点不可能是边界点, 即 $\partial S \subseteq S$. 反之, 若 $\partial S \subseteq S$, 则 $S = \bar{S}$ 是闭集.
- 当 $S \subseteq T$ 时, $\bar{S} \subseteq \bar{T}$. 这是因为, 此时 $\mathbb{R}^n \setminus S \supseteq \mathbb{R}^n \setminus T$, 从而 $\operatorname{ext} S \supseteq \operatorname{ext} T$, 即 $\bar{S} \subseteq \bar{T}$ 成立.

例 14.5.1 球的边界.

设 $\pmb{u} \in \mathbb{R}^n, r > 0$. 由于 $B_r(\pmb{u})$ 和 $\mathbb{R}^n \setminus \overline{B_r(\pmb{u})}$ 均为开集, 故

$$
\partial B _ {r} (\boldsymbol {u}) = \left\{\boldsymbol {x} \in \mathbb {R} ^ {n}   \big |   \| \boldsymbol {x} - \boldsymbol {u} \| = r \right\},
$$

称为以 u 为中心, r 为半径的 n-1 维球面.

下面我们将 $\mathbb{R}$ 中零测集的概念推广到 $\mathbb{R}^n$ 中.

零测集: 设 $C \subseteq \mathbb{R}^n$. 如果任给 $\varepsilon > 0$, 存在至多可数个矩形 $\{I_i\}$, 使得

$$
C \subseteq \bigcup_ {i \geqslant 1} I _ {i}, \quad \sum_ {i \geqslant 1} \nu (I _ {i}) <   \varepsilon ,
$$

则称 C 为  $R^{n}$  中的零测集.

和一维的情形类似, 不难看出: 有限点集均为零测集, 零测集的子集仍为零测集, 可数个零测集之并仍为零测集.

设  $\boldsymbol{u}=(u_{1},u_{2},\cdots,u_{n})\in\mathbb{R}^{n},r>0,$  记  $I_{r}(\boldsymbol{u})=\prod_{i=1}^{n}[u_{i}-r,u_{i}+r]$ ，称为以 u 为中心，2r 为边长的 n 维（闭）方体。在零测集定义中，“矩形”也可以换成“方体”，这可以从如下简单引理看出来。

引理 14.5.1 设 I 为 n 维矩形, 则 I 可被容积之和不超过  $2^{n-1}\nu(I)$  的有限个方体所覆盖.

---

234

第十四章 多元函数与映射的极限与连续

证明 不妨设 $n \geqslant 2$. 基本的想法是将 $I$ 的各边延长为最短边长度的整数倍, 然后将其分割为若干个 $n$ 维方体. 设 $I = \prod_{i=1}^{n}[a_i, b_i]$, 记 $\ell = \min\{b_i - a_i \mid 1 \leqslant i \leqslant n\}$, 不妨设 $b_1 - a_1 = \ell$. 记 $k_1 = 0, c_1 = b_1$. 当 $i > 1$ 时, 设 $k_i$ 是不超过 $(b_i - a_i)/\ell$ 的最大整数, 记 $c_i = a_i + (k_i + 1)\ell$. 令 $J = \prod_{i=1}^{n}[a_i, c_i]$, 则 $I \subseteq J$. 显然, $J$ 可以分割为 $\prod_{i=1}^{n}(k_i + 1)$ 个边长为 $\ell$ 的 $n$ 维方体, 其容积之和满足

$$
\left(\prod_ {i = 1} ^ {n} (k _ {i} + 1)\right) \ell^ {n} \leqslant \left(\prod_ {i = 2} ^ {n} (2 k _ {i})\right) \ell^ {n} \leqslant 2 ^ {n - 1} \nu (I).
$$

例 14.5.2 设 I 为 n 维矩形,  $f: I \rightarrow R^{m}$  为连续映射. 记

$$
G _ {\boldsymbol {f}} = \big \{\big (\boldsymbol {x}, \boldsymbol {f} (\boldsymbol {x}) \big) \in \mathbb {R} ^ {n + m} \mid \boldsymbol {x} \in I \big \},
$$

证明: $G_{f}$ 是 $\mathbb{R}^{n + m}$ 中的零测集.

证明 先看一个最简单的情形: $f \equiv c$, 其中 $c \in \mathbb{R}^m$. 任给 $\varepsilon > 0$, 设 $\delta$ 为待定正数. 设 $I_{\delta}(c)$ 是以 $c$ 为中心的 $m$ 维方体, 记 $J = I \times I_{\delta}(c)$, 则 $J$ 为 $n + m$ 维矩形. 显然, $G_f \subseteq J$, 且当 $\delta$ 充分小时, $J$ 的容积满足

$$
\nu (J) = \nu (I) \nu \big (I _ {\delta} (\boldsymbol {c}) \big) = \nu (I) (2 \delta) ^ {m} <   \varepsilon .
$$

按照定义, $G_{f}$ 为 $R^{n+m}$ 中的零测集.

我们再看一般情形.任给 $\varepsilon > 0$，设 $\delta$ 为待定正数.根据定理14.4.3，我们可以将 $I$ 等分为有限个小矩形 $\{I_i\}$，使得每一个 $f(I_i)$ 的直径均小于 $\delta$.取 $c_i \in f(I_i)$，则 $f(I_i) \subseteq I_\delta(c_i)$.于是 $G_f$ 包含于有限个 $n + m$ 维矩形 $\{I_i \times I_\delta(c_i)\}$ 的并集之中.当 $\delta$ 充分小时，它们的容积之和满足

$$
\sum_ {i} \nu (I _ {i}) \nu \big (I _ {\delta} (\boldsymbol {c} _ {i}) \big) = \sum_ {i} \nu (I _ {i}) (2 \delta) ^ {m} = \nu (I) (2 \delta) ^ {m} <   \varepsilon .
$$

按照定义, $G_{f}$ 为 $R^{n+m}$ 中的零测集.

下面我们再简单介绍一下零测集的不变性质, 这将用于多元函数积分的变量替换.

Lipschitz 映射: 设 $S \subseteq \mathbb{R}^n$, $\pmb{f}: S \to \mathbb{R}^m$ 为映射. 如果存在非负常数 $L$, 使得

$$
d \big (\boldsymbol {f} (\boldsymbol {x}), \boldsymbol {f} (\boldsymbol {y}) \big) \leqslant L   d (\boldsymbol {x}, \boldsymbol {y}), \forall \boldsymbol {x}, \boldsymbol {y} \in S, \tag {14.5.1}
$$

则称 $f$ 为Lipschitz映射, $m = 1$ 时称为Lipschitz函数. 显然, Lipschitz映射是一致连续的.

例 14.5.3 设  $S \subseteq R^{n}$  为非空子集, 当  $x \in R^{n}$  时, 定义

$$
d (\boldsymbol {x}, S) = \inf \{d (\boldsymbol {x}, \boldsymbol {u}) \mid \boldsymbol {u} \in S \},
$$

证明: $d(\pmb {x},S)$ 是Lipschitz函数，且 $d(\pmb {x},S) = 0$ 当且仅当 $\pmb {x}\in \bar{S}$

---

14.5 Lipschitz 映射和零测集

235

证明 任取 $x, y \in \mathbb{R}^n$, 由三角不等式可知

$$
d (\boldsymbol {x}, \boldsymbol {u}) \leqslant d (\boldsymbol {x}, \boldsymbol {y}) + d (\boldsymbol {y}, \boldsymbol {u}), \forall \boldsymbol {u} \in S.
$$

在上式中关于  $u \in S$  取下确界可得  $d(x, S) \leqslant d(x, y) + d(y, S)$ . 交换 x, y 的位置时此不等式当然也成立, 这说明  $|d(x, S) - d(y, S)| \leqslant d(x, y)$ .

显然, $d(\pmb {x},S)\geqslant 0$ .若 $d(\pmb {x},S) = 0$ ，则存在 $S$ 中一列点 $\{\pmb{u}_i\}$ ，使得 $\lim_{i\to +\infty}d(\pmb {x},\pmb{u}_i) = 0,$ 此时 $\pmb {x}\in \bar{S}$ .反之，若 $\pmb {x}\in \bar{S}$ ，则存在 $S$ 中一列点 $\{\pmb {u}_i\}$ ，使得 $\lim_{i\to +\infty}d(\pmb {x},\pmb{u}_i) = 0$ ，此时$d(\pmb {x},S) = 0.$

$d(\boldsymbol{x},S)$  称为到 S 的距离函数, 它的一个用处体现在下例中.

例 14.5.4 设 C, D 是  $R^{n}$  中两个不相交的非空闭集, 证明: 存在连续函数  $\rho: R^{n} \rightarrow R$ , 使得

$$
0 \leqslant \rho \leqslant 1, \left. \rho \right| _ {C} \equiv 1, \left. \rho \right| _ {D} \equiv 0.
$$

证明 根据前例, 当  $x \in R^{n}$  时均有  $d(x, C) + d(x, D) > 0$ . 令

$$
\rho (\boldsymbol {x}) = \frac {d (\boldsymbol {x} , D)}{d (\boldsymbol {x} , C) + d (\boldsymbol {x} , D)}, \forall \boldsymbol {x} \in \mathbb {R} ^ {n},
$$

则  $\rho$  是满足要求的连续函数.

例 14.5.5 设 U 为  $R^{n}$  中的道路连通的开子集, 证明: 任给  $u_{0}, u_{1} \in U$ , 存在 U 中分段  $C^{1}$  的道路连接  $u_{0}, u_{1}$ .

证明 若 $U = \mathbb{R}^n$，取 $\sigma(t) = (1 - t)\pmb{u}_0 + t\pmb{u}_1$，则 $\pmb{\sigma}$ 是连接 $\pmb{u}_0$ 和 $\pmb{u}_1$ 的 $C^1$ 道路。下设 $U \neq \mathbb{R}^n$，$\pmb{\sigma}$ 是 $U$ 中连接 $\pmb{u}_0$ 和 $\pmb{u}_1$ 的道路。距离函数 $d(\pmb{x}, \mathbb{R}^n \setminus U)$ 在有界闭集 $\pmb{\sigma}([0,1])$ 上的最小值记为 $\delta$，则 $\delta > 0$。根据一致连续性，存在正整数 $m$，使得对每一个 $0 \leqslant i \leqslant m - 1$，$\pmb{\sigma}([t_i, t_{i+1}])$ 的直径均小于 $\delta$，其中 $t_i = \frac{i}{m} (0 \leqslant i \leqslant m)$。定义 $\tau: [0,1] \to \mathbb{R}^n$ 为

$$
\boldsymbol {\tau} (t) = m (t _ {i + 1} - t) \boldsymbol {\sigma} (t _ {i}) + m (t - t _ {i}) \boldsymbol {\sigma} (t _ {i + 1}), \forall t \in [ t _ {i}, t _ {i + 1} ], i = 0, 1, \dots , m - 1.
$$

$\tau$ 是连接 $u_{0}$ 和 $u_{1}$ 的折线段. 容易验证 $\tau([0,1]) \subseteq U$.

![](../../raw/pages_0529-0544/images/page_539_image_16.jpg)

注14.5.1 $\mathbb{R}^n$ 上的道路连通开集常称为区域，区域的闭包常称为闭区域(闭域).

受距离函数定义的启发, 我们还有如下结果.

引理14.5.2 设 $S$ 为 $\mathbb{R}^n$ 中的子集, $f: S \to \mathbb{R}$ 满足条件 $|f(x) - f(y)| \leqslant Ld(x,y)$, 则存在函数 $F: \mathbb{R}^n \to \mathbb{R}$, 满足条件 $F|_S = f$ 且 $|F(x) - F(y)| \leqslant Ld(x,y)$.

证明 若 $F$ 是预想中的函数, 则当 $\pmb{x} \in \mathbb{R}^n$ 时, 应该有

$$
F (\boldsymbol {x}) \leqslant F (\boldsymbol {u}) + L d (\boldsymbol {x}, \boldsymbol {u}) = f (\boldsymbol {u}) + L d (\boldsymbol {x}, \boldsymbol {u}), \forall \boldsymbol {u} \in S.
$$

---

236

第十四章 多元函数与映射的极限与连续

受此启发, 我们定义 $F(\pmb{x}) = \inf \{f(\pmb{u}) + Ld(\pmb{x},\pmb{u})\mid \pmb {u}\in S\}$. 我们首先说明 $F(\pmb {x})$ 有意义: 固定一个 $\pmb {v}\in S,$ 则当 $\pmb {x}\in \mathbb{R}^n$ 时

$$
f (\boldsymbol {u}) + L d (\boldsymbol {x}, \boldsymbol {u}) \geqslant f (\boldsymbol {v}) - L d (\boldsymbol {u}, \boldsymbol {v}) + L d (\boldsymbol {x}, \boldsymbol {u}) \geqslant f (\boldsymbol {v}) - L d (\boldsymbol {x}, \boldsymbol {v}),
$$

这说明  $\{f(\boldsymbol{u})+L\,d(\boldsymbol{x},\boldsymbol{u})\mid\boldsymbol{u}\in S\}$  有下界, 从而有下确界.

其次, 我们验证 $F|_{S} = f$. 设 $\pmb{v} \in S$, 由题设可得

$$
f (\boldsymbol {v}) \leqslant f (\boldsymbol {u}) + L d (\boldsymbol {v}, \boldsymbol {u}), \forall \boldsymbol {u} \in S,
$$

且 u = v 时等号成立. 这说明  $F(v) = f(v)$ .

最后, 我们验证 $F$ 是 Lipschitz 函数. 当 $\pmb{x}, \pmb{y} \in \mathbb{R}^n$ 时, 由三角不等式可得

$$
f (\boldsymbol {u}) + L d (\boldsymbol {x}, \boldsymbol {u}) \leqslant f (\boldsymbol {u}) + L d (\boldsymbol {y}, \boldsymbol {u}) + L d (\boldsymbol {x}, \boldsymbol {y}),
$$

在上式中关于 $\pmb{u} \in S$ 取下确界可得 $F(\pmb{x}) \leqslant F(\pmb{y}) + Ld(\pmb{x},\pmb{y})$. 交换 $\pmb{x},\pmb{y}$ 的位置不等式当然也成立, 这说明 $|F(\pmb{x}) - F(\pmb{y})| \leqslant Ld(\pmb{x},\pmb{y})$.

$F$ 称为 $f$ 的Lipschitz延拓.利用上述引理,我们还可以将向量值的Lipschitz函数做类似的延拓.

推论14.5.3 设 $S$ 为 $\mathbb{R}^n$ 中的子集, $\pmb{f}: S \to \mathbb{R}^m$ 为 Lipschitz 映射, 则存在 Lipschitz 映射 $\pmb{F}: \mathbb{R}^n \to \mathbb{R}^m$, 使得 $\pmb{F}|_S = \pmb{f}$.

证明 设 f 满足条件 (14.5.1) 式. 记  $\boldsymbol{f}(\boldsymbol{x}) = (f_{1}(x), f_{2}(x), \cdots, f_{m}(x))$ ，则

$$
\left| f _ {i} (\boldsymbol {x}) - f _ {i} (\boldsymbol {y}) \right| \leqslant d \big (f (\boldsymbol {x}), f (\boldsymbol {y}) \big) \leqslant L d (\boldsymbol {x}, \boldsymbol {y}), \forall 1 \leqslant i \leqslant m.
$$

由前一引理, 存在  $F_{i}: R^{n} \rightarrow R$ , 使得  $F_{i}|_{S} = f_{i}$ , 且  $|F_{i}(\boldsymbol{x}) - F_{i}(\boldsymbol{y})| \leqslant L d(\boldsymbol{x}, \boldsymbol{y})$ . 记  $\boldsymbol{F}(\boldsymbol{x}) = (F_{1}(\boldsymbol{x}), F_{2}(\boldsymbol{x}), \cdots, F_{m}(\boldsymbol{x}))$ , 则

$$
d \big (\boldsymbol {F} (\boldsymbol {x}), \boldsymbol {F} (\boldsymbol {y}) \big) = \| \boldsymbol {F} (\boldsymbol {x}) - \boldsymbol {F} (\boldsymbol {y}) \| \leqslant \sqrt {m} L d (\boldsymbol {x}, \boldsymbol {y}).
$$

注 14.5.2 1934 年, Kirschbraun 证明了更强的结论: 可以适当地选取延拓 F, 使得  $d(\boldsymbol{F}(\boldsymbol{x}), \boldsymbol{F}(\boldsymbol{y})) \leqslant L d(\boldsymbol{x}, \boldsymbol{y})$ .

最后我们说明 Lipschitz 映射与零测集之间的关系.

命题14.5.4 设 $S$ 为 $\mathbb{R}^n$ 中的零测集, $f: S \to \mathbb{R}^n$ 为 Lipschitz 映射, 则 $f(S)$ 也是 $\mathbb{R}^n$ 中的零测集.

证明 根据上述推论, 不妨设 $f$ 定义在整个 $\mathbb{R}^n$ 上. 根据零测集的定义以及引理14.5.1, 任给 $\varepsilon > 0$, 存在至多可数个方体 $\{I_i = I_{r_i}(\boldsymbol{u}_i)\}$, 使得

$$
S \subseteq \bigcup_ {i \geqslant 1} I _ {i}, \quad \sum_ {i \geqslant 1} \nu (I _ {i}) = \sum_ {i \geqslant 1} (2 r _ {i}) ^ {n} <   \varepsilon .
$$

---

14.5 Lipschitz 映射和零测集

237

设 $\| f(x) - f(y)\| \leqslant L\| x - y\|$, 则当 $x \in I_i$ 时,

$$
\| \boldsymbol {f} (\boldsymbol {x}) - \boldsymbol {f} (\boldsymbol {u} _ {i}) \| \leqslant L \| \boldsymbol {x} - \boldsymbol {u} _ {i} \| \leqslant \sqrt {n} L r _ {i}.
$$

这说明 $\pmb{f}(I_i)\subseteq B_{\delta_i}\big(\pmb {f}(\pmb {u}_i)\big)$ ，其中 $\delta_i = \sqrt{n} Lr_i$ 记 $J_{i} = I_{\delta_{i}}\big(\pmb {f}(\pmb {u}_{i})\big)$ ，则 $J_{i}\supseteq \pmb {f}(I_{i})$ ，于是

$$
\boldsymbol {f} (S) \subseteq \bigcup_ {i \geqslant 1} \boldsymbol {f} (I _ {i}) \subseteq \bigcup_ {i \geqslant 1} J _ {i},
$$

且

$$
\sum_ {i \geqslant 1} \nu (J _ {i}) = \sum_ {i \geqslant 1} (2 \sqrt {n} L r _ {i}) ^ {n} <   (\sqrt {n} L) ^ {n} \varepsilon ,
$$

这说明  $f(S)$  为  $R^{n}$  中的零测集.

设 $A \in M_{n \times n}, b \in \mathbb{R}^n$, 记 $\varphi(x) = Ax + b$, 映射 $\varphi: \mathbb{R}^n \to \mathbb{R}^n$ 称为仿射变换. 由范数不等式可知

$$
\| \varphi (\boldsymbol {x}) - \varphi (\boldsymbol {y}) \| = \| \boldsymbol {A} (\boldsymbol {x} - \boldsymbol {y}) \| \leqslant \| \boldsymbol {A} \| \| \boldsymbol {x} - \boldsymbol {y} \|,
$$

这说明仿射变换是 Lipschitz 映射, 因此将零测集映为零测集.

## 习题14.5

1. 设 $f$ 是定义在 $S$ 上的一致连续函数. 证明: 存在定义在 $\bar{S}$ 上的一致连续函数 $g$, 使得 $g|_S = f$.

2. 设 $f: \mathbb{R}^n \to \mathbb{R}^m$ 为连续映射, $S \subseteq \mathbb{R}^n$.

(1) 证明: $\boldsymbol{f}(\bar{S}) \subseteq \overline{\boldsymbol{f}(S)}$.
(2) 举例说明 f 未必将闭集映为闭集.

3. 设 $S, T$ 为 $\mathbb{R}^n$ 中的子集, 证明:

$$
\chi_ {S \cap T} = \chi_ {S} \chi_ {T}, \chi_ {S \cup T} = \chi_ {S} + \chi_ {T} - \chi_ {S} \chi_ {T}.
$$

4. 设 $S, T \subseteq \mathbb{R}^n$, 证明: $\operatorname{int}(S \cap T) = \operatorname{int} S \cap \operatorname{int} T$, $\overline{S \cup T} = \bar{S} \cup \bar{T}$.
5. 设 $S \subseteq \mathbb{R}^n$, 证明: $\partial \bar{S} \subseteq \partial S$, 并举例说明等号不一定成立.
6. 设 $S \subseteq \mathbb{R}^n$, $\pmb{u} \in S$. 如果存在 $r > 0$, 使得 $B_r(\pmb{u}) \cap S = \{\pmb{u}\}$, 则称 $\pmb{u}$ 为 $S$ 的孤立点. 证明: 孤立点必为边界点.

7. 设 $S \subseteq \mathbb{R}^n$, $S$ 的聚点的全体记为 $S'$. 证明: $S'$ 为闭集, 且 $S' \cup \partial S = \bar{S}$.

8. 设 $S \subseteq \mathbb{R}^n$, $\pmb{u} \in \bar{S}$. 证明: $S$ 中存在收敛于 $\pmb{u}$ 的点列.

9. 设 $D$ 为 $\mathbb{R}^n$ 中的开集, $S \subseteq D$. 若 $S$ 为有界闭集, 证明: 存在 $\delta > 0$, 使得 $\{\pmb{x} \in \mathbb{R}^n \mid d(\pmb{x}, S) \leqslant \delta\} \subseteq D$.

10. 设 $S \subseteq \mathbb{R}^n$. 如果任给 $\pmb{x} \in \mathbb{R}^n$, 均存在 $r > 0$, 使得 $S \cap B_r(\pmb{x})$ 为零测集, 证明: $S$ 为零测集.

---

238

第十四章 多元函数与映射的极限与连续

11. 设 $S$ 为 $\mathbb{R}^n$ 中的零测集, 证明: $S \times \mathbb{R}^m$ 为 $\mathbb{R}^{n+m}$ 中的零测集.
12. 设 $\gamma : (a, b) \to \mathbb{R}^2$ 为连续曲线, 其中 $\gamma(t) = (x(t), y(t))$. 如果 $x$ 或 $y$ 为 $t$ 的 $C^1$ 函数, 证明: $\gamma((a, b))$ 为 $\mathbb{R}^2$ 中的零测集.
13. 设 $I$ 为 $\mathbb{R}^n$ 中的 $n$ 维矩形, 证明: $\partial I$ 为 $\mathbb{R}^n$ 中的零测集.
14. 设 $V$ 为 $\mathbb{R}^n$ 中的仿射子向量空间. 证明: 若 $V \neq \mathbb{R}^n$, 则 $V$ 为 $\mathbb{R}^n$ 中的零测集.
15. 证明: $S^{n-1}$ 是 $\mathbb{R}^n$ 中的零测集.
