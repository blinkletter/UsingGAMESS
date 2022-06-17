# Water: Getting Started

What can we explore with computational chemistry? Let us **explore the electronic structure** of some small molecules. In this chapter we will learn ways to input molecules into *GAMESS* via input files and interpret the resulting log files. 


## Learning Goals

This exercise will hopefully accomplish the following goals while learning new skills:
-	We will confirm that your installation of *GAMESS* is **working properly**
-	We will **construct** a *GAMESS* input file with a text editor.
-	We will use three methods for creating a description of the **atomic positions**
    -	Cartesian coordinates (classic *xyz* 3D space)
    -	Unique Cartesian coordinates with symmetry point groups
    -	Internal coordinates using a Z-matrix
-	We will use *GAMESS* to determine the **optimized structure** of small molecules using semi-empirical methods. 
-	We will create new input files **using the results** of the previous calculation and calculate the optimized structure using **more expensive** methods.
-	We will humbly recognize that we are organic chemists and that we are using *GAMESS* as a **recipe** with poor understanding of the **consequences** of our choices. We will observe these consequences in our results as we move forward. If we knew what we were doing, we might avoid many inevitable **pitfalls**. We have a whole box a band aids and always wear our safety goggles. Let’s go!


## Small Molecules

**Methane**, **ammonia** and **water**: these three molecules are *sp<sup>3</sup>* hybridized and should be **tetrahedral** in their VSEPR geometry. We expect to see bonds or lone pairs at angles of near 109˚

To investigate these molecules, will need to **describe** a molecule for a computer. We will discuss two methods: Cartesian coordinates, where every atom is placed in 3D space with *xyz* values; **unique Cartesian coordinates**, where only atoms that are symmetry unique are placed and the rest are automatically generated to satisfy the symmetry point group; and the **Z-matrix**, where each atom is placed in space relative to the previous one in a carefully created list.

*GAMESS* works by positioning the nuclei and then creating a mathematical function for the **energy** of the electrons. By taking the **derivative** of that function, *GAMESS* can determine if the current position is on a **slope** and then change the positions by a small amount to follow that slope downhill in energy. A new function is calculated and the process repeats again and again

In this exercise, we will be **manually** creating and running input files. In the future, we will learn how to use *MacMolPlt* and *Avogadro* to quickly build molecules and **automatically** create input files. But lets us first get our hands dirty before we start using power tools to do the hard work for us. Wax on, wax off!

## Water

Water has three atoms that have found an **arrangement** in space for the nuclei and electrons that is as **low in energy** as possible. Can we calculate that arrangement and see if it fits with observations? First, we must create a data set that describes the positions of the nuclei. Let us begin by discussing the nature of the 3D **coordinate space** used by *GAMESS*.

### The 3D World

*x*,*y*,*z*… That triplet describes the **entire universe**. But *GAMESS* does not treat *x*, *y* and *z* equally. Consider the axis diagram in {numref}`fig1`.

```{figure} images/GAMESS_AXES.png
---
width: 700px
name: fig1
---
*The axis scheme for *GAMESS* atomic coordinates*
```

When constructing a structure using either Cartesian coordinates or a Z-matrix, we don’t consider any priority for an axis. However, when using **point groups** and symmetry to define molecules with **unique** Cartesian coordinates, we must pay attention to how *GAMESS* manipulates **symmetry**. The **primary axis** of the point group is expected to be the *z*-axis. Any vertical &sigma;-plane should first be set up in the *xz* plane. The horizontal &sigma;-plane should be considered to be the *xy* plane. The first perpendicular 2-fold axis should be set up along the *x*-axis. Keep these ideas in mind as we construct our first molecules.

### Symmetry

Symmetry is beautiful. It also helps with math. If a molecule has symmetry, we should use it to make the calculations performed by *GAMESS* **less expensive**. A molecule that is known to possess 2-fold symmetry may be half as difficult to analyze because we may only need half the math. This depends a lot on the basis set chosen to describe each atomic orbital but, most of the time, it is to our advantage to declare and use a **symmetry point group**.

**Water** has a *C<sub>2</sub>* axis. There is no perpendicular *C<sub>2</sub>* axis so we remain in the *C* group rather than rising to *D*. There is no *&sigma;<sub>h</sub>* but there are two *&sigma;<sub>v</sub>* planes. Therefore water is in the *C<sub>2v</sub>* point group. We will use Cartesian coordinates that place the **primary axis** along the *z*-axis and the atoms in the *xz* plane. See {numref}`fig2` for how we will position water in the 3D space used by *GAMESS*.

```{figure} images/WATER_AXES.png
---
width: 700px
name: fig2
---
*Water positioned in *GAMESS* 3D space with the *C<sub>2</sub>* axis along the z-axis and the primary *&sigma;<sub>v</sub>* plane as the xz plane*
```
 
### Building Water

So how shall we build water? We can provide cartesian coordinates that position **oxygen** at the origin. Then we can position a **hydrogen** in on *xz* quadrant and the second hydrogen in the opposite quadrant. Compare the below set of coordinates to {numref}`fig2`.

| Atom	   |   x   | y     | z     |
|:-----    | :---: | :---: | :---: |
| Oxygen   | 0	   | 0	   | 0     |   
| Hydrogen | b	   | 0	   | –a    |
| Hydrogen | –b    | 0     | –a    |

What values should we use for *a* and *b*? We know that the **bond angle** should be 104.5˚ and that the **bond length** in water is 0.95 Å. We could use trigonometry and position the atoms accordingly. Or we could just throw some **guess** in and let *GAMESS* start there as it moves toward finding the optimal structure. I will set both a and b to 0.7 Å. Our initial guess at water will have a bond angle of 90˚ and a bond length of $\sqrt{(0.7+0.7)}$.
 
### Your First Input File

We now need to create a **text file** that will be read into *GAMESS* to provide the information for the calculation. We must tell *GAMESS* what **kind** of calculation, the **methods** to use for determining energy, The **conditions** for declaring a satisfactory structure, and the **data** for the structure.

Below in {numref}`water.inp` is the text file for this first *GAMESS* run. I created a file called water.inp and typed in the following text (feel free to cut and paste.)

```{code-block} 
---
name: water.inp
linenos: True
lineno-start: 1
emphasize-lines: 
caption: water.inp
---
 $CONTRL SCFTYP=RHF RUNTYP=OPTIMIZE MAXIT=30 MULT=1 ICHARG=0 COORD=CART $END
 $SYSTEM TIMLIM=525600 MEMORY=1000000 $END
 $BASIS GBASIS=AM1 $END
 $SCF DIRSCF=.TRUE. $END
 $STATPT OPTTOL=0.0001 NSTEP=100 $END
 $DATA 
Water
CNV 2

O     8.0   0.0   0.0   0.0
H     1.0  -0.7   0.0  -0.7
H     1.0   0.7   0.0  -0.7
 $END
```

### The Structure of The Input File

A *GAMESS* input file is a series of text lines called “**cards**.” (Before your parents were born, computers did not receive input via a keyboard, they used punched paper cards.) Each line must be less than **80 characters** (those paper cards were only so big.)

The input is separated in a series a “**groups**.” Each group begins with a `$` character and ends with a `$END` string. There are many, many groups available to the sophisticated theoretical chemist. We will only use a handful. In the water.inp file, we use the following groups: `$CONTRL`, `$SYSTEM`, `$BASIS`, `$STATPT` and `$DATA`. The `$` character for a group MUST be in the **second column** of a card (*GAMESS* is written in *FORTRAN*, an ancient computer language that is based on paper cards and therefore obsessive about columns in data input.) After several *GAMESS* jobs fail spectacularly on you, you will come to believe in this second column requirement.

### *GAMESS* groups

Here is a quick **overview** of the groups used in our first job. We will add to our skills as we move forward.

#### The \$CONTRL Group

The `$CONTRL` group establishes the **kind of calculation**. It may contain many parameters. The ones used here are our beginning set.

```{code-block} 
---
linenos: True
lineno-start: 1
emphasize-lines: 
caption: water.inp
---
 $CONTRL SCFTYP=RHF RUNTYP=OPTIMIZE MAXIT=30 MULT=1 ICHARG=0 COORD=CART $END
```

| Parameter | Notes |
| :---- | :---- |
| `SCFTYP=RHF` | The **method** used is “restricted Hartee-Fock.” This assumes that all electrons are paired. |
| `RUNTYP=OPTIMIZE` | The **calculation** is a structural optimization. |
| `MAXIT=30` | The **maximum** number of iterations to determine the derivative of the function that describes everything about everything in the molecule. |
| `MULT=1` | The **spin** multiplicity (1 means all electron spins are paired) |
| `ICHARG=0` | The **charge** on the molecule |
| `COORD=CART` | The **coordinate** system that we are using. We will use `CART` for describing the xyz of all atoms, `UNIQUE` for describing the xyz coordinates of atoms unique in the symmetry point group, and `ZMT` for internal coordinates in *Z-matrix* format. The very first run with `COORD=CART` will convert the *xyz* data into a symmetrical system aligned with the **primary axis** (we are already there) and with the origin at the center of mass of the molecule (we are definitely not there). The first result file will report the unique symmetry coordinates for the molecule and we should use these new coordinates and `COORD=UNIQUE` for all subsequent calculations. |

