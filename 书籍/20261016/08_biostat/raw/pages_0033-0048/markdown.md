## 1.4.4 Visualizing distributions of data: histograms and boxplots

Graphs show important features of a distribution that are not evident from numerical summaries, such as asymmetry or extreme values. While dot plots show the exact value of each observation, histograms and boxplots graphically summarize distributions.

In a **histogram**, observations are grouped into bins and plotted as bars. Figure 1.17 shows the number of clutches with volume between 0 and 200 mm<sup>3</sup>, 200 and 400 mm<sup>3</sup>, etc. up until 2,600 and 2,800 mm<sup>3</sup>.31 These binned counts are plotted in Figure 1.18.

| Clutch volumes | 0-200 | 200-400 | 400-600 | 600-800 | ... | 2400-2600 | 2600-2800 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Count | 4 | 29 | 69 | 99 | ... | 2 | 1 |

Figure 1.17: The counts for the binned clutch.volume data.

![](images/page_32_chart_7.jpg)

<details>
<summary>histogram</summary>

| Clutch Volume (Bin) | Frequency |
| --- | --- |
| 0~250 | ~4 |
| 250~500 | ~30 |
| 500~750 | ~70 |
| 750~1000 | ~100 |
| 1000~1250 | ~94 |
| 1250~1500 | ~56 |
| 1500~1750 | ~45 |
| 1750~2000 | ~18 |
| 2000~2250 | ~7 |
| 2250~2500 | ~7 |
| 2500~2750 | ~1 |
| 2750~3000 | ~2 |
| 3000~3250 | ~1 |
</details>

Figure 1.18: A histogram of clutch.volume.

Histograms provide a view of the **data density**. Higher bars indicate more frequent observations, while lower bars represent relatively rare observations. Figure 1.18 shows that most of the egg clutches have volumes between 500-1,000 mm<sup>3</sup>, and there are many more clutches with volumes smaller than 1,000 mm<sup>3</sup>than clutches with larger volumes.

Histograms show the **shape** of a distribution. The tails of a **symmetric** distribution are roughly equal, with data trailing off from the center roughly equally in both directions. Asym metry arises when one tail of the distribution is longer than the other. A distribution is said to be **right skewed** when data trail off to the right, and **left skewed** when data trail off to the left.<sup>32</sup> Figure 1.18 shows that the distribution of clutch volume is right skewed; most clutches have relatively small volumes, and only a few clutches have high volumes.

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">31<sub>By</sub> default in R, the bins are left-open and right-closed; i.e., the intervals are of the form (a, b]. Thus, an observation with value 200 would fall into the 0-200 bin instead of the 200-400 bin.</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">32<sub>Other</sub> ways to describe data that are skewed to the right/left: skewed to the right/left or skewed to the positive/negative end.</span></small>

A **mode** is represented by a prominent peak in the distribution.<sup>33</sup> Figure 1.19 shows histograms that have one, two, or three major peaks. Such distributions are called **unimodal**, **bimodal**, and **multimodal**, respectively. Any distribution with more than two prominent peaks is called multimodal. Note that the less prominent peak in the unimodal distribution was not counted since it only differs from its neighboring bins by a few observations. Prominent is a subjective term, but it is usually clear in a histogram where the major peaks are.

![](images/page_33_image_3.jpg)

Figure 1.19: From left to right: unimodal, bimodal, and multimodal distributions.

A **boxplot** indicates the positions of the first, second, and third quartiles of a distribution in addition to extreme observations.<sup>34</sup> Figure 1.20 shows a boxplot of clutch.volume alongside a vertical dot plot.

![](images/page_33_chart_6.jpg)

<details>
<summary>boxplot</summary>

| Metric | Value |
| --- | --- |
| Q1 (first quartile) | ~600 |
| Q3 (third quartile) | ~1100 |
| Median (second quartile) | ~850 |
| Upper Whisker | ~1850 |
| Lower Whisker | ~200 |
</details>

Figure 1.20: A boxplot and dot plot of clutch.volume. The horizontal dashes indicate the bottom 50% of the data and the open circles represent the top 50%.

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">33<sub>Another</sub> definition of mode, which is not typically used in statistics, is the value with the most occurrences. It is common that a dataset contains no observations with the same value, which makes this other definition impractical for many datasets.</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">34<sub>Boxplots</sub> are also known as box-and-whisker plots.</span></small>

In a boxplot, the interquartile range is represented by a rectangle extending from the first quartile to the third quartile, and the rectangle is split by the median (second quartile). Extending outwards from the box, the **whiskers** capture the data that fall between $Q_{1}-1.5 \times IQR   and   Q_{3}+1.5 \times$ IQR. The whiskers must end at data points; the values given by adding or subtracting $1 . 5 \times I Q R$ define the maximum reach of the whiskers. For example, with the clutch.volume variable, $Q _ { 3 } +$ $1.5 \times IQR = 1, 096.5 + 1.5 \times 486.4 = 1, 826.1 \;  mm ^3$ . However, there was no clutch with volume 1,826.1 $\mathrm { m m } ^ { 3 } ;$ thus, the upper whisker extends to 1,819.7 mm<sup>3</sup>, the largest observation that is smaller than $Q _ { 3 } + 1 . 5 \times I Q R .$

Any observation that lies beyond the whiskers is shown with a dot; these observations are called outliers. An **outlier** is a value that appears extreme relative to the rest of the data. For the clutch.volume variable, there are several large outliers and no small outliers, indicating the presence of some unusually large egg clutches.

The high outliers in Figure 1.20 reflect the right-skewed nature of the data. The right skew is also observable from the position of the median relative to the first and third quartiles; the median is slightly closer to the first quartile. In a symmetric distribution, the median will be halfway between the first and third quartiles.

