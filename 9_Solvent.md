# 10. Solvent: The Environment Matters

Every calculation demonstrated so far had been performed in **gas phase**. We are modelling a single molecule in a vacuum. That is not the real world. Reactions occur at air pressure, at somewhat sane temperatures (generally less than 200 &deg;C) and in **solvent**. 

## Solvent Models

A charged system will be very high in energy in a **vacuum** but may be perfectly stable in **water**, where dipoles can arrange to oppose the charge and relax the system. Solvent can have many effects. protic solvents can assist the reaction by interacting **directly** with the reactants. Solvents might serve as an acid or a base **catalyst**, for example. Solvents can form structured **cages** around reactants and affect the outcome of very fast reactions.

But the biggest effect will be **stabilization** of charges by dipole-dipole interactions. There is a lot to think about for solvent effects and so models that adjust the energies of the calculation by including solvent effects can be **quite complex**. We can include the molecules of the solvent in our ***ab initio*** calculations, we could model the solvent using **molecular mechanics** to account for its random motion but still involve its presence when atoms become near enough to the reactant to be included in *ab initio* methods. These methods will be costly.

A common method that is less costly is to treat solvent like an electric field. this is the **continuum model**. The solvent is mathematically modelled as a field that **interacts** with the molecule being modelled. There are many optiions and we will be using the popular PCM continuum model.

## The \$PCM Group

The PCM model can be included in the *GAMESS* calculation by adding a `$PCM` group. There are many **parameters** that can be included but we will use it without any changes by simply declaring the `SOLVNT` parameter.

