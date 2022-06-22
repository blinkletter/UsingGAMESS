#!/usr/bin/env python
# coding: utf-8

# # Data Workflow
# 
# If you open the `results.txt` file in a text editor you will see nineteen lines of data, one line for ezch file. 
# 
# Within the file name is the torsion angle. The step number for the last energy calculation, NSERCH, is next. The energy follows that and the value is in units of Hartrees/molecule. We will want to convert that to kJ/mole. Then we have the energy gradient for the last structure of the optimization. It should be less than 0.0001 for the claulation to stop. We could have set this lower or higher. The last value recorded in each line is the RMS deviation for the gradient calculation.

# **results.txt**
# ```
# Cyclohexene_Cs_scan.inp_SCAN_1.45_330.log: NSERCH:  11  E=     -232.9995497493  GRAD. MAX=  0.0000706  R.M.S.=  0.0000276
# Cyclohexene_Cs_scan.inp_SCAN_1.50_331.log: NSERCH:  10  E=     -233.0074050634  GRAD. MAX=  0.0000652  R.M.S.=  0.0000285
# Cyclohexene_Cs_scan.inp_SCAN_1.55_332.log: NSERCH:   5  E=     -233.0091271727  GRAD. MAX=  0.0000742  R.M.S.=  0.0000284
# Cyclohexene_Cs_scan.inp_SCAN_1.60_333.log: NSERCH:  11  E=     -233.0061114211  GRAD. MAX=  0.0000633  R.M.S.=  0.0000303
# Cyclohexene_Cs_scan.inp_SCAN_1.65_334.log: NSERCH:  19  E=     -232.9994858977  GRAD. MAX=  0.0000841  R.M.S.=  0.0000299
# Cyclohexene_Cs_scan.inp_SCAN_1.70_335.log: NSERCH:  20  E=     -232.9901643852  GRAD. MAX=  0.0000448  R.M.S.=  0.0000193
# Cyclohexene_Cs_scan.inp_SCAN_1.75_336.log: NSERCH:  20  E=     -232.9789005901  GRAD. MAX=  0.0000484  R.M.S.=  0.0000219
# Cyclohexene_Cs_scan.inp_SCAN_1.80_337.log: NSERCH:  20  E=     -232.9663220865  GRAD. MAX=  0.0000507  R.M.S.=  0.0000230
# Cyclohexene_Cs_scan.inp_SCAN_1.85_338.log: NSERCH:  20  E=     -232.9529605653  GRAD. MAX=  0.0000630  R.M.S.=  0.0000252
# Cyclohexene_Cs_scan.inp_SCAN_1.90_339.log: NSERCH:  21  E=     -232.9392786848  GRAD. MAX=  0.0000377  R.M.S.=  0.0000135
# Cyclohexene_Cs_scan.inp_SCAN_1.95_340.log: NSERCH:  21  E=     -232.9256963349  GRAD. MAX=  0.0000557  R.M.S.=  0.0000175
# Cyclohexene_Cs_scan.inp_SCAN_2.00_341.log: NSERCH:  21  E=     -232.9126284280  GRAD. MAX=  0.0000797  R.M.S.=  0.0000244
# Cyclohexene_Cs_scan.inp_SCAN_2.05_342.log: NSERCH:  21  E=     -232.9005442078  GRAD. MAX=  0.0000807  R.M.S.=  0.0000270
# Cyclohexene_Cs_scan.inp_SCAN_2.10_343.log: NSERCH:  21  E=     -232.8900966067  GRAD. MAX=  0.0000969  R.M.S.=  0.0000275
# Cyclohexene_Cs_scan.inp_SCAN_2.15_344.log: NSERCH:  21  E=     -232.8824624035  GRAD. MAX=  0.0000699  R.M.S.=  0.0000306
# Cyclohexene_Cs_scan.inp_SCAN_2.20_345.log: NSERCH:  22  E=     -232.8796092131  GRAD. MAX=  0.0000435  R.M.S.=  0.0000185
# Cyclohexene_Cs_scan.inp_SCAN_2.25_346.log: NSERCH:  22  E=     -232.8812781492  GRAD. MAX=  0.0000789  R.M.S.=  0.0000249
# Cyclohexene_Cs_scan.inp_SCAN_2.30_347.log: NSERCH:  23  E=     -232.8851867409  GRAD. MAX=  0.0000450  R.M.S.=  0.0000158
# Cyclohexene_Cs_scan.inp_SCAN_2.35_348.log: NSERCH:  24  E=     -232.8900395999  GRAD. MAX=  0.0000381  R.M.S.=  0.0000143
# Cyclohexene_Cs_scan.inp_SCAN_2.40_349.log: NSERCH:  25  E=     -232.8952063985  GRAD. MAX=  0.0000422  R.M.S.=  0.0000158
# Cyclohexene_Cs_scan.inp_SCAN_2.45_350.log: NSERCH:  25  E=     -232.9003522433  GRAD. MAX=  0.0000530  R.M.S.=  0.0000214
# Cyclohexene_Cs_scan.inp_SCAN_2.50_351.log: NSERCH:  25  E=     -232.9052913516  GRAD. MAX=  0.0000648  R.M.S.=  0.0000247
# Cyclohexene_Cs_scan.inp_SCAN_2.55_352.log: NSERCH:  25  E=     -232.9099213808  GRAD. MAX=  0.0000692  R.M.S.=  0.0000268
# Cyclohexene_Cs_scan.inp_SCAN_2.60_353.log: NSERCH:  26  E=     -232.9141903297  GRAD. MAX=  0.0000746  R.M.S.=  0.0000315
# Cyclohexene_Cs_scan.inp_SCAN_2.65_354.log: NSERCH:  28  E=     -232.9180777391  GRAD. MAX=  0.0000929  R.M.S.=  0.0000313
# Cyclohexene_Cs_scan.inp_SCAN_2.70_355.log: NSERCH:  29  E=     -232.9215830460  GRAD. MAX=  0.0000847  R.M.S.=  0.0000318
# Cyclohexene_Cs_scan.inp_SCAN_2.75_356.log: NSERCH:  30  E=     -232.9247190604  GRAD. MAX=  0.0000694  R.M.S.=  0.0000316
# Cyclohexene_Cs_scan.inp_SCAN_2.80_357.log: NSERCH:  32  E=     -232.9275067283  GRAD. MAX=  0.0000777  R.M.S.=  0.0000320
# Cyclohexene_Cs_scan.inp_SCAN_2.85_358.log: NSERCH:  35  E=     -232.9299717690  GRAD. MAX=  0.0000860  R.M.S.=  0.0000298
# Cyclohexene_Cs_scan.inp_SCAN_2.90_359.log: NSERCH:  33  E=     -232.9321410104  GRAD. MAX=  0.0000732  R.M.S.=  0.0000328
# Cyclohexene_Cs_scan.inp_SCAN_2.95_360.log: NSERCH:  32  E=     -232.9340442270  GRAD. MAX=  0.0000658  R.M.S.=  0.0000251
# Cyclohexene_Cs_scan.inp_SCAN_3.00_361.log: NSERCH:  32  E=     -232.9357093441  GRAD. MAX=  0.0000431  R.M.S.=  0.0000171
# ```

