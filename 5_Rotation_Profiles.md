# Butane: Rotation Energy Profiles

One of the easiest chemical **transformations** to model and explore in computational chemistry is **conformational** changes. We will start with potential energy profiles for **rotation**. We will build butane using the build tools in *wxMacMolPlt* and then submit the data to *GAMESS* as an optimization calculation via *GamessQ*.

No more symmetry (for now). If we want to rotate molecules around bonds, the symmetry will be **changing** with the rotation. Do consider that symmetry saved a lot of computational effort and should be considered carefully when using expensive methods. We will downgrade our **method** for optimizations to HF/3-21G

## Learning Goals

In this exercise, we will accomplish the following…

1.	Use *MacMolPlt* to **build** molecules, generate input files and **interpret** results. 
2.	**Freeze a coordinate** in a series of internal coordinates.
3.	**Change** the frozen coordinate and obtain the optimized structure and energy within that limitation.
4.	Learn **how to use** the command-line Unix tools *sed* and *grep* to generate a large series of input files with different values for the frozen coordinate and to **extract data** quickly from large numbers of files. We will submit all these files at once via *GamessQ*.
5.	With these methods we will create a **rotational energy profile** around a given bond in an alkane.

## Building Butane

Run *MacMolPlt*. Click on `Builder` &rarr; `Show Build Tools`. Choose carbon atoms and set the coordination number to 4 (four bonds to an sp3 carbon). Then click in the window to **build** the molecule, A carbon with four connections will appear. Then click on one of the connections to add a new carbon. When you have added all four carbon atoms, change the build tool to hydrogen and then click on the remaining connections to include bonds. In the end you will have a window that looks **like this** perhaps. 


```{figure} images/profiles_Picture1B.png
---
width: 600px
name: fig5-1
---
**MacMolPlt* window with the initial structure for butadiene.*
```
 
The structure in {numref}`fig5-1` is an initial **rough sketch**. Note that the terminal carbons are in *eclipsed* conformations. We will need to calculate the correct structure by creating an input file for *GAMESS*. Click on `Subwindow` &rarr; `Input Builder` and set the following **parameters**:

- In the `Control` menu section, set `Run Type` to `Optimization`. This will instruct *GAMESS* that we are doing a calculation to find the optimizes molecular geometry.
- In the `Basis` section, set `Basis Set` to `3-21G` and set `#D heavy atom polarizations functions` to `1`. This will run at the 3-21G
- In the `Data` section, set `Coord. Type` to `Z-Matrix` and set `# of Z-matrix variables` to `36` (14 atoms, so 3N – 6 = 36)
- In the `Misc. Prefs` section, check the `MolPlt` button. This will ensure that *GAMESS* outputs information in a format that can be read by the *MacMolPlt* application.
- Click on the `Edit and Save` button in the bottom of the `Input Builder` window. Then click on `Save As…` and save your file. Choose a name like `butane.inp`.

## Preparing to use *GAMESS*

We can now take the data file that was **written** out by *MacMolPlt* and use it as the input for *GAMESS*.

### The *GAMESS* Input File

**Open** the input file you just saved from *MacMolPlt* in a text editor.  You should see the following text…

```{code-block} 
---
name: butane.inp
linenos: True
lineno-start: 1
emphasize-lines: 2,5,14
caption: butane.inp
---
!   File created by MacMolPlt 7.7.2
 $CONTRL SCFTYP=RHF RUNTYP=OPTIMIZE MAXIT=30 MULT=1 COORD=ZMT NZVAR=36 
    MOLPLT=.TRUE. $END
 $SYSTEM TIMLIM=525600 MEMORY=1000000 $END
 $BASIS GBASIS=N21 NGAUSS=3 $END
 $SCF DIRSCF=.TRUE. $END
 $STATPT OPTTOL=0.0001 NSTEP=20 $END
 $DATA 
Butane
C1
C
C   1    1.54000
C   2    1.54000  1  109.4712
C   1    1.54000  2  109.4712  3 -180.0000
H   1    1.14000  2  109.4712  4 -120.0000
H   1    1.14000  5  109.4712  2  120.0000
H   2    1.14000  1  109.4712  3 -120.0000
H   2    1.14000  7  109.4712  1  120.0000
H   3    1.14000  2  109.4712  8    0.0000
H   3    1.14000  9  109.4712  2  120.0000
H   3    1.14000  9  109.4712  10 120.0000
H   4    1.14000  1  109.4712  6   -0.0000
H   4    1.14000  12 109.4712  1  120.0000
H   4    1.14000  12 109.4712  13 120.0000
 $END
 $ZMAT IZMAT(1)=1,2,1, 
                1,3,2,  2,3,2,1, 
                1,4,1,  2,4,1,2,   3,4,1,2,3, 
                1,5,1,  2,5,1,2,   3,5,1,2,4, 
                1,6,1,  2,6,1,5,   3,6,1,5,2, 
                1,7,2,  2,7,2,1,   3,7,2,1,3, 
                1,8,2,  2,8,2,7,   3,8,2,7,1, 
                1,9,3,  2,9,3,2,   3,9,3,2,8, 
                1,10,3, 2,10,3,9,  3,10,3,9,2, 
                1,11,3, 2,11,3,9,  3,11,3,9,10, 
                1,12,4, 2,12,4,1,  3,12,4,1,6, 
                1,13,4, 2,13,4,12, 3,13,4,12,1, 
                1,14,4, 2,14,4,12, 3,14,4,12,13 $END
```
```{note}
*Unix* comes with many text editors that will run in the terminal but most people would use a GUI tool. *BBedit* is a professional grade text editor and a free version is available for *MacOS* computers. Microsoft *Visual Studio Code* is also free.
```

### Interpreting The Input File

