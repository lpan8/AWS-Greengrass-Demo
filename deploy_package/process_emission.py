import json
import logging
import sys

import greengrasssdk

# Logging
logger = logging.getLogger(__name__)
logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)

# SDK Client
client = greengrasssdk.client("iot-data")

# Counter
max_co2 = 0
def lambda_handler(event, context):
    global max_co2
    #TODO1: Get your data

    
    #TODO2: Calculate max CO2 emission
    if "co2" in event:
        co2 = event["co2"]
        if co2 > max_co2:
            max_co2 = co2

    #TODO3: Return the result
    client.publish(
        topic="vehicle0/max_co2",
        payload=json.dumps(
            {"message": "Hello world! Sent from Greengrass Core.  Max CO2: {}".format(max_co2)}
        ),
    )
    return