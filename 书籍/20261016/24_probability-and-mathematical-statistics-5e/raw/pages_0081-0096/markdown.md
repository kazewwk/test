$$
F _ {X} (x) = F (x, \infty) = \sum_ {x _ {i} \leqslant x} \sum_ {j = 1} ^ {\infty} p _ {i j}.
$$

与第二章(3.2)式比较,知道X的分布律为

$$
P \{X = x _ {i} \} = \sum_ {j = 1} ^ {\infty} p _ {i j}, \quad i = 1, 2, \dots .
$$

同样， $Y$ 的分布律为

$$
P \{Y = y _ {j} \} = \sum_ {i = 1} ^ {\infty} p _ {i j}, \quad j = 1, 2, \dots .
$$

记 $p_{i\cdot} = \sum_{j=1}^{\infty} p_{ij} = P\{X = x_i\}, \quad i = 1,2,\cdots,$

$$
p _ {. j} = \sum_ {i = 1} ^ {\infty} p _ {i j} = P \{Y = y _ {j} \}, \quad j = 1, 2, \dots ,
$$

分别称 $p_i$. $(i = 1,2,\dots)$ 和 $p_{.j}(j = 1,2,\dots)$ 为 $(X,Y)$ 关于 $X$ 和关于 $Y$ 的边缘分布律（注意，记号 $p_i$ 中的“·”表示 $p_i$ 是由 $p_{ij}$ 关于 $j$ 求和后得到的；同样，$p_{.j}$ 是由 $p_{ij}$ 关于 $i$ 求和后得到的）.

对于连续型随机变量 $(X,Y)$ ，设它的概率密度为 $f(x,y)$ ，由于

$$
F _ {X} (x) = F (x, \infty) = \int_ {- \infty} ^ {x} \left[ \int_ {- \infty} ^ {\infty} f (x, y) \mathrm{d} y \right] \mathrm{d} x,
$$

由第二章(4.1)式知道， $X$ 是一个连续型随机变量，且其概率密度为

$$
f _ {X} (x) = \int_ {- \infty} ^ {\infty} f (x, y) \mathrm{d} y. \tag {2.3}
$$

同样， $Y$ 也是一个连续型随机变量，其概率密度为

$$
f _ {Y} (y) = \int_ {- \infty} ^ {\infty} f (x, y) \mathrm{d} x. \tag {2.4}
$$

分别称 $f_{X}(x), f_{Y}(y)$ 为 $(X, Y)$ 关于 $X$ 和关于 $Y$ 的边缘概率密度.

例 1 一整数 N 等可能地在  $1,2,3,\cdots,10$  十个值中取一个值. 设  $D=D(N)$  是能整除 N 的正整数的个数,  $F=F(N)$  是能整除 N 的素数的个数 (注意 1 不是素数). 试写出 D 和 F 的联合分布律, 并求边缘分布律.

解 先将试验的样本空间及 $D, F$ 取值的情况列出如下:

| 样本点 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| D | 1 | 2 | 2 | 3 | 2 | 4 | 2 | 4 | 3 | 4 |
| F | 0 | 1 | 1 | 1 | 1 | 2 | 1 | 1 | 1 | 2 |

$D$ 所有可能取的值为 $1,2,3,4;F$ 所有可能取的值为 $0,1,2$. 容易得到 $(D,F)$ 取 $(i,j),i = 1,2,3,4,j = 0,1,2$ 的概率，例如

$$
P \{D = 1, F = 0 \} = \frac {1}{1 0}, \quad P \{D = 2, F = 1 \} = \frac {4}{1 0},
$$

可得 $D$ 和 $F$ 的联合分布律及边缘分布律如下表所示:

| $F\ \ D$ | 1 | 2 | 3 | 4 | $P\{F=j\}$ |
| --- | --- | --- | --- | --- | --- |
| 0 | $\frac{1}{10}$ | 0 | 0 | 0 | $\frac{1}{10}$ |
| 1 | 0 | $\frac{4}{10}$ | $\frac{2}{10}$ | $\frac{1}{10}$ | $\frac{7}{10}$ |
| 2 | 0 | 0 | 0 | $\frac{2}{10}$ | $\frac{2}{10}$ |
| $P\{D=i\}$ | $\frac{1}{10}$ | $\frac{4}{10}$ | $\frac{2}{10}$ | $\frac{3}{10}$ | 1 |

即有边缘分布律

| D | 1 | 2 | 3 | 4 |
| --- | --- | --- | --- | --- |
| $p_k$ | $\frac{1}{10}$ | $\frac{4}{10}$ | $\frac{2}{10}$ | $\frac{3}{10}$ |

| F | 0 | 1 | 2 |
| --- | --- | --- | --- |
| $p_k$ | $\frac{1}{10}$ | $\frac{7}{10}$ | $\frac{2}{10}$ |

我们常常将边缘分布律写在联合分布律表格的边缘上,如上表所示.这就是“边缘分布律”这个名词的来源.

例 2 设随机变量 X 和 Y 具有联合概率密度 (图 3-5)

