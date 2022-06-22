# *GAMESS* Workflow

Here will be presented the **step by step** workflow for calculating the energy profile for rotating the central bond of butane. We have seen that butane has energy minima at torsion angles of 180&deg; and 67&deg;. It also has a maximum at 0&deg;. Is the other maxima at 120&deg; or is it slightly **offset** due to the size difference between a hydrogen and a methyl group? We will make many input files with locked torsion angles varying fro 0&deg; to 180&deg; and then calculate the **optimized** structures at each locked angle. The energies will be extracted from the output files and we will then plot the potential energy profile for bond rotation.

## The Input File

First we **write** an input file for butane. We will not use symmetry because we want to rotate the bond to many different angles. We will use the *Z-matrix* method because it will identify the central **torsion** as a coordinate. Then we can **lock** that coordinate.

```{code-block}
---
name: butane-SCAN.inp
linenos: True
lineno-start: 1
emphasize-lines: 
caption: butane-SCAN.inp
---
 $CONTRL 
     SCFTYP=RHF 
     RUNTYP=OPTIMIZE 
     MAXIT=30 
     MULT=1 
     COORD=ZMT 
     NZVAR=36 
 $END
 $SYSTEM 
     TIMLIM=525600 
     MEMORY=1000000 
 $END
 $BASIS 
     GBASIS=N21 
     NGAUSS=3 
 $END
 $SCF DIRSCF=.TRUE. $END
 $STATPT 
     OPTTOL=0.0001 
     NSTEP=1000 
     IFREEZ(1)=6 $END
 $DATA 
Butane
C1
C
C   1    1.54000
C   2    1.54000  1 109.0
C   1    1.54000  2 109.4712   3   NUMBER
H   1    1.14000  2 109.4712   4 -120.0000
H   1    1.14000  5 108.5      2  120.0000
H   2    1.14000  1 109.4712   3 -120.0000
H   2    1.14000  7 109.4712   1  120.0000
H   3    1.14000  2 109.4712   8    0.0000
H   3    1.14000  9 109.4712   2  120.0000
H   3    1.14000  9 109.4712  10  120.0000
H   4    1.14000  1 109.0      6   -0.0000
H   4    1.14000  12 108.5     1  120.0000
H   4    1.14000  12 109.4712 13  119.0000
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
                1,14,4, 2,14,4,12, 3,14,4,12,13 
 $END
```

You will see that not all angles are 109.47&deg;. I **jiggled** some to avoid any perfect symmetry locks that prevented the energy minimization from converging in one of the jobs last time.

## Making the Series

We will then use the following **shell script** to replace the string "NUMBER" with number from a list and create a new file with a name series based on the list. The script is shown below.

```{code-block} bash
---
name: makescan.sh1
caption: makescan.sh
---
input_file=butane-SCAN.inp
spacer=_
for num in $(seq -w 000 010 180)
do
  sed "s/NUMBER/$num/" $input_file > "$input_file$spacer$num.inp"
done
```

This script will take the **contents** of the `butane-SCAN.inp` file and use the *sed* tool to replace the string "`NUMBER`" with the value `num`. The result is then **written** to a new file ending with the same value, `num`.

I **executed** the script with the following command: 

```shell
bash makescan.sh
```

Nineteen new files are created with angles for the `4,1,2,3` torsion varying from `00` to `180` in steps of `10`. **Observe** the sequence of commands shown in {numref}`fig5w-1`. We start with `ls` to list the files in the directory and see the two files that we created. Then the bash script is executed. A second `ls` command then reveals all the new files that were created.

```{figure} images/workflow1.png
---
width: 500px
name: fig5w-1
---
*A *Unix* terminal running the command to setup the file list.*
```

## Running the Jobs

We now have nineteen jobs to submit to *GAMESS*. I will use the *GamessQ* GUI interface to do that. Execute the *GamessQ* application. Drag and drop the file series into the *GamessQ* window. *GamessQ* will copy the input files so we will have a set of identical input files created that we don't care about. As *GAMESS* produces output files they will be saved alongside the copied input files. I set up the destination to be the same folder as where the original files were placed. The window of the whole *GamessQ* operation in progress is shown in {numref}`fig5w-2`

```{figure} images/workflow2.png
---
width: 500px
name: fig5w-2
---
**GamessQ* running a queue of *GAMESS* jobs*
```

## Extracting the Results

When the jobs are all complete we will run a *bash* script that will **extract** the last `NSERCH ENERGY` line from each file and save this set of lines in a single result file that we will name `butane_result.txt`. The script is presented below.

```{code-block} bash
---
name: extract.sh1
caption: extract.sh
---
for name in butane_SCAN*.log; do
    grep -H "NSERCH" "$name" | grep "GRAD" | tail -n 1
done
```

