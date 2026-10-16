即

$$
\lim _ {x \to x _ {0}} \frac {f (x) - f (x _ {0})}{x - x _ {0}} = \lim _ {x \to x _ {0}} f ^ {\prime} (x).
$$

## 7.2.2 $\frac{\infty}{\infty}$ 型极限

定理 7.2.3 (L'Hôpital 法则之二) 设 $f(x), g(x)$ 在 $a$ 点的 ${\delta }_{0}$ 去心邻域 ${\overset{ \circ  }{B}}_{{\delta }_{0}}\left( a\right)$ , 即 $0 < \left| {x - a}\right|  < {\delta }_{0}\left( {{\delta }_{0} > 0}\right)$ 内可导,且满足

(1) $\lim_{x\to a}g(x) = \infty$;
(2) $g^{\prime}(x)\neq 0,\forall x\in \mathring{B}_{\delta_{0}}(a);$
(3) $\lim_{x\to a}\frac{f'(x)}{g'(x)} = \ell$ ，其中 $\ell$ 为实数或 $\pm \infty$

则 $\lim_{x\to a}\frac{f(x)}{g(x)} = \ell .$

证明 我们只对 $\ell \in \mathbb{R}, x \to a^{+}$ 的情形给以证明, 其他情况的证明完全类似, 请读者自行补充.

根据假设, 对任给  $\varepsilon > 0$ , 存在  $0 < \eta < \delta_{0}$ , 当  $x \in (a, a + \eta)$  时

$$
\ell - \frac {\varepsilon}{4} <   \frac {f ^ {\prime} (x)}{g ^ {\prime} (x)} <   \ell + \frac {\varepsilon}{4}. \tag {7.2.4}
$$

对任意的 $x \in (a, a + \eta)$, 在 $(x, a + \eta)$ 内应用 Cauchy 中值定理, 知存在 $\xi \in (x, a + \eta)$, 使得

$$
\ell - \frac {\varepsilon}{4} <   \frac {f (x) - f (a + \eta)}{g (x) - g (a + \eta)} = \frac {f ^ {\prime} (\xi)}{g ^ {\prime} (\xi)} <   \ell + \frac {\varepsilon}{4}.
$$

现在对 $\frac{f(x)}{g(x)} -\ell$ 进行估计.由于

$$
\frac {f (x)}{g (x)} - \ell = \frac {f (a + \eta) - \ell \cdot g (a + \eta)}{g (x)} + \left(1 - \frac {g (a + \eta)}{g (x)}\right) \cdot \left(\frac {f (x) - f (a + \eta)}{g (x) - g (a + \eta)} - \ell\right).
$$

从而

$$
\left| \frac {f (x)}{g (x)} - \ell \right| \leqslant \left| \frac {f (a + \eta) - \ell \cdot g (a + \eta)}{g (x)} \right| + \left| 1 - \frac {g (a + \eta)}{g (x)} \right| \cdot \frac {\varepsilon}{4}.
$$

根据定理条件 (1) 可知, 当 $x \to a^{+}$ 时, 上述关系式中右端第一个绝对值趋于 0 , 第二个绝对值趋于 1 . 即对前面给定的 $\varepsilon$, 存在 $0 < \delta < \eta$, 使得当 $x \in (a, a + \delta)$ 时

$$
\left| \frac {f (a + \eta) - \ell \cdot g (a + \eta)}{g (x)} \right| <   \frac {\varepsilon}{2}, \quad \left| 1 - \frac {g (a + \eta)}{g (x)} \right| <   2.
$$

这样我们就证明了

$$
\left| \frac {f (x)}{g (x)} - \ell \right| <   \varepsilon .
$$

注7.2.3 定理中的 $a$ 可以为 $\pm \infty$.

我们看到, 所谓的 $\frac{\infty}{\infty}$ 型不定式的极限, 其实并没有要求分子中的函数趋于无穷大, 因此一个夸张的能说明问题的例子是, 极限 $\lim_{x \to \infty} \frac{1}{x}$ 的计算是可以使用 L'Hôpital 法则的.

完全类同于注7.2.1，在应用L'Hôpital法则时，必须每一步都要先验证极限 $\lim_{x\to a}\frac{f'(x)}{g'(x)}$ 是否存在.因此求极限 $\lim_{x\to \infty}\frac{\sin x}{x}$ 时，虽然分母中的函数趋于无穷大，但仍然不宜应用L'Hôpital法则.

例7.2.7 设 $f(x)$ 在 $(a, +\infty)$ 上可微, 若 $\lim_{x \to +\infty} (f'(x) + f(x)) = \alpha \in \mathbb{R}$. 证明: $\lim_{x \to +\infty} f(x) = \alpha$.

证明 可以直接通过计算实现证明

$$
\lim _ {x \to + \infty} f (x) = \lim _ {x \to + \infty} \frac {\mathrm{e} ^ {x} f (x)}{\mathrm{e} ^ {x}} = \lim _ {x \to + \infty} \frac {\left(\mathrm{e} ^ {x} f (x)\right) ^ {\prime}}{\mathrm{e} ^ {x}} = \lim _ {x \to + \infty} \left(f ^ {\prime} (x) + f (x)\right) = \alpha . \quad \square
$$

例7.2.8 设 $f$ 在 $(a, +\infty)$ 上可导.

(1) 如果  $\lim_{x\to+\infty}xf'(x)=\lambda\neq0,$  则  $\lim_{x\to+\infty}f(x)=\infty;$
(2) 如果 $f$ 为有界函数, 且 $f'$ 为单调函数, 则 $\lim_{x \to +\infty} x f'(x) = 0$.

证明 (1) 当 $x \to +\infty$ 时, $\ln x \to +\infty$, 故由 L'Hôpital 法则可得

$$
\lim _ {x \to + \infty} \frac {f (x)}{\ln x} = \lim _ {x \to + \infty} \frac {f ^ {\prime} (x)}{1 / x} = \lim _ {x \to + \infty} x f ^ {\prime} (x) = \lambda ,
$$

特别地， $\lim_{x\to+\infty}f(x)=\infty.$

(2) 由 $f'$ 单调可知, 当 $x$ 充分大时 $f'$ 不变号, 从而 $f$ 也是单调的. 由 $f$ 有界可知极限 $\lim_{x \to +\infty} f(x)$ 存在且有限, 记为 $\beta$. 当 $x$ 充分大时, 根据 Lagrange 定理, 存在 $\xi \in (x/2, x), \zeta \in (x, 2x)$, 使得

$$
f (x) - f (x / 2) = \frac {1}{2} x f ^ {\prime} (\xi), f (2 x) - f (x) = x f ^ {\prime} (\zeta).
$$

由 $\lim_{x\to +\infty}f(x) = \beta$ 可知 $\lim_{x\to +\infty}xf'(\xi) = 0,\lim_{x\to +\infty}xf'(\zeta) = 0.$ 注意到 $xf^{\prime}(x)$ 介于 $xf^{\prime}(\xi)$ 与 $xf^{\prime}(\zeta)$ 之间，从而极限也等于零. □

例7.2.9 求极限 $\lim_{x\to +\infty}\frac{x^{\alpha}}{\mathrm{e}^{x}}$ ，其中 $\alpha >0$

解 这是一个 $\frac{\infty}{\infty}$ 型极限. 应用 L'Hôpital 法则, 可得

$$
\lim _ {x \to + \infty} \frac {x ^ {\alpha}}{\mathrm{e} ^ {x}} = \lim _ {x \to + \infty} \frac {\alpha x ^ {\alpha - 1}}{\mathrm{e} ^ {x}}.
$$

后者仍然有可能是一个 $\frac{\infty}{\infty}$ 型极限 (比如当 $\alpha > 1$ 时). 可以多次应用 L'Hôpital 法则, 直到

$$
\lim _ {x \to + \infty} \frac {x ^ {\alpha}}{\mathrm{e} ^ {x}} = \dots = \lim _ {x \to + \infty} \frac {\alpha (\alpha - 1) \cdots (\alpha - [ \alpha ]) x ^ {\alpha - [ \alpha ] - 1}}{\mathrm{e} ^ {x}} = 0.
$$

例7.2.10 考虑函数

$$
f (x) = \left\{ \begin{array}{l l} \mathrm{e} ^ {- \frac {1}{x ^ {2}}}, & x \neq 0, \\ 0, & x = 0. \end{array} \right.
$$

证明 $f(x)\in C^{\infty}(\mathbb{R})$ ，即 $f(x)$ 是 $\mathbb{R}$ 上的光滑函数 $(C^k (I)$ 和 $C^\infty (I)$ 见定义6.5.2).

证明 当 $x \neq 0$ 时,

$$
f ^ {\prime} (x) = \frac {2}{x ^ {3}} \mathrm{e} ^ {- \frac {1}{x ^ {2}}}.
$$

当 $x = 0$ 时, 根据导数的定义, 有

$$
f ^ {\prime} (0) = \lim _ {x \to 0} \frac {f (x) - f (0)}{x} = \lim _ {x \to 0} \frac {\mathrm{e} ^ {- \frac {1}{x ^ {2}}}}{x} = \lim _ {t \to \infty} \frac {t}{\mathrm{e} ^ {t ^ {2}}} = \lim _ {t \to \infty} \frac {1}{2 t \mathrm{e} ^ {t ^ {2}}} = 0,
$$

其中中间一步我们作了变量替换 $t = \frac{1}{x}$，最后一步应用了L'Hôpital法则.因此我们证明了 $f(x)\in C^{1}(\mathbb{R})$

在求导的过程中, 可以归纳证明 $f^{(n)}(x)$ 具有形式

$$
f ^ {(n)} (x) = \left\{ \begin{array}{l l} P _ {3 n} \left(\frac {1}{x}\right) \mathrm{e} ^ {- \frac {1}{x ^ {2}}}, & x \neq 0, \\ 0, & x = 0, \end{array} \right.
$$

其中  $P_{k}(t)$  是 t 的 k 次多项式.

下面我们用数学归纳法证明 $f(x) \in C^{n}(\mathbb{R}) (n > 1)$. 前面已证 $n = 1$ 时结论为真. 假设对自然数 $n$ 结论成立, 我们来看 $n + 1$ 时的情形.

当 $x \neq 0$ 时，

$$
f ^ {(n + 1)} (x) = \left(\frac {2}{x ^ {3}} P _ {3 n} \left(\frac {1}{x}\right) - \frac {1}{x ^ {2}} P _ {3 n} ^ {\prime} \left(\frac {1}{x}\right)\right) \mathrm{e} ^ {- \frac {1}{x ^ {2}}} = P _ {3 (n + 1)} \left(\frac {1}{x}\right) \mathrm{e} ^ {- \frac {1}{x ^ {2}}}.
$$

而

$$
f ^ {(n + 1)} (0) = \lim _ {x \to 0} \frac {1}{x} P _ {3 n} \left(\frac {1}{x}\right) \mathrm{e} ^ {- \frac {1}{x ^ {2}}} = \lim _ {t \to \infty} \frac {t P _ {3 n} (t)}{\mathrm{e} ^ {t ^ {2}}} = 0.
$$

故结论成立.

例子中的这个函数 (或者相应的变形) 是数学诸多分支中极其重要的函数, 在以后的章节中我们还会与这个函数打交道. 该函数的一个重要作用之一是可以 “磨光” 一些函数. 比如, 为了把定义在 $(- \infty, 0] \cup [1, +\infty)$ 上的函数

$$
\varPhi (x) = \left\{ \begin{array}{l l} 0, & x \leqslant 0, \\ 1, & x \geqslant 1 \end{array} \right.
$$

在区间 $[0,1]$ 上无穷次光滑地连接起来, 我们可以对例题中的函数适当“加工”, 定义

$$
\varphi (x) = \left\{ \begin{array}{l l} \mathrm{e} ^ {- \frac {1}{x ^ {2}}}, & x > 0, \\ 0, & x \leqslant 0. \end{array} \right.
$$

则 $\varphi (x)\in C^{\infty}(\mathbb{R})$ ，函数 $\varPhi (x) = \frac{\varphi(x)}{\varphi(x) + \varphi(1 - x)}$ 满足要求.

例 7.2.11 设  $f(x) \in C^{2}(\mathbb{R})$ ，满足  $f''(x) + xf'(x) + f(x) = 0$ 。证明: $f(x)$  和  $f'(x)$  均为有界函数。更进一步，成立

$$
\lim _ {x \to + \infty} f (x) = 0, \quad \lim _ {x \to + \infty} f ^ {\prime} (x) = 0.
$$

证明 注意到

$$
f ^ {\prime \prime} (x) + x f ^ {\prime} (x) + f (x) = (f ^ {\prime} (x) + x f (x)) ^ {\prime} = 0,
$$

故有  $f'(x) + xf(x) = c.$  因此,

$$
\lim _ {x \to + \infty} f (x) = \lim _ {x \to + \infty} \frac {f (x) \mathrm{e} ^ {\frac {x ^ {2}}{2}}}{\mathrm{e} ^ {\frac {x ^ {2}}{2}}} = \lim _ {x \to + \infty} \frac {(x f (x) + f ^ {\prime} (x)) \mathrm{e} ^ {\frac {x ^ {2}}{2}}}{x \mathrm{e} ^ {\frac {x ^ {2}}{2}}} = \lim _ {x \to + \infty} \frac {c}{x} = 0.
$$

因此存在实数 $M > 0$ ，使得当 $|x| > M$ 时，有 $|f(x)| < 1$ ，故 $f(x)$ 有界；而当 $|x| \leqslant M$ 时，由 $f(x)$ 的连续性知在 $[-M, M]$ 上也是有界的.

同理, 有

$$
\lim _ {x \to + \infty} f ^ {\prime} (x) = \lim _ {x \to + \infty} \frac {f ^ {\prime} (x) \mathrm{e} ^ {\frac {x ^ {2}}{2}}}{\mathrm{e} ^ {\frac {x ^ {2}}{2}}} = \lim _ {x \to + \infty} \frac {(f ^ {\prime \prime} (x) + x f ^ {\prime} (x)) \mathrm{e} ^ {\frac {x ^ {2}}{2}}}{x \mathrm{e} ^ {\frac {x ^ {2}}{2}}} = \lim _ {x \to + \infty} \frac {- f (x)}{x} = 0.
$$

特别地, $f'(x)$ 在 $\mathbb{R}$ 上也有界.

## 习题 7.2

1. 求下列极限:

(1) $\lim_{x\to 0}\frac{\mathrm{e}^x - 1}{\sin{x}};$
(3) $\lim_{x\to a}\frac{a^x - x^a}{x - a};$
(5) $\lim_{x\to 0}\frac{x\cot x - 1}{x^2};$

2. 求下列极限  $(a, b > 0)$ :

(1) $\lim_{x\to +\infty}\frac{\ln(x\ln x)}{x^a};$
(3) $\lim_{x\to 0}\frac{\mathrm{e}^{ax} - \mathrm{e}^{bx}}{\sin ax - \sin bx};$

(2) $\lim_{x\to 1}x^{\frac{1}{1 - x}};$
(4) $\lim_{x\to 0}(\tan x)^{\frac{1}{x^2}};$
(6) $\lim_{x\to 1}\frac{1 - \sin^2\frac{\pi x}{2}}{1 - x^2}.$
(2) $\lim_{x\to +\infty}x\left(\left(1 + \frac{1}{x}\right)^x -\mathrm{e}\right);$
(4) $\lim_{x\to +\infty}\left(\frac{\pi}{2} -\arctan x\right)^{1 / \ln x}.$

3. 试分别就 $a \in \{0, \pm 1, \pm \infty\}$, 求极限 $\lim_{x \to a} \left( \frac{a_1^x + a_2^x + \cdots + a_n^x}{n} \right)^{1/x} (a_i \geqslant 0)$.

4. 设  $f(x)$  是一个在点 a 二阶可导的函数, 证明:

$$
\lim _ {h \to 0} \frac {f (a + h) + f (a - h) - 2 f (a)}{h ^ {2}} = f ^ {\prime \prime} (a).
$$

5. 求下列极限:

(1) $\lim_{x\to 0}\frac{1}{x^2}\left(2(1 + x)^{\frac{1}{x}} + \mathrm{e}(x - 2)\right);$
(2) $\lim_{x\to 0}\frac{1}{x^2}\left((1 + \ln (1 + x))^{\frac{1}{\tan x}} + \mathrm{e}(x - 1))\right)$.

6. 设 $\alpha, \beta$ 为方程 $x^{2} + bx + c = 0$ 的两个不同的实根. 求极限

$$
\lim _ {x \to \beta} \frac {\mathrm{e} ^ {2 (x ^ {2} + b x + c)} - 1 - 2 (x ^ {2} + b x + c)}{(x - \beta) ^ {2}}.
$$

7. 设

$$
f (x) = \left\{ \begin{array}{l l} \frac {1}{x} (g (x) - \cos x), & x > 0, \\ a x + b, & x \leqslant 0, \end{array} \right.
$$

其中 $g''(0) = 5, g'(0) = 2, g(0) = 1$. 试确定 $a, b$ 的值, 使得 $f(x)$ 在 $x = 0$ 处可导, 并求 $f'(0)$.

8. 设 $f$ 在 $(a, +\infty)$ 上有定义, 在每一个有界区间内有界 $\lim_{x \to +\infty} \frac{f(x+1)-f(x)}{x^n} = \ell$. 试求极限 $\lim_{x \to +\infty} \frac{f(x)}{x^{n+1}}$.

9. 设 $f$ 是方程

$$
\left\{ \begin{array}{l l} f ^ {\prime \prime} (x) + 3 f ^ {\prime} (x) + 4 f (x) = \frac {4 x ^ {2}}{x ^ {2} + x + 1}, & x \geqslant 0, \\ f (0) = 1, \quad f ^ {\prime} (0) = 2 \end{array} \right.
$$

的解. 证明: $\lim_{x\to +\infty}f''(x) = \lim_{x\to +\infty}f'(x) = 0.$

10. (1) 设 $f$ 在 $[a, +\infty)$ 上二阶可导, 且满足

$$
| f ^ {\prime \prime} (x) | \leqslant M | f (x) |, f (a) = f ^ {\prime} (a) = 0, M > 0, \forall x \in [ a, + \infty).
$$

证明: 在  $[a, +\infty)$  上  $f(x) \equiv 0$ .

(2) 结合 (1) 的条件和结论以及习题 7.1 中题目 12, 能否给出一个更一般的结论?

11. 设 $f$ 在 $\mathbb{R}$ 上连续可微, 且

$$
\forall x \in \mathbb {R}, \quad f (x + 1) - f (x) = f ^ {\prime} (x), \quad \lim _ {x \to + \infty} f ^ {\prime} (x) = c.
$$

证明: $f'(x) \equiv c$.

12. 设 $f$ 在 $\mathbb{R}$ 上可导且 $\forall x \in \mathbb{R}, |f'(x)| < 1$, 又设 $x_0 \in \mathbb{R}, x_{n+1} = f(x_n) (n \geqslant 0)$. 举例说明 $\{x_n\}$ 可能发散.

13. 试求对于任何 $x \in \left(0, \frac{\pi}{2}\right)$ 使得 $x < \frac{\sin x}{\cos^{\alpha} x}$ 都成立的最小的 $\alpha$.

14. 证明: $\forall x \in \left(0, \frac{\pi}{2}\right)$, 有 $\sin x < x < 4\sin \frac{x}{2} - \sin x$.

15. 求使得不等式

$$
\tan x + \alpha \sin x \geqslant (1 + \alpha) x, \quad \forall x \in \left(0, \frac {\pi}{2}\right)
$$

成立的  $\alpha$ .

16. 设  $f(x)$  是 [0,1] 上的可微函数， $f(0)=0,\ f(1)=1$ ,

$$
\lambda_ {1}, \lambda_ {1}, \dots , \lambda_ {n} > 0, \quad \lambda_ {1} + \lambda_ {2} + \dots + \lambda_ {n} = 1.
$$

证明: 区间 [0,1] 上存在 n 个两两互异的实数  $x_{1}, x_{2}, \cdots, x_{n}$  使得  $\sum_{k=1}^{n} \frac{\lambda_{k}}{f'(x_{k})} = 1$ .

17. 设 $f(x)$ 是 $[0,1]$ 上的连续可微函数，$f(0) = 0$，$f(1) = 1$。证明或否定下面的结论:

对任意的  $\varepsilon > 0$ ，都存在自然数 N，以及两两互异的  $x_{1}, x_{2}, \cdots, x_{N} \in (0,1)$  使得

$$
\left| \frac {1}{2 f ^ {\prime} (x _ {1})} + \frac {1}{2 ^ {2} f ^ {\prime} (x _ {2})} + \frac {1}{2 ^ {3} f ^ {\prime} (x _ {3})} + \dots + \frac {1}{2 ^ {N} f ^ {\prime} (x _ {N})} - 1 \right| <   \varepsilon .
$$

18. 设 $f(x)$ 和 $\tilde{f}(x)$ 均为连续可微函数, 满足

$$
f (x _ {1}) = f (x _ {2}) = 0, \quad \tilde {f} (\tilde {x} _ {1}) = \tilde {f} (\tilde {x} _ {2}) = 0,
$$

其中 $x_{1} < x_{2}$, 而 $\tilde{x}_{i} (i = 1,2)$ 是由 $x_{i}$ 向右移动得到的, 且满足 $\tilde{x}_{1} < \tilde{x}_{2}$. 根据 Rolle 中值定理, 应该分别存在 $\xi \in (x_{1}, x_{2})$ 和 $\tilde{\xi} \in (\tilde{x}_{1}, \tilde{x}_{2})$ 使得 $f'(\xi) = 0$ 和 $\tilde{f}'(\tilde{\xi}) = 0$. 问是否一定成立 $\xi < \tilde{\xi}$? 如果成立, 请证明, 如果不成立, 举个反例.

19. 设 $P(x)$ 和 $\tilde{P}(x)$ 均为 $n$ 次首一 (最高阶项系数为 1) 多项式, 均有 $n$ 个实单根,

$$
\begin{array}{l} P (x) = (x - x _ {1}) (x - x _ {2}) \dots (x - x _ {n}), \\ \tilde {P} (x) = (x - \tilde {x} _ {1}) (x - \tilde {x} _ {2}) \dots (x - \tilde {x} _ {n}), \\ \end{array}
$$

其中  $x_{1}<x_{2}<\cdots<x_{n}$ ，而  $\tilde{x}_{i}$  是由  $x_{i}$  向右移动得到的，且满足  $\tilde{x}_{1}<\tilde{x}_{2}<\cdots<\tilde{x}_{n}$ 。记  $P'(x)$  位于  $(x_{i},x_{i+1})$  内的零点为  $\xi_{i};\tilde{P}'(x)$  位于  $(\tilde{x}_{i},\tilde{x}_{i+1})$  内的零点为  $\tilde{\xi}_{i}(i=1,2,\cdots,n-1)$ 。证明: $\tilde{P}'(x)$  的每个零点都分别位于  $P'(x)$  的相应的零点右侧，即  $\xi_{i}<\tilde{\xi}_{i}$ 。

20. 设函数 $f$ 在点 $x_0$ 处二阶可导, 且 $f''(x_0) \neq 0$. 由微分中值定理, 当 $h$ 充分小时, 存在 $\theta = \theta(h) (0 < \theta < 1)$, 使得 $f(x_0 + h) - f(x_0) = f'(x_0 + \theta h)h$. 证明 $\lim_{h \to 0} \theta = \frac{1}{2}$.

21. 设  $a_{i} \in R (1 \leqslant i \leqslant n)$ . 求极限  $\lim_{x \to 0} \frac{1}{x^{2}} \left(1 - \cos(a_{1}x) \cos(a_{2}x) \cdots \cos(a_{n}x)\right)$ .

22. 设 $f''(x_0)$ 存在, $f'(x_0) \neq 0$. 求极限 $\lim_{x \to x_0} \left( \frac{1}{f(x) - f(x_0)} - \frac{1}{f'(x_0)(x - x_0)} \right)$.

23. 设 $a_1 \in (0, \pi)$, $a_{n+1} = \sin a_n$ ($n \geqslant 1$). 证明: $\lim_{n \to +\infty} \sqrt{n} a_n = \sqrt{3}$.

24. 设 $f$ 在 0 点的某一邻域内有二阶导数, 且 $f(0) = 0$, 定义 $g(0) = f'(0)$ 且当 $x \neq 0$ 时, $g(x) = \frac{f(x)}{x}$. 求证: $g$ 在该邻域内有连续的导函数.

25. 设 $f$ 在 $(a, +\infty)$ 上可导，若 $\lim_{x \to +\infty} (f(x) + xf'(x) \ln x) = \ell$，证明:$\lim_{x \to +\infty} f(x) = \ell$.

## 7.3 Taylor 展开式

本节我们利用导数和高阶导数来讨论函数的逼近问题. 具体来说, 在前面章节我们考察了无穷小增量公式与有限增量公式, 这些公式借助于线性式 (即一次多项式) 研究可导函数. 现在我们把上述公式推广到用 n 次多项式来研究 n 次可导的函数.

## 7.3.1 带 Peano 型余项的 Taylor 展开式

我们知道, 如果函数 $f(x)$ 在点 $x_0$ 处连续, 则

$$
f (x) - f (x _ {0}) = o (1) \quad (x \to x _ {0}),
$$

即在点 $x_0$ 附近 $f$ 可用常值函数来逼近. 如果 $f(x)$ 在点 $x_0$ 处可导的话, 则

$$
f (x) - \left(f (x _ {0}) + f ^ {\prime} (x _ {0}) (x - x _ {0})\right) = o (x - x _ {0}) \quad (x \to x _ {0}),
$$

即在点 $x_0$ 附近 $f$ 可用线性函数 $T_{1}$ 来逼近, 其中

$$
T _ {1} (x) = f (x _ {0}) + f ^ {\prime} (x _ {0}) (x - x _ {0}).
$$

因此

$$
f (x) = T _ {1} (x) + o (x - x _ {0}) \quad (x \to x _ {0}),
$$

我们先来看一下如果  $f(x)$  在点  $x_{0}$  处二阶可导的情景.

例 7.3.1 设 f 在点  $x_{0}$  处二阶可导, 求极限  $\lim_{h\to0}\frac{1}{h^{2}}\left(f(x_{0}+h)-f(x_{0})-f'(x_{0})h\right)$ .
解 由 L'Hôpital 法则和已知条件可得

$$
\lim _ {h \to 0} \frac {f (x _ {0} + h) - f (x _ {0}) - f ^ {\prime} (x _ {0}) h}{h ^ {2}} = \lim _ {h \to 0} \frac {f ^ {\prime} (x _ {0} + h) - f ^ {\prime} (x _ {0})}{2 h} = \frac {1}{2} f ^ {\prime \prime} (x _ {0}).
$$

记 $x = x_0 + h$ ，则上式表明，如果 $f$ 在点 $x_0$ 处二阶可导，则

$$
f (x) - \left(f (x _ {0}) + f ^ {\prime} (x _ {0}) (x - x _ {0}) + \frac {1}{2} f ^ {\prime \prime} (x _ {0}) (x - x _ {0}) ^ {2}\right) = o ((x - x _ {0}) ^ {2}) \quad (x \to x _ {0}),
$$

即在点 $x_0$ 附近 $f(x)$ 可用二次多项式 $T_{2}$ 来逼近, 其中

$$
T _ {2} (x) = f (x _ {0}) + f ^ {\prime} (x _ {0}) (x - x _ {0}) + \frac {1}{2} f ^ {\prime \prime} (x _ {0}) (x - x _ {0}) ^ {2}.
$$

因此

$$
f (x) = T _ {2} (x) + o ((x - x _ {0}) ^ {2}) \quad (x \to x _ {0}).
$$

现在一个自然的问题是, 对于更一般情况, 如果 $f(x)$ 在点 $x_0$ 处具有 $n$ 阶导数, 是否可以用某个 $n$ 次多项式逼近? 即是否存在 $n$ 次多项式 $T_n(x)$, 使得下面相应的关系式成立:

$$
f (x) = T _ {n} (x) + o ((x - x _ {0}) ^ {n}) \quad (x \to x _ {0}).
$$

进一步, 如果成立的话, 那么  $T_{n}(x)$  的表达式能否给出? 下面的定理对这个问题给出了一个肯定的回答.

定理 7.3.1 (带 Peano 型余项的 Taylor 公式) 设  $f(x)$  在点  $x_{0}$  处 n 阶可导, 则

$$
f (x) = \sum_ {k = 0} ^ {n} \frac {f ^ {(k)} (x _ {0})}{k !} (x - x _ {0}) ^ {k} + o \big ((x - x _ {0}) ^ {n} \big) \quad (x \to x _ {0}), \tag {7.3.1}
$$

其中约定 $f^{(0)}(x) = f(x), (x - x_0)^0 = 1$.

证明 记

$$
T _ {n} (x) = \sum_ {k = 0} ^ {n} \frac {f ^ {(k)} (x _ {0})}{k !} (x - x _ {0}) ^ {k}, \tag {7.3.2}
$$

又记

$$
R _ {n} (x) = f (x) - T _ {n} (x). \tag {7.3.3}
$$

则

$$
R (x _ {0}) = R ^ {\prime} (x _ {0}) = \dots = R ^ {(n)} (x _ {0}) = 0.
$$

反复利用 L'Hôpital 法则可得

$$
\begin{array}{l} \lim _ {x \to x _ {0}} \frac {R (x)}{(x - x _ {0}) ^ {n}} = \lim _ {x \to x _ {0}} \frac {R ^ {\prime} (x)}{n (x - x _ {0}) ^ {n - 1}} = \dots = \lim _ {x \to x _ {0}} \frac {R ^ {(n - 1)} (x)}{n ! (x - x _ {0})} \\ = \lim _ {x \to x _ {0}} \frac {1}{n !} \frac {R ^ {(n - 1)} (x) - R ^ {(n - 1)} (x _ {0})}{x - x _ {0}} = \frac {1}{n !} R ^ {(n)} (x _ {0}) = 0, \\ \end{array}
$$

这说明  $R(x)=o\left((x-x_{0})^{n}\right)\quad(x\rightarrow x_{0}).$

我们给出几个基本概念,并澄清一下它们之间内涵上的异同.

定义 7.3.1 (Taylor 多项式、Taylor 展开式、展开式余项) 设  $f(x)$  在点  $x_{0}$  处 n 阶可导, 则称

$$
T _ {n} (x) = \sum_ {k = 0} ^ {n} \frac {f ^ {(k)} (x _ {0})}{k !} (x - x _ {0}) ^ {k}.
$$

为 $f(x)$ 的 $n$ 阶Taylor多项式. 表达式

$$
f (x) = \sum_ {k = 0} ^ {n} \frac {f ^ {(k)} (x _ {0})}{k !} (x - x _ {0}) ^ {k} + o \big ((x - x _ {0}) ^ {n} \big) \quad (x \to x _ {0}), \tag {7.3.4}
$$

称为 $f(x)$ 带 Peano 型余项的 Taylor 公式或称 Taylor 展开式, 称

$$
R _ {n} (x) = f (x) - T _ {n} (x) = o ((x - x _ {0}) ^ {n})
$$

为  $f(x)$  的 Taylor 展开式的余项.

特别地, 当 $x_0 = 0$ 时, $f(x)$ 的 $n$ 阶 Taylor 展开式称为函数的 $n$ 阶 Maclaurin$^{\text{①}}$ 展开式.

换句话说, $f(x)$ 在点 $x_0$ 的 $n$ 阶Taylor多项式 $T_{n}(x)$ 是一个阶数不高于 $n$ 次的多项式, 它与 $f(x)$ 在点 $x_0$ 处的所有不高于 $n$ 阶的导数都相等.

注7.3.1 由定理7.3.1可以看出，如果 $f(x)$ 在点 $x_0$ 处 $n$ 阶可导，且

$$
f ^ {\prime} (x _ {0}) = f ^ {\prime \prime} (x _ {0}) = \dots = f ^ {(n)} (x _ {0}) = 0,
$$

那么带 Peano 型余项的 Taylor 公式为

$$
f (x) = o \big ((x - x _ {0}) ^ {n} \big) \quad (x \to x _ {0}). \tag {7.3.5}
$$

但是, 需要注意的是, 反过来, 如果函数 $f(x)$ 在点 $x_0$ 处有估计式 (7.3.5), 则一般来说, 我们并不能得到 $f(x)$ 在点 $x_0$ 的连续性和可导性. 事实上, 无论多么大的 $n$, 我们只能证明: 假如 $f(x)$ 在点 $x_0$ 处连续, 那么它必定一阶可导, 但不一定二阶可导.

例如

$$
f (x) = \left\{ \begin{array}{l l} 0, & x = 0, \\ x ^ {n + 1} \sin \frac {1}{x ^ {n}}, & x \neq 0. \end{array} \right.
$$

则 $f(x)$ 在0点附近满足 $f(x) = o(x^n)(x\to 0)$ ，但 $f(x)$ 在 $x = 0$ 处的二阶导数并不存在.事实上，如果改变 $f(0) = 0$ 的值，那么 $f$ 在0点都不连续.

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">① Maclaurin, Colin, 1698 年 2 月 — 1746 年 6 月 14 日, 英国数学家.</span></small>

换句话说, 上面的注解告诉我们, 如果函数 $f(x)$ 没有高阶导数存在性的假设, 仅凭在点 $x_0$ 附近的估计式

$$
f (x) = P _ {n} (x) + o \big ((x - x _ {0}) ^ {n} \big) \quad (x \to x _ {0}),
$$

其中 $P_{n}(x)$ 是 $n$ 次多项式, 我们不能称 $P_{n}(x)$ 为 $f(x)$ 的Taylor多项式, 也得不到 $f''(x) - P_n''(x)$ 的任何估计, 因为 $f''(x_0)$ 可能根本不存在. 但是, 另一方面, 如果 $f(x)$ 的 $n$ 阶导数存在, 则可以得到两者各阶导数的相等性. 这一重要性质可以概括为下面的结论, 即Taylor展开式的唯一性. 唯一性这个结果为我们计算Taylor展开式提供了极大的灵活和方便; 反过来, 这一特点也为计算某函数在指定点处的高阶导数提供了可能.

引理 7.3.2 设对于常数  $a_{k}, b_{k} (0 \leqslant k \leqslant n)$ ，在点  $x_{0}$  附近有

$$
\sum_ {k = 0} ^ {n} a _ {k} (x - x _ {0}) ^ {k} = \sum_ {k = 0} ^ {n} b _ {k} (x - x _ {0}) ^ {k} + o \big ((x - x _ {0}) ^ {n} \big) \quad (x \to x _ {0}). \tag {7.3.6}
$$

则 $a_{k} = b_{k}$ $(0\leqslant k\leqslant n)$

证明 在 (7.3.6) 式两端令 $x \to x_0$ 即得 $a_0 = b_0$. 进而得到

$$
\sum_ {k = 1} ^ {n} a _ {k} (x - x _ {0}) ^ {k} = \sum_ {k = 1} ^ {n} b _ {k} (x - x _ {0}) ^ {k} + o \big ((x - x _ {0}) ^ {n} \big) \quad (x \to x _ {0}). \tag {7.3.7}
$$

于是, 在 (7.3.7) 式两端除以 $x - x_0$ 后再令 $x \to x_0$ 又可以得到 $a_1 = b_1$. 因此可得对任何 $0 \leqslant k \leqslant n$, $a_k = b_k$. □

我们把上述唯一性结论再以下面的方式重述一下. 证明同上述引理.

定理 7.3.3 (Taylor 公式系数的唯一性) 设  $f(x)$  在点  $x_{0}$  处 n 阶可导, 且

$$
f (x) = \sum_ {k = 0} ^ {n} a _ {k} (x - x _ {0}) ^ {k} + o \big ((x - x _ {0}) ^ {n} \big) (x \to x _ {0}),
$$

则

$$
a _ {k} = \frac {1}{k !} f ^ {(k)} (x _ {0}), k = 0, 1, \dots , n.
$$

例 7.3.2 求  $f(x)=\mathrm{e}^{x}$  的 n 阶 Maclaurin 展开式.

解 注意到  $\left.\frac{d^{n}e^{x}}{dx^{n}}\right|_{x=0}=e^{0}=1\quad(n=0,1,2,\cdots)$ ，所以有

$$
\mathrm{e} ^ {x} = 1 + x + \frac {1}{2 !} x ^ {2} + \dots + \frac {1}{n !} x ^ {n} + o (x ^ {n}) \quad (x \to 0).
$$

例 7.3.3 求  $f(x)=\sin x$  和  $g(x)=\cos x$  的 n 阶 Maclaurin 展开式.

解 通过直接计算不难得到

$$
\sin x = x - \frac {x ^ {3}}{3 !} + \frac {x ^ {5}}{5 !} - \dots + (- 1) ^ {n - 1} \frac {x ^ {2 n - 1}}{(2 n - 1) !} + o (x ^ {2 n}) \quad (x \to 0)
$$

和

$$
\cos x = 1 - \frac {x ^ {2}}{2 !} + \frac {x ^ {4}}{4 !} - \dots + (- 1) ^ {n} \frac {x ^ {2 n}}{(2 n) !} + o (x ^ {2 n + 1}) \quad (x \to 0).
$$

例 7.3.4 求  $f(x)=\arctan x$  的 n 阶 Maclaurin 展开式.

解 我们只需计算出 $f(x)$ 在 $x = 0$ 处的各阶导数 $f^{(n)}(0)$ 即可.

由  $(1+x^{2})f'(x)=1$ ，可以在等式两端对 x 求其 n 阶导数，并且利用 Leibniz 公式，得出

$$
(1 + x ^ {2}) f ^ {(n + 1)} (x) + 2 n x f ^ {(n)} (x) + n (n - 1) f ^ {(n - 1)} (x) = 0.
$$

将 x = 0 代入上式, 得

$$
f ^ {(n + 1)} (0) = - (n - 1) n f ^ {(n - 1)} (0).
$$

从而

$$
f ^ {(n)} (0) = \left\{ \begin{array}{l l} {0,} & {n \text {为偶数},} \\ {(- 1) ^ {k} (2 k)!,} & {n = 2 k + 1,} \end{array} \right.
$$

其中  $k=0,1,2,\cdots$ . 所以有

$$
\arctan x = \sum_ {k = 0} ^ {n} \frac {(- 1) ^ {k}}{2 k + 1} x ^ {2 k + 1} + o (x ^ {2 n + 2}) \quad (x \to 0).
$$

例 7.3.5 求下面函数的 n 阶 Maclaurin 展开式:

$$
\ln (1 + x), \quad (1 + x) ^ {\alpha}, \quad \frac {1}{1 + x}, \quad \arcsin x.
$$

我们可以给出类似的讨论和展式表达, 具体计算细节略:

$$
\ln (1 + x) = x - \frac {x ^ {2}}{2} + \frac {x ^ {3}}{3} + \dots + (- 1) ^ {n - 1} \frac {x ^ {n}}{n} + o (x ^ {n}) \quad (x \to 0).
$$

对于 $\alpha \in \mathbb{R}$, 当 $x > -1$, $x \to 0$ 时,

$$
(1 + x) ^ {\alpha} = 1 + \alpha x + \frac {\alpha (\alpha - 1)}{2 !} x ^ {2} + \dots + \frac {\alpha (\alpha - 1) \cdots (\alpha - n + 1)}{n !} x ^ {n} + o (x ^ {n}).
$$

特别地, 当  $\alpha = -1$  时,

$$
\frac {1}{1 + x} = 1 - x + x ^ {2} + \dots + (- 1) ^ {n} x ^ {n} + o (x ^ {n}) \quad (x \to 0).
$$

$$
\arcsin x = x + \frac {1}{3} \frac {1}{2 ! !} x ^ {3} + \frac {1}{5} \frac {3 ! !}{4 ! !} x ^ {5} + \dots + \frac {1}{2 n + 1} \frac {(2 n - 1) ! !}{(2 n) ! !} x ^ {2 n + 1} + o (x ^ {2 n + 2}) \quad (x \to 0).
$$

## 7.3.2 带 Lagrange 型余项的 Taylor 展开式

上面我们讨论了函数在一点附近用多项式逼近的问题, 相应的误差只是定性描述, 而非定量的估计, 所以它只适用于求无穷小量的阶或求极限等问题. 为了研究函数 (比如整个区间内) 的大范围估计, 就需要给出误差的定量描述. 带 Lagrange 型余项的 Taylor 公式可以回答这一问题.

定理 7.3.4 (带 Lagrange 型余项的 Taylor 公式) 设  $f(x)$  在区间  $(a, b)$  内有直到  $n+1$  阶的导数,  $x_{0}, x \in (a, b)$ . 则存在介于 x 与  $x_{0}$  之间的  $\xi$ , 使得

$$
f (x) = T _ {n} (x) + \frac {f ^ {(n + 1)} (\xi)}{(n + 1) !} (x - x _ {0}) ^ {n + 1} \quad (\mathrm{Lagrange} \text {型余项}).
$$

可以看出, 定理中如果 $n = 0$, 刚好是前面讨论过的 Lagrange 中值定理, 因为此时 $T_0(x) = f(x_0)$,

$$
f (x) - T _ {0} (x) = f (x) - f (x _ {0}) = f ^ {\prime} (\xi) (x - x _ {0}).
$$

所以上述定理可以看出是Lagrange中值定理的推广，余项 $R_{n}(x) = f(x) - T_{n}(x)$ 的表达形式也吻合Lagrange中值定理表述的推广.定理余项中的 $\xi$ 又常表示成

$$
\xi = x _ {0} + \theta (x - x _ {0}), \quad \text {其中} \quad 0 <   \theta <   1.
$$

下面给出定理的证明.

证明 可以反复使用 Cauchy 中值定理: 设  $T_{n}$  由 (7.3.2) 式给出的 Taylor 多项式, 则

$$
\begin{array}{l} \frac {f (x) - T _ {n} (x)}{(x - x _ {0}) ^ {n + 1}} = \frac {\left(f (x) - T _ {n} (x)\right) - \left(f (x _ {0}) - T _ {n} (x _ {0})\right)}{(x - x _ {0}) ^ {n + 1} - (x _ {0} - x _ {0}) ^ {n + 1}} \\ = \frac {f ^ {\prime} (\xi_ {1}) - T _ {n} ^ {\prime} (\xi_ {1})}{(n + 1) (\xi_ {1} - x _ {0}) ^ {n}} = \frac {f ^ {\prime \prime} (\xi_ {2}) - T _ {n} ^ {\prime \prime} (\xi_ {2})}{(n + 1) n (\xi_ {2} - x _ {0}) ^ {n - 1}} \\ = \dots = \frac {f ^ {(n)} (\xi_ {n}) - T _ {n} ^ {(n)} (\xi_ {n})}{(n + 1) ! (\xi_ {n} - x _ {0})} = \frac {f ^ {(n + 1)} (\xi)}{(n + 1) !}, \\ \end{array}
$$

其中  $\xi_{1}$  介于  $x_{0}$  与 x 之间,  $\xi_{2}$  介于  $x_{0}$  与  $\xi_{1}$  之间,  $\cdots$ ,  $\xi = \xi_{n+1}$  介于  $x_{0}$  与  $\xi_{n}$  之间. 定理得证. □

下面是几个常见函数的Lagrange型余项表达式.

$$
\mathrm{e} ^ {x} = 1 + \frac {x}{1 !} + \frac {x ^ {2}}{2 !} + \dots + \frac {x ^ {n}}{n !} + \frac {\mathrm{e} ^ {\theta x}}{(n + 1) !} x ^ {n + 1}, \quad x \in \mathbb {R}, 0 <   \theta <   1.
$$

$$
\sin x = x - \frac {x ^ {3}}{3 !} + \frac {x ^ {5}}{5 !} - \dots + (- 1) ^ {n - 1} \frac {x ^ {2 n - 1}}{(2 n - 1) !} + (- 1) ^ {n} \frac {\cos \theta x}{(2 n + 1) !} x ^ {2 n + 1}, x \in \mathbb {R}, 0 <   \theta <   1.
$$

$$
\cos x = 1 - \frac {x ^ {2}}{2 !} + \frac {x ^ {4}}{4 !} - \dots + (- 1) ^ {n} \frac {x ^ {2 n}}{(2 n) !} + (- 1) ^ {n + 1} \frac {\cos \theta x}{(2 n + 2) !} x ^ {2 n + 2}, x \in \mathbb {R}, 0 <   \theta <   1.
$$

$$
\ln (1 + x) = x - \frac {x ^ {2}}{2} + \frac {x ^ {3}}{3} + \dots + (- 1) ^ {n - 1} \frac {x ^ {n}}{n} + \frac {(- 1) ^ {n}}{n + 1} \frac {x ^ {n + 1}}{(1 + \theta x) ^ {n + 1}}, | x | <   1, 0 <   \theta <   1.
$$

在上述证明过程中, 我们也不难得到下面的一种余项表示, 称之为 Cauchy 型余项.

定理 7.3.5（带 Cauchy 型余项的 Taylor 公式）设  $f(x)$  在区间  $(a, b)$  内有直到  $n + 1$  阶的导数， $x_{0}, x \in (a, b)$ . 则存在介于 x 与  $x_{0}$  之间的  $\zeta$ ，使得

$$
f (x) = T _ {n} (x) + \frac {f ^ {(n + 1)} (\zeta)}{n !} (x - \zeta) ^ {n} (x - x _ {0}).
$$

只要考虑对函数 $F(t) = T_{n}(t) = \sum_{k=0}^{n}\frac{f^{(k)}(t)}{k!}(x - t)^{k}$ 和 $G(t) = \frac{x - t}{x - x_0}$ 在 $x$ 与 $x_0$ 之间应用Cauchy中值定理即可完成证明.

关于 Taylor 展开式余项更精细的估计方法有待于引入定积分理论后, 通过建立带积分型余项的 Taylor 展开式来实现.

Lagrange 型余项或 Cauchy 型余项的确能让我们对一个函数给出一个多项式逼近，并且能够估计在整个区间上的误差。这使得在应用中非常方便。

例 7.3.6 试用 10 次多项式在  $\left[-\frac{\pi}{2}, \frac{\pi}{2}\right]$  上逼近正弦函数  $\sin x$ ，并给出误差估计.

解 取 $\sin x$ 的 10 阶 Taylor 多项式 $T_{10}(x)$ 作为其逼近多项式

$$
T _ {1 0} (x) = x - \frac {x ^ {3}}{3 !} + \frac {x ^ {5}}{5 !} - \frac {x ^ {7}}{7 !} + \frac {x ^ {9}}{9 !},
$$

则

$$
| \sin x - T _ {1 0} (x) | \leqslant \frac {| x | ^ {1 1}}{1 1 !} \leqslant \frac {\pi^ {1 1}}{2 ^ {1 1} 1 1 !} <   3. 5 9 8 8 \times 1 0 ^ {- 6}.
$$

这个估计在整个区间 $\left[-\frac{\pi}{2},\frac{\pi}{2}\right]$ 上都成立，其精度还是相当高的.

## 习题7.3

1. 计算下列极限:

(1) $\lim_{x\to +\infty}x\left(\left(1 + \frac{1}{x}\right)^x -\mathrm{e}\right);$

(2) $\lim_{x\to +\infty}\left(\frac{\mathrm{e}}{2} x + x^2\left(\left(1 + \frac{1}{x}\right)^x -\mathrm{e}\right)\right);$

(3) $\lim_{x\to 0}(\cos x)^{1 / x^2}$;

(4) $\lim_{x\to 0}\frac{\sin^2x - x^2\cos x}{x^4}.$

2. 计算下列极限:

(1) $\lim_{x\to +\infty}x^{3 / 2}\left(\sqrt{x + 1} +\sqrt{x - 1} +2\sqrt{x}\right);$

(2) $\lim_{x\to 0}\frac{\cos x - \mathrm{e}^{-x^2 / 2}}{x^4};$

(3) $\lim_{x\to +\infty}x\left(\left(1 + \frac{1}{x}\right)^x -\mathrm{e}x\ln \left(1 + \frac{1}{x}\right)\right);$

(4) $\lim_{x\to 0}x\left(\frac{1}{x} -\cot x\right)$.

3. 计算函数 $f(x) = (7 + \cos x)^{\frac{-1}{3}}$ 的带 Peano 型余项的三阶 Maclaurin 展开式.

4. 将 $\sqrt[3]{1 + \sin^4 x}$ 在0点附近展开到 $x^{12}$.

5. 设函数 $f$ 在 $x = 1$ 处有三阶导数, 并满足 $f'(x) = f(f(x))$ 以及 $f(1) = 1$. 试求 $f$ 在 $x = 1$ 处的带 Peano 型余项的三阶 Taylor 展开式.

6. 设  $f(x)=\sin x\sin 2x\sin 3x \cdots \sin nx$ . 试计算  $f^{(n)}(0)$ .

7. 设函数 $y = y(x)$ 在 $x = 0$ 处有五阶导数, $y(0) = 0$, 其反函数 $x = x(y)$ 满足 $x = y - 3y^3 + 5y^5 + o(y^5)$ ($y \to 0$). 试求 $y(x)$ 带 Peano 型余项的五阶 Maclaurin 展开式.

8. 设函数 $y = y(x)$ 在 $x = 1$ 处有三阶导数, $y(1) = 0$, 其反函数 $x = x(y)$ 满足 $x = 1 + y + 3y^2 - 4y^3 + o(y^3)$ ($y \to 0$). 试求 $y(x)$ 在 $x = 1$ 处的带 Peano 型余项的三阶 Taylor 展开式.

9. 设定义在 0 点附近的光滑函数 $y = y(x)$ 满足 $y(0) = 0$ 以及 $x = \tan y - 2y$. 计算 $y(x)$ 在 $x = 0$ 处的带 Peano 型余项的五阶 Taylor 展开式.

10. 设光滑函数 $y = y(x)$ 满足 $x = \sqrt{y - \ln(1 + y)}\mathrm{sgn}(y)$. 试求 $y(x)$ 带 Peano 型余项的二阶 Maclaurin 展开式.

11. 设实数 $a, A, B$ 满足 $\lim_{x \to \infty} \left( A \left( \cos \frac{1}{x} + a \sin \frac{1}{x^2} + 2 \cos \frac{1}{x^3} + \sin \frac{1}{x^4} \right) \right)^{x^4} = B$. 试求 $a, A, B$.

12. 设 $f$ 在原点有二阶导数, 且 $\lim_{x\to 0}\left(\frac{\sin {3}x}{x^3} +\frac{f(x)}{x^2}\right) = 0$. 试求:

(1) $f(0),\quad f'(0),\quad f''(0);$

(2) $\lim_{x\to 0}\frac{f(x) + 3}{x^2}.$

13. 若 $f(x) = \sum_{k=0}^{n+1} a_k x^k + o(x^{n+1}) \quad (x \to 0)$，问是否有

$$
f ^ {\prime} (x) = \sum_ {k = 0} ^ {n} (k + 1) a _ {k + 1} x ^ {k} + o (x ^ {n}) \quad (x \to 0)
$$

成立？如果成立，请证明.如若不然，请举反例并且完善命题成立的条件.

14. 试把 $(- \infty, 0]$ 上的常值函数 $\ell(x) \equiv 0$ 和 $[1, +\infty)$ 上的常值函数 $r(x) \equiv 1$ 通过定义在 $[0, 1]$ 上的函数延拓为 $(- \infty, +\infty)$ 上的 $C^k$ 但不是 $C^{k+1}$ 函数, 其中 $k \geqslant 2$ 为自然数.

15. 设函数 $f$ 在 $\mathbb{R}$ 上有三阶导数, 且 ${M}_{0},{M}_{3} <  + \infty$ , 其中

$$
M _ {m} := \sup _ {x \in \mathbb {R}} | f ^ {(m)} (x) | \quad (m = 0, 1, 2, 3).
$$

证明: 存在与 $f$ 无关的常数 $C > 0$ 使得 $M_2 \leqslant CM_0^{\frac{1}{3}} M_3^{\frac{2}{3}}$.

16. 设 $n \geqslant 1$, 函数 $f$ 在 $\mathbb{R}$ 上有 $n + 1$ 阶导数, 且 $M_0, M_{n+1} < +\infty$, 其中

$$
M _ {m} := \sup _ {x \in \mathbb {R}} | f ^ {(m)} (x) | \quad (m = 0, 1, \dots , n + 1).
$$

证明: 对于 $1 \leqslant m \leqslant n$, 存在与 $f$ 无关的常数 $C_m > 0$ 使得 $M_m \leqslant C_m M_0^{1 - \frac{m}{n+1}} M_{n+1}^{\frac{m}{n+1}}$.

17. 设 $f$ 是 $[0, +\infty)$ 上的有界函数，并有三阶导数，且 $\lim_{x \to +\infty} f'''(x) = \alpha$，其中 $\alpha \in \mathbb{R}$.

(1) 证明: $\lim_{x\to +\infty}f''(x) = 0.$
(2) 问是否 $\lim_{x\to +\infty}f'(x) = 0$ 成立？如果假设 $\lim_{x\to +\infty}f(x) = 0,$ 证明: $\lim_{x\to +\infty}f'(x) = 0.$

18. 设 $f \in  {C}^{\infty }\left( \mathbb{R}\right) ,m$ 和 $n$ 为两正整数, $0 < m < n$ . 试讨论下面的问题:

(1) 如果 $\sup_{x\in \mathbb{R}}|f^{(m)}(x)|$ 和 $\sup_{x\in \mathbb{R}}|f^{(n)}(x)|$ 均有界, 证明: 对任意的自然数 $k, m < k < n, \sup_{x\in \mathbb{R}}|f^{(k)(x)}|$ 均有界.

(2) 如果 $\lim_{x\to +\infty}|f^{(m)}(x)|$ 和 $\lim_{x\to +\infty}|f^{(n)}(x)|$ 都存在且有限, 证明: 对任意的自然数 $k, m < k < n$, 极限 $\lim_{x\to +\infty}|f^{(k)}(x)|$ 也存在且有限, 并求其值.

(3) 如果 $\lim_{x\to +\infty}|f^{(m)}(x)|$ 存在且有限, $\sup_{x\in \mathbb{R}}|f^{(n)}(x)|$ 有界, 问对任意的自然数 $k, m < k < n$, 极限 $\lim_{x\to +\infty}|f^{(k)}(x)|$ 是否存在?

(4) 设 k 为正整数, 试分别对 k < m 和 k > n 两种情况, 重新讨论上面问题中的结论是否仍然成立.

19. 设数列 $\{a_{n}\}$ 有界, 满足

$$
\lim _ {n \to + \infty} \left(a _ {n + 2} - 2 a _ {n + 1} + a _ {n}\right) = 0,
$$

问是否有 $\lim_{n\to +\infty}\left(a_{n + 1} - a_n\right) = 0?$

20. 设 $f$ 在 $(-1,1)$ 内有定义, 在 0 点处二阶可导且 $f(0) = 0$. 证明

$$
\lim _ {n \to + \infty} \sum_ {k = - n} ^ {n} f \Big (\frac {k}{n ^ {\frac {3}{2}}} \Big) = \frac {1}{3} f ^ {\prime \prime} (0).
$$

21. 设函数 $f$ 在 $[0, +\infty)$ 上有二阶连续导数, 满足 $f(0) = f'(0) = 0$ 以及

$$
f ^ {\prime \prime} (x) + 3 f ^ {\prime} (x) + 2 f (x) \geqslant 0.
$$

证明: $f(x)\geqslant 0$ $(\forall x\in [0, + \infty))$

22. 设函数 $f$ 在区间 $[-1, 1]$ 上连续, 在 $(-1, 1)$ 内三阶可导. 证明: 存在 $\xi \in (-1, 1)$ 使得

$$
f ^ {\prime \prime \prime} (\xi) = 3 \Big (f (1) - f (- 1) - 2 f ^ {\prime} (0) \Big).
$$

23. 设函数 $f$ 为 $\mathbb{R}$ 上的有界可微函数, 且对任何 $x$ 均有 $|f'(x)| < 1$. 证明: 存在 $M < 1$ 使得对任何 $x \in \mathbb{R}$ 有 $|f(x) - f(0)| \leqslant M|x|$.

进一步, 是否有常数 $K < 1$ 使得对任何 $x, y \in \mathbb{R}$ 均有 $|f(x) - f(y)| \leqslant K|x - y|$?

24. 设函数 $f$ 是 $\mathbb{R}$ 上的连续可微函数, 且 $\forall x \in \mathbb{R}, f'(x) > f(f(x))$. 证明: $\forall x \geqslant 0, f(f(f(x))) \leqslant 0$.

25. 设 $c > \frac{1}{\mathrm{e}}$，证明:不存在在 $\mathbb{R}$ 上为正的可微函数 $f$ 使得 $f'(x) \geqslant f(x + c)$.

若 $0 < c \leqslant \frac{1}{\mathrm{e}}$，试寻找在 $\mathbb{R}$ 上为正的可微函数 $f$ 满足 $f'(x) \geqslant f(x + c)$.

26. 已知 $f(x) \in C^4[0,1]$, $p(x)$ 为三次多项式, 满足

$$
p (0) = f (0), \quad p ^ {\prime} (0) = f ^ {\prime} (0), \quad p (1) = f (1), \quad p ^ {\prime} (1) = f ^ {\prime} (1).
$$

证明:

$$
| f (x) - p (x) | \leqslant \frac {1}{3 8 4} \max | f ^ {(4)} | (x).
$$

27. 设函数  $f(x)$  在 R 上任意次可导，且  $f(0) = f'(0) = \cdots = f^{(k-1)}(0) = 0, f^{(k)}(0) \neq 0$ . 证明:函数  $g(x) = \frac{f(x)}{x^k}$  在 R 上也任意次可导.

## 7.4 Lagrange 插值多项式

插值是数值分析中离散函数逼近的重要方法, 它是在离散数据的基础上通过补插连续函数, 使得这个连续函数通过全部给定的离散数据点 $\{x_{i}, y_{i}\}$. 利用连续函数通过函数在有限个点处的取值状况, 可以估算出函数在其他点处的近似值.

连续函数类的选取可以非常灵活, 但合理的选取标准应该满足简单、方便、光滑性好等特点. 所以多项式函数类无疑应该是插值函数中最自然的函数类之一. 为此, 我们把多项式插值的具体提法明确一下:

给定一组 $n + 1$ 个数据点 $(x_0, y_0), (x_1, y_1), \dots, (x_n, y_n)$，其中 $x_0, x_1, \dots, x_n \in [a, b]$ 两两不同。假设这组数据来自某个（并不知道的）函数关系 $f(x)$，即

$$
y _ {i} = f (x _ {i}), \qquad i = 0, 1, \dots , n.
$$

我们希望寻求一个多项式 $P(x)$ ，它刚好通过这些给定的数据点，即

$$
P (x _ {i}) = y _ {i}, \quad i = 0, 1, \dots , n. \tag {7.4.1}
$$

对于给定的插值数据 $\{(x_i,y_i)\}_{i = 0}^n$ ，满足条件(7.4.1)的多项式 $P(x)$ 称为 $f(x)$ 的插值多项式.

初步分析可以看出, 如果存在满足插值数据的插值多项式 $P(x)$, 一般来说, $P(x)$ 应该有 $n + 1$ 个参数. 所以这又使得我们自然而然地在所有 $n$ 次多项式集合中寻找满足这些条件的 $P_{n}(x)$.