```{note}
The `CART` coordinate option has been deprecated in modern versions of *GAMESS*. The new flag is `PRINAXIS`. The `CART` option will perform the job of `PRINAXIS`, but `CART` may someday be gone entirely. Both `CART` and `PRINAXIS` will reorient the molecule along the primary axis of the point group and generate a set of Cartesian coordinates for the symmetry unique atoms. You will only ever run a `CART` or `PRINAXIS` calculation once and thereafter will use the symmetry unique atoms and `COORD=UNIQUE` in all future calculations with your molecule.
```

#### The \$SYSTEM Group

The `$SYSTEM` group defines parameters for the computer system.

```{code-block} 
---
linenos: True
lineno-start: 2
emphasize-lines: 
caption: water.inp
---
 $SYSTEM TIMLIM=525600 MEMORY=1000000 $END
```

| Parameter | Notes |
| :---- | :---- |
|`TIMLIM=525600` | The **time limit** for the calculation. 525,600 minutes – how do you measure a year in the life? |
|`MEMORY=1000000` | The **memory** to be used (for each processor core.) Increase this if your job crashes out and complains about a lack of memory. |

#### The \$BASIS Group

The `$BASIS` group defines the **theoretical rigor** of the calculation. We will discuss this in more detail later. By using the AM1 level of theory we are declaring that we will use **semi-empirical** methods. This is a very **low level** calculation and requires little in computer resources. We will soon explore methods that will take some serious computer time (and time is money.)

```{code-block} 
---
linenos: True
lineno-start: 3
emphasize-lines: 
caption: water.inp
---
 $BASIS GBASIS=AM1 $END
```

#### The \$SCF Group

The `$SCF` group is specific to the way the calculation is **performed**. The first derivative of the energy function is calculated and stored in a temporary file on disk. Later, when it is needed again, it is read from the disk (it is called several times in the calculation method.) Modern processors can actually **recalculate** this function from scratch faster than a computer hard disk can spin. The `DIRSCF=.TRUE.` command sets *GAMESS* to recalculate the function **each time** it is needed rather than read from the much slower disk drive (modern SSD storage may change this requirement – computers are improving all the time.)

```{code-block} 
---
linenos: True
lineno-start: 4
emphasize-lines: 
caption: water.inp
---
 $SCF DIRSCF=.TRUE. $END
```

#### The \$STATPT Group

The `$STATPT` group establishes the parameters for deciding when we have reached a “**stationary point**” where the derivative of the energy function is near zero (zero slope is likely the bottom of an energy well, the lowest point along the path that *GAMESS* has taken).

```{code-block} 
---
linenos: True
lineno-start: 5
emphasize-lines: 
caption: water.inp
---
 $STATPT OPTTOL=0.0001 NSTEP=100 $END
```
| Parameter | Notes |
| :---- | :---- |
|`OPTTOL=0.0001` | If the RMS average of the energy gradients (slopes) for the whole system is less than this value then we declare that we are **finished**. |
|`NSTEP=100` | The maximum number of steps that we take in the algorithm before we **give up**. |


#### The \$DATA Group

The above groups instructed *GAMESS* how to treat the next group, the **star of the show**, the `$DATA` group. Let us now examine this importanjt part of the input file.

```{code-block} 
---
linenos: True
lineno-start: 6
emphasize-lines: 3
caption: water.inp
---
 $DATA 
Water
CNV 2

O     8.0   0.0   0.0   0.0
H     1.0  -0.7   0.0  -0.7
H     1.0   0.7   0.0  -0.7
 $END
 ```
| Line | Notes |
| :---- | :---- |
| Line 7 | The first line in the `$DATA` group is the **name** of the job. Put whatever you want there. I chose water, it seemed appropriate. |
| Line 8 | The next line is the **symmetry point group**. Water is *C<sub>2v</sub>*. *GAMESS* establishes this in two parts: first we declare *C<sub>nv</sub>* and then we set the value of $n$ as 2.|
| Line 9 | The next line is **blank**. This is important. Leave it blank. (If we are not using symmetry, we will declare the point group to be *C<sub>1</sub>* and then the blank line will not be used.  Don’t worry, after a few crashed jobs you will get the hang of this.) |
| Lines 10..n | All the following lines are the data for the nuclei. The first column is the **name** (it can be **anything** up to 10 characters), the next is the **nuclear charge** (this **defines** the atom), and then the *xyz* coordinates. Like all *GAMESS* groups, the `$DATA` group is ended by the `$END` string. |

Since we defined `COORD=CART` in the `$CONTRL` group, *GAMESS* will input all the **atomic coordinates** and attempt to interpret them via the *C<sub>2v</sub>* point group. If your coordinates do not fit in that point group, the calculation will probably fail. If they fit the *C<sub>2v</sub>* group, then *GAMESS* will identify the symmetry and use only the **unique atoms** within the point group in the subsequent calculation. Defining the symmetry point group is very useful in **minimizing the costs** of a calculation.


-----

## Your First *GAMESS* Job

Now we have an **input file** named `water.inp`. We can run that job via *GamessQ*, but in this exercise we will stay with the basics and run it via the **command line**.

Open a terminal emulator window and type in the following command…

```
gms water.inp
```

*gms* is the script that calls *GAMESS*. After that is the **input file** name, `water.inp`. The script will ask for a name for the **result file**. I just hit return to accept the default, `water.log`. That .log file will be written into the current directory. In about three seconds the job finished. That’s all there is to it. 

The exact syntax depends on the directory that you are in and the locations of the input files and the gms script involved. I set the **environmental variable** `$PATH` to enable command calls to find *gms* in the `/Applications/gamess` directory on my own computer. 

```{tip}
Use the following command to create a path to the *gms* script (change the path to suit your situation): 
`export PATH=$PATH:/Applications/gamess` 
```

```{tip}
Enter `gms help` for information about using *gms*.
```

-----

## Your First Output File

The result file is named `water.log` in this case. Open it in a **text editor** and examine the contents.

**Search** for the string NSERCH. Every time it appears involves setting up or declaring the results of an energy calculation. The first time it appears we see the text show in the excerpt of {numref}`water.log1`

```{code-block} 
---
name: water.log1
linenos: True
lineno-start: 287
emphasize-lines: 11,12,13
caption: water.log
---
BEGINNING GEOMETRY SEARCH POINT NSERCH=   0 ...

 COORDINATES OF SYMMETRY UNIQUE ATOMS (ANGS)
   ATOM   CHARGE       X              Y              Z
 ------------------------------------------------------------
 O           8.0   0.0000000000   0.0000000000   0.0783404292
 H           1.0  -0.7000000000   0.0000000000  -0.6216595708
 COORDINATES OF ALL ATOMS ARE (ANGS)
   ATOM   CHARGE       X              Y              Z
 ------------------------------------------------------------
 O           8.0   0.0000000000   0.0000000000   0.0783404292
 H           1.0   0.7000000000  -0.0000000000  -0.6216595708
 H           1.0  -0.7000000000   0.0000000000  -0.6216595708
```

We see that *GAMESS* has found the **unique atoms** of the **point group**. From these, all the atoms can be created. *GAMESS* is using our initial values but has positioned the center of mass at the origin by adding 0.0783 Å to the z-axis.

Keep searching for NSERCH. Almost **200 lines later** in the water.log result file we see that we have finished step zero ({numref}`water.log2`.) 


```{code-block} 
---
name: water.log2
linenos: True
lineno-start: 432
emphasize-lines: 1, 10
caption: water.log
---
NSERCH:   0  E=      -12.8027678782  GRAD. MAX=  0.0593284  R.M.S.=  0.0244052

          FORCE CONSTANT MATRIX NOT UPDATED --- TAKING FIRST STEP
          MIN SEARCH, CORRECT HESSIAN, TRYING PURE NR STEP
               NR STEP HAS LENGTH         =   0.474433
          TRIM/QA LAMBDA FOR NON-TS MODES =  -0.06454854
          TRIM/QA STEP HAS LENGTH         =   0.300000
          RADIUS OF STEP TAKEN=   0.30000  CURRENT TRUST RADIUS=   0.30000

 BEGINNING GEOMETRY SEARCH POINT NSERCH=   1 ...

 COORDINATES OF SYMMETRY UNIQUE ATOMS (ANGS)
   ATOM   CHARGE       X              Y              Z
 ------------------------------------------------------------
 O           8.0   0.0000000000   0.0000000000  -0.0197579410
 H           1.0  -0.7733745023  -0.0000000000  -0.5726103857
 COORDINATES OF ALL ATOMS ARE (ANGS)
   ATOM   CHARGE       X              Y              Z
 ------------------------------------------------------------
 O           8.0   0.0000000000   0.0000000000  -0.0197579410
 H           1.0   0.7733745023  -0.0000000000  -0.5726103857
 H           1.0  -0.7733745023  -0.0000000000  -0.5726103857
```


