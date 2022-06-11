
# Building Your System

First we must build a system of tools for computational chemistry. You can access the software and install it on your computer using the following instructions.

## The Software

These instructions below assume that you are using a *Unix*-based computer, like a *Linux* system or an Apple *MacOS* computer. I have lived in this *Unix* world my whole academic life and am largely unfamiliar with *Windows* systems. However, the websites below have information on installing these tools on *Windows* systems. 

### *GAMESS*

*GAMESS* is proprietary application that performs quantum mechanical calculations. There is too much about quantum chemistry to even begin to explain it here. We will use it as a mysterious black box so be sure to follow the recipes. The *GAMESS* software and instructions can be obtained at https://www.msg.chem.iastate.edu/GAMESS/

You will need to apply for a free academic license and wait for a reply with a password for downloading *GAMESS*. You can obtain compiled executable binaries for *Windows*, *Linux* and *MacOS* machines. You can also get the source code if you want to compile it yourself.

### *GamessQ*

*GamessQ* is a graphical batch queue for *GAMESS*. You will be able to add files to the queue and observe their progress. It is the best way to run *GAMESS* so I recommend using it. The software and instructions can be obtained at https://www.msg.chem.iastate.edu/GAMESS/GamessQ/

### MacMolPlt

*MacMolPlt* is a graphical interface for building molecules, creating input files for *GAMESS* and then visualizing the information in the output files produced by *GAMESS*. It can be obtained at http://brettbode.github.io/wxmacmolplt/

### Avogadro
*Avogadro* is similar to *MacMolPlt* but more modern is style. It is open source and benefits from many contributors. *Avogadro* can be obtained at http://avogadro.cc

### Required Tools

#### Text Editor

