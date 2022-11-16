#!/usr/bin/bash

import struct

def p(x):
	return struct.pack("I",x)

def u(x):
	return struct.unpack("I",x)

1234==u(p(1234))
