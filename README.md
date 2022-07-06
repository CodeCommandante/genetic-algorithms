# Evolutionary Algorithm
***
## Problem Description
---
Knapsack problems are popular examples of discrete optimization problems which arise in a number of application domains.   The goal is to maximize the value of
the collection of items placed into a container, the knapsack, which is subject to a weight constraint.  Traditionally it is addressed via dynamic programming
or branch and bound techniques.  

In this problem, we were asked to find optimal candidate solutions for the
Knapsack problem, a widely and long-studied problem.  This problem is
multi-variate, typically involving three primary variables:  a value per item, a
weight per item, and the allowable capacity (weight) of the Knapsack, not to be
exceeded.  For greater numbers of items, and corresponding values and weights,
the problem becomes computationally complex - if not impossible - given time,
memory, and CPU constraints.

Similarly to the first set of problems from Homework 1, here we are asked to use
a stochastic algorithm to attempt to find the candidate solutions to the
Knapsack problem.  Specifically, we were asked to construct an Evolutionary
Algorithm that uses recombination and mutation to generate potential solutions.
Evolutionary Algorithms are algorithms that borrow their methods from the
evolutionary model.

## Methodology
### Overview
---
Solving the Knapsack problem via a stochastic Evolutionary Algorithm (EA) introduces
an interesting paradox:  while the EA can in a sense _train_ itself to
approach candidate solutions (but, not with a high level of certainty), it also introduces several new variables into the
already mutli-variate problem.  This means that finding candidate solutions is
often a matter of performing many many tests wherein the variables are
differentiated throughout.  As discussed in class, that is why EA's are
classified as "Generate and Test" algorithms.

The introduction of new variables meant that testing was often extensive,
unpredictable, and unsatisfying - unsatisfying in that it was hard to nail down
a predictable trend that could be exploited to produce candidate solutions with
known combinations of said variables.  This notwithstanding, I was able to
construct a model that met the demonstrative and academic purposes of this
project and actually converged frequently enough to satisfy the problem.

Below, I've broken the **Results** section into two basic comparitive versions.  In the first
version of the problem, the weights are identical for all of the items,
and only the values are varied.  This version allowed me to compare a known
optimum against the results of my trials.  In the second version, the weights
are varied along with the values; which means that I am relegated to having to
trust the candidate solutions are optimal - or at the very least, "good enough".

### Variable Selection and Test Structure
---
For all the trials demonstrated below, the generations (iterations) were fixed
to 500; the "genome" length (the maximum number of items allowed in the
knapsack) was fixed at 23; and the possible values were a range from 0-22 (the
"chromosomes" in the "genome") randomly distributed.  I also placed a floor
on the lowest number of remaining candidates in a population to 4.  Without a
floor on the number of candidates that can be removed during selection, it was
possible (and very likely in low-weight limit scenarios), that the population would
"go extinct", so to speak.

Each trial consisted of having three populations, each with different population
selection sizes - 10, 50, and 100 for "Green", "Yellow", and "Blue",
respectively - run in tandem.  This allowed me to see how selection size relates
to the "stochasticity" of the algorthm.  Based on the many trials I ran
(including those not shown in this report), it would appear that selection size
corresponded to a greater likelihood of convergence towards optimal candidate
solutions.  In other words, with some regularity the "Blue" population would be
the first to converge on a candidate solution; followed by the "Yellow"
population; and finally followed by the "Green" population.  This makes sense intuitively.
Because the selected population of "Blue" is twice the size of "Yellow", and ten
times the size of "Green", the number of reproduced "children" (and, therefore,
potentially better candidate solutions) remaining in the population means a
higher likelihood of finding better candidates.

### Reproduction Method
---
I chose to model the reproduction procedure around human systems.
With an existing population, a pair of "parents" were selected at random and
used to reproduce a "child" solution.  This was done 3 times per pair of
parents, or **size(Population)\*(3/2)** times.  The new child was added to the
population, but not allowed to become part of the breeding population until the
next generation (after selection).  After the reproduction cycle was completed,
the parents in the population were killed off, leaving only the children for the
selection phase of the algorithm.

### Recombination Method
---
The recombination method took a first part of the "genome" from the first
parent and spliced it another part "genome" of the second parent.  The length of
the first splice was determined randomly, and the second splice was made up of
the difference, such that the final splicing resulted in a new "genome" of
length 23.

