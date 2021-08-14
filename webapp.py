#!/usr/bin/python3

import cgi
import subprocess
import time


print("content-type:  text/html")
print()

#time.sleep(10)
f=cgi.FieldStorage()
cmd=(f.getvalue("x")).lower()
depod=f.getvalue("y")
f2=f.getvalue("z")
ser_type=f.getvalue("c")
cmd=cmd.split()
#print(cmd)
#print(depod)
#print(f2)


#Launch/Run Pod
if(("make" in cmd) or ("launch" in cmd) or ("run" in cmd)  or ("create" in cmd)):
        if("pod" in cmd) or ("pods" in cmd):
                print(subprocess.getoutput("sudo kubectl run {} --image={} ".format(depod,f2)))

        elif("deployment" in cmd) or ("deployments" in cmd) or ("deploy" in cmd):
                print(subprocess.getoutput("sudo kubectl create deploy  {} --image={} ".format(depod,f2)))

#show resources
elif (("running" in cmd) or ("current" in cmd) or ("show" in cmd) or ("list" in cmd)):
        if (("pod" in cmd) or ("pods" in cmd) or ("po" in cmd)):
                print(subprocess.getoutput("sudo kubectl get pod"))
        elif (("deployment" in cmd) or ("deployments" in cmd) or ("deploy" in cmd)):
                print(subprocess.getoutput("sudo kubectl get deploy"))
        elif (("service" in cmd) or ("services" in cmd) or ("svc" in cmd)):
                print(subprocess.getoutput("sudo kubectl get svc"))


#Delete Entire environment
elif (("remove" or "delete" or "terminate") and "environment") in cmd:
    print(subprocess.getoutput("sudo kubectl delete all --all"))


#Delete specific resources
elif(("remove" in cmd) or ("delete" in cmd) or ("terminate" in cmd)):
        if(("pod" in cmd) or ("pods" in cmd)):
                print(subprocess.getoutput("sudo kubectl delete po {} ".format(depod)))
        elif(("deployment" in cmd) or ("deployments" in cmd)):
                print(subprocess.getoutput("sudo kubectl delete deploy {} ".format(depod)))
        elif(("service" in cmd) or ("services" in cmd) or ("svc" in cmd)):
                print(subprocess.getoutput("sudo kubectl delete service {} ".format(depod)))


#Expose services on given port number
elif (("expose" in cmd) or ("launch" in cmd) or ("create")):
        if (("services" in cmd) or ("service" in cmd) or ("svc" in cmd) or ("deployment" in cmd) or ("deployments" in cmd)):
                print(subprocess.getoutput("sudo kubectl expose deploy {} --port={} --type={}".format(depod,f2,ser_type)))


#Scale resources or create replicas
elif (("replicas" in cmd) or ("replica" in cmd) or ("scale" in cmd)  or ("scale" in cmd)):
        if (("pod" in cmd) or ("deployment" in cmd) or ("deployments" in cmd) or ("deploy" in cmd) or ("pods" in cmd)):
                print(subprocess.getoutput("sudo kubectl scale deploy {} --replicas={} ".format(depod,f2)))

else:
    print("Plz enter your command again")
