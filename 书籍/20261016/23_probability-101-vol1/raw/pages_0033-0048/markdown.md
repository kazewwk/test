(3) 根据加法公式有

$$
\mathbf {P} (E) + \mathbf {P} (F) = \mathbf {P} (E \cup F) + \mathbf {P} (E \cap F) = \frac {\pi l + 2 l}{\pi t}.
$$

因 $\mathbf{P}(E) = \mathbf{P}(F)$ 得

$$
\mathbf {P} (E) = \frac {\pi l + 2 l}{2 \pi t}.
$$

例 1.2.18 参加集会的 n 个人将帽子放在一起, 会后每个人任取一顶帽子戴上. 求  $B_{n}=\{n \text{ 个人中至少一人戴对自己的帽子}\}$  和  $B_{n}^{c}=\{n \text{ 个人中无人戴对自己的帽子}\}$  的概率.

解 将参加集会的人和帽子对应地用数  $1,2,\cdots,n$  编号. 样本空间  $\Omega$  取为这 n 个数的排列  $(r_{1},r_{2},\cdots,r_{n})$  所有可能的形式, 它共有  $n!$  个样本点. 记  $A_{i}=\{ 第 i 个人戴对自己帽子 \}=\{(r_{1},r_{2},\cdots,r_{n}):r_{i}=i\}$ . 则不难算出

$$
\mathbf {P} (A _ {i}) = \frac {(n - 1) !}{n !} = \frac {1}{n} \quad (1 \leqslant i \leqslant n),
$$

$$
\mathbf {P} (A _ {i} A _ {j}) = \frac {1}{n (n - 1)} \quad (1 \leqslant i <   j \leqslant n), \dots .
$$

注意 $B_{n} = \bigcup_{i = 1}^{n}A_{i}$ 根据加法公式，

$$
\begin{array}{l} \mathbf {P} (B _ {n}) = \sum_ {i = 1} ^ {n} \mathbf {P} (A _ {i}) - \sum_ {1 \leqslant i <   j \leqslant n} \mathbf {P} (A _ {i} A _ {j}) + \\ \sum_ {1 \leqslant i <   j <   k \leqslant n} \mathbf {P} (A _ {i} A _ {j} A _ {k}) + \dots + (- 1) ^ {n - 1} \mathbf {P} (A _ {1} A _ {2} \dots A _ {n}) \\ = \sum_ {i = 1} ^ {n} \frac {1}{n} - \sum_ {1 \leqslant i <   j \leqslant n} \frac {1}{n (n - 1)} + \dots + (- 1) ^ {n - 1} \frac {1}{n !} \\ = \frac {1}{1 !} - \frac {1}{2 !} + \dots + (- 1) ^ {n - 1} \frac {1}{n !}, \\ \end{array}
$$

因而

$$
\mathbf {P} (B _ {n} ^ {c}) = 1 - \mathbf {P} (B _ {n}) = \sum_ {i = 0} ^ {n} (- 1) ^ {i} \frac {1}{i !}.
$$

例 1.2.19 在例 1.2.18 的情况下, 求  $E_{n,k} = \{n \text{ 个人中恰有 } k \text{ 个戴对自己的帽子}\}$  的概率.

解 注意 $E_{n,k} = \{(r_1, r_2, \dots, r_n)$: 对 $k$ 个标号 $\alpha$ 有 $r_\alpha = \alpha$ 而对其余 $n - k$ 个标号 $\alpha$ 有 $r_\alpha \neq \alpha\}$. 令 $m(A)$ 为事件 $A \subseteq \Omega$ 所含的样本点的总数. 不难发现 $m(E_{n,k}) = C_n^k m(E_{n-k,0})$. 根据例 1.2.18 的结论有

$$
m (E _ {n - k, 0}) = (n - k)! \boldsymbol {P} (E _ {n - k, 0}) = (n - k)! \sum_ {i = 0} ^ {n - k} (- 1) ^ {i} \frac {1}{i !},
$$

因而

$$
m (E _ {n, k}) = \frac {n !}{k !} \sum_ {i = 0} ^ {n - k} (- 1) ^ {i} \frac {1}{i !}.
$$

所以有

$$
\mathbf {P} (E _ {n, k}) = \frac {1}{k !} \sum_ {i = 0} ^ {n - k} (- 1) ^ {i} \frac {1}{i !}.
$$

## 练习题

1. 假设某个随机试验包含可数无穷多个不同的结果, 且每个结果出现的概率均严格大于零. 解释为何不会所有结果发生的概率都相同.
2. 设 $(\Omega, \mathcal{F})$ 为可测空间. 给定非空集 $E \subseteq \Omega$, 记 $\mathcal{E} = \{E \cap A : A \in \mathcal{F}\}$.

(1) 证明 $\mathcal{E}$ 是 $E$ 上的 $\sigma$ 代数;
(2) 是否有 $\mathcal{E} \subseteq \mathcal{F}$?

3. 设  $(\Omega_{1}, \mathcal{F}_{1}, \mu_{1}), (\Omega_{2}, \mathcal{F}_{2}, \mu_{2}), \cdots, (\Omega_{n}, \mathcal{F}_{n}, \mu_{n})$  是 n 个有限测度空间, 其中  $\Omega_{1}, \Omega_{2}, \cdots, \Omega_{n}$  两两不相交. 令  $\Omega = \bigcup_{k=1}^{n} \Omega_{k}$ .

(1) 证明 $\mathcal{F} := \{A \subseteq \Omega : A \cap \Omega_k \in \mathcal{F}_k, 1 \leqslant k \leqslant n\}$ 是 $\Omega$ 上的 $\sigma$ 代数;
(2) 对 $A \in \mathcal{F}$ 令 $\mu(A) = \sum_{k=1}^{n} \mu_k (A \cap \Omega_k)$. 证明 $\mu$ 是 $(\Omega, \mathcal{F})$ 上的有限测度.

4. 设 $(\Omega, \mathcal{F}, \mathbf{P})$ 为概率空间. 证明对 $A, B \in \mathcal{F}$ 有 $P(A \cap B) \geqslant P(A) + P(B) - 1$.
5. 设事件 $A, B$ 满足 $\mathbf{P}(A) = 3 / 4$ 和 $\mathbf{P}(B) = 1 / 3$. 证明 $1 / 12 \leqslant \mathbf{P}(A \cap B) \leqslant 1 / 3$.
6. 对于随机事件序列 $A_{1}, A_{2}, \cdots \in \mathcal{F}$, 证明: 若对一切 $k \geqslant 1$ 有 $\mathbf{P}(A_k) = 1$, 则 $\mathbf{P}\left(\bigcap_{k=1}^{\infty} A_k\right) = 1$.

## 1.3 条件概率

## 1.3.1 条件概率与乘法公式

定义1.3.1 假设 $(\Omega, \mathcal{F}, \mathbf{P})$ 为概率空间。再设 $B \in \mathcal{F}$ 满足 $\mathbf{P}(B) > 0$。对事件 $A \in \mathcal{F}$ 定义

$$
\mathbf {P} (A | B) = \frac {\mathbf {P} (A B)}{\mathbf {P} (B)}. \tag {1.3.1}
$$

称  $\mathbf{P}(A|B)$  为已知 B 发生的情况下 A 的条件概率.

对 $A \in \mathcal{F}$ 记 $\mathbf{P}_B(A) = \mathbf{P}(A|B)$. 利用 (1.3.1) 式易证 $\mathbf{P}_B$ 也是可测空间 $(\Omega, \mathcal{F})$ 上的概率测度. 我们称 $\mathbf{P}_B$ 为给定事件 $B$ 的条件概率测度, 而称 $(\Omega, \mathcal{F}, \mathbf{P}_B)$ 为给定事件 $B$ 的条件概率空间.

另外, 由 (1.3.1) 式易得下面的乘法公式:

$$
\mathbf {P} (A B) = \mathbf {P} (B) \mathbf {P} (A | B), \quad A, B \in \mathcal {F}. \tag {1.3.2}
$$

为了运算方便, 我们规定当  $\mathbf{P}(B)=0$  时上式右端理解为零. 这样, 对于乘法公式 (1.3.2) 可以不须假定  $\mathbf{P}(B)>0$ .

利用数学归纳法可以证明:

定理 1.3.1 (乘法定理) 对任何  $A_{1}, A_{2}, \cdots, A_{n} \in F$  有

$$
\mathbf {P} (A _ {1} A _ {2} \dots A _ {n}) = \mathbf {P} (A _ {1}) \mathbf {P} (A _ {2} | A _ {1}) \dots \mathbf {P} (A _ {n} | A _ {1} \dots A _ {n - 1}).
$$

基于乘法公式, 有时可以通过条件化和递推方法计算某些复杂的概率.

例 1.3.1 假设 n 对夫妇在 2n 个椅子上随机地就座. 求  $A_{n}=\{丈夫全坐在妻子右方\}$  的概率.

解 将夫妇用数字  $1, 2, \cdots, 2n$  编号. 记  $B_{1} = \{1 号丈夫在妻子右方\}$ ，则

$$
\mathbf {P} (B _ {1}) = \frac {\mathrm{C} _ {2 n} ^ {2} (2 n - 2) !}{(2 n) !} = \frac {1}{2}.
$$

利用乘法公式,

$$
\mathbf {P} (A _ {n}) = \mathbf {P} (A _ {n} | B _ {1}) \mathbf {P} (B _ {1}) = \frac {1}{2} \mathbf {P} (A _ {n - 1}).
$$

利用上面递推关系立得  $\mathbf{P}(A_{n})=1/2^{n}$ .

## 1.3.2 全概率公式

根据之前引入的概念, 如果事件序列  $\{B_{1}, B_{2}, \cdots\} \subseteq F$  两两不交且满足  $\bigcup_{n=1}^{\infty} B_{n} = \Omega$ , 则  $\{B_{1}, B_{2}, \cdots\}$  构成  $\Omega$  的一个可数划分.

定理 1.3.2（全概率公式） 假设  $\{B_{n}\} \subseteq F$  为  $\Omega$  的可数划分. 则对任何  $A \in F$  有

$$
\mathbf {P} (A) = \sum_ {n = 1} ^ {\infty} \mathbf {P} (B _ {n}) \mathbf {P} (A | B _ {n}).
$$

证明 由 $\{B_n\}$ 两两不交知 $\{B_nA\}$ 两两不交. 显然 $A = \bigcup_{n=1}^{\infty} B_n A$. 由可数可加性及乘法公式有

$$
\mathbf {P} (A) = \sum_ {n = 1} ^ {\infty} \mathbf {P} (B _ {n} A) = \sum_ {n = 1} ^ {\infty} \mathbf {P} (B _ {n}) \mathbf {P} (A | B _ {n}).
$$

故得欲证等式.

全概率公式是很常用的公式. 特别地, 当事件 $A$ 的发生涉及某种因素时, 我们往往会根据该因素的不同情况, 分别计算 $A$ 的条件概率, 然后利用全概率公式求得 $\mathbf{P}(A)$. 与乘法公式的情况类似, 当 $\mathbf{P}(B_n) = 0$ 时, 我们规定 $\mathbf{P}(B_n)\mathbf{P}(A|B_n) = 0$, 因此这里不须假定 $\mathbf{P}(B_n) > 0$.

例 1.3.2 设袋中有 r 个红球和 b 个黑球. 每次从袋中任取 1 球, 查看颜色后连同 s 个同色球一起放回. 以  $R_{n}$  表示第 n 次取出红球. 证明  $\mathbf{P}(R_{n}) = r / (r + b)$ .

证明 首先, 容易看出 $\mathbf{P}(R_1) = r / (r + b)$, 即欲证结果对于 1 次摸球试验成立. 假定该结果对于 $n - 1$ 次摸球试验成立. 则

$$
\mathbf {P} (R _ {n} | R _ {1}) = \frac {r + s}{r + s + b}, \quad \mathbf {P} (R _ {n} | R _ {1} ^ {c}) = \frac {r}{r + s + b}.
$$

利用全概率公式, 有

$$
\begin{array}{l} \mathbf {P} (R _ {n}) = \mathbf {P} (R _ {1}) \mathbf {P} (R _ {n} | R _ {1}) + \mathbf {P} (R _ {1} ^ {c}) \mathbf {P} (R _ {n} | R _ {1} ^ {c}) \\ = \frac {r}{r + b} \cdot \frac {r + s}{r + s + b} + \frac {b}{r + b} \cdot \frac {r}{r + s + b} \\ = \frac {r}{r + b}. \\ \end{array}
$$

根据数学归纳法即得结论.

例 1.3.3 甲乙二人轮流掷骰子, 甲先掷, 以后谁掷出 1 点时则交给对方掷, 否则此人继续掷. 求 $A_{n} = \{\text{第 } n \text{ 次由甲掷}\}$ 的概率.

解 记 $p_n = \mathbf{P}(A_n)$. 由题意知 $p_1 = 1$. 利用全概率公式,

$$
\begin{array}{l} p _ {n} = \mathbf {P} (A _ {n - 1}) \mathbf {P} (A _ {n} | A _ {n - 1}) + \mathbf {P} (A _ {n - 1} ^ {c}) \mathbf {P} (A _ {n} | A _ {n - 1} ^ {c}) \\ = \frac {5}{6} p _ {n - 1} + \frac {1}{6} (1 - p _ {n - 1}) = \frac {2}{3} p _ {n - 1} + \frac {1}{6}. \\ \end{array}
$$

根据上面递推关系，

$$
p _ {n} = \frac {2}{3} \Big (\frac {2}{3} p _ {n - 2} + \frac {1}{6} \Big) + \frac {1}{6} = \Big (\frac {2}{3} \Big) ^ {2} p _ {n - 2} + \frac {1}{6} \times \frac {2}{3} + \frac {1}{6} = \dots
$$

$$
\begin{array}{l} = \left(\frac {2}{3}\right) ^ {n - 1} p _ {1} + \frac {1}{6} \sum_ {i = 1} ^ {n - 1} \left(\frac {2}{3}\right) ^ {i - 1} = \left(\frac {2}{3}\right) ^ {n - 1} + \frac {1}{6} \cdot \frac {1 - \left(\frac {2}{3}\right) ^ {n - 1}}{1 - \frac {2}{3}} \\ = \left(\frac {2}{3}\right) ^ {n - 1} + \frac {1}{2} \left[ 1 - \left(\frac {2}{3}\right) ^ {n - 1} \right] = \frac {1}{2} \left[ 1 + \left(\frac {2}{3}\right) ^ {n - 1} \right]. \\ \end{array}
$$

## 1.3.3 贝叶斯公式

首先, 我们看两个例子.

例 1.3.4 某工厂的第 1, 2, 3 车间生产同一产品, 产量比分别为 0.5, 0.25, 0.25, 而次品率分别为 0.01, 0.01, 0.02. 现从这个厂的产品中任取一件, 求取到次品的概率.

解 令 $A = \{$ 取到一件次品 $\}$ 和 $B_{i} = \{$ 取到的产品来自第 $i$ 车间 $\}$. 由题意有

$$
\begin{array}{l} \mathbf {P} (B _ {1}) = 0. 5, \quad \mathbf {P} (B _ {2}) = 0. 2 5, \quad \mathbf {P} (B _ {3}) = 0. 2 5, \\ \mathbf {P} (A | B _ {1}) = 0. 0 1, \mathbf {P} (A | B _ {2}) = 0. 0 1, \mathbf {P} (A | B _ {3}) = 0. 0 2. \\ \end{array}
$$

