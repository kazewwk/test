# 第四章 积分和数学期望

原始 PDF 第 106–147 页。

## 第四章

## 积分和数学期望

---

92

第四章 积分和数学期望

数学期望是概率论中最基本的概念之一. 某个随机变量的数学期望直观上是其取值按照相应概率的平均, 在数学上可以通过相对于其分布函数的斯蒂尔切斯 (Stieltjes) 积分定义. 本章首先对斯蒂尔切斯积分的定义和性质做简单的介绍, 在此基础上讨论随机变量的数学期望、方差和高阶矩、条件期望和预测等, 还介绍了非负整数值随机变量的母函数.

## 4.1 斯蒂尔切斯积分

本节讨论的斯蒂尔切斯积分是数学分析中的黎曼积分的直接推广. 由于这里的证明与黎曼积分的情况类似, 很多时候我们只给出结论, 而将证明留给读者.

## 4.1.1 有界区间上的积分

考虑有界区间 $[a, b] \subseteq \mathbb{R}$. 设 $G$ 是 $[a, b]$ 上的右连续不降函数. 根据定理 2.4.4 不难证明, 存在 $(\mathbb{R}, \mathcal{B})$ 上的有限测度 $\mu$ 使得

$$
\mu ([ a, x ]) = G (x) - G (a), \quad a \leqslant x \leqslant b.
$$

因此, 可以认为 $G$ 是 $\mu$ 的某个分布函数在 $[a, b]$ 上的限制.

定义 4.1.1 设 f 为区间  $[a, b]$  上的函数. 对整数  $k \geqslant 1$ , 取  $[a, b]$  的分割点  $a = x_{k,0} < x_{k,1} < \cdots < x_{k,n_{k}} = b$  满足

$$
\delta_ {k} := \max _ {1 \leqslant i \leqslant n _ {k}} (x _ {k, i} - x _ {k, i - 1}) \to 0, \quad k \to \infty ,
$$

并取 $t_{k,i}\in [x_{k,i - 1},x_{k,i}]$ .令

$$
\begin{array}{l} \sigma_ {k} (f, G; a, b) = \sum_ {i = 1} ^ {n _ {k}} f (t _ {k, i}) [ G (x _ {k, i}) - G (x _ {k, i - 1}) ] \\ = \sum_ {i = 1} ^ {n _ {k}} f (t _ {k, i}) \mu ((x _ {k, i - 1}, x _ {k, i} ]). \tag {4.1.1} \\ \end{array}
$$

若存在有限的极限 $\lim_{k\to \infty}\sigma_k(f,G;a,b)$ 且该极限与 $\{x_{k,i}\}$ 和 $\{t_{k,i}\}$ 的具体选取无关，则称 $f$ 在 $[a,b]$ 上相对于 $G$ 斯蒂尔切斯可积，简称 $G$ 可积.称该极限为 $f$ 在 $[a,b]$ 上相对于 $G$ 的斯蒂尔切斯积分，简称 $G$ 积分，并记作

$$
\int_ {a} ^ {b} f (x) \mathrm{d} G (x) = \lim _ {k \to \infty} \sigma_ {k} (f, G; a, b).
$$

---

4.1 斯蒂尔切斯积分

93

例 4.1.1 若在定义 4.1.1 中取  $G(x) \equiv x + c$ ，其中 c 为常数，则 f 在  $[a, b]$  上相对于 G 的斯蒂尔切斯积分就是它的黎曼积分.

对于 $k \geqslant 1$ 令 $[a, b]$ 的分割点 $\{x_{k,i}\}$ 如定义4.1.1给出，并分别用 $M_{k,i}(f)$ 和 $m_{k,i}(f)$ 表示函数 $f$ 在区间 $[x_{k,i-1}, x_{k,i}]$ 上的上确界和下确界。再记

$$
D _ {k} (f, G; a, b) = \sum_ {i = 1} ^ {n _ {k}} [ M _ {k, i} (f) - m _ {k, i} (f) ] [ G (x _ {k, i}) - G (x _ {k, i - 1}) ]. \tag {4.1.2}
$$

定理4.1.1 函数 $f$ 在区间 $[a,b]$ 上 $G$ 可积的充要条件是 $\lim_{k\to \infty}D_k(f,G;a,b) = 0.$

定理4.1.2 有界区间上的 $G$ 积分具有如下性质:

(1) 区间  $[a, b]$  上的任何有界连续函数在该区间上 G 可积;
(2) 设 $a \leqslant b \leqslant c \in \mathbb{R}$. 若 $f$ 在 $[a, c]$ 上 $G$ 可积, 则 $f$ 在 $[a, b]$ 和 $[b, c]$ 上 $G$ 可积且

$$
\int_ {a} ^ {c} f (x) \mathrm{d} G (x) = \int_ {a} ^ {b} f (x) \mathrm{d} G (x) + \int_ {b} ^ {c} f (x) \mathrm{d} G (x);
$$

(3) 设 $\alpha \geqslant 0, \beta \in \mathbb{R}$ 而 $f$ 在 $[a, b]$ 上 $G$ 可积. 则 $\beta f$ 在该区间上 $\alpha G$ 可积且

$$
\int_ {a} ^ {b} \beta f (x) \mathrm{d} (\alpha G) (x) = \beta \alpha \int_ {a} ^ {b} f (x) \mathrm{d} G (x);
$$

(4) 若 $f_{1}, f_{2}$ 均在 $[a, b]$ 上 $G$ 可积, 则 $f_{1} + f_{2}$ 在 $[a, b]$ 上 $G$ 可积且

$$
\int_ {a} ^ {b} [ f _ {1} (x) + f _ {2} (x) ] \mathrm{d} G (x) = \int_ {a} ^ {b} f _ {1} (x) \mathrm{d} G (x) + \int_ {a} ^ {b} f _ {2} (x) \mathrm{d} G (x);
$$

(5) 若 $f$ 在 $[a, b]$ 上 $G_{1}$ 可积且 $G_{2}$ 可积, 则 $f$ 在 $[a, b]$ 上 $G_{1} + G_{2}$ 可积且

$$
\int_ {a} ^ {b} f (x) \mathrm{d} (G _ {1} + G _ {2}) (x) = \int_ {a} ^ {b} f (x) \mathrm{d} G _ {1} (x) + \int_ {a} ^ {b} f (x) \mathrm{d} G _ {2} (x);
$$

(6) 若 $f_{1}, f_{2}$ 均在 $[a, b]$ 上 $G$ 可积且 $f_{1} \leqslant f_{2}$, 则

$$
\int_ {a} ^ {b} f _ {1} (x) \mathrm{d} G (x) \leqslant \int_ {a} ^ {b} f _ {2} (x) \mathrm{d} G (x).
$$

上述两个定理的证明与黎曼积分的相应结果类似, 请读者自行完成. 对于函数 $f$, 定义其正部 $f^{+} = 0 \vee f$ 和负部 $f^{-} = 0 \vee (-f)$. 注意 $f^{+}$ 和 $f^{-}$ 都是非负函数, 且有 $f = f^{+} - f^{-}$.

定理4.1.3 函数 $f$ 在 $[a,b]$ 上 $G$ 可积当且仅当 $f^{+}$ 和 $f^{-}$ 均在 $[a,b]$ 上 $G$ 可积.在这种情况下有

$$
\int_ {a} ^ {b} f (x) \mathrm{d} G (x) = \int_ {a} ^ {b} f ^ {+} (x) \mathrm{d} G (x) - \int_ {a} ^ {b} f ^ {-} (x) \mathrm{d} G (x). \tag {4.1.3}
$$

---

94

第四章 积分和数学期望

证明 假定 $f$ 在 $[a, b]$ 上 $G$ 可积. 注意 $M_{k,i}(f^{+}) - m_{k,i}(f^{+}) \leqslant M_{k,i}(f) - m_{k,i}(f)$. 由定理4.1.1不难看出 $f^{+}$ 在 $[a, b]$ 上 $G$ 可积, 类似地可知 $f^{-}$ 在 $[a, b]$ 上 $G$ 可积. 另一方面, 若 $f^{+}$ 和 $f^{-}$ 均在 $[a, b]$ 上 $G$ 可积, 由定理4.1.2知 $f = f^{+} - f^{-}$ 在 $[a, b]$ 上 $G$ 可积且(4.1.3)式成立.

## 4.1.2 常用积分性质

定理4.1.4 设 $g$ 是 $[a, b]$ 上的非负 $G$ 可积函数。固定 $F(a)$ 并定义积分上限的函数

$$
F (y) = F (a) + \int_ {a} ^ {y} g (x) \mathrm{d} G (x), \quad y \in [ a, b ]. \tag {4.1.4}
$$

则 $F$ 在 $[a, b]$ 上右连续且不降.

证明 显然 $F$ 是 $[a, b]$ 上的不降函数, 故它在每点处存在左、右极限. 下证 $F$ 在 $[a, b]$ 上右连续. 分两种情况讨论: (i) 若存在 $r \in (a, b]$ 使当 $x \in [a, r]$ 时有 $G(x) = G(a)$, 则显然对 $y \in [a, r]$ 有 $F(y) = F(a)$. (ii) 若对一切 $x \in (a, b]$ 有 $G(x) > G(a)$, 则由 $g$ 的 $G$ 可积性必有 $r \in (a, b]$ 使 $M := \sup_{a \leqslant x \leqslant r} g(x) < \infty$, 故当 $y \in [a, r]$ 有

$$
0 \leqslant F (y) - F (a) = \int_ {a} ^ {y} g (x) \mathrm{d} G (x) \leqslant M [ G (y) - G (a) ].
$$

由 $G$ 的右连续性得 $\lim_{y\to a+}F(y) = F(a)$, 故 $F$ 在 $a$ 处右连续. 再应用定理4.1.2中的性质(3)易知 $F$ 在 $[a,b]$ 上右连续. 所以定理的结论成立. □

定理4.1.5 设 $g$ 是 $[a, b]$ 上的非负 $G$ 可积函数，而 $F$ 是由(4.1.4)式定义的右连续不降函数。则有界函数 $f$ 在 $[a, b]$ 上 $F$ 可积当且仅当 $fg$ 在 $[a, b]$ 上 $G$ 可积，且在这种情况下有

$$
\int_ {a} ^ {b} f (x) \mathrm{d} F (x) = \int_ {a} ^ {b} f (x) g (x) \mathrm{d} G (x). \tag {4.1.5}
$$

证明 对于 $k \geqslant 1$ 令 $\{x_{k,i}\}$ 和 $\{t_{k,i}\}$ 如定义4.1.1给出，并分别用 $M_{k,i}(g)$ 和 $m_{k,i}(g)$ 表示函数 $g$ 在区间 $[x_{k,i-1}, x_{k,i}]$ 上的上确界和下确界. 注意

$$
\begin{array}{l} \left| \sigma_ {k} (f, F; a, b) - \sigma_ {k} (f g, G; a, b) \right| \\ = \left| \sum_ {i = 1} ^ {n _ {k}} f (t _ {k, i}) \left[ \int_ {x _ {k, i - 1}} ^ {x _ {k, i}} g (x) \mathrm{d} G (x) - g (t _ {k, i}) [ G (x _ {k, i}) - G (x _ {k, i - 1}) ] \right] \right| \\ = \left| \sum_ {i = 1} ^ {n _ {k}} f (t _ {k, i}) \int_ {x _ {k, i - 1}} ^ {x _ {k, i}} [ g (x) - g (t _ {k, i}) ] \mathrm{d} G (x) \right| \\ \leqslant \| f \| \sum_ {i = 1} ^ {n _ {k}} [ M _ {k, i} (g) - m _ {k, i} (g) ] [ G (x _ {k, i}) - G (x _ {k, i - 1}) ]. \\ \end{array}
$$

---

4.1 斯蒂尔切斯积分

95

因 $g$ 在 $[a, b]$ 上 $G$ 可积, 上式右端当 $k \to \infty$ 时趋于零, 故有欲证结论.

推论4.1.6 设 $F$ 是以 $g$ 为密度函数的绝对连续型分布函数. 则有界函数 $f$ 在 $[a, b]$ 上 $F$ 可积当且仅当 $fg$ 在 $[a, b]$ 上黎曼可积, 且在这种情况下有

$$
\int_ {a} ^ {b} f (x) \mathrm{d} F (x) = \int_ {a} ^ {b} f (x) g (x) \mathrm{d} x. \tag {4.1.6}
$$

定理 4.1.7 设 G 是离散型分布函数且在左开右闭区间  $(a, b]$  中的跳跃点集为  $S := \{y_j : j = 1, 2, \cdots\}$ . 若函数 f 在  $[a, b]$  上有界且在 S 的每点处连续（当  $b \in S$  时只要求 f 在此处左连续），则它在  $[a, b]$  上 G 可积且有

$$
\int_ {a} ^ {b} f (x) \mathrm{d} G (x) = \sum_ {j = 1} ^ {\infty} f (y _ {j}) [ G (y _ {j}) - G (y _ {j} -) ]. \tag {4.1.7}
$$

证明 对于任何 $\varepsilon > 0$, 可取充分大的 $m \geqslant 1$ 使得

$$
\sum_ {j = m + 1} ^ {\infty} \left[ G (y _ {j}) - G (y _ {j} -) \right] = \sum_ {j = m + 1} ^ {\infty} \mu (\{y _ {j} \}) <   \varepsilon .
$$

对于 $k \geqslant 1$ 令 $[a, b]$ 的分割点 $\{x_{k,i}\}$ 如定义4.1.1给出。当 $k \geqslant 1$ 充分大时，有限集 $\{y_1, y_2, \dots, y_m\}$ 中的不同的点属于 $[x_{k,i-1}, x_{k,i}]$，$i = 1, 2, \dots, n_k$ 中不同的区间。不妨设 $y_j \in [x_{k,i_j-1}, x_{k,i_j}]$，$j = 1, 2, \dots, m$。不难发现

$$
\begin{array}{l} \left| \sigma_ {k} (f, G; a, b) - \sum_ {j = 1} ^ {\infty} f (y _ {j}) [ G (y _ {j}) - G (y _ {j} -) ] \right| \\ \leqslant \left| \sum_ {i = 1} ^ {n _ {k}} f (t _ {k, i}) [ G (x _ {k, i}) - G (x _ {k, i - 1}) ] - \sum_ {j = 1} ^ {m} f (y _ {j}) [ G (y _ {j}) - G (y _ {j} -) ] \right| + \\ \sum_ {j = m + 1} ^ {\infty} | f (y _ {j}) | [ G (y _ {j}) - G (y _ {j} -) ] \\ \leqslant \left| \sum_ {j = 1} ^ {m} f (t _ {k, i _ {j}}) [ G (y _ {j}) - G (y _ {j} -) ] - \sum_ {j = 1} ^ {m} f (y _ {j}) [ G (y _ {j}) - G (y _ {j} -) ] \right| + \\ 2 \| f \| \sum_ {j = m + 1} ^ {\infty} [ G (y _ {j}) - G (y _ {j} -) ] \\ \leqslant \sum_ {j = 1} ^ {m} | f (t _ {k, i _ {j}}) - f (y _ {j}) | [ G (y _ {j}) - G (y _ {j} -) ] + 2 \| f \| \varepsilon . \\ \end{array}
$$

显然, 当 $k \to \infty$ 时有 $|t_{k,i_j} - y_j| \to 0$, 故 $|f(t_{k,i_j}) - f(y_j)| \to 0$. 在上式两端令 $k \to \infty$ 取上极限, 再由 $\varepsilon > 0$ 的任意性即知 (4.1.7) 式成立. □

---

96

第四章 积分和数学期望

定理 4.1.8 设函数  $f_{n}, n=1,2,\cdots$  在  $[a,b]$  上 G 可积且一致地  $\lim_{n\to\infty}f_{n}=f$ . 则 f 在  $[a,b]$  上 G 可积且

$$
\lim _ {n \to \infty} \int_ {a} ^ {b} f _ {n} (x) \mathrm{d} G (x) = \int_ {a} ^ {b} f (x) \mathrm{d} G (x). \tag {4.1.8}
$$

证明 对于 $k \geqslant 1$ 令 $[a, b]$ 的分割点 $\{x_{k,i}\}$ 如定义4.1.1给出. 对于任意的 $\varepsilon > 0$ 可取充分大的 $N \geqslant 1$, 使当 $n \geqslant N$ 时, 对 $x \in [a, b]$ 有 $|f_n(x) - f(x)| \leqslant \varepsilon$. 此时显然有

$$
M _ {k, i} (f) - m _ {k, i} (f) \leqslant M _ {k, i} (f _ {n}) - m _ {k, i} (f _ {n}) + 2 \varepsilon .
$$

再由 (4.1.2) 式易见

$$
D _ {k} (f, G; a, b) \leqslant D _ {k} (f _ {n}, G; a, b) + 2 \varepsilon [ G (b) - G (a) ].
$$

因 $f_{n}$ 在 $[a,b]$ 上 $G$ 可积, 根据定理4.1.1有 $\lim_{k\to \infty}D_k(f_n,G;a,b) = 0$. 在上式两端取上极限得

$$
\operatorname * {l i m s u p} _ {k \to \infty} D _ {k} (f, G; a, b) \leqslant 2 \varepsilon [ G (b) - G (a) ].
$$

由 $\varepsilon > 0$ 的任意性有 $\lim_{k \to \infty} D_k(f, G; a, b) = 0$. 再由定理4.1.1知 $f$ 在 $[a, b]$ 上 $G$ 可积. 此外, 应用定理4.1.2不难看出, 当 $n \geqslant N$ 时有

$$
\left| \int_ {a} ^ {b} f _ {n} (x) \mathrm{d} G (x) - \int_ {a} ^ {b} f (x) \mathrm{d} G (x) \right| \leqslant \int_ {a} ^ {b} | f _ {n} (x) - f (x) | \mathrm{d} G (x) \leqslant \varepsilon [ G (b) - G (a) ].
$$

在上式两端令  $n \rightarrow \infty$  取上极限, 再由  $\varepsilon > 0$  的任意性可知 (4.1.8) 式成立.

## 4.1.3 全空间上的积分

现在考虑一维欧氏空间 $\mathbb{R}$ 上的积分. 设 $G$ 是 $\mathbb{R}$ 上的分布函数, 即存在 $(\mathbb{R}, \mathcal{B})$ 上的局部有限测度 $\mu$ 使得

$$
G (b) - G (a) = \mu (a, b ], \quad a \leqslant b \in \mathbb {R}. \tag {4.1.9}
$$

定义4.1.2 设 $\mathbb{R}$ 上的函数 $f$ 在每个有界区间 $[a, b] \subseteq \mathbb{R}$ 上 $G$ 可积. 令 $f^{+} = 0 \vee f$ 和 $f^{-} = 0 \vee (-f)$ 分别是 $f$ 的正部和负部. 如果两个极限

$$
\int_ {- \infty} ^ {\infty} f ^ {\pm} (x) \mathrm{d} G (x) := \lim _ {a \to - \infty} \lim _ {b \to \infty} \int_ {a} ^ {b} f ^ {\pm} (x) \mathrm{d} G (x) \tag {4.1.10}
$$

中至少有一个有限, 就称 $f$ 在 $\mathbb{R}$ 上相对于 $G$ 的斯蒂尔切斯积分存在. 在这种情况下, 定义 $f$ 相对于 $G$ 的斯蒂尔切斯积分为

$$
\int_ {- \infty} ^ {\infty} f (x) \mathrm{d} G (x) = \int_ {- \infty} ^ {\infty} f ^ {+} (x) \mathrm{d} G (x) - \int_ {- \infty} ^ {\infty} f ^ {-} (x) \mathrm{d} G (x). \tag {4.1.11}
$$

---

4.1 斯蒂尔切斯积分

97

上式也简称为 $f$ 在 $\mathbb{R}$ 上的 $G$ 积分. 如果 (4.1.10) 式中的两个极限都有限, 就称 $f$ 在 $\mathbb{R}$ 上关于 $G$ 斯蒂尔切斯可积, 简称 $G$ 可积.

基于有界区间上斯蒂尔切斯积分的相应结论, 不难证明如下的几个定理:

定理4.1.9 一维空间 $\mathbb{R}$ 上的 $G$ 积分具有如下性质:

(1) 若 $f$ 在 $\mathbb{R}$ 上 $G$ 可积, 则它在 $[a, b] \subseteq \mathbb{R}$ 上 $G$ 可积且

$$
\int_ {a} ^ {b} f (x) \mathrm{d} G (x) = \int_ {- \infty} ^ {\infty} 1 _ {(a, b ]} (x) f (x) \mathrm{d} G (x);
$$

