# Table of Contents

This resource is intended to help organic chemistry students set up the ***GAMESS*** computational chemistry software on their own computer and perform a series of small calculations. It supports my course in physical organic chemistry. There is another course available in computational chemistry that will take you much farther if you catch the bug here. I hear that that course is all math, but mine is all fun. Let us have some **fun with *GAMESS***.

Below is a list of the chapters in this book and some notes on what you will find in each.

## [1. Building Your System](1_Setup.md)

Here you will be shown where to **obtain the software** and how to **install and run it** on a *MacOS Unix* system. These instructions should be easily applied to *Linux*. Essential ***Unix* tools** will be explained.

## [2. Water: Getting Started](2_SmallMolecules.md)

This chapter will introduce how to **run a job** in *GAMESS*. We will explore the ways that molecules are described to *GAMESS* in **input files**. We will see examples of using *xyz* **Cartessian coordinates** to describe the locations of atoms, using symmetry point groups so that we need only describe the symmetry unique atoms and using internal coordinates via the ***Z-matrix***. We will optimize the structures of **water and ammonia** using *GAMESS*. We will use semi-empirical and *ab initio* methods and introduce the idea of **levels of theory** in calculations. *GAMESS* will be run using the command line in the terminal. Results will be interpretted using the **log files** generated as output from *GAMESS*.

## [3. Methane: Visual Input and Output](3_Visual_Input.md)

Here we will see how to use the helper application ***MacMolPlt*** to build molecules and generate input files. We will run the *GAMESS* jobs using the batch controller application ***GamessQ***. We will also use *MacMolPlt* to **analyze** the results and **visualize** structure, localize *bonding orbitals* and *molecular orbitals*. 

## [4. Ethane: Symmetry in Calculations](4_Ethane.md)

Sometimes you want to explore the structure and energies of unstable systems, like transition states. We need to **constrain the optimization** to find a best structure in a high-energy situation. In this chapter we will explore the rotational **energy profile** of ethane using **symmetry point groups** to enforce the *anti* and the *eclipsed* conformations. We will calculate the energy for these two cases.

## [5. Butane: Rotation Energy Profiles](5_Rotation_Profiles.md)

We can extend the idea of locking specific elements of a structure and performing a constrained optimization to explore the full **potential energy surface** for the rotation of the central C-C bond in butane. We will use **internal coordinates** to set values of for the torsion angle  and **constrain** that value using the \$STATPT IFREEZ option. We will also use ***Unix*** tools to **build** a series of input files and **extract** the data from the result files. Interactive ***Python*** will be demonstrated for **analyzing and plotting** the data.


## [6. Allyl Cation: &pi; Orbitals](6_Pi_Orbitals.md)

We have already used simplified Hückel molecular orbital theory and interactive *Python* to calculate the &pi;-molecular orbitals for **conjugated systems**. Now let us demonstrate that goal with *GAMESS*. We will **calculate and visualize** the &pi;-molecular orbitals for the **allyl system** and for **benzene** using *GAMESS* and *MacMolPlt*. We will revisit the idea of using **symmetry** in calculations.

## [7. Butadiene: Transition State for Rotation](7_Butadiene.md)

We will use internal ***Z-matrix*** coordinates and *Unix* tools to create a series of input files for **constrained optization** of different rotational conformers of butadiene. Interactive *Python* will be used to analyze and plot the results. Then we will explore **optimizing a transition state** structure for the highest energy point in the bond rotation. 

## [8. Diels-Alder Reaction: Intrinsic Reaction Coordinates](8A_Diels_Alder.md)

We've all seen those little movies of a **reaction in progress**. We can make our own movies. We will use the Diels-Alder cycloaddition reaction as an example to demonstrate a **reaction coordinate scan** using a new method to **contrain coordinates**. We will not use the *Z-matrix*, but will use unique Cartessian coordinates and freeze automatically-generated internal coordinates of specific atoms using the \$ZMAT IFZMAT and FVALUE options. We can then use this system to generate a **series of structures** that may track near the **reaction coordinate**. From this series we will identify a structure that is near the transition state and perform a **transition state optimization**. Finally we will use the transition state as a starting point for following the potential energy surface down to the products on either side via an **intrinsic reaction coordinate** calculation. We will use *MacMolPlt* to assemble the complete reaction coordinate from the log files and **visualize** the structures. *MacMolPlt* will produce an **energy plot** for us. In the end, we will **make a movie**.