def get_standards_version():
    for line in open('/usr/share/lintian/data/standards-version/release-dates').readlines():
        line = line.strip()
        if not line: continue
        if line.startswith('#'): continue
        return line.split()[0].strip()

import subprocess

def git_cmd(d, *args):
    args = ['"%s"'%a if ' ' in a else a for a in args]
    cmd = 'git -C %s %s'%(d, ' '.join(args))
    print(cmd)
    proc = subprocess.Popen(args=[cmd], stdout=subprocess.PIPE, shell=True)
    if proc.wait() != 0: raise Exception("Failed %s"%cmd)
    return proc.communicate()[0].decode('utf-8')
