例1（随机相位周期过程）设 $s(t)$ 是一周期为 $T$ 的函数，$\Theta$ 是在 $(0, T)$ 上服从均匀分布的随机变量，称 $X(t) = s(t + \Theta)$ 为随机相位周期过程。试讨论它的平稳性。

解 由假设, $\Theta$ 的概率密度为

$$
f (\theta) = \left\{ \begin{array}{l l} 1 / T, & \theta \in (0, T), \\ 0, & \text {其他}. \end{array} \right.
$$

于是， $X(t)$ 的均值函数为

$$
\begin{array}{l} E [ X (t) ] = E [ s (t + \Theta) ] \\ = \int_ {0} ^ {T} s (t + \theta) \frac {1}{T} \mathrm{d} \theta = \frac {1}{T} \int_ {t} ^ {t + T} s (\varphi) \mathrm{d} \varphi . \\ \end{array}
$$

利用 $s(\varphi)$ 的周期性可知

$$
E [ X (t) ] = \frac {1}{T} \int_ {0} ^ {T} s (\varphi) \mathrm{d} \varphi
$$

是常数. 而自相关函数

$$
\begin{array}{l} R _ {X} (t, t + \tau) = E [ s (t + \Theta) s (t + \tau + \Theta) ] \\ = \int_ {0} ^ {T} s (t + \theta) s (t + \tau + \theta) \frac {1}{T} \mathrm{d} \theta = \frac {1}{T} \int_ {t} ^ {t + T} s (\varphi) s (\varphi + \tau) \mathrm{d} \varphi . \\ \end{array}
$$

同样, 利用 $s(\varphi)s(\varphi + \tau)$ 的周期性, 可知自相关函数仅与 $\tau$ 有关. 所以随机相位周期过程是平稳的. 特别, 第十二章 §2 例 2 中的随机相位正弦波是平稳的. □

例 2(随机电报信号) 信号  $X(t)$  由只取 I 或 -I 的电流给出(图 14-1 画出了  $X(t)$  的一条样本曲线), 这里

$$
P \{X (t) = I \} = P \{X (t) = - I \} = 1 / 2.
$$

而正负号在区间 $(t,t+\tau)$ 内变化的次数 $N(t,t+\tau)$ 是随机的，且假设 $N(t,t+\tau)$ 服从泊松分布，亦即事件

![](images/page_352_chart_15.jpg)

<details>
<summary>line</summary>

| Time (t) | Value (x(t)) |
| --- | --- |
| 0 | I |
| 1 | -I |
| 2 | I |
| 3 | -I |
| 4 | I |
| 5 | -I |
| 6 | I |
| 7 | -I |
| 8 | I |
| 9 | -I |
| 10 | I |
| 11 | -I |
| 12 | I |
| 13 | -I |
| 14 | I |
| 15 | -I |
| 16 | I |
| 17 | -I |
| 18 | I |
| 19 | -I |
| 20 | I |
| 21 | -I |
| 22 | I |
| 23 | -I |
| 24 | I |
| 25 | -I |
| 26 | I |
| 27 | -I |
| 28 | I |
| 29 | -I |
| 30 | I |
| 31 | -I |
| 32 | I |
| 33 | -I |
| 34 | I |
| 35 | -I |
| 36 | I |
| 37 | -I |
| 38 | I |
| 39 | -I |
| 40 | I |
| 41 | -I |
| 42 | I |
| 43 | -I |
| 44 | I |
| 45 | -I |
| 46 | I |
| 47 | -I |
| 48 | I |
| 49 | -I |
| 50 | I |
| 51 | -I |
| 52 | I |
| 53 | -I |
| 54 | I |
| 55 | -I |
| 56 | I |
| 57 | -I |
| 58 | I |
| 59 | -I |
| 60 | I |
| 61 | -I |
| 62 | I |
| 63 | -I |
| 64 | I |
| 65 | -I |
| 66 | I |
| 67 | -I |
| 68 | I |
| 69 | -I |
| 70 | I |
| 71 | -I |
| 72 | I |
| 73 | -I |
| 74 | I |
| 75 | -I |
| 76 | I |
| 77 | -I |
| 78 | I |
| 79 | -I |
| 80 | I |
| 81 | -I |
| 82 | I |
| 83 | -I |
| 84 | I |
| 85 | -I |
| 86 | I |
| 87 | -I |
| 88 | I |
| 89 | -I |
| 90 | I |
| 91 | -I |
| 92 | I |
| 93 | -I |
| 94 | I |
| 95 | -I |
| 96 | I |
| 97 | -I |
| 98 | I |
| 99 | -I |
| 100 | I |
| 101 | -I |
| 102 | I |
| 103 | -I |
| 104 | I |
| 105 | -I |
| 106 | I |
| 107 | -I |
| 108 | I |
| 109 | -I |
| 110 | I |
| 111 | -I |
| 112 | I |
| 113 | -I |
| 114 | I |
| 115 | -I |
| 116 | I |
| 117 | -I |
| 118 | I |
| 119 | -I |
| 120 | I |
| 121 | -I |
| 122 | I |
| 123 | -I |
| 124 | I |
| 125 | -I |
| 126 | I |
| 127 | -I |
| 128 | I |
| 129 | -I |
| 130 | I |
| 131 | -I |
| 132 | I |
| 133 | -I |
| 134 | I |
| 135 | -I |
| 136 | I |
| 137 | -I |
| 138 | I |
| 139 | -I |
| 140 | I |
| 141 | -I |
| 142 | I |
| 143 | -I |
| 144 | I |
| 145 | -I |
| 146 | I |
| 147 | -I |
| 148 | I |
| 149 | -I |
| 150 | I |
| 151 | -I |
| 152 | I |
| 153 | -I |
| 154 | I |
| 155 | -I |
| 156 | I |
| 157 | -I |
| 158 | I |
| 159 | -I |
| 160 | I |
| 161 | -I |
| 162 | I |
| 163 | -I |
| 164 | I |
| 165 | -I |
| 166 | I |
| 167 | -I |
| 168 | I |
| 169 | -I |
| 170 | I |
| 171 | -I |
| 172 | I |
| 173 | -I |
| 174 | I |
| 175 | -I |
| 176 | I |
| 177 | -I |
| 178 | I |
| 179 | -I |
| 180 | I |
| 181 | -I |
| 182 | I |
| 183 | -I |
| 184 | I |
| 185 | -I |
| 186 | I |
| 187 | -I |
| 188 | I |
| 189 | -I |
| 190 | I |
| 191 | -I |
| 192 | I |
| 193 | -I |
| 194 | I |
| 195 | -I |
| 196 | I |
| 197 | -I |
| 198 | I |
| 199 | -I |
| 200 | I |

*Note: The chart shows a square wave signal with constant amplitude between approximately ±2.5 and ±2.5, and zero amplitude between ±2.5 and ±2.5.*
</details>

图14-1

$$
A _ {k} = \{N (t, t + \tau) = k \}
$$

的概率为

$$
P (A _ {k}) = \frac {(\lambda \tau) ^ {k}}{k !} \mathrm{e} ^ {- \lambda \tau}, \quad k = 0, 1, 2, \dots ,
$$

其中 $\lambda > 0$ 是单位时间内变号次数的数学期望. 试讨论 $X(t)$ 的平稳性.

解 显然, $E[X(t)]=0$ . 现在来计算  $R_{X}(t,t+\tau)=E[X(t)X(t+\tau)]$ . 先设  $\tau>0$ , 注意到如果电流在  $(t,t+\tau)$  内变号偶数次, 则  $X(t)$  和  $X(t+\tau)$  同号且乘积为  $I^{2}$ ; 如果变号奇数次, 则乘积为  $-I^{2}$ . 因为事件

$$
\{X (t) X (t + \tau) = I ^ {2} \}
$$

的概率为  $P(A_{0}) + P(A_{2}) + P(A_{4}) + \cdots$ ，而事件

$$
\{X (t) X (t + \tau) = - I ^ {2} \}
$$

的概率为  $P(A_{1}) + P(A_{3}) + P(A_{5}) + \cdots$ ，于是

$$
\begin{array}{l} R _ {X} (t, t + \tau) = E [ X (t) X (t + \tau) ] = I ^ {2} \sum_ {k = 0} ^ {\infty} P (A _ {2 k}) - I ^ {2} \sum_ {k = 0} ^ {\infty} P (A _ {2 k + 1}) \\ = I ^ {2} \mathrm{e} ^ {- \lambda \tau} \sum_ {k = 0} ^ {\infty} \frac {(- \lambda \tau) ^ {k}}{k !} = I ^ {2} \mathrm{e} ^ {- 2 \lambda \tau}. \\ \end{array}
$$

注意,上述结果与 t 无关.若  $\tau<0$ , 只需令  $s=t+\tau$ , 则有

$$
R _ {X} (t, t + \tau) = R _ {X} (s, s - \tau) = I ^ {2} \mathrm{e} ^ {2 \lambda \tau}.
$$

故这一过程的自相关函数

$$
R _ {X} (t, t + \tau) {\stackrel {\text {记成}} {=}} R _ {X} (\tau) = I ^ {2} \mathrm{e} ^ {- 2 \lambda | \tau |}
$$

只与  $\tau$  有关. 其图形如图 14-2 所示. 因此, 随机电报信号是一平稳过程. ☐

![](images/page_353_chart_17.jpg)

<details>
<summary>contour</summary>

| \(\tau\) | \(R_X(\tau)\) |
| --- | --- |
| 0 | ~0.1 |
| O | \(I^{2}\) |
| >O | ~0.1 |
</details>

图14-2

## § 2 各态历经性

本节主要讨论根据试验记录确定平稳过程的均值和自相关函数的理论依据和方法.

首先注意,如果按照数学期望的定义来计算平稳过程  $X(t)$  的数字特征,就需要预先确定  $X(t)$  的一族样本函数或一维、二维分布函数,但这实际上是不易办到的.事实上,即使我们用统计试验方法,例如可以把均值和自相关函数近似地表示为

$$
\mu_ {X} \approx \frac {1}{N} \sum_ {k = 1} ^ {N} x _ {k} (t _ {1}),
$$

$$
R _ {X} (t _ {2} - t _ {1}) \approx \frac {1}{N} \sum_ {k = 1} ^ {N} x _ {k} (t _ {1}) x _ {k} (t _ {2}),
$$

那也需要对一个平稳过程重复进行大量观察，以便获得数量很多的一族样本函数  $x_{k}(t), k=1,2,\cdots,N$ ，而这正是实际困难所在。

但是,平稳过程的统计特性是不随时间的推移而变化的,于是我们自然期望在一个很长时间内观察得到的一个样本曲线,可以作为得到这个过程的数字特征的充分依据.本节给出的各态历经定理将证实:对平稳过程而言,只要满足一些较宽的条件,那么集平均(均值和自相关函数等)实际上可以用一个样本函数在整个时间轴上的平均值来代替.这样,在解决实际问题时就节约了大量的工作量.

在叙述各态历经性之前,我们先简要地介绍往后多处要遇到的有关随机过程积分的概念.

给定二阶矩过程 $\{X(t), t \in T\}$, 如果它的每一个样本函数在 $[a, b] \subset T$ 上的积分都存在, 我们就说随机过程 $X(t)$ 在 $[a, b]$ 上的积分存在, 并记为

$$
Y = \int_ {a} ^ {b} X (t) \mathrm{d} t. \tag {2.1}
$$

显然， $Y$ 是一随机变量.

但是,在某些情形下,对于随机过程的所有样本函数来说,在 $[a,b]$ 上的积分未必全都存在.此时,引入所谓均方意义上的积分,即考虑 $[a,b]$ 内的一组分点

$$
a = t _ {0} <   t _ {1} <   t _ {2} <   \dots <   t _ {n} = b,
$$

且记

$$
\Delta t _ {i} = t _ {i} - t _ {i - 1}, \quad \tau_ {i} \in [ t _ {i - 1}, t _ {i} ], \quad i = 1, 2, \dots , n,
$$

如果有满足

$$
\lim _ {\max \Delta t _ {i} \to 0} E \Big \{\Big [ Y - \sum_ {i = 1} ^ {n} X (\tau_ {i}) \Delta t _ {i} \Big ] ^ {2} \Big \} = 0
$$

的随机变量 $Y$ 存在, 则称 $Y$ 为 $X(t)$ 在 $[a, b]$ 上的均方积分①, 并仍以符号(2.1)记之. 可以证明: 二阶矩过程 $X(t)$ 在 $[a, b]$ 上的均方积分存在的充分条件是自相关函数的二重积分, 即

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">① 设  $X_{1}, X_{2}, \cdots, X_{n}, \cdots$  是一随机变量序列，如果存在随机变量  $X_{0}$ ，使</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$\lim_{n\to \infty}E[(X_n - X_0)^2 ] = 0,$</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">则称 $X_0$ 是 $X_{n}$ 的均方极限，记为l.i.m. $X_{n} = X_{0}$. 本章出现的涉及随机过程的极限和积分都应在均方意义下理解. 但我们约定仍以记号“lim”替代“l.i.m.”，请读者注意. 有关这方面的进一步知识（即随机分析的内容）超出本书的要求.</span></small>

$$
\int_ {a} ^ {b} \int_ {a} ^ {b} R _ {X} (s, t) \mathrm{d} s \mathrm{d} t
$$

存在. 而且此时还有

$$
E (Y) = \int_ {a} ^ {b} E [ X (t) ] \mathrm{d} t \tag {2.2}
$$

成立. 就是说, 过程 $X(t)$ 的积分均值等于过程的均值函数的积分.

现在引入随机过程 $X(t)$ 沿整个时间轴上的两种时间平均

$$
\langle X (t) \rangle = \lim _ {T \to \infty} \frac {1}{2 T} \int_ {- T} ^ {T} X (t) \mathrm{d} t \tag {2.3}
$$

和

$$
\langle X (t) X (t + \tau) \rangle = \lim _ {T \to \infty} \frac {1}{2 T} \int_ {- T} ^ {T} X (t) X (t + \tau) \mathrm{d} t, \tag {2.4}
$$

分别称为随机过程 $X(t)$ 的时间均值和时间相关函数. 我们可以沿用高等数学中的方法求积分和极限, 其结果一般来说是随机的.

以下讨论时间平均与集平均之间的关系. 先看一个例子.

例(随机相位正弦波) 计算随机相位正弦波  $X(t)=a\cos(\omega t+\Theta)$  的时间均值  $\langle X(t)\rangle$  和时间相关函数  $\langle X(t)X(t+\tau)\rangle$ .

解 $\langle X(t)\rangle = \lim_{T\to \infty}\frac{1}{2T}\int_{-T}^{T}a\cos (\omega t + \Theta)\mathrm{d}t = \lim_{T\to \infty}\frac{a\cos\Theta\sin\omega T}{\omega T} = 0,$

$$
\langle X (t) X (t + \tau) \rangle = \lim _ {T \to \infty} \frac {1}{2 T} \int_ {- T} ^ {T} a ^ {2} \cos (\omega t + \Theta) \cos [ \omega (t + \tau) + \Theta ] \mathrm{d} t = \frac {a ^ {2}}{2} \cos \omega \tau . \quad \square
$$

与第十二章 §2 例 2 比较可知

$$
\mu_ {X} = E [ X (t) ] = \langle X (t) \rangle ,
$$

$$
R _ {X} (\tau) = E [ X (t) X (t + \tau) ] = \langle X (t) X (t + \tau) \rangle .
$$

这表明对于随机相位正弦波,用时间平均与集平均分别算得的均值和自相关函数是相等的.这一特性并不是随机相位正弦波所独有的.下面引入一般概念.

定义(各态历经性) 设  $X(t)$  是一平稳过程.

$1^{\circ}$ 如果

$$
\langle X (t) \rangle = E [ X (t) ] = \mu_ {X} \tag {2.5}
$$

以概率1成立，则称过程 $X(t)$ 的均值具有各态历经性.

$2^{\circ}$  如果对任意实数  $\tau$ ,

$$
\langle X (t) X (t + \tau) \rangle = E [ X (t) X (t + \tau) ] = R _ {X} (\tau) \tag {2.6}
$$

以概率1成立，则称过程 $X(t)$ 的自相关函数具有各态历经性.特别当 $\tau = 0$ 时，称均方值具有各态历经性.

$3^{\circ}$ 如果 $X(t)$ 的均值和自相关函数都具有各态历经性，则称 $X(t)$ 是各态历经过程，或者说 $X(t)$ 是各态历经的.

定义中“以概率1成立”是对 $X(t)$ 的所有样本函数而言的.

各态历经性也称遍历性. 按定义, 上例中的随机相位正弦波是各态历经过程. 当然, 并不是任意一个平稳过程都具有各态历经性. 例如平稳过程

$$
X (t) = Y,
$$

其中 $Y$ 是方差异于零的随机变量, 就不是各态历经过程. 事实上, $\langle X(t) \rangle = \langle Y \rangle = Y$, 亦即时间均值随 $Y$ 取不同可能值而不同. 因 $Y$ 的方差异于零, 这样 $\langle X(t) \rangle$ 就不可能以概率 1 等于常数 $E[X(t)] = E(Y)$.

一个平稳过程应该满足怎样的条件才是各态历经的呢？下面两个定理从理论上回答了这个问题.

定理1(均值各态历经定理) 平稳过程 $X(t)$ 的均值具有各态历经性的充要条件是

$$
\lim _ {T \to \infty} \frac {1}{T} \int_ {0} ^ {2 T} \left(1 - \frac {\tau}{2 T}\right) [ R _ {X} (\tau) - \mu_ {X} ^ {2} ] \mathrm{d} \tau = 0. \tag {2.7}
$$

证 先计算 $\langle X(t)\rangle$ 的均值与方差. 由(2.3)式

$$
E \big [ \langle X (t) \rangle \big ] = E \bigg [ \lim _ {T \to \infty} \frac {1}{2 T} \int_ {- T} ^ {T} X (t) \mathrm{d} t \bigg ],
$$

交换极限与期望的运算顺序，并注意到 $E[X(t)] = \mu_X$ ，即有

$$
E \big [ \langle X (t) \rangle \big ] = \lim _ {T \to \infty} \frac {1}{2 T} \int_ {- T} ^ {T} E \big [ X (t) \big ] \mathrm{d} t = \mu_ {X}.
$$

而 $\langle X(t)\rangle$ 的方差为

$$
\begin{array}{l} D [ \langle X (t) \rangle ] = E \left\{\left[ \langle X (t) \rangle - \mu_ {X} \right] ^ {2} \right\} \\ = \lim _ {T \to \infty} E \left\{\left[ \frac {1}{2 T} \int_ {- T} ^ {T} X (t) \mathrm{d} t \right] ^ {2} \right\} - \mu_ {X} ^ {2} \\ = \lim _ {T \to \infty} E \left[ \frac {1}{4 T ^ {2}} \int_ {- T} ^ {T} X (t _ {1}) \mathrm{d} t _ {1} \int_ {- T} ^ {T} X (t _ {2}) \mathrm{d} t _ {2} \right] - \mu_ {X} ^ {2} \\ = \lim _ {T \rightarrow \infty} \frac {1}{4 T ^ {2}} \int_ {- T} ^ {T} \int_ {- T} ^ {T} E \left[ X (t _ {1}) X (t _ {2}) \right] \mathrm{d} t _ {1} \mathrm{d} t _ {2} - \mu_ {X} ^ {2}, \\ \end{array}
$$

由 $X(t)$ 的平稳性，$E[X(t_1)X(t_2)] = R_X(t_2 - t_1)$，上式可改写为

$$
D [ \langle X (t) \rangle ] = \lim _ {T \to \infty} \frac {1}{4 T ^ {2}} \int_ {- T} ^ {T} \int_ {- T} ^ {T} R _ {X} (t _ {2} - t _ {1}) \mathrm{d} t _ {1} \mathrm{d} t _ {2} - \mu_ {X} ^ {2}. \tag {2.8}
$$

为了简化上式右端的积分, 引入变量变换  $\tau_{1}=t_{1}+t_{2}$  和  $\tau_{2}=t_{2}-t_{1}$ . 此变换的雅可比(Jacobi)式是

$$
\left| \frac {\partial (t _ {1} , t _ {2})}{\partial (\tau_ {1} , \tau_ {2})} \right| = \frac {1}{2},
$$

而积分区域转化为 $D = \{(\tau_1,\tau_2)\mid -2T\leqslant \tau_1\pm \tau_2\leqslant 2T\}$ .于是(2.8)式中的二重积分用新变量可表示为

$$
\int_ {- T} ^ {T} \int_ {- T} ^ {T} R _ {X} (t _ {2} - t _ {1}) \mathrm{d} t _ {1} \mathrm{d} t _ {2} = \iint_ {D} R _ {X} (\tau_ {2}) \frac {1}{2} \mathrm{d} \tau_ {1} \mathrm{d} \tau_ {2}. \tag {2.9}
$$

注意到被积函数 $R_{X}(\tau_{2})$ 是 $\tau_{2}$ 的偶函数，且与 $\tau_{1}$ 无关，因而积分值为在区域 $G = \{(\tau_1,\tau_2)\mid \tau_1,\tau_2\geqslant 0,\tau_1 + \tau_2\leqslant 2T\}$ （如图14-3所示）上积分值的4倍，即

![](images/page_357_image_6.jpg)

<details>
<summary>text_image</summary>

(1)
t₂
(T,T)
O
t₁
τ₂
G
O
(2T,0)
τ₁
(2)
</details>

图14-3

$$
\begin{array}{l} \int_ {- T} ^ {T} \int_ {- T} ^ {T} R _ {X} (t _ {2} - t _ {1}) \mathrm{d} t _ {1} \mathrm{d} t _ {2} = 4 \iint_ {G} R _ {X} (\tau_ {2}) \frac {1}{2} \mathrm{d} \tau_ {1} \mathrm{d} \tau_ {2} \\ = 2 \int_ {0} ^ {2 T} \mathrm{d} \tau_ {2} \int_ {0} ^ {2 T - \tau_ {2}} R _ {X} (\tau_ {2}) \mathrm{d} \tau_ {1} = 2 \int_ {0} ^ {2 T} (2 T - \tau) R _ {X} (\tau) \mathrm{d} \tau . \\ \end{array}
$$

把这个式子代入(2.8)式就有

$$
\begin{array}{l} D [ \langle X (t) \rangle ] = \lim _ {T \to \infty} \frac {1}{T} \int_ {0} ^ {2 T} \left(1 - \frac {\tau}{2 T}\right) R _ {X} (\tau) \mathrm{d} \tau - \mu_ {X} ^ {2} \\ = \lim _ {T \rightarrow \infty} \frac {1}{T} \int_ {0} ^ {2 T} \left(1 - \frac {\tau}{2 T}\right)\left[ R _ {X} (\tau) - \mu_ {X} ^ {2} \right] \mathrm{d} \tau . \tag {2.10} \\ \end{array}
$$

由第四章 §2 方差的性质 $4^{\circ}$ 知道 $\langle X(t)\rangle = E[\langle X(t)\rangle]$ 以概率1成立的充要条件是 $D[\langle X(t)\rangle] = 0$. 结合(2.10)式, 定理得证. □

推论 在 $\lim_{\tau \to \infty} R_X(\tau)$ 存在的条件下, 若 $\lim_{\tau \to \infty} R_X(\tau) = \mu_X^2$, 则 (2.7) 式成立, 均值具有各态历经性; 若 $\lim_{\tau \to \infty} R_X(\tau) \neq \mu_X^2$, 则 (2.7) 式不成立, 均值不具有各态历经性. (证略.)

注意,对前例中的随机相位正弦波而言, $\lim_{\tau\to\infty}R_{X}(\tau)$ 不存在,但它的均值具有各态历经性.

在定理1的证明中将 $X(t)$ 换成 $X(t)X(t + \tau)$，就可得

定理2(自相关函数各态历经定理) 平稳过程 $X(t)$ 的自相关函数 $R_{X}(\tau)$ 具有各态历经性的充要条件是

$$
\lim _ {T \to \infty} \frac {1}{T} \int_ {0} ^ {2 T} \left(1 - \frac {\tau_ {1}}{2 T}\right) \left[ B (\tau_ {1}) - R _ {X} ^ {2} (\tau) \right] \mathrm{d} \tau_ {1} = 0, \tag {2.11}
$$

其中 $B(\tau_1) = E[X(t)X(t + \tau)X(t + \tau_1)X(t + \tau +\tau_1)]$

在(2.11)式中令 $\tau = 0$ ，就可得到均方值具有各态历经性的充要条件.如若在定理2中以 $X(t)Y(t + \tau)$ 代替 $X(t)X(t + \tau)$ ，以 $R_{XY}(\tau)$ 代替 $R_{X}(\tau)$ 来进行讨论，那么还可以相应地得到互相关函数各态历经性的充要条件.

在实际应用中通常只考虑定义在 $t \in [0, \infty)$ 上的平稳过程，此时上面的所有时间平均都应以 $t \in [0, \infty)$ 上的时间平均来代替，而相应的各态历经定理可表示为下述形式:

定理 3(均值各态历经定理)

$$
\lim _ {T \to \infty} \frac {1}{T} \int_ {0} ^ {T} X (t) \mathrm{d} t = E [ X (t) ] = \mu_ {X}
$$

以概率1成立的充要条件是

$$
\lim _ {T \to \infty} \frac {1}{T} \int_ {0} ^ {T} \left(1 - \frac {\tau}{T}\right) [ R _ {X} (\tau) - \mu_ {X} ^ {2} ] \mathrm{d} \tau = 0. \tag {2.12}
$$

定理4(自相关函数各态历经定理)

$$
\lim _ {T \to \infty} \frac {1}{T} \int_ {0} ^ {T} X (t) X (t + \tau) \mathrm{d} t = E [ X (t) X (t + \tau) ] = R _ {X} (\tau)
$$

以概率1成立的充要条件是

$$
\lim _ {T \to \infty} \frac {1}{T} \int_ {0} ^ {T} \left(1 - \frac {\tau_ {1}}{T}\right) \left[ B (\tau_ {1}) - R _ {X} ^ {2} (\tau) \right] \mathrm{d} \tau_ {1} = 0. \tag {2.13}
$$

各态历经定理的重要价值在于它从理论上给出了如下保证:一个平稳过程 $X(t), t \in [0, \infty)$ ，只要它满足条件(2.12)和(2.13)，便可以根据“以概率1成立”的含义，从一次试验所得到的样本函数 $x(t)$ 来确定出该过程的均值和自相关函数，即

$$
\lim _ {T \to \infty} \frac {1}{T} \int_ {0} ^ {T} x (t) \mathrm{d} t = \mu_ {X} \tag {2.14}
$$

和

$$
\lim _ {T \to \infty} \frac {1}{T} \int_ {0} ^ {T} x (t) x (t + \tau) \mathrm{d} t = R _ {X} (\tau). \tag {2.15}
$$

这就是本节开头所预告的论断.

如果试验记录 $x(t)$ 只在时间区间 $[0, T]$ 上给出，则相应于(2.14)和(2.15)式，有以下无偏估计式:

$$
\mu_ {X} \approx \hat {\mu} _ {X} = \frac {1}{T} \int_ {0} ^ {T} x (t) \mathrm{d} t \tag {2.16}
$$

和

$$
\begin{array}{l} R _ {X} (\tau) \approx \hat {R} _ {X} (\tau) = \frac {1}{T - \tau} \int_ {0} ^ {T - \tau} x (t) x (t + \tau) \mathrm{d} t \\ = \frac {1}{T - \tau} \int_ {\tau} ^ {T} x (t) x (t - \tau) \mathrm{d} t, \quad 0 \leqslant \tau <   T. \tag {2.17} \\ \end{array}
$$

不过在实际问题中一般不可能给出 $x(t)$ 的表达式，因而通常通过模拟方法或数值计算方法来进行估计.

最后指出,各态历经定理的条件是比较宽的,应用中遇到的大多数平稳过程都能够满足.不过,要去验证它们是否成立却是十分困难的.因此在实践中,通常事先假定所研究的平稳过程具有各态历经性,并从这个假定出发,对相关资料进行分析和处理,看所得的结论是否与实际相符.如果不符,则要修改假设,另作处理.

## § 3 相关函数的性质

在第十二章中已经指出，用数字特征来描绘随机过程，要比用分布函数来描绘随机过程更为简便实用。由上节的分析看到，对于具有各态历经性的平稳过程，其均值和相关函数可以用一个样本函数来估计。在这种场合下，利用均值和相关函数来研究随机过程更方便。特别是对于正态平稳过程，它的均值和相关函数能完全地刻画其统计特性。为了方便地使用数字特征去研究随机过程，下面的定理给出了相关函数的主要性质。

定理(相关函数的性质) 设 $X(t)$ 和 $Y(t)$ 是平稳相关过程, $R_{X}(\tau), R_{Y}(\tau), R_{XY}(\tau)$ 分别是它们的自相关函数和互相关函数. 则

$1^{\circ}R_{X}(0) = E[X^{2}(t)] = \Psi_{X}^{2}\geqslant 0.$

$2^{\circ}R_{X}(-\tau) = R_{X}(\tau)$ ，即 $R_{X}(\tau)$ 是偶函数.而互相关函数既不是偶函数也不是奇函数，但满足 $R_{XY}(-\tau) = R_{YX}(\tau)$

$3^{\circ}$ 自相关函数和自协方差函数满足不等式

$$
\left| R _ {X} (\tau) \right| \leqslant R _ {X} (0), \quad \left| C _ {X} (\tau) \right| \leqslant C _ {X} (0) = \sigma_ {X} ^ {2}.
$$

$4^{\circ} R_{X}(\tau)$ 是非负定的，即对任意数组 $t_{1}, t_{2}, \cdots, t_{n} \in T$ 和任意实函数 $g(t)$ 都有

$$
\sum_ {i, j = 1} ^ {n} R _ {X} (t _ {i} - t _ {j}) g (t _ {i}) g (t _ {j}) \geqslant 0.
$$

$5^{\circ}$ 如果平稳过程 $X(t)$ 满足条件 $P\{X(t + T_0) = X(t)\} = 1$ ，则称它为周期是

$T_{0}$ 的平稳过程. 这样的平稳过程的自相关函数也是周期为 $T_{0}$ 的周期函数.

证 $1^{\circ}$ 和 $2^{\circ}$ 可由定义直接推出. 结合柯西一施瓦茨不等式、自相关函数和自协方差函数的定义就可得到 $3^{\circ}$. 根据自相关函数的定义和均值的运算性质，即有

$$
\begin{array}{l} \sum_ {i, j = 1} ^ {n} R _ {X} (t _ {i} - t _ {j}) g (t _ {i}) g (t _ {j}) = \sum_ {i, j = 1} ^ {n} E [ X (t _ {i}) X (t _ {j}) ] g (t _ {i}) g (t _ {j}) \\ = E \left[ \sum_ {i, j = 1} ^ {n} X (t _ {i}) X (t _ {j}) g (t _ {i}) g (t _ {j}) \right] \\ = E \left\{\left[ \sum_ {i = 1} ^ {n} X (t _ {i}) g (t _ {i}) \right] ^ {2} \right\} \geqslant 0. \\ \end{array}
$$

这就证明了 $4^{\circ}$. 最后来证明 $5^{\circ}$. 由平稳性, $E[X(t) - X(t + T_0)] = 0$. 又由第四章 §2 方差的性质, 条件 $P\{X(t + T_0) = X(t)\} = 1$ 与 $E\{[X(t + T_0) - X(t)]^2\} = 0$ 等价. 于是, 由柯西一施瓦茨不等式,

$$
\left\{E \big [ X (t) (X (t + \tau + T _ {0}) - X (t + \tau)) \big ] \right\} ^ {2} \leqslant E \big [ X ^ {2} (t) \big ] E \big \{\big [ X (t + \tau + T _ {0}) - X (t + \tau) \big ] ^ {2} \big \}
$$

右端为零,推知

$$
E \{X (t) [ X (t + \tau + T _ {0}) - X (t + \tau) ] \} = 0,
$$

展开即得 $R_{X}(\tau + T_{0}) = R_{X}(\tau)$.

在下节中将看到 $R_{X}(0)$ 表示平稳过程 $X(t)$ 的“平均功率”. 由性质 $2^{\circ}$, 在实际问题中只需计算或测量 $R_{X}(\tau), R_{Y}(\tau), R_{XY}(\tau)$ 和 $R_{YX}(\tau)$ 在 $\tau \geqslant 0$ 的值.

性质 $3^{\circ}$ 表明自相关函数（自协方差函数）都在 $\tau = 0$ 处取最大值①.类似地，可以推出以下有关互相关函数和互协方差函数的不等式:

$$
\left| R _ {X Y} (\tau) \right| ^ {2} \leqslant R _ {X} (0) R _ {Y} (0), \quad \left| C _ {X Y} (\tau) \right| ^ {2} \leqslant C _ {X} (0) C _ {Y} (0).
$$

在应用上常用的还有标准自协方差函数和标准互协方差函数,它们的定义为

$$
\rho_ {X} (\tau) = \frac {C _ {X} (\tau)}{C _ {X} (0)}, \quad \rho_ {X Y} (\tau) = \frac {C _ {X Y} (\tau)}{\sqrt {C _ {X} (0) C _ {Y} (0)}}.
$$

由上述不等式知: $|\rho_{X}(\tau)|\leqslant 1$ 和 $|\rho_{XY}(\tau)|\leqslant 1.$ 且当 $\rho_{XY}(\tau) = 0$ 时， $X(t)$ 和 $Y(t)$ 不相关.

对于平稳过程而言,自相关函数的非负定性是最本质的.因为理论上可以证明:任一连续函数,只要具有非负定性,就必为某平稳过程的自相关函数.

另外，在实际中各种具有零均值的非周期性噪声和干扰一般当 $|\tau|$ 值适当

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">① 但这并不排除它们在 $\tau \neq 0$ 处也可取到最大值.例如，随机相位正弦波的自相关函数 $R_{X}(\tau) = \frac{a^{2}}{2}\cos \omega \tau$ 在 $\tau = \frac{2k\pi}{\omega}, k = 0, \pm 1, \pm 2, \dots$ 时均取到最大值.</span></small>

增大时， $X(t+\tau)$  和  $X(t)$  即呈现独立或不相关，于是有

$$
\lim _ {\tau \to \infty} R _ {X} (\tau) = \lim _ {\tau \to \infty} C _ {X} (\tau) = 0.
$$

下面是一个应用例子.

例(噪声与信号) 设某接收机输出电压  $V(t)$  是周期信号  $S(t)$  和噪声电压  $N(t)$  之和, 即

$$
V (t) = S (t) + N (t).
$$

又设 $S(t)$ 和 $N(t)$ 是两个互不相关（实际问题中一般都是如此）的各态历经过程，且 $E[N(t)] = 0.$ 根据第十二章 §2(2.12)式，$V(t)$ 的自相关函数应为

$$
R _ {V} (\tau) = R _ {S} (\tau) + R _ {N} (\tau).
$$

由性质 $5^{\circ}, R_{S}(\tau)$ 是周期函数，又因为一般噪声电压 $N(t)$ 当 $|\tau|$ 值适当增大时，$N(t + \tau)$ 和 $N(t)$ 即呈现独立或不相关，即有

$$
\lim _ {\tau \to \infty} R _ {N} (\tau) = 0.
$$

于是,对于充分大的  $\tau$  值有

$$
R _ {V} (\tau) \approx R _ {S} (\tau).
$$

作为特例,假设接收机输出电压中周期信号和噪声电压的自相关函数分别为

$$
R _ {s} (\tau) = \frac {a ^ {2}}{2} \cos \tau \omega ,
$$

$$
R _ {N} (\tau) = b ^ {2} \mathrm{e} ^ {- \alpha | \tau |}, \quad \alpha > 0.
$$

那么即使噪声平均功率(见下节) $R_{N}(0)=b^{2}$ 远大于信号平均功率 $R_{S}(0)=a^{2}/2$ ，当 $|\tau|$ 充分大时，依然有

$$
R _ {V} (\tau) = \frac {a ^ {2}}{2} \cos \tau \omega + b ^ {2} \mathrm{e} ^ {- \alpha | \tau |} \approx \frac {a ^ {2}}{2} \cos \tau \omega .
$$

也就是说我们可以从强噪声中检测到微弱的正弦信号(见图14-4). □

![](images/page_361_chart_19.jpg)

<details>
<summary>line</summary>

| \(\tau\) | \(R_V(\tau)\) |
| --- | --- |
| 0 | High |
| ~1.5 | Low |
| ~3.0 | Medium |
| ~4.5 | Low |
| ~6.0 | Medium |
| ~7.5 | Low |
| ~9.0 | Medium |
| ~10.5 | Low |
</details>

图14-4

## § 4 平稳随机过程的功率谱密度

傅里叶(Fourier)变换是确立时间函数频率结构的有效工具,下面我们来讨论如何运用这一工具来分析平稳过程的频率结构——功率谱密度.

## (一) 平稳过程的功率谱密度

设有时间函数 $x(t), t \in (-\infty, \infty)$ (为了便于理解物理术语, 可把 $x(t)$ 设想

为加于单位电阻上的电压). 如果 $x(t)$ 的总能量有限, 即

$$
\int_ {- \infty} ^ {\infty} x ^ {2} (t) \mathrm{d} t <   \infty , \tag {4.1}
$$

那么， $x(t)$ 的傅里叶变换存在或者说具有频谱

$$
F _ {x} (\omega) = \int_ {- \infty} ^ {\infty} x (t) \mathrm{e} ^ {- \mathrm{i} \omega t} \mathrm{d} t.
$$

且同时有傅里叶逆变换

$$
x (t) = \frac {1}{2 \pi} \int_ {- \infty} ^ {\infty} F _ {x} (\omega) \mathrm{e} ^ {\mathrm{i} \omega t} \mathrm{d} \omega .
$$

$F_{x}(\omega)$ 一般是复函数，其共轭函数为 $F_{x}^{*}(\omega) = F_{x}(-\omega)$. 在 $x(t)$ 和 $F_{x}(\omega)$ 之间成立有帕塞瓦尔(Parseval)等式

$$
\int_ {- \infty} ^ {\infty} x ^ {2} (t) \mathrm{d} t = \frac {1}{2 \pi} \int_ {- \infty} ^ {\infty} | F _ {x} (\omega) | ^ {2} \mathrm{d} \omega ,
$$

等式左边表示 $x(t)$ 在 $(-\infty, \infty)$ 上的总能量，而右边的被积函数 $|F_x(\omega)|^2$ 相应地称为 $x(t)$ 的能谱密度。这样，帕塞瓦尔等式又可理解为总能量的谱表示式。

但是,应用中很多重要的时间函数的总能量是无限的.正弦函数就是一例.平稳过程的样本函数一般来说也是如此.这时我们转而研究 $x(t)$ 在 $(-\infty,\infty)$ 上的平均功率,即

$$
\lim _ {T \to \infty} \frac {1}{2 T} \int_ {- T} ^ {T} x ^ {2} (t) \mathrm{d} t.
$$

在以下讨论中,我们都假定这个平均功率是存在的.

为了用傅里叶变换给出平均功率的谱表示式,先由给定的  $x(t)$  构造一个截尾函数

$$
x _ {T} (t) = \left\{ \begin{array}{l l} x (t), & | t | \leqslant T, \\ 0, & | t | > T. \end{array} \right. \tag {4.2}
$$

易知 $x_{T}(t)$ 满足(4.1).记 $x_{T}(t)$ 的傅里叶变换为

$$
F _ {x} (\omega , T) = \int_ {- \infty} ^ {\infty} x _ {T} (t) \mathrm{e} ^ {- \mathrm{i} \omega t} \mathrm{d} t = \int_ {- T} ^ {T} x (t) \mathrm{e} ^ {- \mathrm{i} \omega t} \mathrm{d} t, \tag {4.3}
$$

并写出它的帕塞瓦尔等式

$$
\int_ {- \infty} ^ {\infty} x _ {T} ^ {2} (t) \mathrm{d} t = \frac {1}{2 \pi} \int_ {- \infty} ^ {\infty} | F _ {x} (\omega , T) | ^ {2} \mathrm{d} \omega ,
$$

将上式两边除以 $2T$ ，并利用 $x_{T}(t)$ 的定义(4.2)，得

$$
\frac {1}{2 T} \int_ {- T} ^ {T} x ^ {2} (t) \mathrm{d} t = \frac {1}{4 \pi T} \int_ {- \infty} ^ {\infty} | F _ {x} (\omega , T) | ^ {2} \mathrm{d} \omega . \tag {4.4}
$$

令 $T\to \infty ,x(t)$ 在 $(-\infty ,\infty)$ 上的平均功率即可表示为

$$
\lim _ {T \to \infty} \frac {1}{2 T} \int_ {- T} ^ {T} x ^ {2} (t) \mathrm{d} t = \frac {1}{2 \pi} \int_ {- \infty} ^ {\infty} \lim _ {T \to \infty} \frac {1}{2 T} | F _ {x} (\omega , T) | ^ {2} \mathrm{d} \omega . \tag {4.5}
$$

类似能谱密度,我们把(4.5)式右端的被积式称作函数  $x(t)$  的平均功率谱密度,简称功率谱密度,并记为

$$
S _ {x} (\omega) = \lim _ {T \to \infty} \frac {1}{2 T} \left| F _ {x} (\omega , T) \right| ^ {2}. \tag {4.6}
$$

而(4.5)的右端就是平均功率的谱表示式.

现在我们把平均功率和功率谱密度的概念推广到平稳过程 $X(t), t \in (-\infty, \infty)$. 为此，相应于(4.3)和(4.4)式写出

$$
F _ {X} (\omega , T) = \int_ {- T} ^ {T} X (t) \mathrm{e} ^ {- \mathrm{i} \omega t} \mathrm{d} t, \tag {4.7}
$$

和

$$
\frac {1}{2 T} \int_ {- T} ^ {T} X ^ {2} (t) \mathrm{d} t = \frac {1}{4 \pi T} \int_ {- \infty} ^ {\infty} \left| F _ {X} (\omega , T) \right| ^ {2} \mathrm{d} \omega . \tag {4.8}
$$

显然，(4.7)和(4.8)式中的积分都是随机的.我们将(4.8)式左端的均值的极限，即

$$
\lim _ {T \to \infty} E \left[ \frac {1}{2 T} \int_ {- T} ^ {T} X ^ {2} (t) \mathrm{d} t \right] \tag {4.9}
$$

定义为平稳过程 $X(t)$ 的平均功率.

交换(4.9)式中积分与均值的运算顺序,并注意到平稳过程的均方值是常数 $\Psi_{X}^{2}$ ,于是

$$
\lim _ {T \to \infty} E \left[ \frac {1}{2 T} \int_ {- T} ^ {T} X ^ {2} (t) \mathrm{d} t \right] = \lim _ {T \to \infty} \frac {1}{2 T} \int_ {- T} ^ {T} E [ X ^ {2} (t) ] \mathrm{d} t = \Psi_ {X} ^ {2}, \tag {4.10}
$$

即平稳过程的平均功率等于该过程的均方值或 $R_{X}(0)$

接着，把(4.8)式的右端代入(4.10)式的左端，交换运算顺序后可得

$$
\Psi_ {X} ^ {2} = \frac {1}{2 \pi} \int_ {- \infty} ^ {\infty} \lim _ {T \to \infty} \frac {1}{2 T} E [ | F _ {X} (\omega , T) | ^ {2} ] \mathrm{d} \omega . \tag {4.11}
$$

相应于(4.5)，(4.6)式，我们把(4.11)式中的被积式称为平稳过程 $X(t)$ 的平均功率谱密度，简称为功率谱密度，并记为 $S_{XX}(\omega)$ 或 $S_{X}(\omega)$，即

$$
S _ {X} (\omega) = \lim _ {T \to \infty} \frac {1}{2 T} E [ | F _ {X} (\omega , T) | ^ {2} ]. \tag {4.12}
$$

利用记号 $S_{X}(\omega)$ ，(4.11)式可简写为

$$
\Psi_ {X} ^ {2} = \frac {1}{2 \pi} \int_ {- \infty} ^ {\infty} S _ {X} (\omega) \mathrm{d} \omega , \tag {4.13}
$$

此式称为平稳过程  $X(t)$  的平均功率的谱表示式.

功率谱密度 $S_{X}(\omega)$ 通常也简称为自谱密度或谱密度①，它是从频率这个角度描述 $X(t)$ 的统计规律的最主要的数字特征.由(4.13)式知，它的物理意义是表示 $X(t)$ 的平均功率关于频率的分布.

## (二) 谱密度的性质

下面的定理给出了谱密度的两个重要性质.

定理(谱密度的性质) 设 $X(t), t \in (-\infty, \infty)$ 为平稳过程. 则

$1^{\circ}S_{X}(\omega)$ 是 $\omega$ 的实的、非负的偶函数.

$2^{\circ}$ 若 $X(t)$ 的自相关函数 $R_{X}(\tau)$ 满足 $\int_{-\infty}^{\infty}|R_X(\tau)|\mathrm{d}\tau <  \infty$ ，则它和 $S_{X}(\omega)$ 构成傅里叶变换对，即

$$
S _ {X} (\omega) = \int_ {- \infty} ^ {\infty} R _ {X} (\tau) \mathrm{e} ^ {- \mathrm{i} \omega \tau} \mathrm{d} \tau , \tag {4.14}
$$

$$
R _ {X} (\tau) = \frac {1}{2 \pi} \int_ {- \infty} ^ {\infty} S _ {X} (\omega) \mathrm{e} ^ {\mathrm{i} \omega \tau} \mathrm{d} \omega . \tag {4.15}
$$

(4.14)和(4.15)式统称为维纳一辛钦(Wiener-Khinchin)公式.而且由于 $R_{X}$ (τ)和 $S_{X}(\omega)$ 都是偶函数,利用欧拉(Euler)公式,它们还可写成

$$
S _ {X} (\omega) = 2 \int_ {0} ^ {\infty} R _ {X} (\tau) \cos \omega \tau \mathrm{d} \tau , \tag {4.16}
$$

$$
R _ {X} (\tau) = \frac {1}{\pi} \int_ {0} ^ {\infty} S _ {X} (\omega) \cos \omega \tau \mathrm{d} \omega . \tag {4.17}
$$

证 在(4.12)式中,量

$$
\mid F _ {X} (\omega , T) \mid^ {2} = F _ {X} (\omega , T) F _ {X} (- \omega , T)
$$

是 $\omega$ 的实的、非负的偶函数，所以它的均值的极限也必是实的、非负的偶函数。这就得到 $1^{\circ}$

为证 $2^{\circ}$, 将(4.7)代入(4.12)式, 得

$$
S _ {X} (\omega) = \lim _ {T \to \infty} \frac {1}{2 T} E \Big [ \int_ {- T} ^ {T} X (t _ {1}) \mathrm{e} ^ {\mathrm{i} \omega t _ {1}} \mathrm{d} t _ {1} \int_ {- T} ^ {T} X (t _ {2}) \mathrm{e} ^ {- \mathrm{i} \omega t _ {2}} \mathrm{d} t _ {2} \Big ].
$$

把括号内的积分乘积改写成重积分形式,交换积分与均值的运算顺序,并注意到

$$
E \big [ X (t _ {1}) X (t _ {2}) \big ] = R _ {X} (t _ {2} - t _ {1}),
$$

即有

$$
S _ {X} (\omega) = \lim _ {T \to \infty} \frac {1}{2 T} \int_ {- T} ^ {T} \int_ {- T} ^ {T} E \big [ X (t _ {1}) X (t _ {2}) \big ] \mathrm{e} ^ {- \mathrm{i} \omega (t _ {2} - t _ {1})} \mathrm{d} t _ {1} \mathrm{d} t _ {2}
$$

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">① 可以指出，平稳过程的总能量为无限，而且能谱密度也不存在，故在平稳过程理论中“谱密度”一词总是指功率谱密度.</span></small>

$$
= \lim _ {T \to \infty} \frac {1}{2 T} \int_ {- T} ^ {T} \int_ {- T} ^ {T} R _ {X} (t _ {2} - t _ {1}) \mathrm{e} ^ {- \mathrm{i} \omega (t _ {2} - t _ {1})} \mathrm{d} t _ {1} \mathrm{d} t _ {2}.
$$

接着，依照 §2 定理 1 的证明，作变量变换 $\tau_{1} = t_{1} + t_{2}, \tau_{2} = t_{2} - t_{1}$，可以得到

$$
\begin{array}{l} S _ {X} (\omega) = \lim _ {T \rightarrow \infty} \int_ {- 2 T} ^ {2 T} \left(1 - \frac {| \tau |}{2 T}\right) R _ {X} (\tau) \mathrm{e} ^ {- \mathrm{i} \omega \tau} \mathrm{d} \tau \\ = \lim _ {T \to \infty} \int_ {- \infty} ^ {\infty} R _ {X} ^ {T} (\tau) \mathrm{e} ^ {- \mathrm{i} \omega \tau} \mathrm{d} \tau , \tag {4.18} \\ \end{array}
$$

式中

$$
R _ {X} ^ {T} (\tau) = \left\{ \begin{array}{l l} \Big (1 - \frac {| \tau |}{2 T} \Big) R _ {X} (\tau), & | \tau | \leqslant 2 T, \\ 0, & | \tau | > 2 T. \end{array} \right.
$$

当 $T \to \infty$ 时，注意到对每个 $\tau, R_X^T(\tau) \to R_X(\tau)$，于是由(4.18)式就可得到公式(4.14). 由傅里叶逆变换的公式即得(4.15)式. □

维纳一辛钦公式又称为平稳过程自相关函数的谱表示式, 它们揭示了从时间角度描述平稳过程  $X(t)$  的统计规律和从频率角度描述  $X(t)$  的统计规律之间的联系. 据此, 在应用上我们可以根据实际情况选择时间域方法或等价的频率域方法. 实际的计算可以利用傅里叶变换手册, 表 14-1 列出了若干个常用的自相关函数以及对应的谱密度.

表14-1

|  | $R_{X}(\tau)$ | $S_{X}(\omega)$ |
| --- | --- | --- |
| 1 | $e^{-a\|\tau\|}$ | $\frac{2a}{a^{2}+\omega^{2}}$ |
| 2 | $\max\{1-\|\tau\|,0\}$ | $\frac{4\sin^{2}(\omega T/2)}{T\omega^{2}}$ |
| 3 | $e^{-a\|\tau\|}\cos\omega_{0}\tau$ | $\frac{a}{a^{2}+(\omega-\omega_{0})^{2}}+\frac{a}{a^{2}+(\omega+\omega_{0})^{2}}$ |
| 4 | $\frac{\sin\omega_{0}\tau}{\omega_{0}\tau}$ | $\chi_{[-\omega_{0},\omega_{0}]}(\omega)$ |
| 5 | 1 | $2\pi\delta(\omega)$ |
| 6 | $\delta(\tau)$ | 1 |
| 7 | $\cos\omega_{0}\tau$ | $\pi\delta(\omega-\omega_{0})+\pi\delta(\omega+\omega_{0})$ |

注: $\chi_{A}$  表示集 A 的特征函数，定义为  $\chi_{A}(\tau)=\left\{\begin{aligned}&1,&\tau\in A,\\ &0,&\tau\notin A.\end{aligned}\right.$

例1 已知平稳过程 $X(t)$ 的自相关函数为

$$
R _ {X} (\tau) = \mathrm{e} ^ {- a | \tau |} \cos \omega_ {0} \tau ,
$$

求 $X(t)$ 的谱密度 $S_{X}(\omega)$.

解 由表14-1可直接查出

$$
S _ {X} (\omega) = \frac {a}{a ^ {2} + (\omega - \omega_ {0}) ^ {2}} + \frac {a}{a ^ {2} + (\omega + \omega_ {0}) ^ {2}}.
$$

例 2 已知平稳过程  $X(t)$  的谱密度

$$
S _ {X} (\omega) = \frac {\omega^ {2} + 4}{\omega^ {4} + 1 0 \omega^ {2} + 9},
$$

求  $X(t)$  的自相关函数和均方值.

解 用查表方法. 先把 $S_{X}(\omega)$ 改写成部分分式之和, 即

$$
S _ {X} (\omega) = \frac {\omega^ {2} + 4}{(\omega^ {2} + 1) (\omega^ {2} + 9)} = \frac {1}{8} \left(\frac {3}{\omega^ {2} + 1 ^ {2}} + \frac {5}{\omega^ {2} + 3 ^ {2}}\right). \tag {4.19}
$$

由于傅里叶逆变换(4.15)也是线性变换,所以可对上式右端两项分别查表14-1第1栏后相加,经整理后得

$$
R _ {X} (\tau) = \frac {1}{4 8} (9 \mathrm{e} ^ {- | \tau |} + 5 \mathrm{e} ^ {- 3 | \tau |}).
$$

而均方值为

$$
\Psi_ {X} ^ {2} = R _ {X} (0) = \frac {7}{2 4}.
$$

形如(4.19)式的谱密度属于有理谱密度.根据谱密度性质 $1^{\circ}$ ，其一般形式应为

$$
S _ {X} (\omega) = S _ {0} \frac {\omega^ {2 n} + a _ {2 n - 2} \omega^ {2 n - 2} + \cdots + a _ {0}}{\omega^ {2 m} + b _ {2 m - 2} \omega^ {2 m - 2} + \cdots + b _ {0}},
$$

式中 $S_0 > 0$。又由于要求均方值有限，所以由(4.13)式还应有 $m > n$，且分母应无实数根。有理谱密度是实用上最常见的一类谱密度。已知有理谱密度要求自相关函数，通常使用例2中的部分分式方法结合查表来进行。

另外,已知平稳过程的自相关函数的估计,由维纳一辛钦公式及数值积分就可以得到谱密度的估计.

最后需要指出的是,在实际问题中常常碰到这样一些平稳过程(例如随机相位正弦波),讨论它们的自相关函数和谱密度需要用到狄拉克(Dirac)的  $\delta$  函数,定义如下:

$$
\left\{ \begin{array}{l} \delta (t) = 0, \quad t \neq 0, \\ \int_ {- \infty} ^ {\infty} \delta (t) \mathrm{d} t = 1. \end{array} \right.
$$

通常用图14-5中的单位有向线段来表示.

δ 函数的最重要的性质是: 对任一在 t=0 连续的函数  $f(t)$ ，有

$$
\int_ {- \infty} ^ {\infty} \delta (t) f (t) \mathrm{d} t = f (0).
$$

一般,若函数  $f(t)$  在  $t=t_{0}$  连续,就有(筛选性)

$$
\int_ {- \infty} ^ {\infty} \delta (t - t _ {0}) f (t) \mathrm{d} t = f (t _ {0}).
$$

据此,可以写出以下傅里叶变换对:

![](images/page_367_image_8.jpg)

<details>
<summary>text_image</summary>

δ(t)
1
O
t
</details>

图14-5

$$
\int_ {- \infty} ^ {\infty} \delta (\tau) \mathrm{e} ^ {- \mathrm{i} \omega \tau} \mathrm{d} \tau = 1 \longleftrightarrow \delta (\tau) = \frac {1}{2 \pi} \int_ {- \infty} ^ {\infty} 1 \cdot \mathrm{e} ^ {\mathrm{i} \omega \tau} \mathrm{d} \omega , \tag {4.20}
$$

$$
\int_ {- \infty} ^ {\infty} \frac {1}{2 \pi} \mathrm{e} ^ {- \mathrm{i} \omega \tau} \mathrm{d} \tau = \delta (\omega) \longleftrightarrow \frac {1}{2 \pi} = \frac {1}{2 \pi} \int_ {- \infty} ^ {\infty} \delta (\omega) \mathrm{e} ^ {\mathrm{i} \omega \tau} \mathrm{d} \omega . \tag {4.21}
$$

(4.21)式表明:当自相关函数 $R_{X}(\tau)=1$ 时,谱密度 $S_{X}(\omega)=2\pi\delta(\omega)$ .其次,还可求得正弦型自相关函数 $R_{X}(\tau)=a\cos\omega_{0}\tau$ 的谱密度为

$$
S _ {X} (\omega) = a \pi [ \delta (\omega - \omega_ {0}) + \delta (\omega + \omega_ {0}) ]. \tag {4.22}
$$

事实上，

$$
\begin{array}{l} S _ {X} (\omega) = \int_ {- \infty} ^ {\infty} a \cos \omega_ {0} \tau \mathrm{e} ^ {- \mathrm{i} \omega \tau} \mathrm{d} \tau \\ = \frac {a}{2} \int_ {- \infty} ^ {\infty} (\mathrm{e} ^ {\mathrm{i} \omega_ {0} \tau} + \mathrm{e} ^ {- \mathrm{i} \omega_ {0} \tau}) \mathrm{e} ^ {- \mathrm{i} \omega \tau} \mathrm{d} \tau \\ = \frac {a}{2} \left[ \int_ {- \infty} ^ {\infty} \mathrm{e} ^ {- \mathrm{i} (\omega - \omega_ {0}) \tau} \mathrm{d} \tau + \int_ {- \infty} ^ {\infty} \mathrm{e} ^ {- \mathrm{i} (\omega + \omega_ {0}) \tau} \mathrm{d} \tau \right], \\ \end{array}
$$

利用变换式(4.21)即得(4.22)式.

由此可见，自相关函数为常数或正弦型函数的平稳过程，其谱密度都是离散的。对应的变换可见表14-1第5,7栏。

例3 求自相关函数

$$
R _ {V} (\tau) = \frac {a ^ {2}}{2} \cos \omega_ {0} \tau + b ^ {2} \mathrm{e} ^ {- a | \tau |}
$$

所对应的谱密度  $S_{V}(\omega)$ .

解 利用傅里叶变换的线性性质及表14-1第1和第7栏即可知道

$$
S _ {V} (\omega) = \frac {\pi a ^ {2}}{2} \big [ \delta (\omega - \omega_ {0}) + \delta (\omega + \omega_ {0}) \big ] + \frac {2 a b ^ {2}}{a ^ {2} + \omega^ {2}}.
$$

相应的谱密度如图14-6所示.此图说明了谱密度是如何表明噪声以外的周期信号的.