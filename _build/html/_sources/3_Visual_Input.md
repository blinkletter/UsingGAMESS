# Methane: Visual Input and Output

A **hand crafted** input file is a powerful thing. We can set it up exactly as we like. But there is another way. We can use various helper programs that enable the **visual creation** of a molecule and automatic generation of *GAMESS* input files. These files will often need further editing to get what you want out of *GAMESS* but, after we start using molecules larger than benzene, we will appreciate the **graphical interface** (and curse it often).

When interpreting the **output file**, we can evaluate energies and bond lengths and angles easily. But **visualization** of the whole molecule will help see the **relationships** between distant atoms and also quickly identify structures that optimized to a nonsense answer. In addition, we can now interpret more mathematical aspects of the output like bond **vibrations** and mathematical **surfaces** that represent electron density and **molecular orbital** functions.

The two applications that we will use are *MacMolPlt* and *Avogadro*. Both have different **strengths** and we will get to know them both. In this exercise, we will use *MacMolPlt*.

## Learning Goals

In this exercise, we will **accomplish** the following…

1.	Use *MacMolPlt* to **build** molecules, generate input files and interpret results. 
2.	Use *GamessQ* to **submit** jobs to *GAMESS*
3.	Use *MacMolPlt* to generate graphical **images** of the molecule and surfaces that represent electron density and **molecular orbitals**.
4.	Identify the molecular orbitals that are most closely associated with the **bonding local molecular orbitals** and lone pair local MOs. How do you think about bonds and electronic structure? Do you think using **local** MOs that align with the Lewis structure or do you think using the molecular orbitals that describe the combined interactions of all atomic orbitals.

## Making Methane

Open your copy of *wxMacMolPlt* and **navigate** to the build menu: `Builder` &rarr; `Show Build Tools`. Select carbon with a coordination number of 4 and click in the empty window. Then select `Builder` &rarr; `Add Hydrogens` to complete your structure of methane. Efforts to enforce symmetry on files created by *MacMolPlt* often fail and manual creation of files that use symmetry is preferred. *GAMESS* requires perfection when you are declaring symmetry. As a result, we will **not use** symmetry in this calculation. 

```{note}
*MacMolPlt* has a symmetry builder function that can apply the point group as you build the molecule. We will discuss it later and build without symmetry for now.
```

Select `Subwindow` &rarr; `Input Builder` to start making an **input file** for *GAMESS*. In the `Basis` window select 6-311G for the basis set. Set “1” for `D and light atom polarization functions` (this is the “d,p” in the 6-311G(d,p) basis set.) Check the `Diffuse l-shell` and `s-shell` options (this is the “++” in 6-311G(d,p)++.)

In the `Control` window select `Run Type: Optimization` and also select `Localization Method: Edmiston-Ruedenberg`. The localization method will command *GAMESS* to write **information** into the output file that can be used to make **local** bonding molecular orbitals (we will be using them very soon in this exercise).

In the `Data` window make sure that the coordinate option is set to `Unique Cartesian`. Set the `symmetry point group` to *C<sub>1</sub>*. With *C<sub>1</sub>*, every atom will be unique as we are not declaring symmetry.
In the `Misc Prefs` window set the *MacMolPlt* option. This will **result** in data written into the output file that helps *MacMolPlt* interpret the results.

In the `Stat. Point` window we can set the number of steps to a higher number that 20. We will use 20 for now.

Click on the `Edit and Save` button and you will get a text window with the generated input file. You can make changes now or you can use a text editor later. Save the file. below is the file as saved by *MacMolPlt*.