## GUIDED PRACTICE 1.12

Use the histogram and boxplot in Figure 1.21 to describe the distribution of height in the famuss data, where height is measured in inches.<sup>35</sup>

![](images/page_34_image_7.jpg)

Figure 1.21: A histogram and boxplot of height in the famuss data.

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">35<sub>The</sub> data are roughly symmetric (the left tail is slightly longer than the right tail), and the distribution is unimodal with one prominent peak at about 67 inches. The middle 50% of individuals are between 5.5 feet and just under 6 feet tall. There is one low outlier and one high outlier, representing individuals that are unusually short/tall relative to the other individuals.</span></small>

![](images/page_34_image_10.jpg)

## 1.4.5 Transforming data

When working with strongly skewed data, it can be useful to apply a **transformation**, and rescale the data using a function. A natural log transformation is commonly used to clarify the features of a variable when there are many values clustered near zero and all observations are positive.

![](images/page_35_chart_4.jpg)

<details>
<summary>histogram</summary>

| Income (USD) | Frequency |
| --- | --- |
| 0~10k | ~110 |
| 10k~20k | ~20 |
| 20k~30k | ~10 |
| 30k~40k | ~7 |
| 40k~50k | ~8 |
| 50k~60k | ~9 |
| 60k~70k | ~3 |
| 70k~80k | ~0 |
| 80k~90k | ~3 |
| 90k~100k | ~0 |
| 100k~110k | ~2 |
| 110k~120k | ~1 |
</details>

(a)

![](images/page_35_chart_6.jpg)

<details>
<summary>histogram</summary>

| Income (log USD) | Frequency |
| --- | --- |
| 5.0~5.3 | ~1 |
| 5.3~5.6 | ~5 |
| 5.6~5.9 | ~12 |
| 5.9~6.2 | ~16 |
| 6.2~6.5 | ~19 |
| 6.5~6.8 | ~9 |
| 6.8~7.1 | ~18 |
| 7.1~7.4 | ~23 |
| 7.4~7.7 | ~14 |
| 7.7~8.0 | ~14 |
| 8.0~8.3 | ~10 |
| 8.3~8.6 | ~18 |
| 8.6~8.9 | ~4 |
| 8.9~9.2 | ~2 |
</details>

(b)

Figure 1.22: (a) Histogram of per capita income. (b) Histogram of the logtransformed per capita income.

For example, income data are often skewed right; there are typically large clusters of low to moderate income, with a few large incomes that are outliers. Figure 1.22(a) shows a histogram of average yearly per capita income measured in US dollars for 165 countries in 2011.<sup>36</sup> The data are heavily right skewed, with the majority of countries having average yearly per capita income lower than \$10,000. Once the data are log-transformed, the distribution becomes roughly symmetric (Figure 1.22(b)).<sup>37</sup>

For symmetric distributions, the mean and standard deviation are particularly informative summaries. If a distribution is symmetric, approximately 70% of the data are within one standard deviation of the mean and 95% of the data are within two standard deviations of the mean; this guideline is known as the **empirical rule**.

## EXAMPLE 1.13

On the log-transformed scale, mean log income is 8.50, with standard deviation 1.54. Apply the empirical rule to describe the distribution of average yearly per capita income among the 165 countries.

According to the empirical rule, the middle 70% of the data are within one standard deviation of the mean, in the range (8.50 - 1.54, 8.50 + 1.54) = (6.96, 10.04) log(USD). 95% of the data are within two standard deviations of the mean, in the range $\left( 8.50 \text{- } 2(1.54),   8.50 \text{+ } 2(1.54) \right) = \left( 5.42,   11.58 \right)$ log(USD).

Undo the log transformation. The middle 70% of the data are within the range $( e ^ { 6 . 9 6 } , e ^ { 1 0 . 0 4 } )$ = (\$1,054, \$22,925). The middle 95% of the data are within the range $( e ^ { 5 . 4 2 } , e ^ { 1 1 . 5 8 } )   =   ( \S 2 2 6 ,$ \$106,937).

Functions other than the natural log can also be used to transform data, such as the square root and inverse.

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">36<sub>The</sub> data are available as wdi.2011 in the R package oibiostat.</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">37<sub>In</sub> statistics, the natural logarithm is usually written log. In other settings it is sometimes written as ln.</span></small>

## 1.5 Categorical data

This section introduces tables and plots for summarizing categorical data, using the famuss dataset introduced in Section 1.2.2.

A table for a single variable is called a **frequency table**. Figure 1.23 is a frequency table for the actn3.r577x variable, showing the distribution of genotype at location r577x on the ACTN3 gene for the FAMuSS study participants.

In a **relative frequency table** like Figure 1.24, the proportions per each category are shown instead of the counts.

|  | CC | CT | TT | Sum |
| --- | --- | --- | --- | --- |
| Counts | 173 | 261 | 161 | 595 |

Figure 1.23: A frequency table for the actn3.r577x variable.

|  | CC | CT | TT | Sum |
| --- | --- | --- | --- | --- |
| Proportions | 0.291 | 0.439 | 0.271 | 1.000 |

Figure 1.24: A relative frequency table for the actn3.r577x variable.

A bar plot is a common way to display a single categorical variable. The left panel of Figure 1.25 shows a **bar plot** of the counts per genotype for the actn3.r577x variable. The plot in the right panel shows the proportion of observations that are in each level (i.e. in each genotype).

![](images/page_36_image_11.jpg)

Figure 1.25: Two bar plots of actn3.r577x. The left panel shows the counts, and the right panel shows the proportions for each genotype.

## 1.6 Relationships between two variables