```
 $PCM SOLVNT = WATER $END
```
There are many solvent **options**. See the [*GAMESS* documentation](https://www.msg.chem.iastate.edu/gamess/documentation.html) for more information. Other **popular** choices are WATER, CH3OH, BENZENE, C6H12, THF and DMSO

We could **repeat** any exercise that we have performed so far by adding the `$PCM` group to the input files. The results would likely be a little different, but not in an important way. Nothing we have tried so far involves **charged** systems. The effect of solvent will be most obvious relative to gas phase if we use ions.

We will **set up** an transition state for a *S<sub>N</sun>2* reaction and **optimize** it in a polar **solvent** and in **gas phase**. then we will run an IRC calculation and compare the two reaction coordinates.

## Setting Up the IRC

Symmetry makes life easy. If we consider chloride **reacting** with methylchloride in a *S<sub>N</sun>2* manner, we will have a *D<sub>3h</sub>* structure. I will try to set it up using my understanding of the coordinate space used by *GAMESS* and the **nature** of the *D<sub>3h</sub>* point group. 

```{figure} images/Solvent_1.png
---
width: 600px
name: fig9_1
---
*A symmetrical *S<sub>N</sun>2* reaction. *
```


There will be only **three** unique atoms. The primary axis in *GAMESS* is the *z*-axis. The carbon will be at the **origin** and the chloride will be on the *z*-axis. It will be **reflected** down to the other side along the *z*-axis by the symmetry to give the second chloride. The primary *&sigma;<sub>v</sub>* plane is the *xz* plane. The unique C-H bond will **along** the *x*-axis and the two other hydrogens will be **positioned** by symmetry in the other two *&sigma;<sub>v</sub>* planes with in the *xy* *&sigma;<sub>h</sub>* plane.

```{figure} images/Solvent_2.png
---
width: 600px
name: fig9_2
---
*A symmetrical *S<sub>N</sun>2* reaction. *
```

### The Input Files

Our first input file will be in the ags phase. I used the B3LYP DFT **method** by including `DFTTYP=B3LYP` in the `$CONTRL` group. I picked the 3-21G **basis set** (probably a poor choice, but I wanted to finish the calculation quickly). I set up a `$ZMAT` group for automatic generation of redundant **internal coordinates** so that I can read bond distances and angles out of the text file. The `NONVDW` options are to make sure that both C-Cl bonds are **included** in the auto generation even if they are **too long** to fit the definition of a bond. 

The **unique** coordinates will be 0,0,0 for **carbon**, 1,0,0 for the unique **hydrogen** and 0,0,2 for the unique **chloride**. I know that C-H bonds are generally about 1 &angst; and a typical C-Cl bond is 1.7 &angst; so I chose 2 &angst; since the bonds should be breaking and forming. Nobody knows the true values, but some people think that they can be calculated. The whole system will have a **charge** of -1. 

```{code-block} 
---
name: SN2_321_U.inp
caption: SN2_321_U.inp
---
 $CONTRL SCFTYP=ROHF RUNTYP=OPTIMIZE DFTTYP=B3LYP MAXIT=30 
    ICHARG=-1 MULT=1 COORD=UNIQUE NZVAR=12 $END
 $SYSTEM TIMLIM=525600 MEMORY=1000000 $END
 $BASIS GBASIS=N21 NGAUSS=3 $END
 $SCF DIRSCF=.TRUE. $END
 $STATPT OPTTOL=0.0001 NSTEP=40 $END
 $DATA 
SN2
DNH 3

Cl    17.0    0.00000     0.00000     2.00000
C     6.0     0.00000     0.00000     0.00000
H     1.0     1.00000     0.00000     0.00000
 $END
 $ZMAT AUTO=.TRUE. DLC=.TRUE. NONVDW(1)=1,3, 2,3 $END
```

The transition state must, by symmetry, be **defined** by the *D<sub>3h</sub>* point group. So I don't have to constrain anything. The C-Cl bonds will be **forced** to be identical by the symmetry requirements. As long as they don't fly away to infinity, we should get something that looks like a *S<sub>N</sun>2* transition state. 

The second input file will be a **copy** of the first. All I will do is **add** the $PCM group for a **solvent**. I will choose water.

```{code-block} 
---
name: SN2_H2O_321_U.inp
emphasize-lines: 7
caption: N2_H2O_321_U.inp
---
 $CONTRL SCFTYP=ROHF RUNTYP=OPTIMIZE DFTTYP=B3LYP MAXIT=30 
    ICHARG=-1 MULT=1 COORD=UNIQUE NZVAR=12 $END
 $SYSTEM TIMLIM=525600 MEMORY=1000000 $END
 $BASIS GBASIS=N21 NGAUSS=3 $END
 $SCF DIRSCF=.TRUE. $END
 $STATPT OPTTOL=0.0001 NSTEP=40 $END
 $PCM SOLVNT = WATER $END
 $DATA 
SN2
DNH 3

Cl    17.0    0.00000     0.00000     2.00000
C     6.0     0.00000     0.00000     0.00000
H     1.0     1.00000     0.00000     0.00000
 $END
 $ZMAT AUTO=.TRUE. DLC=.TRUE. NONVDW(1)=1,3, 2,3 $END
```

### Initial Results

I submitted the jobs to *GAMESS* and after a **few minutes** I had my result files in hand.  I openned them and found the last occurance of `NSERCH`, which usually occurs at the **final optimized structure**. I found the list of internal coordinates and took note of the bond distances (the angles are defined by the point group and will be perfect, by definition.) What are the C-H and C-Cl bond lengths?
```{margin}
I had used *C<sub>3h</sub>* symmetry in my first attempts while learning how to do this. What can I say, point groups are not my thing. As a result the calculation completed in both cases but gave an incorrect structure for the solvent job. We are actually optimizing a saddle point here and *GAMESS* will try to escape downhill unless the symmetry makes an air-tight constraint. 
```
The water calculation setteld down to a seemingly **stable** *D<sub>3h</sub>* structure but it **kept fighting** that answer. the gradient never found a low value that would end the calculation as the structure **thrashed** (ever so slightly) around the saddle point. Eventually it fell over the edge and broke symmetry to find a structure that appears to be the **starting materials**/products. It **failed** to find a transition state-like structure.



### Hessian Calculations

I will **take** the coordinates from the **gas phase** optimization where the *D<sub>3h</sub>* symmetry held up and use them in **both** new calculations for vibrational analysis, with and without solvent. If **imaginary vibrations** are found then I will copy in the orbital and vibrational data (the $VEC and $HESS groups from the .dat files) and perform the saddle point optimization.

So I **copied** in the coordinates, **changed** to `RUNTYP=HESSIAN` and ran the jobs. They failed again and again. Eventually I read the error information at the end of the file. It stated that the system was unable to create a derivative of at least one of the needed functions. It then **suggested** that I change `METHOD=ANALYTIC` to `METHOD=SEMINUM` in the `$FORCE` group. When you can't get a derivative by using **calculus**, you can still get it **using numeric** methods.

Below are the Hessian input files for the two jobs. Observe how they **differ** only by the presence of the `$PCM` group.

```{code-block} 
---
name: SN2_D3h_321G_HESS.inp
emphasize-lines: 8
caption: SN2_D3h_321G_HESS.inp
---
 $CONTRL SCFTYP=ROHF RUNTYP=HESSIAN DFTTYP=B3LYP MAXIT=30 
    ICHARG=-1 MULT=1 COORD=UNIQUE NZVAR=12 $END
 $SYSTEM TIMLIM=525600 MEMORY=1000000 $END
 $BASIS GBASIS=N21 NGAUSS=3 $END
 $SCF DIRSCF=.TRUE. $END
 $STATPT OPTTOL=0.0001 NSTEP=40 $END
 $GUESS GUESS=HUCKEL $END
 $FORCE METHOD=SEMINUM VIBANL=.TRUE. $END
 $DATA 
SN2
DNH 3

 CL         17.0   0.0000000000  -0.0000000000   2.3842905066
 C           6.0   0.0000000000   0.0000000000   0.0000000000
 H           1.0   1.0737765052  -0.0000000000  -0.0000000000
 $END
 $ZMAT AUTO=.TRUE. DLC=.TRUE. NONVDW(1)=1,3, 2,3 
 $END
```

```{code-block} 
---
name: SN2_D3h_H2O_321G_HESS.inp
emphasize-lines: 8,9
caption: SN2_D3h_H2O_321G_HESS.inp
---
 $CONTRL SCFTYP=ROHF RUNTYP=HESSIAN DFTTYP=B3LYP MAXIT=30 
    ICHARG=-1 MULT=1 COORD=UNIQUE NZVAR=12 $END
 $SYSTEM TIMLIM=525600 MEMORY=1000000 $END
 $BASIS GBASIS=N21 NGAUSS=3 $END
 $SCF DIRSCF=.TRUE. $END
 $STATPT OPTTOL=0.0001 NSTEP=40 $END
 $GUESS GUESS=HUCKEL $END
 $FORCE METHOD=SEMINUM VIBANL=.TRUE. $END
 $PCM SOLVNT = WATER $END
 $DATA 
SN2
DNH 3

 CL         17.0   0.0000000000  -0.0000000000   2.3842905066
 C           6.0   0.0000000000   0.0000000000   0.0000000000
 H           1.0   1.0737765052  -0.0000000000  -0.0000000000
 $END
 $ZMAT AUTO=.TRUE. DLC=.TRUE. NONVDW(1)=1,3, 2,3 
 $END
```

The **log files** showed that the Hessian calculations took over two minutes each. I was using a very small basis set so you can imagine that this job might take hours with a higher level of theory. Let us hope that the 3-21G basis set is enough for this task.

The results revealed an imaginary vibration in both files. Look for the block of frequency results at the end of the Hessian log file. A small section is excerpted below.

```{code-block} 
---
name: SN2_D3h_321G_HESS.log
linenos: True
lineno-start: 2764
emphasize-lines: 11,16,19,22
caption: Excerpt from SN2_D3h_321G_HESS.log
---
 --- SYMMETRY FOR NORMAL MODES ---
 INCLUDING TRANSLATION AND ROTATION
    2*A1'    0*A1"    3*A2'    6*A2"    7*E''   10*E'  
 EXCLUDING TRANSLATION AND ROTATION (SAYVETZ < 0.01)
    2*A1'    0*A1"    0*A2'    1*A2"    0*E''    4*E'  

     FREQUENCIES IN CM**-1, IR INTENSITIES IN DEBYE**2/AMU-ANGSTROM**2,
     REDUCED MASSES IN AMU.

                            1           2           3           4           5
       FREQUENCY:       207.30 I     28.09        8.07        3.43        2.19  
        SYMMETRY:         A2"         A2'         E'          E''         E'  
    REDUCED MASS:     13.20895     1.01510    16.26869    21.20951    18.17196
    IR INTENSITY:     19.94752     0.00000     0.00001     0.00020     0.00002

  1   CL           X -0.00024042 -0.00016391  0.02390436  0.08918910  0.03907482
                   Y -0.00000030 -0.00202211  0.13898461 -0.05936660 -0.02570863
                   Z -0.04586490  0.00957406 -0.00312118 -0.06143099  0.02482619
  2   CL           X  0.00022961  0.00017522 -0.05170792 -0.07725766  0.08478517
                   Y  0.00000018 -0.00046495  0.04672898  0.04280349  0.12249206
                   Z -0.04586570  0.00922298 -0.00311768 -0.06144903  0.02477948
  3   C            X -0.00002341  0.00002374 -0.01450706  0.00598728  0.06233970
                   Y -0.00000032 -0.00146562  0.09277105 -0.00817242  0.04812668
                   Z  0.26652151  0.00952704 -0.00289935 -0.06046632  0.02447910
  4   H            X  0.00030897 -0.49610162 -0.02223393 -0.01719531  0.07180766
                   Y  0.00019186 -0.28790877  0.08833730 -0.02155593  0.05361895
```

Observe that in {numref}`SN2_D3h_321G_HESS.log`, there is a frequency labelled `207.30 I`. The "I" indicates an **imaginary frequency**. We might say that is has a frequency of -207.3&nbsp;*cm<sub>-1</sub>*. Below it are the vectors for **motion** of each atom in the vibrations. We can see that there is motion of the *z*-axis for the C and both Cl atoms. Both chlorides are moving at 0.046 in one direction (let us say "left") and the central carbon is moving at 0.267 in the other direction (to the "right"). The **carbon** is the **lightest** element and will take on the **largest** motion in this vibration. One bond is getting **shorter** and one is getting **longer**. This is consistent with the outcome of the reaction. We have **found** the imaginary vibration that aligns with the transition state. **Both** log files showed similar results. I used *MacMolPlt* to visiualize the vibration as shown in {numref}`fig9_3`.

```{figure} images/Solvent_3.png
---
width: 600px
name: fig9_3
---
*The imaginary vibration for the gas-phase Hessian calculation. The solvent calculation gave similar results.*
```
We are now **ready** to set up the saddle point calculation.

### Saddle Point Calculations

**Take** the Hessian input file and **change** the `RUNTYP` to `SADPOINT`. Track down the .dat file. It can be found in the *GAMESS* scratch directory (I just searched for "filename.dat" on my computer). Open it and **cut and paste** the `$HESS` group into the new input file. Save the file and run it. 

```{note}
You must use the `$HESS` group from the solvent run for the solvent saddlepoint. The vibrations for gas phase, although similar, are not the same.
```

Now I will have the two input files that **differ** by having different `$HESS` groups and by whether a `$PCM` group is present to declare **solvent**. The solvent calculation input file is shown below.

```{code-block} 
---
name: SN2_D3h_H2O_321G_SADL.inp
emphasize-lines: 1,9,20
caption: Excerpt from SN2_D3h_H2O_321G_SADL.inp
---
 $CONTRL SCFTYP=ROHF RUNTYP=SADPOINT DFTTYP=B3LYP MAXIT=30 
    ICHARG=-1 MULT=1 COORD=UNIQUE NZVAR=12 $END
 $SYSTEM TIMLIM=525600 MEMORY=1000000 $END
 $BASIS GBASIS=N21 NGAUSS=3 $END
 $SCF DIRSCF=.TRUE. $END
 $STATPT OPTTOL=0.0001 NSTEP=40 $END
 $GUESS GUESS=HUCKEL $END
 $FORCE METHOD=SEMINUM VIBANL=.TRUE. $END
 $PCM SOLVNT = WATER $END
 $DATA 
SN2
DNH 3

 CL         17.0   0.0000000000  -0.0000000000   2.3842905066
 C           6.0   0.0000000000   0.0000000000   0.0000000000
 H           1.0   1.0737765052  -0.0000000000  -0.0000000000
 $END
 $ZMAT AUTO=.TRUE. DLC=.TRUE. NONVDW(1)=1,3, 2,3 
 $END
 $HESS
ENERGY IS     -955.6969584956 E(NUC) IS      107.7130912280
 1  1 7.24722865E-03 4.72760552E-09 1.40751890E-03 1.64032676E-03 6.23241611E-09
 1  2-3.73066173E-05-1.28704249E-02 3.54710281E-09-5.72539922E-04 6.79441863E-04
 1  3-8.50832638E-04 3.79570720E-03 6.79439778E-04 8.50829497E-04 3.79570862E-03
 ...
 ...
 Many More Lines... 
```

I ran both calculations and both were **successfull**.

## Running the IRC

We now have data for optimized saddle points of **both gas-phase and solvent** conditions. 

### Analyzing the TS structures

Below are the coordinates for the **two results**.  We immediately see that, while the **gas phase** system maintained the *D<sub>3h</sub>* symmetry, the **solvent** calculation again broke symmetry.  It was held at the saddle point by the math of the saddle point calculation, but was clearly fighting to twist out of the *D<sub>3h</sub>* shape.

```{code-block} 
---
name: SN2_D3h_321G_SADL.log
linenos: True
lineno-start: 1295
emphasize-lines: 11,12,13,16
caption: Excerpt from SN2_D3h_321G_SADL.log
---
      ***** SADDLE POINT LOCATED *****
 COORDINATES OF SYMMETRY UNIQUE ATOMS (ANGS)
   ATOM   CHARGE       X              Y              Z
 ------------------------------------------------------------
 CL         17.0   0.0000000000  -0.0000000000   2.3842905066
 C           6.0   0.0000000000   0.0000000000   0.0000000000
 H           1.0   1.0737765052  -0.0000000000  -0.0000000000
 COORDINATES OF ALL ATOMS ARE (ANGS)
   ATOM   CHARGE       X              Y              Z
 ------------------------------------------------------------
 CL         17.0   0.0000000000   0.0000000000  -2.3842905066
 CL         17.0   0.0000000000  -0.0000000000   2.3842905066
 C           6.0   0.0000000000   0.0000000000   0.0000000000
 H           1.0  -0.5368882526   0.9299177315   0.0000000000
 H           1.0  -0.5368882526  -0.9299177315   0.0000000000
 H           1.0   1.0737765052  -0.0000000000  -0.0000000000
```

```{code-block} 
---
name: SN2_D3h_H2O_321G_SADL.log
linenos: True
lineno-start: 1705
emphasize-lines: 5,6,7,10
caption: Excerpt from SN2_D3h_H2O_321G_SADL.log
---
      ***** SADDLE POINT LOCATED *****
 COORDINATES OF ALL ATOMS ARE (ANGS)
   ATOM   CHARGE       X              Y              Z
 ------------------------------------------------------------
 CL         17.0   0.0000240609  -0.0000000004  -2.3912433892
 CL         17.0   0.0000539071  -0.0000000002   2.3907345964
 C           6.0  -0.0001082120  -0.0000000588   0.0011965211
 H           1.0  -0.5383474068   0.9310013615   0.0003691778
 H           1.0  -0.5383478700  -0.9310011483   0.0003691615
 H           1.0   1.0752784580   0.0000005078   0.0026686497
```

The motions that broke symmetry are very small. **Perhaps** starting with the gas phase strucrture and applying a solvent Hessian calculation resulted in a bad start. **Perhaps** the solvent environment breaks the symmetry (it is modelling a "cavity" that may not fit the *D<sub>3h</sub>* point group). 

### Read the Documentation

I **looked up** the [documentation](https://www.msg.chem.iastate.edu/gamess/GAMESS_Manual/docs-references.txt) and see that **PCM methods ignore symmetry**. So the symmetry lock is not present when using the \$PCM group. The transition state in the solvent calculation is almost perfectly symmetrical and the small perturbations away from *D<sub>3h</sub>* are within the error induced by bond vibrations. We are about 0.2\% away from perfect *D<sub>3h</sub>*.

There are **other solvent models** that may respect symmetry (I would actually have to look them up and learn about them) but we will **stick with PCM** here.

### Build the Input Files

To be fair, I will **not use symmetry** with the gas phase calculation. I will use the `C1` symmetry setting and the full set of cartessian **coordinates** in the IRC input files. I will have to again track down the \$HESS groups from the .dat files for the saddle point calculations and cut and paste them into the respective input files for IRC.

I **copied** a previous IRC input file (from the [Diels Alder project](8A_Diels_Alder.md)) and **added** in the coordinates from the results above for each case. I added the \$PCM group for the solvent input file. I then **pasted** in the appropriate \$HESS group from the corresponding .dat file.

The recipe looks like this...

1. Take a previous input file
2. Swap out the coordinates
3. Add a \$PCM group if needed
4. Swap out the \$HESS group

```{note}
Once you get used to the text-based world of *Unix* you will find that it is often faster to modify text files than to plod through the menus of a GUI tool to do the same thing.
```

In this case, I am **calculating** the orbitals, so I will not need the \$VEC group from the .dat files and I am using **auto** generation of internal coordinates so I will not need the IZMAT matrix in the \$ZMAT group.

**Below** are the first lines of the input files for the IRC calculations.  They will each have to be run again after **changing** `FORWRD=.TRUE.` to `FORWRD=.FALSE.` to run the other direction in the IRC.

```{code-block} 
---
name: SN2_D3h_321G_IRC.inp
emphasize-lines: 1, 6,7
caption: Excerpt from SN2_D3h_321G_IRC.inp
---
 $CONTRL SCFTYP=ROHF RUNTYP=IRC DFTTYP=B3LYP MAXIT=30 
    ICHARG=-1 MULT=1 COORD=UNIQUE NZVAR=12 $END
 $SYSTEM TIMLIM=525600 MEMORY=1000000 $END
 $BASIS GBASIS=N21 NGAUSS=3 $END
 $SCF DIRSCF=.TRUE. $END
 $IRC PACE=GS2 OPTTOL=0.0001 MXOPT=300 STRIDE=0.30 
      SADDLE=.TRUE. TSENGY=.TRUE. FORWRD=.TRUE. NPOINT=300 $END
 $GUESS GUESS=HUCKEL $END
 $FORCE METHOD=SEMINUM VIBANL=.TRUE. $END
 $DATA 
SN2
C1
 CL         17.0   0.0000000000   0.0000000000  -2.3842905066
 CL         17.0   0.0000000000  -0.0000000000   2.3842905066
 C           6.0   0.0000000000   0.0000000000   0.0000000000
 H           1.0  -0.5368882526   0.9299177315   0.0000000000
 H           1.0  -0.5368882526  -0.9299177315   0.0000000000
 H           1.0   1.0737765052  -0.0000000000  -0.0000000000
 $END
 $ZMAT AUTO=.TRUE. DLC=.TRUE. NONVDW(1)=1,3, 2,3 
 $END
 $HESS
ENERGY IS     -955.6090406225 E(NUC) IS      107.7130912280
 1  1 6.79543992E-03-5.28518145E-10-1.13662054E-05 1.86962073E-03-4.41178632E-07
 1  2 1.84498964E-07-1.17868321E-02 4.91464415E-06 9.80471951E-06 3.79074842E-04
 1  3-1.10591017E-03 3.64577504E-03 3.80950771E-04 1.10401128E-03 3.64690486E-03
 1  4 2.36174580E-03-2.57404697E-06-7.29130292E-03
 2  1-5.28518145E-10 6.86601184E-03-2.97887583E-09 4.40191839E-07 1.94030136E-03
 ...
 ...
 Many More Lines... 
```



```{code-block} 
---
name: SN2_D3h_H2O_321G_IRC.inp
emphasize-lines: 1, 6,7, 10
caption: Excerpt from SN2_D3h_H2O_321G_IRC.inp
---
 $CONTRL SCFTYP=ROHF RUNTYP=IRC DFTTYP=B3LYP MAXIT=30 
    ICHARG=-1 MULT=1 COORD=UNIQUE NZVAR=12 $END
 $SYSTEM TIMLIM=525600 MEMORY=1000000 $END
 $BASIS GBASIS=N21 NGAUSS=3 $END
 $SCF DIRSCF=.TRUE. $END
 $IRC PACE=GS2 OPTTOL=0.0001 MXOPT=300 STRIDE=0.30 
      SADDLE=.TRUE. TSENGY=.TRUE. FORWRD=.TRUE. NPOINT=300 $END
 $GUESS GUESS=HUCKEL $END
 $FORCE METHOD=SEMINUM VIBANL=.TRUE. $END
 $PCM SOLVNT = WATER $END
 $DATA 
SN2
C1
 CL         17.0   0.0000240609  -0.0000000004  -2.3912433892
 CL         17.0   0.0000539071  -0.0000000002   2.3907345964
 C           6.0  -0.0001082120  -0.0000000588   0.0011965211
 H           1.0  -0.5383474068   0.9310013615   0.0003691778
 H           1.0  -0.5383478700  -0.9310011483   0.0003691615
 H           1.0   1.0752784580   0.0000005078   0.0026686497
 $END
 $ZMAT AUTO=.TRUE. DLC=.TRUE. NONVDW(1)=1,3, 2,3 
 $END
 $HESS
ENERGY IS     -955.6969739956 E(NUC) IS      107.4285285723
 1  1 6.95543756E-03 3.42600959E-09 9.55860879E-04 1.93857897E-03 1.77783245E-09
 1  2-1.95792854E-04-1.25911383E-02 9.12793077E-09-4.63052182E-04 5.56425838E-04
 ...
 ...
 Many More Lines... 
```

All four calculation completed **successfully**.

## Interpretation of IRC Results

Below qre the **animations** of the reaction coordinate using *MacMolPlt* for both IRC calculations. As demonstrated in the [Diels-Alder exercise](8A_Diels_Alder.md), I **loaded** in the .log file for one of the IRC results and then **appended** frames using the second file that used the **reverse** direction. I then **annotated** the bond lengths and **exported** the animation.

We can see that the solvent IRC we see that the C-Cl bond length is much longer at the end compared to the gas phase IRC. 

Compare the two IRC profiles below. In the "products", the gas phase profile keeps the chloride closer and the C-Cl bond is longer. The energy minimum is also much higher than in the solvent case (don't trust the values with thses low level methods, but the relative magnitudes are instructive). In gas phase, the lowest energy **complex** is actually slightly along the reaction coordinate to the transition state. Chloride anion in a **vacuum** is very high in energy and **pushing** electron density into the back of the methyl chloride results in a charge-transfer comples with some of the negative charge now being **shared** on the chloride of the methyl chloride. Sharing the charge lowers the energy even though bonds are "starting" to change. Gas phase is an **extreme** environment and charged species will be **very high** in energy here.


```{figure} images/SN2_2.gif
---
width: 700px
name: fig9_5
---
*The IRC result for gas phase*
```

```{figure} images/SN2_H2O_2.gif
---
width: 700px
name: fig9_6
---
*The IRC result for solvent*
```



### The Ground State

What is the calculated C-Cl **bond length** in the methyl chloride starting material? We can quickly modify the input file that we used for the transtion state search. All we need to do is **change** the point group. The transition state was *D<sub>3h</sub>* and methyl chloride is *C<sub>3v</sub>*. That change alone will give us the methyl chloride arrangement. Below are the **two input files** for this calculation. Compare them to {numref}`SN2_321_U.inp` and {numref}`SN2_H2O_321_U.inp`.

```{code-block} 
---
name: SN2_C3V_H2O_CH3Cl.inp
emphasize-lines: 5,6,7,10
caption: SN2_C3V_H2O_CH3Cl.inp
---
 $CONTRL SCFTYP=ROHF RUNTYP=OPTIMIZE DFTTYP=B3LYP MAXIT=30 
    ICHARG=-0 MULT=1 COORD=UNIQUE NZVAR=9 $END
 $SYSTEM TIMLIM=525600 MEMORY=1000000 $END
 $BASIS GBASIS=N21 NGAUSS=3 $END
 $SCF DIRSCF=.TRUE. $END
 $STATPT OPTTOL=0.0001 NSTEP=40 $END
 $PCM SOLVNT = WATER $END
 $DATA 
methyl Chloride
CNV 3

Cl    17.0    0.00000     0.00000     2.00000
C     6.0     0.00000     0.00000     0.00000
H     1.0     1.00000     0.00000     0.00000
 $END
 $ZMAT AUTO=.TRUE. DLC=.TRUE. $END
```

```{code-block} 
---
name: SN2_C3V_CH3Cl.inp
emphasize-lines: 5,6,7,10
caption: SN2_C3V_CH3Cl.inp
---
 $CONTRL SCFTYP=ROHF RUNTYP=OPTIMIZE DFTTYP=B3LYP MAXIT=30 
    ICHARG=-0 MULT=1 COORD=UNIQUE NZVAR=9 $END
 $SYSTEM TIMLIM=525600 MEMORY=1000000 $END
 $BASIS GBASIS=N21 NGAUSS=3 $END
 $SCF DIRSCF=.TRUE. $END
 $STATPT OPTTOL=0.0001 NSTEP=40 $END
 $DATA 
methyl Chloride
CNV 3

Cl    17.0    0.00000     0.00000     2.00000
C     6.0     0.00000     0.00000     0.00000
H     1.0     1.00000     0.00000     0.00000
 $END
 $ZMAT AUTO=.TRUE. DLC=.TRUE. $END
```
In the results we again see the slight off-symmetry of the PCM result. Without symmetry being enforced it will not be perfect but it is within 1\% of *C<sub>3v</sub>* symmetry. The key observation is that in methyl choride, the calculated for the C-Cl bond **in solvent** is 1.92&nbsp;&angst;. The IRC settles down to a ground state with the two C-Cl distances being 1.96&nbsp;&angst; and 3.11&nbsp;&angst;. This is very much like a chloride and a methyl chloride. **In water**, the chloride ion is much **more stable** on its own and will be able to relax to a fully non-bonding distance.

In **gas-phase**, the calculated C-Cl length in methyl chloride is 1.92&nbsp;&angst; In the IRC, the ground state was reached with C-Cl lengths of 2.10&nbsp;&angst; and 2.73&nbsp;&angst; We have a bond that is significantly **longer** than the covalent C-Cl distance for methyl chloride and the other is significantly **shorter** than a non-bonded distance.

### Conclusion

We can conclude that the solvent model made a **large difference**. This fact will be amde even more obvious if we visualize the data by plotting it.

## Plotting Results

*MacMolPlt* produces an energy plot, but we can make other **plots** easily using interactive *Python* and the *Unix* toolchain. The first thing that I need is a **table** of the two C–Cl bond lengths and the energy for each point on the IRC bath. The .log file is enormous. How can I get my data quickly?

### Processing the Data

We can use *grep* to **isolate** the lines that contain the **information** that we want. We could use *awk* if we wanted to be elegant but I will keep things simpole and brute force this job with *grep*.

I want to **collect** the following infomation&hellip;

- The step number
- The "stride" value (representative of the overall change between steps)
- The energy at that step
- The two C-Cl internal coordinates

I have found **text** that is associated with each datum. I can **extract** the lines using *grep*. 

I **observe** that the reaction progression (total stride distance) is in lines that contain "`AT PATH DISTANCE STOTAL`" The command below will make a file that contains the **stride** distance (and other text as well).

``` bash
grep "AT PATH DISTANCE STOTAL" SN2_H2O_321G_D3h_IRC_3.log > stride.txt
```
I found that the string "`          TOTAL ENERGY'" (with all eleven spaces) was used to report the **final energy** after each step of the IRC. So the command&hellip;
```bash
grep "          TOTAL ENERGY" IRClogfilename.log > energy.txt
```
&hellip;will strip out the energies at each step. I could now **plot energy vs. reaction progression** (the stride value).

The string "`STRETCH   1  3`" appears on each line with the C-Cl **internal coordinate** for the 1-3 C-Cl bond. Look at the coordinates: Carbon is the third atom and the two chlorides are atoms first and second in the list. The string "`STRETCH   2  3`" appears on each line with the other C-Cl **bond distance**.

The following two commands will give me **a list** of lines with the bond lengths.
```bash
grep "STRETCH   1  3" IRClogfilename.log > C-Cl-1-3.txt
grep "STRETCH   2  3" IRClogfilename.log > C-Cl-2-3.txt
```
I could write a quick **shell script** to do all this and generate the four files. But I'm too lazy to make my life easier.
```{margin}
Experience is a good teacher. You will learn what to look for and when you do this again you will have everything set up for. Always take notes as you work. 
```

```{warning}
Here we see that there are 50 entries in the C-Cl lists but only 49 in the energy.txt and stride.txt lists. this is because step zero had a stride of zero (not explicitly reported, but obvious when you think about it) and the energy for step zero was the saddle point energy which is reported with the text "`FINAL RO-B3LYP ENERGY`" on a line near the beginning of the .log file.
```

If I did write a **shell script** I might just collect the commands all in one file so that they can be run as a batch. Below in {numref}`processIRC.sh` is an example. Here I am **processing** the data for the gas phase IRC. You can modify the filenames to suit.

```{code-block} 
---
name: processIRC.sh
caption: processIRC.sh
---
grep "AT PATH DISTANCE STOTAL" SN2_321G_D3h_IRC_3R.log > gstride_r.txt
grep "          TOTAL ENERGY" SN2_321G_D3h_IRC_3R.log > genergy_r.txt
grep "STRETCH   1  3" SN2_321G_D3h_IRC_3R.log > gC-Cl-1-3_r.txt
grep "STRETCH   2  3" SN2_321G_D3h_IRC_3R.log > gC-Cl-2-3_r.txt
grep "AT PATH DISTANCE STOTAL" SN2_321G_D3h_IRC_3R.log > gstride.txt
grep "          TOTAL ENERGY" SN2_321G_D3h_IRC_3R.log > genergy.txt
grep "STRETCH   1  3" SN2_321G_D3h_IRC_3R.log > gC-Cl-1-3.txt
grep "STRETCH   2  3" SN2_321G_D3h_IRC_3R.log > gC-Cl-2-3.txt
```

All I need to do is place this script in the same directory as my .log files and then run the following command.

```bash
bash processIRC.sh
```

After I performed the commands again with the reverse direction IRC log file and doubled my files to 8. I could easily extract the columns with a text editor but I am going to do it all in a **Jupyter notebook** so that all my work is **documented**. If there is a mistake the stepwise code in the notebook can be examined. We now have the following **data files**. 


| Files    |  Description    |
|  :---------------------------    | :-------------------------  |
| stride.txt \& stride_r.txt       | The stride distance. neither file includes zero
| energy.txt \& energy_r.txt       | The energies, neither file includes energy at step zero
| C-Cl-1-3.txt \& C-Cl-1-3_r.txt   | The C-Cl bond length at all steps, including step zero in both files
| C-Cl-2-3.txt \& C-Cl-2-3_r.txt   | The other C-Cl bond length. Also includes step zero in bioth files

We also observe from the .log file (by searching for ` $HESS GROUP READ FROM CARDS`) that the **energy** of the original saddle point is -955.6969739956&nbsp;*Ha*. With these facts in mind we will depart to the Jupyter notebook to clean and collate the processed data and then make plots to help us **interpret** the IRC data for both the gas-phase and the solvent IRC calculations. 



### Cleaning the Data

We now have the data in a series of **text files**. i would like to **clean and collate** the data so that it is in a nice neat table. I could use a text editor to do this. I could paste the data into Microsoft Excel and organize it that way. But I will use a *Jupyter* notebook. That way I can also provide detailed **documentation** in both text and code that others can follow when interpreting my work.

The process of importing the data files and arranging a table is best **presented** in the *Jupyter* notebooks themselves. You can **download** the notebooks using the link at the top right corner of this web book. You can also see an typeset version (not executable) as part of this book.

In the [first notebook](10_Solvent_IRC_Plots.ipynb) we need to clean and collate the data. Then we will save the data tables for future use. In the [second notebook](10_Solvent_IRC_Plots-Data.ipynb) we will import the tables and plot some data.

First we must **decide** what to plot. Below are some ideas.

### Comparing IRC Plots

The stride value should be similar for each since it is the same bonds in both cases that are changing (stride is a composite value that encompases the totality of bond changes). How do the energies **compare** in gas phase vs. water as bonds break and form across the transition state? Let us plot the **relative energy** vs. **stride**.

```{figure} images/Solvent_plot1.png
---
width: 500px
name: fig9_7
---
*The IRC expressed as a plot of relative energy vs. stride. Black is the solvent IRC and red is the gas phase IRC*
```
In the gas phase, the **relative energy** between the ground state and the transition stste is **much smaller**. This is because the **negatively charged** chloride nucleophile/leaving group is very **high in energy** in a **vacuum** where it cannot share its electrons. In the **solvent** model, the energy is less as chloride can be stabilized by the **electric dipole** of water. In fact the gas phase IRC ends early because the **energy** is actually about to start **going back up** as the nucleophile moves away. In a vacumm, chloride separated widely from the methyl chloride is actually **higher in energy** than the transition state.

### Comparing More-O'Ferrell Jencks Plots

The famous More-O'Ferrell Jencks plot follows one **coordinate** of the reaction with respect to **another**. This reaction has a **nucleophile** that moves in to make a bond and a **leaving group** that departs, breaking a bond. We could plot "making" on one axis and "breaking" on the other. 

There are **two** C-Cl distances in each IRC: the **incoming** nucleophile and the departing leaving group. The C-Cl bond in methyl chlorife is calculated to be about 1.95&nbsp;&angst;. The incoming nucleophile starts at a longer distance and **moves** in. The leaving group bond will begin to break. At the transition state, they should be identical (defined by symmetry). Let us plot **one** length against the **other**. Will it be a straight line? Will it be a curve?

```{figure} images/Solvent_plot2.png
---
width: 500px
name: fig9_8
---
*The IRC expressed as a plot of distances to nucleophile and leaving group. Black is the solvent IRC and red is the gas phase IRC*
```
The black line is the **solvent** IRC. What would you call that? I vote for "double ended hockey stick". It is clear that, at the beginning, **most** of the stride score is due to the nucleophile **moving in** towards the carbon. When it has moved in from 3.1&nbsp;&angst; to about 2.85&nbsp;&angst; we finally see the leaving group **start to move** in concert. Would you say that the reaction "begins" when the nucleophile **reaches** 2.85&nbsp;&angst;? Does it end when the leaving group reaches that distance on the **other side**? Or should be include the translation of the nucleophile in from 3.1&nbsp;&angst; (or even farther)?

The **gas phase** IRC is shorter because of the high cost of moving the chloride away in a vacuum. The key takeaway here is that solvent modeling has a **very large effect** in charged systems and probably a significant effect in every system.

### The 3<sup>rd</sup> Dimension

We can use a 3D plot to combine the information in the two previous plots above. Below is a 3D plot of the solvent IRC. Does that help you to imagine the nucleophile translating in, the making and breaking of bonds, and the leaving group translating away? I wonder what other kinds of plots we could use.

```{figure} images/Solvent_plot3.png
---
width: 500px
name: fig9_9
---
*The IRC for the reaction in solvent*
```


## Summary

Adding the **solvent model** made a huge difference in the energy of the reaction.  The IRC for *S<sub>N</sub>2* was familiar to us when modelled in **water** but was not when modelled in **gas phase**.

In the **solvent model**, the system moves to lower energy as the chloride **leaves** into the pool of mathematical water. We can easily imagine **separate** chloride and methyl chloride that meet and react. 

In **gas phase**, the chloride is not stabilized and is a high energy when it is alone. To relax its electron density it is actually the lowests energy state to have a **partial bond** to the carbon of methyl chloride and, consequently, to have the C-Cl bond in methyl chloride **partialy broken**. This is a state that we would consider to be "on the way" to reacting and not a ground state. But we are familiar with solvent reactions, not gas phase.

**Gas phase is not the same as solvent**. Should we redo everything that we did up until now by adding a $PCM group to all our input files and running them again? That will be left as an exercise for the reader.

## A Challenge

Is the rotational energy profile of **butane** different in water and cyclohexane solvents compared to gas phase? My hypothesis is that there will be little difference.

Is the rotational energy profile of **butadiene** different in water and cyclohexane solvents compared to gas phase? My hypothesis is that there will be a detectable, but not large difference. We do have large changes in electronic structure as the &pi; system changes with rotation but no charges are involved.

Is the IRC of the **Diels-Alder** reaction different in water and cyclohexane solvents compared to gas phase? I think this would respond similarly to the butadiene rotation for the same reasons. But we could be surprised. Go try it.

Modify the butane rotational energy profile by using **ethylene glycol**. Does the energy at different torsional values change between water, cyclohexane and gas phase? 

Modify the butadiene rotational energy profile by using **glyoxal**. Does the energy at different torsional values change between water, cyclohexane and gas phase? 

Are the energies (Eigenvalues) and coefficients (Eigenvectors) of **molecular orbitals** different when solvent is applied? Model **butadiene** in the *s-trans* conformer and see. Then do the same with **acrolein**.


