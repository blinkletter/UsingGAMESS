# Transition States in GAMESS

One of the most useful activities in computational chemistry is examining reaction energy barriers. If we can compare the energy of a transition state as we change structure, we can learn the reasons for these kinetic effects and make predictions. Calculating transition states is challenging. Partially formed bonds and separated charges require higher levels of theory to accurately describe and so the computation cost rises rapidly. The T.S. itself may not be easy to find, especially when there are high degrees of freedom (lots of ways to arrange the structure).

So let us start with a common example, the Diels Alder reaction.  This electrocyclic addition reaction is a good candidate for these calculation because of its organized transition state (fewer degrees of freedom) and lack of charge separation.

The very first step is to set up GAMESS on your computer. We have done that already in a previous exercise. This exercise assumes that you have a working suite of GAMESS, GamessQ and MacMolPlt. We also should be familiar with Unix tools and text editing.

## Starting the Journey to the T.S.

The easiest way to find the T.S. for a cycloaddition reaction is to start with a symmetrical system and run a scan of distances between the atoms that form the new bonds.  In a symmetrical system the two bond lengths should be identical in the T.S. The reaction that we will model is presented in {numref}`fig8_1`.

```{figure} images/Diels_1.png
---
width: 600px
name: fig8_1
---
*A typical Diels-Alder cycloaddition reaction.*
```

The easiest approach is to model the product and then calculate minimized structures as we force the two new bonds apart. Hopefully, we will encounter the transition state along that coordinate.

First we will build the product, cyclohexene, using *MacMolPlt* and then create an input file for a structure optimization. We will use 6-31G<sup>*</sup> basis set. Our calculations should still finish in minutes – I hope.


### Building Cyclohexene

Using the Builder Tool panel in *wxMacMolPlt*, Chose carbon with a coordination number of 3. Add the two carbon atoms of the alkene group. Then increase the coordination number to 4 and add an *sp<sup>3</sup>* carbon to each end of the alkene. Then add one more *sp<sup>3</sup>* carbon to each of the current *sp<sup>3</sup>* carbon atoms.  We now have six carbon atoms in total. Now grab each terminal *sp<sup>3</sup>* carbon and move them in space to try to connect them together without breaking any bonds. Fiddle with it a bit and you’ll get the knack. In the end we will have a structure like that shown in {numref}`fig8_2`.

```{figure} images/Diels_2.png
---
width: 600px
name: fig8_2
---
*The initial structure for cyclohexene in MacMolPlt.*
```

Export an input file from `Subwindow` → `Input Builder`. We choose a `Runtype: Optimization`  with the `3-21G` basis set with `1 D Heavy Atom Polarization Function` (3-21G<sup>\*</sup>). We set `Coord. Type: Z-Matrix` and `# of Z-Matrix Variables` to `42` (3 × 16 atoms – 6).
I submitted the calculation to *GAMESS* via *GamessQ* and it ran successfully.  In {numref}`Cyclohexene-ZMAT.inp` is the input file and the Z-matrix for the resulting optimized structure.



