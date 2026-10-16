# 上册 / 第三章 序列极限

原始 PDF 第 57–99 页。

## 第三章

## 序列极限

---

44

第三章 序列极限

极限贯穿整个数学分析课程, 学习数学分析是一个从理解简单的极限到理解复杂的极限的不断深入的过程.

## 3.1 数列极限

所谓实数列, 是指一个从正整数集映到实数集的函数 $a: \mathbb{N}_+ \to \mathbb{R}$. 若记 $a(n)$ 为 $a_n$, 则我们用 $\{a_n\}$ 表示该数列, $a_n$ 称为数列的一般项或通项. 通常, 我们也把数列 $\{a_n\}$ 写成

$$
a _ {1}, a _ {2}, \dots , a _ {n}, a _ {n + 1}, \dots . \tag {3.1.1}
$$

必要时, 对于整数 $m$, 我们用 $\{a_{n}\}_{m}^{\infty}$ 表示数列

$$
a _ {m}, a _ {m + 1}, a _ {m + 2}, \dots , a _ {n}, a _ {n + 1}, \dots . \tag {3.1.2}
$$

我们定义数列极限如下:

定义 3.1.1 设有数列  $\{a_{n}\}$  与给定常数 A, 如果对任意  $\varepsilon > 0$ , 都存在  $N \geqslant 1$ , 使得当  $n \geqslant N$  时, 有

$$
\left| a _ {n} - A \right| <   \varepsilon , \tag {3.1.3}
$$

则称数列 $\{a_{n}\}$ 收敛于① $A$ 或极限存在, $A$ 称为 $\{a_{n}\}$ 的极限, 记作②

$$
\lim _ {n \rightarrow + \infty} a _ {n} = A \tag {3.1.4}
$$

或

$$
a _ {n} \rightarrow A, \quad \text {当} n \rightarrow + \infty \text {时}. \tag {3.1.5}
$$

当  $\{a_{n}\}$  不收敛时, 我们就称它是发散的.

通俗地讲, $\{a_{n}\}$ 的极限为 $A$, 就是只要 $n$ 足够大, $a_{n}$ 与 $A$ 要多接近就有多接近. 体现在直角坐标系中, 就是当 $n$ 足够大时, $(n, a_{n})$ 都落在带形 $(- \infty, +\infty) \times (A - \varepsilon, A + \varepsilon)$ 上, 如图3.1所示. 也可以这样理解 $\{a_{n}\}$ 的极限为 $A$: 无论 $\varepsilon > 0$ 有多小, 数列 $\{a_{n}\}$ 中都只有有限项落在区间 $(A - \varepsilon, A + \varepsilon)$ 之外, 如图3.2所示.

对于数列 $\{a_{n}\}$, 可形成一个新的数列 $\left\{\sum_{k=1}^{n} a_{k}\right\}$, 我们用 $\sum_{n=1}^{\infty} a_{n}$ 表示, 称为无穷级数或级数. 若 $\left\{\sum_{k=1}^{n} a_{k}\right\}$ 收敛到 $A$, 则称级数 $\sum_{n=1}^{\infty} a_{n}$ 收敛到 $A$, 又称级数的和为 $A$. $\sum_{k=1}^{n} a_{k}$ 称为级数的部分和. 易见, $\lim_{n \to +\infty} a_{n} = 0$ 是级数 $\sum_{n=1}^{\infty} a_{n}$ 收敛的必要条件.

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">① “收敛于 A” 也时常说成 “趋于 A”.</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">② 鉴于数列极限中的 n 通常为自然数或正整数,  $n \rightarrow +\infty$  时常写为  $n \rightarrow \infty$ .</span></small>

---

3.1 数列极限

45

![](../../raw/pages_0049-0064/images/page_58_chart_2.jpg)

<details>
<summary>scatter</summary>

| Point | x (approx) | y (approx) |
| --- | --- | --- |
| a1 | ~0.5 | ~-2.5 |
| a2 | ~1.5 | ~7.5 |
| a3 | ~2.5 | ~4.5 |
| a4 | ~3.5 | ~-1.5 |
| a5 | ~4.5 | ~6.0 |
| a6 | ~5.5 | ~-0.5 |
| an | ~6.5 | ~-0.5 |
| an+1 | ~7.5 | ~-1.0 |
| Unlabeled 1 | ~8.5 | ~-0.5 |
| Unlabeled 2 | ~9.5 | ~-0.5 |
| Unlabeled 3 | ~10.5 | ~-0.5 |
| Unlabeled 4 | ~11.5 | ~-0.5 |
| Unlabeled 5 | ~12.5 | ~-0.5 |
| Unlabeled 6 | ~13.5 | ~-0.5 |
| Unlabeled 7 | ~14.5 | ~-0.5 |
| Unlabeled 8 | ~15.5 | ~-0.5 |
| Unlabeled 9 | ~16.5 | ~-0.5 |
| Unlabeled 10 | ~17.5 | ~-0.5 |
| Unlabeled 11 | ~18.5 | ~-0.5 |
| Unlabeled 12 | ~19.5 | ~-0.5 |
| Unlabeled 13 | ~20.5 | ~-0.5 |
| Unlabeled 14 | ~21.5 | ~-0.5 |
| Unlabeled 15 | ~22.5 | ~-0.5 |
| Unlabeled 16 | ~23.5 | ~-0.5 |
| Unlabeled 17 | ~24.5 | ~-0.5 |
| Unlabeled 18 | ~25.5 | ~-0.5 |
| Unlabeled 19 | ~26.5 | ~-0.5 |
| Unlabeled 20 | ~27.5 | ~-0.5 |
| Unlabeled 21 | ~28.5 | ~-0.5 |
| Unlabeled 22 | ~29.5 | ~-0.5 |
| Unlabeled 23 | ~30.5 | ~-0.5 |
| Unlabeled 24 | ~31.5 | ~-0.5 |
| Unlabeled 25 | ~32.5 | ~-0.5 |
| Unlabeled 26 | ~33.5 | ~-0.5 |
| Unlabeled 27 | ~34.5 | ~-0.5 |
| Unlabeled 28 | ~35.5 | ~-0.5 |
| Unlabeled 29 | ~36.5 | ~-0.5 |
| Unlabeled 30 | ~37.5 | ~-0.5 |
| Unlabeled 31 | ~38.5 | ~-0.5 |
| Unlabeled 32 | ~39.5 | ~-0.5 |
| Unlabeled 33 | ~40.5 | ~-0.5 |
| Unlabeled 34 | ~41.5 | ~-0.5 |
| Unlabeled 35 | ~42.5 | ~-0.5 |
| Unlabeled 36 | ~43.5 | ~-0.5 |
| Unlabeled 37 | ~44.5 | ~-0.5 |
| Unlabeled 38 | ~45.5 | ~-0.5 |
| Unlabeled 39 | ~46.5 | ~-0.5 |
| Unlabeled 40 | ~47.5 | ~-0.5 |
| Unlabeled 41 | ~48.5 | ~-0.5 |
| Unlabeled 42 | ~49.5 | ~-0.5 |
| Unlabeled 43 | ~50.5 | ~-0.5 |
| Unlabeled 44 | ~51.5 | ~-0.5 |
| Unlabeled 45 | ~52.5 | ~-0.5 |
| Unlabeled 46 | ~53.5 | ~-0.5 |
| Unlabeled 47 | ~54.5 | ~-0.5 |
| Unlabeled 48 | ~55.5 | ~-0.5 |
| Unlabeled 49 | ~56.5 | ~-0.5 |
| Unlabeled 50 | ~57.5 | ~-0.5 |
| Unlabeled 51 | ~58.5 | ~-0.5 |
| Unlabeled 52 | ~59.5 | ~-0.5 |
| Unlabeled 53 | ~60.5 | ~-0.5 |
| Unlabeled 54 | ~61.5 | ~-0.5 |
| Unlabeled 55 | ~62.5 | ~-0.5 |
| Unlabeled 56 | ~63.5 | ~-0.5 |
| Unlabeled 57 | ~64.5 | ~-0.5 |
| Unlabeled 58 | ~65.5 | ~-0.5 |
| Unlabeled 59 | ~66.5 | ~-0.5 |
| Unlabeled 60 | ~67.5 | ~-0.5 |
| Unlabeled 61 | ~68.5 | ~-0.5 |
| Unlabeled 62 | ~69.5 | ~-0.5 |
| Unlabeled 63 | ~70.5 | ~-0.5 |
| Unlabeled 64 | ~71.5 | ~-0.5 |
| Unlabeled 65 | ~72.5 | ~-0.5 |
| Unlabeled 66 | ~73.5 | ~-0.5 |
| Unlabeled 67 | ~74.5 | ~-0.5 |
| Unlabeled 68 | ~75.5 | ~-0.5 |
| Unlabeled 69 | ~76.5 | ~-0.5 |
| Unlabeled 70 | ~77.5 | ~-0.5 |
| Unlabeled 71 | ~78.5 | ~-0.5 |
| Unlabeled 72 | ~79.5 | ~-0.5 |
| Unlabeled 73 | ~80.5 | ~-0.5 |
| Unlabeled 74 | ~81.5 | ~-0.5 |
| Unlabeled 75 | ~82.5 | ~-0.5 |
| Unlabeled 76 | ~83.5 | ~-0.5 |
| Unlabeled 77 | ~84.5 | ~-0.5 |
| Unlabeled 78 | ~85.5 | ~-0.5 |
| Unlabeled 79 | ~86.5 | ~-0.5 |
| Unlabeled 80 | ~87.5 | ~-0.5 |
| Unlabeled 81 | ~88.5 | ~-0.5 |
| Unlabeled 82 | ~89.5 | ~-0.5 |
| Unlabeled 83 | ~90.5 | ~-0.5 |
| Unlabeled 84 | ~91.5 | ~-0.5 |
| Unlabeled 85 | ~92.5 | ~-0.5 |
| Unlabeled 86 | ~93.5 | ~-0.5 |
| Unlabeled 87 | ~94.5 | ~-0.5 |
| Unlabeled 88 | ~95.5 | ~-0.5 |
| Unlabeled 89 | ~96.5 | ~-0.5 |
| Unlabeled 90 | ~97.5 | ~-0.5 |
| Unlabeled 91 | ~98.5 | ~-0.5 |
| Unlabeled 92 | ~99.5 | ~-0.5 |
</details>

图3.1

![](../../raw/pages_0049-0064/images/page_58_image_4.jpg)

<details>
<summary>text_image</summary>

a₄ a₁
A−ε aₙ A Aₙ₊₁ A+ε a₃ a₂
</details>

图3.2

类似地, 由数列 $\{a_{n}\}$ 形成的另一个数列 $\left\{\prod_{k=1}^{n} a_{k}\right\}$ 称为无穷乘积, 用 $\prod_{n=1}^{\infty} a_{n}$ 表示. 若 $\left\{\prod_{k=1}^{n} a_{k}\right\}$ 收敛到实数 $A \neq 0$, 则称无穷乘积 $\prod_{n=1}^{\infty} a_{n}$ 收敛到 $A$, 又称作乘积为 $A$. $\prod_{k=1}^{n} a_{k}$ 称为无穷乘积的部分积. 易见, $\lim_{n \to +\infty} a_{n} = 1$ 是无穷乘积 $\prod_{n=1}^{\infty} a_{n}$ 收敛的必要条件.

用定义说明极限存在关键是找到合适的 N. 满足要求的 N 并不唯一. 许多初学者习惯于寻找使不等式 (3.1.3) 成立的那个最小的 N. 但这是没有必要的. 正确的思路是用尽量简单的方法找一个正确的简单的 N.

例3.1.1 证明 $\lim_{n\to +\infty}\frac{n}{2n + 1} = \frac{1}{2}$

证明 $\forall \varepsilon > 0$, 要使得

$$
\left| \frac {n}{2 n + 1} - \frac {1}{2} \right| <   \varepsilon ,
$$

即

$$
2 (2 n + 1) > \frac {1}{\varepsilon},
$$

只要

$$
n \geqslant \left[ \frac {1}{\varepsilon} \right].
$$

取 $N = \left[\frac{1}{\varepsilon}\right]$, 则当 $n \geqslant N$ 时, 有

$$
\left| \frac {n}{2 n + 1} - \frac {1}{2} \right| <   \varepsilon .
$$

于是, 根据极限的定义, 得到  $\lim_{n\to+\infty}\frac{n}{2n+1}=\frac{1}{2}$ .

---

46

第三章 序列极限

当 $\varepsilon > 1$ 时, 上面所取的 $N = 0$, 不符合极限定义中 $N \geqslant 1$ 的条件. 为此, 我们可以用取 $N = \left[\frac{1}{\varepsilon}\right] + 1$ 来代替原先的取法.

另一方面, 极限定义中之所以要求 $N \geqslant 1$, 是因为数列定义中的起始项对应于 $n = 1$. 但这不是本质的. 在 (3.1.2) 式中, 数列的起始项对应于整数 $n = m$, 此时极限定义中的 “$N \geqslant 1$” 自然应修改为 “$N \geqslant m$”.

在例 3.1.1 中, 我们不妨认为数列的起始项对应于 n = 0 的项  $\frac{0}{0 + 1} = 0$ . 这样, 就不必刻意去要求  $N \geqslant 1$ .

当情况更为复杂时, 较大的 $\varepsilon$ 反而造成一些麻烦. 为此, 可限制 $\varepsilon$ 取值于 $(0, \delta_0)$, 其中 $\delta_0$ 是一个预先给定的正数. 换言之, 极限定义中的 “$\forall \varepsilon > 0$”, 可以替换为 “$\forall \varepsilon \in (0,1)$” 或 “$\forall \varepsilon \in \left(0, \frac{1}{2}\right)$” 等.

例 3.1.2 设 a > 1, 证明  $\lim_{n \to +\infty} \sqrt[n]{a} = 1$ .

证明 $\forall \varepsilon > 0,$ 要使得

$$
\left| \sqrt [ n ]{a} - 1 \right| <   \varepsilon ,
$$

即

$$
a <   (1 + \varepsilon) ^ {n} = 1 + n \varepsilon + \mathrm{C} _ {n} ^ {2} \varepsilon^ {2} + \dots + \mathrm{C} _ {n} ^ {n} \varepsilon^ {n},
$$

只要

$$
a <   n \varepsilon .
$$

取 $N = \left[\frac{a}{\varepsilon}\right] + 1$ ，则当 $n \geqslant N$ 时，有

$$
\left| \sqrt [ n ]{a} - 1 \right| <   \varepsilon .
$$

于是, 根据极限的定义, 得到  $\lim_{n\to+\infty}\sqrt[n]{a}=1$ .

例 3.1.3 证明  $\lim_{n\to+\infty}\sqrt[n]{n}=1$ .

证明 $\forall \varepsilon > 0,$ 要使得

$$
\left| \sqrt [ n ]{n} - 1 \right| <   \varepsilon ,
$$

即

$$
n <   (1 + \varepsilon) ^ {n} = 1 + n \varepsilon + \mathrm{C} _ {n} ^ {2} \varepsilon^ {2} + \dots + \mathrm{C} _ {n} ^ {n} \varepsilon^ {n},
$$

只要 $n \geqslant 2$ ，且

$$
n <   \frac {n (n - 1)}{2} \varepsilon^ {2}. \tag {3.1.6}
$$

这只要 $n \geqslant 2$ ，且

$$
n > \frac {2}{\varepsilon^ {2}} + 1.
$$

取 $N = \left[\frac{2}{\varepsilon^2}\right] + 2,$ 则当 $n\geqslant N$ 时，有

$$
\left| \sqrt [ n ]{n} - 1 \right| <   \varepsilon .
$$

---

3.1 数列极限

47

于是, 根据极限的定义, 得到 $\lim_{n\to +\infty}\sqrt[n]{n} = 1$.

在上面的讨论中, 为了 $(1 + \varepsilon)^n$ 的展开式出现 (3.1.6) 式中的 $\frac{n(n - 1)}{2}\varepsilon^2$, 我们附加了 $n \geqslant 2$ 的要求. 事实上, 即使 $n < 2$, 认为 $(1 + \varepsilon)^n$ 的展开式中含有 $\frac{n(n - 1)}{2}\varepsilon^2$ 也并无不妥. 而在默认 $n \geqslant 0$ 时, $(1 + \varepsilon)^n \geqslant \frac{n(n - 1)}{2}\varepsilon^2$ 也总是成立. 因此, $n \geqslant 2$ 这个要求可以不用专门提.

例3.1.4 设 $q \in (-1, 1)$. 证明 $\lim_{n \to +\infty} q^n = 0$.

证明 $\forall \varepsilon > 0,$ 要使得

$$
\left| q ^ {n} \right| <   \varepsilon ,
$$

即

$$
n \lg | q | <   \lg \varepsilon ,
$$

亦即

$$
n > \frac {\lg \varepsilon}{\lg | q |},
$$

可取 $N = \left[\frac{\lg\varepsilon}{\lg|q|}\right] + 1,$ 则当 $n\geqslant N$ 时，有

$$
\left| q ^ {n} \right| <   \varepsilon .
$$

于是, 根据极限的定义, 得到  $\lim_{n\to+\infty}q^{n}=0$ .

例 3.1.5 证明  $\lim_{n\to+\infty}\frac{10n^{3}-456n^{2}+123n-89}{2n^{3}-99n^{2}+7n-8}=5.$

证明 任取 $\varepsilon \in (0,1)$, 要使得

$$
\left| \frac {1 0 n ^ {3} - 4 5 6 n ^ {2} + 1 2 3 n - 8 9}{2 n ^ {3} - 9 9 n ^ {2} + 7 n - 8} - 5 \right| <   \varepsilon ,
$$

即

$$
\left| \frac {3 9 n ^ {2} + 8 8 n - 4 9}{2 n ^ {3} - 9 9 n ^ {2} + 7 n - 8} \right| <   \varepsilon ,
$$

只要 $n \geqslant 100$ ，且

$$
\frac {4 0 n ^ {2}}{n ^ {3}} <   \varepsilon .
$$

取 $N = \left[\frac{100}{\varepsilon}\right]$, 则当 $n \geqslant N$ 时, 有

$$
\left| \frac {1 0 n ^ {3} - 4 5 6 n ^ {2} + 1 2 3 n - 8 9}{2 n ^ {3} - 9 9 n ^ {2} + 7 n - 8} - 5 \right| <   \varepsilon .
$$

于是, 根据极限的定义, 得到  $\lim_{n\to+\infty}\frac{10n^{3}-456n^{2}+123n-89}{2n^{3}-99n^{2}+7n-8}=5.$

---

48

第三章 序列极限

注3.1.1 在很多场合, 严格地按照极限定义的形式进行讨论会显得很不方便. 因此, 我们需要熟悉与定义3.1.1等价的陈述. 例如, $\lim_{n\to +\infty}a_n = A$ 等价于:

$\forall \varepsilon \in (0,1),\exists N\geqslant 10,$ 使得当 $n\geqslant 100N$ 时，有

$$
| a _ {n} - A | \leqslant 1 0 0 0 \varepsilon . \tag {3.1.7}
$$

一般地, 对于固定的  $\varepsilon_{0}>0, N_{0}\geqslant1$ , 以及 M>0,  $\lim_{n\to+\infty}a_{n}=A$  等价于:
 $\forall\varepsilon\in(0,\varepsilon_{0})$  (亦可改为  $(0,\varepsilon_{0}]$ ),  $\exists N\geqslant N_{0}$  (亦可改为  $N>N_{0}$ ), 使得当  $n\geqslant N$  (亦可改为 n>N) 时, 有

$$
| a _ {n} - A | <   M \varepsilon \qquad (\text {亦可改为} \quad | a _ {n} - A | \leqslant M \varepsilon). \tag {3.1.8}
$$

现在我们来考察收敛数列的基本性质. 首先, 我们来给出唯一性、有界性、保序性和保号性.

定理 3.1.1 设数列  $\{a_{n}\}$  收敛到 A.

(1) (保号性) 若 A > 0, 则存在  $N \geqslant 1$ , 使得当  $n \geqslant N$  时, 有  $a_{n} > 0$ .

一般地, 若 A > B, 则存在  $N \geqslant 1$ , 使得当  $n \geqslant N$  时, 有  $a_{n} > B$ .

特别地, 若 A > 0, 则存在  $N \geqslant 1$ , 使得当  $n \geqslant N$  时, 有  $a_{n} > \frac{A}{2}$ .

