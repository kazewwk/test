其中 $\theta \in (0,1)$ 因此有(13.4.1)式成立

同理, 由 $\cos^{(n)}(0) = \cos \frac{n\pi}{2}$, 对任意的 $x \in \mathbb{R}$, 其 Taylor 公式中的 Lagrange 余项为

$$
\left| \frac {\cos (\theta x + n \pi)}{(2 n) !} x ^ {2 n} \right| \leqslant \frac {| x | ^ {2 n}}{(2 n) !} \rightarrow 0 \quad (n \rightarrow + \infty),
$$

其中 $\theta \in (0,1)$ 因此有(13.4.2)式成立

对数函数的幂级数展开:用同样的方法，也可以得到前面已经给出的对数函数的Maclaurin展式:

$$
\ln (1 + x) = \sum_ {n = 1} ^ {+ \infty} \frac {(- 1) ^ {n + 1}}{n} x ^ {n}, \quad x \in (- 1, 1).
$$

上述函数的 Taylor 展式的收敛域可以通过单独考虑幂级数在收敛区间端点的敛散性得到, 在此不再赘述. 比如可以证明 $\ln (1 + x)$ 的收敛域为 $(-1,1]$, $\arctan x$ 的收敛域为 $[-1,1]$, $\arcsin x$ 的收敛域为 $[-1,1]$.

更一般函数的 Taylor 展式, 可以通过下一节幂级数之间的代数运算、已知幂级数展开的逐项求导或逐项积分, 再结合幂级数的唯一性的灵活运用得到. 前面提到的等式 (13.2.4), (13.2.5), (13.3.10) 和 (13.3.12) 等, 都是这些方法的灵活应用.

## 13.5 幂级数的代数运算

我们简要讨论一下幂级数间的代数运算. 首先, 关于幂级数的加减, 有下面的结论:

定理 13.5.1 如果幂级数  $\sum_{n=1}^{+\infty}a_{n}x^{n}$  和  $\sum_{n=1}^{+\infty}b_{n}x^{n}$  的收敛半径分别为  $R_{1}$  和  $R_{2}$ ，则幂级数  $\sum_{n=1}^{+\infty}(a_{n}\pm b_{n})x^{n}$  的收敛半径 R 为

(1) 若  $R_{1} \neq R_{2}$ ，则  $R = \min\{R_{1}, R_{2}\}$ .
(2) 若  $R_{1}=R_{2}=R_{0}$ ，则  $R\geqslant R_{0}$ .

不难看出, 在情形 (2), 对于任意的 $\lambda > R_0$, 都可以找到这样的幂级数, 使得两幂级数和形成的幂级数收敛半径为 $\lambda$. 事实上, 只要取 $a_n = -b_n + \frac{1}{\lambda^n}$ 即可.

关于两个幂级数的乘积, 首先, 我们知道, 对于两个给定的幂级数 $\sum_{n=0}^{+\infty} a_n x^n$ 和 $\sum_{n=0}^{+\infty} b_n x^n$, 如果它们的收敛半径均为 $R > 0$, 则当 $|x| < R$ 时, 这两个幂级数都绝对收敛, 因此它们

的乘积都等于它们的 Cauchy 乘积, 即

$$
\left(\sum_ {n = 0} ^ {+ \infty} a _ {n} x ^ {n}\right) \left(\sum_ {n = 0} ^ {+ \infty} b _ {n} x ^ {n}\right) = \sum_ {n = 0} ^ {+ \infty} c _ {n} x ^ {n},
$$

其中  $c_{n}=\sum_{i=0}^{n}a_{i}b_{n-i}\ (n=0,1,2,\cdots)$ . 即有下面的结论:

定理 13.5.2 设幂级数  $\sum_{n=0}^{+\infty}a_{n}x^{n}$  和  $\sum_{n=0}^{+\infty}b_{n}x^{n}$  的收敛半径都是 R, 那么当  $x \in (-R, R)$  时, 有

$$
\left(\sum_ {n = 0} ^ {+ \infty} a _ {n} x ^ {n}\right) \left(\sum_ {n = 0} ^ {+ \infty} b _ {n} x ^ {n}\right) = \sum_ {n = 0} ^ {+ \infty} c _ {n} x ^ {n},
$$

其中  $c_{n}=\sum_{i=0}^{n}a_{i}b_{n-i}\ (n=0,1,2,\cdots)$ .

我们再从幂级数的角度重新考虑一下 Abel 定理 11.4.11.

定理 13.5.3 (Abel 定理) 设  $\sum_{n=0}^{+\infty}a_{n}=A$  和  $\sum_{n=0}^{+\infty}b_{n}=B$  均为收敛级数, 如果它们的 Cauchy 乘积级数  $\sum_{n=0}^{+\infty}c_{n}=C$  也收敛, 其中  $c_{n}=a_{0}b_{n}+a_{1}b_{n-1}+\cdots+a_{n}b_{0}$ , 则成立

$$
C = A B.
$$

证明 根据假设, 级数

$$
\sum_ {n = 0} ^ {+ \infty} a _ {n} x ^ {n}, \quad \sum_ {n = 0} ^ {+ \infty} b _ {n} x ^ {n}, \quad \sum_ {n = 0} ^ {+ \infty} c _ {n} x ^ {n}
$$

的收敛半径都不小于1, 因此当  $|x| < 1$  时, 成立

$$
\left(\sum_ {n = 0} ^ {+ \infty} a _ {n} x ^ {n}\right) \left(\sum_ {n = 0} ^ {+ \infty} b _ {n} x ^ {n}\right) = \sum_ {n = 0} ^ {+ \infty} c _ {n} x ^ {n}.
$$

在上式两端取 $x \to 1^{-}$ 的极限, 根据Abel第二定理知定理成立.

例 13.5.1 假设幂级数  $\sum_{n=0}^{+\infty}a_{n}x^{n}$  的收敛半径为 1, 考虑它与幂级数  $\sum_{n=0}^{+\infty}x^{n}$  的乘积. 因为两者有相同的收敛半径, 根据上述定理, 有

$$
\left(\sum_ {n = 0} ^ {+ \infty} x ^ {n}\right) \left(\sum_ {n = 0} ^ {+ \infty} a _ {n} x ^ {n}\right) = \sum_ {n = 0} ^ {+ \infty} S _ {n} x ^ {n},
$$

其中  $S_{n}=a_{0}+a_{1}+\cdots+a_{n}(n=0,1,2,\cdots)$ . 即

$$
\frac {1}{1 - x} \cdot \left(\sum_ {n = 0} ^ {+ \infty} a _ {n} x ^ {n}\right) = \sum_ {n = 0} ^ {+ \infty} S _ {n} x ^ {n}.
$$

如果再进行一次上式操作过程, 可得

$$
\frac {1}{(1 - x) ^ {2}} \cdot \left(\sum_ {n = 0} ^ {+ \infty} a _ {n} x ^ {n}\right) = \sum_ {n = 0} ^ {+ \infty} T _ {n} x ^ {n},
$$