(2) 设 $\alpha \geqslant 0, \beta \in \mathbb{R}$ 而 $f$ 在 $\mathbb{R}$ 上 $G$ 可积. 则 $\beta f$ 在 $\mathbb{R}$ 上 $\alpha G$ 可积且

$$
\int_ {- \infty} ^ {\infty} \beta f (x) \mathrm{d} (\alpha G) (x) = \beta \alpha \int_ {- \infty} ^ {\infty} f (x) \mathrm{d} G (x);
$$

(3) 若 $f_{1}, f_{2}$ 均在 $\mathbb{R}$ 上 $G$ 可积, 则 $f_{1} + f_{2}$ 在 $\mathbb{R}$ 上 $G$ 可积且

$$
\int_ {- \infty} ^ {\infty} [ f _ {1} (x) + f _ {2} (x) ] \mathrm{d} G (x) = \int_ {- \infty} ^ {\infty} f _ {1} (x) \mathrm{d} G (x) + \int_ {- \infty} ^ {\infty} f _ {2} (x) \mathrm{d} G (x);
$$

(4) 若 $f$ 在 $\mathbb{R}$ 上 $G_{1}$ 可积且 $G_{2}$ 可积, 则 $f$ 在 $\mathbb{R}$ 上 $G_{1} + G_{2}$ 可积且

$$
\int_ {- \infty} ^ {\infty} f (x) \mathrm{d} (G _ {1} + G _ {2}) (x) = \int_ {- \infty} ^ {\infty} f (x) \mathrm{d} G _ {1} (x) + \int_ {- \infty} ^ {\infty} f (x) \mathrm{d} G _ {2} (x);
$$

(5) 若 $f_{1}, f_{2}$ 均在 $\mathbb{R}$ 上 $G$ 可积且 $f_{1} \leqslant f_{2}$, 则

$$
\int_ {- \infty} ^ {\infty} f _ {1} (x) \mathrm{d} G (x) \leqslant \int_ {- \infty} ^ {\infty} f _ {2} (x) \mathrm{d} G (x).
$$

定理4.1.10 设非负函数 $g$ 在 $\mathbb{R}$ 的每个有界闭区间上 $G$ 可积. 固定常数 $a$ 和 $F(a)$, 并定义 $\mathbb{R}$ 上的函数

$$
F (y) = F (a) - 1 _ {\{y \leqslant a \}} \int_ {y} ^ {a} g (x) \mathrm{d} G (x) + 1 _ {\{y > a \}} \int_ {a} ^ {y} g (x) \mathrm{d} G (x). \tag {4.1.12}
$$

则 F 是 R 上的分布函数.

定理4.1.11 设非负函数 $g$ 在 $\mathbb{R}$ 的每个有界闭区间上 $G$ 可积, 而 $F$ 是由(4.1.12)式定义的分布函数. 则局部有界函数 $f$ 在 $\mathbb{R}$ 上 $F$ 可积当且仅当 $fg$ 在 $\mathbb{R}$ 上 $G$ 可积, 且在这种情况下有

$$
\int_ {- \infty} ^ {\infty} f (x) \mathrm{d} F (x) = \int_ {- \infty} ^ {\infty} f (x) g (x) \mathrm{d} G (x). \tag {4.1.13}
$$

定理4.1.12 设 $F$ 是以 $g$ 为密度函数的绝对连续型分布函数, 而 $fg$ 在每个有界区间上黎曼可积. 则有

$$
\int_ {- \infty} ^ {\infty} f (x) \mathrm{d} F (x) = \int_ {- \infty} ^ {\infty} f (x) g (x) \mathrm{d} x. \tag {4.1.14}
$$

---

98

第四章 积分和数学期望

定理 4.1.13 设 G 是跳跃点集为  $E := \{x_{i} : i = 1, 2, \cdots\}$  的离散型分布函数，而 f 在 R 上局部有界且在 E 的每点处连续。则有

$$
\int_ {- \infty} ^ {\infty} f (x) \mathrm{d} G (x) = \sum_ {i = 1} ^ {\infty} f (x _ {i}) [ G (x _ {i}) - G (x _ {i} -) ]. \tag {4.1.15}
$$

定理 4.1.12 和定理 4.1.13 给出了两种典型的情况下, 全空间上斯蒂尔切斯积分的常用的计算方法. 定理中的等式的含义为: 只要等号两端有一边的积分存在则另一边的积分也存在且等式成立.

设分布函数 $F$ 和 $G$ 满足关系 (4.1.12) 式, 而 $\nu$ 和 $\mu$ 分别是 $F$ 和 $G$ 对应的 $(\mathbb{R}, \mathcal{B})$ 上的局部有限测度. 在这种情况下, 我们称 $F$ 或 $\nu$ 相对于 $G$ 或 $\mu$ 绝对连续且有密度函数 $g$, 简记作

$$
\mathrm{d} F (x) = g (x) \mathrm{d} G (x) \text {或} \nu (\mathrm{d} x) = g (x) \mu (\mathrm{d} x).
$$

这样, 此前定义的绝对连续型分布函数的概念就相当于这里 $G(x) \equiv x$ 的特例.

参考数学分析中的黎曼瑕积分的定义, 也可以讨论 $f$ 或 $G$ 在一个或多个点附近无界时的 $G$ 积分. 例如, 在定义4.1.2中将 $a \to -\infty$ 换为 $a \to 0+$ 就可以给出 $f$ 或 $G$ 在0右侧附近无界时在 $(0, \infty)$ 上的积分的定义.

## 4.1.4 多维空间上的积分

前面的讨论可以类似地拓展到多维空间的情况. 设 $G$ 是 $(\mathbb{R}^d, \mathcal{B}^d)$ 上的某个局部有限测度 $\mu$ 的分布函数, 即存在欧氏可测空间 $(\mathbb{R}^d, \mathcal{B}^d)$ 上的局部有限测度 $\mu$ 满足

$$
\mu (a, b ] = G (b) - G (a), \quad a \leqslant b \in \mathbb {R} ^ {d}. \tag {4.1.16}
$$

定义 4.1.3 令 f 为区间  $[a,b]=[a_{1},b_{1}]\times[a_{2},b_{2}]\times\cdots\times[a_{d},b_{d}]\subseteq\mathbb{R}^{d}$  上的函数. 对整数  $k\geqslant1$  和  $i=1,2,\cdots,d$ ，取区间  $[a_{i},b_{i}]$  的分割点  $a_{i}=x_{k,i,0}<x_{k,i,1}<\cdots<x_{k,i,n_{i,k}}=b_{i}$  满足

$$
\delta_ {k} := \max _ {1 \leqslant i \leqslant d} \max _ {1 \leqslant r \leqslant n _ {i, k}} (x _ {k, i, r} - x _ {k, i, r - 1}) \to 0, \quad k \to \infty ,
$$

并取 $t_{k,i,r}\in [x_{k,i,r - 1},x_{k,i,r}]$ .令

$$
\sigma_ {k} (f, G; a, b) = \sum_ {r _ {1} = 1} ^ {n _ {1, k}} \dots \sum_ {r _ {d} = 1} ^ {n _ {d, k}} f (t _ {k, 1, r _ {1}}, t _ {k, 2, r _ {2}}, \dots , t _ {k, d, r _ {d}}) \mu (\varDelta_ {k, r _ {1}, r _ {2}, \dots , r _ {d}}),
$$

其中

$$
\Delta_ {k, r _ {1}, r _ {2}, \dots , r _ {d}} = (x _ {k, 1, r _ {1} - 1}, x _ {k, 1, r _ {1}} ] \times (x _ {k, 2, r _ {2} - 1}, x _ {k, 2, r _ {2}} ] \times \dots \times (x _ {k, d, r _ {d} - 1}, x _ {k, d, r _ {d}} ].
$$

---

4.1 斯蒂尔切斯积分

99

若存在有限的极限 $\lim_{k\to \infty}\sigma_k(f,G;a,b)$ 且该极限与 $\{x_{k,i,r}\}$ 和 $\{t_{k,i,r}\}$ 的具体选取无关，则称 $f$ 在 $[a,b]$ 上相对于 $G$ 斯蒂尔切斯可积，简称 $G$ 可积.称该极限为 $f$ 在 $[a,b]$ 上相对于 $G$ 的斯蒂尔切斯积分，简称 $G$ 积分，并记作

$$
\int_ {a _ {1}} ^ {b _ {1}} \dots \int_ {a _ {d}} ^ {b _ {d}} f (x _ {1}, x _ {2}, \dots , x _ {d}) \mathrm{d} G (x _ {1}, x _ {2}, \dots , x _ {d}) = \lim _ {k \to \infty} \sigma_ {k} (f, G; a, b).
$$

定义 4.1.4 设  $R^{d}$  上的函数 f 在每个有界区间  $[a,b]=[a_{1},b_{1}]\times[a_{2},b_{2}]\times\cdots\times[a_{d},b_{d}]\subseteq\mathbb{R}^{d}$  上 G 可积. 如果极限

$$
\begin{array}{l} \int_ {- \infty} ^ {\infty} \dots \int_ {- \infty} ^ {\infty} f ^ {\pm} (x _ {1}, x _ {2}, \dots , x _ {d}) \mathrm{d} G (x _ {1}, x _ {2}, \dots , x _ {d}) \\ \begin{array}{r l} & {:= \lim _ {a _ {1}, \dots , a _ {d} \to - \infty} \lim _ {b _ {1}, \dots , b _ {d} \to \infty} \int_ {a _ {1}} ^ {b _ {1}} \dots \int_ {a _ {d}} ^ {b _ {d}} f ^ {\pm} (x _ {1}, x _ {2}, \dots , x _ {d}) \mathrm{d} G (x _ {1}, x _ {2}, \dots , x _ {d})} \end{array} \tag {4.1.17} \\ \end{array}
$$

中至少有一个有限, 我们就称 $f$ 在 $\mathbb{R}^d$ 上相对于 $G$ 的斯蒂尔切斯积分存在, 并将该积分定义为

$$
\begin{array}{l} \int_ {- \infty} ^ {\infty} \dots \int_ {- \infty} ^ {\infty} f (x _ {1}, x _ {2}, \dots , x _ {d}) \mathrm{d} G (x _ {1}, x _ {2}, \dots , x _ {d}) \\ = \int_ {- \infty} ^ {\infty} \dots \int_ {- \infty} ^ {\infty} f ^ {+} (x _ {1}, x _ {2}, \dots , x _ {d}) \mathrm{d} G (x _ {1}, x _ {2}, \dots , x _ {d}) - \\ \int_ {- \infty} ^ {\infty} \dots \int_ {- \infty} ^ {\infty} f ^ {-} (x _ {1}, x _ {2}, \dots , x _ {d}) \mathrm{d} G (x _ {1}, x _ {2}, \dots , x _ {d}). \\ \end{array}
$$

上式也简称为 $f$ 在 $\mathbb{R}^d$ 上的 $G$ 积分. 如果 (4.1.17) 式中的两个极限都有限, 就称 $f$ 在 $\mathbb{R}^d$ 上相对于 $G$ 斯蒂尔切斯可积, 简称 $G$ 可积.

特别地, 当 G 在  $R^{d}$  上有界时, 通过 (3.1.7) 式可以定义 G 的边缘分布函数  $G_{1}, G_{2}, \cdots, G_{d}$ . 此时, 若函数 f 只依赖于  $(x_{1}, x_{2}, \cdots, x_{d})$  的某个分量  $x_{i}$ , 则有

$$
\int_ {- \infty} ^ {\infty} \dots \int_ {- \infty} ^ {\infty} f (x _ {i}) \mathrm{d} G (x _ {1}, x _ {2}, \dots , x _ {d}) = \int_ {- \infty} ^ {\infty} f (x) \mathrm{d} G _ {i} (x).
$$

更一般地, 若函数 $f$ 只依赖于 $(x_{1}, x_{2}, \cdots, x_{d})$ 的某个子向量 $(x_{i_{1}}, x_{i_{2}}, \cdots, x_{i_{r}})$, 则它关于 $G$ 的积分可以转化为 $r$ 维空间上的斯蒂尔切斯积分.

前面证明的一维空间上的斯蒂尔切斯积分的性质都可以推广到多维空间.

## 4.1.5 关于积分的说明

设 $d$ 维欧氏可测空间 $(\mathbb{R}^d, \mathcal{B}^d)$ 上的局部有限测度 $\mu$ 有分布函数 $G$. 我们也称 $\mathbb{R}^d$ 上的函数 $f(x) = f(x_1, x_2, \dots, x_d)$ 关于 $G$ 的斯蒂尔切斯积分为它关于 $\mu$ 的斯蒂尔切斯

---

100

第四章 积分和数学期望

积分, 简称积分, 并将该积分写为

$$
\int_ {\mathbb {R} ^ {d}} f (x) \mathrm{d} G (x) = \int_ {\mathbb {R} ^ {d}} f (x) \mu (\mathrm{d} x).
$$

对于 $E \in \mathcal{B}^d$ 写

$$
\int_ {E} f (x) \mu (\mathrm{d} x) = \int_ {\mathbb {R} ^ {d}} f (x) 1 _ {E} (x) \mu (\mathrm{d} x).
$$

注意, 在此约定之下对 $a \leqslant b \in \mathbb{R}^d$ 有

$$
\int_ {a} ^ {b} f (x) \mathrm{d} G (x) = \int_ {(a, b ]} f (x) \mathrm{d} G (x) = \int_ {(a, b ]} f (x) \mu (\mathrm{d} x).
$$

设 $\mu_{1}$ 和 $\mu_{2}$ 是 $(\mathbb{R}^{d},\mathcal{B}^{d})$ 上的两个局部有限测度. 对于 $B\in \mathcal{B}^d$ 令 $\eta (B) = \mu_1(B) -$ $\mu_{2}(B)$ .称 $\eta$ 为符号测度，它是两个测度之差. 给定 $\mathbb{R}^d$ 上的函数 $f$ ，定义其关于 $\eta$ 的积分为

$$
\int_ {\mathbb {R} ^ {d}} f (x) \eta (\mathrm{d} x) = \int_ {\mathbb {R} ^ {d}} f (x) \mu_ {1} (\mathrm{d} x) - \int_ {\mathbb {R} ^ {d}} f (x) \mu_ {2} (\mathrm{d} x),
$$

这里要求等号右端的表达式有意义.分别用 $F_{1}, F_{2}$ 表示 $\mu_{1}, \mu_{2}$ 的分布函数.则函数 $F := F_{1} - F_{2}$ 作为两个单调函数之差在任何有界区间上有有界变差.我们也可以将上式右端解释为 $f$ 相对于 $F$ 的积分.关于有界变差函数的斯蒂尔切斯积分的更多讨论，可以参见[6].

斯蒂尔切斯积分与黎曼积分的定义方式非常相似, 因此对初学者比较容易理解. 但这种积分有个很大的缺点, 就是对于被积函数的要求太强, 以至于很多自然的函数在斯蒂尔切斯积分意义下不可积分. 例如, 在定理 4.1.7 和定理 4.1.13 中, 关于被积函数在分布函数的跳跃点的连续性就非常不自然.

本册书附录中介绍了函数对 $\sigma$ 有限测度的积分, 它大为扩展了可积分的函数类. 特别地, 在抽象测度积分的意义下, 任何有界可测函数相对于有限测度都是可积的. 在定理4.1.13的情况下, 可测函数 $f$ 相对于 $G$ 决定的局部有限测度的积分仍由(4.1.15)式给出. 由于这个原因, 后面在遇到 $\mathbb{R}$ 上的函数关于离散型分布函数的积分时, 我们并不严格要求被积函数的连续性, 而直接将积分理解为(4.1.15)式右端的级数. 对于多维空间的情况也做类似的理解.

## 练习题

1. 设 $G$ 是 $\mathbb{R}$ 上的连续分布函数. 证明: 若函数 $f$ 在有界区间 $[a, b]$ 上每点处有有限的左、右极限, 且至多在有限个点不连续, 则它在 $[a, b]$ 上 $G$ 可积.

---

4.2 随机变量的数学期望

101

2. 设 $G$ 是 $\mathbb{R}$ 上的分布函数. 证明: 若函数 $f$ 在有界区间 $[a, b]$ 上 $G$ 可积, 则它在任何子区间 $[c, d] \subseteq [a, b]$ 上 $G$ 可积.

3. 设 $G$ 是 $\mathbb{R}$ 上的分布函数, 而函数 $f$ 在 $[a, b]$ 上连续可微. 证明分部积分公式:

$$
\int_ {a} ^ {b} f (x) \mathrm{d} G (x) = f (x) G (x) \big | _ {a} ^ {b} - \int_ {a} ^ {b} f ^ {\prime} (x) G (x) \mathrm{d} x.
$$

4. 设 $G$ 是 $\mathbb{R}$ 上的分布函数. 证明:

(1) 若函数 $f_{1}, f_{2}$ 均在有界区间 $[a, b] \subseteq \mathbb{R}$ 上 $G$ 可积, 则 $f_{1} + f_{2}$ 在 $[a, b]$ 上 $G$ 可积且

$$
\int_ {a} ^ {b} [ f _ {1} (x) + f _ {2} (x) ] \mathrm{d} G (x) = \int_ {a} ^ {b} f _ {1} (x) \mathrm{d} G (x) + \int_ {a} ^ {b} f _ {2} (x) \mathrm{d} G (x).
$$

(2) 若函数 $f_{1}, f_{2}$ 均在 $\mathbb{R}$ 上 $G$ 可积, 则 $f_{1} + f_{2}$ 在 $\mathbb{R}$ 上 $G$ 可积且

$$
\int_ {- \infty} ^ {\infty} [ f _ {1} (x) + f _ {2} (x) ] \mathrm{d} G (x) = \int_ {- \infty} ^ {\infty} f _ {1} (x) \mathrm{d} G (x) + \int_ {- \infty} ^ {\infty} f _ {2} (x) \mathrm{d} G (x).
$$

## 4.2 随机变量的数学期望

数学期望是随机变量的取值对相应的概率的加权平均, 可以用相对于分布函数的斯蒂尔切斯积分表示. 特别地, 离散型随机变量的数学期望进一步可以转化为级数的求和, 而绝对连续型随机变量的数学期望的计算可用黎曼积分计算.

## 4.2.1 定义和基本性质

定义 4.2.1 设  $\xi$  是定义于概率空间  $(\Omega, \mathcal{F}, \mathbf{P})$  的随机变量, 有分布  $\mu_{\xi}$  和分布函数  $F_{\xi}$ . 如果函数  $f_{1}(x) \equiv x$  在 R 上关于分布函数  $F_{\xi}$  的斯蒂尔切斯积分存在, 就称该积分为  $\xi$  的数学期望或均值, 并记作  $E\xi$  或  $\mathbf{E}(\xi)$ , 即

$$
\mathbf {E} \xi = \int_ {- \infty} ^ {\infty} x \mathrm{d} F _ {\xi} (x). \tag {4.2.1}
$$

若函数 $f_{1}$ 在 $\mathbb{R}$ 上 $F_{\xi}$ 可积, 则称随机变量 $\xi$ 是可积的.

根据定理4.1.12和定理4.1.13有

命题 4.2.1 设  $\xi$  为绝对连续型随机变量且有分布密度 p. 若  $\xi$  的数学期望存在, 则

$$
\mathbf {E} \xi = \int_ {- \infty} ^ {\infty} x p (x) \mathrm{d} x.
$$

---

102

第四章 积分和数学期望

命题 4.2.2 设  $\xi$  为取值于可数集  $E := \{x_{1}, x_{2}, \cdots\} \subseteq R$  的离散型随机变量且有分布密度 p. 若  $\xi$  的数学期望存在, 则

$$
\mathbf {E} \xi = \sum_ {i = 1} ^ {\infty} x _ {i} p (x _ {i}).
$$

数学期望是随机变量的典型的数字特征, 它反映了该随机变量的整体性质.

例 4.2.1 根据医学数据分析, 某种流行病的患病率为 q (0 < q < 1). 现把 k (k ≥ 1) 个人分为一组, 将其血样混合后进行化验. 若结果为阴性, 则通过检验; 若结果为阳性, 则这 k 个人需要再分别化验一次. 记这 k 个人的化验次数为  $\xi$ , 则

$$
\mathbf {P} (\xi = 1) = (1 - q) ^ {k}, \quad \mathbf {P} (\xi = k + 1) = 1 - (1 - q) ^ {k}.
$$

所以