```{code-block} 
---
name: amethane.inp
linenos: True
lineno-start: 1
emphasize-lines: 
caption: methane.inp
---
!   File created by MacMolPlt 7.7.2
 $CONTRL SCFTYP=RHF RUNTYP=OPTIMIZE MAXIT=30 MULT=1 LOCAL=RUEDNBRG COORD=UNIQUE 
    $END
 $SYSTEM TIMLIM=525600 MEMORY=1000000 $END
 $BASIS GBASIS=N311 NGAUSS=6 NDFUNC=1 NPFUNC=1 DIFFSP=.TRUE. DIFFS=.TRUE. $END
 $SCF DIRSCF=.TRUE. $END
 $STATPT OPTTOL=0.0001 NSTEP=20 $END
 $DATA 
Methane
C1
C     6.0     0.00000     0.00000     0.00000
H     1.0     0.64179    -0.64179    -0.64179
H     1.0    -0.64179     0.64179    -0.64179
H     1.0    -0.64179    -0.64179     0.64179
H     1.0     0.64179     0.64179     0.64179
 $END
```

## Using *GamessQ*

Open *GamessQ* (first **run** the binary in a terminal window and then **start** the GUI by clicking on the application icon.) **Drag and drop** the input file into the *GamessQ* window. Watch as its status changes from pending to running to done. The output file will be in the directory **specified** in the *GamessQ* preference pane. Find that log file and **open** it in a text editor. **Look** quickly to the end of the file for the phrase `GAMESS TERMINATED NORMALLY`. If there was an error, trouble shoot the input file and **try again**. Find the `EQUILIBRIUM GEOMETRY LOCATED` statement and record the energy (and check the new optimized coordinates for sanity).
 
## Viewing in *MacMolPlt*

Use *MacMolPlt* to **open** the .log file that was produced by *GAMESS*. You will see an **image** of the methane molecule. Practice **rotating** it and **zooming** in an out.

We can **measure** lengths and angles in *MacMolPlt*. Click on an atom to select it. Then click on a second atom while holding `[SHIFT]`. Then select `View` &rarr; `Annotations` &rarr; `Display Length`. Do this with any three atoms and select `View` &rarr; `Annotations` &rarr; `Display Angle`. You can **measure** lengths angles and torsions right off the screen. You can **display** atom numbers with `View` &rarr; `Atoms Labels` &rarr; `Atom Number`. **Explore** the menus and see what you can do.

You can **save** the image in the window using `File` &rarr; `Export`. Explore the **options** and see what makes the best image file for you. See {numref}`fig1A` for an example.



```{figure} images/Methane_Measured.png
---
width: 250px
name: fig1A
---
**MacMolPlt* view of methane with some annotations added.*
```

We can **display** the electron density surface of methane using `Subwindow` &rarr; `Surfaces`. Select `3D Total Electron Density` from the list and chose settings until you get a **picture** like the one in {numref}`fig2A`. 

```{figure} images/Methane_surface.png
---
width: 350px
name: fig2A
---
*The electron density surface colored according to molecular electrostatic potential (MEP). Can you set the values to make the image look like this?*
```

Methane is very **nonpolar** so the MEP will be mostly one color. Molecules with heteroatoms will be more revealing in this regard.

## Molecular Orbitals

We often see **molecular orbital diagrams** in textbooks. Let’s try to make our own for methane. 

### Visualizing MOs

Use the `surface` subwindow again and this time select `3D orbital` as the choice. Choose `Molecular Eigenvectors` as the orbital set and then **change settings** until you get an image similar to the one in {numref}`fig3A`.
`
```{figure} images/Methane_HOMO-nosym.png
---
width: 500px
name: fig3A
---
*One of the three degenerate HOMOs of methane. The lack of symmetry in the calculation leads to a lack of symmetry in the orbitals.*
```

We see the familiar methane HOMO there but it is not **perfectly** symmetrical. We did not use symmetry in our calculations because input files generated by *MacMolPlt* often fail symmetry requirements. 

### *T<sub>d</sub>* Methane

We can **construct** a symmetrical structure of methane using symmetry tools in *MacMolPlt*. However, for now let us do this **manually**. First I will make an AM1 input file for structural **optimization** *T<sub>d</sub>* methane. 

```{code-block} 
---
name: methane_AM1_U.inp1
linenos: True
lineno-start: 1
emphasize-lines: 
caption: methane_AM1_U.inp1
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


After submitting it, we will have the coordinates optimized at the AM1 level. We can then **copy** them into an input file for the HF/6-311G(d,p)++ **energy** at *T<sub>d</sub>* symmetry. I **added the command** for creating local bonding orbitals.

