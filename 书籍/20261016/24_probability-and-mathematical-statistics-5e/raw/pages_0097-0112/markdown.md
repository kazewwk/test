![](images/page_96_image_2.jpg)

图3-12

$$
\begin{array}{l} = \int_ {- \infty} ^ {0} \left[ \int_ {- \infty} ^ {z} (- x) f (x, x u) \mathrm{d} u \right] \mathrm{d} x + \int_ {0} ^ {\infty} \left[ \int_ {- \infty} ^ {z} x f (x, x u) \mathrm{d} u \right] \mathrm{d} x \\ = \int_ {- \infty} ^ {\infty} \left[ \int_ {- \infty} ^ {z} | x | f (x, x u) \mathrm{d} u \right] \mathrm{d} x \\ = \int_ {- \infty} ^ {z} \left[ \int_ {- \infty} ^ {\infty} | x | f (x, x u) \mathrm{d} x \right] \mathrm{d} u, \\ \end{array}
$$

由概率密度的定义即得(5.7)式.

类似地,可求出  $f_{XY}(z)$  的概率密度为(5.8)式.

例 4 某公司提供一种地震保险,保险费 Y 的概率密度为

$$
f (y) = \left\{ \begin{array}{l l} \frac {y}{2 5} \mathrm{e} ^ {- y / 5}, & y > 0, \\ 0, & \text {其他}. \end{array} \right.
$$

保险赔付 $X$ 的概率密度为

$$
g (x) = \left\{ \begin{array}{l l} \frac {1}{5} \mathrm{e} ^ {- x / 5}, & x > 0, \\ 0, & \text {其他.} \end{array} \right.
$$

设 X 与 Y 相互独立, 求 Z = Y / X 的概率密度.

解 由(5.9)式知, 当 z<0 时,  $f_{Z}(z)=0$ ; 当 z>0 时, Z 的概率密度为

$$
\begin{array}{l} f _ {Z} (z) = \int_ {0} ^ {\infty} x \cdot \frac {1}{5} \mathrm{e} ^ {- x / 5} \cdot \frac {x z}{2 5} \mathrm{e} ^ {- x z / 5} \mathrm{d} x = \frac {z}{1 2 5} \int_ {0} ^ {\infty} x ^ {2} \mathrm{e} ^ {- x \cdot \frac {1 + z}{5}} \mathrm{d} x \\ = \frac {z}{1 2 5} \frac {\Gamma (3)}{\left[ (1 + z) / 5 \right] ^ {3}} = \frac {2 z}{(1 + z) ^ {3}}. \\ \end{array}
$$

## （三） $M = \max \{X,Y\}$ 及 $N = \min \{X,Y\}$ 的分布

设 $X, Y$ 是两个相互独立的随机变量，它们的分布函数分别为 $F_{X}(x)$ 和

$F_{Y}(y)$. 现在来求 $M = \max \{X, Y\}$ 及 $N = \min \{X, Y\}$ 的分布函数.

由于 $M = \max \{X,Y\}$ 不大于 $z$ 等价于 $X$ 和 $Y$ 都不大于 $z$ ，故有

$$
P \{M \leqslant z \} = P \{X \leqslant z, Y \leqslant z \}.
$$

又由于 $X$ 和 $Y$ 相互独立，得到 $M = \max \{X, Y\}$ 的分布函数为

$$
F _ {\max} (z) = P \{M \leqslant z \} = P \{X \leqslant z, Y \leqslant z \} = P \{X \leqslant z \} P \{Y \leqslant z \}.
$$

即有 $F_{\mathrm{max}}(z) = F_X(z)F_Y(z)$. (5.11)

类似地, 可得  $N = \min\{X, Y\}$  的分布函数为

$$
\begin{array}{l} F _ {\min} (z) = P \{N \leqslant z \} = 1 - P \{N > z \} \\ = 1 - P \{X > z, Y > z \} = 1 - P \{X > z \} P \{Y > z \}. \\ \end{array}
$$

即 $F_{\mathrm{min}}(z) = 1 - [1 - F_X(z)][1 - F_Y(z)].$ (5.12)

以上结果容易推广到 n 个相互独立的随机变量的情况. 设  $X_{1}, X_{2}, \cdots, X_{n}$  是 n 个相互独立的随机变量. 它们的分布函数分别为  $F_{X_{i}}(x_{i}) (i=1,2,\cdots,n)$ ，则  $M=\max\{X_{1}, X_{2}, \cdots, X_{n}\}$  及  $N=\min\{X_{1}, X_{2}, \cdots, X_{n}\}$  的分布函数分别为

$$
F _ {\max} (z) = F _ {X _ {1}} (z) F _ {X _ {2}} (z) \dots F _ {X _ {n}} (z), \tag {5.13}
$$

$$
F _ {\min} (z) = 1 - [ 1 - F _ {X _ {1}} (z) ] [ 1 - F _ {X _ {2}} (z) ] \dots [ 1 - F _ {X _ {n}} (z) ]. \tag {5.14}
$$

特别，当  $X_{1}, X_{2}, \cdots, X_{n}$  相互独立且具有相同分布函数  $F(x)$  时有

$$
F _ {\max} (z) = \left[ F (z) \right] ^ {n}, \tag {5.15}
$$

$$
F _ {\min} (z) = 1 - \left[ 1 - F (z) \right] ^ {n}. \tag {5.16}
$$

例5 设系统 $L$ 由两个相互独立的子系统 $L_{1}, L_{2}$ 连接而成，连接的方式分别为(i)串联，(ii)并联，(iii)备用（当系统 $L_{1}$ 损坏时，系统 $L_{2}$ 开始工作），如图3-13所示.设 $L_{1}, L_{2}$ 的寿命分别为 $X, Y$ ，已知它们的概率密度分别为

$$
f _ {X} (x) = \left\{ \begin{array}{l l} \alpha \mathrm{e} ^ {- \alpha x}, & x > 0, \\ 0, & x \leqslant 0, \end{array} \right. \tag {5.17}
$$

$$
f _ {Y} (y) = \left\{ \begin{array}{l l} \beta \mathrm{e} ^ {- \beta y}, & y > 0, \\ 0, & y \leqslant 0, \end{array} \right. \tag {5.18}
$$

其中 $\alpha > 0, \beta > 0$ 且 $\alpha \neq \beta$. 试分别就以上三种连接方式写出 $L$ 的寿命 $Z$ 的概率密度.

解 (i) 串联的情况.

![](images/page_97_image_22.jpg)

图3-13

由于当 $L_{1}, L_{2}$ 中有一个损坏时，系统 $L$ 就停止工作，所以这时 $L$ 的寿命为

$$
Z = \min \{X, Y \}.
$$

由(5.17)，(5.18)式 $X,Y$ 的分布函数分别为

$$
F _ {X} (x) = \left\{ \begin{array}{l l} 1 - \mathrm{e} ^ {- \alpha x}, & x > 0, \\ 0, & x \leqslant 0, \end{array} \right. F _ {Y} (y) = \left\{ \begin{array}{l l} 1 - \mathrm{e} ^ {- \beta y}, & y > 0, \\ 0, & y \leqslant 0. \end{array} \right.
$$

由(5.12)式得 $Z = \min \{X,Y\}$ 的分布函数为

$$
F _ {\min} (z) = \left\{ \begin{array}{l l} 1 - \mathrm{e} ^ {- (\alpha + \beta) z}, & z > 0, \\ 0, & z \leqslant 0. \end{array} \right.
$$

于是 $Z = \min \{X,Y\}$ 的概率密度为

$$
f _ {\min} (z) = \left\{ \begin{array}{l l} (\alpha + \beta) \mathrm{e} ^ {- (\alpha + \beta) z}, & z > 0, \\ 0, & z \leqslant 0. \end{array} \right.
$$

## (ii) 并联的情况.

由于当且仅当 $L_{1}, L_{2}$ 都损坏时，系统 $L$ 才停止工作，所以这时 $L$ 的寿命 $Z$ 为

$$
Z = \max \{X, Y \}.
$$

按(5.11)式得 $Z = \max \{X,Y\}$ 的分布函数为

$$
F _ {\max} (z) = F _ {X} (z) F _ {Y} (z) = \left\{ \begin{array}{l l} (1 - \mathrm{e} ^ {- \alpha z}) (1 - \mathrm{e} ^ {- \beta z}), & z > 0, \\ 0, & z \leqslant 0. \end{array} \right.
$$

于是 $Z = \max \{X,Y\}$ 的概率密度为

$$
f _ {\max} (z) = \left\{ \begin{array}{l l} \alpha \mathrm{e} ^ {- \alpha z} + \beta \mathrm{e} ^ {- \beta z} - (\alpha + \beta) \mathrm{e} ^ {- (\alpha + \beta) z}, & z > 0, \\ 0, & z \leqslant 0. \end{array} \right.
$$

## (iii) 备用的情况.

由于这时当系统 $L_{1}$ 损坏时系统 $L_{2}$ 才开始工作，因此整个系统 $L$ 的寿命 $Z$ 是 $L_{1}, L_{2}$ 两者寿命之和，即

$$
Z = X + Y.
$$

按(5.3)式, 当 z > 0 时  $Z = X + Y$  的概率密度为

$$
\begin{array}{l} f (z) = \int_ {- \infty} ^ {\infty} f _ {X} (z - y) f _ {Y} (y) \mathrm{d} y = \int_ {0} ^ {z} \alpha \mathrm{e} ^ {- \alpha (z - y)} \beta \mathrm{e} ^ {- \beta y} \mathrm{d} y \\ = \alpha \beta \mathrm{e} ^ {- \alpha z} \int_ {0} ^ {z} \mathrm{e} ^ {- (\beta - \alpha) y} \mathrm{d} y = \frac {\alpha \beta}{\beta - \alpha} (\mathrm{e} ^ {- \alpha z} - \mathrm{e} ^ {- \beta z}). \\ \end{array}
$$

当 $z \leqslant 0$ 时，$f(z) = 0$，于是 $Z = X + Y$ 的概率密度为

$$
f (z) = \left\{ \begin{array}{l l} \frac {\alpha \beta}{\beta - \alpha} (\mathrm{e} ^ {- \alpha z} - \mathrm{e} ^ {- \beta z}), & z > 0, \\ 0, & z \leqslant 0. \end{array} \right.
$$

□

## 小结

将一维随机变量的概念加以扩充, 就得到多维随机变量. 我们着重讨论了二维随机变量. 和一维随机变量一样, 我们定义二维随机变量  $(X,Y)$  的分布函数

$$
F (x, y) = P \{X \leqslant x, Y \leqslant y \}, - \infty <   x <   \infty , - \infty <   y <   \infty .
$$

对于离散型随机变量 $(X,Y)$ 定义了分布律

$$
P \{X = x _ {i}, Y = y _ {j} \} = p _ {i j}, i = 1, 2, \dots , j = 1, 2, \dots \Big (p _ {i j} \geqslant 0, \sum_ {i = 1} ^ {\infty} \sum_ {j = 1} ^ {\infty} p _ {i j} = 1 \Big).
$$

对于连续型随机变量 $(X,Y)$ 定义了概率密度 $f(x,y)(f(x,y)\geqslant 0)$，且有

$$
F (x, y) = \int_ {- \infty} ^ {y} \int_ {- \infty} ^ {x} f (x, y) \mathrm{d} x \mathrm{d} y, \quad \text {对于任意} x, y.
$$

二维随机变量的分布律与概率密度的性质与一维的类似.特别，对于二维连续型随机变量，有公式

$$
P \{(X, Y) \in G \} = \iint_ {G} f (x, y) \mathrm{d} x \mathrm{d} y,
$$

其中， $G$ 是平面上的某区域（它是一维连续型随机变量的公式 $P\{a < X \leqslant b\} = \int_{a}^{b} f(x) \, \mathrm{d}x$ 的扩充).这一公式常用来求随机变量的不等式成立的概率，例如

$$
P \{Y \leqslant X \} = P \{(X, Y) \in G \} = \iint_ {G} f (x, y) \mathrm{d} x \mathrm{d} y,
$$

其中， $G$ 为半平面 $y\leqslant x$

在研究二维随机变量 $(X,Y)$ 时，除了讨论上述与一维随机变量类似的内容外，还要讨论以下的新内容:边缘分布、条件分布、随机变量的独立性等.

注意到,对于 $(X,Y)$ 而言,由 $(X,Y)$ 的分布可以确定关于X、关于Y的边缘分布.反之,由关于X和关于Y的边缘分布一般是不能确定 $(X,Y)$ 的分布的.只有当X,Y相互独立时,由两边缘分布能确定 $(X,Y)$ 的分布.

随机变量的独立性是随机事件独立性的扩充.我们也常利用问题的实际意义去判断两个随机变量的独立性.例如，若 $X,Y$ 分别表示两个工厂生产的显像管的寿命，我们可以认为$X,Y$ 是相互独立的.

我们还讨论了 $Z = X + Y, Z = Y / X, Z = XY, M = \max \{X, Y\}, N = \min \{X, Y\}$ 的分布的求法（设 $(X, Y)$ 的分布已知）.

本章在进行各种问题的计算时，要用到二重积分或用到二元函数固定其中一个变量对另一个变量的积分.此时千万要搞清楚积分变量的变化范围.题目做错，往往是由于在进行积分运算时，将有关的积分区间或积分区域搞错了.在做题时，画出有关函数的定义域的图形，对于正确确定积分上下限肯定是有帮助的.另外，所求得的边缘概率密度、条件概率密度或 $Z=X+Y$ 的概率密度等，往往是分段函数，正确写出分段函数的表达式当然是必需的.

## ■重要术语及主题

二维随机变量 $(X,Y)$ （ $X,Y$ )的分布函数 离散型随机变量 $(X,Y)$ 的分布律 连续型随机变量 $(X,Y)$ 的概率密度 离散型随机变量 $(X,Y)$ 的边缘分布律 连续型随机变量 $(X,Y)$ 的边缘概率密度 条件分布函数 条件分布律 条件概率密度 两个随机变量 $X,Y$ 的独立性 $Z = X + Y, Z = Y / X, Z = XY$ 的概率密度 $M = \max \{X,Y\}, N = \min \{X,Y\}$ 的概率密度

## 习题

1. 在一箱子中装有 12 只开关, 其中 2 只是次品, 在其中取两次, 每次任取一只, 考虑两种试验: (1) 放回抽样; (2) 不放回抽样. 我们定义随机变量 $X, Y$ 如下:

$$
X = \left\{ \begin{array}{l l} 0, & \text {若第一次取出的是正品,} \\ 1, & \text {若第一次取出的是次品;} \end{array} \right.
$$

$$
Y = \left\{ \begin{array}{l l} 0, & \text {若第二次取出的是正品,} \\ 1, & \text {若第二次取出的是次品.} \end{array} \right.
$$

试分别就(1)、(2)两种情况,写出X和Y的联合分布律.

2.（1）盒子里装有3只黑球、2只红球、2只白球，在其中任取4只球.以 $X$ 表示取到黑球的只数，以 $Y$ 表示取到红球的只数.求 $X$ 和 $Y$ 的联合分布律.

(2) 在(1)中求  $P\{X > Y\}$ ,  $P\{Y = 2X\}$ ,  $P\{X + Y = 3\}$ ,  $P\{X < 3 - Y\}$ .

3. 设随机变量 $(X, Y)$ 的概率密度为

$$
f (x, y) = \left\{ \begin{array}{l l} k (6 - x - y), & 0 <   x <   2, 2 <   y <   4, \\ 0, & \text {其他.} \end{array} \right.
$$

(1) 确定常数 k.
(2) 求  $P\{X<1,Y<3\}$ .
(3) 求  $P\{X<1.5\}$ .
(4) 求  $P\{X+Y \leqslant 4\}$ .

4. 设 X, Y 都是非负的连续型随机变量, 它们相互独立.

(1) 证明 $P\{X < Y\} = \int_{0}^{\infty} F_X(x) f_Y(x) \, \mathrm{d}x,$

其中  $F_{X}(x)$  是 X 的分布函数,  $f_{Y}(y)$  是 Y 的概率密度.

(2) 设 X, Y 相互独立, 其概率密度分别为

$$
f _ {X} (x) = \left\{ \begin{array}{l l} \lambda_ {1} \mathrm{e} ^ {- \lambda_ {1} x}, & x > 0, \\ 0, & \text {其他}, \end{array} \quad f _ {Y} (y) = \left\{ \begin{array}{l l} \lambda_ {2} \mathrm{e} ^ {- \lambda_ {2} y}, & y > 0, \\ 0, & \text {其他}, \end{array} \right. \right.
$$

求 $P\{X < Y\}$ .

5. 设随机变量 $(X, Y)$ 具有分布函数

$$
F (x, y) = \left\{ \begin{array}{l l} 1 - \mathrm{e} ^ {- x} - \mathrm{e} ^ {- y} + \mathrm{e} ^ {- x - y}, & x > 0, y > 0, \\ 0, & \text {其他.} \end{array} \right.
$$

求边缘分布函数.

6. 将一枚硬币掷 3 次, 以 $X$ 表示前 2 次中出现 $H$ 的次数, 以 $Y$ 表示 3 次中出现 $H$ 的次数. 求 $X, Y$ 的联合分布律以及 $(X, Y)$ 的边缘分布律.

7. 设二维随机变量 $(X, Y)$ 的概率密度为

$$
f (x, y) = \left\{ \begin{array}{l l} 4. 8 y (2 - x), & 0 \leqslant x \leqslant 1, 0 \leqslant y \leqslant x, \\ 0, & \text {其他}. \end{array} \right.
$$

求边缘概率密度.

8. 设二维随机变量 $(X, Y)$ 的概率密度为

$$
f (x, y) = \left\{ \begin{array}{l l} \mathrm{e} ^ {- y}, & 0 <   x <   y, \\ 0, & \text {其他}. \end{array} \right.
$$

求边缘概率密度.

9. 设二维随机变量 $(X, Y)$ 的概率密度为

$$
f (x, y) = \left\{ \begin{array}{l l} c x ^ {2} y, & x ^ {2} \leqslant y \leqslant 1, \\ 0, & \text {其他}. \end{array} \right.
$$

(1) 确定常数 c.

(2) 求边缘概率密度.

10. 将某医药公司8月份和9月份收到的青霉素针剂的订货单数分别记为 $X$ 和 $Y$. 据以往积累的资料知 $X$ 和 $Y$ 的联合分布律为

| Y\\X | 51 | 52 | 53 | 54 | 55 |
| --- | --- | --- | --- | --- | --- |
| 51 | 0.06 | 0.05 | 0.05 | 0.01 | 0.01 |
| 52 | 0.07 | 0.05 | 0.01 | 0.01 | 0.01 |
| 53 | 0.05 | 0.10 | 0.10 | 0.05 | 0.05 |
| 54 | 0.05 | 0.02 | 0.01 | 0.01 | 0.03 |
| 55 | 0.05 | 0.06 | 0.05 | 0.01 | 0.03 |

(1) 求边缘分布律.
(2) 求 8 月份的订单数为 51 时, 9 月份订单数的条件分布律.

11. 以 $X$ 记某医院一天出生的婴儿的个数, $Y$ 记其中男婴的个数, 设 $X$ 和 $Y$ 的联合分布律为

$$
P \{X = n, Y = m \} = \frac {\mathrm{e} ^ {- 1 4} \times 7 . 1 4 ^ {m} \times 6 . 8 6 ^ {n - m}}{m ! (n - m) !},
$$

$$
m = 0, 1, 2, \dots , n; \quad n = 0, 1, 2, \dots .
$$

(1) 求边缘分布律.
(2) 求条件分布律.
(3) 特别, 写出当 X=20 时, Y 的条件分布律.

12. 求 §1 例 1 中的条件分布律: $P\{Y = k \mid X = i\}$.

13. 在第 9 题中:

(1) 求条件概率密度  $f_{X|Y}(x|y)$ ，特别，写出当  $Y=\frac{1}{2}$  时 X 的条件概率密度.
(2) 求条件概率密度  $f_{Y|X}(y|x)$ ，特别，分别写出当  $X=\frac{1}{3}$ ， $X=\frac{1}{2}$  时 Y 的条件概率密度.

(3) 求条件概率

$$
P \left\{Y \geqslant \frac {1}{4}   \Big |   X = \frac {1}{2} \right\}, \quad P \left\{Y \geqslant \frac {3}{4}   \Big |   X = \frac {1}{2} \right\}.
$$

14. 设随机变量 $(X, Y)$ 的概率密度为

$$
f (x, y) = \left\{ \begin{array}{l l} 1, & | y | <   x, 0 <   x <   1, \\ 0, & \text {其他}. \end{array} \right.
$$

求条件概率密度 $f_{Y|X}(y|x), f_{X|Y}(x|y)$.

15. 设随机变量 $X \sim U(0,1)$，当给定 $X = x$ 时，随机变量 $Y$ 的条件概率密度为

$$
f _ {Y \mid X} (y \mid x) = \left\{ \begin{array}{l l} x, & 0 <   y <   \frac {1}{x}, \\ 0, & \text {其他}. \end{array} \right.
$$

(1) 求 X 和 Y 的联合概率密度  $f(x, y)$ .
(2) 求边缘概率密度  $f_{Y}(y)$ ，并画出它的图形.
(3) 求  $P\{X > Y\}$ .

16.（1）问第1题中的随机变量 $X$ 和 $Y$ 是否相互独立？

(2) 问第 14 题中的随机变量 X 和 Y 是否相互独立(需说明理由)?

17.（1）设随机变量 $(X,Y)$ 具有分布函数

$$
F (x, y) = \left\{ \begin{array}{l l} (1 - \mathrm{e} ^ {- \alpha x}) y, & x \geqslant 0, 0 \leqslant y \leqslant 1, \\ 1 - \mathrm{e} ^ {- \alpha x}, & x \geqslant 0, y > 1, \\ 0, & \text {其他.} \end{array} \quad \alpha > 0, \right.
$$

证明 X, Y 相互独立.

(2) 设随机变量 $(X,Y)$ 具有分布律

$$
P \{X = x, Y = y \} = p ^ {2} (1 - p) ^ {x + y - 2}, \quad 0 <   p <   1, x, y \text {均为正整数，}
$$

问 X, Y 是否相互独立？

18. 设 $X$ 和 $Y$ 是两个相互独立的随机变量, $X$ 在区间 $(0,1)$ 上服从均匀分布, $Y$ 的概率密度为

$$
f _ {Y} (y) = \left\{ \begin{array}{l l} \frac {1}{2} \mathrm{e} ^ {- y / 2}, & y > 0, \\ 0, & y \leqslant 0. \end{array} \right.
$$

(1) 求 X 和 Y 的联合概率密度.
(2) 设含有 a 的二次方程为  $a^{2} + 2Xa + Y = 0$ ，试求 a 有实根的概率.

19. 进行打靶, 设弹着点 $A(X, Y)$ 的坐标 $X$ 和 $Y$ 相互独立, 且都服从 $N(0, 1)$ 分布, 规定

点 A 落在区域  $D_{1}=\{(x,y)\mid x^{2}+y^{2}\leqslant1\}$  得 2 分；

点 A 落在  $D_{2} = \{(x, y) \mid 1 < x^{2} + y^{2} \leqslant 4\}$  得 1 分；

点 A 落在  $D_{3} = \{(x, y) \mid x^{2} + y^{2} > 4\}$  得 0 分.

以 $Z$ 记打靶的得分. 写出 $X, Y$ 的联合概率密度, 并求 $Z$ 的分布律.

20. 设 $X$ 和 $Y$ 是相互独立的随机变量, 其概率密度分别为

$$
f _ {X} (x) = \left\{ \begin{array}{l l} \lambda \mathrm{e} ^ {- \lambda x}, & x > 0, \\ 0, & x \leqslant 0, \end{array} \right. f _ {Y} (y) = \left\{ \begin{array}{l l} \mu \mathrm{e} ^ {- \mu y}, & y > 0, \\ 0, & y \leqslant 0, \end{array} \right.
$$

其中 $\lambda > 0, \mu > 0$ 是常数. 引入随机变量

$$
Z = \left\{ \begin{array}{l l} 1, & \text {当} X \leqslant Y, \\ 0, & \text {当} X > Y. \end{array} \right.
$$

(1) 求条件概率密度  $f_{X|Y}(x|y)$ .
(2) 求 Z 的分布律和分布函数.

21. 设随机变量 $(X, Y)$ 的概率密度为

$$
f (x, y) = \left\{ \begin{array}{l l} x + y, & 0 <   x <   1, 0 <   y <   1, \\ 0, & \text {其他.} \end{array} \right.
$$

分别求(1) $Z=X+Y$ ,(2)Z=XY的概率密度.

22. 设 $X$ 和 $Y$ 是两个相互独立的随机变量, 其概率密度分别为

$$
f _ {X} (x) = \left\{ \begin{array}{l l} 1, & 0 \leqslant x \leqslant 1, \\ 0, & \text {其他}, \end{array} \quad f _ {Y} (y) = \left\{ \begin{array}{l l} \mathrm{e} ^ {- y}, & y > 0, \\ 0, & \text {其他}. \end{array} \right. \right.
$$

求随机变量 $Z = X + Y$ 的概率密度.

23. 某种商品一周的需求量是一个随机变量,其概率密度为

$$
f (t) = \left\{ \begin{array}{l l} t \mathrm{e} ^ {- t}, & t > 0, \\ 0, & t \leqslant 0. \end{array} \right.
$$

设各周的需求量是相互独立的. 求(1) 两周,(2) 三周的需求量的概率密度.

24. 设随机变量 $(X, Y)$ 的概率密度为

$$
f (x, y) = \left\{ \begin{array}{l l} \frac {1}{2} (x + y) \mathrm{e} ^ {- (x + y)}, & x > 0, y > 0, \\ 0, & \text {其他.} \end{array} \right.
$$

(1) 问 X 和 Y 是否相互独立?
(2) 求  $Z = X + Y$  的概率密度.

25. 设随机变量 $X, Y$ 相互独立，且具有相同的分布，它们的概率密度均为

$$
f (x) = \left\{ \begin{array}{l l} \mathrm{e} ^ {1 - x}, & x > 1, \\ 0, & \text {其他}. \end{array} \right.
$$

求 $Z = X + Y$ 的概率密度.

26. 设随机变量 $X, Y$ 相互独立，它们的概率密度均为

$$
f (x) = \left\{ \begin{array}{l l} {\mathrm{e} ^ {- x},} & {x > 0,} \\ {0,} & {\text {其他}.} \end{array} \right.
$$

求 $Z = Y / X$ 的概率密度.

27. 设随机变量 $X, Y$ 相互独立，它们都在区间 $(0,1)$ 上服从均匀分布。$A$ 是以 $X, Y$ 为边长的矩形的面积，求 $A$ 的概率密度。
28. 设 $X, Y$ 是相互独立的随机变量，它们都服从正态分布 $N(0, \sigma^2)$. 试验证随机变量 $Z = \sqrt{X^2 + Y^2}$ 的概率密度为

$$
f _ {Z} (z) = \left\{ \begin{array}{l l} \frac {z}{\sigma^ {2}} \mathrm{e} ^ {- z ^ {2} / (2 \sigma^ {2})}, & z > 0, \\ 0, & \text {其他.} \end{array} \right.
$$

我们称 $Z$ 服从参数为 $\sigma (\sigma >0)$ 的瑞利(Rayleigh)分布.

29. 设随机变量 $(X, Y)$ 的概率密度为

$$
f (x, y) = \left\{ \begin{array}{l l} b \mathrm{e} ^ {- (x + y)}, & 0 <   x <   1, 0 <   y <   \infty , \\ 0, & \text {其他}. \end{array} \right.
$$

(1) 试确定常数 b.

(2) 求边缘概率密度  $f_{X}(x)$ ,  $f_{Y}(y)$ .

(3) 求函数  $U = \max\{X, Y\}$  的分布函数.

30. 设某种型号的电子元件的寿命(以 h 计)近似地服从正态分布  $N(160,20^{2})$ ，随机地选取 4 只，求其中没有一只寿命小于 180 的概率.

31. 对某种电子装置的输出测量了 5 次, 得到结果为 $X_{1}, X_{2}, X_{3}, X_{4}, X_{5}$. 设它们是相互独立的随机变量且都服从参数 $\sigma = 2$ 的瑞利分布.

(1) 求  $Z=\max\{X_{1}, X_{2}, X_{3}, X_{4}, X_{5}\}$  的分布函数.

(2) 求  $P\{Z>4\}$ .

32. 设随机变量 $X, Y$ 相互独立，且服从同一分布，试证明

$$
P \{a <   \min \{X, Y \} \leqslant b \} = (P \{X > a \}) ^ {2} - (P \{X > b \}) ^ {2} \quad (a \leqslant b).
$$

33. 设 $X, Y$ 是相互独立的随机变量, 其分布律分别为

$$
P \{X = k \} = p (k), \quad k = 0, 1, 2, \dots ,
$$

$$
P \{Y = r \} = q (r), \quad r = 0, 1, 2, \dots .
$$

证明随机变量 $Z = X + Y$ 的分布律为

$$
P \{Z = i \} = \sum_ {k = 0} ^ {i} p (k) q (i - k), \quad i = 0, 1, 2, \dots .
$$

34. 设 $X, Y$ 是相互独立的随机变量，$X \sim \pi(\lambda_1), Y \sim \pi(\lambda_2)$. 证明 $Z = X + Y \sim \pi(\lambda_1 + \lambda_2)$.

35. 设 $X, Y$ 是相互独立的随机变量，$X \sim b(n_1, p), Y \sim b(n_2, p)$. 证明

$$
Z = X + Y \sim b (n _ {1} + n _ {2}, p).
$$

36. 设随机变量 $(X, Y)$ 的分布律为

| Y\\X | 0 | 1 | 2 | 3 | 4 | 5 |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 0.00 | 0.01 | 0.03 | 0.05 | 0.07 | 0.09 |
| 1 | 0.01 | 0.02 | 0.04 | 0.05 | 0.06 | 0.08 |
| 2 | 0.01 | 0.03 | 0.05 | 0.05 | 0.05 | 0.06 |
| 3 | 0.01 | 0.02 | 0.04 | 0.06 | 0.06 | 0.05 |

(1) 求  $P\{X=2 \mid Y=2\}$ ,  $P\{Y=3 \mid X=0\}$ .
(2) 求  $V = \max\{X, Y\}$  的分布律.
(3) 求  $U = \min\{X, Y\}$  的分布律.
(4) 求  $W = X + Y$  的分布律.

## 第四章 随机变量的数字特征

上一章介绍了随机变量的分布函数、概率密度和分布律，它们都能完整地描述随机变量，但在某些实际或理论问题中，人们感兴趣于某些能描述随机变量某一种特征的常数。例如，一篮球队上场比赛的运动员的身高是一个随机变量，人们常关心上场运动员的平均身高。一个城市一户家庭拥有汽车的辆数是一个随机变量，在考察城市的交通情况时，人们关心户均拥有汽车的辆数。评价棉花的质量时，既需要注意纤维的平均长度，又需要注意纤维长度与平均长度的偏离程度，平均长度较大，偏离程度较小，质量就较好。这种由随机变量的分布所确定的，能刻画随机变量某一方面的特征的常数统称为数字特征，它在理论和实际应用中都很重要。本章将介绍几个重要的数字特征:数学期望、方差、相关系数和矩。

## § 1 数学期望

先看一个例子. 一射手进行打靶练习, 规定射入区域 $e_2$ (图4-1) 得 2 分; 射入区域 $e_1$ 得 1 分; 脱靶, 即射入区域 $e_0$, 得 0 分. 射手一次射击所得分数 $X$ 是一个随机变量. 设 $X$ 的分布律为

$$
P \{X = k \} = p _ {k}, \quad k = 0, 1, 2.
$$

现在射击 $N$ 次，其中得0分的有 $a_0$ 次，得1分的有 $a_1$ 次，得2分的有 $a_2$ 次，$a_0 + a_1 + a_2 = N$. 他射击 $N$ 次得分的总和为 $a_0 \times 0 + a_1 \times 1 + a_2 \times 2$. 于是平均一次射击的得分数为

$$
\frac {a _ {0} \times 0 + a _ {1} \times 1 + a _ {2} \times 2}{N} = \sum_ {k = 0} ^ {2} k \frac {a _ {k}}{N}.
$$

![](images/page_105_image_7.jpg)

<details>
<summary>text_image</summary>

e₂
e₁
e₀
</details>

图4-1

这里， $a_{k} / N$ 是事件 $\{X = k\}$ 的频率.在第五章将会讲到，当 $N$ 很大时， $a_{k} / N$ 在一定意义下接近于事件 $\{X = k\}$ 的概率 $p_k$ .就是说，在试验次数很大时，随机变量$X$ 的观察值的算术平均 $\sum_{k = 0}^{2}k\frac{a_k}{N}$ 在一定意义下接近于 $\sum_{k = 0}^{2}kp_k.$ 我们称 $\sum_{k = 0}^{2}kp_k$ 为随机变量 $X$ 的数学期望或均值.一般，有以下的定义.

定义 设离散型随机变量 $X$ 的分布律为

$$
P \{X = x _ {k} \} = p _ {k}, \quad k = 1, 2, \dots .
$$

若级数

$$
\sum_ {k = 1} ^ {\infty} x _ {k} p _ {k}
$$

绝对收敛,则称级数  $\sum_{k=1}^{\infty}x_{k}p_{k}$  的和为随机变量 X 的数学期望,记为  $E(X)$ . 即

$$
E (X) = \sum_ {k = 1} ^ {\infty} x _ {k} p _ {k}. \tag {1.1}
$$

设连续型随机变量 $X$ 的概率密度为 $f(x)$，若积分

$$
\int_ {- \infty} ^ {\infty} x f (x) \mathrm{d} x
$$

绝对收敛,则称积分 $\int_{-\infty}^{\infty}xf(x)\mathrm{d}x$ 的值为随机变量X的数学期望,记为 $E(X)$ .即

$$
E (X) = \int_ {- \infty} ^ {\infty} x f (x) \mathrm{d} x. \tag {1.2}
$$

数学期望简称期望,又称为均值.

数学期望 $E(X)$ 完全由随机变量 $X$ 的概率分布所确定.若 $X$ 服从某一分布，也称 $E(X)$ 是这一分布的数学期望.

例1 某医院当新生儿诞生时,医生要根据婴儿的皮肤颜色、肌肉弹性、反应的敏感性、心脏的搏动等方面的情况进行评分,新生儿的得分 $X$ 是一个随机变量.据以往的资料表明 $X$ 的分布律为

| X | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| $p_k$ | 0.002 | 0.001 | 0.002 | 0.005 | 0.02 | 0.04 | 0.18 | 0.37 | 0.25 | 0.12 | 0.01 |

试求 $X$ 的数学期望 $E(X)$.

$$
\begin{array}{l} + 5 \times 0. 0 4 + 6 \times 0. 1 8 + 7 \times 0. 3 7 + 8 \times 0. 2 5 + 9 \times 0. 1 2 + 1 0 \times 0. 0 1 \\ = 7. 1 5 (\text {分}). \\ \end{array}
$$

解 $E(X) = 0 \times 0.002 + 1 \times 0.001 + 2 \times 0.002 + 3 \times 0.005 + 4 \times 0.02$

这意味着,若考察医院出生的很多新生儿,例如1 000个,则一个新生儿的平均得分约为7.15分,1 000个新生儿共得分约7 150分. □

例2有两个相互独立工作的电子装置，它们的寿命(以h计) $X_{k}(k = 1,2)$ 服从同一指数分布，其概率密度为

$$
f (x) = \left\{ \begin{array}{l l} \frac {1}{\theta} \mathrm{e} ^ {- x / \theta}, & x > 0, \\ 0, & x \leqslant 0, \end{array} \right. \quad \theta > 0.
$$

若将这两个电子装置串联连接组成整机,求整机寿命(以 h 计)N 的数学期望.

解 $X_{k}(k = 1,2)$ 的分布函数为

$$
F (x) = \left\{ \begin{array}{l l} 1 - \mathrm{e} ^ {- x / \theta}, & x > 0, \\ 0, & x \leqslant 0. \end{array} \right.
$$

由第三章 §5 的(5.12)式, $N=\min\{X_{1},X_{2}\}$ 的分布函数为

$$
F _ {\min} (x) = 1 - \left[ 1 - F (x) \right] ^ {2} = \left\{ \begin{array}{l l} 1 - \mathrm{e} ^ {- 2 x / \theta}, & x > 0, \\ 0, & x \leqslant 0, \end{array} \right.
$$

因而 $N$ 的概率密度为

$$
f _ {\min} (x) = \left\{ \begin{array}{l l} \frac {2}{\theta} \mathrm{e} ^ {- 2 x / \theta}, & x > 0, \\ 0, & x \leqslant 0. \end{array} \right.
$$

于是 $N$ 的数学期望为

$$
E (N) = \int_ {- \infty} ^ {\infty} x f _ {\min} (x) \mathrm{d} x = \int_ {0} ^ {\infty} \frac {2 x}{\theta} \mathrm{e} ^ {- 2 x / \theta} \mathrm{d} x = \frac {\theta}{2}.
$$

例 3 按规定, 某车站每天 8:00\~9:00, 9:00\~10:00 都恰有一辆客车到站, 但到站的时刻是随机的, 且两者到站的时间相互独立. 其规律为

<table><tr><td rowspan="2">到站时刻</td><td>8:10</td><td>8:30</td><td>8:50</td></tr><tr><td>9:10</td><td>9:30</td><td>9:50</td></tr><tr><td>概率</td><td> $\frac{1}{6}$ </td><td> $\frac{3}{6}$ </td><td> $\frac{2}{6}$ </td></tr></table>

一旅客 8:20 到车站, 求他候车时间的数学期望.

解 设旅客的候车时间为 $X$ （以 $\min$ 计）. $X$ 的分布律为

| X | 10 | 30 | 50 | 70 | 90 |
| --- | --- | --- | --- | --- | --- |
| $p_k$ | $\frac{3}{6}$ | $\frac{2}{6}$ | $\frac{1}{6} \times \frac{1}{6}$ | $\frac{1}{6} \times \frac{3}{6}$ | $\frac{1}{6} \times \frac{2}{6}$ |

在上表中,例如

$$
P \{X = 7 0 \} = P (A B) = P (A) P (B) = \frac {1}{6} \times \frac {3}{6},
$$

其中 $A$ 为事件“第一班车在8:10到站”，$B$ 为“第二班车在9:30到站”。候车时间的数学期望为

$$
E (X) = 1 0 \times \frac {3}{6} + 3 0 \times \frac {2}{6} + 5 0 \times \frac {1}{3 6} + 7 0 \times \frac {3}{3 6} + 9 0 \times \frac {2}{3 6} = 2 7. 2 2.
$$

例4 某商店对某种家用电器的销售采用先使用后付款的方式. 记使用寿命为 $X$ （以年计），规定:

$X \leqslant 1$ ,一台付款1500元;

$1<X\leqslant2$ ,一台付款2000元;

$2<X\leqslant3$ ,一台付款2500元;

X>3,一台付款3 000元.

设寿命 X 服从指数分布, 概率密度为

$$
f (x) = \left\{ \begin{array}{l l} \frac {1}{1 0} \mathrm{e} ^ {- x / 1 0}, & x > 0, \\ 0, & x \leqslant 0. \end{array} \right.
$$

试求该商店一台这种家用电器收费 $Y$ 的数学期望.

解 先求出寿命 $X$ 落在各个时间区间的概率. 即有

$$
P \{X \leqslant 1 \} = \int_ {0} ^ {1} \frac {1}{1 0} \mathrm{e} ^ {- x / 1 0} \mathrm{d} x = 1 - \mathrm{e} ^ {- 0. 1} = 0. 0 9 5 2,
$$

$$
P \{1 <   X \leqslant 2 \} = \int_ {1} ^ {2} \frac {1}{1 0} \mathrm{e} ^ {- x / 1 0} \mathrm{d} x = \mathrm{e} ^ {- 0. 1} - \mathrm{e} ^ {- 0. 2} = 0. 0 8 6 1,
$$

$$
P \{2 <   X \leqslant 3 \} = \int_ {2} ^ {3} \frac {1}{1 0} \mathrm{e} ^ {- x / 1 0} \mathrm{d} x = \mathrm{e} ^ {- 0. 2} - \mathrm{e} ^ {- 0. 3} = 0. 0 7 7 9,
$$

$$
P \{X > 3 \} = \int_ {3} ^ {\infty} \frac {1}{1 0} \mathrm{e} ^ {- x / 1 0} \mathrm{d} x = \mathrm{e} ^ {- 0. 3} = 0. 7 4 0 8.
$$

一台家用电器收费 $Y$ (以元计)的分布律为

| Y | 1 500 | 2 000 | 2 500 | 3 000 |
| --- | --- | --- | --- | --- |
| $p_k$ | 0.095 2 | 0.086 1 | 0.077 9 | 0.740 8 |

得 $E(Y) = 2732.15$ ，即平均一台收费2732.15元

例5 在一个人数很多的团体中普查某种疾病,为此要抽验 $N$ 个人的血,可以用两种方法进行.(i)将每个人的血分别去验,这就需验 $N$ 次.(ii)按 $k$ 个人一组进行分组,把从 $k$ 个人抽来的血混合在一起进行检验.如果这混合血液呈阴性反应,就说明 $k$ 个人的血都呈阴性反应,这样,这 $k$ 个人的血就只需验一次;若呈阳性,则再对这 $k$ 个人的血液分别进行化验,这样,$k$ 个人的血总共要化验 $k+1$ 次.假设每个人化验呈阳性的概率为 $p$,且这些人的试验反应是相互独立的.试说明当 $p$ 较小时,选取适当的 $k$,按第二种方法可以减少化验的次数.并说明 $k$ 取什么值时最适宜.

解 各人的血呈阴性反应的概率为 $q = 1 - p$. 因而 $k$ 个人的混合血呈阴性反应的概率为 $q^k, k$ 个人的混合血呈阳性反应的概率为 $1 - q^k$.

设以 $k$ 个人为一组时，组内每人化验的次数为 $X$ ，则 $X$ 是一个随机变量，其分布律为

| X | $\frac{1}{k}$ | $\frac{k+1}{k}$ |
| --- | --- | --- |
| $p_k$ | $q^k$ | $1-q^k$ |

$X$ 的数学期望为

$$
E (X) = \frac {1}{k} q ^ {k} + \left(1 + \frac {1}{k}\right) (1 - q ^ {k}) = 1 - q ^ {k} + \frac {1}{k}.
$$

$N$ 个人平均需化验的次数为

$$
N \Big (1 - q ^ {k} + \frac {1}{k} \Big).
$$

由此可知,只要选择 k 使

$$
1 - q ^ {k} + \frac {1}{k} <   1,
$$

则 $N$ 个人平均需化验的次数 $< N$. 当 $p$ 固定时, 我们选取 $k$ 使得

$$
L = 1 - q ^ {k} + \frac {1}{k}
$$

小于1且取到最小值,这时就能得到最好的分组方法.

例如，$p = 0.1$，则 $q = 0.9$，当 $k = 4$ 时，$L = 1 - q^k + \frac{1}{k}$ 取到最小值。此时得到最好的分组方法。若 $N = 1000$，此时以 $k = 4$ 分组，则按第二种方法平均只需化验

$$
1 0 0 0 \left(1 - 0. 9 ^ {4} + \frac {1}{4}\right) = 5 9 4 (\text {次}).
$$

这样平均来说,约可以减少40%的工作量.

例 6 设随机变量  $X \sim \pi(\lambda)$ ，求  $E(X)$ .

解 $X$ 的分布律为

$$
P \{X = k \} = \frac {\lambda^ {k} \mathrm{e} ^ {- \lambda}}{k !}, \quad k = 0, 1, 2, \dots , \quad \lambda > 0.
$$

$X$ 的数学期望为

$$
E (X) = \sum_ {k = 0} ^ {\infty} k \frac {\lambda^ {k} \mathrm{e} ^ {- \lambda}}{k !} = \lambda \mathrm{e} ^ {- \lambda} \sum_ {k = 1} ^ {\infty} \frac {\lambda^ {k - 1}}{(k - 1) !} = \lambda \mathrm{e} ^ {- \lambda} \cdot \mathrm{e} ^ {\lambda} = \lambda ,
$$

即 $E(X) = \lambda$.

例 7 设随机变量  $X \sim U(a, b)$ ，求  $E(X)$ .

解 $X$ 的概率密度为

$$
f (x) = \left\{ \begin{array}{l l} \frac {1}{b - a}, & a <   x <   b \\ 0, & \text {其他}. \end{array} \right.
$$

$X$ 的数学期望为

$$
E (X) = \int_ {- \infty} ^ {\infty} x f (x) \mathrm{d} x = \int_ {a} ^ {b} \frac {x}{b - a} \mathrm{d} x = \frac {a + b}{2}.
$$

即数学期望位于区间 $(a,b)$ 的中点.

我们经常需要求随机变量的函数的数学期望,例如飞机机翼受到压力  $W = kV^{2}$  (V 是风速, k > 0 是常数) 的作用, 需要求 W 的数学期望, 这里 W 是随机变量 V 的函数. 这时, 可以通过下面的定理来求 W 的数学期望.

定理 设 $Y$ 是随机变量 $X$ 的函数: $Y = g(X)$ ($g$ 是连续函数).

(i) 如果 X 是离散型随机变量, 它的分布律为  $P\{X=x_{k}\}=p_{k}, k=1,2,\cdots$ , 若  $\sum_{k=1}^{\infty} g(x_{k}) p_{k}$  绝对收敛, 则有

$$
E (Y) = E [ g (X) ] = \sum_ {k = 1} ^ {\infty} g (x _ {k}) p _ {k}. \tag {1.3}
$$

(ii) 如果 $X$ 是连续型随机变量, 它的概率密度为 $f(x)$, 若 $\int_{-\infty}^{\infty} g(x)f(x) \mathrm{d}x$ 绝对收敛, 则有

$$
E (Y) = E [ g (X) ] = \int_ {- \infty} ^ {\infty} g (x) f (x) \mathrm{d} x. \tag {1.4}
$$

定理的重要意义在于当我们求 $E(Y)$ 时，不必算出 $Y$ 的分布律或概率密度，而只需利用 $X$ 的分布律或概率密度就可以了，定理的证明超出了本书的范围。我们只对下述特殊情况加以证明。

证 设 $X$ 是连续型随机变量, 且 $y = g(x)$ 满足第二章 §5 中定理的条件.

由第二章 §5 中的(5.2)式知道随机变量 $Y = g(X)$ 的概率密度为

$$
f _ {Y} (y) = \left\{ \begin{array}{l l} f _ {X} [ h (y) ] | h ^ {\prime} (y) |, & \alpha <   y <   \beta , \\ 0, & \text {其他}, \end{array} \right.
$$

于是

$$
E (Y) = \int_ {- \infty} ^ {\infty} y f _ {Y} (y) \mathrm{d} y = \int_ {a} ^ {\beta} y f _ {X} [ h (y) ] | h ^ {\prime} (y) | \mathrm{d} y.
$$

当 $h^{\prime}(y)$ 恒 $>0$ 时

$$
E (Y) = \int_ {\alpha} ^ {\beta} y f _ {X} [ h (y) ] h ^ {\prime} (y) \mathrm{d} y = \int_ {- \infty} ^ {\infty} g (x) f (x) \mathrm{d} x.
$$

当 $h^{\prime}(y)$ 恒 $< 0$ 时

$$
\begin{array}{l} E (Y) = - \int_ {\alpha} ^ {\beta} y f _ {X} [ h (y) ] h ^ {\prime} (y) \mathrm{d} y \\ = - \int_ {\infty} ^ {- \infty} g (x) f (x) \mathrm{d} x = \int_ {- \infty} ^ {\infty} g (x) f (x) \mathrm{d} x. \\ \end{array}
$$

综合上两式，(1.4)式得证.

□

上述定理还可以推广到两个或两个以上随机变量的函数的情况.

例如, 设 $Z$ 是随机变量 $X, Y$ 的函数 $Z = g(X, Y)$ ($g$ 是连续函数), 那么, $Z$ 是一个一维随机变量. 若二维随机变量 $(X, Y)$ 的概率密度为 $f(x, y)$, 则有

$$
E (Z) = E [ g (X, Y) ] = \int_ {- \infty} ^ {\infty} \int_ {- \infty} ^ {\infty} g (x, y) f (x, y) \mathrm{d} x \mathrm{d} y, \tag {1.5}
$$

这里设上式右边的积分绝对收敛. 又若 $(X,Y)$ 为离散型随机变量, 其分布律为 $P\{X=x_{i},Y=y_{j}\}=p_{ij},i,j=1,2,\cdots$ , 则有

$$
E (Z) = E [ g (X, Y) ] = \sum_ {j = 1} ^ {\infty} \sum_ {i = 1} ^ {\infty} g (x _ {i}, y _ {j}) p _ {i j}, \tag {1.6}
$$

这里设上式右边的级数绝对收敛.

例 8 设风速 V 在  $(0, a)$  上服从均匀分布, 即具有概率密度

$$
f (v) = \left\{ \begin{array}{l l} { \frac {1}{a},} & {0 <   v <   a,} \\ {0,} & {\text {其他}.} \end{array} \right.
$$

又设飞机机翼受到的正压力 $W$ 是 $V$ 的函数:$W = kV^2 (k > 0, \text{常数})$，求 $W$ 的数学期望.

解 由(1.4)式有

$$
E (W) = \int_ {- \infty} ^ {\infty} k v ^ {2} f (v) \mathrm{d} v = \int_ {0} ^ {a} k v ^ {2} \frac {1}{a} \mathrm{d} v = \frac {1}{3} k a ^ {2}.
$$

例9 设随机变量 $(X,Y)$ 的概率密度

$$
f (x, y) = \left\{ \begin{array}{l l} \frac {3}{2 x ^ {3} y ^ {2}}, & \frac {1}{x} <   y <   x, x > 1, \\ 0, & \text {其他.} \end{array} \right.
$$

求数学期望  $E(Y)$ ,  $E\left(\frac{1}{XY}\right)$ .

解 由(1.5)式得

$$
\begin{array}{l} E (Y) = \int_ {- \infty} ^ {\infty} \int_ {- \infty} ^ {\infty} y f (x, y) \mathrm{d} y \mathrm{d} x = \int_ {1} ^ {\infty} \int_ {\frac {1}{x}} ^ {x} \frac {3}{2 x ^ {3} y} \mathrm{d} y \mathrm{d} x \\ = \frac {3}{2} \int_ {1} ^ {\infty} \frac {1}{x ^ {3}} \left[ \ln y \right] _ {\frac {1}{x}} ^ {x} \mathrm{d} x = 3 \int_ {1} ^ {\infty} \frac {\ln x}{x ^ {3}} \mathrm{d} x \\ = \left[ - \frac {3}{2} \frac {\ln x}{x ^ {2}} \right] _ {1} ^ {\infty} + \frac {3}{2} \int_ {1} ^ {\infty} \frac {1}{x ^ {3}} \mathrm{d} x = \frac {3}{4}. \\ \end{array}
$$

$$
E \left(\frac {1}{X Y}\right) = \int_ {- \infty} ^ {\infty} \int_ {- \infty} ^ {\infty} \frac {1}{x y} f (x, y) \mathrm{d} y \mathrm{d} x = \int_ {1} ^ {\infty} \mathrm{d} x \int_ {\frac {1}{x}} ^ {x} \frac {3}{2 x ^ {4} y ^ {3}} \mathrm{d} y = \frac {3}{5}.
$$

例 10 某公司计划开发一种新产品市场,并试图确定该产品的产量.他们估计出售一件产品可获利 m 元,而积压一件产品将导致 n 元的损失.再者,他们预测销售量 Y(件)服从指数分布,其概率密度为