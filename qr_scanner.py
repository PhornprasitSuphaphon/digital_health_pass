
import socket
import sys
import struct
import time
import binascii
import requests
import threading
import json
import zlib
import base45
import cbor2
from cose.messages import CoseMessage

class qr_code_scanner:

    def __init__(self,host,port,api,token,gate_id,vaccineStatus=2),:

        self.VaccineStatus = vaccineStatus # default vaccineTotal 2 unit
        self.gate_id = gate_id
        self.api = api
        self.token = token
        self.dataAPI = {'token':self.token,'gate_id':self.gate_id}

        self.host = host
        self.port = port
        self.clientSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

        self.inputHex = binascii.unhexlify("4C4F4E0D") #sent command start QR Code Reader  
        self.clientSocket.connect((self.host, self.port))
        self.clientSocket.send(self.inputHex)
        time.sleep(1)

        print('Socket connected to ' + self.host + ' port '+str(self.port)) 
        self.ThreadRun = threading.Thread(target=self.main)
        self.ThreadRun.start()

    def main (self):
        while True :
            msg = self.clientSocket.recv(1024).decode("utf-8")
            data = self.decode(msg)
            self.VaccineStatus(data)
            
    def VaccineStatus(self,data):
        status = ""
        msg = int(data[-260][1]['v'][0]['dn'])
        if (msg >= self.VaccineStatus ) :
            # requests api open barrier gate
            status = 'Pass'
            r = requests.post(url = self.api , data = self.dataAPI)
            pastebin_url = r.text
            print("The pastebin URL is:%s"%pastebin_url)
        else :
            status = 'Not Pass'
        print('Vaccine Total : '+ str(msg) +'Status :'+status)

    def decode(self,msg):
        # decode Base45 (remove HC1: prefix)
        payload=msg[4:]
        decoded = base45.b45decode(payload.strip())
        decompressed = zlib.decompress(decoded)
        cose = CoseMessage.decode(decompressed)
        data = cbor2.loads(cose.payload)
        return data

    def setVaccineStatus(self,value)
        self.vaccineTotal = value

    def getsetVaccineStatus(self)
        data = self.vaccineTotal 
        return data

    




