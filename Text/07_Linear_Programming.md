# Chapter 7: Linear programming and reductions

## reductions

Manyoftheproblemsforwhichwewantalgorithmsare*optimization*tasks: the*shortest*path,

the *cheapest* spanning tree, the *longest* increasing subsequence, and so on. In such cases, we

seek a solution that (1) satis es certain constraints (for instance, the path must use edges

of the graph and lead from $s$ to $t,$ the tree must touch all nodes, the subsequence must be

increasing);and(2)isthebestpossible,withrespecttosomewell-de nedcriterion, amongall

solutionsthatsatisfythese constraints.

*Linear* *programming* describes a broad class of optimization tasks in which both the con-

straintsandtheoptimizationcriterionare*linearfunctions*. Itturnsoutanenormousnumber

of problems canbeexpressed inthisway.

Giventhevastnessofitstopic,thischapterisdividedintoseveralparts,whichcanberead

separately subjectto the followingdependencies.

Flows and

matchings

Introduction to

Duality

linear programming

Games

and reductions

Simplex

## 7.1 An introduction to linear programming

In a linear programming problem we are given a set of variables, and we want to assign real

valuestothemsoasto(1)satisfyasetoflinearequationsand/orlinearinequalitiesinvolving

these variablesand(2)maximizeor minimizeagivenlinearobjective function.

201

202

Algorithms

```mermaid
flowchart TD %% Figure 7.1 (a) The feasible region for a linear program. n0[" "] n1[" "] n0 --> n1
```

*Figure 7.1 (a) The feasible region for a linear program.*

(b) Contour lines of the objective

function: $x_1+6x_2$ $=c$for different valuesof the pro t $c$.

$$x_2$$

$$x_2$$

(a)

(b)

400

400

Optimumpoint

Pro t$=$1900$

300

300

$$c=1500$$

200

200

$$c=1200$$

100

100

$$c=600$$

$$x_1$$

$$x_1$$

100

200

300

400

100

200

300

400

0

0

### 7.1.1 Example: pro t maximization

A boutique chocolatier has two products:

its agship assortment of triangular chocolates,

called*Pyramide*,andthemoredecadentanddeluxe*PyramideNuit*. Howmuchofeachshould

it produce to maximizepro ts? Let's say it makes $x_1$ boxes of Pyramide per day, at apro t of

$$1$each,and$x_2$ boxesofNuit,atamoresubstantialpro tof$$6$apiece;$x_1$ and$x_2$ areunknown

valuesthatwewishtodetermine. Butthisisnotall;therearealsosomeconstraintson$x_1$ and

$x_2$ that must be accommodated (besides the obvious one, $x_1;x_2$

$0)$. First, the daily demand

for these exclusive chocolates is limited to at most $200$ boxes of Pyramide and $300$ boxes of

Nuit. Also,thecurrentworkforcecanproduceatotalofatmost$400$boxesofchocolateperday.

Whatare theoptimallevelsof production?

We represent the situationbya*linear* *program*, asfollows.

Objective function $maxx_1+6x_2$

$$x_1$$

$$200$$

Constraints

$$x_2$$

$$300$$

$$x_1+x_2$$

$$400$$

$$x_1;x_2$$

$$0$$

A linear equation in $x_1$ and $x_2$ de nes a line in the two-dimensional (2D) plane, and a

linear inequality designates a *half-space*, the region on one side of the line. Thus the set

of all *feasible* *solutions* of this linear program, that is, the points $(x_1;x_2)$ which satisfy all

constraints,istheintersectionof vehalf-spaces. Itisaconvexpolygon,showninFigure7.1.

We want to nd the point in this polygon at which the objective function the pro t is

maximized. Thepoints withapro t of $c$ dollarslieonthe line$x_1+6x_2$ $=c,$ whichhasaslope

$1=6$ and is shown in Figure 7.1 for selected values of $c$. As $c$ increases, this pro t line

of

moves parallel to itself, up and to the right. Since the goal is to maximize $c,$ we must move

S.Dasgupta,C.H.Papadimitriou,andU.V.Vazirani

203

the line as far up as possible, while still touching the feasible region. The optimum solution

will be the very last feasible point that the pro t line sees and must therefore be a vertex of

the polygon, as shown in the gure. If the slope of the pro t line were different, then its last

contact withthe polygoncouldbeanentire edge rather thanasinglevertex. Inthiscase, the

optimumsolutionwouldnot beunique,butthere wouldcertainlybeanoptimumvertex.

It is a general rule of linear programs that the optimum is achieved at a vertex of the

feasible region. The only exceptions are cases in whichthere is no optimum; this can happen

intwo ways:

1. Thelinearprogramis*infeasible*;thatis,theconstraintsaresotightthatitisimpossible

to satisfyallof them. For instance,

$$x$$

$$1; x$$

$$2:$$

2. The constraints are so loose that the feasible region is *unbounded*, and it is possible to

achieve arbitrarilyhighobjective values. For instance,

$$max x_1+x_2$$

$$x_1;x_2$$

$$0$$

**Solvinglinear** **programs**

Linear programs (LPs) can be solved by the *simplex* *method*, devised by George Dantzig in

1947. We shall explain it in more detail in Section 7.6, but brie y, this algorithm starts at a

vertex, in our case perhaps $(0;0),$ and repeatedly looks for an adjacent vertex (connected by

an edge of the feasible region) of better objective value. In this way it does *hill-climbing* on

theverticesofthepolygon,walkingfromneighbortoneighborsoastosteadilyincreasepro t

alongthe way. Here'sapossibletrajectory.

Pro t$1900

300

$1400

200

100

$200

$0

0

100

200

Upon reaching a vertex that has no better neighbor, simplex declares it to be optimal and

halts. Why does this *local* test imply *global* optimality? By simple geometry think of the

pro t linepassing throughthis vertex. Since allthe vertex's neighbors lie below the line, the

rest of thefeasiblepolygonmustalsoliebelowthisline.

204

Algorithms

```mermaid
flowchart TD %% Figure 7.2 Thefeasiblepolyhedron for athree-variablelinearprogram. n0[" "] n1[" "] n0 --> n1
```

*Figure 7.2 Thefeasiblepolyhedron for athree-variablelinearprogram.*

$$x_2$$

Optimum

$$x_1$$

$$x_3$$

**More** **products**

Encouragedbyconsumerdemand,the chocolatier decides to introduce athirdandeven more

exclusivelineofchocolates,called*PyramideLuxe*. Oneboxofthesewillbringinapro tof$$13$.

Let$x_1;x_2;x_3$ denotethenumberofboxesofeachchocolateproduceddaily,with$x_3$ referringto

Luxe. The old constraints on $x_1$ and $x_2$ persist, althoughthe labor restriction now extends to

$x_3$ as well: the sum of all three variables can be at most $400$. What's more, it turns out that

Nuit and Luxe require the same packaging machinery, except that Luxe uses it three times

as much, which imposes another constraint $x_2$ $+3x_3$

$600$. What are the best possible levels

of production?

Here isthe updated linearprogram.

$$max x_1+6x_2+13x_3$$

$$x_1$$

$$200$$

$$x_2$$

$$300$$

$$x_1+x_2+x_3$$

$$400$$

$$x_2+3x_3$$

$$600$$

$$x_1;x_2;x_3$$

$$0$$

S.Dasgupta,C.H.Papadimitriou,andU.V.Vazirani

205

Thespace ofsolutionsisnowthree-dimensional. Eachlinearequationde nesa3Dplane,

andeachinequalityahalf-spaceononesideoftheplane. Thefeasibleregionisanintersection

ofsevenhalf-spaces,apolyhedron(Figure7.2). Lookingatthe gure,canyoudecipher which

inequalitycorresponds to eachface of the polyhedron?

A pro t of $c$ corresponds to the plane $x_1+6x_2$ $+13x_3$ $=$ $c$. As $c$ increases, this pro t-plane

movesparalleltoitself,furtherandfurtherintothepositiveorthantuntilitnolongertouches

the feasible region. The point of nal contact is the optimal vertex: $(0;300;100),$ with total

pro t
$$3100$.

How would the simplex algorithm behave on this modi ed problem? As before, it would

move from vertex to vertex, alongedges of thepolyhedron, increasingpro t steadily. Apossi-

ble trajectory is shown in Figure 7.2, corresponding to the following sequence of vertices and

pro ts:

$$(0;300;100)$$

$$(200;0;200)$$

$$(200;200;0)$$

$$(200;0;0)$$

$$(0;0;0)$$

$$$3100$$

$$$2800$$

$$$1400$$

$$$200$$

$$$0$$

$$!$$

$$!$$

$$!$$

$$!$$

Finally, upon reaching a vertex with no better neighbor, it would stop and declare this to be

the optimal point. Once again by basic geometry, if all the vertex's neighbors lie on one side

of the pro t-plane, thenso mustthe entire polyhedron.

**A** **magic** **trick** **called** **duality**

Hereiswhyyoushouldbelievethat$(0;300;100),$ withatotalpro tof$$3100,$ istheoptimum:

Look back at the linear program. Add the second inequality to the third, and add to them

the fourthmultipliedby$4$. Theresult isthe inequality$x_1+6x_2+13x_3$

$3100$.

Doyousee? Thisinequalitysaysthatnofeasiblesolution(values$x_1;x_2;x_3$ satisfyingthe

constraints)canpossiblyhaveapro t greater than$3100$. Sowemustindeed havefoundthe

optimum! The only question is, where did we get these mysterious multipliers $(0;1;1;4)$ for

the fourinequalities?

In Section 7.4 we'll see that it is always possible to come up with such multipliers by

solvinganother LP!Except that (it gets even better) we do not even need to solve this other

LP, because it is in fact so intimately connected to the original one it is called the *dual*

that solving the original LP solves the dual as well! But we are getting far ahead of our

story.

What if we add a fourth line of chocolates, or hundreds more of them? Then the problem

becomes high-dimensional, and hard to visualize. Simplex continues to work in this general

setting, although we can no longer rely upon simple geometric intuitions for its description

andjusti cation. We willstudy thefulledged simplexalgorithminSection 7.6.

Inthe meantime, we canrest assured inthe knowledge that there are manyprofessional,

industrial-strength packages that implement simplex and take care of all the tricky details

likenumericprecision. Inatypicalapplication,themaintaskisthereforetocorrectlyexpress

the problemasalinearprogram. Thepackagethentakes care of therest.

Withthisinmind,let'slookat ahigh-dimensionalapplication.

206

Algorithms

### 7.1.2 Example: production planning

This time, our company makes handwoven carpets, a product for which the demand is ex-

tremely seasonal. Ouranalysthasjustobtaineddemandestimates for allmonthsof the next

calendaryear: $d_1;d_2;:::;d_{12}$. Asfeared, theyare very uneven,rangingfrom 440to 920.

Here's a quick snapshot of the company. We currently have 30 employees, each of whom

makes 20 carpets per month and gets a monthly salary of
$$2;000$. We have no initial surplus

of carpets.

Howcanwehandlethe uctuationsindemand? There are three ways:

1. *Overtime*, but this is expensive since overtime pay is $80%$ more than regular pay. Also,

workers canputinat most $30%$ overtime.

2. *Hiring* *and* *ring*,butthese cost $320and$400,respectively, per worker.

3. *Storing* *surplus* *production*, but this costs $8 per carpet per month. We currently have

no stored carpets on hand,andwemustend theyear withoutanycarpets stored.

Thisrather involvedproblem canbe formulated andsolved asalinearprogram!

Acrucial rststep isde ningthevariables.

$w_i$ $=$ numberof workers during$i$thmonth; $w_0$ $=30$.

$x_i$ $=$ numberof carpets madeduring$i$th month.

$o_i$ $=$ numberof carpets madebyovertime inmonth$i$.

$h_i;f_i$ $=$ numberof workers hiredand red, respectively, at beginningof month$i$.

$s_i$ $=$ numberof carpets stored atendof month$i$; $s_0$ $=0$.

Allinall,there are 72variables(74ifyoucount $w_0$ and$s_0)$.

We nowwritethe constraints. First,allvariablesmustbe nonnegative:

$$w_i;x_i;o_i;h_i;f_i;s_i$$

$$0;$$

$$i=1;:::;12:$$

Thetotalnumberofcarpets madepermonthconsistsofregularproductionplusovertime:

$$x_i =20w_i+o_i$$

(one constraint for each $i$ $=$ $1;:::;12)$. The number of workers can potentially change at the

start of each month:

$$w_i =w_i$$

$$_1+h_i$$

$$f_i:$$

The number of carpets stored at the end of each month is what we started with, plus the

numberwemade, minusthedemandfor themonth:

$$s_i =s_i$$

$$_1+x_i$$

$$d_i:$$

Andovertime islimited:

$$o_i$$

$$6w_i:$$

S.Dasgupta,C.H.Papadimitriou,andU.V.Vazirani

207

Finally,whatisthe objective function? It isto minimizethetotal cost:

$$o_i;$$

$$s_i + 180$$

$$f_i + 8$$

$$h_i + 400$$

$$w_i + 320$$

$$min 2000$$

$$X^i$$

$$X^i$$

$$X^i$$

$$X^i$$

$$X^i$$

a linear function of the variables. Solving this linear program by simplex should take less

thanasecond andwillgiveustheoptimum businessstrategy for our company.

Well, almost. Theoptimum solution mightturn out to be *fractional*; for instance, it might

involvehiring$10:6$ workers inthemonthofMarch. Thisnumberwouldhaveto beroundedto

either $10$ or $11$ in order to make sense, and the overall cost would then increase correspond-

