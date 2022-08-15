
# 1. Building Your System

First we must build a system of ***tools*** for computational chemistry. You can **acquire** the software and **install** it on your computer using the following **instructions**.



## The Software

We have some intuition about **chemical structure and energy**. We know that butane is at its lowest energy in the *anti* conformation and that there is a small energy barrier to bond rotation due to steric clash. We know that the amide bond the nitrogen is planar, rather than tetrahedral, and has a higher energy barrier to rotation due to its **electronic structure**. We can demonstrate these effects and **explore consequences of changes in structure** on our desktop using a computer and software that can calculate the energy of molecules. There are software packages that cost many thousands of dollars (per year!) and there are options that are **free to all** or free for academic use.

***GAMESS***[^gamess1][^gamess2][^gamess_link] is an *ab initio* computation package for investigating molecular structure and energy. There are others, such as ***NWChem*** [^nwchem][^nwchem_link] and ***ORCA*** [^orca][^orca_link]. 

***MacMolPlt*** [^macmolplt][^macmolplt_link]  is a graphical front end for *GAMESS*. It can build molecules, export input files and interpret the output files produced by GAMESS. ***Avogadro*** [^avogadro][^avogadro_link] is a more modern option but lacks some useful tools compared to *MacMolPlt*. There are others, such as ***Gabedit*** [^gabedit][^gabedit_link] and ***Molden***. [^molden][^molden_link] 

We will use *GAMESS* and *MacMolPlt* together. We will also use *Avagadro*. 

[^gamess1]:  "General atomic and molecular electronic structure system" Michael W. Schmidt et. al., Journal of Computational Chemistry. 1993, 14 , 1347–1363. https://doi.org/10.1002/jcc.540141112
[^gamess2]:  “Recent developments in the general atomic and molecular electronic structure system” 
Giuseppe M.J. Barca et. al., J. Chem. Phys., 2020, 152, 154102, https://doi.org/10.1063/5.0005188
[^gamess_link]:  https://www.msg.chem.iastate.edu/gamess/
[^nwchem]:  "NWChem: a comprehensive and scalable open-source solution for large scale molecular simulations" 
M. Valiev et. al.,  Comput. Phys. Commun., 2010, 181, 1477. https://doi.org/10.1016/j.cpc.2010.04.018
[^nwchem_link]:  https://nwchemgit.github.io
[^orca]:  "Software update: The ORCA program system, version 4.0" Frank Neese, Wiley Interdisciplinary Reviews: Computational Molecular Science, 2018, 1, e1327. https://doi.org/10.1002/wcms.1327
[^orca_link]:  https://orcaforum.kofo.mpg.de/app.php/portal
[^macmolplt]:  “MacMolPlt: a graphical user interface for GAMESS” B.M. Bode and M.S.J. Gordon, Mol. Graphics and Modeling, 1999, 16, 133-138. https://doi.org/10.1016/s1093-3263(99)00002-9
[^macmolplt_link]:  http://brettbode.github.io/wxmacmolplt/
[^avogadro]:  “Avogadro: an advanced semantic chemical editor, visualization, and analysis platform” 
Marcus D Hanwell et. al., J. Cheminform., 2012, 4, 17. https://doi.org/10.1186/1758-2946-4-17
[^avogadro_link]: http://avogadro.cc
[^gabedit]:  “Gabedit - A graphical user interface for computational chemistry softwares” 
A.R. Allouche, Journal of Computational Chemistry, 2011, 32, 174-182. https://doi.org/10.1002/jcc.21600
[^gabedit_link]:  http://gabedit.sourceforge.net/home.html
[^molden]:  “Molden: a pre- and post-processing program for molecular and electronic structures” D. Schaftenaar, J. Noordik, J. Comput. Aided Mol. Des., 2000, 14, 123–134 (2000). https://doi.org/10.1023/A:1008193805436
[^molden_link]: https://www.theochem.ru.nl/molden/

These instructions below **assume** that you are using a *Unix*-based computer, like a *Linux* system or an Apple *MacOS* computer. I have lived in this *Unix* world my whole academic life and am largely unfamiliar with *Windows* systems. However, the websites below have information on installing these tools on *Windows* systems. 

### *GAMESS*