This section introduces numerical and graphical methods for exploring and summarizing relationships between two variables. Approaches vary depending on whether the two variables are both numerical, both categorical, or whether one is numerical and one is categorical.

## 1.6.1 Two numerical variables

## Scatterplots

In the frog parental investment study, researchers used clutch volume as a primary variable of interest rather than egg size because clutch volume represents both the eggs and the protective gelatinous matrix surrounding the eggs. The larger the clutch volume, the higher the energy required to produce it; thus, higher clutch volume is indicative of increased maternal investment. Previous research has reported that larger body size allows females to produce larger clutches; is this idea supported by the frog data?

A **scatterplot** provides a case-by-case view of the relationship between two numerical variables. Figure 1.26 shows clutch volume plotted against body size, with clutch volume on the y-axis and body size on the x-axis. Each point represents a single case. For this example, each case is one egg clutch for which both volume and body size (of the female that produced the clutch) have been recorded.

![](images/page_37_chart_8.jpg)

<details>
<summary>scatter</summary>

| Female Body Size (cm) | Clutch Volume \((mm^{3})\) |
| --- | --- |
| ~3.75 | ~200 |
| ~3.75 | ~250 |
| ~3.85 | ~150 |
| ~3.90 | ~250 |
| ~3.90 | ~300 |
| ~3.95 | ~350 |
| ~4.00 | ~400 |
| ~4.05 | ~750 |
| ~4.10 | ~550 |
| ~4.15 | ~600 |
| ~4.20 | ~500 |
| ~4.25 | ~650 |
| ~4.30 | ~400 |
| ~4.35 | ~300 |
| ~4.40 | ~550 |
| ~4.45 | ~350 |
| ~4.50 | ~600 |
| ~4.60 | ~450 |
| ~4.65 | ~650 |
| ~4.70 | ~1050 |
| ~4.75 | ~600 |
| ~4.80 | ~850 |
| ~4.85 | ~650 |
| ~4.90 | ~900 |
| ~4.95 | ~550 |
| ~5.00 | ~1150 |
| ~5.05 | ~750 |
| ~5.10 | ~1150 |
| ~5.15 | ~850 |
| ~5.20 | ~1150 |
| ~5.25 | ~750 |
| ~5.30 | ~1650 |
| ~5.35 | ~1750 |
| ~5.40 | ~1650 |
| ~5.45 | ~1750 |
| ~5.50 | ~1700 |
| ~5.60 | ~1650 |
| ~5.70 | ~1450 |
| ~5.75 | ~1200 |
| ~5.80 | ~1200 |
| ~5.85 | ~950 |
| ~5.90 | ~800 |
| ~6.00 | ~1450 |
| ~6.10 | ~1850 |
| ~6.15 | ~1300 |
| ~6.20 | ~1100 |
</details>

Figure 1.26: A scatterplot showing clutch.volume (vertical axis) vs. body.size (horizontal axis).

The plot shows a discernible pattern, which suggests an **association**, or relationship, between clutch volume and body size; the points tend to lie in a straight line, which is indicative of a **linear association**. Two variables are **positively associated** if increasing values of one tend to occur with increasing values of the other; two variables are **negatively associated** if increasing values of one variable occurs with decreasing values of the other. If there is no evident relationship between two variables, they are said to be **uncorrelated** or **independent**.

As expected, clutch volume and body size are positively associated; larger frogs tend to produce egg clutches with larger volumes. These observations suggest that larger females are capable of investing more energy into offspring production relative to smaller females.

The National Health and Nutrition Examination Survey (NHANES) consists of a set of surveys and measurements conducted by the US CDC to assess the health and nutritional status of adults and children in the United States. The following example uses data from a sample of 500 adults (individuals ages 21 and older) from the NHANES dataset.<sup>38</sup>

## EXAMPLE 1.14

Body mass index (BMI) is a measure of weight commonly used by health agencies to assess whether someone is overweight, and is calculated from height and weight.<sup>39</sup> Describe the relationships shown in Figure 1.27. Why is it helpful to use BMI as a measure of obesity, rather than weight?

Figure 1.27(a) shows a positive association between height and weight; taller individuals tend to be heavier. Figure 1.27(b) shows that height and BMI do not seem to be associated; the range of BMI values observed is roughly consistent across height.

Weight itself is not a good measure of whether someone is overweight; instead, it is more reasonable to consider whether someone’s weight is unusual relative to other individuals of a comparable height. An individual weighing 200 pounds who is 6 ft tall is not necessarily an unhealthy weight; however, someone who weighs 200 pounds and is 5 ft tall is likely overweight. It is not reasonable to classify individuals as overweight or obese based only on weight.

BMI acts as a relative measure of weight that accounts for height. Specifically, BMI is used as an estimate of body fat. According to US National Institutes of Health (US NIH) and the World Health Organization (WHO), a BMI between 25.0 - 29.9 is considered overweight and a BMI over 30 is considered obese.<sup>40</sup>

![](images/page_38_chart_8.jpg)

<details>
<summary>scatter</summary>

