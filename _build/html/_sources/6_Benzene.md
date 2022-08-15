# 7. Benzene: MOs and Symmetry

Benzene is the **iconic** organic molecule. Imagine if I had to design a superhero outfit for “Chemistry Man” (He can change phase from solid to liquid, but he requires a heat source to do so). I would choose a **hexagon**, representing the planar benzene structure, as the superhero **symbol** emblazoned on the cape.

We have already created a** molecular orbital diagram** for the *p*-system of benzene using SHMO theory. Let us now **repeat** that exercise using *GAMESS*.

## Learning Goals

In this exercise, we will accomplish the following…

1.	Use *macMolPlt* to **build** benzene. We will use **symmetry** and the *D<sub>6h</sub>* point group. We will also use the *C<sub>2v</sub>* point group.
2.	We will then **optimize** the structure and **visualize** the orbitals. 
3.	This will be a good system to demonstrate the benefits of symmetry. We will try an expensive energy calculation using the two point groups above and the *C<sub>1</sub> point group.

## Building Benzene

Using the **symmetry building tools** in *macMolPlt*, build benzene. With the *D<sub>6h</sub>* point group you will be **placing** only two atoms in the *xy* plane. With the *C<sub>2v</sub>* point group you will be placing 4 atoms in the *xz* plane with two of the atoms on the *z*-axis. Have fun and leave lots of time to **make mistakes**. We are beginning to leave behind the world of words; more and more you will find that **doing** will be your teacher.

After a brief **struggle** I created the following two builds. How did you fare?

```{figure} images/pi-Benzene-1.png
---
width: 700px
name: fig6_2A
---
*Benzene built using *D<sub>6h</sub>* symmetry and *C<sub>2v</sub>* symmetry. Take note that the *z*-axis is the highest order rotational axis (the *C<sub>6</sub>* axis for *D<sub>6h</sub>* benzene and the *C<sub>2</sub>* axis for *C<sub>2v</sub>* benzene).*
```

```{note}
I am aware that the *C<sub>2v</sub>* structure above in {numref}`fig6_2A` is actually *C<sub>2h</sub>. I am using *C<sub>2v</sub>* because the symmetry will reduce to that point group when a substutent is added. These files can be used in future calculations with substituted benzene*
```

The *C<sub>2v</sub>* optimization **succeeded** but the *D<sub>6h</sub>* file failed. *macMolPlt* did not place the atoms precisely enough to fit the requirements of *GAMESS*. I decided to help it by keeping the **unique** atoms on the *x*-axis. Also, I realized that I could create a *C<sub>2v</sub>* structure that had only three unique atoms. That would be 25% **less expensive** in our high-level energy calculation (I hope). It also fits better with some future builds for naphthalene and azulene that I have planned.  The four-atom *C<sub>2v</sub>* will be useful for the creation of **substituted** benzene systems like the cumyl cation or aniline, so I will keep both around.

```{figure} images/pi-Benzene-2.png
---
width: 700px
name: fig6_2B
---
*The new *D<sub>6h</sub>* version of benzene and the three-atom *C<sub>2v</sub>* version of benzene.*
```

Both the three-atom *C<sub>2v</sub>* and the *x*-axis *D<sub>6h</sub>* input files completed successfully. When a file fails, try **different** versions of coordinates and **read** the documentation if necessary. *GAMESS* is like a cat: you don’t train it, it trains you. 

## Evaluating the Structure

**Benzene** is a very well-studied molecule and its structure is known. Below is a table that **compares** the HF/3-21G optimized structure with the literature values. 

|               |	HF/3-21G	| Literature[^literatutebenzene] |
| :----         | :-----        | :-----                         |
| C–C length	| 1.385 Å	    |   1.397 Å                      |
| C–H length	| 1.072 Å	    |   1.084 Å                      |


The HF/3-21G results were very close to the **literature** values. Now we will use these optimized coordinates in energy calculations to **experience** the benefits of symmetry. 

## Expensive Calculations

We will **calculate** the energy of benzene using the HF/3-21G optimized structures. I will chose an extensive basis set and use an expensive method. 

We will use the B3LYP density functional **method** and use the Dunning aug-cc-pCVTZ **basis set**. This is a correlation-consistent basis set that includes **extra** orbital polarization functions. The “aug” indicates the diffuse functions are also present. When you examine the output file you will see that each carbon atom was calculated using 69 atomic orbitals. Each hydrogen came with 24 atomic orbitals. There were 564 atomic orbitals used in the **calculation** of the 564 molecular orbitals!
B3LYP scales at n4 (some other DFT methods scale at n3). That means that when we increase the number or orbitals (and the gaussian functions that approximate them), we increase effort enormously.

