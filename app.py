import json
import sys
import zlib
import base45
import cbor2
import threading
from qr_scanner import qr_code_scanner

#barrier gate
api = "http://1.1.178.75:50002/api/ws/requestopengate/"
token = "31Ln4SmOCkG9NPhKeFtnKOH4oA8lMBSyx4M9wpfs35vh_UIPBgYiyB6qAFb2dk20zwgy1Dv0hvRVp6Zbi-tukrlQ"
gateID = {1 : 300000001, 2 : 300000002, 3 : 300000003, 4 :300000004}

# ip and port qr-code reader 
hostname = {1 : '192.168.1.130', 2 : '192.168.1.131', 3 : '192.168.1.133', 4 :'192.168.1.134'}
port = 9004

#set vaccinestatus for open barrier gate 
vaccineStatus = 2 

qr1 = qr_code_scanner(hostname[1],port,api,token,gateID[1],vaccineStatus)
qr2 = qr_code_scanner(hostname[2],port,api,token,gateID[2],vaccineStatus)
qr3 = qr_code_scanner(hostname[3],port,api,token,gateID[3],vaccineStatus)
qr4 = qr_code_scanner(hostname[4],port,api,token,gateID[4],vaccineStatus)