再根据全概率公式,

$$
\begin{array}{l} \mathbf {P} (A) = \mathbf {P} (B _ {1}) \mathbf {P} (A | B _ {1}) + \mathbf {P} (B _ {2}) \mathbf {P} (A | B _ {2}) + \mathbf {P} (B _ {3}) \mathbf {P} (A | B _ {3}) \\ = 0. 5 \times 0. 0 1 + 0. 2 5 \times 0. 0 1 + 0. 2 5 \times 0. 0 2 = 0. 0 1 2 5. \\ \end{array}
$$

例 1.3.5 在例 1.3.4 的解答中, 假定  $A = \{$  取到一件次品 \}, 则在全概率公式的基础上利用条件概率定义得到

$$
\mathbf {P} (B _ {1} | A) = \frac {\mathbf {P} (A B _ {1})}{\mathbf {P} (A)} = \frac {\mathbf {P} (B _ {1}) \mathbf {P} (A | B _ {1})}{\mathbf {P} (A)} = \frac {0 . 5 \times 0 . 0 1}{0 . 0 1 2 5} = 0. 4.
$$

由前面例子中的计算过程可以总结出一个重要的概率计算公式. 这就是下面定理给出的贝叶斯 (Bayes) 公式.

定理 1.3.3（贝叶斯公式）设  $\{B_{1}, B_{2}, \cdots\} \subseteq F$  为  $\Omega$  的一个划分，而  $A \in F$  满足  $\mathbf{P}(A) > 0$ 。则对任何  $n \geqslant 1$  有

$$
\mathbf {P} (B _ {n} | A) = \frac {\mathbf {P} (B _ {n}) \mathbf {P} (A | B _ {n})}{\mathbf {P} (A)} = \frac {\mathbf {P} (B _ {n}) \mathbf {P} (A | B _ {n})}{\sum_ {k = 1} ^ {\infty} \mathbf {P} (B _ {k}) \mathbf {P} (A | B _ {k})}.
$$

例 1.3.6 医学中的诊断错误包括完全漏诊和完全误诊: 把有病诊断为无病称为完全漏诊; 把无病诊断为有病称为完全误诊. 假设通过验血诊断某种疾病的完全误诊率和完全漏诊率分别仅为 $1\%$ 和 $3\%$. 也就是说, 若记

$$
A = \{\text {验血结果为阳性} \}, \quad B = \{\text {受检者患此病} \},
$$

则有 $\mathbf{P}(A|B^c) = 0.01$ 和 $\mathbf{P}(A^c |B) = 0.03$. 再设 $\mathbf{P}(B) = 0.005$. 分别求 $\mathbf{P}(B|A)$ 和 $\mathbf{P}(B|A^c)$.

解 首先, 由全概率公式,

$$
\begin{array}{l} \mathbf {P} (A) = \mathbf {P} (B) \mathbf {P} (A | B) + \mathbf {P} (B ^ {c}) \mathbf {P} (A | B ^ {c}) \\ = 0. 0 0 5 \times (1 - 0. 0 3) + (1 - 0. 0 0 5) \times 0. 0 1 \\ = 0. 0 0 4 8 5 + 0. 0 0 9 9 5 = 0. 0 1 4 8, \\ \end{array}
$$

故有 $\mathbf{P}(A^c) = 0.9852$. 再由贝叶斯公式有

$$
\mathbf {P} (B | A) = \frac {\mathbf {P} (B) \mathbf {P} (A | B)}{\mathbf {P} (A)} = \frac {0 . 0 0 5 \times (1 - 0 . 0 3)}{0 . 0 1 4 8} = \frac {0 . 0 0 4 8 5}{0 . 0 1 4 8} \approx 0. 3 2 8
$$

和

$$
\mathbf {P} (B | A ^ {c}) = \frac {\mathbf {P} (B) \mathbf {P} (A ^ {c} | B)}{\mathbf {P} (A ^ {c})} = \frac {0 . 0 0 5 \times 0 . 0 3}{0 . 9 8 5 2} = \frac {0 . 0 0 0 1 5}{0 . 9 8 5 2} \approx 0. 0 0 0 1 5 2.
$$

在上例中, 由于总患病率 $\mathbf{P}(B) = 0.005$ 很低, 化验结果为阳性时, 受检者实际患病的条件概率 $\mathbf{P}(B|A) = 0.328$ 并不很大. 同样的原因导致, 化验结果为阴性时, 受检者实际患病的条件概率 $\mathbf{P}(B|A^c) = 0.000152$ 非常小.

## \*1.3.4 蒙提霍尔问题

有个请嘉宾选择奖品的游戏, 主办方在编号为 1, 2, 3 的三个门中等可能地随机选择一个, 放入一辆跑车, 另两个门里各放一只山羊. 节目的嘉宾不知道哪个门里是跑车. 主持人请嘉宾选择一个门, 门后的奖品由他获得. 嘉宾当然希望选中跑车!

问题 假如你是嘉宾, 选择了 1 号门, 在此门打开之前, 主持人首先打开了余下的门中的一个有山羊的门, 并给你重新选择的机会. 不妨假设他打开的是 3 号门, 你是坚持选 1 号门? 还是改选 2 号门?

这个问题来源于一个著名的电视节目, 曾经引起广泛关注和讨论, 被称为蒙提霍尔 (Monty Hall) 问题. 下面用两种方法给出问题的解答.

解 解法 1 因为放跑车的门是等可能随机抽取的, 所以 1 号门里有跑车的概率为 1/3, 有山羊的概率为 2/3. 如果决策是不改选, 那么你在 1 号门里有跑车的情况下获得跑车, 你成功的概率为 1/3; 如果决策是换 2 号门, 那么你在 1 号门里有山羊的情况下获得跑车, 你成功的概率为 2/3. 所以, 你应该改变选择.

解法2 按照假设你已经选择了1号门. 用 $A_{1}, A_{2}, A_{3}$ 分别表示1,2,3号门里有跑车, 用 $B_{1}, B_{2}, B_{3}$ 分别表示主持人打开1,2,3号门. 因为你在选择1号门时不知道车在哪个门里, 你的选择不影响跑车在三个门里的概率, 所以

$$
\mathbf {P} (A _ {1}) = \mathbf {P} (A _ {2}) = \mathbf {P} (A _ {3}) = \frac {1}{3}. \tag {1.3.3}
$$

主持人打开 1 号门之外一个放山羊的门, 有以下几种可能的情况:

(1) 跑车在 1 号门里, 主持人有 2, 3 号门可以打开, 故  $\mathbf{P}(B_{3}|A_{1})=1/2;$
(2) 跑车在 2 号门里, 主持人只有 3 号门可以打开, 故  $\mathbf{P}(B_{3}|A_{2})=1$ ;
(3) 跑车在 3 号门里, 主持人只有 2 号门可以打开, 故  $\mathbf{P}(B_{3}|A_{3})=0$ .

利用全概率公式, 主持人打开 3 号门的概率为

$$
\mathbf {P} (B _ {3}) = \sum_ {i = 1} ^ {3} \mathbf {P} (A _ {i}) \mathbf {P} (B _ {3} | A _ {i}) = \frac {1}{3} \times \left(\frac {1}{2} + 1 + 0\right) = \frac {1}{2}.
$$

再根据贝叶斯公式, 在 3 号门打开的情况下 1 号和 2 号门里有跑车的条件概率分别为

$$
\mathbf {P} (A _ {1} | B _ {3}) = \frac {\mathbf {P} (A _ {1}) \mathbf {P} (B _ {3} | A _ {1})}{\mathbf {P} (B _ {3})} = \frac {1}{3} \tag {1.3.4}
$$

和