### Mutation Method
---
For mutation, I used a simple "bit-flip" procedure.  For each newly bred
"child" in the reproduction process, a single value in the knapsack (a single
"chromosome" in the child) was flipped to 'TRUE' or 'FALSE', representing the
presence of that value in the knapsack.

### Selection Method
---
As mentioned before, each of the three populations had their own unique
selection size.  For the "Green" population, all but 10 of the newly bred
"children" in the population are removed; for "Yellow", all but 50; and for
"Blue", all but 100.  However, before doing this, I also introduced a procedure
to kill off any overweight candidates (with the only constraint on this process
being that the population is at present above 4 candidates).  Altogether, the
procedure amounted to:  1. sort the population based on highest aggregate value
in the knapsack; 2. kill off overweight candidates (with mentioned caveat); and
3. if population is still greater than the selection size limit, remove the
lower portion.

### Summary and Final Remarks
---
Finally, I'll mention that the weight limit itself proved to be one of the
biggest determining factors in the effectiveness of this type of model.  The
lower the weight limit, the less likely the algorithm will converge without
simultaneously extending the number of generations.  With a
lower weight limit, you are forced to "throw away" far more candidate solutions
(knapsacks). which limits the "breeding" population - which, in turn, limits the
variation in new selected populations.  If the exisitng population is small and
lacking in candidate diversity, it seems to get easily trapped in a range that
can be hard to escape from - though, certainly not impossible; which is what
makes these algorithms so interesting and useful for certain types of problems.