```{code-block} 
---
name: Cyclohexene-ZMAT.inp
linenos: True
lineno-start: 1
emphasize-lines: 12, 15, 16
caption: Cyclohexene.inp
---
!   File created by MacMolPlt 7.7.2
 $CONTRL SCFTYP=RHF RUNTYP=OPTIMIZE MAXIT=30 MULT=1 COORD=ZMT NZVAR=42 NOSYM=1 
    MOLPLT=.TRUE. $END
 $SYSTEM TIMLIM=525600 MEMORY=1000000 $END
 $BASIS GBASIS=N21 NGAUSS=3 NDFUNC=1 $END
 $SCF DIRSCF=.TRUE. $END
 $STATPT OPTTOL=0.0001 NSTEP=50 $END
 $DATA 
Cyclohexene
C1
C
C   1    1.54000
C   2    1.54000  1 120.0000
C   1    1.54000  2 120.0000  3   0.0000
C   4    1.41037  1  89.6402  2  47.3676
C   3    1.42617  2  96.3800  5 -23.8081
H   1    1.14000  4 120.0000  2 180.0000
H   2    1.14000  1 120.0000  3 180.0000
H   3    1.14000  6 112.6374  2 117.7914
H   3    1.14000  9 110.4255  6 -126.1402
H   4    1.14000  5 114.1752  1 116.4929
H   4    1.14000  11 111.0397  5 -129.4079
H   5    1.14000  4 104.3204  6 -122.5757
H   5    1.14000  13 108.4843  4 111.1625
H   6    1.14000  3 107.6066  5 -121.0604
H   6    1.14000  15 109.0496  3 116.6663
 $END
 $ZMAT IZMAT(1)=1,2,1, 1,3,2, 2,3,2,1, 1,4,1, 2,4,1,2, 3,4,1,2,3, 1,5,4, 
    2,5,4,1, 3,5,4,1,2, 1,6,3, 2,6,3,2, 3,6,3,2,5, 1,7,1, 2,7,1,4, 3,7,1,4,2, 
    1,8,2, 2,8,2,1, 3,8,2,1,3, 1,9,3, 2,9,3,6, 3,9,3,6,2, 1,10,3, 2,10,3,9, 
    3,10,3,9,6, 1,11,4, 2,11,4,5, 3,11,4,5,1, 1,12,4, 2,12,4,11, 3,12,4,11,5, 
    1,13,5, 2,13,5,4, 3,13,5,4,6, 1,14,5, 2,14,5,13, 3,14,5,13,4, 1,15,6, 
    2,15,6,3, 3,15,6,3,5, 1,16,6, 2,16,6,15, 3,16,6,15,3 $END
```
After the optimization the following structure was calculated to have a minimum energy. It may not be the global minimum but it is the conformer that will relate to the path toward the transition state. Observe the changes. One large change is the distance between atoms 1 and 2 (the C=C alkene bond). In the initial structure it was created with the length of a single bond (1.54 Å) but it settled down to the length of a double bond (1.32&nbsp;Å).
```{code-block} 
---
name: Z-matrix from final structure in Cyclohexene_322.log
linenos: True
lineno-start: 7359
emphasize-lines: 4, 10, 13
caption: Cyclohexene-ZMAT.log
---
                 - - ATOMS - -         COORDINATE      COORDINATE
 NO.   TYPE    I  J  K  L  M  N        (BOHR,RAD)       (ANG,DEG)
 ----------------------------------------------------------------
   1 STRETCH   2  1                     2.4900161       1.3176599
   2 STRETCH   3  2                     2.8598456       1.5133652
   3 BEND      3  2  1                  2.0706722     118.6407771
   4 STRETCH   4  1                     2.8599234       1.5134064
   5 BEND      4  1  2                  2.0706667     118.6404608
   6 TORSION   4  1  2  3               0.0002332       0.0133607
   7 STRETCH   5  4                     2.9373147       1.5543601
   8 BEND      5  4  1                  1.9213701     110.0863959
   9 TORSION   5  4  1  2               0.8352742      47.8576842
  10 STRETCH   6  3                     2.9370306       1.5542097
  11 BEND      6  3  2                  1.9210199     110.0663316
  12 TORSION   6  3  2  5              -0.4042907     -23.1641501
  13 STRETCH   7  1                     2.0280922       1.0732202
  14 BEND      7  1  4                  2.0829141     119.3421846
  15 TORSION   7  1  4  2              -3.1386066    -179.8289142
  16 STRETCH   8  2                     2.0280685       1.0732077
  17 BEND      8  2  1                  2.1296072     122.0175058
  18 TORSION   8  2  1  3              -3.1391054    -179.8574920
  19 STRETCH   9  3                     2.0466718       1.0830522
  20 BEND      9  3  6                  1.9131273     109.6141214
  21 TORSION   9  3  6  2               2.1407494     122.6559047
  22 STRETCH  10  3                     2.0546998       1.0873004
  23 BEND     10  3  9                  1.8735587     107.3470048
  24 TORSION  10  3  9  6              -2.0650527    -118.3188042
  25 STRETCH  11  4                     2.0546895       1.0872949
  26 BEND     11  4  5                  1.9031911     109.0448198
  27 TORSION  11  4  5  1               2.0959496     120.0890683
  28 STRETCH  12  4                     2.0466137       1.0830214
  29 BEND     12  4 11                  1.8737531     107.3581450
  30 TORSION  12  4 11  5              -2.0714183    -118.6835243
  31 STRETCH  13  5                     2.0479066       1.0837056
  32 BEND     13  5  4                  1.9058546     109.1974274
  33 TORSION  13  5  4  6              -2.1442210    -122.8548136
  34 STRETCH  14  5                     2.0463503       1.0828820
  35 BEND     14  5 13                  1.8744682     107.3991153
  36 TORSION  14  5 13  4               2.0385284     116.7990748
  37 STRETCH  15  6                     2.0463017       1.0828563
  38 BEND     15  6  3                  1.8840213     107.9464669
  39 TORSION  15  6  3  5              -2.1063663    -120.6858990
  40 STRETCH  16  6                     2.0478824       1.0836928
  41 BEND     16  6 15                  1.8747644     107.4160889
  42 TORSION  16  6 15  3               2.0534373     117.6532891



The resulting log file, Cyclohexene_322.log, was opened and examined in a text editor. A selection from the log file is shown in {numref}`Cyclohexene-ZMAT.log`. We see that the bonds that we want to stretch as we move toward the transition state are C5–C4 and C6–C3 (highlighted above). These two bond lengths are the 7th and 10th $ZMAT coordinates. 

I will open the log file with *MacMolPlt* and I chose to view the atom labels. I chose to display the atom numbers by selecting `View` → `Atom Labels` → `Atom Number`. We can now clearly see that the bond lengths between carbons 4,5 and 3,6 are going to define the reaction coordinate. See {numref}`fig8_3`.


```{figure} images/Diels_3.png
---
width: 600px
name: fig8_3
---
*Optimized structure of cyclohexene*
```

We did not use symmetry in the above calculation. The optimization found the symmetrical boat conformation of cyclohexene because we started very close to it with our initial structure. The more stable half-chair conformation could easily have been the result. Also, in my reading, I have learned that the boat conformation is a shallow energy well in a wide energy “plateau” between the two possible half-chair conformations.[^Shishkin2011] This means that it has a high entropy and could easily swing off-track when we are trying to scan bond distances. However, GAMESS will maintain symmetry when we request it and the boat conformation is *C<sub>S</sub>* and the half-chair is *C<sub>2</sub>*. So we might be able to keep things in the groove that way. Be prepared to tack if the wind changes.

As an exercise, let us construct the boat and twist-boat versions of cyclohexene and compare their energies. We will use the symmetry builder function of *MacMolPlt* to build a moleculke that fits the given symmetry exactly and then enforce that symmetry throughout the calculation.

[^Shishkin2011]: “Unusual Properties of Usual Molecules. Conformational Analysis of Cyclohexene, Its Derivatives and Heterocyclic Analogues.” O.V. Shishkin & S.V. Shishkina, *Practical Aspects of Computational Chemistry I*, Leszczynski J., Shukla M. (eds), I. Springer, Dordrecht, **2011**, *557–578*. https://doi.org/10.1007/978-94-007-0919-5_19 

### Building *C<sub>s</sub>* Cyclohexene

Open *MacMolPlt* and start new file. Select `View` → `Show Axis` to display the three *xyz* axes. We must keep track of the axes when building with symmetry. The *C<sub>s</sub>* cyclohexene with have a σ<sub>xy</sub> plane so we will want the three unique atoms above or below that plane so they can be reflected to the other side. However, *MacMolPlt* will place the first three atoms that you drop in into the xy plane. We will solve this by adding a single atom and then dragging it above the plane. Follow along and all will become clear.

Now let us set up the symmetry build. Click on `Builder` → `Edit with Symmetry`. Then we must define the symmetry we are using. Click on `Molecule` → `Set Point Group` → `Point Group` → `Cs`. We are now ready to add the first carbon.

Click on `Builder` → `Show Build Tools` and choose Carbon with a coordination number of 3 (this would be a *sp<sup>2</sup>* carbon). Click in the *MacMolPlt* window to place the atom. Now rotate the view in the window so that the xy plane becomes horizontal and the z-axis is vertical. Drag the carbon attom upwards and observe how its reflection appears on the other side of the xy plane. Drag it until you get a double bond between the atom and its doppelganger. Now go back to the Build Tools and choose carbon with a coordination number of 4 (this is *sp<sup>3</sup>*). Add a new carbon tom one of the bonds and then extend the chain one more carbon. You will have three atoms and three reflected atoms placed. Drag the finl carbon toward its mirror conterpart until *MacMolPlt* assigns a bond. Return to the Build Tools and choose Hyfrogen. Populate all the remaining bonds with hydrogen atoms. We now have a starting structure.

Now we need to center the molecule in the symmetry system. MacMolPlt can make all the right decisions for us. Click on `Molecule` → `Set Coordinates to principal Orientation` and the molecule will be centered on the *xyz* coordinate system. Save your work. The image in the MacMolPlt window might look like {numref}`fig8_4`

```{figure} images/Diels_4.png
---
width: 600px
name: fig8_4
---
*Initial build of *C<sub>s</sub>* Cyclohexene*
```

### Optimizing *C<sub>s</sub>* Cyclohexene

We know that *C<sub>s</sub>* cyclohexene is not the lowest energy conformer. But by enforcing the *C<sub>s</sub>* symmetry we can hold it in this conformation while it minimizes. Open `Subwindow` → `Input Builder` and set up an optimization at the 6-31G<sup>*</sup> level. I initially created a GAMESS input file with Z-matrix coordinates but the calculation immediately failed. The nature of the Z-matrix often results in tiny rounding errors in the coordinate va;lues combining to a slightly bigger error by the time the positioning has worked its way along all the internal cooridnates. This error was obviously enough to place an atom or two outside of the tolerance for the symmetry calculation. We should use `Unique Coordinates` for symmetry calculations. the input file is reproduced in {numref}`Cyclohexene_Cs_cart.inp`.

```{code-block} 
---
name: Cyclohexene_Cs_cart.inp
linenos: True
lineno-start: 1
emphasize-lines: 10, 22
caption: Cyclohexene_Cs_cart.inp
---
!   File created by MacMolPlt 7.7.2
 $CONTRL SCFTYP=RHF RUNTYP=OPTIMIZE MAXIT=30 MULT=1 COORD=UNIQUE NZVAR=42 
    MOLPLT=.TRUE. $END
 $SYSTEM TIMLIM=525600 MEMORY=1000000 $END
 $BASIS GBASIS=N31 NGAUSS=6 NDFUNC=1 $END
 $SCF DIRSCF=.TRUE. $END
 $STATPT OPTTOL=0.0001 NSTEP=30 $END
 $DATA 
