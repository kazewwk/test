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

![](images/page_579_image_12.jpg)

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

函数的最值和极值通常放在一起讨论. 我们知道, 极值是一个局部概念, 关注的是函数在某点邻域内取值的大小比较, 所以一个函数在一点处的极大值很有可能不如该函数在另一点处的极小值来得大. 最值是一个全局概念, 研究的是函数在整个定义域或在指定点集上的最大 (小) 值. 然而两者又有密切的联系. 最值的讨论一般是在考虑了所有的极值点、边界点和一些特殊点处的函数值后, 加以比较, 再从中考虑其最大或最小值.

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

![](images/page_586_image_2.jpg)

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