The *GAMESS* input file **starts** off with essential settings and information in the `$CONTRL`, `$SYSTEM`, `$BASIS`, `$SCF` and `$STATPT` groups. Each group **ends** with `$END`. The settings within each group will be discussed where needed as we proceed, and detailed information is found in the [*GAMESS* documentation](https://www.msg.chem.iastate.edu/GAMESS/)

```{Note}
All white space must be spaces, not tabs. And all lines that start with a \$ symbol must have that \$ symbol in the **second** column, not the first. Examine the above file and observe this fact.
```

The `$DATA` group contains the **description** of the molecule. The first line after the declaration of `$DATA` is the name of the molecule. You can change “Title” to “Butane” in the input builder if you wish.

The next line is the **symmetry**. We are not using symmetry, so the symmetry point group is declared to be *C<sub>1</sub>* (no symmetry). Using symmetry will greatly reduce the work of the calculation. We will ignore this useful idea for now.

The next line begins the **structure** of the molecule. We could use an *xyz* coordinate system but that is a block of numbers that can be difficult to interpret. We will use **internal coordinates** that describe each atoms relationship to another atom or atoms. This will make more sense when examined by the human eye and allows for greater control in setting up initial **geometries** and bond angles. The internal coordinate system that we will use is the *Z-matrix*

### The *Z-Matrix*

The *Z-matrix* for butane is composed of 14 lines for the 14 atoms. Here is the *Z-matrix* that was produced by *MacMolPlt*.

```
C
C   1    1.54000
C   2    1.54000  1  109.4712
C   1    1.54000  2  109.4712  3 -180.0000
H   1    1.14000  2  109.4712  4 -120.0000
H   1    1.14000  5  109.4712  2  120.0000
H   2    1.14000  1  109.4712  3 -120.0000
H   2    1.14000  7  109.4712  1  120.0000
H   3    1.14000  2  109.4712  8    0.0000
H   3    1.14000  9  109.4712  2  120.0000
H   3    1.14000  9  109.4712  10 120.0000
H   4    1.14000  1  109.4712  6   -0.0000
H   4    1.14000  12 109.4712  1  120.0000
H   4    1.14000  12 109.4712  13 120.0000
```

Let us build the *Z-matrix* **line by line** using the example above.

The **first** atom in the matrix is a carbon and will be atom \#1 in the system. 

```
C
```

The **second** atom is also a carbon and will be atom \#2. It is 1.54 Å away from that atom \#1. For two atoms, all we need to define the molecule is that single **bond lengt**h value.

```
C
C   1    1.54000
```

The **third** line is atom \#3. In this matrix it describes the third carbon atom in butadiene. It will be 1.54 Å from atom \#2 but now the distance no longer completely describes its position in the system. We know the **distance** from atom \#2 to this atom \#3, but we also now need a bond **angle** between atoms \#3, 2 and 1. In *sp<sup>3</sup>* carbons that angle is 109.4˚ (120 for *sp<sup>2</sup>* and 180˚ for *sp*).

```
C
C   1    1.54000
C   2    1.54000  1  109.4712
```

The **fourth** line describes the fourth carbon atom, atom \#4. It is 1.54 Å from atom \#1. The bond angle between atoms \#4, 1, and 2 is 109.5˚. However, this is not enough information for four atoms. Three atoms are in a **plane**, by definition. Distance and angle will locate them all. However, a fourth atom is potentially outside of the plane of the first three. We now will add the angle to that fourth atom relative to the plane of the first three. This is a **dihedral angle**. In the case of our structure, the angle of the bond between atoms \#4 and \#1 relative to the plane of atoms \#1, 2 and 3 is 180˚. That is the same as saying that the plane described by \#1,2,3 is 180˚ relative to the plane described by \#4,1,2.

This fourth line is very important. This dihedral angle is the **bond rotation** along the central C–C bond. This is the angle we will be using to rotate the centre bond of butane. {numref}`fig5-2A` shows the `Z-matrix` so far.

```
C
C   1    1.54000
C   2    1.54000  1  109.4712
C   1    1.54000  2  109.4712  3  -180.0000
```

And that describes the following structures as we read each line…

```{figure} images/profiles_Picture2A.png
---
width: 500px
name: fig5-2A
---
*The 10th line of the *Z-matrix* is applied.*
```
 
By the **last line**, we will have constructed the following molecule. Note how the tenth line describes the bond, bond angle and dihedral angle for hydrogen atom #10 as shown in {numref}`fig5-2`.

```{figure} images/profiles_Picture2.png
---
width: 700px
name: fig5-2
---
*The 10th line of the *Z-matrix* is applied.*
```

We now have our molecule with the nuclei **positioned** in space (relative to each other via internal coordinates). The *GAMESS* program will place the nuclei in a Cartesian space and then calculate the locations of electrons from first principles using *ab initio* quantum mechanical calculations. We did tell *GAMESS* that all electrons were **paired** (no radicals) by using the `MULT=1` parameter and we did not specify a charge so that means there is no charge by **default**. 

We must always start **close** to the correct structure so that the calculation will snap to the closest lower energy minimum. If we **start** crazy, we might just **end up** crazy.

The final `$ZMAT` group describes a list of **descriptors** for every bond length, bond angle and dihedral angle. We will leave it be for now but will return to it soon.

## Finding Optimal Structure Using *GAMESS*

### Optimizing the Structure

Now we will feed the input file into the *GAMESS* program. **Run** the *GamessQ* program. You will get a window. **Drag** your input file into the window. *GamessQ* will ask you how many processors to use. Choose "one" for now. Your modern computer probably has 4 cores or more so we can always throw more power at the problem but this small calculation won’t need any heavy iron.

The job will **run** and produce an output file that will **contain** a description of the structure with the minimum overall energy. This might be the most stable structure for our molecule.

### The Output File

A **detailed** discussion of a *GAMESS* **output file** is presented in the next chapter where we repeat this exercise with butadiene. There will also be a discussion of useful *Unix* tools for making everything that we do here much easier. For now we will do things the **hard way**.

The *GamessQ* program will copy the input file and produce an output file to the folder designated it its preference pane. The file will have a number **appended**. In our case, the input file was named butane.inp.  The files written are the copy of the input file and the output file. In this case they were: butane_246.inp and butane_246.log. (Yes, I have run 245 jobs already trying to figure out how to use *GAMESS*.)

The log file has **thousands of lines** of text (assuming it didn’t crash out with an error because I goofed up the input file.) There is ultimately a line that states `EXECUTION OF GAMESS TERMINATED NORMALLY`. Open the log file and **search** for the word `NORMALLY` in the text. The phrase should appear near the end of the file. If you find the word `ABNORMALLY` instead, then the run has crashed out. **Error information** will be in the file to troubleshoot. Crashes are almost always a problem with the input file.

The run exited in a controlled manner, but that does not mean that things went well. Let us examine the butane_246.log file. **Each step** of the search for an energy minimum involved calculating the **function** that describes the energy and then calculating the **derivative** of that function for each atom. The derivative is the gradient (a slope). If the gradient is zero then we are at a **stationary point** (either a maximum or minimum) and if the slope has a value then there is a **direction** downhill. *GAMESS* will calculate the change for each atom that will **follow** that gradient. The change will be applied to each atom and the new structure will be recalculated. This will repeat until the total gradient for the molecule has reached a very small value, indicating that we are at the **bottom** (or top!) of an energy surface. 

### Are We Done?

Each **step** in initiated in the text of the log file by the term `NSERCH`. If we **search** through the text file until the last time `NSERCH` appears we will find the **final** structural calculation and result (there are better ways to do this.) In our case we see the last line containing `NSERCH` is…
```
NSERCH:  20  E=     -156.4322927357  GRAD. MAX=  0.0017274  R.M.S.=  0.0008046
```
The **maximum** number of iterations was set to 20 in the input file (look for NSTEP=20 in the butane.inp file). So we have **reached that maximum**. Just a few lines later we get the news…
```
      ***** FAILURE TO LOCATE STATIONARY POINT, TOO MANY STEPS TAKEN *****
```
So no, we are **not done**. We need to set `NSTEP` to a higher number. Normally 20 steps is **enough** and we are likely close. I will open butane.inp in a text editor and change `NSTEP=20` to `NSTEP=30`.

### Optimized Structure and Energy

The new output file generated is butane_247.log and the final line containing NSERCH is…
```
NSERCH:  28  E=     -156.4324667260  GRAD. MAX=  0.0000511  R.M.S.=  0.0000220
```
We **reached the end** of the calculation before the maximum number of steps. We also see the line…
```
       ***** EQUILIBRIUM GEOMETRY LOCATED *****
```
…So we now know that *GAMESS* has declared the calculation a **success**.

We can **open** the log file in *MacMolPlt* and it will **display** the final structure shown in {numref}`fig5-3`. There is a **slider** at the bottom of the window that will show all the structures in the **journey** if you scrub it back and forth. 


```{figure} images/profiles_Picture3.png
---
width: 600px
name: fig5-3
---
*The optimized structure as calculated by *GAMESS*.*
```

Immediately after the last `NSERCH` line is a series of data blocks containing the **structural information**. We can see the molecule described in Cartesian *xyz* coordinates. Following that, we see a block that describes all the **internal coordinates** (bond lengths, angles and torsions). There are 36 such coordinates and observe how each **corresponds** to an entry in the `$ZMAT` group at the end of the butane.inp input file. This data block is reproduced below.

```{code-block} 
---
name: butane_247.log
linenos: True
lineno-start: 8834
emphasize-lines: 13
caption: butane_247.log
---
                     --------------------
                     INTERNAL COORDINATES
                     --------------------

                 - - ATOMS - -         COORDINATE      COORDINATE
 NO.   TYPE    I  J  K  L  M  N        (BOHR,RAD)       (ANG,DEG)
 ----------------------------------------------------------------
   1 STRETCH   2  1                     2.9108112       1.5403351
   2 STRETCH   3  2                     2.9117022       1.5408066
   3 BEND      3  2  1                  1.9568840     112.1211961
   4 STRETCH   4  1                     2.9117022       1.5408065
   5 BEND      4  1  2                  1.9568842     112.1212082
   6 TORSION   4  1  2  3              -3.1414618    -179.9925051
   7 STRETCH   5  1                     2.0519139       1.0858261
   8 BEND      5  1  2                  1.9050638     109.1521181
   9 TORSION   5  1  2  4              -2.1213243    -121.5429320
  10 STRETCH   6  1                     2.0519041       1.0858210
  11 BEND      6  1  5                  1.8712475     107.2145814
  12 TORSION   6  1  5  2               2.0616607     118.1244578
  13 STRETCH   7  2                     2.0519138       1.0858261
  14 BEND      7  2  1                  1.9050635     109.1520961
  15 TORSION   7  2  1  3              -2.1213244    -121.5429333
  16 STRETCH   8  2                     2.0519041       1.0858210
  17 BEND      8  2  7                  1.8712471     107.2145635
  18 TORSION   8  2  7  1               2.0616608     118.1244625
  19 STRETCH   9  3                     2.0493776       1.0844840
  20 BEND      9  3  2                  1.9395112     111.1258057
  21 TORSION   9  3  2  8               1.0234135      58.6372736
  22 STRETCH  10  3                     2.0503225       1.0849840
  23 BEND     10  3  9                  1.8878418     108.1653650
  24 TORSION  10  3  9  2               2.1211950     121.5355228
  25 STRETCH  11  3                     2.0503015       1.0849729
  26 BEND     11  3  9                  1.8881259     108.1816436
  27 TORSION  11  3  9 10               2.0404044     116.9065612
  28 STRETCH  12  4                     2.0493776       1.0844840
  29 BEND     12  4  1                  1.9395113     111.1258133
  30 TORSION  12  4  1  6               1.0234135      58.6372723
  31 STRETCH  13  4                     2.0503225       1.0849840
  32 BEND     13  4 12                  1.8878418     108.1653687
  33 TORSION  13  4 12  1               2.1211951     121.5355240
  34 STRETCH  14  4                     2.0503015       1.0849729
  35 BEND     14  4 12                  1.8881259     108.1816474
  36 TORSION  14  4 12 13               2.0404045     116.9065642
```

The sixth coordinate in the list describes the **torsion** around the central C—C bond (atoms 1 and 2) as described by the **dihedral angle** between the bonds to the other two carbons. See {numref}`fig5-4` for a diagram describing that coordinate.


```{figure} images/profiles_Picture4.png
---
width: 600px
name: fig5-4
---
*The coordinate describing the central C–C bond torsion.*
```

We have found the **structure and energy** of the most stable conformer, the *anti* conformer. 

## The Other Conformer

We started the calculation above with a structure that was already *anti* in conformation. It is no surprise that we then **settled** into a bottom of an energy well that describes that situation.

There is another **stable** conformer, the *gauche* conformer. In this conformer the torsion angle should be near 60˚. If we set the 4,1,2,3 bond torsion to 60˚ in the input file and then run an optimization calculation, *GAMESS* will settle down into the **nearest** energy well, which should be the *gauche* conformer.

Let us open the butane.inp file again with the text editor. We will **change** only the value for the 4,1,2,3 torsion angle. The new file is shown below. We will name it as butane60.inp.

```{code-block} 
---
name: butane60.inp
linenos: True
lineno-start: 7568
emphasize-lines: 14
caption: butane60.inp
---
!   File created by MacMolPlt 7.7.2
 $CONTRL SCFTYP=RHF RUNTYP=OPTIMIZE MAXIT=30 MULT=1 COORD=ZMT NZVAR=36 
    MOLPLT=.TRUE. $END
 $SYSTEM TIMLIM=525600 MEMORY=1000000 $END
 $BASIS GBASIS=N21 NGAUSS=3 $END
 $SCF DIRSCF=.TRUE. $END
 $STATPT OPTTOL=0.0001 NSTEP=30 $END
 $DATA 
Butane
C1
C
C   1    1.54000
C   2    1.54000  1  109.4712
C   1    1.54000  2  109.4712  3   60.0000
H   1    1.14000  2  109.4712  4 -120.0000
H   1    1.14000  5  109.4712  2  120.0000
H   2    1.14000  1  109.4712  3 -120.0000
H   2    1.14000  7  109.4712  1  120.0000
H   3    1.14000  2  109.4712  8    0.0000
H   3    1.14000  9  109.4712  2  120.0000
H   3    1.14000  9  109.4712  10 120.0000
H   4    1.14000  1  109.4712  6   -0.0000
H   4    1.14000  12 109.4712  1  120.0000
H   4    1.14000  12 109.4712  13 120.0000
 $END
 $ZMAT IZMAT(1)=1,2,1, 1,3,2, 2,3,2,1, 1,4,1, 2,4,1,2, 3,4,1,2,3, 1,5,1, 
    2,5,1,2, 3,5,1,2,4, 1,6,1, 2,6,1,5, 3,6,1,5,2, 1,7,2, 2,7,2,1, 3,7,2,1,3, 
    1,8,2, 2,8,2,7, 3,8,2,7,1, 1,9,3, 2,9,3,2, 3,9,3,2,8, 1,10,3, 2,10,3,9, 
    3,10,3,9,2, 1,11,3, 2,11,3,9, 3,11,3,9,10, 1,12,4, 2,12,4,1, 3,12,4,1,6, 
    1,13,4, 2,13,4,12, 3,13,4,12,1, 1,14,4, 2,14,4,12, 3,14,4,12,13 $END
```

We **submit** the job via *GamessQ* and the **log file** butane60_248.log is produced. Searching for the last occurrence of NSERCH reveals that we have reached a **final structure** after 23 steps.

```
NSERCH:  23  E=     -156.4312439164  GRAD. MAX=  0.0000721  R.M.S.=  0.0000279
```
Examining the first 10 lines of the **internal coordinates** of the result shows that the central C–C torsion is 67˚. This is very close to the expected value. It is not exactly 60˚ because of the **steric size** of the methyl group.

```{code-block} 
---
name: butane60_248.log1
linenos: True
lineno-start: 1
emphasize-lines: 13
caption: butane60_248.log
---
                     --------------------
                     INTERNAL COORDINATES
                     --------------------

                 - - ATOMS - -         COORDINATE      COORDINATE
 NO.   TYPE    I  J  K  L  M  N        (BOHR,RAD)       (ANG,DEG)
 ----------------------------------------------------------------
   1 STRETCH   2  1                     2.9158702       1.5430121
   2 STRETCH   3  2                     2.9128559       1.5414171
   3 BEND      3  2  1                  1.9742294     113.1150123
   4 STRETCH   4  1                     2.9128532       1.5414156
   5 BEND      4  1  2                  1.9742485     113.1161071
   6 TORSION   4  1  2  3               1.1739939      67.2648974
   7 STRETCH   5  1                     2.0521415       1.0859466
   8 BEND      5  1  2                  1.9051708     109.1582461
...Lines Removed...
```

## Communication The Results

We can use *MacMolPlt* to create **images** of the two results. We will load in the log file of each. As an example we will use the most recent result stored as butane60_248.log. I will use the mouse pointer to select the four carbon atoms. Then I will **display** the value of the dihedral angle by choosing `View` &rarr; `Annotations` &rarr; `Display Dihedral`. I then choose `File` &rarr; `Export…` and export the image as PNG. There are many settings here, feel free to explore. In the end I generated the two images shown in {numref}`fig5-5`.

```{figure} images/profiles_Picture5.png
---
width: 500px
name: fig5-5
---
*The optimized *gauche* and *anti* conformations*
```

## The Energy

The energy of each **structure** was calculated.  The energy reported is the “energy of atomization.” This is the energy released when these atoms come together. If a gas of neutral carbon atoms (only 4 electrons in their valence shells – very unhappy) combined with neutral hydrogen atoms (also with unfilled valence shells) then the **energy** reported by *GAMESS* is what is released (per molecule). The unit for this atomization energy is Hartrees.

One **Hartree** (*Ha*) is 4.3597 &times; 10<sup>−18</sup> *J*. When we **multiply** by Avogadro’s number we get 2625.50 *kJ/mole*

The **energies** for the final structures in our two calculations are: E = -156.4324667260 *Ha* for the *anti* conformer and E = -156.4312439164 *Ha* for the *gauche* conformer. The difference is 0.001223 *Ha*. This comes out to 3.21 *kJ/mole*. The **literature** vale is 3.8 *kJ/mole*, so even this low level of theory (3-21G) performed well.

## Freezing a Coordinate

Allowing the structure to **relax** to minimums at torsional angles of near 180˚ (*anti*) and 60˚ (*gauche*) merely requires **allowing** it to happen. But how do we optimize a structure for a maximum? The *syn* conformer and the *eclipsed* conformer are each **peaks** in energy. We can **freeze** the value for any of the coordinates in the `$ZMAT` group using the `IFREEZ` setting within the `$STATPT` group.

The sixth coordinate in the `$ZMAT` group is for the central C–C bond **torsion**. If we add the command `IFREEZ(1)=6` then the value of that **internal coordinate** will not be able to change.  All the other bond lengths, angles and torsions will seek their lowest energy so we will hopefully find the lowest energy versions of the *syn* and *eclipsed* conformations.

I will use a text editor to change our input file. We will change the `4,1,2,3` torsion to `0˚` (*syn*) and then lock the sixth coordinate in the `$ZMAT` group that **corresponds** to that internal coordinate. The new input file is shown below.

```{code-block} 
---
name: butane_scan_0.inp1
linenos: True
lineno-start: 1
emphasize-lines: 14
caption: butane_scan_0.inp
---
!   File created by MacMolPlt 7.7.2
 $CONTRL SCFTYP=RHF RUNTYP=OPTIMIZE MAXIT=30 MULT=1 COORD=ZMT NZVAR=36 
    MOLPLT=.TRUE. $END
 $SYSTEM TIMLIM=525600 MEMORY=1000000 $END
 $BASIS GBASIS=N21 NGAUSS=3 $END
 $SCF DIRSCF=.TRUE. $END
 $STATPT OPTTOL=0.0001 NSTEP=50 IFREEZ(1)=6 $END
 $DATA 
Butane
C1
C
C   1    1.54000
C   2    1.54000  1 109.4712
C   1    1.54000  2 109.4712   3    0.0000
H   1    1.14000  2 109.4712   4 -120.0000
H   1    1.14000  5 109.4712   2  120.0000
H   2    1.14000  1 109.4712   3 -120.0000
H   2    1.14000  7 109.4712   1  120.0000
H   3    1.14000  2 109.4712   8    0.0000
H   3    1.14000  9 109.4712   2  120.0000
H   3    1.14000  9 109.4712  10  120.0000
H   4    1.14000  1 109.4712   6   -0.0000
H   4    1.14000  12 109.4712  1  120.0000
H   4    1.14000  12 109.4712 13  120.0000
 $END
 $ZMAT IZMAT(1)=1,2,1, 1,3,2, 2,3,2,1, 1,4,1, 2,4,1,2, 3,4,1,2,3, 1,5,1, 
    2,5,1,2, 3,5,1,2,4, 1,6,1, 2,6,1,5, 3,6,1,5,2, 1,7,2, 2,7,2,1, 3,7,2,1,3, 
    1,8,2, 2,8,2,7, 3,8,2,7,1, 1,9,3, 2,9,3,2, 3,9,3,2,8, 1,10,3, 2,10,3,9, 
    3,10,3,9,2, 1,11,3, 2,11,3,9, 3,11,3,9,10, 1,12,4, 2,12,4,1, 3,12,4,1,6, 
    1,13,4, 2,13,4,12, 3,13,4,12,1, 1,14,4, 2,14,4,12, 3,14,4,12,13 $END
```

The calculation **failed** because of the high symmetry of this `Z-matrix`. I found this **error message** new the end of a short log file.

```
UNABLE TO GENERATE PRINCIPAL AXES 
```

The **zero degree** torsion resulted in a situation where *GAMESS* was **unable** to take a guess at which atoms to place along the primary axis (the *z*-axis in most calculations). When this happens all we need to do is **mess up** the symmetry of the input file. I’m going to **change** a few of the 120.000 values to 119.000 and see if that helps.

It did help. *GAMESS* converts your *Z-matrix* into Cartesian *xyz* data for the calculation. If it cannot decide how your molecule relates to the three axes then it will choke. If you get an error like the above just tweak a few values to break symmetry. Here is the **final energy** reported.

```
NSERCH:  23  E=     -156.4228465004  GRAD. MAX=  0.0000753  R.M.S.=  0.0000261
```

I then set the **torsion angle** to 120˚ (*eclipsed*) and submitted the calculation again. I searched the log file for the final NSERCH line and again found an energy for the optimized **structure** with the C–C torsion frozen at 120˚. The reported energy was…

```
NSERCH:  26  E=     -156.4267263644  GRAD. MAX=  0.0000638  R.M.S.=  0.0000200
```

## The Energy Profile

We now have points for **all four** identified conformers. If we use the *anti* conformer as the base, we can calculate the difference in energy to the two maximums. We calculate that the *anti* conformer is $25.3 \, kJ/mole$ higher in energy and the *eclipsed* conformer is $15.2 \, kJ/mole$.

We could use this information to **sketch** out the rotational energy profile. The line in {numref}`fig5-6` is just drawn in and has no mathematical value, although it’s likely close to how the energy changes with torsion angle. Remember, we are using a low level of theory and are in **gas phase**, so accuracy will be low but the trend is clear.

```{figure} images/profiles_Picture6.png
---
width: 500px
name: fig5-6
---
*Rotational energy profile for butane.*
```

We can display images that represent the minimized structures for the *syn* and *eclipsed* conformers using *MacMolPlt* as we did above. See {numref}`fig5-7`.

```{figure} images/profiles_Picture7.png
---
width: 600px
name: fig5-7
---
*The calculated structure for the *anti*, *eclipsed*, *gauche*, and *syn* conformers.*
```

We can **repeat** these calculations again and again using **different values** for the 4,1,2,3 torsion. All it takes is typing and time.

In the **next chapter** you will see ways to use the power of your computer and *Unix* tools to enable these operations to be **done quickly**. Below is a plot of data points between zero and 180˚. I performed calculations at 5˚ intervals. It took only minutes to manually **create** the 36 input files and then drop them all into *GamessQ*. After a pause to brew a coffee, the jobs finished (it is a low cost level of theory – we could use basis sets that would result in run times of days on my little desktop computer.) I then was able to **extract** the energies with a single command and get a **plot** in less than a minute of effort. That is the power of *Unix*. See {numref}`fig5-8`


```{figure} images/profiles_Picture8.png
---
width: 500px
name: fig5-8
---
*Rotational energy profile for butane at 3-21G level.*
```

### Higher Level Theory

For fun I set up a **calculation** for a scan of the central C–C torsion using the 6-311G(d,p)++ level of theory. I selected the 6-31G basis set. Then I set the `# D atom polarization functions` to 1 and the `# Light atom polarization functions` to 1. {numref}`fig5-9` is a plot of the 3-21G level compared to the 6-311G(d,p)++ level.

```{figure} images/profiles_Picture9.png
---
width: 500px
name: fig5-9
---
*Rotational energy profile for butane at 3-21G (black) and 6-311G(d,p)++ level (orange).*
```

You can see that they are very similar. The **torsion angle** for the *gauche* conformer was calculated to be 65˚ when using the 6-311G(d,p)++ basis set (compared to 67˚). The **energy profile** is very similar. When using 1st and 2nd row elements with no charges or strained bonds, the 3-21G basis set gives good results. 

## Using Unix

Using the *Unix* skills described in the Setting Up *GAMESS* document, we can **manipulate** the text output files to **extract** important bits of information. First open a window in your terminal emulator.

### Extracting Information

We will now extract just the **lines that we want** from the large log file. *grep* is a tool that can be called from the shell. It will read the file line by line and return only the lines that contain a given text string. 
The command `grep "NSERCH" butane60_248.log > energy.txt` will extract the text lines that I observed contained both the calculated energy and the step number for each optimization step. The file `energy.txt` now **contains** the following content.

```
BEGINNING GEOMETRY SEARCH POINT NSERCH=   0 ...
          NSERCH=  0     ENERGY=    -156.3973907
 NSERCH:   0  E=     -156.3973906884  GRAD. MAX=  0.0345239  R.M.S.=  0.0202989
 BEGINNING GEOMETRY SEARCH POINT NSERCH=   1 ...
          NSERCH=  1     ENERGY=    -156.4193191
 NSERCH:   1  E=     -156.4193191232  GRAD. MAX=  0.0156691  R.M.S.=  0.0064738
 BEGINNING GEOMETRY SEARCH POINT NSERCH=   2 ...
          NSERCH=  2     ENERGY=    -156.4203894
 NSERCH:   2  E=     -156.4203894091  GRAD. MAX=  0.0120703  R.M.S.=  0.0050416
 BEGINNING GEOMETRY SEARCH POINT NSERCH=   3 ...
          NSERCH=  3     ENERGY=    -156.4216985
 NSERCH:   3  E=     -156.4216985281  GRAD. MAX=  0.0038327  R.M.S.=  0.0014703
................................. 42 Lines Removed.................................
NSERCH:  17  E=     -156.4310603910  GRAD. MAX=  0.0005127  R.M.S.=  0.0001197
 BEGINNING GEOMETRY SEARCH POINT NSERCH=  18 ...
          NSERCH= 18     ENERGY=    -156.4310612
 NSERCH:  18  E=     -156.4310612168  GRAD. MAX=  0.0002001  R.M.S.=  0.0000740
 BEGINNING GEOMETRY SEARCH POINT NSERCH=  19 ...
          NSERCH= 19     ENERGY=    -156.4310616
 NSERCH:  19  E=     -156.4310615872  GRAD. MAX=  0.0000573  R.M.S.=  0.0000161 
```
You can see that this is **every** line in the file that includes the string `NSERCH`. I want just the lines that **contain** the energy and the gradient. So I will *grep* this file again for `GRAD`.

The command `grep "GRAD" energy.txt > energy2.txt` will produce the file named `energy2.txt` that contains the following lines.
```
 NSERCH:   0  E=     -156.3973906884  GRAD. MAX=  0.0345239  R.M.S.=  0.0202989
 NSERCH:   1  E=     -156.4193191232  GRAD. MAX=  0.0156691  R.M.S.=  0.0064738
 NSERCH:   2  E=     -156.4203894091  GRAD. MAX=  0.0120703  R.M.S.=  0.0050416
 NSERCH:   3  E=     -156.4216985281  GRAD. MAX=  0.0038327  R.M.S.=  0.0014703
 NSERCH:   4  E=     -156.4217778293  GRAD. MAX=  0.0030297  R.M.S.=  0.0011089
 NSERCH:   5  E=     -156.4218675393  GRAD. MAX=  0.0016220  R.M.S.=  0.0006746
....7 Lines Removed.............................................................
 NSERCH:  13  E=     -156.4284752043  GRAD. MAX=  0.0145371  R.M.S.=  0.0042503
 NSERCH:  14  E=     -156.4297571137  GRAD. MAX=  0.0059127  R.M.S.=  0.0020276
 NSERCH:  15  E=     -156.4309126800  GRAD. MAX=  0.0023459  R.M.S.=  0.0007784
 NSERCH:  16  E=     -156.4310541268  GRAD. MAX=  0.0010362  R.M.S.=  0.0003577
 NSERCH:  17  E=     -156.4310603910  GRAD. MAX=  0.0005127  R.M.S.=  0.0001197
 NSERCH:  18  E=     -156.4310612168  GRAD. MAX=  0.0002001  R.M.S.=  0.0000740
 NSERCH:  19  E=     -156.4310615872  GRAD. MAX=  0.0000573  R.M.S.=  0.0000161 
```

I can then import `energy2.txt` into a spreadsheet program or **pandas dataframe** and make a graph of the energy and the gradient as we go through the steps. In {numref}`fig5-10A` and {numref}`fig5-10B`, we see these plots. The energy in the **result table** was in Hartrees, a unit common in computational chemistry. We will convert to *kJ/mole*. 
   
```{figure} images/profiles_Picture10A.png
---
width: 500px
name: fig5-10A
---
*Plot of relative energy energy at each optimization step as the minimization proceeds.*
```
```{figure} images/profiles_Picture10B.png
---
width: 500px
name: fig5-10B
---
*Plot of the gradient calculated before each optimization step.*
```

The energy **changes** quickly in the first few steps and then we keep making small changes until the *GAMESS* program halted the optimization. There was one phase where the process found a **steeper** path to the finish line. It’s like going down a ski hill. You will always follow the **steepest** line from where you are standing, not always the best line. And you will encounter trees occasionally.

Instead of **searching** through the output file for the energy and gradient at each step, we used *grep* to extract the lines that we needed automatically.

### Making Many Similar Files

We can use *Unix* tools to quickly produce a series of files for the **scan** of the torsion coordinate for the central C–C bond of butane.

First I will create a **new version** of the input file that we have been using and I will replace the value for the frozen torsion coordinate with the string `NUMBER`.
 
Below is the new input file

```{code-block} 
---
name: butane-SCAN.inp1
linenos: True
lineno-start: 1
emphasize-lines: 14
caption: butane-SCAN.inp
---
!   File created by MacMolPlt 7.7.2
 $CONTRL SCFTYP=RHF RUNTYP=OPTIMIZE MAXIT=30 MULT=1 COORD=ZMT NZVAR=36 
    MOLPLT=.TRUE. $END
 $SYSTEM TIMLIM=525600 MEMORY=1000000 $END
 $BASIS GBASIS=N21 NGAUSS=3 $END
 $SCF DIRSCF=.TRUE. $END
 $STATPT OPTTOL=0.0001 NSTEP=1000 IFREEZ(1)=6 $END
 $DATA 
Butane
C1
C
C   1    1.54000
C   2    1.54000  1 109.4712
C   1    1.54000  2 109.4712   3   NUMBER
H   1    1.14000  2 109.4712   4 -120.0000
H   1    1.14000  5 109.4712   2  120.0000
H   2    1.14000  1 109.4712   3 -120.0000
H   2    1.14000  7 109.4712   1  120.0000
H   3    1.14000  2 109.4712   8    0.0000
H   3    1.14000  9 109.4712   2  120.0000
H   3    1.14000  9 109.4712  10  120.0000
H   4    1.14000  1 109.4712   6   -0.0000
H   4    1.14000  12 109.4712  1  120.0000
H   4    1.14000  12 109.4712 13  119.0000
 $END
 $ZMAT IZMAT(1)=1,2,1, 1,3,2, 2,3,2,1, 1,4,1, 2,4,1,2, 3,4,1,2,3, 1,5,1, 
    2,5,1,2, 3,5,1,2,4, 1,6,1, 2,6,1,5, 3,6,1,5,2, 1,7,2, 2,7,2,1, 3,7,2,1,3, 
    1,8,2, 2,8,2,7, 3,8,2,7,1, 1,9,3, 2,9,3,2, 3,9,3,2,8, 1,10,3, 2,10,3,9, 
    3,10,3,9,2, 1,11,3, 2,11,3,9, 3,11,3,9,10, 1,12,4, 2,12,4,1, 3,12,4,1,6, 
    1,13,4, 2,13,4,12, 3,13,4,12,1, 1,14,4, 2,14,4,12, 3,14,4,12,13 $END
```

I then created the following **script** file in my text editor. You will have to **change** the first filename to suit your own series and can change the values in the series if you wish.

```{code-block} bash
---
name: makescan.sh2
caption: makescan.sh
---
input_file=butane-SCAN.inp
spacer=_
for num in $(seq -w 000 010 180)
do
  sed "s/NUMBER/$num/" $input_file > "$input_file$spacer$num.inp"
done
```

*sed* is a *Unix* tool that will **replace** one string of text with another. It has many options. The way it is used here it will replace the first instance of `NUMBER` with the string stored in the variable `$num`. The string stored in `$num` will also be **appended** to the output file created by the command.

You can **learn more** about each tool used in this script by using the *man* tool, e.g. type `man seq` to learn more about the *seq* tool that created the list of numbers that was traversed by the for loop.

Once I create the butane-SCAN.inp input file and the makescan.sh script, I am ready. I can **run the script** by calling it with the shell that I want to run it. We will use the bash shell. Use the following command to run the script.

```
bash makescan.sh
```

Nineteen files will be **created** with values written into the 4,1,2,3 torsion coordinate from 0 to 180 degrees. **Examine** any of the new files and see that this is true. Select all the new input files and drop them onto the *GamessQ* window. In a few minutes all the files will have been run and nineteen new output files will result.

We now have **nineteen outout files**. We can use the previous *grep* commands and take the final energy **from each file**. Or we could **automate** the process with the following shell script.

```{code-block} bash
---
name: extract.sh2
caption: extract.sh
---
for name in butane-SCAN*.log; do
    grep -H "NSERCH" "$name" | grep "GRAD" | tail -n 1
done
```

The vertical characters are “pipes”. The **output** of a command is **piped** as the input of the **next command**. The first two *grep* commands will create the list of energies and gradients from a given file and the tail command will take the last line. The script will output the last `NSERCH` line in each .log file and we will **write** those lines into the butane-result.txt file as shown below.

```
bash extract.sh > butane-result.txt
```

The butane-result.txt file now contains the **last energy value** for each result file.

```{code-block} bash
---
name: butane-result.txt1
caption: butane-result.txt
---
butane-SCAN.inp_000_113.log: NSERCH:  23  E=     -156.4228465418  GRAD. MAX=  0.0000585  R.M.S.=  0.0000204
butane-SCAN.inp_010_114.log: NSERCH:  18  E=     -156.4233726910  GRAD. MAX=  0.0000931  R.M.S.=  0.0000255
butane-SCAN.inp_020_115.log: NSERCH:  16  E=     -156.4247889225  GRAD. MAX=  0.0000789  R.M.S.=  0.0000273
butane-SCAN.inp_030_116.log: NSERCH:  16  E=     -156.4267021853  GRAD. MAX=  0.0000394  R.M.S.=  0.0000149
butane-SCAN.inp_040_117.log: NSERCH:  19  E=     -156.4286426893  GRAD. MAX=  0.0000765  R.M.S.=  0.0000260
butane-SCAN.inp_050_118.log: NSERCH:  18  E=     -156.4301847220  GRAD. MAX=  0.0000241  R.M.S.=  0.0000105
butane-SCAN.inp_060_119.log: NSERCH:  23  E=     -156.4310615763  GRAD. MAX=  0.0000675  R.M.S.=  0.0000212
butane-SCAN.inp_070_120.log: NSERCH:  25  E=     -156.4312168483  GRAD. MAX=  0.0000339  R.M.S.=  0.0000129
butane-SCAN.inp_080_121.log: NSERCH:  24  E=     -156.4306888649  GRAD. MAX=  0.0000987  R.M.S.=  0.0000300
butane-SCAN.inp_090_122.log: NSERCH:  26  E=     -156.4295739060  GRAD. MAX=  0.0000494  R.M.S.=  0.0000155
butane-SCAN.inp_100_123.log: NSERCH:1000  E=     -156.4251866611  GRAD. MAX=  0.0059215  R.M.S.=  0.0016768
butane-SCAN.inp_110_124.log: NSERCH:  23  E=     -156.4271414620  GRAD. MAX=  0.0000819  R.M.S.=  0.0000247
butane-SCAN.inp_120_125.log: NSERCH:  24  E=     -156.4267263463  GRAD. MAX=  0.0000884  R.M.S.=  0.0000234
butane-SCAN.inp_130_126.log: NSERCH: 284  E=     -156.4271134924  GRAD. MAX=  0.0000383  R.M.S.=  0.0000148
butane-SCAN.inp_140_127.log: NSERCH:  21  E=     -156.4281850977  GRAD. MAX=  0.0000701  R.M.S.=  0.0000323
butane-SCAN.inp_150_128.log: NSERCH:  21  E=     -156.4296331216  GRAD. MAX=  0.0000712  R.M.S.=  0.0000225
butane-SCAN.inp_160_129.log: NSERCH: 698  E=     -156.4310602050  GRAD. MAX=  0.0000561  R.M.S.=  0.0000155
butane-SCAN.inp_170_130.log: NSERCH:  20  E=     -156.4320918106  GRAD. MAX=  0.0000675  R.M.S.=  0.0000216
butane-SCAN.inp_180_131.log: NSERCH:  23  E=     -156.4324667182  GRAD. MAX=  0.0000605  R.M.S.=  0.0000189
```

You can see that **one run failed** to find a result. After 1000 steps it still had a large gradient and the energy is still high. We could graph the energy per step and the gradients as we did before and see the path taken. We could manually **check that file** and perhaps change a few values to see if that helps. However, we have lots of points so we could just drop that one from the data set. I loaded butane-result.txt into a *pandas* dataframe in *Python* and produced the following **plot** in {numref}`fig5-11`.

We can load the log file into *MacMolPlt* and **scrub** along the minimization **path**. We can also **plot** the energy and gradients within *MacMolPlt*. Seek and you will find.

```{figure} images/profiles_Picture11.png
---
width: 500px
name: fig5-11
---
*The rotational energy profile for butane. It behaves as expected.*
```
## Summary

We used *MacMolPlt* to **build** a model of butane and export an initial input file for an optimization calculation. We **optimized** the structure for the *anti* conformation and found the *gauche* conformation by starting with an initial structure that was to **near** that conformation. Thus we located the **global** minimum and a **local** minimum on the **rotational energy surface**.

Then we edited the file to **freeze** the coordinate that corresponded to the central C–C **bond rotation** and the set the internal coordinate for that **torsion** to 0˚ and 120˚ to find the energy of the *syn* conformation and an *eclipsed* conformation. With this, we have the important parts of the rotational energy profile.

We learned how to use *Unix* tools to **extract** information from large text files and from multiple text files and we learned how to **create** multiple input files using an **automated** process. We were introduced to the idea of shell scripts and to useful tools such as *grep* and *sed*.

We examined the **format** of the `Z-matrix` in detail. We used the **internal coordinates** to easily create the series of input files for the rotational coordinate scan. Using *Unix* tools, we created many input files with frozen torsion coordinates to create a rotational energy profile. We used *GamessQ* to submit the files as a **batch job**. We extracted the energy from these files and plotted the complete rotational energy profile.


## Exercise
Read the accompanying discussion and then try the following exercises.


### The Activities

**Construct** ethane, propane, butane, 2-methylbutane using *MacMolPlt*. **Export** input files for *GAMESS* with `Z-matrices` and using the `$ZMAT` group for declaring internal coordinates. 

**Identify** all likely minima and maxima along the **rotational energy surface** using the central C–C torsion coordinate of each molecule. **Calculate** the HF/3-21G energy for optimized structures at these points in the coordinate. Use frozen coordinates (or symmetry) for the energy maxima. **Create** a table with the energies and torsion angles for all your calculations (relative to the global minimum in each) with units in *kJ/mole* and degrees.

Using *Unix* tools (or brute force) **generate** input files for rotational energy scans of these molecules. Produce a **plot** of energy vs. angle to create a **visual representation** of the rotational energy profile of each molecule. Try placing all four profiles on the same plot for comparison. 

### The Report

Present a ONE PAGE **document** with the table of angles and energies for maxima and minima that you generated. Include the plot of the entire rotational energy profile and **comment** if it fits with your table. 

If you brute forced the operation, please **report the time** it took to create all the files and extract the energy data from each result file. If you used the *Unix* tools, please **report the time** as well. The table and plot must be professional in appearance.

