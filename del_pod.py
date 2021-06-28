#!/usr/bin/python3
print("content-type: text/html")
print()


import cgi
import subprocess
cmd = cgi.FieldStorage()
cont = cmd.getvalue("y")

output=subprocess.getoutput("sudo kubectl delete pod " +cont+ " --kubeconfig /root/k8s_tasks/admin.conf")
print("Command Executed\n")
print(output)

