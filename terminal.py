#!/usr/bin/python3

import cgi
import subprocess

print("content-type: text/html")
print()

recieve = cgi.FieldStorage()
stat=recieve.getvalue("k")

var = stat.split()
if var[0] == "1":
    deployment_name = var[2]
    image_name = var[1]
    cmd = "kubectl create deployment " + (deployment_name) + " --image=" + (image_name)
    output = subprocess.getoutput("sudo " + cmd + " --kubeconfig /root/k8s_tasks/admin.conf")
    print(output)
elif var[0] == "2":
    pod_name = var[2]
    image_name = var[1]
    cmd = "kubectl run " + (pod_name) + " --image=" + (image_name)
    output = subprocess.getoutput("sudo " + cmd + " --kubeconfig /root/k8s_tasks/admin.conf")
    print(output)
elif var[0] == "3":
    pod_name = var[1]
    cmd = "kubectl delete pod " + (pod_name)
    output = subprocess.getoutput("sudo " + cmd + " --kubeconfig /root/k8s_tasks/admin.conf")
    print(output)
elif var[0] == "4":
    deployment_name = var[1]
    cmd = "kubectl delete deployment " + (deployment_name)
    output = subprocess.getoutput("sudo " + cmd + " --kubeconfig /root/k8s_tasks/admin.conf")
    print(output)
elif var[0] == "5":
    deployment_name = var[1]
    port_no = var[2]
    Expose_type =  var[3]
    cmd = "kubectl expose deployment " + (deployment_name) + " --port=" + (port_no) + " --type=" + (Expose_type)
    output = subprocess.getoutput("sudo " + cmd + " --kubeconfig /root/k8s_tasks/admin.conf")
    print(output)
elif var[0] == "6":
    deployment_name = var[1]
    replica = var[2]
    cmd = "kubectl scale deployment " + (deployment_name) + " --replicas=" + (replica)
    output = subprocess.getoutput("sudo " + cmd + " --kubeconfig /root/k8s_tasks/admin.conf")
    print(output)
elif var[0] == "7":
    cmd = "sudo kubectl get pods --kubeconfig /root/k8s_tasks/admin.conf"
    output = subprocess.getoutput(cmd)
    print(output)
elif var[0] == "8":
    cmd = "kubectl get deployments --kubeconfig /root/k8s_tasks/admin.conf"
    output = subprocess.getoutput("sudo " + cmd)
    print(output)
elif var[0] == "9":
    cmd = "kubectl get svc --kubeconfig /root/k8s_tasks/admin.conf"
    output = subprocess.getoutput(cmd)
    print(output)
elif var[0] == "10":
    cmd = "kubectl delete all --all --kubeconfig /root/k8s_tasks/admin.conf"
    output = subprocess.getoutput("sudo " + cmd)
    print(output)
elif var[0] == "11":
    print("command not found")