其中  $T_{n}=S_{0}+S_{1}+\cdots+S_{n}(n=0,1,2,\cdots)$ .

例 13.5.2 设  $r \in (-1,1)$ ,  $x \in R$ , 求下面级数的和:

$$
1 + \sum_ {n = 1} ^ {+ \infty} r ^ {n} \cos n x.
$$

解 我们计算级数的乘积:

$$
\begin{array}{l} \left(1 - 2 r \cos x + r ^ {2}\right) \left(1 + \sum_ {n = 1} ^ {+ \infty} r ^ {n} \cos n x\right) \\ = 1 - 2 r \cos x + r ^ {2} + \sum_ {n = 1} ^ {+ \infty} r ^ {n} \cos n x - 2 r \sum_ {n = 1} ^ {+ \infty} r ^ {n} \cos x \cos n x + \sum_ {n = 1} ^ {+ \infty} r ^ {n + 2} \cos n x \\ = 1 - 2 r \cos x + r ^ {2} + \sum_ {n = 1} ^ {+ \infty} r ^ {n} \cos n x - r \sum_ {n = 1} ^ {+ \infty} r ^ {n} (\cos (n - 1) x + \cos (n + 1) x) + \\ \sum_ {n = 1} ^ {+ \infty} r ^ {n + 2} \cos n x \\ = 1 - r \cos x. \\ \end{array}
$$

由此可得等式

$$
\frac {1 - r \cos x}{1 - 2 r \cos x + r ^ {2}} = 1 + \sum_ {n = 1} ^ {+ \infty} r ^ {n} \cos n x, \quad r \in (- 1, 1). \tag {13.5.1}
$$

将上式中右端的 1 移到左端, 两边除以 $r$, 再关于 $r$ 逐项积分, 得

$$
\ln (1 - 2 r \cos x + r ^ {2}) = - 2 \sum_ {n = 1} ^ {+ \infty} \frac {r ^ {n}}{n} \cos n x, r \in (- 1, 1). \tag {13.5.2}
$$

上式两端关于 x 积分, 则得如下 Dini 积分:

$$
\int_ {0} ^ {\pi} \ln (1 - 2 r \cos x + r ^ {2}) \mathrm{d} x = 0, | r | <   1. \tag {13.5.3}
$$

□

下面我们考虑幂级数的除法运算, 它可以看成是乘法运算的逆运算.

定理 13.5.4 设幂级数  $\sum_{n=0}^{+\infty}a_{n}x^{n}$  在区间  $(-R,R)$  中收敛,  $a_{0}\neq0$ . 则存在 r>0,
使得幂级数  $\sum_{n=0}^{+\infty}b_{n}x^{n}$  在  $(-r,r)$  中收敛, 且

$$
\left(\sum_ {n = 0} ^ {+ \infty} a _ {n} x ^ {n}\right) \left(\sum_ {n = 0} ^ {+ \infty} b _ {n} x ^ {n}\right) \equiv 1, \forall x \in (- r, r).
$$

证明 不妨设  $a_{0}=1$ . 递归定义  $b_{n}$  如下: 令  $b_{0}=1$ ,

$$
b _ {n} = - \sum_ {i = 0} ^ {n - 1} a _ {n - i} b _ {i}, n \geqslant 1.
$$

我们先证明幂级数 $\sum_{n=0}^{+\infty} b_n x^n$ 具有正的收敛半径. 事实上, 因为 $\sum_{n=0}^{+\infty} a_n x^n$ 在 $(-R, R)$ 中收敛, 故存在 $M > 0$, 使得 $\left|a_n \left(\frac{R}{2}\right)^n \right| \leqslant M$. 因此有

$$
\left| b _ {n} \left(\frac {R}{2}\right) ^ {n} \right| \leqslant \sum_ {i = 0} ^ {n - 1} \left| a _ {n - i} \left(\frac {R}{2}\right) ^ {n - i} \right| \left| b _ {i} \left(\frac {R}{2}\right) ^ {i} \right| \leqslant M \sum_ {i = 0} ^ {n - 1} \left| b _ {i} \left(\frac {R}{2}\right) ^ {i} \right|.
$$

由数学归纳法不难得到

$$
\left| b _ {n} \left(\frac {R}{2}\right) ^ {n} \right| \leqslant (1 + M) ^ {n}, \forall n \geqslant 0.
$$

故幂级数 $\sum_{n=0}^{+\infty} b_n x^n$ 的收敛半径至少为 $r = \frac{R}{2(1 + M)}$. 根据 $\{b_n\}$ 的构造, 显然有

$$
\left(\sum_ {n = 0} ^ {+ \infty} a _ {n} x ^ {n}\right) \left(\sum_ {n = 0} ^ {+ \infty} b _ {n} x ^ {n}\right) = \sum_ {n = 0} ^ {+ \infty} \left(\sum_ {i + j = n} a _ {i} b _ {j}\right) x ^ {n} = 1.
$$

例 13.5.3 试研究函数  $\frac{1}{1+x+x^{2}+\cdots+x^{m-1}}\quad(m>1)$  的 Maclaurin 级数展开.
解 直接计算可得

$$
\frac {1}{1 + x + x ^ {2} + \cdots + x ^ {m - 1}} = (1 - x) \sum_ {n = 0} ^ {+ \infty} x ^ {m n} = \sum_ {n = 0} ^ {+ \infty} x ^ {m n} - \sum_ {n = 0} ^ {+ \infty} x ^ {m n + 1}, \quad x \in (- 1, 1).
$$

例 13.5.4 试研究函数  $\frac{x}{e^{x}-1}$  在 x=0 处的幂级数展开.

解记

$$
\frac {x}{\mathrm{e} ^ {x} - 1} = \sum_ {n = 0} ^ {+ \infty} \frac {B _ {n}}{n !} x ^ {n}, \tag {13.5.4}
$$

其系数 $B_{n}$ 称为第 $n$ 个Bernoulli数. 我们有

$$
\begin{array}{l} \frac {x}{\mathrm{e} ^ {x} - 1} = \left(\frac {\mathrm{e} ^ {x} - 1}{x}\right) ^ {- 1} = \left(\sum_ {n = 0} ^ {+ \infty} \frac {x ^ {n}}{(n + 1) !}\right) ^ {- 1} \\ = 1 - \frac {x}{2} + \frac {x ^ {2}}{1 2} - \frac {x ^ {4}}{7 2 0} + \frac {x ^ {6}}{3 0 2 4 0} - \frac {x ^ {8}}{1 2 0 9 6 0 0} + \dots . \\ \end{array}
$$

注意到上式中 $B_{1} = -\frac{1}{2}$, 当 $n \geqslant 1$ 时 $B_{2n+1} = 0$, 这是因为

$$
\frac {x}{\mathrm{e} ^ {x} - 1} + \frac {x}{2} = \frac {x}{2} \frac {\mathrm{e} ^ {x} + 1}{\mathrm{e} ^ {x} - 1} = \frac {x}{2} \coth \frac {x}{2}, \tag {13.5.5}
$$

