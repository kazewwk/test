## 习题七

1. 生成 $n = 20,30,50$ 个来自 $Exp(1)$ 的随机变量, 比较样本均值 $\bar{X}$ 的精确分布、CLT近似分布和bootstrap方法构造的分布之间的差异, 并讨论bootstrap方法相比于CLT近似法的优缺点.
2. 假设总体均值为 $\mu$, 我们感兴趣的是估计 $\mu^2$, 现考虑直接使用 $\bar{X}^2$ 作为估计, 请问如何使用 bootstrap 方法进行偏差修正?
3. 假设  $(X_{i}, Y_{i}), i = 1, 2, \cdots, n$  是来自二元正态分布  $N(\mathbf{0}, \Sigma)$  的一组独立同分布样本, 其中  $\Sigma = \begin{pmatrix} 1 & \rho \\ \rho & 1 \end{pmatrix}$ . 对于不同样本数 n = 20, 30, 50, 比较运用大样本理论和 bootstrap 方法对样本相关系数 r 的渐近方差的估计效果.
4. 证明例7.3.1中 $T_{n}^{*}$ 的渐近分布.
5. 假设  $X_{1}, X_{2}, \cdots, X_{n}$  为来自 Cauchy 分布  $C(0,1)$  的独立同分布样本. 对不同样本数 n = 20, 50, 比较运用大样本理论和 bootstrap 方法构造 Cauchy 分布  $C(0,1)$  中位数的置信水平为 0.95 的置信区间的效果.
6. (1) 给出一个运用 bootstrap 方法估计中位数失效的例子; (2) 给出一个运用 bootstrap 方法估计均值失效的例子.

## 附录

## 补充知识

## A.1 随机变量序列的收敛性

设  $X_{n}, n \geqslant 1$  与 X 是给定概率空间  $(\Omega, \mathcal{F}, P)$  上的随机变量.

定义A.1.1(依概率收敛) 如果对于任意 $\varepsilon >0$ 有

$$
\lim _ {n \to \infty} P \left(| X _ {n} - X | > \varepsilon\right) = 0,
$$

则称  $\{X_{n}\}$  依概率收敛到 X，记作  $X_{n} \xrightarrow{P} X$ .

对于 $p$ 维随机变量 $\mathbf{X}_n, n \geqslant 1$ 和 $\mathbf{X}$, 如果 $||\mathbf{X}_n - \mathbf{X}|| \xrightarrow{\mathrm{P}} 0$, 则称 $\mathbf{X}_n \xrightarrow{\mathrm{P}} \mathbf{X}$. 易证, $\mathbf{X}_n \xrightarrow{\mathrm{P}} \mathbf{X}$ 当且仅当 $\mathbf{X}_n$ 的每一维度都依概率收敛到 $\mathbf{X}$ 的对应维度.

定理 A.1.1 (Chebyshev 不等式) 设随机变量 X 具有数学期望  $E(X) = \mu$ ，方差  $\mathrm{Var}(X) = \sigma^{2}$ 。则对任意正数  $\varepsilon$ ，有

$$
P \left(\left| X - \mu \right| \geqslant \varepsilon\right) \leqslant \frac {\sigma^ {2}}{\varepsilon^ {2}}.
$$

证明 设 $X$ 的分布函数为 $F(x)$. 则对任意的 $\varepsilon > 0$, 有

$$
\begin{array}{l} \sigma^ {2} = E [ (X - \mu) ^ {2} ] = \int (x - \mu) ^ {2} \mathrm{d} F (x) \\ \geqslant \int_ {| X - \mu | \geqslant \varepsilon} (x - \mu) ^ {2} \mathrm{d} F (x) \geqslant \varepsilon^ {2} \int_ {| X - \mu | \geqslant \varepsilon} \mathrm{d} F (x) = \varepsilon^ {2} P \left(| X - \mu | \geqslant \varepsilon\right). \\ \end{array}
$$

得证.

□

例A.1.1 对于一列独立同分布的二项分布试验 $B(1,0.5)$, $X_{n}$ 表示在前 $n$ 次试验中出现一次成功下一次失败的事件个数. 设

$$
T _ {i} = I \{\text {第} i \text {次试验成功且第} i + 1 \text {次试验失败} \},
$$

则 $X_{n} = \sum_{i = 1}^{n - 1}T_{i}$ ，且

$$
\begin{array}{l} E (X _ {n}) = \frac {n - 1}{4}, \\ = \frac {3 (n - 1)}{1 6} - \frac {2 (n - 2)}{1 6} = \frac {n + 1}{1 6}. \\ \end{array}
$$

$$
\mathrm{Var} (X _ {n}) = \sum_ {i = 1} ^ {n - 1} \mathrm{Var} (T _ {i}) + 2 \sum_ {i = 1} ^ {n - 2} \mathrm{Cov} (T _ {i}, T _ {i + 1})
$$

因此, 由 Chebyshev 不等式可知 $\frac{X_n}{n} \xrightarrow{\mathrm{p}} \frac{1}{4}$.

定义A.1.2(依概率有界) 如果对所有 $\varepsilon > 0$，存在常数 $B_{\varepsilon} > 0$ 以及整数 $N_{\varepsilon}$ 使得当 $n \geqslant N_{\varepsilon}$ 时，

$$
P \left(\left| X _ {n} \right| \geqslant B _ {\varepsilon}\right) <   \varepsilon ,
$$

则称随机变量序列  $\{X_{n}\}$  依概率有界, 记作  $X_{n}=O_{p}(1)$ .

任意一个随机变量 (向量) 都依概率有界. 如果  $X_{n} \stackrel{P}{\rightarrow} 0$ , 则记  $X_{n} = o_{p}(1)$ . 一般地, 对于给定的一个随机变量序列  $\{R_{n}\}$ ,

$$
X _ {n} = o _ {p} (R _ {n}) \text {表示} X _ {n} = Y _ {n} R _ {n}, Y _ {n} \xrightarrow {\mathrm{P}} 0;
$$

$$
X _ {n} = O _ {p} (R _ {n}) \text {表示} X _ {n} = Y _ {n} R _ {n}, Y _ {n} = O _ {p} (1).
$$

对于一个实数序列 $\{a_{n}\}$, 如果 $a_{n}X_{n} \stackrel{\mathrm{P}}{\rightarrow} 0$, 则 $X_{n} = o_{p}(a_{n}^{-1})$; 如果 $a_{n}X_{n} = O_{p}(1)$, 则 $X_{n} = O_{p}(a_{n}^{-1})$.

定理A.1.2 $X_{n} = O_{p}(1),Y_{n} = o_{p}(1)$ ，则 $X_{n}Y_{n} = o_{p}(1)$

证明 令 $\varepsilon > 0$ ，选择 $B_{\varepsilon} > 0$ 和整数 $N_{\varepsilon}$ 使得

$$
n \geqslant N _ {\varepsilon} \Rightarrow P \left(\left| X _ {n} \right| \leqslant B _ {\varepsilon}\right) \geqslant 1 - \varepsilon .
$$

那么

$$
\lim _ {n \to \infty} P \left(| X _ {n} Y _ {n} | \geqslant \varepsilon\right) \leqslant \lim _ {n \to \infty} P \left(| X _ {n} Y _ {n} | \geqslant \varepsilon , | X _ {n} | \leqslant B _ {\varepsilon}\right) +
$$

$$
\lim _ {n \to \infty} P \left(| X _ {n} Y _ {n} | \geqslant \varepsilon , | X _ {n} | > B _ {\varepsilon}\right)
$$

