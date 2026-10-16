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