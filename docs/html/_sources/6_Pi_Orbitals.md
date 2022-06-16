# Allyl Cation: $\pi$ Orbitals

Simplified Hückel Molecular Orbital Theory (SHMO) allows us to create $\pi$-molecular orbitals for planar systems. It is qualitatively accurate and often all one needs to interpret $\pi$-systems in physical organic chemistry. We have explored SHMO and created MO diagrams for ethylene, allyl anion & cation, butadiene and the cumyl cation. We have explored the phenol and the nitrobenzene system as well. And we explored the surprising polar nature of azulene compared to naphthalene. We did all this with Python and the NumPy \& SciPy packages.

Can we do the same, only better, with GAMESS? Let’s get busy.

## Goals

In this exercise, we will accomplish the following…

1.	Use MacMolPlt to build molecules, generate input files and interpret results and use GamessQ to submit jobs to GAMESS
2.	Use MacMolPlt to generate graphical images of the molecule and surfaces that represent electron density and molecular and local orbitals. 
3.	Use the colour-coded electrostatic potential energy surface to interpret the polarity of the molecules. 
4.	Use the information in the result files to determine free valence and charge on each atom and compare these to SHMO results.
5.	Create a detailed MO diagram for the molecules described above and include relevant images of the molecular orbitals.

## The Allyl System

For an example we will build the allyl cation and examine the results of the calculation. First we will build the allyl group with MacMolPlt and attempt to use symmetry (MacMolPlt files often fail with GAMESS when applying symmetry). If that fails we will construct the molecule manually.

In MacMolPlt first we will set the point group using `Molecule` $\rightarrow$ `Set Point Group` $\rightarrow$ `Point Group` $\rightarrow$ `Cnv` and then `…`$\rightarrow$ `Order of Principal Axis` $\rightarrow$ `2`. Set up the build with `Builder` $\rightarrow$ `Edit with Symmetry` and then call the build window with `Builder` $\rightarrow$ `Show Build Tools`. It helps to show the axes of the symmetry space via `View` $\rightarrow$ `Show Axis`. After that, it is up to trial and error.

You will find that each atom placed may be copied in space according to the point group. The z-axis is the principal axis. Give it a try. I managed to get a structure that resembles the basics of an allyl group. See {numref}`fig6A1` for an example.



```{figure} images/pi_symmetryBuild.png
---
width: 550
name: fig6A1
---
*Building an allyl cation with symmetry using MacMolPlt. The solid atoms are the ones that I placed and the faded ones are being generated according to the requirements of the point group.*
```
 
I then exported an input file using `Subwindow` $\rightarrow$ `Input Builder`. Be sure to make sure that the multiplicity is 1 (singlet) and the charge is 1 (cation). Use the 6-311G basis set and add d and p orbitals and use both diffuse functions. The diffuse functions are important as they improve results for charged systems. Here is the input file that was generated. Only the unique atoms (2 carbons, the third is defined by symmetry) are in the $DATA group.

**AllylCat_6311_U.inp**
```
!   File created by MacMolPlt 7.7.2
 $CONTRL SCFTYP=RHF RUNTYP=OPTIMIZE MAXIT=30 ICHARG=1 MULT=1 MOLPLT=.TRUE. $END
 $SYSTEM TIMLIM=525600 MEMORY=1000000 $END
 $BASIS GBASIS=N311 NGAUSS=6 NDFUNC=1 NPFUNC=1 DIFFSP=.TRUE. DIFFS=.TRUE. $END
 $SCF DIRSCF=.TRUE. $END
 $STATPT OPTTOL=0.0001 NSTEP=100 $END
 $DATA 
Allyl
CNV 2

C     6.0     0.00000     1.05078     0.00000
C     6.0     0.00000     0.00000     1.10972
H     1.0     0.00000     0.00000     2.24972
H     1.0     0.00000     2.15957     0.26491
H     1.0     0.00000     0.72580    -1.09270
 $END
```

### Analysis of Charges

The file was submitted to GAMESS via GamessQ. The resulting .log file was opened with MacMolPlt. 

Bond distances and angles were measured as shown in {numref}`fig6B`. The structure is not a close match to the literature values.  For example, the C–C–C bond angle is 118˚ while the literature value is 124.6˚. It is expected that the angle should be greater than 120˚ so I was suspicious of the result. Ions are tough. More expensive methods will be needed but we can still obtain fairly decent descriptions of the orbitals and charge density. They won’t be perfect, but will give us the general idea.

```{figure} images/pi_allylresult.png
---
width: 550
name: fig6B
---
*HF/6-3111(d,p)++ optimized structure of the allyl cation.*
```

