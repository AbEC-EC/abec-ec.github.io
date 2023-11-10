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
02   00020  000600  0003:[-1.31, -0.0]  0.0218
03   00020  000600  0025:[-1.37, 0.08]  0.0107
04   00020  000600  0002:[-1.4, -0.12]  0.0164
01   00020  000600  0027:[-1.41, 0.01]  0.0001
05   00020  000600  0019:[-1.42, 0.02]  0.0006
09   00020  000600  0021:[-1.42, 0.0]  0.0000
07   00020  000600  0019:[-1.43, -0.07]  0.0057
08   00020  000600  0020:[-1.45, -0.05]  0.0056
06   00020  000600  0017:[-1.4, 0.11]  0.0134
10   00020  000600  0011:[-1.42, 0.02]  0.0007

[RESULTS]

[FILES GENERATED]

-[PATH] ../experiments/example1/results/
	-[FILE] 0001/PSO_20231013_0642_0001_42_OPTIMA.csv
	-[FILE] 0001/PSO_20231013_0642_0001_42_RUN.csv
	-[FILE] 0002/PSO_20231013_0642_0002_43_OPTIMA.csv
	-[FILE] 0002/PSO_20231013_0642_0002_43_RUN.csv
	-[FILE] 0003/PSO_20231013_0642_0003_44_OPTIMA.csv
	-[FILE] 0003/PSO_20231013_0642_0003_44_RUN.csv
	-[FILE] 0004/PSO_20231013_0642_0004_45_OPTIMA.csv
	-[FILE] 0004/PSO_20231013_0642_0004_45_RUN.csv
	-[FILE] 0005/PSO_20231013_0642_0005_46_OPTIMA.csv
	-[FILE] 0005/PSO_20231013_0642_0005_46_RUN.csv
	-[FILE] 0006/PSO_20231013_0642_0006_47_OPTIMA.csv
	-[FILE] 0006/PSO_20231013_0642_0006_47_RUN.csv
	-[FILE] 0007/PSO_20231013_0642_0007_48_OPTIMA.csv
	-[FILE] 0007/PSO_20231013_0642_0007_48_RUN.csv
	-[FILE] 0008/PSO_20231013_0642_0008_49_OPTIMA.csv
	-[FILE] 0008/PSO_20231013_0642_0008_49_RUN.csv
	-[FILE] 0009/PSO_20231013_0642_0009_50_OPTIMA.csv
	-[FILE] 0009/PSO_20231013_0642_0009_50_RUN.csv
	-[FILE] 0010/PSO_20231013_0642_0010_51_OPTIMA.csv
	-[FILE] 0010/PSO_20231013_0642_0010_51_RUN.csv
	-[FILE] ecMean.csv
	-[FILE] ecMean.png
	-[FILE] eoMean.csv
	-[FILE] eoMean.png
	-[FILE] readme.txt
	-[FILE] results.csv

==============================================
[RUNS:10]
[BEST POS (RUN 9) : [-1.42, 0.0]]
[BEST FIT (RUN 9): 0.0000]
[Ec  MEAN: 0.0075(0.0077)]
[Eo  MEAN: 0.5934(0.1658)]
[RUNTIME(s): 9.45 | 0.18(0.04)/run 1]
==============================================
[DATE: 10/13/2023 at 06:42]
[END] Thx :)


AbEC developed by Alexandre Mascarenhas
For more informations please go to https://abec-ec.github.io
Eh nois