$$
\mathbf {E} \xi = (1 - q) ^ {k} + (k + 1) [ 1 - (1 - q) ^ {k} ] = k + 1 - k (1 - q) ^ {k}.
$$

通常 $q$ 的值很小, 此时可取适当的 $k$ 使 $k(1 - q)^k > 1$, 故 $\mathbf{E}\xi < k$. 也就是说, 用这样的方式可以减少化验次数, 从而降低成本.

若两个随机变量 $\xi$ 和 $\eta$ 满足 $\xi \stackrel{\mathrm{a.s.}}{=} \eta$, 则它们有相同的分布函数, 根据 (4.2.1) 式有 $\mathbf{E}\xi = \mathbf{E}\eta$.

定理4.2.3 设 $\xi$ 为非负随机变量. 则 $\mathbf{E}\xi \geqslant 0$, 且 $\mathbf{E}\xi = 0$ 当且仅当 $\xi = 0$ (a.s.).

证明 因 $\xi$ 是非负随机变量, 当 $x < 0$ 有 $F_{\xi}(x) = 0$. 根据斯蒂尔切斯积分的定义和性质易知

$$
\mathbf {E} \xi = \int_ {0} ^ {\infty} x \mathrm{d} F _ {\xi} (x) \geqslant 0.
$$

若 $\xi = 0$ (a.s.), 则 $F_{\xi}(x) = 1_{\{x \geqslant 0\}}$, 故由命题4.2.2有 $\mathbf{E}\xi = 0$. 反之, 若 $\mathbf{E}\xi = 0$, 则对任意的 $a > 0$ 有

$$
0 = \int_ {0} ^ {\infty} x \mathrm{d} F _ {\xi} (x) \geqslant \int_ {a} ^ {\infty} x \mathrm{d} F _ {\xi} (x) \geqslant a \int_ {a} ^ {\infty} \mathrm{d} F _ {\xi} (x) = a [ 1 - F _ {\xi} (a) ],
$$

故 $F_{\xi}(a) = 1$ ，再由右连续性得 $F_{\xi}(0) = 1$ ，从而 $\xi = 0$ (a.s.).

定理4.2.4 给定随机变量 $\xi$ ，令 $\xi^{+} = 0\lor \xi$ 和 $\xi^{-} = 0\lor (-\xi)$ .则有

$$
\mathbf {E} \xi^ {+} = \int_ {0} ^ {\infty} x \mathrm{d} F _ {\xi} (x) = \int_ {0} ^ {\infty} [ 1 - F _ {\xi} (t) ] \mathrm{d} t
$$

和

$$
\mathbf {E} \xi^ {-} = - \int_ {- \infty} ^ {0} x \mathrm{d} F _ {\xi} (x) = \int_ {- \infty} ^ {0} F _ {\xi} (t) \mathrm{d} t.
$$

---

4.2 随机变量的数学期望

103

证明 由于 $\xi^{+},\xi^{-}$ 都是非负随机变量, 对于 $x < 0$ 有 $F_{\xi^{+}}(x) = F_{\xi^{-}}(x) = 0$. 对任意的 $x \geqslant 0$, 显然有 $F_{\xi^{+}}(x) = F_{\xi}(x)$. 根据数学期望的定义, 并交换积分次序 (承认这是允许的) 得

$$
\begin{array}{l} \mathbf {E} \xi^ {+} = \int_ {0} ^ {\infty} x \mathrm{d} F _ {\xi} (x) = \int_ {0} ^ {\infty} \mathrm{d} F _ {\xi} (x) \int_ {0} ^ {x} \mathrm{d} t \\ = \int_ {0} ^ {\infty} \mathrm{d} t \int_ {t} ^ {\infty} \mathrm{d} F _ {\xi} (x) = \int_ {0} ^ {\infty} [ 1 - F _ {\xi} (t) ] \mathrm{d} t. \\ \end{array}
$$

所以定理中关于 $\mathbf{E}\xi^{+}$ 的表达式成立. 此外, 对 $x \geqslant 0$ 有

$$
F _ {\xi^ {-}} (x) = \mathbf {P} (\xi^ {-} \leqslant x) = \mathbf {P} (\xi \geqslant - x) = 1 - \mathbf {P} (\xi <   - x) = 1 - F _ {\xi} (- x -),
$$

注意这里 $x \mapsto -F_{\xi}(-x-)$ 是 $[0, \infty)$ 上的右连续不降函数. 在该函数的连续点集中取不降数列 $b_n \to \infty$. 根据上式有

$$
\begin{array}{l} \mathbf {E} \xi^ {-} = - \int_ {0} ^ {\infty} x \mathrm{d} F _ {\xi} (- x -) = - \lim _ {n \to \infty} \int_ {0} ^ {b _ {n}} x \mathrm{d} F _ {\xi} (- x -) \\ = - \lim _ {n \to \infty} \int_ {- b _ {n}} ^ {0} x \mathrm{d} F _ {\xi} (x) = - \int_ {- \infty} ^ {0} x \mathrm{d} F _ {\xi} (x) \\ = \int_ {- \infty} ^ {0} \mathrm{d} F _ {\xi} (x) \int_ {x} ^ {0} \mathrm{d} t = \int_ {- \infty} ^ {0} \mathrm{d} t \int_ {- \infty} ^ {t} \mathrm{d} F _ {\xi} (x) \\ = \int_ {- \infty} ^ {0} F _ {\xi} (t) \mathrm{d} t. \\ \end{array}
$$

这说明定理中关于  $E\xi^{-}$  的表达式成立.

由 (4.2.10) 和定理 4.2.4 易得

定理4.2.5 若随机变量 $\xi$ 的数学期望存在, 则有

$$
\mathbf {E} \xi = \int_ {0} ^ {\infty} \mathbf {P} (\xi > t) \mathrm{d} t - \int_ {- \infty} ^ {0} \mathbf {P} (\xi \leqslant t) \mathrm{d} t
$$

和

$$
\mathbf {E} | \xi | = \int_ {0} ^ {\infty} \mathbf {P} (\xi > t) \mathrm{d} t + \int_ {- \infty} ^ {0} \mathbf {P} (\xi \leqslant t) \mathrm{d} t.
$$

例 4.2.2 设  $\xi$  为取值于数集  $\{0,1,2,\cdots\}$  的离散型随机变量. 则

$$
\begin{array}{l} \mathbf {E} \xi = \int_ {0} ^ {\infty} \mathbf {P} (\xi > t) \mathrm{d} t = \sum_ {n = 1} ^ {\infty} \int_ {n - 1} ^ {n} \mathbf {P} (\xi > t) \mathrm{d} t \\ = \sum_ {n = 1} ^ {\infty} \int_ {n - 1} ^ {n} \mathbf {P} (\xi \geqslant n) \mathrm{d} t = \sum_ {n = 1} ^ {\infty} \mathbf {P} (\xi \geqslant n). \\ \end{array}
$$

---

104

第四章 积分和数学期望

## 4.2.2 随机变量函数的期望

假设随机变量 $\xi$ 有分布函数 $F_{\xi}$. 我们之前讨论过如何对可测函数 $f$ 求出随机变量 $f(\xi)$ 的分布函数 $F_{f(\xi)}$. 按照数学期望的定义有

$$
\mathbf {E} f (\xi) = \int_ {- \infty} ^ {\infty} x \mathrm{d} F _ {f (\xi)} (x).
$$

因此, 可以先求出 $f(\xi)$ 的分布, 再根据上式计算其数学期望 $\mathbf{E}f(\xi)$. 事实上, 我们也可以从 $\xi$ 的分布出发直接计算 $\mathbf{E}f(\xi)$.

命题 4.2.6 设  $\xi$  为取值于可数集  $E := \{x_{1}, x_{2}, \cdots\} \subseteq R$  的离散型随机变量，且有分布密度 p。再设 f 为 E 上的函数。若随机变量  $f(\xi)$  的数学期望存在，则有

$$
\mathbf {E} f (\xi) = \sum_ {i = 1} ^ {\infty} f (x _ {i}) p (x _ {i}).
$$

证明 令 $\{z_k : k = 1,2,\cdots\}$ 是去除数列 $\{f(x_i) : i = 1,2,\cdots\}$ 中多余的重复元素所得的集合. 则 $\zeta := f(\xi)$ 是取值于 $\{z_k : k = 1,2,\cdots\}$ 的离散型随机变量, 且其分布密度 $q$ 由 (3.3.2) 式给出. 再由命题 4.2.2 即知欲证结论成立. □

命题 4.2.6 中的结论可以推广到一般分布的形式. 为此注意, 根据定理 4.1.9, 对任意的  $a \leqslant b \in R$  有

$$
\int_ {- \infty} ^ {\infty} 1 _ {(a, b ]} (x) \mathrm{d} F _ {\xi} (x) = F _ {\xi} (b) - F _ {\xi} (a) = \mathbf {P} (a <   \xi \leqslant b).
$$

事实上, 对于相当一般的集合 $B \in \mathcal{B}$ 可以证明

$$
\int_ {- \infty} ^ {\infty} 1 _ {B} (x) \mathrm{d} F _ {\xi} (x) = \mathbf {P} (\xi \in B) = \mu_ {\xi} (B). \tag {4.2.2}
$$

定理4.2.7 设随机变量 $\xi$ 有分布函数 $F_{\xi}$, 而 $f$ 为 $\mathbb{R}$ 上的可测函数. 则随机变量 $f(\xi)$ 的数学期望存在当且仅当 $f$ 的 $F_{\xi}$ 积分存在, 且此时

$$
\mathbf {E} f (\xi) = \int_ {- \infty} ^ {\infty} f (x) \mathrm{d} F _ {\xi} (x). \tag {4.2.3}
$$

证明 此证明假定 (4.2.2) 式对于形如 $\{x \in \mathbb{R} : f(x) > t\}$ 和 $\{x \in \mathbb{R} : f(x) \leqslant t\}$ 的集合成立. 根据定理 4.2.5 有

$$
\begin{array}{l} \mathbf {E} f (\xi) = \int_ {0} ^ {\infty} \mathbf {P} (f (\xi) > t) \mathrm{d} t - \int_ {- \infty} ^ {0} \mathbf {P} (f (\xi) \leqslant t) \mathrm{d} t \\ = \int_ {0} ^ {\infty} \mathrm{d} t \int_ {- \infty} ^ {\infty} 1 _ {\{f (x) > t \}} \mathrm{d} F _ {\xi} (x) - \int_ {- \infty} ^ {0} \mathrm{d} t \int_ {- \infty} ^ {\infty} 1 _ {\{f (x) \leqslant t \}} \mathrm{d} F _ {\xi} (x) \\ \end{array}
$$

---

4.2 随机变量的数学期望

105

$$
\begin{array}{l} = \int_ {- \infty} ^ {\infty} \mathrm{d} F _ {\xi} (x) \int_ {0} ^ {\infty} 1 _ {\{f (x) > t \}} \mathrm{d} t - \int_ {- \infty} ^ {\infty} \mathrm{d} F _ {\xi} (x) \int_ {- \infty} ^ {0} 1 _ {\{f (x) \leqslant t \}} \mathrm{d} t \\ = \int_ {- \infty} ^ {\infty} f ^ {+} (x) \mathrm{d} F _ {\xi} (x) - \int_ {- \infty} ^ {\infty} f ^ {-} (x) \mathrm{d} F _ {\xi} (x). \\ \end{array}
$$

这里假定上面的积分换序是允许的. 因此定理结论成立.

![](../../raw/pages_0113-0128/images/page_119_image_4.jpg)

基于上面的定理, 并利用关于斯蒂尔切斯积分的结果可得

命题 4.2.8 设  $\xi$  为绝对连续型随机变量且有分布密度 p. 再设 f 为 R 上的可测函数. 若随机变量  $f(\xi)$  的数学期望存在, 则有

$$
\mathbf {E} f (\xi) = \int_ {- \infty} ^ {\infty} f (x) p (x) \mathrm{d} x.
$$

## 4.2.3 随机向量函数的期望

前面小节中的定理可以推广到随机向量的函数的情况. 为了表述上的方便, 这里只给出若干结果的二维形式.

定理4.2.9 设二维随机向量 $(\xi, \eta)$ 有联合分布函数 $F$，而 $f$ 为 $\mathbb{R}^2$ 上的可测函数。则随机变量 $f(\xi, \eta)$ 的数学期望存在当且仅当 $f$ 的 $F$ 积分存在，且此时

$$
\mathbf {E} f (\xi , \eta) = \int_ {- \infty} ^ {\infty} \int_ {- \infty} ^ {\infty} f (x, y) \mathrm{d} F (x, y). \tag {4.2.4}
$$

推论 4.2.10 设  $\alpha, \beta$  为常数而  $\xi, \eta$  为可积随机变量. 则  $\alpha\xi + \beta\eta$  为可积随机变量且

$$
\mathbf {E} (\alpha \xi + \beta \eta) = \alpha \mathbf {E} \xi + \beta \mathbf {E} \eta .
$$

推论 4.2.11 若  $\xi, \eta$  为可积随机变量且  $\xi \leqslant \eta$  (a.s.), 则  $E\xi \leqslant E\eta$ .

证明 在假定条件下有 $\eta -\xi \geqslant 0$ (a.s.). 再由定理4.2.3和推论4.2.10知 $\mathbf{E}\eta -\mathbf{E}\xi = \mathbf{E}(\eta -\xi)\geqslant 0.$

定理4.2.12 设 $\xi, \eta$ 为可积随机变量. 则 $\xi \leqslant \eta$ (a.s.) 当且仅当对任何 $A \in \mathcal{F}$ 都有 $\mathbf{E}(1_A\xi) \leqslant \mathbf{E}(1_A\eta)$.

证明 若 $\xi \leqslant \eta$ (a.s.), 则对 $A \in \mathcal{F}$ 显然有 $1_A\xi \leqslant 1_A\eta$ (a.s.), 由推论4.2.11有 $\mathbf{E}(1_A\xi) \leqslant \mathbf{E}(1_A\eta)$. 反之, 假设对任何 $A \in \mathcal{F}$ 都有 $\mathbf{E}(1_A\xi) \leqslant \mathbf{E}(1_A\eta)$. 取 $A = \{\xi - \eta > 0\}$ 得 $\mathbf{E}[1_A(\xi - \eta)] = \mathbf{E}(1_A\xi) - \mathbf{E}(1_A\eta) \leqslant 0$. 另一方面, 因 $1_A(\xi - \eta) \geqslant 0$, 必有 $\mathbf{E}[1_A(\xi - \eta)] = 0$, 再由定理4.2.3有 $1_A(\xi - \eta) = 0$ (a.s.). 因此 $\mathbf{P}(A) = 0$, 即 $\mathbf{P}(\xi \leqslant \eta) = 1$.

推论4.2.13 设 $\xi, \eta$ 为可积随机变量. 则 $\xi = \eta$ (a.s.) 当且仅当对任何 $A \in \mathcal{F}$ 都有 $\mathbf{E}(1_A\xi) = \mathbf{E}(1_A\eta)$.

---

106

第四章 积分和数学期望

命题 4.2.14 设  $(\xi,\eta)$  为取值于可数集  $E:=\{(x_{i},y_{j}):i,j=1,2,\cdots\}$  的二维离散型随机向量且有联合分布密度 p. 再设 f 为 E 上的函数. 若随机变量  $f(\xi,\eta)$  的数学期望存在, 则有

$$
\mathbf {E} f (\xi , \eta) = \sum_ {i = 1} ^ {\infty} \sum_ {j = 1} ^ {\infty} f (x _ {i}, y _ {j}) p (x _ {i}, y _ {j}).
$$

命题 4.2.15 设  $(\xi,\eta)$  为绝对连续型二维随机向量且有联合分布密度 p. 再设 f 为  $R^{2}$  上的函数. 若随机变量  $f(\xi,\eta)$  的数学期望存在, 则有

$$
\mathbf {E} f (\xi , \eta) = \int_ {- \infty} ^ {\infty} \int_ {- \infty} ^ {\infty} f (x, y) p (x, y) \mathrm{d} x \mathrm{d} y.
$$

下面是关于两个独立随机变量积的数学期望的一个常用的结果.

定理 4.2.16 若可积随机变量  $\xi$  和  $\eta$  相互独立, 则有  $\mathbf{E}(\xi\eta)=\mathbf{E}\xi\mathbf{E}\eta$ .

证明 因为 $\xi$ 和 $\eta$ 相互独立, 随机向量 $(\xi, \eta)$ 的联合分布函数 $F$ 为两个边缘分布函数之积, 即 $F(x, y) = F_{\xi}(x)F_{\eta}(y)$. 考虑有界区间 $[a, b] \subseteq \mathbb{R}^2$. 对于 $k \geqslant 1$ 令 $\{x_{k,i}\}$ 和 $\{t_{k,r,i}\}$ 如定义4.1.3给出. 分别用 $\mu$ 和 $\mu_{\xi}, \mu_{\eta}$ 表示 $(\xi, \eta)$ 的联合分布和两个边缘分布. 令

$$
\sigma_ {k} (a, b) = \sum_ {i = 1} ^ {m _ {k}} \sum_ {j = 1} ^ {m _ {k}} t _ {k, 1, i} t _ {k, 2, j} \mu \big ((x _ {k, 1, i - 1}, x _ {k, 1, i} ] \times (x _ {k, 2, j - 1}, x _ {k, 2, j} ] \big).
$$

由定理3.2.2知

$$
\mu \big ((x _ {k, 1, i - 1}, x _ {k, 1, i} ] \times (x _ {k, 2, j - 1}, x _ {k, 2, j} ] \big) = \mu_ {\xi} \big ((x _ {k, 1, i - 1}, x _ {k, 1, i} ] \big) \mu_ {\eta} \big ((x _ {k, 2, j - 1}, x _ {k, 2, j} ] \big).
$$

因此

$$
\sigma_ {k} (a, b) = \sum_ {i = 1} ^ {m _ {k}} t _ {k, 1, i} \mu_ {\xi} \big ((x _ {k, 1, i - 1}, x _ {k, 1, i} ] \big) \sum_ {j = 1} ^ {m _ {k}} t _ {k, 2, j} \mu_ {\eta} \big ((x _ {k, 2, j - 1}, x _ {k, 2, j} ] \big).
$$

令 $k\to \infty$ 得

$$
\int_ {a _ {1}} ^ {b _ {1}} \int_ {a _ {2}} ^ {b _ {2}} x y \mathrm{d} F (x, y) = \int_ {a _ {1}} ^ {b _ {1}} x \mathrm{d} F _ {\xi} (x) \int_ {a _ {2}} ^ {b _ {2}} y \mathrm{d} F _ {\eta} (y).
$$

再令 $a_{r}\rightarrow -\infty$ 和 $b_{r}\to \infty ,r = 1,2$ 得

$$
\int_ {- \infty} ^ {\infty} x y \mathrm{d} F (x, y) = \int_ {- \infty} ^ {\infty} x \mathrm{d} F _ {\xi} (x) \int_ {- \infty} ^ {\infty} y \mathrm{d} F _ {\eta} (y).
$$

这说明  $\mathbf{E}(\xi\eta)=\mathbf{E}\xi\mathbf{E}\eta.$

---

4.2 随机变量的数学期望

107

例4.2.3 令 $\xi$ 为给定的随机变量. 若 $\mathbb{R}$ 上的不降函数 $f, g$ 满足 $\mathbf{E}[|f(\xi)| + |g(\xi)|] < \infty$. 则有

$$
\mathbf {E} [ f (\xi) ] \mathbf {E} [ g (\xi) ] \leqslant \mathbf {E} [ f (\xi) g (\xi) ]. \tag {4.2.5}
$$

为说明上式成立, 令 $\eta$ 为与 $\xi$ 独立同分布的随机变量. 因为 $f, g$ 都是不降函数, 总有 $[f(\xi) - f(\eta)][g(\xi) - g(\eta)] \geqslant 0$. 于是

$$
\begin{array}{l} 0 \leqslant \mathbf {E} \left\{\left[ f (\xi) - f (\eta) \right] \left[ g (\xi) - g (\eta) \right] \right\} \\ \leqslant \mathbf {E} [ f (\xi) g (\xi) ] - \mathbf {E} [ f (\eta) g (\xi) ] - \mathbf {E} [ f (\xi) g (\eta) ] + \mathbf {E} [ f (\eta) g (\eta) ] \\ \leqslant 2 \mathbf {E} [ f (\xi) g (\xi) ] - \mathbf {E} [ f (\eta) ] \mathbf {E} [ g (\xi) ] - \mathbf {E} [ f (\xi) ] \mathbf {E} [ g (\eta) ] \\ \leqslant 2 \mathbf {E} [ f (\xi) g (\xi) ] - 2 \mathbf {E} [ f (\xi) ] \mathbf {E} [ g (\xi) ]. \\ \end{array}
$$