We will need a text editor. We could use *TextEdit*, which comes with *MacOS*. I use *[BBEdit](https://www.barebones.com/products/bbedit/)*, which has a useful free version available for *MacOS*. Also Microsoft provides a free tyext editor designed for writing code called *[VisualStudio](https://code.visualstudio.com/)*.

#### Terminal Emulator

We will be accessing the *Unix* file system and tools. On a *MacOS* system there is an application called *Terminal* that will allow us to access the real computer that lives inside your computer. 


---------
## Installing GAMESS

*GAMESS* is a modern and constantly updated suite of software. However, it has no interface that the user interacts with. Jobs will be sent to *GAMESS* and output files will be sent back. It is controlled from the command line or via helper applications like *GamessQ* (see below). So, we will need to do a small amount of configuring via a text editor.

### Obtain and Install

Apply for a license for *GAMESS* by following the instruction on the Mark Gordon group website.[^gamess_link]  You will receive an email with instructions on downloading the files. You can download the source code or a pre-compiled binary for a your computer. 

The *GAMESS* application is available as a pre-compiled binary for *MacOS* and *Windows*.[^linux]  I received my email, followed the instructions and downloaded a file for the latest version of the *MacOS* binary. I decompressed the file and placed the resulting gamess directory folder in my `/Applications` folder.

### The GAMESS Folder

Within the `/Applications/gamess` directory are several important files. Two of which you may chose to edit. Below are the files and some brief descriptions.

| File                  | Description                                                    |
| :-------------------- | :------------------------------------------------------------- |
| auxdata               | A directory with important data for calculations               |
| gamess.30Jun2020R1.x	| The *GAMESS* application binary                                  |
| gms-files.csh	        | A shell script that defines environmental variables for *GAMESS*|
| rungms 	            | A shell script that is use to send your input file to *GAMESS*    |
| tests	                | A directory of sample jobs to test your installation           |
| ddikick.x	            | A binary application used by *GAMESS* to complete a run          |
| gms	                | A shell script used to call the *rungms* shell script            |
| README	            | Instructions for using the *gms* shell script to run **GAMESS      |

The *rungms* and *gms* scripts contain variables that can be changed to customize the behaviour of *GAMESS* on your computer. 

### Editing RUNGMS

Open *rungms* in a text editor. The first lines of the script define directories for the scratch files. These are important to define. The default is the home directory of the rungms script, but you will likely want your result files to appear somewhere else. I changed the first four lines of the script…

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

This means that the *GAMESS* scratch directory (SCR) is no longer the home directory of the application but a directory within it called scr. The scratch directory contains huge temporary files that are generally deleted when the calculation is complete, but if it crashes the files may remain. I wanted a separate directory so that any leftover junk would be easy to delete every now and then.

Be sure to create the `/Applications/gamess/scr` directory.

The user scratch (USERSCR) directory contains data files that are written out with the completion of a calculation. These files contain orbital and frequency data among many other sets of useful information. We only occasionally need these files but they will now be stored in a directory of my choice rather than the `/Applications/gamess` directory. Be sure to create that directory where it is expected to be.

The location of the *GAMESS* binary file is specified with GMSPATH. I set it to the location of the `gamess.30Jun2020R1.x` binary in my `/Applications` folder. The *gms* script generally does not need any changes, but you may want to change the very last line that declares the location of *rungms*. *gms* is used to run a *GAMESS* job from the command line and assumes that *rungms* is in the same directory as *gms*.

### Running GAMESS

*GAMESS* can be run from the terminal command line by calling `gms`. For example, the command:
`gms cyclohexane.inp` will call the *rungms* script using 1 processor and produce a result file called `cyclohexane.log`.

`gms -l result.log -n 2 cyclohexane.inp` will do the same but write the result to a file named `result.log` and use 2 processors in your computer.

We will begin with using the terminal command line to run *GAMESS*. Later, we will use a batch controller called *GamessQ*. 

------------
## Installing GamessQ

*GamessQ* is a batch queue for *GAMESS* provided by the Gordon group. It is available from the same web site.[^gamess_link]  

### Obtain and Install

Download the compressed file and extract it. Put the resulting folder in `/Applications`. In the `/Applications/GamessQ` directory we will see the following files$\ldots$

| File                  | Description                                                    |
| :-------------------- | :------------------------------------------------------------- |
| GamessQ.app	        | The application for the MacOS GUI interface                    |
| gamessq.html	        | Instructions                                                   |
| gamessqd	            | The background daemon application                              |

You will need to run the *gamessqd* application first. If you double-click on it it will run via a terminal window. The *Terminal* app will open and run the executable binary *gamessqd*. It will keep running as long as that terminal window is open. After this daemon has been launched, you will double-click on the *GamessQ* application to open the graphic interface. *GamessQ* will not run if *gamessqd* has not already been activated.

Click on the *GammesQ* icon to run the program. In the menus, open \[GamessQ`$\rightarrow$`Preferences\] and you will see two important settings. The first is the location of the spool directory for *GamessQ*. This is where *GamessQ* will move the final result files from a *GAMESS* calculation. The second is the location of the directory for the *rungms* script that runs *GAMESS*.  Create a directory for the result files and point *GamessQ* there. And then enter the location of the `/Applications/gamess` folder. Now it is ready to launch jobs.

### Using GamessQ

To use *GamessQ*, you drag and drop the input files onto its window. This will place the job in the queue. You can see when jobs are waiting, running and finished. You can drop in dozens of jobs and let them run over the weekend this way.

There is a command line version of *GamessQ* that you can compile and run directly on your computer. This can be useful if you want to set up a dedicated computer to run *GAMESS*. You will be able to *telnet* (look it up) using *ssh*[^telnet] (look it up) into your account on that computer. Then you can transfer over input files and submit jobs to the queue using *gamessq* directly. 


------

## Summary of System Setup

The following directories were created and files and settings altered accordingly:

| Directory Created	| Where to make changes |
| :----- | :------- |
| `/Applications/gamess/scr` |	edit *rungms* |
| `~/Documents/CompChem/GAMESS-SCR` |	edit *rungms* |
| `~/Documents/CompChem/GAMESS-RESULTS` |	preferences in *GamessQ*  |


With this setup we will see copies of the input files and the result file produced by calculation appear in the GAMESS-RESULTS directory. The data files will appear in the GAMESS-SCR directory. BEWARE! Result files and input file copies in GAMESS-RESULTS will be deleted whenever you clear the queue in GamessQ by clicking on the cleanup button. So be sure to copy them to somewhere else if you want to be sure to keep them.

You can create your own setup however you like. Just edit the rungms script and the GamessQ preferences accordingly.

------

## Installing MacMolPlt

MacMolPlt is a molecular editing and visualization application. It can be used to construct 3-D structures and create input files for GAMESS. It can interpret the resulting output files and produce visualization of bond vibrations and frequencies, molecular energies and molecular orbitals and other surfaces.

### Obtain and Install

You can obtain MacMolPlt at the github repository. Just unpack the downloaded file and put the application folder in your /Applications directory. If you are running MacOS 12 (Monterey) or later you will have to edit a configuration file within the application itself. Don’t worry, instructions are below. 

```{warning}
On more modern *MacOS* computers (*MacOS 12* and later) you will need to edit the `info.plist` file in the package of the *MacMolPlt* application and add the following parameter in the first `<dict>` group…
  
  `<key>NSHighResolutionCapable</key>` <br>
  `<string>False</string>`

This will avoid a scaling problem with the high-resolution screens on modern Apple computers. It will force the program to operate in old-fashioned regular resolution. It is an old program and expects old screens.
On *MacOS 11* and earlier, you can check a box in the "Get Info" menu item of *wxMacMolPlt* for “Open in Low Resolution.” Apple deprecated this option and eliminated it in *MacOS 12*, hence the awkward word-around above. I have no idea what the new “Apple Silicon” macs will do with this. Buy me a new MacBook and I’ll let you know.
```

### Using wxMacMolPlt

The application itself is called *wxMacMolPlt*. I will continue to refer to it as *MacMolPlt* in this document. Just click on the application icon and you will get a blank window to start building a molecule. Explore the menu and you will quickly get the hang of it.

An instruction manual is available on the website.[^macmolplt] More specific instructions on using *MacMolPlt* will be given in each exercise where we build molecules, optimize their structure and analyze the results of GAMESS calculations. Practice makes perfect.

------

## Installing Avogadro

*Avogadro* is an open source application for building molecules and can export and interpret input and output files for *GAMESS*. It has many interesting features to explore. One very useful tool is the auto-optimization feature that will minimize the energy of your molecule using molecular mechanics. This will produce a structure that is closer to ground state and therefore faster to optimize in *GAMESS*
. 
### Obtain and Install

You can download Avogadro from the project’s website.[^avogadro_link] Install the software and that’s it. Open it and explore the menus.

### Using Avogadro

An instruction manual is available at the same website. We will explore *Avogadro* as we perform our experiments. There is no substitute for experience.

------

## Using Unix

The results file may contain thousands of lines of text. How can we find the useful bits. I am using a Unix (sort of) operating system and can access the enormously powerful Unix toolchain. I will be using the terminal running a shell (a command line interface), standard directory navigation and the Unix tools *grep*, *sed* and *awk*.

### The Shell
A common Unix shell is *bash*. It provides commands for navigating directories and for running programs. It also provides a scripting language so that I can make my own tools using a set of shell commands in a file. Lots of information is available about *bash*.

```{note} 
Recent versions of *MacOS* use *zsh* rather than *bash*. But *bash* is still available and we will be using it to run our scripts. *zsh* is almost completely compatible with *bash* and the scripts will run fine in *zsh*. I am a creature of habit.
```

### The Terminal Application

On my computer there is an application called *Terminal* that runs a terminal emulation window to the *Unix* system underneath the GUI interface. When the terminal window opens, we are already in the shell program. Most *Unix* systems will start with the *bash* shell  and you can change to other shell programs easily if you wish. 


### Unix Commands

Here are some essential Unix commands to know. 

``` {note}
A starting point for learning Unix tools can be found at http://mally.stanford.edu/~sr/computing/basic-unix.html and also at https://en.wikipedia.org/wiki/List_of_Unix_commands . Search and you shall find.
```

#### *cd*

The *cd* this command will change the directory. The directory structure in Unix begins with ~. The squiggle is your home directory.  If you enter `cd ~`, you will switch to your home directory. I entered `cd ~/Documents/CompChem/Folder` to switch to a directory named Folder in my CompChem directory in my Documents folder in my home (~) folder
.
#### *pwd*

“Present working directory” is what *pwd* is. This command will return the directory where you are.  It is useful when you want to see exactly where you are in the directory system.

#### *ls*

This command will give you a list of files, applications and directories. Enter `ls` and you will get the list for the current directory.

#### *man*

The *man* tool is very useful. It will call up the documentation any Unix command or tool it its database. Type `man` and see what happens. Use arrow keys to move around the document or the space bar to page down. Strike CTRL-Z to exit the *man* system. Between *man* and the internet you can learn much more about these essential commands.

### Manipulating Text Files

#### *grep*

We can extract just the lines that we want from the large result file. *grep* will read a file (or a list of files) line by line and return only the lines that contain a given text string. The command `grep "NSERCH" ResultFile.log` will extract the text lines that contain the string NSERCH, which is the step number for each optimization step of an optimization calculation. The last step will include the final energy. Rather than scan through 2000 of more lines of text output we could just grep out the lines we want.

#### Redirect

You can redirect the output of command from the screen to a file. The `>` character is a shell operator that will write output that would have been printed to your terminal window to a file instead.  The command `ls > directory.txt` will create a file called directory.txt and flow the output of ls into that file.

#### Pipes
A “pipe” is the ‘\|’ character.  This use usually over the backslash (\\) on your keyboard and is accessed via \[shift\]-\\. (Usually located on the right-hand side of an ANSI QWERTY keyboard, above the \[RETURN/ENTER\] key and under the \[BACKSPACE/DELETE\] key.) It is a shell operator that can be used to combine commands. (Just like how the plus sign is an operator that can combine two numbers in math).

A pipe is placed between two commands. The output of the first command is “piped” into the second command as its input. For example the command ls -l will produce a detailed file list for your current directory. What if you have hundreds of files in your directory and you are looking for just the details on one. The command `ls -l | grep ResultFile` will pipe the output of the directory command into the grep command, which will then output the lines that contain the string "ResultFile", e.g. ResultFile.log and ResultFile.inp.

#### *sed*

We can search and substitute a string in a text file with the *sed* tool. It is a powerful command-line version of “search and replace.” For example the command `sed "s/NUMBER/100/" InputFile.inp > NewInputFile.inp` will read the file “InputFile.inp”, replace the string “NUMBER” with the string “100” and direct the output to a file names “NewInputFile.inp”.

#### *awk*

What *grep* and *sed* are to text lines, awk is to text columns. It is a powerful tool for manipulating table data in text files. There are many tables of data output in *GAMESS* result files. Perhaps we will use it someday.

### Shell Scripts

You can place a series of *Unix* tools and shell commands and operators in a text file and run it as a shell script. That way you can execute a series of commands and even use logic and loops to perform more complicated tasks. We will be using scripts to automate making a series of related input files using *sed* and also to extract final energies from a related series of output files using *grep*
. 
#### Ready To Go

We are now ready to do some calculations. We can build molecules and create input files using *MacMolPlt* or *Avogadro*. We can submit the files to *GAMESS* using *GamessQ*. We can then extract specific information using *Unix* tools and shell scripts or load the result files into *MacMolPlt* or *Avogadro* and examine the result graphically. We will be able to explore how steric strain arises in molecules and how structure affects the transition state in reactions. We will be able to see graphical representations of molecular orbitals and, in many cases, the local bonding orbitals that more closely align with Lewis structure. I hope that you will gain a more intuitive understanding of molecular structure and reaction kinetics.


[^linux]:  Linux users will have to compile the source code. Go for it! Please make notes on your epic journey and share them with your peers. Everyone should use Linux, we just need you to show us the way. I am too timid to leave my soft warm bed and so I use MacOS. I envy you, but I will not join you; others may if you lead them. Rock on!
[^telnet]: Your Unix system will have a secure shell (ssh) tool that can be called using the ssh command. It will likely be an implementation of the OpenSSH suite of internet tools. No one uses telnet anymore, but it has become a verb for the act of using ssh.