即  $\frac{x}{\mathrm{e}^{x}-1}+\frac{x}{2}$  为偶函数的缘故.

根据幂级数的除法公式, 我们容易得到  $B_{n}$  的如下递推公式:

$$
B _ {0} = 1, B _ {n} = - \frac {1}{n + 1} \sum_ {k = 0} ^ {n - 1} \mathrm{C} _ {n + 1} ^ {k} B _ {k}.
$$

例如, 开头的几个 Bernoulli 数 $^{①}$ 为

$$
B _ {0} = 1, \quad B _ {1} = - \frac {1}{2}, \quad B _ {2} = \frac {1}{6}, \quad B _ {3, 5, 7} = 0, \quad B _ {4} = - \frac {1}{3 0}, \quad B _ {6} = \frac {1}{4 2}, \quad B _ {8} = - \frac {1}{3 0}. \quad \square
$$

例13.5.5 设

$$
f (x) = \frac {x}{1} + \frac {x ^ {3}}{1 \times 3} + \frac {x ^ {5}}{1 \times 3 \times 5} + \dots + \frac {x ^ {2 n + 1}}{(2 n + 1) ! !} + \dots , \tag {13.5.6}
$$

以及

$$
g (x) = 1 + \frac {x ^ {2}}{2} + \frac {x ^ {4}}{2 \times 4} + \dots + \frac {x ^ {2 n}}{(2 n) ! !} + \dots . \tag {13.5.7}
$$

证明: 上述两个幂级数的比值满足

$$
\frac {f (x)}{g (x)} = \sum_ {n = 0} ^ {+ \infty} (- 1) ^ {n} \frac {x ^ {2 n + 1}}{(2 n) ! ! (2 n + 1)}. \tag {13.5.8}
$$

证明 容易看出, $g(x) = \mathrm{e}^{x^2 / 2}$, 同时还有 (13.5.8) 式右边的级数

$$
\sum_ {n = 0} ^ {+ \infty} (- 1) ^ {n} \frac {x ^ {2 n + 1}}{(2 n) ! ! (2 n + 1)} = \sum_ {n = 0} ^ {+ \infty} \int_ {0} ^ {x} \frac {1}{n !} \left(\frac {- t ^ {2}}{2}\right) ^ {n} \mathrm{d} t = \int_ {0} ^ {x} \mathrm{e} ^ {- t ^ {2} / 2} \mathrm{d} t.
$$

因此，只需证明

$$
f (x) = g (x) \int_ {0} ^ {x} \mathrm{e} ^ {- t ^ {2} / 2} \mathrm{d} t = \mathrm{e} ^ {x ^ {2} / 2} \int_ {0} ^ {x} \mathrm{e} ^ {- t ^ {2} / 2} \mathrm{d} t
$$

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">① 这样定义的 Bernoulli 数称为第一 Bernoulli 数, 此时  $B_{1} = -\frac{1}{2}$ . 当定义  $B_{1} = \frac{1}{2}$ , 其他  $B_{k}$  不变时, 称为第二 Bernoulli 数, 第二 Bernoulli 数可通过考虑函数  $\frac{x e^{x}}{e^{x} - 1}$  的幂级数展开得到.</span></small>

即可. 记 $h(x) = \mathrm{e}^{x^2 / 2}\int_0^x\mathrm{e}^{-t^2 / 2}\mathrm{d}t.$ 事实上，一方面由(13.5.6)式逐项求导，容易看出

$$
f ^ {\prime} (x) = 1 + x f (x).
$$

另一方面，

$$
h ^ {\prime} (x) = \frac {\mathrm{d}}{\mathrm{d} x} \Big (\mathrm{e} ^ {x ^ {2} / 2} \int_ {0} ^ {x} \mathrm{e} ^ {- t ^ {2} / 2} \mathrm{d} t \Big) = 1 + x \mathrm{e} ^ {x ^ {2} / 2} \int_ {0} ^ {x} \mathrm{e} ^ {- t ^ {2} / 2} \mathrm{d} t = 1 + x h (x).
$$

所以，我们看到 $f(x)$ 和 $h(x)$ 满足相同的微分方程关系式 $y' = 1 + xy$ ，并且两者还都满足 $f(0) = 0$ 和 $h(0) = 0$ 因此 $f(x) \equiv h(x)^{\text{①}}$ □

幂级数之间还可以做代入运算, 或者称之为幂级数的复合运算, 即把一个幂级数代入到另一个幂级数. 限于篇幅, 我们在此不再铺开讨论.

下面的例子说明: 光滑函数的 Taylor 展开的系数可以为任意实数列.

例 13.5.6 对于任意给定的数列  $\{a_{n}\}$ ，都可以构造一个光滑函数  $f(x)$ ，使得该函数在 x=0 处的 Maclaurin 级数的系数恰好满足  $f^{(n)}(0)=a_{n}, n=0,1,2,\cdots$ .

解 设 $\varphi \in C^{\infty}(\mathbb{R})$ 满足