# ## Import Raw Data
# We could edit the data in a text editor but we will do everything using the data analysis tools of Python and pandas. First we will import the data as a dataframe using pandas. The datafile must be in the same directory as this workbook, or you must specify the file path. Don't worry, python will scream at you if you make a mistake and you will be able to fix any problems.
# 
# We will use the `pandas.read_csv()` function to read the file and create a dataframe object. The `header = None` setting prevents the first line from being used to label the columns. The `sep = r"\s+|_"` establishes that one or more spaces separates columns and also the `_` character separates columns. The `engine = "python"` means to use the python engine rather than the default cpython engine. The cpython engine is much faster, but it is not compatible with the way I am using the `sep` parameter. How do I know this? I got an error message that told me what to do.

# In[1]:


import pandas as pd

df = pd.read_csv("/Users/blink/Documents/CompChem/GAMESS-RESULTS/results.txt", header = None, sep = r"\s+|_", engine = "python") 
display(df.head())


# ## Cleaning the Data
# 
# Data cleaning is half the work in data analysis. We need to drop empty records and malformed records (each line could be considered a record in this case). We will need to drop any fields (the columns in eacxh record are the fields). Inspecting the dataframe shows me that I only need columns 4,7,9,12. We will rename the columns for what they represent. inspect the orginal dataframe above to see where I got my lables from. 
# 
# In the code below I create a new dataframe by selecting the four chosen columns out of the previous dataframe. Then I renamed the column headres from numbers to labels so I don't forget what they are.