(2) (保序性) 若数列 $\{b_n\}$ 收敛到 $B$, 而从某一项开始, 有 $a_n \geqslant b_n$, 则 $A \geqslant B$.
(3) (唯一性) 若  $\{a_{n}\}$  同时收敛到 B, 则 A = B.
(4) (有界性)  $\{a_{n}\}$  有界.

证明 (1) 只要证明 A > B 时的一般结论.

取 $\varepsilon_0 = A - B$ ，则 $\varepsilon_0 > 0$ 根据极限定义，存在 $N\geqslant 1$ ，使得当 $n\geqslant N$ 时，有$|a_n - A| <   \varepsilon_0.$ 此时， $a_{n} > A - \varepsilon_{0} = B.$

(2) 若结论不真, 则 $A < B$. 易见 $\lim_{n \to +\infty} (-a_n) = -A$. 由 (1) 以及

$$
\lim _ {n \to + \infty} b _ {n} = B > \frac {A + B}{2}
$$

可得, 存在  $N_{1} \geqslant 1$  使得当  $n \geqslant N_{1}$  时, 有  $b_{n} > \frac{A + B}{2}$ .

同样地, 由 (1) 以及

$$
\lim _ {n \to + \infty} \left(- a _ {n}\right) = - A > - \frac {A + B}{2}
$$

可得, 存在  $N_{2} \geqslant 1$ , 使得当  $n \geqslant N_{2}$  时, 有  $-a_{n} > -\frac{A + B}{2}$ .

取  $N = N_{1} + N_{2}$ ，则当  $n \geqslant N$  时，有

$$
b _ {n} - a _ {n} > \frac {A + B}{2} - \frac {A + B}{2} = 0.
$$

---

3.1 数列极限

49

与假设矛盾. 因此  $A \geqslant B$ .

(3) 取 $\{b_n\}$ 为 $\{a_n\}$, 由 (2), 立即得到 $A \geqslant B$ 与 $B \geqslant A$ 同时成立. 因此, $A = B$.

(4) 由极限定义, 存在 $N \geqslant 1$, 使得当 $n \geqslant N$ 时, 有 $|a_n - A| < \varepsilon_0 = 1$. 此时 $|a_n| < |A| + 1$. 取 $M = \sum_{k=1}^{n} |a_k| + |A| + 1$, 则对于任何 $n \geqslant 1$, 有 $|a_n| \leqslant M$. 即证 $\{a_n\}$ 有界.

这里需要注意 (4) 的结果还基于数列的每一项都是实数. 例如, 不能由 $\lim_{n\to +\infty}\frac{n + 1}{n - 100} = 1$ 得出存在 $M > 0$ 使得对任何 $n \geqslant 1$ 有 $\left|\frac{n + 1}{n - 100}\right| \leqslant M$, 进而 $|n - 100| \geqslant \frac{n + 1}{M}$.

在今后的讨论中, 夹逼准则是一个简单而非常有用的定理.

定理 3.1.2 设数列  $\{x_{n}\},\{y_{n}\}$  和  $\{z_{n}\}$  满足如下条件:

$$
y _ {n} \leqslant x _ {n} \leqslant z _ {n}, \quad \forall n \geqslant 1.
$$

若

$$
\lim _ {n \to + \infty} y _ {n} = \lim _ {n \to + \infty} z _ {n} = A.
$$

则

$$
\lim _ {n \to + \infty} x _ {n} = A. \tag {3.1.9}
$$

证明 $\forall \varepsilon > 0,$ 由 $\lim_{n\to +\infty}y_n = A$ 可得, 存在 $N \geqslant 1$, 使得当 $n \geqslant N$ 时, 有

$$
A - \varepsilon <   y _ {n} <   A + \varepsilon .
$$

对于上述 $^{①}$   $\varepsilon$ , 由  $\lim_{n\to+\infty}z_n=A$  可得, 存在 $^{②}\widetilde{N}\geqslant1$ , 使得当  $n\geqslant\widetilde{N}$  时, 有

$$
A - \varepsilon <   z _ {n} <   A + \varepsilon .
$$

取 $M = \max \left\{N, \widetilde{N}\right\}$, 则当 $n \geqslant M$ 时, 有

$$
A - \varepsilon <   y _ {n} \leqslant x _ {n} \leqslant z _ {n} <   A + \varepsilon .
$$

因此, 由极限定义可见  $\lim_{n\to+\infty}x_{n}=A.$

注3.1.2 如果像定理3.1.1(2)的证明中那样, 把在上面证明中的 $N, \widetilde{N}, M$ 依次用 $N_{1}, N_{2}, N$ 代替, 则证明的可读性会更好. 如何选择符号, 是我们在叙述中需要留意的. 尤其遵循符号使用上一些通行的习惯是值得鼓励的.

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">① “ $\forall\varepsilon>0$ ” 在前面已经出现过，意味着此时  $\varepsilon$  已经确定，因此，不能再使用 “ $\forall\varepsilon>0$ ”.</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">② 同样地，“存在 $N \geqslant 1$”在前面已经出现过，意味着此时 $N$ 也已经确定，因此，不能再使用“存在 $N \geqslant 1$”，而应该另换一个字符表示另一个可能不同的值.</span></small>

---

50

第三章 序列极限

另一方面，在有一定的熟练度以后，可以跳过 $N_{1}, N_{2}$ 而直接给出 $N$。例如，在定理3.1.2的证明中，可以这样写:$\forall \varepsilon > 0$，由 $\lim_{n \to +\infty} y_n = \lim_{n \to +\infty} z_n = A$，可得存在 $N \geqslant 1$，使得当 $n \geqslant N$ 时，有

$$
\left| y _ {n} - A \right| <   \varepsilon , \quad \left| z _ {n} - A \right| <   \varepsilon .
$$

在今后的证明中, 我们将逐步略过一些证明细节.

注 3.1.3 根据数列极限的定义, 数列极限是否存在以及值为多少, 与数列的前有限项无关. 因此, 我们在考虑数列极限的时候, 只需要关心 n 充分大时的项. 我们用记号 “≫”, 表示 “大大大于”. 通常使用的是 “n ≫ 1”, 其含义是 n 充分大, 即对于某个给定的 (通常是在证明之初待定的) N ≥ 1, 有 n ≥ N.

类似地, 对于 “大大小于” 符号, “ $0 < \varepsilon \ll 1$ ” 表示正数  $\varepsilon$  足够小, 即 “对于某个给定的 (通常是在证明之初待定的)  $\delta > 0$ , 有  $0 < \varepsilon < \delta$ ”.

最后, 我们给出关于极限四则运算的性质.

定理3.1.3 设 $\lim_{n\to +\infty}a_n = A,\lim_{n\to +\infty}b_n = B.$

(1) 设 $\alpha, \beta \in \mathbb{R}$ 为常数, 则

$$
\lim _ {n \to + \infty} (\alpha a _ {n} + \beta b _ {n}) = \alpha A + \beta B;
$$

(2) $\lim_{n\to +\infty}(a_nb_n) = AB;$
(3) 若 $B \neq 0$, 则 $\lim_{n \to +\infty} \frac{a_n}{b_n} = \frac{A}{B}$.

证明 (1) 对于任何 $\varepsilon > 0$, 由 $\lim_{n \to +\infty} a_n = A$ 可得, 存在 $N_1 \geqslant 1$, 使得当 $n \geqslant N_1$ 时, 有①

$$
| a _ {n} - A | <   \frac {\varepsilon}{1 + | \alpha | + | \beta |}. \tag {3.1.10}
$$

另一方面, 由 $\lim_{n\to +\infty}b_n = B$ 可得, 对上述 $\varepsilon$, 存在 $N_2 \geqslant 1$, 使得当 $n \geqslant N_2$ 时, 有

$$
| b _ {n} - B | <   \frac {\varepsilon}{1 + | \alpha | + | \beta |}. \tag {3.1.11}
$$

取 $N = N_{1} + N_{2}$, 则当 $n \geqslant N$ 时, (3.1.10) 式与 (3.1.11) 式同时成立. 此时,

$$
\left| \alpha a _ {n} + \beta b _ {n} - (\alpha A + \beta B) \right| \leqslant | \alpha | \left| a _ {n} - A \right| + | \beta | \left| b _ {n} - B \right| <   \varepsilon . \tag {3.1.12}
$$

因此, 由极限定义得到 $\lim_{n\to +\infty}(\alpha a_n + \beta b_n) = \alpha A + \beta B.$

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">① 采用含有1的 $1 + |\alpha| + |\beta|$ 是考虑到 $\alpha = \beta = 0$ 这种特殊情形.</span></small>

---

3.1 数列极限

51

(2) 由收敛数列的有界性, 存在常数 $M > 0$ 使得对任何 $n \geqslant 1$, 都有 $|a_{n}| \leqslant M$. 于是, $\forall \varepsilon > 0$, 存在 $N \geqslant 1$, 使得当 $n \geqslant N$ 时, 有