Title
CS

C     6.0    -1.35474    -0.12747    -0.65064
C     6.0    -0.07172     0.23663    -1.42064
C     6.0     1.42646    -0.10916    -0.75855
H     1.0    -2.30450    -0.39699    -1.22064
H     1.0     1.75283    -1.13977    -1.12040
H     1.0    -0.12286    -0.30664    -2.42156
H     1.0     2.17392     0.67089    -1.12244
H     1.0    -0.10252     1.36058    -1.60873
 $END
 $ZMAT IZMAT(1)=1,2,1, 1,3,1, 2,3,1,2, 1,4,2, 2,4,2,1, 3,4,2,1,3, 1,5,3, 
    2,5,3,1, 3,5,3,1,4, 1,6,5, 2,6,5,3, 3,6,5,3,1, 1,7,1, 2,7,1,2, 3,7,1,2,3, 
    1,8,2, 2,8,2,1, 3,8,2,1,4, 1,9,5, 2,9,5,6, 3,9,5,6,3, 1,10,6, 2,10,6,5, 
    3,10,6,5,9, 1,11,3, 2,11,3,1, 3,11,3,1,5, 1,12,4, 2,12,4,2, 3,12,4,2,6, 
    1,13,5, 2,13,5,9, 3,13,5,9,6, 1,14,6, 2,14,6,10, 3,14,6,10,5, 1,15,3, 
    2,15,3,11, 3,15,3,11,1, 1,16,4, 2,16,4,12, 3,16,4,12,2 $END
```
This calculation completed normaly. After it finished we find this block of text for the final results. The last `NSERCH` entry reveals that the calculation has reached a stationary point and finished. The energy is reported along with the symmetry unique *xyz* cartessian coordinates, the full set of coordinates and the internal coordinates that were listed in the `IZMAT(1)` matrix. 

Examine the values in {numref}`Cyclohexene_Cs_cart.log`. You will see that the 5,3 bond length is the bond that will be extended as the two atoms of ethylene depart the atoms of the butadiene. The 4,6 bond length is not in the IZMAT(1) list. But it will be identical to the 5,3 bond as required by the symmetry point group. If we lock it, will will lock both.

```{code-block} 
---
name: Cyclohexene_Cs_cart.log
linenos: True
lineno-start: 7629
emphasize-lines: 4, 53
caption: Cyclohexene_Cs_cart.log
---
 NSERCH:  13  E=     -233.0092034708  GRAD. MAX=  0.0000982  R.M.S.=  0.0000328


      ***** EQUILIBRIUM GEOMETRY LOCATED *****
 COORDINATES OF SYMMETRY UNIQUE ATOMS (ANGS)
   ATOM   CHARGE       X              Y              Z
 ------------------------------------------------------------
 C           6.0  -1.2361448368  -0.1946329600  -0.6600113451
 C           6.0  -0.0378417377   0.3464128969  -1.4003885217
 C           6.0   1.2786263669  -0.1546858673  -0.7750422486
 H           1.0  -2.0799554481  -0.5613400776  -1.2195305741
 H           1.0   1.4530973204  -1.1662228431  -1.1266412274
 H           1.0  -0.0703048808   0.0705907162  -2.4493138697
 H           1.0   2.1015046661   0.4444993783  -1.1525848695
 H           1.0  -0.0627168721   1.4351432438  -1.3719834428
 COORDINATES OF ALL ATOMS ARE (ANGS)
   ATOM   CHARGE       X              Y              Z
 ------------------------------------------------------------
 C           6.0  -1.2361448368  -0.1946329600   0.6600113451
 C           6.0  -1.2361448368  -0.1946329600  -0.6600113451
 C           6.0  -0.0378417377   0.3464128969   1.4003885217
 C           6.0  -0.0378417377   0.3464128969  -1.4003885217
 C           6.0   1.2786263669  -0.1546858673   0.7750422486
 C           6.0   1.2786263669  -0.1546858673  -0.7750422486
 H           1.0  -2.0799554481  -0.5613400776   1.2195305741
 H           1.0  -2.0799554481  -0.5613400776  -1.2195305741
 H           1.0   1.4530973204  -1.1662228431   1.1266412274
 H           1.0   1.4530973204  -1.1662228431  -1.1266412274
 H           1.0  -0.0703048808   0.0705907162   2.4493138697
 H           1.0  -0.0703048808   0.0705907162  -2.4493138697
 H           1.0   2.1015046661   0.4444993783   1.1525848695
 H           1.0   2.1015046661   0.4444993783  -1.1525848695
 H           1.0  -0.0627168721   1.4351432438   1.3719834428
 H           1.0  -0.0627168721   1.4351432438  -1.3719834428


                     --------------------
                     INTERNAL COORDINATES
                     --------------------

                 - - ATOMS - -         COORDINATE      COORDINATE
 NO.   TYPE    I  J  K  L  M  N        (BOHR,RAD)       (ANG,DEG)
 ----------------------------------------------------------------
   1 STRETCH   2  1                     2.4944812       1.3200227
   2 STRETCH   3  1                     2.8514326       1.5089133
   3 BEND      3  1  2                  2.0836538     119.3845714
   4 STRETCH   4  2                     2.8514326       1.5089133
   5 BEND      4  2  1                  2.0836538     119.3845714
   6 TORSION   4  2  1  3               0.0000000       0.0000000
   7 STRETCH   5  3                     2.9124143       1.5411834
   8 BEND      5  3  1                  1.9419391     111.2649171
   9 TORSION   5  3  1  4              -0.7686612     -44.0410407
  10 STRETCH   6  5                     2.9292350       1.5500845
  11 BEND      6  5  3                  1.9886035     113.9385868
  12 TORSION   6  5  3  1               0.7244789      41.5095860
  13 STRETCH   7  1                     2.0349043       1.0768251
  14 BEND      7  1  2                  2.1171801     121.3054817
  15 TORSION   7  1  2  3               3.1274445     179.1893718
  16 STRETCH   8  2                     2.0349043       1.0768251
  17 BEND      8  2  1                  2.1171801     121.3054817
  18 TORSION   8  2  1  4              -3.1274445    -179.1893718
  19 STRETCH   9  5                     2.0503910       1.0850203
  20 BEND      9  5  6                  1.9008019     108.9079266
  21 TORSION   9  5  6  3               2.1053019     120.6249126
  22 STRETCH  10  6                     2.0503910       1.0850203
  23 BEND     10  6  5                  1.9008019     108.9079266
  24 TORSION  10  6  5  9               0.0000000       0.0000000
  25 STRETCH  11  3                     2.0504843       1.0850696
  26 BEND     11  3  1                  1.9384410     111.0644875
  27 TORSION  11  3  1  5              -2.1356366    -122.3629638
  28 STRETCH  12  4                     2.0504843       1.0850696
  29 BEND     12  4  2                  1.9384410     111.0644875
  30 TORSION  12  4  2  6               2.1356366     122.3629638
  31 STRETCH  13  5                     2.0516282       1.0856749
  32 BEND     13  5  9                  1.8545479     106.2577655
  33 TORSION  13  5  9  6              -2.0746275    -118.8673992
  34 STRETCH  14  6                     2.0516282       1.0856749
  35 BEND     14  6 10                  1.8545479     106.2577655
  36 TORSION  14  6 10  5               2.0746275     118.8673992
  37 STRETCH  15  3                     2.0586389       1.0893849
  38 BEND     15  3 11                  1.8530987     106.1747371
  39 TORSION  15  3 11  1               2.0680856     118.4925790
  40 STRETCH  16  4                     2.0586389       1.0893849
  41 BEND     16  4 12                  1.8530987     106.1747371
  42 TORSION  16  4 12  2              -2.0680856    -118.4925790
