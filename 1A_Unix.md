# Using Unix

The results file may contain **thousands of lines** of text. How can we find the useful bits? I am using a *Unix* (sort of) operating system and can access the enormously powerful ***Unix* toolchain**. I will be using the **terminal** running a **shell** (a command line interface), standard directory navigation and the *Unix* tools ***grep***, ***sed*** and ***awk***.

## The Shell
```{margin} 
Recent versions of *MacOS* use *zsh* rather than *bash*. But *bash* is still available and we will be using it to run our scripts. *zsh* is almost completely compatible with *bash* and the scripts will run fine in *zsh*. I am a creature of habit.
```

A common *Unix* shell is ***bash***. It provides commands for **navigating** directories and for **running** programs. It also provides a **scripting language** so that I can make my own tools using a set of **shell commands** in a file. Lots of information is available about *bash*.


## The Terminal Application

On my computer there is an application called ***Terminal*** that runs a terminal emulation window to the *Unix* system underneath the GUI interface. When the terminal window opens, we are already in the shell program. Most *Unix* systems will start with the *bash* shell and you can change to other shell programs easily if you wish. 


## Unix Commands

``` {margin}
A starting point for learning Unix tools can be found [here](http://mally.stanford.edu/~sr/computing/basic-unix.html) and [here](https://en.wikipedia.org/wiki/List_of_Unix_commands). Search and you shall find.
```
Here are some essential *Unix* commands to know. 

### *cd*

The *cd* command will **change the directory**. The directory structure in *Unix* begins with `~`. The squiggle is your home directory.  If you enter `cd ~`, you will switch to your home directory. I entered `cd ~/Documents/CompChem/Folder` to switch to a directory named Folder in my CompChem directory in my Documents folder in my home (~) folder.

### *pwd*

“**Present working directory**” is what *pwd* is. This command will return the directory where you are.  It is useful when you want to see exactly where you are in the directory system.

### *ls*

This command will give you a **list of files**, applications and directories. Enter `ls` and you will get the list for the current directory.

### *man*

The *man* tool is very useful. It will call up the **documentation** any *Unix* command or tool it its database. Type `man` and see what happens. Use arrow keys to move around the document or the space bar to page down. Strike CTRL-Z to exit the *man* system. Between *man* and the internet you can **learn more** about all of these essential commands.

## Manipulating Text Files

### *grep*

We can **extract** just the lines that we want from the large result file. *grep* will read a file (or a list of files) line by line and return **only the lines** that contain a given text string. The command `grep "NSERCH" ResultFile.log` will extract the text lines that contain the string NSERCH, which is the step number for each optimization step in a calculation. The last optimization step will include the final energy. Rather than scan through 2000 of more lines of text output we could just *grep* out the lines we want.

### Redirect

You can **redirect** the output of command from the screen **to a file**. The `>` character is a shell operator that will write output (that would have been printed to your terminal window) to a file.  The command `ls > directory.txt` will create a file called directory.txt and flow the output of *ls* into that file.

### Pipes
A “pipe” is the ‘\|’ character.  This use usually over the backslash (\\) on your keyboard and is accessed via \[shift\]-\\ . (It is usually located on the right-hand side of an ANSI QWERTY keyboard, above the \[RETURN/ENTER\] key and under the \[BACKSPACE/DELETE\] key.) It is a shell operator that can be used to **combine commands**. (Just like how the plus sign is an operator that can combine two numbers in math).

A pipe is placed **between** two commands. The output of the first command is “piped” into the second command as its input. For example the command `ls -l` will produce a detailed file list for your current directory. What if you have hundreds of files in your directory and you are looking for just the details on one? The command `ls -l | grep ResultFile` will pipe the output of the directory command into the *grep* command, which will then output the lines that contain the string `ResultFile`, e.g. ResultFile.log and ResultFile.inp.

### *sed*

We can **search and substitute** in a line in a text file with the *sed* tool. It is a powerful command-line version of “search and replace.” For example, the command `sed "s/NUMBER/100/" InputFile.inp > NewInputFile.inp` will read the file “InputFile.inp”, replace the string “NUMBER” with the string “100” and direct the output to a file named “NewInputFile.inp”.

### *awk*

What *grep* and *sed* are to text lines, awk is to text **columns**. It is a powerful tool for manipulating table data in text files. There are many **tables** of data output in *GAMESS* result files. Perhaps we will use it someday.

## Shell Scripts

You can place a series of *Unix* tools and shell commands and operators in a text file and run it as a shell script. That way you can **execute a series of commands** and even use **logic and loops** to perform more complicated tasks. We will be using scripts to **automate** making a series of related input files using *sed* and also to extract final energies from a related series of output files using *grep*.
