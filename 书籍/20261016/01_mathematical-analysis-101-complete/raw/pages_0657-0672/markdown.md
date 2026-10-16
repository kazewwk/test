解 被积函数是连续函数, 因此重积分可以化为累次积分:

$$
\begin{array}{l} \iiint_ {I} \frac {\mathrm{d} x \mathrm{d} y \mathrm{d} z}{(1 + x + y + z) ^ {3}} = \int_ {0} ^ {1} \mathrm{d} x \int_ {0} ^ {1} \mathrm{d} y \int_ {0} ^ {1} \frac {\mathrm{d} z}{(1 + x + y + z) ^ {3}} \\ = \int_ {0} ^ {1} \mathrm{d} x \int_ {0} ^ {1} \frac {1}{2} \left[ \frac {1}{(1 + x + y) ^ {2}} - \frac {1}{(2 + x + y) ^ {2}} \right] \mathrm{d} y \\ = \int_ {0} ^ {1} \frac {1}{2} \left[ \left(\frac {1}{1 + x} - \frac {1}{2 + x}\right) - \left(\frac {1}{2 + x} - \frac {1}{3 + x}\right) \right] \mathrm{d} x \\ = \frac {1}{2} (5 \ln 2 - 3 \ln 3). \\ \end{array}
$$

现在我们讨论 Jordan 可测集上的重积分化为累次积分的问题, 这往往可以通过考虑矩形上的积分予以解决.

设 $y_{1}(x)\leqslant y_{2}(x)$ 为 $[a,b]$ 上的连续函数(图16.4)，考虑有界集合

$$
A = \{(x, y) \in \mathbb {R} ^ {2} \mid y _ {1} (x) \leqslant y \leqslant y _ {2} (x), a \leqslant x \leqslant b \},
$$

其边界为零测集, 因此 A 为 Jordan 可测集.

![](images/page_656_image_8.jpg)

<details>
<summary>text_image</summary>

y
y₂(x)
A
y₁(x)
O
a
x
b
x
</details>

图16.4 重积分的投影法

定理 16.3.4 设 $y_{1}, y_{2}$ 和 $A$ 如上, $f \in R(A)$, 且对于每一个 $x \in [a, b]$, 关于 $y$ 的积分 $\int_{y_{1}(x)}^{y_{2}(x)} f(x, y) \mathrm{d}y$ 均存在, 则

$$
\int_ {A} f = \int_ {a} ^ {b} \mathrm{d} x \int_ {y _ {1} (x)} ^ {y _ {2} (x)} f (x, y) \mathrm{d} y.
$$

证明 记 $y_{1}$ 的最小值为 $c, y_{2}$ 的最大值为 $d$, 则 $A \subseteq [a, b] \times [c, d]$. 由 $f \in R(A)$ 可知 $f_{A}$ 在 $[a, b] \times [c, d]$ 上可积. 当 $x \in [a, b]$ 时, $f_{A}(x, y)$ 关于 $y$ 在 $[c, d]$ 上的积分等于 $f(x, y)$ 关于 $y$ 在 $A_{x} = [y_{1}(x), y_{2}(x)]$ 上的积分. 从而有

$$
\begin{array}{l} \int_ {A} f = \int_ {[ a, b ] \times [ c, d ]} f _ {A} = \int_ {a} ^ {b} \mathrm{d} x \int_ {c} ^ {d} f _ {A} (x, y) \mathrm{d} y \\ = \int_ {a} ^ {b} \mathrm{d} x \int_ {y _ {1} (x)} ^ {y _ {2} (x)} f (x, y) \mathrm{d} y. \\ \end{array}
$$

□

同理, 如果 A 形如

$$
\{(x, y) \in \mathbb {R} ^ {2} \mid x _ {1} (y) \leqslant x \leqslant x _ {2} (y), c \leqslant y \leqslant d \},
$$

在类似条件下就有 (图 16.5)

$$
\int_ {A} f = \int_ {c} ^ {d} \mathrm{d} y \int_ {x _ {1} (y)} ^ {x _ {2} (y)} f (x, y) \mathrm{d} x.
$$

![](images/page_657_image_6.jpg)

<details>
<summary>text_image</summary>

y
d
A
x₁(y)
y
c
O
x₂(y)
</details>

图16.5 向 $y$ 轴的投影

对于一般的 n 重积分, 类似的结果也成立, 我们仅举例说明.

例 16.3.4 计算积分  $I=\iint_{A}x^{2}y^{2}\,dx\,dy$ ，其中 A 是由直线 y=0, x=1 和 y=x 围成的三角形区域 (图 16.6).

![](images/page_657_image_10.jpg)

<details>
<summary>text_image</summary>

y
y=x
A
O
x=1
1
x
</details>

图 16.6 三角区域投影

解 利用向 x 轴作投影, 得

$$
I = \int_ {0} ^ {1} \mathrm{d} x \int_ {0} ^ {x} x ^ {2} y ^ {2} \mathrm{d} y = \int_ {0} ^ {1} \frac {1}{3} x ^ {5} \mathrm{d} x = \frac {1}{1 8}.
$$

例 16.3.5 计算积分  $I = \iint_{A} y^{2} dx dy$ ，其中 A 是由直线 2x - y - 1 = 0 与抛物线  $x = y^{2}$  所围成的区域.

解 如图 16.7(a), 直线 2x - y - 1 = 0 与抛物线  $x = y^{2}$  的交点为  $(1/4, -1/2)$  和  $(1, 1)$ . 利用向 y 轴作投影, 得

$$
I = \int_ {- \frac {1}{2}} ^ {1} \mathrm{d} y \int_ {y ^ {2}} ^ {\frac {y + 1}{2}} y ^ {2} \mathrm{d} x = \int_ {- \frac {1}{2}} ^ {1} \left[ \frac {1}{2} y ^ {2} (y + 1) - y ^ {4} \right] \mathrm{d} y = \frac {6 3}{6 4 0}.
$$

![](images/page_658_image_4.jpg)

<details>
<summary>text_image</summary>

y
x=\frac{1}{2}(y+1)
1
x=y^2
O
A
-1/2
x
1
</details>

(a)

![](images/page_658_chart_6.jpg)

<details>
<summary>area</summary>

| Point | X | Y |
| --- | --- | --- |
| Intersection (x=0, y=x) | 0 | 0 |
| Intersection (x=1, y=x) | 1 | 1 |
</details>

(b)

图 16.7 直线和抛物线相交区域的投影

例16.3.6 计算积分 $I = \int_0^1\mathrm{d}y\int_{y}^{\sqrt{y}}\frac{\sin x}{x}\mathrm{d}x.$

解 这个积分必须交换次序才行. 如图 16.7(b), 它可以看成连续函数  $\frac{\sin x}{x}$  在由直线 y = x 和抛物线  $y = x^{2}$  所围成的区域中的积分, 因而

$$
I = \int_ {0} ^ {1} \mathrm{d} x \int_ {x ^ {2}} ^ {x} \frac {\sin x}{x} \mathrm{d} y = \int_ {0} ^ {1} \frac {\sin x}{x} (x - x ^ {2}) \mathrm{d} x = 1 - \sin 1.
$$

![](images/page_658_image_12.jpg)

例 16.3.7 求 n 维单形  $\Delta_{n}(a)$  (a > 0) 的容积, 其中