As you can see neither script was complicated, but they are both very cryptic. Everyday I promise myself that I will rewrite then in *Python* but, since they work, that may never happen.

the output of extract.sh will go to the STDOUT (the screen in most cases) but we can direct it into a file using the `>` operator. I will execute the script using the following command. In {numref}`fig5w-3` we see a **terminal** with the command executed

```shell
bash extract.sh > butane_result.txt
```

```{figure} images/workflow3.png
---
width: 500px
name: fig5w-3
---
*Terminal window showing the execution of the *extract.sh* script.*
```

## Inspecting the Result

If you open the `butane_result.txt` file in a text editor you will see nineteen lines of data, one line for ezch file. 

```{code-block}
---
name: butane_result.txt
caption: butane_result.txt
---
butane_SCAN.inp_000_303.log: NSERCH:  23  E=     -156.4228465418  GRAD. MAX=  0.0000585  R.M.S.=  0.0000204
butane_SCAN.inp_010_304.log: NSERCH:  18  E=     -156.4233726910  GRAD. MAX=  0.0000931  R.M.S.=  0.0000255
butane_SCAN.inp_020_305.log: NSERCH:  16  E=     -156.4247889225  GRAD. MAX=  0.0000789  R.M.S.=  0.0000273
butane_SCAN.inp_030_306.log: NSERCH:  16  E=     -156.4267021853  GRAD. MAX=  0.0000394  R.M.S.=  0.0000149
butane_SCAN.inp_040_307.log: NSERCH:  19  E=     -156.4286426893  GRAD. MAX=  0.0000765  R.M.S.=  0.0000260
butane_SCAN.inp_050_308.log: NSERCH:  18  E=     -156.4301847220  GRAD. MAX=  0.0000241  R.M.S.=  0.0000105
butane_SCAN.inp_060_309.log: NSERCH:  23  E=     -156.4310615763  GRAD. MAX=  0.0000675  R.M.S.=  0.0000212
butane_SCAN.inp_070_310.log: NSERCH:  25  E=     -156.4312168483  GRAD. MAX=  0.0000339  R.M.S.=  0.0000129
butane_SCAN.inp_080_311.log: NSERCH:  24  E=     -156.4306888649  GRAD. MAX=  0.0000987  R.M.S.=  0.0000300
butane_SCAN.inp_090_312.log: NSERCH:  26  E=     -156.4295739060  GRAD. MAX=  0.0000494  R.M.S.=  0.0000155
butane_SCAN.inp_100_313.log: NSERCH: 390  E=     -156.4282209688  GRAD. MAX=  0.0000578  R.M.S.=  0.0000160
butane_SCAN.inp_110_314.log: NSERCH:  23  E=     -156.4271414620  GRAD. MAX=  0.0000819  R.M.S.=  0.0000247
butane_SCAN.inp_120_315.log: NSERCH:  24  E=     -156.4267263463  GRAD. MAX=  0.0000884  R.M.S.=  0.0000234
butane_SCAN.inp_130_316.log: NSERCH: 362  E=     -156.4271134870  GRAD. MAX=  0.0000551  R.M.S.=  0.0000145
butane_SCAN.inp_140_317.log: NSERCH:  21  E=     -156.4281850977  GRAD. MAX=  0.0000701  R.M.S.=  0.0000323
butane_SCAN.inp_150_318.log: NSERCH:  21  E=     -156.4296331216  GRAD. MAX=  0.0000712  R.M.S.=  0.0000225
butane_SCAN.inp_160_319.log: NSERCH: 646  E=     -156.4310600533  GRAD. MAX=  0.0000567  R.M.S.=  0.0000254
butane_SCAN.inp_170_320.log: NSERCH:  20  E=     -156.4320918106  GRAD. MAX=  0.0000675  R.M.S.=  0.0000216
butane_SCAN.inp_180_321.log: NSERCH:  23  E=     -156.4324667182  GRAD. MAX=  0.0000605  R.M.S.=  0.0000189
```

Observe that three of the jobs took a **longer time** to converge. We could open them in *MacMolPlt* and watch a "movie" of their journey and plot the energies along the way. Where did they get stuck? All three eventually found their way home, but only because this was a light-weight theory level and I was confidient in **allowing** for a large number of steps. If the level of theory was higher I might have set the **limit** to 100 steps, or even 30 steps. All other jobs converged in less than 30 steps.

Why did these three take so long? **Bad luck** with the exact structure of the input started them on the long path. Tweak a few bond lengths or angles and they might converge just like the others. Clearly, **how you start matters**. For high levels of theory it is important to start as close to the final answer as possible.

We now have the raw data. Next we will process it and **plot the results** using Python. The next subchapter is an **interactive *Python*** notebook that details this workflow.