# In[2]:


coord = df[:][[4,7,9,12]]
coord = coord.rename({4:'Length', 7:'NSERCH', 9:'Energy', 12:'GRAD'}, axis='columns')
display(coord.head())


# ## Processing the Data
# 
# We now have a cleaned up data set. We could have done all of this in Excel by importing the text file, setting column breaks manually, deleting unwanted columns manually and then typing in names for the columns. Python and pandas may seem like a bit of work but it is not any more than you would do setting up the data in Excel.
# 
# We know that a Hartree is $2625.7\, kJ/mole$. So we can convert the energy to a more familiar unit. Then we should set our lowest energy structure as the zero referemce and substract that value from all the energies to establish a relative scale.

# In[3]:


import numpy as np
hartree_conversion = 2625.7

lowest_energy = np.min(coord[:]["Energy"])
coord["DeltaE"] = (coord[:]["Energy"] - lowest_energy) * hartree_conversion
display(coord)


# ## Plotting the Profile
# 
# Now we have a set of data that we can plot. Let us visualize the profile using the MatPlotLib library.

# In[4]:


import matplotlib.pyplot as plt

x = coord[:]["Length"]
y = coord[:]["DeltaE"]

plt.plot(x,y, "ko-")
plt.show()


# ## Publication Quality
# 
# We can be more stylish. I will use the stylesheet that I editted to my preference. It must be in the local directory.
# 
# Divverent journals have different standards for plots. Just follow their instructions. many will hae stylesheets available for your word processor, for $\LaTeX$ and  even for MacMolPlt. use the `savefig()` method of the `fig` object to save the plot as a file. The `.pdf` extension will tell it to save in PDF format. 
# 

# In[5]:


x = coord[:]["Length"]
y = coord[:]["DeltaE"]

plt.style.use("S2_classic2.mplstyle")        
fig, ax = plt.subplots(nrows=1, ncols=1, figsize=(6,4))  

ax.plot(x,y,"o-")

ax.set(title="Reaction Coordinate Energy Profile",       
          ylabel=r"Energy $\left(\frac{kJ}{mole}\right)$", 
          xlabel=r"Distance $\left(\AA\right)$",                
          xlim=[1.4,3.0],                  
          ylim=[0,360]
      )                   

#fig.savefig("plot.pdf")
plt.show()


# The plot above is a "connect-the-dots" style plot.  There are many data points and it looks fine. We do not have an exact function to which to fit the data but we could apply the infamous "cubic spline." We will use the `CubicSpline` function available from the `scipy.interpolate` library ([Documentation](https://docs.scipy.org/doc/scipy/reference/generated/scipy.interpolate.CubicSpline.html)) to generate a function that represents the curve fit.  We will then feed an x-axis of many data points into that function to create a x,y data set that represents that curve fit as a smooth line.

# In[6]:


from scipy.interpolate import CubicSpline