```
## Proposing a Hypothetical Transition State

We now have the *C<sub>s</sub>* strtucture of cyclohexene. This structure is on the path to the retro-Diels-Alder products. The twist-boat *C<sub>2</sub>* conformer is the most stable. It will be in equilibrium with the *C<sub>s</sub>* boat conformer. From there, bonds must stretch as we move from cyclohexene, through a transition state, to butadiene and ethylene. We will consider our reaction to from *C<sub>2</sub>* cyclohexene, through a *C<sub>2</sub>*  transition state, to a *C<sub>2</sub>*  arrangement of products. Does this seem reasonable to you?

The scheme for the reaction with symmetries noted is shown in {numref}`fig8_7`. We will need to create a series of input files with longer and longer C-C bond lengths for the two breaking bonds. We will lock that internal coordinate in the IZMAT(1) matrix and allow the structure to relax with only that longer bond length enforced. Take note that that bond length involves the 3,5 and 4,6 bonds, but only the 3,5 is defined in the internal; coordinates.  The C<sub>s</sub> symmetry will hold the 4.6 identical to the 3,5 (I hope).

```{figure} images/Diels_7.png
---
width: 600px
name: fig8_7
---
*Reaction coordinate for the retro-Diels_Alder reaction of cyclohexene*
```

### Scanning Using Cartesian Coordinates

Let us examine the result of the C<sub>s</sub> optimization of cyclohexene that was performed above. In {numref}`fig8_6` we see the axes and the atom numbers. I observe that atom 5 (and its symmetry-matched atom 6) are somewhat aligned with the *x-axis*. By simply adding a set value to the *x-axis* coordinate for this group, we can increase the length of the bond. Before we go any farther, let us increase it by 0.4 Å. We will need to add a value to the *x-axis* for the carbnon and the two hydrogen atoms attached to it. In {numref}`fig8_8` We see the general idea plotted out graphically. Eventually we will run a series of input files with increasing increments to the *x-axis* for the three symmetry unique atoms that define the departing ethylene group.

```{figure} images/Diels_6.png
---
width: 600px
name: fig8_6
---
*C<sub>s</sub> structure of cyclohexene showing coordinate axes that define the *xyz* position of atoms in the input file.*
```

```{figure} images/Diels_8.png
---
width: 600px
name: fig8_8
---
*Diagram of the plan for constructing the coordinate scan*
```

But which atoms in the input file represent the carbon atoms 5 and 6 9and attached hydrogens) in the image in {numref}`fig8_6`? We know that these atoms should have the most positive x-axis values. looking at the symmetry unique coordinates in the log file from {numref}`Cyclohexene_Cs_cart.log` we see that it is the third, fith and seventh atoms in the list that are highest along the x-axis and represent the atoms of the future ethylene product. See {numref}`Cyclohexene_Cs_cart_excerpt` for an excerpt.

```{code-block} 
---
name: Cyclohexene_Cs_cart_excerpt
linenos: True
lineno-start: 7633
emphasize-lines: 6,8,10
caption: Cyclohexene_Cs_cart.log
---
 COORDINATES OF SYMMETRY UNIQUE ATOMS (ANGS)
   ATOM   CHARGE       X              Y              Z
 ------------------------------------------------------------
 C           6.0  -1.2361448368  -0.1946329600  -0.6600113451
 C           6.0  -0.0378417377   0.3464128969  -1.4003885217
 C           6.0   1.2786263669  -0.1546858673  -0.7750422486
 H           1.0  -2.0799554481  -0.5613400776  -1.2195305741
 H           1.0   1.4530973204  -1.1662228431  -1.1266412274
 H           1.0  -0.0703048808   0.0705907162  -2.4493138697
 H           1.0   2.1015046661   0.4444993783  -1.1525848695
 H           1.0  -0.0627168721   1.4351432438  -1.3719834428
