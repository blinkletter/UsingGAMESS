# Butadiene.inp

Below is the output file for the butadiene optimization job.

```{code-block} 
---
name: Butadiene.inpFILE
caption: Butadiene.inp
---
!   File created by MacMolPlt 7.7.2
 $CONTRL SCFTYP=RHF RUNTYP=OPTIMIZE MAXIT=30 MULT=1 COORD=ZMT NZVAR=24 
    MOLPLT=.TRUE. $END
 $SYSTEM TIMLIM=525600 MEMORY=1000000 $END
 $BASIS GBASIS=N21 NGAUSS=3 NDFUNC=1 $END
 $SCF DIRSCF=.TRUE. $END
 $STATPT OPTTOL=0.0001 NSTEP=20 HESS=GUESS $END
 $DATA 
Title
C1
C
C  1    1.54000
C   2    1.54000  1 120.0000
C   3    1.54000  2 120.0000  1 180.0000
H   1    1.14000  2 120.0000  3   0.0000
H   1    1.14000  5 120.0000  2 180.0000
H   2    1.14000  1 120.0000  3 180.0000
H   3    1.14000  4 120.0000  2 180.0000
H   4    1.14000  3 120.0000  7   0.0000
H   4    1.14000  9 120.0000  3 180.0000
 $END
 $ZMAT IZMAT(1)=1,2,1, 1,3,2, 2,3,2,1, 1,4,3, 2,4,3,2, 3,4,3,2,1, 1,5,1, 
    2,5,1,2, 3,5,1,2,3, 1,6,1, 2,6,1,5, 3,6,1,5,2, 1,7,2, 2,7,2,1, 3,7,2,1,3, 
    1,8,3, 2,8,3,4, 3,8,3,4,2, 1,9,4, 2,9,4,3, 3,9,4,3,7, 1,10,4, 2,10,4,9, 
    3,10,4,9,3 $END
```