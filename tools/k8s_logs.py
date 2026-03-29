import subprocess

def get_pod_logs():
    cmd = "kubectl logs $(kubectl get pods -l app=crash-app -o jsonpath='{.items[0].metadata.name}')"
    result = subprocess.getoutput(cmd)
    return result