The initial **energy** and the derivative (slope or gradient of the energy function) has been **calculated**. The gradient w.r.t. each axis will be used to compute a distance to **move** for each atom. Each change is **applied** and the data set for step one is declared a few lines later.

The energy and gradients will be computed again and the coordinates altered accordingly. This will **repeat** until we fulfil the conditions for the stationary point set in the `$STATPT` group. In our example, the **stationary point** is declared to be located after we finish step 3 as shown in {numref}`water.log3`

```{code-block} 
---
name: water.log3
linenos: True
lineno-start: 689
emphasize-lines: 1, 13-15
caption: water.log
---
NSERCH:   3  E=      -12.8093121210  GRAD. MAX=  0.0000133  R.M.S.=  0.0000072


      ***** EQUILIBRIUM GEOMETRY LOCATED *****
 COORDINATES OF SYMMETRY UNIQUE ATOMS (ANGS)
   ATOM   CHARGE       X              Y              Z
 ------------------------------------------------------------
 O           8.0   0.0000000000   0.0000000000   0.0083001974
 H           1.0  -0.7550350900   0.0000000000  -0.5866394549
 COORDINATES OF ALL ATOMS ARE (ANGS)
   ATOM   CHARGE       X              Y              Z
 ------------------------------------------------------------
 O           8.0   0.0000000000   0.0000000000   0.0083001974
 H           1.0   0.7550350900  -0.0000000000  -0.5866394549
 H           1.0  -0.7550350900   0.0000000000  -0.5866394549

          INTERNUCLEAR DISTANCES (ANGS.)
          ------------------------------

                1 O          2 H          3 H     

   1 O       0.0000000    0.9612654 *  0.9612654 *
   2 H       0.9612654 *  0.0000000    1.5100702 *
   3 H       0.9612654 *  1.5100702 *  0.0000000  

  * ... LESS THAN  3.000
```

We now have the **energy** that was calculated and the coordinates for the final iteration of the **structure**. Next, *GAMESS* will write molecular orbital data and any other sets of data requested in the input file. We will uses this extra data to visualize molecular orbitals in a future exercise.

We see that the **bond lengths** are 0.961 Å and are identical, as required by the symmetry point group.

## Higher Levels of Theory

AM1 uses precalculated values and assumptions to **simplify** the math. It is good for systems that it has been designed for, mostly simple organic molecules. However, if we want to explore strained systems or calculate **accurate** molecular orbitals we will have to use *ab initio* methods. We will use Hartree-Fock theory and basis sets of atomic orbitals to get more accurate answers.

```{note}
Don't think about it too much. The two levels of rigour described below are nowhere near the state of the art, but they will serve for what we need to do. To understand the theory and the choice of orbital basis sets you should enjoy the **computational chemistry course** that is taking place in parallel with this course. We will use *GAMESS* without having a clue what we are doing. Lives are not at stake here.
```

### A Higher Level: HF/3-21G

It took my little laptop computer 0.2 seconds to calculate the final structure and energy of water at the AM1 level. AM1 uses pre-configured functions to enable fast calculations but may not be accurate in all situations (although small neutral molecules should give **excellent results**.)

The **next level** up in mathematical rigour is Hartree-Fock. HF theory attempts to describe the atomic orbitals using mathematical **approximations** but makes no simplifications. It does ignore electron correlation and the Restricted Hartree Fock method (RHF) that we will be using enforces that all electrons are **paired** in molecular orbitals. The math approximations that describe the atomic orbitals use Gaussian functions to model the atomic orbitals. **Gaussian functions** are far easier for a computer to calculate and adding many Gaussians together can get very close to the real answer. The more Gaussians and the more ways they are combined will give better accuracy but will also be more expensive in computer time.

We will use 3-21G, a very low cost basis set and 6-311G(d,p)++, a much more complete and much more expensive basis set in all our work.

We will change the `$BASIS` group in the `water.inp` file to use the 3-21G basis set

```
$BASIS GBASIS=N21 NGAUSS=3 $END
```

We will also cut and paste the final coordinates from the AM1 job. We should always use the work of those who have gone before to advance our goals. We stand on the shoulders of giants. When we work up to very expensive methods, it is best to start with an optimized structure from a cheaper method.

```{code-block} 
---
name: water321G.inp1
linenos: True
lineno-start: 1
emphasize-lines: 3
caption: water321G.inp
---
 $CONTRL SCFTYP=RHF RUNTYP=OPTIMIZE MAXIT=30 MULT=1 ICHARG=0 COORD=UNIQUE $END
 $SYSTEM TIMLIM=525600 MEMORY=1000000 $END
 $BASIS GBASIS=N21 NGAUSS=3 $END
 $SCF DIRSCF=.TRUE. $END
 $STATPT OPTTOL=0.0001 NSTEP=20 $END
 $DATA 
Water 3-21G
CNV 2

O           8.0   0.0000000000   0.0000000000   0.0083001974
H           1.0  -0.7550350900   0.0000000000  -0.5866394549
 $END
```
The **changes** from the original input file have been highlighted in {numref}`water321G.inp1`. Note that the `COORD` parameter has been changed to `UNIQUE`. *GAMESS* reported the *xyz* coordinates of the **symmetry unique atoms** in the previous output file. Since we are now using unique coordinates we must inform the software of that fact. 

I ran the job via the *gms* script.

```
gms water_321G.inp
```

A **result file** named water_321G.log was created. I **searched** for the last occurrence of `NSERCH` and found the results. The job reached a stationary point after five optimization steps. We now have the energy and structure at the HF/3-21G level. {numref}`water321G.log1` is an **excerpt** of the output file.

```{code-block} 
---
name: water321G.log1
linenos: True
lineno-start: 1019
emphasize-lines: 1
caption: water321G.log
---
NSERCH:   5  E=      -75.5859597578  GRAD. MAX=  0.0000143  R.M.S.=  0.0000060


      ***** EQUILIBRIUM GEOMETRY LOCATED *****
 COORDINATES OF SYMMETRY UNIQUE ATOMS (ANGS)
   ATOM   CHARGE       X              Y              Z
 ------------------------------------------------------------
 O           8.0   0.0000000000   0.0000000000  -0.0081020518
 H           1.0  -0.7804697613  -0.0000000000  -0.5784383303
 COORDINATES OF ALL ATOMS ARE (ANGS)
   ATOM   CHARGE       X              Y              Z
 ------------------------------------------------------------
 O           8.0   0.0000000000   0.0000000000  -0.0081020518
 H           1.0   0.7804697613  -0.0000000000  -0.5784383303
 H           1.0  -0.7804697613  -0.0000000000  -0.5784383303

          INTERNUCLEAR DISTANCES (ANGS.)
          ------------------------------

                1 O          2 H          3 H     

   1 O       0.0000000    0.9666522 *  0.9666522 *
   2 H       0.9666522 *  0.0000000    1.5609395 *
   3 H       0.9666522 *  1.5609395 *  0.0000000  
```

The **bond lengths** are slightly longer and the calculated **energy** is very different. We **can’t compare** AM1 energy values to HF because AM1 is a very different method. However we **can compare** HF/3-21G to HF/6-311G(d,p)++. It is the same method, but with a more complete basis set.
 
### More Power: HF/6-311G(d,p)++

By changing the `$BASIS` group to the following we will be implementing the 6-311G(d,p)++ basis set.

```
$BASIS GBASIS=N311 NGAUSS=6 NDFUNC=1 NPFUNC=1 DIFFSP=.TRUE. DIFFS=.TRUE. $END
```

We will use the coordinate data from the 3-21G run to start as **close** to the true answer **as possible**. After running the job with the following input file we reached a stationary point after three optimization steps.

```{code-block} 
---
name: water6311G.inp1
linenos: True
lineno-start: 1
emphasize-lines: 3
caption: water6311G.inp
---
 $CONTRL SCFTYP=RHF RUNTYP=OPTIMIZE MAXIT=30 MULT=1 ICHARG=0 COORD=UNIQUE $END
 $SYSTEM TIMLIM=525600 MEMORY=1000000 $END
 $BASIS GBASIS=N311 NGAUSS=6 NDFUNC=1 NPFUNC=1 DIFFSP=.TRUE. DIFFS=.TRUE. $END
 $SCF DIRSCF=.TRUE. $END
 $STATPT OPTTOL=0.0001 NSTEP=20 $END
 $DATA 
Water 6-311G(d,p)++
CNV 2

 O           8.0   0.0000000000   0.0000000000  -0.0081020518
 H           1.0  -0.7804697613  -0.0000000000  -0.5784383303
 $END
```

