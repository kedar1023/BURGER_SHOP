import requests
import json

URL = 'https://www.way2sms.com/api/v1/sendCampaign'

# get request
def sendPostRequest(reqUrl, apiKey, secretKey, useType, phoneNo, senderId, textMessage):
  req_params = {
  'apikey':apiKey,
  'secret':secretKey,
  'usetype':useType,
  'phone': phoneNo,
  'message':textMessage,
  'senderid':senderId
  }
  return requests.post(reqUrl, req_params)


with open('Parents.txt', 'r') as reader:
     # Read and print the entire file line by line
    line = reader.readline()
    while line != '':  # The EOF char is an empty string
        print(line)
        arrr=line.split(',')
        phone=arrr[0]
        msg=arrr[1]
        response = sendPostRequest(URL, '0WZKELWU9AS2VKKGJ8AP5TLW12EZX5SU', 'F5B3UBMI4RZ7GTPY', 'stage', phone,
                           'ksparsewar1023@gmail.com', msg)
        
        print response.text
        print(phone)
        print(msg)
        line = reader.readline()
        
        