$$
\mathbf {P} (A _ {2} | B _ {3}) = \frac {\mathbf {P} (A _ {2}) \mathbf {P} (B _ {3} | A _ {2})}{\mathbf {P} (B _ {3})} = \frac {2}{3}. \tag {1.3.5}
$$

通过比较发现, 改选 2 号门是正确的决策.

上面利用贝叶斯公式计算条件概率的解答方法包含了重要的思想. 在统计推断中, 称 (1.3.3) 式中的概率为先验概率, 而称 (1.3.4) 式和 (1.3.5) 式中的条件概率为后验概率. 后验概率是根据主持人打开有山羊的 3 号门这个信息, 对于前面的先验概率的修正.

这种通过获得信息利用贝叶斯公式得到后验概率, 并根据后验概率改进决策的过程非常近似于人类的学习模式, 也是贝叶斯方法许多应用的关键. 正是由于这个特点, 贝叶斯方法在机器学习领域发挥了重要作用, 已经成为学习型人工智能的理论基础.

## 练习题

1. 对于事件 $A$ 和 $B$, 证明: 若 $\mathbf{P}(A|B) > \mathbf{P}(A)$, 则 $\mathbf{P}(B|A) > \mathbf{P}(B)$.

2. 假设有三个事件 A, B 和 C.

(1) 已知 $\mathbf{P}(A|C) > \mathbf{P}(B|C)$ 和 $\mathbf{P}(A|C^c) > \mathbf{P}(B|C^c)$. 问是否一定有 $\mathbf{P}(A) > \mathbf{P}(B)$? 若是, 加以证明; 否则举出反例.
(2) 已知 $\mathbf{P}(A|C) > \mathbf{P}(A|C^c)$ 和 $\mathbf{P}(B|C) > \mathbf{P}(B|C^c)$. 问是否一定有 $\mathbf{P}(A) > \mathbf{P}(B)$? 若是, 加以证明; 否则举出反例.

3. 考试中的一道多选题共有 5 个选项, 某同学知道正确答案的概率为 $p$, 他在不知道答案时猜中答案的概率为 $1/5$.

(1) 求该同学做对一道多选题的概率;
(2) 设对某道题该同学选对了答案. 求他确实知道正确答案的概率.

4. 盒子里有 15 个乒乓球, 其中 9 个是新球. 第一场比赛时从中取出了 3 个用完后放回盒中. 第二场比赛时再从中取出 3 个, 求这 3 个都是新球的概率.
5. 在信号传递中发送信号 “0” 或 “1” 占比分别为 1/3 和 2/3. 由于外界干扰等原因, 接收到的信号可能出现错误. 已知出错的概率为 0.05. 设接收到的信号为 “1”, 求发送的信号确实为 “1” 的概率.
6. 盒子里有标号为  $0,1,\cdots,k$  的  $k+1$  枚不均匀的硬币. 已知投掷第 i 号硬币正面朝上的概率为 i/k. 从盒中随机取一枚硬币重复投掷. 设前 n 次投掷的结果都是正面朝上. 求第  $n+1$  次也是正面朝上的概率.

## 1.4 事件的独立性

随机事件和随机试验的独立性是非常重要的概念. 首先考虑两个随机事件的独立性.

## 1.4.1 两个事件的独立性

定义1.4.1 给定概率空间 $(\Omega, \mathcal{F}, \mathbf{P})$，称事件 $A, B \in \mathcal{F}$ 是独立的，是指它们满足

$$
\mathbf {P} (A B) = \mathbf {P} (A) \mathbf {P} (B). \tag {1.4.1}
$$

若 $\mathbf{P}(B) > 0$ ，则事件 $A,B$ 独立当且仅当 $\mathbf{P}(A|B) = \mathbf{P}(A)$ .类似地，若 $\mathbf{P}(A) > 0$ 则事件 $A,B$ 独立当且仅当 $\mathbf{P}(B|A) = \mathbf{P}(B)$ 直观上，事件 $A,B$ 相互独立意味着事件$B$ 的发生不会对 $A$ 发生的概率造成影响，而事件 $A$ 的发生不会对 $B$ 发生的概率造成影响.

独立事件与互斥事件是完全不同的概念. 事实上, 若事件 $A, B$ 独立且 $\mathbf{P}(A) > 0$, $\mathbf{P}(B) > 0$, 则有 $\mathbf{P}(AB) = \mathbf{P}(A)\mathbf{P}(B) > 0$, 故它们不可能互斥. 反之, 若事件 $A, B$ 互斥且 $\mathbf{P}(A) > 0$, $\mathbf{P}(B) > 0$, 则有 $0 = \mathbf{P}(AB) \neq \mathbf{P}(A)\mathbf{P}(B) > 0$, 故它们不可能独立.

例 1.4.1 若 $A \in \mathcal{F}$ 与自己独立, 则 $\mathbf{P}(A) = \mathbf{P}(AA) = \mathbf{P}(A)^2$, 故有 $\mathbf{P}(A) = 0$ 或 1.

例 1.4.2 袋中有 r 个红球和 b 个黑球. 现连续取球 2 次, 令  $R_{i}=\{$  第 i 次取到红球  $\}, i=1,2.$  问  $R_{1}$  与  $R_{2}$  是否独立?

解 (1) 有放回抽取. 此时显然有 $\mathbf{P}(R_i) = r / (r + b)$ 和

$$
\mathbf {P} (R _ {1} R _ {2}) = \frac {r ^ {2}}{(r + b) ^ {2}} = \mathbf {P} (R _ {1}) \mathbf {P} (R _ {2}),
$$

故 $R_{1}$ 与 $R_{2}$ 独立.

(2) 无放回抽取. 根据例 1.1.11 有 $\mathbf{P}(R_i) = r / (r + b)$. 所以

$$
\mathbf {P} (R _ {1} R _ {2}) = \frac {r (r - 1)}{(r + b) (r + b - 1)} \neq \frac {r ^ {2}}{(r + b) ^ {2}} = \mathbf {P} (R _ {1}) \mathbf {P} (R _ {2}),
$$

故 $R_{1}$ 与 $R_{2}$ 不独立.

容易证明下面的结论:

命题 1.4.1 下面的性质等价: 事件 A 与 B 独立; A 与  $B^{c}$  独立;  $A^{c}$  与 B 独立;  $A^{c}$  与  $B^{c}$  独立.

证明 假设事件 $A$ 与 $B$ 独立, 则 $\mathbf{P}(AB) = \mathbf{P}(A)\mathbf{P}(B)$. 因此有

$$
\begin{array}{l} \mathbf {P} (A B ^ {c}) = \mathbf {P} (A \setminus (A B)) = \mathbf {P} (A) - \mathbf {P} (A B) \\ = \mathbf {P} (A) - \mathbf {P} (A) \mathbf {P} (B) = \mathbf {P} (A) [ 1 - \mathbf {P} (B) ] \\ = \mathbf {P} (A) \mathbf {P} (B ^ {c}), \\ \end{array}
$$

故 A 与  $B^{c}$  独立. 其他蕴涵关系的证明类似.

例 1.4.3 概率为 0 或 1 的事件与任何事件独立. 事实上, 若  $\mathbf{P}(A)=0$ , 由概率的单调性知  $\mathbf{P}(AB)=0$ , 故  $\mathbf{P}(AB)=\mathbf{P}(A)\mathbf{P}(B)$ , 即 A 与 B 独立. 若  $\mathbf{P}(A)=1$ , 则  $\mathbf{P}(A^{c})=0$ , 由已证结果知  $A^{c}$  与 B 独立, 再由命题 1.4.1 知 A 与 B 也独立.

例 1.4.4 向区间  $[0,1]$  内随机地任投一粒子.

(i) 用 $A_{1}$ 表示粒子落在 $[0,1/2]$ 内, $B_{1}$ 表示粒子落在子区间 $[1/4,3/4]$ 内. 则