Here is an excerpt from the output file.

```{code-block} 
---
name: water6311G.log1
linenos: True
lineno-start: 1345
emphasize-lines: 1
caption: water6311G.log
---
NSERCH:   5  E=      -76.0534461703  GRAD. MAX=  0.0000111  R.M.S.=  0.0000051


      ***** EQUILIBRIUM GEOMETRY LOCATED *****
 COORDINATES OF SYMMETRY UNIQUE ATOMS (ANGS)
   ATOM   CHARGE       X              Y              Z
 ------------------------------------------------------------
 O           8.0   0.0000000000   0.0000000000  -0.0116217188
 H           1.0  -0.7527830929  -0.0000000000  -0.5766784968
 COORDINATES OF ALL ATOMS ARE (ANGS)
   ATOM   CHARGE       X              Y              Z
 ------------------------------------------------------------
 O           8.0   0.0000000000   0.0000000000  -0.0116217188
 H           1.0   0.7527830929  -0.0000000000  -0.5766784968
 H           1.0  -0.7527830929  -0.0000000000  -0.5766784968

          INTERNUCLEAR DISTANCES (ANGS.)
          ------------------------------

                1 O          2 H          3 H     

   1 O       0.0000000    0.9412606 *  0.9412606 *
   2 H       0.9412606 *  0.0000000    1.5055662 *
   3 H       0.9412606 *  1.5055662 *  0.0000000  
```

The HF/6311G(d,p)++ energy was -76.0534 Hartrees whereas the HF/3-21G energy was -75.5860 Hartrees. **Higher** levels of theory will give **lower** energy values.  The bond length is also now shorter; is that closer to the truth?

```{note}
In general, a calculated energy is always higher that the “true” energy. Only a perfect basis set that includes an exact model for the atomic orbitals will give the lowest value possible, the truth. Nothing is perfect, but we can get close if we take the time to run more expensive methods and basis sets.
```

If we **calculate** the HF/6-311G(d,p)++ energy **using** the HF/3-21G optimized structure, we get an energy value of -76.0520 Hartrees. The HF/3-21G structure has an HF/6-311G(d,p)++ energy that is very close to the energy of the HF/6-311G(d,p)++ optimized structure. Perhaps we can use **cheaper** methods to calculate optimized structures and then **more expensive** methods for single point energy calculations. Quite often, stationary points are very similar between different levels of theory because we are dealing with relative energies and the bottom of the energy well is in the almost the same location, even if the absolute energy is not accurate. With more complex systems, such as transition states, we may need to optimize structure at higher levels of theory for accuracy.

## Units

Hartrees? You may notice that data tables in the output file report energy in **Hartree units**, distances in both **Angstroms** and **Bohr atomic units** and angles in degrees and in radians. Deep inside *GAMESS*, the math uses Bohr a.u. for distance and radians for angles in its calculations. It also uses the elementary charge and mass of the electron and Planck’s constant. The Hartree is an energy unit derived from the **fundamental** measurements of a hydrogen atom and the intrinsic properties of space and time. 

*GAMESS* will output distances and angles in **familiar** units such as Angstroms and degrees but will always report energy in Hartrees. One Hartree is 4.3597 &times; 10<sup>−18</sup> *J*. When we multiply by Avogadro’s number we get 2625.50 *kJ/mole*.

```{note}
Keep this conversion factor close by: 1 Hartree = 2,625.5 *kJ/mole*.
```

## Internal Coordinates

For many of our exercises, we will be building molecules using **internal coordinates**. These coordinates define atomic positions relative the first atom defined in list. This list is called the *Z-matrix*. A **Z-matrix** is a defined format for creating these internal coordinates. 

Imagine three towns in a flat prairie, the last three towns on Earth. If I start at town A and travel 10 miles to town B, turn 45˚ left and travel 5 miles to town C, then I can place the towns exactly. I will know the distance between A and C and all other angles from those first three coordinates.

Here is a Z-matrix for our town map…

```
A
B  1  10
C  2   5  1  45
```
It can be interpreted as…

| Line | Notes |
| :---- | :---- |
| Line 1 |	Town A is declared to **exist** |
| Line 2 |	Town B is connected to line 1 by a **distance** of 10 miles |
| Line 3 |	Town C is connected to line 2 by a **distance** of 5 miles \& the **angle** through line 2 to line 1 is 45˚|
 
### The *Z-matrix* with Water

Here is a *Z-matrix* for the molecule water. It is interpreted in {numref}`fig3`

```
Water
CNV 2

H
O  1  1.0
H  2  1.0  1  109.5
```

```{figure} images/Zmatrix.png
---
width: 600px
name: fig3
---
*Parsing the *Z-matrix* for water*
```

*GAMESS* will **attempt** to fit the molecule to your declared symmetry point group and define a principal axis, etc. However, if your initial structure does not fit the point group the calculation will **fail**. To fit the *C<sub>2v</sun>* point group, the two bond lengths must be the same in the *Z-matrix* for water. One way that we can make sure that this is true is to use **variables** in the Z-matrix. Consider the example below.

```
Water
CNV 2

H
O  1  bond_length
H  2  bond_length  1  bond_angle

bond_length=1.0
bond_angle=109.5
```

By using variables appropriately we can **make sure** that certain values are always identical, as required in a given point group. However, sometime we must be creative to enforce symmetry in a *Z-matrix*. {numref}`water_Z_AM1.inp1` shows the complete input file for an AM1 optimization of water using the Z-matrix.

```{code-block} 
---
name: water_Z_AM1.inp1
linenos: True
lineno-start: 1
emphasize-lines: 1
caption: water_Z_AM1.inp
---
 $CONTRL SCFTYP=RHF RUNTYP=OPTIMIZE MAXIT=30 MULT=1 ICHARG=0 COORD=ZMT $END
 $SYSTEM TIMLIM=525600 MEMORY=1000000 $END
 $BASIS GBASIS=AM1 $END
 $SCF DIRSCF=.TRUE. $END
 $STATPT OPTTOL=0.0001 NSTEP=100 $END
 $DATA 
Water
CNV 2

H
O  1  1.0
H  2  1.0  1  109.5
 $END
```

We see the *Z-matrix* used for the atomic coordinates in the `$DATA` group and we also see that the `COORD=CART` has been changed to `COORD=ZMT`.

When we submit the job, *GAMESS* will use the *Z-matrix* to create a set of Cartesian coordinates for the actual calculation. It will then attempt to identify the **primary axis** and apply the symmetry point group to create a set of **unique Cartesian coordinates**. It will then optimize the coordinates and, when a stationary point is reached, it will output the *xyz* coordinates, the unique coordinates and the new *Z-matrix*.

The *Z-matrix* is useful because we can **see** directly the **bond lengths and angles** in the result. We will not have to use trigonometry to calculate the bond angle from the *xyz* data. In the excerpt from the result file shown below, we see that we reached an **optimized** geometry after 3 steps and that the AM1 Bond lengths were calculated to be 0.961 Å and the bond angle to be 103.5˚. Note that *GAMESS* oriented the water molecule in the *xz* plane, as expected, but that it has the molecule **upside-down** compared to our original Cartesian input file described above. Interesting.

```{code-block} 
---
name: water_Z_AM1.log1
linenos: True
lineno-start: 976
emphasize-lines: 1
caption: water_Z_AM1.log
---
NSERCH:   6  E=      -12.8093121220  GRAD. MAX=  0.0000047  R.M.S.=  0.0000020


      ***** EQUILIBRIUM GEOMETRY LOCATED *****
 COORDINATES OF SYMMETRY UNIQUE ATOMS (ANGS)
   ATOM   CHARGE       X              Y              Z
 ------------------------------------------------------------
 H           1.0  -0.7550622398   0.0000000000   0.5184764054
 O           8.0  -0.0000000000   0.0000000000  -0.0764358674
 COORDINATES OF ALL ATOMS ARE (ANGS)
   ATOM   CHARGE       X              Y              Z
 ------------------------------------------------------------
 H           1.0   0.7550622398  -0.0000000000   0.5184764054
 H           1.0  -0.7550622398   0.0000000000   0.5184764054
 O           8.0  -0.0000000000   0.0000000000  -0.0764358674

 THE CURRENT FULLY SUBSTITUTED Z-MATRIX IS
 H   
 O      1   0.9612698
 H      2   0.9612698  1   103.5309684
```