所以 (4.2.5) 式成立.

## 4.2.4 常见分布的期望

例 4.2.4 设  $\xi$  服从伯努利分布  $B(1,p)$ . 则  $\mathbf{E}\xi = 1 \cdot p + 0 \cdot (1 - p) = p$ .

例 4.2.5 设  $\xi$  服从二项分布  $B(n,p)$ . 则  $\xi \stackrel{d}{=} \xi_{1} + \xi_{2} + \cdots + \xi_{n}$ ，其中  $\xi_{1}, \xi_{2}, \cdots, \xi_{n}$  相互独立且服从伯努利分布  $B(1,p)$ . 所以  $E\xi = E\xi_{1} + E\xi_{2} + \cdots + E\xi_{n} = np$ .

例4.2.6 设 $\xi$ 服从几何分布 $G(p)$. 利用幂级数的求导公式

$$
\begin{array}{l} \mathbf {E} \xi = \sum_ {i = 1} ^ {\infty} i (1 - p) ^ {i - 1} p = p \sum_ {i = 1} ^ {\infty} i (1 - p) ^ {i - 1} \\ = - p \frac {\mathrm{d}}{\mathrm{d} p} \sum_ {i = 1} ^ {\infty} (1 - p) ^ {i} = - p \frac {\mathrm{d}}{\mathrm{d} p} \left(\frac {1}{p} - 1\right) = \frac {1}{p}. \\ \end{array}
$$

我们知道, $\xi$ 同分布于可数重伯努利试验中到第 1 次成功时的试验次数. 由上式可以看出, 当 $p$ 变小时 $\mathbf{E}\xi$ 会变大, 即平均试验次数变大.

例 4.2.7 设随机变量  $\xi$  服从泊松分布  $P(\lambda)$ . 则

$$
\mathbf {E} \xi = \sum_ {i = 1} ^ {\infty} \frac {i \lambda^ {i}}{i !} \mathrm{e} ^ {- \lambda} = \lambda \sum_ {i = 1} ^ {\infty} \frac {\lambda^ {i - 1}}{(i - 1) !} \mathrm{e} ^ {- \lambda} = \lambda .
$$

例 4.2.8 设  $\xi$  服从均匀分布  $U(a,b)$ . 则

$$
\mathbf {E} \xi = \int_ {a} ^ {b} \frac {x}{b - a} \mathrm{d} x = \frac {a + b}{2}.
$$

例4.2.9 设随机变量 $\xi$ 服从指数分布 $E(\lambda)$. 则

$$
\mathbf {E} \xi = \int_ {0} ^ {\infty} x \lambda \mathrm{e} ^ {- \lambda x} \mathrm{d} x = - x \mathrm{e} ^ {- \lambda x} \big | _ {0} ^ {\infty} + \int_ {0} ^ {\infty} \mathrm{e} ^ {- \lambda x} \mathrm{d} x = \frac {1}{\lambda}.
$$

---

108

第四章 积分和数学期望

例4.2.10 设随机变量 $\xi$ 服从正态分布 $N(a, \sigma^2)$. 则

$$
\begin{array}{l} \mathbf {E} \xi = \frac {1}{\sqrt {2 \pi} \sigma} \int_ {- \infty} ^ {\infty} x \mathrm{e} ^ {- \frac {(x - a) ^ {2}}{2 \sigma^ {2}}} \mathrm{d} x \\ = \frac {1}{\sqrt {2 \pi} \sigma} \int_ {- \infty} ^ {\infty} (x + a) \mathrm{e} ^ {- \frac {x ^ {2}}{2 \sigma^ {2}}} \mathrm{d} x = a. \\ \end{array}
$$

例 4.2.11 设  $\xi$  服从卡方分布  $\chi^{2}(n)$ . 则  $\xi \stackrel{d}{=} \sum_{i=1}^{n} \xi_{i}^{2}$ , 其中  $\xi_{i}, i=1,2,\cdots,n$  独立且服从分布  $N(0,1)$ . 因此

$$
\mathbf {E} \xi = \sum_ {i = 1} ^ {n} \mathbf {E} (\xi_ {i} ^ {2}) = n \mathbf {E} (\xi_ {1} ^ {2}) = \frac {n}{\sqrt {2 \pi}} \int_ {- \infty} ^ {\infty} x ^ {2} \mathrm{e} ^ {- \frac {x ^ {2}}{2}} \mathrm{d} x = n.
$$

例 4.2.12 设  $\xi$  服从学生分布  $t(n)$ . 根据学生分布的定义, 若取 X 服从分布  $N(0,1)$  和 Y 服从分布  $\chi^{2}(n)$  且二者相互独立, 则  $\xi \stackrel{\mathrm{d}}{=} X / \sqrt{Y / n}$ . 利用独立性得

$$
\mathbf {E} \xi = \mathbf {E} X \cdot \mathbf {E} \Big (\frac {1}{\sqrt {Y / n}} \Big) = 0.
$$

例 4.2.13 柯西分布的数学期望不存在. 以具有参数  $(0,1)$  的柯西分布为例. 该分布的密度函数为

$$
p (x) = \frac {1}{\pi (1 + x ^ {2})}, \quad x \in \mathbb {R}.
$$

因此有

$$
\int_ {- \infty} ^ {\infty} | x | p (x) \mathrm{d} x = \int_ {- \infty} ^ {\infty} \frac {| x |}{\pi (1 + x ^ {2})} \mathrm{d} x = \infty .
$$

## 4.2.5 期望和积分收敛定理

定理 4.2.17（有界收敛定理） 设随机变量  $\xi, \xi_{n}, n=1,2,\cdots$  满足  $\lim_{n\to\infty}\xi_{n}\stackrel{a.s.}{=} \xi$ . 若有常数  $M \geqslant 0$  使得  $|\xi_{n}| \leqslant M$  (a.s.),  $n=1,2,\cdots$ , 则有  $\lim_{n\to\infty}E\xi_{n}=E\xi$ .

证明 显然, 可以假定在全空间 $\Omega$ 上有 $\lim_{n\to \infty}\xi_n = \xi$ 且 $|\xi_n| \leqslant M, n = 1,2,\dots$. 这样, 显然有 $|\xi| \leqslant M$, 故随机变量 $\xi, \xi_n, n = 1,2,\dots$ 均可积. 对于 $\varepsilon > 0$, 令 $A_n = \{\omega \in \Omega : \sup_{k \geqslant n} |\xi_k(\omega) - \xi(\omega)| \geqslant \varepsilon\}$. 则事件序列 $\{A_n\} \subseteq \mathscr{F}$ 不增且有 $\bigcap_{n=1}^{\infty} A_n = \varnothing$. 由数学期望的性质,

$$
\left| \mathbf {E} \xi_ {n} - \mathbf {E} \xi \right| \leqslant \mathbf {E} | \xi_ {n} - \xi | \leqslant \mathbf {E} (2 M 1 _ {A _ {n}} + \varepsilon) = 2 M \mathbf {P} (A _ {n}) + \varepsilon .
$$

根据概率的上连续性有 $\lim_{n\to \infty}\mathbf{P}(A_n) = 0$ ，故得 $\limsup_{n\to \infty}|\mathbf{E}\xi_n - \mathbf{E}\xi |\leqslant \varepsilon .$ 再由 $\varepsilon >0$ 的任意性知 $\limsup_{n\to \infty}|\mathbf{E}\xi_n - \mathbf{E}\xi | = 0,$ 故有 $\lim_{n\to \infty}\mathbf{E}\xi_n = \mathbf{E}\xi .$ □

---

4.2 随机变量的数学期望

109

定理 4.2.17 称为有界收敛定理. 在此基础上, 可以证明下面的单调收敛定理、法图 (Fatou) 定理和控制收敛定理. 它们构成关于随机变量的数学期望收敛性质的基本定理.

定理 4.2.18（单调收敛定理） 设  $\xi, \xi_{n}, n = 1, 2, \cdots$  为非负随机变量且单调不降地  $\lim_{n \to \infty} \xi_{n} \stackrel{a.s.}{=} \xi$ . 则有  $\lim_{n \to \infty} E\xi_{n} = E\xi$ .

证明 当 $\xi$ 有界时, 根据定理4.2.17有 $\lim_{n\to \infty}\mathbf{E}\xi_n = \mathbf{E}\xi$. 下面考虑一般情况. 显然 $\limsup_{n\to \infty}\mathbf{E}\xi_n\leqslant \mathbf{E}\xi$. 另一方面, 任取 $k\geqslant 1$ 并对随机变量 $\xi \wedge k$ 和 $\xi_{n}\wedge k$ 应用定理4.2.17得

$$
\operatorname * {l i m i n f} _ {n \to \infty} \mathbf {E} \xi_ {n} \geqslant \lim _ {n \to \infty} \mathbf {E} (\xi_ {n} \wedge k) = \mathbf {E} (\xi \wedge k) \geqslant \mathbf {E} (\xi 1 _ {\{\xi \leqslant k \}}),
$$

其中

$$
\mathbf {E} (\xi 1 _ {\{\xi \leqslant k \}}) = \int_ {0} ^ {\infty} x 1 _ {\{x \leqslant k \}} \mathrm{d} F (x) = \int_ {0} ^ {k} x \mathrm{d} F (x).
$$

根据斯蒂尔切斯积分的定义有 $\lim_{k\to \infty}\mathbf{E}(\xi 1_{\{\xi \leqslant k\}}) = \infty$ ，因此有 $\liminf_{n\to \infty}\mathbf{E}\xi_n\geqslant \mathbf{E}\xi .$

定理 4.2.19（法图定理） 对于任何非负随机变量  $\xi_{n}, n=1,2,\cdots$  有

$$
\operatorname * {l i m i n f} _ {n \to \infty} \mathbf {E} \xi_ {n} \geqslant \mathbf {E} \big (\operatorname * {l i m i n f} _ {n \to \infty} \xi_ {n} \big). \tag {4.2.6}
$$

证明 令 $\eta_{n} = \inf_{k\geqslant n}\xi_{k}$ .则有 $0\leqslant \eta_n\leqslant \xi_n$ 且单调不降地 $\lim_{n\to \infty}\eta_n = \liminf_{n\to \infty}\xi_n$ 利用单调收敛定理即得(4.2.6)式.

定理 4.2.20（控制收敛定理） 设随机变量  $\xi, \xi_{n}, n=1,2,\cdots$  满足  $\lim_{n\to\infty}\xi_{n}\stackrel{a.s.}{=} \xi$ . 若有非负可积随机变量  $\eta$  使得  $|\xi_{n}|\leqslant\eta$  (a.s.),  $n=1,2,\cdots$ , 则有  $\lim_{n\to\infty}E\xi_{n}=E\xi$ .

证明 在假设条件下  $\eta \pm \xi_{n}, n = 1, 2, \cdots$  均为非负随机变量. 根据法图定理有

$$
\operatorname * {l i m   i n f} _ {n \to \infty} (\mathbf {E} \eta \pm \mathbf {E} \xi_ {n}) = \operatorname * {l i m   i n f} _ {n \to \infty} \mathbf {E} (\eta \pm \xi_ {n}) \geqslant \mathbf {E} (\eta \pm \xi) = \mathbf {E} \eta \pm \mathbf {E} \xi .
$$

因此有  $\lim_{n\to\infty}E\xi_{n}=E\xi.$

例 4.2.14 取  $\Omega=(0,1)$  和  $\mathcal{F}=(0,1)\cap\mathcal{B}$ ，令 P 为  $(\Omega,\mathcal{F})$  上的勒贝格测度。则  $(\Omega,\mathcal{F},\mathbf{P})$  为概率空间。对  $n\geqslant1$  令  $\xi_{n}=n1_{(0,1/n]}$ 。显然  $\lim_{n\to\infty}\xi_{n}=0$  在  $\Omega$  上处处成立。但是  $\lim_{n\to\infty}\mathbf{E}\xi_{n}=1\neq0$ 。这说明极限与数学期望次序的交换并不是无条件成立的。

因为随机变量的数学期望是用关于其分布或分布函数的积分定义的, 所以上面的基本收敛定理本质上是关于积分的收敛定理. 下面分别给出了便于应用的有界收敛定理和控制收敛定理的积分形式.

定理 4.2.21（有界收敛定理）令 G 是  $(\mathbb{R}, \mathcal{B})$  上的有限测度  $\mu$  的分布函数。设  $f, f_{n}, n = 1, 2, \cdots$  是 R 上的 G 可积函数且相对  $\mu$  有  $\lim_{n \to \infty} f_{n} = f$  (a.e.)。若有常数  $M \geqslant 0$  使得  $|f_{n}| \leqslant M$  (a.e.),  $n = 1, 2, \cdots$ ，则

$$
\lim _ {n \to \infty} \int_ {- \infty} ^ {\infty} f _ {n} (x) \mathrm{d} G (x) = \int_ {- \infty} ^ {\infty} f (x) \mathrm{d} G (x). \tag {4.2.7}
$$

---

110

第四章 积分和数学期望

证明 只需考虑 G 为概率分布函数的情况. 此时, 令  $\xi$  是以 G 为分布函数的随机变量. 根据假定条件, 显然有  $\lim_{n\to\infty}f_n(\xi)=f(\xi)$  和  $|f_n(\xi)|\leqslant M$  (a.s.),  $n=1,2,\cdots$ . 由定理 4.2.7 和定理 4.2.17 即得欲证结论. □

称 $\mathbb{R}$ 上的函数 $f$ 有有界支撑, 是指存在常数 $A \geqslant 0$ 使当 $|x| \geqslant A$ 有 $f(x) = 0$.

推论4.2.22 设 $F$ 和 $G$ 是 $\mathbb{R}$ 上的有界分布函数且 $F(-\infty) = G(-\infty) = 0$. 若对于任何有有界支撑的连续函数 $f$ 都有

$$
\int_ {- \infty} ^ {\infty} f (x) \mathrm{d} F (x) = \int_ {- \infty} ^ {\infty} f (x) \mathrm{d} G (x), \tag {4.2.8}
$$

则 $F$ 和 $G$ 在 $\mathbb{R}$ 上恒相等.

证明 任取 $a < b \in \mathbb{R}$. 易证 $g(x) := \inf \{|x - y| : y \in (a, b)^c\}$ 为 $\mathbb{R}$ 上的非负连续函数, 且对 $x \in (a, b)$ 有 $g(x) > 0$, 而对 $x \in (a, b)^c$ 有 $g(x) = 0$. 再对 $k \geqslant 1$ 令 $f_k(x) = 1 \wedge [kg(x)]$. 则 $f_k$ 为 $\mathbb{R}$ 上的有有界支撑的非负连续函数, 且当 $k \to \infty$ 时单调不降地 $f_k(x) \to 1_{(a, b)}(x)$. 对函数 $f_k$ 应用 (4.2.8) 式, 再令 $k \to \infty$, 由定理 4.2.21 得

$$
\int_ {- \infty} ^ {\infty} 1 _ {(a, b)} (x) \mathrm{d} F (x) = \int_ {- \infty} ^ {\infty} 1 _ {(a, b)} (x) \mathrm{d} G (x),
$$

即有 $F(b - ) - F(a) = G(b - ) - G(a)$. 取 $a = x - n$ 和 $b = x + 1 / n$ 并令 $n\to \infty$ 即得$F(x) = G(x)$ □

定理 4.2.23（控制收敛定理）令 G 是  $(\mathbb{R}, \mathcal{B})$  上的局部有限测度  $\mu$  的分布函数。设  $f, f_{n}, n = 1, 2, \cdots$  是 R 上的 G 可积函数且相对  $\mu$  有  $\lim_{n \to \infty} f_{n} = f$  (a.e.). 若有非负 G 可积函数 g 使得  $|f_{n}| \leqslant g$  (a.e.),  $n = 1, 2, \cdots$ ，则

$$
\lim _ {n \to \infty} \int_ {- \infty} ^ {\infty} f _ {n} (x) \mathrm{d} G (x) = \int_ {- \infty} ^ {\infty} f (x) \mathrm{d} G (x). \tag {4.2.9}
$$

证明 令 $F$ 是由 (4.1.12) 式定义的分布函数. 因为 $g$ 是 $G$ 可积函数, 所以 $F$ 在 $\mathbb{R}$ 上有界, 故它是某个有限测度 $\nu$ 的分布函数. 显然相对 $\nu$ 有 $\lim_{n\to \infty}f_n g^{-1}1_{\{g > 0\}} = fg^{-1}1_{\{g > 0\}}$ (a.e.). 根据定理 4.1.11 有

$$
\int_ {- \infty} ^ {\infty} f _ {n} (x) \mathrm{d} G (x) = \int_ {- \infty} ^ {\infty} f _ {n} (x) g (x) ^ {- 1} 1 _ {\{g (x) > 0 \}} \mathrm{d} F (x).
$$

对有界函数序列 $\{f_n g^{-1} 1_{\{g > 0\}}\}$ 和分布函数 $F$ 应用定理4.2.21即得欲证结论.

## 4.2.6 斯坦方程

设随机变量 $Z$ 服从标准正态分布 $N(0,1)$. 给定 $\mathbb{R}$ 上的有界可测函数 $h$, 考虑下面的关于该函数的斯坦 (Stein) 方程:

$$
f ^ {\prime} (x) - x f (x) = h (x) - \mathbf {E} h (Z). \tag {4.2.10}
$$

---

4.2 随机变量的数学期望

111

称绝对连续函数 $f$ 是方程 (4.2.10) 的解, 是指该方程对几乎所有 $x \in \mathbb{R}$ 成立. 将方程两边同乘因子 $\mathrm{e}^{-x^2 / 2}$ 得

$$
\left[ \mathrm{e} ^ {- x ^ {2} / 2} f (x) \right] ^ {\prime} = \mathrm{e} ^ {- x ^ {2} / 2} \big [ h (x) - \mathbf {E} h (Z) \big ].
$$

由此易知方程 (4.2.10) 有特解

$$
f _ {-} (x) = \mathrm{e} ^ {x ^ {2} / 2} \int_ {- \infty} ^ {x} \left[ h (y) - \mathbf {E} h (Z) \right] \mathrm{e} ^ {- y ^ {2} / 2} \mathrm{d} y \tag {4.2.11}
$$

和

$$
f _ {+} (x) = - \mathrm{e} ^ {x ^ {2} / 2} \int_ {x} ^ {\infty} \big [ h (y) - \mathbf {E} h (Z) \big ] \mathrm{e} ^ {- y ^ {2} / 2} \mathrm{d} y. \tag {4.2.12}
$$

注意, 对  $x \geqslant 1$  有

$$
| f _ {+} (x) | \leqslant 2 \| h \| \mathrm{e} ^ {x ^ {2} / 2} \int_ {x} ^ {\infty} y \mathrm{e} ^ {- y ^ {2} / 2} \mathrm{d} y = 2 \| h \|.
$$

所以 $f_{+}$ 在任何形如 $[a, \infty)$ 的区间上有界；同理 $f_{-}$ 在任何形如 $(- \infty, a]$ 的区间上有界。斯坦方程在正态分布及相关极限定理的研究中有重要的应用。基于该方程的方法称为斯坦方法。

定理4.2.24 随机变量 $X$ 服从正态分布 $N(0,1)$ 当且仅当对 $\mathbb{R}$ 上的任何满足 $\mathbf{E}|f'(X)| < \infty$ 的连续且分段连续可微函数 $f$ 有

$$
\mathbf {E} f ^ {\prime} (X) = \mathbf {E} [ X f (X) ]. \tag {4.2.13}
$$

证明 假设随机变量 $X$ 服从分布 $N(0,1)$. 再设连续且分段连续可微函数 $f$ 满足 $\mathbf{E}|f'(X)| < \infty$. 则

