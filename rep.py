#!/usr/bin/python3
print("content-type: text/html")
print()


import cgi
import subprocess
cmd = cgi.FieldStorage()
cont=cmd.getvalue("d")
rep=cmd.getvalue("z")
rep=int(rep)
reps=subprocess.getoutput('sudo kubectl scale deployment ' +cont+ ' --replicas= ' +rep+ ' --kubeconfig /root/k8s_tasks/admin.conf')

print("Your replica created  Successfully Launch : " +reps)

