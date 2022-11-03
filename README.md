# AWS-Greengrass-Demo
Sample command to run basicDiscovery.py:

`python .\basicDiscovery.py --endpoint greengrass-ats.iot.us-east-1.amazonaws.com --rootCA AmazonRootCA1.pem --cert certs/vehicle0/79268b4b566cccedfe714df61d7e93a254620c23f933820cff03f934fd99c92f-certificate.pem.crt --key certs/vehicle0/79268b4b566cccedfe714df61d7e93a254620c23f933820cff03f934fd99c92f-private.pem.key --thingName Vehicle0 --topic 'vehicle0/max_co2' --mode both`