$$
\begin{array}{l} \mathbf {E} f ^ {\prime} (X) = \frac {1}{\sqrt {2 \pi}} \int_ {- \infty} ^ {\infty} f ^ {\prime} (y) \mathrm{e} ^ {- y ^ {2} / 2} \mathrm{d} y \\ = \frac {1}{\sqrt {2 \pi}} \int_ {0} ^ {\infty} f ^ {\prime} (y) \mathrm{d} y \int_ {y} ^ {\infty} x \mathrm{e} ^ {- x ^ {2} / 2} \mathrm{d} x - \frac {1}{\sqrt {2 \pi}} \int_ {- \infty} ^ {0} f ^ {\prime} (y) \mathrm{d} y \int_ {- \infty} ^ {y} x \mathrm{e} ^ {- x ^ {2} / 2} \mathrm{d} x \\ = \frac {1}{\sqrt {2 \pi}} \int_ {0} ^ {\infty} x \mathrm{e} ^ {- x ^ {2} / 2} \mathrm{d} x \int_ {0} ^ {x} f ^ {\prime} (y) \mathrm{d} y - \frac {1}{\sqrt {2 \pi}} \int_ {- \infty} ^ {0} x \mathrm{e} ^ {- x ^ {2} / 2} \mathrm{d} x \int_ {x} ^ {0} f ^ {\prime} (y) \mathrm{d} y \\ = \frac {1}{\sqrt {2 \pi}} \int_ {- \infty} ^ {\infty} [ f (x) - f (0) ] x \mathrm{e} ^ {- x ^ {2} / 2} \mathrm{d} x. \\ \end{array}
$$

因此 (4.2.13) 式成立. 反之, 假设对任何满足 $\mathbf{E}|f'(X)| < \infty$ 的连续且分段连续可微函数 $f$ 有 (4.2.13) 式成立. 将特解表达式 (4.2.11) 和 (4.2.12) 应用于函数 $h(x) = 1_{\{x \leqslant a\}}$, 对于 $x \leqslant a$ 有

$$
f _ {-} (x) = \mathrm{e} ^ {x ^ {2} / 2} \int_ {- \infty} ^ {x} \mathrm{e} ^ {- y ^ {2} / 2} [ 1 - \varPhi (a) ] \mathrm{d} y = \sqrt {2 \pi} \mathrm{e} ^ {x ^ {2} / 2} \varPhi (x) [ 1 - \varPhi (a) ],
$$

---

112

第四章 积分和数学期望

而对于 $x \geqslant a$ 有

$$
f _ {+} (x) = - \mathrm{e} ^ {x ^ {2} / 2} \int_ {x} ^ {\infty} \mathrm{e} ^ {- y ^ {2} / 2} \varPhi (a) \mathrm{d} y = \sqrt {2 \pi} \mathrm{e} ^ {x ^ {2} / 2} \varPhi (a) [ 1 - \varPhi (x) ].
$$

显然, 函数 $f_{a}(x) := f_{-}(x)1_{\{x \leqslant a\}} + f_{+}(x)1_{\{x > a\}}$ 在 $\mathbb{R}$ 上有界连续、分段连续可微, 并且也是关于 $h(x) = 1_{\{x \leqslant a\}}$ 的斯坦方程的解. 再根据 (4.2.10) 式和 (4.2.13) 式有

$$
0 = \mathbf {E} \big [ f _ {a} ^ {\prime} (X) - X f _ {a} (X) \big ] = \mathbf {E} \big [ 1 _ {\{X \leqslant a \}} - \varPhi (a) \big ] = \mathbf {P} (X \leqslant a) - \varPhi (a).
$$

所以 X 服从标准正态分布  $N(0,1)$ .

## 练习题

1. 设  $\xi$  为非负整数值随机变量且有常数 a, b > 0 使得

$$
\mathbf {P} (\xi = n) = \frac {a b ^ {n}}{n !}, \quad n = 0, 1, 2, \dots .
$$

已知  $E\xi = A$ . 求 a, b 的值.

2. 设 $\xi$ 是非负整数值随机变量. 证明 $\xi$ 服从参数为 $\lambda > 0$ 的泊松分布当且仅当对任何整数 $k \geqslant 1$ 有 $\lambda \mathbf{P}(\xi = k - 1) = k \mathbf{P}(\xi = k)$.
3. 设  $\xi, \eta$  独立同分布且服从正态分布  $N(0,1)$ . 证明  $\mathbf{E}(\xi \vee \eta) = 1/\sqrt{\pi}$ .
4. 某城市共有 N 辆汽车, 车牌号从 1 到 N. 现随机地记下 n 辆车的牌号, 记其最大牌号为  $\xi$ . 求数学期望  $E\xi$ .
5. 设随机变量  $\xi, \eta$  相互独立且均服从指数分布  $E(\lambda)$ . 求数学期望  $\mathbf{E}[(\xi + \eta)^{2}]$ .
6. 在  $(0,1)$  区间随机取 n 个点, 求相距最远的两点距离的期望.

## 4.3 方差、协方差和高阶矩

方差是随机变量的二阶中心矩, 反映了它的取值与期望偏离的程度, 具有非常重要的统计学意义. 协方差包含了两个随机变量之间相互关系有用的信息.

## 4.3.1 方差和标准差

设 $(\Omega, \mathcal{F}, \mathbf{P})$ 是一个概率空间. 称随机变量 $\xi$ 平方可积, 是指满足 $\mathbf{E}(\xi^2) < \infty$. 此时有 $\mathbf{E}|\xi| < \mathbf{E}(1 + \xi^2) < \infty$, 故 $\xi$ 可积. 令 $L^2$ 是由 $(\Omega, \mathcal{F}, \mathbf{P})$ 上的所有平方可积随机变量构成的集合.

---

4.3 方差、协方差和高阶矩

113

定理4.3.1 假设有 $\xi, \eta \in L^2$. 则随机变量 $\xi \eta$ 可积且有

$$
\left[ \mathbf {E} (\xi \eta) \right] ^ {2} \leqslant \mathbf {E} (\xi^ {2}) \mathbf {E} (\eta^ {2}), \tag {4.3.1}
$$

且其中的等号成立当且仅当存在 $t \in \mathbb{R}$ 使 $\eta \stackrel{\mathrm{a.s.}}{=} t\xi$.

证明 考虑 $\mathbb{R}$ 上的二次函数

$$
u (t) := \mathbf {E} [ (t \xi - \eta) ^ {2} ] = \mathbf {E} (\xi^ {2}) t ^ {2} - 2 \mathbf {E} (\xi \eta) t + \mathbf {E} (\eta^ {2}).
$$

由 $u(t) \geqslant 0$ 知 (4.3.1) 式成立, 且等号成立当且仅当方程 $u(t) = 0$ 有唯一实根 $t \in \mathbb{R}$. 此时, 根据定理 4.2.3 有 $\eta \stackrel{\mathrm{a.s.}}{=} t\xi$. □

通常称 (4.3.1) 式为柯西-施瓦茨 (Cauchy-Schwarz) 不等式.

命题 4.3.2 平方可积随机变量集  $L^{2}$  是一个线性空间.

证明 假设 $\xi, \eta \in L^2$. 对任何 $\alpha, \beta \in \mathbb{R}$, 由柯西-施瓦茨不等式有

$$
\begin{array}{l} \mathbf {E} \big [ (\alpha \xi + \beta \eta) ^ {2} \big ] = \alpha^ {2} \mathbf {E} (\xi^ {2}) + 2 \alpha \beta \mathbf {E} (\xi \eta) + \beta^ {2} \mathbf {E} (\eta^ {2}) \\ \leqslant \alpha^ {2} \mathbf {E} (\xi^ {2}) + 2 | \alpha \beta | \left[ \mathbf {E} (\xi^ {2}) \mathbf {E} (\eta^ {2}) \right] ^ {1 / 2} + \beta^ {2} \mathbf {E} (\eta^ {2}) <   \infty . \\ \end{array}
$$

所以  $L^{2}$  是一个线性空间.

定义 4.3.1 对于  $\xi \in L^{2}$  记  $a = E\xi$ . 我们称

$$
\mathbf {V a r} \xi := \mathbf {E} [ (\xi - a) ^ {2} ] = \mathbf {E} (\xi^ {2}) - a ^ {2} = \mathbf {E} (\xi^ {2}) - (\mathbf {E} \xi) ^ {2} \tag {4.3.2}
$$

为 $\xi$ 的方差, 而称 $\sqrt{\mathrm{Var}\xi}$ 为 $\xi$ 的标准差.

粗略地讲, 方差 $\operatorname{Var} \xi$ 给出了随机变量 $\xi$ 与其期望值 $\mathbf{E}\xi$ 之间的偏差大小的一个度量. 由 (4.3.2) 式, 显然 $\operatorname{Var} \xi \geqslant 0$. 由定理 4.2.3 易知 $\operatorname{Var} \xi = 0$ 当且仅当 $(\xi - a)^2 \stackrel{\mathrm{a.s.}}{=} 0$, 而这等价于 $\xi \stackrel{\mathrm{a.s.}}{=} a = \mathbf{E}\xi$. 另外, 显然对任何 $c \in \mathbb{R}$ 有

$$
\mathbf {V a r} (\xi + c) = \mathbf {V a r} \xi , \quad \mathbf {V a r} (c \xi) = c ^ {2} \mathbf {V a r} \xi .
$$

命题 4.3.3 对于  $\xi \in L^{2}$ ，函数  $f(c) = \mathbf{E}[(\xi - c)^{2}]$  当且仅当  $c = E\xi$  时取得最小值 Var $\xi$ .

证明 记 $a = \mathbf{E}\xi$ . 由数学期望的性质, 有

$$
\begin{array}{l} f (c) = \mathbf {E} \big \{[ (\xi - a) - (c - a) ] ^ {2} \big \} \\ = \mathbf {E} [ (\xi - a) ^ {2} ] + (c - a) ^ {2} - 2 \mathbf {E} [ (\xi - a) (c - a) ] \\ = \mathbf {V a r} \xi + (c - a) ^ {2} = \mathbf {V a r} \xi + (c - \mathbf {E} \xi) ^ {2} \geqslant \mathbf {V a r} \xi , \\ \end{array}
$$

其中等号当且仅当  $c = E\xi$  时成立.

---

114

第四章 积分和数学期望

例4.3.1 设随机变量 $\xi$ 服从泊松分布 $P(\lambda)$. 由例4.2.7有 $\mathbf{E}\xi = \lambda$. 再注意

$$
\begin{array}{l} \mathbf {E} (\xi^ {2}) = \sum_ {i = 1} ^ {\infty} \frac {i ^ {2} \lambda^ {i}}{i !} \mathrm{e} ^ {- \lambda} = \lambda \sum_ {i = 1} ^ {\infty} \frac {i \lambda^ {i - 1}}{(i - 1) !} \mathrm{e} ^ {- \lambda} \\ = \lambda \left[ \sum_ {i = 1} ^ {\infty} \frac {\lambda^ {i - 1}}{(i - 1) !} + \lambda \sum_ {i = 2} ^ {\infty} \frac {\lambda^ {i - 2}}{(i - 2) !} \right] e ^ {- \lambda} \\ = \lambda (1 + \lambda). \\ \end{array}
$$

所以  $\mathbf{Var}\xi = \mathbf{E}(\xi^{2}) - (\mathbf{E}\xi)^{2} = \lambda.$

例 4.3.2 设随机变量  $\xi$  服从指数分布  $E(\lambda)$ . 根据例 4.2.9 有  $E\xi = 1/\lambda$ . 再注意

$$
\begin{array}{l} \mathbf {E} (\xi^ {2}) = \int_ {0} ^ {\infty} x ^ {2} \lambda \mathrm{e} ^ {- \lambda x} \mathrm{d} x = - x ^ {2} \mathrm{e} ^ {- \lambda x} | _ {0} ^ {\infty} + 2 \int_ {0} ^ {\infty} x \mathrm{e} ^ {- \lambda x} \mathrm{d} x \\ = - 2 x \mathrm{e} ^ {- \lambda x} \big | _ {0} ^ {\infty} + \frac {2}{\lambda} \int_ {0} ^ {\infty} \mathrm{e} ^ {- \lambda x} \mathrm{d} x = \frac {2}{\lambda^ {2}}. \\ \end{array}
$$

所以 $\mathbf{Var}\xi = \mathbf{E}(\xi^2) - (\mathbf{E}\xi)^2 = 1 / \lambda^2.$

例 4.3.3 设随机变量  $\xi$  服从正态分布  $N(a,\sigma^{2})$ . 由例 4.2.10 有  $E\xi = a$ . 所以

$$
\begin{array}{l} \mathrm{Var} \xi = \frac {1}{\sqrt {2 \pi} \sigma} \int_ {- \infty} ^ {\infty} (x - a) ^ {2} \mathrm{e} ^ {- \frac {(x - a) ^ {2}}{2 \sigma^ {2}}} \mathrm{d} x \\ = \frac {\sigma^ {2}}{\sqrt {2 \pi}} \int_ {- \infty} ^ {\infty} u ^ {2} \mathrm{e} ^ {- \frac {u ^ {2}}{2}} \mathrm{d} u \\ = \frac {\sigma^ {2}}{\sqrt {2 \pi}} \Big (- u \mathrm{e} ^ {- \frac {u ^ {2}}{2}} \Big | _ {- \infty} ^ {\infty} + \int_ {- \infty} ^ {\infty} \mathrm{e} ^ {- \frac {u ^ {2}}{2}} \mathrm{d} u \Big) = \sigma^ {2}. \\ \end{array}
$$

## 4.3.2 协方差和协方差矩阵

定义 4.3.2 给定随机变量  $\xi, \eta \in L^{2}$ ，我们称

$$
\mathbf {C o v} (\xi , \eta) := \mathbf {E} [ (\xi - \mathbf {E} \xi) (\eta - \mathbf {E} \eta) ] = \mathbf {E} (\xi \eta) - \mathbf {E} \xi \mathbf {E} \eta \tag {4.3.3}
$$

为  $\xi$  与  $\eta$  的协方差.

由 (4.3.3) 式可以看出, 粗略地讲, 若 $\mathbf{Cov}(\xi, \eta) > 0$, 则随机变量 $\xi - \mathbf{E}\xi$ 和 $\eta - \mathbf{E}\eta$ 倾向于取同号. 反之, 若 $\mathbf{Cov}(\xi, \eta) < 0$, 则随机变量 $\xi - \mathbf{E}\xi$ 和 $\eta - \mathbf{E}\eta$ 倾向于取异号.

命题 4.3.4 令  $\xi,\eta,\zeta\in L^{2}$ . 下面的性质成立:

(1) (对称性)  $\mathbf{Cov}(\xi,\eta)=\mathbf{Cov}(\eta,\xi);$
(2) (双线性性) 对任意的 $a, b \in \mathbb{R}$;

$$
\mathbf {C o v} (a \xi + b \eta , \zeta) = a \mathbf {C o v} (\xi , \zeta) + b \mathbf {C o v} (\eta , \zeta),
$$

---

4.3 方差、协方差和高阶矩

115

$$
\mathbf {C o v} (\xi , a \eta + b \zeta) = a \mathbf {C o v} (\xi , \eta) + b \mathbf {C o v} (\xi , \zeta);
$$

(3) $\mathbf{Var}(\xi + \eta) = \mathbf{Var}\xi + \mathbf{Var}\eta + 2\mathbf{Cov}(\xi, \eta)$.

证明 显然 (1), (2) 成立. 记 $a = \mathbf{E}\xi$ 和 $b = \mathbf{E}\eta$. 则有

$$
\begin{array}{l} \mathbf {V a r} (\xi + \eta) = \mathbf {E} \left\{\left[ (\xi + \eta) - (a + b) \right] ^ {2} \right\} \\ = \mathbf {E} \left\{\left[ (\xi - a) + (\eta - b) \right] ^ {2} \right\} \\ = \mathbf {E} [ (\xi - a) ^ {2} ] + \mathbf {E} [ (\eta - b) ^ {2} ] + 2 \mathbf {E} [ (\xi - a) (\eta - b) ], \\ \end{array}
$$

即 (3) 成立.

定义 4.3.3 给定随机变量  $\xi_{1}, \xi_{2}, \cdots, \xi_{n} \in L^{2}$ ，我们称

$$
B = (b (i, j)) _ {1 \leqslant i, j \leqslant n} := (\mathbf {C o v} (\xi_ {i}, \xi_ {j})) _ {1 \leqslant i, j \leqslant n}
$$

为随机向量  $\xi := (\xi_{1}, \xi_{2}, \cdots, \xi_{n})$  的协方差矩阵, 并记作  $B = \mathbf{Var}(\xi)$ .

定理 4.3.5 对于  $\xi_{1}, \xi_{2}, \cdots, \xi_{n} \in L^{2}$ ，随机向量  $(\xi_{1}, \xi_{2}, \cdots, \xi_{n})$  的协方差矩阵 B 为半正定对称矩阵.

证明 根据命题 4.3.4 (1) 知 $B$ 为对称矩阵. 对于 $x \in \mathbb{R}^n$, 我们有

$$
\begin{array}{l} \sum_ {i, j} x _ {i} x _ {j} \mathbf {C o v} (\xi_ {i}, \xi_ {j}) = \sum_ {i, j} x _ {i} x _ {j} \mathbf {E} [ (\xi_ {i} - \mathbf {E} \xi_ {i}) (\xi_ {j} - \mathbf {E} \xi_ {j}) ] \\ = \mathbf {E} \Big [ \sum_ {i, j} x _ {i} x _ {j} (\xi_ {i} - \mathbf {E} \xi_ {i}) (\xi_ {j} - \mathbf {E} \xi_ {j}) \Big ] \\ = \mathbf {E} \left\{\left[ \sum_ {i = 1} ^ {n} x _ {i} (\xi_ {i} - \mathbf {E} \xi_ {i}) \right] ^ {2} \right\} \geqslant 0. \\ \end{array}
$$

即 B 为半正定矩阵.

定义 4.3.4 若随机变量  $\xi, \eta \in L^{2}$  满足  $\mathbf{Cov}(\xi, \eta) = 0$ ，则称它们是不相关的.

由定义 4.3.2 和命题 4.3.4 不难得到:

命题 4.3.6 对于  $\xi, \eta \in L^{2}$  下面的性质相互等价:

(1) $\xi, \eta$ 不相关;
(2)  $\mathbf{E}(\xi\eta)=\mathbf{E}\xi\mathbf{E}\eta;$

(3) $\mathbf{Var}(\xi + \eta) = \mathbf{Var}\xi + \mathbf{Var}\eta$.

命题 4.3.7 若  $\xi, \eta \in L^{2}$  相互独立, 则它们不相关.

例 4.3.4 已知  $\theta$  服从分布  $U(-\pi, \pi)$ . 令  $\xi = \sin\theta, \eta = \cos\theta$ . 证明  $\xi, \eta$  不相关且不独立.

证明 此时, 显然有 $\mathbf{E}\xi = \mathbf{E}\eta = 0$. 而因为 $\sin x\cos x$ 是奇函数, 所以

$$
\mathbf {E} (\xi \eta) = \frac {1}{2 \pi} \int_ {- \pi} ^ {\pi} \sin x \cos x \mathrm{d} x = 0.
$$

---

116

第四章 积分和数学期望

因此 $\xi, \eta$ 不相关. 注意

$$
\mathbf {P} (0 <   \xi <   1 / 2) = \mathbf {P} (\{0 <   \theta <   \pi / 6 \} \cup \{5 \pi / 6 <   \theta <   \pi \}) = 1 / 6,
$$

$$
\mathbf {P} (0 <   \eta <   1 / 2) = \mathbf {P} (\{- \pi / 2 <   \theta <   - \pi / 3 \} \cup \{\pi / 3 <   \theta <   \pi / 2 \}) = 1 / 6.
$$

另外，

$$
\mathbf {P} (0 <   \xi <   1 / 2, 0 <   \eta <   1 / 2) = \mathbf {P} (\varnothing) = 0.
$$

所以  $\xi,\eta$  不独立.

例4.3.5 设 $\xi$ 服从伯努利分布 $B(1,p)$. 则有 $\mathbf{E}\xi = p$ 和

$$
\mathbf {V a r} \xi = \mathbf {E} [ (\xi - p) ^ {2} ] = (1 - p) ^ {2} p + p ^ {2} (1 - p) = p (1 - p).
$$

例 4.3.6 设  $\xi$  服从二项分布  $B(n,p)$ . 则  $\xi \stackrel{d}{=} \xi_{1} + \xi_{2} + \cdots + \xi_{n}$ ，其中  $\xi_{1}, \xi_{2}, \cdots, \xi_{n}$  相互独立且服从伯努利分布  $B(1,p)$ . 所以有 E\xi = np 和 Var\x = np(1 - p).

## 4.3.3 相关系数

根据之前定义的概念, 随机变量 $\xi$ 是退化的, 是指存在常数 $a$ 使得 $\mathbf{P}(\xi = a) = 1$. 否则 $\xi$ 就是非退化的. 显然 $\xi \in L^2$ 非退化当且仅当 $\operatorname{Var}\xi > 0$.

