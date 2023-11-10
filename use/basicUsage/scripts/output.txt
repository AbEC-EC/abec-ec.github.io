=================================================================
            AbEC -> Ajustable Evolutionary Components        
             A framework for Optimization Problems         
=================================================================
*                                                               *
*                                                               *
*                    I hope you enjoy!                          *
*                                                               *
*                                                               *
*                                                               *
*                                                               *
* For more informations please visit: https://abec-ec.github.io *

[ALGORITHM SETUP]
- Name: PSO
- Individuals p/ population:	30
- [OPTIMIZERS]:
-- [PSO]
---- % of POP: 100%
---- PHI1: 2.05
---- PHI2: 2.05
---- W: 0.729
---- MIN_VEL: -10
---- MAX_VEL: 10
- [COMPONENTS]:

[FRAMEWORK SETUP]
- RUNS:		 10
- NEVALS p/ RUN: 600
- SEED:		 42

[PROBLEM SETUP]
- Name: CUSTOM
- NDIM: 2

[RUNNING]

RUN | GEN | NEVALS |                    BEST                   | ERROR
03   00020  000600  0025:[-1.37, 0.08]  -4.2781
05   00020  000600  0015:[-1.36, 0.02]  -4.2815
02   00020  000600  0003:[-1.31, -0.0]  -4.2670
04   00020  000600  0029:[-1.45, -0.01]  -4.2857
01   00020  000600  0010:[-1.49, 0.1]  -4.2667
06   00020  000600  0017:[-1.4, 0.11]  -4.2754
07   00020  000600  0019:[-1.39, 0.0]  -4.2873
08   00020  000600  0020:[-1.45, -0.05]  -4.2832
09   00020  000600  0021:[-1.42, 0.0]  -4.2888
10   00020  000600  0010:[-1.43, -0.04]  -4.2862

[RESULTS]

[FILES GENERATED]

-[PATH] ../experiments/example1/results/
	-[FILE] 0001/PSO_20231013_0632_0001_42_OPTIMA.csv
	-[FILE] 0001/PSO_20231013_0632_0001_42_RUN.csv
	-[FILE] 0002/PSO_20231013_0632_0002_43_OPTIMA.csv
	-[FILE] 0002/PSO_20231013_0632_0002_43_RUN.csv
	-[FILE] 0003/PSO_20231013_0632_0003_44_OPTIMA.csv
	-[FILE] 0003/PSO_20231013_0632_0003_44_RUN.csv
	-[FILE] 0004/PSO_20231013_0632_0004_45_OPTIMA.csv
	-[FILE] 0004/PSO_20231013_0632_0004_45_RUN.csv
	-[FILE] 0005/PSO_20231013_0632_0005_46_OPTIMA.csv
	-[FILE] 0005/PSO_20231013_0632_0005_46_RUN.csv
	-[FILE] 0006/PSO_20231013_0632_0006_47_OPTIMA.csv
	-[FILE] 0006/PSO_20231013_0632_0006_47_RUN.csv
	-[FILE] 0007/PSO_20231013_0632_0007_48_OPTIMA.csv
	-[FILE] 0007/PSO_20231013_0632_0007_48_RUN.csv
	-[FILE] 0008/PSO_20231013_0632_0008_49_OPTIMA.csv
	-[FILE] 0008/PSO_20231013_0632_0008_49_RUN.csv
	-[FILE] 0009/PSO_20231013_0632_0009_50_OPTIMA.csv
	-[FILE] 0009/PSO_20231013_0632_0009_50_RUN.csv
	-[FILE] 0010/PSO_20231013_0632_0010_51_OPTIMA.csv
	-[FILE] 0010/PSO_20231013_0632_0010_51_RUN.csv
	-[FILE] ecMean.csv
	-[FILE] ecMean.png
	-[FILE] eoMean.csv
	-[FILE] eoMean.png
	-[FILE] readme.txt
	-[FILE] results.csv

==============================================
[RUNS:10]
[BEST POS (RUN 9) : [-1.42, 0.0]]
[BEST FIT (RUN 9): -4.2888]
[Ec  MEAN: -4.2800(0.0081)]
[Eo  MEAN: -2.9277(0.0866)]
[RUNTIME(s): 6.92 | 0.13(0.06)/run 1]
==============================================
[DATE: 10/13/2023 at 06:32]
[END] Thx :)


AbEC developed by Alexandre Mascarenhas
For more informations please go to https://abec-ec.github.io
Eh nois