$$
\mathbf {P} (A _ {1}) = 1 - \frac {1}{2} = \frac {1}{2}, \quad \mathbf {P} (B _ {1}) = \frac {3}{4} - \frac {1}{4} = \frac {1}{2},
$$

$$
\mathbf {P} (A _ {1} B _ {1}) = \frac {1}{2} - \frac {1}{4} = \frac {1}{4} = \mathbf {P} (A _ {1}) \mathbf {P} (B _ {1}).
$$

所以 A, B 不互斥且独立.

(ii) 用 $A_{2}$ 表示粒子落在 $[1/5, 1/3]$ 内, $B_{2}$ 表示粒子落在子区间 $[1/4, 1]$ 内. 则

$$
\mathbf {P} (A _ {2}) = \frac {1}{3} - \frac {1}{5} = \frac {2}{1 5}, \quad \mathbf {P} (B _ {2}) = 1 - \frac {1}{4} = \frac {3}{4},
$$

$$
\mathbf {P} (A _ {2} B _ {2}) = \frac {1}{3} - \frac {1}{4} = \frac {1}{1 2} \neq \frac {1}{1 0} = \mathbf {P} (A _ {2}) \mathbf {P} (B _ {2}).
$$

所以  $A_{2}, B_{2}$  不互斥且不独立.

定义 1.4.2 称概率空间  $(\Omega, \mathcal{F}, \mathbf{P})$  上的两个事件类 A 和 C 是独立的, 是指对于任何  $A \in A$  和  $C \in C$ , 事件 A 和 C 独立.

下面命题的证明用到了本书附录中介绍的邓肯类和邓肯类定理.

命题1.4.2 设 $\mathcal{F}$ 的子类 $\mathcal{A}$ 和 $\mathcal{C}$ 对交运算封闭且相互独立. 则它们生成的 $\sigma$ 代数 $\sigma(\mathcal{A})$ 和 $\sigma(\mathcal{C})$ 也相互独立.

证明 对 $A \in \mathcal{F}$ 记 $\mathcal{D}_A = \{B \in \sigma(\mathcal{F}) : \mathbf{P}(AB) = \mathbf{P}(A)\mathbf{P}(B)\}$. 易证 $\mathcal{D}_A$ 是邓肯类. 根据假设, 当 $A \in \mathcal{A}$ 有 $\mathcal{D}_A \supseteq \mathcal{C}$. 再由邓肯类定理知 $\mathcal{D}_A \supseteq d(\mathcal{C}) = \sigma(\mathcal{C})$, 即 $A \in \mathcal{A}$ 与任意的 $B \in \sigma(\mathcal{C})$ 独立. 以此为基础, 重复上面推导可知当 $C \in \sigma(\mathcal{C})$ 有 $\mathcal{D}_C \supseteq d(\mathcal{A}) = \sigma(\mathcal{A})$. 这说明任意的 $A \in \sigma(\mathcal{A})$ 和 $C \in \sigma(\mathcal{C})$ 独立. □

## 1.4.2 多个事件的独立性

定义 1.4.3 给定概率空间  $(\Omega, \mathcal{F}, \mathbf{P})$ ，称事件  $A_{1}, A_{2}, \cdots, A_{n} \in \mathcal{F} (n \geqslant 2)$  独立，是指对任何  $2 \leqslant k \leqslant n$  及  $1 \leqslant i_{1} < i_{2} < \cdots < i_{k} \leqslant n$  都有

$$
\mathbf {P} (A _ {i _ {1}} A _ {i _ {2}} \dots A _ {i _ {k}}) = \mathbf {P} (A _ {i _ {1}}) \mathbf {P} (A _ {i _ {2}}) \dots \mathbf {P} (A _ {i _ {k}}). \tag {1.4.2}
$$

显然, 当  $A_{1}, A_{2}, \cdots, A_{n}$  独立时, 其中的任意  $m (2 \leqslant m \leqslant n)$  个事件也独立. 注意 (1.4.2) 式中包括了  $2^{n} - n - 1$  个式子.

例1.4.5 考虑样本空间 $\Omega = \{1,2,3,4\}$ 的古典概型. 记 $A_{1} = \{1,2\}, A_{2} = \{1,3\}, A_{3} = \{1,4\}$. 显然

$$
\mathbf {P} (A _ {1} A _ {2}) = \mathbf {P} (\{1 \}) = \frac {1}{4} = \mathbf {P} (A _ {1}) \mathbf {P} (A _ {2}),
$$

$$
\mathbf {P} (A _ {2} A _ {3}) = \mathbf {P} (\{1 \}) = \frac {1}{4} = \mathbf {P} (A _ {2}) \mathbf {P} (A _ {3}),
$$

$$
\mathbf {P} (A _ {3} A _ {1}) = \mathbf {P} (\{1 \}) = \frac {1}{4} = \mathbf {P} (A _ {3}) \mathbf {P} (A _ {1}).
$$

所以 $A_{1}, A_{2}, A_{3}$ 两两独立. 但

$$
\mathbf {P} (A _ {1} A _ {2} A _ {3}) = \mathbf {P} (\{1 \}) = \frac {1}{4} \neq \frac {1}{8} = \mathbf {P} (A _ {1}) \mathbf {P} (A _ {2}) \mathbf {P} (A _ {3}),
$$

故 $A_{1}, A_{2}, A_{3}$ 不是相互独立的. 这说明两两独立不能推出相互独立.

例1.4.6 考虑样本空间 $\Omega = \{1,2,3,4,5,6\}$ 的古典概型. 记 $A_{1} = \{1,2,3,4\}$ 和 $A_{2} = A_{3} = \{4,5,6\}$. 则 $\mathbf{P}(A_1) = 2 / 3, \mathbf{P}(A_2) = \mathbf{P}(A_3) = 1 / 2,$ 从而

$$
\mathbf {P} (A _ {1} A _ {2} A _ {3}) = \mathbf {P} (\{4 \}) = \frac {1}{6} = \mathbf {P} (A _ {1}) \mathbf {P} (A _ {2}) \mathbf {P} (A _ {3}).
$$

但是

$$
\mathbf {P} (A _ {2} A _ {3}) = \mathbf {P} (A _ {2}) = \frac {1}{2} \neq \mathbf {P} (A _ {2}) \mathbf {P} (A _ {3}).
$$

所以 $A_{1}, A_{2}, A_{3}$ 不相互独立.

定理 1.4.3 事件  $A_{1}, A_{2}, \cdots, A_{n} \in F$  独立当且仅当事件  $\hat{A}_{1}, \hat{A}_{2}, \cdots, \hat{A}_{n} \in F$  独立，其中  $\hat{A}_{i} = A_{i}$  或  $A_{i}^{c}$ .

证明 与命题 1.4.1 的证明类似, 从略.

下面的定理给出了两个常用的与独立性有关的概率计算公式.

定理 1.4.4 若  $A_{1}, A_{2}, \cdots, A_{n} \in F$  独立, 则有

$$
\mathbf {P} \Big (\bigcap_ {i = 1} ^ {n} A _ {i} \Big) = \prod_ {i = 1} ^ {n} \mathbf {P} (A _ {i}), \quad \mathbf {P} \Big (\bigcup_ {i = 1} ^ {n} A _ {i} \Big) = 1 - \prod_ {i = 1} ^ {n} [ 1 - \mathbf {P} (A _ {i}) ].
$$

证明 显然, 第一个等式已经包括在定义 (1.4.2) 式中. 由定理 1.4.3 知 $A_{1}^{c}, A_{2}^{c}, \cdots, A_{n}^{c} \in \mathcal{F}$ 独立, 故

$$
\mathbf {P} \Big (\bigcup_ {i = 1} ^ {n} A _ {i} \Big) = 1 - \mathbf {P} \Big (\bigcap_ {i = 1} ^ {n} A _ {i} ^ {c} \Big) = 1 - \prod_ {i = 1} ^ {n} \mathbf {P} (A _ {i} ^ {c}),
$$