```

We can take these coordinates for the optimized C<sub>s</sub> cyclohexene and past them into a new input file. I will use the original file shown in {numref}`Cyclohexene_Cs_cart.inp` but I will cut and paste in the block of coordinates from {numref}`Cyclohexene_Cs_cart_excerpt` above.  Then I will add exactly 0.4 Å to the *x-axis* values for the three atoms defining the departing group. I will examine the `IZMAT(1)` matrix in the input file and identifty that the 3,5 stretch is the seventh entry. I will then freeze the seventh internal coordinate by adding the `IFREEZ(1)=7` command to the `$STATPT` group. the new input file is shown in {numref}`Cyclohexene_Cs_scan_0.4.inp`. Will it work? I submitted it via GamessQ and then openned the log file to examine the internal coordinates of the final structure.

```{code-block} 
---
name: Cyclohexene_Cs_scan_0.4.inp
linenos: True
lineno-start: 1
emphasize-lines: 7, 14, 16, 18
caption: Cyclohexene_Cs_scan_0.4.inp
---
!   File created by MacMolPlt 7.7.2
 $CONTRL SCFTYP=RHF RUNTYP=OPTIMIZE MAXIT=30 MULT=1 COORD=UNIQUE NZVAR=42 
    MOLPLT=.TRUE. $END
 $SYSTEM TIMLIM=525600 MEMORY=1000000 $END
 $BASIS GBASIS=N31 NGAUSS=6 NDFUNC=1 $END
 $SCF DIRSCF=.TRUE. $END
 $STATPT OPTTOL=0.0001 NSTEP=30 IFREEZ(1)=7 $END
 $DATA 
Title
CS

 C           6.0  -1.2361448368  -0.1946329600  -0.6600113451
 C           6.0  -0.0378417377   0.3464128969  -1.4003885217
 C           6.0   1.6786263669  -0.1546858673  -0.7750422486
 H           1.0  -2.0799554481  -0.5613400776  -1.2195305741
 H           1.0   1.8530973204  -1.1662228431  -1.1266412274
 H           1.0  -0.0703048808   0.0705907162  -2.4493138697
 H           1.0   2.5015046661   0.4444993783  -1.1525848695
 H           1.0  -0.0627168721   1.4351432438  -1.3719834428
 $END
 $ZMAT IZMAT(1)=1,2,1, 1,3,1, 2,3,1,2, 1,4,2, 2,4,2,1, 3,4,2,1,3, 1,5,3, 
    2,5,3,1, 3,5,3,1,4, 1,6,5, 2,6,5,3, 3,6,5,3,1, 1,7,1, 2,7,1,2, 3,7,1,2,3, 
    1,8,2, 2,8,2,1, 3,8,2,1,4, 1,9,5, 2,9,5,6, 3,9,5,6,3, 1,10,6, 2,10,6,5, 
    3,10,6,5,9, 1,11,3, 2,11,3,1, 3,11,3,1,5, 1,12,4, 2,12,4,2, 3,12,4,2,6, 
    1,13,5, 2,13,5,9, 3,13,5,9,6, 1,14,6, 2,14,6,10, 3,14,6,10,5, 1,15,3, 
    2,15,3,11, 3,15,3,11,1, 1,16,4, 2,16,4,12, 3,16,4,12,2 
    $END
```
The calculation failed. the coordinate was not frozen. I looked at the *GAMESS* documentation and learned about a command in the `$ZMAT` group called `IFZMAT`. It will freeze coorinates created by games. I tried including `IFZMAT(1)=1,3,5` to freeze the stretch (1) between the two atoms (3,5) but it failed as well. I tried using automatically generated internal coordinates by deleting the `IZMAT` matrix and using `DLC = .True. AUTO = .True. NONVDW(1) = 3,5, 4,6`. Nothing worked.  You can learn more about [those commands](https://www.msg.chem.iastate.edu/gamess/GAMESS_Manual/docs-input.txt) in the [documentation for GAMESS](https://www.msg.chem.iastate.edu/gamess/documentation.html).

### Freezing Bonds in Cartessian Coordinates
After searching the web I found a [good discussion on how to solve this issue](https://chemistry.stackexchange.com/questions/87389/how-do-i-perform-a-partial-optimisation-in-gamess). We will need to set up internal coordniates and freeze them. What is new here is the `FVALUE` list. It is the values to hold in the `IFFREEZ` list. We will need to use both in the `$ZMAT` group.

We will construct an input file with the correct code to freeze the coordinate. First we will run a quick job to check the calculation and have GAMESS generate the internal coordinates automatically.  Then we will set up an input file where we use this internal coordinate information to identify the two bonds that we wish to change. We will freeze those bonds at various lengths and optimize the geometry of the molecule otherwise. As we optimize at various lengths we will be scanning through the reaction coordinate.

#### Build an input file

As above I will take the input file derived from the optimized structure (see {numref}`Cyclohexene_Cs_scan_0.4.inp`). I will modify the file to change the parameters for a simple check run. Observe that in {numref}`Cyclohexene_Cs_Internal_Check.inp` I have changed the `RUNTYPE` to `ENERGY` and added the command `EXETYPE=CHECK`. This will keep the calculation to one step (calculating the energy of the bstructure as entered) and will check for any errors. Thereis no `$STATPT` gropup here as that does not apply in a single-step energy calculation. I then used the `AUTO=.TRUE. DLC=.TRUE. NONVDW(1)=3,5, 4,6` command to auto-generqte the internal coordinates. the `NONVDW` list informs *GAMESS* that some connections may be too long to be detected as a bond, but we do want them to be treated as a bond.

```{code-block} 
---
name: Cyclohexene_Cs_Internal_Check.inp
linenos: True
lineno-start: 1
emphasize-lines: 1, 19
caption: Cyclohexene_Cs_Internal_Check.inp
---
 $CONTRL SCFTYP=RHF RUNTYP=ENERGY EXETYP=CHECK MULT=1 COORD=UNIQUE NZVAR=42 
    MOLPLT=.TRUE. $END
 $SYSTEM TIMLIM=525600 MEMORY=1000000 $END
 $BASIS GBASIS=N31 NGAUSS=6 NDFUNC=1 $END
 $SCF DIRSCF=.TRUE. $END
 $DATA 
Cyclohexene
CS

 C           6.0  -1.2361448368  -0.1946329600  -0.6600113451
 C           6.0  -0.0378417377   0.3464128969  -1.4003885217
 C           6.0   1.6786263669  -0.1546858673  -0.7750422486
 H           1.0  -2.0799554481  -0.5613400776  -1.2195305741
 H           1.0   1.8530973204  -1.1662228431  -1.1266412274
 H           1.0  -0.0703048808   0.0705907162  -2.4493138697
 H           1.0   2.5015046661   0.4444993783  -1.1525848695
 H           1.0  -0.0627168721   1.4351432438  -1.3719834428
 $END
 $ZMAT AUTO=.TRUE. DLC=.TRUE. NONVDW(1)=3,5, 4,6 $END
