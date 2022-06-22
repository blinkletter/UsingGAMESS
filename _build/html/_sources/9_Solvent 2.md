# Solvent: The Environment Matters

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
linenos: True
lineno-start: 1
emphasize-lines: 
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
linenos: True
lineno-start: 1
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

The water calculation setteld down to a seemingly **stable** *D<sub>3h</sub>* structure but it **kept fighting** that answer. the gradient never found a low value that would end the calculation as the structure **thrashed** (ever so slightly) around the saddle point. Eventually it fell over the edge and broke symmetry to find a structure that appears to be the **starting materials**/products. It **failed** to find a transition state-like structure.

```{note}
I had used *C<sub>3h</sub>* symmetry in my first attempts while learning how to do this. What can I say, point groups are not my thing. As a result the calculation completed in both cases but gave an incorrect structure for the solvent job. We are actually optimizing a saddle point here and `GAMESS` will try to escape downhill unless the symmetry makes an air-tight constraint. 
```

### Hessian Calculations

I will **take** the coordinates from the **gas phase** optimization where the *D<sub>3h</sub>* symmetry held up and use them in **both** new calculations for vibrational analysis, with and without solvent. If **imaginary vibrations** are found then I will copy in the orbital and vibrational data (the $VEC and $HESS groups from the .dat files) and perform the saddle point optimization.

So I **copied** in the coordinates, **changed** to `RUNTYP=HESSIAN` and ran the jobs. They failed again and again. Eventually I read the error information at the end of the file. It stated that the system was unable to create a derivative of at least one of the needed functions. It then **suggested** that I change `METHOD=ANALYTIC` to `METHOD=SEMINUM` in the `$FORCE` group. When you can't get a derivative by using **calculus**, you can still get it **using numeric** methods.

Below are the Hessian input files for the two jobs. Observe how they **differ** only by the presence of the `$PCM` group.

```{code-block} 
---
name: SN2_D3h_321G_HESS.inp
linenos: True
lineno-start: 1
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
linenos: True
lineno-start: 1
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
width: 700px
name: fig9_3
---
*The imaginary vibration for the gas-phase Hessian calculation. The solvent calculation gave similar results.*
```
We are now ready to set up the sadlle point calculation.

### Saddle Point Calculations