*GAMESS* is proprietary application that performs **quantum mechanical calculations**. There is too much about quantum chemistry to even begin to explain it here. We will use it as a mysterious black box so be sure to follow the recipes. The ***GAMESS* software and instructions** can be obtained [here](https://www.msg.chem.iastate.edu/GAMESS/)

You will need to apply for a **free academic license** and wait for a reply with a password for downloading *GAMESS*. You can obtain compiled executable binaries for *Windows*, *Linux* and *MacOS* machines. You can also get the source code if you want to compile it yourself.

### *GamessQ*

*GamessQ* is a graphical **batch queue** for *GAMESS*. You will be able to add files to the queue and observe their progress. It is the best way to run *GAMESS* so I recommend using it. The **software and instructions** can be obtained [here](https://www.msg.chem.iastate.edu/GAMESS/GamessQ/)

### *MacMolPlt*

*MacMolPlt* is a **graphical interface** for building molecules, creating input files for *GAMESS* and then **visualizing** the information in the output files produced by *GAMESS*. It can be obtained [here](http://brettbode.github.io/wxmacmolplt/)

### Avogadro
*Avogadro* is similar to *MacMolPlt* but more modern is style. It is **open source** and benefits from many contributors. *Avogadro* can be obtained [here](http://avogadro.cc)

### Required Tools

We will need a text editor. Microsoft provides a **free cross-platform text editor** designed for writing code called *[Visual Studio Code](https://code.visualstudio.com/)*. I will be using *Visual Studio Code* in my demonstrations as it works on all our computers.

You will need a **Terminal Emulator**. We will be accessing the *Unix* file system and tools. On a *MacOS* system there is an application called *Terminal* that will allow us to access the real computer that lives inside your computer. *Visual Studio Code* has a built-in terminal emulator.

## Installing GAMESS

*GAMESS* is a modern and constantly updated suite of software. However, it has no interface that the user interacts with. **Input files** will be submitted to *GAMESS* and **output files** will be sent back. It is controlled from the command line or via helper applications like *GamessQ* (see below). So, we will need to do a small amount of configuring via a text editor.

### Obtain and Install

Apply for a **license** for *GAMESS* by following the instruction on the [Mark Gordon group website](https://www.msg.chem.iastate.edu/gamess/). You will receive an email with instructions on downloading the files. You can download the source code or a pre-compiled binary for a your computer. 

The *GAMESS* application is available as a pre-compiled binary for *MacOS* and *Windows*.[^linux]  I received my email, **followed the instructions** and downloaded a file for the latest version of the *MacOS* binary. I decompressed the file and placed the resulting `gamess` directory folder in my `/Applications` folder.

### The GAMESS Folder

Within the `/Applications/gamess` directory are several **important files**. Two of which you may chose to edit. Below are the files and some brief descriptions.

| File                  | Description                                                    |
| :-------------------- | :------------------------------------------------------------- |
| auxdata               | A directory with important data for calculations               |
| *gamess.30Jun2020R1.x*	| The *GAMESS* application binary                                  |
| *gms-files.csh*	        | A shell script that defines environmental variables for *GAMESS*|
| *rungms* 	            | A shell script that is used to send your input file to *GAMESS*    |
| tests	                | A directory of sample jobs to test your installation           |
| *ddikick.x*	            | A binary application used by *GAMESS* to complete a run          |
| *gms*	                | A shell script used to call the *rungms* shell script            |
| README	            | Instructions for using the *gms* shell script to run **GAMESS      |

The *rungms* and *gms* scripts contain variables that can be changed to **customize** the behaviour of *GAMESS* on your computer. 

### Editing RUNGMS

Open *rungms* in a **text editor**. The first lines of the script define directories for the **scratch files**. These are important to define. The default is the home directory of the *rungms* script, but you will likely want your result files to appear somewhere else. I changed the first four lines of the script…

```
set TARGET=sockets
set SCR=./
set USERSCR=./
set GMSPATH=./
```
to…
```
set TARGET=sockets
set SCR=/Applications/gamess/scr
set USERSCR=/Users/Barry/Documents/CompChem/GAMESS-SCR
set GMSPATH=/Applications/gamess
```

This means that the *GAMESS* scratch directory (`SCR`) is no longer the home directory of the application but a directory within it called *scr*. The scratch directory contains huge **temporary** files that are generally **deleted** when the calculation is **complete**. If it crashes, the files may **remain**. I wanted a separate directory so that any leftover junk would be easy to delete every now and then.

Be sure to create the `/Applications/gamess/scr` directory.

The user scratch directory (`USERSCR`) contains data files that are written out with the completion of a calculation. These files contain **orbital and frequency data** among many other sets of useful information. We only occasionally need these files, but they will now be stored in a directory of my choice rather than the `/Applications/gamess` directory. Be sure to create that directory where it is expected to be.

The location of the *GAMESS* binary file is specified with `GMSPATH`. I set it to the location of the `gamess.30Jun2020R1.x` binary in my `/Applications` folder. The *gms* script generally does not need any changes, but you may want to change the very last line that declares the location of *rungms*. *gms* is used to run a *GAMESS* job from the command line and assumes that *rungms* is in the same directory as *gms*.

### Running GAMESS

*GAMESS* can be run from the **terminal command line** by calling *gms*. For example, the command:
`gms cyclohexane.inp` will call the *rungms* script using 1 processor and produce a result file called `cyclohexane.log`.

`gms -l result.log -n 2 cyclohexane.inp` will do the same, but write the result to a file named `result.log` and use 2 processors in your computer.

We will **begin** with using the terminal **command line** to run *GAMESS*. Later, we will use a **batch controller** called *GamessQ*. 


## Installing *GamessQ*

*GamessQ* is a batch controller for *GAMESS* provided by the Gordon group. It is available from the [same web site](https://www.msg.chem.iastate.edu/gamess/). It can **queue** a whole batch of filkes and send them to be executed one at a time while you sleep.

### Obtain and Install

Download the compressed file and extract it. Put the resulting folder in `/Applications`. In the `/Applications/GamessQ` directory we will see the following files&hellip;

| File                  | Description                                                    |
| :-------------------- | :------------------------------------------------------------- |
| GamessQ.app	        | The application for the MacOS GUI interface                    |
| gamessq.html	        | Instructions                                                   |
| gamessqd	            | The background daemon application                              |

### Running *GamessQ*

You will need to run the *gamessqd* application **first**. If you double-click on it, it will run via a terminal window. The *Terminal* app will open and run the executable binary *gamessqd*. It will keep running as long as that terminal window is open. After this **daemon** has been launched, you will double-click on the *GamessQ* application to **open** the graphic interface. *GamessQ* will not run if *gamessqd* has not already been activated.

**Click** on the *GamessQ* icon to run the program. In the menus, open `GamessQ` &rarr; `Preferences` and you will see two **important settings**. The first is the location of the **spool directory** for *GamessQ*. This is where *GamessQ* will move the final result files from a *GAMESS* calculation. The second is the location of the directory for the ***rungms* script** that runs *GAMESS*.  Create a directory for the result files and point *GamessQ* there. And then enter the location of the `/Applications/gamess` folder. Now it is **ready to launch** jobs.

### Using *GamessQ*

To use *GamessQ*, you **drag and drop** the text input files onto its window. This will place the job in the **queue**. You can see when jobs are **waiting, running and finished**. You can drop in dozens of jobs and let them run over the weekend this way.

There is a **command line version** of *GamessQ* that you can compile and run directly on your computer. This can be useful if you want to set up a dedicated computer to run *GAMESS*. You will be able to *telnet* (look it up) using *ssh*[^telnet] (look it up) into your account on that computer. Then you can transfer over input files and submit jobs to the queue using *gamessq* directly. 


### Summary of System Setup

The following **directories** were created and **files and settings** altered accordingly:

| Directory Created	| Where to make changes |
| :----- | :------- |
| `/Applications/gamess/scr` |	edit *rungms* |
| `~/Documents/CompChem/GAMESS-SCR` |	edit *rungms* |
| `~/Documents/CompChem/GAMESS-RESULTS` |	preferences in *GamessQ*  |


With this setup, we will see copies of the input files and the result files appear in the `GAMESS-RESULTS` directory. The data files will appear in the `GAMESS-SCR` directory. BEWARE! Result files and input file copies in `GAMESS-RESULTS` will be deleted whenever you clear the queue in *GamessQ* by clicking on the `cleanup` button. So be sure to copy them to somewhere else if you want to be sure to keep them.

You can **create your own setup** however you like. Just edit the *rungms* script and the *GamessQ* preferences accordingly.



## Installing *MacMolPlt*

*MacMolPlt* is a molecular editing and visualization application. It can be used to **construct** 3-D structures and create **input files** for *GAMESS*. It can **interpret** the resulting output files and produce **visualizations** of bond vibrations and frequencies, molecular energies and molecular orbitals and more.

### Obtain and Install

You can obtain *MacMolPlt* at the [github repository](http://brettbode.github.io/wxmacmolplt/). Just unpack the downloaded file and put the application folder in your `/Applications` directory. If you are running *MacOS 12* (*Monterey*) or later, you will have to edit a **configuration file** within the application container itself. Don’t worry, instructions are in the warning box below. 

```{warning}
:class: dropdown
On more modern *MacOS* computers (*MacOS 12* and later) you will need to **edit** the `info.plist` file in the package of the *MacMolPlt* application and add the following parameter in the first `<dict>` group…
  
  `<key>NSHighResolutionCapable</key>` <br>
  `<string>False</string>`

Find the application icon and right-click on it. Select Show package Contents from the drop-down menu. navigate and find the info.plist file and open it to make your changes. Back it up before you do so. This will force the program to operate in old-fashioned regular resolution. It is an old program and expects old screens.

On *MacOS 11* and earlier, you can check a box in the `Get Info` menu item of *wxMacMolPlt* for `Open in Low Resolution.` Apple deprecated this option and eliminated it in *MacOS 12*, hence the **awkward work-around** above. I have no idea what the new “Apple Silicon” macs will do with this. Buy me a new MacBook and I’ll let you know.
```

### Using *wxMacMolPlt*

The application itself is called *wxMacMolPlt*. I will continue to refer to it as *MacMolPlt* in this document. Just click on the application icon and you will get a blank window to **start building** a molecule. Explore the menu and you will quickly get the hang of it.

An [instruction manual](http://brettbode.github.io/wxmacmolplt/) is available on the website. More specific instructions on using *MacMolPlt* will be given in each exercise where we **build** molecules, **optimize** their structure and **analyze** the results of *GAMESS* calculations. Practice makes perfect.



## Installing Avogadro

*Avogadro* is an open source application for **building molecules** and can export and interpret input and output files for *GAMESS*. It has many interesting features to explore. One very useful tool is the auto-optimization feature that will minimize the energy of your molecule using **molecular mechanics**. This will produce a structure that is closer to ground state and therefore faster to optimize in *GAMESS*.

### Obtain and Install

You can [download *Avogadro*](http://avogadro.cc) from the project’s website. Install the software and that’s it. Open it and **explore** the menus.

### Using Avogadro

An [instruction manual](http://avogadro.cc) is available at the same website. We will explore *Avogadro* as we perform our experiments. There is no substitute for trial and error.




## Next Steps

We are now ready to do some calculations. We can **build** molecules and create **input files** using *MacMolPlt* or *Avogadro*. We can **submit** the files to *GAMESS* using *GamessQ*. We can then **extract** specific information using *Unix* tools and shell scripts or load the result files into *MacMolPlt* or *Avogadro* to **visualize** the result. We will be able to explore how steric strain arises in molecules and how structure affects the transition state in reactions. We will be able to see graphical representations of molecular orbitals and, in many cases, the local bonding orbitals that more closely align with Lewis structure. I hope that you will gain a **more intuitive understanding** of molecular structure and reaction kinetics.


[^linux]: *Linux* users will have to compile the source code. Go for it! Please make notes on your epic journey and share them with your peers. Everyone should use *Linux*, we just need you to show us the way. I am too timid and so I use *MacOS*. I envy you, but I will not join you; others may if you lead them. Rock on!
[^telnet]: Your *Unix* system will have a secure shell (*ssh*) tool that can be called using the *ssh* command. It will likely be an implementation of the *OpenSSH* suite of internet tools. No one uses *telnet* anymore, but it has become a verb for the act of using *ssh*.