其中 $\mathbf{P}(A_i^c) = 1 - \mathbf{P}(A_i)$, 故得第二个等式.

在理论和应用中, 也经常需要考虑任意多的事件或事件类的独立性问题. 为此我们给出下面的

定义 1.4.4 设 $A_{i}, i \in I$ 是某概率空间上的一族随机事件, 其中 $I$ 是任意的非空集. 如果对任何有限子集 $\{i_{1}, i_{2}, \cdots, i_{n}\} \subseteq I$ 事件 $A_{i_{1}}, A_{i_{2}}, \cdots, A_{i_{n}}$ 都独立, 就称 $A_{i}, i \in I$ 是独立的.

定义1.4.5 设 $\mathcal{A}_i, i \in I$ 是某概率空间 $(\Omega, \mathcal{F}, \mathbf{P})$ 上的一族事件类, 其中 $I$ 是任意的非空集. 如果对于任取的 $A_i \in \mathcal{A}_i$, $i \in I$, 事件 $A_i, i \in I$ 都独立, 就称 $\mathcal{A}_i, i \in I$ 是独立的.

## 1.4.3 二维乘积概率空间

定义1.4.6 假设 $(\Omega_1, \mathcal{F}_1)$ 和 $(\Omega_2, \mathcal{F}_2)$ 是两个可测空间. 我们称乘积集

$$
\Omega_ {1} \times \Omega_ {2} := \{(\omega_ {1}, \omega_ {2}): \omega_ {1} \in \Omega_ {1}, \omega_ {2} \in \Omega_ {2} \}
$$

为 $\Omega_{1}$ 和 $\Omega_{2}$ 的乘积样本空间. 记

$$
\mathcal {C} = \{A _ {1} \times A _ {2}: A _ {1} \in \mathcal {F} _ {1}, A _ {2} \in \mathcal {F} _ {2} \}. \tag {1.4.3}
$$

称  $\mathcal{F}_{1} \times \mathcal{F}_{2} := \sigma(\mathcal{C})$  为  $F_{1}$  和  $F_{2}$  的乘积  $\sigma$  代数，称  $(\Omega_{1} \times \Omega_{2}, \mathcal{F}_{1} \times \mathcal{F}_{2})$  为  $(\Omega_{1}, \mathcal{F}_{1})$  和  $(\Omega_{2}, \mathcal{F}_{2})$  的乘积可测空间.

例 1.4.7 设  $\Omega_{1}=\Omega_{2}=\{1,2\}$ ，并令  $F_{1}=F_{2}=\{\varnothing,\{1\},\{2\},\{1,2\}\}$  为  $\{1,2\}$  的所有子集构成的  $\sigma$  代数。再令 C 由 (1.4.3) 式定义。不难发现

$$
\begin{array}{l} \mathscr {C} = \{\varnothing , \{1 \} \times \{1 \}, \{1 \} \times \{2 \}, \{1 \} \times \Omega_ {2}, \\ \{2 \} \times \{1 \}, \{2 \} \times \{2 \}, \{2 \} \times \Omega_ {2}, \\ \Omega_ {1} \times \{1 \}, \Omega_ {1} \times \{2 \}, \Omega_ {1} \times \Omega_ {2} \}. \\ \end{array}
$$

该集类不是  $\sigma$  代数. 事实上,

$$
(\{1 \} \times \{1 \}) \cup (\{2 \} \times \{2 \}) = \{(1, 1) \} \cup \{(2, 2) \} = \{(1, 1), (2, 2) \} \notin \mathscr {C},
$$

故 $\mathcal{C}$ 对于并运算不封闭.

定理1.4.5 对于概率空间 $(\Omega_1, \mathcal{F}_1, \mathbf{P}_1)$ 和 $(\Omega_2, \mathcal{F}_2, \mathbf{P}_2)$, 存在乘积 $\sigma$ 代数 $\mathcal{F}_1 \times \mathcal{F}_2$ 上的唯一的概率测度 $\mathbf{Q}$ 满足性质:

$$
\mathbf {Q} (A _ {1} \times A _ {2}) = \mathbf {P} _ {1} (A _ {1}) \mathbf {P} _ {2} (A _ {2}), \quad A _ {1} \in \mathscr {F} _ {1}, A _ {2} \in \mathscr {F} _ {2}. \tag {1.4.4}
$$

证明 可数样本空间情况. 设 $\Omega_1$ 和 $\Omega_2$ 都是可数集. 不妨设 $\mathcal{F}_1$ 和 $\mathcal{F}_2$ 分别为 $\Omega_1$ 和 $\Omega_2$ 的所有子集构成的 $\sigma$ 代数. 这样 $\mathcal{F}_1 \times \mathcal{F}_2$ 是 $\Omega_1 \times \Omega_2$ 的所有子集构成的 $\sigma$ 代数. 根据 (1.4.4) 式可以唯一确定 $\mathbf{Q}$ 在 $\mathcal{F}_1 \times \mathcal{F}_2$ 中的单点集上的取值, 即

$$
\mathbf {Q} (\{(\omega_ {1}, \omega_ {2}) \}) = \mathbf {P} _ {1} (\{\omega_ {1} \}) \mathbf {P} _ {2} (\{\omega_ {2} \}), \quad \omega_ {1} \in \Omega_ {1}, \omega_ {2} \in \Omega_ {2}. \tag {1.4.5}
$$

由于任何 $A \in \mathcal{F}_1 \times \mathcal{F}_2$ 至多包含可数个点, 利用可数可加性可以唯一确定 $\mathbf{Q}(A)$ 的值. 所以具有性质 (1.4.4) 的概率测度 $\mathbf{Q}$ 存在且唯一. □

定理 1.4.5 的一般情况的证明超出了本课程的范围, 可参考测度论或高等概率论方面的著作, 如见 [19,20].

定义1.4.7 对于给定的概率空间 $(\Omega_1, \mathcal{F}_1, \mathbf{P}_1)$ 和 $(\Omega_2, \mathcal{F}_2, \mathbf{P}_2)$, 我们称乘积 $\sigma$ 代数 $\mathcal{F}_1 \times \mathcal{F}_2$ 上满足性质 (1.4.4) 的概率测度 $\mathbf{Q}$ 为 $\mathbf{P}_1$ 和 $\mathbf{P}_2$ 的乘积概率测度, 并记作 $\mathbf{P}_1 \times \mathbf{P}_2$. 称 $(\Omega_1 \times \Omega_2, \mathcal{F}_1 \times \mathcal{F}_2, \mathbf{P}_1 \times \mathbf{P}_2)$ 为 $(\Omega_1, \mathcal{F}_1, \mathbf{P}_1)$ 和 $(\Omega_2, \mathcal{F}_2, \mathbf{P}_2)$ 的乘积概率空间.

乘积概率空间 $(\Omega_1 \times \Omega_2, \mathcal{F}_1 \times \mathcal{F}_2, \mathbf{P}_1 \times \mathbf{P}_2)$ 描述了由 $(\Omega_1, \mathcal{F}_1, \mathbf{P}_1)$ 和 $(\Omega_2, \mathcal{F}_2, \mathbf{P}_2)$ 给出的两次独立试验构成的联合随机试验. 令 $A_1 \in \mathcal{F}_1$ 和 $A_2 \in \mathcal{F}_2$. 则 $A_1 \times \Omega_2 \in \mathcal{F}_1 \times \mathcal{F}_2$ 表示 {第 1 次试验中事件 $A_1$ 发生}, 而 $\Omega_1 \times A_2 \in \mathcal{F}_1 \times \mathcal{F}_2$ 表示 {第 2 次试验中事件 $A_2$ 发生}. 显然有