We could now paste the new *Z-matrix* or the unique coordinates into the HF/3-21G and the HF/6-311(d,p)++ input files and **carry on** optimizing the structure at **higher** levels of theory. We should get identical structures and energies because the molecule is the **same** no matter which coordinate system that we used to describe it.

### The Z-Matrix for Ammonia

Water is a planar system (for the atoms) but **ammonia** is going to require a **third dimension**. Here is one option for the *Z-matrix*.

```
Ammonia
CNV 3

N
H   1   1.0
H   1   1.0   2   109.5
H   1   1.0   3   109.5   2   120
```

This describes the *Z-matrix* as shown parsed in {numref}`fig4`

```{figure} images/Zmatrix_Ammonia.png
---
width: 800px
name: fig4
---
*A Z-matrix for ammonia*
```

But when I submit the job with the above the **calculation failed**. Near the end of the short result file that was produced was the following text message.

```
ERROR!
 YOUR CART/ZMT/ZMTMPC INPUT GENERATED 12 ATOMS,
 BUT ONLY 4 ATOMS WERE PRESENT IN YOUR $DATA.
 THIS MEANS THERE IS A MISTAKE IN YOUR COORDINATES,
 OR YOUR CHOICE OF GROUP. ADIOS, MY FRIEND!!
```

Although the *Z-matrix* will create a structure that looks a lot like ammonia, the three **bond angles** between H and N will not all be identical as the *Z-matrix* is converted to Cartesian coordinates. We defined the 3,1,2 and the 4,1,2 angles as 109.5˚, However we did not define the 4,1,3 bond angle. It will be the result of **positioning** the atoms according to the *Z-matrix* (1.0 Å from the nitrogen, 109.5˚ from the 2,1 bond and 120˚ from the 1,2,3 plane.) This should give us the correct structure. However, after the math is done that third 4,1,3 bond angle is **not exactly the same** as the stated 4,1,2 and 3,1,2 angles. As a result, *GAMESS* could not determine the correct primary axis because the structure was not an exact fit to *C<sub>3v</sub>* symmetry.

There is another way.

### Dummy Atoms in the Z-Matrix

When constructing symmetrical molecules it can be useful to use **dummy atoms**. These are defined by the letter X in the *Z-matrix*.

```{code-block} 
---
name: ammonia_ZX.inp1
linenos: True
lineno-start: 1
emphasize-lines: 
caption: ammonia_ZX.inp
---
 $CONTRL SCFTYP=RHF RUNTYP=OPTIMIZE MAXIT=30 MULT=1 ICHARG=0 COORD=ZMT $END
 $SYSTEM TIMLIM=525600 MEMORY=1000000 $END
 $BASIS GBASIS=AM1 $END
 $SCF DIRSCF=.TRUE. $END
 $STATPT OPTTOL=0.0001 NSTEP=100 $END
 $DATA 
Ammonia
CNV 3

X
N  1  1.0
H  2  1.0  1  109.5
H  2  1.0  1  109.5  3  +120.0
H  2  1.0  1  109.5  3  -120.0
 $END
```

Using this matrix gives a **successful** calculation for the optimized geometry of ammonia at the AM1 level. The *Z-matrix* is outlined in {numref}`fig4` and the input file is described in {numref}`ammonia_ZX.inp1`.

```{figure} images/Dummy_Atoms.png
---
width: 800px
name: fig5
---
*The Z-matrix for ammonia with a dummy atom to define symmetry*
```

{numref}`ammonia_ZX.log1` is an **excerpt** from the result file. You will see that the *Z-matrix* was **not recreated**.  This is because the **dummy atom** was used and *GAMESS* does not want to include it, yet it **cannot create** a *Z-matrix* that is guaranteed to fit the *C<sub>2v</sub>* symmetry without it. So it is sticking with Cartesian coordinates.

```{code-block} 
---
name: ammonia_ZX.log1
linenos: True
lineno-start: 783
emphasize-lines: 
caption: ammonia_ZX.log
---
NSERCH:   4  E=       -9.1354556208  GRAD. MAX=  0.0000006  R.M.S.=  0.0000004


      ***** EQUILIBRIUM GEOMETRY LOCATED *****
 COORDINATES OF SYMMETRY UNIQUE ATOMS (ANGS)
   ATOM   CHARGE       X              Y              Z
 ------------------------------------------------------------
 N           7.0   0.0000000000   0.0000000000  -0.0630644261
 H           1.0   0.9385359335   0.0000000000   0.2757943561
 COORDINATES OF ALL ATOMS ARE (ANGS)
   ATOM   CHARGE       X              Y              Z
 ------------------------------------------------------------
 N           7.0   0.0000000000   0.0000000000  -0.0630644261
 H           1.0  -0.4692679667   0.8127959607   0.2757943561
 H           1.0  -0.4692679667  -0.8127959607   0.2757943561
 H           1.0   0.9385359335   0.0000000000   0.2757943561

          INTERNUCLEAR DISTANCES (ANGS.)
          ------------------------------

                1 N          2 H          3 H          4 H     

   1 N       0.0000000    0.9978351 *  0.9978351 *  0.9978351 *
   2 H       0.9978351 *  0.0000000    1.6255919 *  1.6255919 *
   3 H       0.9978351 *  1.6255919 *  0.0000000    1.6255919 *
   4 H       0.9978351 *  1.6255919 *  1.6255919 *  0.0000000  
```

We can see that the AM1 bond **distances** we optimized at 0.998 Å. But we cannot easily see the H–N–H bond **angles**.

### The \$ZMAT Group

The above job essentially just **converted** the *Z-matrix* with a dummy atom to unique cartesian coordinates for us. We can now use these Cartesian coordinates and ask *GAMESS* to **keep track** of the internal coordinates. We will create a new input file using the unique coordinates that were just generated by *GAMESS*.  

We will perform the AM1 calculation **again** now with internal coordinates **declared** via a `$ZMAT` group. The `$ZMAT` group can be used to establish information about internal coordinates. Even if we submit the structure via Cartesian coordinates we can still have *GAMESS* use the internal coordinates of **our choice** . We no longer have a dummy atom, just the four atoms in NH<sub>3</sub>. Recall the original *Z-matrix* for ammonia that we built above. We can use those coordinates for our current calculation. 

We must **declare** that we are using internal coordinates in the `$CONTRL` group by specifying **how many** will be use. We will add `$NZVAR=6` to that group. There is a coordinate for each **degree of freedom** in a molecule. That is 3n-6. (3n-5 for linear molecules). For the four atoms of ammonia that is 3(4)-6 = 6 coordinates. 
 
We will then construct the `$ZMAT` group as follows…

```
$ZMAT IZMAT(1)=1,2,1,  
               1,3,1,  2,3,1,2, 
               1,4,1,  2,4,1,2,  3,4,1,2,3   $END  
```

The `IZMAT` matrix is populated by a series of numbers. Each **group** starts with a number and then is followed by the expected atom numbers. Here is how the `IZMAT` coordinates are declared.

- 1 indicates a **bond length** and is followed by the two atoms involved. e.g. 1,2,1 is a coordinate for the bond length between atoms 2 and 1.
- 2 indicates a **bond angle** and is followed by the three atoms involved. The central atom is the vertex. e.g. 2,3,1,2 is the bond angle between bonds 3,1 and 1,2.
- 3 indicates a **torsion** and is followed by the four atoms involved. e.g. 3,4,1,2,3 is the angle between the planes defined by atoms 4,1,2 and 1,2,3.

This would **correspond** to the failed *Z-matrix* that we used before we applied the dummy atoms. It is reproduced below.

```
N
H   1   1.0
H   1   1.0   2   109.5
H   1   1.0   2   109.5   3   120
```

Now *GAMESS* will **track** those coordinates. In fact, *GAMESS* will be using those coordinates to calculate **gradients**. Rather than a gradient in each axis for each atom, *GAMESS* will use the gradient for the energy function of that coordinate. With **carefully designed** internal coordinates, this can speed the calculation quite a bit. Below is the input file for an AM1 optimization using the results from the previous AM1 job.

```{code-block} 
---
name: ammonia_UZ.inp1
linenos: True
lineno-start: 1
emphasize-lines: 2,14-16
caption: ammonia_UZ.inp
---
 $CONTRL SCFTYP=RHF RUNTYP=OPTIMIZE MAXIT=30 MULT=1 ICHARG=0 
  COORD=UNIQUE NZVAR=6 $END
 $SYSTEM TIMLIM=525600 MEMORY=1000000 $END
 $BASIS GBASIS=AM1 $END
 $SCF DIRSCF=.TRUE. $END
 $STATPT OPTTOL=0.0001 NSTEP=100 $END
 $DATA 
Ammonia
CNV 3

N  7.0   0.0            0.0  -0.0630644261
H  1.0   0.9385359335   0.0   0.2757943561
 $END
 $ZMAT IZMAT(1)=1,2,1,  
                1,3,1,  2,3,1,2, 
                1,4,1,  2,4,1,2,  3,4,1,2,3   $END   
```

