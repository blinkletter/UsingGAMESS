# Ethane: Symmetry in Calculations

Ethane can rotate freely along the C–C bond. The lowest energy conformation is the anti form and the highest energy is the syn form. It is easy to get GAMESS to optimize the anti structure, the software will seek the lowest energy state. How do we get the syn form? We could use ways to lock coordinates but another way is to enforce symmetry.

## Learning Goals

This exercise will hopefully accomplish the following goals while learning new skills:

1.	We will manually construct Z-matrices for larger molecules and identify an internal coordinate that defines the torsion angle between the two methyl groups of ethane.
2.	We will use the symmetry of the anti and syn conformations to lock their conformations
3.	We will determine optimized structure and the energy difference between the syn and anti-conformations and compare our results to literature values.

## Point Groups in Ethane

Each of the extreme cases in ethane has symmetry. They have different symmetry and so we can use that to our advantage. The symmetry of the syn conformation is $D_{3h}$ and for the anti it is $D_{3d}$. By declaring the symmetry group, the optimization will start with that symmetry and end with that symmetry. This will enforce the anti conformation for us. Additionally, by symmetry each molecule can be reduce to just two atoms for the purposes of the calculation. Using symmetry when possible will greatly reduce the cost of calculation.

## Z-Matrix for Ethane

We can start with a Z-matrix for ethane. If the structure described fits the symmetry group declared, then GAMESS will align it appropriately in the xyz coordinate system and identify the symmetry unique atoms. Take note of how the two methyl groups are set up so that they refer to their own atoms as much as possible and there is only one coordinate that describes the bond rotation. Below is the initial input file for the anti conformation with $D_{3d}$ symmetry.


**Ethane_anti_AM1_Z.inp**
```
 $CONTRL SCFTYP=RHF RUNTYP=OPTIMIZE MAXIT=30 MULT=1 ICHARG=0 
  COORD=ZMT $END
 $SYSTEM TIMLIM=525600 MEMORY=1000000 $END
 $BASIS GBASIS=AM1 $END
 $SCF DIRSCF=.TRUE. $END
 $STATPT OPTTOL=0.0001 NSTEP=100 $END
 $DATA 
anti ethane
DND 3

C  
C   1  1.5
H   2  1.0  1  110
H   2  1.0  1  110  3  120
H   2  1.0  1  110  3  -120
H   1  1.0  2  110  3  180
H   1  1.0  2  110  6  120
H   1  1.0  2  110  6  -120
 $END
```

## Calculating the Structure and Energy of Anti-Ethane

The result file produced the symmetry unique coordinates optimized at the AM1 level. I used those to construct an input file for the HF/6-311(d,p)++ optimization. That file is reproduced below. The IZMAT matrix was constructed using the ENCODED Z MATRIX section of the AM1 result file.

**Ethane_anti_6311_U.inp**
```
 $CONTRL SCFTYP=RHF RUNTYP=OPTIMIZE MAXIT=30 MULT=1 ICHARG=0 
  COORD=UNIQUE NZVAR=18 $END
 $SYSTEM TIMLIM=525600 MEMORY=1000000 $END
 $BASIS GBASIS=N311 NGAUSS=6 NDFUNC=1 NPFUNC=1 DIFFSP=.TRUE. DIFFS=.TRUE. $END
 $SCF DIRSCF=.TRUE. $END
 $STATPT OPTTOL=0.0001 NSTEP=20 $END
 $DATA 
anti ethane
DND 3

 C           6.0   0.0000000000   0.0000000000  -0.7501162007
 H           1.0   0.0000000000   1.0448521625   1.1453263085
 $END
 $ZMAT IZMAT(1)=1,1,2,
                1,8,1,  2,8,1,2,
                1,4,1,  2,4,1,2,  3,4,1,2,8,
                1,3,1,  2,3,1,2,  3,3,1,2,8,
                1,5,2,  2,5,2,1,  3,5,2,1,8,
                1,6,2,  2,6,2,1,  3,6,2,1,5,
                1,7,2,  2,7,2,6,  3,7,2,1,5   $END  
```

```{note}
I altered one of the IZMAT coordinates to correspond to a H–C–H bond angle. In the last line, I changes the `2,7,2,1` (an H–C–C angle) to `2,7,2,6` (an H–C–H angle.)
```

We get an energy from this calculation and a geometry that we can read from the INTERNAL COORDINATES section of the result file. This section is available because we set NZVAR=18 and provided the IZMAT list. Here is a summary of the calculated data at HF/6311(d,p)++ level. Note that the internal coordinates chosen by GAMESS are not in the same pattern as the Z-matrix. We can manually choose these coordinates if we wish, but the number or coordinates must match the number of degrees of freedom (3n-6) and the coordinates must be able to be used to describe the position of all atoms.

| Coordinate       | Value           |
| :-------         | :-------        |
| C–C length       |    1.527 Å      |
| C–H length       |    1.086 Å      |
| H–C–C angle      |  111.2˚         |
| H–C–H angle      |  107.7˚         |
| Energy (Ha)      | -79.2520118108  |


