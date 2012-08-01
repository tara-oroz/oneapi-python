# -*- coding: utf-8 -*-

import pdb

import sys as sys
import logging as logging
import time as time

import oneapi as oneapi
import oneapi.models as models
import oneapi.dummyserver as dummyserver

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s')

if len(sys.argv) < 2:
    print 'Please enter username, password and your public ip address'
    sys.exit(1)

username = sys.argv[1]
password = sys.argv[2]

sms_client = oneapi.SmsClient(username, password)

sms = models.SMSRequest()
sms.sender_address = '38598854702'
sms.address = '38598854702'
sms.message = 'Test message'
sms.callback_data = 'Any string'

result = sms_client.send_sms(sms)

if not result.is_success():
    print 'Error sending message:', result.exception
    sys.exit(1)

print result
print 'Is success = ', result.is_success()
print 'Client correlator = ', result.client_correlator

# Few seconds later we can check for the sending status
time.sleep(10)

query_status = sms_client.query_delivery_status(result.client_correlator)
print query_status.delivery_info[0].delivery_status
