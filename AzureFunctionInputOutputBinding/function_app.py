import logging
import azure.functions as func

app = func.FunctionApp()

@app.function_name(name="AzureFunctionInputOutputBinding")
@app.route(route="hello")
@app.blob_input(arg_name="inputblob",
                path="inputbinding/ReadMe.txt",
                connection="BLOB_CONNECTION_SETTING")
@app.blob_output(arg_name="outputblob",
                path="outputbinding/test.txt",
                connection="BLOB_CONNECTION_SETTING")
def main(req: func.HttpRequest, inputblob: str, outputblob: func.Out[str]):
    logging.info(f'Python Queue trigger function processed {len(inputblob)} bytes')
    outputblob.set(inputblob)
    return "ok"