The absolute QM energy value is just a number until we compare it to a similar structure. In this case we will compare it to a very similar structure, the syn conformation. This is probably the best case scenario for calculating relative energies between two situations.

## The Syn Ethane Conformer

The syn structure had $D_{3h}$ symmetry and the Z-matrix is almost identical. We just had to change the one coordinate that defined the torsion angle between the two methyl groups. This is the 6,1,2,8 torsion angle (line 6 of the Z-matrix.) I just need to change the angle to zero degrees and the symmetry to $D_{3h}$ and repeat all the above. First we altered the anti input file and submitted the job.

```
Ethane_syn_AM1_Z.inp
 $CONTRL SCFTYP=RHF RUNTYP=OPTIMIZE MAXIT=30 MULT=1 ICHARG=0 
  COORD=ZMT $END
 $SYSTEM TIMLIM=525600 MEMORY=1000000 $END
 $BASIS GBASIS=AM1 $END
 $SCF DIRSCF=.TRUE. $END
 $STATPT OPTTOL=0.0001 NSTEP=100 $END
 $DATA 
anti ethane
DNH 3

C  
C   1  1.5
H   2  1.0  1  110
H   2  1.0  1  110  3  120
H   2  1.0  1  110  3  -120
H   1  1.0  2  110  3  0
H   1  1.0  2  110  6  120
H   1  1.0  2  110  6  -120
 $END
```

Then we used the unique coordinate generated to create the HF/6-311G(d,p)++ input file. Observe that the unique coordinates have been aligned by GAMESS into a different plane. In the $D_{3d}$ anti symmetry, the yz plane was used for the unique atoms, and in the $D_{3h}$ syn case, the xz plane was chosen.  The x-axis is the perpendicular 2-fold axis of symmetry (that defines the $D$ rather than $C$ point groups). This places the primary $\sigma_d$-plane in the yz plane for the anti conformation and in the xz for the syn conformation.  I had tried to just change the symmetry to $D_{3h}$ and use the previous unique $D_{3d}$ coordinates and the symmetry failed. Below is the HF/6-311G(d,p)++ input file.



**Ethane_syn_6311_U.inp**
```
 $CONTRL SCFTYP=RHF RUNTYP=OPTIMIZE MAXIT=30 MULT=1 ICHARG=0 
  COORD=UNIQUE NZVAR=18 $END
 $SYSTEM TIMLIM=525600 MEMORY=1000000 $END
 $BASIS GBASIS=N311 NGAUSS=6 NDFUNC=1 NPFUNC=1 DIFFSP=.TRUE. DIFFS=.TRUE. $END
 $SCF DIRSCF=.TRUE. $END
 $STATPT OPTTOL=0.0001 NSTEP=20 $END
 $DATA 
syn ethane
DNH 3

 C           6.0   0.0000000000  -0.0000000000  -0.7517425284
 H           1.0   1.0424482146   0.0000000000   1.1528384766
 $END
 $ZMAT IZMAT(1)=1,1,2,
                1,8,1,  2,8,1,2,
                1,4,1,  2,4,1,2,  3,4,1,2,8,
                1,3,1,  2,3,1,2,  3,3,1,2,8,
                1,5,2,  2,5,2,1,  3,5,2,1,8,
                1,6,2,  2,6,2,1,  3,6,2,1,5,
                1,7,2,  2,7,2,6,  3,7,2,1,5   $END  
```

By examining the output file, a summary of the result for the syn conformation can be made.

| Coordinate   | Value         |
| :-------     | :-------      |
| C–C length   |   1.541 Å     |
| C–H length   |   1.085 Å     |
| H–C–C angle  | 111.6˚        |
| H–C–H angle  | 107.2˚        |
| Energy (Ha)  | -79.2471515134|
   
We can now make some comparisons.

## Discussion

Here is the data gather together so that we can explore the differences in bond lengths, angles and molecular energy.

| Coordinate   | syn conformer | anti conformer |
| :-------     | :-------      | :---------     |
| C–C length   |      1.541 Å  |     1.527 Å    |
| C–H length   |      1.085 Å  |     1.086 Å    |
| H–C–C angle  |    111.6˚     |   111.2˚       |
| H–C–H angle  |    107.2˚     |   107.7˚       |
| $\Delta$E (kJ/mol)  |    +12.8      |     0          |

The C–C bond is shorter in the anti conformer, as expected. And the H–C–H angle was larger, as expected.
 
## Literature and The Controversy

The literature value for the ethane rotational energy barrier is 12.1 kJ/mole.[^Hirota1979]  We were pretty close with what today is considered a low level of theory. There has been lots of recent work in this subject. Despite its simplicity, or because of it, it has been a focus for theoretical investigations. It started with an argument that molecular orbital interactions stabilizing the anti conformation were the more important contributor to the energy difference compared to electronic repulsion in the syn conformation.[^Goodman2001]  This is an idea that has been floated since the 1970’s[^Lowe1973] but it gained new life with the Nature publication. People disagreed and the fight was on.[^Bickelhaupt2004] There are ongoing efforts to further refine the model for the energy difference.[^Baranac2015][^Mo2011]

