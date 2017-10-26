#!/usr/bin/env python
# -*- coding:utf-8 -*-

import socket
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

if len(sys.argv) < 2:
    print 'Usage:\n\t', sys.argv[0], 'IP PORT'
    exit()

ip = sys.argv[1]
port = int(sys.argv[2])

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_address = (ip, port)
message = 'This is the message.  It will be repeated.'

try:

    # Send data
    print >>sys.stderr, 'sending "%s"' % message
    sent = sock.sendto(message, server_address)

    # Receive response
    print >>sys.stderr, 'waiting to receive'
    data, server = sock.recvfrom(4096)
    print >>sys.stderr, 'received "%s"' % data

finally:
    print >>sys.stderr, 'closing socket'
    sock.close()