$$
\leqslant \lim _ {n \to \infty} P \left(| Y _ {n} | \geqslant \varepsilon / B _ {\varepsilon}\right) + \varepsilon = \varepsilon .
$$

得证.

定义 A.1.3(依概率 1 收敛) 如果 $P\left(\lim_{n \to \infty} X_n = X\right) = 1$, 则称 $\{X_n\}$ 依概率 1 收敛到 $X$, 记作 $X_n \stackrel{\text{a.s.}}{\rightarrow} X$.

对于多维随机变量  $X_{n}$ ，如果  $\left|\left|X_{n}-X\right|\right|\stackrel{a.s.}{\rightarrow}0$ ，则称  $X_{n}\stackrel{a.s.}{\rightarrow}X$ .

定理 A.1.3  $X_{n} \stackrel{a.s.}{\rightarrow} X$  的充要条件是对任意的  $\varepsilon > 0,$

$$
\lim _ {n \to \infty} P \left(| X _ {m} - X | <   \varepsilon , m \geqslant n\right) = 1. \tag {A.1.1}
$$

定理 A.1.3 的证明参见 Serfling (1980) 的第七页.

推论 A.1.1 若  $X_{n} \stackrel{a.s.}{\rightarrow} X$ ，则  $X_{n} \stackrel{p}{\rightarrow} X$ .

推论 A.1.2 如果对任意的  $\varepsilon > 0, \sum_{n=1}^{\infty} P(|X_n - X| > \varepsilon) < \infty,$  则  $X_n \stackrel{a.s.}{\rightarrow} X$ .

例 A.1.2 设  $X_{1}, X_{2}, \cdots, X_{n}$  是一列来自  $U(0,1)$  的独立同分布随机变量序列. 则  $X_{(n)} \stackrel{\mathrm{def}}{=} \max\{X_{1}, X_{2}, \cdots, X_{n}\} \stackrel{\mathrm{a.s.}}{\rightarrow} 1$ , 因为

$$
P \left(\left| X _ {(n)} - 1 \right| \leqslant \varepsilon , \forall n \geqslant m\right)
$$

$$
\begin{array}{l} = P \left(X _ {(n)} \geqslant 1 - \varepsilon , \forall n \geqslant m\right) \\ = P \left(X _ {(m)} \geqslant 1 - \varepsilon\right) = 1 - (1 - \varepsilon) ^ {m} \rightarrow 1, \quad m \rightarrow \infty . \\ \end{array}
$$

定义 A.1.4 (r 阶收敛) 设 r > 0 为常数, 如果  $\lim_{n \to \infty} E[|X_n - X|^r] = 0$ , 则称  $\{X_n\}$  为 r 阶收敛到 X, 记作  $X_n \xrightarrow{r^{th}} X$ .

对多维随机变量  $X_{n}$ ，若  $\lim_{n\to\infty}E[||X_{n}-X||^{r}]=0$ ，则  $X_{n}\stackrel{rth}{\rightarrow}X$ .

定理A.1.4（Markov不等式） 设随机变量 $X$ 的 $r$ 阶矩有限，则对任意的 $\varepsilon > 0$ 有

$$
P \left(| X | > \varepsilon\right) \leqslant \frac {E (| X | ^ {r})}{\varepsilon^ {r}}.
$$

定理A.1.4是定理A.1.1的推广，证明同理.由定理A.1.4，我们很容易得到如下推论.

推论 A.1.3 若  $X_{n} \stackrel{r^{th}}{\rightarrow} X$ ，则  $X_{n} \stackrel{p}{\rightarrow} X$ .

例 A.1.3 设  $U \sim U(0,1)$ ,  $X = \sqrt{n}I(0 < U < 1/n)$ . 则  $P(|X| > \varepsilon) = P(0 < U < 1/n) = \frac{1}{n} \rightarrow 0$ . 因此  $X \xrightarrow{p} 0$ . 但是  $E(X^{2}) = 1$ , X 并不 r 阶收敛到 0.

定义A.1.5 设随机变量 $X_{n}$ 与 $X$ 分别有分布函数 $F_{n}(x)$ 与 $F(x)$，且在函数 $F$ 的连续点集上有 $\lim_{n\to \infty}F_n(x) = F(x)$，则称 $\{X_n\}$ 依分布收敛到 $X$，记作 $X_{n}\stackrel {\mathrm{d}}{\rightarrow}X$。

定理 A.1.5 若  $X_{n} \stackrel{p}{\rightarrow} X$ ，则  $X_{n} \stackrel{d}{\rightarrow} X$ .

证明 对于任意的 $x \in \mathbb{R}, \varepsilon > 0$, 我们有

$$
\begin{array}{l} F _ {n} (x) = P (X _ {n} \leqslant x) = P (X _ {n} \leqslant x, X > x + \varepsilon) + P (X _ {n} \leqslant x, X \leqslant x + \varepsilon) \\ \leqslant P \left(\left| X _ {n} - X \right| > \varepsilon\right) + P (X \leqslant x + \varepsilon). \\ \end{array}
$$

因此由 $X_{n} \stackrel{\mathrm{P}}{\to} X$，我们有 $\varlimsup_{n \to \infty} F_{n}(x) \leqslant F(x + \varepsilon), x \in C_{F}$，其中 $C_{F}$ 表示 $F(x)$ 的连续点集。同理 $\varliminf_{n \to \infty} F_{n}(x) \geqslant F(x - \varepsilon), x \in C_{F}$。令 $\varepsilon \to 0$，可证。$\square$

例 A.1.4 设 $X \sim N(0,1), X_n = -X$. 易知 $X_n \sim N(0,1)$, 因此 $X_n \stackrel{\mathrm{d}}{\to} X$. 但是 $P(|X_n - X| > \varepsilon) = P(2|X| > \varepsilon) = 1 - 2\Phi(\varepsilon/2) \nrightarrow 0$. 因此 $\{X_n\}$ 并不依概率收敛到 $X$.

定理A.1.6 若 $X_{n}\xrightarrow{\mathrm{d}}c$ ，则 $X_{n}\xrightarrow{\mathrm{p}}c.$

证明 对任意的  $\varepsilon > 0,$

$$
\begin{array}{l} P \left(\left| X _ {n} - c \right| > \varepsilon\right) = P \left(X _ {n} \geqslant c + \varepsilon\right) + P \left(X _ {n} \leqslant c - \varepsilon\right) \\ = 1 - F _ {n} (c + \varepsilon) + F _ {n} (c - \varepsilon + 0) \rightarrow 0. \\ \end{array}
$$

得证.

□

对于分布函数为  $F_{n}(\boldsymbol{x})$  的多维随机变量  $\boldsymbol{X}_{n}=(X_{n1},X_{n2},\cdots,X_{np})$ ，如果在  $\boldsymbol{X}=(X_{1},X_{2},\cdots,X_{p})$  的分布函数  $F(\boldsymbol{x})$  的连续集合上  $\lim_{n\to\infty}F_{n}(\boldsymbol{x})=F(\boldsymbol{x})$ ，则称  $X_{n}\stackrel{d}{\rightarrow}X$ 。显然，如果  $X_{n}\stackrel{d}{\rightarrow}X$ ，则  $X_{nk}\stackrel{d}{\rightarrow}X_{k}, k=1,2,\cdots,p$ 。但是反之并不成立。