```{tip}
Observe that the `$CONTRL` group is split over two lines in this example. The single line was more than 80 columns and no characters after that will be read into the system. We can have as many new lines as we want. The group is terminated by the `$END` string, not the end of a line.
```

Take note of the **list** of internal coordinates that was written out by *GAMESS*. Each is **classified** as a STRETCH, BEND or TORSION. This **corresponds** to the 1, 2 and 3 that we used to set up each coordinate. The 4,1,2,3 torsion is not 120˚ like we had set up earlier. This is why the *Z-matrix* failed when we enforced *C<sub>3v</sub>* symmetry.

Since the `$DATA` group was copied from the result of the **same** AM1 method, we started at a stationary point and so no optimization was performed. What is **different** is that *GAMESS* now includes the list of internal coordinates with the structural data. We can easily **see the values** for all the lengths and angles.

```{code-block} 
---
name: ammonia_UZ.log1
linenos: True
lineno-start: 484
emphasize-lines: 1,31
caption: ammonia_UZ.log
---
NSERCH:   0  E=       -9.1354556208  GRAD. MAX=  0.0000009  R.M.S.=  0.0000004


      ***** EQUILIBRIUM GEOMETRY LOCATED *****
 COORDINATES OF SYMMETRY UNIQUE ATOMS (ANGS)
   ATOM   CHARGE       X              Y              Z
 ------------------------------------------------------------
 N           7.0   0.0000000000   0.0000000000  -0.0630644261
 H           1.0   0.9385359335   0.0000000000   0.2757943561
 COORDINATES OF ALL ATOMS ARE (ANGS)
   ATOM   CHARGE       X              Y              Z
 ------------------------------------------------------------
 N           7.0   0.0000000000   0.0000000000  -0.0630644261
 H           1.0  -0.4692679668   0.8127959608   0.2757943561
 H           1.0  -0.4692679668  -0.8127959608   0.2757943561
 H           1.0   0.9385359335   0.0000000000   0.2757943561


                     --------------------
                     INTERNAL COORDINATES
                     --------------------

                 - - ATOMS - -         COORDINATE      COORDINATE
 NO.   TYPE    I  J  K  L  M  N        (BOHR,RAD)       (ANG,DEG)
 ----------------------------------------------------------------
   1 STRETCH   2  1                     1.8856350       0.9978351
   2 STRETCH   3  1                     1.8856350       0.9978351
   3 BEND      3  1  2                  1.9039384     109.0876324
   4 STRETCH   4  1                     1.8856350       0.9978351
   5 BEND      4  1  2                  1.9039384     109.0876324
   6 TORSION   4  1  2  3              -2.0782059    -119.0724272
```

We observe that the bond lengths are all **exactly** the same and the bond angles are also **exactly** the same. AM1 bond lengths and angles are 1.00 Å and 109.1˚

We can take the result of the AM1 calculation and use it to build an **input file** for HF/3-21G and HF/6-3111G(d,p)++ optimizations. Below is a file for the **more expensive** option.

```{code-block} 
---
name: ammonia_UZ_6311G.inp1
linenos: True
lineno-start: 1
emphasize-lines: 
caption: ammonia_UZ_6311G.inp
---
 $CONTRL SCFTYP=RHF RUNTYP=OPTIMIZE MAXIT=30 MULT=1 ICHARG=0 
  COORD=UNIQUE NZVAR=6 $END
 $SYSTEM TIMLIM=525600 MEMORY=1000000 $END
 $BASIS GBASIS=N311 NGAUSS=6 NDFUNC=1 NPFUNC=1 DIFFSP=.TRUE. DIFFS=.TRUE. $END
 $SCF DIRSCF=.TRUE. $END
 $STATPT OPTTOL=0.0001 NSTEP=100 $END
 $DATA 
Ammonia
CNV 3

N   7.0   0.0            0.0  -0.0630644261
H   1.0   0.9385359335   0.0   0.2757943561
 $END
 $ZMAT IZMAT(1)=1,2,1,  
                1,3,1,  2,3,1,2, 
                1,4,1,  2,4,1,2,  
                        2,4,1,3   $END  
```

In the above input file, I set up the `$IZMAT` matrix differently and applied a bend rather than a torsion for the last coordinate. This way I have coordinates that describe all three bond lengths and all three bends. I can do this because the torsion angles are set by the symmetry group (spaced evenly around the principal axis.) Now see how that is reflected in the results. An excerpt from the result file is shown below.


```{code-block} 
---
name: ammonia_UZ_6311G.log1
linenos: True
lineno-start: 1448
emphasize-lines: 
caption: ammonia_UZ_6311G.log
---
NSERCH:   3  E=      -56.2147746439  GRAD. MAX=  0.0000023  R.M.S.=  0.0000013


      ***** EQUILIBRIUM GEOMETRY LOCATED *****
 COORDINATES OF SYMMETRY UNIQUE ATOMS (ANGS)
   ATOM   CHARGE       X              Y              Z
 ------------------------------------------------------------
 N           7.0   0.0000000000   0.0000000000  -0.0652973431
 H           1.0   0.9365806163   0.0000000000   0.2861359970
 COORDINATES OF ALL ATOMS ARE (ANGS)
   ATOM   CHARGE       X              Y              Z
 ------------------------------------------------------------
 N           7.0   0.0000000000   0.0000000000  -0.0652973431
 H           1.0  -0.4682903082   0.8111026064   0.2861359970
 H           1.0  -0.4682903082  -0.8111026064   0.2861359970
 H           1.0   0.9365806163   0.0000000000   0.2861359970


                     --------------------
                     INTERNAL COORDINATES
                     --------------------

                 - - ATOMS - -         COORDINATE      COORDINATE
 NO.   TYPE    I  J  K  L  M  N        (BOHR,RAD)       (ANG,DEG)
 ----------------------------------------------------------------
   1 STRETCH   2  1                     1.8903765       1.0003443
   2 STRETCH   3  1                     1.8903765       1.0003443
   3 BEND      3  1  2                  1.8911154     108.3529298
   4 STRETCH   4  1                     1.8903765       1.0003443
   5 BEND      4  1  2                  1.8911154     108.3529298
   6 BEND      4  1  3                  1.8911154     108.3529298 
```

Now we see the HF/6311(d,p)++ results have bond **lengths** of 1.00 Å and bond **angles** of 108.4˚.

## Summary

We have explored using *GAMESS* to **calculate** the structure and energy of some small molecules. We tried using **Cartesian coordinates** to describe the initial structure and using **internal coordinates** with the *Z-matrix*. We have used **symmetry** to simplify the structure to the **unique Cartesian coordinates** needed to describe the structure in a **point group**.

We have run *GAMESS* using text input files that we created and submitting the jobs via the *gms* script from the **command line**.

We have used the `$ZMAT` group to **establish internal coordinates** when using Cartesian coordinates so that bond lengths and angles can be easily **interpreted directly** from the text result file. We have examined the **text output** and determined that the results were as expected.

Now go to the instructions for the exercise that this discussion supports and explore *GAMESS* for yourself.

## Files

The following files were created during this tutorial and are available with this document. Feel free to use them as templates and cut and paste as you build the other calculations.

| Filename | Notes |
| :---- | :---- |
|water_AM1_C.inp	| The initial input for an AM1 optimization file demonstrating creating a starting structure for water with Cartesian coordinates. |
|water_AM1_Z.inp	| An input file for an AM1 optimization using a Z-matrix for water |
|water_AM1_U.inp	| An input file using the unique coordinates that resulted from the initial calculation with either of the two previous input files. |
|water_321_U.inp	| An input file for an HF/3-21G optimization |
|water_6311_U.inp	| An input file for an HF/6-311G(d,p)++ optimization |
|water_6311_U_E.inp	| An input file for an HF/6-311G(d,p)++ single point energy calculation. |

## Exercise

Read the accompanying introduction to *GAMESS*, "Getting Started with Small Molecules", and then try the following exercises.

### The Activity

**Write** an input file for the tetrahedral methane molecule. **Use** the *T<sub>d</sub>* point group with a *Z-matrix* for the first attempt. Look to the ammonia *Z-matrix* with the dummy atom for inspiration. **Run** the job on your computer. If you are successful, you will have accomplished the first four of our learning goals. If it was not successful, **try another way** to build the molecule so that it fits *T<sub>d</sub>* symmetry. Perhaps a different construction of the *Z-matrix* or a set of cartesian coordinates would work. Errors are learning opportunities. Give yourself time to make lots of them.