| Height (cm) | Weight (kg) |
| --- | --- |
| ~145 | ~42 |
| ~146 | ~58 |
| ~147 | ~60 |
| ~148 | ~85 |
| ~149 | ~105 |
| ~150 | ~122 |
| ~151 | ~110 |
| ~152 | ~70 |
| ~153 | ~65 |
| ~154 | ~75 |
| ~155 | ~80 |
| ~156 | ~90 |
| ~157 | ~100 |
| ~158 | ~110 |
| ~159 | ~135 |
| ~160 | ~105 |
| ~161 | ~95 |
| ~162 | ~85 |
| ~163 | ~75 |
| ~164 | 145 |
| ~165 | ~190 |
| ~166 | ~140 |
| ~167 | ~125 |
| ~168 | ~115 |
| ~169 | ~105 |
| ~170 | ~95 |
| ~171 | ~85 |
| ~172 | ~75 |
| ~173 | ~65 |
| ~174 | ~55 |
| ~175 | ~45 |
| ~176 | ~35 |
| ~177 | ~25 |
| ~178 | ~15 |
| ~179 | ~5 |
| ~180 | ~20 |
| ~181 | ~30 |
| ~182 | ~40 |
| ~183 | ~50 |
| ~184 | ~60 |
| ~185 | ~70 |
| ~186 | ~80 |
| ~187 | ~90 |
| ~188 | ~100 |
| ~189 | ~110 |
| ~190 | 225 |
| ~191 | 122 |
| ~192 | 75 |
| ~193 | 85 |
| ~194 | 72 |
</details>

(a)

![](images/page_38_chart_10.jpg)

<details>
<summary>scatter</summary>

| Series | Height (cm) (range) | BMI (range) |
| --- | --- | --- |
| Blue circles | 145~195 | 20~70 |
| Red circle | ~164 | ~54 |
</details>

(b)

Figure 1.27: (a) A scatterplot showing height versus weight from the 500 individuals in the sample from NHANES. One participant 163.9 cm tall (about 5 ft, 4 in) and weighing 144.6 kg (about 319 lb) is highlighted. (b) A scatterplot showing height versus BMI from the 500 individuals in the sample from NHANES. The same individual highlighted in (a) is marked here, with BMI 53.83.

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">38<sub>The</sub> sample is available as nhanes.samp.adult.500 in the R oibiostat package.</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">39<sub>BMI</sub> = weightkg weightlb × 703. height2m = height2i</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">40<a href="https://www.nhlbi.nih.gov/health/educational/lose_wt/risk.htm"><sub>https</sub>://www.nhlbi.nih.gov/health/educational/lose\_wt/risk.htm</a></span></small>

![](images/page_39_image_2.jpg)

## EXAMPLE 1.15

Figure 1.28 is a scatterplot of life expectancy versus annual per capita income for 165 countries in 2011. Life expectancy is measured as the expected lifespan for children born in 2011 and income is adjusted for purchasing power in a country. Describe the relationship between life expectancy and annual per capita income; do they seem to be linearly associated?

Life expectancy and annual per capita income are positively associated; higher per capita income is associated with longer life expectancy. However, the two variables are not linearly associated. When income is low, small increases in per capita income are associated with relatively large increases in life expectancy. However, once per capita income exceeds approximately \$20,000 per year, increases in income are associated with smaller gains in life expectancy.

In a linear association, change in the y-variable for every unit of the x-variable is consistent across the range of the x-variable; for example, a linear association would be present if an increase in income of \$10,000 corresponded to an increase in life expectancy of 5 years, across the range of income.

![](images/page_39_chart_7.jpg)

<details>
<summary>bubble</summary>

| X ($) | Life Expectancy (years) |
| --- | --- |
| ~1000 | ~48 |
| ~1500 | ~52 |
| ~2000 | ~51 |
| ~2500 | ~55 |
| ~3000 | ~60 |
| ~3500 | ~63 |
| ~4000 | ~67 |
| ~4500 | ~70 |
| ~5000 | ~72 |
| ~5500 | ~74 |
| ~6000 | ~76 |
| ~6500 | ~78 |
| ~7000 | ~79 |
| ~7500 | ~81 |
| ~8000 | ~82 |
| ~8500 | ~83 |
| ~9000 | ~84 |
| ~9500 | ~85 |
| ~10000 | ~86 |
| ~10500 | ~87 |
| ~11000 | ~88 |
| ~11500 | ~89 |
| ~12000 | ~90 |
| ~12500 | ~91 |
| ~13000 | ~92 |
| ~13500 | ~93 |
| ~14000 | ~94 |
| ~14500 | ~95 |
| ~15000 | ~96 |
| ~15500 | ~97 |
| ~16000 | ~98 |
| ~16500 | ~99 |
| ~17000 | ~100 |
| ~17500 | ~101 |
| ~18000 | ~102 |
| ~18500 | ~103 |
| ~19000 | ~104 |
| ~19500 | ~105 |
| ~20000 | ~106 |
| ~21000 | ~107 |
| ~22000 | ~108 |
| ~23000 | ~109 |
| ~24000 | ~110 |
| ~25000 | ~111 |
| ~26000 | ~112 |
| ~27000 | ~113 |
| ~28000 | ~114 |
| ~29000 | ~115 |
| ~30000 | ~116 |
| ~31000 | ~117 |
| ~32000 | ~118 |
| ~33000 | ~119 |
| ~34000 | ~120 |
| ~35000 | ~121 |
| ~36000 | ~122 |
| ~37000 | ~123 |
| ~38000 | ~124 |
| ~39000 | ~125 |
| ~40000 | ~126 |
| ~41000 | ~127 |
| ~42000 | ~128 |
| ~43000 | ~129 |
| ~44000 | ~130 |
| ~45000 | ~131 |
| ~46000 | ~132 |
| ~47000 | ~133 |
| ~48000 | ~134 |
| ~49000 | ~135 |
| ~50000 | ~136 |
| ~51000 | ~137 |
| ~52000 | ~138 |
| ~53000 | ~139 |
| ~54000 | ~140 |
| ~55000 | ~141 |
| ~56000 | ~142 |
| ~57000 | ~143 |
| ~58000 | ~144 |
| ~59000 | ~145 |
| ~60000 | ~146 |
| ~61000 | ~147 |
| ~62000 | ~148 |
| ~63000 | ~149 |
| ~64000 | ~150 |
| ~65000 | ~151 |
| ~66000 | ~152 |
| ~67000 | ~153 |
| ~68000 | ~154 |
| ~69000 | ~155 |
| ~70000 | ~156 |
| ~71000 | ~157 |
| ~72000 | ~158 |
| ~73000 | ~159 |
| ~74000 | ~160 |
| ~75000 | ~161 |
| ~76000 | ~162 |
| ~77<fcel>67~78 (clustered points) |
</details>