例A.1.5 设 $X \sim U(0,1), X_n = X$ 且

$$
Y _ {n} = \left\{ \begin{array}{l l} {{X,}} & {{n \text {为偶数},}} \\ {{1 - X,}} & {{n \text {为奇数}.}} \end{array} \right.
$$

则 $X_{n}\xrightarrow{\mathrm{d}}U(0,1),Y_{n}\xrightarrow{\mathrm{d}}U(0,1)$ ，但是 $(X_{n},Y_{n})$ 并不依分布收敛.

如下三个定理常用来证明变量之间的依分布收敛性.

定理 A.1.7  $X_{n} \xrightarrow{d} X \Longleftrightarrow$  对任意有界连续函数  $g, E[g(X_{n})] \to E[g(X)]$ .

定理A.1.8 设 $\varphi_{\pmb{X}}, \varphi_{\pmb{X}_n}$ 分别为 $X, X_n$ 的特征函数，则 $X_n \xrightarrow{\mathrm{d}} X \Longleftrightarrow$ 对任意 $t \in \mathbb{R}^p$, $\varphi_{\pmb{X}_n}(\pmb{t}) \to \varphi_{\pmb{X}}(\pmb{t})$.

定理A.1.9 $X_{n}\xrightarrow{\mathrm{d}}X$ 当且仅当对任意的 $c\in \mathbb{R}^p$ 有 $c^{\mathrm{T}}X_{n}\xrightarrow{\mathrm{d}}c^{\mathrm{T}}X.$

定理 A.1.7 的证明参见 Serfling (1980) 第 16 页. 定理 A.1.8 的证明参见 Shao (2003) 第 57 页. 定理 A.1.9 可以由定理 A.1.8 推导出来, 留作练习.

## A.2 连续映射定理与 Slutsky 定理

定理A.2.1（连续映射定理）令 $g:\mathbb{R}^p\mapsto \mathbb{R}^m$ 为在集合 $C$ 中几乎处处连续的映射.如果 $\{\pmb {X}_n\}$ 依概率/依概率1收敛/依分布收敛到 $\pmb {X}$ ，则 $\{g(X_n)\}$ 依概率/依概率1收敛/依分布收敛到 $g(\pmb {X})$

连续映射定理的证明参见 Serfling (1980) 第 24 页.

推论A.2.1 设 $p$ 维随机变量序列 $\{X_{n}\}$ 依概率/依概率1/依分布收敛到 $X$ ，则对$A\in \mathbb{R}^{q\times p},B\in \mathbb{R}^{p\times p},\{AX_n\} ,\{X_n^{\mathrm{T}}BX_n\}$ 依概率/依概率1/依分布收敛到 $AX,X^{\mathrm{T}}BX.$

例A.2.1 若 $\pmb{X}_n\stackrel{\mathrm{d}}{\to}N(\pmb {\mu},\Sigma),C\in \mathbb{R}^{q\times p}$ ，则 $C\pmb {X}_n\xrightarrow{\mathrm{d}}N(C\pmb {\mu},C\Sigma C^{\mathrm{T}})$ 且 $(\pmb {X}_n - \pmb {\mu})^{\mathrm{T}}\Sigma^{-1}(\pmb {X}_n - \pmb {\mu})\stackrel{\mathrm{d}}{\to}\chi_p^2.$

推论A.2.2 设 $g$ 是定义在 $\mathbb{R}^p$ 上的函数且 $g(\mathbf{0}) = 0$. 若 $X_{n} \stackrel{\mathrm{P}}{\to} 0$, 则

(1) 如果当  $t \rightarrow 0$  时  $g(t) = o(||t||^{r})$ ，则  $g(\boldsymbol{X}_{n}) = o_{p}(||\boldsymbol{X}_{n}||^{r})$ ;
(2) 如果当  $t \rightarrow 0$  时  $g(t) = O(||t||^{r})$ ，则  $g(\boldsymbol{X}_{n}) = O_{p}(||\boldsymbol{X}_{n}||^{r})$ .

定理A.2.2(Slutsky定理) 令 $X_{n}\xrightarrow{\mathrm{d}}X$ 且 $Y_{n}\xrightarrow{\mathrm{p}}c,$ 其中 $c$ 为常数.则

(1) $X_{n}+Y_{n}\xrightarrow{d}X+c;$
(2) $X_{n}Y_{n}\xrightarrow{d}cX;$

(3) $Y_{n}^{-1}X_{n}\xrightarrow{d}c^{-1}X$ ，其中 $c\neq0$ .

证明 (1) 设 $x$ 是一个实数使得 $F(x)$ 在点 $x - c$ 处连续, 且 $\varepsilon$ 满足 $x - c + \varepsilon$ 仍然是 $F(x)$ 的一个连续点, 则

$$
\begin{array}{l} P \left(X _ {n} + Y _ {n} \leqslant x\right) = P \left(\left\{X _ {n} + Y _ {n} \leqslant x \right\} \cap \left\{\left| Y _ {n} - c \right| \leqslant \varepsilon \right\}\right) + \\ P \left(\{X _ {n} + Y _ {n} \leqslant x \} \cap \{| Y _ {n} - c | > \varepsilon \}\right) \\ \leqslant P \left(\left\{X _ {n} + Y _ {n} \leqslant x \right\} \cap \left\{\left| Y _ {n} - c \right| \leqslant \varepsilon \right\}\right) + P \left(\left| Y _ {n} - c \right| > \varepsilon\right) \\ \leqslant P \left(X _ {n} + c - \varepsilon \leqslant x\right) + P \left(\left| Y _ {n} - c \right| > \varepsilon\right). \\ \end{array}
$$

两边取极限可得

$$
\varlimsup_ {n \to \infty} P \left(X _ {n} + Y _ {n} \leqslant x\right) \leqslant \varlimsup_ {n \to \infty} P \left(X _ {n} + c - \varepsilon \leqslant x\right) + \varlimsup_ {n \to \infty} P \left(\left| Y _ {n} - c \right| > \varepsilon\right).
$$

由 $Y_{n}\stackrel {\mathrm{P}}{\rightarrow}c$ 可知上式右边第二项趋于0.因此

$$
\varlimsup_ {n \to \infty} P \left(X _ {n} + Y _ {n} \leqslant x\right) \leqslant \varlimsup_ {n \to \infty} P \left(X _ {n} + c \leqslant x + \varepsilon\right).
$$

由 $X_{n}\stackrel {\mathrm{d}}{\to}X$ 且令 $\varepsilon \rightarrow 0$ ，可得

$$
\varlimsup_ {n \to \infty} P (X _ {n} + Y _ {n} \leqslant x) \leqslant P (X + c \leqslant x).
$$

同理可得

$$
\varliminf_ {n \to \infty} P \left(X _ {n} + Y _ {n} \leqslant x\right) \geqslant P (X + c \leqslant x).
$$

因此

$$
\lim _ {n \to \infty} P (X _ {n} + Y _ {n} \leqslant x) = P (X + c \leqslant x).
$$

(2) 设  $\pm\varepsilon/\delta$  是  $F(x)$  的连续点. 不妨设  $Y_{n} \stackrel{P}{\rightarrow} 0$ :

$$
P \left(\left| X _ {n} Y _ {n} \right| > \varepsilon\right) = P \left(\left\{\left| X _ {n} Y _ {n} \right| > \varepsilon \right\} \cap \left\{\left| Y _ {n} \right| > \delta \right\}\right) + P \left(\left\{\left| X _ {n} Y _ {n} \right| > \varepsilon \right\} \cap \left\{\left| Y _ {n} \right| \leqslant \delta \right\}\right).
$$

因为

$$
| Y _ {n} | \leqslant \delta \Rightarrow \frac {1}{| Y _ {n} |} \geqslant \frac {1}{\delta} \Rightarrow \frac {| X _ {n} Y _ {n} |}{| Y _ {n} |} \geqslant \frac {\varepsilon}{\delta} \Rightarrow | X _ {n} | \geqslant \frac {\varepsilon}{\delta}
$$

且 $(\{|X_nY_n| > \varepsilon\} \cap \{|Y_n| > \delta\}) \subseteq \{|Y_n| > \delta\}$, 可知

$$
\begin{array}{l} P \left(\left| X _ {n} Y _ {n} \right| > \varepsilon\right) \leqslant P \left(\left| Y _ {n} \right| > \delta\right) + P \left(\left| X _ {n} \right| > \frac {\varepsilon}{\delta}\right) \\ \leqslant P \left(\left| Y _ {n} \right| > \delta\right) + P \left(X _ {n} > \frac {\varepsilon}{\delta}\right) + P \left(X _ {n} \leqslant \frac {- \varepsilon}{\delta}\right) \\ \end{array}
$$

$$
\begin{array}{l} = P \left(\left| Y _ {n} \right| > \delta\right) + 1 - P \left(X _ {n} \leqslant \frac {\varepsilon}{\delta}\right) + P \left(X _ {n} \leqslant \frac {- \varepsilon}{\delta}\right) \\ = P \left(\left| Y _ {n} \right| > \delta\right) + 1 - F _ {n} \left(\frac {\varepsilon}{\delta}\right) + F _ {n} \left(\frac {- \varepsilon}{\delta}\right). \\ \end{array}
$$

因此

$$
\varlimsup_ {n \to \infty} P \left(| X _ {n} Y _ {n} | > \varepsilon\right) \leqslant \varlimsup_ {n \to \infty} P \left(| Y _ {n} | > \delta\right) + \varlimsup_ {n \to \infty} 1 - \varlimsup_ {n \to \infty} F _ {n} \left(\frac {\varepsilon}{\delta}\right) + \varliminf_ {n \to \infty} F _ {n} \left(\frac {- \varepsilon}{\delta}\right).
$$

由 $Y_{n}\stackrel {\mathrm{p}}{\to}0$ 且 $F(x)$ 的连续性可得

$$
\varlimsup_ {n \to \infty} P \left(| X _ {n} Y _ {n} | > \varepsilon\right) \leqslant 1 - F \left(\frac {\varepsilon}{\delta}\right) + F \left(\frac {- \varepsilon}{\delta}\right).
$$

令 $\delta \to 0$ ，则 $F\left(\frac{\varepsilon}{\delta}\right) \to 1$ 且 $F\left(\frac{-\varepsilon}{\delta}\right) \to 0$ ，从而 $P(|X_nY_n| > \varepsilon) \to 0$ ，即 $X_{n}Y_{n} \stackrel{\mathrm{p}}{\to} 0.$ 如果 $c \neq 0$ ，则存在一个随机变量 $Z_{n} \stackrel{\mathrm{p}}{\to} 0$ 使得 $Y_{n} = c + Z_{n}$. 因此 $X_{n}Y_{n} = X_{n}Z_{n} + cX_{n}$. 由(1)和连续映射定理可知(2)成立.

$$
\frac {X _ {n}}{Y _ {n}} - c ^ {- 1} X _ {n} = X _ {n} (Y _ {n} ^ {- 1} - c ^ {- 1}). \tag {3}
$$

由连续映射定理可知 $Y_{n}^{-1}\xrightarrow{\mathrm{p}}c^{-1}$ ，即 $Y_{n}^{-1} - c^{-1} = o_{p}(1)$ .由(2)可知， $X_{n}(Y_{n}^{-1} - c^{-1})\xrightarrow{\mathrm{d}}$ 0.由定理A.1.6, $X_{n}(Y_{n}^{-1} - c^{-1})\xrightarrow{\mathrm{p}}0.$ 由(1)可知， $Y_{n}^{-1}X_{n}\xrightarrow{\mathrm{d}}c^{-1}X_{n}.$ 再由(2)可知结论成立.

例 A.2.2 设  $X_{1}, X_{2}, \cdots, X_{n}$  是一列独立同分布的随机变量序列且  $E(X_{1}) = 0$ ,  $\sigma^{2} = E(X_{1}^{2}) < \infty$ . 则由 Chebyshev 不等式, 我们可证  $\frac{1}{n} \sum_{i=1}^{n} X_{i}^{2} \xrightarrow{P} \sigma^{2}, \bar{X}_{n} \xrightarrow{P} 0$ . 由连续映射定理可知  $\bar{X}_{n}^{2} \xrightarrow{P} 0$ . 进一步, 由 Slutsky 定理可知

$$
S _ {n} ^ {2} = \frac {1}{n - 1} \sum_ {i = 1} ^ {n} (X _ {i} - \bar {X} _ {n}) ^ {2} = \frac {n}{n - 1} \left(\frac {1}{n} \sum_ {i = 1} ^ {n} X _ {i} ^ {2} - \bar {X} _ {n} ^ {2}\right) \xrightarrow {\mathrm{P}} \sigma^ {2}.
$$

由连续映射定理可知 $S_{n}\xrightarrow{\mathrm{p}}\sigma$ 由中心极限定理可知， $\sqrt{n}\bar{X}_n\xrightarrow{\mathrm{d}}N(0,\sigma^2)$ 因此，由Slutsky定理可知 $t$ 统计量 $\sqrt{n}\bar{X}_n / S_n\xrightarrow{\mathrm{d}}N(0,1)$

最后, 我们给出如下关于  $o_{p}$  和  $O_{p}$  的结论:

$$
o _ {p} (1) + o _ {p} (1) = o _ {p} (1), o _ {p} (1) + O _ {p} (1) = O _ {p} (1), O _ {p} (1) o _ {p} (1) = o _ {p} (1),
$$

$$
\left[ 1 + o _ {p} (1) \right] ^ {- 1} = O _ {p} (1), o _ {p} \left(R _ {n}\right) = R _ {n} o _ {p} (1),
$$

$$
O _ {p} \left(R _ {n}\right) = R _ {n} O _ {p} (1), o _ {p} \left(O _ {p} (1)\right) = o _ {p} (1).
$$

## A.3 大数定律与中心极限定理

本节给出关于独立随机变量序列求和的大数定理. 本节定理的证明参见 Billingsley (1995).

定义A.3.1 设 $\{X_{n}\}$ 为随机变量序列且有有限的期望 $E(X_{n})$ .如果

$$
\frac {1}{n} \sum_ {i = 1} ^ {n} \left[ X _ {i} - E (X _ {i}) \right] \xrightarrow {\mathrm{p}} 0, \tag {A.3.1}
$$

则称 $\{X_{n}\}$ 满足（弱）大数定律.如果

$$
\frac {1}{n} \sum_ {i = 1} ^ {n} \left[ X _ {i} - E (X _ {i}) \right] \stackrel {\mathrm{a.s.}} {\rightarrow} 0, \tag {A.3.2}
$$

则称  $\{X_{n}\}$  满足强大数定律.

定理 A.3.1 假设  $\{X_{n}\}$  是一列独立同分布的随机变量序列, 则

(1) (Khinchin (辛钦) 大数定律) 弱大数定律成立的充要条件是  $E(X_{n}) = a$  有限;
(2) 如果  $E(X_{n}) = a$  有限, 则强大数定律成立.

下面给出一些独立但并不同分布的大数定律.

定理 A.3.2 假设  $\{X_{n}\}$  是一列期望有限的随机变量序列且  $E(X_{i})=\mu_{i},\mathrm{Var}(X_{i})=\sigma_{i}^{2}$ .

(1) 假设  $X_{1}, X_{2}, \cdots, X_{n}$  互不相关,  $\lim_{n\to\infty}\frac{1}{n^{2}}\sum_{i=1}^{n}\sigma_{i}^{2}=0$ , 则

$$
\frac {1}{n} \sum_ {i = 1} ^ {n} X _ {i} - \frac {1}{n} \sum_ {i = 1} ^ {n} \mu_ {i} \xrightarrow {\mathrm{p}} 0.
$$

(2) 假设  $X_{1}, X_{2}, \cdots, X_{n}$  独立,  $\sum_{i=1}^{\infty} \sigma_{i}^{2}/c_{i}^{2} < \infty$ , 其中  $c_{i} \rightarrow \infty$  且严格单增, 则

$$
c _ {n} ^ {- 1} \sum_ {i = 1} ^ {n} (X _ {i} - \mu_ {i}) \stackrel {\text {a.s.}} {\rightarrow} 0.
$$

(3) 假设  $X_{1}, X_{2}, \cdots, X_{n}$  独立且  $\mu_{i} = \mu, \sum_{i=1}^{\infty} \sigma_{i}^{-2} = \infty$ ，则

$$
\sum_ {i = 1} ^ {n} \frac {X _ {i}}{\sigma_ {i}} / \sum_ {i = 1} ^ {n} \sigma_ {i} ^ {- 2} \stackrel {{\text {a.s.}}} {{\rightarrow}} \mu .
$$

例 A.3.1 假设  $(X_{i}, Y_{i}), i = 1, 2, \cdots, n$  是一列独立同分布的二元随机变量且  $E(X_{1}) = \mu_{1}, E(Y_{1}) = \mu_{2}, \operatorname{Var}(X_{1}) = \sigma_{1}^{2}, \operatorname{Var}(Y_{1}) = \sigma_{2}^{2}, \operatorname{Cor}(X_{1}, Y_{1}) = \rho.$  设样本相关系数为

$$
r _ {n} = \frac {\frac {1}{n} \sum X _ {i} Y _ {i} - \bar {X} \bar {Y}}{\sqrt {\left(\sum \frac {X _ {i} ^ {2}}{n} - \bar {X} ^ {2}\right) \left(\sum \frac {Y _ {i} ^ {2}}{n} - \bar {Y} ^ {2}\right)}}.
$$

则由大数定律和连续映射定理知 $r_n \stackrel{\mathrm{a.s.}}{\rightarrow} \frac{E(X_1Y_1) - \mu_1\mu_2}{\sigma_1^2\sigma_2^2} = \rho$.

下面我们介绍常用的中心极限定理. 首先介绍独立同分布假设条件下的中心极限定理.

定理 A.3.3 (Lindeberg-Lévy (林德伯格-莱维) 定理) 假设  $X_{1}, X_{2}, \cdots, X_{n}$  独立同分布且  $E(X) = \mu, \operatorname{Var}(X) = \sigma^{2} < \infty$ ，则

$$
\frac {\sqrt {n} (\bar {X} - \mu)}{\sigma} \xrightarrow {\mathrm{d}} N (0, 1). \tag {A.3.3}
$$

例 A.3.2 设  $X_{1}, X_{2}, \cdots, X_{n}$  是一列独立同分布的随机变量序列.  $E(X_{1}) = \mu$ ,  $\mathrm{Var}(X_{1}) = \sigma^{2}$ ,  $E(X_{1}^{4}) = \mu_{4} < \infty$ . 则对于样本方差  $S_{n}^{2}$ , 我们有

$$
\sqrt {n} \left(S _ {n} ^ {2} - \sigma^ {2}\right) = \sqrt {n} \left[ \frac {1}{n - 1} \sum_ {i = 1} ^ {n} \left(X _ {i} - \mu\right) ^ {2} - \sigma^ {2} \right] - \sqrt {n} \frac {n}{n - 1} \left(\bar {X} _ {n} - \mu\right) ^ {2}.
$$

由定理 A.3.3 知右边第一项渐近服从  $N(0, \mu_{4} - \sigma^{4})$ . 由大数定律知第二项依概率收敛到 0. 故由 Slutsky 定理知

$$
\sqrt {n} \left(S _ {n} ^ {2} - \sigma^ {2}\right) \xrightarrow {\mathrm{d}} N \left(0, \mu_ {4} - \sigma^ {4}\right).
$$

定理 A.3.4（多元中心极限定理） 假设  $X_{1}, X_{2}, \cdots, X_{n}$  独立同分布且  $E(X) = \mu, \operatorname{Var}(X) = \Sigma$ ，则

$$
\sqrt {n} (\overline {{\boldsymbol {X}}} - \boldsymbol {\mu}) \xrightarrow {\mathrm{d}} N _ {p} (\boldsymbol {0}, \Sigma). \tag {A.3.4}
$$

对于独立但不同分布的情况, 我们有如下定理.

定理 A.3.5 (Lindeberg-Feller (林德伯格-费勒) 定理) 假设 $\{X_{n}\}$ 是一列期望

为 $\mu_{n}$, 方差 $\sigma_{n}^{2}$ 有限的随机变量序列. 设 $F_{i}(x)$ 是 $X_{i}$ 的累积分布函数, $s_{n}^{2} = \sum_{i=1}^{n} \sigma_{i}^{2}$. 如果对于任意的 $\varepsilon > 0$,

$$
\frac {1}{s _ {n} ^ {2}} \sum_ {j = 1} ^ {n} \int_ {| x - \mu_ {j} | > \varepsilon s _ {n}} (x - \mu_ {j}) ^ {2} \mathrm{d} F _ {j} (x) \rightarrow 0, \tag {A.3.5}
$$

则

$$
\frac {\sum_ {i = 1} ^ {n} \left(X _ {i} - \mu_ {i}\right)}{s _ {n}} \xrightarrow {\mathrm{d}} N (0, 1).
$$

条件 (A.3.5) 称为 Lindeberg-Feller 条件. 一般来说, Lindeberg-Feller 条件比较难验证. 下面有一个更加容易验证的条件——Lyapunov (李雅普诺夫) 条件 (A.3.6).

定理A.3.6 (Lyapunov定理) 假设 $\{X_{n}\}$ 是一列期望为 $\mu_{n}$, 方差 $\sigma_{n}^{2}$ 有限的随机变量序列. 设 $s_n^2 = \sum_{i=1}^{n} \sigma_i^2$. 如果存在 $\delta > 0$, 使得

$$
\frac {1}{s _ {n} ^ {2 + \delta}} \sum_ {j = 1} ^ {n} E [ | X _ {j} - \mu_ {j} | ^ {2 + \delta} ] \to 0, \tag {A.3.6}
$$

则

$$
\frac {\sum_ {i = 1} ^ {n} \left(X _ {i} - \mu_ {i}\right)}{s _ {n}} \xrightarrow {\mathrm{d}} N (0, 1).
$$

例 A.3.3 设  $X_{i} \sim B(1, p_{i})$  且  $X_{1}, X_{2}, \cdots, X_{n}$  独立. 则

$$
\begin{array}{l} \sum_ {i = 1} ^ {n} E [ | X _ {i} - E (X _ {i}) | ^ {3} ] = \sum_ {i = 1} ^ {n} [ (1 - p _ {i}) ^ {3} p _ {i} + p _ {i} ^ {3} (1 - p _ {i}) ] \\ \leqslant 2 s _ {n} ^ {2} = 2 \sum_ {i = 1} ^ {n} E [ | X _ {i} - E (X _ {i}) | ^ {2} ] = 2 \sum_ {i = 1} ^ {n} p _ {i} \left(1 - p _ {i}\right). \\ \end{array}
$$

如果存在常数 $c_{1}, c_{2}$ 使得 $0 < c_{1} < p_{i} < c_{2} < 1$, 则 $s_{n}^{2} \to \infty$ 且 Lyapunov 条件成立. 从而 $\frac{\sum_{i=1}^{n}(X_i - p_i)}{s_n} \xrightarrow{\mathrm{d}} N(0,1)$.

对于非等权的求和式, 我们有如下中心极限定理.

定理 A.3.7 (Hajek-Šidák 定理) 假设  $X_{1}, X_{2}, \cdots, X_{n}$  是一列独立同分布的随机变量序列.  $E(X) = \mu, \operatorname{Var}(X) = \sigma^{2} < \infty$ . 设  $c_{n} = (c_{n1}, c_{n2}, \cdots, c_{nn})$  是一组向量满足当  $n \to \infty$  时,

$$
\max _ {1 \leqslant i \leqslant n} \frac {c _ {n i} ^ {2}}{\sum_ {j = 1} ^ {n} c _ {n j} ^ {2}} \to 0, \tag {A.3.7}
$$

则

$$
\frac {\sum_ {i = 1} ^ {n} c _ {n i} \left(X _ {i} - \mu\right)}{\sigma \sqrt {\sum_ {j = 1} ^ {n} c _ {n j} ^ {2}}} \xrightarrow {\mathrm{d}} N (0, 1).
$$

同样地, 我们有如下多元 Lindeberg-Feller 定理.

定理 A.3.8 假设  $X_{i}, i=1,2,\cdots,n$  是一列独立的多元随机变量序列.  $E(\boldsymbol{X}_{i})=\boldsymbol{\mu}_{i}, \operatorname{Var}(\boldsymbol{X}_{i})=\Sigma_{i}.$   $X_{i}$  的累积分布函数为  $F_{i}.$  如果当  $n\to\infty$  时,  $\frac{1}{n}\sum_{i=1}^{n}\Sigma_{i}\to\Sigma$  且对任意的  $\varepsilon>0,$

$$
\frac {1}{n} \sum_ {j = 1} ^ {n} \int_ {\| \boldsymbol {x} - \boldsymbol {\mu} _ {j} \| > \varepsilon \sqrt {n}} \left\| \boldsymbol {x} - \boldsymbol {\mu} _ {j} \right\| ^ {2} \mathrm{d} F _ {j} (\boldsymbol {x}) \to 0,
$$

则

$$
\frac {1}{\sqrt {n}} \sum_ {i = 1} ^ {n} (\boldsymbol {X} _ {i} - \boldsymbol {\mu} _ {i}) \xrightarrow {\mathrm{d}} N (\boldsymbol {0}, \Sigma).
$$

## A.4 Delta 方法

如果统计量  $T_{n}$  服从渐近正态分布, 那么对于连续函数  $g(x), g(T_{n})$  是否仍然具有渐近正态性? 下面的 Delta 定理给出了相应的结论.

定理A.4.1 (Delta定理) 假设统计量 $T_{n}$ 满足 $\sqrt{n}(T_n - \theta)\xrightarrow{\mathrm{d}}N\left(0,\sigma^2 (\theta)\right)$. 实数空间上函数 $g(x)$ 在 $\theta$ 处一阶可导且 $g^{\prime}(\theta)\neq 0$. 则

$$
\sqrt {n} \left[ g \left(T _ {n}\right) - g (\theta) \right] \xrightarrow {\mathrm{d}} N \left(0, \left[ g ^ {\prime} (\theta) \right] ^ {2} \sigma^ {2} (\theta)\right).
$$

证明 由 $T_{n}$ 的渐近正态性假设知 $T_{n} - \theta = o_{p}(1)$. 因此由Taylor展开知

$$
g \left(T _ {n}\right) = g (\theta) + \left(T _ {n} - \theta\right) g ^ {\prime} (\theta) + o _ {p} \left(T _ {n} - \theta\right).
$$

等式两边同时乘 $\sqrt{n}$ 可得

$$
\sqrt {n} \left[ g \left(T _ {n}\right) - g (\theta) \right] = \sqrt {n} \left(T _ {n} - \theta\right) g ^ {\prime} (\theta) + \sqrt {n} o _ {p} \left(T _ {n} - \theta\right).
$$

由于 $\sqrt{n}(T_n - \theta) = O_p(1)$, 因此 $\sqrt{n} o_p(T_n - \theta) = o_p(1)$. 由 Slutsky 定理得知

$$
\sqrt {n} \left[ g \left(T _ {n}\right) - g (\theta) \right] \xrightarrow {\mathrm{d}} N \left(0, \left[ g ^ {\prime} (\theta) \right] ^ {2} \sigma^ {2} (\theta)\right).
$$

当  $g'(\theta)=0$  时， $g(T_{n})$  的渐近分布则由 Taylor 展开的更高阶项决定.

定理A.4.2 假设统计量 $T_{n}$ 满足 $\sqrt{n}(T_n - \theta)\stackrel{\mathrm{d}}{\to}N\left(0,\sigma^2 (\theta)\right)$. 实数空间上函数 $g(x)$ 在 $\theta$ 处 $k$ 阶可导且 $g^{(k)}(\theta)\neq 0,g^{(j)}(\theta) = 0,j < k.$ 则

$$
(\sqrt {n}) ^ {k} \left[ g \left(T _ {n}\right) - g (\theta) \right] \xrightarrow {\mathrm{d}} \frac {1}{k !} g ^ {(k)} (\theta) \left[ N \left(0, \sigma^ {2} (\theta)\right) \right] ^ {k}.
$$

定理 A.4.2 的证明类似于定理 A.4.1 的证明, 区别在于利用了高阶 Taylor 展开式. 具体证明过程留作练习.

例 A.4.1 设  $X_{1}, X_{2}, \cdots, X_{n}$  是一列独立同分布的随机变量.  $E(X) = \mu, \operatorname{Var}(X) = \sigma^{2} < \infty$ . 定义  $T_{n} = \bar{X}_{n}, \theta = \mu, \sigma^{2}(\theta) = \sigma^{2}, g(x) = x^{2}$ . 当  $\mu \neq 0$  时,  $g'(\theta) = 2\mu \neq 0$ . 由定理 A.4.1 知

$$
\sqrt {n} \left(\bar {X} _ {n} ^ {2} - \mu^ {2}\right) \xrightarrow {\mathrm{d}} N \left(0, 4 \mu^ {2} \sigma^ {2}\right).
$$

当 $\mu = 0$ 时，$g'(\theta) = 0, g''(\theta) = 2$，由定理A.4.2知，$n\bar{X}_n^2 / \sigma^2 \xrightarrow{\mathrm{d}} \chi_1^2$.

类似地, 我们有多元 Delta 定理.

定理A.4.3 设 $\{\pmb{T}_n\}$ 是一列 $p$ 维随机向量满足 $\sqrt{n} (\pmb{T}_n - \pmb{\theta})\xrightarrow{\mathrm{d}}N_p(\mathbf{0},\Sigma (\pmb {\theta}))$ .函数 $g:\mathbb{R}^p\to \mathbb{R}^m$ 在 $\pmb{\theta}$ 处一阶可导，导数为 $\nabla g(\pmb {\theta})$ .如果 $[\nabla g(\pmb {\theta})]^{\mathrm{T}}\Sigma (\pmb {\theta})\nabla g(\pmb {\theta})$ 正定，则

$$
\sqrt {n} \left[ g \left(\boldsymbol {T} _ {n}\right) - g (\boldsymbol {\theta}) \right] \xrightarrow {\mathrm{d}} N _ {m} \left(\boldsymbol {0}, [ \nabla g (\boldsymbol {\theta}) ] ^ {\mathrm{T}} \Sigma (\boldsymbol {\theta}) \nabla g (\boldsymbol {\theta})\right).
$$

定理 A.4.3 的证明类似于一元 Delta 定理, 留作练习.

例 A.4.2 设  $X_{1}, X_{2}, \cdots, X_{n}$  是一列独立同分布的随机变量.  $E(X) = \mu, \operatorname{Var}(X) = \sigma^{2} < \infty, \mu_{3} = E(X^{3}) < \infty, \mu_{4} = E(X^{4}) < \infty.$  则由定理 A.4.3 可知,

$$
\sqrt {n} \binom{\bar {X} _ {n} - \mu}{S _ {n} ^ {2} - \sigma^ {2}} \xrightarrow {\mathrm{d}} N _ {2} \left(\binom{0}{0}, \left( \begin{array}{c c} \sigma^ {2} & \mu_ {3} \\ \mu_ {3} & \mu_ {4} - \sigma^ {4} \end{array} \right)\right).
$$

故  $\bar{X}_{n}$  与  $S_{n}^{2}$  渐近独立的一个充分条件是  $\mu_{3}=0$ .

## A.5 常见重要概率不等式

除了 Chebyshev 不等式和 Markov 不等式外, 本节给出一些常见的重要概率不等式. 这些不等式在统计学的理论分析中运用非常广泛.

定理 A.5.1 (Cantelli 不等式) 若 X 是一个随机变量, 其方差为  $\sigma^{2} \in (0, \infty)$ , 则对于  $\lambda > 0$ ,

$$
P (X - E (X) \geqslant \lambda) \leqslant \frac {\sigma^ {2}}{\sigma^ {2} + \lambda^ {2}}.
$$

证明 令 $Y = X - E(X)$, 并令 $u \geqslant 0$. 那么

$$
\begin{array}{l} P (X - E (X) \geqslant \lambda) = P (Y + u \geqslant \lambda + u) \leqslant P \left((Y + u) ^ {2} \geqslant (\lambda + u) ^ {2}\right) \\ \leqslant \frac {E \left[ (Y + u) ^ {2} \right]}{(\lambda + u) ^ {2}} = \frac {\sigma^ {2} + u ^ {2}}{(\lambda + u) ^ {2}}, \\ \end{array}
$$

令  $\mu = \sigma^{2}/\lambda,$  则不等式成立.

Cantelli 不等式是对 Chebyshev 不等式单边尾部的改进. 若选取  $\lambda = \sigma$ , 我们可以通过 Cantelli 不等式得到  $P(X \geqslant E(X) + \sigma) \leqslant \frac{1}{2}$  和  $P(X \leqslant E(X) - \sigma) \leqslant \frac{1}{2}$ . 因此, Cantelli 不等式表明, 随机变量的平均数和中位数的差不会超过一个标准差.

定理 A.5.2 (Cauchy 不等式) 设 X, Y 为任意两个随机变量, 若  $E(X^{2}) < \infty$ ,  $E(Y^{2}) < \infty$ , 则有

$$
\left[ E (X Y) \right] ^ {2} \leqslant E \left(X ^ {2}\right) E \left(Y ^ {2}\right).
$$

证明 设 $g(t) = E[(tX - Y)^2] = t^2 E(X^2) - 2tE(XY) + E(Y^2)$. 因为对任意的 $t, (tX - Y)^2 \geqslant 0, g(t) \geqslant 0$, 故

$$
\Delta = [ 2 E (X Y) ] ^ {2} - 4 E \left(X ^ {2}\right) E \left(Y ^ {2}\right) \leqslant 0.
$$

所以

$$
\left[ E (X Y) \right] ^ {2} \leqslant E \left(X ^ {2}\right) E \left(Y ^ {2}\right),
$$

当且仅当 $tX = Y$ 时等号成立.

![](images/page_349_image_9.jpg)

例 A.5.1 Cauchy 不等式在数理统计中的一个具体应用是在计算相关系数的上、下界时. 相关系数是两个随机变量之间线性关系的度量, 其定义为

$$
\rho_ {X Y} = \frac {E \left[ (X - \mu_ {X}) (Y - \mu_ {Y}) \right]}{\sigma_ {X} \sigma_ {Y}},
$$

其中， $\mu_{X}$  和  $\mu_{Y}$  分别是随机变量 X 和 Y 的期望， $\sigma_{X}$  和  $\sigma_{Y}$  是它们的标准差。根据 Cauchy 不等式，我们有

$$
\left\{E \left[ (X - \mu_ {X}) (Y - \mu_ {Y}) \right] \right\} ^ {2} \leqslant E \left[ (X - \mu_ {X}) ^ {2} \right] E \left[ (Y - \mu_ {Y}) ^ {2} \right],
$$

即

$$
(\rho_ {X Y}) ^ {2} \leqslant 1.
$$

因此, 我们得到了相关系数的上、下界:  $-1 \leqslant \rho_{XY} \leqslant 1$ .

定理 A.5.3 (Jensen 不等式) 设 X 为随机变量,  $\psi$  为一个凸函数, 则

$$
\psi (E (X)) \leqslant E [ \psi (X) ].
$$

证明 由凸函数的定义知,

$$
\psi (X) \geqslant \psi (E (X)) + c [ X - E (X) ],
$$

其中 $c$ 是某个常数. 对不等式两边取期望可得

$$
E [ \psi (X) ] \geqslant \psi (E (X)) + c [ E (X) - E (X) ] = \psi (E (X)).
$$

反之, 如果  $\psi$  是一个凹函数, 则  $E[\psi(X)] \leqslant \psi(E(X))$ .

![](images/page_349_image_24.jpg)

例A.5.2 设 $X$ 是一个正的随机变量. 我们来讨论 $E(X^a)$ 与 $[E(X)]^a$ 的大小关系. 首先,

$$
E \left(X ^ {a}\right) = 1 = [ E (X) ] ^ {a}, \qquad \text {如果} a = 0,
$$

$$
E \left(X ^ {a}\right) = E (X) = [ E (X) ] ^ {a}, \text {如果} a = 1.
$$

当 a < 0 或者 a > 1 时,  $\psi(x) = x^{a}$  是一个凸函数. 当 0 < a < 1 时,  $\psi(x)$  是一个凹函数. 故由 Jensen 不等式, 有

$$
E \left(X ^ {a}\right) \geqslant [ E (X) ] ^ {a}, \quad \text {如果} a <   0 \text {或者} a > 1,
$$

$$
E \left(X ^ {a}\right) \leqslant [ E (X) ] ^ {a}, \quad \text {如果} 0 <   a <   1.
$$

特别地, 当 $a = 2$ 时, $E(X^2) \geqslant [E(X)]^2$, 即 $\operatorname{Var}(X) \geqslant 0$.

Hölder (赫尔德) 不等式是 Cauchy 不等式的推广. 在概率论中, 我们常用如下形式的 Hölder 不等式.

定理 A.5.4 (Hölder 不等式) 假设 $p, q \in (1, \infty)$ 且 $\frac{1}{p} + \frac{1}{q} = 1$. 对随机变量 $X, Y$, 若 $E(|X|^p) < \infty, E(|Y|^q) < \infty$, 有

$$
E (| X Y |) \leqslant [ E (| X | ^ {p}) ] ^ {\frac {1}{p}} [ E (| Y | ^ {q}) ] ^ {\frac {1}{q}}.
$$

证明 首先, 如果 $E(|X|^p) = 0$ 或 $E(|Y|^q) = 0$, 那么 Hölder 不等式显然成立. 因此, 我们可以假设 $E(|X|^p) > 0$ 且 $E(|Y|^q) > 0$. 然后, 我们可以利用 Young (杨) 不等式 (Young's inequality) 来证明 Hölder 不等式. Young 不等式的形式为: 对于任意的正数 $a, b, p, q$, 其中 $1/p + 1/q = 1$, 有

$$
a b \leqslant \frac {a ^ {p}}{p} + \frac {b ^ {q}}{q}.
$$

取 $a = |X| / [E(|X|^p)]^{\frac{1}{p}}, b = |Y| / [E(|Y|^q)]^{\frac{1}{q}}$，将它们代入Young不等式，得到

$$
\frac {| X Y |}{[ E (| X | ^ {p}) ] ^ {\frac {1}{p}} [ E (| Y | ^ {q}) ] ^ {\frac {1}{q}}} \leqslant \frac {| X | ^ {p}}{p E (| X | ^ {p})} + \frac {| Y | ^ {q}}{q E (| Y | ^ {q})}.
$$

不等式两边取期望可得

$$
\frac {E (| X Y |)}{[ E (| X | ^ {p}) ] ^ {\frac {1}{p}} [ E (| Y | ^ {q}) ] ^ {\frac {1}{q}}} \leqslant \frac {E (| X | ^ {p})}{p E (| X | ^ {p})} + \frac {E (| Y | ^ {q})}{q E (| Y | ^ {q})} = 1.
$$

即证.

□

Hölder 不等式的一个推论是 Minkowski (闵可夫斯基) 不等式.

定理 A.5.5 (Minkowski 不等式) 对随机变量 X, Y, 若  $E(|X|^{p}) < \infty$ ,  $E(|Y|^{p}) < \infty$ , 其中  $1 \leqslant p < \infty$ , 有

$$
[ E \left(| X + Y | ^ {p}\right) ] ^ {\frac {1}{p}} \leqslant [ E \left(| X | ^ {p}\right) ] ^ {\frac {1}{p}} + [ E \left(| Y | ^ {p}\right) ] ^ {\frac {1}{p}}.
$$

证明 首先, 我们可以将不等式左侧中括号内的和式变形, 即把一个和式写成两个和式之和的形式:

$$
\begin{array}{l} E \left(| X + Y | ^ {p}\right) = E \left[ (X + Y) (X + Y) ^ {p - 1} \right] \\ = E \left[ X (X + Y) ^ {p - 1} \right] + E \left[ Y (X + Y) ^ {p - 1} \right]. \\ \end{array}
$$

然后, 我们可以对上式右端两个和式都应用 Hölder 不等式. 因此, 我们有

$$
E \left[ X (X + Y) ^ {p - 1} \right] \leqslant \left[ E \left(| X | ^ {p}\right) \right] ^ {\frac {1}{p}} \left\{E \left[ \left| (X + Y) ^ {p - 1} \right| ^ {q} \right] \right\} ^ {\frac {1}{q}},
$$

$$
E \left[ Y (X + Y) ^ {p - 1} \right] \leqslant [ E \left(| Y | ^ {p}\right) ] ^ {\frac {1}{p}} \left\{E \left[ \left| (X + Y) ^ {p - 1} \right| ^ {q} \right] \right\} ^ {\frac {1}{q}}
$$

其中 $1 / p + 1 / q = 1$ 将上述两个不等式相加，我们得到

$$
\begin{array}{l} E \left(| X + Y | ^ {p}\right) \\ \leqslant \left[ E \left(| X | ^ {p}\right) \right] ^ {\frac {1}{p}} \left\{E \left[ \left| (X + Y) ^ {p - 1} \right| ^ {q} \right] \right\} ^ {\frac {1}{q}} + \left[ E \left(| Y | ^ {p}\right) \right] ^ {\frac {1}{p}} \left\{E \left[ \left| (X + Y) ^ {p - 1} \right| ^ {q} \right] \right\} ^ {\frac {1}{q}} \\ = \left\{\left[ E \left(| X | ^ {p}\right) \right] ^ {\frac {1}{p}} + \left[ E \left(| Y | ^ {p}\right) \right] ^ {\frac {1}{p}} \right\} \left\{E \left[ \left| (X + Y) ^ {p - 1} \right| ^ {q} \right] \right\} ^ {\frac {1}{q}}. \\ \end{array}
$$

由于 $\left\{E\left[\left|(X + Y)^{p - 1}\right|^q\right]\right\}^{\frac{1}{q}} = [E(|X + Y|^p)]^{\frac{1}{q}}$ ，我们得到

$$
[ E \left(| X + Y | ^ {p}\right) ] ^ {\frac {1}{p}} \leqslant [ E \left(| X | ^ {p}\right) ] ^ {\frac {1}{p}} + [ E \left(| Y | ^ {p}\right) ] ^ {\frac {1}{p}}.
$$

对于有界独立随机变量之和, Hoeffding (霍夫丁) 不等式给出了偏离其期望的概率的上界.

定理 A.5.6 (Hoeffding 不等式) 若随机变量  $X_{1}, X_{2}, \cdots, X_{n}$  是独立的，且每个  $X_{i}$  在区间  $[a_{i}, b_{i}]$  上取值，则对于任意  $\varepsilon > 0$  和  $S_{n} = \sum_{i=1}^{n} X_{i}$ ,

$$
\begin{array}{l} P \left(S _ {n} - E \left(S _ {n}\right) \geqslant \varepsilon\right) \leqslant \exp \left\{- \frac {2 \varepsilon^ {2}}{\sum_ {i = 1} ^ {n} \left(b _ {i} - a _ {i}\right) ^ {2}} \right\}, \\ P \left(S _ {n} - E \left(S _ {n}\right) \leqslant - \varepsilon\right) \leqslant \exp \left\{- \frac {2 \varepsilon^ {2}}{\sum_ {i = 1} ^ {n} \left(b _ {i} - a _ {i}\right) ^ {2}} \right\}. \\ \end{array}
$$

证明 在证明Hoeffding不等式之前，先证明一个Hoeffding引理:对于一个随机变量 $X, P(X \in [a, b]) = 1, E(X) = 0$ ，有

$$
E \left(\mathrm{e} ^ {s X}\right) \leqslant \exp \left\{\frac {1}{8} s ^ {2} (b - a) ^ {2} \right\}.
$$