After you get it working, copy the coordinate data into **higher** level input files and **optimize** for HF/3-21G and HF/6-311(d,p)++ levels of theory.

If you use the optimized *Z-matrix* (no dummy atoms were needed for methane) then you will have a *Z-matrix* in the results from which you can locate **bond lengths and angles**. If you prefer the unique coordinates you can set up a `$ZMAT` group to get those value directly from the output.

What are the bond lengths and angles for **methane** at the three levels of theory? Perform HF/6311(d,p)++ energy calculation using the optimized coordinates from the results for all three levels of theory. How do they **compare**? Which had the lowest energy (and was therefore the most accurate of the three structures)?

Using the input files in this document **repeat** the above for water and ammonia. **Compare** the bond angles and bond lengths for the most accurate structures in each case.

### The Report

**Create** a ONE PAGE document summarizing your **results** (energies, bond lengths and angles for methane) in a table.  Do the results fit with what you know about VSEPR theory?

In the table, **report** the energies for AM1/HF/6-311(d,p)++ (optimized at AM1, energy calculated at HF/6-311(d,p)++), HF/3-21G/6-311(d,p)++ and HF/6-311(d,p)++ for each of the three molecules. The lowest energy should be the most accurate. Which was it in each case?

**Comment** on how you did all this in a completely text-based world. Did you miss **visualizing** the molecules in 3-D graphics?  More complicated molecules could benefit from using visual molecule building/display programs. But, when you really want to control symmetry, it is best to manually create the input file.

```{warning}
Remember that the visualization programs work for the machines. Sometimes you must look at the real world in its **raw text** format.
```

Include an appendix with the text for all the input files that you used. (Please do not include any result files – there will be no trees left!) Preface each with the file name and a note on its purpose and use a fixed-width font.

## Example Exercise Report

### Methane Calculations

The input file was created using unique Cartesian coordinates because the Z-matrix conversion by *GAMESS* failed to achieve $T_d$ symmetry. (Bond angles of 109.5˚ did not fit the definition of Td. They should be 109.4712206˚.)  Once that problem was solved the geometry was calculated at AM1, HF/3-21G and HF/6-311G(d,p)++ levels. Then the energy was calculated at HF/6-311G(d,p)++ for all three structures. 

#### Methane Data

| Optimization	  | C–H length (Å)|  H–C–H angle	  |  HF/6-311G(d,p)++ Energy           | ∆E (kJ/mole)  |
| :-------------- | :------------ |  :--------------  |  :--------------                   | :-----------  |
| AM1	          | 1.1119128	  |  109.4712206	  |  –40.2072033858	                   | +5.16         |
| HF/3-21G	      | 1.0829028	  |  109.4712206	  |  –40.2091641123	                   | +0.0133       |
| HF/6-311(d,p)++ | 1.0829125	  |  109.4712206	  |  –40.2091691920	                   | 0             |
| Experimental 	  | 1.087	      |  109.471	      |  -40.2091492019	                   | +0.052        |