```{code-block} 
---
name: methane_6311_U_E.inp1
linenos: True
lineno-start: 1
emphasize-lines: 2
caption: methane_6311_U_E.inp
---
 $CONTRL SCFTYP=RHF RUNTYP=ENERGY MAXIT=30 MULT=1 ICHARG=0 
  NZVAR=9 LOCAL=RUEDNBRG COORD=UNIQUE $END
 $SYSTEM TIMLIM=525600 MEMORY=1000000 $END
 $BASIS GBASIS=N311 NGAUSS=6 NDFUNC=1 NPFUNC=1 DIFFSP=.TRUE. DIFFS=.TRUE. $END
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

### MOs for *T<sub>d</sub>* Methane

I **openned** the log file in *MacMolPlt* and when I **displayed** the HOMO for this symmetrical calculation the orbitals were perfect. It should be noted that both sets of MOs were really the same. It is exactly the same math. The less symmetrical image was produced using axes that did not perfectly align with the **elements of symmetry** of the orbitals. However, just because there was a little more *x* and a little less *y* does not change the way the orbitals behave. It’s just how the **picture** is calculated, the underlying math of the MO never changes. The new improved MO image is present in {numref}`fig4A`.

```{figure} images/Methane_HOMO-sym.png
---
width: 250px
name: fig4A
---
*The HOMO of methane generated from a calculation that used the Td symmetry requirement.
Local Bonding Orbitals*
```

We are used to describing **bonds** around second-row elements like carbon as *sp*, *sp<sup>2</sup>*, or *sp<sup>3</sup>*. A *sp<sup>3</sup>* bonding MO can be constructed from the overlap of the carbon *sp<sup>3</sup>* AO and the hydrogens *s*-orbital. This would be a **simple model** that describes the electron pair for that bond (not really) and relates more directly to **Lewis structure** (if you prefer stick drawings to the truth of math.) In the `Subwindow` &rarr; `Surfaces` window choose the `3D Orbital` option and then choose the `Localized Orbitals` option from the `Orbital Set` menu. Select one of the orbitals and then **choose** settings that produce and image similar to what you see in {numref}`fig5A`. Have fun and try lots of settings.

```{figure} images/Methane_LOCAL_4.png
---
width: 350px
name: fig5A
---
*A local bonding MO for the C–H bond in methane.*
```

Which seems **easier** to interpret when explaining the C–H bond: the true MO or a local bonding MO model? When you are **constructing** a MO diagram using hybrid atomic orbitals, you will naturally be constructing the local bonding MOs from *sp<sup>3</sup>* carbon AOs and hydrogen s-AOs. You can the further **combine** these local MOs to make the orthogonal MOs that actually describe the electronic structure.

## A Molecular Orbital Diagram

In this exercise, you will be asked to **construct** MO diagrams with visualized MOs and local bonding MOs. Here is a pair of molecular orbital **diagrams**. {numref}`fig6A` uses the atomic orbitals to make the true molecular orbitals for the molecule. However it is often **more informative** to consider local molecular orbitals as presented in {numref}`fig7A`.

```{figure} images/MOs_Diagram_Methane1.png
---
width: 700px
name: fig6A
---
*MO diagram for methane.*
``` 
 
```{figure} images/MOs_Diagram_Methane2.png
---
width: 700px
name: fig7A
---
*MO diagram using the local molecular orbital model.*
```

## The Multiverse
The *T<sub>d</sub>* symmetry **enforces** that the hydrogens are each in one of the octants of 3D space. This means that the cardinal planes are not through any of the hydrogen atoms. If you considered that the four hydrogens were each at corners of the cube, then the planes are slicing through the faces of the cube. This is why all three of the degenerate orbitals are **identical** in appearance.

Your textbook may present **different** images of these orbitals. They are exactly the **same** orbitals, just with different placements of the cardinal planes w.r.t. the bonds. We used *C<sub>3v</sub>* symmetry for the ammonia molecule and, if we had used it with the methane *Z-matrix* that was created by modifying the ammonia *Z-matrix*, it would have worked just fine. The *C<sub>3v</sub>* symmetry requires that one of the four C–H bonds be along the *z*-axis. This means that two C–H bonds will be in a cardinal plane. The three degenerate orbitals all appear different because they each have a different relationship to the symmetry space. Despite this, they are identical. If orbitals have exactly the **same** energy then they are **identical**. The *C<sub>3v</sub>* arrangement is perhaps the most useful for interpreting a reaction. A hydrogen abstraction by a radical will occur by the radical approaching along a **bond axis**. Adding that element will reduce the symmetry to *C<sub>3v</sub>* from *T<sub>d</sub>*. The molecular orbital that **aligns** with the *z*-axis best describes the **frontier orbital** that will guide the reaction as the atoms approach each other.

Another **option** is to use the *C<sub>2v</sub>* symmetry space. This will result in two separate pairs of C–H bonds being in cardinal planes. As a result two of the orbital images will appear identical with a third image being with a plane placed perpendicular to the other two. Again, it must be emphasized that all three degenerate molecular orbitals are **identical**.

I prefer the *T<sub>d</sub>* MO set since it does emphasize the idea that all three degenerate MOs are **identical**. (How many times have I said that already?) The *C<sub>3v</sub>* set is best for explaining frontier orbital interactions with an **approaching** radical, but I prefer using the idea of a **local** bonding C–H &sigma;-orbital when discussing a reaction with a C–H bond. **Compare** the local orbital with the *z*-axis MO and see how they are both great for discussing **frontier** molecular orbital theory.  The **local** orbital is far easier to use when we want to invoke the anti-bonding orbital that an approaching radical will actually be interacting with.

You will be exploring these ideas in the exercise supported by this discussion. Good luck.

## Summary

We have used *MacMolPlt* to **build** a small molecule and generate an input file for *GAMESS*. We have **submitted** that file to *GAMESS* via the *GamessQ* program.

We have used *MacMolPlt* to **measure** bond lengths and angles and to **visualize** the molecular orbital data generated by *GAMESS*. We have exported the **images** in our favourite graphic file format.

Where will we go from here? Open the instructions for the exercise that this discussion supports. Have fun.


## Exercise

Read the discussion above and then try the following activities.

### The Activities

You will have HF/6-311G(d,p)++ optimized structures for methane (*T<sub>d</sub>*), Ammonia (*C<sub>3v</sub>*) and water (*C<sub>2v</sub>*) from a previous exercise. **Use** the data for those structures to perform an energy (or optimization) calculation and **add** the local orbital command to the `$SYSTEM` group. 

Use the result file with *MacMolPlt* to **visualize** the bonding molecular orbitals and the localized bonding orbitals. Are there degenerate sets in the molecular orbitals? Do any local orbitals resemble lone pairs? Do any of the MOs seem more closely related to lone pairs or more closely related to bonds? What are the relative energies of these MO sets and do the energies fit with expectations?

**Construct** input files for methane using *C<sub>3v</sub>* and *C<sub>2v</sub>* symmetry and **compare** the shapes of these versions of the orbitals to those in ammonia and water. What similarities and differences do you observe?

### The Report

**Create** a ONE-PAGE document summarizing your results. Create **images** for each of the three molecules: methane, water, and ammonia. **Include** bond length and angles in the images. Create images of the molecules with the electron density surface colored by electrostatic potential. **Discuss** the reasons for different bond lengths and angles using VSEPR theory.

Create a SECOND ONE-PAGE document with images of local and molecular bonding orbitals for all three molecules. **Identify** which orbitals in each set best represent lone pairs and which best represent bonds to hydrogen atoms.

Create a THIRD ONE-PAGE document that presents the images of the methane **molecular orbitals** using *C<sub>3v</sub>* and *C<sub>2v</sub>* symmetry. **Compare** these with the corresponding orbitals in ammonia and water. 

Include an **appendix** with the text input files used with *GAMESS* for all the above.

In all your discussions be brief, but consider the questions raised above. Do your best to make the document in a clear and **professional** style.