定义 4.3.5 对于非退化的随机变量  $\xi \in L^{2}$ ，我们定义其标准化随机变量

$$
\xi^ {*} := \frac {\xi - \mathbf {E} \xi}{\sqrt {\mathbf {V a r} \xi}}.
$$

注意  $\mathbf{E}(\xi^{*})=0$  而  $\mathbf{Var}(\xi^{*})=1$ .

定义 4.3.6 假设随机变量  $\xi, \eta \in L^{2}$  非退化. 我们称

$$
r := \mathbf {E} (\xi^ {*} \eta^ {*}) = \mathbf {C o v} (\xi^ {*}, \eta^ {*}) = \frac {\mathbf {C o v} (\xi , \eta)}{\sqrt {\mathbf {V a r} \xi \cdot \sqrt {\mathbf {V a r} \eta}}}
$$

为  $\xi$  和  $\eta$  的相关系数.

显然, 当 $r = 0$ 时 $\xi$ 与 $\eta$ 不相关. 在一般情况下, 相关系数 $r$ 体现了 $\xi$ 和 $\eta$ 相互关联或影响的程度.

定理4.3.8 假设 $\xi, \eta \in L^2$ 非退化. 则有 $|r| \leqslant 1$ 且

(1) $r = 1 \Leftrightarrow \xi^{*} \stackrel{\text{a.s.}}{=} \eta^{*}$; (2) $r = -1 \Leftrightarrow \eta^{*} \stackrel{\text{a.s.}}{=} -\xi^{*}$.

证明 根据柯西-施瓦茨不等式, 有

$$
| r | = | \mathbf {E} (\xi^ {*} \eta^ {*}) | \leqslant \left\{\mathbf {E} [ (\xi^ {*}) ^ {2} ] \mathbf {E} [ (\eta^ {*}) ^ {2} ] \right\} ^ {1 / 2} = \sqrt {\mathbf {V a r} (\xi^ {*}) \mathbf {V a r} (\eta^ {*})} = 1,
$$

且等号成立当且仅当有 $t \in \mathbb{R}$ 使得 $\eta^{*} = t\xi^{*}$. 此时, 由上式得

$$
1 = | r | = | \mathbf {E} (\xi^ {*} \eta^ {*}) | = | t | \mathbf {E} [ (\xi^ {*}) ^ {2} ] = | t |.
$$

[Unreadable]

---

4.3 方差、协方差和高阶矩

117

进而易知结论成立.

推论4.3.9 假设 $\xi$ 和 $\eta \in L^2$ 非退化. 若 $|r| = 1$, 则存在常数 $a, b$, 使 $\eta \stackrel{\mathrm{a.s.}}{=} a + b\xi$ 且 $rb > 0$.

证明 先考虑 $r = 1$ 的情况. 此时, 由定理4.3.8有 $\eta^{*} \stackrel{\mathrm{a.s.}}{=} \xi^{*}$, 即

$$
\frac {\xi - \mathbf {E} \xi}{\sqrt {\mathbf {V a r} \xi}} = \frac {\eta - \mathbf {E} \eta}{\sqrt {\mathbf {V a r} \eta}},
$$

从而 (a.s.)

$$
\eta = \mathbf {E} \eta + \frac {\sqrt {\mathbf {V a r} \eta}}{\sqrt {\mathbf {V a r} \xi}} (\xi - \mathbf {E} \xi) = a + b \xi ,
$$

其中

$$
a = \mathbf {E} \eta - \frac {\sqrt {\mathbf {V a r} \eta}}{\sqrt {\mathbf {V a r} \xi}} \mathbf {E} \xi , \quad b = \frac {\sqrt {\mathbf {V a r} \eta}}{\sqrt {\mathbf {V a r} \xi}} > 0.
$$

当 r = -1 时, 证明类似.

例 4.3.7 设随机向量  $(\xi,\eta)$  服从二维正态分布  $N(a_{1},a_{2};\sigma_{1}^{2},\sigma_{2}^{2};r)$ . 证明  $\xi,\eta$  有协方差  $r\sigma_{1}\sigma_{2}$  和相关系数 r.

证明 根据假设, 随机向量  $(\xi, \eta)$  的联合分布密度为

$$
\begin{array}{l} p (x, y) = \frac {1}{2 \pi \sigma_ {1} \sigma_ {2} \sqrt {1 - r ^ {2}}} \exp \left\{- \frac {1}{2 (1 - r ^ {2})} \left[ \frac {(x - a _ {1}) ^ {2}}{\sigma_ {1} ^ {2}} - \right. \right. \\ \left. 2 r \frac {(x - a _ {1}) (y - a _ {2})}{\sigma_ {1} \sigma_ {2}} + \frac {(y - a _ {2}) ^ {2}}{\sigma_ {2} ^ {2}} \right] \Bigg \}. \\ \end{array}
$$

所以

$$
\begin{array}{l} \mathbf {C o v} (\xi , \eta) = \int_ {- \infty} ^ {\infty} \int_ {- \infty} ^ {\infty} (x - a _ {1}) (y - a _ {2}) p (x, y) \mathrm{d} x \mathrm{d} y \\ = \frac {\sigma_ {1} \sigma_ {2}}{2 \pi \sqrt {1 - r ^ {2}}} \int_ {- \infty} ^ {\infty} \int_ {- \infty} ^ {\infty} u v \mathrm{e} ^ {- \frac {u ^ {2} - 2 r u v + v ^ {2}}{2 (1 - r ^ {2})}} \mathrm{d} u \mathrm{d} v, \\ \end{array}
$$

其中

$$
u = \frac {x - a _ {1}}{\sigma_ {1}}, v = \frac {y - a _ {2}}{\sigma_ {2}}.
$$

再作变量替换