$$
f (x, y) = \left\{ \begin{array}{l l} 6, & x ^ {2} \leqslant y \leqslant x, \\ 0, & \text {其他}. \end{array} \right.
$$

求边缘概率密度 $f_{X}(x), f_{Y}(y)$.

![](images/page_81_image_13.jpg)

<details>
<summary>text_image</summary>

y
y=x
y=x²
O
x
</details>

图3-5

解

$$
f _ {X} (x) = \int_ {- \infty} ^ {\infty} f (x, y) \mathrm{d} y = \left\{ \begin{array}{l l}  \int_ {x ^ {2}} ^ {x} 6 \mathrm{d} y = 6 (x - x ^ {2})  , & 0 \leqslant x \leqslant 1  , \\ 0  , & \text {其他}. \end{array} \right.
$$

$$
f _ {Y} (y) = \int_ {- \infty} ^ {\infty} f (x, y) \mathrm{d} x = \left\{ \begin{array}{l l}  \int_ {y} ^ {\sqrt {y}} 6 \mathrm{d} x = 6 (\sqrt {y} - y), & 0 \leqslant y \leqslant 1, \\ 0, & \text {其他}. \end{array} \right.
$$

其他.

□

例3 设二维随机变量 $(X,Y)$ 的概率密度为

$$
\begin{array}{l} f (x, y) = \frac {1}{2 \pi \sigma_ {1} \sigma_ {2} \sqrt {1 - \rho^ {2}}} \exp \left\{\frac {- 1}{2 (1 - \rho^ {2})} \left[ \frac {(x - \mu_ {1}) ^ {2}}{\sigma_ {1} ^ {2}} \right. \right. \\ \left. - 2 \rho \frac {\left(x - \mu_ {1}\right) \left(y - \mu_ {2}\right)}{\sigma_ {1} \sigma_ {2}} + \frac {\left(y - \mu_ {2}\right) ^ {2}}{\sigma_ {2} ^ {2}} \right] \Bigg \}, \\ \end{array}
$$

其中 $\mu_1, \mu_2, \sigma_1, \sigma_2, \rho$ 都是常数，且 $\sigma_1 > 0, \sigma_2 > 0, -1 < \rho < 1$. 我们称 $(X, Y)$ 为服从参数为 $\mu_1, \mu_2, \sigma_1, \sigma_2, \rho$ 的二维正态分布（这五个参数的意义将在下一章说明），记为 $(X, Y) \sim N(\mu_1, \mu_2, \sigma_1^2, \sigma_2^2, \rho)$. 试求二维正态随机变量的边缘概率密度.

解 $f_{X}(x) = \int_{-\infty}^{\infty}f(x,y)\mathrm{d}y$ ，由于

$$
\begin{array}{l} \frac {(y - \mu_ {2}) ^ {2}}{\sigma_ {2} ^ {2}} - 2 \rho \frac {(x - \mu_ {1}) (y - \mu_ {2})}{\sigma_ {1} \sigma_ {2}} \\ = \left(\frac {y - \mu_ {2}}{\sigma_ {2}} - \rho \frac {x - \mu_ {1}}{\sigma_ {1}}\right) ^ {2} - \rho^ {2} \frac {(x - \mu_ {1}) ^ {2}}{\sigma_ {1} ^ {2}}, \\ \end{array}
$$

于是

$$
f _ {X} (x) = \frac {1}{2 \pi \sigma_ {1} \sigma_ {2} \sqrt {1 - \rho^ {2}}} \mathrm{e} ^ {- \frac {(x - \mu_ {1}) ^ {2}}{2 \sigma_ {1} ^ {2}}} \int_ {- \infty} ^ {\infty} \mathrm{e} ^ {- \frac {1}{2 (1 - \rho^ {2})} \left(\frac {y - \mu_ {2}}{\sigma_ {2}} - \rho \frac {x - \mu_ {1}}{\sigma_ {1}}\right) ^ {2}} \mathrm{d} y.
$$

令

$$
t = \frac {1}{\sqrt {1 - \rho^ {2}}} \Big (\frac {y - \mu_ {2}}{\sigma_ {2}} - \rho \frac {x - \mu_ {1}}{\sigma_ {1}} \Big),
$$

则有

$$
f _ {X} (x) = \frac {1}{2 \pi \sigma_ {1}} \mathrm{e} ^ {- \frac {(x - \mu_ {1}) ^ {2}}{2 \sigma_ {1} ^ {2}}} \int_ {- \infty} ^ {\infty} \mathrm{e} ^ {- t ^ {2 / 2}} \mathrm{d} t,
$$

即 $f_{X}(x) = \frac{1}{\sqrt{2\pi}\sigma_{1}}\mathrm{e}^{-\frac{(x - \mu_{1})^{2}}{2\sigma_{1}^{2}}},\quad -\infty < x < \infty .$

同理

$$
f _ {Y} (y) = \frac {1}{\sqrt {2 \pi} \sigma_ {2}} \mathrm{e} ^ {- \frac {(y - \mu_ {2}) ^ {2}}{2 \sigma_ {2} ^ {2}}}, \quad - \infty <   y <   \infty .
$$

我们看到二维正态分布的两个边缘分布都是一维正态分布，并且都不依赖于参数 $\rho$ ，亦即对于给定的 $\mu_1, \mu_2, \sigma_1, \sigma_2$ ，不同的 $\rho$ 对应不同的二维正态分布，它们的边缘分布却都是一样的。这一事实表明，单由关于 $X$ 和关于 $Y$ 的边缘分布，一般来说是不能确定随机变量 $X$ 和 $Y$ 的联合分布的。

## § 3 条件分布

我们由条件概率很自然地引出条件概率分布的概念.

设 $(X,Y)$ 是二维离散型随机变量,其分布律为

$$
P \{X = x _ {i}, Y = y _ {j} \} = p _ {i j}, \quad i, j = 1, 2, \dots .
$$

$(X,Y)$ 关于 $X$ 和关于 $Y$ 的边缘分布律分别为

$$
P \{X = x _ {i} \} = p _ {i.} = \sum_ {j = 1} ^ {\infty} p _ {i j}, \quad i = 1, 2, \dots ,
$$

$$
P \{Y = y _ {j} \} = p _ {. j} = \sum_ {i = 1} ^ {\infty} p _ {i j}, \quad j = 1, 2, \dots .
$$

设 $p_{.j} > 0$ ，我们来考虑在事件 $\{Y = y_j\}$ 已发生的条件下事件 $\{X = x_i\}$ 发生的概率，也就是来求事件

$$
\{X = x _ {i} \mid Y = y _ {j} \}, \quad i = 1, 2, \dots
$$

的概率.由条件概率公式,可得

$$
P \{X = x _ {i} \mid Y = y _ {j} \} = \frac {P \{X = x _ {i} , Y = y _ {j} \}}{P \{Y = y _ {j} \}} = \frac {p _ {i j}}{p _ {\cdot j}}, \quad i = 1, 2, \dots .
$$

易知上述条件概率具有分布律的性质:

$$
1 ^ {\circ} P \{X = x _ {i} | Y = y _ {j} \} \geqslant 0.
$$

$$
2 ^ {\circ} \sum_ {i = 1} ^ {\infty} P \{X = x _ {i} \mid Y = y _ {j} \} = \sum_ {i = 1} ^ {\infty} \frac {p _ {i j}}{p _ {\cdot j}} = \frac {1}{p _ {\cdot j}} \sum_ {i = 1} ^ {\infty} p _ {i j} = \frac {p _ {\cdot j}}{p _ {\cdot j}} = 1.
$$

于是我们引入以下的定义.

定义 设 $(X, Y)$ 是二维离散型随机变量，对于固定的 $j$，若 $P\{Y = y_j\} > 0$ 则称

$$
P \{X = x _ {i}   |   Y = y _ {j} \} = \frac {P \{X = x _ {i} , Y = y _ {j} \}}{P \{Y = y _ {j} \}} = \frac {p _ {i j}}{p _ {\cdot j}}, \quad i = 1, 2, \dots \tag {3.1}
$$

为在 $Y = y_{j}$ 条件下随机变量 $X$ 的条件分布律.

同样，对于固定的 $i$ ，若 $P\{X = x_i\} >0$ ，则称

$$
P \{Y = y _ {j} \mid X = x _ {i} \} = \frac {P \{X = x _ {i} , Y = y _ {j} \}}{P \{X = x _ {i} \}} = \frac {p _ {i j}}{p _ {i}}  , \quad j = 1, 2, \dots \tag {3.2}
$$

为在 $X = x_{i}$ 条件下随机变量 $Y$ 的条件分布律.

例1 在一汽车工厂中，一辆汽车有两道工序是由机器人完成的。其一是紧固3只螺栓，其二是焊接2处焊点。以 $X$ 表示由机器人紧固的螺栓中紧固得不良的数目，以 $Y$ 表示由机器人焊接的不良焊点的数目。据积累的资料知 $(X, Y)$ 具有分布律:

| Y\\X | 0 | 1 | 2 | 3 | P{Y=j} |
| --- | --- | --- | --- | --- | --- |
| 0 | 0.840 | 0.030 | 0.020 | 0.010 | 0.900 |
| 1 | 0.060 | 0.010 | 0.008 | 0.002 | 0.080 |
| 2 | 0.010 | 0.005 | 0.004 | 0.001 | 0.020 |
| P{X=i} | 0.910 | 0.045 | 0.032 | 0.013 | 1.000 |

（1）求在 $X = 1$ 的条件下，$Y$ 的条件分布律。（2）求在 $Y = 0$ 的条件下，$X$ 的条件分布律。

解 边缘分布律已经求出列在上表中.

(1) 在 $X = 1$ 的条件下, $Y$ 的条件分布律为

$$
P \{Y = 0 \mid X = 1 \} = \frac {P \{X = 1 , Y = 0 \}}{P \{X = 1 \}} = \frac {0 . 0 3 0}{0 . 0 4 5},
$$

$$
P \{Y = 1 \mid X = 1 \} = \frac {P \{X = 1 , Y = 1 \}}{P \{X = 1 \}} = \frac {0 . 0 1 0}{0 . 0 4 5},
$$

$$
P \{Y = 2 \mid X = 1 \} = \frac {P \{X = 1 , Y = 2 \}}{P \{X = 1 \}} = \frac {0 . 0 0 5}{0 . 0 4 5},
$$

或写成

| Y=k | 0 | 1 | 2 |
| --- | --- | --- | --- |
| P{Y=k\|X=1} | $\frac{6}{9}$ | $\frac{2}{9}$ | $\frac{1}{9}$ |

(2) 同样可得在 Y=0 的条件下 X 的条件分布律为

| X=k | 0 | 1 | 2 | 3 |
| --- | --- | --- | --- | --- |
| P{X=k\|Y=0} | $\frac{84}{90}$ | $\frac{3}{90}$ | $\frac{2}{90}$ | $\frac{1}{90}$ |

例2 一射手进行射击，击中目标的概率为 $p(0 < p < 1)$，射击直至击中目标两次为止。设以 $X$ 表示首次击中目标所进行的射击次数，以 $Y$ 表示总共进行的射击次数，试求 $X$ 和 $Y$ 的联合分布律及条件分布律。

解 按题意 Y=n 就表示在第 n 次射击时击中目标, 且在第 1 次, 第 2 次, …, 第 n-1 次射击中恰有一次击中目标. 已知各次射击是相互独立的, 于是不管 $m(m < n)$ 是多少，概率 $P\{X = m, Y = n\}$ 都应等于

$$
p \cdot p \cdot \underbrace {q \cdot q \cdot \cdots \cdot q} _ {n - 2 \text {个}} = p ^ {2} q ^ {n - 2} \quad (\text {这里} q = 1 - p).
$$

即得 $X$ 和 $Y$ 的联合分布律为

$$
P \{X = m, Y = n \} = p ^ {2} q ^ {n - 2}, \quad n = 2, 3, \dots ; m = 1, 2, \dots , n - 1.
$$

$$
\begin{array}{l} = p ^ {2} \sum_ {n = m + 1} ^ {\infty} q ^ {n - 2} = \frac {p ^ {2} q ^ {m - 1}}{1 - q} = p q ^ {m - 1}, \quad m = 1, 2, \dots , \\ P \{Y = n \} = \sum_ {m = 1} ^ {n - 1} P \{X = m, Y = n \} \\ = \sum_ {m = 1} ^ {n - 1} p ^ {2} q ^ {n - 2} = (n - 1) p ^ {2} q ^ {n - 2}, \quad n = 2, 3, \dots . \\ \end{array}
$$

又 $P\{X = m\} = \sum_{n = m + 1}^{\infty}P\{X = m,Y = n\} = \sum_{n = m + 1}^{\infty}p^{2}q^{n - 2}$

$$
\begin{array}{l} P \{Y = n \} = \sum_ {m = 1} ^ {n - 1} P \{X = m, Y = n \} \\ = \sum_ {m = 1} ^ {n - 1} p ^ {2} q ^ {n - 2} = (n - 1) p ^ {2} q ^ {n - 2}, \quad n = 2, 3, \dots . \\ \end{array}
$$

于是由(3.1)，(3.2)式得到所求的条件分布律为

当  $n=2,3,\cdots$  时，

$$
P \{X = m | Y = n \} = \frac {p ^ {2} q ^ {n - 2}}{(n - 1) p ^ {2} q ^ {n - 2}} = \frac {1}{n - 1}, \quad m = 1, 2, \dots , n - 1;
$$

当  $m=1,2,\cdots$  时，

$$
P \{Y = n \mid X = m \} = \frac {p ^ {2} q ^ {n - 2}}{p q ^ {m - 1}} = p q ^ {n - m - 1}, \quad n = m + 1, m + 2, \dots .
$$

例如， $P\{X=m|Y=3\}=\frac{1}{2},\quad m=1,2;$

$$
P \{Y = n \mid X = 3 \} = p q ^ {n - 4}, \quad n = 4, 5, \dots .
$$

现设 $(X,Y)$ 是二维连续型随机变量，这时由于对任意 $x,y$ 有 $P\{X = x\} = 0$ $P\{Y = y\} = 0$ ，因此就不能直接用条件概率公式引入“条件分布函数”了.

设 $(X,Y)$ 的概率密度为 $f(x,y),(X,Y)$ 关于 $Y$ 的边缘概率密度为 $f_{Y}(y)$. 给定 $y$, 对于任意固定的 $\varepsilon > 0$, 对于任意 $x$, 考虑条件概率

$$
P \{X \leqslant x \mid y <   Y \leqslant y + \varepsilon \},
$$

设 $P\{y < Y \leqslant y + \varepsilon\} > 0$，则有

$$
\begin{array}{l} P \{X \leqslant x \mid y <   Y \leqslant y + \varepsilon \} = \frac {P \{X \leqslant x , y <   Y \leqslant y + \varepsilon \}}{P \{y <   Y \leqslant y + \varepsilon \}} \\ = \frac {\int_ {- \infty} ^ {x} \left[ \int_ {y} ^ {y + \epsilon} f (x , y) \mathrm{d} y \right] \mathrm{d} x}{\int_ {y} ^ {y + \epsilon} f _ {Y} (y) \mathrm{d} y}. \\ \end{array}
$$

在某些条件下，当 $\varepsilon$ 很小时，上式右端分子、分母分别近似于 $\varepsilon \int_{-\infty}^{x} f(x, y) \mathrm{d}x$ 和 $\varepsilon f_{Y}(y)$，于是当 $\varepsilon$ 很小时，有

$$
P \{X \leqslant x \mid y <   Y \leqslant y + \varepsilon \} \approx \frac {\varepsilon \int_ {- \infty} ^ {x} f (x , y) \mathrm{d} x}{\varepsilon f _ {Y} (y)} = \int_ {- \infty} ^ {x} \frac {f (x , y)}{f _ {Y} (y)} \mathrm{d} x. \tag {3.3}
$$

与一维随机变量概率密度的定义式第二章(4.1)式比较,我们给出以下的定义.

定义 设二维随机变量 $(X,Y)$ 的概率密度为 $f(x,y),(X,Y)$ 关于Y的边缘概率密度为 $f_{Y}(y)$ . 若对于固定的 $y,f_{Y}(y)>0$ , 则称 $\frac{f(x,y)}{f_{Y}(y)}$ 为在Y=y的条件下X的条件概率密度, 记为①

$$
f _ {X | Y} (x \mid y) = \frac {f (x , y)}{f _ {Y} (y)}. \tag {3.4}
$$

称 $\int_{-\infty}^{x}f_{X|Y}(x\mid y)\mathrm{d}x = \int_{-\infty}^{x}\frac{f(x,y)}{f_Y(y)}\mathrm{d}x$ 为在 $Y = y$ 的条件下 $X$ 的条件分布函数，记为 $P\{X\leqslant x\mid Y = y\}$ 或 $F_{X|Y}(x\mid y)$，即

$$
F _ {X | Y} (x \mid y) = P \{X \leqslant x \mid Y = y \} = \int_ {- \infty} ^ {x} \frac {f (x , y)}{f _ {Y} (y)} \mathrm{d} x. \tag {3.5}
$$

类似地，可以定义 $f_{Y|X}(y\mid x) = \frac{f(x,y)}{f_X(x)}$ 和 $F_{Y|X}(y\mid x) = \int_{-\infty}^{y}\frac{f(x,y)}{f_X(x)}\mathrm{d}y.$

由(3.3)式知道,当  $\varepsilon$  很小时,有

$$
P \{X \leqslant x \mid y <   Y \leqslant y + \varepsilon \} \approx \int_ {- \infty} ^ {x} f _ {X | Y} (x \mid y) \mathrm{d} x = F _ {X | Y} (x \mid y),
$$

上式说明了条件密度和条件分布函数的含义.

例3设 $G$ 是平面上的有界区域，其面积为 $A$ .若二维随机变量 $(X,Y)$ 具有概率密度

$$
f (x, y) = \left\{ \begin{array}{l l}  \frac {1}{A}, & (x, y) \in G, \\ 0, & \text {其他}, \end{array} \right.
$$

则称 $(X,Y)$ 在 $G$ 上服从均匀分布. 现设二维随机变量 $(X,Y)$ 在圆域 $x^{2} + y^{2}\leqslant 1$ 上服从均匀分布，求条件概率密度 $f_{X|Y}(x|y)$.

解 由假设,随机变量 $(X,Y)$ 具有概率密度

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">① 条件概率密度满足条件: $f_{X|Y}(x \mid y) = \frac{f(x, y)}{f_Y(y)} \geqslant 0;$</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$\int_{-\infty}^{\infty}f_{X|Y}(x \mid y)\mathrm{d}x = \int_{-\infty}^{\infty}\frac{f(x,y)}{f_Y(y)}\mathrm{d}x = \frac{1}{f_Y(y)}\int_{-\infty}^{\infty}f(x,y)\mathrm{d}x = 1.$</span></small>

$$
f (x, y) = \left\{ \begin{array}{l l} { \frac {1}{\pi},} & {x ^ {2} + y ^ {2} \leqslant 1,} \\ {0,} & {\text {其他},} \end{array} \right.
$$

且有边缘概率密度

$$
\begin{array}{l} f _ {Y} (y) = \int_ {- \infty} ^ {\infty} f (x, y) \mathrm{d} x \\ = \left\{ \begin{array}{l l} { \frac {1}{\pi} \int_ {- \sqrt {1 - y ^ {2}}} ^ {\sqrt {1 - y ^ {2}}} \mathrm{d} x = \frac {2}{\pi}   \sqrt {1 - y ^ {2}}  ,} & {- 1 \leqslant y \leqslant 1  ,} \\ {0  ,} & {\text {其他}.} \end{array} \right. \\ \end{array}
$$

于是当 $-1 < y < 1$ 时有

$$
f _ {X \mid Y} (x \mid y) = \left\{ \begin{array}{l l}  \frac {\frac {1}{\pi}}{\frac {2}{\pi} \sqrt {1 - y ^ {2}}} = \frac {1}{2 \sqrt {1 - y ^ {2}}}, & - \sqrt {1 - y ^ {2}} \leqslant x \leqslant \sqrt {1 - y ^ {2}}, \\ 0, & \text {其他}. \end{array} \right.
$$

当 $y = 0$ 和 $y = \frac{1}{2}$ 时 $f_{X|Y}(x|y)$ 的图形分别如图3-6，图3-7所示.

![](images/page_87_chart_8.jpg)

<details>
<summary>contour</summary>

| -1 | 0.5 |
| --- | --- |
| 1 | 0.5 |
</details>

图3-6

![](images/page_87_chart_10.jpg)

<details>
<summary>contour</summary>

| -0.866 | 0.577 |
| --- | --- |
| 0.866 | 0.577 |
</details>

图3-7

例 4 设数 X 在区间  $(0,1)$  上随机地取值，当观察到  $X = x (0 < x < 1)$  时，数 Y 在区间  $(x,1)$  上随机地取值。求 Y 的概率密度  $f_{Y}(y)$ 。

解 按题意 $X$ 具有概率密度

$$
f _ {X} (x) = \left\{ \begin{array}{l l} 1, & 0 <   x <   1, \\ 0, & \text {其他}. \end{array} \right.
$$

对于任意给定的值 $x(0 < x < 1)$，在 $X = x$ 的条件下 $Y$ 的条件概率密度为

$$
f _ {Y \mid X} (y \mid x) = \left\{ \begin{array}{l l} \frac {1}{1 - x}, & x <   y <   1, \\ 0, & \text {其他}. \end{array} \right.
$$

由(3.4)式得 $X$ 和 $Y$ 的联合概率密度为

$$
f (x, y) = f _ {Y \mid X} (y \mid x) f _ {X} (x) = \left\{ \begin{array}{l l} \frac {1}{1 - x}, & 0 <   x <   y <   1, \\ 0, & \text {其他.} \end{array} \right.
$$

于是得关于 $Y$ 的边缘概率密度为

$$
\begin{array}{l} f _ {Y} (y) = \int_ {- \infty} ^ {\infty} f (x, y) \mathrm{d} x \\ = \left\{ \begin{array}{l l} \int_ {0} ^ {y} \frac {1}{1 - x} \mathrm{d} x = - \ln (1 - y), & 0 <   y <   1, \\ 0, & \text {其他.} \end{array} \right. \\ \end{array}
$$

其他.

## § 4 相互独立的随机变量

本节我们将利用两个事件相互独立的概念引出两个随机变量相互独立的概念,这是一个十分重要的概念.

定义 设 $F(x, y)$ 及 $F_{X}(x), F_{Y}(y)$ 分别是二维随机变量 $(X, Y)$ 的分布函数及边缘分布函数. 若对于所有 $x, y$ 有

$$
P \{X \leqslant x, Y \leqslant y \} = P \{X \leqslant x \} P \{Y \leqslant y \}, \tag {4.1}
$$

即 $F(x,y) = F_{X}(x)F_{Y}(y),$ (4.2)

则称随机变量 X 和 Y 是相互独立的.

设 $(X,Y)$ 是连续型随机变量, $f(x,y)$ , $f_{X}(x)$ , $f_{Y}(y)$ 分别为 $(X,Y)$ 的概率密度和边缘概率密度,则X和Y相互独立的条件(4.2)式等价于:等式

$$
f (x, y) = f _ {X} (x) f _ {Y} (y) \tag {4.3}
$$

在平面上几乎处处①成立.

当 $(X,Y)$ 是离散型随机变量时,X和Y相互独立的条件(4.2)式等价于:对于 $(X,Y)$ 的所有可能取的值 $(x_{i},y_{j})$ 有

$$
P \{X = x _ {i}, Y = y _ {j} \} = P \{X = x _ {i} \} P \{Y = y _ {j} \}. \tag {4.4}
$$

在实际中使用(4.3)式或(4.4)式要比使用(4.2)式方便.

例如 §1 例 2 中的随机变量 X 和 Y, 由于

$$
f _ {X} (x) = \left\{ \begin{array}{l l} 2 \mathrm{e} ^ {- 2 x}, & x > 0, \\ 0, & \text {其他}, \end{array} \quad f _ {Y} (y) = \left\{ \begin{array}{l l} \mathrm{e} ^ {- y}, & y > 0, \\ 0, & \text {其他}, \end{array} \right. \right.
$$

故有 $f(x,y) = f_{X}(x)f_{Y}(y)$，因而 $X,Y$ 是相互独立的。

又如, 若 X, Y 具有联合分布律

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">① 此处“几乎处处成立”的含义是:在平面上除去“面积”为零的集合以外,处处成立.</span></small>

| Y\\X | 0 | 1 | P{Y=j} |
| --- | --- | --- | --- |
| 1 | 1/6 | 2/6 | 1/2 |
| 2 | 1/6 | 2/6 | 1/2 |
| P{X=i} | 1/3 | 2/3 | 1 |

则有 $P\{X = 0,Y = 1\} = 1 / 6 = P\{X = 0\} P\{Y = 1\}$

$$
P \{X = 0, Y = 2 \} = 1 / 6 = P \{X = 0 \} P \{Y = 2 \},
$$

$$
P \{X = 1, Y = 1 \} = 2 / 6 = P \{X = 1 \} P \{Y = 1 \},
$$

$$
P \{X = 1, Y = 2 \} = 2 / 6 = P \{X = 1 \} P \{Y = 2 \},
$$

因而 $X, Y$ 是相互独立的.

再如 §2 例 1 中的随机变量 $F$ 和 $D$, 由于 $P\{D=1, F=0\}=1/10 \neq P\{D=1\} \times P\{F=0\}$, 因而 $F$ 和 $D$ 不是相互独立的.

下面考察二维正态随机变量 $(X,Y)$ ，它的概率密度为

$$
\begin{array}{l} f (x, y) = \frac {1}{2 \pi \sigma_ {1} \sigma_ {2} \sqrt {1 - \rho^ {2}}} \exp \left\{\frac {- 1}{2 (1 - \rho^ {2})} \left[ \frac {(x - \mu_ {1}) ^ {2}}{\sigma_ {1} ^ {2}} \right. \right. \\ \left. - 2 \rho \frac {(x - \mu_ {1}) (y - \mu_ {2})}{\sigma_ {1} \sigma_ {2}} + \frac {(y - \mu_ {2}) ^ {2}}{\sigma_ {2} ^ {2}} \right] \Bigg \}. \\ \end{array}
$$

由 §2 中例 3 知道, 其边缘概率密度 $f_{X}(x), f_{Y}(y)$ 的乘积为

$$
f _ {X} (x) f _ {Y} (y) = \frac {1}{2 \pi \sigma_ {1} \sigma_ {2}} \exp \left\{- \frac {1}{2} \left[ \frac {(x - \mu_ {1}) ^ {2}}{\sigma_ {1} ^ {2}} + \frac {(y - \mu_ {2}) ^ {2}}{\sigma_ {2} ^ {2}} \right] \right\}.
$$

因此，如果 $\rho = 0$ ，则对于所有 $x, y$ 有 $f(x, y) = f_X(x)f_Y(y)$，即 $X$ 和 $Y$ 相互独立。反之，如果 $X$ 和 $Y$ 相互独立，由于 $f(x, y), f_X(x), f_Y(y)$ 都是连续函数，故对于所有的 $x, y$ 有 $f(x, y) = f_X(x)f_Y(y)$。特别，令 $x = \mu_1, y = \mu_2$，自这一等式得到

$$
\frac {1}{2 \pi \sigma_ {1} \sigma_ {2} \sqrt {1 - \rho^ {2}}} = \frac {1}{2 \pi \sigma_ {1} \sigma_ {2}},
$$

从而  $\rho=0$ . 综上所述, 得到以下的结论:

对于二维正态随机变量 $(X,Y)$ ，X和Y相互独立的充要条件是参数 $\rho=0$ .

例 一负责人到达办公室的时间均匀分布在8～12时，他的秘书到达办公室的时间均匀分布在7～9时，设他们两人到达的时间相互独立，求他们到达办公室的时间相差不超过5 min(1/12 h)的概率.

解 设 $X$ 和 $Y$ 分别是负责人和他的秘书到达办公室的时间, 由假设 $X$ 和 $Y$ 的概率密度分别为

$$
f _ {X} (x) = \left\{ \begin{array}{l l} \frac {1}{4}, & 8 <   x <   1 2, \\ 0, & \text {其他}, \end{array} \right. \quad f _ {Y} (y) = \left\{ \begin{array}{l l} \frac {1}{2}, & 7 <   y <   9, \\ 0, & \text {其他}, \end{array} \right.
$$

因为 $X, Y$ 相互独立, 故 $(X, Y)$ 的概率密度为

$$
f (x, y) = f _ {X} (x) f _ {Y} (y) = \left\{ \begin{array}{l l} \frac {1}{8}, & 8 <   x <   1 2, 7 <   y <   9, \\ 0, & \text {其他.} \end{array} \right.
$$

按题意需要求概率 $P\{|X - Y| \leqslant 1 / 12\}$. 画出区域: $|x - y| \leqslant 1 / 12$, 以及长方形 $[8 < x < 12; 7 < y < 9]$, 它们的公共部分是四边形 $BCC'B'$, 记为 $G$ (如图3-8). 显然仅当 $(X, Y)$ 取值于 $G$ 内, 他们两人到达的时间相差才不超过 $1 / 12\mathrm{h}$. 因此, 所求的概率为

$$
\begin{array}{l} P \left\{\mid X - Y \mid \leqslant \frac {1}{1 2} \right\} = \iint_ {G} f (x, y) \mathrm{d} x \mathrm{d} y \\ = \frac {1}{8} \times (G \text {的面积}). \\ \end{array}
$$

而 $G$ 的面积 $=$ 三角形 $ABC$ 的面积一三角形 $AB'C'$ 的面积

$$
= \frac {1}{2} \left(\frac {1 3}{1 2}\right) ^ {2} - \frac {1}{2} \left(\frac {1 1}{1 2}\right) ^ {2} = \frac {1}{6}.
$$

于是 $P\left\{|X - Y|\leqslant \frac{1}{12}\right\} = \frac{1}{48}.$

即负责人和他的秘书到达办公室的时间相差不超过 5 min 的概率为 1/48. □

以上所述关于二维随机变量的一些概念,容易推广到 n 维随机变量的情况.

上面说过，n 维随机变量 $(X_{1}, X_{2}, \cdots, X_{n})$ 的分布函数定义为

$$
F (x _ {1}, x _ {2}, \dots , x _ {n}) = P \{X _ {1} \leqslant x _ {1}, X _ {2} \leqslant x _ {2}, \dots , X _ {n} \leqslant x _ {n} \},
$$

其中  $x_{1}, x_{2}, \cdots, x_{n}$  为任意实数.

若存在非负可积函数  $f(x_{1}, x_{2}, \cdots, x_{n})$ ，使对于任意实数  $x_{1}, x_{2}, \cdots, x_{n}$  有

$$
F (x _ {1}, x _ {2}, \dots , x _ {n}) = \int_ {- \infty} ^ {x _ {n}} \int_ {- \infty} ^ {x _ {n - 1}} \dots \int_ {- \infty} ^ {x _ {1}} f (x _ {1}, x _ {2}, \dots , x _ {n}) \mathrm{d} x _ {1} \mathrm{d} x _ {2} \dots \mathrm{d} x _ {n},
$$

则称  $f(x_{1},x_{2},\cdots,x_{n})$  为  $(X_{1},X_{2},\cdots,X_{n})$  的概率密度函数.

设 $(X_{1},X_{2},\cdots,X_{n})$ 的分布函数 $F(x_{1},x_{2},\cdots,x_{n})$ 为已知，则 $(X_{1},X_{2},\cdots,X_{n})$ 的 $k(1\leqslant k<n)$ 维边缘分布函数就随之确定.例如 $(X_{1},X_{2},\cdots,X_{n})$ 关于 $X_{1}$ 、关于 $(X_{1},X_{2})$ 的边缘分布函数分别为

$$
F _ {X _ {1}} (x _ {1}) = F (x _ {1}, \infty , \infty , \dots , \infty),
$$

![](images/page_90_image_20.jpg)

<details>
<summary>text_image</summary>

y
9
A C' C
B' G
B
7
O 8 10 12 x
</details>

图3-8

$$
F _ {X _ {1}, X _ {2}} (x _ {1}, x _ {2}) = F (x _ {1}, x _ {2}, \infty , \infty , \dots , \infty).
$$

又若  $f(x_{1}, x_{2}, \cdots, x_{n})$  是  $(X_{1}, X_{2}, \cdots, X_{n})$  的概率密度，则  $(X_{1}, X_{2}, \cdots, X_{n})$  关于  $X_{1}$ 、关于  $(X_{1}, X_{2})$  的边缘概率密度分别为

$$
\begin{array}{l} f _ {X _ {1}} (x _ {1}) = \int_ {- \infty} ^ {\infty} \int_ {- \infty} ^ {\infty} \dots \int_ {- \infty} ^ {\infty} f (x _ {1}, x _ {2}, \dots , x _ {n}) \mathrm{d} x _ {2} \mathrm{d} x _ {3} \dots \mathrm{d} x _ {n}, \\ f _ {X _ {1}, X _ {2}} (x _ {1}, x _ {2}) = \int_ {- \infty} ^ {\infty} \int_ {- \infty} ^ {\infty} \dots \int_ {- \infty} ^ {\infty} f (x _ {1}, x _ {2}, \dots , x _ {n}) \mathrm{d} x _ {3} \mathrm{d} x _ {4} \dots \mathrm{d} x _ {n}. \\ \end{array}
$$

若对于所有的  $x_{1}, x_{2}, \cdots, x_{n}$  有

$$
F (x _ {1}, x _ {2}, \dots , x _ {n}) = F _ {X _ {1}} (x _ {1}) F _ {X _ {2}} (x _ {2}) \dots F _ {X _ {n}} (x _ {n}),
$$

则称  $X_{1}, X_{2}, \cdots, X_{n}$  是相互独立的.

若对于所有的  $x_{1}, x_{2}, \cdots, x_{m}; y_{1}, y_{2}, \cdots, y_{n}$  有

$$
F (x _ {1}, x _ {2}, \dots , x _ {m}, y _ {1}, y _ {2}, \dots , y _ {n}) = F _ {1} (x _ {1}, x _ {2}, \dots , x _ {m}) F _ {2} (y _ {1}, y _ {2}, \dots , y _ {n}),
$$

其中  $F_{1}, F_{2}, F$  依次为随机变量  $(X_{1}, X_{2}, \cdots, X_{m}), (Y_{1}, Y_{2}, \cdots, Y_{n})$  和  $(X_{1}, X_{2}, \cdots, X_{m}, Y_{1}, Y_{2}, \cdots, Y_{n})$  的分布函数，则称随机变量  $(X_{1}, X_{2}, \cdots, X_{m})$  和  $(Y_{1}, Y_{2}, \cdots, Y_{n})$  是相互独立的.

我们有以下的定理,它在数理统计中是很有用的.

定理 设 $(X_{1},X_{2},\cdots,X_{m})$ 和 $(Y_{1},Y_{2},\cdots,Y_{n})$ 相互独立，则 $X_{i}(i=1,2,\cdots,m)$ 和 $Y_{j}(j=1,2,\cdots,n)$ 相互独立。又若h,g是连续函数，则 $h(X_{1},X_{2},\cdots,X_{m})$ 和 $g(Y_{1},Y_{2},\cdots,Y_{n})$ 相互独立。

(证明略.)

## § 5 两个随机变量的函数的分布

上一章 §5 中已经讨论过一个随机变量的函数的分布, 本节讨论两个随机变量的函数的分布. 我们只就下面几个具体的函数来讨论.

## (一) $Z = X + Y$ 的分布

设 $(X,Y)$ 是二维连续型随机变量，它具有概率密度 $f(x,y)$. 则 $Z = X + Y$ 仍为连续型随机变量，其概率密度为

$$
f _ {X + Y} (z) = \int_ {- \infty} ^ {\infty} f (z - y, y) \mathrm{d} y, \tag {5.1}
$$

或 $f_{X + Y}(z) = \int_{-\infty}^{\infty}f(x,z - x)\mathrm{d}x.$ (5.2)

又若 $X$ 和 $Y$ 相互独立，设 $(X,Y)$ 关于 $X,Y$ 的边缘概率密度分别为 $f_{X}(x)$，$f_{Y}(y)$，则(5.1)，(5.2)式分别化为

$$
f _ {X + Y} (z) = \int_ {- \infty} ^ {\infty} f _ {X} (z - y) f _ {Y} (y) \mathrm{d} y \tag {5.3}
$$

和

$$
f _ {X + Y} (z) = \int_ {- \infty} ^ {\infty} f _ {X} (x) f _ {Y} (z - x) \mathrm{d} x. \tag {5.4}
$$

这两个公式称为 $f_{X}$ 和 $f_{Y}$ 的卷积公式，记为 $f_{X} * f_{Y}$，即

$$
f _ {X} * f _ {Y} = \int_ {- \infty} ^ {\infty} f _ {X} (z - y) f _ {Y} (y) \mathrm{d} y = \int_ {- \infty} ^ {\infty} f _ {X} (x) f _ {Y} (z - x) \mathrm{d} x.
$$

证 先来求 $Z = X + Y$ 的分布函数 $F_{Z}(z)$，即有

$$
F _ {Z} (z) = P \{Z \leqslant z \} = \iint_ {x + y \leqslant z} f (x, y) \mathrm{d} x \mathrm{d} y,
$$

这里积分区域 $G: x + y \leqslant z$ 是直线 $x + y = z$ 及其左下方的半平面(如图3-9). 将二重积分化成累次积分, 得

$$
F _ {z} (z) = \int_ {- \infty} ^ {\infty} \left[ \int_ {- \infty} ^ {z - y} f (x, y) \mathrm{d} x \right] \mathrm{d} y.
$$

固定 $z$ 和 $y$ 对积分 $\int_{-\infty}^{z - y}f(x,y)\mathrm{d}x$ 作变量变换，令$x = u - y$ ，得

$$
\int_ {- \infty} ^ {z - y} f (x, y) \mathrm{d} x = \int_ {- \infty} ^ {z} f (u - y, y) \mathrm{d} u.
$$

![](images/page_92_image_13.jpg)

<details>
<summary>text_image</summary>

y
x+y=z
O
x
</details>

图3-9

于是

$$
F _ {Z} (z) = \int_ {- \infty} ^ {\infty} \left[ \int_ {- \infty} ^ {z} f (u - y, y) \mathrm{d} u \right] \mathrm{d} y = \int_ {- \infty} ^ {z} \left[ \int_ {- \infty} ^ {\infty} f (u - y, y) \mathrm{d} y \right] \mathrm{d} u.
$$

由概率密度的定义即得(5.1)式. 类似可证得(5.2)式.

例1 设 $X$ 和 $Y$ 是两个相互独立的随机变量. 它们都服从 $N(0,1)$ 分布, 其概率密度为

$$
f _ {X} (x) = \frac {1}{\sqrt {2 \pi}} \mathrm{e} ^ {- x ^ {2} / 2}, \quad - \infty <   x <   \infty ,
$$

$$
f _ {Y} (y) = \frac {1}{\sqrt {2 \pi}} \mathrm{e} ^ {- y ^ {2} / 2}, \quad - \infty <   y <   \infty .
$$

求  $Z=X+Y$  的概率密度.

解 由(5.4)式

$$
\begin{array}{l} f _ {Z} (z) = \int_ {- \infty} ^ {\infty} f _ {X} (x) f _ {Y} (z - x) \mathrm{d} x \\ = \frac {1}{2 \pi} \int_ {- \infty} ^ {\infty} \mathrm{e} ^ {- \frac {x ^ {2}}{2}} \cdot \mathrm{e} ^ {- \frac {(z - x) ^ {2}}{2}} \mathrm{d} x = \frac {1}{2 \pi} \mathrm{e} ^ {- \frac {z ^ {2}}{4}} \int_ {- \infty} ^ {\infty} \mathrm{e} ^ {- \left(x - \frac {z}{2}\right) ^ {2}} \mathrm{d} x, \\ \end{array}
$$

令 $t = x - \frac{z}{2}$ 得

$$
f _ {Z} (z) = \frac {1}{2 \pi} \mathrm{e} ^ {- \frac {z ^ {2}}{4}} \int_ {- \infty} ^ {\infty} \mathrm{e} ^ {- t ^ {2}} \mathrm{d} t = \frac {1}{2 \pi} \mathrm{e} ^ {- \frac {z ^ {2}}{4}} \sqrt {\pi} = \frac {1}{2 \sqrt {\pi}} \mathrm{e} ^ {- \frac {z ^ {2}}{4}}.
$$

即 $Z$ 服从 $N(0,2)$ 分布.

一般，设 X, Y 相互独立且  $X \sim N(\mu_{1}, \sigma_{1}^{2})$ ,  $Y \sim N(\mu_{2}, \sigma_{2}^{2})$ . 由 (5.4) 式经过计算知  $Z = X + Y$  仍然服从正态分布，且有  $Z \sim N(\mu_{1} + \mu_{2}, \sigma_{1}^{2} + \sigma_{2}^{2})$ . 这个结论还能推广到 n 个独立正态随机变量之和的情况. 即若  $X_{i} \sim N(\mu_{i}, \sigma_{i}^{2})$  ( $i = 1, 2, \cdots, n$ ), 且它们相互独立，则它们的和  $Z = X_{1} + X_{2} + \cdots + X_{n}$  仍然服从正态分布，且有  $Z \sim N(\mu_{1} + \mu_{2} + \cdots + \mu_{n}, \sigma_{1}^{2} + \sigma_{2}^{2} + \cdots + \sigma_{n}^{2})$ .

更一般地,可以证明有限个相互独立的正态随机变量的线性组合仍然服从正态分布.

例2 在一简单电路中，两电阻 $R_{1}$ 和 $R_{2}$ 串联连接，设 $R_{1}, R_{2}$ 相互独立，它们的概率密度均为

$$
f (x) = \left\{ \begin{array}{l l} { \frac {1 0 - x}{5 0},} & {0 \leqslant x \leqslant 1 0,} \\ {0,} & {\text {其他}.} \end{array} \right.
$$

求总电阻 $R = R_{1} + R_{2}$ 的概率密度.

解 由(5.4)式,R 的概率密度为

$$
f _ {R} (z) = \int_ {- \infty} ^ {\infty} f (x) f (z - x) \mathrm{d} x.
$$

易知仅当

$$
\left\{ \begin{array}{l l} 0 <   x <   1 0, \\ 0 <   z - x <   1 0, \end{array} \right. \text {即} \left\{ \begin{array}{l l} 0 <   x <   1 0, \\ z - 1 0 <   x <   z \end{array} \right.
$$

时上述积分的被积函数不等于零. 参考图 3-10, 即得

$$
f _ {R} (z) = \left\{ \begin{array}{l l}  \int_ {0} ^ {z} f (x) f (z - x) \mathrm{d} x, & 0 \leqslant z <   1 0, \\  \int_ {z - 1 0} ^ {1 0} f (x) f (z - x) \mathrm{d} x, & 1 0 \leqslant z \leqslant 2 0, \\ 0, & \text {其他}. \end{array} \right.
$$

![](images/page_93_chart_15.jpg)

<details>
<summary>line</summary>

| z | x=z | x=z-10 |
| --- | --- | --- |
| 0 | 0 | — |
| 10 | 10 | 10 |
| 20 | — | 10 |
</details>

图3-10

将 $f(x)$ 的表达式代入上式得

$$
f _ {R} (z) = \left\{ \begin{array}{l l}  \frac {1}{1 5 0 0 0} (6 0 0 z - 6 0 z ^ {2} + z ^ {3}), & 0 \leqslant z <   1 0, \\  \frac {1}{1 5 0 0 0} (2 0 - z) ^ {3}, & 1 0 \leqslant z <   2 0, \\ 0, & \text {其他}. \end{array} \right.
$$

![](images/page_93_image_19.jpg)

例3 设随机变量 $X, Y$ 相互独立，且分别服从参数为 $\alpha, \theta; \beta, \theta$ 的 $\Gamma$ 分布（分别记成 $X \sim \Gamma(\alpha, \theta), Y \sim \Gamma(\beta, \theta)$. $X, Y$ 的概率密度分别为

$$
f _ {X} (x) = \left\{ \begin{array}{l l} {{ \frac {1}{\theta^ {\alpha} \Gamma (\alpha)} x ^ {\alpha - 1} \mathrm{e} ^ {- x / \theta},}} & {{x > 0,}} \\ {{0,}} & {{\text {其他},}} \end{array} \right. \quad \alpha > 0, \theta > 0.
$$

$$
f _ {Y} (y) = \left\{ \begin{array}{l l} \frac {1}{\theta^ {\beta} \Gamma (\beta)} y ^ {\beta - 1} \mathrm{e} ^ {- y / \theta}, & y > 0, \\ 0, & \text {其他}, \end{array} \right. \quad \beta > 0, \theta > 0.
$$

试证明 $Z = X + Y$ 服从参数为 $\alpha +\beta ,\theta$ 的 $\Gamma$ 分布，即 $X + Y\sim \Gamma (\alpha +\beta ,\theta)$

证 由(5.4)式 $Z = X + Y$ 的概率密度为

$$
f _ {Z} (z) = \int_ {- \infty} ^ {\infty} f _ {X} (x) f _ {Y} (z - x) \mathrm{d} x.
$$

易知仅当

$$
\left\{ \begin{array}{l l} x > 0, \\ z - x > 0, \end{array} \right. \quad \text {亦即} \quad \left\{ \begin{array}{l l} x > 0, \\ x <   z \end{array} \right.
$$

时上述积分的被积函数不等于零,于是(参见图3-11)知当z<0时 $f_{Z}(z)=0$ ,而当z>0时有

$$
\begin{array}{l} f _ {Z} (z) = \int_ {0} ^ {z} \frac {1}{\theta^ {\alpha} \Gamma (\alpha)} x ^ {\alpha - 1} \mathrm{e} ^ {- x / \theta} \frac {1}{\theta^ {\beta} \Gamma (\beta)} (z - x) ^ {\beta - 1} \mathrm{e} ^ {- (z - x) / \theta} \mathrm{d} x \\ = \frac {\mathrm{e} ^ {- z / \theta}}{\theta^ {\alpha + \beta} \Gamma (\alpha) \Gamma (\beta)} \int_ {0} ^ {z} x ^ {\alpha - 1} (z - x) ^ {\beta - 1} \mathrm{d} x (\text {令} x = z t) \\ = \frac {z ^ {\alpha + \beta - 1} \mathrm{e} ^ {- z / \theta}}{\theta^ {\alpha + \beta} \Gamma (\alpha) \Gamma (\beta)} \int_ {0} ^ {1} t ^ {\alpha - 1} (1 - t) ^ {\beta - 1} \mathrm{d} t \\ \stackrel {\text {记成}} {=} A z ^ {\alpha + \beta - 1} \mathrm{e} ^ {- z / \theta}, \\ \end{array}
$$

其中 $A = \frac{1}{\theta^{\alpha + \beta}\Gamma(\alpha)\Gamma(\beta)}\int_{0}^{1}t^{\alpha -1}(1 - t)^{\beta -1}\mathrm{d}t.$ (5.5)①

现在来计算 A. 由概率密度的性质得到

$$
\begin{array}{l} 1 = \int_ {- \infty} ^ {\infty} f _ {Z} (z) \mathrm{d} z = \int_ {0} ^ {\infty} A z ^ {\alpha + \beta - 1} \mathrm{e} ^ {- z / \theta} \mathrm{d} z \\ = A \theta^ {\alpha + \beta} \int_ {0} ^ {\infty} (z / \theta) ^ {\alpha + \beta - 1} \mathrm{e} ^ {- z / \theta} \mathrm{d} (z / \theta) = A \theta^ {\alpha + \beta} \Gamma (\alpha + \beta), \\ \end{array}
$$

![](images/page_94_image_15.jpg)

<details>
<summary>text_image</summary>

x
O
z
</details>

图3-11

① (5.5)式中的积分

$$
\int_ {0} ^ {1} t ^ {\alpha - 1} (1 - t) ^ {\beta - 1} \mathrm{d} t \stackrel {\text {记成}} {=} \mathrm{B} (\alpha , \beta), \qquad \alpha , \beta > 0,
$$

称为 Beta 函数. 由(5.5), (5.6)式知 Beta 函数与  $\Gamma$  函数有如下关系:

$$
\mathrm{B} (\alpha , \beta) = \frac {\Gamma (\alpha) \Gamma (\beta)}{\Gamma (\alpha + \beta)}.
$$

即有 $A = \frac{1}{\theta^{\alpha + \beta}\Gamma(\alpha + \beta)}.$ (5.6)

于是 $f_{Z}(z) = \left\{ \begin{array}{ll} \frac{1}{\theta^{\alpha + \beta}\Gamma(\alpha + \beta)} z^{\alpha + \beta - 1}\mathrm{e}^{-z / \theta}, & z > 0,\\ 0, & \text{其他.} \end{array} \right.$

即 $X + Y\sim \Gamma (\alpha +\beta ,\theta)$

上述结论还能推广到 n 个相互独立的  $\Gamma$  分布变量之和的情况. 即若  $X_{1}, X_{2}, \cdots, X_{n}$  相互独立, 且  $X_{i}$  服从参数为  $\alpha_{i}, \beta (i = 1, 2, \cdots, n)$  的  $\Gamma$  分布, 则  $\sum_{i=1}^{n} X_{i}$  服从参数为  $\sum_{i=1}^{n} \alpha_{i}, \beta$  的  $\Gamma$  分布. 这一性质称为  $\Gamma$  分布的可加性.

## （二） $Z = \frac{Y}{X}$ 的分布、 $Z = XY$ 的分布

设 $(X,Y)$ 是二维连续型随机变量，它具有概率密度 $f(x,y)$，则 $Z = \frac{Y}{X}$，$Z = XY$ 仍为连续型随机变量，其概率密度分别为

$$
f _ {Y / X} (z) = \int_ {- \infty} ^ {\infty} | x | f (x, x z) \mathrm{d} x, \tag {5.7}
$$

$$
f _ {X Y} (z) = \int_ {- \infty} ^ {\infty} \frac {1}{| x |} f \Big (x, \frac {z}{x} \Big) \mathrm{d} x. \tag {5.8}
$$

又若 $X$ 和 $Y$ 相互独立. 设 $(X, Y)$ 关于 $X, Y$ 的边缘概率密度分别为 $f_{X}(x), f_{Y}(y)$, 则(5.7)式化为

$$
f _ {Y / X} (z) = \int_ {- \infty} ^ {\infty} | x | f _ {X} (x) f _ {Y} (x z) \mathrm{d} x. \tag {5.9}
$$

而(5.8)式化为

$$
f _ {X Y} (z) = \int_ {- \infty} ^ {\infty} \frac {1}{| x |} f _ {X} (x) f _ {Y} \Big (\frac {z}{x} \Big) \mathrm{d} x. \tag {5.10}
$$

证 $Z = Y / X$ 的分布函数为(如图3-12)

$$
\begin{array}{l} F _ {Y / X} (z) = P \{Y / X \leqslant z \} = \iint_ {G _ {1} \cup G _ {2}} f (x, y) \mathrm{d} x \mathrm{d} y \\ = \iint_ {y / x \leqslant z, x <   0} f (x, y) \mathrm{d} y \mathrm{d} x + \iint_ {y / x \leqslant z, x > 0} f (x, y) \mathrm{d} y \mathrm{d} x \\ = \int_ {- \infty} ^ {0} \left[ \int_ {z x} ^ {\infty} f (x, y) \mathrm{d} y \right] \mathrm{d} x + \int_ {0} ^ {\infty} \left[ \int_ {- \infty} ^ {z x} f (x, y) \mathrm{d} y \right] \mathrm{d} x \\ \xlongequal {\text {令} y = x u} \int_ {- \infty} ^ {0} \left[ \int_ {z} ^ {- \infty} x f (x, x u) \mathrm{d} u \right] \mathrm{d} x + \int_ {0} ^ {\infty} \left[ \int_ {- \infty} ^ {z} x f (x, x u) \mathrm{d} u \right] \mathrm{d} x \\ \end{array}
$$