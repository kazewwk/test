## 习题5.4

1. 考虑

$$
f (x) := \left\{ \begin{array}{l l} x \sin \frac {1}{x ^ {2}}, & x \in (0, 1 ], \\ 0, & x = 0. \end{array} \right.
$$

试证明 $f$ 在 $[0,1]$ 上连续并考察 $f$ 在 $[0,1]$ 上是否满足 Hölder 条件.

2. 考虑

$$
f (x) := \left\{ \begin{array}{l l} x \sin \mathrm{e} ^ {\frac {1}{x}}, & x \in (0, 1 ], \\ 0, & x = 0. \end{array} \right.
$$

试证明 $f$ 在 $[0,1]$ 上连续并考察 $f$ 在 $[0,1]$ 上是否满足 Hölder 条件.

3. 试构造 $\mathbb{R}$ 上的函数 $f$ 使得 $|f(x) - f(y)| < |x - y|$ 对任何 $x \neq y$ 成立, 但 $f$ 没有不动点.
4. 设 $f$ 为 $\mathbb{R}$ 上的有界函数, 且对任何 $x \neq y$ 有 $|f(x) - f(y)| < |x - y|$. 任取 $x_0 \in \mathbb{R}$, 并设 $x_{n+1} = f(x_n) (n \geqslant 0)$. 证明: $\{x_n\}$ 收敛.
5. 设 $f$ 是 $\mathbb{R}$ 上周期为 1 的函数, 满足 $|f(x) - f(y)| \leqslant |x - y|$ $(x, y \in \mathbb{R})$. 考察函数 $g(x) = x + f(x)$. 任取 $x_0 \in \mathbb{R}$, 令 $x_{n+1} = g(x_n) (n \geqslant 0)$. 证明: $\lim_{n \to +\infty} \frac{x_n}{n}$ 存在且不依赖于 $x_0$ 的选择.

## 5.5 指数函数、对数函数和三角函数的定义

利用上确界存在定理, 我们在第二章定义了正数 $a$ 的 $n$ 次方根 $a^{\frac{1}{n}}$, 并由此出发定义了实指数幂 $a^{b}$ 以及对数 $\log_{a} b$. 这一定义过程比较自然, 但较为烦琐. 以下我们展示如何通过极限或级数直接定义 $\mathrm{e}^{x}$, 然后再来定义其他相关函数的过程. 另一方面, 我们也将用极限或级数来定义三角函数, 这一过程比较简捷, 但相对说来, 缺乏直观.

关于通过积分定义对数函数 $\ln x$ ，然后再定义指数函数的过程，可参见文献[42]第四章第2节或文献[44]第八章附录.关于利用微分方程定义三角函数，可参见文献[43]第四章第4节.关于利用积分定义三角函数，可参见文献[44]第八章附录.

在接下来的讨论中, 我们将利用极限或级数一并定义指数函数与三角函数. 自然, 如下的讨论中, 之前已经得到的指数函数和对数函数的性质以及我们承认的三角函数的性质都将从零开始加以建立.

## 5.5.1 复指数函数

为减少重复讨论, 我们直接引入复指数函数.

定义 5.5.1 对于 $z \in \mathbb{C}$, 定义

$$
\exp (z) := \lim _ {n \to + \infty} \left(1 + \frac {z}{n}\right) ^ {n}. \tag {5.5.1}
$$

我们有

定理5.5.1 对任何 $z\in \mathbb{C}$ ， $\exp (z)$ 是合理定义的，且

$$
\exp (z) = \sum_ {n = 0} ^ {\infty} \frac {z ^ {n}}{n !}. \tag {5.5.2}
$$

证明 证明完全类似于 (5.2.18) 式的证明.

由单调收敛定理得级数 $\sum_{n=0}^{\infty} \frac{|z|^n}{n!}$ 收敛. 而由 Cauchy 收敛准则得到 $\sum_{n=0}^{\infty} \frac{z^n}{n!}$ 也收敛. 于是, 固定 $m \geqslant 2$, 当 $n \geqslant m$ 时, 利用二项展开式, 有

$$
\begin{array}{l} \left| \left(1 + \frac {z}{n}\right) ^ {n} - \sum_ {k = 0} ^ {\infty} \frac {z ^ {k}}{k !} \right| \\ \leqslant \left| \sum_ {k = 0} ^ {m} \frac {z ^ {k}}{k !} - \left(1 + z + \frac {z ^ {2}}{2 !} \left(1 - \frac {1}{n}\right) + \dots + \frac {z ^ {m}}{m !} \prod_ {k = 1} ^ {m - 1} \left(1 - \frac {k}{n}\right)\right) \right| + 2 \sum_ {k = m + 1} ^ {\infty} \frac {| z | ^ {k}}{k !}. \\ \end{array}
$$

上式中令 $n\to +\infty$ 可得

$$
\varlimsup_ {n \to + \infty} \left| \left(1 + \frac {z}{n}\right) ^ {n} - \sum_ {k = 0} ^ {\infty} \frac {z ^ {k}}{k !} \right| \leqslant 2 \sum_ {k = m + 1} ^ {\infty} \frac {| z | ^ {k}}{k !}.
$$

再令 $m\to +\infty$ 即得 $\lim_{n\to +\infty}\left(1 + \frac{z}{n}\right)^n$ 存在且(5.5.2)式成立.

我们有如下重要的结果.

定理 5.5.2 设  $z, w \in C, n \in Z$ ，则

(1)  $\exp(z+w)=\exp(z)\exp(w);$
(2) $\left(\exp (z)\right)^n = \exp (nz)$.

证明 (1) 证法 1 任取整数 $k \geqslant 2|z + w|$, 我们有

$$
\left(1 + \frac {z}{k}\right) ^ {k} \left(1 + \frac {w}{k}\right) ^ {k} = \left(1 + \frac {z + w}{k} + \frac {z w}{k ^ {2}}\right) ^ {k} = \left(1 + \frac {z + w}{k}\right) ^ {k} \left(1 + \frac {\frac {z w}{k ^ {2}}}{1 + \frac {z + w}{k}}\right) ^ {k}. \tag {5.5.3}
$$

而由二项展开式，

$$
\left| \left(1 + \frac {\frac {z w}{k ^ {2}}}{1 + \frac {z + w}{k}}\right) ^ {k} - 1 \right| \leqslant \sum_ {j = 1} ^ {k} \frac {1}{j !} \left| \frac {\frac {z w}{k ^ {2}}}{1 + \frac {z + w}{k}} \right| ^ {j} \leqslant \frac {1}{k} \sum_ {j = 1} ^ {k} \frac {(2 | z w |) ^ {j}}{j !} \leqslant \frac {1}{k} \exp (2 | z w |). \tag {5.5.4}
$$

结合 (5.5.3) 式和 (5.5.4) 式得 $\exp (z + w) = \exp (z)\exp (w)$.

证法 2 任取整数  $N \geqslant 2$ ，由二项展开式，我们有

$$
\Big|\sum_{m = 0}^{N}\frac{(z + w)^{m}}{m!} -\sum_{k = 0}^{N}\frac{z^{k}}{k!}\sum_{j = 0}^{N}\frac{w^{j}}{j!}\Big| = \Big|\sum_{m = 0}^{N}\sum_{\substack{0\leqslant k,j\leqslant N\\ k + j = m}}\frac{z^{k}w^{j}}{k!\cdot j!} -\sum_{m = 0}^{2N}\sum_{\substack{0\leqslant k,j\leqslant N\\ k + j = m}}\frac{z^{k}w^{j}}{k!\cdot j!}\Big|
$$

$$
\begin{array}{l} = \left|\sum_{m = N + 1}^{2N}\sum_{\substack{0\leqslant k,j\leqslant N\\ k + j = m}}\frac{z^kw^j}{k!\cdot j!}\right| \\ \leqslant \sum_ {m = N + 1} ^ {2 N} \sum_ {\substack {0 \leqslant k, j \leqslant N \\ k + j = m}} \frac {| z | ^ {k} | w | ^ {j}}{k ! \cdot j !} \leqslant \sum_ {m = N + 1} ^ {\infty} \frac {(| z | + | w |) ^ {m}}{m !}. \\ \end{array}
$$

令  $m \rightarrow +\infty$  即得  $\exp(z + w) = \exp(z) \exp(w)$ .

(2) 由 (1) 立即可得对任何整数 $n \geqslant 1$, $\left(\exp(z)\right)^n = \exp(nz)$ 成立. 另一方面, 由 (1), $\exp(z) \exp(-z) = \exp(0) = 1$. 因此, $\exp(z) \neq 0$, $\left(\exp(z)\right)^{-1} = \exp(-z)$. 由此可得对任何整数 $n \leqslant 0$, $\left(\exp(z)\right)^n = \exp(nz)$ 也成立.

鉴于以上定理, 以下记  $\exp(z)$  为  $e^{z}$ , 其中  $e = \exp(1)$ .

## 5.5.2 自然指数函数与自然对数函数

定理 5.5.3 函数  $e^{x}$  在 R 上恒正、连续、严格单增，且值域为  $(0, +\infty)$ .

证明 易见 $\mathrm{e}^x$ 在 $[0, +\infty)$ 上恒正, 且严格单增. 结合 $\mathrm{e}^{-x} = (\mathrm{e}^{x})^{-1}$ 即得 $\mathrm{e}^x$ 在 $\mathbb{R}$ 上恒正, 且严格单增.

利用 (5.5.2) 式, 易得当  $|x| \leqslant 1$  时,

$$
\left| \mathrm{e} ^ {x} - 1 \right| \leqslant \sum_ {n = 1} ^ {\infty} \frac {| x | ^ {n}}{n !} \leqslant | x | \sum_ {n = 1} ^ {\infty} \frac {1}{n !} = (\mathrm{e} - 1) | x |.
$$

从而 $\lim_{x\to 0}\mathrm{e}^x = 1$ ，即 $\mathrm{e}^x$ 在 $x = 0$ 连续.结合 $\mathrm{e}^x = \mathrm{e}^{x_0}\mathrm{e}^{x - x_0}$ 得到 $\mathrm{e}^x$ 在 $\mathbb{R}$ 上连续

另一方面, 易见 $\lim_{x\to +\infty}e^x = +\infty$. 结合 $e^{-x} = (e^x)^{-1}$ 得到 $\lim_{x\to -\infty}e^x = 0$. 于是, 由介值定理, 知 $e^x$ 的值域为 $(0, +\infty)$. □

定义 5.5.2 称 R 上的函数  $e^{x}$  为自然指数函数, 称  $e^{x}$  的反函数为自然对数函数, 记作  $\ln(x)$  (常简记为  $\ln x$ ), 即  $\ln x$  满足  $e^{\ln x} = x$ .

由定理5.5.2和5.5.3可得

定理 5.5.4 函数  $\ln x$  的自然定义域为  $(0, +\infty)$ ，值域为 R，它在  $(0, +\infty)$  上连续、严格单增，且对任何 x, y > 0 以及  $n \in Z$ ，有

(1)  $\ln 1 = 0;$
(2)  $\ln(xy)=\ln x+\ln y;$
(3) $\ln x^n = n\ln x$.

## 5.5.3 一般的指数函数与对数函数

定义 5.5.3 对于 a > 0 以及  $b, c \in R$ ，定义  $a^{b} := e^{b \ln a}$ .

进一步, 若  $a \neq 1$ , 定义  $a^{x}$  的反函数为  $\log_{a} x$ , 即  $a^{\log_{a} x} = x$ .

易见当 $a = \mathrm{e}$ 时, $a^b$ 与 $\mathrm{e}^b$ 是一致的, 而 $\log_{\mathrm{e}}x = \ln x$. 进一步, 有 $(a^{b})^{c} = a^{bc}, a^{b}a^{c} = a^{b + c}$. 特别地, 可得 $(\mathrm{e}^{x})^{y} = \mathrm{e}^{xy}, (a^{\frac{1}{n}})^{n} = a$ 等.

而对于 $a > 0, a \neq 1$, 有 $\log_a x = \frac{\ln x}{\ln a}$.

当 $x > 0$ 时, 可以补充定义 $0^x = 0$. 而当 $x$ 是分母为奇数的有理数 $\frac{m}{2n + 1}$ 时, 可以补充定义 $(-a)^{\frac{m}{2n + 1}} = (-1)^m a^{\frac{m}{2n + 1}}$.

## 5.5.4 三角函数

我们只给出正弦函数和余弦函数的定义并建立相关性质. 其余函数的性质易由正弦函数和余弦函数的性质导出.

定义 5.5.4 定义正弦函数 sin 和余弦函数 cos 如下:

$$
\sin x = \operatorname{Im} \mathrm{e} ^ {\mathrm{i} x} = \sum_ {n = 0} ^ {\infty} \frac {(- 1) ^ {n}}{(2 n + 1) !} x ^ {2 n + 1}, \quad x \in \mathbb {R}, \tag {5.5.5}
$$

$$
\cos x = \operatorname{Re} \mathrm{e} ^ {\mathrm{i} x} = \sum_ {n = 0} ^ {\infty} \frac {(- 1) ^ {n}}{(2 n) !} x ^ {2 n}, \quad x \in \mathbb {R}. \tag {5.5.6}
$$

显然, sin 是奇函数, cos 是偶函数. 自然, Euler 公式

$$
\mathrm{e} ^ {\mathrm{i} x} = \cos x + \mathrm{i} \sin x, \quad x \in \mathbb {R} \tag {5.5.7}
$$

成立. 进一步, 我们有如下结果.

## 定理 5.5.5 (1) Pythagoras 恒等式

$$
\sin^ {2} x + \cos^ {2} x = 1, \quad \forall x \in \mathbb {R} \tag {5.5.8}
$$

成立;

$$
\lim _ {x \to 0} \frac {\sin x}{x} = 1; \tag {5.5.9}
$$

(3) sin, cos 是 R 上的连续函数;
(4) $\sin$ 有最小正零点, 设为 $\pi^{①}$, $\sin$ 在 $(0, \pi)$ 内恒正;
(5) $2\pi$ 是 $\sin$ 以及 $\cos$ 的最小正周期, $\sin \frac{\pi}{2} = 1$, $\cos \pi = -1$.

证明 (1) 我们有

$$
\sin^ {2} x + \cos^ {2} x = | \cos x + \mathrm{i} \sin x | ^ {2} = | \mathrm{e} ^ {\mathrm{i} x} | ^ {2} = \mathrm{e} ^ {\mathrm{i} x} \overline {{\mathrm{e} ^ {\mathrm{i} x}}} = \mathrm{e} ^ {\mathrm{i} x} \mathrm{e} ^ {- \mathrm{i} x} = \mathrm{e} ^ {0} = 1.
$$

即 (5.5.8) 式成立.

(2) 对于 $0 < |x| \leqslant 1$, 我们有

$$
\left| \frac {\sin x}{x} - 1 \right| = \left| \sum_ {n = 1} ^ {\infty} \frac {(- 1) ^ {n}}{(2 n + 1) !} x ^ {2 n} \right| \leqslant x ^ {2} \sum_ {n = 1} ^ {\infty} \frac {1}{(2 n + 1) !}.
$$

于是由夹逼准则即得 (5.5.9) 式.

(3) 对任何 $x, y \in \mathbb{R}$, 若 $|x - y| \leqslant 1$, 则

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">① 注意, 到这一步,  $\pi$  还没有与圆周率相关联.</span></small>

$$
\begin{array}{l} \left| \sin x - \sin y \right| ^ {2} + \left| \cos x - \cos y \right| ^ {2} = \left| \cos x - \cos y + \mathrm{i} (\sin x - \sin y) \right| ^ {2} \\ = \left| \mathrm{e} ^ {\mathrm{i} x} - \mathrm{e} ^ {\mathrm{i} y} \right| ^ {2} = \left| \mathrm{e} ^ {\mathrm{i} y} \left(\mathrm{e} ^ {\mathrm{i} (x - y)} - 1\right) \right| ^ {2} \\ = \left| \mathrm{e} ^ {\mathrm{i} y} \right| ^ {2} \cdot \left| \mathrm{e} ^ {\mathrm{i} (x - y)} - 1 \right| ^ {2} = \left| \sum_ {n = 1} ^ {\infty} \frac {\mathrm{i} ^ {n} (x - y) ^ {n}}{n !} \right| ^ {2} \\ \leqslant \left(\sum_ {n = 1} ^ {\infty} \frac {| x - y | ^ {n}}{n !}\right) ^ {2} \leqslant \left(\sum_ {n = 1} ^ {\infty} \frac {1}{n !}\right) ^ {2} | x - y | ^ {2}. \\ \end{array}
$$

于是由夹逼准则即得 $\sin, \cos$ 在 $\mathbb{R}$ 上连续.

(4) 我们有  $\cos 0 = 1$ ,

$$
\begin{array}{l} \cos 2 = \sum_ {n = 0} ^ {\infty} \frac {(- 1) ^ {n} 2 ^ {2 n}}{(2 n) !} \\ = 1 - \frac {2 ^ {2}}{2 !} + \frac {2 ^ {4}}{4 !} - \sum_ {k = 1} ^ {\infty} \left(\frac {2 ^ {4 k + 2}}{(4 k + 2) !} - \frac {2 ^ {4 k + 4}}{(4 k + 4) !}\right) \\ = - \frac {1}{3} - \sum_ {k = 1} ^ {\infty} \frac {2 ^ {4 k + 2}}{(4 k + 2) !} \left(1 - \frac {4}{(4 k + 4) (4 k + 3)}\right) <   0. \\ \end{array}
$$

由介值定理, 有 $\beta > 0$ 使得 $\cos \beta = 0$. 此时, 由 (5.5.8) 式, $\sin \beta = \pm 1$. 即 $e^{\beta i} = \pm i$. 从而 $e^{4\beta i} = (\pm i)^4 = 1$. 因此 $\sin 4\beta = 0$. 即 $4\beta$ 是 $\sin$ 的正零点. 而由 (2), 存在 $\delta > 0$ 使得 $\forall x \in (0, \delta)$, 有 $\sin x > 0$. 因此, $\sin$ 有最小正零点. 结合介值定理可得对于这个最小正零点 $\pi$, $\sin$ 在 $(0, \pi)$ 内恒正.

(5) 由 (5.5.8) 式, $\cos \pi = \pm 1$. 我们断言, $\cos \pi = -1$. 否则, $e^{i\pi} = 1$. 从而 $\left(e^{i\frac{\pi}{2}}\right)^2 = 1$. 于是 $e^{i\frac{\pi}{2}} = \pm 1$. 由此即得 $\sin \frac{\pi}{2} = 0$. 这与 $\pi$ 为 $\sin$ 的最小正零点矛盾.

因此, $e^{i\pi}=-1$ ,进而 $e^{2\pi i}=1$ .即得 $2\pi$ 是sin,cos的正周期.

由 $\sin$ 在 $(0, \pi)$ 内恒正知 $\sin$ 有最小正周期，且最小正周期只能是 $\pi$ 或 $2\pi$。又由于 $\sin$ 是奇函数，$\sin$ 在 $(- \pi, 0)$ 内为负。因此，$\sin$ 的最小正周期必然是 $2\pi$。同理，由 $\cos 0 = 1$ 以及 $\cos \pi = -1$ 可见，$\cos$ 的最小正周期也是 $2\pi$。

另一方面，由 $\left(\mathrm{e}^{\mathrm{i}\frac{\pi}{2}}\right)^2 = \mathrm{e}^{\mathrm{i}\pi} = -1$ 可得 $\mathrm{e}^{\mathrm{i}\frac{\pi}{2}} = \pm \mathrm{i}$. 因此，$\sin \frac{\pi}{2} = \pm 1$. 结合 $\sin$ 在 $(0, \pi)$ 内恒正得到 $\sin \frac{\pi}{2} = 1$.

正弦函数和余弦函数的很多常用性质可以由 $\mathrm{e}^{\mathrm{i}(x + y)} = \mathrm{e}^{\mathrm{i}x}\mathrm{e}^{\mathrm{i}y}$ 得到.

首先, 由该式立即可得正弦函数和余弦函数的和角公式 $^{①}$ 、倍角公式、积化和差公式与和差化积公式等.

具体地, 将  $\mathrm{e}^{\mathrm{i}(x\pm y)}=\mathrm{e}^{\mathrm{i}x}\mathrm{e}^{\pm\mathrm{i}y}$  两边展开并比较实部和虚部得到和角公式:

$$
\left\{ \begin{array}{l} \cos (x + y) = \cos x \cos y - \sin x \sin y, \\ \sin (x + y) = \sin x \cos y + \cos x \sin y, \\ \cos (x - y) = \cos x \cos y + \sin x \sin y, \\ \sin (x - y) = \sin x \cos y - \cos x \sin y. \end{array} \right. \tag {5.5.10}
$$

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">① 按目前的定义, $\sin x, \cos x$ 中的自变量与角度没有关系. 这里只是采用习惯的称呼.</span></small>

在(5.5.10)式的第一、第二式中令 $y = x$ ，亦即利用 $\mathrm{e}^{2\mathrm{i}x} = \left(\mathrm{e}^{\mathrm{i}x}\right)^{2}$ 得到倍角公式

$$
\left\{ \begin{array}{l} \cos 2 x = \cos^ {2} x - \sin^ {2} x, \\ \sin 2 x = 2 \sin x \cos x. \end{array} \right. \tag {5.5.11}
$$

一般地, 可以利用  $\mathrm{e}^{\mathrm{i}nx} = \left(\mathrm{e}^{\mathrm{i}x}\right)^{n}$  将  $\cos nx$  和  $\sin nx$  展开成  $\cos x, \sin x$  的多项式.

取 $\varepsilon_1, \varepsilon_2$ 为1或-1，由

$$
(\mathrm{e} ^ {\mathrm{i} x} + \varepsilon_ {1} \mathrm{e} ^ {- \mathrm{i} x}) (\mathrm{e} ^ {\mathrm{i} y} + \varepsilon_ {2} \mathrm{e} ^ {- \mathrm{i} y}) = \mathrm{e} ^ {\mathrm{i} (x + y)} + \varepsilon_ {1} \mathrm{e} ^ {- \mathrm{i} (x - y)} + \varepsilon_ {2} \mathrm{e} ^ {\mathrm{i} (x - y)} + \varepsilon_ {1} \varepsilon_ {2} \mathrm{e} ^ {- \mathrm{i} (x + y)}
$$

可得积化和差公式

$$
\left\{ \begin{array}{l} 2 \cos x \cos y = \cos (x + y) + \cos (x - y), \\ - 2 \sin x \sin y = \cos (x + y) - \cos (x - y), \\ 2 \sin x \cos y = \sin (x + y) + \sin (x - y), \\ 2 \cos x \sin y = \sin (x + y) - \sin (x - y). \end{array} \right. \tag {5.5.12}
$$

在(5.5.12)式中用 $\frac{x + y}{2},\frac{x - y}{2}$ 代替 $x,y$ 即得和差化积公式

$$
\left\{ \begin{array}{l} \cos x + \cos y = 2 \cos \frac {x + y}{2} \cos \frac {x - y}{2}, \\ \cos x - \cos y = - 2 \sin \frac {x + y}{2} \sin \frac {x - y}{2}, \\ \sin x + \sin y = 2 \sin \frac {x + y}{2} \cos \frac {x - y}{2}, \\ \sin x - \sin y = 2 \cos \frac {x + y}{2} \sin \frac {x - y}{2}. \end{array} \right. \tag {5.5.13}
$$

再者, 利用  $\mathrm{e}^{\mathrm{i}\left(\frac{\pi}{2}-x\right)}=\mathrm{e}^{\mathrm{i}\frac{\pi}{2}}\mathrm{e}^{-\mathrm{i}x}=\mathrm{i}\mathrm{e}^{-\mathrm{i}x}$  可得余角公式

$$
\left\{ \begin{array}{l l} \sin \left(\frac {\pi}{2} - x\right) = \cos x, \\ \cos \left(\frac {\pi}{2} - x\right) = \sin x, \end{array} \right. \quad \forall x \in \mathbb {R}. \tag {5.5.14}
$$

利用 $\mathrm{e}^{\mathrm{i}(\pi -x)} = \mathrm{e}^{\mathrm{i}\pi}\mathrm{e}^{-\mathrm{i}x} = -\mathrm{e}^{-\mathrm{i}x}$ 可得补角公式

$$
\left\{ \begin{array}{l} \sin (\pi - x) = \sin x, \\ \cos (\pi - x) = - \cos x, \end{array} \quad \forall x \in \mathbb {R}. \right. \tag {5.5.15}
$$

由余角公式可得 $\cos$ 在 $\left(0, \frac{\pi}{2}\right)$ 内为正. 这样, 对于 $0 \leqslant x < y \leqslant \frac{\pi}{2}$, 由和差化积公式,

$$
\sin y - \sin x = 2 \cos {\frac {x + y}{2}} \sin {\frac {y - x}{2}} > 0.
$$

因此，$\sin$ 在 $\left[0, \frac{\pi}{2}\right]$ 上严格单增。结合 $\sin$ 为奇函数可得 $\sin$ 在 $\left[-\frac{\pi}{2}, \frac{\pi}{2}\right]$ 上严格单增。利用 $\sin (x + \pi) = -\sin x$ 可得 $\sin$ 在 $\left[\frac{\pi}{2}, \frac{3\pi}{2}\right]$ 上严格单减。

进一步, 易得  $\cos x = \sin\left(x + \frac{\pi}{2}\right)$ , 进而  $\cos$  在  $[0, \pi]$  上严格单减, 在  $[\pi, 2\pi]$  上严格单增.

利用上述性质, 容易得到 sin, cos 在一些特殊点的值. 例如

$$
\sin \frac {\pi}{4} = \cos \frac {\pi}{4} = \sqrt {\frac {2 \sin \frac {\pi}{4} \cos \frac {\pi}{4}}{2}} = \sqrt {\frac {\sin \frac {\pi}{2}}{2}} = \frac {\sqrt {2}}{2}.
$$

由

$$
\cos \frac {\pi}{6} = \sin \left(\frac {\pi}{2} - \frac {\pi}{6}\right) = \sin \frac {2 \pi}{6} = 2 \sin \frac {\pi}{6} \cos \frac {\pi}{6}
$$

得到 $\cos \frac{\pi}{3} = \sin \frac{\pi}{6} = \frac{1}{2}$ 进而

$$
\sin \frac {\pi}{3} = \cos \frac {\pi}{6} = \sqrt {1 - \sin^ {2} \frac {\pi}{6}} = \frac {\sqrt {3}}{2}.
$$

## 5.5.5 圆周率

现在考虑平面 $\mathbb{R}^2$ 中的单位圆周 $x^{2} + y^{2} = 1$ ，则利用正弦函数和余弦函数，它可以用参数表示为

$$
\left\{ \begin{array}{l} x = \cos t, \\ y = \sin t, \end{array} \right. \quad t \in [ 0, 2 \pi ].
$$

任取  $n \geqslant 3$ ，将参数的取值区间作 n 等分，得到圆周的内接 n 边形（图 5.1），其周长为

$$
\begin{array}{l} L _ {n} = \sum_ {k = 1} ^ {n} \left| \mathrm{e} ^ {\mathrm{i} \frac {2 k \pi}{n}} - \mathrm{e} ^ {\mathrm{i} \frac {2 (k - 1) \pi}{n}} \right| = \sum_ {k = 1} ^ {n} \left| \mathrm{e} ^ {\mathrm{i} \frac {2 (k - 1) \pi}{n}} \right| \cdot \left| \mathrm{e} ^ {\mathrm{i} \frac {2 \pi}{n}} - 1 \right| \\ = n \sqrt {\left(\cos \frac {2 \pi}{n} - 1\right) ^ {2} + \sin^ {2} \frac {2 \pi}{n}} = n \sqrt {2 - 2 \cos \frac {2 \pi}{n}} \\ = 2 n \sin \frac {\pi}{n}. \\ \end{array}
$$

由(5.5.9)式可得

$$
\lim _ {n \to + \infty} L _ {n} = 2 \pi.
$$

从推导过程可以看出, 上面的内接 n 边形是内接正 n 边形. 进一步可以证明, 对任何  $\varepsilon > 0$ , 存在  $\delta > 0$ , 使得对任何  $0 = \theta_{0} < \theta_{1} < \theta_{2} < \cdots < \theta_{m} = 2\pi$ , 只要  $\max_{1 \leqslant k \leqslant m} (\theta_{k} - \theta_{k-1}) < \delta$ , 就有

$$
\Big | \sum_ {k = 1} ^ {m} \big | \mathrm{e} ^ {\mathrm{i} \theta_ {k}} - \mathrm{e} ^ {\mathrm{i} \theta_ {k - 1}} \big | - 2 \pi \Big | <   \varepsilon .
$$

这相当于说单位圆周的周长是  $2\pi$ .

![](images/page_135_image_2.jpg)

<details>
<summary>text_image</summary>

(cos 4π/n, sin 4π/n)
(cos 2π/n, sin 2π/n)
</details>

图5.1

另一方面, 由 $\cos 2 < 0$ 可得 $\frac{\pi}{2} < 2$, 即 $\pi < 4$. 则当 $x \in \left(0, \frac{\pi}{2}\right)$ 时,

$$
\sin x - x = \sum_ {n = 1} ^ {\infty} \frac {(- 1) ^ {n} x ^ {2 n + 1}}{(2 n + 1) !} = - \sum_ {n = 0} ^ {\infty} \Big (\frac {1}{(4 n + 3) !} - \frac {x ^ {2}}{(4 n + 5) !} \Big) x ^ {4 n + 3}
$$

$$
= - \sum_ {n = 0} ^ {\infty} \left(1 - \frac {x ^ {2}}{(4 n + 4) (4 n + 5)}\right) \frac {x ^ {4 n + 3}}{(4 n + 3) !} <   0,
$$

$$
\begin{array}{l} \sin x + x - 4 \sin \frac {x}{2} = \sum_ {n = 1} ^ {\infty} \frac {(- 1) ^ {n} x ^ {2 n + 1}}{(2 n + 1) !} - 4 \sum_ {n = 1} ^ {\infty} \frac {(- 1) ^ {n} x ^ {2 n + 1}}{2 ^ {2 n + 1} (2 n + 1) !} \\ = - \sum_ {n = 0} ^ {\infty} \left((1 - \frac {1}{2 ^ {4 n + 1}}) - (1 - \frac {1}{2 ^ {4 n + 3}}) \frac {x ^ {2}}{(4 n + 4) (4 n + 5)}\right) \frac {x ^ {4 n + 3}}{(4 n + 3) !} \\ <   - \sum_ {n = 0} ^ {\infty} \left(\frac {1}{2} - 1 \cdot \frac {1}{5}\right) \frac {x ^ {4 n + 3}}{(4 n + 3) !} <   0. \\ \end{array}
$$

这就得到了

$$
\sin x <   x <   4 \sin \frac {x}{2} - \sin x, \quad \forall x \in \left(0, \frac {\pi}{2}\right). \tag {5.5.16}
$$

自然, 今后引入导数以后, 上式的证明将更容易.

对于正整数 $n \geqslant 1$ ，取 $x = \frac{\pi}{3 \cdot 2^n}$ ，即得

$$
3 \cdot 2 ^ {n} \sin \frac {\pi}{3 \cdot 2 ^ {n}} <   \pi <   3 \cdot 2 ^ {n + 2} \sin \frac {\pi}{3 \cdot 2 ^ {n + 1}} - 3 \cdot 2 ^ {n} \sin \frac {\pi}{3 \cdot 2 ^ {n}}. \tag {5.5.17}
$$

这本质上就是刘徽 $^{①}$ 在其割圆术中所采用的不等式. 由  $\sin\frac{\pi}{6}=\frac{1}{2}$ ，并反复利用

$$
\sin^ {2} \frac {t}{2} = \frac {1 - \sqrt {1 - \sin^ {2} t}}{2}, \quad \forall t \in \left(0, \frac {\pi}{2}\right)
$$

可以计算 $^{②}\sin\frac{\pi}{3\cdot2^{n}}$ 并得到 $\pi$ 的近似值. 取 n=6, 刘徽得到了 $\pi\approx192\sin\frac{\pi}{192}\approx3.14$ , 并指出若取 $n = 10$ 得到① $\pi \approx 3072\sin \frac{\pi}{3072} \approx 3.1416$. 在 (5.5.16) 式中取 $n = 12$, 就得到祖冲之②、祖暅③父子得到的

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">① 刘徽, 三国时期魏国人, 约 225 年—约 295 年, 中国古代数学家.</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">② 正如刘徽在《九章算术注》中所作的那样, 对于 $1 < k < n$, 只需要计算 $\sin^2 \frac{\pi}{3 \cdot 2^k}$ 而不需要计算 $\sin \frac{\pi}{3 \cdot 2^k}$.</span></small>

$$
3. 1 4 1 5 9 2 6 <   \pi <   3. 1 4 1 5 9 2 7.
$$

自然, 在刘徽和祖冲之的时代没有三角函数. 这里只是借用现代数学的语言来解释相关工作.

## 5.5.6 夹角 正弦定理 余弦定理

考虑平面 $\mathbb{R}^2$ 中的单位圆周 $x^{2} + y^{2} = 1$ 上两点 $A(\cos \theta ,\sin \theta)$ 和 $B(\cos \varphi ,\sin \varphi)$ (图5.2).则有整数 $k$ 以及 $\alpha \in (-\pi ,\pi ]$ 使得 $\varphi -\theta = 2k\pi +\alpha$ .我们称 $\beta = |\alpha |$ 为 $\angle AOB$ 的弧度，或称 $\overrightarrow{OA}$ 和 $\overrightarrow{OB}$ 的夹角为 $\beta$ 易见在这一定义下，夹角在旋转变换下不变.进一步，可见 $\beta$ 由 $\cos \beta$ 唯一确定:

$$
\cos \beta = \cos \alpha = \cos (\varphi - \theta) = \cos \varphi \cos \theta + \sin \varphi \sin \theta = \overrightarrow {O A} \cdot \overrightarrow {O B}.
$$

在射线 OA 以及射线 OB 上各任取一点 P, Q (P, Q 不为 O). 则

$$
\cos \beta = \frac {\overrightarrow {O P} \cdot \overrightarrow {O Q}}{| O P | \cdot | O Q |},
$$

这里 $|OP|$, $|OQ|$ 表示线段 $OP, OQ$ 的长度. 由此, 对于 $\mathbb{R}^2$ 中三个不同的点 $P_k(x_k, y_k) (k = 0, 1, 2)$, 可一般地定义 $\overrightarrow{P_0P_1}$ 与 $\overrightarrow{P_0P_2}$ 的夹角为

$$
\arccos \frac {\overrightarrow {P _ {0} P _ {1}} \cdot \overrightarrow {P _ {0} P _ {2}}}{| P _ {0} P _ {1} | \cdot | P _ {0} P _ {2} |} = \frac {(x _ {1} - x _ {0}) (x _ {2} - x _ {0}) + (y _ {1} - y _ {0}) (y _ {2} - y _ {0})}{\sqrt {(x _ {1} - x _ {0}) ^ {2} + (y _ {1} - y _ {0}) ^ {2}} \sqrt {(x _ {2} - x _ {0}) ^ {2} + (y _ {2} - y _ {0}) ^ {2}}}, \tag {5.5.18}
$$

其中 $\arccos$ 是 $\cos$ 在 $[0, \pi]$ 上的反函数. 根据上面的讨论可见, 这里定义的夹角在旋转变换与平移变换下不变.

![](images/page_136_image_13.jpg)

<details>
<summary>text_image</summary>

y
B(cos φ, sin φ)
Q
β
A(cos θ, sin θ)
P
O
x
</details>

图5.2

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">① 刘徽还给出了另一种方法得到 $\pi \approx 3.1416$，该法利用 $n \leqslant 6$ 的数据来估算圆周率。该法究竟是什么样的方法，今人难以确定。</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">② 祖冲之, 字文远, 429 年—500 年, 南北朝时期数学家、天文学家.</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">③ 祖暅，一作祖暅之，字景烁，5—6世纪，南北朝时期数学家、天文学家.</span></small>

更一般地, 在 $\mathbb{R}^n (n\geqslant 2)$ 中, 可以同样地定义两个向量的夹角. 同样可以证明, 该夹角在旋转变换与平移变换下不变.

定义 5.5.5 设  $n \geqslant 2$ ,  $P_{k}(x_{1,k}, x_{2,k}, \cdots, x_{n,k}) (k = 0, 1, 2)$  为  $R^{n}$  中三个不同的点. 则  $P_{0}P_{1}$  与  $P_{0}P_{2}$  的夹角定义为

$$
\mathrm{arccos} \frac {\overrightarrow {P _ {0} P _ {1}} \cdot \overrightarrow {P _ {0} P _ {2}}}{| P _ {0} P _ {1} | \cdot | P _ {0} P _ {2} |} = \mathrm{arccos} \frac {\sum_ {j = 1} ^ {n} (x _ {j , 1} - x _ {j , 0}) (x _ {j , 2} - x _ {j , 0})}{\sqrt {\sum_ {j = 1} ^ {n} (x _ {j , 1} - x _ {j , 0}) ^ {2}} \sqrt {\sum_ {j = 1} ^ {n} (x _ {j , 2} - x _ {j , 0}) ^ {2}}}.\tag {5.5.19}
$$

现在考虑  $R^{n}$  中的  $\triangle ABC$  (图 5.3)，依次用 A, B, C 表示顶点 A, B, C 对应的三个内角，用 a, b, c 依次表示顶点 A, B, C 所对的边的边长。由定义，

$$
2 \cos C = \frac {2 \overrightarrow {C A} \cdot \overrightarrow {C B}}{| C A | \cdot | C B |} = \frac {\overrightarrow {C B} \cdot \overrightarrow {C B} + \overrightarrow {C A} \cdot \overrightarrow {C A} - (\overrightarrow {C A} - \overrightarrow {C B}) \cdot (\overrightarrow {C A} - \overrightarrow {C B})}{| C A | \cdot | C B |} = \frac {a ^ {2} + b ^ {2} - c ^ {2}}{a b}.
$$

![](images/page_137_image_7.jpg)

<details>
<summary>text_image</summary>

B
a
c
C
b
A
</details>

图5.3

这就是余弦定理. 特别地, 当且仅当 $C = \frac{\pi}{2}$ 时有勾股定理

$$
c ^ {2} = a ^ {2} + b ^ {2}.
$$

我们有

$$
\begin{array}{l} \frac {\sin C}{c} = \frac {1}{c} \sqrt {1 - \cos^ {2} C} = \frac {1}{2 a b c} \sqrt {4 a ^ {2} b ^ {2} - (a ^ {2} + b ^ {2} - c ^ {2}) ^ {2}} \\ = \frac {1}{2 a b c} \sqrt {(a + b + c) (a + b - c) (b + c - a) (c + a - b)}. \\ \end{array}
$$

由此可见 $\frac{\sin C}{c} = \frac{\sin B}{b} = \frac{\sin A}{a}$. 这就是正弦定理.

最后, 我们来证明三角形的内角和为  $\pi$ , 即  $A + B + C = \pi$ . 由

$$
\begin{array}{l} \sin (A + B) = \sin A \cos B + \cos A \sin B = (a \cos B + b \cos A) \frac {\sin C}{c} \\ = \left(\frac {a ^ {2} + c ^ {2} - b ^ {2}}{2 c} + \frac {b ^ {2} + c ^ {2} - a ^ {2}}{2 c}\right) \frac {\sin C}{c} = \sin C > 0, \tag {5.5.20} \\ \end{array}
$$

以及 $0 < A + B < 2\pi$ 可见 $0 < A + B < \pi$.

若 $A + B + C \neq \pi$, 则由 (5.5.20)式必有 $A + B = C$. 同理可证 $B = A + C$. 这与 $A > 0$ 矛盾. 因此, 必有 $A + B + C = \pi$.

于是, 当 $C = \frac{\pi}{2}$ 时, $A + B = \frac{\pi}{2}$. 从而

$$
\sin A = \cos B = \frac {a ^ {2} + c ^ {2} - b ^ {2}}{2 a c} = \frac {2 a ^ {2}}{2 a c} = \frac {a}{c}.
$$

## 习题5.5

1. 对于 $x_0 \in \mathbb{R}$, 计算 $\lim_{x \to x_0} \frac{\sin x - \sin x_0}{x - x_0}$.
2. 对于 $x_0 \in \mathbb{R}$, 计算 $\lim_{x \to x_0} \frac{\cos x - \cos x_0}{x - x_0}$.
3. 对于 $x_0 \in \mathbb{R}$, 计算 $\lim_{x \to x_0} \frac{\tan x - \tan x_0}{x - x_0}$.
4. 对于 $x_0 \in \mathbb{R}$, 计算 $\lim_{x \to x_0} \frac{\arctan x - \arctan x_0}{x - x_0}$.
5. 计算  $\lim_{x\to0}\frac{\sin x-x+\frac{x^{3}}{6}}{x^{5}}$ .
6. 计算  $\lim_{x\to0}\frac{\arcsin x-x-\frac{x^{3}}{6}}{x^{5}}$ .
7. 计算 $\lim_{x\to 0}\frac{\tan x - x}{x^3}.$
8. 计算 $\lim_{x\to 0}\frac{\arctan x - x + \frac{x^3}{3}}{x^5}.$

## 第六章

## 导数与微分

数学分析的核心内容主要包括微分和积分两部分, 也就是所谓的微积分. 如果我们把微分和积分分别看成是 “微观” 和 “宏观”, 再把前面引入的 “连续” 当作 “中观” 的话, 那么数学分析可以理解为是一门介绍 “微观” “中观” 和 “宏观” 方法的学科. 或者通俗地说, 数学分析是用此 “三观” 来观察和研究函数的学科.

本章我们将着重从“微观”的角度来研究函数, 即所谓的一元函数微分学的内容.

微分的思想萌芽可以追溯到古希腊时期, 当时是在解决具体问题时, 以朴素的、零散的碎片方式表现出来的. 而更接近现代观点的微分学, 比较认可的说法是在 16 世纪前后逐渐形成和发展的. 代表人物和所讨论的问题有 Kepler $^{①}$ 研究的行星运行、Descartes 讨论的曲线的切线、Fermat $^{②}$ 考虑的函数的极值和曲线的切线、Barrow $^{③}$ 通过微分三角形探讨的切线方程等. 这些前期的酝酿, 为后来的代表人物 Newton 和 Leibniz 系统地创立微积分提供了充足的素材和准备. 我们现在介绍的内容, 是经过了 19 世纪的长足发展, 在理论上给予严谨化和进一步的提升、推广和应用后的体系.

顺便提到一点的是, 积分思想的诞生要早于, 至少不迟于, 微分的诞生. 因此, 从历史发展的顺序来说, 微分与积分观念形成的先后与通常教科书中的陈述顺序刚好相反. 本书也将采取先讨论微分再讲述积分的顺序. 这一点其实也不奇怪, 正如大多数分析教材也都是站在 19 世纪数学严谨化之后的角度来讲授的, 而不是完全按时间顺序介绍前人的思想、方法和结论, 然后再逐一打补丁填补不严谨之处.

## 6.1 导数的引入与定义

引入导数这一微分学的核心概念的方式通常有如下两种, 一种是从曾经产生过重大历史影响的两个经典问题入手, 即当初 Newton 和 Leibniz 分别讨论的质点运动的瞬时速度和曲线的切线问题的模型, 然后进行数学抽象和提升; 另一种是跳过对具体问题的介绍, 直接从逻辑上给出严格的数学定义. 这两种方式各有利弊, 完全视读者的知识背景和储备.

对于初学者来说, 也许第一种引入方式较为自然, 也能产生一定的质感, 学习和关注的重点在于如何从介绍朴素的案例的过程中捕捉到数学的本质, 再对其提炼和提升. 第二种引入方法其优点在于简明精练, 主题鲜明.

我们下面采用第一种模式来引入导数. 我们这样做还有一个原因, 就是这两个经典模型的背后代表着学习这门课时两种不同的角度, 一种是分析味道浓郁, 一种几何直观凸显. 它们均为数学分析中极其重要的理念和方法, 在后面的章节中也能隐约体会到它们在处理问题时带来的不同影响.

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">① Kepler, Johannes, 1571 年 12 月 27 日—1630 年 11 月 15 日, 德国天文学家、物理学家、数学家.</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">② Fermat, Pierre de, 1601 年 8 月 17 日—1665 年 1 月 12 日, 法国数学家.</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">③ Barrow, Isaac, 1630 年 10 月 — 1677 年 5 月 4 日, 英国数学家.</span></small>

我们来讨论下面两个经典模型, 它们正是当年 Newton 和 Leibniz 分别创建微积分时研究的问题. 起源于对质点瞬时速度和曲线切线及其斜率的讨论,

(1) 质点运动学问题: 求质点变速直线运动的瞬时速度.
(2) 几何图形中的切线问题: 求曲线上一点处的切线斜率.

## 1. 质点运动学问题, 非匀速直线运动的瞬时速度

在经典的匀速直线运动框架下，质点的速度定义为质点在单位时间内移动的改变。顾名思义，它应为常值才和匀速直线运动吻合，既不依时间单位长短 $\Delta t$ 的改变而改变，也不依测量时刻 $t$ 的不同而不同。但事实上，严格意义下的匀速直线运动仅仅是一种理想状态。稍微一般的情况应该是非匀速直线运动，以及更一般的曲线变速运动。在此，我们仅重点考虑前者，即质点的非匀速直线运动。

所谓的非匀速直线运动, 是指在给定的时间段 (比如单位时间) 内, 质点运动的位移会有所不同. 这种采用给定时间段去除运动位移改变的计算方法, 是与前面匀速直线运动速度的计算方法兼容的. 这样得到的比值, 称为质点在这段时间的平均速度.

Newton 关于质点运动的瞬时速度, 是在上述平均速度的基础上引入的. 换句话说, 我们将上述时间段的长度取得越来越小, 如果平均速度有极限的话, 就定义为指定质点的瞬时速度. 我们给出如下严格的描述.

设质点在直线 (取为 $x$ 轴) 上运动, 在时刻 $t_0$, 质点的位置为 $x(t_0)$, 那么从时刻 $t_0$ 到时刻 $t_0 + \tau$, 质点的位移变化为

$$
\Delta x = x (t _ {0} + \tau) - x (t _ {0}).
$$

这里我们允许 $\tau < 0$ ，此时可以理解为经过时间段 $-\tau$ 后，质点从位置 $x(t_0 + \tau)$ 到达位置 $x(t_0)$ .质点在 $\tau$ 时间段内的平均速度为

$$
\bar {v} := \frac {\Delta x}{\tau} = \frac {x (t _ {0} + \tau) - x (t _ {0})}{\tau}.
$$

对于固定的非常小的 $\tau$, 可以将它看成是在 $t_0$ 时刻质点速度的一个近似值. 因此, 如果极限

$$
\lim _ {\tau \to 0} \frac {\Delta x}{\tau} = \lim _ {\tau \to 0} \frac {x (t _ {0} + \tau) - x (t _ {0})}{\tau}
$$

存在且有限时, 我们称此极限值为质点在时刻  $t_{0}$  的瞬时速度.

## 2. 曲线切线问题

我们在中学讨论圆的切线时, 曾经把和圆只有一个公共交点的直线称为圆的切线. 对于圆来说, 这种定义切线的方式倒也无妨, 因为这的确是圆的切线所具有的特征, 但这一特征显然不宜当作一般曲线切线的定义. 比如对于抛物线而言, 任何一条平行于抛物线对称轴的直线与抛物线都只有一个交点, 而这些直线显然不能称为抛物线的切线. 由此看出, 对于一般曲线, 我们尚未严谨引入过 “切线” 的概念. 下面我们简要介绍一下 Leibniz 研究曲线切线时所采用的基本思想和方法. 为简单计, 我们假设所讨论的曲线是由显式函数给出的, 即曲线是由形如 $y = f(x)$ 的函数给出的图像.

在曲线 $y = f(x)$ 上，任取一点 $P_0(x_0, y_0), y_0 = f(x_0)$，在点 $P_0$ 附近再在曲线上取一点 $P = (x, y)$. 连接两点 $P$ 与 $P_0$ 作曲线的一条“割线”，则此割线的斜率为

$$
\tan \alpha = \frac {Q P}{P _ {0} Q},
$$

其中 Q 为坐标是  $(x, y_{0})$  的点 (见图 6.1).

![](images/page_142_chart_6.jpg)

<details>
<summary>line</summary>

| Point | x | y |
| --- | --- | --- |
| Intersection (P0) | x0 | y0 |
</details>

图6.1

容易看出, 当点 P 沿着曲线向点  $P_{0}$  移动时,

$$
\tan \alpha = \frac {f (x) - f (x _ {0})}{x - x _ {0}}.
$$

割线 $P_0P$ 以及夹角 $\alpha$ 都随着 $P$ 变化而变化. 如果当 $x \to x_0$ 时, $\tan \alpha$ 存在有限的极限 $k$, 即

$$
\lim _ {x \to x _ {0}} \frac {f (x) - f (x _ {0})}{x - x _ {0}} = k,
$$

那么我们很自然地可以把经过点 $P_{0}$ 斜率为 $k$ 的直线定义为曲线 $y = f(x)$ 在点 $P_{0}$ 处的切线 $\ell$. 显然, 如此定义的切线 $\ell$ 有解析表达式

$$
y = y _ {0} + k (x - x _ {0}).
$$

上述两个经典数学模型, 表现形式相去甚远, 但其背后的共同点都是讨论函数的改变量与自变量改变量的比率, 我们将其进行数学上的提炼、抽象和统一处理, 即可引入导数的定义.

定义 6.1.1 (导数) 设函数 $y = f\left( x\right)$ 在点 ${x}_{0}$ 附近有定义,如果极限

$$
\lim _ {x \to x _ {0}} \frac {f (x) - f (x _ {0})}{x - x _ {0}} \tag {6.1.1}
$$

存在且有限, 则称 $f(x)$ 在点 $x_0$ 处可导, 并称其极限值为 $f(x)$ 在点 $x_0$ 处的导数, 记为 $f'(x_0)$ 或 $y'(x_0)$.

关于导数符号的几句话: 数学符号的引入通常有其历史背景或文化背景, 或有其内含抑或个人偏好. 导数的记号也不例外. 比如, 上面表示导数的符号' 是 Lagrange $^{①}$  创建的, 最显著的特点是简捷明了,  $f'(x_{0})$  蕴涵着是由函数  $f(x)$  而非另外的函数  $g(x)$  诱导出来的数. 除了 Lagrange 的符号外, 常见的表示导数的符号还有下面 Leibniz 给出的形式:

$$
\left. \frac {\mathrm{d} y}{\mathrm{d} x} \right| _ {x = x _ {0}}, \quad \frac {\mathrm{d} f}{\mathrm{d} x} (x _ {0}), \quad \left. \frac {\mathrm{d} f}{\mathrm{d} x} \right| _ {x = x _ {0}}.
$$

Leibniz 引入的符号初看起来略显啰唆, 当然它传递的信息更多. 当我们讨论的场景稍微复杂时, 比如有多个函数代数运算时, Leibniz 的符号能更清晰地反映出变量间的依赖关系. 不仅如此, 我们还看到这些符号特有的 “分数” 形式, 它更像是两个量的比值. 事实上, 的确如此, 我们对导数的定义稍作形式上的处理, 很快将会看到为什么导数又叫差商的极限了. 在引入微分的概念之后, 这些形式符号被赋予了更深刻的内涵: 导数 $\frac{\mathrm{dy}}{\mathrm{dx}}$ 中的分子和分母可以被看成独立的运算符号, 即微分 $\mathrm{dy}$ 和 $\mathrm{dx}$ 之商了.

除了讨论函数 $f(x)$ 某点 $x_0$ 的可导性外, 我们还经常讨论它在一个集合上的可导性. 对于一个给定的点集 $E \subseteq \mathbb{R}$, 如果 $f(x)$ 在 $E$ 中的每个点都可导, 则称 $f(x)$ 在集合 $E$ 上可导. 当我们的关注点落在函数在集合 $E$ 上的可导性而不是指定点 $x_0$ 的可导性时, 我们常常把 $x_0$ 中的下标去掉, 代之以更灵活和方便的符号 $f'(x)$, 并称之为函数 $f(x)$ 的导函数.

点集 $E \subseteq \mathbb{R}$ 最常见的形式为区间, 包括开区间 $(a, b)$ 和闭区间 $E = [a, b]$ 以及各种组合, 此时我们也说 $f(x)$ 在区间上可导.

我们对定义6.1.1中的导数作一些形式上的处理: 对于固定点 $x_0$ 以及附近的点 $x$, 我们更习惯于将 $x$ 与 $x_0$ 的差用 $\Delta x$ 表示, 类似地, 用 $\Delta f(x)$ 或者 $\Delta y$ 表示相应的函数值的差 $f(x) - f(x_0)$, 即

$$
\Delta x = x - x _ {0}, \qquad \Delta y = f (x) - f (x _ {0}).
$$

于是 $x = x_0 + \Delta x, f(x) = f(x_0) + \Delta y,$ 而 $x\to x_0$ 则等价于 $\Delta x\to 0.$ 表达式（6.1.1）就变成了

$$
f ^ {\prime} (x _ {0}) = \lim _ {\Delta x \to 0} \frac {\Delta y}{\Delta x}. \tag {6.1.2}
$$

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">① Lagrange, Joseph-Louis, 1736 年 1 月 25 日 — 1813 年 4 月 10 日, 意大利裔法国数学家.</span></small>