Figure 1.28: A scatterplot of life expectancy (years) versus annual per capita income (US dollars) in the wdi.2011 dataset.

## Correlation

**Correlation** is a numerical summary statistic that measures the strength of a linear relationship between two variables. It is denoted by r, the **correlation coe**ffi**cient**, which takes on values between -1 and 1.

If the paired values of two variables lie exactly on a line, r = ±1; the closer the correlation coefficient is to ±1, the stronger the linear association. When two variables are positively associated, with paired values that tend to lie on a line with positive slope, $r > 0 .$ . If two variables are negatively associated, $r < 0 .$ A value of r that is 0 or approximately 0 indicates no apparent association between two variables.<sup>41</sup>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">41<sub>If</sub> paired values lie perfectly on either a horizontal or vertical line, there is no association and r is mathematically undefined.</span></small>

![](images/page_40_chart_2.jpg)

<details>
<summary>scatter</summary>

| X (range) | Y (range) |
| --- | --- |
| 0~100 | 0~100 |
</details>

R = 0.33

![](images/page_40_chart_4.jpg)

<details>
<summary>scatter</summary>

| X (range) | Y (range) |
| --- | --- |
| 0~100 | 0~100 |
</details>

R = 0.69

![](images/page_40_chart_6.jpg)

<details>
<summary>scatter</summary>

| X (range) | Y (range) |
| --- | --- |
| 0~100 | 0~100 |
</details>

R = 0.98

![](images/page_40_chart_8.jpg)

<details>
<summary>scatter</summary>

| X (range) | Y (range) |
| --- | --- |
| 0~100 | 0~100 |
</details>

R = 1.00

![](images/page_40_chart_10.jpg)

<details>
<summary>scatter</summary>

| X (range) | Y (range) |
| --- | --- |
| 0~100 | 0~100 |
</details>

R = −0.08

![](images/page_40_chart_12.jpg)

<details>
<summary>scatter</summary>

| X (range) | Y (range) |
| --- | --- |
| 0~100 | 0~100 |
</details>

R = −0.64

![](images/page_40_chart_14.jpg)

<details>
<summary>scatter</summary>

| X (range) | Y (range) |
| --- | --- |
| 0~100 | 0~100 |
</details>

R = −0.92

![](images/page_40_chart_16.jpg)

<details>
<summary>scatter</summary>

| X (range) | Y (range) |
| --- | --- |
| 0~100 | 0~100 |
</details>

R = −1.00

Figure 1.29: Scatterplots and their correlation coefficients. The first row shows positive associations and the second row shows negative associations. From left to right, strength of the linear association between x and y increases.

The correlation coefficient quantifies the strength of a linear trend. Prior to calculating a correlation, it is advisable to confirm that the data exhibit a linear relationship. Although it is mathematically possible to calculate correlation for any set of paired observations, such as the life expectancy versus income data in Figure 1.28, correlation cannot be used to assess the strength of a nonlinear relationship.

## CORRELATION

The correlation between two variables x and y is given by:

$$
r = \frac {1}{n - 1} \sum_ {i = 1} ^ {n} \left(\frac {x _ {i} - \overline {{x}}}{s _ {x}}\right) \left(\frac {y _ {i} - \overline {{y}}}{s _ {y}}\right), \tag {1.16}
$$

where $(x_{1},y_{1}),(x_{2},y_{2}),\cdots,(x_{n},y_{n})$ are the n paired values of x and y, and $s _ { x }$ and $s _ { y }$ are the sample standard deviations of the x and y variables, respectively.

## EXAMPLE 1.17

Calculate the correlation coefficient of x and y, plotted in Figure 1.30.

Calculate the mean and standard deviation for x and y: $\overline { { x } } = 2 ,   \overline { { y } } = 3 ,   s _ { x } = 1$ , and $s _ { y } = 2 . 6 5 .$

$$
\begin{array}{l} r = \frac {1}{n - 1} \sum_ {i = 1} ^ {n} \left(\frac {x _ {i} - \overline {{x}}}{s _ {x}}\right) \left(\frac {y _ {i} - \overline {{y}}}{s _ {y}}\right) \\ = \frac {1}{3 - 1} \left[ \left(\frac {1 - 2}{1}\right) \left(\frac {5 - 3}{2 . 6 5}\right) + \left(\frac {2 - 2}{1}\right) \left(\frac {4 - 3}{2 . 6 5}\right) + \left(\frac {3 - 2}{1}\right) \left(\frac {0 - 3}{2 . 6 5}\right) \right] \\ = - 0. 9 4. \\ \end{array}
$$

The correlation is -0.94, which reflects the negative association visible from the scatterplot in Figure 1.30.

![](images/page_41_chart_7.jpg)

<details>
<summary>scatter</summary>

| x | y |
| --- | --- |
| 1.0 | 5 |
| 2.0 | 4 |
| 3.0 | 0 |
</details>

Figure 1.30: A scatterplot showing three points: (1, 5), (2, 4), and (3, 0).

## EXAMPLE 1.18

Is it appropriate to use correlation as a numerical summary for the relationship between life expectancy and income after a log transformation is applied to both variables? Refer to Figure 1.31.

