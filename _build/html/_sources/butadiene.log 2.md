# Butadiene.log

Below is the output file for the butadiene optimization job.

**Butadiene.log**
```{code-block} 
---
name: Butadiene.logFILE
linenos: True
lineno-start: 1
emphasize-lines:
caption: Butadiene.log
---
----- GAMESS execution script 'rungms' -----
This job is running on host Barrys-MacBook-Pro-13.local
under operating system Darwin at Tue 2 Nov 2021 00:37:04 ADT
Available scratch disk space (Kbyte units) at beginning of the job is
Filesystem   1024-blocks      Used Available Capacity iused     ifree %iused  Mounted on
/dev/disk1s2   488245288 427946380  41166280    92% 2989458 411662800    1%   /System/Volumes/Data
GAMESS temporary binary files will be written to ./
GAMESS supplementary output files will be written to ./
Copying input file ../../TempFiles/Butadiene_121.inp to your run's scratch directory...
cp ../../TempFiles/Butadiene_121.inp .//Butadiene_121.F05
unset echo
.//ddikick.x .//gamess.30Jun2020R1.x Butadiene_121 -ddi 1 1 localhost -scr ./

 Distributed Data Interface kickoff program.
 Initiating 1 compute processes on 1 nodes to run the following command:
 .//gamess.30Jun2020R1.x Butadiene_121 

          *******************************************************
          *                                                     *
          *          GAMESS VERSION = 30 JUN 2020 (R1)          *
          *                                                     *
          *              doi.org/10.1063/5.0005188              *
          *                                                     *
          **************** 64 BIT APPLE VERSION *****************

  GAMESS HAS BEEN MADE POSSIBLE WITH IMPORTANT CONTRIBUTIONS FROM
  THE FOLLOWING INDIVIDUALS (IN ALPHABETICAL ORDER):

     IVANA ADAMOVIC, CHRISTINE AIKENS, TOMOKO AKAMA,
     YURI ALEXEEV, YURIKO AOKI, POOJA ARORA, TOSHIO ASADA,
     ANDREY ASADCHEV, KIM K. BALDRIDGE, PRADIPTA BANDYOPADHYAY,
     MARIA BARYSZ, ROB BELL, JONATHAN BENTZ, COLLEEN BERTONI,
     JERRY A. BOATZ, BRETT BODE, KURT BRORSEN, KURT R. BRORSEN,
     LAIMUTIS BYTAUTAS, CALEB CARLIN, LAURA CARRINGTON,
     GALINA CHABAN, BENOIT CHAMPAGNE, WEI CHEN, MAHITO CHIBA,
     DAN CHIPMAN, CHEOL HO CHOI, TANNER CULPITT, PAUL DAY,
     ALBERT DEFUSCO, NUWAN DESILVA, J. EMILIANO DEUSTUA,
     TIM DUDLEY, MICHEL DUPUIS, STEVEN T. ELBERT,
     DMITRI FEDOROV, ALEX FINDLATER, GRAHAM FLETCHER,
     MARK FREITAG, CHRISTIAN FRIEDL, DAVID GARMER,
     IGOR S. GERASIMOV, KURT GLAESEMANN, MARK S. GORDON,
     JEFFREY GOUR, FENG LONG GU, EMILIE B. GUIDEZ,
     ANASTASIA GUNINA, SHARON HAMMES-SCHIFFER, MASATAKE HARUTA,
     KIMIHIKO HIRAO, YASUHIRO IKABATA, TZVETELIN IORDANOV,
     STEPHAN IRLE, KAZUYA ISHIMURA, JOE IVANIC, FRANK JENSEN,
     JAN H. JENSEN, VISVALDAS KAIRYS, MUNEAKI KAMIYA,
     MICHIO KATOUDA, NAOAKI KAWAKAMI, DAN KEMP, BERNARD KIRTMAN,
     KAZUO KITAURA, MARIUSZ KLOBUKOWSKI, MASATO KOBAYASHI,
     PRAKASHAN KORAMBATH, JACEK KORCHOWIEC, SHIRO KOSEKI,
     KAROL KOWALSKI, JIMMY KROMANN, STANISLAW KUCHARSKI,
     HENRY KURTZ, SAROM SOK LEANG, HUI LI, SHUHUA LI, WEI LI,
     JESSE LUTZ, ALEKSANDR O. LYKHIN, MARCIN MAKOWSKI,
     JOANI MATO, NIKITA MATSUNAGA, BENEDETTA MENNUCCI,
     GRANT MERRILL, NORIYUKI MINEZAWA, VLADIMIR MIRONOV,
     EISAKU MIYOSHI, JOHN A. MONTGOMERY JR., HIROTOSHI MORI,
     JONATHAN MULLIN, MONIKA MUSIAL, SHIGERU NAGASE,
     TAKESHI NAGATA, HIROMI NAKAI, TAKAHITO NAKAJIMA,
     YUYA NAKAJIMA, HARUYUKI NAKANO, HIROYA NAKATA, SEAN NEDD,
     HEATHER NETZLOFF, KIET A. NGUYEN, YOSHIO NISHIMOTO,
     BOSILJKA NJEGIC, RYAN OLSON, MIKE PAK, ROBERTO PEVERATI,
     BUU PHAM, PIOTR PIECUCH, ANNA POMOGAEVA, DAVID POOLE,
     SPENCER PRUITT, OLIVIER QUINET, LUKE ROSKOP,
     KLAUS RUEDENBERG, ANDREW SAND, TOSAPORN SATTASATHUCHANA,
     NOZOMI SAWADA, MICHAEL W. SCHMIDT, PATRICK E. SCHNEIDER,
     JUNJI SEINO, PRACHI SHARMA, JUN SHEN, JIM SHOEMAKER,
     YINAN SHU, DEJUN SI, JONATHAN SKONE, LYUDMILA SLIPCHENKO,
     TONY SMITH, JIE SONG, MARK SPACKMAN, CASPER STEINMANN,
     WALT STEVENS, PEIFENG SU, SHUJUN SU, CHET SWALINA,
     TETSUYA TAKETSUGU, ZHEN TAO, NANDUN THELLAMUREGE
     SEIKEN TOKURA, JACOPO TOMASI, TSUGUKI TOUMA, TAKAO TSUNEDA,
     HIROAKI UMEDA, JORGE LUIS GALVEZ VALLEJO, YALI WANG,
     SIMON WEBB, AARON WEST, THERESA L. WINDUS, MARTA WLOCH,
     PENG XU, KIYOSHI YAGI, SUSUMU YANAGISAWA, YANG YANG,
     SOOHAENG YOO, TAKESHI YOSHIKAWA, FEDERICO ZAHARIEV,
     TOBY ZENG

  WHO ARE SUPPORTED BY THEIR INSTITUTION/UNIVERSITY/COMPANY/GROUP
  (IN ALPHABETICAL ORDER):

     EP ANALYTICS, FACULTES UNIVERSITAIRES NOTRE-DAME DE LA PAIX,
     INSTITUTE FOR MOLECULAR SCIENCE, IOWA STATE UNIVERSITY,
     JACKSON STATE UNIVERSITY, JOHANNES KEPLER UNIVERSITY LINZ,
     KYUSHU UNIVERSITY, MICHIGAN STATE UNIVERSITY,
     MIE UNIVERSITY, MOSCOW STATE UNIVERSITY,
     N. COPERNICUS UNIVERSITY, NAGOYA UNIVERSITY,
     NANJING UNIVERSITY, NAT. INST. OF ADVANCED INDUSTRIAL
     SCIENCE AND TECHNOLOGY, NATIONAL INST. OF STANDARDS AND
     TECHNOLOGY, NESMEYANOV INSTITUTE OF ORGANOELEMENT COMPOUNDS
     OF RUSSIAN ACADEMY OF SCIENCES, OSAKA PREFECTURE UNIVERSITY,
     PENNSYLVANIA STATE UNIVERSITY, TOKYO INSTITUTE OF TECHNOLOGY,
     UNIVERSITY OF AARHUS, UNIVERSITY OF ALBERTA,
     UNIVERSITY OF CALIFORNIA AT SANTA BARBARA,
     UNIVERSITY OF COPENHAGEN, UNIVERSITY OF IOWA,
     UNIVERSITY OF MEMPHIS, UNIVERSITY OF MINNESOTA,
     UNIVERSITY OF NEBRASKA, UNIVERSITY OF NEW ENGLAND,
     UNIVERSITY OF NOTRE DAME, UNIVERSITY OF PISA,
     UNIVERSITY OF SILESIA, UNIVERSITY OF TOKYO,
     UNIVERSITY OF ZURICH, WASEDA UNIVERSITY, YALE UNIVERSITY

  GAMESS SOFTWARE MANAGEMENT TEAM FOR THIS RELEASE:

     MARK S. GORDON (TEAM LEAD),
     BRETT BODE (SENIOR ADVISOR),
     GIUSEPPE BARCA,
     COLLEEN BERTONI,
     KRISTOPHER KEIPERT (ADVISOR),
     SAROM S. LEANG (DEVELOPMENT LEAD),
     BUU PHAM,
     JORGE LUIS GALVEZ VALLEJO (WEBSITE ADMINISTRATOR),
     PENG XU

 EXECUTION OF GAMESS BEGUN Tue Nov  2 00:37:04 2021

            ECHO OF THE FIRST FEW INPUT CARDS -
 INPUT CARD>!   File created by MacMolPlt 7.7.2                                             
 INPUT CARD> $CONTRL SCFTYP=RHF RUNTYP=OPTIMIZE MAXIT=30 MULT=1 COORD=ZMT NZVAR=24          
 INPUT CARD>    MOLPLT=.TRUE. $END                                                          
 INPUT CARD> $SYSTEM TIMLIM=525600 MEMORY=1000000 $END                                      
 INPUT CARD> $BASIS GBASIS=N21 NGAUSS=3 NDFUNC=1 $END                                       
 INPUT CARD> $SCF DIRSCF=.TRUE. $END                                                        
 INPUT CARD> $STATPT OPTTOL=0.0001 NSTEP=20 HESS=GUESS $END                                 
 INPUT CARD> $DATA                                                                          
 INPUT CARD>Title                                                                           
 INPUT CARD>C1                                                                              
 INPUT CARD>C                                                                               
 INPUT CARD>C  1    1.54000                                                                 
 INPUT CARD>C   2    1.54000  1 120.0000                                                    
 INPUT CARD>C   3    1.54000  2 120.0000  1 180.0000                                        
 INPUT CARD>H   1    1.14000  2 120.0000  3   0.0000                                        
 INPUT CARD>H   1    1.14000  5 120.0000  2 180.0000                                        
 INPUT CARD>H   2    1.14000  1 120.0000  3 180.0000                                        
 INPUT CARD>H   3    1.14000  4 120.0000  2 180.0000                                        
 INPUT CARD>H   4    1.14000  3 120.0000  7   0.0000                                        
 INPUT CARD>H   4    1.14000  9 120.0000  3 180.0000                                        
 INPUT CARD> $END                                                                           
 INPUT CARD> $ZMAT IZMAT(1)=1,2,1, 1,3,2, 2,3,2,1, 1,4,3, 2,4,3,2, 3,4,3,2,1, 1,5,1,        
 INPUT CARD>    2,5,1,2, 3,5,1,2,3, 1,6,1, 2,6,1,5, 3,6,1,5,2, 1,7,2, 2,7,2,1, 3,7,2,1,3,   
 INPUT CARD>    1,8,3, 2,8,3,4, 3,8,3,4,2, 1,9,4, 2,9,4,3, 3,9,4,3,7, 1,10,4, 2,10,4,9,     
 INPUT CARD>    3,10,4,9,3 $END                                                             
    1000000 WORDS OF MEMORY AVAILABLE

     BASIS OPTIONS
     -------------
     GBASIS=N21          IGAUSS=       3      POLAR=COMMON  
     NDFUNC=       1     NFFUNC=       0     DIFFSP=       F
     NPFUNC=       0      DIFFS=       F     BASNAM=        


     RUN TITLE
     ---------
 Title                                                                           

 THE POINT GROUP OF THE MOLECULE IS C1      
 THE ORDER OF THE PRINCIPAL AXIS IS     0

 YOUR FULLY SUBSTITUTED Z-MATRIX IS
 C   
 C      1   1.5400000
 C      2   1.5400000  1  120.0000
 C      3   1.5400000  2  120.0000  1  180.0000  0
 H      1   1.1400000  2  120.0000  3    0.0000  0
 H      1   1.1400000  5  120.0000  2  180.0000  0
 H      2   1.1400000  1  120.0000  3  180.0000  0
 H      3   1.1400000  4  120.0000  2  180.0000  0
 H      4   1.1400000  3  120.0000  7    0.0000  0
 H      4   1.1400000  9  120.0000  3  180.0000  0

 THE MOMENTS OF INERTIA ARE (AMU-ANGSTROM**2)
 IXX=    14.591   IYY=   135.646   IZZ=   150.238

 ATOM      ATOMIC                      COORDINATES (BOHR)
           CHARGE         X                   Y                   Z
 C           6.0    -3.8423404036        0.2396005484        0.0000000000
 C           6.0    -1.1570973044       -0.8822753861        0.0000000000
 C           6.0     1.1570973044        0.8822753861        0.0000000000
 C           6.0     3.8423404036       -0.2396005484        0.0000000000
 H           1.0    -4.1170126629        2.3763060324        0.0000000000
 H           1.0    -5.5554455036       -1.0666253479        0.0000000000
 H           1.0    -0.8824250451       -3.0189808701        0.0000000000
 H           1.0     0.8824250451        3.0189808701        0.0000000000
 H           1.0     4.1170126629       -2.3763060324        0.0000000000
 H           1.0     5.5554455036        1.0666253479        0.0000000000

          INTERNUCLEAR DISTANCES (ANGS.)
          ------------------------------

                1 C          2 C          3 C          4 C          5 H     

   1 C       0.0000000    1.5400000 *  2.6673582 *  4.0744570    1.1400000 *
   2 C       1.5400000 *  0.0000000    1.5400000 *  2.6673582 *  2.3295493 *
   3 C       2.6673582 *  1.5400000 *  0.0000000    1.5400000 *  2.9007585 *
   4 C       4.0744570    2.6673582 *  1.5400000 *  0.0000000    4.4335539  
   5 H       1.1400000 *  2.3295493 *  2.9007585 *  4.4335539    0.0000000  
   6 H       1.1400000 *  2.3295493 *  3.6988106    4.9923141    1.9745379 *
   7 H       2.3295493 *  1.1400000 *  2.3295493 *  2.9007585 *  3.3288436  
   8 H       2.9007585 *  2.3295493 *  1.1400000 *  2.3295493 *  2.6673582 *
   9 H       4.4335539    2.9007585 *  2.3295493 *  1.1400000 *  5.0309840  
  10 H       4.9923141    3.6988106    2.3295493 *  1.1400000 *  5.1651525  

                6 H          7 H          8 H          9 H         10 H     

   1 C       1.1400000 *  2.3295493 *  2.9007585 *  4.4335539    4.9923141  
   2 C       2.3295493 *  1.1400000 *  2.3295493 *  2.9007585 *  3.6988106  
   3 C       3.6988106    2.3295493 *  1.1400000 *  2.3295493 *  2.3295493 *
   4 C       4.9923141    2.9007585 *  2.3295493 *  1.1400000 *  1.1400000 *
   5 H       1.9745379 *  3.3288436    2.6673582 *  5.0309840    5.1651525  
   6 H       0.0000000    2.6800000 *  4.0348978    5.1651525    5.9870193  
   7 H       2.6800000 *  0.0000000    3.3288436    2.6673582 *  4.0348978  
   8 H       4.0348978    3.3288436    0.0000000    3.3288436    2.6800000 *
   9 H       5.1651525    2.6673582 *  3.3288436    0.0000000    1.9745379 *
  10 H       5.9870193    4.0348978    2.6800000 *  1.9745379 *  0.0000000  

  * ... LESS THAN  3.000


     ATOMIC BASIS SET
     ----------------
 THE CONTRACTED PRIMITIVE FUNCTIONS HAVE BEEN UNNORMALIZED
 THE CONTRACTED BASIS FUNCTIONS ARE NOW NORMALIZED TO UNITY

  SHELL TYPE  PRIMITIVE        EXPONENT          CONTRACTION COEFFICIENT(S)

 C         

      1   S       1           172.2560000    0.061766907377
      1   S       2            25.9109000    0.358794042852
      1   S       3             5.5333500    0.700713083689

      2   L       4             3.6649800   -0.395895162119    0.236459946619
      2   L       5             0.7705450    1.215834355681    0.860618805716

      3   L       6             0.1958570    1.000000000000    1.000000000000

 C         

      4   S       7           172.2560000    0.061766907377
      4   S       8            25.9109000    0.358794042852
      4   S       9             5.5333500    0.700713083689

      5   L      10             3.6649800   -0.395895162119    0.236459946619
      5   L      11             0.7705450    1.215834355681    0.860618805716

      6   L      12             0.1958570    1.000000000000    1.000000000000

 C         

      7   S      13           172.2560000    0.061766907377
      7   S      14            25.9109000    0.358794042852
      7   S      15             5.5333500    0.700713083689

      8   L      16             3.6649800   -0.395895162119    0.236459946619
      8   L      17             0.7705450    1.215834355681    0.860618805716

      9   L      18             0.1958570    1.000000000000    1.000000000000

 C         

     10   S      19           172.2560000    0.061766907377
     10   S      20            25.9109000    0.358794042852
     10   S      21             5.5333500    0.700713083689

     11   L      22             3.6649800   -0.395895162119    0.236459946619
     11   L      23             0.7705450    1.215834355681    0.860618805716

     12   L      24             0.1958570    1.000000000000    1.000000000000

 H         

     13   S      25             5.4471780    0.156284978695
     13   S      26             0.8245472    0.904690876670

     14   S      27             0.1831916    1.000000000000

 H         

     15   S      28             5.4471780    0.156284978695
     15   S      29             0.8245472    0.904690876670

     16   S      30             0.1831916    1.000000000000

 H         

     17   S      31             5.4471780    0.156284978695
     17   S      32             0.8245472    0.904690876670

     18   S      33             0.1831916    1.000000000000

 H         

     19   S      34             5.4471780    0.156284978695
     19   S      35             0.8245472    0.904690876670

     20   S      36             0.1831916    1.000000000000

 H         

     21   S      37             5.4471780    0.156284978695
     21   S      38             0.8245472    0.904690876670

     22   S      39             0.1831916    1.000000000000

 H         

     23   S      40             5.4471780    0.156284978695
     23   S      41             0.8245472    0.904690876670

     24   S      42             0.1831916    1.000000000000

 TOTAL NUMBER OF BASIS SET SHELLS             =   24
 NUMBER OF CARTESIAN GAUSSIAN BASIS FUNCTIONS =   48
 NUMBER OF ELECTRONS                          =   30
 CHARGE OF MOLECULE                           =    0
 SPIN MULTIPLICITY                            =    1
 NUMBER OF OCCUPIED ORBITALS (ALPHA)          =   15
 NUMBER OF OCCUPIED ORBITALS (BETA )          =   15
 TOTAL NUMBER OF ATOMS                        =   10
 THE NUCLEAR REPULSION ENERGY IS       94.9499408736

     $CONTRL OPTIONS
     ---------------
 SCFTYP=RHF          RUNTYP=OPTIMIZE     EXETYP=RUN     
 MPLEVL=       0     CITYP =NONE         CCTYP =NONE         VBTYP =NONE    
 DFTTYP=NONE         TDDFT =NONE    
 MULT  =       1     ICHARG=       0     NZVAR =      24     COORD =ZMT     
 PP    =NONE         RELWFN=NONE         LOCAL =NONE         NUMGRD=       F
 ISPHER=      -1     NOSYM =       0     MAXIT =      30     UNITS =ANGS    
 PLTORB=       F     MOLPLT=       T     AIMPAC=       F     FRIEND=        
 NPRINT=       7     IREST =       0     GEOM  =INPUT   
 NORMF =       0     NORMP =       0     ITOL  =      20     ICUT  =       9
 INTTYP=BEST         GRDTYP=BEST         QMTTOL= 1.0E-06

     $SYSTEM OPTIONS
     ---------------
  REPLICATED MEMORY=     1000000 WORDS (ON EVERY NODE).
 DISTRIBUTED MEMDDI=           0 MILLION WORDS IN AGGREGATE,
 MEMDDI DISTRIBUTED OVER   1 PROCESSORS IS           0 WORDS/PROCESSOR.
 TOTAL MEMORY REQUESTED ON EACH PROCESSOR=     1000000 WORDS.
 TIMLIM=      525600.00 MINUTES, OR     365.0 DAYS.
 PARALL= F  BALTYP=  DLB     KDIAG=    0  COREFL= F
 MXSEQ2=     300 MXSEQ3=     150  mem10=         0  mem22=         0

 Using Gaussians for PCM contribution to MEP, params: 0.10000E+01 0.10000E-07

          ----------------
          PROPERTIES INPUT
          ----------------

     MOMENTS            FIELD           POTENTIAL          DENSITY
 IEMOM =       1   IEFLD =       0   IEPOT =       0   IEDEN =       0
 WHERE =COMASS     WHERE =NUCLEI     WHERE =NUCLEI     WHERE =NUCLEI  
 OUTPUT=BOTH       OUTPUT=BOTH       OUTPUT=BOTH       OUTPUT=BOTH    
 IEMINT=       0   IEFINT=       0                     IEDINT=       0
                                                       MORB  =       0
          EXTRAPOLATION IN EFFECT
          SOSCF IN EFFECT
 ORBITAL PRINTING OPTION: NPREO=     1    48     2     1

     -------------------------------
     INTEGRAL TRANSFORMATION OPTIONS
     -------------------------------
     NWORD  =            0
     CUTOFF = 1.0E-09     MPTRAN =       0
     DIRTRF =       T     AOINTS =DUP     

          ----------------------
          INTEGRAL INPUT OPTIONS
          ----------------------
 NOPK  =       1 NORDER=       0 SCHWRZ=       T

   --- ENCODED Z MATRIX ---
 COORD  TYPE   I   J   K   L   M   N
    1      1    2   1
    2      1    3   2
    3      2    3   2   1
    4      1    4   3
    5      2    4   3   2
    6      3    4   3   2   1
    7      1    5   1
    8      2    5   1   2
    9      3    5   1   2   3
   10      1    6   1
   11      2    6   1   5
   12      3    6   1   5   2
   13      1    7   2
   14      2    7   2   1
   15      3    7   2   1   3
   16      1    8   3
   17      2    8   3   4
   18      3    8   3   4   2
   19      1    9   4
   20      2    9   4   3
   21      3    9   4   3   7
   22      1   10   4
   23      2   10   4   9
   24      3   10   4   9   3

 THE DETERMINANT OF THE G MATRIX IS 10**(   -14)


                     --------------------
                     INTERNAL COORDINATES
                     --------------------

                 - - ATOMS - -         COORDINATE      COORDINATE
 NO.   TYPE    I  J  K  L  M  N        (BOHR,RAD)       (ANG,DEG)
 ----------------------------------------------------------------
   1 STRETCH   2  1                     2.9101780       1.5400000
   2 STRETCH   3  2                     2.9101780       1.5400000
   3 BEND      3  2  1                  2.0943951     120.0000000
   4 STRETCH   4  3                     2.9101780       1.5400000
   5 BEND      4  3  2                  2.0943951     120.0000000
   6 TORSION   4  3  2  1               3.1415927     180.0000000
   7 STRETCH   5  1                     2.1542876       1.1400000
   8 BEND      5  1  2                  2.0943951     120.0000000
   9 TORSION   5  1  2  3               0.0000000       0.0000000
  10 STRETCH   6  1                     2.1542876       1.1400000
  11 BEND      6  1  5                  2.0943951     120.0000000
  12 TORSION   6  1  5  2               3.1415927     180.0000000
  13 STRETCH   7  2                     2.1542876       1.1400000
  14 BEND      7  2  1                  2.0943951     120.0000000
  15 TORSION   7  2  1  3               3.1415927     180.0000000
  16 STRETCH   8  3                     2.1542876       1.1400000
  17 BEND      8  3  4                  2.0943951     120.0000000
  18 TORSION   8  3  4  2               3.1415927     180.0000000
  19 STRETCH   9  4                     2.1542876       1.1400000
  20 BEND      9  4  3                  2.0943951     120.0000000
  21 TORSION   9  4  3  7               0.0000000       0.0000000
  22 STRETCH  10  4                     2.1542876       1.1400000
  23 BEND     10  4  9                  2.0943951     120.0000000
  24 TORSION  10  4  9  3               3.1415927     180.0000000

     ------------------------------------------
     THE POINT GROUP IS C1 , NAXIS= 0, ORDER= 1
     ------------------------------------------

     DIMENSIONS OF THE SYMMETRY SUBSPACES ARE
 A   =   48

 ..... DONE SETTING UP THE RUN .....
 STEP CPU TIME =     0.00 TOTAL CPU TIME =          0.0 (      0.0 MIN)
 TOTAL WALL CLOCK TIME=          0.0 SECONDS, CPU UTILIZATION IS     0.00%


          -----------------------------
          STATIONARY POINT LOCATION RUN
          -----------------------------

 OBTAINING INITIAL HESSIAN, HESS=GUESS   
 DIAGONAL GUESS HESSIAN IN INTERNAL COORDS IS
     1  0.3601     2  0.3601     3  0.2471     4  0.3601     5  0.2471
     6  0.2500     7  0.3143     8  0.2206     9  0.2500    10  0.3143
    11  0.1985    12  0.2500    13  0.3143    14  0.2206    15  0.2500
    16  0.3143    17  0.2206    18  0.2500    19  0.3143    20  0.2206
    21  0.2500    22  0.3143    23  0.1985    24  0.2500

          PARAMETERS CONTROLLING GEOMETRY SEARCH ARE
          METHOD =QA                  UPHESS =BFGS    
          NNEG   =         0          NFRZ   =         0
          NSTEP  =        20          IFOLOW =         1
          HESS   =GUESS               RESTAR =         F
          IHREP  =         0          HSSEND =         F
          NPRT   =         0          NPUN   =         0
          OPTTOL = 1.000E-04          RMIN   = 1.500E-03
          RMAX   = 1.000E-01          RLIM   = 7.000E-02
          DXMAX  = 3.000E-01          PURIFY =         F
          MOVIE  =         F          TRUPD  =         T
          TRMAX  = 5.000E-01          TRMIN  = 5.000E-02
          ITBMAT =         5          STPT   =         F
          STSTEP = 1.000E-02          PROJCT=          T

 BEGINNING GEOMETRY SEARCH POINT NSERCH=   0 ...

 COORDINATES OF ALL ATOMS ARE (ANGS)
   ATOM   CHARGE       X              Y              Z
 ------------------------------------------------------------
 C           6.0  -2.0332791254   0.1267911591   0.0000000000
 C           6.0  -0.6123095686  -0.4668800619   0.0000000000
 C           6.0   0.6123095686   0.4668800619   0.0000000000
 C           6.0   2.0332791254  -0.1267911591   0.0000000000
 H           1.0  -2.1786294360   1.2574870896   0.0000000000
 H           1.0  -2.9398153699  -0.5644338676   0.0000000000
 H           1.0  -0.4669592580  -1.5975759923   0.0000000000
 H           1.0   0.4669592580   1.5975759923   0.0000000000
 H           1.0   2.1786294360  -1.2574870896   0.0000000000
 H           1.0   2.9398153699   0.5644338676   0.0000000000


                     --------------------
                     INTERNAL COORDINATES
                     --------------------

                 - - ATOMS - -         COORDINATE      COORDINATE
 NO.   TYPE    I  J  K  L  M  N        (BOHR,RAD)       (ANG,DEG)
 ----------------------------------------------------------------
   1 STRETCH   2  1                     2.9101780       1.5400000
   2 STRETCH   3  2                     2.9101780       1.5400000
   3 BEND      3  2  1                  2.0943951     120.0000000
   4 STRETCH   4  3                     2.9101780       1.5400000
   5 BEND      4  3  2                  2.0943951     120.0000000
   6 TORSION   4  3  2  1               3.1415927     180.0000000
   7 STRETCH   5  1                     2.1542876       1.1400000
   8 BEND      5  1  2                  2.0943951     120.0000000
   9 TORSION   5  1  2  3               0.0000000       0.0000000
  10 STRETCH   6  1                     2.1542876       1.1400000
  11 BEND      6  1  5                  2.0943951     120.0000000
  12 TORSION   6  1  5  2               3.1415927     180.0000000
  13 STRETCH   7  2                     2.1542876       1.1400000
  14 BEND      7  2  1                  2.0943951     120.0000000
  15 TORSION   7  2  1  3               3.1415927     180.0000000
  16 STRETCH   8  3                     2.1542876       1.1400000
  17 BEND      8  3  4                  2.0943951     120.0000000
  18 TORSION   8  3  4  2               3.1415927     180.0000000
  19 STRETCH   9  4                     2.1542876       1.1400000
  20 BEND      9  4  3                  2.0943951     120.0000000
  21 TORSION   9  4  3  7               0.0000000       0.0000000
  22 STRETCH  10  4                     2.1542876       1.1400000
  23 BEND     10  4  9                  2.0943951     120.0000000
  24 TORSION  10  4  9  3               3.1415927     180.0000000

          ********************
          1 ELECTRON INTEGRALS
          ********************
 ...... END OF ONE-ELECTRON INTEGRALS ......
 STEP CPU TIME =     0.00 TOTAL CPU TIME =          0.0 (      0.0 MIN)
 TOTAL WALL CLOCK TIME=          0.0 SECONDS, CPU UTILIZATION IS     0.00%

          -------------
          GUESS OPTIONS
          -------------
          GUESS =HUCKEL            NORB  =       0          NORDER=       0
          MIX   =       F          PRTMO =       F          PUNMO =       F
          TOLZ  = 1.0E-08          TOLE  = 1.0E-05
          SYMDEN=       F          PURIFY=       F

 INITIAL GUESS ORBITALS GENERATED BY HUCKEL   ROUTINE.
 HUCKEL GUESS REQUIRES     26718 WORDS.

 SYMMETRIES FOR INITIAL GUESS ORBITALS FOLLOW.   BOTH SET(S).
    15 ORBITALS ARE OCCUPIED (    4 CORE ORBITALS).
     5=A        6=A        7=A        8=A        9=A       10=A       11=A   
    12=A       13=A       14=A       15=A       16=A       17=A       18=A   
    19=A       20=A       21=A       22=A       23=A       24=A       25=A   
 ...... END OF INITIAL ORBITAL SELECTION ......
 STEP CPU TIME =     0.00 TOTAL CPU TIME =          0.0 (      0.0 MIN)
 TOTAL WALL CLOCK TIME=          0.0 SECONDS, CPU UTILIZATION IS     0.00%

                    ----------------------
                    AO INTEGRAL TECHNOLOGY
                    ----------------------
     S,P,L SHELL ROTATED AXIS INTEGRALS, REPROGRAMMED BY
        KAZUYA ISHIMURA (IMS) AND JOSE SIERRA (SYNSTAR).
     S,P,D,L SHELL ROTATED AXIS INTEGRALS PROGRAMMED BY
        KAZUYA ISHIMURA (INSTITUTE FOR MOLECULAR SCIENCE).
     S,P,D,F,G SHELL TO TOTAL QUARTET ANGULAR MOMENTUM SUM 5,
        ERIC PROGRAM BY GRAHAM FLETCHER (ELORET AND NASA ADVANCED
        SUPERCOMPUTING DIVISION, AMES RESEARCH CENTER).
     S,P,D,F,G,L SHELL GENERAL RYS QUADRATURE PROGRAMMED BY
        MICHEL DUPUIS (PACIFIC NORTHWEST NATIONAL LABORATORY).

          --------------------
          2 ELECTRON INTEGRALS
          --------------------

 DIRECT SCF METHOD SKIPS INTEGRAL STORAGE ON DISK.
 DIRECT TRANSFORMATION SKIPS AO INTEGRAL STORAGE ON DISK.
  ...... END OF TWO-ELECTRON INTEGRALS .....
 STEP CPU TIME =     0.02 TOTAL CPU TIME =          0.0 (      0.0 MIN)
 TOTAL WALL CLOCK TIME=          0.0 SECONDS, CPU UTILIZATION IS    40.00%

          --------------------------
                 RHF SCF CALCULATION
          --------------------------

     NUCLEAR ENERGY =        94.9499408736
     MAXIT =   30     NPUNCH=    2
     EXTRAP=T  DAMP=F  SHIFT=F  RSTRCT=F  DIIS=F  DEM=F  SOSCF=T
     DENSITY MATRIX CONV=  2.00E-05
     SOSCF WILL OPTIMIZE     495 ORBITAL ROTATIONS, SOGTOL=   0.250
     MEMORY REQUIRED FOR RHF ITERS=     63736 WORDS.

 DIRECT SCF CALCULATION, SCHWRZ=T   FDIFF=T,  DIRTHR=  0.00E+00 NITDIR=10
 SCHWARZ INEQUALITY OVERHEAD:      1158 INTEGRALS, T=        0.01

                                                                                   NONZERO     BLOCKS
 ITER EX DEM     TOTAL ENERGY        E CHANGE  DENSITY CHANGE     ORB. GRAD      INTEGRALS    SKIPPED
   1  0  0     -153.6541167403  -153.6541167403   0.326696917   0.000000000         358179      10178
          ---------------START SECOND ORDER SCF---------------
   2  1  0     -153.9407941677    -0.2866774275   0.091122610   0.036422362         357057      11018
   3  2  0     -153.9521209550    -0.0113267872   0.052855269   0.011659022         354149      12093
   4  3  0     -153.9539796873    -0.0018587324   0.011051093   0.004837295         352331      12691
   5  4  0     -153.9541720398    -0.0001923525   0.000866458   0.000565021         345046      13986
   6  5  0     -153.9541755950    -0.0000035552   0.000650188   0.000226779         332777      16653
   7  6  0     -153.9541763356    -0.0000007406   0.000087896   0.000047212         329362      17438
   8  7  0     -153.9541763732    -0.0000000375   0.000031990   0.000020760         317939      19177
   9  8  0     -153.9541763808    -0.0000000076   0.000017221   0.000008839         311489      19893
  10  9  0     -153.9541763815    -0.0000000007   0.000005214   0.000001962         300316      21882

          -----------------
          DENSITY CONVERGED
          -----------------
     TIME TO FORM FOCK OPERATORS=       0.2 SECONDS (       0.0 SEC/ITER)
     FOCK TIME ON FIRST ITERATION=       0.0, LAST ITERATION=       0.0
     TIME TO SOLVE SCF EQUATIONS=       0.0 SECONDS (       0.0 SEC/ITER)

 FINAL RHF ENERGY IS     -153.9541763815 AFTER  10 ITERATIONS

          ------------
          EIGENVECTORS
          ------------

                      1          2          3          4          5
                  -11.2298   -11.2294   -11.2145   -11.2144    -1.0259
                     A          A          A          A          A   
    1  C  1  S    0.002700  -0.011881  -0.697945   0.697762  -0.084409
    2  C  1  S    0.001529  -0.003219  -0.067157   0.066440   0.091671
    3  C  1  X   -0.000203  -0.000458  -0.000199  -0.000170   0.048538
    4  C  1  Y    0.000193  -0.000113  -0.000078  -0.000062  -0.012965
    5  C  1  Z   -0.000000  -0.000000   0.000000  -0.000000  -0.000000
    6  C  1  S   -0.011273   0.014781   0.042292  -0.039907   0.187208
    7  C  1  X   -0.006941   0.008596   0.004529  -0.001751   0.000859
    8  C  1  Y   -0.000929  -0.001998  -0.001197   0.001373  -0.003251
    9  C  1  Z   -0.000000  -0.000000   0.000000  -0.000000  -0.000000
   10  C  2  S   -0.698302   0.697801  -0.002310   0.011454  -0.138832
   11  C  2  S   -0.069664   0.066426   0.000976  -0.000681   0.148864
   12  C  2  X   -0.000250  -0.000234  -0.000880  -0.000176   0.021038
   13  C  2  Y   -0.000744   0.000569   0.000216  -0.000176   0.040755
   14  C  2  Z   -0.000000  -0.000000   0.000000  -0.000000  -0.000000
   15  C  2  S    0.058957  -0.034784  -0.010929   0.009799   0.325807
   16  C  2  X    0.007935   0.008985   0.008062  -0.005564  -0.005407
   17  C  2  Y    0.010807  -0.003837  -0.002683   0.002656   0.022735
   18  C  2  Z   -0.000000  -0.000000   0.000000  -0.000000  -0.000000
   19  C  3  S    0.698302   0.697801   0.002310   0.011454  -0.138832
   20  C  3  S    0.069664   0.066426  -0.000976  -0.000681   0.148864
   21  C  3  X   -0.000250   0.000234  -0.000880   0.000176  -0.021038
   22  C  3  Y   -0.000744  -0.000569   0.000216   0.000176  -0.040755
   23  C  3  Z   -0.000000  -0.000000   0.000000  -0.000000  -0.000000
   24  C  3  S   -0.058957  -0.034784   0.010929   0.009799   0.325807
   25  C  3  X    0.007935  -0.008985   0.008062   0.005564   0.005407
   26  C  3  Y    0.010807   0.003837  -0.002683  -0.002656  -0.022735
   27  C  3  Z   -0.000000  -0.000000   0.000000  -0.000000  -0.000000
   28  C  4  S   -0.002700  -0.011881   0.697945   0.697762  -0.084409
   29  C  4  S   -0.001529  -0.003219   0.067157   0.066440   0.091671
   30  C  4  X   -0.000203   0.000458  -0.000199   0.000170  -0.048538
   31  C  4  Y    0.000193   0.000113  -0.000078   0.000062   0.012965
   32  C  4  Z   -0.000000  -0.000000   0.000000  -0.000000  -0.000000
   33  C  4  S    0.011273   0.014781  -0.042292  -0.039907   0.187208
   34  C  4  X   -0.006941  -0.008596   0.004529   0.001751  -0.000859
   35  C  4  Y   -0.000929   0.001998  -0.001197  -0.001373   0.003251
   36  C  4  Z   -0.000000  -0.000000   0.000000  -0.000000  -0.000000
   37  H  5  S    0.000968  -0.000762   0.000555  -0.000948   0.041502
   38  H  5  S    0.001129  -0.000406  -0.007780   0.008061   0.008687
   39  H  6  S    0.000076  -0.000595   0.000775  -0.000755   0.036902
   40  H  6  S   -0.001049   0.001343  -0.007415   0.008419   0.000875
   41  H  7  S    0.000246  -0.001732   0.000511  -0.000631   0.066095
   42  H  7  S   -0.006235   0.005977  -0.000765   0.000706   0.016091
   43  H  8  S   -0.000246  -0.001732  -0.000511  -0.000631   0.066095
   44  H  8  S    0.006235   0.005977   0.000765   0.000706   0.016091
   45  H  9  S   -0.000968  -0.000762  -0.000555  -0.000948   0.041502
   46  H  9  S   -0.001129  -0.000406   0.007780   0.008061   0.008687
   47  H 10  S   -0.000076  -0.000595  -0.000775  -0.000755   0.036902
   48  H 10  S    0.001049   0.001343   0.007415   0.008419   0.000875

                      6          7          8          9         10
                   -0.9353    -0.8128    -0.7381    -0.6018    -0.5988
                     A          A          A          A          A   
    1  C  1  S    0.133658  -0.119962  -0.051928   0.004511   0.013881
    2  C  1  S   -0.140097   0.123892   0.053849  -0.005352  -0.012680
    3  C  1  X   -0.029392  -0.070704  -0.070800  -0.038080   0.237667
    4  C  1  Y    0.016382   0.014834   0.082566  -0.210404   0.056119
    5  C  1  Z   -0.000000   0.000000   0.000000   0.000000   0.000000
    6  C  1  S   -0.353484   0.366971   0.174106  -0.013405  -0.067398
    7  C  1  X   -0.008804  -0.032929  -0.036488  -0.023573   0.169383
    8  C  1  Y    0.008489   0.009341   0.048504  -0.156282   0.049824
    9  C  1  Z   -0.000000   0.000000   0.000000   0.000000   0.000000
   10  C  2  S    0.079987   0.075259   0.100063  -0.005573  -0.035956
   11  C  2  S   -0.081258  -0.079744  -0.101740   0.004407   0.035486
   12  C  2  X    0.096499  -0.122477   0.005233  -0.117541  -0.129212
   13  C  2  Y   -0.005316  -0.008783   0.146668  -0.165687   0.133949
   14  C  2  Z   -0.000000   0.000000   0.000000   0.000000   0.000000
   15  C  2  S   -0.222283  -0.224829  -0.341017   0.028104   0.121783
   16  C  2  X    0.019102  -0.052525  -0.008086  -0.067715  -0.082941
   17  C  2  Y   -0.010530  -0.003142   0.084175  -0.126618   0.096703
   18  C  2  Z   -0.000000   0.000000   0.000000   0.000000   0.000000
   19  C  3  S   -0.079987   0.075259  -0.100063  -0.005573   0.035956
   20  C  3  S    0.081258  -0.079744   0.101740   0.004407  -0.035486
   21  C  3  X    0.096499   0.122477   0.005233   0.117541  -0.129212
   22  C  3  Y   -0.005316   0.008783   0.146668   0.165687   0.133949
   23  C  3  Z   -0.000000   0.000000   0.000000   0.000000   0.000000
   24  C  3  S    0.222283  -0.224829   0.341017   0.028104  -0.121783
   25  C  3  X    0.019102   0.052525  -0.008086   0.067715  -0.082941
   26  C  3  Y   -0.010530   0.003142   0.084175   0.126618   0.096703
   27  C  3  Z   -0.000000   0.000000   0.000000   0.000000   0.000000
   28  C  4  S   -0.133658  -0.119962   0.051928   0.004511  -0.013881
   29  C  4  S    0.140097   0.123892  -0.053849  -0.005352   0.012680
   30  C  4  X   -0.029392   0.070704  -0.070800   0.038080   0.237667
   31  C  4  Y    0.016382  -0.014834   0.082566   0.210404   0.056119
   32  C  4  Z   -0.000000   0.000000   0.000000   0.000000   0.000000
   33  C  4  S    0.353484   0.366971  -0.174106  -0.013405   0.067398
   34  C  4  X   -0.008804   0.032929  -0.036488   0.023573   0.169383
   35  C  4  Y    0.008489  -0.009341   0.048504   0.156282   0.049824
   36  C  4  Z   -0.000000   0.000000   0.000000   0.000000   0.000000
   37  H  5  S   -0.074603   0.096408   0.090594  -0.134374   0.005472
   38  H  5  S   -0.022684   0.045201   0.063020  -0.115775   0.004076
   39  H  6  S   -0.076600   0.107639   0.044821   0.096825  -0.157373
   40  H  6  S   -0.022697   0.056135   0.026448   0.087205  -0.138588
   41  H  7  S   -0.041806  -0.057429  -0.156044   0.097802  -0.062161
   42  H  7  S   -0.011390  -0.024037  -0.099118   0.078533  -0.060745
   43  H  8  S    0.041806  -0.057429   0.156044   0.097802   0.062161
   44  H  8  S    0.011390  -0.024037   0.099118   0.078533   0.060745
   45  H  9  S    0.074603   0.096408  -0.090594  -0.134374  -0.005472
   46  H  9  S    0.022684   0.045201  -0.063020  -0.115775  -0.004076
   47  H 10  S    0.076600   0.107639  -0.044821   0.096825   0.157373
   48  H 10  S    0.022697   0.056135  -0.026448   0.087205   0.138588

                     11         12         13         14         15
                   -0.5392    -0.5085    -0.4991    -0.4020    -0.2840
                     A          A          A          A          A   
    1  C  1  S    0.001979   0.016912  -0.013249   0.000000  -0.000000
    2  C  1  S   -0.003365  -0.020498   0.013001   0.000000  -0.000000
    3  C  1  X   -0.021274  -0.142978   0.210247   0.000000  -0.000000
    4  C  1  Y    0.243054   0.140381   0.065051   0.000000  -0.000000
    5  C  1  Z    0.000000   0.000000  -0.000000   0.176513  -0.256940
    6  C  1  S    0.002830  -0.020634   0.039376   0.000000  -0.000000
    7  C  1  X   -0.001404  -0.076335   0.184525   0.000000  -0.000000
    8  C  1  Y    0.218136   0.124354   0.081288   0.000000  -0.000000
    9  C  1  Z    0.000000   0.000000  -0.000000   0.216365  -0.357276
   10  C  2  S   -0.007772   0.009688   0.010042   0.000000  -0.000000
   11  C  2  S    0.009257  -0.009840  -0.011034   0.000000  -0.000000
   12  C  2  X    0.099453   0.104401  -0.249454   0.000000  -0.000000
   13  C  2  Y   -0.111075  -0.212002  -0.112943   0.000000  -0.000000
   14  C  2  Z    0.000000   0.000000  -0.000000   0.250430  -0.183839
   15  C  2  S    0.023253  -0.019706  -0.027620   0.000000  -0.000000
   16  C  2  X    0.048922   0.115933  -0.183949   0.000000  -0.000000
   17  C  2  Y   -0.118768  -0.226138  -0.108625   0.000000  -0.000000
   18  C  2  Z    0.000000   0.000000  -0.000000   0.289967  -0.258338
   19  C  3  S    0.007772   0.009688   0.010042   0.000000  -0.000000
   20  C  3  S   -0.009257  -0.009840  -0.011034   0.000000  -0.000000
   21  C  3  X    0.099453  -0.104401   0.249454   0.000000  -0.000000
   22  C  3  Y   -0.111075   0.212002   0.112943   0.000000  -0.000000
   23  C  3  Z    0.000000   0.000000  -0.000000   0.250430   0.183839
   24  C  3  S   -0.023253  -0.019706  -0.027620   0.000000  -0.000000
   25  C  3  X    0.048922  -0.115933   0.183949   0.000000  -0.000000
   26  C  3  Y   -0.118768   0.226138   0.108625   0.000000  -0.000000
   27  C  3  Z    0.000000   0.000000  -0.000000   0.289967   0.258338
   28  C  4  S   -0.001979   0.016912  -0.013249   0.000000  -0.000000
   29  C  4  S    0.003365  -0.020498   0.013001   0.000000  -0.000000
   30  C  4  X   -0.021274   0.142978  -0.210247   0.000000  -0.000000
   31  C  4  Y    0.243054  -0.140381  -0.065051   0.000000  -0.000000
   32  C  4  Z    0.000000   0.000000  -0.000000   0.176513   0.256940
   33  C  4  S   -0.002830  -0.020634   0.039376   0.000000  -0.000000
   34  C  4  X   -0.001404   0.076335  -0.184525   0.000000  -0.000000
   35  C  4  Y    0.218136  -0.124354  -0.081288   0.000000  -0.000000
   36  C  4  Z    0.000000   0.000000  -0.000000   0.216365   0.357276
   37  H  5  S    0.170738   0.105721   0.046100   0.000000  -0.000000
   38  H  5  S    0.155272   0.117478   0.038427   0.000000  -0.000000
   39  H  6  S   -0.096339   0.001551  -0.145528   0.000000  -0.000000
   40  H  6  S   -0.082597   0.018021  -0.143980   0.000000  -0.000000
   41  H  7  S    0.092695   0.163280   0.053117   0.000000  -0.000000
   42  H  7  S    0.071622   0.151647   0.051638   0.000000  -0.000000
   43  H  8  S   -0.092695   0.163280   0.053117   0.000000  -0.000000
   44  H  8  S   -0.071622   0.151647   0.051638   0.000000  -0.000000
   45  H  9  S   -0.170738   0.105721   0.046100   0.000000  -0.000000
   46  H  9  S   -0.155272   0.117478   0.038427   0.000000  -0.000000
   47  H 10  S    0.096339   0.001551  -0.145528   0.000000  -0.000000
   48  H 10  S    0.082597   0.018021  -0.143980   0.000000  -0.000000

                     16         17         18         19         20
                    0.0807     0.2134     0.2675     0.2746     0.2780
                     A          A          A          A          A   
    1  C  1  S   -0.000000   0.000000   0.094249   0.072728   0.062160
    2  C  1  S   -0.000000   0.000000  -0.045750  -0.031640  -0.027678
    3  C  1  X   -0.000000   0.000000   0.017633   0.056811   0.140574
    4  C  1  Y   -0.000000   0.000000  -0.085901   0.072362  -0.027434
    5  C  1  Z    0.261963  -0.172824   0.000000   0.000000   0.000000
    6  C  1  S   -0.000000   0.000000  -1.048222  -0.864916  -0.761986
    7  C  1  X   -0.000000   0.000000   0.161411   0.220556   0.581163
    8  C  1  Y   -0.000000   0.000000  -0.255477   0.283306  -0.157281
    9  C  1  Z    0.489809  -0.427729   0.000000   0.000000   0.000000
   10  C  2  S   -0.000000   0.000000  -0.051932   0.037647   0.048930
   11  C  2  S   -0.000000   0.000000   0.041165  -0.006379  -0.013394
   12  C  2  X   -0.000000   0.000000  -0.019050  -0.061745  -0.017100
   13  C  2  Y   -0.000000   0.000000  -0.076056   0.122181   0.112292
   14  C  2  Z   -0.189977   0.290046   0.000000   0.000000   0.000000
   15  C  2  S   -0.000000   0.000000   0.394319  -0.546105  -0.730990
   16  C  2  X   -0.000000   0.000000  -0.196893  -0.351867   0.077960
   17  C  2  Y   -0.000000   0.000000  -0.356047   0.343563   0.367576
   18  C  2  Z   -0.333087   0.655361   0.000000   0.000000   0.000000
   19  C  3  S   -0.000000   0.000000   0.051932  -0.037647   0.048930
   20  C  3  S   -0.000000   0.000000  -0.041165   0.006379  -0.013394
   21  C  3  X   -0.000000   0.000000  -0.019050  -0.061745   0.017100
   22  C  3  Y   -0.000000   0.000000  -0.076056   0.122181  -0.112292
   23  C  3  Z   -0.189977  -0.290046   0.000000   0.000000   0.000000
   24  C  3  S   -0.000000   0.000000  -0.394319   0.546105  -0.730990
   25  C  3  X   -0.000000   0.000000  -0.196893  -0.351867  -0.077960
   26  C  3  Y   -0.000000   0.000000  -0.356047   0.343563  -0.367576
   27  C  3  Z   -0.333087  -0.655361   0.000000   0.000000   0.000000
   28  C  4  S   -0.000000   0.000000  -0.094249  -0.072728   0.062160
   29  C  4  S   -0.000000   0.000000   0.045750   0.031640  -0.027678
   30  C  4  X   -0.000000   0.000000   0.017633   0.056811  -0.140574
   31  C  4  Y   -0.000000   0.000000  -0.085901   0.072362   0.027434
   32  C  4  Z    0.261963   0.172824   0.000000   0.000000   0.000000
   33  C  4  S   -0.000000   0.000000   1.048222   0.864916  -0.761986
   34  C  4  X   -0.000000   0.000000   0.161411   0.220556  -0.581163
   35  C  4  Y   -0.000000   0.000000  -0.255477   0.283306   0.157281
   36  C  4  Z    0.489809   0.427729   0.000000   0.000000   0.000000
   37  H  5  S   -0.000000   0.000000   0.038638   0.010095   0.003027
   38  H  5  S   -0.000000   0.000000   0.906270   0.094369   0.558977
   39  H  6  S   -0.000000   0.000000   0.024726   0.039375   0.047879
   40  H  6  S   -0.000000   0.000000   0.433509   0.847538   0.834926
   41  H  7  S   -0.000000   0.000000  -0.030751   0.068231  -0.013998
   42  H  7  S   -0.000000   0.000000  -0.666035   0.835081   0.689783
   43  H  8  S   -0.000000   0.000000   0.030751  -0.068231  -0.013998
   44  H  8  S   -0.000000   0.000000   0.666035  -0.835081   0.689783
   45  H  9  S   -0.000000   0.000000  -0.038638  -0.010095   0.003027
   46  H  9  S   -0.000000   0.000000  -0.906270  -0.094369   0.558977
   47  H 10  S   -0.000000   0.000000  -0.024726  -0.039375   0.047879
   48  H 10  S   -0.000000   0.000000  -0.433509  -0.847538   0.834926

                     21         22         23         24         25
                    0.3158     0.3307     0.3684     0.4432     0.4991
                     A          A          A          A          A   
    1  C  1  S   -0.087189  -0.018995   0.033495   0.060909  -0.063342
    2  C  1  S    0.037328   0.016521  -0.016905  -0.036077  -0.016985
    3  C  1  X    0.017308  -0.015254   0.083127  -0.233633   0.049626
    4  C  1  Y    0.091346  -0.155358   0.203096  -0.015877  -0.087085
    5  C  1  Z    0.000000   0.000000   0.000000  -0.000000  -0.000000
    6  C  1  S    0.989268   0.098678  -0.340004  -0.628840   1.197068
    7  C  1  X    0.178744  -0.116034   0.320014  -1.216173   1.271704
    8  C  1  Y    0.374129  -0.697520   0.936688   0.078922  -0.455778
    9  C  1  Z    0.000000   0.000000   0.000000  -0.000000  -0.000000
   10  C  2  S    0.069421   0.111042  -0.040396  -0.095898   0.049100
   11  C  2  S   -0.031152  -0.058669   0.004119   0.030258  -0.009804
   12  C  2  X    0.063638  -0.111009  -0.069370  -0.127778   0.161882
   13  C  2  Y    0.073644  -0.033826  -0.095460   0.131898  -0.185979
   14  C  2  Z    0.000000   0.000000   0.000000  -0.000000  -0.000000
   15  C  2  S   -0.815086  -1.199011   0.667852   1.250196  -0.804392
   16  C  2  X    0.211388  -0.390506  -0.121068  -0.538681   1.361944
   17  C  2  Y    0.257742  -0.053279  -0.525368   0.628788  -1.171494
   18  C  2  Z    0.000000   0.000000   0.000000  -0.000000  -0.000000
   19  C  3  S    0.069421  -0.111042  -0.040396   0.095898   0.049100
   20  C  3  S   -0.031152   0.058669   0.004119  -0.030258  -0.009804
   21  C  3  X   -0.063638  -0.111009   0.069370  -0.127778  -0.161882
   22  C  3  Y   -0.073644  -0.033826   0.095460   0.131898   0.185979
   23  C  3  Z    0.000000   0.000000   0.000000  -0.000000  -0.000000
   24  C  3  S   -0.815086   1.199011   0.667852  -1.250196  -0.804392
   25  C  3  X   -0.211388  -0.390506   0.121068  -0.538681  -1.361944
   26  C  3  Y   -0.257742  -0.053279   0.525368   0.628788   1.171494
   27  C  3  Z    0.000000   0.000000   0.000000  -0.000000  -0.000000
   28  C  4  S   -0.087189   0.018995   0.033495  -0.060909  -0.063342
   29  C  4  S    0.037328  -0.016521  -0.016905   0.036077  -0.016985
   30  C  4  X   -0.017308  -0.015254  -0.083127  -0.233633  -0.049626
   31  C  4  Y   -0.091346  -0.155358  -0.203096  -0.015877   0.087085
   32  C  4  Z    0.000000   0.000000   0.000000  -0.000000  -0.000000
   33  C  4  S    0.989268  -0.098678  -0.340004   0.628840   1.197068
   34  C  4  X   -0.178744  -0.116034  -0.320014  -1.216173  -1.271704
   35  C  4  Y   -0.374129  -0.697520  -0.936688   0.078922   0.455778
   36  C  4  Z    0.000000   0.000000   0.000000  -0.000000  -0.000000
   37  H  5  S   -0.071971   0.036170   0.020778  -0.051753   0.013417
   38  H  5  S   -0.972674   0.722321  -0.770299   0.061647   0.192595
   39  H  6  S    0.006840  -0.044383   0.004563   0.008967   0.057748
   40  H  6  S   -0.050859  -0.714854   1.093756  -0.667403   0.149945
   41  H  7  S    0.056726   0.015198   0.019347   0.005666   0.028481
   42  H  7  S    0.728016   0.559469  -0.717254   0.208806  -0.954903
   43  H  8  S    0.056726  -0.015198   0.019347  -0.005666   0.028481
   44  H  8  S    0.728016  -0.559469  -0.717254  -0.208806  -0.954903
   45  H  9  S   -0.071971  -0.036170   0.020778   0.051753   0.013417
   46  H  9  S   -0.972674  -0.722321  -0.770299  -0.061647   0.192595
   47  H 10  S    0.006840   0.044383   0.004563  -0.008967   0.057748
   48  H 10  S   -0.050859   0.714854   1.093756   0.667403   0.149945

                     26         27         28         29         30
                    0.5306     0.8993     0.9276     0.9613     0.9807
                     A          A          A          A          A   
    1  C  1  S   -0.002233   0.014920   0.024322  -0.009641   0.021919
    2  C  1  S    0.004672  -0.005562  -0.072637   0.038435  -0.022142
    3  C  1  X    0.056167   0.272326  -0.286170   0.520546  -0.496836
    4  C  1  Y   -0.150708   0.197898  -0.207700  -0.260240   0.378582
    5  C  1  Z    0.000000   0.000000   0.000000  -0.000000  -0.000000
    6  C  1  S    0.155102   0.061654   0.318294   0.012195   0.134685
    7  C  1  X    0.112808  -0.425101   0.399387  -0.785922   0.780668
    8  C  1  Y   -0.912815  -0.324027   0.350297   0.321934  -0.583490
    9  C  1  Z    0.000000   0.000000   0.000000  -0.000000  -0.000000
   10  C  2  S   -0.058137  -0.022450  -0.015462   0.029803  -0.016677
   11  C  2  S    0.008093  -0.020117  -0.006926  -0.106472   0.003015
   12  C  2  X    0.189929  -0.248289  -0.561540  -0.336613  -0.049224
   13  C  2  Y    0.210030   0.306840  -0.119922  -0.184466   0.166244
   14  C  2  Z    0.000000   0.000000   0.000000  -0.000000  -0.000000
   15  C  2  S    0.941000   0.333220  -0.239136   0.828107  -0.344295
   16  C  2  X    1.565475   0.294903   0.631669   0.409210   0.266407
   17  C  2  Y    1.225383  -0.215737  -0.052598   0.462644  -0.372956
   18  C  2  Z    0.000000   0.000000   0.000000  -0.000000  -0.000000
   19  C  3  S    0.058137   0.022450  -0.015462  -0.029803  -0.016677
   20  C  3  S   -0.008093   0.020117  -0.006926   0.106472   0.003015
   21  C  3  X    0.189929  -0.248289   0.561540  -0.336613   0.049224
   22  C  3  Y    0.210030   0.306840   0.119922  -0.184466  -0.166244
   23  C  3  Z    0.000000   0.000000   0.000000  -0.000000  -0.000000
   24  C  3  S   -0.941000  -0.333220  -0.239136  -0.828107  -0.344295
   25  C  3  X    1.565475   0.294903  -0.631669   0.409210  -0.266407
   26  C  3  Y    1.225383  -0.215737   0.052598   0.462644   0.372956
   27  C  3  Z    0.000000   0.000000   0.000000  -0.000000  -0.000000
   28  C  4  S    0.002233  -0.014920   0.024322   0.009641   0.021919
   29  C  4  S   -0.004672   0.005562  -0.072637  -0.038435  -0.022142
   30  C  4  X    0.056167   0.272326   0.286170   0.520546   0.496836
   31  C  4  Y   -0.150708   0.197898   0.207700  -0.260240  -0.378582
   32  C  4  Z    0.000000   0.000000   0.000000  -0.000000  -0.000000
   33  C  4  S   -0.155102  -0.061654   0.318294  -0.012195   0.134685
   34  C  4  X    0.112808  -0.425101  -0.399387  -0.785922  -0.780668
   35  C  4  Y   -0.912815  -0.324027  -0.350297   0.321934   0.583490
   36  C  4  Z    0.000000   0.000000   0.000000  -0.000000  -0.000000
   37  H  5  S   -0.020079   0.239164  -0.187972  -0.263931   0.381149
   38  H  5  S    0.853831  -0.017486  -0.038561   0.024244  -0.012108
   39  H  6  S    0.081931  -0.234287   0.333290  -0.078160   0.123716
   40  H  6  S   -0.384874  -0.025337  -0.056402  -0.102324   0.015232
   41  H  7  S   -0.017682  -0.450486   0.026578   0.207410  -0.231864
   42  H  7  S    0.645846   0.145072  -0.094958  -0.050099   0.012533
   43  H  8  S    0.017682   0.450486   0.026578  -0.207410  -0.231864
   44  H  8  S   -0.645846  -0.145072  -0.094958   0.050099   0.012533
   45  H  9  S    0.020079  -0.239164  -0.187972   0.263931   0.381149
   46  H  9  S   -0.853831   0.017486  -0.038561  -0.024244  -0.012108
   47  H 10  S   -0.081931   0.234287   0.333290   0.078160   0.123716
   48  H 10  S    0.384874   0.025337  -0.056402   0.102324   0.015232

                     31         32         33         34         35
                    0.9855     1.0158     1.0328     1.0781     1.0901
                     A          A          A          A          A   
    1  C  1  S   -0.000000  -0.000000   0.028890  -0.000000   0.000000
    2  C  1  S   -0.000000  -0.000000   0.118542  -0.000000   0.000000
    3  C  1  X   -0.000000  -0.000000  -0.134164  -0.000000   0.000000
    4  C  1  Y   -0.000000  -0.000000   0.049977  -0.000000   0.000000
    5  C  1  Z    0.516799  -0.773665   0.000000  -0.583133   0.090023
    6  C  1  S   -0.000000  -0.000000   0.123495  -0.000000   0.000000
    7  C  1  X   -0.000000  -0.000000   0.466316  -0.000000   0.000000
    8  C  1  Y   -0.000000  -0.000000  -0.262241  -0.000000   0.000000
    9  C  1  Z   -0.379310   0.705110   0.000000   0.658754  -0.296883
   10  C  2  S   -0.000000  -0.000000   0.000957  -0.000000   0.000000
   11  C  2  S   -0.000000  -0.000000   0.067498  -0.000000   0.000000
   12  C  2  X   -0.000000  -0.000000  -0.536753  -0.000000   0.000000
   13  C  2  Y   -0.000000  -0.000000  -0.081963  -0.000000   0.000000
   14  C  2  Z    0.576087  -0.086289   0.000000   0.525225  -0.778154
   15  C  2  S   -0.000000  -0.000000   0.098106  -0.000000   0.000000
   16  C  2  X   -0.000000  -0.000000   0.898925  -0.000000   0.000000
   17  C  2  Y   -0.000000  -0.000000   0.285044  -0.000000   0.000000
   18  C  2  Z   -0.372490  -0.064689   0.000000  -0.534130   1.050243
   19  C  3  S   -0.000000  -0.000000  -0.000957  -0.000000   0.000000
   20  C  3  S   -0.000000  -0.000000  -0.067498  -0.000000   0.000000
   21  C  3  X   -0.000000  -0.000000  -0.536753  -0.000000   0.000000
   22  C  3  Y   -0.000000  -0.000000  -0.081963  -0.000000   0.000000
   23  C  3  Z    0.576087   0.086289   0.000000   0.525225   0.778154
   24  C  3  S   -0.000000  -0.000000  -0.098106  -0.000000   0.000000
   25  C  3  X   -0.000000  -0.000000   0.898925  -0.000000   0.000000
   26  C  3  Y   -0.000000  -0.000000   0.285044  -0.000000   0.000000
   27  C  3  Z   -0.372490   0.064689   0.000000  -0.534130  -1.050243
   28  C  4  S   -0.000000  -0.000000  -0.028890  -0.000000   0.000000
   29  C  4  S   -0.000000  -0.000000  -0.118542  -0.000000   0.000000
   30  C  4  X   -0.000000  -0.000000  -0.134164  -0.000000   0.000000
   31  C  4  Y   -0.000000  -0.000000   0.049977  -0.000000   0.000000
   32  C  4  Z    0.516799   0.773665   0.000000  -0.583133  -0.090023
   33  C  4  S   -0.000000  -0.000000  -0.123495  -0.000000   0.000000
   34  C  4  X   -0.000000  -0.000000   0.466316  -0.000000   0.000000
   35  C  4  Y   -0.000000  -0.000000  -0.262241  -0.000000   0.000000
   36  C  4  Z   -0.379310  -0.705110   0.000000   0.658754   0.296883
   37  H  5  S   -0.000000  -0.000000   0.377328  -0.000000   0.000000
   38  H  5  S   -0.000000  -0.000000  -0.072934  -0.000000   0.000000
   39  H  6  S   -0.000000  -0.000000   0.487521  -0.000000   0.000000
   40  H  6  S   -0.000000  -0.000000  -0.200020  -0.000000   0.000000
   41  H  7  S   -0.000000  -0.000000   0.125511  -0.000000   0.000000
   42  H  7  S   -0.000000  -0.000000  -0.015786  -0.000000   0.000000
   43  H  8  S   -0.000000  -0.000000  -0.125511  -0.000000   0.000000
   44  H  8  S   -0.000000  -0.000000   0.015786  -0.000000   0.000000
   45  H  9  S   -0.000000  -0.000000  -0.377328  -0.000000   0.000000
   46  H  9  S   -0.000000  -0.000000   0.072934  -0.000000   0.000000
   47  H 10  S   -0.000000  -0.000000  -0.487521  -0.000000   0.000000
   48  H 10  S   -0.000000  -0.000000   0.200020  -0.000000   0.000000

                     36         37         38         39         40
                    1.1047     1.2437     1.2624     1.3130     1.3141
                     A          A          A          A          A   
    1  C  1  S    0.022976  -0.015792   0.006030  -0.030603  -0.017377
    2  C  1  S    0.169142  -0.073075   0.036980   0.127793   0.006204
    3  C  1  X    0.206731  -0.322904  -0.064127  -0.300412  -0.014415
    4  C  1  Y   -0.127027  -0.331552  -0.607619   0.233599   0.532852
    5  C  1  Z   -0.000000   0.000000  -0.000000  -0.000000   0.000000
    6  C  1  S   -0.097774   0.375373   0.002286   0.085092   0.142726
    7  C  1  X   -0.083781   0.679578   0.170703   0.652066   0.186829
    8  C  1  Y    0.084716   0.516769   1.121905  -0.466368  -0.838621
    9  C  1  Z   -0.000000   0.000000  -0.000000  -0.000000   0.000000
   10  C  2  S    0.005348   0.021277   0.012972   0.018104   0.012379
   11  C  2  S    0.234200  -0.124774   0.035373  -0.079417   0.050097
   12  C  2  X   -0.014294  -0.094511   0.080111  -0.299268  -0.072052
   13  C  2  Y    0.286295   0.463160   0.327672   0.386840   0.253329
   14  C  2  Z   -0.000000   0.000000  -0.000000  -0.000000   0.000000
   15  C  2  S   -0.041447   0.203107  -0.334616   0.024188  -0.185482
   16  C  2  X   -0.007542   0.459631  -0.640858   0.772453   0.397729
   17  C  2  Y   -0.171346  -1.108982  -0.927996  -0.364434  -0.375146
   18  C  2  Z   -0.000000   0.000000  -0.000000  -0.000000   0.000000
   19  C  3  S    0.005348   0.021277  -0.012972  -0.018104   0.012379
   20  C  3  S    0.234200  -0.124774  -0.035373   0.079417   0.050097
   21  C  3  X    0.014294   0.094511   0.080111  -0.299268   0.072052
   22  C  3  Y   -0.286295  -0.463160   0.327672   0.386840  -0.253329
   23  C  3  Z   -0.000000   0.000000  -0.000000  -0.000000   0.000000
   24  C  3  S   -0.041447   0.203107   0.334616  -0.024188  -0.185482
   25  C  3  X    0.007542  -0.459631  -0.640858   0.772453  -0.397729
   26  C  3  Y    0.171346   1.108982  -0.927996  -0.364434   0.375146
   27  C  3  Z   -0.000000   0.000000  -0.000000  -0.000000   0.000000
   28  C  4  S    0.022976  -0.015792  -0.006030   0.030603  -0.017377
   29  C  4  S    0.169142  -0.073075  -0.036980  -0.127793   0.006204
   30  C  4  X   -0.206731   0.322904  -0.064127  -0.300412   0.014415
   31  C  4  Y    0.127027   0.331552  -0.607619   0.233599  -0.532852
   32  C  4  Z   -0.000000   0.000000  -0.000000  -0.000000   0.000000
   33  C  4  S   -0.097774   0.375373  -0.002286  -0.085092   0.142726
   34  C  4  X    0.083781  -0.679578   0.170703   0.652066  -0.186829
   35  C  4  Y   -0.084716  -0.516769   1.121905  -0.466368   0.838621
   36  C  4  Z   -0.000000   0.000000  -0.000000  -0.000000   0.000000
   37  H  5  S    0.454266   0.021610   0.497392  -0.323606  -0.583506
   38  H  5  S   -0.292537  -0.293557  -1.023927   0.572133   0.979164
   39  H  6  S    0.440650  -0.553604  -0.228601  -0.355412   0.105379
   40  H  6  S   -0.285263   0.842190   0.636280   0.432020  -0.327331
   41  H  7  S    0.484309   0.290205   0.233821   0.480233   0.440100
   42  H  7  S   -0.351928  -0.894969  -0.609269  -0.672916  -0.622633
   43  H  8  S    0.484309   0.290205  -0.233821  -0.480233   0.440100
   44  H  8  S   -0.351928  -0.894969   0.609269   0.672916  -0.622633
   45  H  9  S    0.454266   0.021610  -0.497392   0.323606  -0.583506
   46  H  9  S   -0.292537  -0.293557   1.023927  -0.572133   0.979164
   47  H 10  S    0.440650  -0.553604   0.228601   0.355412   0.105379
   48  H 10  S   -0.285263   0.842190  -0.636280  -0.432020  -0.327331

                     41         42         43         44         45
                    1.3423     1.5200     1.5551     1.5649     1.7238
                     A          A          A          A          A   
    1  C  1  S   -0.018683   0.007558   0.000675   0.026608  -0.026437
    2  C  1  S    0.010059  -0.436737  -0.044941  -0.405163   0.727636
    3  C  1  X   -0.407579   0.427607   0.117080  -0.133273   0.104990
    4  C  1  Y   -0.268326   0.141825   0.298383  -0.219940  -0.131617
    5  C  1  Z   -0.000000   0.000000   0.000000   0.000000   0.000000
    6  C  1  S    0.125532   1.511690   0.007042  -0.018439  -0.425443
    7  C  1  X    0.748514  -0.321448  -0.624026   0.142921   0.409448
    8  C  1  Y    0.180825  -0.509489  -1.476314   1.172536   0.634235
    9  C  1  Z   -0.000000   0.000000   0.000000   0.000000   0.000000
   10  C  2  S   -0.018347   0.024912  -0.016564   0.007698  -0.020988
   11  C  2  S    0.062973  -0.558599   0.231345  -0.513974   0.230611
   12  C  2  X   -0.294445  -0.404490   0.056670   0.460291  -0.061193
   13  C  2  Y   -0.361225   0.276804  -0.400746   0.231784   0.454083
   14  C  2  Z   -0.000000   0.000000   0.000000   0.000000   0.000000
   15  C  2  S    0.017151   0.387124   0.492706   1.285542   0.336894
   16  C  2  X    0.971235   1.278814   0.787063  -0.987346   0.509166
   17  C  2  Y    0.604492  -1.171348   1.760587  -0.646576  -1.705716
   18  C  2  Z   -0.000000   0.000000   0.000000   0.000000   0.000000
   19  C  3  S    0.018347   0.024912   0.016564   0.007698  -0.020988
   20  C  3  S   -0.062973  -0.558599  -0.231345  -0.513974   0.230611
   21  C  3  X   -0.294445   0.404490   0.056670  -0.460291   0.061193
   22  C  3  Y   -0.361225  -0.276804  -0.400746  -0.231784  -0.454083
   23  C  3  Z   -0.000000   0.000000   0.000000   0.000000   0.000000
   24  C  3  S   -0.017151   0.387124  -0.492706   1.285542   0.336894
   25  C  3  X    0.971235  -1.278814   0.787063   0.987346  -0.509166
   26  C  3  Y    0.604492   1.171348   1.760587   0.646576   1.705716
   27  C  3  Z   -0.000000   0.000000   0.000000   0.000000   0.000000
   28  C  4  S    0.018683   0.007558  -0.000675   0.026608  -0.026437
   29  C  4  S   -0.010059  -0.436737   0.044941  -0.405163   0.727636
   30  C  4  X   -0.407579  -0.427607   0.117080   0.133273  -0.104990
   31  C  4  Y   -0.268326  -0.141825   0.298383   0.219940   0.131617
   32  C  4  Z   -0.000000   0.000000   0.000000   0.000000   0.000000
   33  C  4  S   -0.125532   1.511690  -0.007042  -0.018439  -0.425443
   34  C  4  X    0.748514   0.321448  -0.624026  -0.142921  -0.409448
   35  C  4  Y    0.180825   0.509489  -1.476314  -1.172536  -0.634235
   36  C  4  Z   -0.000000   0.000000   0.000000   0.000000   0.000000
   37  H  5  S   -0.094078   0.157185   0.480741  -0.251000  -0.256829
   38  H  5  S    0.044327  -0.181596   0.338810  -0.422643   0.055381
   39  H  6  S   -0.435958  -0.010092  -0.478641   0.479368   0.152427
   40  H  6  S    0.766599  -0.608173  -0.345632  -0.012166   0.411816
   41  H  7  S   -0.442460  -0.234828   0.368692  -0.103771  -0.550835
   42  H  7  S    0.694252  -0.628718   0.525687  -0.466315  -0.541959
   43  H  8  S    0.442460  -0.234828  -0.368692  -0.103771  -0.550835
   44  H  8  S   -0.694252  -0.628718  -0.525687  -0.466315  -0.541959
   45  H  9  S    0.094078   0.157185  -0.480741  -0.251000  -0.256829
   46  H  9  S   -0.044327  -0.181596  -0.338810  -0.422643   0.055381
   47  H 10  S    0.435958  -0.010092   0.478641   0.479368   0.152427
   48  H 10  S   -0.766599  -0.608173   0.345632  -0.012166   0.411816

                     46         47         48
                    1.7522     1.8831     2.0612
                     A          A          A   
    1  C  1  S   -0.020717  -0.012923   0.022086
    2  C  1  S    1.169832  -0.897490   0.616167
    3  C  1  X    0.078089   0.071511  -0.036431
    4  C  1  Y   -0.014356  -0.049531   0.070328
    5  C  1  Z    0.000000   0.000000   0.000000
    6  C  1  S   -1.843803   2.335985  -1.697610
    7  C  1  X   -0.204414   0.615941  -0.717675
    8  C  1  Y    0.219550  -0.023581  -0.309938
    9  C  1  Z    0.000000   0.000000   0.000000
   10  C  2  S   -0.011686  -0.004825  -0.041637
   11  C  2  S    0.536840   0.988173  -1.327660
   12  C  2  X    0.090644   0.002283   0.076412
   13  C  2  Y    0.015756   0.203046  -0.141390
   14  C  2  Z    0.000000   0.000000   0.000000
   15  C  2  S   -0.787041  -1.657897   3.598181
   16  C  2  X   -0.925970   0.993681   0.379375
   17  C  2  Y   -0.248843  -0.981765   1.201308
   18  C  2  Z    0.000000   0.000000   0.000000
   19  C  3  S    0.011686  -0.004825   0.041637
   20  C  3  S   -0.536840   0.988173   1.327660
   21  C  3  X    0.090644  -0.002283   0.076412
   22  C  3  Y    0.015756  -0.203046  -0.141390
   23  C  3  Z    0.000000   0.000000   0.000000
   24  C  3  S    0.787041  -1.657897  -3.598181
   25  C  3  X   -0.925970  -0.993681   0.379375
   26  C  3  Y   -0.248843   0.981765   1.201308
   27  C  3  Z    0.000000   0.000000   0.000000
   28  C  4  S    0.020717  -0.012923  -0.022086
   29  C  4  S   -1.169832  -0.897490  -0.616167
   30  C  4  X    0.078089  -0.071511  -0.036431
   31  C  4  Y   -0.014356   0.049531   0.070328
   32  C  4  Z    0.000000   0.000000   0.000000
   33  C  4  S    1.843803   2.335985   1.697610
   34  C  4  X   -0.204414  -0.615941  -0.717675
   35  C  4  Y    0.219550   0.023581  -0.309938
   36  C  4  Z    0.000000   0.000000   0.000000
   37  H  5  S   -0.054627  -0.103012   0.214022
   38  H  5  S    0.332526  -0.373929   0.294594
   39  H  6  S    0.033217  -0.033343  -0.059274
   40  H  6  S    0.364309  -0.203359   0.021476
   41  H  7  S   -0.072226  -0.197902  -0.058502
   42  H  7  S    0.187712  -0.051453  -0.077627
   43  H  8  S    0.072226  -0.197902   0.058502
   44  H  8  S   -0.187712  -0.051453   0.077627
   45  H  9  S    0.054627  -0.103012  -0.214022
   46  H  9  S   -0.332526  -0.373929  -0.294594
   47  H 10  S   -0.033217  -0.033343   0.059274
   48  H 10  S   -0.364309  -0.203359  -0.021476
 ...... END OF RHF CALCULATION ......
 STEP CPU TIME =     0.22 TOTAL CPU TIME =          0.2 (      0.0 MIN)
 TOTAL WALL CLOCK TIME=          0.3 SECONDS, CPU UTILIZATION IS    88.89%

     ----------------------------------------------------------------
     PROPERTY VALUES FOR THE RHF   SELF-CONSISTENT FIELD WAVEFUNCTION
     ----------------------------------------------------------------

          -----------------
          ENERGY COMPONENTS
          -----------------

         WAVEFUNCTION NORMALIZATION =       1.0000000000

                ONE ELECTRON ENERGY =    -394.1405375463
                TWO ELECTRON ENERGY =     145.2364202913
           NUCLEAR REPULSION ENERGY =      94.9499408736
                                      ------------------
                       TOTAL ENERGY =    -153.9541763815

 ELECTRON-ELECTRON POTENTIAL ENERGY =     145.2364202913
  NUCLEUS-ELECTRON POTENTIAL ENERGY =    -546.1207143651
   NUCLEUS-NUCLEUS POTENTIAL ENERGY =      94.9499408736
                                      ------------------
             TOTAL POTENTIAL ENERGY =    -305.9343532002
               TOTAL KINETIC ENERGY =     151.9801768187
                 VIRIAL RATIO (V/T) =       2.0129885331

  ...... PI ENERGY ANALYSIS ......

 ENERGY ANALYSIS:
            FOCK ENERGY=   -103.6676818292
          BARE H ENERGY=   -394.1405375463
     ELECTRONIC ENERGY =   -248.9041096878
         KINETIC ENERGY=    151.9801768187
          N-N REPULSION=     94.9499408736
           TOTAL ENERGY=   -153.9541688142
        SIGMA PART(1+2)=   -230.1695518130
               (K,V1,2)=    148.2249839878   -506.2685379609    127.8740021602
           PI PART(1+2)=    -18.7345578748
               (K,V1,2)=      3.7551928309    -39.8521764041     17.3624256984
  SIGMA SKELETON, ERROR=   -135.2196109394      0.0000000000
             MIXED PART= 0.00000E+00 0.00000E+00 0.00000E+00 0.00000E+00
 ...... END OF PI ENERGY ANALYSIS ......

          ---------------------------------------
          MULLIKEN AND LOWDIN POPULATION ANALYSES
          ---------------------------------------

     ATOMIC MULLIKEN POPULATION IN EACH MOLECULAR ORBITAL

                      1          2          3          4          5

                  2.000000   2.000000   2.000000   2.000000   2.000000

    1             0.001551   0.002649   0.995947   0.996002   0.256594
    2             0.997700   0.996550   0.002089   0.001872   0.679527
    3             0.997700   0.996550   0.002089   0.001872   0.679527
    4             0.001551   0.002649   0.995947   0.996002   0.256594
    5            -0.000009  -0.000004   0.001006   0.001032   0.015285
    6             0.000010   0.000011   0.000951   0.001085   0.008914
    7             0.000748   0.000794   0.000007   0.000010   0.039680
    8             0.000748   0.000794   0.000007   0.000010   0.039680
    9            -0.000009  -0.000004   0.001006   0.001032   0.015285
   10             0.000010   0.000011   0.000951   0.001085   0.008914

                      6          7          8          9         10

                  2.000000   2.000000   2.000000   2.000000   2.000000

    1             0.606241   0.498713   0.184644   0.362941   0.453352
    2             0.274552   0.275120   0.480342   0.297664   0.273202
    3             0.274552   0.275120   0.480342   0.297664   0.273202
    4             0.606241   0.498713   0.184644   0.362941   0.453352
    5             0.050561   0.085845   0.084441   0.165559   0.000252
    6             0.053615   0.112448   0.018461   0.089192   0.233645
    7             0.015031   0.027873   0.232112   0.084645   0.039550
    8             0.015031   0.027873   0.232112   0.084645   0.039550
    9             0.050561   0.085845   0.084441   0.165559   0.000252
   10             0.053615   0.112448   0.018461   0.089192   0.233645

                     11         12         13         14         15

                  2.000000   2.000000   2.000000   2.000000   2.000000

    1             0.448391   0.251918   0.337902   0.336168   0.682934
    2             0.149316   0.399994   0.431830   0.663832   0.317066
    3             0.149316   0.399994   0.431830   0.663832   0.317066
    4             0.448391   0.251918   0.337902   0.336168   0.682934
    5             0.255748   0.112315   0.016861   0.000000   0.000000
    6             0.079293   0.000605   0.187482   0.000000   0.000000
    7             0.067252   0.235168   0.025925   0.000000   0.000000
    8             0.067252   0.235168   0.025925   0.000000   0.000000
    9             0.255748   0.112315   0.016861   0.000000   0.000000
   10             0.079293   0.000605   0.187482   0.000000   0.000000

               ----- POPULATIONS IN EACH AO -----
                             MULLIKEN      LOWDIN
              1  C  1  S      1.98669     1.97691
              2  C  1  S      0.37459     0.42487
              3  C  1  X      0.52521     0.49459
              4  C  1  Y      0.53187     0.49596
              5  C  1  Z      0.36964     0.37092
              6  C  1  S      1.02559     0.65434
              7  C  1  X      0.41370     0.55875
              8  C  1  Y      0.53919     0.59176
              9  C  1  Z      0.64946     0.65113
             10  C  2  S      1.98726     1.97668
             11  C  2  S      0.37511     0.41842
             12  C  2  X      0.52865     0.50019
             13  C  2  Y      0.53455     0.50415
             14  C  2  Z      0.36726     0.36025
             15  C  2  S      0.99116     0.62222
             16  C  2  X      0.32873     0.52886
             17  C  2  Y      0.51430     0.57721
             18  C  2  Z      0.61363     0.61769
             19  C  3  S      1.98726     1.97668
             20  C  3  S      0.37511     0.41842
             21  C  3  X      0.52865     0.50019
             22  C  3  Y      0.53455     0.50415
             23  C  3  Z      0.36726     0.36025
             24  C  3  S      0.99116     0.62222
             25  C  3  X      0.32873     0.52886
             26  C  3  Y      0.51430     0.57721
             27  C  3  Z      0.61363     0.61769
             28  C  4  S      1.98669     1.97691
             29  C  4  S      0.37459     0.42487
             30  C  4  X      0.52521     0.49459
             31  C  4  Y      0.53187     0.49596
             32  C  4  Z      0.36964     0.37092
             33  C  4  S      1.02559     0.65434
             34  C  4  X      0.41370     0.55875
             35  C  4  Y      0.53919     0.59176
             36  C  4  Z      0.64946     0.65113
             37  H  5  S      0.44157     0.43476
             38  H  5  S      0.34732     0.45994
             39  H  6  S      0.44163     0.43477
             40  H  6  S      0.34408     0.45773
             41  H  7  S      0.44194     0.43869
             42  H  7  S      0.32685     0.44920
             43  H  8  S      0.44194     0.43869
             44  H  8  S      0.32685     0.44920
             45  H  9  S      0.44157     0.43476
             46  H  9  S      0.34732     0.45994
             47  H 10  S      0.44163     0.43477
             48  H 10  S      0.34408     0.45773

          ----- MULLIKEN ATOMIC OVERLAP POPULATIONS -----
          (OFF-DIAGONAL ELEMENTS NEED TO BE MULTIPLIED BY 2)

             1           2           3           4           5

    1    5.2425721
    2    0.5091445   5.1990581
    3   -0.0625142   0.3142565   5.1990581
    4    0.0008392  -0.0625142   0.5091445   5.2425721
    5    0.3768399  -0.0384756   0.0015077   0.0000106   0.4664369
    6    0.3728879  -0.0343679   0.0011411  -0.0000171  -0.0193810
    7   -0.0251137   0.3827724  -0.0318663   0.0012963   0.0008575
    8    0.0012963  -0.0318663   0.3827724  -0.0251137   0.0010937
    9    0.0000106   0.0015077  -0.0384756   0.3768399   0.0000011
   10   -0.0000171   0.0011411  -0.0343679   0.3728879   0.0000001

             6           7           8           9          10

    6    0.4653685
    7    0.0000743   0.4388575
    8    0.0000070   0.0008153   0.4388575
    9    0.0000001   0.0010937   0.0008575   0.4664369
   10    0.0000001   0.0000070   0.0000743  -0.0193810   0.4653685

          TOTAL MULLIKEN AND LOWDIN ATOMIC POPULATIONS
       ATOM         MULL.POP.    CHARGE          LOW.POP.     CHARGE
    1 C             6.415946   -0.415946         6.219237   -0.219237
    2 C             6.240656   -0.240656         6.105674   -0.105674
    3 C             6.240656   -0.240656         6.105674   -0.105674
    4 C             6.415946   -0.415946         6.219237   -0.219237
    5 H             0.788891    0.211109         0.894701    0.105299
    6 H             0.785713    0.214287         0.892500    0.107500
    7 H             0.768794    0.231206         0.887888    0.112112
    8 H             0.768794    0.231206         0.887888    0.112112
    9 H             0.788891    0.211109         0.894701    0.105299
   10 H             0.785713    0.214287         0.892500    0.107500

          -------------------------------
          BOND ORDER AND VALENCE ANALYSIS     BOND ORDER THRESHOLD=0.050
          -------------------------------

                   BOND                       BOND                       BOND
  ATOM PAIR DIST  ORDER      ATOM PAIR DIST  ORDER      ATOM PAIR DIST  ORDER
    1   2  1.540  1.811        1   4  4.074  0.120        1   5  1.140  0.929
    1   6  1.140  0.927        2   3  1.540  1.025        2   7  1.140  0.927
    3   4  1.540  1.811        3   8  1.140  0.927        4   9  1.140  0.929
    4  10  1.140  0.927

                       TOTAL       BONDED        FREE
      ATOM            VALENCE     VALENCE     VALENCE
    1 C                 3.768       3.768      -0.000
    2 C                 3.733       3.733       0.000
    3 C                 3.733       3.733       0.000
    4 C                 3.768       3.768      -0.000
    5 H                 0.931       0.931      -0.000
    6 H                 0.929       0.929      -0.000
    7 H                 0.925       0.925       0.000
    8 H                 0.925       0.925       0.000
    9 H                 0.931       0.931      -0.000
   10 H                 0.929       0.929      -0.000

          ---------------------
          ELECTROSTATIC MOMENTS
          ---------------------

 POINT   1           X           Y           Z (BOHR)    CHARGE
                -0.000000    0.000000    0.000000       -0.00 (A.U.)
         DX          DY          DZ         /D/  (DEBYE)
     0.000000   -0.000000    0.000000    0.000000
 ...... END OF PROPERTY EVALUATION ......
 STEP CPU TIME =     0.01 TOTAL CPU TIME =          0.2 (      0.0 MIN)
 TOTAL WALL CLOCK TIME=          0.3 SECONDS, CPU UTILIZATION IS    89.29%

 BEGINNING ONE ELECTRON GRADIENT...
 ..... END OF 1-ELECTRON GRADIENT ......
 STEP CPU TIME =     0.00 TOTAL CPU TIME =          0.2 (      0.0 MIN)
 TOTAL WALL CLOCK TIME=          0.3 SECONDS, CPU UTILIZATION IS    89.29%

          ----------------------
          GRADIENT OF THE ENERGY
          ----------------------
 THE COARSE/FINE SCHWARZ SCREENINGS SKIPPED        11157/        5576 BLOCKS.
 THE NUMBER OF GRADIENT INTEGRAL BLOCKS COMPUTED WAS     28297
 ...... END OF 2-ELECTRON GRADIENT ......
 STEP CPU TIME =     0.04 TOTAL CPU TIME =          0.3 (      0.0 MIN)
 TOTAL WALL CLOCK TIME=          0.3 SECONDS, CPU UTILIZATION IS    90.63%

          NSERCH=  0     ENERGY=    -153.9541764

                                 -----------------------
                                 GRADIENT (HARTREE/BOHR)
                                 -----------------------
        ATOM     ZNUC       DE/DX         DE/DY         DE/DZ
 --------------------------------------------------------------
    1  C            6.0    -0.1079504     0.0487970     0.0000000
    2  C            6.0     0.1022041    -0.0599122     0.0000000
    3  C            6.0    -0.1022041     0.0599122     0.0000000
    4  C            6.0     0.1079504    -0.0487970     0.0000000
    5  H            1.0    -0.0059421     0.0435845     0.0000000
    6  H            1.0    -0.0352586    -0.0271117     0.0000000
    7  H            1.0     0.0050912    -0.0442766     0.0000000
    8  H            1.0    -0.0050912     0.0442766     0.0000000
    9  H            1.0     0.0059421    -0.0435845     0.0000000
   10  H            1.0     0.0352586     0.0271117     0.0000000


                     --------------------
                     INTERNAL COORDINATES
                     --------------------

                 - - ATOMS - -         COORDINATE        GRADIENT
 NO.   TYPE    I  J  K  L  M  N         (ANG,DEG)     (H/B,H/RAD)
 ----------------------------------------------------------------
   1 STRETCH   2  1                     1.5400000       0.1627843
   2 STRETCH   3  2                     1.5400000       0.0568822
   3 BEND      3  2  1                120.0000000      -0.0081048
   4 STRETCH   4  3                     1.5400000       0.1627843
   5 BEND      4  3  2                120.0000000      -0.0081048
   6 TORSION   4  3  2  1             180.0000000       0.0000000
   7 STRETCH   5  1                     1.1400000       0.0439864
   8 BEND      5  1  2                120.0000000       0.0011146
   9 TORSION   5  1  2  3               0.0000000       0.0000000
  10 STRETCH   6  1                     1.1400000       0.0444767
  11 BEND      6  1  5                120.0000000       0.0003896
  12 TORSION   6  1  5  2             180.0000000       0.0000000
  13 STRETCH   7  2                     1.1400000       0.0445644
  14 BEND      7  2  1                120.0000000      -0.0012833
  15 TORSION   7  2  1  3             180.0000000       0.0000000
  16 STRETCH   8  3                     1.1400000       0.0445644
  17 BEND      8  3  4                120.0000000      -0.0012833
  18 TORSION   8  3  4  2             180.0000000       0.0000000
  19 STRETCH   9  4                     1.1400000       0.0439864
  20 BEND      9  4  3                120.0000000       0.0011146
  21 TORSION   9  4  3  7               0.0000000       0.0000000
  22 STRETCH  10  4                     1.1400000       0.0444767
  23 BEND     10  4  9                120.0000000       0.0003896
  24 TORSION  10  4  9  3             180.0000000       0.0000000

 NOTE: CARTESIAN GRADIENTS ARE ALWAYS TAKEN TO TEST CONVERGENCE,
       SO THE FOLLOWING GRADIENTS ARE CARTESIAN.

          MAXIMUM GRADIENT = 0.1079504    RMS GRADIENT = 0.0475879

 NSERCH:   0  E=     -153.9541763815  GRAD. MAX=  0.1079504  R.M.S.=  0.0475879

          FORCE CONSTANT MATRIX NOT UPDATED --- TAKING FIRST STEP
          MIN SEARCH, CORRECT HESSIAN, TRYING PURE NR STEP
               NR STEP HAS LENGTH         =   0.745236
          TRIM/QA LAMBDA FOR NON-TS MODES =  -0.51895049
          TRIM/QA STEP HAS LENGTH         =   0.300000
          RADIUS OF STEP TAKEN=   0.30000  CURRENT TRUST RADIUS=   0.30000
          TRANSFORMING DISPLACEMENT FROM INTERNALS TO CARTESIANS
          THE ROOT MEAN SQUARE ERROR IN ITERATION   1 IS   0.00032917
          THE ROOT MEAN SQUARE ERROR IN ITERATION   2 IS   0.00000005
          THE ROOT MEAN SQUARE ERROR IN ITERATION   3 IS   0.00000000

 BEGINNING GEOMETRY SEARCH POINT NSERCH=   1 ...

 COORDINATES OF ALL ATOMS ARE (ANGS)
   ATOM   CHARGE       X              Y              Z
 ------------------------------------------------------------
 C           6.0  -1.9335375295   0.1145843961   0.0000000000
 C           6.0  -0.6055397994  -0.4473791306   0.0000000000
 C           6.0   0.6055397994   0.4473791306   0.0000000000
 C           6.0   1.9335375295  -0.1145843961   0.0000000000
 H           1.0  -2.0686251505   1.2184138603   0.0000000000
 H           1.0  -2.8220523211  -0.5536499227   0.0000000000
 H           1.0  -0.4669195251  -1.5504005660   0.0000000000
 H           1.0   0.4669195251   1.5504005660   0.0000000000
 H           1.0   2.0686251505  -1.2184138603   0.0000000000
 H           1.0   2.8220523211   0.5536499227   0.0000000000


                     --------------------
                     INTERNAL COORDINATES
                     --------------------

                 - - ATOMS - -         COORDINATE      COORDINATE
 NO.   TYPE    I  J  K  L  M  N        (BOHR,RAD)       (ANG,DEG)
 ----------------------------------------------------------------
   1 STRETCH   2  1                     2.7249960       1.4420059
   2 STRETCH   3  2                     2.8454694       1.5057577
   3 BEND      3  2  1                  2.1049752     120.6061933
   4 STRETCH   4  3                     2.7249960       1.4420059
   5 BEND      4  3  2                  2.1049752     120.6061933
   6 TORSION   4  3  2  1               3.1415927     180.0000000
   7 STRETCH   5  1                     2.1014978       1.1120648
   8 BEND      5  1  2                  2.0928879     119.9136438
   9 TORSION   5  1  2  3               0.0000000       0.0000000
  10 STRETCH   6  1                     2.1009093       1.1117534
  11 BEND      6  1  5                  2.0938520     119.9688852
  12 TORSION   6  1  5  2               3.1415927     180.0000000
  13 STRETCH   7  2                     2.1008041       1.1116977
  14 BEND      7  2  1                  2.0961304     120.0994240
  15 TORSION   7  2  1  3               3.1415927     180.0000000
  16 STRETCH   8  3                     2.1008041       1.1116977
  17 BEND      8  3  4                  2.0961304     120.0994240
  18 TORSION   8  3  4  2               3.1415927     180.0000000
  19 STRETCH   9  4                     2.1014978       1.1120648
  20 BEND      9  4  3                  2.0928879     119.9136438
  21 TORSION   9  4  3  7               0.0000000       0.0000000
  22 STRETCH  10  4                     2.1009093       1.1117534
  23 BEND     10  4  9                  2.0938520     119.9688852
  24 TORSION  10  4  9  3               3.1415927     180.0000000

          INTERNUCLEAR DISTANCES (ANGS.)
          ------------------------------

                1 C          2 C          3 C          4 C          5 H     

   1 C       0.0000000    1.4420059 *  2.5607940 *  3.8738596    1.1120648 *
   2 C       1.4420059 *  0.0000000    1.5057577 *  2.5607940 *  2.2170893 *
   3 C       2.5607940 *  1.5057577 *  0.0000000    1.4420059 *  2.7831013 *
   4 C       3.8738596    2.5607940 *  1.4420059 *  0.0000000    4.2183161  
   5 H       1.1120648 *  2.2170893 *  2.7831013 *  4.2183161    0.0000000  
   6 H       1.1117534 *  2.2190586 *  3.5707768    4.7758155    1.9255811 *
   7 H       2.2188157 *  1.1116977 *  2.2674419 *  2.7970989 *  3.1987176  
   8 H       2.7970989 *  2.2674419 *  1.1116977 *  2.2188157 *  2.5571863 *
   9 H       4.2183161    2.7831013 *  2.2170893 *  1.1120648 *  4.8015591  
  10 H       4.7758155    3.5707768    2.2190586 *  1.1117534 *  4.9356496  

                6 H          7 H          8 H          9 H         10 H     

   1 C       1.1117534 *  2.2188157 *  2.7970989 *  4.2183161    4.7758155  
   2 C       2.2190586 *  1.1116977 *  2.2674419 *  2.7831013 *  3.5707768  
   3 C       3.5707768    2.2674419 *  1.1116977 *  2.2170893 *  2.2190586 *
   4 C       4.7758155    2.7970989 *  2.2188157 *  1.1120648 *  1.1117534 *
   5 H       1.9255811 *  3.1987176    2.5571863 *  4.8015591    4.9356496  
   6 H       0.0000000    2.5573741 *  3.9044032    4.9356496    5.7516980  
   7 H       2.5573741 *  0.0000000    3.2383673    2.5571863 *  3.9044032  
   8 H       3.9044032    3.2383673    0.0000000    3.1987176    2.5573741 *
   9 H       4.9356496    2.5571863 *  3.1987176    0.0000000    1.9255811 *
  10 H       5.7516980    3.9044032    2.5573741 *  1.9255811 *  0.0000000  

  * ... LESS THAN  3.000

 ...... END OF ONE-ELECTRON INTEGRALS ......
 STEP CPU TIME =     0.00 TOTAL CPU TIME =          0.3 (      0.0 MIN)
 TOTAL WALL CLOCK TIME=          0.3 SECONDS, CPU UTILIZATION IS    90.63%
  ...... END OF TWO-ELECTRON INTEGRALS .....
 STEP CPU TIME =     0.00 TOTAL CPU TIME =          0.3 (      0.0 MIN)
 TOTAL WALL CLOCK TIME=          0.3 SECONDS, CPU UTILIZATION IS    87.88%

          --------------------------
                 RHF SCF CALCULATION
          --------------------------
     DENSITY MATRIX CONV=  4.00E-04

 DIRECT SCF CALCULATION, SCHWRZ=T   FDIFF=T,  DIRTHR=  0.00E+00 NITDIR=10

                                                                                   NONZERO     BLOCKS
 ITER EX DEM     TOTAL ENERGY        E CHANGE  DENSITY CHANGE     ORB. GRAD      INTEGRALS    SKIPPED
          ---------------START SECOND ORDER SCF---------------
   1  0  0     -154.0153226253  -154.0153226253   0.019921781   0.019279762         366996       8972
   2  1  0     -154.0209290618    -0.0056064365   0.006332787   0.004425260         361465      11209
   3  2  0     -154.0213349132    -0.0004058514   0.001885496   0.001054997         357089      12390
   4  3  0     -154.0213439773    -0.0000090642   0.000546793   0.000648092         350978      13522
   5  4  0     -154.0213486733    -0.0000046959   0.000085416   0.000056110         340681      15256
   6  5  0     -154.0213487134    -0.0000000401   0.000036909   0.000014782         328024      17427
   7  6  0     -154.0213487172    -0.0000000039   0.000007788   0.000002037         320966      18736

          -----------------
          DENSITY CONVERGED
          -----------------
     TIME TO FORM FOCK OPERATORS=       0.2 SECONDS (       0.0 SEC/ITER)
     FOCK TIME ON FIRST ITERATION=       0.0, LAST ITERATION=       0.0
     TIME TO SOLVE SCF EQUATIONS=       0.0 SECONDS (       0.0 SEC/ITER)

 FINAL RHF ENERGY IS     -154.0213487172 AFTER   7 ITERATIONS
 ...... END OF RHF CALCULATION ......
 STEP CPU TIME =     0.19 TOTAL CPU TIME =          0.5 (      0.0 MIN)
 TOTAL WALL CLOCK TIME=          0.5 SECONDS, CPU UTILIZATION IS    94.12%
 ..... END OF 1-ELECTRON GRADIENT ......
 STEP CPU TIME =     0.01 TOTAL CPU TIME =          0.5 (      0.0 MIN)
 TOTAL WALL CLOCK TIME=          0.5 SECONDS, CPU UTILIZATION IS    94.23%
 ...... END OF 2-ELECTRON GRADIENT ......
 STEP CPU TIME =     0.05 TOTAL CPU TIME =          0.5 (      0.0 MIN)
 TOTAL WALL CLOCK TIME=          0.6 SECONDS, CPU UTILIZATION IS    94.74%

          NSERCH=  1     ENERGY=    -154.0213487

                                 -----------------------
                                 GRADIENT (HARTREE/BOHR)
                                 -----------------------
        ATOM     ZNUC       DE/DX         DE/DY         DE/DZ
 --------------------------------------------------------------
    1  C            6.0    -0.0820348     0.0394128     0.0000000
    2  C            6.0     0.0813127    -0.0472683     0.0000000
    3  C            6.0    -0.0813127     0.0472683     0.0000000
    4  C            6.0     0.0820348    -0.0394128     0.0000000
    5  H            1.0    -0.0012579     0.0277487     0.0000000
    6  H            1.0    -0.0210775    -0.0188859     0.0000000
    7  H            1.0     0.0020536    -0.0275503     0.0000000
    8  H            1.0    -0.0020536     0.0275503     0.0000000
    9  H            1.0     0.0012579    -0.0277487     0.0000000
   10  H            1.0     0.0210775     0.0188859     0.0000000


                     --------------------
                     INTERNAL COORDINATES
                     --------------------

                 - - ATOMS - -         COORDINATE        GRADIENT
 NO.   TYPE    I  J  K  L  M  N         (ANG,DEG)     (H/B,H/RAD)
 ----------------------------------------------------------------
   1 STRETCH   2  1                     1.4420059       0.1149319
   2 STRETCH   3  2                     1.5057577       0.0326658
   3 BEND      3  2  1                120.6061933      -0.0126159
   4 STRETCH   4  3                     1.4420059       0.1149319
   5 BEND      4  3  2                120.6061933      -0.0126159
   6 TORSION   4  3  2  1             180.0000000       0.0000000
   7 STRETCH   5  1                     1.1120648       0.0276960
   8 BEND      5  1  2                119.9136438       0.0006343
   9 TORSION   5  1  2  3               0.0000000       0.0000000
  10 STRETCH   6  1                     1.1117534       0.0281968
  11 BEND      6  1  5                119.9688852       0.0050941
  12 TORSION   6  1  5  2             180.0000000       0.0000000
  13 STRETCH   7  2                     1.1116977       0.0275914
  14 BEND      7  2  1                120.0994240      -0.0029364
  15 TORSION   7  2  1  3             180.0000000       0.0000000
  16 STRETCH   8  3                     1.1116977       0.0275914
  17 BEND      8  3  4                120.0994240      -0.0029364
  18 TORSION   8  3  4  2             180.0000000       0.0000000
  19 STRETCH   9  4                     1.1120648       0.0276960
  20 BEND      9  4  3                119.9136438       0.0006343
  21 TORSION   9  4  3  7               0.0000000       0.0000000
  22 STRETCH  10  4                     1.1117534       0.0281968
  23 BEND     10  4  9                119.9688852       0.0050941
  24 TORSION  10  4  9  3             180.0000000       0.0000000

 NOTE: CARTESIAN GRADIENTS ARE ALWAYS TAKEN TO TEST CONVERGENCE,
       SO THE FOLLOWING GRADIENTS ARE CARTESIAN.

          MAXIMUM GRADIENT = 0.0820348    RMS GRADIENT = 0.0360230

 NSERCH:   1  E=     -154.0213487172  GRAD. MAX=  0.0820348  R.M.S.=  0.0360230

          HESSIAN UPDATED USING THE BFGS FORMULA
             ACTUAL ENERGY CHANGE WAS  -0.0671723358
          PREDICTED ENERGY CHANGE WAS  -0.0625073464 RATIO=  1.075
          MIN SEARCH, CORRECT HESSIAN, TRYING PURE NR STEP
               NR STEP HAS LENGTH         =   0.726207
          TRIM/QA LAMBDA FOR NON-TS MODES =  -0.10820002
          TRIM/QA STEP HAS LENGTH         =   0.500000
          RADIUS OF STEP TAKEN=   0.50000  CURRENT TRUST RADIUS=   0.50000
          TRANSFORMING DISPLACEMENT FROM INTERNALS TO CARTESIANS
          THE ROOT MEAN SQUARE ERROR IN ITERATION   1 IS   0.00524848
          THE ROOT MEAN SQUARE ERROR IN ITERATION   2 IS   0.00000411
          THE ROOT MEAN SQUARE ERROR IN ITERATION   3 IS   0.00000000

 BEGINNING GEOMETRY SEARCH POINT NSERCH=   2 ...

 COORDINATES OF ALL ATOMS ARE (ANGS)
   ATOM   CHARGE       X              Y              Z
 ------------------------------------------------------------
 C           6.0  -1.7920228865   0.0871985297   0.0000000000
 C           6.0  -0.6155511679  -0.4002759445  -0.0000000000
 C           6.0   0.6155511679   0.4002759445   0.0000000000
 C           6.0   1.7920228865  -0.0871985298  -0.0000000000
 H           1.0  -1.9292455373   1.1536554925   0.0000000000
 H           1.0  -2.6722585437  -0.5280039303  -0.0000000000
 H           1.0  -0.4535353405  -1.4639050106  -0.0000000000
 H           1.0   0.4535353405   1.4639050106   0.0000000000
 H           1.0   1.9292455372  -1.1536554925   0.0000000000
 H           1.0   2.6722585437   0.5280039302  -0.0000000000


                     --------------------
                     INTERNAL COORDINATES
                     --------------------

                 - - ATOMS - -         COORDINATE      COORDINATE
 NO.   TYPE    I  J  K  L  M  N        (BOHR,RAD)       (ANG,DEG)
 ----------------------------------------------------------------
   1 STRETCH   2  1                     2.4065028       1.2734666
   2 STRETCH   3  2                     2.7750652       1.4685014
   3 BEND      3  2  1                  2.1722079     124.4583472
   4 STRETCH   4  3                     2.4065028       1.2734666
   5 BEND      4  3  2                  2.1722079     124.4583472
   6 TORSION   4  3  2  1               3.1415927     180.0000000
   7 STRETCH   5  1                     2.0319261       1.0752490
   8 BEND      5  1  2                  2.0915827     119.8388630
   9 TORSION   5  1  2  3               0.0000000       0.0000000
  10 STRETCH   6  1                     2.0294011       1.0739129
  11 BEND      6  1  5                  2.0528197     117.6179025
  12 TORSION   6  1  5  2               3.1415927     180.0000000
  13 STRETCH   7  2                     2.0331519       1.0758977
  14 BEND      7  2  1                  2.1147760     121.1677391
  15 TORSION   7  2  1  3               3.1415927     180.0000000
  16 STRETCH   8  3                     2.0331519       1.0758977
  17 BEND      8  3  4                  2.1147760     121.1677391
  18 TORSION   8  3  4  2               3.1415927     180.0000000
  19 STRETCH   9  4                     2.0319261       1.0752490
  20 BEND      9  4  3                  2.0915827     119.8388630
  21 TORSION   9  4  3  7               0.0000000       0.0000000
  22 STRETCH  10  4                     2.0294011       1.0739129
  23 BEND     10  4  9                  2.0528197     117.6179025
  24 TORSION  10  4  9  3               3.1415927     180.0000000

          INTERNUCLEAR DISTANCES (ANGS.)
          ------------------------------

                1 C          2 C          3 C          4 C          5 H     

   1 C       0.0000000    1.2734666 *  2.4278448 *  3.5882863    1.0752490 *
   2 C       1.2734666 *  0.0000000    1.4685014 *  2.4278448 *  2.0348208 *
   3 C       2.4278448 *  1.4685014 *  0.0000000    1.2734666 *  2.6539727 *
   4 C       3.5882863    2.4278448 *  1.2734666 *  0.0000000    3.9226977  
   5 H       1.0752490 *  2.0348208 *  2.6539727 *  3.9226977    0.0000000  
   6 H       1.0739129 *  2.0606697 *  3.4163425    4.4859913    1.8384903 *
   7 H       2.0487731 *  1.0758977 *  2.1489804 *  2.6339804 *  3.0048866  
   8 H       2.6339804 *  2.1489804 *  1.0758977 *  2.0487731 *  2.4028940 *
   9 H       3.9226977    2.6539727 *  2.0348208 *  1.0752490 *  4.4957355  
  10 H       4.4859913    3.4163425    2.0606697 *  1.0739129 *  4.6438432  

                6 H          7 H          8 H          9 H         10 H     

   1 C       1.0739129 *  2.0487731 *  2.6339804 *  3.9226977    4.4859913  
   2 C       2.0606697 *  1.0758977 *  2.1489804 *  2.6539727 *  3.4163425  
   3 C       3.4163425    2.1489804 *  1.0758977 *  2.0348208 *  2.0606697 *
   4 C       4.4859913    2.6339804 *  2.0487731 *  1.0752490 *  1.0739129 *
   5 H       1.8384903 *  3.0048866    2.4028940 *  4.4957355    4.6438432  
   6 H       0.0000000    2.4080373 *  3.7065197    4.6438432    5.4478450  
   7 H       2.4080373 *  0.0000000    3.0651018    2.4028940 *  3.7065197  
   8 H       3.7065197    3.0651018    0.0000000    3.0048866    2.4080373 *
   9 H       4.6438432    2.4028940 *  3.0048866    0.0000000    1.8384903 *
  10 H       5.4478450    3.7065197    2.4080373 *  1.8384903 *  0.0000000  

  * ... LESS THAN  3.000

 ...... END OF ONE-ELECTRON INTEGRALS ......
 STEP CPU TIME =     0.00 TOTAL CPU TIME =          0.5 (      0.0 MIN)
 TOTAL WALL CLOCK TIME=          0.6 SECONDS, CPU UTILIZATION IS    94.74%
  ...... END OF TWO-ELECTRON INTEGRALS .....
 STEP CPU TIME =     0.00 TOTAL CPU TIME =          0.5 (      0.0 MIN)
 TOTAL WALL CLOCK TIME=          0.6 SECONDS, CPU UTILIZATION IS    94.74%

          --------------------------
                 RHF SCF CALCULATION
          --------------------------
     DENSITY MATRIX CONV=  4.00E-04

 DIRECT SCF CALCULATION, SCHWRZ=T   FDIFF=T,  DIRTHR=  0.00E+00 NITDIR=10

                                                                                   NONZERO     BLOCKS
 ITER EX DEM     TOTAL ENERGY        E CHANGE  DENSITY CHANGE     ORB. GRAD      INTEGRALS    SKIPPED
          ---------------START SECOND ORDER SCF---------------
   1  0  0     -154.0309041913  -154.0309041913   0.035546237   0.040578790         378686       7428
   2  1  0     -154.0513558715    -0.0204516802   0.015094745   0.010274771         375205       8901
   3  2  0     -154.0528629107    -0.0015070392   0.003266107   0.002091004         372367       9661
   4  3  0     -154.0528972527    -0.0000343420   0.000940602   0.001049973         366956      10995
   5  4  0     -154.0529074471    -0.0000101944   0.000409329   0.000190134         361149      12327
   6  5  0     -154.0529076578    -0.0000002107   0.000088032   0.000018159         352690      13419
   7  6  0     -154.0529076654    -0.0000000076   0.000017057   0.000003077         339123      15694

          -----------------
          DENSITY CONVERGED
          -----------------
     TIME TO FORM FOCK OPERATORS=       0.2 SECONDS (       0.0 SEC/ITER)
     FOCK TIME ON FIRST ITERATION=       0.0, LAST ITERATION=       0.0
     TIME TO SOLVE SCF EQUATIONS=       0.0 SECONDS (       0.0 SEC/ITER)

 FINAL RHF ENERGY IS     -154.0529076654 AFTER   7 ITERATIONS
 ...... END OF RHF CALCULATION ......
 STEP CPU TIME =     0.16 TOTAL CPU TIME =          0.7 (      0.0 MIN)
 TOTAL WALL CLOCK TIME=          0.7 SECONDS, CPU UTILIZATION IS    94.59%
 ..... END OF 1-ELECTRON GRADIENT ......
 STEP CPU TIME =     0.01 TOTAL CPU TIME =          0.7 (      0.0 MIN)
 TOTAL WALL CLOCK TIME=          0.8 SECONDS, CPU UTILIZATION IS    94.67%
 ...... END OF 2-ELECTRON GRADIENT ......
 STEP CPU TIME =     0.04 TOTAL CPU TIME =          0.8 (      0.0 MIN)
 TOTAL WALL CLOCK TIME=          0.8 SECONDS, CPU UTILIZATION IS    94.94%

          NSERCH=  2     ENERGY=    -154.0529077

                                 -----------------------
                                 GRADIENT (HARTREE/BOHR)
                                 -----------------------
        ATOM     ZNUC       DE/DX         DE/DY         DE/DZ
 --------------------------------------------------------------
    1  C            6.0     0.0598591    -0.0275935     0.0000000
    2  C            6.0    -0.0642832     0.0324164     0.0000000
    3  C            6.0     0.0642832    -0.0324164     0.0000000
    4  C            6.0    -0.0598591     0.0275935     0.0000000
    5  H            1.0     0.0056810     0.0002733     0.0000000
    6  H            1.0     0.0000501    -0.0024193     0.0000000
    7  H            1.0     0.0018631     0.0015028     0.0000000
    8  H            1.0    -0.0018631    -0.0015028     0.0000000
    9  H            1.0    -0.0056810    -0.0002733     0.0000000
   10  H            1.0    -0.0000501     0.0024193     0.0000000


                     --------------------
                     INTERNAL COORDINATES
                     --------------------

                 - - ATOMS - -         COORDINATE        GRADIENT
 NO.   TYPE    I  J  K  L  M  N         (ANG,DEG)     (H/B,H/RAD)
 ----------------------------------------------------------------
   1 STRETCH   2  1                     1.2734666      -0.0719786
   2 STRETCH   3  2                     1.4685014      -0.0049360
   3 BEND      3  2  1                124.4583472       0.0024638
   4 STRETCH   4  3                     1.2734666      -0.0719786
   5 BEND      4  3  2                124.4583472       0.0024638
   6 TORSION   4  3  2  1             180.0000000      -0.0000000
   7 STRETCH   5  1                     1.0752490      -0.0004540
   8 BEND      5  1  2                119.8388630      -0.0074373
   9 TORSION   5  1  2  3               0.0000000       0.0000000
  10 STRETCH   6  1                     1.0739129       0.0013448
  11 BEND      6  1  5                117.6179025       0.0040826
  12 TORSION   6  1  5  2             180.0000000      -0.0000000
  13 STRETCH   7  2                     1.0758977      -0.0012051
  14 BEND      7  2  1                121.1677391       0.0042048
  15 TORSION   7  2  1  3             180.0000000       0.0000000
  16 STRETCH   8  3                     1.0758977      -0.0012051
  17 BEND      8  3  4                121.1677391       0.0042048
  18 TORSION   8  3  4  2             180.0000000       0.0000000
  19 STRETCH   9  4                     1.0752490      -0.0004540
  20 BEND      9  4  3                119.8388630      -0.0074373
  21 TORSION   9  4  3  7               0.0000000       0.0000000
  22 STRETCH  10  4                     1.0739129       0.0013448
  23 BEND     10  4  9                117.6179025       0.0040826
  24 TORSION  10  4  9  3             180.0000000      -0.0000000

 NOTE: CARTESIAN GRADIENTS ARE ALWAYS TAKEN TO TEST CONVERGENCE,
       SO THE FOLLOWING GRADIENTS ARE CARTESIAN.

          MAXIMUM GRADIENT = 0.0642832    RMS GRADIENT = 0.0252608

 NSERCH:   2  E=     -154.0529076654  GRAD. MAX=  0.0642832  R.M.S.=  0.0252608

          HESSIAN UPDATED USING THE BFGS FORMULA
             ACTUAL ENERGY CHANGE WAS  -0.0315589481
          PREDICTED ENERGY CHANGE WAS  -0.0582025268 RATIO=  0.542
          MIN SEARCH, CORRECT HESSIAN, TRYING PURE NR STEP
               NR STEP HAS LENGTH         =   0.182363
          RADIUS OF STEP TAKEN=   0.18236  CURRENT TRUST RADIUS=   0.50000
          TRANSFORMING DISPLACEMENT FROM INTERNALS TO CARTESIANS
          THE ROOT MEAN SQUARE ERROR IN ITERATION   1 IS   0.00071722
          THE ROOT MEAN SQUARE ERROR IN ITERATION   2 IS   0.00000007
          THE ROOT MEAN SQUARE ERROR IN ITERATION   3 IS   0.00000000

 BEGINNING GEOMETRY SEARCH POINT NSERCH=   3 ...

 COORDINATES OF ALL ATOMS ARE (ANGS)
   ATOM   CHARGE       X              Y              Z
 ------------------------------------------------------------
 C           6.0  -1.8500480270   0.0975908461  -0.0000000000
 C           6.0  -0.6100740615  -0.4093209284   0.0000000000
 C           6.0   0.6100740615   0.4093209284  -0.0000000000
 C           6.0   1.8500480270  -0.0975908461   0.0000000000
 H           1.0  -2.0148780951   1.1567871970  -0.0000000000
 H           1.0  -2.7158507474  -0.5288198322  -0.0000000000
 H           1.0  -0.4579065296  -1.4716750641   0.0000000000
 H           1.0   0.4579065295   1.4716750641  -0.0000000000
 H           1.0   2.0148780952  -1.1567871970  -0.0000000000
 H           1.0   2.7158507474   0.5288198323   0.0000000000


                     --------------------
                     INTERNAL COORDINATES
                     --------------------

                 - - ATOMS - -         COORDINATE      COORDINATE
 NO.   TYPE    I  J  K  L  M  N        (BOHR,RAD)       (ANG,DEG)
 ----------------------------------------------------------------
   1 STRETCH   2  1                     2.5314535       1.3395876
   2 STRETCH   3  2                     2.7766345       1.4693318
   3 BEND      3  2  1                  2.1625632     123.9057430
   4 STRETCH   4  3                     2.5314535       1.3395876
   5 BEND      4  3  2                  2.1625632     123.9057430
   6 TORSION   4  3  2  1               3.1415927     180.0000000
   7 STRETCH   5  1                     2.0256821       1.0719449
   8 BEND      5  1  2                  2.1132528     121.0804668
   9 TORSION   5  1  2  3               0.0000000       0.0000000
  10 STRETCH   6  1                     2.0194485       1.0686462
  11 BEND      6  1  5                  2.0427427     117.0405325
  12 TORSION   6  1  5  2               3.1415927     180.0000000
  13 STRETCH   7  2                     2.0280478       1.0731968
  14 BEND      7  2  1                  2.1011415     120.3865396
  15 TORSION   7  2  1  3               3.1415927     180.0000000
  16 STRETCH   8  3                     2.0280478       1.0731968
  17 BEND      8  3  4                  2.1011415     120.3865396
  18 TORSION   8  3  4  2               3.1415927     180.0000000
  19 STRETCH   9  4                     2.0256821       1.0719449
  20 BEND      9  4  3                  2.1132528     121.0804668
  21 TORSION   9  4  3  7               0.0000000       0.0000000
  22 STRETCH  10  4                     2.0194485       1.0686462
  23 BEND     10  4  9                  2.0427427     117.0405325
  24 TORSION  10  4  9  3               3.1415927     180.0000000

          INTERNUCLEAR DISTANCES (ANGS.)
          ------------------------------

                1 C          2 C          3 C          4 C          5 H     

   1 C       0.0000000    1.3395876 *  2.4797936 *  3.7052404    1.0719449 *
   2 C       1.3395876 *  0.0000000    1.4693318 *  2.4797936 *  2.1038462 *
   3 C       2.4797936 *  1.4693318 *  0.0000000    1.3395876 *  2.7293002 *
   4 C       3.7052404    2.4797936 *  1.3395876 *  0.0000000    4.0633875  
   5 H       1.0719449 *  2.1038462 *  2.7293002 *  4.0633875    0.0000000  
   6 H       1.0686462 *  2.1091646 *  3.4557031    4.5862174    1.8255503 *
   7 H       2.0977734 *  1.0731968 *  2.1630369 *  2.6860308 *  3.0549917  
   8 H       2.6860308 *  2.1630369 *  1.0731968 *  2.0977734 *  2.4927531 *
   9 H       4.0633875    2.7293002 *  2.1038462 *  1.0719449 *  4.6466721  
  10 H       4.5862174    3.4557031    2.1091646 *  1.0686462 *  4.7722257  

                6 H          7 H          8 H          9 H         10 H     

   1 C       1.0686462 *  2.0977734 *  2.6860308 *  4.0633875    4.5862174  
   2 C       2.1091646 *  1.0731968 *  2.1630369 *  2.7293002 *  3.4557031  
   3 C       3.4557031    2.1630369 *  1.0731968 *  2.1038462 *  2.1091646 *
   4 C       4.5862174    2.6860308 *  2.0977734 *  1.0719449 *  1.0686462 *
   5 H       1.8255503 *  3.0549917    2.4927531 *  4.6466721    4.7722257  
   6 H       0.0000000    2.4468936 *  3.7516283    4.7722257    5.5337133  
   7 H       2.4468936 *  0.0000000    3.0825352    2.4927531 *  3.7516283  
   8 H       3.7516283    3.0825352    0.0000000    3.0549917    2.4468936 *
   9 H       4.7722257    2.4927531 *  3.0549917    0.0000000    1.8255503 *
  10 H       5.5337133    3.7516283    2.4468936 *  1.8255503 *  0.0000000  

  * ... LESS THAN  3.000

 ...... END OF ONE-ELECTRON INTEGRALS ......
 STEP CPU TIME =     0.00 TOTAL CPU TIME =          0.8 (      0.0 MIN)
 TOTAL WALL CLOCK TIME=          0.8 SECONDS, CPU UTILIZATION IS    94.94%
  ...... END OF TWO-ELECTRON INTEGRALS .....
 STEP CPU TIME =     0.00 TOTAL CPU TIME =          0.8 (      0.0 MIN)
 TOTAL WALL CLOCK TIME=          0.8 SECONDS, CPU UTILIZATION IS    94.94%

          --------------------------
                 RHF SCF CALCULATION
          --------------------------
     DENSITY MATRIX CONV=  1.00E-04

 DIRECT SCF CALCULATION, SCHWRZ=T   FDIFF=T,  DIRTHR=  0.00E+00 NITDIR=10

                                                                                   NONZERO     BLOCKS
 ITER EX DEM     TOTAL ENERGY        E CHANGE  DENSITY CHANGE     ORB. GRAD      INTEGRALS    SKIPPED
          ---------------START SECOND ORDER SCF---------------
   1  0  0     -154.0546695792  -154.0546695792   0.021598367   0.016158733         374541       7896
   2  1  0     -154.0581993702    -0.0035297910   0.005524853   0.003995299         368459      10250
   3  2  0     -154.0584581088    -0.0002587386   0.001924448   0.000991063         365647      10958
   4  3  0     -154.0584656846    -0.0000075757   0.000460856   0.000321694         357684      12669
   5  4  0     -154.0584665878    -0.0000009032   0.000120931   0.000107688         350058      13976
   6  5  0     -154.0584666432    -0.0000000554   0.000044390   0.000015757         338987      15695
   7  6  0     -154.0584666467    -0.0000000035   0.000007125   0.000003972         329997      17566

          -----------------
          DENSITY CONVERGED
          -----------------
     TIME TO FORM FOCK OPERATORS=       0.2 SECONDS (       0.0 SEC/ITER)
     FOCK TIME ON FIRST ITERATION=       0.0, LAST ITERATION=       0.0
     TIME TO SOLVE SCF EQUATIONS=       0.0 SECONDS (       0.0 SEC/ITER)

 FINAL RHF ENERGY IS     -154.0584666467 AFTER   7 ITERATIONS
 ...... END OF RHF CALCULATION ......
 STEP CPU TIME =     0.19 TOTAL CPU TIME =          0.9 (      0.0 MIN)
 TOTAL WALL CLOCK TIME=          1.0 SECONDS, CPU UTILIZATION IS    94.95%
 ..... END OF 1-ELECTRON GRADIENT ......
 STEP CPU TIME =     0.01 TOTAL CPU TIME =          0.9 (      0.0 MIN)
 TOTAL WALL CLOCK TIME=          1.0 SECONDS, CPU UTILIZATION IS    95.96%
 ...... END OF 2-ELECTRON GRADIENT ......
 STEP CPU TIME =     0.04 TOTAL CPU TIME =          1.0 (      0.0 MIN)
 TOTAL WALL CLOCK TIME=          1.0 SECONDS, CPU UTILIZATION IS    96.12%

          NSERCH=  3     ENERGY=    -154.0584666

                                 -----------------------
                                 GRADIENT (HARTREE/BOHR)
                                 -----------------------
        ATOM     ZNUC       DE/DX         DE/DY         DE/DZ
 --------------------------------------------------------------
    1  C            6.0    -0.0258182     0.0084324     0.0000000
    2  C            6.0     0.0176356    -0.0097171     0.0000000
    3  C            6.0    -0.0176356     0.0097171     0.0000000
    4  C            6.0     0.0258182    -0.0084324     0.0000000
    5  H            1.0     0.0010475    -0.0015355     0.0000000
    6  H            1.0     0.0018416     0.0016330     0.0000000
    7  H            1.0     0.0015991     0.0018352     0.0000000
    8  H            1.0    -0.0015991    -0.0018352     0.0000000
    9  H            1.0    -0.0010475     0.0015355     0.0000000
   10  H            1.0    -0.0018416    -0.0016330     0.0000000


                     --------------------
                     INTERNAL COORDINATES
                     --------------------

                 - - ATOMS - -         COORDINATE        GRADIENT
 NO.   TYPE    I  J  K  L  M  N         (ANG,DEG)     (H/B,H/RAD)
 ----------------------------------------------------------------
   1 STRETCH   2  1                     1.3395876       0.0244518
   2 STRETCH   3  2                     1.4693318       0.0027068
   3 BEND      3  2  1                123.9057430       0.0036047
   4 STRETCH   4  3                     1.3395876       0.0244518
   5 BEND      4  3  2                123.9057430       0.0036047
   6 TORSION   4  3  2  1             180.0000000      -0.0000000
   7 STRETCH   5  1                     1.0719449      -0.0016783
   8 BEND      5  1  2                121.0804668      -0.0021102
   9 TORSION   5  1  2  3               0.0000000       0.0000000
  10 STRETCH   6  1                     1.0686462      -0.0024493
  11 BEND      6  1  5                117.0405325      -0.0004919
  12 TORSION   6  1  5  2             180.0000000      -0.0000000
  13 STRETCH   7  2                     1.0731968      -0.0015899
  14 BEND      7  2  1                120.3865396       0.0037379
  15 TORSION   7  2  1  3             180.0000000       0.0000000
  16 STRETCH   8  3                     1.0731968      -0.0015899
  17 BEND      8  3  4                120.3865396       0.0037379
  18 TORSION   8  3  4  2             180.0000000       0.0000000
  19 STRETCH   9  4                     1.0719449      -0.0016783
  20 BEND      9  4  3                121.0804668      -0.0021102
  21 TORSION   9  4  3  7               0.0000000       0.0000000
  22 STRETCH  10  4                     1.0686462      -0.0024493
  23 BEND     10  4  9                117.0405325      -0.0004919
  24 TORSION  10  4  9  3             180.0000000      -0.0000000

 NOTE: CARTESIAN GRADIENTS ARE ALWAYS TAKEN TO TEST CONVERGENCE,
       SO THE FOLLOWING GRADIENTS ARE CARTESIAN.

          MAXIMUM GRADIENT = 0.0258182    RMS GRADIENT = 0.0087885

 NSERCH:   3  E=     -154.0584666467  GRAD. MAX=  0.0258182  R.M.S.=  0.0087885

          HESSIAN UPDATED USING THE BFGS FORMULA
             ACTUAL ENERGY CHANGE WAS  -0.0055589814
          PREDICTED ENERGY CHANGE WAS  -0.0092854495 RATIO=  0.599
          MIN SEARCH, CORRECT HESSIAN, TRYING PURE NR STEP
               NR STEP HAS LENGTH         =   0.055237
          RADIUS OF STEP TAKEN=   0.05524  CURRENT TRUST RADIUS=   0.18236
          TRANSFORMING DISPLACEMENT FROM INTERNALS TO CARTESIANS
          THE ROOT MEAN SQUARE ERROR IN ITERATION   1 IS   0.00043874
          THE ROOT MEAN SQUARE ERROR IN ITERATION   2 IS   0.00000002
          THE ROOT MEAN SQUARE ERROR IN ITERATION   3 IS   0.00000000

 BEGINNING GEOMETRY SEARCH POINT NSERCH=   4 ...

 COORDINATES OF ALL ATOMS ARE (ANGS)
   ATOM   CHARGE       X              Y              Z
 ------------------------------------------------------------
 C           6.0  -1.8291171240   0.0969011128   0.0000000000
 C           6.0  -0.6075798109  -0.4118032626   0.0000000000
 C           6.0   0.6075798109   0.4118032626  -0.0000000000
 C           6.0   1.8291171240  -0.0969011128   0.0000000000
 H           1.0  -1.9986624322   1.1585197876   0.0000000000
 H           1.0  -2.6960663308  -0.5344343934  -0.0000000000
 H           1.0  -0.4772326877  -1.4802647616   0.0000000000
 H           1.0   0.4772326877   1.4802647616  -0.0000000000
 H           1.0   1.9986624321  -1.1585197876  -0.0000000000
 H           1.0   2.6960663308   0.5344343934   0.0000000000


                     --------------------
                     INTERNAL COORDINATES
                     --------------------

                 - - ATOMS - -         COORDINATE      COORDINATE
 NO.   TYPE    I  J  K  L  M  N        (BOHR,RAD)       (ANG,DEG)
 ----------------------------------------------------------------
   1 STRETCH   2  1                     2.5005392       1.3232285
   2 STRETCH   3  2                     2.7740641       1.4679716
   3 BEND      3  2  1                  2.1513350     123.2624136
   4 STRETCH   4  3                     2.5005392       1.3232285
   5 BEND      4  3  2                  2.1513350     123.2624136
   6 TORSION   4  3  2  1               3.1415927     180.0000000
   7 STRETCH   5  1                     2.0315915       1.0750720
   8 BEND      5  1  2                  2.1237666     121.6828624
   9 TORSION   5  1  2  3               0.0000000       0.0000000
  10 STRETCH   6  1                     2.0266687       1.0724670
  11 BEND      6  1  5                  2.0418491     116.9893352
  12 TORSION   6  1  5  2               3.1415927     180.0000000
  13 STRETCH   7  2                     2.0340689       1.0763830
  14 BEND      7  2  1                  2.0867947     119.5645308
  15 TORSION   7  2  1  3               3.1415927     180.0000000
  16 STRETCH   8  3                     2.0340689       1.0763830
  17 BEND      8  3  4                  2.0867947     119.5645308
  18 TORSION   8  3  4  2               3.1415927     180.0000000
  19 STRETCH   9  4                     2.0315915       1.0750720
  20 BEND      9  4  3                  2.1237666     121.6828624
  21 TORSION   9  4  3  7               0.0000000       0.0000000
  22 STRETCH  10  4                     2.0266687       1.0724670
  23 BEND     10  4  9                  2.0418491     116.9893352
  24 TORSION  10  4  9  3               3.1415927     180.0000000

          INTERNUCLEAR DISTANCES (ANGS.)
          ------------------------------

                1 C          2 C          3 C          4 C          5 H     

   1 C       0.0000000    1.3232285 *  2.4569606 *  3.6633642    1.0750720 *
   2 C       1.3232285 *  0.0000000    1.4679716 *  2.4569606 *  2.0978621 *
   3 C       2.4569606 *  1.4679716 *  0.0000000    1.3232285 *  2.7111039 *
   4 C       3.6633642    2.4569606 *  1.3232285 *  0.0000000    4.0283965  
   5 H       1.0750720 *  2.0978621 *  2.7111039 *  4.0283965    0.0000000  
   6 H       1.0724670 *  2.0920837 *  3.4364871    4.5462865    1.8309741 *
   7 H       2.0772683 *  1.0763830 *  2.1809951 *  2.6894134 *  3.0459699  
   8 H       2.6894134 *  2.1809951 *  1.0763830 *  2.0772683 *  2.4967131 *
   9 H       4.0283965    2.7111039 *  2.0978621 *  1.0750720 *  4.6203115  
  10 H       4.5462865    3.4364871    2.0920837 *  1.0724670 *  4.7360279  

                6 H          7 H          8 H          9 H         10 H     

   1 C       1.0724670 *  2.0772683 *  2.6894134 *  4.0283965    4.5462865  
   2 C       2.0920837 *  1.0763830 *  2.1809951 *  2.7111039 *  3.4364871  
   3 C       3.4364871    2.1809951 *  1.0763830 *  2.0978621 *  2.0920837 *
   4 C       4.5462865    2.6894134 *  2.0772683 *  1.0750720 *  1.0724670 *
   5 H       1.8309741 *  3.0459699    2.4967131 *  4.6203115    4.7360279  
   6 H       0.0000000    2.4120153 *  3.7588348    4.7360279    5.4970515  
   7 H       2.4120153 *  0.0000000    3.1105850    2.4967131 *  3.7588348  
   8 H       3.7588348    3.1105850    0.0000000    3.0459699    2.4120153 *
   9 H       4.7360279    2.4967131 *  3.0459699    0.0000000    1.8309741 *
  10 H       5.4970515    3.7588348    2.4120153 *  1.8309741 *  0.0000000  

  * ... LESS THAN  3.000

 ...... END OF ONE-ELECTRON INTEGRALS ......
 STEP CPU TIME =     0.00 TOTAL CPU TIME =          1.0 (      0.0 MIN)
 TOTAL WALL CLOCK TIME=          1.0 SECONDS, CPU UTILIZATION IS    95.19%
  ...... END OF TWO-ELECTRON INTEGRALS .....
 STEP CPU TIME =     0.01 TOTAL CPU TIME =          1.0 (      0.0 MIN)
 TOTAL WALL CLOCK TIME=          1.0 SECONDS, CPU UTILIZATION IS    96.15%

          --------------------------
                 RHF SCF CALCULATION
          --------------------------
     DENSITY MATRIX CONV=  1.00E-04

 DIRECT SCF CALCULATION, SCHWRZ=T   FDIFF=T,  DIRTHR=  0.00E+00 NITDIR=10

                                                                                   NONZERO     BLOCKS
 ITER EX DEM     TOTAL ENERGY        E CHANGE  DENSITY CHANGE     ORB. GRAD      INTEGRALS    SKIPPED
          ---------------START SECOND ORDER SCF---------------
   1  0  0     -154.0590513267  -154.0590513267   0.008376017   0.003879942         375670       7804
   2  1  0     -154.0593000499    -0.0002487232   0.001133643   0.000923004         366044      11020
   3  2  0     -154.0593147651    -0.0000147152   0.000422003   0.000239627         360984      12080
   4  3  0     -154.0593155336    -0.0000007685   0.000098408   0.000074242         352020      13761
   5  4  0     -154.0593156030    -0.0000000694   0.000020875   0.000017710         339257      15684
   6  5  0     -154.0593156091    -0.0000000061   0.000009915   0.000006151         329909      17253

          -----------------
          DENSITY CONVERGED
          -----------------
     TIME TO FORM FOCK OPERATORS=       0.1 SECONDS (       0.0 SEC/ITER)
     FOCK TIME ON FIRST ITERATION=       0.0, LAST ITERATION=       0.0
     TIME TO SOLVE SCF EQUATIONS=       0.0 SECONDS (       0.0 SEC/ITER)

 FINAL RHF ENERGY IS     -154.0593156091 AFTER   6 ITERATIONS
 ...... END OF RHF CALCULATION ......
 STEP CPU TIME =     0.15 TOTAL CPU TIME =          1.1 (      0.0 MIN)
 TOTAL WALL CLOCK TIME=          1.2 SECONDS, CPU UTILIZATION IS    96.64%
 ..... END OF 1-ELECTRON GRADIENT ......
 STEP CPU TIME =     0.00 TOTAL CPU TIME =          1.1 (      0.0 MIN)
 TOTAL WALL CLOCK TIME=          1.2 SECONDS, CPU UTILIZATION IS    96.64%
 ...... END OF 2-ELECTRON GRADIENT ......
 STEP CPU TIME =     0.04 TOTAL CPU TIME =          1.2 (      0.0 MIN)
 TOTAL WALL CLOCK TIME=          1.2 SECONDS, CPU UTILIZATION IS    96.75%

          NSERCH=  4     ENERGY=    -154.0593156

                                 -----------------------
                                 GRADIENT (HARTREE/BOHR)
                                 -----------------------
        ATOM     ZNUC       DE/DX         DE/DY         DE/DZ
 --------------------------------------------------------------
    1  C            6.0    -0.0029205     0.0024487     0.0000000
    2  C            6.0     0.0053538    -0.0053906     0.0000000
    3  C            6.0    -0.0053538     0.0053906     0.0000000
    4  C            6.0     0.0029205    -0.0024487     0.0000000
    5  H            1.0     0.0005560     0.0008545     0.0000000
    6  H            1.0     0.0007453    -0.0010105     0.0000000
    7  H            1.0    -0.0017801    -0.0012167     0.0000000
    8  H            1.0     0.0017801     0.0012167     0.0000000
    9  H            1.0    -0.0005560    -0.0008545     0.0000000
   10  H            1.0    -0.0007453     0.0010105     0.0000000


                     --------------------
                     INTERNAL COORDINATES
                     --------------------

                 - - ATOMS - -         COORDINATE        GRADIENT
 NO.   TYPE    I  J  K  L  M  N         (ANG,DEG)     (H/B,H/RAD)
 ----------------------------------------------------------------
   1 STRETCH   2  1                     1.3232285       0.0023763
   2 STRETCH   3  2                     1.4679716       0.0008028
   3 BEND      3  2  1                123.2624136      -0.0064746
   4 STRETCH   4  3                     1.3232285       0.0023763
   5 BEND      4  3  2                123.2624136      -0.0064746
   6 TORSION   4  3  2  1             180.0000000       0.0000000
   7 STRETCH   5  1                     1.0750720       0.0007561
   8 BEND      5  1  2                121.6828624       0.0011555
   9 TORSION   5  1  2  3               0.0000000       0.0000000
  10 STRETCH   6  1                     1.0724670      -0.0000077
  11 BEND      6  1  5                116.9893352       0.0025446
  12 TORSION   6  1  5  2             180.0000000       0.0000000
  13 STRETCH   7  2                     1.0763830       0.0009922
  14 BEND      7  2  1                119.5645308      -0.0038939
  15 TORSION   7  2  1  3             180.0000000      -0.0000000
  16 STRETCH   8  3                     1.0763830       0.0009922
  17 BEND      8  3  4                119.5645308      -0.0038939
  18 TORSION   8  3  4  2             180.0000000      -0.0000000
  19 STRETCH   9  4                     1.0750720       0.0007561
  20 BEND      9  4  3                121.6828624       0.0011555
  21 TORSION   9  4  3  7               0.0000000      -0.0000000
  22 STRETCH  10  4                     1.0724670      -0.0000077
  23 BEND     10  4  9                116.9893352       0.0025446
  24 TORSION  10  4  9  3             180.0000000       0.0000000

 NOTE: CARTESIAN GRADIENTS ARE ALWAYS TAKEN TO TEST CONVERGENCE,
       SO THE FOLLOWING GRADIENTS ARE CARTESIAN.

          MAXIMUM GRADIENT = 0.0053906    RMS GRADIENT = 0.0023023

 NSERCH:   4  E=     -154.0593156091  GRAD. MAX=  0.0053906  R.M.S.=  0.0023023

          HESSIAN UPDATED USING THE BFGS FORMULA
             ACTUAL ENERGY CHANGE WAS  -0.0008489623
          PREDICTED ENERGY CHANGE WAS  -0.0009124138 RATIO=  0.930
          MIN SEARCH, CORRECT HESSIAN, TRYING PURE NR STEP
               NR STEP HAS LENGTH         =   0.043453
          RADIUS OF STEP TAKEN=   0.04345  CURRENT TRUST RADIUS=   0.11047
          TRANSFORMING DISPLACEMENT FROM INTERNALS TO CARTESIANS
          THE ROOT MEAN SQUARE ERROR IN ITERATION   1 IS   0.00041428
          THE ROOT MEAN SQUARE ERROR IN ITERATION   2 IS   0.00000000
          THE ROOT MEAN SQUARE ERROR IN ITERATION   3 IS   0.00000000

 BEGINNING GEOMETRY SEARCH POINT NSERCH=   5 ...

 COORDINATES OF ALL ATOMS ARE (ANGS)
   ATOM   CHARGE       X              Y              Z
 ------------------------------------------------------------
 C           6.0  -1.8316114078   0.0941147605   0.0000000000
 C           6.0  -0.6125750915  -0.4028794939  -0.0000000000
 C           6.0   0.6125750915   0.4028794939   0.0000000000
 C           6.0   1.8316114078  -0.0941147605   0.0000000000
 H           1.0  -2.0068262802   1.1542231590   0.0000000000
 H           1.0  -2.7033467946  -0.5318622257  -0.0000000000
 H           1.0  -0.4607976282  -1.4675733179   0.0000000000
 H           1.0   0.4607976282   1.4675733179  -0.0000000000
 H           1.0   2.0068262802  -1.1542231589   0.0000000000
 H           1.0   2.7033467946   0.5318622257  -0.0000000000


                     --------------------
                     INTERNAL COORDINATES
                     --------------------

                 - - ATOMS - -         COORDINATE      COORDINATE
 NO.   TYPE    I  J  K  L  M  N        (BOHR,RAD)       (ANG,DEG)
 ----------------------------------------------------------------
   1 STRETCH   2  1                     2.4877386       1.3164546
   2 STRETCH   3  2                     2.7710372       1.4663698
   3 BEND      3  2  1                  2.1727143     124.4873620
   4 STRETCH   4  3                     2.4877386       1.3164546
   5 BEND      4  3  2                  2.1727143     124.4873620
   6 TORSION   4  3  2  1               3.1415927     180.0000000
   7 STRETCH   5  1                     2.0304928       1.0744906
   8 BEND      5  1  2                  2.1217175     121.5654563
   9 TORSION   5  1  2  3               0.0000000       0.0000000
  10 STRETCH   6  1                     2.0280641       1.0732054
  11 BEND      6  1  5                  2.0297553     116.2964149
  12 TORSION   6  1  5  2               3.1415927     180.0000000
  13 STRETCH   7  2                     2.0323204       1.0754577
  14 BEND      7  2  1                  2.0995191     120.2935843
  15 TORSION   7  2  1  3               3.1415927     180.0000000
  16 STRETCH   8  3                     2.0323204       1.0754577
  17 BEND      8  3  4                  2.0995191     120.2935843
  18 TORSION   8  3  4  2               3.1415927     180.0000000
  19 STRETCH   9  4                     2.0304928       1.0744906
  20 BEND      9  4  3                  2.1217175     121.5654563
  21 TORSION   9  4  3  7               0.0000000       0.0000000
  22 STRETCH  10  4                     2.0280641       1.0732054
  23 BEND     10  4  9                  2.0297553     116.2964149
  24 TORSION  10  4  9  3               3.1415927     180.0000000

          INTERNUCLEAR DISTANCES (ANGS.)
          ------------------------------

                1 C          2 C          3 C          4 C          5 H     

   1 C       0.0000000    1.3164546 *  2.4636118 *  3.6680556    1.0744906 *
   2 C       1.3164546 *  0.0000000    1.4663698 *  2.4636118 *  2.0900969 *
   3 C       2.4636118 *  1.4663698 *  0.0000000    1.3164546 *  2.7250286 *
   4 C       3.6680556    2.4636118 *  1.3164546 *  0.0000000    4.0363290  
   5 H       1.0744906 *  2.0900969 *  2.7250286 *  4.0363290    0.0000000  
   6 H       1.0732054 *  2.0947465 *  3.4451531    4.5560365    1.8242875 *
   7 H       2.0779798 *  1.0754577 *  2.1565534 *  2.6723637 *  3.0436855  
   8 H       2.6723637 *  2.1565534 *  1.0754577 *  2.0779798 *  2.4874397 *
   9 H       4.0363290    2.7250286 *  2.0900969 *  1.0744906 *  4.6301546  
  10 H       4.5560365    3.4451531    2.0947465 *  1.0732054 *  4.7511118  

                6 H          7 H          8 H          9 H         10 H     

   1 C       1.0732054 *  2.0779798 *  2.6723637 *  4.0363290    4.5560365  
   2 C       2.0947465 *  1.0754577 *  2.1565534 *  2.7250286 *  3.4451531  
   3 C       3.4451531    2.1565534 *  1.0754577 *  2.0900969 *  2.0947465 *
   4 C       4.5560365    2.6723637 *  2.0779798 *  1.0744906 *  1.0732054 *
   5 H       1.8242875 *  3.0436855    2.4874397 *  4.6301546    4.7511118  
   6 H       0.0000000    2.4299346 *  3.7429337    4.7511118    5.5103399  
   7 H       2.4299346 *  0.0000000    3.0764303    2.4874397 *  3.7429337  
   8 H       3.7429337    3.0764303    0.0000000    3.0436855    2.4299346 *
   9 H       4.7511118    2.4874397 *  3.0436855    0.0000000    1.8242875 *
  10 H       5.5103399    3.7429337    2.4299346 *  1.8242875 *  0.0000000  

  * ... LESS THAN  3.000

 ...... END OF ONE-ELECTRON INTEGRALS ......
 STEP CPU TIME =     0.00 TOTAL CPU TIME =          1.2 (      0.0 MIN)
 TOTAL WALL CLOCK TIME=          1.2 SECONDS, CPU UTILIZATION IS    95.97%
  ...... END OF TWO-ELECTRON INTEGRALS .....
 STEP CPU TIME =     0.00 TOTAL CPU TIME =          1.2 (      0.0 MIN)
 TOTAL WALL CLOCK TIME=          1.2 SECONDS, CPU UTILIZATION IS    95.97%

          --------------------------
                 RHF SCF CALCULATION
          --------------------------
     DENSITY MATRIX CONV=  2.00E-05

 DIRECT SCF CALCULATION, SCHWRZ=T   FDIFF=T,  DIRTHR=  0.00E+00 NITDIR=10

                                                                                   NONZERO     BLOCKS
 ITER EX DEM     TOTAL ENERGY        E CHANGE  DENSITY CHANGE     ORB. GRAD      INTEGRALS    SKIPPED
          ---------------START SECOND ORDER SCF---------------
   1  0  0     -154.0592062875  -154.0592062875   0.003058378   0.004711804         375654       7780
   2  1  0     -154.0593323418    -0.0001260543   0.001829928   0.000720550         365136      11237
   3  2  0     -154.0593405436    -0.0000082019   0.000324095   0.000304569         360516      12136
   4  3  0     -154.0593409885    -0.0000004449   0.000064678   0.000065047         349206      14083
   5  4  0     -154.0593410284    -0.0000000399   0.000016898   0.000020289         337137      16028
   6  5  0     -154.0593410317    -0.0000000032   0.000008765   0.000003090         326643      17717

          -----------------
          DENSITY CONVERGED
          -----------------
     TIME TO FORM FOCK OPERATORS=       0.1 SECONDS (       0.0 SEC/ITER)
     FOCK TIME ON FIRST ITERATION=       0.0, LAST ITERATION=       0.0
     TIME TO SOLVE SCF EQUATIONS=       0.0 SECONDS (       0.0 SEC/ITER)

 FINAL RHF ENERGY IS     -154.0593410317 AFTER   6 ITERATIONS
 ...... END OF RHF CALCULATION ......
 STEP CPU TIME =     0.14 TOTAL CPU TIME =          1.3 (      0.0 MIN)
 TOTAL WALL CLOCK TIME=          1.4 SECONDS, CPU UTILIZATION IS    97.08%
 ..... END OF 1-ELECTRON GRADIENT ......
 STEP CPU TIME =     0.00 TOTAL CPU TIME =          1.3 (      0.0 MIN)
 TOTAL WALL CLOCK TIME=          1.4 SECONDS, CPU UTILIZATION IS    96.38%
 ...... END OF 2-ELECTRON GRADIENT ......
 STEP CPU TIME =     0.05 TOTAL CPU TIME =          1.4 (      0.0 MIN)
 TOTAL WALL CLOCK TIME=          1.4 SECONDS, CPU UTILIZATION IS    96.50%

          NSERCH=  5     ENERGY=    -154.0593410

                                 -----------------------
                                 GRADIENT (HARTREE/BOHR)
                                 -----------------------
        ATOM     ZNUC       DE/DX         DE/DY         DE/DZ
 --------------------------------------------------------------
    1  C            6.0     0.0041820    -0.0027945     0.0000000
    2  C            6.0    -0.0064435     0.0057789     0.0000000
    3  C            6.0     0.0064435    -0.0057789     0.0000000
    4  C            6.0    -0.0041820     0.0027945     0.0000000
    5  H            1.0     0.0003412    -0.0001358     0.0000000
    6  H            1.0    -0.0008711     0.0000107     0.0000000
    7  H            1.0     0.0016358     0.0008156     0.0000000
    8  H            1.0    -0.0016358    -0.0008156     0.0000000
    9  H            1.0    -0.0003412     0.0001358     0.0000000
   10  H            1.0     0.0008711    -0.0000107     0.0000000


                     --------------------
                     INTERNAL COORDINATES
                     --------------------

                 - - ATOMS - -         COORDINATE        GRADIENT
 NO.   TYPE    I  J  K  L  M  N         (ANG,DEG)     (H/B,H/RAD)
 ----------------------------------------------------------------
   1 STRETCH   2  1                     1.3164546      -0.0044839
   2 STRETCH   3  2                     1.4663698      -0.0010538
   3 BEND      3  2  1                124.4873620       0.0051341
   4 STRETCH   4  3                     1.3164546      -0.0044839
   5 BEND      4  3  2                124.4873620       0.0051341
   6 TORSION   4  3  2  1             180.0000000      -0.0000000
   7 STRETCH   5  1                     1.0744906      -0.0001896
   8 BEND      5  1  2                121.5654563      -0.0016867
   9 TORSION   5  1  2  3               0.0000000       0.0000000
  10 STRETCH   6  1                     1.0732054       0.0007013
  11 BEND      6  1  5                116.2964149      -0.0010482
  12 TORSION   6  1  5  2             180.0000000      -0.0000000
  13 STRETCH   7  2                     1.0754577      -0.0005766
  14 BEND      7  2  1                120.2935843       0.0035252
  15 TORSION   7  2  1  3             180.0000000      -0.0000000
  16 STRETCH   8  3                     1.0754577      -0.0005766
  17 BEND      8  3  4                120.2935843       0.0035252
  18 TORSION   8  3  4  2             180.0000000       0.0000000
  19 STRETCH   9  4                     1.0744906      -0.0001896
  20 BEND      9  4  3                121.5654563      -0.0016867
  21 TORSION   9  4  3  7               0.0000000       0.0000000
  22 STRETCH  10  4                     1.0732054       0.0007013
  23 BEND     10  4  9                116.2964149      -0.0010482
  24 TORSION  10  4  9  3             180.0000000      -0.0000000

 NOTE: CARTESIAN GRADIENTS ARE ALWAYS TAKEN TO TEST CONVERGENCE,
       SO THE FOLLOWING GRADIENTS ARE CARTESIAN.

          MAXIMUM GRADIENT = 0.0064435    RMS GRADIENT = 0.0026388

 NSERCH:   5  E=     -154.0593410317  GRAD. MAX=  0.0064435  R.M.S.=  0.0026388

          HESSIAN UPDATED USING THE BFGS FORMULA
             ACTUAL ENERGY CHANGE WAS  -0.0000254226
          PREDICTED ENERGY CHANGE WAS  -0.0002553204 RATIO=  0.100
          MIN SEARCH, CORRECT HESSIAN, TRYING PURE NR STEP
               NR STEP HAS LENGTH         =   0.020558
          RADIUS OF STEP TAKEN=   0.02056  CURRENT TRUST RADIUS=   0.05000
          TRANSFORMING DISPLACEMENT FROM INTERNALS TO CARTESIANS
          THE ROOT MEAN SQUARE ERROR IN ITERATION   1 IS   0.00009897
          THE ROOT MEAN SQUARE ERROR IN ITERATION   2 IS   0.00000000

 BEGINNING GEOMETRY SEARCH POINT NSERCH=   6 ...

 COORDINATES OF ALL ATOMS ARE (ANGS)
   ATOM   CHARGE       X              Y              Z
 ------------------------------------------------------------
 C           6.0  -1.8315553690   0.0954393300   0.0000000000
 C           6.0  -0.6103997416  -0.4069488932   0.0000000000
 C           6.0   0.6103997416   0.4069488932  -0.0000000000
 C           6.0   1.8315553690  -0.0954393300   0.0000000000
 H           1.0  -2.0062031599   1.1554694560   0.0000000000
 H           1.0  -2.7010272788  -0.5320144832  -0.0000000000
 H           1.0  -0.4691109419  -1.4732343860   0.0000000000
 H           1.0   0.4691109419   1.4732343860  -0.0000000000
 H           1.0   2.0062031599  -1.1554694560  -0.0000000000
 H           1.0   2.7010272788   0.5320144832   0.0000000000


                     --------------------
                     INTERNAL COORDINATES
                     --------------------

                 - - ATOMS - -         COORDINATE      COORDINATE
 NO.   TYPE    I  J  K  L  M  N        (BOHR,RAD)       (ANG,DEG)
 ----------------------------------------------------------------
   1 STRETCH   2  1                     2.4953079       1.3204601
   2 STRETCH   3  2                     2.7726737       1.4672358
   3 BEND      3  2  1                  2.1632737     123.9464516
   4 STRETCH   4  3                     2.4953079       1.3204601
   5 BEND      4  3  2                  2.1632737     123.9464516
   6 TORSION   4  3  2  1               3.1415927     180.0000000
   7 STRETCH   5  1                     2.0301724       1.0743211
   8 BEND      5  1  2                  2.1243853     121.7183106
   9 TORSION   5  1  2  3               0.0000000       0.0000000
  10 STRETCH   6  1                     2.0262231       1.0722312
  11 BEND      6  1  5                  2.0326143     116.4602224
  12 TORSION   6  1  5  2               3.1415927     180.0000000
  13 STRETCH   7  2                     2.0325997       1.0756055
  14 BEND      7  2  1                  2.0928330     119.9104996
  15 TORSION   7  2  1  3               3.1415927     180.0000000
  16 STRETCH   8  3                     2.0325997       1.0756055
  17 BEND      8  3  4                  2.0928330     119.9104996
  18 TORSION   8  3  4  2               3.1415927     180.0000000
  19 STRETCH   9  4                     2.0301724       1.0743211
  20 BEND      9  4  3                  2.1243853     121.7183106
  21 TORSION   9  4  3  7               0.0000000       0.0000000
  22 STRETCH  10  4                     2.0262231       1.0722312
  23 BEND     10  4  9                  2.0326143     116.4602224
  24 TORSION  10  4  9  3               3.1415927     180.0000000

          INTERNUCLEAR DISTANCES (ANGS.)
          ------------------------------

                1 C          2 C          3 C          4 C          5 H     

   1 C       0.0000000    1.3204601 *  2.4617439 *  3.6680806    1.0743211 *
   2 C       1.3204601 *  0.0000000    1.4672358 *  2.4617439 *  2.0950939 *
   3 C       2.4617439 *  1.4672358 *  0.0000000    1.3204601 *  2.7215609 *
   4 C       3.6680806    2.4617439 *  1.3204601 *  0.0000000    4.0364791  
   5 H       1.0743211 *  2.0950939 *  2.7215609 *  4.0364791    0.0000000  
   6 H       1.0722312 *  2.0943650 *  3.4419763    4.5535594    1.8249336 *
   7 H       2.0777372 *  1.0756055 *  2.1680481 *  2.6816757 *  3.0451168  
   8 H       2.6816757 *  2.1680481 *  1.0756055 *  2.0777372 *  2.4956271 *
   9 H       4.0364791    2.7215609 *  2.0950939 *  1.0743211 *  4.6303178  
  10 H       4.5535594    3.4419763    2.0943650 *  1.0722312 *  4.7483381  

                6 H          7 H          8 H          9 H         10 H     

   1 C       1.0722312 *  2.0777372 *  2.6816757 *  4.0364791    4.5535594  
   2 C       2.0943650 *  1.0756055 *  2.1680481 *  2.7215609 *  3.4419763  
   3 C       3.4419763    2.1680481 *  1.0756055 *  2.0950939 *  2.0943650 *
   4 C       4.5535594    2.6816757 *  2.0777372 *  1.0743211 *  1.0722312 *
   5 H       1.8249336 *  3.0451168    2.4956271 *  4.6303178    4.7483381  
   6 H       0.0000000    2.4222604 *  3.7511064    4.7483381    5.5058470  
   7 H       2.4222604 *  0.0000000    3.0922384    2.4956271 *  3.7511064  
   8 H       3.7511064    3.0922384    0.0000000    3.0451168    2.4222604 *
   9 H       4.7483381    2.4956271 *  3.0451168    0.0000000    1.8249336 *
  10 H       5.5058470    3.7511064    2.4222604 *  1.8249336 *  0.0000000  

  * ... LESS THAN  3.000

 ...... END OF ONE-ELECTRON INTEGRALS ......
 STEP CPU TIME =     0.00 TOTAL CPU TIME =          1.4 (      0.0 MIN)
 TOTAL WALL CLOCK TIME=          1.4 SECONDS, CPU UTILIZATION IS    96.50%
  ...... END OF TWO-ELECTRON INTEGRALS .....
 STEP CPU TIME =     0.00 TOTAL CPU TIME =          1.4 (      0.0 MIN)
 TOTAL WALL CLOCK TIME=          1.4 SECONDS, CPU UTILIZATION IS    96.50%

          --------------------------
                 RHF SCF CALCULATION
          --------------------------
     DENSITY MATRIX CONV=  2.00E-05

 DIRECT SCF CALCULATION, SCHWRZ=T   FDIFF=T,  DIRTHR=  0.00E+00 NITDIR=10

                                                                                   NONZERO     BLOCKS
 ITER EX DEM     TOTAL ENERGY        E CHANGE  DENSITY CHANGE     ORB. GRAD      INTEGRALS    SKIPPED
          ---------------START SECOND ORDER SCF---------------
   1  0  0     -154.0594220965  -154.0594220965   0.001277610   0.002151468         375554       7812
   2  1  0     -154.0594537243    -0.0000316278   0.000803109   0.000385452         362192      11962
   3  2  0     -154.0594558909    -0.0000021666   0.000168778   0.000155174         356681      12823
   4  3  0     -154.0594560299    -0.0000001390   0.000032794   0.000035279         343874      15038
   5  4  0     -154.0594560415    -0.0000000116   0.000009488   0.000009438         331639      17056
   6  5  0     -154.0594560426    -0.0000000011   0.000005682   0.000002088         320829      18671

          -----------------
          DENSITY CONVERGED
          -----------------
     TIME TO FORM FOCK OPERATORS=       0.1 SECONDS (       0.0 SEC/ITER)
     FOCK TIME ON FIRST ITERATION=       0.0, LAST ITERATION=       0.0
     TIME TO SOLVE SCF EQUATIONS=       0.0 SECONDS (       0.0 SEC/ITER)

 FINAL RHF ENERGY IS     -154.0594560426 AFTER   6 ITERATIONS
 ...... END OF RHF CALCULATION ......
 STEP CPU TIME =     0.13 TOTAL CPU TIME =          1.5 (      0.0 MIN)
 TOTAL WALL CLOCK TIME=          1.6 SECONDS, CPU UTILIZATION IS    96.79%
 ..... END OF 1-ELECTRON GRADIENT ......
 STEP CPU TIME =     0.00 TOTAL CPU TIME =          1.5 (      0.0 MIN)
 TOTAL WALL CLOCK TIME=          1.6 SECONDS, CPU UTILIZATION IS    96.79%
 ...... END OF 2-ELECTRON GRADIENT ......
 STEP CPU TIME =     0.04 TOTAL CPU TIME =          1.5 (      0.0 MIN)
 TOTAL WALL CLOCK TIME=          1.6 SECONDS, CPU UTILIZATION IS    96.87%

          NSERCH=  6     ENERGY=    -154.0594560

                                 -----------------------
                                 GRADIENT (HARTREE/BOHR)
                                 -----------------------
        ATOM     ZNUC       DE/DX         DE/DY         DE/DZ
 --------------------------------------------------------------
    1  C            6.0    -0.0003388    -0.0000976     0.0000000
    2  C            6.0     0.0000329    -0.0000067     0.0000000
    3  C            6.0    -0.0000329     0.0000067     0.0000000
    4  C            6.0     0.0003388     0.0000976     0.0000000
    5  H            1.0     0.0001721    -0.0000662     0.0000000
    6  H            1.0     0.0001101     0.0000631     0.0000000
    7  H            1.0    -0.0000232     0.0000350     0.0000000
    8  H            1.0     0.0000232    -0.0000350     0.0000000
    9  H            1.0    -0.0001721     0.0000662     0.0000000
   10  H            1.0    -0.0001101    -0.0000631     0.0000000


                     --------------------
                     INTERNAL COORDINATES
                     --------------------

                 - - ATOMS - -         COORDINATE        GRADIENT
 NO.   TYPE    I  J  K  L  M  N         (ANG,DEG)     (H/B,H/RAD)
 ----------------------------------------------------------------
   1 STRETCH   2  1                     1.3204601       0.0000140
   2 STRETCH   3  2                     1.4672358       0.0000791
   3 BEND      3  2  1                123.9464516      -0.0000475
   4 STRETCH   4  3                     1.3204601       0.0000140
   5 BEND      4  3  2                123.9464516      -0.0000475
   6 TORSION   4  3  2  1             180.0000000      -0.0000000
   7 STRETCH   5  1                     1.0743211      -0.0000933
   8 BEND      5  1  2                121.7183106      -0.0002960
   9 TORSION   5  1  2  3               0.0000000      -0.0000000
  10 STRETCH   6  1                     1.0722312      -0.0001263
  11 BEND      6  1  5                116.4602224       0.0000269
  12 TORSION   6  1  5  2             180.0000000       0.0000000
  13 STRETCH   7  2                     1.0756055      -0.0000378
  14 BEND      7  2  1                119.9104996      -0.0000375
  15 TORSION   7  2  1  3             180.0000000      -0.0000000
  16 STRETCH   8  3                     1.0756055      -0.0000378
  17 BEND      8  3  4                119.9104996      -0.0000375
  18 TORSION   8  3  4  2             180.0000000       0.0000000
  19 STRETCH   9  4                     1.0743211      -0.0000933
  20 BEND      9  4  3                121.7183106      -0.0002960
  21 TORSION   9  4  3  7               0.0000000      -0.0000000
  22 STRETCH  10  4                     1.0722312      -0.0001263
  23 BEND     10  4  9                116.4602224       0.0000269
  24 TORSION  10  4  9  3             180.0000000      -0.0000000

 NOTE: CARTESIAN GRADIENTS ARE ALWAYS TAKEN TO TEST CONVERGENCE,
       SO THE FOLLOWING GRADIENTS ARE CARTESIAN.

          MAXIMUM GRADIENT = 0.0003388    RMS GRADIENT = 0.0001087

 NSERCH:   6  E=     -154.0594560426  GRAD. MAX=  0.0003388  R.M.S.=  0.0001087

          HESSIAN UPDATED USING THE BFGS FORMULA
             ACTUAL ENERGY CHANGE WAS  -0.0001150109
          PREDICTED ENERGY CHANGE WAS  -0.0001157288 RATIO=  0.994
          MIN SEARCH, CORRECT HESSIAN, TRYING PURE NR STEP
               NR STEP HAS LENGTH         =   0.002107
          RADIUS OF STEP TAKEN=   0.00211  CURRENT TRUST RADIUS=   0.05000
          TRANSFORMING DISPLACEMENT FROM INTERNALS TO CARTESIANS
          THE ROOT MEAN SQUARE ERROR IN ITERATION   1 IS   0.00000188
          THE ROOT MEAN SQUARE ERROR IN ITERATION   2 IS   0.00000000

 BEGINNING GEOMETRY SEARCH POINT NSERCH=   7 ...

 COORDINATES OF ALL ATOMS ARE (ANGS)
   ATOM   CHARGE       X              Y              Z
 ------------------------------------------------------------
 C           6.0  -1.8315526139   0.0955967856   0.0000000000
 C           6.0  -0.6104266397  -0.4067910643   0.0000000000
 C           6.0   0.6104266397   0.4067910643  -0.0000000000
 C           6.0   1.8315526139  -0.0955967855   0.0000000000
 H           1.0  -2.0076669597   1.1555294051   0.0000000000
 H           1.0  -2.7004344186  -0.5330115028  -0.0000000000
 H           1.0  -0.4689788041  -1.4731068720   0.0000000000
 H           1.0   0.4689788040   1.4731068720  -0.0000000000
 H           1.0   2.0076669598  -1.1555294051  -0.0000000000
 H           1.0   2.7004344186   0.5330115029   0.0000000000


                     --------------------
                     INTERNAL COORDINATES
                     --------------------

                 - - ATOMS - -         COORDINATE      COORDINATE
 NO.   TYPE    I  J  K  L  M  N        (BOHR,RAD)       (ANG,DEG)
 ----------------------------------------------------------------
   1 STRETCH   2  1                     2.4952558       1.3204326
   2 STRETCH   3  2                     2.7724274       1.4671055
   3 BEND      3  2  1                  2.1634648     123.9573995
   4 STRETCH   4  3                     2.4952558       1.3204326
   5 BEND      4  3  2                  2.1634648     123.9573995
   6 TORSION   4  3  2  1               3.1415927     180.0000000
   7 STRETCH   5  1                     2.0304430       1.0744642
   8 BEND      5  1  2                  2.1257551     121.7967942
   9 TORSION   5  1  2  3               0.0000000       0.0000000
  10 STRETCH   6  1                     2.0265970       1.0724290
  11 BEND      6  1  5                  2.0324478     116.4506783
  12 TORSION   6  1  5  2               3.1415927     180.0000000
  13 STRETCH   7  2                     2.0326960       1.0756565
  14 BEND      7  2  1                  2.0929842     119.9191599
  15 TORSION   7  2  1  3               3.1415927     180.0000000
  16 STRETCH   8  3                     2.0326960       1.0756565
  17 BEND      8  3  4                  2.0929842     119.9191599
  18 TORSION   8  3  4  2               3.1415927     180.0000000
  19 STRETCH   9  4                     2.0304430       1.0744642
  20 BEND      9  4  3                  2.1257551     121.7967942
  21 TORSION   9  4  3  7               0.0000000       0.0000000
  22 STRETCH  10  4                     2.0265970       1.0724290
  23 BEND     10  4  9                  2.0324478     116.4506783
  24 TORSION  10  4  9  3               3.1415927     180.0000000

          INTERNUCLEAR DISTANCES (ANGS.)
          ------------------------------

                1 C          2 C          3 C          4 C          5 H     

   1 C       0.0000000    1.3204326 *  2.4617280 *  3.6680915    1.0744642 *
   2 C       1.3204326 *  0.0000000    1.4671055 *  2.4617280 *  2.0959785 *
   3 C       2.4617280 *  1.4671055 *  0.0000000    1.3204326 *  2.7230540 *
   4 C       3.6680915    2.4617280 *  1.3204326 *  0.0000000    4.0379356  
   5 H       1.0744642 *  2.0959785 *  2.7230540 *  4.0379356    0.0000000  
   6 H       1.0724290 *  2.0938157 *  3.4416609    4.5530471    1.8251294 *
   7 H       2.0778447 *  1.0756565 *  2.1677482 *  2.6814136 *  3.0458644  
   8 H       2.6814136 *  2.1677482 *  1.0756565 *  2.0778447 *  2.4969240 *
   9 H       4.0379356    2.7230540 *  2.0959785 *  1.0744642 *  4.6329148  
  10 H       4.5530471    3.4416609    2.0938157 *  1.0724290 *  4.7490786  

                6 H          7 H          8 H          9 H         10 H     

   1 C       1.0724290 *  2.0778447 *  2.6814136 *  4.0379356    4.5530471  
   2 C       2.0938157 *  1.0756565 *  2.1677482 *  2.7230540 *  3.4416609  
   3 C       3.4416609    2.1677482 *  1.0756565 *  2.0959785 *  2.0938157 *
   4 C       4.5530471    2.6814136 *  2.0778447 *  1.0744642 *  1.0724290 *
   5 H       1.8251294 *  3.0458644    2.4969240 *  4.6329148    4.7490786  
   6 H       0.0000000    2.4213991 *  3.7509587    4.7490786    5.5050694  
   7 H       2.4213991 *  0.0000000    3.0919152    2.4969240 *  3.7509587  
   8 H       3.7509587    3.0919152    0.0000000    3.0458644    2.4213991 *
   9 H       4.7490786    2.4969240 *  3.0458644    0.0000000    1.8251294 *
  10 H       5.5050694    3.7509587    2.4213991 *  1.8251294 *  0.0000000  

  * ... LESS THAN  3.000

 ...... END OF ONE-ELECTRON INTEGRALS ......
 STEP CPU TIME =     0.01 TOTAL CPU TIME =          1.6 (      0.0 MIN)
 TOTAL WALL CLOCK TIME=          1.6 SECONDS, CPU UTILIZATION IS    97.50%
  ...... END OF TWO-ELECTRON INTEGRALS .....
 STEP CPU TIME =     0.00 TOTAL CPU TIME =          1.6 (      0.0 MIN)
 TOTAL WALL CLOCK TIME=          1.6 SECONDS, CPU UTILIZATION IS    97.50%

          --------------------------
                 RHF SCF CALCULATION
          --------------------------
     DENSITY MATRIX CONV=  2.00E-05

 DIRECT SCF CALCULATION, SCHWRZ=T   FDIFF=T,  DIRTHR=  0.00E+00 NITDIR=10

                                                                                   NONZERO     BLOCKS
 ITER EX DEM     TOTAL ENERGY        E CHANGE  DENSITY CHANGE     ORB. GRAD      INTEGRALS    SKIPPED
          ---------------START SECOND ORDER SCF---------------
   1  0  0     -154.0594560218  -154.0594560218   0.000182794   0.000149906         375552       7818
   2  1  0     -154.0594563785    -0.0000003566   0.000086626   0.000035490         345290      14511
   3  2  0     -154.0594564079    -0.0000000294   0.000019948   0.000009784         337973      15767
   4  3  0     -154.0594564093    -0.0000000014   0.000005023   0.000004161         326304      17935

          -----------------
          DENSITY CONVERGED
          -----------------
     TIME TO FORM FOCK OPERATORS=       0.1 SECONDS (       0.0 SEC/ITER)
     FOCK TIME ON FIRST ITERATION=       0.0, LAST ITERATION=       0.0
     TIME TO SOLVE SCF EQUATIONS=       0.0 SECONDS (       0.0 SEC/ITER)

 FINAL RHF ENERGY IS     -154.0594564093 AFTER   4 ITERATIONS
 ...... END OF RHF CALCULATION ......
 STEP CPU TIME =     0.09 TOTAL CPU TIME =          1.6 (      0.0 MIN)
 TOTAL WALL CLOCK TIME=          1.7 SECONDS, CPU UTILIZATION IS    97.63%
 ..... END OF 1-ELECTRON GRADIENT ......
 STEP CPU TIME =     0.00 TOTAL CPU TIME =          1.6 (      0.0 MIN)
 TOTAL WALL CLOCK TIME=          1.7 SECONDS, CPU UTILIZATION IS    97.06%
 ...... END OF 2-ELECTRON GRADIENT ......
 STEP CPU TIME =     0.04 TOTAL CPU TIME =          1.7 (      0.0 MIN)
 TOTAL WALL CLOCK TIME=          1.7 SECONDS, CPU UTILIZATION IS    97.13%

          NSERCH=  7     ENERGY=    -154.0594564

                                 -----------------------
                                 GRADIENT (HARTREE/BOHR)
                                 -----------------------
        ATOM     ZNUC       DE/DX         DE/DY         DE/DZ
 --------------------------------------------------------------
    1  C            6.0    -0.0000747     0.0000862     0.0000000
    2  C            6.0    -0.0000511    -0.0000267     0.0000000
    3  C            6.0     0.0000511     0.0000267     0.0000000
    4  C            6.0     0.0000747    -0.0000862     0.0000000
    5  H            1.0     0.0000390     0.0000491     0.0000000
    6  H            1.0     0.0000635    -0.0000764     0.0000000
    7  H            1.0     0.0000401     0.0000023     0.0000000
    8  H            1.0    -0.0000401    -0.0000023     0.0000000
    9  H            1.0    -0.0000390    -0.0000491     0.0000000
   10  H            1.0    -0.0000635     0.0000764     0.0000000


                     --------------------
                     INTERNAL COORDINATES
                     --------------------

                 - - ATOMS - -         COORDINATE        GRADIENT
 NO.   TYPE    I  J  K  L  M  N         (ANG,DEG)     (H/B,H/RAD)
 ----------------------------------------------------------------
   1 STRETCH   2  1                     1.3204326      -0.0000035
   2 STRETCH   3  2                     1.4671055      -0.0000330
   3 BEND      3  2  1                123.9573995       0.0000263
   4 STRETCH   4  3                     1.3204326      -0.0000035
   5 BEND      4  3  2                123.9573995       0.0000263
   6 TORSION   4  3  2  1             180.0000000       0.0000000
   7 STRETCH   5  1                     1.0744642       0.0000420
   8 BEND      5  1  2                121.7967942       0.0001065
   9 TORSION   5  1  2  3               0.0000000       0.0000000
  10 STRETCH   6  1                     1.0724290      -0.0000067
  11 BEND      6  1  5                116.4506783       0.0002010
  12 TORSION   6  1  5  2             180.0000000      -0.0000000
  13 STRETCH   7  2                     1.0756565       0.0000030
  14 BEND      7  2  1                119.9191599       0.0000814
  15 TORSION   7  2  1  3             180.0000000       0.0000000
  16 STRETCH   8  3                     1.0756565       0.0000030
  17 BEND      8  3  4                119.9191599       0.0000814
  18 TORSION   8  3  4  2             180.0000000      -0.0000000
  19 STRETCH   9  4                     1.0744642       0.0000420
  20 BEND      9  4  3                121.7967942       0.0001065
  21 TORSION   9  4  3  7               0.0000000      -0.0000000
  22 STRETCH  10  4                     1.0724290      -0.0000067
  23 BEND     10  4  9                116.4506783       0.0002010
  24 TORSION  10  4  9  3             180.0000000       0.0000000

 NOTE: CARTESIAN GRADIENTS ARE ALWAYS TAKEN TO TEST CONVERGENCE,
       SO THE FOLLOWING GRADIENTS ARE CARTESIAN.

          MAXIMUM GRADIENT = 0.0000859    RMS GRADIENT = 0.0000460

 NSERCH:   7  E=     -154.0594564093  GRAD. MAX=  0.0000859  R.M.S.=  0.0000460

          HESSIAN UPDATED USING THE BFGS FORMULA
             ACTUAL ENERGY CHANGE WAS  -0.0000003667
          PREDICTED ENERGY CHANGE WAS  -0.0000005113 RATIO=  0.717
          MIN SEARCH, CORRECT HESSIAN, TRYING PURE NR STEP
               NR STEP HAS LENGTH         =   0.001279
          RADIUS OF STEP TAKEN=   0.00128  CURRENT TRUST RADIUS=   0.05000
          TRANSFORMING DISPLACEMENT FROM INTERNALS TO CARTESIANS
          THE ROOT MEAN SQUARE ERROR IN ITERATION   1 IS   0.00000060
          THE ROOT MEAN SQUARE ERROR IN ITERATION   2 IS   0.00000000

 BEGINNING GEOMETRY SEARCH POINT NSERCH=   8 ...

 COORDINATES OF ALL ATOMS ARE (ANGS)
   ATOM   CHARGE       X              Y              Z
 ------------------------------------------------------------
 C           6.0  -1.8315147099   0.0955268947   0.0000000000
 C           6.0  -0.6104014945  -0.4068198729   0.0000000000
 C           6.0   0.6104014945   0.4068198729  -0.0000000000
 C           6.0   1.8315147099  -0.0955268947   0.0000000000
 H           1.0  -2.0077155939   1.1554304299   0.0000000000
 H           1.0  -2.7009344743  -0.5324515299  -0.0000000000
 H           1.0  -0.4691968027  -1.4731766379   0.0000000000
 H           1.0   0.4691968027   1.4731766379  -0.0000000000
 H           1.0   2.0077155939  -1.1554304299  -0.0000000000
 H           1.0   2.7009344743   0.5324515299   0.0000000000


                     --------------------
                     INTERNAL COORDINATES
                     --------------------

                 - - ATOMS - -         COORDINATE      COORDINATE
 NO.   TYPE    I  J  K  L  M  N        (BOHR,RAD)       (ANG,DEG)
 ----------------------------------------------------------------
   1 STRETCH   2  1                     2.4952039       1.3204051
   2 STRETCH   3  2                     2.7724087       1.4670956
   3 BEND      3  2  1                  2.1634382     123.9558759
   4 STRETCH   4  3                     2.4952039       1.3204051
   5 BEND      4  3  2                  2.1634382     123.9558759
   6 TORSION   4  3  2  1               3.1415927     180.0000000
   7 STRETCH   5  1                     2.0304156       1.0744497
   8 BEND      5  1  2                  2.1258139     121.8001628
   9 TORSION   5  1  2  3               0.0000000       0.0000000
  10 STRETCH   6  1                     2.0267235       1.0724960
  11 BEND      6  1  5                  2.0315940     116.4017636
  12 TORSION   6  1  5  2               3.1415927     180.0000000
  13 STRETCH   7  2                     2.0327124       1.0756652
  14 BEND      7  2  1                  2.0927300     119.9045963
  15 TORSION   7  2  1  3               3.1415927     180.0000000
  16 STRETCH   8  3                     2.0327124       1.0756652
  17 BEND      8  3  4                  2.0927300     119.9045963
  18 TORSION   8  3  4  2               3.1415927     180.0000000
  19 STRETCH   9  4                     2.0304156       1.0744497
  20 BEND      9  4  3                  2.1258139     121.8001628
  21 TORSION   9  4  3  7               0.0000000       0.0000000
  22 STRETCH  10  4                     2.0267235       1.0724960
  23 BEND     10  4  9                  2.0315940     116.4017636
  24 TORSION  10  4  9  3               3.1415927     180.0000000

          INTERNUCLEAR DISTANCES (ANGS.)
          ------------------------------

                1 C          2 C          3 C          4 C          5 H     

   1 C       0.0000000    1.3204051 *  2.4616779 *  3.6680085    1.0744497 *
   2 C       1.3204051 *  0.0000000    1.4670956 *  2.4616779 *  2.0959754 *
   3 C       2.4616779 *  1.4670956 *  0.0000000    1.3204051 *  2.7230415 *
   4 C       3.6680085    2.4616779 *  1.3204051 *  0.0000000    4.0378935  
   5 H       1.0744497 *  2.0959754 *  2.7230415 *  4.0378935    0.0000000  
   6 H       1.0724960 *  2.0943045 *  3.4419728    4.5534601    1.8246912 *
   7 H       2.0776768 *  1.0756652 *  2.1679297 *  2.6816398 *  3.0457536  
   8 H       2.6816398 *  2.1679297 *  1.0756652 *  2.0776768 *  2.4972100 *
   9 H       4.0378935    2.7230415 *  2.0959754 *  1.0744497 *  4.6329003  
  10 H       4.5534601    3.4419728    2.0943045 *  1.0724960 *  4.7496830  

                6 H          7 H          8 H          9 H         10 H     

   1 C       1.0724960 *  2.0776768 *  2.6816398 *  4.0378935    4.5534601  
   2 C       2.0943045 *  1.0756652 *  2.1679297 *  2.7230415 *  3.4419728  
   3 C       3.4419728    2.1679297 *  1.0756652 *  2.0959754 *  2.0943045 *
   4 C       4.5534601    2.6816398 *  2.0776768 *  1.0744497 *  1.0724960 *
   5 H       1.8246912 *  3.0457536    2.4972100 *  4.6329003    4.7496830  
   6 H       0.0000000    2.4219035 *  3.7513033    4.7496830    5.5058339  
   7 H       2.4219035 *  0.0000000    3.0921805    2.4972100 *  3.7513033  
   8 H       3.7513033    3.0921805    0.0000000    3.0457536    2.4219035 *
   9 H       4.7496830    2.4972100 *  3.0457536    0.0000000    1.8246912 *
  10 H       5.5058339    3.7513033    2.4219035 *  1.8246912 *  0.0000000  

  * ... LESS THAN  3.000

 ...... END OF ONE-ELECTRON INTEGRALS ......
 STEP CPU TIME =     0.00 TOTAL CPU TIME =          1.7 (      0.0 MIN)
 TOTAL WALL CLOCK TIME=          1.7 SECONDS, CPU UTILIZATION IS    97.13%
  ...... END OF TWO-ELECTRON INTEGRALS .....
 STEP CPU TIME =     0.00 TOTAL CPU TIME =          1.7 (      0.0 MIN)
 TOTAL WALL CLOCK TIME=          1.7 SECONDS, CPU UTILIZATION IS    97.13%

          --------------------------
                 RHF SCF CALCULATION
          --------------------------
     DENSITY MATRIX CONV=  2.00E-05

 DIRECT SCF CALCULATION, SCHWRZ=T   FDIFF=T,  DIRTHR=  0.00E+00 NITDIR=10

                                                                                   NONZERO     BLOCKS
 ITER EX DEM     TOTAL ENERGY        E CHANGE  DENSITY CHANGE     ORB. GRAD      INTEGRALS    SKIPPED
          ---------------START SECOND ORDER SCF---------------
   1  0  0     -154.0594565167  -154.0594565167   0.000066110   0.000051040         375544       7818
   2  1  0     -154.0594565651    -0.0000000483   0.000036747   0.000015016         338210      15642
   3  2  0     -154.0594565685    -0.0000000034   0.000005044   0.000003214         330685      17167
   4  3  0     -154.0594565686    -0.0000000001   0.000001631   0.000001137         313016      19772

          -----------------
          DENSITY CONVERGED
          -----------------
     TIME TO FORM FOCK OPERATORS=       0.1 SECONDS (       0.0 SEC/ITER)
     FOCK TIME ON FIRST ITERATION=       0.0, LAST ITERATION=       0.0
     TIME TO SOLVE SCF EQUATIONS=       0.0 SECONDS (       0.0 SEC/ITER)

 FINAL RHF ENERGY IS     -154.0594565686 AFTER   4 ITERATIONS
 ...... END OF RHF CALCULATION ......
 STEP CPU TIME =     0.08 TOTAL CPU TIME =          1.8 (      0.0 MIN)
 TOTAL WALL CLOCK TIME=          1.8 SECONDS, CPU UTILIZATION IS    97.25%
 ..... END OF 1-ELECTRON GRADIENT ......
 STEP CPU TIME =     0.01 TOTAL CPU TIME =          1.8 (      0.0 MIN)
 TOTAL WALL CLOCK TIME=          1.8 SECONDS, CPU UTILIZATION IS    97.27%
 ...... END OF 2-ELECTRON GRADIENT ......
 STEP CPU TIME =     0.04 TOTAL CPU TIME =          1.8 (      0.0 MIN)
 TOTAL WALL CLOCK TIME=          1.9 SECONDS, CPU UTILIZATION IS    97.85%

          NSERCH=  8     ENERGY=    -154.0594566

                                 -----------------------
                                 GRADIENT (HARTREE/BOHR)
                                 -----------------------
        ATOM     ZNUC       DE/DX         DE/DY         DE/DZ
 --------------------------------------------------------------
    1  C            6.0     0.0000626    -0.0000079     0.0000000
    2  C            6.0     0.0000087     0.0000217     0.0000000
    3  C            6.0    -0.0000087    -0.0000217     0.0000000
    4  C            6.0    -0.0000626     0.0000079     0.0000000
    5  H            1.0    -0.0000057     0.0000132     0.0000000
    6  H            1.0    -0.0000426    -0.0000167     0.0000000
    7  H            1.0    -0.0000040    -0.0000100     0.0000000
    8  H            1.0     0.0000040     0.0000100     0.0000000
    9  H            1.0     0.0000057    -0.0000132     0.0000000
   10  H            1.0     0.0000426     0.0000167     0.0000000


                     --------------------
                     INTERNAL COORDINATES
                     --------------------

                 - - ATOMS - -         COORDINATE        GRADIENT
 NO.   TYPE    I  J  K  L  M  N         (ANG,DEG)     (H/B,H/RAD)
 ----------------------------------------------------------------
   1 STRETCH   2  1                     1.3204051      -0.0000175
   2 STRETCH   3  2                     1.4670956      -0.0000159
   3 BEND      3  2  1                123.9558759      -0.0000142
   4 STRETCH   4  3                     1.3204051      -0.0000175
   5 BEND      4  3  2                123.9558759      -0.0000142
   6 TORSION   4  3  2  1             180.0000000       0.0000000
   7 STRETCH   5  1                     1.0744497       0.0000140
   8 BEND      5  1  2                121.8001628      -0.0000162
   9 TORSION   5  1  2  3               0.0000000       0.0000000
  10 STRETCH   6  1                     1.0724960       0.0000443
  11 BEND      6  1  5                116.4017636      -0.0000232
  12 TORSION   6  1  5  2             180.0000000      -0.0000000
  13 STRETCH   7  2                     1.0756652       0.0000094
  14 BEND      7  2  1                119.9045963      -0.0000108
  15 TORSION   7  2  1  3             180.0000000       0.0000000
  16 STRETCH   8  3                     1.0756652       0.0000094
  17 BEND      8  3  4                119.9045963      -0.0000108
  18 TORSION   8  3  4  2             180.0000000      -0.0000000
  19 STRETCH   9  4                     1.0744497       0.0000140
  20 BEND      9  4  3                121.8001628      -0.0000162
  21 TORSION   9  4  3  7               0.0000000      -0.0000000
  22 STRETCH  10  4                     1.0724960       0.0000443
  23 BEND     10  4  9                116.4017636      -0.0000232
  24 TORSION  10  4  9  3             180.0000000      -0.0000000

 NOTE: CARTESIAN GRADIENTS ARE ALWAYS TAKEN TO TEST CONVERGENCE,
       SO THE FOLLOWING GRADIENTS ARE CARTESIAN.

          MAXIMUM GRADIENT = 0.0000626    RMS GRADIENT = 0.0000215

 NSERCH:   8  E=     -154.0594565686  GRAD. MAX=  0.0000626  R.M.S.=  0.0000215


      ***** EQUILIBRIUM GEOMETRY LOCATED *****
 COORDINATES OF ALL ATOMS ARE (ANGS)
   ATOM   CHARGE       X              Y              Z
 ------------------------------------------------------------
 C           6.0  -1.8315147099   0.0955268947   0.0000000000
 C           6.0  -0.6104014945  -0.4068198729   0.0000000000
 C           6.0   0.6104014945   0.4068198729  -0.0000000000
 C           6.0   1.8315147099  -0.0955268947   0.0000000000
 H           1.0  -2.0077155939   1.1554304299   0.0000000000
 H           1.0  -2.7009344743  -0.5324515299  -0.0000000000
 H           1.0  -0.4691968027  -1.4731766379   0.0000000000
 H           1.0   0.4691968027   1.4731766379  -0.0000000000
 H           1.0   2.0077155939  -1.1554304299  -0.0000000000
 H           1.0   2.7009344743   0.5324515299   0.0000000000


                     --------------------
                     INTERNAL COORDINATES
                     --------------------

                 - - ATOMS - -         COORDINATE      COORDINATE
 NO.   TYPE    I  J  K  L  M  N        (BOHR,RAD)       (ANG,DEG)
 ----------------------------------------------------------------
   1 STRETCH   2  1                     2.4952039       1.3204051
   2 STRETCH   3  2                     2.7724087       1.4670956
   3 BEND      3  2  1                  2.1634382     123.9558759
   4 STRETCH   4  3                     2.4952039       1.3204051
   5 BEND      4  3  2                  2.1634382     123.9558759
   6 TORSION   4  3  2  1               3.1415927     180.0000000
   7 STRETCH   5  1                     2.0304156       1.0744497
   8 BEND      5  1  2                  2.1258139     121.8001628
   9 TORSION   5  1  2  3               0.0000000       0.0000000
  10 STRETCH   6  1                     2.0267235       1.0724960
  11 BEND      6  1  5                  2.0315940     116.4017636
  12 TORSION   6  1  5  2               3.1415927     180.0000000
  13 STRETCH   7  2                     2.0327124       1.0756652
  14 BEND      7  2  1                  2.0927300     119.9045963
  15 TORSION   7  2  1  3               3.1415927     180.0000000
  16 STRETCH   8  3                     2.0327124       1.0756652
  17 BEND      8  3  4                  2.0927300     119.9045963
  18 TORSION   8  3  4  2               3.1415927     180.0000000
  19 STRETCH   9  4                     2.0304156       1.0744497
  20 BEND      9  4  3                  2.1258139     121.8001628
  21 TORSION   9  4  3  7               0.0000000       0.0000000
  22 STRETCH  10  4                     2.0267235       1.0724960
  23 BEND     10  4  9                  2.0315940     116.4017636
  24 TORSION  10  4  9  3               3.1415927     180.0000000

          INTERNUCLEAR DISTANCES (ANGS.)
          ------------------------------

                1 C          2 C          3 C          4 C          5 H     

   1 C       0.0000000    1.3204051 *  2.4616779 *  3.6680085    1.0744497 *
   2 C       1.3204051 *  0.0000000    1.4670956 *  2.4616779 *  2.0959754 *
   3 C       2.4616779 *  1.4670956 *  0.0000000    1.3204051 *  2.7230415 *
   4 C       3.6680085    2.4616779 *  1.3204051 *  0.0000000    4.0378935  
   5 H       1.0744497 *  2.0959754 *  2.7230415 *  4.0378935    0.0000000  
   6 H       1.0724960 *  2.0943045 *  3.4419728    4.5534601    1.8246912 *
   7 H       2.0776768 *  1.0756652 *  2.1679297 *  2.6816398 *  3.0457536  
   8 H       2.6816398 *  2.1679297 *  1.0756652 *  2.0776768 *  2.4972100 *
   9 H       4.0378935    2.7230415 *  2.0959754 *  1.0744497 *  4.6329003  
  10 H       4.5534601    3.4419728    2.0943045 *  1.0724960 *  4.7496830  

                6 H          7 H          8 H          9 H         10 H     

   1 C       1.0724960 *  2.0776768 *  2.6816398 *  4.0378935    4.5534601  
   2 C       2.0943045 *  1.0756652 *  2.1679297 *  2.7230415 *  3.4419728  
   3 C       3.4419728    2.1679297 *  1.0756652 *  2.0959754 *  2.0943045 *
   4 C       4.5534601    2.6816398 *  2.0776768 *  1.0744497 *  1.0724960 *
   5 H       1.8246912 *  3.0457536    2.4972100 *  4.6329003    4.7496830  
   6 H       0.0000000    2.4219035 *  3.7513033    4.7496830    5.5058339  
   7 H       2.4219035 *  0.0000000    3.0921805    2.4972100 *  3.7513033  
   8 H       3.7513033    3.0921805    0.0000000    3.0457536    2.4219035 *
   9 H       4.7496830    2.4972100 *  3.0457536    0.0000000    1.8246912 *
  10 H       5.5058339    3.7513033    2.4219035 *  1.8246912 *  0.0000000  

  * ... LESS THAN  3.000


          NUCLEAR ENERGY    =      104.4802181898
          ELECTRONIC ENERGY =     -258.5396747585
          TOTAL ENERGY      =     -154.0594565686

          ------------------
          MOLECULAR ORBITALS
          ------------------

                      1          2          3          4          5
                  -11.1786   -11.1781   -11.1664   -11.1663    -1.0934
                     A          A          A          A          A   
    1  C  1  S   -0.009008   0.001366  -0.697780  -0.697692   0.096079
    2  C  1  S    0.001647   0.003545  -0.068891  -0.067879  -0.108577
    3  C  1  X    0.001096   0.001731  -0.000368  -0.000082  -0.074465
    4  C  1  Y   -0.000406  -0.000445  -0.000028   0.000137   0.022249
    5  C  1  Z    0.000000   0.000000   0.000000   0.000000   0.000000
    6  C  1  S   -0.018120  -0.024866   0.053522   0.047334  -0.175180
    7  C  1  X   -0.010697  -0.012719   0.008469   0.003252   0.005141
    8  C  1  Y   -0.001608   0.002587  -0.002049  -0.002432   0.004873
    9  C  1  Z    0.000000   0.000000   0.000000   0.000000   0.000000
   10  C  2  S   -0.698106  -0.697822   0.009367  -0.000981   0.140860
   11  C  2  S   -0.071526  -0.067981   0.003565   0.002989  -0.154475
   12  C  2  X   -0.000292   0.000819  -0.002424  -0.001163   0.007108
   13  C  2  Y   -0.001023  -0.000506   0.000897   0.000671  -0.046725
   14  C  2  Z    0.000000   0.000000   0.000000   0.000000   0.000000
   15  C  2  S    0.072818   0.044274  -0.021516  -0.016746  -0.297766
   16  C  2  X    0.008987  -0.013793   0.012010   0.007743   0.014190
   17  C  2  Y    0.013826   0.007599  -0.005018  -0.002743  -0.026705
   18  C  2  Z    0.000000   0.000000   0.000000   0.000000   0.000000
   19  C  3  S    0.698106  -0.697822  -0.009367  -0.000981   0.140860
   20  C  3  S    0.071526  -0.067981  -0.003565   0.002989  -0.154475
   21  C  3  X   -0.000292  -0.000819  -0.002424   0.001163  -0.007108
   22  C  3  Y   -0.001023   0.000506   0.000897  -0.000671   0.046725
   23  C  3  Z    0.000000   0.000000   0.000000   0.000000   0.000000
   24  C  3  S   -0.072818   0.044274   0.021516  -0.016746  -0.297766
   25  C  3  X    0.008987   0.013793   0.012010  -0.007743  -0.014190
   26  C  3  Y    0.013826  -0.007599  -0.005018   0.002743   0.026705
   27  C  3  Z    0.000000   0.000000   0.000000   0.000000   0.000000
   28  C  4  S    0.009008   0.001366   0.697781  -0.697692   0.096079
   29  C  4  S   -0.001647   0.003545   0.068891  -0.067879  -0.108577
   30  C  4  X    0.001096  -0.001731  -0.000368   0.000082   0.074465
   31  C  4  Y   -0.000406   0.000445  -0.000028  -0.000137  -0.022249
   32  C  4  Z    0.000000   0.000000   0.000000   0.000000   0.000000
   33  C  4  S    0.018120  -0.024866  -0.053522   0.047334  -0.175180
   34  C  4  X   -0.010697   0.012719   0.008469  -0.003252  -0.005141
   35  C  4  Y   -0.001608  -0.002587  -0.002049   0.002432  -0.004873
   36  C  4  Z    0.000000   0.000000   0.000000   0.000000   0.000000
   37  H  5  S    0.001368   0.001040   0.000656   0.001292  -0.043657
   38  H  5  S    0.001476   0.000863  -0.008686  -0.008939  -0.003703
   39  H  6  S    0.000108   0.000677   0.001075   0.001002  -0.038418
   40  H  6  S   -0.001766  -0.001906  -0.007901  -0.009568   0.007105
   41  H  7  S    0.000431   0.002254   0.000554   0.000862  -0.064433
   42  H  7  S   -0.006756  -0.005606  -0.001030  -0.000139  -0.009634
   43  H  8  S   -0.000431   0.002254  -0.000554   0.000862  -0.064433
   44  H  8  S    0.006756  -0.005606   0.001030  -0.000139  -0.009634
   45  H  9  S   -0.001368   0.001040  -0.000656   0.001292  -0.043657
   46  H  9  S   -0.001476   0.000863   0.008686  -0.008939  -0.003703
   47  H 10  S   -0.000108   0.000677  -0.001075   0.001002  -0.038418
   48  H 10  S    0.001766  -0.001906   0.007901  -0.009568   0.007105

                      6          7          8          9         10
                   -1.0073    -0.8219    -0.7558    -0.6497    -0.6402
                     A          A          A          A          A   
    1  C  1  S   -0.134679  -0.114335   0.052315  -0.023389   0.008505
    2  C  1  S    0.145633   0.118218  -0.052125   0.016265  -0.006754
    3  C  1  X    0.066766  -0.077102   0.070334  -0.256738   0.007201
    4  C  1  Y   -0.032569   0.004489  -0.110046  -0.018753  -0.224539
    5  C  1  Z    0.000000   0.000000   0.000000   0.000000   0.000000
    6  C  1  S    0.317805   0.356969  -0.183442   0.121916  -0.035893
    7  C  1  X    0.014534  -0.029309   0.024930  -0.148182   0.001526
    8  C  1  Y   -0.012141   0.002922  -0.061047  -0.021513  -0.155049
    9  C  1  Z    0.000000   0.000000   0.000000   0.000000   0.000000
   10  C  2  S   -0.092960   0.077882  -0.088343   0.035212  -0.009284
   11  C  2  S    0.100068  -0.080737   0.090884  -0.039273   0.009052
   12  C  2  X   -0.130026  -0.156805  -0.002824   0.135025  -0.154061
   13  C  2  Y    0.021907  -0.011669  -0.156744  -0.148374  -0.156734
   14  C  2  Z    0.000000   0.000000   0.000000   0.000000   0.000000
   15  C  2  S    0.226940  -0.244647   0.306604  -0.119465   0.034312
   16  C  2  X   -0.009486  -0.054629   0.008254   0.060980  -0.079767
   17  C  2  Y    0.014274  -0.010286  -0.090227  -0.109564  -0.116230
   18  C  2  Z    0.000000   0.000000   0.000000   0.000000   0.000000
   19  C  3  S    0.092960   0.077882   0.088343  -0.035212  -0.009284
   20  C  3  S   -0.100068  -0.080737  -0.090884   0.039273   0.009052
   21  C  3  X   -0.130026   0.156805  -0.002824   0.135025   0.154061
   22  C  3  Y    0.021907   0.011669  -0.156744  -0.148374   0.156734
   23  C  3  Z    0.000000   0.000000   0.000000   0.000000   0.000000
   24  C  3  S   -0.226940  -0.244647  -0.306604   0.119465   0.034312
   25  C  3  X   -0.009486   0.054629   0.008254   0.060980   0.079767
   26  C  3  Y    0.014274   0.010286  -0.090227  -0.109564   0.116230
   27  C  3  Z    0.000000   0.000000   0.000000   0.000000   0.000000
   28  C  4  S    0.134679  -0.114335  -0.052315   0.023389   0.008505
   29  C  4  S   -0.145633   0.118218   0.052125  -0.016265  -0.006754
   30  C  4  X    0.066766   0.077102   0.070334  -0.256738  -0.007201
   31  C  4  Y   -0.032569  -0.004489  -0.110046  -0.018753   0.224539
   32  C  4  Z    0.000000   0.000000   0.000000   0.000000   0.000000
   33  C  4  S   -0.317805   0.356969   0.183442  -0.121916  -0.035893
   34  C  4  X    0.014534   0.029309   0.024930  -0.148182  -0.001526
   35  C  4  Y   -0.012141  -0.002922  -0.061047  -0.021513   0.155049
   36  C  4  Z    0.000000   0.000000   0.000000   0.000000   0.000000
   37  H  5  S    0.065998   0.093643  -0.108355   0.033499  -0.146342
   38  H  5  S    0.008851   0.035906  -0.065896   0.025648  -0.107423
   39  H  6  S    0.068543   0.115049  -0.039463   0.157155   0.070542
   40  H  6  S    0.008415   0.052687  -0.021439   0.119369   0.052592
   41  H  7  S    0.040850  -0.062459   0.156510   0.069349   0.088820
   42  H  7  S    0.003156  -0.023321   0.084686   0.051897   0.056730
   43  H  8  S   -0.040850  -0.062459  -0.156510  -0.069349   0.088820
   44  H  8  S   -0.003156  -0.023321  -0.084686  -0.051897   0.056730
   45  H  9  S   -0.065998   0.093643   0.108355  -0.033499  -0.146342
   46  H  9  S   -0.008851   0.035906   0.065896  -0.025648  -0.107423
   47  H 10  S   -0.068543   0.115049   0.039463  -0.157155   0.070542
   48  H 10  S   -0.008415   0.052687   0.021439  -0.119369   0.052592

                     11         12         13         14         15
                   -0.5618    -0.5425    -0.4847    -0.4480    -0.3251
                     A          A          A          A          A   
    1  C  1  S   -0.019712   0.004628   0.002267   0.000000   0.000000
    2  C  1  S    0.031025  -0.008658  -0.004647   0.000000   0.000000
    3  C  1  X    0.263885   0.012955   0.069764   0.000000   0.000000
    4  C  1  Y   -0.038459   0.247503   0.143835   0.000000   0.000000
    5  C  1  Z    0.000000   0.000000   0.000000   0.191460  -0.261864
    6  C  1  S   -0.004350  -0.003089   0.023677   0.000000   0.000000
    7  C  1  X    0.151468   0.034906   0.106067   0.000000   0.000000
    8  C  1  Y   -0.006078   0.229602   0.159888   0.000000   0.000000
    9  C  1  Z    0.000000   0.000000   0.000000   0.203642  -0.327231
   10  C  2  S    0.000352  -0.021975   0.017556   0.000000   0.000000
   11  C  2  S    0.006996   0.019928  -0.019281   0.000000   0.000000
   12  C  2  X   -0.238808   0.086437  -0.132993   0.000000   0.000000
   13  C  2  Y    0.125815  -0.104688  -0.220182   0.000000   0.000000
   14  C  2  Z    0.000000   0.000000   0.000000   0.253832  -0.200790
   15  C  2  S   -0.019327   0.080848  -0.056307   0.000000   0.000000
   16  C  2  X   -0.180613   0.028251  -0.066256   0.000000   0.000000
   17  C  2  Y    0.121900  -0.122806  -0.247556   0.000000   0.000000
   18  C  2  Z    0.000000   0.000000   0.000000   0.261508  -0.251945
   19  C  3  S    0.000352   0.021975   0.017556   0.000000   0.000000
   20  C  3  S    0.006996  -0.019928  -0.019281   0.000000   0.000000
   21  C  3  X    0.238808   0.086437   0.132993   0.000000   0.000000
   22  C  3  Y   -0.125815  -0.104688   0.220182   0.000000   0.000000
   23  C  3  Z    0.000000   0.000000   0.000000   0.253832   0.200790
   24  C  3  S   -0.019327  -0.080848  -0.056307   0.000000   0.000000
   25  C  3  X    0.180613   0.028251   0.066256   0.000000   0.000000
   26  C  3  Y   -0.121900  -0.122806   0.247556   0.000000   0.000000
   27  C  3  Z    0.000000   0.000000   0.000000   0.261508   0.251945
   28  C  4  S   -0.019712  -0.004628   0.002267   0.000000   0.000000
   29  C  4  S    0.031025   0.008658  -0.004647   0.000000   0.000000
   30  C  4  X   -0.263885   0.012955  -0.069764   0.000000   0.000000
   31  C  4  Y    0.038459   0.247503  -0.143835   0.000000   0.000000
   32  C  4  Z    0.000000   0.000000   0.000000   0.191460   0.261864
   33  C  4  S   -0.004350   0.003089   0.023677   0.000000   0.000000
   34  C  4  X   -0.151468   0.034906  -0.106067   0.000000   0.000000
   35  C  4  Y    0.006078   0.229602  -0.159888   0.000000   0.000000
   36  C  4  Z    0.000000   0.000000   0.000000   0.203642   0.327231
   37  H  5  S   -0.038479   0.170919   0.112335   0.000000   0.000000
   38  H  5  S   -0.050593   0.139673   0.111753   0.000000   0.000000
   39  H  6  S   -0.113103  -0.121592  -0.121643   0.000000   0.000000
   40  H  6  S   -0.108183  -0.092928  -0.099980   0.000000   0.000000
   41  H  7  S   -0.110707   0.105010   0.149795   0.000000   0.000000
   42  H  7  S   -0.090019   0.072636   0.135927   0.000000   0.000000
   43  H  8  S   -0.110707  -0.105010   0.149795   0.000000   0.000000
   44  H  8  S   -0.090019  -0.072636   0.135927   0.000000   0.000000
   45  H  9  S   -0.038479  -0.170919   0.112335   0.000000   0.000000
   46  H  9  S   -0.050593  -0.139673   0.111753   0.000000   0.000000
   47  H 10  S   -0.113103   0.121592  -0.121643   0.000000   0.000000
   48  H 10  S   -0.108183   0.092928  -0.099980   0.000000   0.000000

                     16         17         18         19         20
                    0.1318     0.2705     0.2864     0.3000     0.3088
                     A          A          A          A          A   
    1  C  1  S    0.000000   0.000000   0.019165  -0.055190   0.103732
    2  C  1  S    0.000000   0.000000  -0.007088   0.017000  -0.044304
    3  C  1  X    0.000000   0.000000  -0.017788  -0.134763   0.083493
    4  C  1  Y    0.000000   0.000000  -0.145733   0.005877  -0.005790
    5  C  1  Z    0.253772  -0.156698   0.000000   0.000000   0.000000
    6  C  1  S    0.000000   0.000000  -0.238615   0.776739  -1.475750
    7  C  1  X    0.000000   0.000000   0.002766  -0.615149   0.463792
    8  C  1  Y    0.000000   0.000000  -0.508636   0.137225   0.028293
    9  C  1  Z    0.544309  -0.545139   0.000000   0.000000   0.000000
   10  C  2  S    0.000000   0.000000  -0.032136  -0.050664   0.011911
   11  C  2  S    0.000000   0.000000   0.015320   0.011418   0.011842
   12  C  2  X    0.000000   0.000000  -0.013837   0.022187  -0.029951
   13  C  2  Y    0.000000   0.000000  -0.154825  -0.122335   0.033203
   14  C  2  Z   -0.190302   0.276694   0.000000   0.000000   0.000000
   15  C  2  S    0.000000   0.000000   0.367921   0.921208  -0.431889
   16  C  2  X    0.000000   0.000000  -0.027256  -0.033928  -0.459224
   17  C  2  Y    0.000000   0.000000  -0.538177  -0.502771  -0.037482
   18  C  2  Z   -0.395399   0.779606   0.000000   0.000000   0.000000
   19  C  3  S    0.000000   0.000000   0.032136  -0.050664  -0.011911
   20  C  3  S    0.000000   0.000000  -0.015320   0.011418  -0.011842
   21  C  3  X    0.000000   0.000000  -0.013837  -0.022187  -0.029951
   22  C  3  Y    0.000000   0.000000  -0.154825   0.122335   0.033203
   23  C  3  Z   -0.190302  -0.276694   0.000000   0.000000   0.000000
   24  C  3  S    0.000000   0.000000  -0.367921   0.921208   0.431889
   25  C  3  X    0.000000   0.000000  -0.027256   0.033928  -0.459224
   26  C  3  Y    0.000000   0.000000  -0.538177   0.502771  -0.037482
   27  C  3  Z   -0.395399  -0.779606   0.000000   0.000000   0.000000
   28  C  4  S    0.000000   0.000000  -0.019165  -0.055190  -0.103732
   29  C  4  S    0.000000   0.000000   0.007088   0.017000   0.044304
   30  C  4  X    0.000000   0.000000  -0.017788   0.134763   0.083493
   31  C  4  Y    0.000000   0.000000  -0.145733  -0.005877  -0.005790
   32  C  4  Z    0.253772   0.156698   0.000000   0.000000   0.000000
   33  C  4  S    0.000000   0.000000   0.238615   0.776739   1.475750
   34  C  4  X    0.000000   0.000000   0.002766   0.615149   0.463792
   35  C  4  Y    0.000000   0.000000  -0.508636  -0.137225   0.028293
   36  C  4  Z    0.544309   0.545139   0.000000   0.000000   0.000000
   37  H  5  S    0.000000   0.000000   0.023605   0.016192   0.017150
   38  H  5  S    0.000000   0.000000   0.832209  -0.487104   0.743773
   39  H  6  S    0.000000   0.000000  -0.018520  -0.037730   0.022101
   40  H  6  S    0.000000   0.000000  -0.357665  -0.925694   1.079655
   41  H  7  S    0.000000   0.000000  -0.047617   0.015893   0.033341
   42  H  7  S    0.000000   0.000000  -1.008724  -0.869746   0.268719
   43  H  8  S    0.000000   0.000000   0.047617   0.015893  -0.033341
   44  H  8  S    0.000000   0.000000   1.008724  -0.869746  -0.268719
   45  H  9  S    0.000000   0.000000  -0.023605   0.016192  -0.017150
   46  H  9  S    0.000000   0.000000  -0.832209  -0.487104  -0.743773
   47  H 10  S    0.000000   0.000000   0.018520  -0.037730  -0.022101
   48  H 10  S    0.000000   0.000000   0.357665  -0.925694  -1.079655

                     21         22         23         24         25
                    0.3579     0.3757     0.4057     0.5588     0.5614
                     A          A          A          A          A   
    1  C  1  S    0.072859  -0.018702  -0.049609  -0.068973   0.061965
    2  C  1  S   -0.024201   0.011541   0.016234   0.007603   0.054054
    3  C  1  X    0.002881  -0.054659  -0.100240   0.060213   0.035869
    4  C  1  Y   -0.158407  -0.120156  -0.145835   0.094837   0.057658
    5  C  1  Z    0.000000   0.000000   0.000000   0.000000   0.000000
    6  C  1  S   -1.046457   0.117821   0.654066   1.150154  -2.432562
    7  C  1  X   -0.128792  -0.318106  -0.403902   1.461087  -1.978463
    8  C  1  Y   -0.721798  -0.719628  -0.941990   0.377516   0.675711
    9  C  1  Z    0.000000   0.000000   0.000000   0.000000   0.000000
   10  C  2  S   -0.046164   0.102108   0.048843   0.123430  -0.058016
   11  C  2  S    0.023723  -0.049839  -0.005511  -0.012833   0.005144
   12  C  2  X   -0.013005  -0.121025   0.056634   0.015266  -0.095757
   13  C  2  Y   -0.048944   0.026182   0.117047  -0.194929   0.137760
   14  C  2  Z    0.000000   0.000000   0.000000   0.000000   0.000000
   15  C  2  S    0.574393  -1.262358  -1.005585  -2.707042   2.045006
   16  C  2  X   -0.084280  -0.451482   0.120225  -0.416510  -2.055641
   17  C  2  Y   -0.098993   0.308531   0.857655  -1.485059   1.575236
   18  C  2  Z    0.000000   0.000000   0.000000   0.000000   0.000000
   19  C  3  S   -0.046164  -0.102108   0.048843  -0.123430  -0.058016
   20  C  3  S    0.023723   0.049839  -0.005511   0.012833   0.005144
   21  C  3  X    0.013005  -0.121025  -0.056634   0.015266   0.095757
   22  C  3  Y    0.048944   0.026182  -0.117047  -0.194929  -0.137760
   23  C  3  Z    0.000000   0.000000   0.000000   0.000000   0.000000
   24  C  3  S    0.574393   1.262358  -1.005585   2.707042   2.045006
   25  C  3  X    0.084280  -0.451482  -0.120225  -0.416510   2.055641
   26  C  3  Y    0.098993   0.308531  -0.857655  -1.485059  -1.575236
   27  C  3  Z    0.000000   0.000000   0.000000   0.000000   0.000000
   28  C  4  S    0.072859   0.018702  -0.049609   0.068973   0.061965
   29  C  4  S   -0.024201  -0.011541   0.016234  -0.007603   0.054054
   30  C  4  X   -0.002881  -0.054659   0.100240   0.060213  -0.035869
   31  C  4  Y    0.158407  -0.120156   0.145835   0.094837  -0.057658
   32  C  4  Z    0.000000   0.000000   0.000000   0.000000   0.000000
   33  C  4  S   -1.046457  -0.117821   0.654066  -1.150154  -2.432562
   34  C  4  X    0.128792  -0.318106   0.403902   1.461087   1.978463
   35  C  4  Y    0.721798  -0.719628   0.941990   0.377516  -0.675711
   36  C  4  Z    0.000000   0.000000   0.000000   0.000000   0.000000
   37  H  5  S    0.045215   0.032489  -0.039479   0.115966  -0.022531
   38  H  5  S    1.375854   0.664819   0.525161  -0.601604  -0.203911
   39  H  6  S   -0.015329  -0.034745   0.023265  -0.046077  -0.101859
   40  H  6  S   -0.158852  -0.915362  -1.273319   0.744129  -0.207138
   41  H  7  S   -0.054750   0.000382  -0.024679  -0.016313  -0.016488
   42  H  7  S   -0.549496   0.966532   1.122888  -0.480738   1.029847
   43  H  8  S   -0.054750  -0.000382  -0.024679   0.016313  -0.016488
   44  H  8  S   -0.549496  -0.966532   1.122888   0.480738   1.029847
   45  H  9  S    0.045215  -0.032489  -0.039479  -0.115966  -0.022531
   46  H  9  S    1.375854  -0.664819   0.525161   0.601604  -0.203911
   47  H 10  S   -0.015329   0.034745   0.023265   0.046077  -0.101859
   48  H 10  S   -0.158852   0.915362  -1.273319  -0.744129  -0.207138

     ----------------------------------------------------------------
     PROPERTY VALUES FOR THE RHF   SELF-CONSISTENT FIELD WAVEFUNCTION
     ----------------------------------------------------------------

          -----------------
          ENERGY COMPONENTS
          -----------------

         WAVEFUNCTION NORMALIZATION =       1.0000000000

                ONE ELECTRON ENERGY =    -413.0400185074
                TWO ELECTRON ENERGY =     154.5003437489
           NUCLEAR REPULSION ENERGY =     104.4802181898
                                      ------------------
                       TOTAL ENERGY =    -154.0594565686

 ELECTRON-ELECTRON POTENTIAL ENERGY =     154.5003437489
  NUCLEUS-ELECTRON POTENTIAL ENERGY =    -566.7844277240
   NUCLEUS-NUCLEUS POTENTIAL ENERGY =     104.4802181898
                                      ------------------
             TOTAL POTENTIAL ENERGY =    -307.8038657852
               TOTAL KINETIC ENERGY =     153.7444092166
                 VIRIAL RATIO (V/T) =       2.0020491630

  ...... PI ENERGY ANALYSIS ......

 ENERGY ANALYSIS:
            FOCK ENERGY=   -104.0393114367
          BARE H ENERGY=   -413.0400185074
     ELECTRONIC ENERGY =   -258.5396649720
         KINETIC ENERGY=    153.7444092166
          N-N REPULSION=    104.4802181898
           TOTAL ENERGY=   -154.0594467822
        SIGMA PART(1+2)=   -238.4980656654
               (K,V1,2)=    149.8119452427   -524.3149308590    136.0049199508
           PI PART(1+2)=    -20.0415993066
               (K,V1,2)=      3.9324639738    -42.4694968650     18.4954335845
  SIGMA SKELETON, ERROR=   -134.0178474756      0.0000000000
             MIXED PART= 0.00000E+00 0.00000E+00 0.00000E+00 0.00000E+00
 ...... END OF PI ENERGY ANALYSIS ......

          ---------------------------------------
          MULLIKEN AND LOWDIN POPULATION ANALYSES
          ---------------------------------------

     ATOMIC MULLIKEN POPULATION IN EACH MOLECULAR ORBITAL

                      1          2          3          4          5

                  2.000000   2.000000   2.000000   2.000000   2.000000

    1             0.003469   0.005288   0.992857   0.994282   0.295382
    2             0.995673   0.993891   0.004809   0.003138   0.650448
    3             0.995673   0.993891   0.004809   0.003138   0.650448
    4             0.003469   0.005288   0.992857   0.994281   0.295382
    5            -0.000028  -0.000019   0.001223   0.001236   0.014207
    6             0.000037   0.000037   0.001095   0.001341   0.005749
    7             0.000848   0.000804   0.000016   0.000003   0.034215
    8             0.000848   0.000804   0.000016   0.000003   0.034215
    9            -0.000028  -0.000019   0.001223   0.001236   0.014207
   10             0.000037   0.000037   0.001095   0.001341   0.005749

                      6          7          8          9         10

                  2.000000   2.000000   2.000000   2.000000   2.000000

    1             0.580072   0.441291   0.223473   0.458843   0.386241
    2             0.339206   0.335796   0.435483   0.265051   0.325414
    3             0.339206   0.335796   0.435483   0.265051   0.325414
    4             0.580072   0.441291   0.223473   0.458843   0.386241
    5             0.033234   0.073516   0.111484   0.010617   0.183014
    6             0.035800   0.118323   0.013638   0.221600   0.042510
    7             0.011688   0.031074   0.215922   0.043890   0.062820
    8             0.011688   0.031074   0.215922   0.043890   0.062820
    9             0.033234   0.073516   0.111484   0.010617   0.183014
   10             0.035800   0.118323   0.013638   0.221600   0.042510

                     11         12         13         14         15

                  2.000000   2.000000   2.000000   2.000000   2.000000

    1             0.367261   0.448697   0.198253   0.361049   0.655414
    2             0.391966   0.124612   0.397753   0.638951   0.344586
    3             0.391966   0.124612   0.397753   0.638951   0.344586
    4             0.367261   0.448697   0.198253   0.361049   0.655414
    5             0.019206   0.232974   0.108385   0.000000   0.000000
    6             0.117723   0.114123   0.111016   0.000000   0.000000
    7             0.103844   0.079594   0.184594   0.000000   0.000000
    8             0.103844   0.079594   0.184594   0.000000   0.000000
    9             0.019206   0.232974   0.108385   0.000000   0.000000
   10             0.117723   0.114123   0.111016   0.000000   0.000000

               ----- POPULATIONS IN EACH AO -----
                             MULLIKEN      LOWDIN
              1  C  1  S      1.98724     1.97763
              2  C  1  S      0.39724     0.42178
              3  C  1  X      0.62194     0.58908
              4  C  1  Y      0.57351     0.53661
              5  C  1  Z      0.40215     0.39585
              6  C  1  S      0.95020     0.56741
              7  C  1  X      0.33482     0.51210
              8  C  1  Y      0.53047     0.56723
              9  C  1  Z      0.61431     0.62558
             10  C  2  S      1.98795     1.97724
             11  C  2  S      0.39892     0.41774
             12  C  2  X      0.63121     0.60218
             13  C  2  Y      0.57698     0.54746
             14  C  2  Z      0.40055     0.38662
             15  C  2  S      0.91165     0.53899
             16  C  2  X      0.24010     0.48144
             17  C  2  Y      0.51643     0.55183
             18  C  2  Z      0.58298     0.59195
             19  C  3  S      1.98795     1.97724
             20  C  3  S      0.39892     0.41774
             21  C  3  X      0.63121     0.60218
             22  C  3  Y      0.57698     0.54746
             23  C  3  Z      0.40055     0.38662
             24  C  3  S      0.91165     0.53899
             25  C  3  X      0.24010     0.48144
             26  C  3  Y      0.51643     0.55183
             27  C  3  Z      0.58298     0.59195
             28  C  4  S      1.98724     1.97763
             29  C  4  S      0.39724     0.42178
             30  C  4  X      0.62194     0.58908
             31  C  4  Y      0.57351     0.53661
             32  C  4  Z      0.40215     0.39585
             33  C  4  S      0.95020     0.56741
             34  C  4  X      0.33482     0.51210
             35  C  4  Y      0.53047     0.56723
             36  C  4  Z      0.61431     0.62558
             37  H  5  S      0.47679     0.47087
             38  H  5  S      0.31226     0.43544
             39  H  6  S      0.47779     0.47126
             40  H  6  S      0.30520     0.43082
             41  H  7  S      0.47792     0.47800
             42  H  7  S      0.29139     0.42488
             43  H  8  S      0.47792     0.47800
             44  H  8  S      0.29139     0.42488
             45  H  9  S      0.47679     0.47087
             46  H  9  S      0.31226     0.43544
             47  H 10  S      0.47779     0.47126
             48  H 10  S      0.30520     0.43082

          ----- MULLIKEN ATOMIC OVERLAP POPULATIONS -----
          (OFF-DIAGONAL ELEMENTS NEED TO BE MULTIPLIED BY 2)

             1           2           3           4           5

    1    5.2068833
    2    0.5281882   5.2284676
    3   -0.0901721   0.3235079   5.2284676
    4    0.0017267  -0.0901721   0.5281882   5.2068833
    5    0.4011275  -0.0575986   0.0003663   0.0001151   0.4615270
    6    0.3959918  -0.0492586   0.0025481  -0.0000617  -0.0207217
    7   -0.0344210   0.4009065  -0.0401783   0.0024933   0.0020776
    8    0.0024933  -0.0401783   0.4009065  -0.0344210   0.0021493
    9    0.0001151   0.0003663  -0.0575986   0.4011275   0.0000059
   10   -0.0000617   0.0025481  -0.0492586   0.3959918  -0.0000013

             6           7           8           9          10

    6    0.4566329
    7   -0.0021408   0.4368898
    8    0.0000045   0.0015305   0.4368898
    9   -0.0000013   0.0021493   0.0020776   0.4615270
   10    0.0000004   0.0000045  -0.0021408  -0.0207217   0.4566329

          TOTAL MULLIKEN AND LOWDIN ATOMIC POPULATIONS
       ATOM         MULL.POP.    CHARGE          LOW.POP.     CHARGE
    1 C             6.411871   -0.411871         6.193277   -0.193277
    2 C             6.246777   -0.246777         6.095453   -0.095453
    3 C             6.246777   -0.246777         6.095453   -0.095453
    4 C             6.411871   -0.411871         6.193277   -0.193277
    5 H             0.789047    0.210953         0.906311    0.093689
    6 H             0.782994    0.217006         0.902080    0.097920
    7 H             0.769311    0.230689         0.902880    0.097120
    8 H             0.769311    0.230689         0.902880    0.097120
    9 H             0.789047    0.210953         0.906311    0.093689
   10 H             0.782994    0.217006         0.902080    0.097920

          -------------------------------
          BOND ORDER AND VALENCE ANALYSIS     BOND ORDER THRESHOLD=0.050
          -------------------------------

                   BOND                       BOND                       BOND
  ATOM PAIR DIST  ORDER      ATOM PAIR DIST  ORDER      ATOM PAIR DIST  ORDER
    1   2  1.320  1.845        1   4  3.668  0.087        1   5  1.074  0.945
    1   6  1.072  0.942        2   3  1.467  1.025        2   7  1.076  0.938
    3   4  1.320  1.845        3   8  1.076  0.938        4   9  1.074  0.945
    4  10  1.072  0.942

                       TOTAL       BONDED        FREE
      ATOM            VALENCE     VALENCE     VALENCE
    1 C                 3.762       3.762       0.000
    2 C                 3.712       3.712      -0.000
    3 C                 3.712       3.712      -0.000
    4 C                 3.762       3.762       0.000
    5 H                 0.926       0.926       0.000
    6 H                 0.923       0.923       0.000
    7 H                 0.920       0.920      -0.000
    8 H                 0.920       0.920      -0.000
    9 H                 0.926       0.926       0.000
   10 H                 0.923       0.923       0.000

          ---------------------
          ELECTROSTATIC MOMENTS
          ---------------------

 POINT   1           X           Y           Z (BOHR)    CHARGE
                -0.000000    0.000000    0.000000        0.00 (A.U.)
         DX          DY          DZ         /D/  (DEBYE)
     0.000000   -0.000000   -0.000000    0.000000
 ...... END OF PROPERTY EVALUATION ......
 STEP CPU TIME =     0.00 TOTAL CPU TIME =          1.8 (      0.0 MIN)
 TOTAL WALL CLOCK TIME=          1.9 SECONDS, CPU UTILIZATION IS    97.33%
  $VIB   
          IVIB=   0 IATOM=   0 ICOORD=   0 E=     -154.0594565686
  6.258297551E-05-7.937779917E-06-6.553528318E-23 8.739580302E-06 2.173150996E-05
 -1.922439440E-22-8.739563320E-06-2.173150736E-05 1.922439440E-22-6.258299126E-05
  7.937801310E-06 6.553528318E-23-5.697171651E-06 1.320325447E-05 2.824636604E-23
 -4.263948710E-05-1.666551234E-05-3.008422188E-23-4.033493403E-06-1.003515572E-05
 -5.027132141E-23 4.033497810E-06 1.003515105E-05 5.027132141E-23 5.697171613E-06
 -1.320326501E-05-2.824636604E-23 4.263948151E-05 1.666550355E-05 3.008422188E-23
  2.482618618E-11-6.813768825E-11-2.460955748E-18
 ......END OF GEOMETRY SEARCH......
 STEP CPU TIME =     0.00 TOTAL CPU TIME =          1.8 (      0.0 MIN)
 TOTAL WALL CLOCK TIME=          1.9 SECONDS, CPU UTILIZATION IS    97.33%
 AN INPUT FILE FOR -MOLPLT- HAS BEEN PUNCHED.
               580000  WORDS OF DYNAMIC MEMORY USED
 EXECUTION OF GAMESS TERMINATED NORMALLY Tue Nov  2 00:37:06 2021
 DDI: 263640 bytes (0.3 MB / 0 MWords) used by master data server.

 ----------------------------------------
 CPU timing information for all processes
 ========================================
 0: 1.786 + 0.44 = 1.831
 1: 0.02 + 0.02 = 0.04
 ----------------------------------------
 ddikick.x: exited gracefully.
unset echo
----- accounting info -----
Files used on the master node Barrys-MacBook-Pro-13.local were:
-rw-------  1 Barry  staff      896  2 Nov 00:37 .//Butadiene_121.F05
-rw-r--r--  1 Barry  staff  1963200  2 Nov 00:37 .//Butadiene_121.F10
-rw-r--r--  1 Barry  staff   206594  2 Nov 00:37 .//Butadiene_121.dat
ls: No match.
ls: No match.
ls: No match.
Tue  2 Nov 2021 00:37:09 ADT
1.855u 0.157s 0:05.08 39.3%	0+0k 0+0io 642pf+0w

```