$$
\varphi (x) = \left\{ \begin{array}{l l} 1, & | x | \leqslant \frac {1}{4}, \\ 0, & | x | \geqslant \frac {1}{2}. \end{array} \right.
$$

对于实数列  $a_{0}, a_{1}, a_{2}, \cdots$ ，定义

$$
f (x) = \sum_ {n = 0} ^ {+ \infty} \frac {a _ {n}}{n !} \varphi (a _ {n} x) x ^ {n}, \quad \forall   x \in \mathbb {R}.
$$

可以证明 $f \in C^{\infty}(\mathbb{R})$，且 $f^{(n)}(0) = a_n, \forall n \geqslant 0$.

事实上, 因为 $x^{k+1}\varphi^{(k)}(x) \in C^{\infty}(\mathbb{R})$ 且仅在有界集上非零. 因此, 它们在 $\mathbb{R}$ 上都是有界的. 设

$$
\sup _ {x \in \mathbb {R}} | x ^ {k + 1} \varphi^ {(k)} (x) | \leqslant M _ {k}, \quad k = 0, 1, 2, \dots .
$$

则

$$
\left| \frac {a _ {n}}{n !} \varphi (a _ {n} x) x ^ {n} \right| \leqslant \frac {M _ {0} | x | ^ {n - 1}}{n !}, \quad \forall n \geqslant 1, x \in \mathbb {R}.
$$

因此, 级数 $\sum_{n=0}^{+\infty} \frac{a_n}{n!} \varphi(a_n x) x^n$ 在 $\mathbb{R}$ 上内闭一致收敛. 进而可得 $f(x)$ 连续. 从而

$$
f (0) = \sum_ {n = 0} ^ {+ \infty} \frac {a _ {n}}{n !} \varphi (a _ {n} x) x ^ {n} \Big | _ {x = 0} = a _ {0}.
$$

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">① 这里我们利用了常微分方程的一个基本结论:一阶线性微分方程初值问题的解是存在唯一的。读者也可以直接证明两者相等。</span></small>

现考虑级数 $\sum_{n=0}^{+\infty} \frac{a_n}{n!} \varphi(a_n x) x^n$ 形式求导后的级数

$$
a _ {0} ^ {2} \varphi^ {\prime} (a _ {0} x) + \sum_ {n = 1} ^ {+ \infty} \frac {1}{n !} \Big (a _ {n} ^ {2} \varphi^ {\prime} (a _ {n} x) x ^ {n} + n a _ {n} \varphi (a _ {n} x) x ^ {n - 1} \Big).
$$

由于

$$
\left| \frac {1}{n !} \Big (a _ {n} ^ {2} \varphi^ {\prime} (a _ {n} x) x ^ {n} + n a _ {n} \varphi (a _ {n} x) x ^ {n - 1} \Big) \right| \leqslant \frac {1}{n !} \big (M _ {1} + n M _ {0} \big) | x | ^ {n - 2}, \quad \forall   n \geqslant 2,
$$

可知

$$
a _ {0} ^ {2} \varphi^ {\prime} (a _ {0} x) + \sum_ {n = 1} ^ {+ \infty} \frac {1}{n !} \Big (a _ {n} ^ {2} \varphi^ {\prime} (a _ {n} x) x ^ {n} + n a _ {n} \varphi (a _ {n} x) x ^ {n - 1} \Big)
$$

在 $\mathbb{R}$ 上内闭一致收敛. 从而 $f(x)$ 连续可导且导数可以通过对 $\sum_{n=0}^{+\infty} \frac{a_n}{n!} \varphi(a_n x) x^n$ 逐项求导得到. 一般地, 可以证明 $f(x)$ 任意次可导, 且各阶导数可以通过对 $\sum_{n=0}^{+\infty} \frac{a_n}{n!} \varphi(a_n x) x^n$ 逐项求导得到. 因此,

$$
\begin{array}{l} f ^ {(n)} (0) = \sum_ {k = 0} ^ {+ \infty} \left(\frac {a _ {k}}{k !} \varphi (a _ {k} x) x ^ {k}\right) ^ {(n)} \bigg | _ {x = 0} = \sum_ {k = 0} ^ {n} \left(\frac {a _ {k}}{k !} \varphi (a _ {k} x) x ^ {k}\right) ^ {(n)} \bigg | _ {x = 0} \\ = \sum_ {k = 0} ^ {n} \frac {a _ {k}}{k !} \sum_ {i = 1} ^ {n} \mathrm{C} _ {n} ^ {i} (\varphi (a _ {k} x)) ^ {(i)} (x ^ {k}) ^ {(n - i)} \Bigg | _ {x = 0} \\ = \sum_ {k = 0} ^ {n} \frac {a _ {k}}{k !} \mathrm{C} _ {n} ^ {n - k} k! a _ {k} ^ {n - k} \varphi^ {(n - k)} (0) \\ = \sum_ {k = 0} ^ {n} C _ {n} ^ {n - k} a _ {k} ^ {n + 1 - k} \varphi^ {(n - k)} (0) \\ = \mathrm{C} _ {n} ^ {0} a _ {n} \varphi^ {(0)} (0) = a _ {n}, \quad \forall n \in \mathbb {N}. \\ \end{array}
$$

我们上面看到, 的确存在无穷光滑的函数, 其 Taylor 级数的收敛半径为零, 但可以证明, 这些函数不应该是初等函数.

## Tauber 型求和: Cesàro 求和, Abel 求和.

下面我们简要介绍一下另外两种模式下的级数求和: Cesàro 求和与 Abel 求和. 我们知道, 对于给定的数列  $\{a_{n}\}$ , 可以通过引入部分和数列  $\{S_{n}\}$ ,  $S_{n}=a_{1}+a_{2}+\cdots+a_{n}$  ( $n=1,2,\cdots$ ), 以及  $\{S_{n}\}$  的极限存在与否来定义级数的收敛与发散. 因此, 可以看到, 这仅仅是对给定数列  $\{a_{n}\}$  的一种人为的 (经典) 求和模式而已. 既然如此, 我们也可以用其他的方式来定义级数的求和. Cesàro 求和以及 Abel 求和即为另外两种常见求和方式.

Cesàro 求和: 这是由意大利数学家 E. Cesàro 引入的一种计算级数和的方法, 此定义推广了经典的级数求和, 使得不仅适用于收敛的级数, 也适用于某些通常意义下发散的级数. 如果级数在经典意义下收敛到 $S$, 则其 Cesàro 求和也收敛且其值也为 $S$. 对于某些经典模式下发散的级数, 通过 Cesàro 求和方式, 也有可能给出一个和.

定义 13.5.1 级数  $\sum_{n=1}^{+\infty} c_{n}$  称为可 Cesàro 求和 (或 Cesàro 可知), 是指当  $n \to +\infty$  时数列  $\{\sigma_{n}\}$  极限  $\lim_{n \to +\infty} \sigma_{n}$  存在且为有限, 其中

$$
\sigma_ {n} = \frac {S _ {1} + S _ {2} + \cdots + S _ {n}}{n}, \qquad S _ {k} = \sum_ {n = 1} ^ {k} c _ {n},
$$

并且把极限值定义为级数的 Cesàro 意义下的和, 简称 Cesàro 和.

下面的结论可以由 Stolz 公式 (Stolz-Cesàro 定理) 得到.

定理 13.5.5 如果级数  $\sum_{n=1}^{+\infty} c_{n}$  收敛, 则该级数一定可 Cesàro 求和, 且级数和与 Cesàro 和相等.

注意, 定理的逆命题不成立.

例 13.5.7 发散级数  $\sum_{n=1}^{+\infty}(-1)^{n+1}$  是可 Cesàro 求和的, 且 Cesàro 和为  $\frac{1}{2}$ .

如果我们把上述 Cesàro 求和称为一阶 Cesàro 求和, 并称为 Cesàro  $(C,1)$  求和的话, 那么进一步, 我们还可以定义二阶甚至 p 阶的 Cesàro 求和  $(C,p)$  如下:

首先, 考虑通项为  $b_{n} \equiv 1$  的特殊级数

$$
\sum_ {n = 1} ^ {+ \infty} b _ {n} = 1 + 1 + 1 + \dots .
$$

定义

$$
B _ {n} ^ {(- 1)} = b _ {n} = 1 = \mathrm{C} _ {n} ^ {0}, \qquad B _ {n} ^ {(0)} = \sum_ {k = 1} ^ {n} b _ {k} = n = \mathrm{C} _ {n} ^ {1},
$$

$$
B _ {n} ^ {(1)} = \sum_ {k = 1} ^ {n} B _ {k} ^ {(0)} = \frac {n (n + 1)}{2} = \mathrm{C} _ {n + 1} ^ {2}, \quad \dots , \quad B _ {n} ^ {(p)} = \sum_ {k = 1} ^ {n} B _ {k} ^ {(p - 1)} = \mathrm{C} _ {n + p} ^ {p + 1}, \dots .
$$

其次, 对任一给定级数 $\sum_{n=1}^{+\infty} a_n$, 记 $A_n^{(0)} = \sum_{k=1}^{n} a_k$. 把前面定义中的级数 $\sum_{n=1}^{+\infty} a_n$ 的一阶 Cesàro (C, 1) 求和改记为

$$
A _ {n} ^ {(1)} = \lim _ {n \to + \infty} \frac {\sum_ {k = 1} ^ {n} B _ {k} ^ {(- 1)} A _ {k} ^ {(0)}}{B _ {n} ^ {(0)}} = \frac {A _ {1} ^ {(0)} + A _ {2} ^ {(0)} + \cdots + A _ {n} ^ {(0)}}{\mathrm{C} _ {n} ^ {1}}.
$$

定义级数 $\sum_{n=1}^{+\infty} a_n$ 的二阶 Cesàro $(C,2)$ 求和为

$$
A _ {n} ^ {(2)} = \lim _ {n \to + \infty} \frac {\sum_ {k = 1} ^ {n} B _ {k} ^ {(0)} A _ {k} ^ {(1)}}{\sum_ {k = 1} ^ {n} B _ {k} ^ {(0)}} = \frac {n A _ {1} ^ {(0)} + (n - 1) A _ {2} ^ {(0)} + \cdots + A _ {n} ^ {(0)}}{\mathrm{C} _ {n + 1} ^ {2}}.
$$

更一般地, 定义级数  $\sum_{n=1}^{+\infty}a_{n}$  的 p 阶  $(p \geqslant 2)$  Cesàro  $(C, p)$  求和为

$$
A _ {n} ^ {(p)} = \lim _ {n \to + \infty} \frac {\sum_ {k = 1} ^ {n} B _ {k} ^ {(p - 2)} A _ {k} ^ {(p - 1)}}{\sum_ {k = 1} ^ {n} B _ {k} ^ {(p - 2)}} = \frac {\mathrm{C} _ {n + p - 2} ^ {p - 1} A _ {1} ^ {(0)} + \mathrm{C} _ {n + p - 3} ^ {p - 1} A _ {2} ^ {(0)} + \cdots + \mathrm{C} _ {p - 1} ^ {p - 1} A _ {n} ^ {(0)}}{\mathrm{C} _ {n + p - 1} ^ {p}}.
$$

以上求和方法统称为 Cesàro 求和法.

Abel 求和: 我们再来看另一种常见的级数求和——Abel 求和.

定义 13.5.2 级数  $\sum_{n=1}^{+\infty}a_{n}$  称为可 Abel 求和 (或 Abel 可知), 是指极限

$$
\lim _ {x \to 1 ^ {-}} \sum_ {n = 0} ^ {+ \infty} a _ {n} x ^ {n} = S \tag {13.5.9}
$$

存在且为有限. 极限值 S 定义为级数在 Abel 意义下的和, 简称 Abel 和.

容易看出, 若 $\sum_{n=0}^{+\infty} a_n$ 收敛到 $S$, 则根据 Abel 定理, 关系式 (13.5.9) 必然成立. 另一方面, 易见级数 $\sum_{n=0}^{+\infty} (-1)^n$ 是 Abel 可和的, 但非经典可和. 因此, Abel 可和的确是经典级数可和的推广.

如果我们对级数通项加适当条件, 可以得到 Abel 可和与经典可和的关系:

定理 13.5.6 (小 o Tauber 定理) 设  $\lim_{x\to1^{-}}\sum_{n=1}^{+\infty}a_{n}x^{n}=A$  且  $a_{n}=o\left(\frac{1}{n}\right)$ ，则
 $\sum_{n=1}^{+\infty}a_{n}=A.$

证明 $\forall \varepsilon > 0$, 考虑 $\forall N > 0$, 令 $x = 1 - \frac{1}{N}$. 有

$$
\left| \sum_ {n = 1} ^ {N} a _ {n} - \sum_ {n = 1} ^ {N} a _ {n} x ^ {n} \right| \leqslant \sum_ {n = 1} ^ {N} | a _ {n} | \left(1 - \left(1 - \frac {1}{N}\right) ^ {n}\right) \leqslant \sum_ {n = 1} ^ {N} | a _ {n} | \frac {n}{N} \rightarrow 0 \quad (N \rightarrow + \infty).
$$

又

$$
\begin{array}{l} \left| \sum_ {n = 1} ^ {+ \infty} a _ {n} x ^ {n} - \sum_ {n = 1} ^ {N} a _ {n} x ^ {n} \right| \leqslant \sum_ {n > N} | a _ {n} | \left(1 - \frac {1}{N}\right) ^ {n} \leqslant \sum_ {n > N} \frac {n a _ {n}}{N} \left(1 - \frac {1}{N}\right) ^ {n} \leqslant \sum_ {n > N} \frac {\varepsilon}{N} \left(1 - \frac {1}{N}\right) ^ {n} \\ = \varepsilon \left(1 - \frac {1}{N}\right) ^ {N + 1} \rightarrow \frac {\varepsilon}{\mathrm{e}} \quad (N \rightarrow + \infty). \\ \end{array}
$$

综合二者结论得证.

Cesàro 可和与 Abel 可和的关系: 我们有

定理 13.5.7 若级数  $\sum_{n=0}^{+\infty} a_{n}$  Cesàro 可和, 则  $\sum_{n=0}^{+\infty} a_{n}$  也 Abel 可和, 且 Abel 和等于 Cesàro 和.

证明 不妨设 $\sum_{n=0}^{+\infty} a_n$ 的 Cesàro 和为零. 任取 $m \geqslant 1$, 对于 $x \in (0,1)$, 我们有

$$
\begin{array}{l} \left| \sum_ {n = 0} ^ {+ \infty} a _ {n} x ^ {n} \right| = \left| (1 - x) \sum_ {n = 0} ^ {+ \infty} S _ {n} x ^ {n} \right| = \left| (1 - x) ^ {2} \sum_ {n = 0} ^ {+ \infty} (n + 1) \sigma_ {n} x ^ {n} \right| \\ \leqslant (1 - x) ^ {2} \sum_ {n = 0} ^ {m} (n + 1) \left| \sigma_ {n} \right| x ^ {n} + (1 - x) ^ {2} \sup _ {k \geqslant m} \left| \sigma_ {k} \right| \sum_ {n = m + 1} ^ {+ \infty} (n + 1) x ^ {n} \\ \leqslant (1 - x) ^ {2} \sum_ {n = 0} ^ {m} (n + 1) | \sigma_ {n} | x ^ {n} + \sup _ {k \geqslant m} | \sigma_ {k} |. \\ \end{array}
$$

因此 $\lim_{x\to 1^{-}}\left|\sum_{n = 0}^{+\infty}a_nx^n\right|\leqslant \sup_{k\geqslant m}|\sigma_k|$. 再令 $m\to +\infty$ 即得 $\lim_{x\to 1^{-}}\sum_{n = 0}^{+\infty}a_nx^n = 0.$

注意, 上面推导过程中用到关系式

$$
1 = (1 - x) ^ {2} \sum_ {n = 0} ^ {+ \infty} (n + 1) x ^ {n},
$$

以及两次用到 Abel 变换:

$$
\sum_ {n = 0} ^ {+ \infty} a _ {n} x ^ {n} = (1 - x) \sum_ {n = 0} ^ {+ \infty} S _ {n} x ^ {n} = (1 - x) ^ {2} \sum_ {n = 0} ^ {+ \infty} (n + 1) \sigma_ {n} x ^ {n}.
$$

这是因为

$$
\begin{array}{l} \left(1 - 2 x + x ^ {2}\right) \sum_ {n = 0} ^ {+ \infty} (n + 1) \sigma_ {n} x ^ {n} = \sum_ {n = 0} ^ {+ \infty} \left((n + 1) \sigma_ {n} - 2 n \sigma_ {n - 1} + (n - 1) \sigma_ {n - 2}\right) x ^ {n} \\ = \sum_ {n = 0} ^ {+ \infty} (((n + 1) \sigma_ {n} - n \sigma_ {n - 1}) - (n \sigma_ {n - 1} - (n - 1) \sigma_ {n - 2})) x ^ {n} \\ = \sum_ {n = 0} ^ {+ \infty} \left(S _ {n} - S _ {n - 1}\right) x ^ {n} = \sum_ {n = 0} ^ {+ \infty} a _ {n} x ^ {n}. \\ \end{array}
$$

下面的例子告诉我们, Abel 可和不一定蕴涵着 Cesàro 可和. 因此 Abel 可和是一种比 Cesàro 可和更广的求和方式.

例 13.5.8 考虑通项为  $a_{n}=(-1)^{n+1}n$  的级数

$$
1 - 2 + 3 - 4 + 5 - 6 + \dots .
$$

显然, 此级数发散. 进一步, 直接计算可以看出该级数的 Cesàro $(C,1)$ 求和也发散. 事实上, 这是因为

$$
S _ {1} = 1, \quad S _ {2} = - 1, \quad S _ {3} = 2, \quad S _ {4} = - 2, \quad \dots , S _ {2 n - 1} = n, \quad S _ {2 n} = - n, \quad \dots ,
$$

所以

$$
\sigma_ {1} = 1, \quad \sigma_ {2} = 0, \quad \sigma_ {3} = \frac {2}{3}, \quad \sigma_ {4} = 0, \quad \dots , \quad \sigma_ {2 n - 1} = \frac {n}{2 n - 1}, \quad \sigma_ {2 n} = 0, \quad \dots ,
$$

故  $\{\sigma_{n}\}$  的极限不存在.

但可以证明, 此级数是 Abel 可和的. 为此, 考虑幂级数

$$
x - 2 x ^ {2} + 3 x ^ {3} - 4 x ^ {4} + 5 x ^ {5} - 6 x ^ {6} + \dots ,
$$

该幂级数在区间 $(0,1)$ 上有和函数 $f(x) = \frac{x}{(1 + x)^2}$，当 $x\to 1^{-}$ 时趋近于极限 $\frac{1}{4}$，因此该级数在Abel意义下是可和的.

在讨论常数项级数乘积时, 我们在例 11.4.3 中断言, 存在两个条件收敛的级数, 它们的 Cauchy 乘积级数绝对收敛. 下面我们首先证明这个结论.

例 13.5.9 证明: 存在两个条件收敛的级数, 它们的 Cauchy 乘积级数绝对收敛.

证明 注意到当 $|x| < 1$ 时, 对任意实数 $m$, 函数 $(1 + x)^{m}$ 的 Taylor 级数总是绝对收敛的. 若 $-1 < m < 0$, 则当 $x = 1$ 时, 相应的级数是条件收敛的, 当 $x = -1$ 时, 级数发散. 所以, 级数

$$
f (x) = \frac {1 + x}{\sqrt {1 + x ^ {3}}} = \sum_ {n = 0} ^ {+ \infty} a _ {n} x ^ {n}
$$

与级数

$$
g (x) = \frac {1 - x + x ^ {2}}{\sqrt {1 + x ^ {3}}} = \sum_ {n = 0} ^ {+ \infty} b _ {n} x ^ {n}
$$

当 $|x| < 1$ 时绝对收敛, $x = 1$ 时条件收敛. 因此, 级数 $\sum_{n=0}^{+\infty} a_n$, $\sum_{n=0}^{+\infty} b_n$ 都是条件收敛的.

由于对任意的 x，都有  $f(x) \cdot g(x) \equiv 1$ ，故  $c_{0} = 1, c_{n} = 0 (n = 1, 2, \cdots)$ ，其中  $c_{n} = a_{0} b_{n} + a_{1} b_{n-1} + \cdots + a_{n} b_{0}$ 。因此，级数  $\sum_{n=0}^{+\infty} c_{n}$  绝对收敛。

另一方面, 在讨论常数项级数乘积时, 定理 11.4.11 告诉我们, 如果两个收敛级数的 Cauchy 乘积级数收敛, 那么 Cauchy 乘积级数的和等于两个收敛级数和的乘积. 但是, 例 11.4.4 告诉我们, 两个条件收敛级数其 Cauchy 乘积级数有可能不收敛. 下面的定理告诉我们, 两个收敛级数的 Cauchy 乘积级数, 在 Cesàro 意义下总是可求和的. 即, 下面的 Cesàro 定理成立.

定理 13.5.8 (Cesàro 定理) 设级数  $\sum_{n=0}^{+\infty}a_{n}$  和  $\sum_{n=0}^{+\infty}b_{n}$  分别收敛到 A 和 B, 则它

们的 Cauchy 乘积  $\sum_{n=0}^{+\infty}c_{n}$  Cesàro 可和, 且和为 AB.

证明 记

$$
A _ {n} = \sum_ {k = 0} ^ {n} a _ {k}, \quad B _ {n} = \sum_ {k = 0} ^ {n} b _ {k}, \quad C _ {n} = \sum_ {k = 0} ^ {n} c _ {k}, \quad H _ {n} = \sum_ {k = 0} ^ {n} C _ {k}, \quad n \geqslant 0.
$$

由定理假设， $\lim_{n\to+\infty}A_{n}=A,\quad\lim_{n\to+\infty}B_{n}=B.$  而  $\forall x\in(-1,1)$ ,

$$
\begin{array}{l} (1 - x) ^ {2} \sum_ {n = 0} ^ {+ \infty} H _ {n} x ^ {n} = \sum_ {n = 0} ^ {+ \infty} c _ {n} x ^ {n} = \left(\sum_ {n = 0} ^ {+ \infty} a _ {n} x ^ {n}\right) \left(\sum_ {n = 0} ^ {+ \infty} b _ {n} x ^ {n}\right) \\ = \left((1 - x) \sum_ {n = 0} ^ {+ \infty} A _ {n} x ^ {n}\right) \left((1 - x) \sum_ {n = 0} ^ {+ \infty} B _ {n} x ^ {n}\right) \\ = (1 - x) ^ {2} \sum_ {n = 0} ^ {+ \infty} \sum_ {k = 0} ^ {n} A _ {k} B _ {n - k} x ^ {n}. \\ \end{array}
$$

所以

$$
\lim _ {n \to + \infty} \frac {H _ {n}}{n + 1} = \lim _ {n \to + \infty} \frac {1}{n + 1} \sum_ {k = 0} ^ {n} A _ {k} B _ {n - k} = A B.
$$

定理得证.

关于 Abel 求和, 下面的定理成立:

定理 13.5.9 设  $\sum_{n=0}^{+\infty}a_{n}$  和  $\sum_{n=0}^{+\infty}b_{n}$  均 Abel 可和, 且它们的 Abel 和为 A 和 B, 则
 $\sum_{n=0}^{+\infty}a_{n}$  和  $\sum_{n=0}^{+\infty}b_{n}$  的 Cauchy 乘积也 Abel 可和, 且 Abel 和为 AB.

## 习题 13.5

1. 考虑函数 $f(x) = \ln (1 + x + x^2 + x^3 + x^4)$.

(1) 求 $f(x)$ 在 $x_0 = 0$ 处的幂级数展开 $\sum_{n=1}^{+\infty} a_n x^n$.
(2) 确定幂级数的收敛域.
(3) 计算  $\sum_{n=1}^{+\infty}a_{n}$ .

2. 如果在定理 13.5.2 中, 两个幂级数的收敛半径分别为  $R_{1}, R_{2}$ , 问它们乘积级数的收敛半径是多少?

3. 试用形式幂级数的思路, 用待定系数的方法, 即 $y = \sum_{n=0}^{+\infty} a_n x^n$ 以及形式求导和形式二阶导, 验证微分方程 $x^2 y' = (1 - x)y - 1$, $y(0) = 1$ 具有形式幂级数解 $y = \sum_{n=0}^{+\infty} n! x^n$.

4. 试问初等函数的 Taylor 级数有没有可能收敛半径为 0?

5. 设 $P_{m}(x)$ 是给定的 $m$ 次多项式. 考虑由下面级数定义的函数 $f(x)$:

$$
f (x) = \sum_ {n = 0} ^ {+ \infty} \frac {P _ {m} ^ {n} (x)}{n !}.
$$

证明: $f(x)$ 的幂级数展开式中，不可能连着出现 $m$ 个零系数.

6. 证明: 当 $\sum_{n=0}^{+\infty} a_n$ Cesàro 可和时, $\left\{\frac{a_n}{n+1}\right\}$ 有界.

7. 求幂级数  $\sum_{n=1}^{+\infty}\frac{2}{4n-1}x^{2n}$  的和函数.

8. 设级数 $\sum_{n=0}^{+\infty} a_n$ 和 $\sum_{n=0}^{+\infty} b_n$ 均 Cesàro 可和, 试讨论它们的 Cauchy 乘积 $\sum_{n=0}^{+\infty} c_n$ 是否 Cesàro 可和?

9. 证明定理 13.5.9.

10. 设 $\sum_{n=0}^{+\infty} a_n$ 的 Abel 和为 $A$. 证明: $\sum_{n=0}^{+\infty} a_n$ 收敛当且仅当

$$
\lim _ {n \to + \infty} \frac {a _ {1} + 2 a _ {2} + \cdots + n a _ {n}}{n} = 0.
$$

11. 试讨论例 13.5.8 中级数是否可二阶 Cesàro 求和？是否可三阶 Cesàro 求和？进一步思考，是否一个发散的但 Abel 可和的级数，一定存在自然数 k，使得该级数是 k 阶 Cesàro 可和的.

12. 设幂级数

$$
\sum_ {n = 0} ^ {+ \infty} a _ {n} x ^ {n} = f (x)
$$

中的所有系数 $a_{n} \in \{0,1,\dots ,9\}$. 试证明:如果 $f\left(\frac{1}{10}\right) \in \mathbb{Q}$, 那么 $f(x)$ 是一个有理函数, 即 $f(x) = \frac{P(x)}{Q(x)}$, 其中 $P(x), Q(x)$ 是多项式.

## 13.6 连续函数的多项式逼近

函数的逼近是分析学和有关应用学科中极其重要的一部分内容. 它的基本出发点是由简单的、熟悉的、光滑性好的函数, 按照某种度量标准, 逼近一个给定的通常是相对复杂的、陌生的、性质一般的函数. 比如前面章节中看到的用逐段常值函数、折线函数、连续函数来逼近可积函数, 用 Taylor 多项式来逼近一个光滑的函数, 等等.

我们知道, 如果函数  $f(x)$  在  $(-R, R)$  中能展开成幂级数, 那么对任意  $[a, b] \subset (-R, R)$ ,  $f(x)$  在  $[a, b]$  上能用多项式一致逼近, 即  $\forall \varepsilon > 0, \exists N > 0$ , 只要 n > N, 取 n 阶 Taylor 多项式  $T_{n}(x)$  即可做到  $|f(x) - T_{n}(x)| < \varepsilon$ .

但是能展开成幂级数的函数少之又少, 因为它对函数的要求太高了: 要有足够高阶的导数. 所以, 用幂级数来逼近一个函数具有太大的局限性. 另一方面, 一个非常自然的问题是: 对一些光滑性并不那么好的函数是否存在多项式逼近? 特别地, 比如连续函数可否由多项式逼近? 这是因为从函数的复杂性来看, 多项式是一类光滑性好、形式简单、便于分析的函数.

本节重点讨论连续函数的多项式逼近问题. 当然, 我们也有足够的理由用其他类型的“简单的、基本的、熟悉的”函数去逼近, 比如正弦函数、余弦函数等三角函数也具有上述好的特点, 因为毕竟“简单的、基本的”等字眼是主观的标准. 的确, 比如如何用三角函数逼近一般的函数同样是个重要的话题. 与此相关的内容, 我们将放到 Fourier 级数去讨论.

为了陈述方便, 我们先给出以下定义:

定义 13.6.1 设  $f(x)$  是定义在区间  $I \subseteq R$  上的函数, 如果对任意  $\varepsilon > 0$ , 总能找到多项式  $P(x)$ , 使得对 I 中所有的 x 均有

$$
| f (x) - P (x) | <   \varepsilon , \quad x \in I
$$

成立, 则称  $f(x)$  在 I 上能被多项式一致逼近.

显然, $f(x)$ 在 $I$ 上可被多项式一致逼近的充要条件是存在多项式序列 $\{P_n(x)\}$, 使得 $P_n(x) \Rightarrow f(x) (x \in I)$. 另一方面, 我们知道, 如果 $f(x)$ 在 $I$ 上可被多项式一致逼近, 则显然 $f(x)$ 在 $I$ 上连续.

如果 $f(x)$ 在有限开区间 $(a, b)$ 上可被多项式一致逼近, 则由一致性, 可以证明 $f(x)$ 必可以连续延拓到闭区间 $[a, b]$ 上. 若 $I$ 是无穷区间, 当 $f(x)$ 不是多项式时, 则 $f(x)$ 在 $I$ 上一定不能被多项式逼近. 所以, 很自然提出下面的问题: 对于有限闭区间上的连续函数 $f(x)$, 是否一定可被多项式逼近? 下面著名的 Weierstrass 定理对此问题给出了一个充分性的答案:

如下定理称为 Weierstrass 第一逼近定理.

定理 13.6.1. 有界闭区间上的连续函数可用多项式一致逼近. 即对闭区间 $[a, b]$ 上的任意连续函数 $f(x)$, 存在多项式序列 $\{P_n(x)\}$, 使得在 $[a, b]$ 上 $P_n(x) \Rightarrow f(x)$.

Weierstrass 逼近定理有许多经典的证明方法, 这些方法各有鲜明的特点, 其背后通常还蕴含着不同的逼近思想和相关的学科背景. 下面我们给出的证明是基于 Bernstein 多项式的方法.

证法 1 不妨假设  $[a, b] = [0, 1]$ ，因为必要的话，作一个线性变换  $x = a + (b - a)t$ ，即可把问题转化为关于变量  $t \in [0, 1]$  上的连续函数的逼近.

记

$$
p _ {n, k} (x) = \mathrm{C} _ {n} ^ {k} x ^ {k} (1 - x) ^ {n - k},
$$

则有

$$
\sum_ {k = 0} ^ {n} p _ {n, k} (x) = 1. \tag {13.6.1}
$$

设 $f(x)$ 是 $[0,1]$ 上的连续函数, $n \geqslant 0$, 定义 $f$ 的 $n$ 阶 Bernstein 多项式为

$$
B _ {n} (f, x) = \sum_ {k = 0} ^ {n} f \left(\frac {k}{n}\right) p _ {n, k} (x) = \sum_ {k = 0} ^ {n} f \left(\frac {k}{n}\right) \mathrm{C} _ {n} ^ {k} x ^ {k} (1 - x) ^ {n - k}. \tag {13.6.2}
$$

我们将证明: $\{B_{n}(f,x)\}$ 是[0,1]上的一致收敛到 $f(x)$ 的多项式序列.

首先, 对方程 (13.6.1) 两端求导再乘 $x(1 - x)$, 可得

$$
\sum_ {k = 0} ^ {n} \mathrm{C} _ {n} ^ {k} (k - n x) x ^ {k} (1 - x) ^ {n - k} = 0, \quad \forall   x \in [ 0, 1 ]. \tag {13.6.3}
$$

对上式继续求导后再乘 $x(1 - x)$ 可得

$$
\sum_ {k = 0} ^ {n} \mathrm{C} _ {n} ^ {k} (k - n x) ^ {2} x ^ {k} (1 - x) ^ {n - k} = n x (1 - x), \quad \forall   x \in [ 0, 1 ]. \tag {13.6.4}
$$

整理上面的计算, 可得

$$
\begin{array}{l} \sum_ {k = 0} ^ {n} k p _ {n, k} (x) = n x, \\ \sum_ {k = 0} ^ {n} k ^ {2} p _ {n, k} (x) = n (n - 1) x ^ {2} + n x \\ \end{array}
$$

$$
\sum_ {k = 0} ^ {n} \left(x - \frac {k}{n}\right) ^ {2} p _ {n, k} (x) = \frac {x (1 - x)}{n}.
$$

由于 $f(x)$ 在 $[0,1]$ 上一致连续，故对任意 $\varepsilon > 0$ ，存在 $\delta > 0$ ，当 $|x - y| < \delta$ 时，有

$$
| f (x) - f (y) | <   \frac {\varepsilon}{2}.
$$

再由 $f(x)$ 的有界性, 知 $\exists M > 0$, 使得 $|f(x)| \leqslant M$, 当 $|x - y| \geqslant \delta$ 时,

$$
| f (x) | \leqslant M \leqslant \frac {M (x - y) ^ {2}}{\delta^ {2}}.
$$

因此, $\forall x\in [0,1]$ ，都有

$$
\left| f (x) - f \left(\frac {k}{n}\right) \right| <   \frac {\varepsilon}{2} + \frac {2 M}{\delta^ {2}} \left(x - \frac {k}{n}\right) ^ {2}.
$$

从而

$$
\begin{array}{l} \left| f (x) - B _ {n} (x) \right| = \left| \sum_ {k = 0} ^ {n} \left(f (x) - f \left(\frac {k}{n}\right)\right) p _ {n, k} (x) \right| \\ \leqslant \sum_ {k = 0} ^ {n} \left| f (x) - f \left(\frac {k}{n}\right) \right| p _ {n, k} (x) \\ \leqslant \frac {\varepsilon}{2} + \frac {2 M}{\delta^ {2}} \frac {x (1 - x)}{n} \leqslant \frac {\varepsilon}{2} + \frac {M}{2 \delta^ {2}} \frac {1}{n}. \\ \end{array}
$$

即  $B_{n}(f,x)\Rightarrow f(x)$ .

![](images/page_511_image_9.jpg)

下面给出基于 Lebesgue 做法的另一种直观性很强的证明. 我们仅给出基本步骤和思路, 读者可以补充细节.

证法 2  $\forall x \in [-1,1]$ ，令

$$
u _ {0} (x) = 0, \quad u _ {n + 1} (x) = u _ {n} (x) + \frac {1}{2} (x ^ {2} - u _ {n} ^ {2} (x)), \quad n = 0, 1, 2, \dots . \tag {13.6.5}
$$

不难证明以下结论:

(1) 对每个  $n \in N$ ,  $u_{n}(x)$  是一个多项式.
(2) 可以归纳证明, 对每个  $x \in [-1,1]$ ,  $0 \leqslant u_{n}(x) \leqslant u_{n+1}(x) \leqslant |x|$ .
(3) $\{u_{n}(x)\}$ 关于 $n$ 单调, 逐点收敛到极限函数 $|x|$, 由于 $|x|$ 在 $[-1,1]$ 上连续, 根据 Dini 定理, 知上述逐点收敛实则为一致收敛 (注: 也可通过估计

$$
\left| | x | - u _ {n} (x) \right| \leqslant | x | \left(1 - \frac {| x |}{2}\right) ^ {n} <   \frac {2}{n + 1}
$$

直接证明一致收敛性).

(4) 将 (13.6.5) 式中的迭代列换成

$$
u _ {0} (x) = 0, \quad u _ {n + 1} (x) = u _ {n} (x) + \frac {1}{2} \Big ((x - c) ^ {2} - u _ {n} ^ {2} (x) \Big), \quad n = 0, 1, 2, \dots ,
$$

重复上述过程, 可得  $\{u_{n}(x)\}$  一致收敛到  $|x-c|$ .

(5) $\forall \lambda \in \mathbb{R}$, 多项式序列 $\{\lambda u_n(x)\}$ 一致收敛到 $\lambda |x - c|$.
(6) 闭区间 $[a, b]$ 上的连续函数能被逐段折线 (即分段线性函数) 一致逼近.