import logging
import azure.functions as func
from confluent_kafka import Producer

app = func.FunctionApp()



@app.function_name(name="FuncBlobTrigger")
@app.blob_trigger(arg_name="myblob", 
                  path="kmfiles",
                  connection="blobtriggerstorageacc_STORAGE")
def test_function(myblob: func.InputStream):
   logging.info(f"kafka dir : {dir(Producer)}")
   logging.info(f"Python blob trigger V2 function processed blob \n"
                f"Name: {myblob.name}\n"
                f"Blob Size: {myblob.length} bytes")