#!/usr/bin/python3
print("content-type: text/html")
print()


import cgi
import subprocess
cmd = cgi.FieldStorage()
cont=cmd.getvalue("d")
res=subprocess.getoutput('sudo kubectl expose deployment ' +cont + ' --type=LoadBalancer  --port=5555 --kubeconfig /root/k8s_tasks/admin.conf')
print("Your service expose  Successfully Launch : " +res)