```
This input file was submitted using GamessQ. When the job has finished the .log file and the .dat file will contain information taht we will need to manually copy. We will need the list of internal coordinates that we generated to create a new `IZMAT` matrix. We will also need the length of the 3,5 and 4,6 bonds so that we can freeze them at that exact value. You will observe that the `DLC=.TRUE.` command results in many internal coordinates being created (in this case it is 89). We will have to ensure that the `NZVAR` matches this number in the new input file. 

Search your computer for the .dat file. it will have the same names as the input file but end in the .dat extension. In this file will be a `$ZMAT` group for your molecule that was automatically generated by *GAMESS*. Copy and paste it into your input file. Change the `AUTO` flag to `.FALSE.` as we will now be using the `ZMAT` list and do not want it changed by *GAMESS* anymore. We will change `RUNTYPE` to `OPTIMIZE` and return the `$STATPT` group to the file.  

Now find the .log file and locate the list of internal coordinates. I observe that the 3,5 stretch and the 4,6 stretch coordinates are listed a 1.5411834 Å. I have shown a except of the relevent section of the .log file in {numref}`Cyclohexene_Cs_Internal_Check.log`. You may notice that there are redundant coordinates for the 4,6 and 3,6 bonds. The extra copies are forced in by the `NONVDW` command in the `$ZMAT` group.

```{code-block} 
---
name: Cyclohexene_Cs_Internal_Check.log
linenos: True
lineno-start: 810
emphasize-lines: 14, 18
caption: Cyclohexene_Cs_Internal_Check.log
---
                     --------------------
                     INTERNAL COORDINATES
                     --------------------

                 - - ATOMS - -         COORDINATE      COORDINATE
 NO.   TYPE    I  J  K  L  M  N        (BOHR,RAD)       (ANG,DEG)
 ----------------------------------------------------------------
   1 STRETCH   1  7                     2.0349043       1.0768251
   2 STRETCH   1  3                     2.8514326       1.5089133
   3 STRETCH   1  2                     2.4944812       1.3200227
   4 STRETCH   2  4                     2.8514326       1.5089133
   5 STRETCH   2  8                     2.0349043       1.0768251
   6 STRETCH   3 15                     2.0586389       1.0893849
   7 STRETCH   3  5                     2.9124143       1.5411834
   8 STRETCH   3 11                     2.0504843       1.0850696
   9 STRETCH   3  5                     2.9124143       1.5411834
  10 STRETCH   4 12                     2.0504843       1.0850696
  11 STRETCH   4  6                     2.9124143       1.5411834
  12 STRETCH   4  6                     2.9124143       1.5411834
  13 STRETCH   4 16                     2.0586389       1.0893849
  14 STRETCH   5 13                     2.0516282       1.0856749
  15 STRETCH   5  6                     2.9292350       1.5500845
  16 STRETCH   5  9                     2.0503910       1.0850203
  17 STRETCH   6 14                     2.0516282       1.0856749
  18 STRETCH   6 10                     2.0503910       1.0850203
  19 BEND      1  3 11                  1.9384410     111.0644875
  20 BEND      1  3  5                  1.9419391     111.2649171
  21 BEND      1  3  5                  1.9419391     111.2649171
```

Now that we have the $ZMAT group from the .dat file and the bond distance from the .log file, we can set up the input file as described above. the new file is shown in {numref}`Cyclohexene_Cs_Internal_ZMAT.inp`

```{code-block} 
---
name: Cyclohexene_Cs_Internal_ZMAT.inp
linenos: True
lineno-start: 1
emphasize-lines: 1, 20-22
caption: Cyclohexene_Cs_Internal_ZMAT.inp
---
 $CONTRL SCFTYP=RHF RUNTYP=OPTIMIZE MULT=1 COORD=UNIQUE NZVAR=103 
    MOLPLT=.TRUE. $END
 $SYSTEM TIMLIM=525600 MEMORY=1000000 $END
 $BASIS GBASIS=N31 NGAUSS=6 NDFUNC=1 $END
 $SCF DIRSCF=.TRUE. $END
 $STATPT OPTTOL=0.0001 NSTEP=40 $END
 $DATA 
Cyclohexene
CS

 C           6.0  -1.2361448368  -0.1946329600  -0.6600113451
 C           6.0  -0.0378417377   0.3464128969  -1.4003885217
 C           6.0   1.2786263669  -0.1546858673  -0.7750422486
 H           1.0  -2.0799554481  -0.5613400776  -1.2195305741
 H           1.0   1.4530973204  -1.1662228431  -1.1266412274
 H           1.0  -0.0703048808   0.0705907162  -2.4493138697
 H           1.0   2.1015046661   0.4444993783  -1.1525848695
 H           1.0  -0.0627168721   1.4351432438  -1.3719834428
 $END
 $ZMAT AUTO=.FALSE. DLC=.TRUE. NONVDW(1)=3,5, 4,6 
       IFZMAT(1)= 1,3,5,   1,4,6,
       FVALUE(1)= 1.5411834, 1.5411834,
       IZMAT(1)=
         1,   1,   7,
         1,   1,   3,
         1,   1,   2,
         1,   2,   4,
         1,   2,   8,
         1,   3,  15,
         1,   3,   5,
         1,   3,  11,
         1,   3,   5,
         1,   4,  12,
         1,   4,   6,
         1,   4,   6,
         1,   4,  16,
         1,   5,  13,
         1,   5,   6,
         1,   5,   9,
         1,   6,  14,
         1,   6,  10,
         2,   1,   3,  11,
         2,   1,   3,   5,
         2,   1,   3,   5,
         2,   1,   3,  15,
         2,   1,   2,   8,
         2,   1,   2,   4,
         2,   2,   4,  12,
         2,   2,   4,  16,
         2,   2,   1,   3,
         2,   2,   4,   6,
         2,   2,   1,   7,
         2,   2,   4,   6,
         2,   3,   1,   7,
         2,   3,   5,   9,
         2,   3,   5,   6,
         2,   3,   5,  13,
         2,   3,   5,   9,
         2,   3,   5,   6,
         2,   3,   5,  13,
         2,   4,   6,   5,
         2,   4,   6,  14,
         2,   4,   6,  14,
         2,   4,   2,   8,
         2,   4,   6,  10,
         2,   4,   6,   5,
         2,   4,   6,  10,
         2,   5,   3,  15,
         2,   5,   3,  11,
         2,   5,   6,  10,
         2,   5,   6,  14,
         2,   5,   3,  11,
         2,   5,   3,  15,
         2,   6,   4,  16,
         2,   6,   4,  12,
         2,   6,   4,  12,
         2,   6,   5,   9,
         2,   6,   5,  13,
         2,   6,   4,  16,
         2,   9,   5,  13,
         2,  10,   6,  14,
         2,  11,   3,  15,
         2,  12,   4,  16,
         3,   1,   3,   5,   9,
         3,   1,   3,   5,   6,
         3,   1,   2,   4,  16,
         3,   1,   2,   4,   6,
         3,   1,   3,   5,  13,
         3,   1,   2,   4,  12,
         3,   2,   1,   3,  15,
         3,   2,   1,   3,  11,
         3,   2,   4,   6,  10,
         3,   2,   4,   6,  14,
         3,   2,   4,   6,   5,
         3,   2,   1,   3,   5,
         3,   3,   5,   6,  10,
         3,   3,   5,   6,  14,
         3,   3,   5,   6,   4,
         3,   3,   1,   2,   4,
         3,   3,   1,   2,   8,
         3,   4,   6,   5,   9,
         3,   4,   6,   5,  13,
         3,   4,   2,   1,   7,
         3,   5,   3,   1,   7,
         3,   5,   6,   4,  16,
         3,   5,   6,   4,  12,
         3,   6,   5,   3,  11,
         3,   6,   5,   3,  15,
         3,   6,   4,   2,   8,
         3,   7,   1,   2,   8,
         3,   7,   1,   3,  15,
         3,   7,   1,   3,  11,
         3,   8,   2,   4,  16,
         3,   8,   2,   4,  12,
         3,   9,   5,   6,  14,
         3,   9,   5,   6,  10,
         3,   9,   5,   3,  11,
         3,   9,   5,   3,  15,
         3,  10,   6,   5,  13,
         3,  10,   6,   4,  16,
         3,  10,   6,   4,  12,
         3,  11,   3,   5,  13,
         3,  12,   4,   6,  14,
         3,  13,   5,   3,  15,
         3,  13,   5,   6,  14,
         3,  14,   6,   4,  16,
 $END