Experimental results are from the [Computational Chemistry Benchmark DataBase](https://cccbdb.nist.gov)

#### Commentary

The HF/3-21G optimization produced a structure that is very close to the HF/6-311G(d,p)++ optimized structure and the energy was calculated to be very similar as well. The AM1 structure and energy was farther away.

#### Appendix: Input files


```{code-block} 
---
name: methane_AM1_U.inp
linenos: True
lineno-start: 1
emphasize-lines: 
caption: methane_AM1_U.inp
---
 $CONTRL SCFTYP=RHF RUNTYP=OPTIMIZE MAXIT=30 MULT=1 NZVAR=9 $END
 $SYSTEM TIMLIM=525600 MEMORY=1000000 $END
 $BASIS GBASIS=AM1 $END
 $SCF DIRSCF=.TRUE. $END
 $STATPT OPTTOL=0.0001 NSTEP=100 $END
 $DATA 
Methane
Td

C     6.0     0.0    0.0     0.0
H     1.0     0.7    0.7     0.7
 $END
 $ZMAT IZMAT(1)= 1,2,1
                 1,3,1,  2,3,1,2
                 1,4,1,  2,4,1,3,  3,4,1,3,2
                 1,5,1,  2,5,1,4,  3,5,1,4,3
                 $END
```

```{code-block} 
---
name: methane_321_U.inp
linenos: True
lineno-start: 1
emphasize-lines: 
caption: methane_321_U.inp
---
 $CONTRL SCFTYP=RHF RUNTYP=OPTIMIZE MAXIT=30 MULT=1 ICHARG=0 
 COORD=UNIQUE NZVAR=9 $END
 $SYSTEM TIMLIM=525600 MEMORY=1000000 $END
 $BASIS GBASIS=N21 NGAUSS=3 $END
 $SCF DIRSCF=.TRUE. $END
 $STATPT OPTTOL=0.0001 NSTEP=20 $END
 $DATA 
Methane 321
Td

 C           6.0   0.0000000000   0.0000000000   0.0000000000
 H           1.0   0.6417914104   0.6417914104   0.6417914104
 $END
 $ZMAT IZMAT(1)= 1,2,1
                 1,3,1,  2,3,1,2
                 1,4,1,  2,4,1,3,  3,4,1,3,2
                 1,5,1,  2,5,1,4,  3,5,1,4,3
                 $END
```
 
```{code-block} 
---
name: Methane_6311_U.inp
linenos: True
lineno-start: 1
emphasize-lines: 
caption: Methane_6311_U.inp
---
 $CONTRL SCFTYP=RHF RUNTYP=OPTIMIZE MAXIT=30 MULT=1 ICHARG=0 
  NZVAR=9 COORD=UNIQUE $END
 $SYSTEM TIMLIM=525600 MEMORY=1000000 $END
 $BASIS GBASIS=N311 NGAUSS=6 NDFUNC=1 NPFUNC=1 
  DIFFSP=.TRUE. DIFFS=.TRUE. $END
 $SCF DIRSCF=.TRUE. $END
 $STATPT OPTTOL=0.0001 NSTEP=20 $END
 $DATA 
Methane 6311
Td

 C           6.0   0.0000000000   0.0000000000   0.0000000000
 H           1.0   0.6260053431   0.6260053431   0.6260053431
  $END
 $ZMAT IZMAT(1)= 1,2,1
                 1,3,1,  2,3,1,2
                 1,4,1,  2,4,1,3,  3,4,1,3,2
                 1,5,1,  2,5,1,4,  3,5,1,4,3
                 $END
```

```{code-block} 
---
name: Methane_6311_U_E.inp
linenos: True
lineno-start: 1
emphasize-lines: 
caption: Methane_6311_U_E.inp
---
 $CONTRL SCFTYP=RHF RUNTYP=ENERGY MAXIT=30 MULT=1 ICHARG=0 
  NZVAR=9 COORD=UNIQUE $END
 $SYSTEM TIMLIM=525600 MEMORY=1000000 $END
 $BASIS GBASIS=N311 NGAUSS=6 NDFUNC=1 NPFUNC=1 
  DIFFSP=.TRUE. DIFFS=.TRUE. $END
 $SCF DIRSCF=.TRUE. $END
 $STATPT OPTTOL=0.0001 NSTEP=20 $END
 $DATA 
Methane 6311
Td

 C           6.0   0.0000000000   0.0000000000   0.0000000000
 H           1.0   0.6260053431   0.6260053431   0.6260053431
  $END
 $ZMAT IZMAT(1)= 1,2,1
                 1,3,1,  2,3,1,2
                 1,4,1,  2,4,1,3,  3,4,1,3,2
                 1,5,1,  2,5,1,4,  3,5,1,4,3
                 $END
```

Paste in coordinates for the results of the AM1 and 3-21G calculations after running this file.
 
The below file was made to check the energy of the experimental structure. Even with many decimal places, *GAMESS* still did not recognize the symmetry of the structure. So I used C1 symmetry instead. Note that there is NO BLANK LINE after the C1 symmetry designation. 

```{code-block} 
---
name: Methane_6311_Z_E.inp
linenos: True
lineno-start: 1
emphasize-lines: 
caption: Methane_6311_Z_E.inp
---
 $CONTRL SCFTYP=RHF RUNTYP=ENERGY MAXIT=30 MULT=1 ICHARG=0 COORD=ZMT $END
 $SYSTEM TIMLIM=525600 MEMORY=1000000 $END
 $BASIS GBASIS=N311 NGAUSS=6 NDFUNC=1 NPFUNC=1 DIFFSP=.TRUE. DIFFS=.TRUE. $END
 $SCF DIRSCF=.TRUE. $END
 $STATPT OPTTOL=0.0001 NSTEP=100 $END
 $DATA 
Methane
C1
H
C  1  1.087
H  2  1.087  1  109.4712206
H  2  1.087  1  109.4712206  3  +120.0
H  2  1.087  1  109.4712206  3  -120.0
 $END
```
 
### Water Calculations

The first input file was created a Z-matrix and the geometry was calculated at AM1, HF/3-21G and HF/6-311G(d,p)++ levels. Then the energy was calculated at HF/6-311G(d,p)++ for all three structures.

#### Water Data
| Optimization	  | O–H length (Å)|  H–O–H angle	   |  HF/6-311G(d,p)++ Energy    | ∆E (kJ/mole)  |
| :-------------- | :------------ |   :--------------  |  :--------------            | :-----------  |
| AM1	          |   0.9613152	  |  103.5345005	   | -76.0524943643	             |      +2.49    |
| HF/3-21G	      |   0.9666698   |  107.6785306	   | -76.0519604402	             |      +3.89    |
| HF/6-311(d,p)++ |   0.9412543   |  106.2149647	   | -76.0534461704	             |       0       |
| experimental 	  |   0.958       |  104.48		       | -76.0528152807              |      +1.65    |

#### Commentary

The HF/3-21G optimization produced a structure that is very close to the HF/6-311G(d,p)++ optimized structure and the energy was calculated to be very similar as well. The AM1 structure and energy seems closer, but not by much.

#### Appendix: Input files

```{code-block} 
---
name: water_AM1_U.inp
linenos: True
lineno-start: 1
emphasize-lines: 
caption: water_AM1_U.inp
---
 $CONTRL SCFTYP=RHF RUNTYP=OPTIMIZE MAXIT=30 MULT=1 ICHARG=0 
  COORD=ZMT NZVAR=3 $END
 $SYSTEM TIMLIM=525600 MEMORY=1000000 $END
 $BASIS GBASIS=AM1 $END
 $SCF DIRSCF=.TRUE. $END
 $STATPT OPTTOL=0.0001 NSTEP=100 $END
 $DATA 
Water
CNV 2

O
H  1  1.0
H  1  1.0  2  109.5
 $END
 $ZMAT IZMAT(1)=1,2,1,
                1,3,1,  2,3,1,2
                $END
```

### Ammonia Calculations

The first input file was created a Z-matrix and the geometry was calculated at AM1, HF/3-21G and HF/6-311G(d,p)++ levels. Then the energy was calculated at HF/6-311G(d,p)++ for all three structures.

#### Ammonia Data

| Optimization	  | N–H length (Å)|  H–N–H angle	   |  HF/6-311G(d,p)++ Energy    | ∆E (kJ/mole)  |
| :-------------- | :------------ |   :--------------  |  :--------------            | :-----------  |
| AM1             |  0.9978605    |   109.0887396      |  -56.2147354804             |  +0.103       |
| HF/3-21G        |  1.0025827    |   112.3967370      |  -56.2137244548             |  +2.73        |
| HF/6-311(d,p)++ |  1.0003408    |   108.3541849      |  -56.2147746437             |   0           |
| experimental    |  1.0124       |   106.67           |  -56.2143301556             |  +1.17        |

#### Commentary
The HF/3-21G optimization produced a structure that is NOT close to the HF/6-311G(d,p)++ optimized structure. The AM1 structure and energy seems closer, but not by much. The HF/6-311(d,p)++ seems to have given the most accurate structure compared to the experimental data.
 
#### Appendix: Input files

```{code-block} 
---
name: ammonia_AM1_ZD.inp
linenos: True
lineno-start: 1
emphasize-lines: 
caption: ammonia_AM1_ZD.inp
---
 $CONTRL SCFTYP=RHF RUNTYP=OPTIMIZE MAXIT=30 MULT=1 ICHARG=0 
  COORD=ZMT NZVAR=6 $END
 $SYSTEM TIMLIM=525600 MEMORY=1000000 $END
 $BASIS GBASIS=AM1 $END
 $SCF DIRSCF=.TRUE. $END
 $STATPT OPTTOL=0.0001 NSTEP=100 $END
 $DATA 
Ammonia AM1
CNV 3

X
N  1  1.0
H  2  1.0  1  109.5
H  2  1.0  1  109.5  3  +120.0
H  2  1.0  1  109.5  3  -120.0
 $END
! NOTE: Pretend dummy atom does not exist when numbers the IZMAT matrix 
 $ZMAT IZMAT(1)=1,2,1,  
                1,3,1,  2,3,1,2, 
                1,4,1,  2,4,1,2,  3,4,1,2,3   $END  
```

```{code-block} 
---
name: ammonia_321_U.inp
linenos: True
lineno-start: 1
emphasize-lines: 
caption: ammonia_321_U.inp
---
 $CONTRL SCFTYP=RHF RUNTYP=OPTIMIZE MAXIT=30 MULT=1 ICHARG=0 
  COORD=UNIQUE NZVAR=6 $END
 $SYSTEM TIMLIM=525600 MEMORY=1000000 $END
 $BASIS GBASIS=N21 NGAUSS=3 $END
 $SCF DIRSCF=.TRUE. $END
 $STATPT OPTTOL=0.0001 NSTEP=20 $END
 $DATA 
Ammonia 3-21G
CNV 3

 N           7.0  -0.0000000000  -0.0000000000  -0.0601709286
 H           1.0   0.9385662553   0.0000000000   0.2786785817
 $END
 $ZMAT IZMAT(1)=1,2,1,  
                1,3,1,  2,3,1,2, 
                1,4,1,  2,4,1,2,  3,4,1,2,3   $END  
```
 
```{code-block} 
---
name: ammonia_6311_U.inp
linenos: True
lineno-start: 1
emphasize-lines: 
caption: ammonia_6311_U.inp
---
 $CONTRL SCFTYP=RHF RUNTYP=OPTIMIZE MAXIT=30 MULT=1 ICHARG=0 
  COORD=UNIQUE NZVAR=6 $END
 $SYSTEM TIMLIM=525600 MEMORY=1000000 $END
 $BASIS GBASIS=N311 NGAUSS=6 NDFUNC=1 NPFUNC=1 DIFFSP=.TRUE. DIFFS=.TRUE. $END
 $SCF DIRSCF=.TRUE. $END
 $STATPT OPTTOL=0.0001 NSTEP=20 $END
 $DATA 
Ammonia 6-311G(d,p)++
CNV 3

 N           7.0   0.0000000000   0.0000000000  -0.0501412961
 H           1.0   0.9619980493   0.0000000000   0.2322268510
 $END
 $ZMAT IZMAT(1)=1,2,1,  
                1,3,1,  2,3,1,2, 
                1,4,1,  2,4,1,2,  3,4,1,2,3   $END  
```

```{code-block} 
---
name: ammonia_6311_U_E.inp
linenos: True
lineno-start: 1
emphasize-lines: 
caption: ammonia_6311_U_E.inp
---
 $CONTRL SCFTYP=RHF RUNTYP=ENERGY MAXIT=30 MULT=1 ICHARG=0 
  COORD=UNIQUE NZVAR=6 $END
 $SYSTEM TIMLIM=525600 MEMORY=1000000 $END
 $BASIS GBASIS=N311 NGAUSS=6 NDFUNC=1 NPFUNC=1 DIFFSP=.TRUE. DIFFS=.TRUE. $END
 $SCF DIRSCF=.TRUE. $END
 $STATPT OPTTOL=0.0001 NSTEP=20 $END
 $DATA 
Ammonia 6-311G(d,p)++
CNV 3

 N           7.0   0.0000000000   0.0000000000  -0.0501412961
 H           1.0   0.9619980493   0.0000000000   0.2322268510
 $END
 $ZMAT IZMAT(1)=1,2,1,  
                1,3,1,  2,3,1,2, 
                1,4,1,  2,4,1,2,  3,4,1,2,3   $END  
```

```{code-block} 
---
name: ammonia_6311_Z_E.inp
linenos: True
lineno-start: 1
emphasize-lines: 
caption: ammonia_6311_Z_E.inp
---
 $CONTRL SCFTYP=RHF RUNTYP=ENERGY MAXIT=30 MULT=1 ICHARG=0 
  COORD=ZMT $END
 $SYSTEM TIMLIM=525600 MEMORY=1000000 $END
 $BASIS GBASIS=N311 NGAUSS=6 NDFUNC=1 NPFUNC=1 DIFFSP=.TRUE. DIFFS=.TRUE. $END
 $SCF DIRSCF=.TRUE. $END
 $STATPT OPTTOL=0.0001 NSTEP=100 $END
 $DATA 
Water
CNV 3

X
N  1  1.0
H  2  1.0124  1  112.15
H  2  1.0124  1  112.15  3  +120.0
H  2  1.0124  1  112.15  3  -120.0
 $END
! Angle of 112.15 is the X-N-H angle (from the dummy atom)
```