ingly. In the present example, most of the variablestake on fairlylarge (double-digit) values,

and thus rounding is unlikely to affect things too much. There are other LPs, however, in

which rounding decisions have to be made very carefully in order to end up with an integer

solutionof reasonablequality.

In general, there is a tension in linear programming between the ease of obtaining frac-

tional solutions and the desirability of integer ones. As we shall see in Chapter 8, nding

the optimum integer solution of an LP is an important but very hard problem, called *integer*

*linear* *programming.*

### 7.1.3 Example: optimum bandwidth allocation

Next we turn to a miniaturized version of the kind of problem a network service provider

mightface.

Suppose we are managing a network whose lines have the bandwidths shown in Fig-

ure 7.3, and we need to establish three connections: between users $A$ and $B,$ between $B$

and $C,$ and between $A$ and $C$. Each connection requires at least two units of bandwidth, but

can be assigned more. Connection $A$ $B$ pays $3 per unit of bandwidth, and connections $B$ $C$

and$A$ $C$ pay$2and$4,respectively.

Eachconnectioncanberoutedintwoways,alongpathandashortpath,orbyacombina-

tion: for instance, two unitsof bandwidthvia the short route, one viathe long route. How do

weroute these connections to maximizeour network'srevenue?

This is a linear program. We have variables for each connection and each path (long or

short); for example, $x_{AB}$ is the short-path bandwidth allocated to the connection between $A$

and$B,$and$x_{0AB}$ thelong-pathbandwidthforthissameconnection. Wedemandthatnoedge's

bandwidthisexceeded andthateachconnection gets abandwidthof atleast2units.

208

Algorithms

```mermaid
flowchart TD %% Figure 7.3 A communications network between three users A;B, and C. Bandwidths are n0[" "] n1[" "] n2[" "] n3[" "] n4[" "] n5[" "] n6[" "] n7[" "] n8[" "] n9[" "] n10[" "] n11[" "] n12[" "] n13[" "] n14[" "] n15[" "] n16[" "] n0 --- n1 n2 --> n3 n4 --> n5 n6 --> n7 n8 --> n9 n10 --> n11 n12 --> n13 n14 --- n12 n15 --- n16
```

*Figure 7.3 A communications network between three users A;B, and C. Bandwidths are*

shown.

user

A

12

a

11

6

c

b

13

8

10

user

user

C

B

$$max 3x_{AB} +3x_{0AB} +2x_{BC} +2x_{0BC} +4x_{AC} +4x_{0AC}$$

$$10$$

[edge $(b;B)]$

$$x_{AB} +x_{0AB} +x_{BC} +x_{0BC}$$

$$x_{AB} +x_{0AB} +x_{AC} +x_{0AC}$$

$$12$$

[edge $(a;A)]$

$$x_{BC} +x_{0BC} +x_{AC} +x_{0AC}$$

$$8$$

[edge $(c;C)]$

$$6$$

[edge $(a;b)]$

$$x_{AB} +x_{0BC} +x_{0AC}$$

$$x_{0AB} +x_{BC} +x_{0AC}$$

$$13$$

[edge $(b;c)]$

$$x_{0AB} +x_{0BC} +x_{AC}$$

$$11$$

[edge $(a;c)]$

$$x_{AB} +x_{0AB}$$

$$2$$

$$2$$

$$x_{BC} +x_{0BC}$$

$$x_{AC} +x_{0AC}$$

$$2$$

$$x_{AB};x_{0AB};x_{BC};x_{0BC};x_{AC};x_{0AC}$$

$$0$$

Evenatinyexamplelikethisoneishardtosolveonone'sown(tryit!),andyettheoptimal

solutionisobtainedinstantaneouslyviasimplex:

$$x_{AB} =0; x_{0AB} =7; x_{BC} =x_{0BC} =1:5; x_{AC} =0:5; x_{0AC} =4:5:$$

Thissolutionisnotintegral,butinthepresent applicationwedon'tneedittobe,andthusno

roundingisrequired. Lookingbackattheoriginalnetwork,weseethateveryedgeexcept$a$ $c$

isused atfullcapacity.

One cautionary observation: our LP has one variable for every possible path between the

users. Inalargernetwork,therecouldeasilybeexponentiallymanysuchpaths,andtherefore

S.Dasgupta,C.H.Papadimitriou,andU.V.Vazirani

209

thisparticularwayoftranslatingthenetworkproblemintoanLPwillnotscalewell. Wewill

see acleverer andmore scalableformulationinSection 7.2.

Here's a parting question for you to consider. Suppose we removed the constraint that

each connection shouldreceive atleast twounitsof bandwidth. Wouldtheoptimumchange?

**Reductions**

Sometimes a computational task is suf ciently general that any subroutine for it can also

be used to solve a variety of other tasks, which at rst glance might seem unrelated. For

instance, we saw in Chapter 6 how an algorithm for nding the longest path in a dag can,

surprisingly,alsobeusedfor ndinglongestincreasingsubsequences. Wedescribethisphe-

nomenon by saying that the longest increasing subsequence problem *reduces* *to* the longest

path problem in a dag. In turn, the longest path in a dag reduces to the shortest path in a

dag;here'showasubroutinefor the latter canbeused to solvethe former:

function LONGEST PATH($G)$

negate alledge weightsof $G$

return SHORTEST PATH($G)$

Let's step back and take a slightlymore formal view of reductions. If anysubroutine for

task $Q$ can also be used to solve $P,$ we say $P$ *reduces* *to* $Q$. Often, $P$ is solvable by a single

callto$Q$'ssubroutine,whichmeansanyinstance$x$of$P$ canbetransformedintoaninstance

$y$ of $Q$suchthat$P(x)$ canbededuced from $Q(y)$:

Algorithmfor$P$

$$Q(y)$$

$$y$$

Algorithm

$$P(x)$$

$$x$$

Postprocess

Preprocess

for$Q$

(Do you see thatthe reduction from $P$ $=$ LONGEST PATH to $Q$ $=$ SHORTEST PATH follows

thisschema?) Ifthepreandpostprocessing procedures areef cientlycomputablethenthis

creates anef cient algorithmfor $P$ out of *any*ef cient algorithmfor $Q$!

Reductions enhance the power of algorithms: Once we have an algorithm for problem

$Q$ (which could be shortest path, for example) we can use it to solve other problems. In

fact, most of the computational tasks we study in this book are considered core computer

science problems precisely because they arise in so many different applications, which is

another way of saying that many problems reduce to them. This is especially true of linear

programming.

210

Algorithms

### 7.1.4 Variantsof linear programming

Asevidenced inourexamples, agenerallinearprogram hasmanydegrees of freedom.

1. It canbeeither amaximizationor aminimizationproblem.

2. Its constraints canbe equationsand/or inequalities.

3. The variables are often restricted to be nonnegative, but they can also be unrestricted

insign.

We willnow show that these various LP options *can* *all* *be* *reduced* *to* *one* *another* via simple

transformations. Here'show.

1. To turn a maximization problem into a minimization (or vice versa), just multiply the

$1$.

coef cients of the objective functionby

$$n$$

$$_{i=1}a_ix_i$$

$b$ into an equation, introduce a new

2a. To turn an inequality constraint like

variable$s$anduse

$$P$$

$$n$$

$$a_ix_i+s = b$$

$$X^{i=1}$$

$$s$$

$$0:$$

This $s$ is called the *slack* *variable* for the inequality. As justi cation, observe that a

vector $(x_1;:::;x_n)$ satis esthe originalinequalityconstraint ifandonlyifthere issome

$$s$$

$0$ for whichitsatis esthe newequalityconstraint.

2b. To change anequalityconstraint into inequalitiesiseasy: rewrite $ax$ $=$ $b$ as the equiva-

lent pairof constraints$ax$

$b$ and$ax$

$b$.

3. Finally,to dealwithavariable$x$ thatisunrestricted insign,do thefollowing:

Introduce two nonnegativevariables,$x^+;x$

$0$.

Replace$x,$whereveritoccursintheconstraintsortheobjectivefunction,by$x^+$

$x$ .

This way, $x$ can take on any real value by appropriately adjusting the new variables.

More precisely, any feasible solution to the original LP involving $x$ can be mapped to a

feasiblesolutionof the newLPinvolving$x^+;x$ ,andvice versa.

Byapplyingthese transformations we canreduce anyLP(maximizationor minimization,

with both inequalitiesand equations, and with both nonnegative and unrestricted variables)

into an LP of a much more constrained kind that we call the *standard* *form*, in which the

variables are all nonnegative, the constraints are all equations, and the objective function is

to beminimized.

For example, our rst linearprogram gets rewritten thus:

S.Dasgupta,C.H.Papadimitriou,andU.V.Vazirani

211

$$min$$

$$x_1$$

$$6x_2$$

$$max x_1+6x_2$$

$$x_1+s_1 =200$$

$$x_1$$

$$200$$

## =

$$x_2+s_2 =300$$

$$x_2$$

$$300$$

## )

$$x_1+x_2+s_3 =400$$

$$x_1+x_2$$

$$400$$

$$x_1;x_2;s_1;s_2;s_3$$

$$0$$

$$x_1;x_2$$

$$0$$

The original was also in a useful form: maximize an objective subject to certain inequalities.

AnyLPcanlikewisebe recast inthisway,usingthe reductions givenearlier.

**Matrix-vector** **notation**

Alinearfunctionlike$x_1+6x_2$ canbewritten asthe dot product of two vectors

$$1$$

$$x_1$$

$$c =$$

and $x=$

$$;$$

$$6$$

$$x_2$$

$x$or $c^Tx$. Similarly,linearconstraintscanbecompiled into matrix-vector form:

denoted $c$

$$200$$

$$1 0$$

$$x_1$$

$$200$$

$$x_1$$

$$=$$

$$:$$

$$300$$

$$0 1$$

$$x_2$$

$$300$$

$$) 0$$

$$x_2$$

$$0$$

$$1$$

$$1$$

$$400$$

$$1 1$$

$$x_1+x_2$$

$$400$$

$$@$$

$$@$$

$$A$$

$$A$$

$$A$$

$$x$$

$$b$$

$${z$$

$$}$$

$$| {z }$$

$$|$$

Here each row of matrix $A$ corresponds to one constraint: its dot product with $x$ is at most

the value in the corresponding row of $b$. In other words, if the rows of $A$ are the vectors

$a_1;:::;a_m,$thenthe statement $Ax$

$b$isequivalentto

$$a_i$$

$$x$$

$b_i$ for all$i$ $=1;:::;m$.

Withthese notationalconveniences, ageneric LPcanbeexpressed simplyas

$$max c^Tx$$

$$Ax$$

$$b$$

$$x$$

$$0:$$

## 7.2 Flows in networks

### 7.2.1 Shipping oil

```mermaid
flowchart TD %% Figure 7.4(a) shows a directed graph representing a network of pipelines along which oil can v0["x"] v1["ai"] v2["max cTx"] v3["Ax"] v4["b"] v5["x"] v6["0:"] v0 --- v1 v5 --- v6 v3 --- v6 v3 --- v4 v4 --- v5 v2 --- v5 v2 --- v4 v2 --- v6 v0 --- v3
```

*Figure 7.4(a) shows a directed graph representing a network of pipelines along which oil can*

be sent. The goal is to ship as much oil as possible from the *source* $s$ to the *sink* $t$. Each

pipelinehasamaximum*capacity* itcanhandle,andthere arenoopportunities for storingoil

212

Algorithms

```mermaid
flowchart TD %% Figure 7.4 (a)Anetwork withedge capacities. (b) A owinthe network. n0[" "] n1[" "] n2[" "] n3[" "] n4[" "] n5[" "] n6[" "] n7[" "] n8[" "] n9[" "] n10[" "] n11[" "] n12[" "] n13[" "] n14[" "] n15[" "] n0 --> n1 n2 --> n3 n4 --> n3 n5 --> n6 n7 --> n1 n8 --> n9 n10 --> n11 n1 --> n12 n8 --> n13 n14 --> n15 n12 --> n11
```

*Figure 7.4 (a)Anetwork withedge capacities. (b) A owinthe network.*

(a)

(b)

2

2

a

a

d

d

2

2

3

2

0

1

1

10

0

s

s

t

t

b

b

1

1

1

3

1

4

4

5

5

c

c

e

e

5

5

enroute. Figure7.4(b)showsapossible *ow*from $s$to $t,$whichships$7$ unitsinall. Is thisthe

best thatcanbedone?

### 7.2.2 Maximizing ow

The networks we are dealing with consist of a directed graph $G$ $=$ $(V;E)$; two special nodes

$$s;t$$

$V,$ whichare, respectively, asource andsinkof $G$; and*capacities* $c_e$ $>0$ onthe edges.

$$2$$

We would like to send as much oil as possible from $s$ to $t$ without exceeding the capacities

of anyof theedges. Aparticularshippingscheme iscalleda *ow*andconsists of avariable$f_e$

for each edge $e$ of thenetwork, satisfyingthefollowingtwo properties:

1. It doesn't violateedge capacities: $0$

$$f_e$$

$c_e$ for all$e$

$E$.

$$2$$

2. For all nodes $u$ except $s$ and $t,$ the amountof ow entering $u$ equals the amountleaving

$u$:

$$f_{wu} =$$

$$f_{uz}:$$

$$X^{(w;u)}$$

$$E$$

$$X^{(u;z)}$$

$$E$$

$$2$$

$$2$$

Inother words, owis*conserved*.

The *size* of a ow is the total quantity sent from $s$ to $t$ and, by the conservation principle,

isequalto the quantityleaving$s$:

size$(f)$ $=$

$$f_{su}:$$

$$X^{(s;u)}$$

$$E$$

$$2$$

$$f_e : e$$

$$E$$

In short, our goal is to assign values to

that will satisfy a set of linear

$$f$$

$$2$$

$$g$$

constraints and maximize a linear objective function. But this is a linear program! *The*

*maximum-* *owproblem* *reduces* *tolinear* *programming*.

For example, for the network of Figure7.4the LPhas11variables,one per edge. It seeks

to maximize $f_{sa}$ $+f_{sb}$ $+f_{sc}$ subject to a total of 27 constraints: 11 for nonnegativity (such as

$$f_{sa}$$

$0),$ 11 for capacity (such as $f_{sa}$

$3),$ and 5 for ow conservation (one for each node of

the graph other than $s$ and $t,$ such as $f_{sc}$ $+f_{dc}$ $=$ $f_{ce})$. Simplex would take no time at all to

correctly solve the problem andto con rm that,inour example, a owof 7isinfact optimal.

S.Dasgupta,C.H.Papadimitriou,andU.V.Vazirani

213

```mermaid
flowchart TD fig["Figure 7.5 An illustration of the maxow algorithm. (a) A toy network. (b) The rst path"]
```

*Figure 7.5 An illustration of the max- ow algorithm. (a) A toy network. (b) The rst path*

chosen. (c)Thesecondpathchosen. (d)The nal ow. (e)Wecouldhavechosenthispath rst.

(f) Inwhichcase, wewouldhaveto allowthissecond path.

(a)

(b)

a

a

1

1

1

s

s

t

t

1

1

b

(c)

(d)

a

1

1

0

s

s

t

t

1

1

b

b

(e)

(f)

a

a

1

1

1

s

s

t

t

1

1

1

b

b

### 7.2.3 A closer look at the algorithm

All we know so far of the simplex algorithm is the vague geometric intuition that it keeps

making local moves on the surface of a convex feasible region, successively improving the

objective function until it nally reaches the optimal solution. Once we have studied it in

more detail (Section 7.6), we will be in a position to understand exactly how it handles ow

LPs,whichisusefulasasource of inspirationfor designing*direct* maxowalgorithms.

It turnsout thatinfact the behaviorof simplexhasanelementary interpretation:

Start withzero ow.

Repeat: choose an appropriate path from $s$ to $t,$ and increase ow along the edges

of thispathasmuchaspossible.

```mermaid
flowchart TD fig["Figure 7.5(a) (d) shows a small example in which simplex halts after two iterations. The"]
```

*Figure 7.5(a) (d) shows a small example in which simplex halts after two iterations. The*

nal owhassize$2,$ whichiseasilyseen to beoptimal.

214

Algorithms

Thereisjustonecomplication. Whatifwehadinitiallychosenadifferent path,theonein

Figure7.5(e)? Thisgivesonlyoneunitof owandyetseemstoblockallother paths. Simplex

gets around this problem by also allowing paths to *cancel* *existing* *ow*. In this particular

case, it would subsequently choose the path of Figure 7.5(f). Edge $(b;a)$ of this path isn't in

the originalnetwork andhastheeffect of canceling owpreviouslyassignedto edge $(a;b)$.

To summarize, in each iteration simplex looks for an $s$

$t$ path whose edges $(u;v)$ can be

of two types:

1. $(u;v)$ isinthe originalnetwork, andisnot yetat fullcapacity.

2. Thereverse edge $(v;u)$ isintheoriginalnetwork, andthere issome owalongit.

If the current owis$f,$ theninthe rst case, edge $(u;v)$ canhandleupto $c_{uv}$

$f_{uv}$ additional

units of ow, and in the second case, upto $f_{vu}$ additional units (canceling all or part of the

existing ow on $(v;u))$. These ow-increasing opportunities can be captured in a *residual*

*network*$G^f$ $=(V;E^f),$whichhasexactlythetwotypesofedgeslisted,withresidualcapacities

$c^f$:

$$c_{uv}$$

$$f_{uv}$$

if$(u;v)$

$E$ and$f_{uv}$ $<c_{uv}$

$$2$$

$$f_{vu}$$

if$(v;u)$

$E$ and$f_{vu}$ $>0$

$$2$$

Thuswe canequivalentlythinkof simplexaschoosingan$s$

$t$pathintheresidualnetwork.

By simulating the behavior of simplex, we get a direct algorithm for solving maxow. It

proceeds in iterations, each time explicitly constructing $G^f,$ nding a suitable $s$

$t$ path in

$G^f$ byusing,say,alinear-timebreadthrst search, andhaltingifthere isnolongeranysuch

pathalongwhich owcanbe increased.

Figure7.6illustratesthealgorithmonour oilexample.

### 7.2.4 A certi cate of optimality

Now for a truly remarkable fact: not only does simplex correctly compute a maximum ow,

butitalsogenerates ashort proof of the optimalityof this ow!

Let'sseeanexampleofwhatthismeans. Partitionthenodesoftheoilnetwork(Figure7.4)

intotwo groups, $L=$

$$s;a;b$$

and$R$ $=$

$$c;d;e;t$$

:

$$f$$

$$g$$

$$f$$

$$g$$

L

R

2

a

d

2

3

1

10

s

t

b

1

1

3

4

5

c

e

5

Any oil transmitted must pass from $L$ to $R$. Therefore, no ow can possibly exceed the total

capacity of the edges from $L$ to $R,$ which is 7. But this means that the ow we found earlier,

of size7,mustbe optimal!

S.Dasgupta,C.H.Papadimitriou,andU.V.Vazirani

215

More generally, an $(s;t)-$*cut* partitions the vertices into two disjoint groups $L$ and $R$ such

that $s$ is in $L$ and $t$ is in $R$. Its *capacity* is the total capacity of the edges from $L$ to $R,$ and as

arguedpreviously,isanupper boundon *any* ow:

Pickany ow$f$ andany$(s;t)-$cut $(L;R)$. Thensize$(f)$

capacity$(L;R)$.

Some cuts are large and give loose upper bounds cut $($

$$s;b;c$$

$$;$$

$$a;d;e;t$$

$)$ has a capacity of

$$f$$

$$g$$

$$f$$

$$g$$

19. But there is also a cut of capacity 7, which is effectively a *certi* *cate* *of* *optimality* of the

maximum ow. Thisisn'tjustaluckyproperty of our oilnetwork; suchacut *always* exists.

**Max-** **owmin-cuttheorem** Thesizeofthemaximum owinanetworkequalsthecapacity

ofthesmallest$(s;t)-$cut.

Moreover, ouralgorithmautomatically ndsthiscutasaby-product!

Let's see why this is true. Suppose $f$ is the nal ow when the algorithm terminates. We

knowthatnode$t$isnolongerreachablefrom$s$intheresidualnetwork$G^f$. Let$L$bethenodes

that *are* reachable from $s$ in $G^f,$ and let $R$ $=$ $V$

$L$ be the rest of the nodes. Then $(L;R)$ is a

cut inthe graph$G$:

$$R$$

$$L$$

$$e$$

$$s$$

$$t$$

$$e^0$$

We claimthat

size$(f)$ $=$ capacity$(L;R):$

To see this, observe that by the way $L$ is de ned, any edge going from $L$ to $R$ must be at full

capacity (in the current ow $f),$ and any edge from $R$ to $L$ must have zero ow. (So, in the

gure, $f_e$ $=$ $c_e$ and $f_e0$ $=$ $0$.) Therefore the net ow across $(L;R)$ is exactly the capacity of the

cut.

### 7.2.5 Ef ciency

Each iteration of our maximumow algorithm is ef cient, requiring $O($

$$E$$

$)$ time if a depth-

$$j$$

$$j$$

rst or breadthrst search isusedto ndan$s$

$t$path. Buthowmanyiterations arethere?

$C$. Then an inductive

Suppose all edges in the original network have *integer* capacities

argument shows that on each iteration of the algorithm, the ow is always an integer and

increases by an integer amount. Therefore, since the maximum ow is at most $C$

$$E$$

(why?),

$$j$$

$$j$$

it follows that the number of iterations is at most this much. But this is hardly a reassuring

bound: whatif$C$ isinthemillions?

We examine this issue further in Exercise 7.31. It turns out that it is indeed possible to

construct bad examples in which the number of iterations is proportional to $C,$ *if* $s$

$t$ paths

arenotcarefullychosen. However,ifpathsarechoseninasensiblemanner inparticular,by

216

Algorithms

usingabreadthrstsearch, which ndsthepathwiththefewest edges then thenumberof

iterations is at most $O($

$$V$$

$$E$$

$),$ no matter what the capacities are. This latter bound gives

$$j$$

$$j j$$

$$j$$

$^2)$ for maximum ow.

