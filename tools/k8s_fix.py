def fix_pod_issue():
    fix_cmd = "kubectl rollout restart deployment crash-app"
    return subprocess.getoutput(fix_cmd)