## Summary

We have learned more about constructing a Z-matrix and applied this knowledge to design a Z-matrix for ethane within which we can easily create any torsion angle we wish. We have observed how defining symmetry can enforce a given conformation while optimizing a structure. We have observed that the structures and the energy difference were reasonably close to literature values.

In the exercise, you will also explore what happens when we remove the symmetry declaration. Go to the instructions for the exercise and have fun.

## Files

The following files were created during this tutorial and are available with this document. Feel free to use them as templates and cut and paste as you build the other calculations.

| Filename          | Notes |
| :----             | :---- |
| Ethane_syn_AM1_Z.inp	| The initial input the $D_{3h}$ symmetrical structure |
| Ethane_anti_AM1_Z.inp	| The initial input the $D_{3d}$ symmetrical structure |
| Ethane_syn_6311_U.inp	| An input file that you can modify for doing calculations at the HF/6311(d,p)++ level. |


[^Hirota1979]:  “Barrier to internal rotation in ethane from the microwave spectrum of CH$_3$CHD$_2$.” E. Hirota, S. Saito, Y. Endo,  *J. Chem. Phys.*, **1979**, *71*, 1183–1187. https://doi.org/10.1063/1.438464 
[^Goodman2001]: "Hyperconjugation not steric repulsion leads to the staggered structure of ethane". V. Pophristic, L. Goodman, *Nature*, **2001**, *411*, 565–8. https://doi.org/10.1038/35079036 
[^Lowe1973]: “The Barrier to Internal Rotation in Ethane: A qualitative, intuitively useful explanation emerges from a comparison of different theoretical approaches”, J.P. Lowe, *Science*, **1973**, *179*, 527-32. https://doi.org/10.1126/science.179.4073.527 .
[^Bickelhaupt2004]: "The case for steric repulsion causing the staggered conformation of ethane". F.M. Bickelhaupt, E.J. Baerends, *Angew. Chem. Int. Ed.*, **2003**, *42*, 4183–4188. https://doi.org/10.1002/anie.200350947 .
[^Baranac2015]: "Theoretical analysis of the rotational barrier in ethane: cause and consequences". M. Baranac-Stojanović, *Structural Chemistry*, **2015**, *26*, 989–996. https://doi.org/10.1007/s11224-014-0557-5
[^Mo2011]: “Rotational barriers in alkanes”, Y. Mo, *WIREs Comp. Mol. Sci.*, **2011**, *1*, 164-171. https://doi.org/10.1002/wcms.22 


## Exercise

Read the accompanying discussion above and then try the following activities.

### The Activities

Repeat the activities described in the discussion but edit the input files to add a command to output data for localized orbitals. After you have result files for the optimized $D_{3h}$ and $D_{3d}$ structures, produce images of the molecules that display bond lengths and angles. Then produce images showing graphic representations of the unique local bonding orbitals (one C–C $\sigma$-bond and one C–H $\sigma$-bond will suffice). Report the energy difference for the two symmetries (syn and anti). Then present images for the bonding MOs for both symmetries. Compare their energies and their symmetries and discuss which best represent which local bonds (or combinations thereof.)

Now set the symmetry of the syn structure to $C_1$ (no symmetry – this will allow free bond rotation.) Run the optimization at the AM1 level? Is the result syn or anti. Discuss the result. If the result remains syn propose why GAMESS could not bring itself to start the bond rotation. Now change the torsion angle by 0.1˚. Run the optimization again. Discus the result. Compare the energies of the C1 anti and the C1 syn structures at the HF/6-311G(d,p)++ level. Compare bond lengths and angles as well. Do they match with the results that used symmetry? 

### The Report

Create a ONE-PAGE document that presents the images of the molecules and local and molecular orbitals described above. Discuss the relative energies of the orbitals. Are there any degenerate sets? How many nodal planes are in each set? Can you see how the local orbitals could be combined to make the molecular orbitals?

Did fixing the symmetry also fix the bond angles in the syn configuration? Present the consequences of removing the symmetry constraint. If there was no change in torsion when the symmetry was removed propose a reason why. Why did a slight tip in the torsion angle solve the problem? Present the bond lengths and angles for the HF/6-311G(d,p)++ and discuss how they relate to the values with symmetry. 

Try running energy calculations at the HF/6-311G(d,p)++ level with and without symmetry and see if there is a difference in the time each calculation takes. Discuss the difference in time (there may be none as these are small molecules and modern personal computers are enormously powerful).

Include an appendix with the text for all the input files that you used (please do not include any result files – there will be no trees left!) For these files preface each with the file name and a note on its purpose and use a fixed-width font.