Figure 1.31 shows an approximately linear relationship; a correlation coefficient is a reasonable numerical summary of the relationship. As calculated from statistical software, $r = 0 . 7 9$ , which is indicative of a strong linear relationship.

![](images/page_42_chart_5.jpg)

<details>
<summary>scatter</summary>

| Per Capita Income (log USD) | Life Expectancy (log years) |
| --- | --- |
| ~5.6 | ~4.01 |
| ~5.9 | ~4.05 |
| ~6.0 | ~4.08 |
| ~6.1 | ~4.13 |
| ~6.2 | ~3.88 |
| ~6.2 | ~3.90 |
| ~6.3 | ~4.16 |
| ~6.4 | ~4.09 |
| ~6.5 | ~4.13 |
| ~6.6 | ~4.04 |
| ~6.7 | ~4.13 |
| ~6.8 | ~4.23 |
| ~6.9 | ~4.13 |
| ~7.0 | ~3.95 |
| ~7.1 | ~4.25 |
| ~7.2 | ~3.92 |
| ~7.3 | ~4.18 |
| ~7.4 | ~4.21 |
| ~7.5 | ~3.88 |
| ~7.6 | ~4.11 |
| ~7.7 | ~4.00 |
| ~7.8 | ~4.21 |
| ~7.9 | ~4.29 |
| ~8.0 | ~3.95 |
| ~8.1 | ~4.22 |
| ~8.2 | ~4.10 |
| ~8.3 | ~3.89 |
| ~8.4 | ~4.26 |
| ~8.5 | ~4.31 |
| ~8.6 | ~4.32 |
| ~8.7 | ~4.35 |
| ~8.8 | ~4.15 |
| ~8.9 | ~4.37 |
| ~9.0 | ~4.01 |
| ~9.1 | ~4.31 |
| ~9.2 | ~4.37 |
| ~9.3 | ~4.24 |
| ~9.4 | ~4.30 |
| ~9.5 | ~4.39 |
| ~9.6 | ~4.25 |
| ~9.7 | ~4.33 |
| ~9.8 | ~4.30 |
| ~9.9 | ~4.39 |
| ~10.0 | ~4.03 |
| ~10.1 | ~4.39 |
| ~10.2 | ~4.38 |
| ~10.3 | ~4.41 |
| ~10.4 | ~4.38 |
| ~10.5 | ~4.42 |
| ~10.6 | ~4.39 |
| ~10.7 | ~4.41 |
| ~10.8 | ~4.31 |
| ~10.9 | ~4.40 |
| ~11.0 | ~4.36 |
| ~11.1 | ~4.42 |
| ~11.2 | ~4.39 |
</details>

Figure 1.31: A scatterplot showing log(income) (horizontal axis) vs. log(life.expectancy) (vertical axis).

## 1.6.2 Two categorical variables

## Contingency tables

A **contingency table** summarizes data for two categorical variables, with each value in the table representing the number of times a particular combination of outcomes occurs.42 Figure 1.32 summarizes the relationship between race and genotype in the famuss data.

The **row totals** provide the total counts across each row and the **column totals** are the total counts for each column; collectively, these are the **marginal totals**.

|  | CC | CT | TT | Sum |
| --- | --- | --- | --- | --- |
| African Am | 16 | 6 | 5 | 27 |
| Asian | 21 | 18 | 16 | 55 |
| Caucasian | 125 | 216 | 126 | 467 |
| Hispanic | 4 | 10 | 9 | 23 |
| Other | 7 | 11 | 5 | 23 |
| Sum | 173 | 261 | 161 | 595 |

Figure 1.32: A contingency table for race and actn3.r577x.

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">42<sub>Contingency</sub> tables are also known as two-way tables.</span></small>

Like relative frequency tables for the distribution of one categorical variable, contingency tables can also be converted to show proportions. Since there are two variables, it is necessary to specify whether the proportions are calculated according to the row variable or the column variable.

Figure 1.33 shows the row proportions for Figure 1.32; these proportions indicate how genotypes are distributed within each race. For example, the value of 0.593 in the upper left corner indicates that of the African Americans in the study, 59.3% have the CC genotype.

|  | CC | CT | TT | Sum |
| --- | --- | --- | --- | --- |
| African Am | 0.593 | 0.222 | 0.185 | 1.000 |
| Asian | 0.382 | 0.327 | 0.291 | 1.000 |
| Caucasian | 0.268 | 0.463 | 0.270 | 1.000 |
| Hispanic | 0.174 | 0.435 | 0.391 | 1.000 |
| Other | 0.304 | 0.478 | 0.217 | 1.000 |

Figure 1.33: A contingency table with row proportions for the race and actn3.r577x variables.

Figure 1.34 shows the column proportions for Figure 1.32; these proportions indicate the distribution of races within each genotype category. For example, the value of 0.092 indicates that of the CC individuals in the study, 9.2% are African American.

|  | CC | CT | TT |
| --- | --- | --- | --- |
| African Am | 0.092 | 0.023 | 0.031 |
| Asian | 0.121 | 0.069 | 0.099 |
| Caucasian | 0.723 | 0.828 | 0.783 |
| Hispanic | 0.023 | 0.038 | 0.056 |
| Other | 0.040 | 0.042 | 0.031 |
| Sum | 1.000 | 1.000 | 1.000 |

Figure 1.34: A contingency table with column proportions for the race and actn3.r577x variables.

## EXAMPLE 1.19

For African Americans in the study, CC is the most common genotype and TT is the least common genotype. Does this pattern hold for the other races in the study? Do the observations from the study suggest that distribution of genotypes at r577x vary between populations?