I performed a B3LYP/aug-cc-pCVTZ **energy calculation** using *D<sub>3h</sub>*, *C<sub>2v</sub>* (4 atom) and *C<sub>2v</sub>* (3 atom) symmetry. I **also** performed a calculation with *C<sub>1</sub>* symmetry (that means no symmetry). Below is a table of the time it took for each calculation.  

| Symmetry	                | Time for B3LYP/aug-cc-pCVTZ 	| Energy                  | 
| :----                     | :-----                        | :-----                  |
| *C<sub>1</sub>*	        | 71.5 minutes	                | -232.1862001924 Hartree | 
| *C<sub>2v</sub>* (4 atom)	| 37.6	                        | -232.1861986292         | 
| *C<sub>2v</sub>* (3 atom)	| 36.5           	            | -232.1862006973         | 
| *D<sub>6h</sub>*	        | 7.6	                        | -232.1861814727         | 


Wow! The *D<sub>6h</sub>* symmetry was almost five times **faster** than *C<sub>2v</sub>* and almost ten times faster than *C<sub>1</sub>*. The number of atoms in *C<sub>2v</sub>* did not make much difference. The same number or electrons was involved and the physical space was **half the volume** in both cases. The physical space was 1/6th for *D<sub>6h</sub>* compared to the *C<sub>1</sub>* case (I actually have no idea how the space is divided when using symmetry groups. It will be used by the program to its **best advantage**.) *D<sub>6h</sub>* has a horizontal sigma plane that will further subdivide the 3D space. So, **perhaps** we are at 1/12th the volume. It very much depends on how the software handles the **opportunities** provided by symmetry. Here we **observe** a huge benefit. We will always try to use the **highest** symmetry group possible when using **expensive** methods.

All four input files started with the same **coordinates** (the optimized HF/6-31G structures at each symmetry). The calculated energies were virtually identical. Symmetry did not change the answer, but it changed the cost. 

## Visualization of Molecular Orbitals

The molecular eigenvectors produced by the aug-cc-pCVTZ **basis set** included *f*-orbitals all the way out to the fifth energy shell. This **huge number** of interacting atomic orbitals gives more accurate results, but it can complicate the **images** of molecular orbitals. The three bonding &pi;-MOs and the first two antibonding MOs were fine, but the highest level antibonding &pi;-MO (*&pi;<sub>6</sub>*) was mixed with even higher-level empty orbitals and did not have that “textbook” appearance. I performed the energy calculation again using a minimal basis set (STO-3G) and had far fewer molecular orbitals to choose from. The &pi;-MOs fit much better to the **textbook** idea. Am I sticking with a comfortable lie? Should I accept the truth? 

If you find it difficult to **locate** the higher level antibonding MOs in a sea of extra orbitals then try repeating the energy calculation with a smaller basis set. It will be less accurate but may give **prettier pictures**. {numref}`fig6_2C` presents the molecular orbitals produced from the two basis sets. Which do you prefer?

```{figure} images/pi-Benzene-3.png
---
width: 600px
name: fig6_2C
---
*&pi;-MOs for benzene. The left-hand set is from the B3LYP/aug-cc-pCVTZ energy calculation and the right-hand set is from a HF/STO-3G energy calculation. Both sets were using the same optimized HF/3-21G geometry.*
```



## Summary 

We practiced **building** slightly larger molecules using symmetry in *macMolPlt*. We then exported an input file and optimized the **structure** of benzene using different point groups. We compared the calculation time for an expensive energy calculation using the different symmetries and observed that **higher symmetry** gives faster results.

## Exercise

After reading the above discussion, use *macMolPlt* to produce your **own versions** of the three symmetrical treatments of benzene above. Then build it without symmetry. You will have four versions of benzene structures at different symmetry. **Optimize** the structures at slightly higher theory than in this discussion (you could try HF/6-31G(d,p) or B3LYP/6-31G(d,p)).

Report the **bond lengths**. Open the result files in *macMolPlt* and export **images** of the &pi;-MO system. Compare it to your results from the SHMO method.


[^literatutebenzene]: NIST Computational Chemistry Comparison and Benchmark Database, *NIST Standard Reference Database Number 101*, Release 22, May **2022**, Editor: Russell D. Johnson III, http://cccbdb.nist.gov/ DOI:10.18434/T47C7Z

