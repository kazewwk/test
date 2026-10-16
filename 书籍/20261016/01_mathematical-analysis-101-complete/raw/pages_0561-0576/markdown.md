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

![](images/page_567_image_12.jpg)

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

![](images/page_567_image_20.jpg)

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

我们知道对于一元函数, 在函数的复合运算中, 一阶微分具有形式不变性. 下面我们指出, 对于多元函数, 仍然成立一阶微分形式不变性, 即在计算函数的全微分时, 无论该函数的自变量、因变量还是中间变量是什么, 其全微分的形式保持不变. 这是数学分析中的一条极其重要的性质, 它使得我们不必区分变量的类型, 即自变量、因变量或中间变量, 而直接利用一元函数的微分性质进行计算, 从而简化了多元函数微分学的处理过程.

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

如果把定理 15.4.1 类比于 Lagrange 微分中值定理的话, 那么下面的推论则对应着一元函数的 Rolle 微分中值定理, 而证明的基本思想与一元函数的 Fermat 引理如出一辙: 有界闭区域上的连续函数必能取到最大、最小值, 而且在极值点处函数如果可微, 则梯度为零. 作为练习, 详细证明留给读者.

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