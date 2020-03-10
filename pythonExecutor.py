import os
from robot import run
import time
import datetime
strSuiteName="Demo.robot"
arrayTestCses=["TestCase3"]
def run_test(Suite,Testcase):
    strdir=createdir()
    run("D:\\RIDE_DEMO\\DemoProject\\TestCases\\"+Suite, test=Testcase,outputdir=strdir,loglevel='DEBUG:INFO')

def createdir():
    ts=time.time()
    timeStamp = datetime.datetime.fromtimestamp(ts).strftime('%d%m%Y_%H%M%S')
    dir_path=os.path.dirname(os.path.realpath(__file__))
    directory=dir_path+"\\Results\\"+timeStamp
    if not os.path.exists(directory):
        os.makedirs(directory)
    return directory
run_test(strSuiteName,arrayTestCses)