plt.style.use("S2_classic2.mplstyle")        
fig, ax = plt.subplots(nrows=1, ncols=1, figsize=(6,4))  

cs = CubicSpline(x, y)
x = np.arange(1.4, 3.0, 0.1)
y = cs(x)
ax.plot(x, y, "-")

x = coord[:]["Length"]
y = coord[:]["DeltaE"]
ax.plot(x,y,"o")

ax.set(title="Reaction Coordinate",       
          ylabel=r"Energy $\left(\frac{kJ}{mole}\right)$", 
          xlabel=r"Distance $\left(\AA\right)$",                
          xlim=[1.4,3.0],                  
          ylim=[0,360]
      )                   

#fig.savefig("plot.pdf")
plt.show()


# ## Saving the Data
# 
# We have imported, cleaned and processed the data. maybe we should save our work so we can use this data set directly and easily next time.  The dataframe object contains methods to do this. We will use the 'pandas.DataFrame.to_csv()' method([documentation](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_csv.html)) to save the dataframe object as a csv text file.

# In[7]:


coord.to_csv("coord_profile.csv")


# The butane energy profile data is now saved in a file named butane_profile.csv. below the file is reporduced in csv format.
# 
# **coord_profile.csv**
# ```
# ,Length,NSERCH,Energy,GRAD,DeltaE
# 0,1.45,11,-232.9995497493,7.06e-05,25.14744062138847
# 1,1.5,10,-233.0074050634,6.52e-05,4.521742389022088
# 2,1.55,5,-233.0091271727,7.42e-05,0.0
# 3,1.6,11,-233.0061114211,6.33e-05,7.918458976128175
# 4,1.65,19,-232.9994858977,8.41e-05,25.315095767518375
# 5,1.7,20,-232.9901643852,4.48e-05,49.790591138790866
# 6,1.75,20,-232.9789005901,4.84e-05,79.36593793280394
# 7,1.8,20,-232.9663220865,5.07e-05,112.39331483531552
# 8,1.85,20,-232.9529605653,6.3e-05,147.4766610501841
# 9,1.9,21,-232.9392786848,3.77e-05,183.40117467903897
# 10,1.95,21,-232.9256963349,5.57e-05,219.06435081144582
# 11,2.0,21,-232.912628428,7.97e-05,253.3767539587896
# 12,2.05,21,-232.9005442078,8.07e-05,285.1062909379162
# 13,2.1,21,-232.8900966067,9.69e-05,312.5385571461794
# 14,2.15,21,-232.8824624035,6.99e-05,332.5836844884529
# 15,2.2,22,-232.8796092131,4.35e-05,340.0753065217416
# 16,2.25,22,-232.8812781492,7.89e-05,335.69318100396293
# 17,2.3,23,-232.8851867409,4.5e-05,325.4303917772819
# 18,2.35,24,-232.8900395999,3.81e-05,312.68823990095484
# 19,2.4,25,-232.8952063985,4.22e-05,299.12177681696886
# 20,2.45,25,-232.9003522433,5.3e-05,285.61033212557766
# 21,2.5,25,-232.9052913516,6.48e-05,272.64171546228545
# 22,2.55,25,-232.9099213808,6.92e-05,260.48464779184224
# 23,2.6,26,-232.9141903297,7.46e-05,249.27566866509807
# 24,2.65,28,-232.9180777391,9.29e-05,239.0684978035347
# 25,2.7,29,-232.921583046,8.47e-05,229.86461347621594
# 26,2.75,30,-232.9247190604,6.94e-05,221.63038046610126
# 27,2.8,32,-232.9275067283,7.77e-05,214.31080086112297
# 28,2.85,35,-232.929971769,8.6e-05,207.83834349512662
# 29,2.9,33,-232.9321410104,7.32e-05,202.142566351154
# 30,2.95,32,-232.934044227,6.58e-05,197.1452905245371
# 31,3.0,32,-232.9357093441,4.31e-05,192.7731925550579
# ```
