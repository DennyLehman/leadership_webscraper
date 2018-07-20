import sys
import os
import pandas
import pytz
from datetime import datetime
import time
import xlrd
from xlrd import open_workbook ;

print("Welcome to processing the data from Excel");
print ( datetime.now() ) ;

filepath = r'D:\Users\Denny.Lehman\Desktop\Daily Irradiance Maker'
os.chdir(r'D:\Users\Denny.Lehman\Desktop\Daily Irradiance Maker')


EP = {};
Irr = {};

fp = open (filepath + r'\data\output\MonthlyEPDailyIrr2.txt' , 'w' );
fp_err = open(filepath + r'\data\output\ff_Error_Log_file2.txt' , 'w' );

wb = open_workbook (r'D:\Users\Denny.Lehman\Desktop\Daily Irradiance Maker\data\input\shadow\Monthly Shadow Expected Production Through 05_2018.xlsx');

wb_irr = open_workbook (r'D:\Users\Denny.Lehman\Desktop\Daily Irradiance Maker\data\input\weather\System_Snow_And_Weather_Adjustment_Factors_14_Mile_Radius_For_05_2018.xlsx');

for s in wb.sheets():
	print ("Sheet names are : ", s.name ) ;
	print ( "Sheet name is : " , s.name ) ;
	row_range =  s.nrows ;
	col_range = s.ncols ;
	print ( "Rows range are : " , row_range ) ;
	print ( "Col range are : " , col_range ) ;

# Header_Line = str( s.cell(0,0).value ) + ',' + str (s.cell(0,1).value ) + ',' + str (s.cell ( 0,2 ).value ) +',' + str (s.cell ( 0,3 ).value ) +',' + str (s.cell ( 0,4).value )+','+"Date"+','+"Value";
Header_Line = 'SYSTEM_NAME|DATE|EP_VALUE' ;

print ( "Header data is :" , Header_Line );

a1 = s.cell_value(0,1);
datetime_value = xlrd.xldate_as_tuple ( a1,  wb.datemode )  ;
year, month, day, hour, minute, second = xlrd.xldate_as_tuple ( a1,  wb.datemode )  ;
datetime_value = datetime(*xlrd.xldate_as_tuple(a1, 0)) ;
print ( datetime_value ) ;
py_date = datetime_value;
print ("Date is : %s" ,a1) ;
print ("Date is : " ,a1) ;
print ("DateTime Value is :", datetime_value ) ;
print ("py_date is : " , py_date );
print (str(py_date)[0:10] );


#Data is appending over to array (my_array)
print("\nData is appending over to array (my_array)...");
for row in range(1 ,row_range):
	for col in range(1 , col_range):
		cell_value = s.cell_value(row,col);
		v_date = s.cell_value(0,col) ;
		v_date = datetime(*xlrd.xldate_as_tuple(v_date , 0)) ;
		v_date = str(v_date)[0:10];
		arr = [s.cell_value(row,0), v_date, cell_value];
		EP[s.cell_value(row,0)+'_'+v_date] = cell_value;

print("Data appending to array has been done...");

# Print sheet info
for s in wb_irr.sheets():
	print ("Sheet names are : ", s.name ) ;
	print ( "Sheet name is : " , s.name ) ;
	row_range =  s.nrows ;
	col_range = s.ncols ;
	print ( "Rows range are : " , row_range ) ;
	print ( "Col range are : " , col_range ) ;

#Data is appending over to array (my_array)
print("\nData is appending over to array (my_array)...");
for row in range(1 ,row_range):
	for col in range(1 , col_range):
		cell_value = s.cell_value(row,col);
		v_date = s.cell_value(0,col) ;
		v_date = datetime(*xlrd.xldate_as_tuple(v_date , 0)) ;
		v_date = str(v_date)[0:10];
		arr = [s.cell_value(row,0), v_date, cell_value];
		Irr[s.cell_value(row,0)+'_'+v_date] = cell_value;


print("Data appending to array has been done...");







print ("\nExpected Production Data is :\n" );

#for i in my_array:
#	print ("\n", i);

print ("\nAdj Irradiance Data is :\n" );
#for j in my_irr_array:
#	print("\n", j);

fp.write ( Header_Line + "\n" ) ;


print ( "Data comparision is starting now .... \n");

for kep in EP:
	if ( EP[kep] == ''):
		vep = 0;
	else:
		vep = float ( EP[kep] );
	rec_match = 0;
	res = kep in Irr;
	if ( res == 1 ):
		irrfac = float (Irr[kep]);
	else:
		irrfac = 1;
	rec_match = 1 ;
	sys_name , v_date = kep.split('_');
	v_date = datetime.strptime(v_date,'%Y-%m-%d') ;
	v_month = v_date.strftime("%m");
	v_year = v_date.strftime("%Y");
	if ( v_month == '01' or v_month == '03' or v_month == '05' or v_month == '07' or v_month == '08' or v_month == '10' or v_month == '12' ):
		no_of_days = 31;
	elif ( v_month == '02' ):
		no_of_days = 28;
	else:
		no_of_days = 30 ;
	for p in range(1,no_of_days+1):
		next_date = v_year + "-" + v_month + "-" + str(p) ;
		v1 =  vep * irrfac ;
		v1 = v1 / no_of_days ;
		fp_line = sys_name + "|" + next_date + "|" + str( v1 ) + "\n";
		fp.write(fp_line);
	if ( rec_match == 0 ):
		fp_err.write(sys_name + " - " + next_date + " System name and Date has not been found with any irrandiance factor .. \n" );




print ("Output File preparation has been completed successfully....\n" );
print ( datetime.now() ) ;
fp.close();
fp_err.close();