$$
\Delta_ {n} (a) = \{(x _ {1}, x _ {2}, \dots , x _ {n}) \in \mathbb {R} ^ {n} \mid x _ {1} \geqslant 0, x _ {2} \geqslant 0, \dots , x _ {n} \geqslant 0, x _ {1} + x _ {2} + \dots + x _ {n} \leqslant a \}.
$$

n = 3 的情形见图 16.8.

![](images/page_658_image_16.jpg)

<details>
<summary>text_image</summary>

y
a
O
x
a
z
a
</details>

图 16.8 三角面的投影

解 被积区域 $\Delta_n(a)$ 可以表示为

$$
\{x \in \mathbb {R} ^ {n} \mid 0 \leqslant x _ {1} \leqslant a, 0 \leqslant x _ {2} \leqslant a - x _ {1}, \dots ,
$$

$$
0 \leqslant x _ {n} \leqslant a - x _ {1} - \dots - x _ {n - 1} \},
$$

因此

$$
\nu (\Delta_ {n} (a)) = \int_ {0} ^ {a} \mathrm{d} x _ {1} \int_ {0} ^ {a - x _ {1}} \mathrm{d} x _ {2} \dots \int_ {0} ^ {a - x _ {1} - \dots - x _ {n - 1}} \mathrm{d} x _ {n}.
$$

在上式右端中对各个一元积分依次做变量替换

$$
y _ {n} = x _ {1} + x _ {2} + \dots + x _ {n}, \dots , y _ {2} = x _ {1} + x _ {2}, y _ {1} = x _ {1},
$$

可得

$$
\begin{array}{l} \nu (\Delta_ {n} (a)) = \int_ {0} ^ {a} \mathrm{d} y _ {1} \int_ {y _ {1}} ^ {a} \mathrm{d} y _ {2} \dots \int_ {y _ {n - 1}} ^ {a} \mathrm{d} y _ {n} \\ = \int_ {0} ^ {a} \mathrm{d} y _ {1} \int_ {y _ {1}} ^ {a} \mathrm{d} y _ {2} \dots \int_ {y _ {n - 2}} ^ {a} (a - y _ {n - 1}) \mathrm{d} y _ {n - 1} \\ = \dots = \frac {1}{(n - 1) !} \int_ {0} ^ {a} (a - y _ {1}) ^ {n - 1} \mathrm{d} y _ {1} \\ = \frac {a ^ {n}}{n !}. \\ \end{array}
$$

注 16.3.1 显然, $\nu(\Delta_{1}(a))=a$ . 利用向 $x_{1}$ 轴作投影可得

$$
\nu (\Delta_ {n} (a)) = \int_ {0} ^ {a} \nu (\Delta_ {n - 1} (a - x _ {1})) \mathrm{d} x _ {1}.
$$

对 $n$ 进行归纳也容易得出 $\nu (\Delta_n(a)) = \frac{1}{n!} a^n.$

## 习题 16.3

1. 计算下列积分:

(1) $\iint_{I} \frac{x^2}{2 - y^2} \, \mathrm{d}x \, \mathrm{d}y, I = [0,1] \times [0,1]$;
(2) $\iint_{I} \sin (x + y) \, \mathrm{d}x \, \mathrm{d}y, I = [0, \pi/2] \times [0, \pi/2]$;
(3) $\iint_{A} \sin x^{2} \, \mathrm{d}x \, \mathrm{d}y$, $A$ 是由 $y = 0$, $x = \sqrt{\pi/2}$, $y = x$ 所围成的区域;
(4) $\iint_{A} \frac{x^2}{y^2} \, \mathrm{d}x \, \mathrm{d}y$, $A$ 是由 $x = 2$, $y = x$ 和 $xy = 1$ 所围成的区域;
(5) $\iint_{A} xy^{2} \, \mathrm{d}x \, \mathrm{d}y$, $A$ 是由 $y^{2} = 2px$, $x = p/2 (p > 0)$ 所围成的区域.

2. 计算下列积分:

(1) $\iiint_{\Omega}(x + y + z)\mathrm{d}x\mathrm{d}y\mathrm{d}z,\Omega$ 为椭球 $\frac{x^2}{a^2} +\frac{y^2}{b^2} +\frac{z^2}{c^2}\leqslant 1;$

(2) $\iiint_{\Omega} x^3 yz \, \mathrm{d}x \, \mathrm{d}y \, \mathrm{d}z, \Omega$ 是由曲面 $x^2 + y^2 + z^2 = 1$，平面 $x = 0, y = 0$ 与 $z = 0$ 围成的位于第一卦限的有界区域；

(3) $\iiint_{\Omega} z \, \mathrm{d}x \, \mathrm{d}y \, \mathrm{d}z, \, \Omega$ 由曲面 $z = x^2 + y^2$，平面 $z = 1$ 与 $z = 2$ 围成；
(4) $\iiint_{\Omega}(1 + x^4)\mathrm{d}x\mathrm{d}y\mathrm{d}z,\Omega$ 由曲面 $x^{2} = z^{2} + y^{2}$ ，平面 $x = 2$ 与 $x = 4$ 围成；
(5) $\iiint_{\Omega}(x^2 + y^2) \, \mathrm{d}x \, \mathrm{d}y \, \mathrm{d}z, \Omega$ 由 $z = 16(x^2 + y^2)$, $z = 4(x^2 + y^2)$ 与 $z = 64$ 围成.

3. 求由平面 x=0, x=1, y=0, y=2, z=0 与曲面  $z=xy^{2}$  所围区域的体积.

4. 求由平面 $x = -1, x = 1, y = -1, y = 2, z = 0$ 与曲面 $z = x^2 + y^2$ 所围区域的体积.
5. 计算由曲面  $\left|x\right|+\left|y\right|+\left|z\right|=a\ (a>0)$  所围区域的体积.
6. 求由曲面 $z = xy$, 平面 $z = x + y, x + y = 1, x = 0, y = 0$ 所围区域的体积.
7. 设 $A = \{(x, y, z, w) \mid x, y, z, w \geqslant 0, x + y + z + w \leqslant a\}$, 计算积分

$$
\iiint_ {A} x y z w   \mathrm{d} x   \mathrm{d} y   \mathrm{d} z   \mathrm{d} w.
$$

8. 设 $f \in R[a, b]$，对二元函数 $g(x, y) = [f(x) - f(y)]^2$ 应用重积分化为累次积分进行计算的方法证明:

$$
\left(\int_ {a} ^ {b} f (x) \mathrm{d} x\right) ^ {2} \leqslant (b - a) \int_ {a} ^ {b} f ^ {2} (x) \mathrm{d} x.
$$

9. 设 $f$ 为 $[a, b] \times [a, b]$ 上的连续函数, 证明:

$$
\int_ {a} ^ {b} \mathrm{d} x \int_ {a} ^ {x} f (x, y) \mathrm{d} y = \int_ {a} ^ {b} \mathrm{d} y \int_ {y} ^ {b} f (x, y) \mathrm{d} x.
$$

10. 设  $f \in R[a, b]$ ，证明:

$$
\int_ {a} ^ {b} \mathrm{d} x \int_ {a} ^ {x} f (y) \mathrm{d} y = \int_ {a} ^ {b} f (y) (b - y) \mathrm{d} y.
$$

11. 设  $f \in R[a, b]$ ，证明:

$$
\int_ {a} ^ {b} f (x) \mathrm{d} x \int_ {a} ^ {x} f (y) \mathrm{d} y = \frac {1}{2} \left(\int_ {a} ^ {b} f (x) \mathrm{d} x\right) ^ {2}.
$$

12. 设  $f_{i} \in R[a_{i}, b_{i}]$ ,  $i = 1, 2, \cdots, n$ . 记

$$
F (\boldsymbol {x}) = \prod_ {i = 1} ^ {n} f _ {i} (x _ {i}), \boldsymbol {x} = (x _ {1}, x _ {2}, \dots , x _ {n}) \in I = [ a _ {1}, b _ {1} ] \times [ a _ {2}, b _ {2} ] \times \dots \times [ a _ {n}, b _ {n} ],
$$

证明:

$$
\int_ {I} F (\boldsymbol {x}) \mathrm{d} \boldsymbol {x} = \prod_ {i = 1} ^ {n} \int_ {a _ {i}} ^ {b _ {i}} f _ {i} (x _ {i}) \mathrm{d} x _ {i}.
$$

13. 设 $f \in R[a, b]$, 证明:

$$
\int_ {a} ^ {b} f (x _ {1}) \mathrm{d} x _ {1} \int_ {a} ^ {x _ {1}} f (x _ {2}) \mathrm{d} x _ {2} \dots \int_ {a} ^ {x _ {n - 1}} f (x _ {n}) \mathrm{d} x _ {n} = \frac {1}{n !} \left(\int_ {a} ^ {b} f (x) \mathrm{d} x\right) ^ {n}.
$$

14. 设 $D$ 是 $\mathbb{R}^{n-1}$ 中的紧致 Jordan 可测集, $\varphi, \psi$ 是定义在 $D$ 上的连续函数且 $\varphi \leqslant \psi$. 记

$$
A = \big \{(\boldsymbol {x}, y) \in \mathbb {R} ^ {n - 1} \times \mathbb {R} \mid \boldsymbol {x} \in D, \varphi (\boldsymbol {x}) \leqslant y \leqslant \psi (\boldsymbol {x}) \big \}.
$$

证明: (1) $A$ 为 $\mathbb{R}^n$ 中的紧致 Jordan 可测集, 且

$$
\nu (A) = \int_ {D} \left[ \psi (\boldsymbol {x}) - \varphi (\boldsymbol {x}) \right] \mathrm{d} \boldsymbol {x}.
$$

(2) 若 $f$ 是 $A$ 上的连续函数, 则

$$
\iint_ {A} f (\boldsymbol {x}, y) \mathrm{d} \boldsymbol {x} \mathrm{d} y = \int_ {D} \left(\int_ {\varphi (\boldsymbol {x})} ^ {\psi (\boldsymbol {x})} f (\boldsymbol {x}, y) \mathrm{d} y\right) \mathrm{d} \boldsymbol {x}.
$$

15. 计算下列 $n$ 重积分:

(1) $\int_0^1 x_1\mathrm{d}x_1\int_0^{x_1}x_2\mathrm{d}x_2\dots \int_0^{x_{n - 1}}x_n\mathrm{d}x_n;$
(2)  $\iint\cdots\int_{[0,1]^{n}}\max\{x_{1},x_{2},\cdots,x_{n}\}\mathrm{d}x_{1}\mathrm{d}x_{2}\cdots\mathrm{d}x_{n}.$

16. 在 $[0,1] \times [0,1]$ 上定义函数 $f$ 如下:

$$
f (x, y) = \left\{ \begin{array}{l l} 1, & x \text {为无理数}, \\ 3 y ^ {2}, & x \text {为有理数}. \end{array} \right.
$$

证明: $f$ 不可积，但累次积分 $\int_0^1\mathrm{d}x\int_0^1 f(x,y)\mathrm{d}y$ 存在.

17. 在 $[0,1] \times [0,1]$ 上定义函数 $f$ 如下:

$$
f (x, y) = \left\{ \begin{array}{l l} 0, & x, y \text {都是或都不是无理数}, \\ \frac {1}{p}, & x = \frac {r}{p} \text {为既约分数}, y \text {为无理数}, \\ \frac {1}{q}, & x \text {为无理数}, y = \frac {s}{q} \text {为既约分数}. \end{array} \right.
$$

证明: $f$ 可积，但它的累次积分不存在.

18. 设 $f$ 为 $[a, b]$ 上的非负函数, 记

$$
A _ {f} = \big \{(x, y) \in \mathbb {R} ^ {2} \mid a \leqslant x \leqslant b, 0 \leqslant y \leqslant f (x) \big \}.
$$

证明: $A_{f}$ 为 Jordan 可测集当且仅当 $f$ 可积, 此时 $A_{f}$ 的容积 (面积) 等于 $f$ 在 $[a, b]$ 上的积分.

## 16.4 重积分的变量替换

与一元函数的积分类似, 多元函数的积分也有相应的变量替换公式. 我们先考虑仿射变换, 再利用微分学的基本手法将一般的变换线性化并估计误差.

## 16.4.1 仿射变换

设 $\varphi : \mathbb{R}^n \to \mathbb{R}^n$ 为线性变换, 记 $\varphi(\boldsymbol{x}) = \boldsymbol{Q}\boldsymbol{x}$. 设 $I$ 为 $\mathbb{R}^n$ 中的 $n$ 维矩形, 我们先来研究 $\varphi(I)$ 的 Jordan 测度. 若 $\boldsymbol{Q}$ 退化, 则 $\varphi(\mathbb{R}^n)$ 是 $\mathbb{R}^n$ 中的零测集, 此时 $\varphi(I)$ 的 Jordan 测度为零. 下设 $\boldsymbol{Q}$ 非退化, 由 $\partial[\varphi(I)] = \varphi(\partial I)$ 为零测集可知 $\varphi(I)$ 为 Jordan 可测集.

根据线性代数, 非退化线性变换  $\varphi(\boldsymbol{x}) = \boldsymbol{Q}\boldsymbol{x}$  可以分解为有限个如下初等线性变换的复合:

(1) $(x_{1},\cdots,x_{i},\cdots,x_{j},\cdots,x_{n})\mapsto(x_{1},\cdots,x_{j},\cdots,x_{i},\cdots,x_{n})$ ，其中i<j.
(2) $(x_{1},\cdots,x_{i},\cdots,x_{n})\mapsto(x_{1},\cdots,\lambda x_{i},\cdots,x_{n})$ ，其中 $1\leqslant i\leqslant n,\lambda\neq0$ .
(3) $(x_{1},\cdots,x_{i},\cdots,x_{j},\cdots,x_{n})\mapsto(x_{1},\cdots,x_{i},\cdots,x_{j}+x_{i},\cdots,x_{n})$ ，其中i<j.

我们来验证在这三种初等变换下, 均有 $\nu(\varphi(I)) = |\det Q| \nu(I)$. 情形 (1) 和 (2) 比较显然, 我们来看情形 (3), 以 $n = 2$ 为例. 记 $I = [a, b] \times [c, d]$, $(u, v) = \varphi(x, y) = (x, y + x)$, 则 $\varphi(I)$ 可以表示为

$$
\varphi (I) = \{(u, v) \in \mathbb {R} ^ {2} \mid a \leqslant u \leqslant b, c + u \leqslant v \leqslant d + u \},
$$

这是一个平行四边形, 其 Jordan 测度可以用重积分化为累次积分计算:

$$
\nu (\varphi (I)) = \int_ {a} ^ {b} \mathrm{d} u \int_ {c + u} ^ {d + u} \mathrm{d} v = \int_ {a} ^ {b} \mathrm{d} u \int_ {c} ^ {d} \mathrm{d} v = \nu (I).
$$

一般地, 设 $f$ 是 $\mathbb{R}^n$ 中某个 Jordan 可测集上的可积函数. 为了方便起见, 在此 Jordan 可测集外规定 $f$ 为零, 并可以将 $f$ 的积分写成它在整个 $\mathbb{R}^n$ 上的积分. 我们有

引理 16.4.1 设 f 是  $R^{n}$  中某个 Jordan 可测集上的可积函数, Q 是非退化 n 阶方阵, 则

$$
\int_ {\mathbb {R} ^ {n}} f (\boldsymbol {Q} \boldsymbol {x}) \mathrm{d} \boldsymbol {x} = | \det \boldsymbol {Q} | ^ {- 1} \int_ {\mathbb {R} ^ {n}} f (\boldsymbol {x}) \mathrm{d} \boldsymbol {x}. \tag {16.4.1}
$$

证明 如果 $Q = A, B$ 时, 公式 (16.4.1) 对可积函数均成立, 则由 $\det(BA) = (\det B)(\det A)$ 可知公式 (16.4.1) 对 $Q = BA$ 也成立. 因此, 只要对初等变换验证引理成立即可.

取矩形 $I$, 使得 $f$ 在 $I$ 之外为零. 设 $\mathrm{P} = \{I_k\}$ 为 $I$ 的分割, $f$ 在 $I_k$ 中的下确界和上确界分别记为 $m_k$ 和 $M_k$, 则

$$
m _ {k} \nu (Q ^ {- 1} I _ {k}) \leqslant \int_ {Q ^ {- 1} I _ {k}} f (Q x) \mathrm{d} x \leqslant M _ {k} \nu (Q ^ {- 1} I _ {k}).
$$

上式关于 $k$ 求和, 利用之前的讨论可得

$$
| \det Q | ^ {- 1} \sum_ {k} m _ {k} \nu (I _ {k}) \leqslant \int_ {\mathbb {R} ^ {n}} f (Q x) \mathrm{d} x \leqslant | \det Q | ^ {- 1} \sum_ {k} M _ {k} \nu (I _ {k}),
$$

令 P 的模趋于零即得欲证结论.

推论16.4.2 设 $\varphi(x) = Qx + b$ 为仿射变换, $S$ 为 $\mathbb{R}^n$ 中的Jordan可测集, 则 $\nu(\varphi(S)) = |\det Q| \nu(S)$.

证明 不妨设 $b = 0$ 且 $\operatorname{det} Q \neq 0$, 此时 $\varphi(S)$ 为 Jordan 可测集. 在前一引理中, 将 $f$ 取为 $\varphi(S)$ 的特征函数即得欲证结论. □

例 16.4.1 设  $\{v_{i}\}_{i=1}^{n}$  为  $R^{n}$  中的向量, 求如下平行多面体的容积:

$$
P (\boldsymbol {v} _ {1}, \boldsymbol {v} _ {2}, \dots , \boldsymbol {v} _ {n}) = \left\{\sum_ {i = 1} ^ {n} x _ {i} \boldsymbol {v} _ {i} \in \mathbb {R} ^ {n}   \big |   0 \leqslant x _ {i} \leqslant 1, i = 1, 2, \dots , n \right\}.
$$

解 记  $R^{n}$  的标准正交基为  $\{e_{i}\}_{i=1}^{n}$ ，考虑线性变换  $\varphi: R^{n} \rightarrow R^{n}, \varphi(e_{i}) = v_{i}$ . 显然有

$$
\begin{array}{l} P (\boldsymbol {v} _ {1}, \boldsymbol {v} _ {2}, \dots , \boldsymbol {v} _ {n}) = \left\{\sum_ {i = 1} ^ {n} x _ {i} \boldsymbol {v} _ {i} \in \mathbb {R} ^ {n} \mid 0 \leqslant x _ {i} \leqslant 1, i = 1, 2, \dots , n. \right\} \\ = \left\{\varphi \left(\sum_ {i = 1} ^ {n} x _ {i} \boldsymbol {e} _ {i}\right) \in \mathbb {R} ^ {n} \mid 0 \leqslant x _ {i} \leqslant 1, i = 1, 2, \dots , n. \right\} \\ = \varphi (P (\boldsymbol {e} _ {1}, \boldsymbol {e} _ {2}, \dots , \boldsymbol {e} _ {n})). \\ \end{array}
$$

显然， $P(\boldsymbol{e}_{1},\boldsymbol{e}_{2},\cdots,\boldsymbol{e}_{n})=[0,1]^{n}$ ，因此，由上述推论可得

$$
\nu (P (\boldsymbol {v} _ {1}, \boldsymbol {v} _ {2}, \dots , \boldsymbol {v} _ {n})) = | \det \boldsymbol {Q} | \nu ([ 0, 1 ] ^ {n}) = | \det \boldsymbol {Q} |\,
$$

其中 Q 是以  $v_{1}, v_{2}, \cdots, v_{n}$  为列向量的方阵. 例如, 当  $n = 2, \boldsymbol{v}_{1} = (a_{1}, b_{1}), \boldsymbol{v}_{2} = (a_{2}, b_{2})$  时,

$$
\nu (P (\boldsymbol {v} _ {1}, \boldsymbol {v} _ {2})) = | a _ {1} b _ {2} - a _ {2} b _ {1} |,
$$

这是平行四边形的面积公式.

例 16.4.2 设  $\{v_{i}\}_{i=1}^{n}$  为  $R^{n}$  中的向量, 求如下单形的容积:

$$
\Delta (\pmb {v} _ {1}, \pmb {v} _ {2}, \dots , \pmb {v} _ {n}) = \left\{\sum_ {i = 1} ^ {n} x _ {i} \pmb {v} _ {i} \in \mathbb {R} ^ {n} \mid x _ {i} \geqslant 0 (1 \leqslant i \leqslant n), x _ {1} + x _ {2} + \dots + x _ {n} \leqslant 1 \right\}.
$$

解 考虑线性变换 $\varphi : \mathbb{R}^n \to \mathbb{R}^n, \varphi(e_i) = v_i$，则

$$
\Delta (\boldsymbol {v} _ {1}, \boldsymbol {v} _ {2}, \dots , \boldsymbol {v} _ {n}) = \varphi (\Delta_ {n} (1)),
$$

由例16.3.7的结果可得

$$
\nu \left(\Delta (\boldsymbol {v} _ {1}, \boldsymbol {v} _ {2}, \dots , \boldsymbol {v} _ {n})\right) = | \det \boldsymbol {P} | \nu \left(\Delta_ {n} (1)\right) = \frac {1}{n !} | \det \boldsymbol {P} |,
$$

其中 P 是以  $v_{1}, v_{2}, \cdots, v_{n}$  为列向量的方阵.

例 16.4.3 求中心为  $x^{0} \in R^{n}$ ，半径为 r 的 n 维球体  $\overline{B_{r}(x^{0})}$  的容积，其中

$$
\overline {{B _ {r} (\boldsymbol {x} ^ {0})}} = \{\boldsymbol {x} \in \mathbb {R} ^ {n} \mid (\boldsymbol {x} - \boldsymbol {x} ^ {0}) \cdot (\boldsymbol {x} - \boldsymbol {x} ^ {0}) \leqslant r ^ {2} \}.
$$

解 根据容积的平移不变性, 不妨设  $x_{0}$  为原点. 半径为 r 的 n 维球体的容积记为  $\omega_{n}(r)$ . 利用伸缩变换可知  $\omega_{n}(r)=\omega_{n}(1)r^{n}$ , 为了方便起见, 记  $\omega_{n}=\omega_{n}(1)$ . 利用投影法可得

$$
\begin{array}{l} \omega_ {n + 1} = \int_ {- 1} ^ {1} \omega_ {n} \left(\sqrt {1 - x _ {1} ^ {2}}\right) \mathrm{d} x _ {1} = \omega_ {n} \int_ {- 1} ^ {1} (1 - x _ {1} ^ {2}) ^ {\frac {n}{2}} \mathrm{d} x _ {1} \\ = 2 \omega_ {n} \int_ {0} ^ {\frac {\pi}{2}} \sin^ {n + 1} t \mathrm{d} t = 2 \omega_ {n} J _ {n + 1}. \\ \end{array}
$$

其中， $J_{n + 1}$ 在例9.4.6中已经计算过:

$$
J _ {2 k} = \frac {(2 k - 1) ! !}{(2 k) ! !} \frac {\pi}{2}, J _ {2 k + 1} = \frac {(2 k) ! !}{(2 k + 1) ! !}, \forall k \geqslant 0.
$$

根据  $\omega_{1}=2$  以及上述递推公式可得

$$
\omega_ {1} = 2, \omega_ {2} = \pi , \omega_ {n + 2} = \omega_ {n} \frac {2 \pi}{n + 2}, \forall n \geqslant 1.
$$

由此进一步得到

$$
\omega_ {2 k} = \frac {(2 \pi) ^ {k}}{(2 k) ! !} = \frac {\pi^ {k}}{k !}, \omega_ {2 k - 1} = \frac {2 ^ {k} \pi^ {k - 1}}{(2 k - 1) ! !}, \forall k \geqslant 1. \tag {16.4.2}
$$

## 16.4.2 一般的变量替换

设 $D$ 为 $\mathbb{R}^n$ 中的开集, $\varphi : D \to \mathbb{R}^n$ 为 $C^1$ 映射. 根据拟微分中值定理, 从局部上看 $\varphi$ 为 Lipschitz 映射, 因此将零测集映为零测集. 假设 $J\varphi$ 处处非退化, $S$ 为 Jordan 可测集且 $\bar{S} \subseteq D$, 则由逆映射定理可知 $\varphi$ 将 $S$ 的内点映为 $\varphi(S)$ 的内点. 由最值定理可知 $\varphi(\bar{S})$ 为有界闭集. 注意

$$
\partial [ \varphi (S) ] = \overline {{\varphi (S)}} \setminus \mathrm{int} [ \varphi (S) ] \subseteq \varphi (\bar {S}) \setminus \varphi (\mathrm{int} S) \subseteq \varphi (\partial S),
$$

这说明 $\varphi(S)$ 仍为 Jordan 可测集. 为了研究 $\varphi(S)$ 的 Jordan 测度, 我们将 $\varphi$ 线性化并做误差估计.

当  $\boldsymbol{x}=(x_{1},x_{2},\cdots,x_{n})\in\mathbb{R}^{n}$  时，记  $|x|_{\infty}=\max\{|x_{1}|,|x_{2}|,\cdots,|x_{n}|\}$ . 若  $u\in R^{n}, r>0$ ，则以 u 为中心，2r 为边长的方体可以表示为  $I_{r}(\boldsymbol{u})=\{\boldsymbol{x}\in\mathbb{R}^{n}\mid|\boldsymbol{x}-\boldsymbol{u}|_{\infty}<r\}$ .

引理 16.4.3 设  $D \subseteq R^{n}$  为开集,  $\varphi: D \to R^{m}$  为  $C^{1}$  映射. 如果  $C \subseteq D$  为紧凸集, 则任给  $\varepsilon > 0$ , 存在  $\delta > 0$ , 使得只要  $v, u \in C$  且  $\|v - u\| < \delta$ , 就有

$$
\| \varphi (\boldsymbol {v}) - \varphi (\boldsymbol {u}) - J \varphi (\boldsymbol {u}) (\boldsymbol {v} - \boldsymbol {u}) \| \leqslant \varepsilon \| \boldsymbol {v} - \boldsymbol {u} \|\cdot
$$

证明 由题设可知 $J\varphi$ 在 $C$ 上一致连续. 因此任给 $\varepsilon > 0$, 存在 $\delta > 0$, 使得只要 $\pmb{u}', \pmb{u} \in C$ 且 $\| \pmb{u}' - \pmb{u} \| < \delta$, 就有 $\| J\varphi(\pmb{u}') - J\varphi(\pmb{u}) \| < \varepsilon$.

暂时固定 $\pmb{u} \in C$。当 $\pmb{x} \in D$ 时，记 $\psi(\pmb{x}) = \varphi(\pmb{x}) - \varphi(\pmb{u}) - J\varphi(\pmb{u})(\pmb{x} - \pmb{u})$，则 $J\psi(\pmb{x}) = J\varphi(\pmb{x}) - J\varphi(\pmb{u})$。当 $\pmb{v} \in C$ 时，由拟微分中值定理可知

$$
\| \psi (\boldsymbol {v}) \| = \| \psi (\boldsymbol {v}) - \psi (\boldsymbol {u}) \| \leqslant \| J \psi (\boldsymbol {\xi}) \| \| \boldsymbol {v} - \boldsymbol {u} \| = \| J \varphi (\boldsymbol {\xi}) - J \varphi (\boldsymbol {u}) \| \| \boldsymbol {v} - \boldsymbol {u} \|,
$$

其中 $\pmb{\xi} = \theta \pmb{v} + (1 - \theta)\pmb{u}\in C,\theta \in (0,1)$ .若 $\| \pmb {v} - \pmb {u}\| <  \delta$ ，则 $\| \pmb {\xi} - \pmb {u}\| = \theta \| \pmb {v} - \pmb {u}\| <  \delta ,$ 因此

$$
\| \varphi (\boldsymbol {v}) - \varphi (\boldsymbol {u}) - J \varphi (\boldsymbol {u}) (\boldsymbol {v} - \boldsymbol {u}) \| = \| \psi (\boldsymbol {v}) \| \leqslant \varepsilon \| \boldsymbol {v} - \boldsymbol {u} \|\cdot
$$

引理 16.4.4 沿用以上记号, 若 C 为 D 中的紧凸集, 则任给  $\varepsilon > 0$ , 存在  $\eta > 0$ , 使得只要  $0 < r < \eta$ ,  $I_{r}(\boldsymbol{u}) \subseteq C$ , 就有

$$
\nu (\varphi (I _ {r} (\boldsymbol {u}))) \leqslant \big [ | \det J \varphi (\boldsymbol {u}) | + O (\varepsilon) \big ] \nu (I _ {r} (\boldsymbol {u})).
$$

证明 给定 $\varepsilon$ 后, 设 $\delta$ 如引理 16.4.3. 取 $\eta = \frac{\delta}{\sqrt{n}}$, 则当 $0 < r < \eta$, $I_r(\boldsymbol{u}) \subseteq C$ 且 $\boldsymbol{v} \in I_r(\boldsymbol{u})$ 时, $\| \boldsymbol{v} - \boldsymbol{u} \| < \sqrt{n} r < \delta$. 因此由引理 16.4.3 可得

$$
\| \varphi (\boldsymbol {v}) - \varphi (\boldsymbol {u}) - J \varphi (\boldsymbol {u}) (\boldsymbol {v} - \boldsymbol {u}) \| <   \varepsilon \| \boldsymbol {v} - \boldsymbol {u} \|\cdot
$$

考虑仿射变换 $L(\pmb {x}) = \left[J\varphi (\pmb {u})\right]^{-1}(\pmb {x} - \varphi (\pmb {u})) + \pmb {u}$ ，则

$$
L \circ \varphi (\boldsymbol {v}) = \boldsymbol {v} + \left[ J \varphi (\boldsymbol {u}) \right] ^ {- 1} \psi (\boldsymbol {v}),
$$

其中 $\psi (\pmb {v}) = \varphi (\pmb {v}) - \varphi (\pmb {u}) - J\varphi (\pmb {u})(\pmb {v} - \pmb {u})$ 当 $v\in I_r(u)$ 时，有

$$
\left| L \circ \varphi (\boldsymbol {v}) - \boldsymbol {u} \right| _ {\infty} \leqslant | \boldsymbol {v} - \boldsymbol {u} | _ {\infty} + \left\| \left[ J \varphi (\boldsymbol {u}) \right] ^ {- 1} \psi (\boldsymbol {v}) \right\| <   r + M \varepsilon \sqrt {n} r,
$$

其中 $M = \max_{C} \| [J\varphi]^{-1}\|$. 这说明

$$
\nu \left(L \circ \varphi (I _ {r} (\boldsymbol {u}))\right) \leqslant (1 + M \varepsilon \sqrt {n}) ^ {n} \nu (I _ {r} (\boldsymbol {u})),
$$

再由推论 16.4.2 即得欲证结论.

□

定理 16.4.5（重积分的变量替换） 设 D 为  $R^{n}$  中的开集,  $\varphi: D \rightarrow R^{n}$  为  $C^{1}$  单射, 且  $J\varphi$  处处非退化. 设 S 为 Jordan 可测集,  $\bar{S} \subseteq D$ , f 在  $\varphi(S)$  上可积, 则

$$
\int_ {\varphi (S)} f (\boldsymbol {y}) \mathrm{d} \boldsymbol {y} = \int_ {S} f \circ \varphi (\boldsymbol {x}) | \det J \varphi (\boldsymbol {x}) | \mathrm{d} \boldsymbol {x}. \tag {16.4.3}
$$

特别地，

$$
\nu (\varphi (S)) = \int_ {S} | \det J \varphi (\boldsymbol {x}) |   \mathrm{d} \boldsymbol {x}.
$$

证明 不妨设 $f \geqslant 0$, 且在 $\varphi(S)$ 外规定 $f$ 为零. 取 $\delta > 0$, 使得 $\{\pmb{x} \mid d(\pmb{x}, S) \leqslant \delta\} \subseteq D$. 用一个大的方体包含住 $S$, 将大方体等分为小方体, 使得每一个小方体的直径小于 $\delta$. 此时, 与 $S$ 有非空交的小方体都包含在 $D$ 中, 我们只要在每一个小方体中验证 (16.4.3) 式成立就可以了. 因此, 不妨一开始就设 $S$ 为方体. 任给 $S$ 的等分分割 $\{I_k\}$, 我们有

$$
\int_ {\varphi (S)} f (\boldsymbol {y}) \mathrm{d} \boldsymbol {y} = \sum_ {k} \int_ {\varphi (I _ {k})} f (\boldsymbol {y}) \mathrm{d} \boldsymbol {y} \leqslant \sum_ {k} \left[ \sup _ {\varphi (I _ {k})} f \right] \nu (\varphi (I _ {k})).
$$

任给 $\varepsilon > 0$，当分割的模充分小时，由引理16.4.4可得

$$
\int_ {\varphi (S)} f (\boldsymbol {y}) \mathrm{d} \boldsymbol {y} \leqslant \sum_ {k} \left[ \sup _ {I _ {k}} f \circ \varphi \right] | \det J \varphi (\boldsymbol {\xi} _ {k}) | \nu (I _ {k}) + O (\varepsilon).
$$

容易看出 $f\circ \varphi |\det J\varphi (\pmb {x})|$ 在 $S$ 上可积，由上式可得

$$
\int_ {\varphi (S)} f (\boldsymbol {y}) \mathrm{d} \boldsymbol {y} \leqslant \int_ {S} f \circ \varphi (\boldsymbol {x}) | \det J \varphi (\boldsymbol {x}) | \mathrm{d} \boldsymbol {x} + O (\varepsilon),
$$

这里我们把求和与积分之间的误差也归并到 $O(\varepsilon)$ 项中了.令 $\varepsilon \to 0^{+}$ 可得

$$
\int_ {\varphi (S)} f (\boldsymbol {y}) \mathrm{d} \boldsymbol {y} \leqslant \int_ {S} f \circ \varphi (\boldsymbol {x}) | \det J \varphi (\boldsymbol {x}) | \mathrm{d} \boldsymbol {x}.
$$

根据逆映射定理, $\varphi:D\to\varphi(D)$  可逆. 对  $\varphi^{-1}$  重复上述论证就可得到反过来的不等式,于是欲证结论成立. □

例 16.4.4 设 A 是由 x = 0, y = 0 以及  $x + y = 1$  围成的区域 (图 16.9(a)), 计算积分

$$
I = \iint_ {A} \mathrm{e} ^ {\frac {x - y}{x + y}} \mathrm{d} x \mathrm{d} y.
$$

解 被积区域是一个三角形, 被积函数在 $A \setminus \{(0,0)\}$ 上连续, 在 $A$ 上有界. 我们用线性变换简化被积函数, 令 $x - y = u$, $x + y = v$, 解出

$$
x = \frac {1}{2} (u + v), y = \frac {1}{2} (v - u),
$$

$(x,y)$  关于  $(u,v)$  的 Jacobi 行列式为

$$
\frac {\partial (x , y)}{\partial (u , v)} = \left| \begin{array}{c c} 1 / 2 & 1 / 2 \\ - 1 / 2 & 1 / 2 \end{array} \right| = 1 / 2.
$$

在上述线性变换下, 被积区域变为如下三角形区域 (图 16.9(b))

$$
D = \{(u, v) \in \mathbb {R} ^ {2} \mid u + v \geqslant 0, v - u \geqslant 0, v \leqslant 1 \}.
$$

因此

$$
\begin{array}{l} I = \iint_ {D} \mathrm{e} ^ {\frac {u}{v}} \left| \frac {1}{2} \right| \mathrm{d} u \mathrm{d} v = \frac {1}{2} \int_ {0} ^ {1} \mathrm{d} v \int_ {- v} ^ {v} \mathrm{e} ^ {\frac {u}{v}} \mathrm{d} u \\ = \frac {1}{2} \int_ {0} ^ {1} v \big (\mathrm{e} - \mathrm{e} ^ {- 1} \big) \mathrm{d} v = \frac {1}{4} \big (\mathrm{e} - \mathrm{e} ^ {- 1} \big). \\ \end{array}
$$

![](images/page_667_image_8.jpg)

<details>
<summary>text_image</summary>

y
1
x+y=1
A
O
1
x
</details>

(a)

![](images/page_667_image_10.jpg)

<details>
<summary>text_image</summary>

v
1
v+u=0
v=1
D
O
u
v-u=0
</details>

(b)

图16.9 线性变换

例16.4.5 设 $0 < p < q, 0 < a < b$. 抛物线 $y^{2} = px, y^{2} = qx$ 以及双曲线 $xy = a, xy = b$ 围成的区域记为 $A$. 计算积分

$$
I = \iint_ {A} x y \mathrm{d} x \mathrm{d} y.
$$

解 被积区域是一个曲边的四边形 (图 16.10), 为了简化, 我们令 $y^{2} / x = u$, $xy = v$, 则 $(u, v)$ 关于 $(x, y)$ 的 Jacobi 行列式为

$$
\frac {\partial (u , v)}{\partial (x , y)} = \left| \begin{array}{c c} - y ^ {2} / x ^ {2} & 2 y / x \\ y & x \end{array} \right| = - 3 y ^ {2} / x = - 3 u,
$$

因此 $(x,y)$ 关于 $(u,v)$ 的Jacobi行列式为 $-(3u)^{-1}$. 在上述变换下, 被积区域变为矩形 $[p,q] \times [a,b]$, 因此

$$
I = \int_ {p} ^ {q} \mathrm{d} u \int_ {a} ^ {b} v \big | - (3 u) ^ {- 1} \big | \mathrm{d} v = \frac {1}{6} (b ^ {2} - a ^ {2}) \ln \frac {q}{p}.
$$

□

![](images/page_668_image_2.jpg)

<details>
<summary>text_image</summary>

xy=b
y²=qx
xy=a
A
y²=px
O
x
</details>

图 16.10 曲边四边形

## 16.4.3 极坐标变换

我们知道, 在平面 $\mathbb{R}^2$ 上有直角坐标 $(x,y)$ 和极坐标 $(r,\theta)$, 其变换关系为

$$
x = r \cos \theta , y = r \sin \theta , r \geqslant 0, 0 \leqslant \theta \leqslant 2 \pi .
$$

这个变换称为极坐标变换, 其 Jacobi 行列式为

$$
\frac {\partial (x , y)}{\partial (r , \theta)} = \left| \begin{array}{c c} \cos \theta & - r \sin \theta \\ \sin \theta & r \cos \theta \end{array} \right| = r.
$$

这个变换将 $(r, \theta)$ 平面上的矩形 $[0, R] \times [0, 2\pi]$ 变为 $(x, y)$ 平面上的圆 $x^{2} + y^{2} \leqslant R^{2}$. 不过, 这个变换不是一一的, 且在 $r = 0$ 处退化. 尽管如此, 由于此变换在 $(0, +\infty) \times (0, 2\pi)$ 上是一一的且非退化, 因此将定理16.4.5的证明略作改动即知, 积分的变量替换公式对这个变换仍然成立.

例 16.4.6 设 a > 0, 球体  $x^{2} + y^{2} + z^{2} \leqslant a^{2}$  被柱面  $x^{2} + y^{2} = ax$  所截 (图 16.11), 求截出部分的体积.

![](images/page_668_image_11.jpg)

<details>
<summary>text_image</summary>

(0,0,a)
O
(a,0,0)
</details>

图 16.11 球体与柱面

解 根据截出图形的对称性, 只要考虑第一象限部分的体积即可, 这一部分的体积是函数 $z = \sqrt{a^2 - x^2 - y^2}$ 在半圆 $D = \{(x, y) \in \mathbb{R}^2 \mid y \geqslant 0, x^2 + y^2 \leqslant ax\}$ 上的积分,因此体积 V 可以用极坐标变换  $x = r \cos \theta, y = r \sin \theta$  计算如下

$$
\begin{array}{l} V = 4 \iint_ {D} \sqrt {a ^ {2} - x ^ {2} - y ^ {2}} \mathrm{d} x \mathrm{d} y \\ = 4 \int_ {0} ^ {\frac {\pi}{2}} \mathrm{d} \theta \int_ {0} ^ {a \cos \theta} \sqrt {a ^ {2} - r ^ {2}} r \mathrm{d} r \\ = \frac {4}{3} a ^ {3} \int_ {0} ^ {\frac {\pi}{2}} (1 - \sin^ {3} \theta) \mathrm{d} \theta = \frac {4}{3} \left(\frac {\pi}{2} - \frac {2}{3}\right) a ^ {3}. \\ \end{array}
$$

例16.4.7 在圆 $D = \{(x,y)\in \mathbb{R}^2 |x^2 +y^2\leqslant R^2\}$ 中计算积分

$$
I = \iint_ {D} \mathrm{e} ^ {- (x ^ {2} + y ^ {2})} \mathrm{d} x \mathrm{d} y.
$$

解 这个积分用直角坐标是不好计算的. 我们用极坐标变换, 此时有

$$
I = \int_ {0} ^ {R} \mathrm{d} r \int_ {0} ^ {2 \pi} \mathrm{e} ^ {- r ^ {2}} r \mathrm{d} \theta = 2 \pi \int_ {0} ^ {R} \mathrm{e} ^ {- r ^ {2}} r \mathrm{d} r = \pi (1 - \mathrm{e} ^ {- R ^ {2}}).
$$

有时, 伸缩变换和极坐标变换可以结合起来使用.

例 16.4.8 求椭圆  $\frac{x^{2}}{a^{2}} + \frac{y^{2}}{b^{2}} = 1 (a, b > 0)$  所包围的面积.

解 作所谓的广义极坐标变换

$$
x = a r \cos \theta , y = b r \sin \theta , r \in [ 0, 1 ], \theta \in [ 0, 2 \pi ],
$$

其 Jacobi 行列式为

$$
\frac {\partial (x , y)}{\partial (r , \theta)} = \left| \begin{array}{c c} a \cos \theta & - a r \sin \theta \\ b \sin \theta & b r \cos \theta \end{array} \right| = a b r,
$$

因此所求面积为

$$
\int_ {0} ^ {1} \mathrm{d} r \int_ {0} ^ {2 \pi} a b r \mathrm{d} \theta = \pi a b.
$$

下面我们考虑  $R^{3}$  中的一些特殊的坐标变换. 首先有如下的柱面坐标变换:

$$
x = r \cos \theta , y = r \sin \theta , z = z,
$$

其 Jacobi 行列式也是 r.

例 16.4.9 设 D 是球面  $x^{2} + y^{2} + z^{2} = 4$  与抛物面  $x^{2} + y^{2} = 3z$  所围成的区域 (图 16.12)，计算积分  $I = \iiint_{D} z \, dx \, dy \, dz$ .

![](images/page_669_image_20.jpg)

<details>
<summary>text_image</summary>

1
√3
O
</details>

图 16.12 球面与抛物面所围区域

解 用柱面坐标变换, 区域 D 变为

$$
A = \{(r, \theta , z) | r ^ {2} + z ^ {2} \leqslant 4, r ^ {2} \leqslant 3 z \},
$$

$A$ 在 $(r,\theta)$ 平面上的投影为区域 $\{0\leqslant r\leqslant \sqrt{3},0\leqslant \theta \leqslant 2\pi \}$. 固定 $(r,\theta),z$ 的变化范围为区间 $[r^2 /3,\sqrt{4 - r^2} ]$ ，因此所求积分为

$$
I = \iiint_ {A} r z \mathrm{d} r \mathrm{d} \theta \mathrm{d} z = \int_ {0} ^ {2 \pi} \mathrm{d} \theta \int_ {0} ^ {\sqrt {3}} r \mathrm{d} r \int_ {\frac {1}{3} r ^ {2}} ^ {\sqrt {4 - r ^ {2}}} z \mathrm{d} z = \frac {1 3}{4} \pi .
$$

与极坐标变换类似, $\mathbb{R}^3$ 中有所谓的球面坐标变换:

$$
x = r \sin \theta \cos \varphi , y = r \sin \theta \sin \varphi , z = r \cos \theta , r \geqslant 0, \theta \in [ 0, \pi ], \varphi \in [ 0, 2 \pi ].
$$

这个变换的 Jacobi 行列式为

$$
\frac {\partial (x , y , z)}{\partial (r , \theta , \varphi)} = \left| \begin{array}{c c c} \sin \theta \cos \varphi & r \cos \theta \cos \varphi & - r \sin \theta \sin \varphi \\ \sin \theta \sin \varphi & r \cos \theta \sin \varphi & r \sin \theta \cos \varphi \\ \cos \theta & - r \sin \theta & 0 \end{array} \right| = r ^ {2} \sin \theta .
$$

球面坐标变换和伸缩变换结合起来称为广义球面坐标变换.

例 16.4.10 设 D 是球面  $x^{2} + y^{2} + z^{2} = R^{2}$  和锥面  $\sqrt{x^{2} + y^{2}} = z$  围成的区域 (图 16.13), 计算积分

$$
I = \iiint_ {D} (x ^ {2} + y ^ {2} + z ^ {2})   \mathrm{d} x   \mathrm{d} y   \mathrm{d} z.
$$

![](images/page_670_image_13.jpg)

<details>
<summary>text_image</summary>

Geometric diagram of a hemisphere with a cone and labeled point O, showing shaded regions and dashed lines for mathematical analysis.
</details>

图16.13 球面与锥面所围区域

解 用球面坐标变换, 区域 D 变为

$$
A = \{(r, \theta , \varphi) \mid 0 \leqslant r \leqslant R, 0 \leqslant \varphi \leqslant 2 \pi , 0 \leqslant \theta \leqslant \pi / 4 \},
$$

因此

$$
I = \iiint_ {A} r ^ {2} | r ^ {2} \sin \theta | \mathrm{d} r \mathrm{d} \theta \mathrm{d} \varphi = \int_ {0} ^ {R} r ^ {4} \mathrm{d} r \int_ {0} ^ {\frac {\pi}{4}} \sin \theta \mathrm{d} \theta \int_ {0} ^ {2 \pi} \mathrm{d} \varphi = \frac {\pi}{5} (2 - \sqrt {2}) R ^ {5}. \quad \square
$$

例 16.4.11 计算椭球  $\frac{x^{2}}{a^{2}}+\frac{y^{2}}{b^{2}}+\frac{z^{2}}{c^{2}}\leqslant1(a,b,c>0)$  的体积.

解 用广义球面坐标变换:

$$
x = a r \sin \theta \cos \varphi , y = b r \sin \theta \sin \varphi , z = c r \cos \theta,
$$

此变换的 Jacobi 行列式为  $abcr^{2}\sin\theta$ ，积分区域变为

$$
\{(r, \theta , \varphi) \mid r \in [ 0, 1 ], \theta \in [ 0, \pi ], \varphi \in [ 0, 2 \pi ] \},
$$

因此椭球体积为

$$
V = \int_ {0} ^ {1} \mathrm{d} r \int_ {0} ^ {\pi} a b c r ^ {2} \sin \theta \mathrm{d} \theta \int_ {0} ^ {2 \pi} \mathrm{d} \varphi = \frac {4}{3} \pi a b c.
$$

一般地, 在 $\mathbb{R}^n (n\geqslant 3)$ 中也有球面坐标变换

$$
\left\{ \begin{array}{l} x _ {1} = r \cos \theta_ {1}, \\ x _ {2} = r \sin \theta_ {1} \cos \theta_ {2}, \\ x _ {3} = r \sin \theta_ {1} \sin \theta_ {2} \cos \theta_ {3}, \\ \vdots \\ x _ {n - 1} = r \sin \theta_ {1} \sin \theta_ {2} \dots \sin \theta_ {n - 2} \cos \theta_ {n - 1}, \\ x _ {n} = r \sin \theta_ {1} \sin \theta_ {2} \dots \sin \theta_ {n - 2} \sin \theta_ {n - 1}, \end{array} \right.
$$

此变换将矩形

$$
0 \leqslant r \leqslant R, 0 \leqslant \theta_ {1}, \theta_ {2}, \dots , \theta_ {n - 2} \leqslant \pi , 0 \leqslant \theta_ {n - 1} \leqslant 2 \pi,
$$

变为半径为 $R$ 的 $n$ 维 (闭) 球. 此变换的 Jacobi 矩阵有一个特点: 其列向量两两之间互相正交. 利用这一特点不难算出此变换的 Jacobi 行列式为

$$
\frac {\partial (x _ {1} , x _ {2} , \cdots , x _ {n})}{\partial (r , \theta_ {1} , \theta_ {2} , \cdots , \theta_ {n - 1})} = r ^ {n - 1} \sin^ {n - 2} \theta_ {1} \sin^ {n - 3} \theta_ {2} \dots \sin \theta_ {n - 2}.
$$

如果用球面坐标计算 $n$ 维单位球的体积, 则有

$$
\omega_ {n} = \int_ {0} ^ {1} r ^ {n - 1} \mathrm{d} r \iint \dots \int_ {A _ {n}} \sin^ {n - 2} \theta_ {1} \sin^ {n - 3} \theta_ {2} \dots \sin \theta_ {n - 2} \mathrm{d} \theta_ {1} \mathrm{d} \theta_ {2} \dots \mathrm{d} \theta_ {n - 1},
$$

其中

$$
A _ {n} = \{(\theta_ {1}, \theta_ {2}, \dots , \theta_ {n - 1}) | 0 \leqslant \theta_ {1}, \theta_ {2}, \dots , \theta_ {n - 2} \leqslant \pi , 0 \leqslant \theta_ {n - 1} \leqslant 2 \pi \},
$$

因此有

$$
\iint \dots \int_ {A _ {n}} \sin^ {n - 2} \theta_ {1} \sin^ {n - 3} \theta_ {2} \dots \sin \theta_ {n - 2} \mathrm{d} \theta_ {1} \mathrm{d} \theta_ {2} \dots \mathrm{d} \theta_ {n - 1} = n \omega_ {n}, \tag {16.4.4}
$$

此等式在用球面坐标算积分时有用. 以后我们将知道 $n\omega_{n}$ 是 $n - 1$ 维球面的面积