anoverall runningtimeof $O($

$$V$$

$$E$$

$$j$$

$$j j$$

$$j$$

S.Dasgupta,C.H.Papadimitriou,andU.V.Vazirani

217

```mermaid
flowchart TD %% Figure 7.6 The maxow algorithm applied to the network of Figure 7.4. At each iteration, n0[" "] n1[" "] n2[" "] n3[" "] n4[" "] n5[" "] n6[" "] n7[" "] n8[" "] n9[" "] n10[" "] n11[" "] n12[" "] n13[" "] n14[" "] n15[" "] n16[" "] n0 --> n1 n2 --> n3 n4 --> n3 n5 --> n6 n7 --> n8 n9 --> n10 n8 --> n11 n8 --> n12 n9 --> n12 n13 --> n14 n15 --> n16
```

*Figure 7.6 The max- ow algorithm applied to the network of Figure 7.4. At each iteration,*

thecurrent owisshownontheleftandtheresidualnetworkontheright. Thepathschosen

are showninbold.

Current ow

Residualgraph

(a)

2

a

a

d

d

2

3

1

10

s

s

t

t

b

b

1

1

3

4

5

c

c

e

e

5

(b)

1

1

a

d

a

d

1

1

2

1

1

10

2

s

t

b

s

t

1

b

1

3

1

1

4

1

4

1

c

e

c

e

1

4

(c)

2

2

a

d

a

d

2

2

2

1

10

1

s

t

b

s

1

t

1

b

1

3

1

2

4

3

2

1

c

e

c

e

1

4

(d)

2

2

a

a

d

d

2

2

2

1

10

1

s

s

1

t

t

b

b

1

1

3

1

1

3

5

5

3

4

c

c

e

e

4

1

## 218

## Algorithms

## Figure 7.6 Continued

## Current Flow

## ResidualGraph

## (e)

2

2

## a

## a

## d

## d

1

1

2

2

1

10

1

1

## s

## s

## t

## t

## b

## b

1

1

3

1

5

4

4

5

## c

## c

## e

## e

5

5

## (f)

2

2

## a

## a

## d

## d

2

2

2

2

1

1

1

10

1

1

## s

## s

## t

## t

## b

## b

1

1

1

2

5

4

4

5

## c

## c

## e

## e

5

5

S.Dasgupta,C.H.Papadimitriou,andU.V.Vazirani

219

```mermaid
flowchart TD %% Figure 7.7 An edge between two people means they like each other. Is it possible to pair n0[" "] n1[" "] n2[" "] n3[" "] n4[" "] n5[" "] n6[" "] n7[" "] n0 --> n1 n0 --> n2 n0 --> n3 n4 --> n3 n5 --> n1 n0 --> n6 n7 --> n3 n4 --> n6
```

*Figure 7.7 An edge between two people means they like each other. Is it possible to pair*

everyone uphappily?

BOYS

GIRLS

Alice

Al

Beatrice

Bob

Carol

Chet

Danielle

Dan

## 7.3 Bipartite matching

Figure7.7showsagraphwithfour nodes on the left representing boys andfour nodes on the

right representing girls.1 There is an edge between a boy and girl if they like each other (for

instance,Allikesallthegirls). Isitpossibletochoosecouplessothateveryonehasexactlyone

partner, anditissomeone theylike? Ingraph-theoretic jargon,isthere a*perfect* *matching*?

This matchmaking game can be reduced to the maximumow problem, and thereby to

linear programming! Create a new source node, $s,$ with outgoing edges to all the boys; a new

sink node, $t,$ with incoming edges from all the girls; and direct all the edges in the original

bipartite graph from boy to girl (Figure 7.8). Finally, give every edge a capacity of $1$. Then

thereisaperfectmatchingifandonlyifthisnetworkhasa owwhosesizeequalsthenumber

of couples. Canyou ndsucha owinthe example?

Actually,thesituationisslightlymore complicated thanjuststated: whatiseasyto see is

that the optimum *integer-valued* ow corresponds to the optimum matching. We would be at

a bit of a loss interpreting a ow that ships $0:7$ units along the edge Al Carol, for instance!

1Thiskind of graph, inwhich the nodes canbe partitioned into two groups such that alledges are *between* the

groups,iscalled*bipartite*.

```mermaid
flowchart TD fig["Figure 7.8 Amatchmakingnetwork. Eachedge hasacapacityof one."]
```

*Figure 7.8 Amatchmakingnetwork. Eachedge hasacapacityof one.*

Alice

Al

Bob

Beatrice

s

t

Carol

Chet

Dan

Danielle

220

Algorithms

Fortunately, the maximumowproblem has the following property: *if* *all* *edge* *capacities* *are*

*integers,* *then* *the* *optimal* *ow* *found* *by* *our* *algorithm* *is* *integral*. We can see this directly

from the algorithm, which in such cases would increment the ow by an integer amount on

each iteration.

Hence integralitycomes for free inthe maximumowproblem. Unfortunately, thisis the

exception rather than the rule: as we will see in Chapter 8, it is a very dif cult problem to

ndthe optimumsolution(or for thatmatter, *any* solution)of agenerallinearprogram, ifwe

alsodemandthatthe variablesbeintegers.

## 7.4 Duality

Wehaveseenthatinnetworks, owsaresmallerthancuts,butthemaximum owandmini-

mumcutexactlycoincideandeachistherefore acerti cateoftheother'soptimality. Remark-

ableasthisphenomenonis,wenowgeneralizeitfrommaximum owto*any*problemthatcan

be solved by linear programming! It turns out that every linearmaximizationproblem hasa

*dual*minimizationproblem, andtheyrelatetoeachother inmuchthesamewayas owsand

cuts.

To understand what duality is about, recall our introductory LP with the two types of

chocolate:

$$max x_1+6x_2$$

$$x_1$$

$$200$$

$$x_2$$

$$300$$

$$x_1+x_2$$

$$400$$

$$x_1;x_2$$

$$0$$

Simplex declares the optimum solution to be $(x_1;x_2)$ $=$ $(100;300),$ with objective value $1900$.

Canthisanswerbecheckedsomehow? Let'ssee: supposewetakethe rstinequalityandadd

itto sixtimes thesecond inequality. Weget

$$x_1+6x_2$$

$$2000:$$

This is interesting, because it tells us that it is impossible to achieve a pro t of more than

$2000$. CanweaddtogethersomeothercombinationoftheLPconstraintsandbringthisupper

bound even closer to $1900$? After a little experimentation, we nd that multiplyingthe three

inequalitiesby$0,$ $5,$ and$1,$ respectively, andaddingthem upyields

$$x_1+6x_2$$

$$1900:$$

So$1900$mustindeedbethebestpossiblevalue! Themultipliers$(0;5;1)$ magicallyconstitutea

*certi* *cate* *of* *optimality*! It is remarkable that such a certi cate exists for this LP and even

ifwe knewthere were one, howwouldwe systematicallygo about ndingit?

S.Dasgupta,C.H.Papadimitriou,andU.V.Vazirani

221

Let's investigate the issue by describing what we expect of these three multipliers, call

them$y_1;y_2;y_3$.

Multiplier

Inequality

$$y_1$$

$$x_1$$

$$200$$

$$y_2$$

$$x_2$$

$$300$$

$$y_3$$

$$x_1 + x_2$$

$$400$$

To start with, these $y_i$'s must be nonnegative, for otherwise they are unquali ed to multiply

inequalities(multiplyinganinequalitybyanegativenumberwould ipthe

to

). Afterthe

multiplicationandadditionsteps, we get thebound:

$$(y_1+y_3)x_1+(y_2+y_3)x_2$$

$$200y_1+300y_2 +400y_3:$$

We want the left-hand side to look like our objective function $x_1$ $+6x_2$ so that the right-hand

sideisanupperboundontheoptimumsolution. Forthisweneed$y_1+y_3$ tobe$1$and$y_2+y_3$ to

be$6$. Cometothinkofit,itwouldbe neif$y_1+y_3$ werelargerthan$1$ theresultingcerti cate

wouldbeallthe more convincing. Thus,we get anupper bound

$$y_1;y_2;y_3$$

$$0$$

$$x_1+6x_2$$

$$200y_1+300y_2 +400y_3$$

$$y_1+y_3$$

$$1$$

$$:$$

if

$$8$$

$$9$$

$$y_2+y_3$$

$$6$$

$$<$$

$$=$$

We can easily nd $y$'s that satisfy the inequalities on the right by simply making them large

$$:$$

$$;$$

enough, for example $(y_1;y_2;y_3)$ $=$ $(5;3;6)$. But these particular multipliers would tell us that

the optimum solution of the LP is at most $200$

$$5+300$$

$$3+400$$

$6$ $=$ $4300,$ a boundthat is far

too loose to be of interest. What we want is a bound that is as tight as possible, so we should

minimize$200y_1+300y_2$ $+400y_3$ subject to the preceding inequalities. *Andthisis* *a* *newlinear*

*program*!

Therefore, nding the set of multipliers that gives the best upper bound on our original

LPistantamountto solvinganewLP:

$$min 200y_1 +300y_2+400y_3$$

$$y_1+y_3$$

$$1$$

$$y_2+y_3$$

$$6$$

$$y_1;y_2;y_3$$

$$0$$

Bydesign,anyfeasiblevalueofthis*dual*LPisanupperboundontheoriginal*primal*LP.So

if we somehow nd a pair of primal and dual feasible values that are equal, then they must

bothbeoptimal. Here isjustsuchapair:

Primal$:$ $(x_1;x_2)$ $=(100;300);$ Dual$:$ $(y_1;y_2;y_3)=(0;5;1):$

Theybothhavevalue$1900,$ andtherefore theycertify eachother's optimality(Figure7.9).

Amazingly,thisisnotjust aluckyexample,butageneralphenomenon. To start with,the

precedingconstruction creatingamultiplierforeachprimalconstraint;writingaconstraint

222

Algorithms

```mermaid
flowchart TD %% Figure 7.9 By design, dual feasible values n0[" "] n1[" "] n0 --> n1
```

*Figure 7.9 By design, dual feasible values*

primal feasible values. The duality theorem

tellsusthatmoreover their optimacoincide.

Dual

Primal

opt

Primal feasible

opt

Dual feasible

Objective

value

This duality gap is zero

```mermaid
flowchart TD %% Figure 7.10 Ageneric primalLPinmatrix-vector form, andits dual. v0["222"] v1["Algorithms"] v2["Primal"] v3["Dual"] v4["opt"] v5["opt"] v6["Objective"] v7["value"] v3 --- v4 v4 --- v5 v2 --- v3 v2 --- v5
```

*Figure 7.10 Ageneric primalLPinmatrix-vector form, andits dual.*

PrimalLP:

DualLP:

$$max c^Tx$$

$$min y^Tb$$

$$y^TA$$

$$c^T$$

$$Ax$$

$$b$$

$$x$$

$$0$$

$$y$$

$$0$$

in the dual for every variable of the primal, in which the sum is required to be above the

objective coef cient of thecorresponding primalvariable;andoptimizingthe sumof the mul-

tipliers weighted by the primal right-hand sides can be carried out for any LP, as shown in

Figure7.10,andinevengreatergeneralityinFigure7.11. Thesecond gurehasonenotewor-

thy addition: if the primal has an equality constraint, then the corresponding multiplier (or

*dual* *variable*) need not be nonnegative, because the validity of equations is preserved when

multiplied by negative numbers. So, the multipliers of equations are unrestricted variables.

Notice also the simple symmetry between the two LPs, in that the matrix $A$ $=$ $(a_{ij})$ de nes

oneprimalconstraintwitheachof its*rows*, andonedualconstraintwitheach ofits*columns*.

Byconstruction,anyfeasiblesolutionofthedualisanupperboundonanyfeasiblesolution

of the primal. Butmoreover, theiroptima coincide!

**Dualitytheorem** Ifalinearprogramhasaboundedoptimum,thensodoesitsdual,andthe

twooptimumvaluescoincide.

When the primal is the LP that expresses the maxow problem, it is possible to assign

interpretations to the dualvariablesthat showthe dualto be noneother thanthe minimum-

cut problem (Exercise 7.25). The relation between ows and cuts is therefore just a speci c

instanceof thedualitytheorem. Andinfact, the proof of thistheorem fallsoutof thesimplex

algorithm, in much the same way as the maxow min-cut theorem fell out of the analysisof

the maxowalgorithm.

S.Dasgupta,C.H.Papadimitriou,andU.V.Vazirani

223

```mermaid
flowchart TD fig["Figure 7.11 In the most general case of linear programming, we have a set I of inequalities"]
```

*Figure 7.11 In the most general case of linear programming, we have a set I of inequalities*

and a set $E$ of equalities (a total of $m$ $=$

$$I$$

$$+$$

$$E$$

constraints) over $n$ variables, of which a

$$j$$

$$j$$

$$j$$

$$j$$

subset $N$ are constrained to be nonnegative. The dual has $m$ $=$

$$I$$

$$+$$

$$E$$

variables, of which

$$j$$

$$j$$

$$j$$

$$j$$

onlythose corresponding to $I$ havenonnegativityconstraints.

PrimalLP:

DualLP:

$$max c_1x_1+$$

$$+c_nx_n$$

$$min b_1y_1+$$

$$+b_my_m$$

$$a_{i1}x_1+$$

$$+a_{in}x_n$$

$$b_i$$

for $i$

$$I$$

$$a_{1j}y_1+$$

$$+a_{mj}y_m$$

$$c_j$$

for $j$

$$N$$

$$2$$

$$2$$

$$a_{i1}x_1+$$

$$+a_{in}x_n =b_i$$

for $i$

$$E$$

$$a_{1j}y_1+$$

$$+a_{mj}y_m =c_j$$

for $j$

$$N$$

$$2$$

$$62$$

$$x_j$$

$0$ for $j$

$$N$$

$$y_i$$

$0$ for $i$

$$I$$

$$2$$

$$2$$

**Visualizing** **duality**

Onecansolvetheshortest-path problembythefollowing analog device: Givenaweighted

undirected graph, builda *physical* *model* of it inwhicheach edge is a string of lengthequal

to the edge's weight, and each node is a knot at which the appropriate endpoints of strings

aretied together. Thento ndtheshortest pathfrom $s$to $t,$just*pull* $s$awayfrom $t$untilthe

gadgetistaut. Itisintuitivelyclear thatthis ndstheshortest pathfrom $s$to $t$.

A

B

S

T

D

C

There is nothing remarkable or surprising about all this until we notice the following:

the shortest-path problem is a *minimization* problem, right? Then why are we *pulling* $s$

away from $t,$ an act whose purpose is, obviously, *maximization?* Answer: By pulling $s$ away

from $t$ we solve *the* *dual* of the shortest-path problem! This dual has a very simple form

(Exercise 7.28),withonevariable$x_u$ for eachnode $u$:

$$max x_S$$

$$x_T$$

$$x_u$$

$$xvj$$

$$w_{uv}$$

$$u;v$$

for alledges

$$j$$

$$f$$

$$g$$

In words, the dual problem is to stretch $s$ and $t$ as far apart as possible, subject to the

$$u;v$$

are separated byadistanceof atmost $w_{uv}$.

constraintthat theendpoints of anyedge

$$f$$

$$g$$

224

Algorithms

## 7.5 Zero-sumgames

We canrepresent variouscon ictsituationsinlifeby*matrix* *games*. For example, the school-

yard*rock-paper-scissors* gameisspeci edbythe*payoffmatrix*illustratedhere. Therearetwo

$$r;p;s$$

players, called Row and Column, and they each pick a move from

. They then look up

$$f$$

$$g$$

thematrixentrycorrespondingtotheirmoves,andColumnpaysRowthisamount. ItisRow's

gainandColumn'sloss.

Column

$$r$$

$$p$$

$$s$$

$$G =$$

$$r$$

$$0$$

$$1$$

$$1$$

w

$$p$$

$$1$$

$$0$$

$$1$$

o

$$s$$

$$1$$

$$1$$

$$0$$

R

Now suppose the two of them play this game repeatedly. If Row always makes the same

move, Column will quickly catch on and will always play the countermove, winning every

time. Therefore Row should mix things up: we can model this by allowing Row to have a

*mixed* *strategy*, in which on each turn she plays $r$ with probability $x_1,$ $p$ with probability $x_2,$

and $s$ with probability $x_3$. This strategy is speci ed by the vector $x$ $=$ $(x_1;x_2;x_3),$ positive

numbersthataddupto $1$. Similarly,Column'smixedstrategy issome $y$ $=(y_1;y_2;y_3)$.2

On any given round of the game, there is an $x_iy_j$ chance that Row and Column will play

the $i$thand$j$thmoves, respectively. Therefore the *expected* (average) payoff is

$$G_{ij}$$

Prob[Rowplays$i,$ Columnplays$j]$ $=$

$$G_{ij}x_iy_j:$$

$$X^{i;j}$$

$$X^{i;j}$$

Rowwantsto*maximize*this,whileColumnwantsto*minimize*it. Whatpayoffscantheyhope

to achieve in rock-paper-scissors? Well, suppose for instance that Row plays the completely

random strategy $x$ $=$ $(1=3;1=3;1=3)$. If Columnplays $r,$ then the average payoff (reading the

rst columnof the gamematrix)willbe

$$1$$

$$1$$

$$1$$

$$0+$$

$$1+$$

$$1 = 0:$$

$$3$$

$$3$$

$$3$$

ThisisalsotrueifColumnplays$p,$or$s$. Andsincethepayoffofanymixedstrategy$(y_1;y_2;y_3)$

isjustaweightedaverageoftheindividualpayoffsforplaying$r,p,$and$s,$itmustalsobezero.

Thiscanbeseen directly from the preceding formula,

$$1$$

$$1$$

$$y_j =$$

$$y_j$$

$$G_{ij}$$

$$=$$

$$y_j$$

$$0 = 0;$$

$$G_{ij}x_iy_j =$$

$$G_{ij}$$

$$3$$

$$3$$

$$!$$

$$X^j$$

$$X^i$$

$$X^j$$

$$X^{i;j}$$

$$X^{i;j}$$

where the second-to-last equality is the observation that every column of $G$ adds up to zero.

Thus by playing the completely random strategy, Row forces an expected payoff of zero, *no*

*matter* *what* *Column* *does*. This means that Column cannot hope for a negative (expected)

2Also of interest are scenarios in which players alter their strategies from round to round, but these can get

very complicatedandare avastsubject untothemselves.

S.Dasgupta,C.H.Papadimitriou,andU.V.Vazirani

225

payoff (remember that he wants the payoff to be as small as possible). But symmetrically,

if Column plays the completely random strategy, he also forces an expected payoff of zero,

and thus Row cannot hope for a positive (expected) payoff. In short, the best each player can

do is to play completely randomly, with an expected payoff of zero. We have mathematically

con rmed whatyou knewallalongaboutrock-paper-scissors!

Let'sthinkaboutthisinaslightlydifferent way,byconsidering two scenarios:

1. First Rowannouncesher strategy, andthen Columnpicks his.

2. First Columnannounceshisstrategy, andthenRowchooses hers.

We've seen that the average payoff is the same (zero) in either case if both parties play op-

timally. But this might well be due to the high level of symmetry in rock-paper-scissors. In

general games, we'd expect the rst option to favor Column, since he knows Row's strategy

and can fully exploit it while choosing his own. Likewise, we'd expect the second option to

favorRow. Amazingly,thisisnotthecase: ifbothplayoptimally,thenitdoesn'thurtaplayer

to announce his or her strategy in advance! What's more, this remarkable property is a con-

sequence of andinfact equivalentto linearprogrammingduality.

Let'sinvestigatethiswithanonsymmetric game. Imaginea*presidential* *election* scenario

inwhichtherearetwocandidatesforof ce,andthemovestheymakecorrespondtocampaign

issues on which they can focus (the initialsstand for *economy*, *society*, *morality*, and*tax* *cut*).

Thepayoff entries are millionsof votes lost byColumn.

$$m$$

$$t$$

$$G =$$

$$e$$

$$3$$

$$1$$

$$s$$

$$2$$

$$1$$

Suppose Row announces that she will play the mixed strategy $x$ $=$ $(1=2;1=2)$. What should

Columndo? Move$m$willincuranexpected lossof$1=2,$ while$t$willincuranexpected lossof$0$.

Thebest response of Columnistherefore the *pure* strategy $y$ $=(0;1)$.

More generally, once Row's strategy $x$ $=$ $(x_1;x_2)$ is xed, there is always a *pure* strategy

that is optimal for Column: either move $m,$ with payoff $3x_1$

$2x_2,$ or $t,$ with payoff

$x_1$ $+x_2,$

whichever is smaller. After all,anymixed strategy $y$ is a weighted average of these two pure

strategies andthuscannotbeatthe better of thetwo.

Therefore, if Row is forced to announce $x$ before Column plays, she knows that his best

. She should choose $x$

response will achieve an expected payoff of $min$

$$3x_1$$

$$2x_2;$$

$$x1 + x2g$$

$$f$$

*defensively* to maximizeher payoff againstthisbest response:

Pick$(x_1;x_2)$thatmaximizes

$$min$$

$$3x_1$$

$$2x_2;$$

$$x1+x2g$$

$$f$$

payofffromColumn'sbestresponseto$x$

$$|$$

$${z$$

$$}$$

This choice of $x_i$'s gives Row the best possible *guarantee* about her expected payoff. And we

willnowsee thatitcanbefoundbyanLP!Themaintrick isto notice thatfor *xed* $x_1$ and$x_2$

the followingare equivalent:

226

Algorithms

$$max z$$

$$z =min$$

$$3x_1$$

$$2x_2;$$

$$x1+x2g$$

$$z$$

$$3x_1$$

$$2x_2$$

$$f$$

$$z$$

$$x_1+x_2$$

AndRowneeds to choose $x_1$ and$x_2$ to maximizethis$z$.

$$max$$

$$z$$

$$3x_1 + 2x_2 + z$$

$$0$$

$$x_1$$

$$x_2 + z$$

$$0$$

$$x_1 + x_2$$

$$= 1$$

$$x_1;x_2$$

$$0$$

Symmetrically, if Column has to announce his strategy rst, his best bet is to choose the

mixedstrategy $y$ thatminimizeshisloss underRow'sbestresponse, inother words,

Pick$(y_1;y_2)$ thatminimizes

$$max$$

$$3y_1$$

$$y_2;$$

$$2y1+y2g$$

$$f$$

outcomeofRow'sbest responseto$y$

$${z$$

$$}$$

$$|$$

InLPform, thisis

$$min w$$

$$3y_1 + y_2 + w$$

$$0$$

$$2y_1$$

$$y_2 + w$$

$$0$$

$$y_1 + y_2$$

$$= 1$$

$$y_1;y_2$$

$$0$$

The crucial observation now is that *these* *two* *LPs* *are* *dual* *to* *each* *other* (see Figure 7.11)!

Hence, they havethesameoptimum, callit $V$.

Let us summarize. By solving an LP, Row (the maximizer) can determine a strategy for

herself thatguarantees anexpected outcome of atleast $V$ no matter whatColumndoes. And

bysolvingthedualLP,Column(theminimizer)canguaranteeanexpectedoutcomeofatmost

$V,$nomatterwhatRowdoes. Itfollowsthatthisistheuniquelyde nedoptimalplay: apriori

it wasn't even certain that such a play existed. $V$ is known as the *value* of the game. In our

example, it is $1=7$ andis realized whenRow plays her optimum mixed strategy $(3=7;4=7)$ and

Columnplayshisoptimummixedstrategy $(2=7;5=7)$.

This example is easily generalized to arbitrary games and shows the existence of mixed

strategiesthatareoptimalforbothplayersandachievethesamevalue afundamentalresult

of gametheory calledthe *min-max* *theorem*. It canbe writteninequationform asfollows:

$$G_{ij}x_iy_j = min$$

$$max$$

$$G_{ij}x_iy_j:$$

$$max$$

$$min$$

$$y$$

$$x$$

$$x$$

$$y$$

$$X^{i;j}$$

$$X^{i;j}$$

This is surprising, because the left-hand side, in which Row has to announce her strategy

rst,shouldpresumablybebetter forColumnthantheright-handside,inwhichhehasto go

rst. Dualityequalizesthe two, asit didwithmaximum owsandminimumcuts.

S.Dasgupta,C.H.Papadimitriou,andU.V.Vazirani

227

```mermaid
flowchart TD fig["Figure 7.12 Apolyhedron de nedbyseven inequalities."]
```

*Figure 7.12 Apolyhedron de nedbyseven inequalities.*

$$x_2$$

$$max x_1+6x_2+13x_3$$

$$A$$

2

$$x_1$$

$$200$$

1

7

$$x_2$$

$$300$$

$$C$$

2

$$B$$

$$x_1+x_2+x_3$$

$$400$$

3

3

$$x_2+3x_3$$

$$600$$

4

1

$$x_1$$

$$0$$

5

$$x_1$$

5

$$x_2$$

$$0$$

6

$$x_3$$

$$0$$

7

6

4

$$x_3$$

## 7.6 The simplex algorithm

The extraordinary power andexpressiveness of linearprograms wouldbe little consolation if

wedid nothaveawayto solve themef ciently. Thisisthe role of the simplexalgorithm.

Atahighlevel,thesimplexalgorithmtakes aset of linearinequalitiesandalinearobjec-

tive functionand ndstheoptimalfeasiblepoint bythe followingstrategy:

```text
let v be any vertex of the feasible region while there is a neighbor v0 of v with better objective value:
```

$$set v =v_0$$

Inour2Dand3Dexamples(Figure7.1andFigure7.2),thiswassimpletovisualizeandmade

intuitivesense. Butwhatifthere are$n$variables,$x_1;:::;x_n$?

Any setting of the $x_i$'s can be represented by an $n-$tuple of real numbers and plotted in

$n-$dimensional space. A linear equation involving the $x_i$'s de nes a *hyperplane* in this same

space $R^n,$ and the corresponding linear inequality de nes a *half-space*, all points that are

eitherpreciselyonthehyperplaneorlieononeparticularsideofit. Finally,thefeasibleregion

of the linear program is speci ed by a set of inequalities and is therefore the intersection of

the corresponding half-spaces, aconvex polyhedron.

Butwhatdo the concepts of *vertex* and*neighbor*meaninthisgeneralcontext?

### 7.6.1 Vertices and neighbors in n-dimensional space

```mermaid
flowchart TD fig["Figure 7.12 recalls an earlier example. Looking at it closely, we see that each vertex is the"]
```

*Figure 7.12 recalls an earlier example. Looking at it closely, we see that each vertex is the*

*unique* *point* *at* *which* *some* *subset* *of* *hyperplanes* *meet*. Vertex $A,$ for instance, is the sole

point at which constraints 2

, 3

, and 7

are satis ed with equality. On the other hand, the

228

Algorithms

hyperplanes corresponding to inequalities 4

and 6

do not de ne a vertex, because their

intersection isnotjustasinglepointbutanentire line.

Let'smakethisde nitionprecise.

Pickasubsetoftheinequalities. Ifthereisauniquepointthatsatis esthemwith

equality,andthispoint happensto befeasible, thenitisa*vertex*.

Howmanyequationsareneededtouniquelyidentifyapoint? Whenthereare$n$variables,we

needatleast$n$linearequationsifwewantauniquesolution. Ontheotherhand,havingmore

than$n$ equationsis redundant: at least one of them can be rewritten as a linearcombination

of the others andcantherefore be disregarded. Inshort,

Eachvertex isspeci ed byaset of $n$inequalities.3

Anotionof *neighbor*nowfollows naturally.

Twovertices are *neighbors*if theyhave$n$

$1$ de ninginequalitiesincommon.

InFigure7.12,for instance, vertices $A$and$C$ share thetwo de ninginequalities

$;$ 7

and

3

$$f$$

$$g$$

are thusneighbors.

### 7.6.2 The algorithm

Oneachiteration, simplexhastwo tasks:

1. Check whether thecurrent vertex isoptimal(andifso, halt).

2. Determine where to move next.

Aswewillsee, bothtasks areeasyifthe vertex happensto be attheorigin. Andifthe vertex

iselsewhere, we willtransform thecoordinate system to move itto the origin!

First let'ssee whythe originissoconvenient. Suppose wehavesome generic LP

$$max c^Tx$$

$$Ax$$

$$b$$

$$x$$

$$0$$

where $x$ is the vector of variables, $x$ $=$ $(x_1;:::;x_n)$. Suppose the origin is feasible. Then it is

certainlyavertex, sinceit isthe uniquepoint atwhichthe$n$inequalities

$$x_1$$

$$0;:::;x_n$$

$$0$$

$$f$$

$$g$$

are *tight*. Nowlet'ssolve our two tasks. Task1:

Theoriginisoptimalifandonlyifall$c_i$

$0$.

3There is one tricky issue here. It is possible that the same vertex might be generated by different subsets

of inequalities. In Figure 7.12, vertex $B$ is generated by $f$ 2$;$ 3$;$ 4$g,$ but also by $f$ 2$;$ 4$;$ 5$g$. Such vertices are

called *degenerate* and require special consideration. Let's assume for the time being that they don't exist, and

we'll returnto them later.

S.Dasgupta,C.H.Papadimitriou,andU.V.Vazirani

229

$0,$ thenconsidering the constraints$x$

If all$c_i$

$0,$ we can'thope for abetter objective value.

Conversely, if some $c_i$ $>$ $0,$ then the origin is not optimal, since we can increase the objective

functionbyraising$x_i$.

Thus, for task 2, we can move by increasing some $x_i$ for which $c_i$ $>$ $0$. How much can

we increase it? *Until* *we* *hit* *some* *other* *constraint*. That is, we release the tight constraint

$$x_i$$

$0$ and increase $x_i$ until some other inequality, previously loose, now becomes tight. At

thatpoint, weagainhaveexactly $n$tightinequalities,so weare atanewvertex.

For instance,suppose we'redealingwiththe followinglinearprogram.

$$max 2x_1+5x_2$$

$$2x_1$$

$$x_2$$

$$4$$

1

$$x_1+2x_2$$

$$9$$

2

$$x_1+x_2$$

$$3$$

3

$$x_1$$

$$0$$

4

$$x_2$$

$$0$$

5

Simplexcanbe started at the origin,whichis speci ed byconstraints 4

and 5

. Tomove, we

release the tight constraint $x_2$

$0$. As $x_2$ is gradually increased, the rst constraint it runs

$$x_1 +x_2$$

$3,$ and thus it has to stop at $x_2$ $=$ $3,$ at which point this new inequality is

into is

tight. Thenewvertex isthusgivenby 3

and 4

.

So we know what to do if we are at the origin. But what if our current vertex $u$ is else-

where? Thetrick isto transform $u$ intothe origin,byshiftingthe coordinate systemfrom the

usual$(x_1;:::;x_n)$ to the local view from $u$. These local coordinates consist of (appropriately

scaled) distances$y_1;:::;y_n$ to the $n$hyperplanes(inequalities)thatde neandenclose $u$:

$$u$$

$$y_2$$

$$y_1$$

$$x$$

Speci cally, if one of these enclosing inequalities is $a_i$

$$x$$

$b_i,$ then the distance from a point

$x$to thatparticular wall is

$$a_i$$

$$x:$$

$$y_i =b_i$$

The $n$ equations of this type, one per wall, de ne the $y_i$'s as linear functions of the $x_i$'s, and

this relationship can be inverted to express the $x_i$'s as a linear function of the $y_i$'s. Thus

we can rewrite the entire LP in terms of the $y$'s. This doesn't fundamentally change it (for

instance, the optimal value stays the same), but expresses it in a different coordinate frame.

Therevised local LPhasthefollowingthree properties:

230

Algorithms

1. It includes the inequalities $y$

$0,$ which are simply the transformed versions of the

inequalitiesde ning$u$.

2. $u$ itselfisthe originin$y-$space.

3. The cost function becomes $maxc_u$ $+~c^Ty,$ where $c_u$ is the value of the objective function

at$u$ and $~c$ isatransformed cost vector.

In short, we are back to the situation we know how to handle! Figure 7.13 shows this algo-

rithminaction, continuingwithour earlier example.

The simplex algorithm is now fully de ned. It moves from vertex to neighboring vertex,

stopping when the objective function is locally optimal, that is, when the coordinates of the

local cost vector are allzero or negative. As we've just seen, a vertex withthis property must

also be globally optimal. On the other hand, if the current vertex is not locally optimal, then

itslocalcoordinatesystemincludessomedimensionalongwhichtheobjectivefunctioncanbe

improved,sowemovealongthisdirection alongthisedgeofthepolyhedron untilwereach

aneighboringvertex. Bythenondegeneracyassumption(seefootnote 3inSection7.6.1),this

edge has nonzero length, and so we strictly improve the objective value. Thus the process

musteventuallyhalt.

S.Dasgupta,C.H.Papadimitriou,andU.V.Vazirani

231

```mermaid
flowchart TD fig["Figure 7.13 Simplexinaction."]
```

*Figure 7.13 Simplexinaction.*

$;$ 5

InitialLP:

(origin).

*Currentvertex:*

4

$$f$$

$$g$$

*Objectivevalue:* $0$.

$$max 2x_1+5x_2$$

*Move:* increase$x_2$.

$$2x_1$$

$$x_2$$

$$4$$

1

becomestight. Stopat$x_2$ $=3$.

isreleased, 3

5

$$x_1+2x_2$$

$$9$$

2

$$x_1+x_2$$

$$3$$

3

$;$ 3

haslocalcoordinates$(y_1;y_2)$:

Newvertex

4

$$f$$

$$g$$

$$x_1$$

$$0$$

4

$$y_1 = x_1;$$

$$y_2 = 3+x_1$$

$$x_2$$

$$x_2$$

$$0$$

5

$;$ 3

RewrittenLP:

.

*Currentvertex:*

4

$$f$$

$$g$$

*Objectivevalue:* $15$.

$$max 15+7y_1$$

$$5y_2$$

*Move:* increase$y_1$.

$$y_1+y_2$$

$$7$$

1

becomestight. Stopat$y_1$ $=1$.

isreleased, 2

4

$$3y_1$$

$$2y_2$$

$$3$$

2

$$y_2$$

$$0$$

3

$;$ 3

haslocalcoordinates$(z_1;z_2)$:

Newvertex

2

$$f$$

$$g$$

$$y_1$$

$$0$$

4

$$z_1 = 3$$

$$3y_1+2y_2;$$

$$z_2 =y_2$$

$$y_1+y_2$$

$$3$$

5

$;$ 3

RewrittenLP:

.

*Currentvertex:*

2

$$f$$

$$g$$

*Objectivevalue:* $22$.

$$7$$

$$1$$

$$max 22$$

$$_3z_1$$

$$_3z_2$$

*Optimal:* all $c_i$ $<0$.

$$_3z_1+^5$$

$$1$$

$$_3z_2$$

$$6$$

1

$$z_1$$

$$0$$

2

$;$ 3

Solve 2

(in original LP) to get optimal solution

$$z_2$$

$$0$$

3

$(x_1;x_2)=(1;4)$.

$$1$$

$$2$$

$$_3z_1$$

$$_3z_2$$

$$1$$

4

$$1$$

$$_3z_1+^1$$

$$_3z_2$$

$$4$$

5

$;$ 3

2

$$f$$

$$g$$

Increase

$$y_1$$

$;$ 4

3

$$f$$

$$g$$

$;$ 2

1

$$f$$

$$g$$

Increase

$$x_2$$

$;$ 5

$;$ 5

1

4

$$f$$

$$g$$

$$f$$

$$g$$

232

Algorithms

### 7.6.3 Loose ends

There areseveral important issuesinthe simplexalgorithmthatwe haven'tyet mentioned.

**The** **starting** **vertex.** How do we nd a vertex at which to start simplex? In our 2D and

3D examples we always started at the origin, which worked because the linear programs

happenedtohaveinequalitieswithpositiveright-handsides. InageneralLPwewon'talways

be so fortunate. However, it turns out that nding a starting vertex *can* *be* *reduced* *to* *an* *LP*

andsolvedbysimplex!

To see how this is done, start with any linear program in standard form (recall Sec-

tion7.1.4),since weknowLPscanalwaysbe rewritten thisway.

$min$ $c^Tx$ suchthat $Ax=b$and$x$

$$0:$$

We rst make sure that the right-hand sides of the equations are all nonnegative: if $b_i$ $<$ $0,$

justmultiplybothsides of the $i$thequationby

$1$.

Thenwecreate anewLPasfollows:

Create $m$new*arti* *cial* *variables* $z_1;:::;z_m$

$0,$ where $m$isthenumberof equations.

Add $z_i$ to the left-handside of the$i$th equation.

Let the objective, to be*minimized*,be $z_1+z_2+$

$+z_m$.

For this new LP, it's easy to come up with a starting vertex, namely, the one with $z_i$ $=$ $b_i$ for

all$i$andallother variableszero. Therefore wecansolveitbysimplex,to obtaintheoptimum

solution.

There are two cases. If theoptimum valueof $z_1+$

$+z_m$ iszero, thenall$z_i$'sobtainedby

simplexarezero, andhencefromtheoptimumvertexofthenewLPwegetastartingfeasible

vertex of theoriginalLP,justbyignoringthe $z_i$'s. We canat laststart simplex!

But what if the optimum objective turns out to be positive? Let us think. We tried to

minimizethe sum of the $z_i$'s, but simplex decided that it cannot be zero. But this means that

the original linear program is infeasible: it *needs* some nonzero $z_i$'s to become feasible. This

ishowsimplexdiscovers andreports thatanLPisinfeasible.

**Degeneracy.** In the polyhedron of Figure 7.12 vertex $B$ is *degenerate*. Geometrically, this

means that it is the intersection of more than $n$ $=$ $3$ faces of the polyhedron (in this case,

$;$ 3

$;$ 4

$;$ 5

). Algebraically, it means that if we choose any one of four sets of three inequal-

2

$;$ 3

$;$ 4

$$;$$

$;$ 3

$;$ 5

$$;$$

$;$ 4

$;$ 5

$;$ 4

$;$ 5

ities (

, and

) and solve the corresponding system

2

2

2

3

$$f$$

$$g$$

$$f$$

$$g$$

$$f$$

$$g$$

$$f$$

$$g$$

of three linear equations in three unknowns, we'll get the same solution in all four cases:

$(0;300;100)$. This is a serious problem: simplex may return a suboptimal degenerate vertex

simply because all its neighbors are identical to it and thus have no better objective. And if

we modify simplex so that it detects degeneracy and continues to hop from vertex to vertex

despite lackof anyimprovement inthecost, itmayenduploopingforever.

Onewayto xthisisbya*perturbation*: changeeach$b_i$ byatinyrandomamountto$b_i$

$i$.

Thisdoesn't change the essence of the LPsince the $i$'s are tiny,but it has the effect of differ-

entiatingbetween thesolutionsofthelinearsystems. Tosee whygeometrically,imaginethat

S.Dasgupta,C.H.Papadimitriou,andU.V.Vazirani

233

$;$ 3

$;$ 4

$;$ 5

were joltedalittle. Wouldn'tvertex$B$ splitintotwovertices, very

thefourplanes 2

close to oneanother?

**Unboundedness.** In some cases an LP is unbounded, in that its objective function can be

made arbitrarily large (or small, if it's a minimization problem). If this is the case, simplex

will discover it: in exploring the neighborhood of a vertex, it will notice that taking out an

inequalityand adding another leads to an underdetermined system of equations that has an

in nity of solutions. And in fact (this is an easy test) the space of solutions contains a whole

line across which the objective can become larger and larger, all the way to

. In this case

$$1$$

simplexhaltsandcomplains.

### 7.6.4 The running time of simplex

Whatisthe runningtimeof simplex, for ageneric linearprogram

$max$ $c^Tx$ suchthat $Ax$

$0$ and$x$

$$0;$$

where there are $n$ variablesand $A$ contains $m$ inequalityconstraints? Since it is aniterative

algorithm that proceeds from vertex to vertex, let's start by computing the time taken for a

singleiteration. Supposethecurrentvertexis$u$. Byde nition,itistheuniquepointatwhich

$n$inequalityconstraintsaresatis edwithequality. Eachofitsneighborsshares$n$

$1$ofthese

inequalities,so$u$canhaveatmost$n$

$m$neighbors: choosewhichinequalitytodropandwhich

newone to add.

A naive way to perform an iteration would be to check each potential neighbor to see

whether it really is a vertex of the polyhedron and to determine its cost. Finding the cost is

quick,justadotproduct, butcheckingwhetheritisatruevertexinvolvessolvingasystemof

$n$equationsin$n$unknowns(thatis,satisfyingthe$n$choseninequalitiesexactly)andchecking

whether the result is feasible. By Gaussian elimination (see the following box) this takes

$O(n^3)$ time, givinganunappetizingrunningtimeof $O(mn^4)$ per iteration.

Fortunately, there is amuchbetter way, andthis$mn^4$ factor canbe improved to $mn,$mak-

ingsimplexapracticalalgorithm. Recallour earlierdiscussion(Section 7.6.2)aboutthe*local*

*view* from vertex $u$. It turns out that the per-iteration overhead of rewriting the LP in terms

of the current local coordinates is just $O((m+n)n)$; this exploits the fact that the local view

changesonlyslightlybetweeniterations, injustoneof its de ninginequalities.

Next, to select the best neighbor,werecall thatthe (localviewof) the objective functionis

oftheform $max$ $c_u+~c$

$y$ where$c_u$isthevalueoftheobjectivefunctionat$u$. Thisimmediately

identi esapromisingdirection to move: we pick any $~c_i$ $>0($if there isnone, thenthe current

vertexisoptimalandsimplexhalts). SincetherestoftheLPhasnowbeenrewritteninterms

of the $y-$coordinates, it is easy to determine how much $y_i$ can be increased before some other

inequalityisviolated. (Andifwecanincrease $y_i$ inde nitely,weknowthe LPisunbounded.)

It follows that the running time per iteration of simplex is just $O(mn)$. But how many

$$m+n$$

iterationscouldtherebe? Naturally,therecan'tbemorethan

,whichisanupperbound

$$n$$

on the number of vertices. But this upper bound is exponential in $n$. And in fact, there are

examples of LPs for which simplex does indeed take an exponential number of iterations. In

234

Algorithms

other words, *simplex* *is* *an* *exponential-time* *algorithm.* However, such exponential examples

donotoccurinpractice, anditisthisfactthatmakessimplexsovaluableandsowidelyused.

S.Dasgupta,C.H.Papadimitriou,andU.V.Vazirani

235

**Gaussian** **elimination**

Under our algebraic de nition, merely writing down the coordinates of a vertex involves

solvingasystem of linearequations. Howisthisdone?

Weare givenasystem of $n$linearequationsin$n$unknowns,say$n=4$and

$$x_1$$

$$2x_3$$

$$= 2$$

$$x_2 + x_3$$

$$= 3$$

$$x_1 + x_2$$

$$x_4 = 4$$

$$x_2 + 3x_3 + x_4 = 5$$

The high school method for solving such systems is to repeatedly apply the following rule:

*if* *we* *add* *a* *multiple* *of* *one* *equation* *to* *another* *equation,* *the* *overall* *system* *of* *equations*

$1$timesthe rstequationtothethirdone,weget

*remainsequivalent.* Forexample,adding

the equivalentsystem

$$x_1$$

$$2x_3$$

$$= 2$$

$$x_2 + x_3$$

$$= 3$$

$$x_2 + 2x_3$$

$$x_4 = 2$$

$$x_2 + 3x_3 + x_4 = 5$$

This transformation is clever in the following sense: it *eliminates* the variable $x_1$ from the

thirdequation,leavingjustoneequationwith$x_1$. Inotherwords,ignoringthe rstequation,

we have a system of *three* equations in *three* unknowns: we decreased $n$ by $1$! We can solve

thissmallersystem to get $x_2;x_3;x_4,$andthenplugthese into the rst equationto get $x_1$.

Thissuggests analgorithm oncemore dueto Gauss.

*proceduregauss*($E;X)$

```text
Input: A system E = of equations in n unknowns X =
```

:

$$e_1;:::;e_ng$$

$$x_1;:::;x_ng$$

$$f$$

$$f$$

$$e_1 :a_{11}x_1+a_{12}x_2+$$

$$+a_{1n}x_n =b_1;$$

$$; e_n :a_{n1}x_1 +a_{n2}x_2+$$

$$+a_{nn}x_n =b_n$$

```text
Output: A solution of the system, if one exists if all coefficients ai1 are zero: halt with message ''either infeasible or not linearly independent''
```

$$if n=1: return b_1=a_{11}$$

```text
choose the coefficient ap1 of largest magnitude, and swap equations e1;ep for i=2 to n:
```

$$e_i =e_i$$

$$(a_{i1}=a_{11})$$

$$e_1$$

$$(x_2;:::;x_n)=gauss(E$$

$$e1g$$

$$;X$$

$$x1g$$

$$)$$

$$f$$

$$f$$

$$_{j>1}a_{1j}x_j)=a_{11}$$

$$x_1 =(b_1$$

$$return (x_1;:::;x_n)$$

$$P$$

$$ap1j$$

(When choosing the equation to swap into rst place, we pick the one with largest

for

$$j$$

reasons of *numerical* *accuracy*; after all,wewillbedividingby$a_{p1}$.)

Gaussian elimination uses $O(n^2)$ *arithmetic* *operations* to reduce the problem size from

$1,$ and thususes $O(n^3)$ operations overall. To showthat this isalso agood estimate

$n$to $n$

of the total *running* *time*, we need to argue that the numbers involved remain polynomi-

ally bounded for instance, that the solution $(x_1;:::;x_n)$ does not require too much more

precisionto write downthantheoriginalcoef cients $a_{ij}$ and$b_i$. Doyousee whythisistrue?

236

Algorithms

**Linear** **programming** **in** **polynomial** **time**

Simplex is not a polynomial time algorithm. Certain rare kinds of linear programs cause

it to go from one corner of the feasible region to a better corner and then to a still better

one, andsoonforanexponentialnumberofsteps. Foralongtime, linearprogrammingwas

considered aparadox,aproblem thatcanbesolved inpractice, butnot intheory!

Then, in 1979, a young Soviet mathematician called Leonid Khachiyan came up with

the *ellipsoid* *algorithm*, one that is very different from simplex, extremely simple in its

conception (but sophisticated in its proof) and yet one that solves any linear program in

polynomial time.

Instead of chasing the solution from one corner of the polyhedron to

the next, Khachiyan'salgorithm con nes it to smaller and smaller ellipsoids (skewed high-

dimensionalballs). Whenthisalgorithmwasannounced,itbecameakindof mathematical

Sputnik, a splashy achievement that had the U.S. establishment worried, in the height of

the Cold War, about the possible scienti c superiority of the Soviet Union. The ellipsoid

algorithmturned out to beanimportant theoretical advance, butdid not compete well with

simplex in practice. The paradox of linear programming deepened: A problem with two

algorithms,one thatisef cient intheory, andone thatisef cient inpractice!

A few years later Narendra Karmarkar, a graduate student at UC Berkeley, came up

with a completely different idea, which led to another provably polynomial algorithm for

linearprogramming. Karmarkar'salgorithmisknownas*theinterior* *pointmethod*,because

it does just that: it dashes to the optimum corner not by hopping from corner to corner on

the surface of the polyhedron like simplex does, but by cutting a clever path in the interior

of the polyhedron. Andit does perform wellinpractice.

But perhaps the greatest advance in linear programming algorithms was not

Khachiyan's theoretical breakthrough or Karmarkar's novel approach, but an unexpected

consequence of the latter: the erce competition between the two approaches, simplex and

interior point, resulted inthedevelopment of very fastcode for linearprogramming.

## 7.7 Postscript: circuit evaluation

The importance of linear programming stems from the astounding variety of problems that

reduce to it and thereby bear witness to its expressive power. In a sense, this next one is the

*ultimate* application.

We aregivena*Boolean* *circuit*, that is,adagof gates of thefollowingtypes.

*Inputgates* haveindegree zero, withvaluetrueor false.

AND gates and OR gateshaveindegree $2$.

NOT gates haveindegree $1$.

Inaddition,one of thegates isdesignatedasthe *output*. Here's anexample.

S.Dasgupta,C.H.Papadimitriou,andU.V.Vazirani

237

output

AND

NOT

OR

AND

OR

NOT

true

false

true

The CIRCUIT VALUE problem is the following: when the laws of Boolean logic are applied to

the gatesintopologicalorder, does the output evaluateto true?

Thereisasimple,automaticwayoftranslatingthisproblemintoalinearprogram. Create

avariable$x_g$ for each gate $g,$ withconstraints $0$

$$x_g$$

$1$. Add additionalconstraints for each

type of gate:

$$g$$

$$g$$

$$g$$

$$g$$

gate$g$

OR

AND

NOT

true

false

$$x_g =1$$

$$x_g =0$$

$$h_0$$

$$h$$

$$h$$

$$h$$

$$h_0$$

$$x_g$$

$$x_h$$

$$x_g$$

$$x_h$$

$$x_g =1$$

$$x_h$$

$$x_g$$

$$x_h0$$

$$x_g$$

$$x_h0$$

$$x_g$$

$$x_h+x_h0$$

$$1$$

$$x_g$$

$$x_h+x_h0$$

These constraints force all the gates to take on exactly the right values $0$ for false, and $1$

for true. We don't need to maximize or minimize anything, and we can read the answer off

from the variable$x_o$ corresponding to the outputgate.

This is a straightforward reduction to linear programming, from a problem that may not

seem very interesting at rst. However, the CIRCUIT VALUE problem is in a sense *the* *most*

*general* *problem* *solvable* *in* *polynomial* *time!* After all, any algorithm will eventually run on

a computer, and the computer is ultimately a Boolean combinationalcircuit implemented on

a chip. If the algorithm runs in polynomial time, it can be rendered as a Boolean circuit con-

sisting of polynomially many copies of the computer's circuit, one per unit of time, with the

values of the gates in one layer used to compute the values for the next. Hence, the fact that

CIRCUIT VALUE reducestolinearprogrammingmeansthat*allproblems* *thatcanbesolvedin*

*polynomial* *time* *do!*

238

Algorithms

In our next topic, **NP***-completeness*, we shall see that many *hard* problems reduce, much

the sameway,to *integer* *programming*, linearprogramming'sdif culttwin.

Another parting thought: by what other means can the circuit evaluation problem be

solved? Let's think a circuit is a dag. And what algorithmic technique is most appropriate

for solving problems on dags? That's right: dynamic programming! Together with linear

programming,theworld'stwo most generalalgorithmictechniques.

S.Dasgupta,C.H.Papadimitriou,andU.V.Vazirani

239

## Exercises

7.1. Considerthefollowinglinearprogram.

maximize $5x+3y$

$$5x$$

$$2y$$

$$0$$

$$x+y$$

$$7$$

$$x$$

$$5$$

$$x$$

$$0$$

$$y$$

$$0$$

Plot thefeasibleregionandidentifytheoptimalsolution.

7.2. DuckwheatisproducedinKansasandMexicoandconsumedinNewYorkandCalifornia. Kansas

produces15shnupellsofduckwheatandMexico8. Meanwhile,NewYorkconsumes10shnupells

and California 13. The transportation costs per shnupell are $4 from Mexico to New York, $1

fromMexicotoCalifornia,$2fromKansas toNewYork,and$3andfromKansastoCalifornia.

Write a linear program that decides the amounts of duckwheat (in shnupells and fractions of a

shnupell) to be transported from each producerto each consumer, so as to minimize the overall

transportationcost.

7.3. A cargo plane can carry a maximum weight of 100 tons and a maximum volume of 60 cubic

meters. Therearethreematerialstobetransported,andthecargocompanymaychoosetocarry

anyamountofeach,uptothemaximumavailable limits givenbelow.

Material1hasdensity2tons/cubicmeter,maximumavailableamount40cubicmeters,and

revenue$1,000 percubicmeter.

Material2hasdensity1ton/cubicmeter,maximumavailableamount30cubicmeters,and

revenue$1,200 percubicmeter.

Material3hasdensity3tons/cubicmeter,maximumavailableamount20cubicmeters,and

revenue$12,000 percubicmeter.

Write alinearprogramthat optimizesrevenuewithintheconstraints.

7.4. MoeisdecidinghowmuchRegularDuffbeerandhowmuchDuffStrongbeertoordereachweek.

RegularDuffcosts Moe$$1$perpintandhesells itat$$2$perpint;DuffStrongcostsMoe$$1:50$per

pint and he sells it at
$$3$ per pint. However, as part of a complicated marketing scam, the Duff

companywillonlysellapintofDuffStrongforeachtwopintsormoreofRegularDuffthat Moe

buys. Furthermore, due to past events that are better left untold, Duff will not sell Moe more

than $3;000$pints per week. Moe knows that he can sell howevermuch beer he has. Formulate a

linear program for deciding how much Regular Duff and how much Duff Strong to buy, so as to

maximizeMoe'spro t. Solvetheprogramgeometrically.

7.5. The Canine Products company offers two dog foods, Frisky Pup and Husky Hound, that are

made from a blend of cereal and meat. A package of Frisky Pup requires $1$ pound of cereal and

$1:5$ pounds of meat, and sells for
$$7$. A package of Husky Hound uses $2$ pounds of cereal and

$1$ pound of meat, and sells for
$$6$. Raw cereal costs
$$1$ per pound and raw meat costs
$$2$ per

pound. It also costs
$$1:40$ to package the Frisky Pup and
$$0:60$ to package the Husky Hound. A

total of$240;000$poundsofcerealand $180;000$poundsof meatare available each month. The only

productionbottleneckisthatthefactorycanonlypackage$110;000$bagsofFriskyPuppermonth.

Needlesstosay,managementwouldliketomaximizepro t.

240

Algorithms

(a) Formulatetheproblemasalinearprogramintwovariables.

(b) Graph the feasible region, givethe coordinates of everyvertex,and circle the vertexmaxi-

mizingpro t. What is themaximumpro tpossible?

7.6. Give an exampleof a linear program in two variables whosefeasible regionis in nite, but such

that thereisanoptimumsolutionofboundedcost.

7.7. Findnecessaryandsuf cientconditionsonthereals $a$and$b$underwhichthelinearprogram

$$max x+y$$

$$ax+by$$

$$1$$

$$x;y$$

$$0$$

(a) Is infeasible.

(b) Is unbounded.

(c) Has auniqueoptimalsolution.

7.8. Youaregiventhefollowingpointsintheplane:

$$(1;3); (2;5); (3;7); (5;11); (7;14); (8;15); (10;19):$$

You want to nd a line $ax+by$ $=$ $c$ that approximately passes throughthese points (no line is a

perfect t). Writealinearprogram(youdon'tneedtosolveit)to ndthelinethatminimizesthe

*maximumabsoluteerror*,

$$max$$

$$ax_i+by_i$$

$$c$$

$$:$$

$$7j$$

$$j$$

$$1$$

$$i$$

7.9. A*quadraticprogramming*problemseekstomaximizeaquadratricobjectivefunction(withterms

like $3x^2$

$1$ or $5x_1x_2)$ subject to a set of linear constraints. Givean exampleof a quadratic program

in two variables $x_1;x_2$ such that the feasible region is nonempty and bounded, and yet none of

theverticesofthis regionoptimizethe(quadratic)objective.

7.10. For the following network, with edge capacities as shown, nd the maximum ow from $S$ to $T,$

alongwitha matchingcut.

4

A

5

D

G

6

1

2

2

10

12

1

S

B

E

20

T

6

2

10

4

C

F

5

7.11. Write thedualtothefollowinglinearprogram.

$$max x+y$$

$$2x+y$$

$$3$$

$$x+3y$$

$$5$$

$$x;y$$

$$0$$

FindtheoptimalsolutionstobothprimalanddualLPs.

S.Dasgupta,C.H.Papadimitriou,andU.V.Vazirani

241

7.12. For thelinearprogram

$$max x_1$$

$$2x_3$$

$$x_1$$

$$x_2$$

$$1$$

$$2x_2$$

$$x_3$$

$$1$$

$$x_1;x_2;x_3$$

$$0$$

provethat thesolution$(x_1;x_2;x_3)$ $=(3=2;1=2;0)$is optimal.

7.13. *Matching* *pennies.* In this simple two-player game, the players (call them $R$ and $C)$ each choose

anoutcome,*heads*or*tails*. Ifbothoutcomesareequal,$C$ givesadollarto$R$;iftheoutcomesare

different,$R$ givesadollarto$C$.

(a) Representthepayoffsbya$2$

$2$matrix.

(b) What is thevalueofthisgame,andwhataretheoptimalstrategiesforthetwoplayers?

7.14. The pizza business in Little Town is split between two rivals, Tony and Joey. They are each

investigatingstrategiestostealbusinessawayfromtheother. Joeyisconsideringeitherlowering

pricesorcuttingbiggerslices. Tonyislookingintostartingupalineofgourmetpizzas,oroffering

outdoor seating, or giving free sodas at lunchtime. The effects of these various strategies are

summarized in the following payoff matrix (entries are dozens of pizzas, Joey's gain and Tony's

loss).

TONY

Gourmet Seating Freesoda

$$+2$$

$$0$$

$$3$$

JOEY Lowerprice

$$1$$

$$2$$

$$+1$$

Biggerslices

Forinstance,ifJoeyreducespricesandTonygoeswiththegourmetoption,thenTonywilllose2

dozenpizzasworthofbusiness toJoey.

What is thevalueofthisgame,andwhataretheoptimalstrategiesforTonyandJoey?

7.15. Findthevalueofthegamespeci edbythefollowingpayoffmatrix.

$$0$$

$$0$$

$$1$$

$$1$$

$$0$$

$$1$$

$$2$$

$$1$$

$$1$$

$$1$$

$$1$$

$$1$$

$$1$$

$$0$$

$$0$$

$$1$$

$$1$$

$$2$$

$$0$$

$$3$$

$$1$$

$$1$$

$$1$$

$$1$$

$$0$$

$$3$$

$$2$$

$$1$$

$$0$$

$$2$$

$$1$$

$$1$$

(*Hint:* Considerthemixedstrategies $(1=3;0;0;1=2;1=6;0;0;0)$and$(2=3;0;0;1=3)$.)

7.16. A salad is any combination of the following ingredients: (1) tomato, (2) lettuce, (3) spinach, (4)

carrot, and (5) oil. Each salad must contain: (A) at least 15 grams of protein, (B) at least 2

and at most 6 grams offat, (C)at least 4 grams of carbohydrates, (D)at most 100 milligrams of

sodium. Furthermore,(E)youdonotwantyoursalad tobemorethan50% greensbymass. The

nutritionalcontentsoftheseingredients(per100grams)are

242

Algorithms

ingredient

energy

protein

fat

carbohydrate

sodium

(kcal)

(grams)

(grams)

(grams)

(milligrams)

tomato

21

0.85

0.33

4.64

9.00

lettuce

16

1.62

0.20

2.37

8.00

spinach

371

12.78

1.58

74.69

7.00

carrot

346

8.39

1.39

80.70

508.20

oil

884

0.00

100.00

0.00

0.00

Find a linear programming applet on the Web and use it to make the salad with the fewest

calories under the nutritional constraints. Describe your linear programming formulation and

theoptimalsolution(thequantityofeachingredientandthevalue). CitetheWebresourcesthat

youused.

7.17. Considerthefollowingnetwork(thenumbersareedgecapacities).

4

A

C

9

7

2

S

T

2

6

5

B

D

3

(a) Findthemaximum ow$f$ anda minimumcut.

(b) Drawtheresidualgraph$G_f$ (alongwithitsedgecapacities). Inthisresidualnetwork,mark

theverticesreachablefrom$S$ andtheverticesfromwhich$T$ isreachable.

(c) An edge of a network is called a *bottleneck* *edge* if increasing its capacity results in an

increaseinthemaximum ow. List allbottleneckedgesintheabovenetwork.

(d) Give a very simple example (containing at most four nodes) of a network which has no

bottleneckedges.

(e) Give an ef cient algorithm to identify all bottleneck edges in a network. (*Hint:* Start by

runningtheusual network owalgorithm,andthenexaminetheresidualgraph.)

7.18. Therearemanycommonvariationsofthemaximum owproblem. Herearefourofthem.

(a) There are many sources and many sinks, and we wish to maximize the total ow from all

sourcestoallsinks.

(b) Each*vertex*alsohas acapacityonthemaximum owthatcanenterit.

(c) Eachedgehasnotonlyacapacity,butalsoa*lowerbound*onthe owitmust carry.

(d) The outgoing owfrom eachnode$u$ is notthe same as the incoming ow,but is smaller by

a factorof$(1$

$_u),$where $u$ is aloss coef cientassociatedwithnode$u$.

Eachofthesecanbesolvedef ciently. Showthisbyreducing(a)and(b)totheoriginalmaxow

problem,andreducing(c)and(d)tolinearprogramming.

7.19. Suppose someone presents you with a solution to a maxow problem on some network. Give a

*linear*timealgorithmtodeterminewhetherthesolutiondoesindeedgiveamaximum ow.

S.Dasgupta,C.H.Papadimitriou,andU.V.Vazirani

243

7.20. Considerthefollowinggeneralizationofthemaximum owproblem.

You are given a directed network $G$ $=$ $(V;E)$ with edge capacities

$$ceg$$

. Instead of a single $(s;t)$

$$f$$

pair,youaregivenmultiplepairs$(s_1;t_1);(s_2;t_2);:::;(s_k;t_k),$wherethe$s_i$aresourcesof$G$andthe

$t_i$ aresinks of$G$. Youarealsogiven$k$ *demands*$d_1;:::;d_k$. Thegoalisto nd$k$ ows$f^{(1)};:::;f^{(k)}$

withthefollowingproperties:

$f^{(i)}$ is avalid owfrom$s_i$ to$t_i$.

For eachedge$e,$thetotal ow$f^{(1)}$

$$_e +f^{(2)}$$

$$+f^{(k)}$$

$$_e +$$

$e$ doesnotexceedthecapacity$c_e$.

Thesizeofeach ow$f^{(i)}$ is atleast thedemand$d_i$.

Thesizeofthe*total* ow(thesumofthe ows)is as largeas possible.

Howwouldyousolvethis problem?

7.21. An edge of a ow network is called *critical* if decreasing the capacity of this edge results in a

decreaseinthemaximum ow. Giveanef cientalgorithmthat ndsacriticaledgeinanetwork.

7.22. Inaparticularnetwork$G=(V;E)$whoseedgeshaveintegercapacities$c_e,$wehavealreadyfound

the maximum ow $f$ from node $s$ to node $t$. However, we now nd out that one of the capacity

valuesweusedwaswrong: foredge$(u;v)$ weused$c_{uv}$ whereasitshouldhavebeen$c_{uv}$

$1$. This

is unfortunatebecausethe ow$f$ usesthat particularedgeatfullcapacity: $f_{uv}$ $=c_{uv}$.

We could redo the ow computation from scratch, but there's a faster way. Show how a new

optimal owcanbecomputedin$O($

$$V$$

$$+$$

$$E$$

$)$ time.

$$j$$

$$j$$

$$j$$

$$j$$

7.23. A *vertex* *cover* of an undirectedgraph $G$ $=$ $(V;E)$ is a subset of the vertices which touches every

edge thatis, asubset $S$

$V$ suchthat foreachedge

$$u;v$$

$E,$oneorbothof$u;v$ arein$S$.

$$f$$

$$g2$$

Showthattheproblemof ndingtheminimumvertexcoverina*bipartite*graphreducestomax-

imum ow. (*Hint:* Canyourelatethis problemtotheminimumcutinanappropriatenetwork?)

7.24. *Directbipartitematching.* We'veseenhowto nda maximummatching ina bipartite graphvia

reductiontothemaximum owproblem. We nowdevelopadirectalgorithm.

Let$G=(V1[$

$V_2;E)$beabipartitegraph(soeachedgehasoneendpointin$V_1$ andoneendpointin

$V_2),$ andlet$M$

$E$ be amatching inthe graph(that is, a set ofedgesthat don'ttouch). A vertex

$$2$$

is said to be *covered* by $M$ if it is the endpoint of one of the edges in $M$. An *alternating* *path* is

a path ofodd lengththat starts and ends with a non-coveredvertex,and whoseedgesalternate

between$M$ and$E$

$M$.

(a) Inthebipartite graphbelow,amatching$M$ is showninbold. Findanalternatingpath.

E

A

F

B

G

C

H

D

I

244

Algorithms

(b) Provethat amatching$M$ is maximalifandonlyiftheredoesnotexistanalternatingpath

withrespecttoit.

(c) Design an algorithm that nds an alternating path in $O($

$$V$$

$$+$$

$$E$$

$)$ time using a variant of

$$j$$

$$j$$

$$j$$

$$j$$

breadthrstsearch.

(d) Giveadirect$O($

$$V$$

$$E$$

$)$algorithmfor ndinga maximalmatchinginabipartite graph.

$$j$$

$$j j$$

$$j$$

7.25. *Thedualofmaximum* *ow.* Considerthefollowingnetworkwithedgecapacities.

A

2

1

1

S

T

3

1

B

(a) Write theproblemof ndingthemaximum owfrom$S$ to$T$ as alinearprogram.

(b) Write downthe dual of this linear program. Thereshould be a dual variable foreach edge

ofthenetworkandforeachvertexotherthan$S;T$.

Now we'll solve the same problem in full generality. Recall the linear program for a general

maximum owproblem(Section7.2).

(c) Write down the dual of this general ow LP, using a variable $y_e$ for each edge and $x_u$ for

eachvertex$u$

$=s;t$.

$$6$$

(d) Showthat anysolutionto thegeneraldualLP must satisfy the followingproperty: forany

directedpathfrom$s$to$t$inthenetwork,thesumofthe$y_e$ valuesalongthepathmustbeat

least $1$.

(e) What are the intuitive meanings of the dual variables? Show that any $s$

$t$ cut in the

networkcanbetranslatedintoadualfeasiblesolutionwhosecostisexactlythecapacityof

that cut.

7.26. Inasatis able system oflinearinequalities

$$a_{11}x_1+$$

$$+a_{1n}x_n$$

$$b_1$$

...

$$a_{m1}x_1 +$$

$$+a_{mn}x_n$$

$$b_m$$

we describe the $j$th inequality as *forced-equal* if it is satis ed with equality by *every* solution

$b_j$ is *not*forced-equalif thereexists an $x$

$x$ $=$ $(x_1;:::;x_n)$ ofthesystem. Equivalently,

$$_ia_{ji}x_i$$

$_ia_{ji}x_i$ $<b_j$.

that satis es thewholesystemandsuchthat

$$P$$

For example,in

$$P$$

$$x_1+x_2$$

$$2$$

$$x_1$$

$$x_2$$

$$2$$

$$x_1$$

$$1$$

$$x_2$$

$$0$$

S.Dasgupta,C.H.Papadimitriou,andU.V.Vazirani

245

the rst two inequalities are forced-equal, while the third and fourth are not. A solution $x$ to

the system is called *characteristic*if, for everyinequality $I$ that is not forced-equal,$x$ satis es $I$

withoutequality. Intheinstanceabove,suchasolutionis$(x_1;x_2)=($

$1;3),$forwhich$x_1$ $<1$and

$x_2$ $<0$while$x_1+x_2$ $=2$and

$$x_1$$

$$x_2 =$$

$2$.

(a) Showthat anysatis able systemhasa characteristicsolution.

(b) Given a satis able system of linear inequalities, show how to use linear programming to

determinewhichinequalitiesareforced-equal,andto ndacharacteristic solution.

7.27. Show that the *change-making* *problem* (Exercise 6.17) can be formulated as an integer linear

program. Can wesolvethis programas anLP, inthecertaintythat thesolutionwill turnoutto

beintegral(asinthecaseofbipartitematching)? Eitherproveitorgivea counterexample.

7.28. *A* *linear* *program* *for* *shortest* *path.* Suppose we want to compute the shortest path from node $s$

tonode$t$inadirectedgraphwithedgelengths$l_e$ $>0$.

$_el_ef_e$ subject to

(a) Show that this is equivalent to nding an $s$

$t$ ow $f$ that minimizes

size$(f)$ $=1$. Therearenocapacityconstraints.

$$P$$

(b) Write theshortestpathproblemas alinearprogram.

(c) Showthat thedualLP canbewrittenas

$$max x_s$$

$$x_t$$

$$x_u$$

$$x_v$$

$l_{uv}$ forall$(u;v)$

$$E$$

$$2$$

(d) An interpretation for the dual is given in the box on page 223. Why isn't our dual LP

identicaltotheoneonthatpage?

7.29. *Hollywood.* A lm producer is seeking actors and investors for his new movie. There are $n$

availableactors;actor$i$charges$s_i$ dollars. Forfunding,thereare$m$availableinvestors. Investor

$j$ will provide $p_j$ dollars, but only on the condition that certain actors $L_j$ $f$

$$1;2;:::;n$$

are

$$g$$

included in the cast (*all* of these actors $L_j$ must be chosen in order to receive funding from

investor$j)$.

The producer's pro t is the sum of the payments from investors minus the payments to actors.

Thegoalis tomaximizethis pro t.

(a) Express this problem as an integer linear program in which the variables take on values

$$0;1$$

.

$$f$$

$$g$$

(b) Nowrelaxthistoalinearprogram,andshowthattheremustinfactbean*integral*optimal

solution(asis thecase,forexample,withmaximum owandbipartitematching).

7.30. *Hall'stheorem.* ReturningtothematchmakingscenarioofSection7.3,supposewehaveabipar-

tite graph with boys on the left and an equal number of girls on the right. Hall's theorem says

that thereis aperfectmatchingifandonlyifthefollowingconditionholds: anysubset $S$ ofboys

$$S$$

is connectedtoatleast

girls.

$$j$$

$$j$$

Provethis theorem. (*Hint:* Themaxowmin-cuttheoremshouldbehelpful.)

7.31. Considerthefollowingsimplenetworkwithedgecapacitiesas shown.

246

Algorithms

A

1000

1000

S

T

1

1000

1000

B

(a) Showthat,iftheFord-Fulkersonalgorithmisrunonthisgraph,acarelesschoiceofupdates

might cause it to take $1000$ iterations. Imagine if the capacities were a million instead of

$1000$!

We will now nd a strategy for choosing paths under which the algorithm is guaranteed to ter-

minateinareasonablenumberofiterations.

Consideran arbitrary directednetwork$(G$ $=$ $(V;E);s;t;$

$$ceg$$

$)$ in whichwewantto ndthe max-

$$f$$

imum ow. Assume for simplicity that all edgecapacities are at least $1,$ and de nethe capacity

ofan$s$

$t$pathtobethesmallestcapacityofitsconstituentedges. The*fattestpath*from$s$to$t$is

thepathwiththemostcapacity.

(b) Show that the fattest $s$

$t$ path in a graph can be computed by a variant of Dijkstra's

algorithm.

(c) Show that the maximum ow in $G$ is the sum of individual ows along at most

$$E$$

paths

$$j$$

$$j$$

from$s$to$t$.

(d) Nowshowthatifwealwaysincrease owalongthefattestpathintheresidualgraph,then

the Ford-Fulkerson algorithm will terminate in at most $O($

$$E$$

$logF)$ iterations, where $F$ is

$$j$$

$$j$$

the size of the maximum ow. (*Hint:* It might help to recall the proof for the greedy set

coveralgorithminSection5.4.)

In fact, an evensimpler rule ndinga path in the residual graph using breadthrst search

guaranteesthat atmost $O($

$$V$$

$$E$$

$)$ iterationswillbeneeded.

$$j$$

$$j j$$

$$j$$