$$
A _ {1} \times A _ {2} = (A _ {1} \times \Omega_ {2}) \cap (\Omega_ {1} \times A _ {2}) \in \mathscr {F} _ {1} \times \mathscr {F} _ {2},
$$

它表示 { 第 1 次和第 2 次试验中分别发生了事件 $A_{1}$ 和 $A_{2}$ } . 由 (1.4.4) 式有

$$
\mathbf {Q} (A _ {1} \times A _ {2}) = \mathbf {Q} (A _ {1} \times \Omega_ {2}) \mathbf {Q} (\Omega_ {1} \times A _ {2}).
$$

所以乘积概率空间 $(\Omega_1 \times \Omega_2, \mathcal{F}_1 \times \mathcal{F}_2, \mathbf{P}_1 \times \mathbf{P}_2)$ 中的事件 $A_1 \times \Omega_2$ 和 $\Omega_1 \times A_2$ 独立.

例 1.4.8 设袋中有 r 个红球和 b 个黑球. 将 r 个红球用数字  $1,2,\cdots,r$  编号, b 个黑球用数字  $r+1,r+2,\cdots,r+b$  编号. 定义样本空间

$$
\Omega = \{1, \dots , r, r + 1, \dots , r + b \},
$$

并令 $(\Omega, \mathcal{F}, \mathbf{P})$ 为相应的古典概型概率空间, 即

$$
\mathbf {P} (\{k \}) = \frac {1}{r + b}, \quad k \in \Omega . \tag {1.4.6}
$$

用此概率空间就可描述一次取球的随机试验. 注意, 事件 $R = \{1, 2, \cdots, r\}$ 表示取到红球, 而事件 $B = \{r + 1, r + 2, \cdots, r + b\}$ 表示取到黑球. 根据古典概型的概率计算公式有

$$
\mathbf {P} (R) = \frac {r}{r + b}, \quad \mathbf {P} (B) = \frac {b}{r + b}.
$$

例 1.4.9 设袋中有 r 个红球和 b 个黑球. 像上例中那样, 将 r 个红球用数字 1,2, $\cdots$ , r 编号, b 个黑球用数字  $r+1, r+2, \cdots, r+b$  编号. 则有放回地两次取球的随机试验可用古典概型概率空间  $(\tilde{\Omega}, \tilde{\mathcal{F}}, \tilde{\mathbf{P}})$  描述, 其中

$$
\tilde {\Omega} = \{(i, j): 1 \leqslant i, j \leqslant r + b \}.
$$

注意对每个样本点 $(i,j)\in \tilde{\Omega}$ 有

$$
\tilde {\mathbf {P}} \big (\{(i, j) \} \big) = \frac {1}{(r + b) ^ {2}}. \tag {1.4.7}
$$

注意, 事件 { 第 1 次取到红球 } 可表示为

$$
\tilde {R} _ {1} = \{(i, j): 1 \leqslant i \leqslant r, 1 \leqslant j \leqslant r + b \},
$$

而事件 { 第 2 次取到黑球 } 可表示为

$$
\tilde {B} _ {2} = \{(i, j): 1 \leqslant i \leqslant r + b, r + 1 \leqslant j \leqslant r + b \}.
$$

根据古典概型的概率计算公式有

$$
\tilde {\mathbf {P}} (\tilde {R} _ {1}) = \frac {r (r + b)}{(r + b) ^ {2}} = \frac {r}{r + b}, \quad \tilde {\mathbf {P}} (\tilde {B} _ {2}) = \frac {(r + b) b}{(r + b) ^ {2}} = \frac {b}{r + b}.
$$

事件 { 第 1 次取到红球且第 2 次取到黑球 } 可表示为

$$
\tilde {R} _ {1} \cap \tilde {B} _ {2} = \{(i, j): 1 \leqslant i \leqslant r, r + 1 \leqslant j \leqslant r + b \}.
$$

不难看出，

$$
\tilde {\mathbf {P}} (\tilde {R} _ {1} \cap \tilde {B} _ {2}) = \frac {r b}{(r + b) ^ {2}}.
$$

这说明事件 $\tilde{R}_1, \tilde{B}_2$ 独立. 若令 $(\Omega, \mathcal{F}, \mathbf{P})$ 为上例中定义的古典概型概率空间, 由 (1.4.6) 式和 (1.4.7) 式有

$$
\tilde {\mathbf {P}} \big (\{(i, j) \} \big) = \frac {1}{(r + b) ^ {2}} = \mathbf {P} (\{i \}) \mathbf {P} (\{j \}).
$$

对比上式和 (1.4.5) 式知 $(\tilde{\Omega}, \tilde{\mathcal{F}}, \tilde{\mathbf{P}})$ 实际上是 $(\Omega, \mathcal{F}, \mathbf{P})$ 与自己的乘积概率空间.

## \*1.4.4 多维乘积概率空间

与二维乘积概率空间类似, 我们可以定义有限或可数维乘积概率空间, 它给出了由有限次或可数次独立试验构成的联合随机试验的数学描述.

定义 1.4.8 设  $(\Omega_{i}, \mathcal{F}_{i}, \mathbf{P}_{i}), i = 1, 2, \cdots, n$  是 n 个概率空间. 我们称乘积集

$$
\Omega_ {1} \times \Omega_ {2} \times \dots \times \Omega_ {n} := \left\{\left(\omega_ {1}, \omega_ {2}, \dots , \omega_ {n}\right): \omega_ {i} \in \Omega_ {i}; i = 1, 2, \dots , n \right\}
$$

为  $\Omega_{i}, i=1,2,\cdots,n$  的乘积样本空间. 记

$$
\mathcal {C} = \{A _ {1} \times A _ {2} \times \dots \times A _ {n}: A _ {i} \in \mathscr {F} _ {i}; i = 1, 2, \dots , n \}. \tag {1.4.8}
$$

称  $\mathcal{F}_{1}\times\mathcal{F}_{2}\times\cdots\times\mathcal{F}_{n}:=\sigma(\mathcal{C})$  为  $F_{i}, i=1,2,\cdots,n$  的乘积  $\sigma$  代数.此时存在  $F_{1}\times F_{2}\times\cdots\times F_{n}$  上的唯一的概率测度  $Q:=P_{1}\times P_{2}\times\cdots\times P_{n}$  满足性质:

$$
\mathbf {Q} (A _ {1} \times A _ {2} \times \dots \times A _ {n}) = \mathbf {P} _ {1} (A _ {1}) \mathbf {P} _ {2} (A _ {2}) \dots \mathbf {P} _ {n} (A _ {n}), \quad A _ {i} \in \mathscr {F} _ {i}; i = 1, 2, \dots , n. \tag {1.4.9}
$$

称  $P_{1} \times P_{2} \times \cdots \times P_{n}$  为  $P_{i}, i = 1, 2, \cdots, n$  的乘积概率测度, 并称

$$
(\Omega_ {1} \times \Omega_ {2} \times \dots \times \Omega_ {n}, \mathcal {F} _ {1} \times \mathcal {F} _ {2} \times \dots \times \mathcal {F} _ {n}, \mathbf {P} _ {1} \times \mathbf {P} _ {2} \times \dots \times \mathbf {P} _ {n})
$$

为 $(\Omega_{i},\mathscr{F}_{i},\mathbf{P}_{i}), i=1,2,\cdots,n$ 的乘积概率空间.

定义 1.4.9 设  $(\Omega_{i}, \mathcal{F}_{i}, \mathbf{P}_{i}), i = 1, 2, \cdots$  是可数个概率空间. 我们称乘积集

$$
\Omega_ {1} \times \Omega_ {2} \times \dots := \{(\omega_ {1}, \omega_ {2}, \dots): \omega_ {i} \in \Omega_ {i}; i = 1, 2, \dots \}
$$

为  $\Omega_{i}, i=1,2,\cdots$  的乘积样本空间. 记

