import os
import sys

from lambda_function.testFirst import lambda_handler

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

filename = "TEST"

argv = {"filename": "select"}
event = {"queryStringParameters": argv}
context = None

result = lambda_handler(event, context)
print(result)