$$
\(| a _ {n} - A | <   \varepsilon , \quad | b _ {n} - B | <   \varepsilon . \tag {3.1.13}
$$

从而

$$
\begin{array}{l} \left| a _ {n} b _ {n} - A B \right| = \left| a _ {n} \left(b _ {n} - B\right) + B \left(a _ {n} - A\right) \right| \\ \leqslant \left| a _ {n} \right| \left| b _ {n} - B \right| + | B | \left| a _ {n} - A \right| \\ \leqslant M \varepsilon + | B | \varepsilon = (M + | B |) \varepsilon . \tag {3.1.14} \\ \end{array}
$$

因此， $\lim_{n\to +\infty}(a_nb_n) = AB.$

(3) 由 (2), 只需对 $a_{n} \equiv 1$ 的情形加以证明. 由 (1), 不妨设 $B > 0$. 由定理 3.1.1, 有 $N \geqslant 1$ 使得当 $n \geqslant N$ 时, 有 $b_{n} \geqslant \frac{B}{2}$. 此时,

$$
\left| \frac {1}{b _ {n}} - \frac {1}{B} \right| = \frac {| b _ {n} - B |}{b _ {n} B} \leqslant \frac {2}{B ^ {2}} | b _ {n} - B |. \tag {3.1.15}
$$

因此, 由 (1) 和夹逼准则即得 $\lim_{n\to +\infty}\frac{1}{b_n} = \frac{1}{B}$.

在定理3.1.3(3)中， $\{b_n\}$ 不一定恒不为零.但由保号性，存在 $n\geqslant m$ 时，$|b_n| > 0.$ 因此，定理中考虑的数列本质上是数列 $\left\{\frac{a_n}{b_n}\right\}_{m}^{\infty}$

而在 (3.1.14) 式中, 不等式的右端是 $(M + |B|)\varepsilon$ 而不是 $\varepsilon$, 其中 $M + |B|$ 是一个与 $\varepsilon$ 无关的常数 (没有特别要求 $M + |B|$ 为正数). 相较于我们刻意使得 (3.1.12) 式的右端为 $\varepsilon$, 并在 (3.1.11) 式中, 为避免分母为零而采用 $1 + |\alpha| + |\beta|$ 代替 $|\alpha| + |\beta|$, 这无疑更为方便.

例3.1.6 计算 $\lim_{n\to +\infty}\frac{5n^3 - 65n^2 + 2n - 17}{3n^3 + 4n^2 + 4n - 3}.$

解 运用极限四则运算的性质, 我们有

$$
\begin{array}{l} \lim _ {n \to + \infty} \frac {5 n ^ {3} - 6 5 n ^ {2} + 2 n - 1 7}{3 n ^ {3} + 4 n ^ {2} + 4 n - 3} = \lim _ {n \to + \infty} \frac {5 - \frac {6 5}{n} + \frac {2}{n ^ {2}} - \frac {1 7}{n ^ {3}}}{3 + \frac {4}{n} + \frac {4}{n ^ {2}} - \frac {3}{n ^ {3}}} \\ = \frac {5 - \lim _ {n \rightarrow + \infty} \frac {6 5}{n} + \lim _ {n \rightarrow + \infty} \frac {2}{n ^ {2}} - \lim _ {n \rightarrow + \infty} \frac {1 7}{n ^ {3}}}{3 + \lim _ {n \rightarrow + \infty} \frac {4}{n} + \lim _ {n \rightarrow + \infty} \frac {4}{n ^ {2}} - \lim _ {n \rightarrow + \infty} \frac {3}{n ^ {3}}} \\ = \frac {5 - 6 5 \cdot 0 + 2 \cdot 0 - 1 7 \cdot 0}{3 + 4 \cdot 0 + 4 \cdot 0 - 3 \cdot 0} = \frac {5}{3}. \tag {3.1.16} \\ \end{array}
$$

上面的计算过程以及书写方式太过详细, 对于书写和阅读都是一种负担. 一般说来, 对

---

52

第三章 序列极限

于初学者, 如下写法就足够详细了:

$$
\lim _ {n \to + \infty} \frac {5 n ^ {3} - 6 5 n ^ {2} + 2 n - 1 7}{3 n ^ {3} + 4 n ^ {2} + 4 n - 3} = \lim _ {n \to + \infty} \frac {5 - \frac {6 5}{n} + \frac {2}{n ^ {2}} - \frac {1 7}{n ^ {3}}}{3 + \frac {4}{n} + \frac {4}{n ^ {2}} - \frac {3}{n ^ {3}}} = \frac {5}{3}.
$$

以后, 对于如此简单的极限, 可直接写出答案:

$$
\lim _ {n \to + \infty} \frac {5 n ^ {3} - 6 5 n ^ {2} + 2 n - 1 7}{3 n ^ {3} + 4 n ^ {2} + 4 n - 3} = \frac {5}{3}.
$$

由定理 3.1.3(1) 的结论直接可得, 任何有限个数列 “和的极限等于极限的和”. 但这一结论不能推广到无限和. 尤其要注意不能推广到形式上有限个, 实质上为无限个数列的和.

例 3.1.7 计算  $\lim_{n\to+\infty}\left(\frac{1}{n^{2}}+\frac{2}{n^{2}}+\cdots+\frac{n}{n^{2}}\right)$ .

解 如果利用“和的极限等于极限的和”得到

$$
\begin{array}{l} \lim _ {n \to + \infty} \left(\frac {1}{n ^ {2}} + \frac {2}{n ^ {2}} + \dots + \frac {n}{n ^ {2}}\right) \\ = \lim _ {n \to + \infty} \frac {1}{n ^ {2}} + \lim _ {n \to + \infty} \frac {2}{n ^ {2}} + \dots + \lim _ {n \to + \infty} \frac {n}{n ^ {2}} \\ = 0 + 0 + \dots + 0 = 0. \\ \end{array}
$$

则论证过程以及结论都是错误的. 这是因为这里和式的项数 $n$ 随着 $n$ 的增大而增大, 并没有一个上限. 以下是正确的推导过程:

$$
\begin{array}{l} \lim _ {n \to + \infty} \left(\frac {1}{n ^ {2}} + \frac {2}{n ^ {2}} + \dots + \frac {n}{n ^ {2}}\right) = \lim _ {n \to + \infty} \frac {1 + 2 + \cdots + n}{n ^ {2}} \\ = \lim _ {n \to + \infty} \frac {n (n + 1)}{2 n ^ {2}} = \frac {1}{2}. \\ \end{array}
$$

通常我们不能像例 3.1.7 那样得到和的表达式. 此时, 可通过适当的放大和缩小, 最后利用夹逼准则得到极限. 如何恰到好处地进行 “放缩”(估计), 是最能体现分析这门学科的基本技巧和思想的地方.

例3.1.8 求 $\lim_{n\to +\infty}\left(\frac{n}{n^2 + 1} +\frac{n - 1}{n^2 + 2} +\dots +\frac{1}{n^2 + n}\right)$

解 我们有

$$
\frac {n + (n - 1) + \cdots + 1}{n ^ {2} + n} \leqslant \frac {n}{n ^ {2} + 1} + \frac {n - 1}{n ^ {2} + 2} + \dots + \frac {1}{n ^ {2} + n} \leqslant \frac {n + (n - 1) + \cdots + 1}{n ^ {2}}.
$$

同例3.1.7, 可得

$$
\lim _ {n \to + \infty} \frac {n + (n - 1) + \cdots + 1}{n ^ {2} + n} = \lim _ {n \to + \infty} \frac {n + (n - 1) + \cdots + 1}{n ^ {2}} = \frac {1}{2}.
$$

于是，由夹逼准则，得到

$$
\lim _ {n \to + \infty} \left(\frac {n}{n ^ {2} + 1} + \frac {n - 1}{n ^ {2} + 2} + \dots + \frac {1}{n ^ {2} + n}\right) = \frac {1}{2}.
$$

---

3.2 无穷大量 无穷小量 Stolz 公式

53

## 习题3.1

1. 用定义证明 $\lim_{n\to +\infty}\frac{3n^3 + 4n^2 - 100}{2n^3 - 9n - 11} = \frac{3}{2}$.

2. 用定义证明 $\lim_{n\to +\infty}\lg \left(1 + \frac{1}{n}\right) = 0.$

3. 证明: $\lim_{n\to +\infty}a_n = 0$ 的充要条件是存在单调下降且无正下界的正数列 $\{\omega_n\}$ 使得 $\forall n\geqslant 1$ 有 $|a_{n}|\leqslant \omega_{n}$.

4. 计算极限  $\lim_{n\to+\infty}\frac{2\sqrt[n]{n}+\sqrt[n]{100}}{3\sqrt[n]{n}-1}$ .

5. 计算极限  $\lim_{n\to+\infty}\left(\frac{3\lg^{3}n+2\lg n+1}{2\lg^{2}n+\lg n}-\frac{6\lg^{3}n+5\lg^{2}n+3\lg n+1}{4\lg^{2}n-\lg n+2}\right)$ .

6. 计算极限  $\lim_{n\to+\infty}\left(\left(1+\frac{1}{n}\right)^{n}+\left(2+\frac{3}{n}\right)^{n}+\left(3+\frac{5}{n}\right)^{n}\right)^{\frac{1}{n}}$

7. 设  $0 \leqslant p \leqslant k - 1$ ，求: $\lim_{n \to +\infty} \frac{C_{kn}^{p} + C_{kn}^{p+k} + \cdots + C_{kn}^{p+(n-1)k}}{2^{kn}}$ .

## 3.2 无穷大量 无穷小量 Stolz 公式

易见 $\lim_{n\to +\infty}a_n = A$ 等价于 $\lim_{n\to +\infty}|a_n - A| = 0.$ 结合夹逼准则, 在证明 $\lim_{n\to +\infty}a_n = A$ 时时常寻求如下不等式:

$$
\left| a _ {n} - b _ {n} \right| \leqslant c _ {n}, \quad \forall n \gg 1,
$$

其中 $\lim_{n\to +\infty}b_n = A,\lim_{n\to +\infty}c_n = 0.$ 因此，极限为零的数列是需要特别关注的数列.类似地，也需要特别关注极限为无穷的数列.具体地，我们给出如下定义:

定义 3.2.1 考虑实数列  $\{a_{n}\}$ .

(1) 若  $\lim_{n\to+\infty}a_{n}=0$ ，则称  $\{a_{n}\}$  为无穷小量；

(2) 若对任何 $M > 0$, 存在 $N \geqslant 1$, 使得当 $n \geqslant N$ 时有 $a_{n} > M$, 则称 $\{a_{n}\}$ 为正无穷大量, 记作 $\lim_{n \to +\infty} a_{n} = +\infty$, 或 $a_{n} \to +\infty (n \to +\infty)$, 或

$$
a _ {n} \rightarrow + \infty , \qquad \text {当} n \rightarrow + \infty \text {时};
$$

(3) 若 $\{-a_{n}\}$ 是正无穷大量, 则称 $\{a_{n}\}$ 为负无穷大量, 记作 $\lim_{n\to +\infty}a_n = -\infty$, 或 $a_{n}\rightarrow -\infty (n\rightarrow +\infty)$, 或

$$
a _ {n} \rightarrow - \infty , \qquad \text {当} n \rightarrow + \infty \text {时};
$$

(4) 若  $\{|a_{n}|\}$  为正无穷大量, 则称  $\{a_{n}\}$  为无穷大量, 记作  $\lim_{n\to+\infty}a_{n}=\infty$ , 或  $a_{n}\to\infty(n\to+\infty)$ , 或

$$
a _ {n} \to \infty , \qquad \text {当} n \to + \infty \text {时}.
$$

---

54

第三章 序列极限

当 $\lim_{n\to +\infty}a_n = +\infty (-\infty$ 或 $\infty)$ 时，可称 $\{a_{n}\}$ 的极限为 $+\infty (-\infty$ 或 $\infty)$. 此时，$\{a_{n}\}$ 是发散的，仍然称 $\{a_{n}\}$ 的极限不存在. 但当 $\lim_{n\to +\infty}a_n = +\infty$ 或 $-\infty$ 时，可称 $\{a_{n}\}$ 在广义实数系中的极限存在或收敛.

在极限的讨论中, 引入如下记号可以带来很大的方便.

定义 3.2.2 考虑实数列  $\{a_{n}\}$  和  $\{b_{n}\}$ . 设有  $N \geqslant 1$  使得当  $n \geqslant N$  时  $b_{n} \neq 0$ .

(1) 若  $\lim_{n\to+\infty}\frac{a_{n}}{b_{n}}=0,$  则记

$$
a _ {n} = o (b _ {n}), \qquad {\text {当}} n \to + \infty \text {时}.
$$

此时, 若 $\{a_{n}\}$ 与 $\{b_{n}\}$ 均为无穷小量, 则称 $\{a_{n}\}$ 是 $\{b_{n}\}$ 的高阶无穷小量, 称 $\{b_{n}\}$ 是 $\{a_{n}\}$ 的低阶无穷小量; 若 $\{a_{n}\}$ 与 $\{b_{n}\}$ 均为无穷大量, 则称 $\{a_{n}\}$ 是 $\{b_{n}\}$ 的低阶无穷大量, 称 $\{b_{n}\}$ 是 $\{a_{n}\}$ 的高阶无穷大量.

(2) 若  $\left\{\frac{a_{n}}{b_{n}}\right\}_{N}^{\infty}$  有界, 则记

$$
a _ {n} = O (b _ {n}), \qquad \text {当} n \to + \infty \text {时}.
$$

(3) 若 $\lim_{n\to +\infty}\frac{a_n}{b_n} = 1$ ，则称 $\{a_n\}$ 与 $\{b_n\}$ 等价，记作

$$
a _ {n} \sim b _ {n}, \qquad \text {当} n \to + \infty \text {时}.
$$

若 $\lim_{n\to +\infty}\frac{a_n}{b_n}$ 存在且不等于零, 则称 $\{a_n\}$ 与 $\{b_n\}$ 同阶.

等价和同阶主要用于 $\{a_{n}\}$ 与 $\{b_n\}$ 均为无穷大量或均为无穷小量的情形.

利用上述记号, 无穷小量可以记作 $o(1)$, 有界量可以记作 $O(1)$.

对于等价量, 利用极限的四则运算, 易见有以下结果.

定理 3.2.1 设  $\{a_{n}\}, \{b_{n}\}$  与  $\{x_{n}\}$  为实数列. 又  $\lim_{n\to+\infty}\frac{a_{n}}{b_{n}}=1,\ell$  是有限数、 $+\infty,-\infty$  或  $\infty$ .

(1) 若  $\lim_{n\to+\infty}a_{n}x_{n}=\ell,$  则  $\lim_{n\to+\infty}b_{n}x_{n}=\ell;$

(2) 若  $\lim_{n\to+\infty}\frac{x_{n}}{a_{n}}=\ell,$  则  $\lim_{n\to+\infty}\frac{x_{n}}{b_{n}}=\ell.$

证明 定理的证明是简单的. 具体地, 我们有

(1) $\lim_{n\to +\infty}b_nx_n = \lim_{n\to +\infty}(a_nx_n)\cdot \lim_{n\to +\infty}\frac{b_n}{a_n} = \ell \cdot 1 = \ell .$
(2) $\lim_{n\to +\infty}\frac{x_n}{b_n} = \lim_{n\to +\infty}\frac{x_n}{a_n}\cdot \lim_{n\to +\infty}\frac{a_n}{b_n} = \ell \cdot 1 = \ell .$

我们给出上述证明过程, 主要是希望读者在具体使用这一定理时, 心里也有这样一个证明过程.

例3.2.1 由于 $\lim_{n\to +\infty}\frac{(n + 1)^{-1}}{n^{-1}} = 1,$ 因此

$$
\lim _ {n \to + \infty} \frac {n ^ {- 1} - (n + 1) ^ {- 1}}{n ^ {- 2}} = \lim _ {n \to + \infty} \frac {n ^ {- 1} - n ^ {- 1}}{n ^ {- 2}} = 0.
$$

---

3.2 无穷大量 无穷小量 Stolz 公式

55

自然, 上述推导过程是错误的. 如果写成

$$
\begin{array}{l} \lim _ {n \to + \infty} \frac {n ^ {- 1} - (n + 1) ^ {- 1}}{n ^ {- 2}} = \lim _ {n \to + \infty} \frac {n ^ {- 1}}{n ^ {- 2}} - \lim _ {n \to + \infty} \frac {(n + 1) ^ {- 1}}{n ^ {- 2}} \\ = \lim _ {n \to + \infty} \frac {n ^ {- 1}}{n ^ {- 2}} - \lim _ {n \to + \infty} \frac {n ^ {- 1}}{n ^ {- 2}} = 0, \\ \end{array}
$$

同样也是错误的. 第一个等式后的两个极限不存在, 因此不能用四则运算中 “和的极限等于极限的和”. 而最后一个等式的左边事实上是  $(+\infty)-(+\infty)$ , 它是没有意义的, 自然这一步也是错的.

再者, 如果写

$$
\lim _ {n \to + \infty} \frac {n ^ {- 1} + (n + 1) ^ {- 1}}{n ^ {- 1}} = \lim _ {n \to + \infty} \frac {n ^ {- 1} + n ^ {- 1}}{n ^ {- 1}} = 2,
$$

虽然结论是正确的,但过程的准确性就有疑问.自然,如下的过程是正确的:

$$
\begin{array}{l} \lim _ {n \to + \infty} \frac {n ^ {- 1} + (n + 1) ^ {- 1}}{n ^ {- 1}} = \lim _ {n \to + \infty} \frac {n ^ {- 1}}{n ^ {- 1}} + \lim _ {n \to + \infty} \frac {(n + 1) ^ {- 1}}{n ^ {- 1}} \\ = \lim _ {n \to + \infty} \frac {n ^ {- 1}}{n ^ {- 1}} + \lim _ {n \to + \infty} \frac {n ^ {- 1}}{n ^ {- 1}} = 1 + 1 = 2. \\ \end{array}
$$

这里我们刻意写了较完整的计算步骤. 事实上, 只要写出关键的第一步, 其后的两步可以省略.

另一方面, 我们有

定理 3.2.2 设实数列 $\{a_{n}\}$ 与 $\{b_{n}\}$ 分别为无穷小量与有界量, 则 $\{a_{n}b_{n}\}$ 为无穷小量.

例3.2.2 由于 $\lim_{n\to +\infty}\frac{1}{n} = 0,\{\sin n\}$ 有界,因此，由定理3.2.2可得 $\lim_{n\to +\infty}\frac{\sin n}{n} =$ 0.但我们不能写

$$
\lim _ {n \to + \infty} \frac {\sin n}{n} = \lim _ {n \to + \infty} \frac {1}{n} \cdot \lim _ {n \to + \infty} \sin n = 0 \cdot \lim _ {n \to + \infty} \sin n = 0.
$$

这是因为 (可以证明) $\lim_{n\to +\infty}\sin n$ 不存在.

在处理商的极限时, 时常需要面对分子、分母同时为无穷小量或无穷大量的情形, 我们称之为 $\frac{0}{0}$ 型或 $\frac{\infty}{\infty}$ 型的不定式. 对此, 一个有效的工具是以下的 Stolz-Cesàro$^{①}$ 定理$^{②}$.

定理3.2.3 设 $\{x_{n}\}$ 和 $\{y_{n}\}$ 是两个实数列, 若

(1) $\{y_{n}\}$ 严格单调增加;
(2) $\lim_{n\to +\infty}y_n = +\infty;$
(3) $\lim_{n\to +\infty}\frac{x_{n + 1} - x_n}{y_{n + 1} - y_n} = \ell$ ，其中 $\ell$ 可以是有限数、 $+\infty$ 或 $-\infty ,$

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">① Cesàro, Ernesto, 1859 年 3 月 12 日—1906 年 9 月 12 日, 意大利数学家.</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">② Stolz-Cesàro 定理习惯上称为 Stolz 定理, 也常称为 Stolz 公式.</span></small>

---

56

第三章 序列极限

则

$$
\lim _ {n \to + \infty} \frac {x _ {n}}{y _ {n}} = \ell . \tag {3.2.1}
$$

证明 我们仅就 $\ell$ 为有限数的情形加以证明. 其余情形类似可证.

由(2)，存在 $N_{1}\geqslant 1$ 使得当 $n\geqslant N_1$ 时，有 $y_{n} > 0$

$\forall\varepsilon\in(0,1)$ ，由(3)，存在 $N_{2}\geqslant N_{1}$ 使得当 $n\geqslant N_{2}$ 时，有

$$
\ell - \varepsilon <   \frac {x _ {n + 1} - x _ {n}}{y _ {n + 1} - y _ {n}} <   \ell + \varepsilon .
$$

即

$$
(\ell - \varepsilon) (y _ {n + 1} - y _ {n}) <   x _ {n + 1} - x _ {n} <   (\ell + \varepsilon) (y _ {n + 1} - y _ {n}).
$$

进而有

$$
(\ell - \varepsilon) \sum_ {k = N _ {2}} ^ {n - 1} \left(y _ {k + 1} - y _ {k}\right) <   \sum_ {k = N _ {2}} ^ {n - 1} \left(x _ {k + 1} - x _ {k}\right) <   (\ell + \varepsilon) \sum_ {k = N _ {2}} ^ {n - 1} \left(y _ {k + 1} - y _ {k}\right), \quad \forall n > N _ {2}.
$$

即

$$
(\ell - \varepsilon) (y _ {n} - y _ {N _ {2}}) <   x _ {n} - x _ {N _ {2}} <   (\ell + \varepsilon) (y _ {n} - y _ {N _ {2}}), \quad \forall n > N _ {2}.
$$

整理得到

$$
- \varepsilon - (\ell - \varepsilon) \frac {y _ {N _ {2}}}{y _ {n}} + \frac {x _ {N _ {2}}}{y _ {n}} <   \frac {x _ {n}}{y _ {n}} - \ell <   \varepsilon - (\ell + \varepsilon) \frac {y _ {N _ {2}}}{y _ {n}} + \frac {x _ {N _ {2}}}{y _ {n}}, \quad \forall n > N _ {2}. \tag {3.2.2}
$$

再次由条件 (2), 可得存在  $N \geqslant N_{2}$  使得当  $n \geqslant N$  时, 有

$$
\frac {\big (| \ell | + \varepsilon \big) | y _ {N _ {2}} | + | x _ {N _ {2}} |}{y _ {n}} <   \varepsilon .
$$

结合 (3.2.2) 式得到

$$
\left| \frac {x _ {n}}{y _ {n}} - \ell \right| <   2 \varepsilon , \quad \forall n \geqslant N.
$$

从而由极限定义知 (3.2.1) 式成立.

由于定理条件没有要求 $\{x_{n}\}$ 趋于无穷, 因此, 这一类型的 $\frac{x_n}{y_n}$ 称为 $\frac{*}{\infty}$ 型的不定式. 由 Stolz 定理, 可得如下推论.

推论 3.2.4 设有实数列  $\{x_{n}\}$ .

(1) 若  $\lim_{n\to+\infty}(x_{n+1}-x_n)=\ell,$  则  $\lim_{n\to+\infty}\frac{x_n}{n}=\ell,$  其中  $\ell$  可以是有限数、 $+\infty$  或  $-\infty;$
(2) 若  $\lim_{n\to+\infty}x_n=\ell,$  则  $\lim_{n\to+\infty}\frac{x_1+x_2+\cdots+x_n}{n}=\ell,$  其中  $\ell$  可以是有限数、 $+\infty$  或  $-\infty;$
(3) 若 $\{x_{n}\}$ 为正数列, 且 $\lim_{n\to +\infty}\frac{x_{n + 1}}{x_n} = \ell$, 则 $\lim_{n\to +\infty}\sqrt[n]{x_n} = \ell$, 其中 $\ell$ 可以是有限数或 $+\infty$.

---

3.2 无穷大量 无穷小量 Stolz 公式

57

易见, (1) 和 (2) 本质上是一样的. 严格说来, 目前 (3) 还不能由 Stolz 定理直接得到. 它需要结合指数函数与对数函数的连续性得到. 但我们可以仿照定理 3.2.3 的证明直接证明 (3).

例 3.2.3 设 k 为自然数, 计算  $\lim_{n\to+\infty}\frac{1^{k}+2^{k}+\cdots+n^{k}}{n^{k+1}}$ .

解 由 Stolz 定理, 我们有

$$
\begin{array}{l} \lim _ {n \to + \infty} \frac {1 ^ {k} + 2 ^ {k} + \cdots + n ^ {k}}{n ^ {k + 1}} = \lim _ {n \to + \infty} \frac {(n + 1) ^ {k}}{(n + 1) ^ {k + 1} - n ^ {k + 1}} \\ = \lim _ {n \to + \infty} \frac {n ^ {k}}{\mathrm{C} _ {k + 1} ^ {1} n ^ {k} + \mathrm{C} _ {k + 1} ^ {2} n ^ {k - 1} + \cdots + \mathrm{C} _ {k + 1} ^ {k} n + \mathrm{C} _ {k + 1} ^ {k + 1}} \\ = \frac {1}{k + 1}. \\ \end{array}
$$

结合定理 2.4.4 以及夹逼准则, 让我们有可能处理 k 不为整数时的极限. 我们把它留作习题.

例3.2.4 设 $k$ 为自然数， $\lim_{n\to +\infty}a_n = a.$ 证明:

$$
\lim _ {n \to + \infty} \frac {n ^ {k} a _ {1} + (n - 1) ^ {k} a _ {2} + \cdots + a _ {n}}{n ^ {k + 1}} = \frac {a}{k + 1}. \tag {3.2.3}
$$

证明 本例是上例的推广. 由上例的结果, 若 $a_{n} \equiv a$, 则结论成立. 鉴此, 令 $\alpha_{n} = a_{n} - a$, 则问题化为在条件 $\lim_{n \to +\infty} \alpha_{n} = 0$ 下证明

$$
\lim _ {n \to + \infty} \frac {n ^ {k} \alpha_ {1} + (n - 1) ^ {k} \alpha_ {2} + \cdots + \alpha_ {n}}{n ^ {k + 1}} = 0. \tag {3.2.4}
$$

这相当于说, 不妨设 a = 0.

我们有

$$
\left| \frac {n ^ {k} \alpha_ {1} + (n - 1) ^ {k} \alpha_ {2} + \cdots + \alpha_ {n}}{n ^ {k + 1}} \right| \leqslant \frac {| \alpha_ {1} | + | \alpha_ {2} | + \cdots + | \alpha_ {n} |}{n}, \quad n \geqslant 1.
$$

于是结合 Stolz 公式与夹逼准则得到 (3.2.4) 式. 结论得证.

易见在证明 (3.2.4) 式的过程中, 对于变量的缩放, 要比直接证明 (3.2.3) 式放得开手脚. 在下例中, 把问题化为证明某个数列的极限为零起到了重要作用.

例3.2.5 设数列 $\{2x_{n + 1} + x_n\}$ 收敛. 证明: $\{x_{n}\}$ 也收敛.

证明 不妨设 $\{2x_{n + 1} + x_n\}$ 收敛到零. 此时 $\lim_{n\to +\infty}(-1)^n (2x_{n + 1} + x_n) = 0.$ 我们有

$$
\begin{array}{l} \lim _ {n \to + \infty} (- 1) ^ {n} x _ {n} = \lim _ {n \to + \infty} \frac {(- 2) ^ {n} x _ {n}}{2 ^ {n}} \\ = \lim _ {n \to + \infty} \frac {(- 2) ^ {n + 1} x _ {n + 1} - (- 2) ^ {n} x _ {n}}{2 ^ {n + 1} - 2 ^ {n}} \\ \end{array}
$$

---

58

第三章 序列极限

$$
= \lim _ {n \to + \infty} (- 1) ^ {n + 1} (2 x _ {n + 1} + x _ {n}) = 0.
$$

因此, $\{x_{n}\}$ 收敛于零.

在上面的论证中, 如果不设  $\{2x_{n+1} + x_{n}\}$  收敛到零, 则在 Stolz 公式的运用中就会遇到麻烦. 读者也可以利用反证法证明例 3.2.5 的结论.

对于分子、分母都是无穷小量的情形, 即  $\frac{0}{0}$  型的不定式, 有如下类似的结果 (同样称之为 Stolz 定理):

定理3.2.5 设有实数列 $\{x_{n}\}$ 和 $\{y_{n}\}$, 若

(1) $\{y_{n}\}$ 严格单调减少;
(2) $\lim_{n\to +\infty}x_n = \lim_{n\to +\infty}y_n = 0;$
(3) $\lim_{n\to +\infty}\frac{x_n - x_{n + 1}}{y_n - y_{n + 1}} = \ell$ ，其中 $\ell$ 可以是有限数、 $+\infty$ 或 $-\infty ,$

则

$$
\lim _ {n \to + \infty} \frac {x _ {n}}{y _ {n}} = \ell . \tag {3.2.5}
$$

证明 定理的证明与定理3.2.3的证明是完全类似的.这里我们对 $\ell = +\infty$ 的情形加以证明.其余情形类似可证.

首先, 由 (1) 和 (2), 易见 $\{y_{n}\}$ 是正数列.

$\forall M>0,$  由(3), 存在  $N\geqslant1$  使得当  $n\geqslant N$  时, 有

$$
\frac {x _ {n} - x _ {n + 1}}{y _ {n} - y _ {n + 1}} > M.
$$

即

$$
x _ {n} - x _ {n + 1} > M \Big (y _ {n} - y _ {n + 1} \Big), \qquad n \geqslant N.
$$

进而, 对任何  $m > n \geqslant N$ , 有

$$
x _ {n} - x _ {m + 1} > M \Big (y _ {n} - y _ {m + 1} \Big).
$$

在上式中令 $m\to +\infty$ 得到

$$
x _ {n} \geqslant M y _ {n}, \quad \forall n \geqslant N.
$$

即

$$
\frac {x _ {n}}{y _ {n}} \geqslant M, \quad \forall n \geqslant N.
$$

这就证明了  $\lim_{n\to+\infty}\frac{x_{n}}{y_{n}}=+\infty.$

例 3.2.6 设 k 为正整数, 计算

$$
\lim _ {n \to + \infty} \frac {(n + 1) ^ {- k - 1} + (n + 2) ^ {- k - 1} + \cdots + (2 n) ^ {- k - 1}}{n ^ {- k}}.
$$

---

3.2 无穷大量 无穷小量 Stolz 公式

59

解 要使用定理 3.2.5, 需要证明分子趋于零. 易见,

$$
0 \leqslant (n + 1) ^ {- k - 1} + (n + 2) ^ {- k - 1} + \dots + (2 n) ^ {- k - 1} \leqslant (n + 1) ^ {- k}.
$$

于是, 由夹逼准则得到

$$
\lim _ {n \to + \infty} \left((n + 1) ^ {- k - 1} + (n + 2) ^ {- k - 1} + \dots + (2 n) ^ {- k - 1}\right) = 0.
$$

这样, 由定理 3.2.5 得到

$$
\begin{array}{l} \lim _ {n \to + \infty} \frac {(n + 1) ^ {- k - 1} + (n + 2) ^ {- k - 1} + \cdots + (2 n) ^ {- k - 1}}{n ^ {- k}}. \\ = \lim _ {n \to + \infty} \frac {(n + 1) ^ {- k - 1} - (2 n + 1) ^ {- k - 1} - (2 n + 2) ^ {- k - 1}}{n ^ {- k} - (n + 1) ^ {- k}} \\ = \lim _ {n \to + \infty} \left(1 - \left(2 - \frac {1}{n + 1}\right) ^ {- k - 1} - 2 ^ {- k - 1}\right) \lim _ {n \to + \infty} \frac {1}{(n + 1) \left(\left(1 + \frac {1}{n}\right) ^ {k} - 1\right)} \\ = \frac {1 - 2 ^ {- k}}{k}. \\ \end{array}
$$

例3.2.7 设 $\ell \in \mathbb{R}$, 数列 $\{2x_{n} - x_{n + 1}\}$ 收敛于 $\ell$, 且 $\lim_{n\to +\infty}2^{-n}x_n = 0$. 证明: $\{x_{n}\}$ 也收敛于 $\ell$.

证明 由 Stolz 公式, 有

$$
\begin{array}{l} \lim _ {n \to + \infty} x _ {n} = \lim _ {n \to + \infty} \frac {2 ^ {- n} x _ {n}}{2 ^ {- n}} \\ = \lim _ {n \to + \infty} \frac {2 ^ {- n} x _ {n} - 2 ^ {- (n + 1)} x _ {n + 1}}{2 ^ {- n} - 2 ^ {- (n + 1)}} = \lim _ {n \to + \infty} (2 x _ {n} - x _ {n + 1}) = \ell . \\ \end{array}
$$

## 习题 3.2

1. 计算  $\lim_{n\to+\infty}\frac{n^{-1}-(n+1)^{-1}}{n^{-2}}$ .

2. 证明: $\lim_{n\to +\infty}\sin n$ 不存在.

3. $\{a_{n}\}$ 的极限为 $L$ 当且仅当 $\{a_{2n}\}$ 与 $\{a_{2n + 1}\}$ 的极限为 $L$, 其中 $L$ 为有限数、 $+\infty, -\infty$ 或 $\infty$.

4. 设  $\alpha > 0$ , 计算  $\lim_{n \to +\infty} \frac{1 + 2^{\alpha} + \cdots + n^{\alpha}}{n^{\alpha+1}}$ .

5. 若  $\alpha \in (-1,0)$ ，则极限  $\lim_{n\to+\infty}\frac{1+2^{\alpha}+\cdots+n^{\alpha}}{n^{\alpha+1}}$  是否存在？请说明理由。若存在，请进一步计算该极限。

6. 若  $\alpha < -1$ ，则极限  $\lim_{n\to+\infty}\frac{(n+1)^{\alpha}+(n+2)^{\alpha}+\cdots+(n+n)^{\alpha}}{n^{\alpha+1}}$  是否存在？请说明理由。若存在，请进一步计算该极限。

---

60

第三章 序列极限

7. 证明定理3.2.3与定理3.2.5的未证部分.

8. 设  $x_{1}=a, x_{2}=b, x_{n+2}=\frac{1}{2}(x_{n}+x_{n+1})$  ( $n=1,2,\cdots$ ). 试证明  $\{x_{n}\}$  收敛, 并求其极限.

(提示: 计算数列的通项公式, 或利用例 3.2.5.)

9. 设  $\{x_{n}\}$  满足  $\lim_{n\to+\infty}x_{n}\sum_{k=1}^{n}x_{k}^{2}=1$ . 证明:  $\lim_{n\to+\infty}\sqrt[3]{3n}x_{n}=1$ .

10. 设 a 和 d 是给定的正数. 对于  $n = 1, 2, 3, \cdots$ , 由等差数列  $a, a + d, \cdots, a + (n - 1)d$  形成算术平均  $A_{n}$  和几何平均  $G_{n}$ , 试求  $\lim_{n \to +\infty} \frac{G_{n}}{A_{n}}$ .

11. 令 $a_{n,k} = \frac{k}{n - k + 1} (n \geqslant k \geqslant 1)$. 证明:

(1) 对于固定的  $k \geqslant 1, \{a_{n,k}\}$  是无穷小量;

(2) $A_{n}:=\prod_{k=1}^{n}a_{n,k}$ 不是无穷小量.

12. 设 $E \subseteq \mathbb{R}$ 为非空集. 证明: 存在 $E$ 中点列 $\{x_k\}$ 使得 $\lim_{k \to +\infty} x_k = \sup E$, 这里 $\sup E$ 可以是 $+\infty$.

注: 对于 $f: D \to \mathbb{R}$, 满足 $\lim_{k \to +\infty} f(x_k) = \sup_{x \in D} f(x) (\inf_{x \in D} f(x))$ 的 $D$ 中的点列 $\{x_k\}$ 称为 $f$ 在 $D$ 上的极大化序列 (极小化序列).

13. (Toeplitz $^{①}$ 定理) 设有无穷三角矩阵 $(t_{nm})_{n\geqslant m}$ :

$$
\left( \begin{array}{c c c c} t _ {1 1} & & & \\ t _ {2 1} & t _ {2 2} & & \\ t _ {3 1} & t _ {3 2} & t _ {3 3} & \\ \vdots & \vdots & \vdots & \ddots \end{array} \right)
$$

满足下列条件:

(i) 每一列元趋于零, 即  $\lim_{n\to+\infty}t_{nm}=0;$

(ii) 各行元素的绝对值之和有界, 即  $\forall n \in N_{+}$ ,

$$
| t _ {n 1} | + | t _ {n 2} | + \dots + | t _ {n n} | \leqslant K <   + \infty .
$$

记  $y_{n}=t_{n1}x_{1}+t_{n2}x_{2}+\cdots+t_{nn}x_{n}$ . 证明:

(1) 若  $\lim_{n\to+\infty}x_{n}=0$ ，则  $\lim_{n\to+\infty}y_{n}=0$ .
(2) 记  $T_{n}=t_{n1}+t_{n2}+\cdots+t_{nn}$ . 若  $\lim_{n\to+\infty}T_{n}=1$ , 且  $\lim_{n\to+\infty}x_{n}=a$  有限, 则  $\lim_{n\to+\infty}y_{n}=a$ .

14. 试考察 Stolz 定理和 Toeplitz 定理的关系.

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">① Toeplitz, Otto, 1881 年 8 月 1 日—1940 年 2 月 15 日, 德国数学家.</span></small>

---

3.3 实数系基本定理

61

## 3.3 实数系基本定理

本节介绍实数系 $\mathbb{R}$ 中的基本定理, 这些定理在分析中有着重要的地位, 其中很多基本定理可以推广到高维情形乃至更抽象的情形.

首先, 我们重述确界存在定理, 即定理 2.3.3 和定理 2.3.5 如下:

定理 3.3.1 (1) R 中任何非空上有界集有上确界;

(2) $\mathbb{R}$ 中任何非空下有界集有下确界.

## 3.3.1 单调收敛定理

由确界存在定理, 立即导出如下的单调收敛定理.

定理 3.3.2 R 中单调有界数列都有极限.

证明 设 $\{a_{n}\}$ 是 $\mathbb{R}$ 中的单调有界数列. 不妨设 $\{a_{n}\}$ 单调增加. 令 $A = \sup_{n\geqslant 1}a_n$. 则 $\forall \varepsilon >0$, 由上确界的定义, 存在 $N\geqslant 1$ 使得 $a_{N} > A - \varepsilon$. 于是由 $\{a_{n}\}$ 单增, 当 $n\geqslant N$ 时, 有 $A - \varepsilon < a_N\leqslant a_n\leqslant A$.

这样, 由极限定义得到 $\lim_{n\to +\infty}a_n = A$, 即 $\{a_n\}$ 有极限.

注意, 数列的极限为无穷不能够说成数列 “有极限”.

另一方面, 若 $\{a_{n}\}$ 单调增加, 则总有 $\lim_{n\to +\infty}a_n = \sup_{n\geqslant 1}a_n$. 同样地, 若 $\{a_{n}\}$ 单调减少, 则有 $\lim_{n\to +\infty}a_n = \inf_{n\geqslant 1}a_n$. 无论哪种情形, 我们都可以说, $\lim_{n\to +\infty}a_n$ 在广义实数系中存在.

例 3.3.1 设  $x_{0}>0, x_{n+1}=\sqrt{2+x_{n}} (n\geqslant0)$ . 证明  $\{x_{n}\}$  收敛并求极限.

证明 易见  $\{x_{n}\}$  是正数列. 进一步, 由递推公式,

$$
x _ {n + 1} - x _ {n} = \sqrt {2 + x _ {n}} - x _ {n} = \frac {(2 - x _ {n}) (1 + x _ {n})}{\sqrt {2 + x _ {n}} + x _ {n}}, \quad \forall n \geqslant 0. \tag {3.3.1}
$$

若 $x_0 \geqslant 2$，则利用递推式归纳可得 $x_n \geqslant 2 (\forall n \geqslant 0)$。进而，利用 (3.3.1) 式归纳可得 $\{x_n\}$ 单调减少。

若 $0 < x_0 < 2$, 归纳可得 $x_n < 2 (\forall n \geqslant 0)$. 进而, 利用 (3.3.1) 式归纳可得 $\{x_n\}$ 单调增加.

总之, $\{x_{n}\}$ 单调有界, 因此有极限, 设极限为 $L$. 则 $L \geqslant 0$. 将递推式平方后, 两端求极限得到 $L^{2} = 2 + L$. 结合 $L \geqslant 0$ 得到 $L = 2$. 即 $\lim_{n \to +\infty} x_{n} = 2$.

例3.3.2 设 $x_0 > 0, x_{n+1} = 2 + \frac{1}{x_n} (n \geqslant 0)$. 证明 $\{x_n\}$ 收敛并求极限.

---

62

第三章 序列极限

证明 利用递推公式归纳可证

$$
x _ {n} > 2, \quad \forall n \geqslant 1.
$$

进而

$$
2 <   x _ {n} <   2 + \frac {1}{2}, \quad \forall n \geqslant 2.
$$

进一步, 由递推公式可得,

$$
\begin{array}{l} x _ {n + 2} - x _ {n} = \frac {1}{x _ {n + 1}} - \frac {1}{x _ {n - 1}} = - \frac {x _ {n + 1} - x _ {n - 1}}{x _ {n + 1} x _ {n - 1}} \\ = \frac {x _ {n} - x _ {n - 2}}{x _ {n + 1} x _ {n - 1} x _ {n} x _ {n - 2}}, \quad \forall n \geqslant 2. \tag {3.3.2} \\ \end{array}
$$

这表明 $x_{n + 2} - x_n$ 与 $x_{n} - x_{n - 2}$ 同时为正、或同时为负、或同时为零.由此可见 $\{x_{2n}\}$ 与$\{x_{2n + 1}\}$ 都是单调有界数列，从而都收敛.设它们的极限依次为 $L$ 与 $\ell$ .则 $L,\ell \in \left[2,\frac{5}{2}\right]$

$$
L = 2 + \frac {1}{\ell}, \quad \ell = 2 + \frac {1}{L}.
$$

解得 $L = \ell = 1 + \sqrt{2}$. 即 $\{x_{2n}\}$ 与 $\{x_{2n+1}\}$ 均收敛到同一极限. 因此, $\{x_n\}$ 收敛, 且 $\lim_{n\to +\infty}x_n = 1 + \sqrt{2}$. □

例3.3.3 设 $x_0 \in (0,1)$, $x_{n+1} = x_n - x_n^3$ ($n \geqslant 0$). 证明: $\lim_{n \to +\infty} \sqrt{n} x_n = \frac{\sqrt{2}}{2}$.

证明 归纳可证 $\{x_{n}\}$ 为单调下降的正数列，从而收敛.设其极限为 $L$ ，则 $L = L - L^{3}$ .从而 $L = 0$ 即 $\lim_{n\to +\infty}x_n = 0.$ 于是

$$
\lim _ {n \to + \infty} \frac {x _ {n + 1}}{x _ {n}} = \lim _ {n \to + \infty} \left(1 - x _ {n} ^ {2}\right) = 1.
$$

而由 Stolz 公式,

$$
\begin{array}{l} \lim _ {n \to + \infty} \frac {x _ {n} ^ {- 2}}{n} = \lim _ {n \to + \infty} (x _ {n + 1} ^ {- 2} - x _ {n} ^ {- 2}) = \lim _ {n \to + \infty} \frac {x _ {n} ^ {2} - x _ {n + 1} ^ {2}}{x _ {n + 1} ^ {2} x _ {n} ^ {2}} \\ = \lim _ {n \to + \infty} \frac {x _ {n} ^ {4} (2 - x _ {n} ^ {2})}{x _ {n} ^ {4} (1 - x _ {n} ^ {2}) ^ {2}} = 2. \\ \end{array}
$$

即 $\lim_{n\to +\infty}nx_n^2 = \frac{1}{2}$ .最后，由

$$
\left| \sqrt {n} x _ {n} - \frac {\sqrt {2}}{2} \right| = \left| \frac {n x _ {n} ^ {2} - \frac {1}{2}}{\sqrt {n} x _ {n} + \frac {\sqrt {2}}{2}} \right| \leqslant \sqrt {2} \left| n x _ {n} ^ {2} - \frac {1}{2} \right|
$$

与夹逼准则得到 $\lim_{n\to +\infty}\sqrt{n} x_n = \frac{\sqrt{2}}{2}$ 今后，利用 $\sqrt{x}$ 的连续性与 $\lim_{n\to +\infty}nx_n^2 = \frac{1}{2}$ 以及$\{x_n\}$ 为正数列，可直接得到上述结论. □

---

3.3 实数系基本定理

63

## 3.3.2 e 的定义

人们发现, 用形为 $\left(1 + \frac{1}{10^n}\right)^{10^n}$ 或 $\left(1 - \frac{1}{10^n}\right)^{10^n}$ 这样的数字作底数, 制作对数表就比较简单. 而 $n$ 取得越大, 则对数表可达到的精度越大.

进一步, 人们发现数列 $\left\{\left(1 + \frac{1}{n}\right)^n\right\}$ 有极限, Euler① 将该极限记为 e. 在现代数学中, e 和圆周率 $\pi$ 时常出现在各种场合, 成为最重要的两个常数.

定理 3.3.3 数列  $\left\{\left(1+\frac{1}{n}\right)^{n}\right\}$  严格单增且有界, 从而收敛.

证明 我们用两种方法给出证明.

证法 1 对任何  $n \geqslant 1$ ，利用算术几何平均不等式，

$$
\left(1 + \frac {1}{n}\right) ^ {n} = \left(1 + \frac {1}{n}\right) ^ {n} \cdot 1 <   \left(\frac {n \left(1 + \frac {1}{n}\right) + 1}{n + 1}\right) ^ {n + 1} = \left(1 + \frac {1}{n + 1}\right) ^ {n + 1}, \tag {3.3.3}
$$

$$
\left(1 + \frac {1}{n}\right) ^ {n + 1} = \frac {1}{\left(\frac {n}{n + 1}\right) ^ {n + 1} \cdot 1} > \frac {1}{\left(\frac {(n + 1) \frac {n}{n + 1} + 1}{n + 2}\right) ^ {n + 2}} = \left(1 + \frac {1}{n + 1}\right) ^ {n + 2}. \tag {3.3.4}
$$

因此, $\left\{\left(1+\frac{1}{n}\right)^{n}\right\}$ 严格单增而 $\left\{\left(1+\frac{1}{n}\right)^{n+1}\right\}$ 严格单减.

从而

$$
2 = (1 + 1) ^ {1} \leqslant \left(1 + \frac {1}{n}\right) ^ {n} <   \left(1 + \frac {1}{n}\right) ^ {n + 1} \leqslant (1 + 1) ^ {2} = 4.
$$

于是, 又得到  $\left\{\left(1+\frac{1}{n}\right)^{n}\right\}$  有界, 从而收敛.

证法 2 对任何  $n \geqslant 1$ ，利用二项展开式，我们有

$$
\left(1 + \frac {1}{n}\right) ^ {n} = 1 + 1 + \frac {1}{2 !} \left(1 - \frac {1}{n}\right) + \dots + \frac {1}{n !} \prod_ {k = 1} ^ {n - 1} \left(1 - \frac {k}{n}\right). \tag {3.3.5}
$$

直接与  $\left(1+\frac{1}{n+1}\right)^{n+1}$  的展开式

$$
1 + 1 + \frac {1}{2 !} \left(1 - \frac {1}{n + 1}\right) + \dots + \frac {1}{n !} \prod_ {k = 1} ^ {n - 1} \left(1 - \frac {k}{n + 1}\right) + \frac {1}{(n + 1) !} \prod_ {k = 1} ^ {n} \left(1 - \frac {k}{n + 1}\right)
$$

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">① Euler, Leonhard, 1707 年 4 月 15 日—1783 年 9 月 18 日, 瑞士数学家、自然科学家.</span></small>

---

64

第三章 序列极限

比较, 即得 $\left\{\left(1 + \frac{1}{n}\right)^n\right\}$ 严格单增. 另一方面, 由 (3.3.5) 式还可以得到

$$
2 \leqslant \left(1 + \frac {1}{n}\right) ^ {n} \leqslant \sum_ {k = 0} ^ {n} \frac {1}{k !} <   2 + \sum_ {k = 2} ^ {\infty} \frac {1}{2 ^ {k - 1}} = 3.
$$

因此, $\left\{\left(1+\frac{1}{n}\right)^{n}\right\}$ 有界,从而收敛.

利用定理3.3.3证明中得到的 $\left\{\left(1 + \frac{1}{n}\right)^n\right\}$ 严格单增以及 $\left\{\left(1 + \frac{1}{n}\right)^{n + 1}\right\}$ 严格单减,可得

$$
\left(1 + \frac {1}{n}\right) ^ {n} <   \mathrm{e} <   \left(1 + \frac {1}{n}\right) ^ {n + 1}, \qquad \forall n \geqslant 1.
$$

两端取对数得到

$$
n \ln \left(1 + \frac {1}{n}\right) <   1 <   (n + 1) \ln \left(1 + \frac {1}{n}\right), \qquad \forall n \geqslant 1.
$$

即

$$
\frac {1}{n + 1} <   \ln \left(1 + \frac {1}{n}\right) <   \frac {1}{n}, \quad \forall n \geqslant 1. \tag {3.3.6}
$$

于是又有

$$
\lim _ {n \to + \infty} n \ln \left(1 + \frac {1}{n}\right) = 1. \tag {3.3.7}
$$

另一方面, 利用定理 3.3.3 证明中的 (3.3.5) 式, 对于固定的 $m \geqslant 2$, 当 $n \geqslant m$ 时, 有

$$
1 + 1 + \frac {1}{2 !} \left(1 - \frac {1}{n}\right) + \dots + \frac {1}{m !} \prod_ {k = 1} ^ {m - 1} \left(1 - \frac {k}{n}\right) \leqslant \left(1 + \frac {1}{n}\right) ^ {n} \leqslant \sum_ {k = 0} ^ {\infty} \frac {1}{k !}.
$$

在上式中令 $n\to +\infty$ 得到

$$
\sum_ {k = 0} ^ {m} \frac {1}{k !} \leqslant \mathrm{e} \leqslant \sum_ {k = 0} ^ {\infty} \frac {1}{k !}.
$$

再在上式中令 $m\to +\infty$ 即得

$$
\mathrm{e} = \sum_ {k = 0} ^ {\infty} \frac {1}{k !}. \tag {3.3.8}
$$

而利用 (3.3.8) 式, 可得对任何正整数 $m$, 有

$$
0 <   \mathrm{e} - \sum_ {k = 0} ^ {m} \frac {1}{k !} <   \frac {1}{(m + 1) !} \sum_ {k = m + 1} ^ {\infty} \frac {1}{(m + 1) ^ {k - m - 1}} = \frac {1}{m \cdot m !}.
$$

---

3.3 实数系基本定理

65

因此，

$$
0 <   m! \Big (\mathrm{e} - \sum_ {k = 0} ^ {m} \frac {1}{k !} \Big) <   \frac {1}{m}.
$$

这表明对任何正整数 $m, m! \mathrm{e}$ 的小数部分总不等于0. 因此, $\mathrm{e}$ 是一个无理数

下例中的常数 $\gamma$ 称为 Euler 常数, $\gamma \approx 0.5772$, 但人们至今还不知道 $\gamma$ 是否为无理数.

例 3.3.4 对于  $n \geqslant 1$ , 考虑

$$
a _ {n} = 1 + \frac {1}{2} + \dots + \frac {1}{n} - \ln n, \quad b _ {n} = 1 + \frac {1}{2} + \dots + \frac {1}{n} - \ln (n + 1).
$$

证明: $\{a_{n}\}$ 和 $\{b_{n}\}$ 均收敛, 且收敛到同一极限. 该极限称为 Euler 常数, 记为 $\gamma$.

证明 对于任何 $n \geqslant 1$, 由 (3.3.6) 式, 我们有

$$
\begin{array}{l} a _ {n + 1} - a _ {n} = \frac {1}{n + 1} - \ln (n + 1) + \ln n = \frac {1}{n + 1} - \ln \left(1 + \frac {1}{n}\right) <   0, \\ b _ {n + 1} - b _ {n} = \frac {1}{n + 1} - \ln (n + 2) + \ln (n + 1) = \frac {1}{n + 1} - \ln \left(1 + \frac {1}{n + 1}\right) > 0. \\ \end{array}
$$

因此， $\{a_{n}\}$  严格单减而  $\{b_{n}\}$  严格单增。另一方面，注意到  $a_{n}>b_{n}(n\geqslant1)$ ，可得

$$
b _ {1} \leqslant b _ {n} <   a _ {n} \leqslant a _ {1}, \quad \forall n \geqslant 1.
$$

即得 $\{a_{n}\}$ 与 $\{b_n\}$ 均单调有界, 从而有极限. 结合 $a_{n+1} = \frac{1}{n+1} + b_{n} (n \geqslant 1)$, 得到它们的极限相同. □

## 3.3.3 闭区间套定理

由单调收敛定理, 或直接利用确界存在定理, 容易得到如下的 Cauchy $^{①}$ -Cantor 闭区间套定理.

定理3.3.4 设 $\{[a_n, b_n]\}$ 是一列闭区间，满足

(1) 对任何 $n \geqslant 1$, $[a_{n+1}, b_{n+1}] \subseteq [a_n, b_n]$;
(2) $\lim_{n\to +\infty}(b_n - a_n) = 0,$

则  $\{[a_{n},b_{n}]\}$  有唯一的公共点.

证明 没有特别说明时, 定理中的 $a_{n}, b_{n}$ 是实数, 且 $a_{n} < b_{n} (n \geqslant 1)$. 因此, 由条件 (1), $\{a_{n}\}$ 单调增加, 且以 $a_{1}$ 为下界, $b_{1}$ 为上界. 因此 $\{a_{n}\}$ 是单调增加的有界数列. 设它的极限 $\xi$. 则由条件 (2),

$$
\lim _ {n \to + \infty} b _ {n} = \lim _ {n \to + \infty} a _ {n} + \lim _ {n \to + \infty} (b _ {n} - a _ {n}) = \xi .
$$

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">① Cauchy, Augustin-Louis, 1789 年 8 月 21 日—1857 年 5 月 23 日, 法国数学家.</span></small>

---

66

第三章 序列极限

另一方面, 任取 $m \geqslant 1$, 当 $n \geqslant m$ 时,

$$
a _ {m} \leqslant a _ {n} <   b _ {n} \leqslant b _ {m}.
$$

令 $n\to +\infty$ 得到

$$
a _ {m} \leqslant \xi \leqslant b _ {m}.
$$

即  $\xi$  是  $\{[a_{n}, b_{n}]\}$  的公共点.

另一方面, 若  $\eta$  也是  $\{[a_{n}, b_{n}]\}$  的公共点. 即对任何  $m \geqslant 1$ ,

$$
a _ {m} \leqslant \eta \leqslant b _ {m}.
$$

则由夹逼准则得到 $\eta = \xi$. 这表明 $\{[a_n, b_n]\}$ 只有唯一一个公共点 $\xi$.

![](../../raw/pages_0065-0080/images/page_79_image_10.jpg)

注3.3.1 定理3.3.4的结论相当于说， $\bigcap_{n = 1}^{\infty}[a_n,b_n] = \{\xi \}$ .若去掉定理的条件(2)，则可证

$$
\bigcap_ {n = 1} ^ {\infty} [ a _ {n}, b _ {n} ] = \left\{x \Big | \lim _ {n \to + \infty} a _ {n} \leqslant x \leqslant \lim _ {n \to + \infty} b _ {n} \right\}.
$$

特别地， $\bigcap_{n = 1}^{\infty}[a_n,b_n]\neq \varnothing$

但有界闭区间改为无界闭区间后,区间套的交集可能为空.例如

$$
\bigcap_ {n = 1} ^ {\infty} [ n, + \infty) = \varnothing.
$$

## 3.3.4 $\mathbb{R}$ 中的基本概念

为进一步的讨论, 我们引入 $\mathbb{R}$ 中的一些基本概念. 对于 $E \subseteq \mathbb{R}$, 用 $\mathscr{C}E$ 表示集合 $\mathbb{R} \setminus E$.

定义 3.3.1 设  $E \subseteq R$ .

(1) 若存在 $\delta > 0$ 使得 $(x_0 - \delta, x_0 + \delta) \subset E$, 则称 $x_0$ 为 $E$ 的内点. $E$ 的内点全体称为 $E$ 的内部, 记作 $E^\circ$.

若  $x_{0}$  是集合 V 的内点, 则称 V 为  $x_{0}$  的邻域.

(2) 若 $x_0$ 是 $\mathcal{C}E$ 的内点, 则称 $x_0$ 为 $E$ 的外点. 这等价于存在 $\delta > 0$ 使得 $(x_0 - \delta, x_0 + \delta) \cap E = \varnothing$. 外点全体称为外部.
(3) 若 $x_0$ 既不是 $E$ 的内点又不是 $E$ 的外点, 则称 $x_0$ 为 $E$ 的边界点. 这等价于: $\forall \delta > 0$, $(x_0 - \delta, x_0 + \delta)$ 内既有 $E$ 中的点, 又有不属于 $E$ 的点. 边界点全体称为边界, 记作 $\partial E$.

---

3.3 实数系基本定理

67

根据定义, $\mathbb{R}$ 被分成两两不交的三部分: 内部、外部和边界.

另一方面, 我们定义

定义 3.3.2 设  $E \subseteq R$ .

(1) 若对任何 $\delta > 0$, $(x_0 - \delta, x_0 + \delta) \cap E$ 为无限集, 则称 $x_0$ 为 $E$ 的聚点, 又称为极限点. $E$ 的极限点全体称为 $E$ 的导集, 记作 $E'$.
(2) 若存在 $\delta > 0$ 使得 $(x_0 - \delta, x_0 + \delta) \cap E = \{x_0\}$, 则称 $x_0$ 为 $E$ 的孤立点.

定理 3.3.5 若对任何  $\delta > 0, (x_{0} - \delta, x_{0} + \delta)$  内包含 E 中异于  $x_{0}$  的点，则  $x_{0}$  为 E 的聚点.

证明 任取 $\delta > 0$. 由假设, 存在 $x_{1} \in (x_{0} - \delta, x_{0} + \delta) \cap E$, 且 $x_{1} \neq x_{0}$. 从而 $\delta_{1} := |x_{1} - x_{0}| > 0$.

于是, 又有 $x_{2} \in (x_{0} - \delta_{1}, x_{0} + \delta_{1}) \cap E$, 满足 $x_{2} \neq x_{0}$. 依次可以找到 $E$ 中点列 $\{x_{n}\}$ 满足 $0 < |x_{n+1} - x_{0}| < |x_{n} - x_{0}| < \delta$. 所以 $(x_{0} - \delta, x_{0} + \delta)$ 内包含了 $E$ 中无限多个点. 即 $x_{0}$ 是 $E$ 的聚点. □

在以上定义的基础上, 我们可以给出 $\mathbb{R}$ 的另一种分类: $\mathbb{R}$ 按 $E$ 的导集、孤立点全体以及外部, 分成两两不交的三部分.

接下来我们引入开集和闭集.

定义 3.3.3 若 E 中的点都是其内点, 即  $E = E^{\circ}$ , 则称 E 为开集.

若 E 包含其所有聚点, 即  $E' \subseteq E$ , 则称 E 为闭集.

根据定义, $\varnothing$ 与 $\mathbb{R}$ 既是开集又是闭集. 今后我们将证明这也是 $\mathbb{R}$ 中仅有的两个既是开集又是闭集的集合.

由定义易见集合的内部是开集. 自然, 它的外部也是开集.

以下定理所列条件是集合为闭集的充要条件, 均可作为闭集的等价定义. 也是判断集合是否为闭集的最常用条件.

定理 3.3.6 设  $E \subseteq R$ . 则 E 为闭集当且仅当以下任一条件成立:

(1)  $\partial E \subseteq E;$
(2) CE 为开集;
(3) E 中任何收敛点列的极限均属于 E.

证明 由边界点与聚点的定义易见, 若 $x_0 \notin F$, 则 $x_0$ 是 $F$ 的边界点当且仅当它是 $F$ 的聚点. 即

$$
\mathscr {C} F \cap \partial F = \mathscr {C} F \cap F ^ {\prime}. \tag {3.3.9}
$$

(1) 由 (3.3.9) 式即得 E 为闭集, 即  $E' \subseteq E$  当且仅当  $\partial E \subseteq E$ .
(2) 由于 $\partial E = \partial (\mathscr{C}E)$, 由 (1), $E$ 为闭集当且仅当 $\mathscr{C}E \cap \partial (\mathscr{C}E) = \varnothing$. 注意到总有 $(\mathscr{C}E)^{\circ} \subseteq \mathscr{C}E \subseteq (\mathscr{C}E)^{\circ} \cup \partial (\mathscr{C}E)$, 可见 $E$ 为闭集等价于 $\mathscr{C}E = (\mathscr{C}E)^{\circ}$, 即 $\mathscr{C}E$ 为开集.

---

68

第三章 序列极限

(3) 若 $E$ 是闭集, 设 $E$ 中点列 $\{x_k\}$ 收敛到 $x_0$, 则当集合 $F := \{x_k | k \geqslant 1\}$ 为有限集时, 必有 $x_0 \in F$, 从而 $x_0 \in E$; 当 $F$ 为无限集时, 必有 $x_0 \in E'$, 从而也有 $x_0 \in E$.

另一方面, 若 $E$ 中收敛点列 $\{x_k\}$ 的极限总是属于 $E$, 则对任何 $x_0 \in E'$ 以及 $k \geqslant 1$, 存在 $x_k \in \left(x_0 - \frac{1}{k}, x_0 + \frac{1}{k}\right) \cap E$. 由此 $\{x_k\}$ 是 $E$ 中收敛到 $x_0$ 的点列, 所以 $x_0 \in E$, 从而 $E$ 为闭集.

对于开集, 有如下重要性质.

定理 3.3.7 (1) 任意个开集的并是开集;

(2) 任意有限个开集的交是开集.

证明 (1) 设 $\{V_{\alpha} | \alpha \in I\}$ 是开集族①, 我们要证 $V := \bigcup_{\alpha \in I} V_{\alpha}$ 是开集.

任取 $x \in V$, 我们有 $\alpha \in I$ 使得 $x \in V_{\alpha}$. 由于 $V_{\alpha}$ 为开集, 存在 $\delta > 0$ 使得 $(x - \delta, x + \delta) \subset V_{\alpha} \subseteq V$. 因此, $V$ 为开集.

(2) 设  $m \geqslant 1, V_{1}, V_{2}, \cdots, V_{m}$  为开集, 我们要证  $V := \bigcap_{1 \leqslant k \leqslant m} V_{k}$  是开集.

任取 $x \in V$, 则对于 $1 \leqslant k \leqslant m$, 都有 $x \in V_k$. 从而有 $\delta_k > 0$ 使得 $(x - \delta_k, x + \delta_k) \subset V_k$. 取 $\delta = \min_{1 \leqslant k \leqslant m} \delta_k$, 则 $\delta > 0$, 且 $(x - \delta, x + \delta) \subset V$. 因此, $V$ 为开集.

结合定理 3.3.6 (2) 和 De Morgan 定律可得如下定理.

定理 3.3.8 (1) 任意个闭集的交是闭集;

(2) 任意有限个闭集的并是闭集.

由定理3.3.8中的(1)以及 $\mathbb{R}$ 本身为闭集, 可见对于任何 $E \subseteq \mathbb{R}$, 集合 $\cap \{F | E \subseteq F \subseteq \mathbb{R}, F$ 为闭集} 是包含 $E$ 的最小闭集. 我们定义如下.

定义 3.3.4 称包含 E 的最小闭集为 E 的闭包, 记作  $\overline{E}$ .

不难证明

$$
\overline {{E}} = E \cup E ^ {\prime} = E \cup \partial E = \mathscr {C} (\mathscr {C} E) ^ {\circ}. \tag {3.3.10}
$$

我们把证明留给读者.

最后, 我们引入稠密性的概念.

定义3.3.5 (1) 若 $E \subseteq F \subseteq \overline{E}$, 则称 $E$ 在 $F$ 中稠密;

(2) 如果 $E$ 的闭包没有内点, 则称 $E$ 为无处稠密集, 又称疏朗集.

## 3.3.5 致密性定理与聚点原则

致密性定理是一个非常常用的定理, 而聚点原则与它之间的等价性非常直接.

定理 3.3.9 R 中任何有界无限集均有聚点.

证明 设 $E \subseteq \mathbb{R}$ 是有界无限集. 则有有界区间 $[a_1, b_1] \subseteq \mathbb{R}$ 使得 $E \subseteq [a_1, b_1]$.

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">① 不能按以下方式设: 设 $\{V_{n} | n \geqslant 1\}$ 为开集族.</span></small>

---

3.3 实数系基本定理

69

由于 $E$ 是无限集, 因此 $\left[a_1, \frac{a_1 + b_1}{2}\right] \cap E$ 与 $\left[\frac{a_1 + b_1}{2}, b_1\right] \cap E$ 至少有一个为无限集. 若 $\left[a_1, \frac{a_1 + b_1}{2}\right] \cap E$ 为无限集, 则令 $[a_2, b_2]$ 为 $\left[a_1, \frac{a_1 + b_1}{2}\right]$. 否则令 $[a_2, b_2]$ 为 $\left[\frac{a_1 + b_1}{2}, b_1\right]$. 这样 $[a_2, b_2] \subseteq [a_1, b_1], [a_2, b_2] \cap E$ 为无限集, 且 $b_2 - a_2 = \frac{b_1 - a_1}{2}$.

一般地, 若对于 $n \geqslant 2$, 已经取定 $[a_n, b_n]$ 使得 $[a_n, b_n] \cap E$ 为无限集. 则类似地可以取到 $[a_{n+1}, b_{n+1}] \subseteq [a_n, b_n]$, 使得 $[a_{n+1}, b_{n+1}] \cap E$ 为无限集, $b_{n+1} - a_{n+1} = \frac{b_n - a_n}{2}$.

这样，$\{[a_n, b_n]\}$ 是满足闭区间套定理所列条件的闭区间套，从而有唯一的公共点 $\xi$。

任取 $\delta > 0$, 由 $\lim_{n \to +\infty} a_n = \lim_{n \to +\infty} b_n = \xi$, 存在 $N \geqslant 1$ 使得 $\xi - \delta < a_N < b_N < \xi + \delta$. 从而 $[a_N, b_N] \subset (\xi - \delta, \xi + \delta)$. 由于 $[a_N, b_N] \cap E$ 是无限集, 因此 $(\xi - \delta, \xi + \delta) \cap E$ 是无限集, 即 $\xi$ 是 $E$ 的聚点.

接下来, 我们介绍致密性定理. 首先, 引入子列概念. 对于点列 $\{a_{n}\}_{n=1}^{\infty}$, 任取严格单增的正整数列 $\{n_{k}\}$, 称 $\{a_{n_{k}}\}$ 为 $\{a_{n}\}$ 的子列.

之前我们用到的  $\{a_{2n}\}$  与  $\{a_{2n+1}\}$  都是  $\{a_{n}\}$  的子列.  $\{a_{n}\}$  本身也是它自己的子列.

容易看到, 若 $\{a_{n}\}$ 的极限为 $L$, 则它的任何子列的极限也为 $L$. 这样, 若数列有两个收敛到不同值的子列, 则该数列发散. 例如, 数列 $\{(-1)^{n}\}$ 的子列 $\{(-1)^{2n}\}$ 收敛到 1, 而另一个子列 $\{(-1)^{2n+1}\}$ 收敛到 -1, 因此 $\{(-1)^{n}\}$ 发散.

接下来的 Bolzano $^{①}$ -Weierstrass 定理 3.3.10, 常常被称为致密性定理, 是我们今后最常用到的定理之一. 它与聚点原则非常类似.

定理 3.3.10 R 中任何有界数列都有收敛子列.

证明 设 $\{a_{n}\}$ 是 $\mathbb{R}$ 中有界数列. 考虑集合 $E := \{a_{n} | n \geqslant 1\}$, 则 $E$ 是有界集.

若 E 是有限集, 则必有某个元 a 在  $\{a_{n}\}$  中出现无限多次, 把相应的项取出来就形成  $\{a_{n}\}$  的一个取常值 a 的子列, 自然, 该子列收敛到 a.

若 $E$ 是无限集, 则 $E$ 有聚点, 设为 $\xi$. 由聚点定义, 在 $(\xi - 1, \xi + 1)$ 内有 $E$ 中无限多个点. 因此, 可以取到 $n_1 \geqslant 1$ 使得 $a_{n_1} \in (\xi - 1, \xi + 1)$. 进一步, 可取到 $n_2 > n_1$ 使得 $a_{n_2} \in \left(\xi - \frac{1}{2}, \xi + \frac{1}{2}\right)$. 依次可以取到严格单增的正整数列 $\{n_k\}$ 使得 $a_{n_{k+1}} \in \left(\xi - \frac{1}{k+1}, \xi + \frac{1}{k+1}\right)$. 易见, $\{a_{n_k}\}$ 是 $\{a_n\}$ 的收敛于 $\xi$ 的一个子列.

例3.3.5 设实数列 $\{x_{n}\}$ 满足等式

$$
x _ {n} ^ {5} - 5 x _ {n} ^ {4} + \frac {1 0 n ^ {2} + 1}{n ^ {2}} x _ {n} ^ {3} - (4 + 6 \sqrt [ n ]{n}) x _ {n} ^ {2} + \left(6 - \mathrm{e} ^ {\frac {1}{n}}\right) x _ {n} - 1 = 0, \quad \forall n \geqslant 1. \tag {3.3.11}
$$

证明: $\{x_{n}\}$ 收敛.

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">① Bolzano, Bernhard Placidus Johann Nepomuk, 1781 年 10 月 5 日—1848 年 12 月 18 日, 波希米亚数学家、神学家、哲学家、逻辑学家.</span></small>

---

70

第三章 序列极限

证明 我们断言 $\lim_{n\to +\infty}x_n = 1$。否则，由极限定义，存在 $\varepsilon_0 > 0$，使得对任何 $N\geqslant 1$ 都有 $n\geqslant N$ 满足 $|x_{n} - 1|\geqslant \varepsilon_{0}$。特别地，可取到 $\{x_{n}\}$ 的子列 $\{x_{k_n}\}$ 使得

$$
\left| x _ {k _ {n}} - 1 \right| \geqslant \varepsilon_ {0}, \quad \forall n \geqslant 1. \tag {3.3.12}
$$

另一方面，由 $2^{n} = (1 + 1)^{n}\geqslant n$ 可得 $n^{\frac{1}{n}}\leqslant 2(\forall n\geqslant 1)$ .于是当 $|x| > 39$ 时，

$$
\begin{array}{l} \left| x ^ {5} - 5 x ^ {4} + \frac {1 0 n ^ {2} + 1}{n ^ {2}} x ^ {3} - (4 + 6 \sqrt [ n ]{n}) x ^ {2} + (6 - \mathrm{e} ^ {\frac {1}{n}}) x - 1 \right| \\ \geqslant | x | ^ {5} - 5 | x | ^ {4} - 1 1 | x | ^ {3} - 1 6 | x | ^ {2} - 6 | x | - 1 \\ \geqslant | x | ^ {4} (| x | - 5 - 1 1 - 1 6 - 6 - 1) = | x | ^ {4} (| x | - 3 9) > 0, \quad \forall n \geqslant 1. \\ \end{array}
$$

因此， $|x_{n}|\leqslant 39(\forall n\geqslant 1)$ ，即 $\{x_{n}\}$ 是有界数列.进而其子列 $\{x_{k_n}\}$ 也是有界数列

由致密性定理, $\{x_{k_n}\}$ 有子列 $\{x_{m_n}\}$ 收敛, 设极限为 $\xi$. 由 (3.3.11) 式得到

$$
\xi^ {5} - 5 \xi^ {4} + 1 0 \xi^ {3} - 1 0 \xi^ {2} + 5 \xi - 1 = 0.
$$

解得 $\xi = 1$

另一方面, 由 (3.3.12) 式可得 $|\xi - 1| \geqslant \varepsilon_0$. 得到矛盾.

因此, 必有  $\lim_{n\to+\infty}x_{n}=1$ .

利用致密性定理, 容易将闭区间套定理 3.3.4 以及注 3.3.1 中的结论作如下推广. 对于非空集 E, 定义其直径为  $\mathrm{diam}E := \sup_{x, y \in E} |x - y|$ .

定理3.3.11 设 $\{E_n\}$ 为 $\mathbb{R}$ 中的有界非空闭集列，满足 $E_{n + 1}\subseteq E_n(n\geqslant 1)$ .则

(1) $\bigcap_{n=1}^{\infty} E_n \neq \varnothing$;
(2) (闭集套定理) 进一步, 若  $\lim_{n\to+\infty}\operatorname{diam}E_n=0$ , 则  $\bigcap_{n=1}^{\infty}E_n$  是单点集.

证明 由定理假设, 对每个 $n \geqslant 1$, 可取到 $x_{n} \in E_{n}$. 进一步, $\{x_{n}\}$ 有界, 从而有收敛子列 $\{x_{k_n}\}$, 设极限为 $\xi$.

对任何 $m \geqslant 1$, 当 $n \geqslant m$ 时有 $k_n \geqslant m$. 从而 $x_{k_n} \in E_{k_n} \subseteq E_m$. 由于 $E_m$ 是闭集, 因此 $\xi \in E_m$. 这就是说 $\xi \in \bigcap_{n=1}^{\infty} E_n$, 即 $\bigcap_{n=1}^{\infty} E_n \neq \varnothing$.

进一步, 对于 $\eta \in \bigcap_{n=1}^{\infty} E_n$, 有 $|\eta - \xi| \leqslant \mathrm{diam} E_n (\forall n \geqslant 1)$. 这样, 如果 $\lim_{n \to +\infty} \mathrm{diam} E_n = 0$, 则可得 $|\eta - \xi| \leqslant 0$, 即 $\eta = \xi$. 这表明此时 $\bigcap_{n=1}^{\infty} E_n$ 是单点集. $\square$

---

3.3 实数系基本定理

71

## 3.3.6 Cauchy 收敛准则

数列收敛的 Cauchy 收敛准则时常被看作数列收敛的等价定义, 其优点是不需要事先知道数列的极限. 首先, 定义基本列如下:

定义 3.3.6 称数列  $\{x_{n}\}$  为基本列或 Cauchy 列, 是指  $\forall \varepsilon > 0$ , 存在  $N \geqslant 1$ , 使得当  $m, n \geqslant N$  时, 有

$$
\left| x _ {m} - x _ {n} \right| <   \varepsilon . \tag {3.3.13}
$$

从定义可见 $\{x_{n}\}$ 是Cauchy列当且仅当

$$
\lim _ {N \rightarrow + \infty} \sup _ {m, n \geqslant N} \left| x _ {m} - x _ {n} \right| = 0. \tag {3.3.14}
$$

也等价于

$$
\lim _ {n \rightarrow + \infty} \sup _ {m \geqslant n} \left| x _ {m} - x _ {n} \right| = 0. \tag {3.3.15}
$$

我们有如下的 Cauchy 收敛准则.

定理 3.3.12 数列收敛的充要条件是它是基本列.

证明 (必要性) 若 $\lim_{n\to +\infty}a_n = A,$ 则 $\forall \varepsilon >0,$ 存在 $N\geqslant 1$ ，使得当 $n\geqslant N$ 时，有

$$
| a _ {n} - A | <   \frac {\varepsilon}{2}.
$$

从而当 $n, m \geqslant N$ 时, 有

$$
| a _ {n} - a _ {m} | \leqslant | a _ {n} - A | + | a _ {m} - A | <   \varepsilon ,
$$

即  $\{a_{n}\}$  是 Cauchy 列.

(充分性) 若  $\{a_{n}\}$  是 Cauchy 列, 则有  $N_{1} \geqslant 1$  使得当  $n \geqslant 1$  时, 有

$$
\left| a _ {n} - a _ {N _ {1}} \right| \leqslant 1.
$$

因此, $\{a_{n}\}$ 是有界数列. 于是由致密性定理, $\{a_{n}\}$ 有子列 $\{a_{n_k}\}$ 收敛, 设极限为 $\xi$.

另一方面, $\forall \varepsilon > 0$, 再次利用 $\{a_n\}$ 是 Cauchy 列, 知存在 $N \geqslant 1$, 使得当 $n, m \geqslant N$ 时, 有

$$
\left| a _ {n} - a _ {m} \right| <   \varepsilon .
$$

特别地, 注意到 $n_m \geqslant m \geqslant N$, 可得

$$
\left| a _ {n} - a _ {n _ {m}} \right| <   \varepsilon .
$$

上式中令 $m\to +\infty$ 即得

$$
| a _ {n} - \xi | \leqslant \varepsilon .
$$

于是, 由极限定义得到 $\lim_{n\to +\infty}a_n = \xi$.

□

---

72

第三章 序列极限

例 3.3.6 设 p > 1, 证明: (1)  $\sum_{n=1}^{\infty} \frac{1}{n^{p}}$  收敛; (2)  $\sum_{n=1}^{\infty} \frac{\sin n}{n^{p}}$  收敛.

证明 (1) 记 $\alpha = p - 1$. 由定理2.4.4的(2.4.9)式, 对任何 $n \geqslant 2$, 有

$$
\begin{array}{l} \frac {1}{n ^ {\alpha}} - \frac {1}{(n + 1) ^ {\alpha}} = \frac {1}{(n + 1) ^ {\alpha}} \left(\left(1 + \frac {1}{n}\right) ^ {\alpha} - 1\right) \\ > \frac {1}{(n + 1) ^ {\alpha}} \frac {\frac {\alpha}{n}}{1 + \frac {1}{n}} = \frac {\alpha}{(n + 1) ^ {p}}. \tag {3.3.16} \\ \end{array}
$$

于是，

$$
\sum_ {k = 2} ^ {n} \frac {1}{k ^ {p}} \leqslant \frac {1}{\alpha} \sum_ {k = 2} ^ {n} \left(\frac {1}{(k - 1) ^ {\alpha}} - \frac {1}{k ^ {\alpha}}\right) \leqslant \frac {1}{\alpha}.
$$

因此, $\left\{\sum_{k=1}^{n} \frac{1}{k^p}\right\}$ 是单调增加的有界数列. 所以 $\sum_{n=1}^{\infty} \frac{1}{n^p}$ 收敛.

(2) $\forall \varepsilon > 0$, 由 (1) 及 Cauchy 收敛准则, 存在 $N \geqslant 1$ 使得当 $m > n \geqslant N$ 时, 有

$$
\sum_ {k = n + 1} ^ {m} \frac {1}{k ^ {p}} = \left| \sum_ {k = 1} ^ {m} \frac {1}{k ^ {p}} - \sum_ {k = 1} ^ {n} \frac {1}{k ^ {p}} \right| <   \varepsilon .
$$

从而

$$
\left| \sum_ {k = 1} ^ {m} \frac {\sin k}{k ^ {p}} - \sum_ {k = 1} ^ {n} \frac {\sin k}{k ^ {p}} \right| = \left| \sum_ {k = n + 1} ^ {m} \frac {\sin k}{k ^ {p}} \right| \leqslant \sum_ {k = n + 1} ^ {m} \frac {1}{k ^ {p}} <   \varepsilon .
$$

于是, 由 Cauchy 收敛准则得到  $\sum_{n=1}^{\infty}\frac{\sin n}{n^{p}}$  收敛.

例 3.3.7 证明: 调和级数  $\sum_{n=1}^{\infty}\frac{1}{n}$  发散.

证明 证法1 取 $\varepsilon_0 = \frac{1}{2}$, 则对任何 $N \geqslant 1$, 取 $m = 2n = 2N$, 我们有

$$
\Big | \sum_ {k = 1} ^ {m} \frac {1}{k} - \sum_ {k = 1} ^ {n} \frac {1}{k} \Big | = \sum_ {k = n + 1} ^ {m} \frac {1}{k} \geqslant \frac {m - n}{m} = \varepsilon_ {0}.
$$

由 Cauchy 收敛准则,  $\sum_{n=1}^{\infty}\frac{1}{n}$  发散.

证法 2 由 (3.3.6) 式,

$$
\sum_ {k = 1} ^ {n} \frac {1}{k} \geqslant \sum_ {k = 1} ^ {n} \ln \left(1 + \frac {1}{k}\right) = \ln (n + 1).
$$

因此, $\sum_{n=1}^{\infty}\frac{1}{n}=+\infty$ ,从而级数发散.

□

---

3.3 实数系基本定理

73

## 3.3.7 有限覆盖定理

最后一个基本定理是 Heine-Borel $^{①}$  有限覆盖定理, 该定理在后继的分析学科中非常重要. 在数学分析课程中, 时常可帮助我们在观察问题时看到问题的本质. 对于  $E \subseteq R$ , 称集族 F 是 E 的一个开覆盖, 是指 F 中的元均为 R 中的开集, 且  $E \subseteq \bigcup_{V \in F} V$ .

定理 3.3.13 R 中有界闭集的任何开覆盖均有有限子覆盖.

证明 证法1 我们用闭集套定理和反证法来证明. 由于 $E$ 有界, 存在有界区间 $[a_1, b_1]$ 使得 $E \subseteq [a_1, b_1]$.

若定理结论不真，则 $E = E \cap [a_1, b_1]$ 不能被 $\mathcal{F}$ 中有限个元素覆盖，简称 $E \cap [a_1, b_1]$ 不能被有限覆盖。将区间 $[a_1, b_1]$ 平分。若 $\left[a_1, \frac{a_1 + b_1}{2}\right] \cap E$ 不能被有限覆盖，令 $[a_2, b_2] = \left[a_1, \frac{a_1 + b_1}{2}\right]$。否则，$\left[\frac{a_1 + b_1}{2}, b_1\right] \cap E$ 必然不能被有限覆盖，此时，令 $[a_2, b_2] = \left[\frac{a_1 + b_1}{2}, b_1\right]$。

以此类推, 可以找到一列闭区间  $\{[a_{n}, b_{n}]\}$  满足如下性质: 对任何  $n \geqslant 1, [a_{n+1}, b_{n+1}] \subseteq [a_{n}, b_{n}], b_{n} - a_{n} = \frac{b_{1} - a_{1}}{2^{n-1}}$ , 且  $[a_{n}, b_{n}] \cap E$  不能被有限覆盖.

由闭集套定理, $\{[a_n, b_n] \cap E\}$ 有唯一的公共点 $\xi$.

由于 $\mathcal{F}$ 覆盖 $E$, 因此, 有 $V \in \mathcal{F}$ 使得 $\xi \in V$. 而由 $V$ 为开集可得存在 $\delta > 0$, 使得 $(\xi - \delta, \xi + \delta) \subseteq V$.

另一方面, 存在 $m \geqslant 1$ 使得 $b_{m} - a_{m} < \delta$. 因此, $\xi - \delta \leqslant b_{m} - \delta < a_{m}$. 同理 $b_{m} < \xi + \delta$. 于是, $[a_{m}, b_{m}] \cap E \subseteq [a_{m}, b_{m}] \subset (\xi - \delta, \xi + \delta) \subseteq V$, 即 $[a_{m}, b_{m}] \cap E$ 可以被 $\mathcal{F}$ 中一个元素 $V$ 覆盖. 得到矛盾.

因此, 一定可以找到 $\mathcal{F}$ 中有限个元覆盖 $E$.

证法2 以下用致密性定理证明. 由定理条件可得, 对于任何 $x \in E$, 令

$$
r (x) := \sup \left\{r \in (0, 1)   \big |   \exists V \in {\mathcal {F}},   \text {使得}   (x - r, x + r) \subseteq V \right\}.
$$

则 $\forall x\in E,$ 有 $r(x) > 0.$ 任取 $x_{1}\in E,$ 有 $V_{1}\in \mathcal{F}$ 使得 $\left(x_1 - \frac{r(x_1)}{2},x_1 + \frac{r(x_1)}{2}\right)\subseteq V_1.$

现设对于某个 $n \geqslant 1$, 已经取到 $x_1, x_2, \dots, x_n \in E$ 以及 $V_1, V_2, \dots, V_n \in \mathcal{F}$. 若 $E \subset \bigcup_{k=1}^{n} V_k$, 则定理得证. 否则, 可取到 $x_{n+1} \in E \setminus \bigcup_{k=1}^{n} V_k$, 以及 $V_{n+1} \in \mathcal{F}$ 使得 $\left(x_{n+1} - \frac{r(x_{n+1})}{2}, x_{n+1} + \frac{r(x_{n+1})}{2}\right) \subset V_{n+1}$.

我们断言以上过程必在有限步内结束. 否则, 因 $E$ 有界, $E$ 中的数列 $\{x_{n}\}$ 有界. 从而它有子列 $\{x_{k_n}\}$ 收敛到某个 $\xi$.

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">① Borel, Félix Édouard Justin Émile, 1871 年 1 月 7 日—1956 年 2 月 3 日, 法国数学家、政治家.</span></small>

---

74

第三章 序列极限

由 $\{x_{n}\}$ 的构造方法, 对任何 $n \geqslant 1$, 有 $x_{k_{n+1}} \notin V_{k_{n}+1}$. 特别地, $r(x_{k_n}) \leqslant 2|x_{k_{n+1}} - x_{k_n}|$. 因此, $\lim_{n \to +\infty} r(x_{k_n}) = 0$.

另一方面, 由于 $E$ 为闭集, 因此 $\xi \in E$. 从而存在 $U \in \mathcal{F}$ 使得 $\left(\xi - \frac{r(\xi)}{2}, \xi + \frac{r(\xi)}{2}\right) \subset U$. 对于充分大的 $n$, 有 $|x_{k_n} - \xi| < \frac{r(\xi)}{2}$, 进而由

$$
\left(x _ {k _ {n}} - \left(\frac {r (\xi)}{2} - | x _ {k _ {n}} - \xi |\right), x _ {k _ {n}} + \left(\frac {r (\xi)}{2} - | x _ {k _ {n}} - \xi |\right)\right) \subset \left(\xi - \frac {r (\xi)}{2}, \xi + \frac {r (\xi)}{2}\right) \subset U,
$$

可得 $r(x_{k_n}) \geqslant \frac{r(\xi)}{2} - |x_{k_n} - \xi|$. 这样, 又有 $\lim_{n \to +\infty} r(x_{k_n}) \geqslant \frac{r(\xi)}{2} > 0$. 得到矛盾.

总之， $E$ 可以被 $\mathcal{F}$ 的有限子集族覆盖.

由有限覆盖定理易得如下的Lebesgue覆盖引理. 我们称 $\delta > 0$ 为 $E$ 的覆盖 $\mathcal{F}$ 的Lebesgue数, 是指它满足如下条件: 对 $E$ 的任何直径小于 $\delta$ 的子集 $A$, 总有 $\mathcal{F}$ 中的元素 $F$ 使得 $A \subseteq F$.

定理 3.3.14 设 F 是 R 中有界闭集 E 的开覆盖, 则 F 有 Lebesgue 数.

证明 考虑集族

$$
\mathcal {F} _ {0} := \left\{(x - r, x + r)   \big |   \exists V \in \mathcal {F}, \text {使得} (x - 2 r, x + 2 r) \subseteq V \right\},
$$

则 $\mathcal{F}_0$ 是 $E$ 的开覆盖. 从而由有限覆盖定理, 有 $(x_k - r_k, x_k + r_k) \in \mathcal{F}_0 (1 \leqslant k \leqslant n)$, 使得 $E \subset \bigcup_{k=1}^{n} (x_k - r_k, x_k + r_k)$. 令 $\delta = \min_{1 \leqslant k \leqslant n} r_k$. 则对于 $E$ 的直径小于 $\delta$ 的非空子集 $A$, 任取一元素 $x_0 \in A$, 必有某个 $k$ 满足 $1 \leqslant k \leqslant n$, 使得 $x_0 \in (x_k - r_k, x_k + r_k)$. 另一方面, 有 $V_k \in \mathcal{F}$ 使得 $(x_k - 2r_k, x_k + 2r_k) \subseteq V_k$. 从而

$$
A \subseteq [ x _ {0} - \delta , x _ {0} + \delta ] \subseteq (x _ {k} - r _ {k} - \delta , x _ {k} + r _ {k} + \delta) \subseteq (x _ {k} - 2 r _ {k}, x _ {k} + 2 r _ {k}) \subseteq V _ {k}.
$$

即  $\delta$  为 F 的一个 Lebesgue 数.

## 3.3.8 基本定理的新舞台

在 $\mathbb{R}$ 中, 各基本定理是等价的. 承认其中任一个定理, 可推出其他任一个定理. 读者可以尝试证明它们的等价性. 比如可以按下述次序证明这种等价性:

下确界存在定理 $\xleftrightarrow{\text{显然}}$ 上确界存在定理 $\xrightarrow{\text{已证}}$ 单调收敛定理 $\xrightarrow{\text{已证}}$ 闭区间套定理 $\xrightarrow{\text{已证}}$ 有限覆盖定理 $\Rightarrow$ 聚点原则 $\xrightarrow{\text{已证}}$ 致密性定理 $\xrightarrow{\text{已证}}$ Cauchy收敛准则 $\Rightarrow$ 闭区间套定理 $\Rightarrow$ 上确界存在定理.

除了确界存在定理与单调收敛定理, 余下五个基本定理都可以推广到 $\mathbb{R}^n$ 中. 进一步, 它们还可以推广到更一般的空间中去.

通常, 我们把具有一定结构的非空集合 $X$ 称为空间. 各种各样的空间为基本定理提供了广阔的舞台.

---

3.3 实数系基本定理

75

## 1. 度量空间与完备性

若  $\rho:X\times X\to[0,+\infty)$  满足如下条件:

(1) 非负性  $\rho(x,y)\geqslant0,$  且等号成立当且仅当 x=y;
(2) 对称性  $\rho(x,y)=\rho(y,x);$
(3) 三角不等式 $\rho(x, z) \leqslant \rho(x, y) + \rho(y, z)$,

则称  $(X,\rho)$  (或 X) 为度量空间或距离空间, 称  $\rho(x,y)$  为 x 与 y 间的距离.

在度量空间中, 可以引入收敛性. 称 $X$ 中的点列 $\{x_{n}\}$ 收敛于 $\xi \in X$, 是指 $\lim_{n\to +\infty} \rho(x_{n}, \xi) = 0$.

类似地, 可以在度量空间中引入 Cauchy 列. 称 X 中的  $\{x_{n}\}$  为 Cauchy 列 (基本列), 是指  $\lim_{N\to+\infty}\sup_{m,n\geqslant N}\rho(x_{m},x_{n})=0$ .

称 $(X, \rho)$ 是完备的度量空间, 是指 $X$ 中的 Cauchy 列都收敛. 即若 $\{x_{n}\}$ 是 Cauchy 列, 则必有 $\xi \in X$ 使得 $\{x_{n}\}$ 收敛到 $\xi$.

易见, $\mathbb{R}$ 及其闭子集 (在通常的度量之下) 是完备度量空间.

## 2. 拓扑空间与紧性

如果  $T \subseteq 2^{X}$  满足如下条件:

(1)  $\varnothing, X \in T;$
(2) $\mathcal{T}$ 的任何子集的并集属于 $\mathcal{T}$, 即若 $\mathcal{F} \subseteq \mathcal{T}$, 则 $\bigcup_{F \in \mathcal{F}} F \in \mathcal{T}$;

(3) T 的任何有限个元素的交集属于 T, 即若  $V_{1}, V_{2}, \cdots, V_{n} \in T$ , 则  $\bigcap_{k=1}^{n} V_{k} \in T$ ,

则称 $(X, \mathcal{T})$ (简记为 $X$) 为一个拓扑空间, $\mathcal{T}$ 中的元素称为 $X$ 的开集. 在拓扑空间中, 如果 $X \setminus F$ 是开集, 则称 $F$ 为闭集. 同样, 对于任何 $E \subseteq X$, 可以定义它的闭包 $\overline{E}$.

若 X 的任何开覆盖都有有限子覆盖, 则称 X 为紧空间. 若  $A \subseteq X$  的任何开覆盖都有有限子覆盖, 则称 A 为紧集, 又称紧致集. 若  $\overline{F} \subseteq E$  且  $\overline{F}$  为紧集, 则称 F 紧包含于 E, 记作  $F \subset \subset E$ .

定理3.3.15 $E$ 是 $\mathbb{R}$ 中的紧集当且仅当 $E$ 是有界闭集.

证明 有限覆盖定理表明, $\mathbb{R}$ 中有界闭集是紧集. 我们只要证明, 若 $E$ 是紧集, 则它一定是有界闭集. 下设 $E$ 为紧集.

为此, 注意到  $\{(-n,n)\}$  是 E 的开覆盖. 因此, 它有有限子覆盖. 即有  $n_{1}, n_{2}, \cdots, n_{m} \in N_{+}$  使得  $E \subseteq \bigcup_{k=1}^{m} (-n_{k}, n_{k}) = (-N, N)$ , 其中  $N = \max_{1 \leqslant k \leqslant m} n_{k}$ . 因此, E 有界.

现设  $\xi\not\in E,$  则  $\left\{\left(-\infty,\xi-\frac{1}{n}\right)\cup\left(\xi+\frac{1}{n},+\infty\right)\right\}$  是 E 的开覆盖. 于是, 它有有限子覆盖, 即有  $n_{1},n_{2},\cdots,n_{m}\in N_{+}$  使得  $E\subseteq\bigcup_{k=1}^{m}\left(\left(-\infty,\xi-\frac{1}{n_{k}}\right)\cup\left(\xi+\frac{1}{n_{k}},+\infty\right)\right)=\mathbb{R}\setminus[\xi-\delta,\xi+\delta]$ , 其中  $\delta=\min_{1\leqslant k\leqslant m}\frac{1}{n_{k}}>0.$  因此,  $\xi\not\in E'$ , 这就是说 E 是闭集. □

## 3. 列紧性

在拓扑空间 $X$ 中可以定义收敛性. 称 $X$ 中的点列 $\{x_{n}\}$ 收敛于 $\xi \in X$, 是指对 $\xi$ 的任何开集 $V$, 有 $N \geqslant 1$ 使得当 $n \geqslant N$ 时, 有 $x_{n} \in V$.

---

76

第三章 序列极限

若 $(X,\rho)$ 是度量空间, 定义相应的 $\mathcal{T}$ (称为由度量 $\rho$ 诱导的拓扑) 如下: $V\in \mathcal{T}$ 当且仅当对任何 $x_0\in V$, 存在 $\delta >0$ 使得

$$
\{x \in X | \rho (x, x _ {0}) <   \delta \} \subseteq V.
$$

易见在距离空间中的收敛性与诱导的拓扑空间中的收敛性是一致的. 度量空间中收敛点列的极限是唯一的, 而在一般的拓扑空间中不一定.

若 $X$ 中的点列均有收敛子列, 则称 $X$ 为列紧空间. 若 $X$ 的子集 $A$ 中的点列, 均有收敛于 $A$ 中点的子列, 则称 $A$ 为列紧集.

在 $\mathbb{R}$ 中，一个集合为紧集或列紧集，均当且仅当它为有界闭集.

## 习题3.3

1. 设 $E \subseteq \mathbb{R}$, 称某性质 $P$ 在 $E$ 上局部成立, 是指对任何 $x \in E$, 存在 $x$ 的一个邻域 $V$, 使得 $P$ 在 $E \cap V$ 上成立. 换言之, 对任何 $x \in E$, 存在 $\delta > 0$ 使得 $P$ 在 $(x - \delta, x + \delta) \cap E$ 上成立.

(1) 设 $-\infty \leqslant a < b \leqslant +\infty$. 证明 $f$ 在 $(a, b)$ 内局部有界当且仅当对任何有界闭集 $E \subseteq (a, b)$, $f$ 在 $E$ 上有界.

(2) 设 $-\infty < a < b \leqslant +\infty$. 证明 $f$ 在 $[a, b)$ 上局部有界当且仅当对任何 $c \in (a, b)$, $f$ 在 $[a, c]$ 上有界.

2. 设 $E \subset \mathbb{R}$ 为非空的有界闭集. 证明: $E$ 有最大、最小值, 即 $\sup E \in E$, $\inf E \in E$.

3. 设 E 为 R 中的无理点全体. 证明  $\overline{E} = R$ .

4. 设 $x_0 \in (0,2)$, $x_{n+1} = x_n(2 - x_n) (n \geqslant 0)$. 证明: $\lim_{n \to +\infty} x_n = 1$.

由此, 对于 $c > 0$, 任取 $y_0 > 0$ 满足 $cy_0 < 1$. 令 $y_{n+1} = y_n(2 - cy_n) (n \geqslant 0)$, 则 $\lim_{n \to \infty} y_n = \frac{1}{c}$. 这一事实让我们有可能利用乘法来计算倒数的近似值.

5. 设 $a_0, b_0 > 0$, $a_{n+1} = \frac{a_n + b_n}{2}$, $b_{n+1} = \frac{2a_nb_n}{a_nb_n}$. 证明: $\{a_n\}$ 和 $\{b_n\}$ 均收敛且极限相同.

6. 设  $c \geqslant -3$ ,

$$
x _ {1} = \frac {c}{2}, \qquad x _ {n + 1} = \frac {c}{2} + \frac {x _ {n} ^ {2}}{2}, \qquad n = 1, 2, 3, \dots .
$$

问  $\{x_{n}\}$  何时收敛, 并求极限.

7. 梳理或证明以下结果, 并尝试对这些结论有一个直观的理解:

(1) 收敛数列的子列收敛到同一极限;
(2) 如果一个数列有两个子列收敛到不同极限, 则该数列发散;
(3) 如果有界数列的收敛子列均收敛到同一个极限, 则该数列收敛;

---

3.3 实数系基本定理

77

(4) 有界数列 $\{a_{n}\}$ 不收敛到 $A$ 当且仅当存在一个收敛到 $B \neq A$ 的子列;
(5)  $\bar{x}$  为 E 的聚点当且仅当存在 E 中两两不同的点列  $\{x_{n}\}$  使得  $x_{n} \rightarrow \bar{x}$ ;
(6)  $\bar{x}$  为 E 的聚点当且仅当存在  $\{x_{n}\} \subseteq E \setminus \{\bar{x}\}$  使得  $x_{n} \to \bar{x}$ .

8. 设 $E \subseteq \mathbb{R}$. 证明存在至多可列集 $F \subseteq E$ 使得 $F$ 在 $E$ 中稠密.

9. 证明: 闭区间 $[a, b]$ 不能表示为两个不相交的非空闭集的并.

10. 证明: $\mathbb{R}$ 中既开又闭的集只有空集和 $\mathbb{R}$.

11. 设 $\{a_{k_n}\}$ 与 $\{a_{m_n}\}$ 是 $\{a_n\}$ 的两个有相同极限的收敛子列, $\{k_n | n \geqslant 1\} \cup \{m_n | n \geqslant 1\} = \mathbb{N}_+$. 证明: $\{a_n\}$ 收敛.

12. 设 E 为 R 中闭集, 证明存在集合 F 使得 F 的导集为 E.

13. 下表穷举了集合的内部、导集、边界和闭包的内部、导集、边界和闭包. 请证明每一格中的结果, 对于非等式的情形, 举出等式成立以及不成立的例子. 进一步, 思考能否得出其他的关系式.

| 集合 | 内部 | 导集 | 边界 | 闭包 |
| --- | --- | --- | --- | --- |
| $E^{\circ}$ | $(E^{\circ})^{\circ}=E^{\circ}$ | $(E^{\circ})'=\overline{E^{\circ}}$ | $\partial(E^{\circ})\subseteq\partial E\cap E'$ | $\overline{E^{\circ}}\subseteq E'$ |
| $E'$ | $(E')^{\circ}=\overline{E}^{\circ}\supseteq E^{\circ}$ | $(E')'\subseteq E'$ | $\partial(E')\subseteq\partial E\cap E'$ | $\overline{E'}=E'$ |
| $\partial E$ | $(\partial E)^{\circ}=\left(\overline{E}\cap\overline{\mathscr{C}E}\right)^{\circ}$ | $(\partial E)'\subseteq\partial E\cap E'$ | $\partial(\partial E)\subseteq\partial E$ | $\overline{\partial E}=\partial E$ |
| $\overline{E}$ | $(\overline{E})^{\circ}\supseteq E^{\circ}$ | $(\overline{E})'=E'$ | $\partial(\overline{E})\subseteq\partial E$ | $(\overline{E})=\overline{E}$ |