```
#### Making the Scan Files

Now that we have an input file we can make a whole series of versions with different `FVALUE` lists. I will replace the numbers in the `FVALUE` list with the string "NUMBER`". I will then edit the *bash* shell script `extract.sh` to create a series of values between 1.5 and 3 and write a series of input files with those values replacing the string. 

```{code-block} shell
---
name: makescan.sh
caption: makescan.sh
---
input_file=Cyclohexene_Cs_scan.inp
spacer=_SCAN_
for num in $(seq -w 1.45 0.05 3.00)
do
  sed "s/NUMBER/$num/" $input_file > "$input_file$spacer$num.inp"
done
```

We will now have a series of 32 input files that run optimizations with the 3,5 and 4,6 bond lengths at longer and longer values. 

#### Running the optimization Series

I submitted the files as a batch by dragging them all into the *GamessQ* window. After XX minutes the whole series was complete.

#### Analyzing the Results

I extracted the final energy from each file by modifying and running the extract.sh script. I sent the output into a text file with the command `bash extract.sh > results.txt`.

```{code-block} shell
---
name: extract.sh
caption: extract.sh
---
for name in Cyclohexene_Cs_scan.inp_SCAN*.log; do
    grep -H "NSERCH" "$name" | grep "GRAD" | tail -n 1
done
```
I then imported the file into a pandas dataframe and plotted the energies using the same method as was demostrated in the [butadiene rotation profile analysis](5_Rotation_Profiles_Workflow_Data.ipynb). 

The plot of the potential energy as we stretch the bond distances is presented in {numref}`fig8_9`.


```{figure} images/Diels_9.png
---
width: 600px
name: fig8_9
---
*Reaction coordinate plot for the retro-Diels_Alder reaction of cyclohexene*
```

We observe that the highest energy occurs near 2.2&nbsp;Å. This is a good file to use for the starting point in a transition state optimization.

## Transition State Optimization

We now have a starting position for a transition state optimization. 

### The Hessian Calculation

The `RUNTYPE` for a transition state optimization is `SADDLEPOINT`. We can set up the input file using *MacMolPlt*. Open the log file for the optimization with bond distances set at 2.2&nbsp;Å and use `Subwindow` → `Input Builder`. Set the `Run Type` to `Hessian` and set the `MO Guess` to `Huckel` (we could have read the MO data from the .dat file for the previous calculation but we are using a low level of theory so we wont bother saving that small amount of time). In Hess. Options make sure that the Vibrational Analysis button is checked so he file is set to perform a vibrational anaysis so that we can identify an imaginary vibration (hopefully). Save the input file. The file is presented in {numref}`Cyclohexene_TS_Hess.inp`. 

```{code-block} 
---
name: Cyclohexene_TS_Hess.inp
linenos: True
lineno-start: 1
emphasize-lines: 2
caption: Cyclohexene_TS_Hess.inp
---
!   File created by MacMolPlt 7.7.2
 $CONTRL SCFTYP=RHF RUNTYP=HESSIAN EXETYP=RUN MAXIT=30 MULT=1
    MOLPLT=.TRUE. $END
 $SYSTEM TIMLIM=525600 MEMORY=1000000 PARALL=.TRUE. $END
 $BASIS GBASIS=N31 NGAUSS=6 NDFUNC=1 $END
 $GUESS GUESS=HUCKEL $END
 $SCF DIRSCF=.TRUE. $END
 $FORCE METHOD=ANALYTIC VIBANL=.TRUE. $END
 $DATA 
Cyclohexene
CS

C     6.0    -1.25696    -0.21327    -0.69596
C     6.0    -0.33240     0.51308    -1.41520
C     6.0     1.58158    -0.29544    -0.69202
H     1.0    -1.83544    -0.96446    -1.20729
H     1.0     1.46204    -1.22096    -1.22142
H     1.0    -0.28274     0.39582    -2.48412
H     1.0     2.14064     0.45769    -1.21783
H     1.0     0.00494     1.46786    -1.06282
 $END
```

The input file was submitted to *GAMESS* and was successful. Now open the log file for the calculation. Go to `Subwindow` → `Frequencies`. I observe that there is an imaginary frequency listed at the top of the list. Clicking on it reveals the vectors in the display window. Check the display and observe if the vectors allign with the reation coordinate. As we can see in {sumref}`fig8_10`, they do. This structure will lead to a transition state. We can now perform the saddlepoint optimiation.

```{figure} images/Diels_10.png
---
width: 600px
name: fig8_10
---
*Structure of the partial optimization with bond lengths of 2.2&nbsp;Å. The imaginary vibration is displayed.*
```

### The Transition State optimization

Open the log file for the Hessian calculation. Click on `Subwindow` → `Input Builder`. Set the `Run Type` to `Saddle Point`. Set # of `Z-matrix variables` to `42`. We will need to supply a `$ZMAT` group. Set `Stat. Point` → `Initial Hessian` to `Calculate` (again, we could have cut this out of the .dat file and included it in the input file but the time saving is minimal in this case). Save the input file.

To get a `$ZMAT` group we will again set up an energy check calcuylation with the internal coordinates set to auto generate. I will open the `Subwindow` → `Input Builder` and set the 'Run Type' to 'Energy' and the 'Exe. Type' to 'Check'. I will save the input file and then edit it to add the final line: `$ZMAT AUTO=.TRUE. DLC=.TRUE. NONVDW(1)=3,5, 4,6 $END`. The input file is presented in {numref}`Cyclohexene_TS_ZMAT_Check.inp`. The `NONVDW` list will be very important here as the bond length if far past what is expected for a covalent bond and would not be detected in the automatic internal coordinates otherwise.

