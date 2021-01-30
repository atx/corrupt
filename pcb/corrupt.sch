EESchema Schematic File Version 4
EELAYER 30 0
EELAYER END
$Descr A4 11693 8268
encoding utf-8
Sheet 1 3
Title ""
Date ""
Rev ""
Comp ""
Comment1 ""
Comment2 ""
Comment3 ""
Comment4 ""
$EndDescr
$Sheet
S 2850 3700 900  1000
U 600DBDDB
F0 "MCU" 50
F1 "mcu.sch" 50
F2 "COL[0..14]" I R 3750 4150 59 
F3 "ROW[0..4]" O R 3750 4000 59 
$EndSheet
$Sheet
S 5450 3750 850  650 
U 601E1EF3
F0 "Keys" 50
F1 "keys.sch" 50
F2 "ROW[0..4]" I L 5450 4000 59 
F3 "COL[0..14]" O L 5450 4150 59 
$EndSheet
$Comp
L Mechanical:MountingHole H1
U 1 1 6044167D
P 900 7450
F 0 "H1" H 1000 7496 50  0000 L CNN
F 1 "M2.5" H 1000 7405 50  0000 L CNN
F 2 "MountingHole:MountingHole_2.7mm_M2.5_Pad" H 900 7450 50  0001 C CNN
F 3 "~" H 900 7450 50  0001 C CNN
	1    900  7450
	1    0    0    -1  
$EndComp
$Comp
L Mechanical:MountingHole H2
U 1 1 60441E7F
P 1250 7450
F 0 "H2" H 1350 7496 50  0000 L CNN
F 1 "M2.5" H 1350 7405 50  0000 L CNN
F 2 "MountingHole:MountingHole_2.7mm_M2.5_Pad" H 1250 7450 50  0001 C CNN
F 3 "~" H 1250 7450 50  0001 C CNN
	1    1250 7450
	1    0    0    -1  
$EndComp
$Comp
L Mechanical:MountingHole H3
U 1 1 60442026
P 1600 7450
F 0 "H3" H 1700 7496 50  0000 L CNN
F 1 "M2.5" H 1700 7405 50  0000 L CNN
F 2 "MountingHole:MountingHole_2.7mm_M2.5_Pad" H 1600 7450 50  0001 C CNN
F 3 "~" H 1600 7450 50  0001 C CNN
	1    1600 7450
	1    0    0    -1  
$EndComp
$Comp
L Mechanical:MountingHole H5
U 1 1 60442794
P 1950 7450
F 0 "H5" H 2050 7496 50  0000 L CNN
F 1 "M2.5" H 2050 7405 50  0000 L CNN
F 2 "MountingHole:MountingHole_2.7mm_M2.5_Pad" H 1950 7450 50  0001 C CNN
F 3 "~" H 1950 7450 50  0001 C CNN
	1    1950 7450
	1    0    0    -1  
$EndComp
Wire Bus Line
	5450 4000 3750 4000
Wire Bus Line
	3750 4150 5450 4150
$EndSCHEMATC
