#!/usr/bin/python3

import cgi
import subprocess

print("content-type: text/html")
print()

recieve = cgi.FieldStorage()
image_name = recieve.getvalue("x")
cont_name = recieve.getvalue("y")


out=subprocess.getoutput('sudo kubectl run ' + cont_name + ' --image='+ image_name + ' --kubeconfig /root/k8s_tasks/admin.conf')
print("Pod successfully launched: \n" +out)