```{code-block} 
---
name: Cyclohexene_TS_ZMAT_Check.inp
linenos: True
lineno-start: 1
emphasize-lines: 2
caption: Cyclohexene_TS_ZMAT_Check.inp
---
!   File created by MacMolPlt 7.7.2
 $CONTRL SCFTYP=RHF RUNTYP=ENERGY EXETYP=CHECK MAXIT=30 MULT=1 COORD=UNIQUE 
    NZVAR=42 MOLPLT=.TRUE. $END
 $SYSTEM TIMLIM=525600 MEMORY=1000000 $END
 $BASIS GBASIS=N31 NGAUSS=6 NDFUNC=1 $END
 $SCF DIRSCF=.TRUE. $END
 $DATA 
Cyclohexene
CS

C     6.0    -1.23614    -0.19463    -0.66001
C     6.0    -0.03784     0.34641    -1.40039
C     6.0     1.27863    -0.15469    -0.77504
H     1.0    -2.07996    -0.56134    -1.21953
H     1.0     1.45310    -1.16622    -1.12664
H     1.0    -0.07030     0.07059    -2.44931
H     1.0     2.10150     0.44450    -1.15258
H     1.0    -0.06272     1.43514    -1.37198
 $END
 $ZMAT AUTO=.TRUE. DLC=.TRUE. NONVDW(1)=3,5, 4,6 $END
```
Run the check calculation in GAMESS and hunt down the .dat file. Copy the $ZMAT group out of it and paste it into the saddlepoint input file. There are 89 entries in the `IZMAT` list so we must change the NZVAR from 42 to 89. With this list of interna;l coordinates established, *GAMESS* will report their values in the log file and we will be able to directly obtain the bond lengths for the 3,5 and 4,6 bonds in the transition state (assuming the calculation succeeds). The edited input file is displayed in {numref}`Cyclohexene_TS_ZMAT_Saddle.inp`.

```{code-block} 
---
name: Cyclohexene_TS_ZMAT_Saddle.inp
linenos: True
lineno-start: 1
emphasize-lines: 2
caption: Cyclohexene_TS_ZMAT_Saddle.inp
---
!   File created by MacMolPlt 7.7.2
 $CONTRL SCFTYP=RHF RUNTYP=SADPOINT MAXIT=30 MULT=1 NZVAR=89 MOLPLT=.TRUE. $END
 $SYSTEM TIMLIM=525600 MEMORY=1000000 PARALL=.TRUE. $END
 $BASIS GBASIS=N31 NGAUSS=6 NDFUNC=1 $END
 $GUESS GUESS=HUCKEL $END
 $SCF DIRSCF=.TRUE. $END
 $STATPT OPTTOL=1e-05 NSTEP=200 HESS=CALC HSSEND=.t. $END
 $FORCE METHOD=ANALYTIC VIBANL=.TRUE. $END
 $DATA 
Cyclohexene
CS

C     6.0    -1.25696    -0.21327    -0.69596
C     6.0    -0.33240     0.51308    -1.41520
C     6.0     1.58158    -0.29544    -0.69202
H     1.0    -1.83544    -0.96446    -1.20729
H     1.0     1.46204    -1.22096    -1.22142
H     1.0    -0.28274     0.39582    -2.48412
H     1.0     2.14064     0.45769    -1.21783
H     1.0     0.00494     1.46786    -1.06282
 $END
 $ZMAT   
 IZMAT(1)=
         1,   1,   2,
         1,   1,   3,
         1,   1,   7,
         1,   2,   4,
         1,   2,   8,
         1,   3,  15,
         1,   3,   5,
         1,   3,  11,
         1,   4,  16,
         1,   4,  12,
         1,   4,   6,
         1,   5,   9,
         1,   5,  13,
         1,   5,   6,
         1,   6,  14,
         1,   6,  10,
         2,   1,   3,  11,
         2,   1,   3,   5,
         2,   1,   3,  15,
         2,   1,   2,   8,
         2,   1,   2,   4,
         2,   2,   1,   3,
         2,   2,   4,   6,
         2,   2,   4,  16,
         2,   2,   1,   7,
         2,   2,   4,  12,
         2,   3,   1,   7,
         2,   3,   5,   6,
         2,   3,   5,  13,
         2,   3,   5,   9,
         2,   4,   6,  10,
         2,   4,   6,  14,
         2,   4,   6,   5,
         2,   4,   2,   8,
         2,   5,   3,  11,
         2,   5,   6,  10,
         2,   5,   6,  14,
         2,   5,   3,  15,
         2,   6,   5,  13,
         2,   6,   5,   9,
         2,   6,   4,  12,
         2,   6,   4,  16,
         2,   9,   5,  13,
         2,  10,   6,  14,
         2,  11,   3,  15,
         2,  12,   4,  16,
         3,   1,   2,   4,  12,
         3,   1,   3,   5,   6,
         3,   1,   2,   4,  16,
         3,   1,   3,   5,  13,
         3,   1,   3,   5,   9,
         3,   1,   2,   4,   6,
         3,   2,   4,   6,  10,
         3,   2,   1,   3,   5,
         3,   2,   4,   6,  14,
         3,   2,   1,   3,  11,
         3,   2,   4,   6,   5,
         3,   2,   1,   3,  15,
         3,   3,   1,   2,   4,
         3,   3,   1,   2,   8,
         3,   3,   5,   6,  10,
         3,   3,   5,   6,  14,
         3,   3,   5,   6,   4,
         3,   4,   6,   5,  13,
         3,   4,   6,   5,   9,
         3,   4,   2,   1,   7,
         3,   5,   6,   4,  12,
         3,   5,   6,   4,  16,
         3,   5,   3,   1,   7,
         3,   6,   4,   2,   8,
         3,   6,   5,   3,  11,
         3,   6,   5,   3,  15,
         3,   7,   1,   2,   8,
         3,   7,   1,   3,  15,
         3,   7,   1,   3,  11,
         3,   8,   2,   4,  16,
         3,   8,   2,   4,  12,
         3,   9,   5,   3,  11,
         3,   9,   5,   3,  15,
         3,   9,   5,   6,  14,
         3,   9,   5,   6,  10,
         3,  10,   6,   4,  12,
         3,  10,   6,   4,  16,
         3,  10,   6,   5,  13,
         3,  11,   3,   5,  13,
         3,  12,   4,   6,  14,
         3,  13,   5,   3,  15,
         3,  13,   5,   6,  14,
         3,  14,   6,   4,  16,
 $END
```
The calculation was succesful and the saddlepoint was immediately located.  We were almost exactly there. We started with a 3,5 and 6,4 bond length of 2.200&nbsp;Å and the sadlle point has a bond length of 2.202&nbsp;Å.


## Discussion of the Reaction Coordinate





