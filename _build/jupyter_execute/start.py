#!/usr/bin/env python
# coding: utf-8

# # Introduction
# We have some intuition about chemical structure and energy. We know that butane is at its lowest energy in the *anti* conformation and that there is a small energy barrier to bond rotation due to steric clash. We know that the amide bond nitrogen is planar, rather than tetrahedral, and has a higher energy barrier to rotation due to its electronic structure. We can demonstrate these effects and explore consequences of changes in structure on our desktop using a computer and software that can calculate the energy of molecules. There are software packages that cost many thousands of dollars (per year!) and there are options that are free to all or free for academic use.
# 
# ***GAMESS***[^gamess1],[^gamess2],[^gamess_link]  is an ab initio computation package for investigating molecular structure and energy. There are others, such as ***NWChem*** [^nwchem],[^nwchem_link]  and ***ORCA*** [^orca],[^orca_link]. 
# 
# ***MacMolPlt*** [^macmolplt],[^macmolplt_link]  is a graphical front end for *GAMESS*. It can build molecules, export input files and interpret the output files produced by GAMESS. ***Avogadro*** [^avogadro],[^avogadro_link]  is a more modern option but lacks some useful tools compared to MacMolPlt. There are others, such as ***Gabedit*** [^gabedit],[^gabedit_link]  and ***Molden***. [^molden],[^molden_link] 
# 
# We will use *GAMESS* and *MacMolPlt* together. We will also use *Avagadro*. 
# 
# [^gamess1]:  "General atomic and molecular electronic structure system" Michael W. Schmidt et. al., Journal of Computational Chemistry. 1993, 14 , 1347–1363. https://doi.org/10.1002/jcc.540141112
# [^gamess2]:  “Recent developments in the general atomic and molecular electronic structure system” 
# Giuseppe M.J. Barca et. al., J. Chem. Phys., 2020, 152, 154102, https://doi.org/10.1063/5.0005188
# [^gamess_link]:  https://www.msg.chem.iastate.edu/gamess/
# [^nwchem]:  "NWChem: a comprehensive and scalable open-source solution for large scale molecular simulations" 
# M. Valiev et. al.,  Comput. Phys. Commun., 2010, 181, 1477. https://doi.org/10.1016/j.cpc.2010.04.018
# [^nwchem_link]:  https://nwchemgit.github.io
# [^orca]:  "Software update: The ORCA program system, version 4.0" Frank Neese, Wiley Interdisciplinary Reviews: Computational Molecular Science, 2018, 1, e1327. https://doi.org/10.1002/wcms.1327
# [^orca_link]:  https://orcaforum.kofo.mpg.de/app.php/portal
# [^macmolplt]:  “MacMolPlt: a graphical user interface for GAMESS” B.M. Bode and M.S.J. Gordon, Mol. Graphics and Modeling, 1999, 16, 133-138. https://doi.org/10.1016/s1093-3263(99)00002-9
# [^macmolplt_link]:  http://brettbode.github.io/wxmacmolplt/
# [^avogadro]:  “Avogadro: an advanced semantic chemical editor, visualization, and analysis platform” 
# Marcus D Hanwell et. al., J. Cheminform., 2012, 4, 17. https://doi.org/10.1186/1758-2946-4-17
# [^avogadro_link]: http://avogadro.cc
# [^gabedit]:  “Gabedit - A graphical user interface for computational chemistry softwares” 
# A.R. Allouche, Journal of Computational Chemistry, 2011, 32, 174-182. https://doi.org/10.1002/jcc.21600
# [^gabedit_link]:  http://gabedit.sourceforge.net/home.html
# [^molden]:  “Molden: a pre- and post-processing program for molecular and electronic structures” D. Schaftenaar, J. Noordik, J. Comput. Aided Mol. Des., 2000, 14, 123–134 (2000). https://doi.org/10.1023/A:1008193805436
# [^molden_link]: https://www.theochem.ru.nl/molden/