14. 试构造 $\mathbb{R}$ 中一列非空集 $\{E_k\}$ 使得 $E_{k + 1} = E_k' \subset E_k (k \geqslant 1)$.

15. 设 $E \subseteq \mathbb{R}$, 用 $S_{E}$ 表示 $E$ 的孤立点全体, $\mathcal{O}_{E}$ 为 $E$ 的外点全体①. 证明:

(1) 内点为不是边界点的聚点, 即  $E^{\circ} = E' \setminus \partial E;$
(2) 外点为既非聚点又非孤立点的点, 即  $\mathcal{O}_{E} = \mathscr{C}(E' \cup \mathcal{S}_{E})$ ;
(3) 边界点为孤立点, 或不是内点的聚点, 即  $\partial E = S_{E} \cup (E' \setminus E^{\circ})$ ;
(4) 聚点为内点, 或不是孤立点的边界点, 即  $E' = E^{\circ} \cup (\partial E \setminus S_{E})$ ;
(5) 孤立点为不是聚点的边界点, 即  $S_{E} = \partial E \setminus E'$ .

16. 设 $x_0 \in (0,1)$, $x_{n+1} = x_n(1 - x_n) (n \geqslant 0)$. 不使用 Stolz 公式, 按以下过程证明:

(1) $\lim_{n\to +\infty}x_n = 0;$
(2) 对任何  $n \geqslant 1$ ，成立  $(n + 1)x_{n} < 1$ ;
(3) 从某一项开始,  $\{nx_{n}\}$  单调有界;
(4) $\lim_{n\to +\infty}nx_n = 1.$

17. 在习题 6 中, 若 c < -3 会如何?

18. 设 $[a, b]$ 上函数列 $\{f_n\}$ 一致有界, 即存在常数 $M > 0$, 使得

$$
| f _ {n} (x) | \leqslant M, \quad \forall n \geqslant 1, x \in [ a, b ].
$$

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">① 这两个不是通用记号.</span></small>

---

78

第三章 序列极限

证明存在子函数列 $\{f_{n_k}\}$ 使得在 $[a,b]$ 的所有有理点收敛.

19. 设整数  $m \geqslant 1$ ，证明: $\lim_{n \to +\infty} \sqrt{m + \sqrt{m + 1 + \sqrt{m + 2 + \cdots + \sqrt{m + n}}}}$  存在，并记该极限为  $a_{m}$ 。进一步，计算  $\lim_{m \to +\infty} (a_{m} - \sqrt{m})$ 。

20. 证明: $\lim_{n\to +\infty}\sqrt{1 + 2\sqrt{1 + 3\sqrt{1 + 4\sqrt{1 + \cdots + n\sqrt{1 + (n + 1)}}}}} = 3.$

21. 推广习题 20.

22. 设 $x_0 \geqslant 0, x_{n+1} = \sqrt{2 + x_n} (n \geqslant 0)$. 问: $\lim_{n \to +\infty} 4^n(2 - x_n)$ 是否存在? 该极限存在时, 能否得到极限的值?

23. 一般地, 对于所求过的极限可考虑进一步的结果, 例如, 若已经得到 $\lim_{n\to +\infty}x_n = A$, 试试能否找到一个与初值 $x_0$ 无关的无穷大量 $\{y_n\}$ 使得 $\lim_{n\to +\infty}y_n(x_n - A)$ 为一个非零实数.

24. 固定 $r \in (0,4)$. 任取 $x_0 \in (0,1)$. 令 $x_{n+1} = rx_n(1 - x_n) (n \geqslant 0)$. 问: 当 $r$ 取什么值时, 你可以证明对于任何 $x_0 \in (0,1)$, 按上述方式定义的数列 $\{x_n\}$ 一定收敛.

试编写一计算机程序, 感受对于不同的 r, 当 n 足够大时  $x_{n}$  的收敛情况.

25. 设 $\{x_{n}\}$ 是在 $[0,1]$ 中稠密的点列, 任取 $\alpha \in \left(0, \frac{1}{2}\right)$, $E := [0,1] \setminus \bigcup_{n=1}^{\infty} \left(x_{n} - \frac{\alpha}{2^{n}}, x_{n} + \frac{\alpha}{2^{n}}\right)$. 证明 $E$ 为非空的疏朗集.

26. 考虑

$$
X := \left\{\{x _ {n} \} _ {n = 1} ^ {\infty} \Big | \sum_ {n = 1} ^ {\infty} | x _ {n} | ^ {2} <   + \infty \right\},
$$

在其上定义

$$
\| \{x _ {n} \} \| := \Big (\sum_ {n = 1} ^ {\infty} | x _ {n} | ^ {2} \Big) ^ {\frac {1}{2}}, \qquad d (\{x _ {n} \}, \{y _ {n} \}) := \| \{x _ {n} - y _ {n} \} \|.
$$

证明 $d$ 是 $X$ 上的距离. 并以此距离定义收敛性、开集、闭集等. 证明:

(1) 在 X 上, Cauchy 收敛准则成立.
(2) 在 X 上, 致密性定理不成立, 即有界点列不一定有收敛子列.
(3) 设 $\{\pmb{x}_k\}$ 是 $X$ 中点列, 它的每一个分量都有界, 即记 $\pmb{x}_k = \{x_{k,n}\}_{n=1}^{\infty}$ 时, 对任何 $n \geqslant 1$, $\{x_{k,n}\}_{k=1}^{\infty}$ 是有界集. 证明: 存在 $\{\pmb{x}_k\}$ 的子列使得其每一个分量都收敛.
(4) 在 X 上, 有限覆盖定理不成立.
(5) 在 $X$ 上, 闭集套定理成立. 即如果 $\{E_n\}$ 是 $X$ 中的一列单调下降且直径趋于零的闭集列, 则 $\bigcap_{n=1}^{\infty} E_n$ 为单点集.

---

3.4 上、下极限

79

(6) X 中存在一列有界非空闭集  $E_{1} \supseteq E_{2} \supseteq E_{3} \supseteq \cdots$  使得  $\bigcap_{n=1}^{\infty} E_{n}$  为空集.

27. (1) 在 $[- \infty, +\infty]$ 中①, 若 $\lim_{n \to +\infty} a_n = +\infty$ 或 $\lim_{n \to +\infty} a_n = -\infty$, 我们就分别称 $\{a_n\}$ 收敛到 $+\infty$ 或 $-\infty$. 试重新考察习题 7.

(2) 对于 $E \subseteq [-\infty, +\infty]$, 若存在 $a \in \mathbb{R}$ 使得 $(a, +\infty] \subseteq E ([-\infty, a) \subseteq E)$, 则称 $+\infty (-\infty)$ 为 $E$ 的内点. 若 $U \subseteq [-\infty, +\infty]$ 的所有点都是其内点, 则称 $U$ 为 $[- \infty, +\infty]$ 的开集. 考虑在 $[- \infty, +\infty]$ 中, 哪些集合是紧集, 即 $[- \infty, +\infty]$ 中满足任何开覆盖都有有限子覆盖的集合.

28. 设 $E \subseteq \mathbb{R}$. 则 $E$ 满足什么条件时, 成立: 对于 $E$ 的任何闭覆盖, 均有有限子覆盖.

29. 设 $U$ 为 $\mathbb{R}$ 中开集. 证明:

(1) 若  $x_{0} \in U$ ，则存在唯一的开区间  $(\alpha, \beta)$  ——这样的区间称为 U 的构成区间，满足:

(i) $x_0 \in (\alpha, \beta) \subseteq U$; (ii) 若 $x_0 \in (a, b) \subseteq U$, 则 $(a, b) \subseteq (\alpha, \beta)$.

(2) U 可以表示为至多可列个两两不交的构成区间的并.

30. 闭区间 $[a, b]$ 不能表示为至少两个但至多可列个两两不交的非空闭集的并.

31. $\mathbb{R}$ 不能表示成一列无处稠密集的并.

32. 设 $\{V_k\}$ 是一列在 $\mathbb{R}$ 中稠密的开集, 证明: $\bigcap_{k} V_k$ 在 $\mathbb{R}$ 中稠密.

33. 在度量空间的定义中, 由 (2)\~(3) 可以得到

(3') 对任何 $x, y, z \in X$, 成立 $\rho(x, z) \leqslant \rho(y, x) + \rho(y, z)$.

证明: (1)\~(3) 与 (1), (3') 等价.

## 3.4 上、下极限

在讨论问题之初不能确定某些极限是否存在, 时常带来很大的麻烦. 引入上、下极限在技术上可以减少这种麻烦. 而通过研究弱意义下的极限来研究极限, 则提供了一种重要的数学思想.

设  $\{a_{n}\}$  是广义实数系中的点列, 考虑

$$
A _ {n} := \sup _ {k \geqslant n} a _ {k}, \quad B _ {n} := \inf _ {k \geqslant n} a _ {k}.
$$

则 $\{A_{n}\}$ 单调减少, $\{B_n\}$ 单调增加. 因此, 它们在广义实数系中有极限. 我们给出如下

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">① 以下说法在 R 中不适用.</span></small>

---

80

第三章 序列极限

定义.

定义 3.4.1 对于广义实数系中的点列  $\{a_{n}\}$ ，称

$$
\varlimsup_ {n \to + \infty} a _ {n} := \lim _ {n \to + \infty} \sup _ {k \geqslant n} a _ {k} \quad \text {和} \quad \varliminf_ {n \to + \infty} a _ {n} := \lim _ {n \to + \infty} \inf _ {k \geqslant n} a _ {k}
$$

为  $\{a_{n}\}$  的上极限和下极限.

由夹逼准则立即可得如下定理, 它使得通过上、下极限来研究极限成为可能.

定理3.4.1 对于广义实数列 $\{a_{n}\}$ ， $\lim_{n\to +\infty}a_n = \ell$ 当且仅当

$$
\varlimsup_ {n \to + \infty} a _ {n} = \varliminf_ {n \to + \infty} a _ {n} = \ell , \tag {3.4.1}
$$

其中  $\ell\in[-\infty,+\infty]$ .

证明 (充分性) 若 (3.4.1) 式成立, 则由

$$
\inf _ {k \geqslant n} a _ {k} \leqslant a _ {n} \leqslant \sup _ {k \geqslant n} a _ {k}
$$

和夹逼准则即得  $\lim_{n\to+\infty}a_{n}=\ell.$

(必要性) 若 $\lim_{n\to +\infty}a_n = \ell$ ，则当 $\ell \in (-\infty , + \infty)$ 时， $\forall \varepsilon >0,$ 存在 $N > 0$ 使得

$$
\ell - \varepsilon \leqslant a _ {n} \leqslant \ell + \varepsilon , \quad \forall n \geqslant N.
$$

于是

$$
\ell - \varepsilon \leqslant \inf _ {k \geqslant n} a _ {k} \leqslant a _ {n} \leqslant \sup _ {k \geqslant n} a _ {k} \leqslant \ell + \varepsilon , \quad \forall n \geqslant N.
$$

这就表明 $\lim_{n\to +\infty}a_n = \varlimsup_{n\to +\infty}a_n = \ell.$ 即(3.4.1)式成立.

当  $\ell = +\infty$  或  $\ell = -\infty$  时, 类似可证 (3.4.1) 式成立.

除了定理 3.4.1, 上、下极限具有如下自然的性质.

定理 3.4.2 对于广义实数列 $\{a_{n}\}$, 有

(1) $\varlimsup_{n\to +\infty}a_n\geqslant \varliminf_{n\to +\infty}a_n;$
(2) $\lim_{n\to +\infty}a_n = \inf_n\sup_{k\geqslant n}a_k,\quad \varliminf_{n\to +\infty}a_n = \sup_n\inf_{k\geqslant n}a_k;$

(3) 设  $\{a_{n_{k}}\}$  为  $\{a_{n}\}$  的一个子列, 则

$$
\varlimsup_ {k \to + \infty} a _ {n _ {k}} \leqslant \varlimsup_ {n \to + \infty} a _ {n}, \quad \varliminf_ {k \to + \infty} a _ {n _ {k}} \geqslant \varliminf_ {n \to + \infty} a _ {n};
$$

(4) 存在  $\{a_{n}\}$  的子列  $\{a_{n_{k}}\}$  和子列  $\{a_{m_{k}}\}$  使得 $^{①}$

$$
\varlimsup_ {n \to + \infty} a _ {n} = \lim _ {k \to + \infty} a _ {n _ {k}}, \quad \varliminf_ {n \to + \infty} a _ {n} = \lim _ {k \to + \infty} a _ {m _ {k}}.
$$

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">① 本结果蕴涵致密性定理.</span></small>

---

3.4 上、下极限

81

定理 3.4.3 对于广义实数列 $\{a_{n}\}$ 和 $\{b_{n}\}$, 有

(1) 若  $a_{n} \leqslant b_{n}$  ( $n = 1, 2, \cdots$ ), 则

$$
\varliminf_ {n \to + \infty} a _ {n} \leqslant \varliminf_ {n \to + \infty} b _ {n}, \quad \varlimsup_ {n \to + \infty} a _ {n} \leqslant \varlimsup_ {n \to + \infty} b _ {n}.
$$

(2) $\lim_{n\to +\infty}(-a_n) = -\lim_{n\to +\infty}a_n.$

(3) 以下每一个不等式, 只要其两端在广义实数系中都有意义, 就一定成立:

$$
\begin{array}{l} \varliminf_ {n \to + \infty} a _ {n} + \varliminf_ {n \to + \infty} b _ {n} \leqslant \varliminf_ {n \to + \infty} (a _ {n} + b _ {n}) \\ \leqslant \varliminf_ {n \to + \infty} a _ {n} + \varlimsup_ {n \to + \infty} b _ {n} \leqslant \varlimsup_ {n \to + \infty} (a _ {n} + b _ {n}) \\ \leqslant \varlimsup_ {n \to + \infty} a _ {n} + \varlimsup_ {n \to + \infty} b _ {n}. \\ \end{array}
$$

(4) 若 $\lim_{n\to +\infty}a_n$ 存在, 则

$$
\begin{array}{l} \varliminf_ {n \to + \infty} (a _ {n} + b _ {n}) = \lim _ {n \to + \infty} a _ {n} + \varliminf_ {n \to + \infty} b _ {n}, \\ \varlimsup_ {n \to + \infty} (a _ {n} + b _ {n}) = \lim _ {n \to + \infty} a _ {n} + \varlimsup_ {n \to + \infty} b _ {n}. \\ \end{array}
$$

(5) 若  $a_{n} > 0 (n = 1, 2, \cdots)$ ，规定  $\frac{1}{0} = +\infty$ ，则我们有

$$
\varlimsup_ {n \to + \infty} \frac {1}{a _ {n}} = \frac {1}{\varliminf_ {n \to + \infty} a _ {n}}.
$$

(6) 设  $a_{n} > 0, b_{n} > 0 (n = 1, 2, \cdots)$ ，则以下每一个不等式，只要其两端在广义实数系中都有意义，就一定成立:

$$
\begin{array}{l} \varliminf_ {n \to + \infty} a _ {n} \varliminf_ {n \to + \infty} b _ {n} \leqslant \varliminf_ {n \to + \infty} (a _ {n} b _ {n}) \leqslant \varliminf_ {n \to + \infty} a _ {n} \varlimsup_ {n \to + \infty} b _ {n} \\ \leqslant \varlimsup_ {n \to + \infty} (a _ {n} b _ {n}) \leqslant \varlimsup_ {n \to + \infty} a _ {n} \varliminf_ {n \to + \infty} b _ {n}. \\ \end{array}
$$

(7) 设  $a_{n} > 0 (n = 1, 2, \cdots)$ ，且  $\lim_{n \to +\infty} a_{n} = 0$ .

若  $\varliminf_{n\to+\infty}b_{n}$  不为  $\pm\infty$ ，则  $\varliminf_{n\to+\infty}(a_{n}b_{n})=0$ .

若 $\lim_{n\to +\infty}b_n$ 不为 $\pm \infty$ ，则 $\lim_{n\to +\infty}(a_nb_n) = 0.$

(8) 设 $\lim_{n\to +\infty}a_n = A\in (0, + \infty)$, 则

$$
\varliminf_ {n \to + \infty} (a _ {n} b _ {n}) = A \varliminf_ {n \to + \infty} b _ {n}, \quad \varlimsup_ {n \to + \infty} (a _ {n} b _ {n}) = A \varlimsup_ {n \to + \infty} b _ {n}.
$$

利用上、下极限, Stolz 公式可作如下推广.

---

82

第三章 序列极限

定理 3.4.4 设  $\{x_{n}\}$  和  $\{y_{n}\}$  是两个实数列,  $\{y_{n}\}$  严格单增, 且  $\lim_{n\to+\infty}y_{n}=+\infty$ . 则

$$
\varliminf_ {n \to + \infty} \frac {x _ {n + 1} - x _ {n}}{y _ {n + 1} - y _ {n}} \leqslant \varliminf_ {n \to + \infty} \frac {x _ {n}}{y _ {n}} \leqslant \varlimsup_ {n \to + \infty} \frac {x _ {n}}{y _ {n}} \leqslant \varlimsup_ {n \to + \infty} \frac {x _ {n + 1} - x _ {n}}{y _ {n + 1} - y _ {n}}. \tag {3.4.2}
$$

证明 对任何 $n > m \geqslant 1$, 我们有

$$
\inf _ {k \geqslant m} \frac {x _ {k + 1} - x _ {k}}{y _ {k + 1} - y _ {k}} \leqslant \frac {\sum_ {j = m} ^ {n - 1} (x _ {j + 1} - x _ {j})}{\sum_ {j = m} ^ {n - 1} (y _ {j + 1} - y _ {j})} \leqslant \sup _ {k \geqslant m} \frac {x _ {k + 1} - x _ {k}}{y _ {k + 1} - y _ {k}}.
$$

即

$$
\inf _ {k \geqslant m} \frac {x _ {k + 1} - x _ {k}}{y _ {k + 1} - y _ {k}} \leqslant \frac {x _ {n} - x _ {m}}{y _ {n} - y _ {m}} \leqslant \sup _ {k \geqslant m} \frac {x _ {k + 1} - x _ {k}}{y _ {k + 1} - y _ {k}}. \tag {3.4.3}
$$

在上式中固定 $m$ ，令 $n\to +\infty$ ，并注意到

$$
\begin{array}{l} \varliminf_ {n \to + \infty} \frac {x _ {n} - x _ {m}}{y _ {n} - y _ {m}} = \varliminf_ {n \to + \infty} \frac {x _ {n} - x _ {m}}{y _ {n}} = \varliminf_ {n \to + \infty} \frac {x _ {n}}{y _ {n}}, \\ \varlimsup_ {n \to + \infty} \frac {x _ {n} - x _ {m}}{y _ {n} - y _ {m}} = \varlimsup_ {n \to + \infty} \frac {x _ {n} - x _ {m}}{y _ {n}} = \varliminf_ {n \to + \infty} \frac {x _ {n}}{y _ {n}}, \\ \end{array}
$$

得到

$$
\inf _ {k \geqslant m} \frac {x _ {k + 1} - x _ {k}}{y _ {k + 1} - y _ {k}} \leqslant \varliminf_ {n \to + \infty} \frac {x _ {n}}{y _ {n}} \leqslant \varlimsup_ {n \to + \infty} \frac {x _ {n}}{y _ {n}} \leqslant \sup _ {k \geqslant m} \frac {x _ {k + 1} - x _ {k}}{y _ {k + 1} - y _ {k}}.
$$

再在上式中令 $m\to +\infty$ 得到

$$
\varliminf_ {n \to + \infty} \frac {x _ {n + 1} - x _ {n}}{y _ {n + 1} - y _ {n}} \leqslant \varliminf_ {n \to + \infty} \frac {x _ {n}}{y _ {n}} \leqslant \varlimsup_ {n \to + \infty} \frac {x _ {n}}{y _ {n}} \leqslant \varlimsup_ {n \to + \infty} \frac {x _ {n + 1} - x _ {n}}{y _ {n + 1} - y _ {n}}.
$$

从而定理成立.

定理 3.4.5 设  $\lim_{n\to+\infty}x_{n}=\lim_{n\to+\infty}y_{n}=0,\{y_{n}\}$  严格单减. 则

$$
\varliminf_ {n \to + \infty} \frac {x _ {n + 1} - x _ {n}}{y _ {n + 1} - y _ {n}} \leqslant \varliminf_ {n \to + \infty} \frac {x _ {n}}{y _ {n}} \leqslant \varlimsup_ {n \to + \infty} \frac {x _ {n}}{y _ {n}} \leqslant \varlimsup_ {n \to + \infty} \frac {x _ {n + 1} - x _ {n}}{y _ {n + 1} - y _ {n}}. \tag {3.4.4}
$$

证明 对任何 $m > n \geqslant 1$, 同样有

$$
\inf _ {k \geqslant n} \frac {x _ {k} - x _ {k + 1}}{y _ {k} - y _ {k + 1}} \leqslant \frac {x _ {n} - x _ {m}}{y _ {n} - y _ {m}} \leqslant \sup _ {k \geqslant n} \frac {x _ {k} - x _ {k + 1}}{y _ {k} - y _ {k + 1}}.
$$

在上式中固定 $n$, 令 $m \to +\infty$ 得到

$$
\inf _ {k \geqslant n} \frac {x _ {k} - x _ {k + 1}}{y _ {k} - y _ {k + 1}} \leqslant \frac {x _ {n}}{y _ {n}} \leqslant \sup _ {k \geqslant n} \frac {x _ {k} - x _ {k + 1}}{y _ {k} - y _ {k + 1}}.
$$

---

3.4 上、下极限

83

再令 $n\to +\infty$ 即得

$$
\varliminf_ {n \to + \infty} \frac {x _ {n} - x _ {n + 1}}{y _ {n} - y _ {n + 1}} \leqslant \varliminf_ {n \to + \infty} \frac {x _ {n}}{y _ {n}} \leqslant \varlimsup_ {n \to + \infty} \frac {x _ {n}}{y _ {n}} \leqslant \varlimsup_ {n \to + \infty} \frac {x _ {n} - x _ {n + 1}}{y _ {n} - y _ {n + 1}}.
$$

因此定理成立.

例3.4.1 设实数列 $\{a_{n}\}$ 满足 $a_{n} \neq -1$ 以及 $a_{n+1} = \frac{2}{a_{n} + 1} (n \geqslant 1)$. 试讨论 $\{a_{n}\}$ 的收敛性及其极限.

解 本例可以仿例 3.3.2 分情形加以讨论, 但相关讨论较为烦琐. 而采用上、下极限则会简捷许多.

记 $f(x) = \frac{2}{x + 1}, L = \varlimsup_{n\to +\infty}a_n, \ell = \varliminf_{n\to +\infty}a_n.$

由于 $a_{n} \neq -1$，而 $f(-3) = -1$，因此 $a_{n} \neq -3$。另一方面，$f(x) > 0$ 的解集为 $(-1, +\infty)$，而 $f(x) > -1$ 的解集，亦即 $f(f(x)) > 0$ 的解集为 $(- \infty, -3) \cup (-1, +\infty)$。

情形1 存在 $N \geqslant 1$ 使得 $a_{N} > -1$ 或者 $a_{N} < -3$.

此时, 可得当 $n \geqslant N + 2$ 时, 有 $a_{n} = f(f(a_{n - 2})) > 0$. 进一步, 归纳可得

$$
\frac {2}{3} \leqslant a _ {n} \leqslant 2, \quad \forall n \geqslant N + 4.
$$

从而 $\frac{2}{3} \leqslant \ell \leqslant L \leqslant 2$. 对递推式两边分别求上极限和下极限得到

$$
L = \frac {2}{\ell + 1}, \quad \ell = \frac {2}{L + 1}.
$$

由此可得 $L = \ell = 1$ .从而 $\lim_{n\to +\infty}a_n = 1.$

情形 2 对任何  $n \geqslant 1$  成立 -3 <  $a_{n} < -1$ . 此时  $-3 \leqslant \ell \leqslant L \leqslant -1$ . 对递推式两边分别求上极限和下极限得到

$$
L = \frac {2}{\ell + 1}, \quad \ell = \frac {2}{L + 1}, \tag {3.4.5}
$$

其中当 $L = -1$ 时, $\frac{2}{L + 1}$ 理解为 $-\infty$, 当 $\ell = -1$ 时, $\frac{2}{\ell + 1}$ 理解为 $-\infty$. 这事实上表明 $L < -1$. 这一点也可以从 $f(a_n) > -3$ 解得 $a_n < -\frac{5}{3}$ 或 $a_n > -1$ (舍去) 得到.

由(3.4.5)式和 $\ell \leqslant L\leqslant -1$ 解得 $L = \ell = -2$ 因此 $\lim_{n\to +\infty}a_n = -2.$

总之, 无论哪种情形, 都可得 $\{a_{n}\}$ 收敛. 且极限为 1 或 -2.

例3.4.2 设正数序列 $\{x_{n}\}$ 满足 $x_{m + n} \leqslant \frac{mx_m + nx_n}{m + n} (\forall m, n \geqslant 1)$. 求证: $\lim_{n \to +\infty} x_n$ 存在.

证明 归纳可证 $0 < x_{n} \leqslant x_{1} (\forall n \geqslant 1)$. 一般地, 有

$$
x _ {m n} \leqslant x _ {n}, \quad \forall m, n \geqslant 1.
$$

---

84

第三章 序列极限

先固定 $n \geqslant 1$, 对于 $m \geqslant n$, 作带余除法, 得到 $m = k_m n + j_m$, 其中 $k_m, j_m$ 为整数, $0 \leqslant j_m \leqslant n - 1$. 则 $\lim_{m \to +\infty} \frac{k_m n}{m} = 1$. 补充定义 $x_0 = 0$. 则

$$
x _ {m} \leqslant \frac {k _ {m} n x _ {k _ {m} n} + j _ {m} x _ {j _ {m}}}{m} \leqslant \frac {k _ {m} n x _ {n} + j _ {m} x _ {1}}{m}.
$$

上式中令 $m\to +\infty$ ，两端取上极限，得到

$$
\varlimsup_ {m \to + \infty} x _ {m} \leqslant x _ {n}, \quad \forall n \geqslant 1.
$$

再令 $n\to +\infty$ ，两端取下极限，得到

$$
\varlimsup_ {m \to + \infty} x _ {m} \leqslant \varliminf_ {n \to + \infty} x _ {n}.
$$

从而

$$
\varlimsup_ {n \to + \infty} x _ {n} = \varliminf_ {n \to + \infty} x _ {n} \leqslant x _ {1},
$$

即  $\lim_{n\to+\infty}x_{n}$  存在.

□

例3.4.3 设 $a_0, a_1 > 0, a_{n+2} = \frac{1}{a_n} + \frac{2}{a_{n+1}} (n \geqslant 0)$. 证明: $\lim_{n \to +\infty} a_n = \sqrt{3}$.

证明 令 $M = \max \left\{a_0, a_1, \frac{3}{a_0}, \frac{3}{a_1}\right\}$. 则归纳可证 $\frac{3}{M} \leqslant a_n \leqslant M (n \geqslant 0)$. 于是 $\{a_n\}$ 的上、下极限 $L, \ell$ 满足 $\frac{3}{M} \leqslant \ell \leqslant L \leqslant M$. 在递推公式两端取下极限可得 $\ell \geqslant \frac{3}{L}$. 而两端取上极限可得 $L \leqslant \frac{3}{\ell}$. 两者结合得到 $L\ell = 3$.

由上极限的性质, 存在 $\{a_{n}\}$ 的子列 $\{a_{k_n + 3}\}$ 使得 $\lim_{k\to +\infty}a_{k_n + 3} = L$. 进一步, 由致密性定理, $\{a_{k_n + 2}\}$ 有子列收敛. 不失一般性, 不妨设 $\{a_{k_n + 2}\}$ 本身收敛, 极限为 $x$. 类似地, 不妨设 $\{a_{k_n + 1}\}$ 和 $\{a_{k_n}\}$ 也收敛①, 极限依次为 $y, z$. 则 $\ell \leqslant x, y, z \leqslant L$. 由递推公式得

$$
L = \frac {2}{x} + \frac {1}{y} \leqslant \frac {2}{\ell} + \frac {1}{\ell} = L.
$$

因此, 必有 $x = y = \ell$. 类似地,

$$
\ell = x = \frac {2}{y} + \frac {1}{z} \geqslant \frac {2}{L} + \frac {1}{L} = \ell .
$$

所以 $y = z = L$. 特别地, 可得 $L = y = \ell$. 结合 $L\ell = 3$ 以及 $\ell \geqslant 0$ 得到 $L = \ell = \sqrt{3}$. 这就证明了 $\lim_{n \to +\infty} a_n = \sqrt{3}$. □

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">① 以上相当于证明或利用了 $\mathbb{R}^3$ 中有界列有收敛子列. 一般地, 对于任何正整数 $m, \mathbb{R}^m$ 中的有界列有收敛子列.</span></small>

---

3.4 上、下极限

85

## 习题3.4

1. 若  $x_{n}>0\ (n=1,2,\cdots)$ ，且  $\varlimsup_{n\to+\infty}x_{n}\cdot\varlimsup_{n\to+\infty}\frac{1}{x_{n}}=1$ 。证明序列  $\{x_{n}\}$  收敛。

2. 设  $\{x_{n}\}$  满足  $0 \leqslant x_{m+n} \leqslant x_{m} \cdot x_{n} (\forall m, n \geqslant 1)$ . 证明:  $\{\sqrt[n]{x_{n}}\}$  收敛.

3. 举例说明, 在习题 2 中,  $\{\sqrt[n]{x_{n}}\}$  可以没有单调性.

4. 设 $\{a_{n}\}$ 满足 $a_{m} + a_{n} - 1 \leqslant a_{m+n} \leqslant a_{m} + a_{n} + 1 (\forall m, n \geqslant 1)$. 求证:

(1) $\lim_{n\to +\infty}\frac{a_n}{n}$ 存在;

(2) 设  $\lim_{n\to+\infty}\frac{a_{n}}{n}=q$ ，则  $nq-1\leqslant a_{n}\leqslant nq+1\quad(n\geqslant1)$ .

5. 设  $r \in (0,1)$ ,  $x_{0} = 0$ ,  $x_{n+1} = r(1 - x_{n}^{2}) (n = 0, 1, 2, \cdots)$ . 试研究  $\{x_{n}\}$  的敛散性.

6. 设 0 < q < 1,  $\{a_{n}\}$ ,  $\{b_{n}\}$  满足  $a_{n} = b_{n} - qa_{n+1} (n = 1, 2, \cdots)$ ，且  $\{a_{n}\}$ ,  $\{b_{n}\}$  有界. 求证:  $\lim_{n \to +\infty} b_{n}$  存在的充要条件是  $\lim_{n \to +\infty} a_{n}$  存在.

7. 在习题 6 中当  $q \notin (0,1)$  时, 结论会怎样?

8. 设 $a_{n} \geqslant 0$ 满足 $a_{n+1} \leqslant a_{n} + \frac{1}{n^{2}}$. 证明: $\{a_{n}\}$ 收敛.

9. 利用上、下极限证明 $\mathbb{R}$ 中的 Cauchy 收敛准则.

10. 证明: 在例 3.4.1 中, 若 $\lim_{n\to +\infty}a_n = -2$, 则 $a_1 = -2$.

11. 推广习题 2 和习题 4.

12. 设  $\{x_{n}\}$  是正数列, 证明  $\lim_{n\to+\infty}n\left(\frac{1+x_{n+1}}{x_{n}}-1\right)\geqslant1$ .

13. 设 $f$ 是 $\mathbb{R}$ 上周期为 1 的实函数, 满足: $\forall x, y \in \mathbb{R}, x \neq y$, 有 $|f(x) - f(y)| < |x - y|$. 任取 $x_0 \in \mathbb{R}$, 定义 $x_{n+1} = f(x_n) (n \geqslant 0)$. 证明: $\{x_n\}$ 收敛, 且极限不依赖于 $x_0$ 的选择.
