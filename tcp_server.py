import socket
import argparse


parser = argparse.ArgumentParser()
parser.add_argument('--host', type=str, default='127.0.0.1', help='host')
parser.add_argument('--port', type=int, default=9004, help='port')  
opt = parser.parse_args()

HOST = opt.host 
PORT = opt.port         
s =  socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST,PORT))
s.listen()
conn, addr = s.accept()  
print('Connected by', addr)
while True:
    print('send msg :')
    msg = input()
    conn.sendall(msg.encode())



# msg = 'HC1:NCFOXN%TSMAHN-H5XS14GBG829I3WI0IIF$3 43 G8C9B7LIO6G.TM0X4%/0 NBMF6.UCOMIN6R%E5BD7ME4CU6O8QGU68ORJSPAEQG*OWSP01RG1RJ+P10P *PH0P4HPOGOBERS69PQN6LBDCN6DJ6473H3PLN+FNHKB1DNRK3FG30IN*J3:HN8E3BB7077Q7BLD3UCNS+0SZ4MJ00T9UKPH+9WC5PF6846%PQX76UW6%V98T5LAAY0Q$UPR$5:NLOEPGMAC45SSPCT9.GUQ$9WC5X9A:416997$P9$PUKQ*PP:+P*.1D9R$P6SRRG8C3AD:XIBEIVG395EV3EVCK09D5WCFVA5RO5VA81K0ECM8CXVDC8C90JK.A+ C/8DXEDKG0CGJ5AL5:4A930JBIFTA30HFE.-B97U: K2*N.ISF0047P7/1AAOC.UUP5FU3R$S6%T2OIC0JYMGIN9P8Q5D8:Q5TW5A 6+O67N6F7E8/RDHN8S78-TCL05I8HQ0.X44:4VAOLNEEND0*URT3CMCI-E$KR6NDKYD04E.WBU7OJPH3WSQ-8G3W*QEQ.9UQCNPATT7N/JXMFYM0LKQ81H'

# HC1:NCFOXN%TSMAHN-H5XS14GBG829I3WI0II*%6 43 G8C9BQMIQ1NBOM%Z49MU5IBMF6.UCOMIN6R%E5BD7ME4CU6O8QGU68ORJSPAEQG*O SP$GO9-RCNP0HOT*OKSOPHQ0IQV+QV*O+GOC0P11Q2ORO1R-MP*NRQ0QGNPESOFTQCIRATQL*ON0PJ+QX*OQHPB0PV*O8SOG$8XQ6/97%8D6IAA%36IASD9YHI5IIX2MZJKJGIYIA FEOMHG.CZ.C4C96+KA0G+G87ED0-9NPMC19BJCCD95LG769ZJC-+9$.B4.C/.DV2MGDIK3MXGG HGMJKB%G.IA.C8KRDL4O54O4IGUJKPGG0JAKE15IAXMFU*GSHGRKMXGG6DBYCB-1JMJKY*K2HQB*0HJP7NVDEBU1JE+4$$05QN 2JIGF5JNBPI$RU2LG84W8L4+W3BPIAYU-:VQQGO2WXZQ/K93QK9NTCW4/NST*QGTAAY7.Y7N31+4WZE2LF7I3BR B/2LWLS6SDA6S.DUAK6HQO4M0EVEV/5ZBT71995Q5/M7 0WS8:$UK8BNM63PN$1J JHF1GQ*N-5RX3J/0RBXU8MLL10PBSJ1