The pattern holds for Asians, but not for other races. For the Caucasian individuals sampled in the study, CT is the most common genotype at 46.3%. CC is the most common genotype for Asians, but in this population, genotypes are more evenly distributed: 38.2% of Asians sampled are CC, 32.7% are CT, and 29.1% are TT. The distribution of genotypes at r577x seems to vary by population.

## GUIDED PRACTICE 1.20

As shown in Figure 1.34, 72.3% of CC individuals in the study are Caucasian. Do these data suggest that in the general population, people of CC genotype are highly likely to be Caucasian?<sup>43</sup>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">43<sub>No</sub>, this is not a reasonable conclusion to draw from the data. The high proportion of Caucasians among CC individuals primarily reflects the large number of Caucasians sampled in the study – 78.5% of the people sampled are Caucasian. The uneven representation of different races is one limitation of the famuss data.</span></small>

## Segmented bar plots

A **segmented bar plot** is a way of visualizing the information from a contingency table. Figure 1.35 graphically displays the data from Figure 1.32; each bar represents a level of actn3.r577x and is divided by the levels of race. Figure 1.35(b) uses the row proportions to create a standardized segmented bar plot.

![](images/page_44_chart_4.jpg)

<details>
<summary>bar_stacked</summary>

| Category | African Am | Asian | Caucasian | Hispanic | Other |
| --- | --- | --- | --- | --- | --- |
| CC | ~15 | ~25 | ~130 | ~5 | ~8 |
| CT | ~5 | ~20 | ~220 | ~10 | ~12 |
| TT | ~5 | ~18 | ~125 | ~12 | ~7 |
</details>

(a)

![](images/page_44_chart_6.jpg)

<details>
<summary>bar_stacked</summary>

| Category | African Am | Asian | Caucasian | Hispanic | Other |
| --- | --- | --- | --- | --- | --- |
| CC | ~0.10 | ~0.12 | ~0.73 | ~0.01 | ~0.04 |
| CT | ~0.02 | ~0.08 | ~0.81 | ~0.03 | ~0.05 |
| TT | ~0.03 | ~0.11 | ~0.76 | ~0.06 | ~0.03 |
</details>

(b)

Figure 1.35: (a) Segmented bar plot for individuals by genotype, with bars divided by race. (b) Standardized version of Figure (a).

Alternatively, the data can be organized as shown in Figure 1.36, with each bar representing a level of race. The standardized plot is particularly useful in this case, presenting the distribution of genotypes within each race more clearly than in Figure 1.36(a).

![](images/page_44_chart_10.jpg)

<details>
<summary>bar_stacked</summary>

| Category | CC | CT | TT |
| --- | --- | --- | --- |
| African Am | ~15 | ~10 | ~8 |
| Asian | ~20 | ~20 | ~18 |
| Caucasian | ~125 | ~235 | ~145 |
| Hispanic | ~5 | ~10 | ~10 |
| Other | ~10 | ~10 | ~10 |
</details>

(a)

![](images/page_44_chart_12.jpg)

<details>
<summary>bar_stacked</summary>

| Category | CC | CT | TT |
| --- | --- | --- | --- |
| African Am | ~0.60 | ~0.21 | ~0.18 |
| Asian | ~0.38 | ~0.32 | ~0.30 |
| Caucasian | ~0.27 | ~0.45 | ~0.26 |
| Hispanic | ~0.18 | ~0.43 | ~0.39 |
| Other | ~0.30 | ~0.47 | ~0.21 |
</details>

(b)

Figure 1.36: (a) Segmented bar plot for individuals by race, with bars divided by genotype. (b) Standardized version of Figure (a).

## Two-by-two tables: relative risk

The results from medical studies are often presented in **two-by-two tables** (2 × 2 tables), contingency tables for categorical variables that have two levels. One of the variables defines two groups of participants, while the other represents the two possible outcomes. Figure 1.37 shows a hypo thetical two-by-two table of outcome by group.

|  | Outcome A | Outcome B | Sum |
| --- | --- | --- | --- |
| Group 1 | a | b | a+b |
| Group 2 | c | d | c+d |
| Sum | a+c | b+d | a+b+c+d=n |

Figure 1.37: A hypothetical two-by-two table of outcome by group.

In the LEAP study, participants are divided into two groups based on treatment (peanut avoidance versus peanut consumption), while the outcome variable records whether an individual passed or failed the oral food challenge (OFC). The results of the LEAP study as shown in Figure 1.2 are in the form of a $: 2 \times 2$ table; the table is reproduced below as Figure 1.38.

A statistic called the **relative risk** (RR) can be used to summarize the data in a $2 \times 2$ table; the relative risk is a measure of the risk of a certain event occurring in one group relative to the risk of the event occurring in another group.<sup>44</sup>

|  | FAIL OFC | PASS OFC | Sum |
| --- | --- | --- | --- |
| Peanut Avoidance | 36 | 227 | 263 |
| Peanut Consumption | 5 | 262 | 267 |
| Sum | 41 | 489 | 530 |

Figure 1.38: Results of the LEAP study, described in Section 1.1.

The question of interest in the LEAP study is whether the risk of developing peanut allergy (i.e., failing the OFC) differs between the peanut avoidance and consumption groups. The relative risk of failing the OFC equals the ratio of the proportion of individuals in the avoidance group who failed the OFC to the proportion of individuals in the consumption group who failed the OFC.

## EXAMPLE 1.21

Using the results from the LEAP study, calculate and interpret the relative risk of failing the oral food challenge, comparing individuals in the avoidance group to individuals in the consumption group.

$$
R R _ {\text {failing OFC}} = \frac {\text {proportion in avoidance group who failed OFC}}{\text {proportion in consumption group who failed OFC}} = \frac {3 6 / 2 6 3}{5 / 2 6 7} = 7. 3 1.
$$