$$
\begin{array}{l} \mathscr {C} = \left\{A _ {1} \times A _ {2} \times \dots \times A _ {n} \times \Omega_ {n + 1} \times \Omega_ {n + 2} \times \dots : \right. \\ A _ {i} \in \mathscr {F} _ {i}; i = 1, 2, \dots , n; n = 1, 2, \dots \}. \tag {1.4.10} \\ \end{array}
$$

称  $\mathcal{F}_{1} \times \mathcal{F}_{2} \times \cdots := \sigma(\mathcal{C})$  为  $F_{i}, i = 1, 2, \cdots$  的乘积  $\sigma$  代数. 此时存在  $F_{1} \times F_{2} \times \cdots$  上的唯一的概率测度  $Q := P_{1} \times P_{2} \times \cdots$  满足性质: 对任意的  $A_{i} \in F_{i}; i = 1, 2, \cdots, n; n = 1, 2, \cdots$ ,

$$
\mathbf {Q} (A _ {1} \times A _ {2} \times \dots \times A _ {n} \times \Omega_ {n + 1} \times \Omega_ {n + 2} \times \dots) = \mathbf {P} _ {1} (A _ {1}) \mathbf {P} _ {2} (A _ {2}) \dots \mathbf {P} _ {n} (A _ {n}). \tag {1.4.11}
$$

称  $P_{1} \times P_{2} \times \cdots$  为  $P_{i}, i = 1, 2, \cdots$  的乘积概率测度，并称

$$
(\Omega_ {1} \times \Omega_ {2} \times \dots , \mathcal {F} _ {1} \times \mathcal {F} _ {2} \times \dots , \mathbf {P} _ {1} \times \mathbf {P} _ {2} \times \dots)
$$

为 $(\Omega_{i},\mathscr{F}_{i},\mathbf{P}_{i}), i=1,2,\cdots$ 的乘积概率空间.

关于乘积概率测度  $P_{1} \times P_{2} \times \cdots \times P_{n}$  和  $P_{1} \times P_{2} \times \cdots$  的存在唯一性, 可参考测度论或高等概率论的书籍. 特别地, 当  $(\Omega_{i}, \mathcal{F}_{i}, \mathbf{P}_{i}) = (\Omega, \mathcal{F}, \mathbf{P})$  与标号 i 无关时, 可将上面定义的乘积概率空间分别记作  $(\Omega^{n}, \mathcal{F}^{n}, \mathbf{P}^{n})$  和  $(\Omega^{\infty}, \mathcal{F}^{\infty}, \mathbf{P}^{\infty})$ , 并分别称之为  $(\Omega, \mathcal{F}, \mathbf{P})$  的 n 维乘积概率空间和可数无穷维乘积概率空间.

例 1.4.10 令  $(\Omega_{1},\mathcal{F}_{1},\mathbf{P}_{1})$  为关于成功事件  $A\subseteq\Omega_{1}$  的一次伯努利试验对应的概率空间, 其中  $F_{1}=\{\varnothing,A,A^{c},\Omega\}$ . 设成功概率为  $\mathbf{P}_{1}(A)=p(0<p<1)$ . 考虑其可数无穷维乘积概率空间  $(\Omega,\mathcal{F},\mathbf{P}):=(\Omega_{1}^{\infty},\mathcal{F}_{1}^{\infty},\mathbf{P}_{1}^{\infty})$ . 此概率空间所描述的随机试验为可数无穷次伯努利试验. 对  $k\geqslant1$  记

$$
B _ {k} = \Omega_ {1} ^ {k - 1} \times A \times \Omega_ {1} ^ {\infty},
$$

则有

$$
B _ {k} ^ {c} = \Omega_ {1} ^ {k - 1} \times A ^ {c} \times \Omega_ {1} ^ {\infty}.
$$

根据 (1.4.10) 式和可数无穷维乘积 $\sigma$ 代数的定义, 显然有 $B_{k} \in \mathcal{F}_{1}^{\infty}$ 和 $B_{k}^{c} \in \mathcal{F}_{1}^{\infty}$. 这两个事件分别表示第 $k$ 次试验的结果为 $A$ 和 $A^{c}$. 利用 (1.4.11) 式不难算出 $\mathbf{P}(B_k) = \mathbf{P}_1(A) = p$ 和 $\mathbf{P}(B_k^c) = \mathbf{P}_1(A^c) = 1 - p$. 另外, 易证事件 $B_1, B_2, \cdots$ 相互独立.

例 1.4.11 求在关于成功事件 A 的可数无穷次伯努利试验中事件  $E = \{A \text{ 终将发生}\}$  的概率.

解 对于 $n \geqslant 1$ 令 $F_{n} = \{\text{前 } n \text{ 次都失败}\}$. 采用上例的记号, 我们有 $F_{n} = B_{1}^{c} \cap B_{2}^{c} \cap \cdots \cap B_{n}^{c}$ 和 $\mathbf{P}(F_{n}) = (1 - p)^{n}$. 注意 $\{F_{n}\}$ 是单调下降的集序列, 且 $E^{c} = \bigcap_{n=1}^{\infty} F_{n}$. 由概率的上连续性得

$$
\mathbf {P} (E) = 1 - \mathbf {P} (E ^ {c}) = 1 - \lim _ {n \to \infty} \mathbf {P} (F _ {n}) = 1 - \lim _ {n \to \infty} (1 - p) ^ {n} = 1.
$$

这说明持续不断地将试验进行下去, 最终一定能够成功.

## 练习题

1. 证明: (1) 若事件 $A$ 与自身独立, 则 $\mathbf{P}(A) = 0$ 或 1;

(2) 若 $\mathbf{P}(A) = 0$ 或 1, 则 $A$ 与任意事件独立.

2. 对于某个家庭考察两个事件 $A = \{\text{至多有一个女孩}\}$ 和 $B = \{\text{男女孩都有}\}$. 设男女孩的出生率都是 $1/2$. 证明: 对 3 孩之家, 事件 $A$ 和 $B$ 独立; 而对 4 孩之家, 事件 $A$ 和 $B$ 不独立.

3. 证明: 事件 $A_{1}, A_{2}, \cdots, A_{n}$ 独立的充要条件是下列 $2^{n}$ 个等式成立:

$$
\mathbf {P} (\hat {A} _ {1} \hat {A} _ {2} \dots \hat {A} _ {n}) = \mathbf {P} (\hat {A} _ {1}) \mathbf {P} (\hat {A} _ {2}) \dots \mathbf {P} (\hat {A} _ {n}),
$$

其中  $\hat{A}_{i}$  取  $A_{i}$  或  $A_{i}^{c}$ .

4. 独立地重复投掷两枚骰子, 并计算点数之和. 求 “和数为 5” 出现在 “和数为 7” 之前的概率.
5. 设 $E$ 和 $F$ 是某随机试验中的互不相容事件. 证明: 若独立重复地进行这样的试验, 则 $E$ 发生在 $F$ 之前的概率为 $\mathbf{P}(E)/[\mathbf{P}(E)+\mathbf{P}(F)]$.
6. 重复投掷硬币, 设第一次出现正面的概率为 $c (0 \leqslant c \leqslant 1)$, 之后每次与上次出现相同面的概率为 $p (0 < p < 1)$. 求第 $n$ 次出现正面的概率 $p_n$, 并讨论当 $n \to \infty$ 时 $p_n$ 的极限.

提示: 根据全概率公式有  $p_{n}=(1-p)+(2p-1)p_{n-1}$ ，于是有

$$
\begin{array}{l} p _ {n} = (1 - p) \big [ 1 + (2 p - 1) + \dots + (2 p - 1) ^ {n - 2} \big ] + c (2 p - 1) ^ {n - 1} \\ = 1 / 2 - (2 p - 1) ^ {n - 1} / 2 + c (2 p - 1) ^ {n - 1}. \\ \end{array}
$$