By using `Subwindow` $\rightarrow$ `Surfaces` $\rightarrow$ `3D Electron Density` and choosing to colour by `MEP` (molecular electrostatic potential we can obtain an image that represents the electron density of the molecule and the colours mapped onto the surface represent the charge. Red are regions that repel a positive charge and blue are regions that attract a positive charge. Green is neutral. We can see in {numref}`fig6C` that the positive charge is located on the two terminal carbon groups, as expected.

```{figure} images/pi_1.png
---
width: 550
name: fig6C
---
*Electron density surface coloured by electrostatic potential. MacMolPlt does not give the best color contrast, but it does the job.*
```

```{note}
Someday, I will explore using Multiwfn, a package for analyzing molecular wavefunction data produced by programs like GAMESS. Perhaps you will be the pioneer. See more at http://sobereva.com/multiwfn/index.html
```

We can get an approximation of the charge held by each group from the data in the result .log file. Open the result file in a text editor and search for the word “`LOWDIN`”. Find the last occurrence of that word in the file. You should see a block of text like the one below.

```
          TOTAL MULLIKEN AND LOWDIN ATOMIC POPULATIONS
       ATOM         MULL.POP.    CHARGE          LOW.POP.     CHARGE
    1 C             6.233846   -0.233846         5.819533    0.180467
    2 C             6.233846   -0.233846         5.819533    0.180467
    3 C             5.725921    0.274079         6.074708   -0.074708
    4 H             0.728455    0.271545         0.860553    0.139447
    5 H             0.763724    0.236276         0.852211    0.147789
    6 H             0.763724    0.236276         0.852211    0.147789
    7 H             0.775243    0.224757         0.860625    0.139375
    8 H             0.775243    0.224757         0.860625    0.139375
```

Here is reported calculations of electron population and partial atomic charge according to two common methods: Mulliken and Lowdin. We will use Lowdin. We see that the two terminal carbons (C1 & C2) are positively charged. However it is better to calculate the total charge on the carbon groups (carbons and hydrogens) and GAMESS is having the positively charged carbon atoms pull in electrons from the hydrogen atoms to spread the charge out. 

Here are my calculations. The atom numbers are revealed in the MacMolPlt image.

| Group	| Charge |
| :----- | :----- |
| C1+H5+H7	| +0.468 |
| C3+H4	| +0.065 |
| C2+H6+H8	| +0.468 |
| Total	| +1.001 |

We see that the ends of the allyl cation share the charge 50/50. This is consistent with the SHMO analysis, which would have placed the full charge of the group on the carbon atom alone (SHMO ignores the hydrogen atoms)

## Analysis of Molecular Orbitals

The molecular orbital diagram can be created using data from the GAMESS result file as interpreted by MacMolPlt. We can provide images of the local bonding $\sigma$-orbitals and the $\pi$-orbitals to create a basic interpretation of the bonding and reactivity of the allyl cation. We can also use the calculated bonding MOs and their relative energies (the eigenvalues for each MO). 

Use `Subwindow` $\rightarrow$ `Surfaces` $\rightarrow$ `3D Molecular Orbitals` and explore the options to create images as seen in figure 4. The energies for each molecular eigenvector (molecular orbital) is listed in the window. You can also find them in the result file. Search the .log file for “`MOLECULAR ORBITALS`” and you will see each MO as a column of values (the eigenvector) with an energy value at the top (the eigenvalue). The first three will be the 1s core orbitals of carbon. There will be 17 MOs that are created by the valence AOs. ($s$, $p_x$, $p_y$, $p_z$ for each carbon and s for each hydrogen). The first eight valence MOs will be filled (that means the first 11 are filled counting the core orbitals). Eigenvectors 4 through 20 represent the bonding and antibonding MOs. Rather than use just 17 valence shell AOs, GAMESS used 104 AOs! It’s just being thorough and these higher level empty MOs do have slight effects on the energy and structure and are there to provide greater accuracy.

Can you make a diagram like the one in {numref}`fig6D`? I exported images from MacMolPlt and made the diagram using the graphics program [Affinity Designer](https://affinity.serif.com), but you could use the free [Inkscape](https://inkscape.org) program as well.  



```{figure} images/pi_MO-Diagram_lowres.png
---
width: 500
name: fig6D
---
*MO diagrams for the allyl cation. Whether we imagine the system using combinations of hybrid atomic orbitals to create local MOs or use the true AOs to calculate the global MOs we see that the LUMO is the same with both approaches and that is what counts.*
```

To get accurate energies for the molecular orbitals I had to use a more advanced method. The density functional theory (DFT) method is another way of calculating wavefunctions. Like Hartee-Fock, it uses basis sets but rather than using Gaussian approximations of Slater-type atomic orbitals, it uses “functionals”. That’s all I know. There are many DFT methods. I used the B3LYP method, which I am told is good for ionic species. The orbitals above were from a B3LYP/6-311(d,p)++ energy calculation of the HF/6-311(d,p)++ optimized structure.

Below is the input file for the energy calculation that produced the orbitals in {numref}`fig6D`.

**AllylCat_B3LYP_U_E.inp**
```
!   File created by MacMolPlt 7.7.2
 $CONTRL SCFTYP=RHF RUNTYP=ENERGY DFTTYP=B3LYP MAXIT=30 ICHARG=1 MULT=1 
    LOCAL=RUEDNBRG MOLPLT=.TRUE. $END
 $SYSTEM TIMLIM=525600 MEMORY=1000000 $END
 $BASIS GBASIS=N311 NGAUSS=6 NDFUNC=1 NPFUNC=1 DIFFSP=.TRUE. DIFFS=.TRUE. $END
 $SCF DIRSCF=.TRUE. $END
 $STATPT OPTTOL=0.0001 NSTEP=100 $END
 $DATA 
Allyl
CNV 2

 C           6.0   0.0000000000   1.1890383616   0.0382935299
 C           6.0   0.0000000000   0.0000000000   0.7413087631
 H           1.0   0.0000000000   0.0000000000   1.8262054383
 H           1.0   0.0000000000   2.1502830490   0.5462821494
 H           1.0   0.0000000000   1.2020058650  -1.0493127800
 $END
```

## Comparing AO Coefficients

In SHMO theory we get the coefficients of each p-atomic orbital as they contribute to each $\pi$-molecular orbital. These coefficients make the list of numbers that make up the Eigenvectors for each HMO. There are similar coefficients in the molecular eigenvectors in the result file. On the following page is a section for the output file. Look for the last occurrence of the string “EIGENVECTORS”.

We see that the $\pi_x$ orbitals are the $p$-atomic orbitals that contribute to the $\pi$-MOs. (The molecule is in the zy-plane.) The terminal carbons are C1 and C2 and the central carbon is C3. Thus we have the following coefficients for the allyl $p_x$-AOs for their respective contributions to each of the $\pi$-MOs.

| Orbital	| $C_1 p_x$	| $C_3 p_x$ | $C_2 p_x$   |
| :----     | :----     | :----     | :----       | 
| 11	    |  0.134	|  0.180    | 	 0.134    |
| 12	    |  0.200	|  0	    |   -0.200    |
| 13	    | -0.134	|  0.219    | 	-0.134    |


How do  these coefficients compare to the HMO method? They are smaller in magnitude because these $p$-orbitals are used in many of the other 104 orbitals that were included in the GAMESS calculation and SHMO only considers the three $\pi$-MOs.		

 
Excerpt from  **AllylCat_B3LYP_U_E.log**

```
 FINAL R-B3LYP ENERGY IS     -116.9224892059 AFTER  17 ITERATIONS
 DFT EXCHANGE + CORRELATION ENERGY =       -14.3077177400
 TOTAL ELECTRON NUMBER             =        22.0000988784

          ------------
          EIGENVECTORS
          ------------

                      1          2          3          4          5
                  -10.4879   -10.4879   -10.4426    -1.0732    -0.9433
                     A1         B2         A1         A1         B2  
    1  C  1  S    0.398498   0.398510  -0.004041  -0.064926  -0.082626
    2  C  1  S    0.324971   0.325022  -0.003310  -0.100525  -0.129587
    3  C  1  X    0.000000   0.000000  -0.000000  -0.000000   0.000000

......Many Lines Removed...Two blocks of data for the first 10 eigenvectors......

  101  H  8  S   -0.008466   0.011802  -0.012339   0.022118   0.000460
  102  H  8  X    0.000000  -0.000000  -0.000000   0.000000  -0.000000
  103  H  8  Y   -0.001868  -0.007693  -0.004355   0.008444  -0.001992
  104  H  8  Z   -0.013912   0.004068  -0.014874  -0.006435   0.006700

                     11         12         13         14         15
                   -0.5752    -0.3840    -0.2157    -0.1603    -0.1437
                     B1         A2         B1         A1         A1  
    1  C  1  S   -0.000000  -0.000000   0.000000  -0.031188  -0.005795
    2  C  1  S   -0.000000  -0.000000   0.000000  -0.051222  -0.009720
    3  C  1  X    0.133628   0.200023  -0.134213  -0.000000   0.000000
    4  C  1  Y   -0.000000  -0.000000   0.000000  -0.038494   0.024973
    5  C  1  Z   -0.000000  -0.000000   0.000000  -0.034446  -0.075716
    6  C  1  S   -0.000000  -0.000000   0.000000   0.174118   0.024304
    7  C  1  X    0.211607   0.312491  -0.199280  -0.000000   0.000000

...... Lines Removed.........

   24  C  2  S   -0.000000  -0.000000   0.000000  -0.031188  -0.005795
   25  C  2  S   -0.000000  -0.000000   0.000000  -0.051222  -0.009720
   26  C  2  X    0.133628  -0.200023  -0.134213  -0.000000   0.000000
   27  C  2  Y   -0.000000  -0.000000   0.000000   0.038494  -0.024973
   28  C  2  Z   -0.000000  -0.000000   0.000000  -0.034446  -0.075716
   29  C  2  S   -0.000000  -0.000000   0.000000   0.174118   0.024304
   30  C  2  X    0.211607  -0.312491  -0.199280  -0.000000   0.000000

...... Lines Removed.........

   47  C  3  S   -0.000000  -0.000000   0.000000  -0.012952   0.024036
   48  C  3  S   -0.000000  -0.000000   0.000000  -0.021349   0.039376
   49  C  3  X    0.179738  -0.000000   0.218916  -0.000000   0.000000
   50  C  3  Y   -0.000000  -0.000000   0.000000  -0.000000   0.000000
   51  C  3  Z   -0.000000  -0.000000   0.000000   0.041306  -0.065483
   52  C  3  S   -0.000000  -0.000000   0.000000   0.069751  -0.125935
   53  C  3  X    0.284633  -0.000000   0.337108  -0.000000   0.000000
   54  C  3  Y   -0.000000  -0.000000   0.000000  -0.000000   0.000000
   55  C  3  Z   -0.000000  -0.000000   0.000000   0.061031  -0.101278
   56  C  3  S   -0.000000  -0.000000   0.000000   0.418506  -0.489405
.............................
```

## Summary 

We have created input files and produced output files for a charged molecule. We have optimized the structure at HF/6-311(d,p)++ and calculated the energy at B3LYP/6-311(d,p)++. We then visualized the electron density and colored the surface with the values of the electrostatic potential. This revealed that the ends of the cation shared the positive charge. We examined the contents of the result file and calculated the partial charge on the carbon groups and again observed equal charge sharing at the ends.

We then visualized the local bonding MOs for representative C–H and C–C bonds. We also visualized the three $\pi$-MOs and the seven $\sigma$-MOs and created molecular orbital diagrams using the simple combination of hybrid AOs and also with the complete combination of all AOs. We also determined the coefficients for the $p$-AOs that contributed from each carbon atom toward the $\pi$-system. 

## Files
The following files were created during this tutorial and are available with this document. Feel free to use them as templates and cut and paste as you build the other calculations.

| Filename | Notes |
| :---- | :---- |
| AllylCat_6311_U.x	| The input file for the HF/6-311(d,p)++ optimization created using symmetry in the builder of MacMolPlt. |
| AllylCat_B3LYP_U_E.x	| The input file for the B3LYP/6-311(d,p)++ energy calculation. Created with MacMolPlt and then the coordinates were pasted in from the output of the above file. |


## Exercise

Read the accompanying discussion and then try the following exercises.

### The Activity

Construct ethylene and then optimize the structure at HF/6-3111(d,p)++. Perform an energy calculation at B3LYP/6-311(d,p)++ with instructions to write data for localized MOs. Use symmetry in the construction of the input file.

### The Report

Present a ONE PAGE document with the molecular orbital diagram with images of the bonding orbitals. Present a table of charges for each carbon group (a carbon atom and all attached hydrogens). Present a table of p-orbital coefficients for each $\pi$-MO. Include an image of the electron density mapped with the electrostatic potential to demonstrate charge location (admittedly there will be no charges in ethylene, but other molecules will reveal detail here)

Compare the $\pi$-MOs, coefficients and charges from your GAMESS calculations to the values from the exercise with SHMO $\pi$-systems.

Now repeat the exercise for the following situations as assigned. Don’t bother making any more images of $\sigma$-orbitals. Just show $\pi$-orbitals in your diagrams (but please do indicate the $\sigma$-orbitals with lines for relative energy levels and arrows for electrons).

1.	Allyl anion 
2.	Butadiene 
3.	Pentadienyl cation or anion 
4.	Cumyl cation 
5.	Naphthalene 
6.	Azulene 
