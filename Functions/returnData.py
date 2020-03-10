import os
from xlrd import *
import datetime
import time

xpathDict = dict()
testdata = dict()
variables = dict()
variable = dict()

def get_variables(strPath):
    print('Loading Data......')
    filepath = os.path.dirname(os.path.realpath(__file__))
    filepath = filepath.split("\\")[0:-2]
    new_path = ""
    for each_path in filepath:
        new_path = new_path + each_path + "\\"
        print(new_path)
        filepath = new_path + strPath
        ts= time.time()
        global timeStamp
        timeStamp = datetime.datetime.fromtimestamp(ts).strftime('%d%m%Y_%H%M%S')
        print("Timestamp is " + timeStamp)
        rb = open_workbook(filepath)
        print(rb._all_sheets_count)
        total_sheets = len(rb._sheet_names)
        for sheetNum in range(0, total_sheets):
            r_sheet = rb.sheet_by_index(sheetNum)
            rowcount = r_sheet.nrows
            colcount = r_sheet.ncols
            for row_index in range(1,rowcount):
                for col_index in range(1,colcount):
                    strTestCase = r_sheet.cell_value(row_index,0)
                    strParameterName = r_sheet.cell_value(0,col_index)
                    strParameterValue = r_sheet.cell_value(row_index,col_index)
                    strParameterValue = return_not_null(strParameterValue)
                    strKey = strTestCase + "." +strParameterName
                    variable[strKey] = strParameterValue
            variables = variable
            print('Data Loaded')
            print(variables)
            return variables

def return_not_null(value):
         try:
             return str(value)
         except:
             return ""
def is_number(s):
         try:
             float(s)
             return True
         except ValueError:
             return False
def convertToString(strToString):
    flag = is_number(strToString)
    if flag:
        try:
            converted_int = int(strToString)
            if  strToString == converted_int:
                return converted_int
            else:
                return strToString
        except:
            return strToString
    return strToString
get_variables("TestData.xlsx")