The relative risk is 7.31. The risk of failing the oral food challenge was more than 7 times greater for participants in the peanut avoidance group than for those in the peanut consumption group.

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">44<sub>Chapter</sub> 8 discusses another numerical summary for 2 × 2 tables, the odds ratio.</span></small>

## EXAMPLE 1.22

An observational study is conducted to assess the association between smoking and cardiovascular disease (CVD), in which researchers identified a cohort of individuals and categorized them ac cording to smoking and disease status. If the relative risk of CVD is calculated as the ratio of the proportion of smokers with CVD to the proportion of non-smokers with CVD, interpret the results of the study if the relative risk equals 1, is less than 1, or greater than 1.

![](images/page_46_image_4.jpg)

A relative risk of 1 indicates that the risk of CVD is equal for smokers and non-smokers.

A relative risk less than 1 indicates that smokers are at a lower risk of CVD than non-smokers; i.e., the proportion of individuals with CVD among smokers is lower than the proportion among non-smokers.

A relative risk greater than 1 indicates that smokers are at a higher risk of CVD than non-smokers; i.e., the proportion of individuals with CVD among smokers is higher than the proportion among non-smokers.

![](images/page_46_image_8.jpg)

## GUIDED PRACTICE 1.23

For the study described in Example 1.22, suppose that of the 231 individuals, 111 are smokers. 40 smokers and 32 non-smokers have cardiovascular disease. Calculate and interpret the relative risk of CVD.<sup>45</sup>

Relative risk relies on the assumption that the observed proportions of an event occurring in each group are representative of the risk, or incidence, of the event occurring within the populations from which the groups are sampled. For example, in the LEAP data, the relative risk assumes that the proportions 33/263 and 5/267 are estimates of the proportion of individuals who would fail the OFC among the larger population of infants who avoid or consume peanut products.

![](images/page_46_image_12.jpg)

## EXAMPLE 1.24

Suppose another study to examine the association between smoking and cardiovascular disease is conducted, but researchers use a different study design than described in Example 1.22. For the new study, 90 individuals with CVD and 110 individuals without CVD are recruited. 40 of the individuals with CVD are smokers, and 80 of the individuals without CVD are non-smokers. Should relative risk be used to summarize the observations from the new study?

Relative risk should not be calculated for these observations. Since the number of individuals with and without CVD is fixed by the study design, the proportion of individuals with CVD within a certain group (smokers or non-smokers) as calculated from the data is not a measure of CVD risk for that population.

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">45<sub>The</sub> relative risk of CVD, comparing smokers to non-smokers, is (40/111)/(32/120) = 1.35. Smoking is associated with a 35% increase in the probability of CVD; in other words, the risk of CVD is 35% greater in smokers compared to non-smokers.</span></small>

![](images/page_47_image_2.jpg)

## GUIDED PRACTICE 1.25

For a study examining the association between tea consumption and esophageal carcinoma, researchers recruited 300 patients with carcinoma and 571 without carcinoma and administered a questionnaire about tea drinking habits.<sup>46</sup> Of the 47 individuals who reported that they regularly drink green tea, 17 had carcinoma. Of the 824 individuals who reported that they never, or very rarely, drink green tea, 283 had carcinoma. Evaluate whether the proportions 17/47 and 283/824 are representative of the incidence rate of carcinoma among individuals who drink green tea regularly and those who do not.<sup>47</sup>

## RELATIVE RISK

The relative risk of Outcome A in the hypothetical two-by-two table (Figure 1.37) can be calculated using either Group 1 or Group 2 as the reference group:

$$
R R _ {\mathrm{A,comparingGroup1toGroup2}} = \frac {a / (a + b)}{c / (c + d)}
$$

$$
R R _ {\mathrm{A,comparingGroup2toGroup1}} = \frac {c / (c + d)}{a / (a + b)}
$$

The relative risk should only be calculated for data where the proportions a/(a+b) and $c / ( c   +   d )$ represent the incidence of Outcome A within the populations from which Groups 1 and 2 are sampled.

## 1.6.3 A numerical variable and a categorical variable

Methods for comparing numerical data across groups are based on the approaches introduced in Section 1.4. **Side-by-side boxplots** and **hollow histograms** are useful for directly comparing how the distribution of a numerical variable differs by category.

Recall the question introduced in Section 1.2.3: is ACTN3 genotype associated with variation in muscle function? Figure 1.39 visually shows the relationship between muscle function (measured as percent change in non-dominant arm strength) and ACTN3 genotype in the famuss data with side-by-side boxplots and hollow histograms. The hollow histograms highlight how the shapes of the distributions of ndrm.ch for each genotype are essentially similar, although the distribution for the CC genotype has less right skewing. The side-by-side boxplots are especially useful for comparing center and spread, and reveal that the T allele appears to be associated with greater muscle function; median percent change in non-dominant arm strength increases across the levels from CC to TT.

## GUIDED PRACTICE 1.26

Using Figure 1.40, assess how maternal investment varies with altitude.<sup>48</sup>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">46<sub>Tea</sub> drinking habits and oesophageal cancer in a high risk area in northern Iran: population based casecontrol study, Islami F, et al., BMJ (2009), doi 10.1136/bmj.b929</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">47<sub>The</sub> proportions calculated from the study data should not be used as estimates of the incidence rate of esophageal carcinoma among individuals who drink green tea regularly and those who do not, since the study selected participants based on carcinoma status.</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">48<sub>As</sub> a general rule, clutches found at higher altitudes have greater volume; median clutch volume tends to increase as altitude increases. This suggests that increased altitude is associated with a higher level of maternal investment.</span></small>