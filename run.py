#!/usr/bin/env python

import os
import subprocess

if __name__ == '__main__':
   for cur, _dirs, files in os.walk("./"):
       for f in files:
          if f.endswith('run.sh'):
             old_dir = os.getcwd()
             os.chdir(cur)
             print(cur)
             print(f)
             p = subprocess.Popen(['bash', f])
             rc = p.wait()
             if rc != 0:
                raise NameError("error")
             os.chdir(old_dir)
