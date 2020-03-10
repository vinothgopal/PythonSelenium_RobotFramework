from robot.libraries.BuiltIn import BuiltIn
import string
import keywords
from robot.api import logger

###########################################################
class MyContinualeError(RuntimeError):
    ROBOT_CONTINUE_ON_FAILURE=True
    ROBOT_EXIT_ON_FAILURE=False

###########################################################
def get_xpath(or_name):
    try:
        or_value= '${'+or_name+'}'
        object_value=BuiltIn.get_variable_value(or_value)
        object_value_new=string.replace(object_value,"xpath=","")
        object_new_value=string.replace(object_value_new,"\\","")
        return object_new_value
    except:
        keywords.log("Xpath not found : "+or_name)
        keywords.log("Xpath not found : " + or_name,"console")
        raise ValueError("Xpath not found :"+or_name)
#############################################################
def get_data_value(data):
    data_variable='${'+data+'}'
    data_value=BuiltIn().get_variable_value(data_variable)
    if data_value==None:
        data_value=""
    return data_value
##############################################################
def get_test_data(value,index=-1):
    try:
        index=int(index)
        test_name=get_data_value("TEST_NAME")
        data=get_data_value(str(test_name)+"."+str(value))
        if index==-1:
            if "|" in data:
                return data.split("|")[0]
            return data
        else:
            if "|" in data:
                return_values=data.split("|")[index-1]
                return return_values
            else:
                return ""
    except:
        return ""
#############################################################
def set_test_data(variable_name,value):
    test_name=get_data_value("TEST_NAME")
    variable_name="${"+test_name+"."+variable_name+"}"
    BuiltIn().set_task_variable(variable_name,value)
    keywords.log_msg("saving test data : "+variable_name+"-----"+value)