from BaseLogger import BaseLogger
import logging
import datetime

class Logger:

    class Singleton(object):
        def __init__(self):
            loggerClass=BaseLogger()
            self.log=loggerClass.log()
    testSuiteList=[]
    testCaseList=[]
    iterationList=[]
    __instance=None
    def __init__(self):
        if not Logger.__instance:
            Logger.__instance=Logger.Singleton()
        self.log=Logger.__instance.log

    def loginfo(self, msg, *args):
        self.log.info("<br>")
        self.log.info(('<b>'+str(msg)+'<b>'+'{0}').format(" ".join(list(args))))
    def logScreenshot(self,file):
        self.log.info("<br>")
        self.log.info('<a href='+file+' target="_blank">Scrrenshot</a>')
    def logWarning(self,msg):
        self.log.warning(msg)
    def logDebug(self,msg):
        self.log.debug(msg)
    def logError(self,msg):
        self.log.error(msg)
    def testSuiteStart(self,testSuiteName):
        self.testSuiteList.append(testSuiteName)
        testSuiteName=testSuiteName.split('-')[-1]
        head= "=" * 100
        msg="<b><font style='color:#3CB371;'>"+testSuiteName+"</b></font>"+" Started"+" "*10
        self.loginfo(head)
        self.suiteStartTime=self.timeFn()
        self.loginfo(str(self.suiteStartTime),' ',msg)
        self.loginfo(head)
    def testSuiteEnd(self,testSuiteName):
        head= "=" * 100
        msg=testSuiteName+" Completed "+ " "*10
        self.loginfo(head)
        self.suiteStartTime=self.timeFn()
        self.loginfo(str(self.suiteStartTime),' ',msg)
        timeTaken=self.timeDifference(self.suiteEndTime,self.suiteStartTime)
        l=len(self.testSuiteList)
        self.loginfo("TestSuite "+"<b>"+(str(l))+"</b>")
        self.loginfo("Suite execuion time : ",str(timeTaken))
        self.loginfo(head)
    def testCaseStart(self,testCaseName):
        self.testCaseList.append(testCaseName)
        testCaseName = testCaseName.split('-')[-1]
        head = "-" * 100
        msg = "<b><font style='color:#3CB371;'>" + testCaseName + "</b></font>" + " Started" + " " * 10
        self.loginfo(head)
        self.tcStartTime = self.timeFn()
        self.loginfo(str(self.testCaseName), ' ', msg)
        self.loginfo(head)
    def testCaseEnd(self,testCaseName):
        head= "=" * 100
        msg=testCaseName+" Completed "+ " "*10
        self.loginfo(head)
        self.tcEndTime=self.timeFn()
        self.loginfo(str(self.tcEndTime),' ',msg)
        timeTaken=self.timeDifference(self.tcEndTime,self.tcStartTime)
        l=len(self.tcStartTime)
        self.loginfo("TestCase "+"<b>"+(str(l))+"</b>")
        self.loginfo("TestCase execuion time : ",str(timeTaken))
        self.loginfo("Iterations executed: "+"<b>"+(str(len(self.iterationList)))+"</b>")
        self.loginfo(head)
    def iterationStart(self,iterationNumber):
        self.iterationList.append(iterationNumber)
        msg="Iteration Start : "+"<b>"+str(iterationNumber)+"</b>"
        self.iterstartTime=self.timeFn()
        self.loginfo(str(self.iterstartTime),' ',msg)
    def iterationEnd(self,iterationNumber):
        msg="Iteration End:  "+str(iterationNumber)
        self.iterationEndTime=self.timeFn()
        self.loginfo(str(self.iterationEndTime),' ',msg)
        timeTaken=self.timeDifference(self.iterationEndTime,self.iterstartTime)
        self.loginfo("Iteration execution time: ",str(timeTaken))
        self.loginfo(str("."*100))
    def startfn(self,methodName):
        msg="***" * 10 +methodName+" start "+"***" *10
        self.loginfo(msg)
    def endfn(self,methodName):
        msg="***" * 10 +methodName+" End "+"***" *10
        self.loginfo(msg)
    def result(self,value):
        msg='PASS' if value else 'FAIL'
        if msg=='PASS':
            code='#008000'
        else:
            code='#FF0000'
        self.loginfo("Result: ","<b><font style='color:{0};'>{1}</font></b>".format(code,msg))
    def timeFn(self):
        return datetime.datetime.now().replace(microsecond=0)
    def timeDifference(self,endTime,startTime):
        return endTime-startTime