$$
\left\{ \begin{array}{l l} u = \sqrt {1 - r ^ {2}} s + r t, \\ v = t, \end{array} \right.
$$

相应的雅可比行列式为

$$
J = \left| \begin{array}{c c} \sqrt {1 - r ^ {2}} & r \\ 0 & 1 \end{array} \right| = \sqrt {1 - r ^ {2}}.
$$

---

118

第四章 积分和数学期望

继续上面的运算，

$$
\begin{array}{l} \mathbf {C o v} (\xi , \eta) = \frac {\sigma_ {1} \sigma_ {2}}{2 \pi} \int_ {- \infty} ^ {\infty} \int_ {- \infty} ^ {\infty} \left(\sqrt {1 - r ^ {2}} s + r t\right) t \mathrm{e} ^ {- \frac {s ^ {2} + t ^ {2}}{2}} \mathrm{d} s \mathrm{d} t \\ = \frac {\sigma_ {1} \sigma_ {2} r}{2 \pi} \int_ {- \infty} ^ {\infty} \int_ {- \infty} ^ {\infty} \mathrm{e} ^ {- \frac {s ^ {2}}{2}} t ^ {2} \mathrm{e} ^ {- \frac {t ^ {2}}{2}} \mathrm{d} s \mathrm{d} t \\ = \frac {\sigma_ {1} \sigma_ {2} r}{2 \pi} \int_ {- \infty} ^ {\infty} \mathrm{e} ^ {- \frac {s ^ {2}}{2}} \mathrm{d} s \int_ {- \infty} ^ {\infty} t ^ {2} \mathrm{e} ^ {- \frac {t ^ {2}}{2}} \mathrm{d} t = r \sigma_ {1} \sigma_ {2}. \\ \end{array}
$$

所以  $\xi,\eta$  有协方差  $r\sigma_{1}\sigma_{2}$ ，从而它们有相关系数 r.

例4.3.8 设 $(\xi, \eta)$ 服从二维正态分布 $N(a_{1}, a_{2}; \sigma_{1}^{2}, \sigma_{2}^{2}; r)$. 显然 $\mathbf{Cov}(\xi, \eta) = 0$ 当且仅当 $r = 0$. 而此时有

$$
p (x, y) = \frac {1}{2 \pi \sigma_ {1} \sigma_ {2}} \exp \bigg \{- \left[ \frac {(x - a _ {1}) ^ {2}}{\sigma_ {1} ^ {2}} + \frac {(y - a _ {2}) ^ {2}}{\sigma_ {2} ^ {2}} \right] \bigg \},
$$

故 $\xi, \eta$ 独立. 再根据定理3.2.4知 $\xi, \eta$ 独立当且仅当它们不相关.

## 4.3.4 原点矩和中心矩

随机变量的矩是反映其性质的重要数字特征, 前面讨论的数学期望和方差分别属于一阶矩和二阶矩. 本小节对于随机变量的一般的矩进行简单的讨论. 令 $r > 0$. 若概率空间 $(\Omega, \mathcal{F}, \mathbf{P})$ 上的随机变量 $\xi$ 满足 $\mathbf{E}(|\xi|^r) < \infty$, 我们写 $\xi \in L^r$.

定义 4.3.7 对整数 $k \geqslant 1$, 我们称 $m_k := \mathbf{E}(\xi^k)$ 为 $\xi \in L^k$ 的 $k$ 阶原点矩, 而称 $c_k := \mathbf{E}[(\xi - \mathbf{E}\xi)^k]$ 为 $\xi \in L^k$ 的 $k$ 阶中心矩.

利用数学期望的计算公式不难证明:

命题 4.3.10 当  $\mathbf{E}(|\xi|^{k})<\infty$  时, 有

$$
c _ {k} = \sum_ {i = 0} ^ {k} \mathrm{C} _ {k} ^ {i} (- m _ {1}) ^ {k - i} m _ {i}, \qquad m _ {k} = \sum_ {i = 0} ^ {k} \mathrm{C} _ {k} ^ {i} c _ {k - i} m _ {1} ^ {i}.
$$

例 4.3.9 (正态分布随机变量的各阶矩) 设  $\xi$  服从分布  $N(0,1)$ . 则

$$
\int_ {- \infty} ^ {\infty} | x | ^ {n} \frac {1}{\sqrt {2 \pi}} \mathrm{e} ^ {- \frac {x ^ {2}}{2}} \mathrm{d} x <   \infty .
$$

当 $n = 2k - 1$ 为奇数时，显然有 $m_{2k - 1} = 0$ 当 $n = 2k$ 为偶数时，有

$$
\begin{array}{l} m _ {2 k} = \int_ {- \infty} ^ {\infty} | x | ^ {2 k} \frac {1}{\sqrt {2 \pi}} \mathrm{e} ^ {- \frac {x ^ {2}}{2}} \mathrm{d} x = \sqrt {\frac {2}{\pi}} \int_ {0} ^ {\infty} x ^ {2 k} \mathrm{e} ^ {- \frac {x ^ {2}}{2}} \mathrm{d} x \quad (x = \sqrt {2 t}) \\ = \frac {2 ^ {k}}{\sqrt {\pi}} \int_ {0} ^ {\infty} t ^ {k - \frac {1}{2}} \mathrm{e} ^ {- t} \mathrm{d} t = \frac {2 ^ {k}}{\sqrt {\pi}} \Gamma \left(k + \frac {1}{2}\right). \\ \end{array}
$$

---

4.3 方差、协方差和高阶矩

119

由熟知的结果,

$$
\Gamma (\alpha + 1) = \alpha \Gamma (\alpha), \quad \Gamma \Big (\frac {1}{2} \Big) = \sqrt {\pi},
$$

故有

$$
m _ {2 k} = \frac {2 ^ {k}}{\sqrt {\pi}} \left(k - \frac {1}{2}\right) \left(k - \frac {3}{2}\right) \dots \frac {1}{2} \cdot \Gamma \left(\frac {1}{2}\right) = (2 k - 1)!!,
$$

再利用命题 4.3.10 给出的关系即可得到  $\xi$  的所有中心矩.

下面定理的结论称为赫尔德 (Hölder) 不等式, 它是前面证明的柯西-施瓦茨不等式的自然推广.

定理4.3.11 假设 $p, q > 1$ 满足 $1 / p + 1 / q = 1$. 若有 $\xi \in L^p$ 和 $\eta \in L^q$, 则有 $\xi \eta \in L^1$ 且

$$
\mathbf {E} (| \xi \eta |) \leqslant \left[ \mathbf {E} (| \xi | ^ {p}) \right] ^ {1 / p} \left[ \mathbf {E} (| \eta | ^ {q}) \right] ^ {1 / q}.
$$

证明 当 $\mathbf{E}(|\xi \eta|) = 0$ 时, 欲证不等式显然成立. 下面假设 $\mathbf{E}(|\xi \eta|) > 0$, 因而有 $\mathbf{E}(|\xi|) > 0$ 和 $\mathbf{E}(|\eta|) > 0$. 根据对数函数的凹性, 对 $x, y > 0$ 有

$$
\frac {1}{p} \ln x + \frac {1}{q} \ln y \leqslant \ln \left(\frac {x}{p} + \frac {y}{q}\right).
$$

因此易知, 对任何 $x, y \geqslant 0$ 有

$$
x ^ {1 / p} y ^ {1 / q} \leqslant \frac {x}{p} + \frac {y}{q}.
$$

在上式中令 $x = |\xi|^p / \mathbf{E}(|\xi|^p)$ 和 $y = |\eta|^q / \mathbf{E}(|\eta|^q)$，再对所得不等式取期望即得欲证结论. □

推论 4.3.12 对任何随机变量 X, 函数  $r \mapsto [\mathbf{E}(|X|^{r})]^{1/r}$  在  $(0, \infty)$  上不降.

证明 取 $r > q > 0$ 并注意 $q / r + (r - q) / r = 1$. 对 $\xi = |X|^q$ 和 $\eta = 1$ 应用定理4.3.11即知 $[\mathbf{E}(|X|^q)]^{1 / q} \leqslant [\mathbf{E}(|X|^r)]^{1 / r}$.

## 练习题

1. 袋子里有编号为 1 至 $n$ 的卡片 $n$ 张. 从中随机抽取 $k$ 张. 针对以下两种情形求 $k$ 张卡片编号之和 $\xi$ 的期望和方差: (1) 有放回抽取; (2) 无放回抽取 $(m \leqslant n)$.

2. 设绝对连续型平方可积随机变量 $X$ 的密度函数为 $\mathbb{R}$ 上的偶函数. 证明 $X$ 与 $|X|$ 不相关但不独立.

3. 设  $(X,Y)$  的密度函数为

$$
p (x, y) = \left\{ \begin{array}{l l} 1, & 0 <   x <   1, | y | <   x <   1, \\ 0, & \text {其他.} \end{array} \right.
$$

---

120

第四章 积分和数学期望

求 $(X,Y)$ 的协方差矩阵.

4. 设随机变量  $\xi_{1}, \xi_{2}, \cdots, \xi_{m+n} (n \geqslant m \geqslant 1)$  是独立同分布随机变量, 且有有限的方差  $\sigma^{2}$ . 求  $X = \xi_{1} + \xi_{2} + \cdots + \xi_{n}$  与  $Y = \xi_{m+1} + \xi_{m+2} + \cdots + \xi_{m+n}$  的协方差和相关系数.

5. 设随机变量 $\xi$ 服从指数分布 $E(\lambda)$. 证明对 $n \geqslant 0$ 有 $\mathbf{E}(\xi^n) = n! / \lambda^n$.

## 4.4 条件期望和预测

## 4.4.1 条件期望的定义和计算

考虑概率空间 $(\Omega, \mathcal{F}, \mathbf{P})$，设事件 $B \in \mathcal{F}$ 满足 $\mathbf{P}(B) > 0$。我们知道，给定事件 $B$ 的条件概率测度 $\mathbf{P}_B := \mathbf{P}(\cdot | B)$ 定义为

$$
\mathbf {P} _ {B} (A) = \mathbf {P} (A | B) = \frac {\mathbf {P} (A B)}{\mathbf {P} (B)}, \quad A \in \mathcal {F}. \tag {4.4.1}
$$

注意 $(\Omega, \mathcal{F}, \mathbf{P}_B)$ 构成一个概率空间, 而原概率空间上的随机变量 $\xi$ 也可视为 $(\Omega, \mathcal{F}, \mathbf{P}_B)$ 上的随机变量.

定义 4.4.1 随机变量  $\xi$  在概率空间  $(\Omega, \mathcal{F}, \mathbf{P}_{B})$  上的数学期望称为它的给定事件 B 的条件期望，并记作  $\mathbf{E}(\xi|B)$ .

显然有 $\mathbf{P}_B(B) = 1$ 和 $\mathbf{P}_B(B^c) = 0$. 我们用 $F_{\xi}(\cdot |B)$ 表示 $\xi$ 作为 $(\Omega, \mathcal{F}, \mathbf{P}_B)$ 上的随机变量的分布函数. 给定 $\mathbb{R}$ 上的博雷尔可测函数, 根据定理4.2.7有

$$
\mathbf {E} [ f (\xi) | B ] = \int_ {- \infty} ^ {\infty} f (x) \mathrm{d} F _ {\xi} (x | B). \tag {4.4.2}
$$

特别地, 若  $\xi$  为取值于可数集  $\{x_{1}, x_{2}, \cdots\} \subseteq R$  的离散型随机变量, 应用命题 4.2.6 得

$$
\mathbf {E} [ f (\xi) | B ] = \sum_ {i = 1} ^ {\infty} f (x _ {i}) \mathbf {P} (\xi = x _ {i} | B). \tag {4.4.3}
$$

定理 4.4.1 设  $(\xi,\eta)$  为取值于  $\{(x_{i},y_{j}):i,j=1,2,\cdots\}$  的离散型随机向量，且有联合分布列

$$
p (x _ {i}, y _ {j}) = \mathbf {P} (\xi = x _ {i}, \eta = y _ {j}), \quad i, j = 1, 2, \dots
$$

及边缘分布列

$$
p _ {\xi} (x _ {i}) = \mathbf {P} (\xi = x _ {i}), p _ {\eta} (y _ {j}) = \mathbf {P} (\eta = y _ {j}), i, j = 1, 2, \dots .
$$

---

4.4 条件期望和预测

121

再设 $p_{\eta}(y_j) = \mathbf{P}(\eta = y_j) > 0.$ 则对 $\mathbb{R}^2$ 上的函数 $f$ 有

$$
\mathbf {E} [ f (\xi , \eta) | \eta = y _ {j} ] = \sum_ {i = 1} ^ {\infty} f (x _ {i}, y _ {j}) p _ {\xi} (x _ {i} | \eta = y _ {j}), \tag {4.4.4}
$$

其中 $p_{\xi}(x_i|\eta = y_j) = p(x_i,y_j) / p_\eta (y_j)$ 为条件分布列.

证明 注意, 在条件概率 $\mathbf{P}(\cdot|\eta = y_j)$ 之下有 $f(\xi, \eta) \stackrel{\mathrm{a.s.}}{=} f(\xi, y_j)$. 对于事件 $B = \{\eta = y_j\}$ 和随机变量 $f(\xi, y_j)$ 应用 (4.4.3) 式即得 (4.4.4) 式. □

如果 $\mathbf{P}(B) = 0$ ，我们不能用(4.4.2)式确定相应的条件期望.但是，对于绝对连续型随机向量，类比定理4.4.1的结果，可以借助条件分布密度给出如下的:

定义4.4.2 设 $(\xi, \eta)$ 为绝对连续型随机向量, 且有联合分布密度 $p$ 及边缘分布密度 $p_{\xi}$ 和 $p_{\eta}$. 再设 $p_{\eta}(y) > 0$. 对于 $\mathbb{R}^2$ 上的可测函数 $f$ 我们定义给定 $\eta = y$ 时 $f(\xi, \eta)$ 的条件期望为

$$
\mathbf {E} [ f (\xi , \eta) | \eta = y ] = \int_ {- \infty} ^ {\infty} f (x, y) p _ {\xi} (x | \eta = y) \mathrm{d} x, \tag {4.4.5}
$$

其中 $p_{\xi}(x|\eta = y) = p(x,y) / p_{\eta}(y)$ 为条件分布密度.

定义 4.4.3 对于离散型或绝对连续型随机变向量  $(\xi,\eta)$ ，若  $p_{\eta}(y)>0$ ，我们称

$$
\mathbf {V a r} (\xi | \eta = y) := \mathbf {E} \big \{[ \xi - \mathbf {E} (\xi | \eta = y) ] ^ {2} | \eta = y \big \}
$$

为给定  $\eta = y$  时  $\xi$  的条件方差.

例 4.4.1 设随机向量  $(\xi, \eta)$  服从单位圆盘上的二维均匀分布. 根据例 3.2.1, 对于  $|y| < 1$  有

$$
p _ {\xi} (x | \eta = y) = \frac {1}{2 \sqrt {1 - y ^ {2}}}, \quad | x | <   \sqrt {1 - y ^ {2}}.
$$

故有

$$
\mathbf {E} (\xi | \eta = y) = \int_ {- \sqrt {1 - y ^ {2}}} ^ {\sqrt {1 - y ^ {2}}} \frac {x \mathrm{d} x}{2 \sqrt {1 - y ^ {2}}} = 0
$$

和

$$
\mathbf {V a r} (\xi | \eta = y) = \mathbf {E} (\xi^ {2} | \eta = y) = \int_ {- \sqrt {1 - y ^ {2}}} ^ {\sqrt {1 - y ^ {2}}} \frac {x ^ {2} \mathrm{d} x}{2 \sqrt {1 - y ^ {2}}} = \frac {1 - y ^ {2}}{3}.
$$

例4.4.2 设 $(\xi, \eta)$ 服从二维正态分布 $N(a_{1}, a_{2}; \sigma_{1}^{2}, \sigma_{2}^{2}; r)$. 根据例3.2.2, 给定 $\eta = y$ 时 $\xi$ 服从条件分布

$$
N (a _ {1} + r \sigma_ {1} (y - a _ {2}) / \sigma_ {2}, \sigma_ {1} ^ {2} (1 - r ^ {2})).
$$

---

122

第四章 积分和数学期望

据此立知

$$
\mathbf {E} (\xi | \eta = y) = a _ {1} + r \sigma_ {1} (y - a _ {2}) / \sigma_ {2}
$$

和

$$
\mathbf {V a r} (\xi | \eta = y) = \sigma_ {1} ^ {2} (1 - r ^ {2}).
$$

## 4.4.2 全期望公式及应用

定理4.4.2（全期望公式） 假定数学期望 $\mathbf{E}f(\xi)$ 存在. 则对 $\Omega$ 的可数划分 $\{B_n\} \subseteq \mathcal{F}$ 有

$$
\mathbf {E} f (\xi) = \sum_ {n = 1} ^ {\infty} \mathbf {P} (B _ {n}) \mathbf {E} [ f (\xi) | B _ {n} ]. \tag {4.4.6}
$$

证明 根据全概率公式, 对于任何 $x \in \mathbb{R}$ 有

$$
F _ {\xi} (x) = \sum_ {n = 1} ^ {\infty} \mathbf {P} (B _ {n}) F _ {\xi} (x | B _ {n}).
$$

根据斯蒂尔切斯积分的性质不难证明

$$
\int_ {- \infty} ^ {\infty} f (x) \mathrm{d} F _ {\xi} (x) = \sum_ {n = 1} ^ {\infty} \mathbf {P} (B _ {n}) \int_ {- \infty} ^ {\infty} f (x) \mathrm{d} F _ {\xi} (x | B _ {n}).
$$

该等式意味着只要等号一边正、负部之一有限则另一边也如此且两边相等.所以等式(4.4.6)式成立. □

与全概率公式类似, 当 $\mathbf{P}(B_i) = 0$ 时我们规定 $\mathbf{P}(B_i)\mathbf{E}[f(\xi)|B_i] = 0$, 故在全期望公式 (4.4.6) 式中并不需假定 $\mathbf{P}(B_i) > 0$. 全期望公式经常被用来计算形如 $\mathbf{E}f(\xi)$ 的数学期望. 下面是一个典型的例子.

例 4.4.3 设  $\{\xi_{i}\}$  为独立同分布可积随机变量序列, 而  $\eta$  为与  $\{\xi_{i}\}$  独立的非负整数值可积随机变量. 则有 (规定  $\sum_{i=1}^{0}=0$ )

$$
\mathbf {E} \left(\sum_ {i = 1} ^ {\eta} \xi_ {i}\right) = \mathbf {E} \eta \mathbf {E} \xi_ {1}. \tag {4.4.7}
$$

事实上, 因为 $\eta$ 与 $\{\xi_i\}$ 独立, 在给定 $B_k := \{\eta = k\}$ 的条件下 $\{\xi_i\}$ 仍为独立同分布随机变量序列, 且分布保持不变 (请读者自行证明). 故对于 $k \geqslant 0$ 有

$$
\mathbf {E} \left(\sum_ {i = 1} ^ {\eta} \xi_ {i} \Big | \eta = k\right) = \mathbf {E} \left(\sum_ {i = 1} ^ {k} \xi_ {i} \Big | \eta = k\right) = \mathbf {E} \left(\sum_ {i = 1} ^ {k} \xi_ {i}\right) = k \mathbf {E} \xi_ {1}.
$$

---

4.4 条件期望和预测

123

再由全期望公式得

$$
\begin{array}{l} \mathbf {E} \left(\sum_ {i = 1} ^ {\eta} \xi_ {i}\right) = \sum_ {k = 0} ^ {\infty} \mathbf {P} (\eta = k) \mathbf {E} \left(\sum_ {i = 1} ^ {\eta} \xi_ {i} \Big | \eta = k\right) \\ = \sum_ {k = 1} ^ {\infty} \mathbf {P} (\eta = k) k \mathbf {E} \xi_ {1} = \mathbf {E} \eta \mathbf {E} \xi_ {1}. \\ \end{array}
$$

## 4.4.3 给定随机变量的条件期望

定义 4.4.4 设  $(\xi,\eta)$  是具有联合分布密度 p 的离散型或绝对连续型随机向量. 分别用  $p_{\xi}$  和  $p_{\eta}$  表示  $\xi$  和  $\eta$  的边缘分布密度, 并记

$$
U = \{x \in \mathbb {R}: p _ {\xi} (x) > 0 \}, \quad V = \{y \in \mathbb {R}: p _ {\eta} (y) > 0 \}. \tag {4.4.8}
$$

注意, 在离散或绝对连续两种情况下都有 $\mathbf{P}(\xi \in U) = 1$ 和 $\mathbf{P}(\eta \in V) = 1$. 给定 $\mathbb{R}^2$ 上的可测函数 $f$, 令

$$
h (y) = 1 _ {V} (y) \mathbf {E} [ f (\xi , \eta) | \eta = y ] = 1 _ {V} (y) \mathbf {E} [ f (\xi , y) | \eta = y ], \tag {4.4.9}
$$

其中的条件期望由(4.4.4)式或(4.4.5)式定义. 我们称 $h(\eta)$ 为给定 $\eta$ 时随机变量 $f(\xi, \eta)$ 的条件期望, 并记作 $\mathbf{E}[f(\xi, \eta)|\eta]$. 类似地, 可以定义 $\mathbf{E}[f(\xi, \eta)|\xi]$.

可以证明, 由 (4.4.9) 式定义的 $h$ 是 $\mathbb{R}$ 上的可测函数, 故 $\mathbf{E}[f(\xi, \eta)|\eta]$ 是关于 $\sigma$ 代数 $\sigma(\eta)$ 可测的随机变量. 类似地可知 $\mathbf{E}[f(\xi, \eta)|\xi]$ 是关于 $\sigma$ 代数 $\sigma(\xi)$ 可测的随机变量.

例 4.4.4 设  $\eta$  服从泊松分布  $P(\lambda)$ ，而  $\xi$  是成功概率为 p (0 < p < 1) 的  $\eta$  重伯努利试验的成功次数。于是在给定  $\eta$  的条件下  $\xi$  服从二项分布  $B(\eta, p)$ 。因此有  $\mathbf{E}(\xi | \eta) = \eta p$  和

$$
\mathbf {E} \xi = \mathbf {E} (\eta p) = p \mathbf {E} \eta = p \lambda .
$$

上式可认为是例 4.4.3 中结果的特殊情况.

例 4.4.5 设  $(\xi,\eta)$  是概率空间  $(\Omega,\mathcal{F},\mathbf{P})$  上的取值于  $\{(x_{i},y_{j}):i,j=1,2,\cdots\}$  的离散型随机向量. 令 V 由 (4.4.8) 式定义. 不妨设  $V=\{y_{j}:j=1,2,\cdots\}$ . 注意  $\eta$  所生成的  $\sigma$  代数  $\sigma(\eta)$  是形如  $B_{j}=\{\eta=y_{j}\}\in\mathcal{F}, j=1,2,\cdots$  的事件的所有可能的并集构成的集类 (规定零个集合的并为空集). 设对每个  $y_{j}\in V$ , 在给定  $\eta=y_{j}$  条件下  $\xi$  可积, 并记

$$
h (y _ {j}) = 1 _ {V} (y _ {j}) \mathbf {E} (\xi | \eta = y _ {j}) = 1 _ {V} (y _ {j}) \mathbf {E} (\xi | B _ {j}).
$$

若 $\omega \in B_{j}$ ，则 $\eta (\omega) = y_{j}$ ，因而

$$
\mathbf {E} (\xi | \eta) (\omega) = h (\eta (\omega)) = h (y _ {j}) = \mathbf {E} (\xi | \eta = y _ {j}) = \mathbf {E} (\xi | B _ {j}).
$$

---

124

第四章 积分和数学期望

所以有

$$
\mathbf {E} (\xi | \eta) = \sum_ {j = 1} ^ {\infty} 1 _ {\{\eta = y _ {j} \}} \mathbf {E} (\xi | \eta = y _ {j}) = \sum_ {j = 1} ^ {\infty} 1 _ {B _ {j}} \mathbf {E} (\xi | B _ {j}).
$$

这说明随机变量 $\mathbf{E}(\xi|\eta)$ 至多取可数个不同的值, 且在事件 $B_{j} = \{\eta = y_{j}\} \in \mathcal{F}$ 上的取值为 $\mathbf{E}(\xi|B_{j}) = \mathbf{E}(\xi|\eta = y_{j})$, 而后者为经典意义下的条件期望.

例 4.4.6 设随机向量  $(\xi,\eta)$  服从区域  $D:=\{(x,y):x,y>0,x+y<1\}$  上的均匀分布, 即其联合分布密度为

$$
p (x, y) = 2, \quad (x, y) \in D.
$$

则 $\eta$ 的边缘分布密度为

$$
p _ {\eta} (y) = 2 \int_ {0} ^ {1 - y} \mathrm{d} x = 2 (1 - y), \quad 0 <   y <   1.
$$

所以

$$
p _ {\xi} (x | \eta = y) = \frac {1}{1 - y}, \quad 0 <   x <   1 - y.
$$

可见给定 $\eta = y$ 时 $\xi$ 的条件分布是 $(0,1 - y)$ 上的均匀分布，因而有

$$
\mathbf {E} (\xi | \eta = y) = \frac {1}{1 - y} \int_ {0} ^ {1 - y} x \mathrm{d} x = \frac {1 - y}{2}.
$$

所以  $\mathbf{E}(\xi|\eta)=(1-\eta)/2.$

定理4.4.3 设 $(\xi, \eta)$ 为离散型或绝对连续型随机向量，而 $f$ 为 $\mathbb{R}$ 上的可测函数且 $f(\xi)$ 可积。若 $\xi$ 和 $\eta$ 独立，则几乎必然有

$$
\mathbf {E} [ f (\xi) | \eta ] = \mathbf {E} [ f (\xi) ]. \tag {4.4.10}
$$

证明 因为 $\xi$ 和 $\eta$ 独立, 根据定理 3.2.3 和定理 3.2.4 可取 $p(x,y) := p_{\xi}(x)p_{\eta}(y)$ 为 $(\xi, \eta)$ 的联合分布密度. 于是对 $y \in V$ 有 $p_{\xi}(\cdot|\eta = y) = p_{\xi}(\cdot)$. 由 (4.4.4) 式和 (4.4.5) 式, 在两种情况下对 $y \in V$ 都有

$$
\mathbf {E} [ f (\xi) | \eta = y ] = \mathbf {E} [ f (\xi) ].
$$

再因 $\mathbf{P}(\eta \in V) = 1$ ，由定义4.4.4即知(4.4.10)式成立.

## 4.4.4 条件期望的平滑性质

对于离散型随机向量的函数的数学期望, 作为全期望公式的特殊情况, 我们有

---

4.4 条件期望和预测

125

定理 4.4.4 设  $(\xi,\eta)$  为取值于  $\{(x_{i},y_{j}):i,j=1,2,\cdots\}$  的离散型随机向量，且有边缘分布密度  $p_{\xi}(x_{i})$  和  $p_{\eta}(y_{j})$ . 再设  $f(\xi,\eta)$  可积. 则

$$
\mathbf {E} [ f (\xi , \eta) ] = \sum_ {j = 1} ^ {\infty} \mathbf {E} [ f (\xi , \eta) | \eta = y _ {j} ] p _ {\eta} (y _ {j}).
$$

对于绝对连续型随机向量的函数的数学期望,与上面结果类似地有

定理4.4.5 假设 $(\xi, \eta)$ 服从绝对连续型分布，且有边缘分布密度 $p_{\xi}(x)$ 和 $p_{\eta}(y)$. 再设 $f$ 为 $\mathbb{R}^2$ 上的可测函数且 $f(\xi, \eta)$ 可积. 则

$$
\mathbf {E} [ f (\xi , \eta) ] = \int_ {- \infty} ^ {\infty} \mathbf {E} [ f (\xi , y) | \eta = y ] p _ {\eta} (y) \mathrm{d} y.
$$

证明 设 $(\xi, \eta)$ 有联合分布密度 $p(x, y)$ 和边缘分布密度 $p_{\xi}(x), p_{\eta}(y)$. 根据条件分布密度的定义有 $p(x, y) = p_{\eta}(y)p_{\xi}(x|\eta = y)$. 于是有

$$
\begin{array}{l} \mathbf {E} [ f (\xi , \eta) ] = \int_ {- \infty} ^ {\infty} \int_ {- \infty} ^ {\infty} f (x, y) p (x, y) \mathrm{d} x \mathrm{d} y \\ = \int_ {- \infty} ^ {\infty} p _ {\eta} (y) \mathrm{d} y \int_ {- \infty} ^ {\infty} f (x, y) p _ {\xi} (x | \eta = y) \mathrm{d} x. \\ \end{array}
$$

再由 (4.4.5) 式即得欲证者.

定理 4.4.6（条件期望的平滑性） 假设  $(\xi,\eta)$  为离散型或绝对连续型随机向量. 再设 f 为  $R^{2}$  上的可测函数且  $f(\xi,\eta)$  可积. 则

$$
\mathbf {E} \{\mathbf {E} [ f (\xi , \eta) | \eta ] \} = \mathbf {E} [ f (\xi , \eta) ].
$$

证明 两种情况的证明类似. 这里只考虑 $(\xi, \eta)$ 服从绝对连续型分布的情况. 令 $h(y)$ 由 (4.4.9) 式定义. 应用定理 4.4.5 有

$$
\mathbf {E} [ f (\xi , \eta) ] = \int_ {- \infty} ^ {\infty} \mathbf {E} [ f (\xi , \eta) | \eta = y ] p _ {\eta} (y) \mathrm{d} y = \int_ {- \infty} ^ {\infty} h (y) p _ {\eta} (y) \mathrm{d} y = \mathbf {E} [ h (\eta) ].
$$

故得欲证结果.

定理 4.4.6 给出的平滑性是条件期望的一个基本性质, 可认为是例 4.4.4 中结果的一般化. 该定理的证明主要基于定理 4.4.4 和定理 4.4.5 给出的全期望公式. 因此我们可以认为该平滑性实质上是全期望公式的另外一种表达形式.

例 4.4.7 设  $\eta$  服从指数分布  $E(\lambda)$ ，而在给定  $\eta$  的条件下  $\xi$  服从均匀分布  $U(0,\eta)$ ，下面求  $\mathbf{E}(\xi|\eta)$  和  $E\xi$ 。根据题意，有  $p_{\xi}(x|\eta=y)=y^{-1}1_{\{0<x<y\}}$ ，故

$$
\mathbf {E} (\xi | \eta = y) = \frac {1}{y} \int_ {0} ^ {y} x \mathrm{d} x = \frac {y}{2}.
$$

---

126

第四章 积分和数学期望

根据定理4.4.5有

$$
\mathbf {E} \xi = \lambda \int_ {0} ^ {\infty} \mathbf {E} (\xi | \eta = y) \mathrm{e} ^ {- \lambda y} \mathrm{d} y = \frac {\lambda}{2} \int_ {0} ^ {\infty} y \mathrm{e} ^ {- \lambda y} \mathrm{d} y = \frac {1}{2 \lambda}.
$$

该结果也可以利用条件期望的平滑性得到

$$
\mathbf {E} \xi = \mathbf {E} [ \mathbf {E} (\xi | \eta) ] = \mathbf {E} \Big (\frac {\eta}{2} \Big) = \frac {1}{2 \lambda}.
$$

定理4.4.7 设 $(\xi, \eta)$ 为离散型或绝对连续型随机向量，而 $g$ 为博雷尔可测函数。令 $V$ 由(4.4.8)式定义。再设 $f$ 为 $\mathbb{R}^2$ 上的可测函数，且对任何 $y \in V$ ，在给定 $\eta = y$ 条件下 $f(\xi, \eta)$ 和 $g(y)f(\xi, \eta)$ 均可积。则

$$
\mathbf {E} [ g (\eta) f (\xi , \eta) | \eta ] = g (\eta) \mathbf {E} [ f (\xi , \eta) | \eta ].
$$

证明 定义 $h(y) = 1_V(y)\mathbf{E}[f(\xi, \eta)|\eta = y]$ 和 $H(y) = 1_V(y)\mathbf{E}[g(\eta)f(\xi, \eta)|\eta = y]$. 注意对 $y \in V$ 有

$$
H (y) = \mathbf {E} [ g (y) f (\xi , \eta) | \eta = y ] = g (y) \mathbf {E} [ f (\xi , \eta) | \eta = y ] = g (y) h (y).
$$

所以

$$
\mathbf {E} [ g (\eta) f (\xi , \eta) | \eta ] = H (\eta) = g (\eta) h (\eta) = g (\eta) \mathbf {E} [ f (\xi , \eta) | \eta ].
$$

故得欲证结果.

推论 4.4.8 设  $(\xi,\eta)$  为离散型或绝对连续型随机向量, 而 g 为博雷尔可测函数. 再设对任何  $y \in V$ , 在给定  $\eta = y$  条件下  $f(\xi,\eta)$  和  $g(\eta)f(\xi,\eta)$  均可积. 则

$$
\mathbf {E} [ g (\eta) f (\xi , \eta) ] = \mathbf {E} \big \{g (\eta) \mathbf {E} [ f (\xi , \eta) | \eta ] \big \}.
$$

推论4.4.9 设 $(\xi, \eta)$ 为离散型或绝对连续型随机向量. 再设对任何 $y \in V$, 在给定 $\eta = y$ 条件下 $f(\xi, \eta)$ 可积. 则对任何 $B \in \sigma(\eta)$ 有

$$
\mathbf {E} [ 1 _ {B} f (\xi , \eta) ] = \mathbf {E} \big \{1 _ {B} \mathbf {E} [ f (\xi , \eta) | \eta ] \big \}.
$$

证明 注意, 存在 $C \in \mathcal{B}$ 使得 $B = \eta^{-1}(C)$, 故 $1_B = 1_C(\eta)$. 再由推论4.4.8即得欲证结果. □

显然, 推论 4.4.8 和推论 4.4.9 都加强了定理 4.4.6 中给出的条件期望的平滑性质.

例 4.4.8 设  $\eta$  服从泊松分布  $P(\lambda)$ ，而  $\xi$  为伯努利试验  $B(p,\eta)$  的成功次数。根据定理 4.4.7 和例 4.3.1 的结论有

$$
\mathbf {E} (\xi \eta) = \mathbf {E} [ \mathbf {E} (\xi \eta | \eta) ] = \mathbf {E} [ \eta \mathbf {E} (\xi | \eta) ] = p \mathbf {E} (\eta^ {2}) = p \lambda (1 + \lambda).
$$

本节的讨论可以容易地推广到  $\eta$  是多维随机向量的情况.

---

4.4 条件期望和预测

127

## \*4.4.5 条件期望的最优预测性

定理4.4.10 设 $(\xi, \eta)$ 为平方可积的离散型或绝对连续型随机向量. 取 $\mathbb{R}$ 上的可测函数 $f$, 并以形如 $f(\eta)$ 的随机变量作为 $\xi$ 的估计. 则使 $\mathbf{E}\{[\xi - f(\eta)]^2\}$ 达最小的估计为 $f(\eta) = \mathbf{E}(\xi|\eta)$.

证明 以绝对连续型分布情况为例. 根据定理4.4.6, 我们有

$$
\begin{array}{l} \mathbf {E} \big \{[ \xi - f (\eta) ] ^ {2} \big \} = \mathbf {E} \big \{\mathbf {E} \big [ (\xi - f (\eta)) ^ {2} | \eta \big ] \big \} \\ = \int_ {- \infty} ^ {\infty} \mathbf {E} \big [ (\xi - f (y)) ^ {2} | \eta = y \big ] p _ {\eta} (y) \mathrm{d} y. \\ \end{array}
$$

再由命题4.3.3知，当 $f(y) = \mathbf{E}(\xi |\eta = y)$ 时 $\mathbf{E}[(\xi -f(y))^2 |\eta = y]$ 达最小.因此定理结论成立. □

基于上面定理, 我们可以把 $f(\eta) = \mathbf{E}(\xi|\eta)$ 作为在已知 $\eta$ 的情况下对于随机变量 $\xi$ 的最优预测.

例4.4.9 设 $(\xi, \eta)$ 服从二维正态分布 $N(a_{1}, a_{2}; \sigma_{1}^{2}, \sigma_{2}^{2}; r)$. 根据例4.4.2的结果知 $f(\eta) = a_{1} + r\sigma_{1}(\eta - a_{2}) / \sigma_{2}$ 是对 $\xi$ 的最优预测. 所以正态情形的最优预测是线性的.

## 练习题

1. 设随机向量 $(\xi, \eta)$ 服从区域 $G := \{(x, y) : x, y > 0, x + y^2 < 1\}$ 上的均匀分布. 求条件期望 $\mathbf{E}(\xi|\eta)$.
2. 设  $(\xi,\eta)$  为概率空间  $(\Omega,\mathcal{F},\mathbf{P})$  上的随机向量, 其中  $\eta$  为取值于可数集  $V:=\{y_{j}:j=1,2,\cdots\}$  的离散型随机变量且有分布列  $p_{\eta}(y_{j})=\mathbf{P}(\eta=y_{j})$ . 再设存在  $R\times V$  上的严格正可积函数  $p(x,y_{j})$  使得

$$
\mathbf {P} (a \leqslant \xi \leqslant b, \eta = y _ {j}) = \int_ {a} ^ {b} p (x, y _ {j}) \mathrm{d} x, \quad a \leqslant b \in \mathbb {R}.
$$

(1) 证明 $\xi$ 为绝对连续型随机变量, 并求出它的密度函数 $p_{\xi}(x)$.
(2) 求  $\xi$  的条件分布函数  $F_{\xi}(x|\eta = y_{j})$  和条件密度函数  $p_{\xi}(x|\eta = y_{j})$ .
(3) 令 $f$ 为 $\mathbb{R}$ 上的有界连续函数. 求 $f(\xi)$ 条件期望 $h(y_j) := \mathbf{E}[f(\xi) | \eta = y_j]$.
(4) 记  $\mathbf{E}[f(\xi)|\eta]=h(\eta)$ . 证明  $\mathbf{E}\{\mathbf{E}[f(\xi)|\eta]\}=\mathbf{E}[f(\xi)]$ .

3. 设 $\eta$ 服从泊松分布 $P(\lambda)$, 而在给定 $\eta$ 的条件下 $\xi$ 服从均匀分布 $U(0, \eta)$. 求 $\mathbf{E}(\xi|\eta)$ 和 $\mathbf{E}\xi$.
4. 设 $\{\xi_i\}$ 为独立同分布可积随机变量列, 而 $\eta$ 为与 $\{\xi_i\}$ 独立的非负整数值可积随机变量. 再设 $\{\xi_i\}$ 和 $\eta$ 都是平方可积随机变量. 证明:

$$
\mathrm{Var} \Big (\sum_ {k = 1} ^ {\eta} \xi_ {k} \Big) = \mathbf {E} \eta \mathrm{Var} \xi_ {1} + \mathrm{Var} \eta (\mathbf {E} \xi_ {1}) ^ {2}.
$$

---

128

第四章 积分和数学期望

## 4.5 随机变量的母函数

取非负整数值的随机变量在概率论中占有重要的位置. 我们前面讨论的二项分布、几何分布、帕斯卡分布和泊松分布都属于这种类型. 对于这类随机变量, 母函数是重要的研究工具. 随机变量的母函数与其分布列相互唯一决定, 可以认为是分布列或分布函数的一种变换, 还是后面将要系统讨论的特征函数的先导.

## 4.5.1 母函数的定义

定义 4.5.1 给定数列  $\{a(i): i=0,1,2,\cdots\}\subseteq[0,1]$ ，我们称幂级数

$$
f (s) := \sum_ {i = 0} ^ {\infty} a (i) s ^ {i} \tag {4.5.1}
$$

为其母函数. 显然, 上面级数至少在区间 $[-1, 1]$ 上绝对收敛且一致收敛. 若 $\{p(i)\}$ 为非负整数值随机变量 $\xi$ 的分布列, 我们也称 $\{p(i)\}$ 的母函数 $g$ 为 $\xi$ 的母函数, 注意此时 $g(s) = \mathbf{E}(s^{\xi})$.

定理 4.5.1（唯一性） 数列  $\{a(i): i=0,1,2,\cdots\}\subseteq[0,1]$  与其母函数 f 相互唯一决定.

证明 显然母函数 $f$ 由数列 $\{a(i)\}$ 唯一决定. 另一方面, 对 (4.5.1) 式两端求导数, 当 $|s| < 1$ 时有

$$
f ^ {(k)} (s) = \sum_ {i = k} ^ {\infty} i (i - 1) \dots (i - k + 1) a (i) s ^ {i - k}.
$$

于是

$$
a (k) = \frac {1}{k !} f ^ {(k)} (0), \quad k = 0, 1, 2, \dots . \tag {4.5.2}
$$

所以数列  $\{a(i)\}$  也由母函数 f 唯一决定.

定理4.5.2 假设 $\xi$ 是以 $g$ 为母函数的非负整数值随机变量，则

$$
\mathbf {E} \xi = g ^ {\prime} (1 -), \quad \mathbf {E} (\xi^ {2}) = g ^ {\prime \prime} (1 -) + g ^ {\prime} (1 -).
$$

证明 对母函数的定义式逐项求导, 当  $|s| < 1$  时有

$$
g ^ {\prime} (s) = \sum_ {i = 1} ^ {\infty} i s ^ {i - 1} p (i), \quad g ^ {\prime \prime} (s) = \sum_ {i = 2} ^ {\infty} i (i - 1) s ^ {i - 2} p (i).
$$

---

4.5 随机变量的母函数

129

令 $s \uparrow 1$ 得

$$
g ^ {\prime} (1 -) = \sum_ {i = 1} ^ {\infty} i p (i) = \mathbf {E} \xi
$$

和

$$
g ^ {\prime \prime} (1 -) = \sum_ {i = 1} ^ {\infty} i (i - 1) p (i).
$$

所以有

$$
g ^ {\prime \prime} (1 -) + g ^ {\prime} (1 -) = \sum_ {i = 1} ^ {\infty} i ^ {2} p (i) = \mathbf {E} (\xi^ {2}).
$$

故得欲证结果.

例4.5.1 二项分布 $B(n,p)$ 的母函数为 $(q = 1 - p)$

$$
g (s) = \sum_ {i = 0} ^ {n} \mathrm{C} _ {n} ^ {i} q ^ {n - i} p ^ {i} s ^ {i} = (q + p s) ^ {n}.
$$

其收敛域为 $(-∞,∞)$ .

例4.5.2 几何分布 $G(p)$ 的母函数为 $(q = 1 - p)$

$$
g (s) = \sum_ {i = 1} ^ {\infty} q ^ {i - 1} p s ^ {i} = p s \sum_ {i = 1} ^ {\infty} (q s) ^ {i - 1} = \frac {p s}{1 - q s}.
$$

其收敛域为 $(-1/q,1/q)$ .

例 4.5.3 根据泰勒展开式, 对  $|x| < 1$  有

$$
\begin{array}{l} (1 - x) ^ {- n} = \sum_ {k = 0} ^ {\infty} \frac {n (n + 1) \cdots (n + k - 1)}{k !} x ^ {k} \\ = \sum_ {k = 0} ^ {\infty} \mathrm{C} _ {n + k - 1} ^ {n - 1} x ^ {k} = \sum_ {k = n} ^ {\infty} \mathrm{C} _ {k - 1} ^ {n - 1} x ^ {k - n}. \\ \end{array}
$$

所以帕斯卡分布 $Pa(n,p)$ 的母函数为 $(q = 1 - p)$

$$
\sum_ {k = n} ^ {\infty} \mathrm{C} _ {k - 1} ^ {n - 1} p ^ {n} q ^ {k - n} s ^ {k} = (p s) ^ {n} \sum_ {k = n} ^ {\infty} \mathrm{C} _ {k - 1} ^ {n - 1} (q s) ^ {k - n} = \left(\frac {p s}{1 - q s}\right) ^ {n}.
$$

其收敛域为 $(-1/q,1/q)$ .

例4.5.4 泊松分布 $P(\lambda)$ 的母函数为

$$
g (s) = \sum_ {i = 0} ^ {\infty} \mathrm{e} ^ {- \lambda} \frac {\lambda^ {i}}{i !} s ^ {i} = \mathrm{e} ^ {- \lambda} \mathrm{e} ^ {\lambda s} = \mathrm{e} ^ {\lambda (s - 1)}.
$$

其收敛域为 $(-∞,∞)$ .

---

130

第四章 积分和数学期望

## 4.5.2 独立变量和的母函数

定理4.5.3 设 $\xi, \eta$ 为相互独立的非负整数值随机变量，且分别有母函数 $g(s), h(s)$. 则 $\zeta := \xi + \eta$ 的母函数为 $f(s) := g(s)h(s)$.

证明 令 $p(i) = \mathbf{P}(\xi = i)$ 和 $q(j) = \mathbf{P}(\eta = j)$. 由离散卷积公式

$$
\mathbf {P} (\zeta = k) = \sum_ {i = 0} ^ {k} p (i) q (k - i).
$$

因此有

$$
\begin{array}{l} f (s) = \sum_ {k = 0} ^ {\infty} \mathbf {P} (\zeta = k) s ^ {k} = \sum_ {k = 0} ^ {\infty} \sum_ {i = 0} ^ {k} p (i) q (k - i) s ^ {k} \\ = \sum_ {i = 0} ^ {\infty} \sum_ {k = i} ^ {\infty} p (i) s ^ {i} q (k - i) s ^ {k - i} = \sum_ {i = 0} ^ {\infty} \sum_ {j = 0} ^ {\infty} p (i) s ^ {i} q (j) s ^ {j}. \\ \end{array}
$$

故得欲证结果.

例4.5.5 设随机变量 $\xi_{1}$ 和 $\xi_{2}$ 独立且分别服从二项分布 $B(k,p)$ 和 $B(n,p)$. 则 $\xi_{1}$ 和 $\xi_{2}$ 分别有母函数 $(q+ps)^{k}$ 和 $(q+ps)^{n}$. 根据定理4.5.3知 $\xi_{1}+\xi_{2}$ 的母函数为 $(q+ps)^{k+n}$. 再由定理4.5.1知 $\xi_{1}+\xi_{2}$ 服从二项分布 $B(k+n,p)$. 这给出了二项分布的再生性的简单证明. 类似地可以给出泊松分布的再生性的证明.

定理 4.5.4 设  $\{\xi_{i}\}$  为相互独立的非负整数值随机变量列，且有共同的母函数  $g(s)$ . 再设  $\eta$  为非负整数值随机变量，有母函数  $h(s)$  且与  $\{\xi_{i}\}$  独立. 则  $\xi := \xi_{1} + \xi_{2} + \cdots + \xi_{\eta}$  的母函数为  $f(s) = h(g(s))$ .

证明 根据定理 4.5.3, 对于  $n \geqslant 1$  随机变量  $\xi_{1} + \xi_{2} + \cdots + \xi_{n}$  有母函数  $g(s)^{n}$ . 根据全概率公式, 并利用  $\eta$  与  $\{\xi_{i}\}$  的独立性, 有

$$
\begin{array}{l} f (s) = \sum_ {k = 0} ^ {\infty} \mathbf {P} (\xi_ {1} + \xi_ {2} + \dots + \xi_ {\eta} = k) s ^ {k} \\ = \sum_ {k = 0} ^ {\infty} \sum_ {n = 0} ^ {\infty} \mathbf {P} (\eta = n) \mathbf {P} (\xi_ {1} + \xi_ {2} + \dots + \xi_ {n} = k | \eta = n) s ^ {k} \\ = \sum_ {n = 0} ^ {\infty} \mathbf {P} (\eta = n) \sum_ {k = 0} ^ {\infty} \mathbf {P} (\xi_ {1} + \xi_ {2} + \dots + \xi_ {n} = k) s ^ {k} \\ = \sum_ {n = 0} ^ {\infty} \mathbf {P} (\eta = n) g (s) ^ {n} = h (g (s)). \\ \end{array}
$$

故得欲证结果.

---

4.5 随机变量的母函数

131

例4.5.6 假设定理4.5.4中的随机变量都可积.则利用母函数与期望的关系易得

$$
\mathbf {E} \xi = f ^ {\prime} (1 -) = h ^ {\prime} (1 -) g ^ {\prime} (1 -) = \mathbf {E} \eta \mathbf {E} \xi_ {1}.
$$

这比例 4.4.3 中相应结果的证明简单了很多.

## 4.5.3 母函数的连续性定理

定理 4.5.5（连续性定理） 设对每个  $n \geqslant 1$  有数列  $\{a_{n}(i): i = 0, 1, 2, \cdots\} \subseteq [0, 1]$ ，并记其母函数为  $g_{n}$ 。则对每个  $i \geqslant 0$  极限  $a(i) := \lim_{n \to \infty} a_{n}(i)$  存在当且仅当对每个 0 < s < 1 极限  $g(s) := \lim_{n \to \infty} g_{n}(s)$  存在。此时 g 与  $\{a(i): i = 0, 1, 2, \cdots\}$  的母函数在区间 (0, 1) 内重合。

证明 设对每个  $i \geqslant 0$  极限  $a(i) := \lim_{n \to \infty} a_n(i)$  存在. 令 f 为  $\{a(i) : i = 0, 1, 2, \cdots\}$  的母函数. 由于  $|a_n(i) - a(i)| \leqslant 1$ , 对于 0 < s < 1 有

$$
\begin{array}{l} | g _ {n} (s) - f (s) | \leqslant \sum_ {i = 0} ^ {k} | a _ {n} (i) - a (i) | s ^ {i} + \sum_ {i = k + 1} ^ {\infty} | a _ {n} (i) - a (i) | s ^ {i} \\ \leqslant \sum_ {i = 0} ^ {k} | a _ {n} (i) - a (i) | + \frac {s ^ {k + 1}}{1 - s}. \\ \end{array}
$$

对任何 $\varepsilon > 0$, 可取充分大的 $N \geqslant 1$ 使当 $k \geqslant N$ 时有 $s^{k+1} / (1 - s) \leqslant \varepsilon$. 这样, 在上式两端取极限有 $\liminf_{n \to \infty} |g_n(s) - f(s)| \leqslant \varepsilon$. 这说明极限 $g(s) := \lim_{n \to \infty} g_n(s)$ 存在, 且 $g$ 与 $f$ 在区间 $(0,1)$ 内重合. 反之, 设对每个 $0 < s < 1$ 极限 $g(s) := \lim_{n \to \infty} g_n(s)$ 存在. 则函数 $g$ 在区间 $(0,1)$ 内单调不降, 故极限 $g(0) := \lim_{s \downarrow 0} g(s)$ 存在. 注意, 对 $0 < s < 1$ 有

$$
a _ {n} (0) \leqslant g _ {n} (s) \leqslant a _ {n} (0) + \sum_ {i = 1} ^ {\infty} s ^ {i} = a _ {n} (0) + \frac {s}{1 - s},
$$

从而

$$
g _ {n} (s) - \frac {s}{1 - s} \leqslant a _ {n} (0) \leqslant g _ {n} (s).
$$

因此有

$$
g (s) - \frac {s}{1 - s} \leqslant \operatorname * {l i m i n f} _ {n \to \infty} a _ {n} (0) \leqslant \operatorname * {l i m s u p} _ {n \to \infty} a _ {n} (0) \leqslant g (s).
$$

令 $s \downarrow 0$ 知 $\lim_{n \to \infty} a_n(0) = g(0) =: a_0$. 再利用假设, 对 $0 < s < 1$ 有

$$
\frac {1}{s} [ g _ {n} (s) - a _ {n} (0) ] = \sum_ {i = 0} ^ {\infty} a _ {n} (i + 1) s ^ {i} \rightarrow \frac {1}{s} [ g (s) - a _ {0} ] = \frac {1}{s} [ g (s) - g (0) ].
$$

---

132

第四章 积分和数学期望

与前面的推导类似, 可知导数 $g'(0)$ 存在且 $\lim_{n\to \infty}a_n(1) = g'(0) =: a(1)$. 利用数学归纳法可以证明每个 $i \geqslant 0$ 极限 $a(i) := \lim_{n\to \infty}a_n(i)$ 存在. 因此定理结论成立. □

作为定理 4.5.5 的特殊情况, 我们有

定理 4.5.6（连续性定理） 设对每个 $n \geqslant 1$ 有分布列 $\{p_n(i): i = 0,1,2,\cdots\}$，并记其母函数为 $g_n$。则存在分布列 $\{p(i): i = 0,1,2,\cdots\}$ 使对每个 $i \geqslant 0$ 有 $p(i) = \lim_{n \to \infty} p_n(i)$ 当且仅当对每个 $0 < s < 1$ 极限 $g(s) := \lim_{n \to \infty} g_n(s)$ 存在且 $\lim_{s \uparrow 1} g(s) = 1$。此时 $g$ 与 $\{p(i): i = 0,1,2,\cdots\}$ 的母函数在区间 $(0,1)$ 内重合。

例4.5.7 设数列 $\{p_n\} \subseteq [0,1]$ 满足 $\lim_{n\to \infty}np_n = \lambda >0$。则二项分布 $B(n,p_n)$ 的母函数为 $g_{n}(s) = [1 - p_{n}(1 - s)]^{n}$。对 $0 < s < 1$ 有

$$
\lim _ {n \to \infty} g _ {n} (s) = \lim _ {n \to \infty} \left\{\left[ 1 - p _ {n} (1 - s) \right] ^ {- 1 / p _ {n} (1 - s)} \right\} ^ {- n p _ {n} (1 - s)} = \mathrm{e} ^ {- \lambda (1 - s)}.
$$

上式右端是泊松分布 $P(\lambda)$ 的母函数. 根据定理4.5.5有

$$
\lim _ {n \to \infty} \mathrm{C} _ {n} ^ {i} (1 - p _ {n}) ^ {n - i} p _ {n} ^ {i} = \mathrm{e} ^ {- \lambda} \frac {\lambda^ {i}}{i !}.
$$

这就给出了定理 2.2.3 的一个简单证明.

## 练习题

1. 设某公共汽车站在时间区间  $[0, t]$  到来的乘客批数  $\eta(t)$  服从参数为  $\lambda t (\lambda > 0)$  的泊松分布，且第 k 批乘客的人数  $\xi_{k}$  服从分布  $\{p(i): i = 0, 1, \cdots\}$ . 再设随机变量  $\eta(t), \xi_{1}, \xi_{2}, \cdots$  相互独立. 求在时间区间  $[0, t]$  到来的乘客总数  $N(t)$  的母函数和数学期望.

2. 利用母函数方法求帕斯卡分布的期望和方差.

3. 设随机变量  $\xi_{1}, \xi_{2}, \cdots, \xi_{n}$  相互独立且均服从几何分布  $G(p)$ . 用母函数方法证明  $\xi_{1} + \xi_{2} + \cdots + \xi_{n}$  服从帕斯卡分布  $Pa(n, p)$ .

4. 利用母函数方法给出泊松分布的再生性的证明.

5. 设 $g$ 为离散型概率分布 $\{p(i): i = 0,1,\dots\}$ 的母函数, 其中 $p(1) \neq 1$. 令 $g_1(z) = g(z)$ 并对 $n \geqslant 2$ 递推地定义 $g_n(z) = g_{n-1}(g(z))$. 证明: 对于任何 $0 \leqslant z < 1$ 极限 $q := \lim_{n \to \infty} g_n(z)$ 存在, 且该极限为方程 $z = g(z)$ 在区间 $[0,1]$ 的最小解.