## References
---
_For supplemental reading on the Knapsack Problem:_
[Wikipedia](https://en.wikipedia.org/wiki/Knapsack\_problem)

## Results
---
First are the results of the fixed weight solutions at weight constraint 70,
138, and 206, respectively.  The total sum of all values in my 23-item knapsack
would amount to 275.  For the latter two trials, general convergence for all
three populations occurred.  Probablistically, this should not be very surpising, as the
likelihood of generating candidates that are already below the weight constriant
goes up as the weight limit increases (this is why having **W** be greater than
the sum of all the weights would result in a trivial solution).

I've provided both the plots and the listing of the top five candidate solutions
generated for each population.  The populations are color coded and the black
line represents the general convergence trend for all three.  Below the plots
I've included listings for the trial outcomes.  The top five candidates along
with their corresponding weights and values are shown.  The inclusion of the
"Genome" is merely for fun.

I also included a **V/W** column merely for academic
interest.  In another version of this problem, one could imagine that rather
than evaluate candidates solely on their maximized value (below the weight
constraint), you might consider which candidates have the highest
value-per-weight.  That is, which knapsacks are proportionally high in value and
low in weight.

Here is fixed-weight Trial 1.  Weight limit 70.  For this Trial, none of
the populations ultimately converged on acceptable candidate solutions.
![Trial 1](https://github.com/CodeCommandante/ThePeoplesRepo/tree/main/Natural%20Computing/Genetic%20Algorithms/plots/Trial(70-F).png)

POPULATION "GREEN"
|Genome|Weight|Value|V/W|
|------|------|-----|---|
|10101000100101010000101  |      108 |       95|       0.8796296296296297|
|10101010000101010010101 |       120 |       95 |      0.7916666666666666|
|10101000000100000010111  |      96    |     80  |     0.8333333333333334|
|10101000000000000010111   |     84    |     76     |  0.9047619047619048|
|00101000000101010000101    |    84     |    76     |  0.9047619047619048|

POPULATION "YELLOW"
|Genome|Weight|Value|V/W|
|------|------|-----|---|
|01101010000110111000101 |       132 |       93 |      0.7045454545454546|
|00001011100110111000001  |      120  |      80  |     0.6666666666666666|
|01101010000110111000001   |     120   |     73   |    0.6083333333333333|
|00001011000110111000001    |    108    |    66    |   0.6111111111111112|
|00001011000110111000001     |   108     |   66     |  0.6111111111111112|

POPULATION "BLUE"
|Genome|Weight|Value|V/W|
|------|------|-----|---|
|00000011001100000110001|        84|        83  |     0.9880952380952381|
|00000011001110001010001 |       96 |       78   |    0.8125|
|00000011001100000010001  |      72  |      64    |   0.8888888888888888|
|00000011001100001000001   |     72   |     63     |  0.875|
|00000011001000011000001    |    72    |    62      | 0.8611111111111112|
\end{verbatim}

Here is fixed-weight Trial 2.  Weight limit 138.  Here, all three
populations had no trouble converging very very quickly.  In spite of this, the
trend appeared to be away from convergence over time:
![Trial 2](https://github.com/CodeCommandante/ThePeoplesRepo/tree/main/Natural%20Computing/Genetic%20Algorithms/plots/Trial(138-F).png)

POPULATION "GREEN"
|Genome|Weight|Value|V/W|
|------|------|-----|---|
|01110111100001011000001|        132 |       142|       1.0757575757575757|
|11000111101001011000001 |       132  |      140 |      1.0606060606060606|
|11000111101001011000001  |      132   |     140  |     1.0606060606060606|
|11100111101001011000000   |     132    |    138   |    1.0454545454545454|
|01100111100001011000001    |    120     |   127    |   1.0583333333333333|

POPULATION "YELLOW"
|Genome|Weight|Value|V/W|
|------|------|-----|---|
|11010101101001001100100 |       132  |      179|       1.356060606060606|
|01111100101001001100100  |      132   |     173 |      1.3106060606060606|
|01111101000001001110100   |     132    |    173  |     1.3106060606060606|
|01010101001101001010101    |    132     |   169   |    1.2803030303030303|
|10010101101101000110100    |    132      |  168    |   1.2727272727272727|

POPULATION "BLUE"
|Genome|Weight|Value|V/W|
|------|------|-----|---|
|01100101001001001110101|        132|        178 |      1.3484848484848484|
|01000101101001101110001 |       132 |       170  |     1.2878787878787878|
|01010100001001011110101  |      132  |      169   |    1.2803030303030303|
|01000101101101000101101   |     132   |     168    |   1.2727272727272727|
|00010101101001001111010    |    132    |    167     |  1.2651515151515151|

Here is fixed-weight Trial 3.  Weight limit 206.  Again, no major issue
converging - as would be expected from a higher tolerable weight limit:
![Trial 3](https://github.com/CodeCommandante/ThePeoplesRepo/tree/main/Natural%20Computing/Genetic%20Algorithms/plots/Trial(206-F).png)

POPULATION "GREEN"
|Genome|Weight|Value|V/W|
|------|------|-----|---|
|11111101101011100111011 |       204|        213 |      1.0441176470588236|
|11111101101011010111011  |      204 |       209  |     1.0245098039215685|
|01111100101011011111110   |     192  |      207   |    1.078125|
|11111101101011000111011    |    192   |     206    |   1.0729166666666667|
|01111101101011011111001     |   192    |    206     |  1.0729166666666667|

POPULATION "YELLOW"
|Genome|Weight|Value|V/W|
|------|------|-----|---|
|11111101101001101111101|        204 |       233|       1.142156862745098|
|11111101101101101110101 |       204  |      231 |      1.1323529411764706|
|11011101101111100111101  |      204   |     218  |     1.0686274509803921|
|11011111101101100111101   |     204    |    217   |    1.0637254901960784|
|11011101101101101101101    |    192     |   215    |   1.1197916666666667|

POPULATION "BLUE"
|Genome|Weight|Value|V/W|
|------|------|-----|---|
|11011101101001111110111|        204|        231|       1.1323529411764706|
|01111101101001111111110 |       204 |       230 |      1.1274509803921569|
|11111101101101001111110  |      204  |      229  |     1.1225490196078431|
|11111101101001011111101   |     204   |     229   |    1.1225490196078431|
|11111101101011101110110    |    204    |    228    |   1.1176470588235294|

Below are the results of the variable-weight trials.  Here the _sum_ of
the weights amount to 276 and again the sum of the values amount to 275.  Each
weight is unique and is in the range 1-23 (a 23-item knapsack or "genome").

Here is variable-weight Trial 1.  Weight limit 70.  The Blue population
appeared to find solutions first, the Yellow second, and the Green not all.  The
trend overall was towards finding solutions.
![V Trial 1](https://github.com/CodeCommandante/ThePeoplesRepo/tree/main/Natural%20Computing/Genetic%20Algorithms/plots/Trial(70).png)

POPULATION "GREEN"
|Genome|Weight|Value|V/W|
|------|------|-----|---|
|01111011001010001100100|        140|        137|       0.9785714285714285|
|01111011001010001100000 |       117 |       117 |      1.0|
|01111010101000001100000  |      97   |      111  |     1.1443298969072164|
|01111010001010001100000   |     106   |     99    |    0.9339622641509434|
|01111010001000001100000    |    88     |    97     |   1.1022727272727273|

POPULATION "YELLOW"
|Genome|Weight|Value|V/W|
|------|------|-----|---|
|01010100101001001010000 |       59  |      130 |      2.2033898305084745|
|01011001001001001011000  |      66   |     126  |     1.9090909090909092|
|11010001001001001001001   |     65    |    121   |    1.8615384615384616|
|10010001101001001011000    |    58     |   121    |   2.086206896551724|
|01010110001001001010000     |   69      |  117     |  1.6956521739130435|

POPULATION "BLUE"
|Genome|Weight|Value|V/W|
|------|------|-----|---|
|01011001101001000011000  |      65|        128 |      1.9692307692307693|
|01010100001001000101001   |     67 |       127  |     1.8955223880597014|
|11010001101001001001000    |    57  |      124   |    2.175438596491228|
|01010001001001000101010     |   58   |     122    |   2.103448275862069|
|01010001101001000011000      |  49    |    120     |  2.4489795918367347|

Here is variable-weight Trial 2.  Weight limit 138.  Almost identical
results to the fixed-weight Trial 2:
![V Trial 2](https://github.com/CodeCommandante/ThePeoplesRepo/tree/main/Natural%20Computing/Genetic%20Algorithms/plots/Trial(138-F).png)


POPULATION "GREEN"
|Genome|Weight|Value|V/W|
|------|------|-----|---|
|01110101101001001111100|        130|        202 |      1.5538461538461539|
|11010101001001101111011 |       133 |       192  |     1.443609022556391|
|01010101001001001111101  |      118  |      190   |    1.6101694915254237|
|01010101101001101011011   |     124   |     182    |   1.467741935483871|
|11011101001001001101011    |    121    |    180     |  1.487603305785124|

POPULATION "YELLOW"
|Genome|Weight|Value|V/W|
|------|------|-----|---|
|01111101101001001101001 |       133|        188|       1.413533834586466|
|11110101101001100110001  |      136 |       187 |      1.375|
|11110101101001100110010   |     131  |      186  |     1.4198473282442747|
|01110101101001110111000    |    132   |     180   |    1.3636363636363635|
|01011101001001100110011     |   130    |    177    |   1.3615384615384616|

POPULATION "BLUE"
|Genome|Weight|Value|V/W|
|------|------|-----|---|
|11110101101001000111011 |       131|        196|       1.4961832061068703|
|01111101101001001110001  |      136 |       195 |      1.4338235294117647|
|01011101101001000110101   |     129  |      194  |     1.503875968992248|
|01010111101001001111100    |    129   |     194   |    1.503875968992248|
|11010101101001010110101     |   132    |    194    |   1.4696969696969697|

Here is variable-weight Trial 3.  Weight limit 206.  Trending towards
convergence, as expected given the higher weight limit.
![V Trial 3](https://github.com/CodeCommandante/ThePeoplesRepo/tree/main/Natural%20Computing/Genetic%20Algorithms/plots/Trial(206).png)

POPULATION "GREEN"
|Genome|Weight|Value|V/W|
|------|------|-----|---|
|01111110101011001101111|        194|        203|       1.0463917525773196|
|01110111001011101110110 |       187 |       202 |      1.0802139037433156|
|10111101101011000101111  |      175  |      197  |     1.1257142857142857|
|11111110101011000101111   |     189   |     196   |    1.037037037037037|
|10111111101011101110010    |    188    |    193    |   1.0265957446808511|

POPULATION "YELLOW"
|Genome|Weight|Value|V/W|
|------|------|-----|---|
|11111101101101001111110|        185|        229|       1.2378378378378379|
|11011101101011101111110 |       182 |       225 |      1.2362637362637363|
|11110101101111101110110  |      204  |      224  |     1.0980392156862746|
|11111111101001101111011   |     197   |     224   |    1.1370558375634519|
|11011101101001011111101    |    162    |    220    |   1.3580246913580247|

POPULATION "BLUE"
|Genome|Weight|Value|V/W|
|------|------|-----|---|
|11110101101001101111111|        185|        235|       1.2702702702702702|
|11111101101001110111111 |       205 |       234 |      1.1414634146341462|
|11011101101001101111111  |      181  |      234  |     1.292817679558011|
|11111101001001111111111   |     206   |     232   |    1.1262135922330097|
|11011111101001101110111    |    196    |    229    |   1.1683673469387754|

## Credits
Additional credit to Dr. Jeff McGough from South Dakota School of Mines and Technology for providing his students with these fun and challenging problems.
