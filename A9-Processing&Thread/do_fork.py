#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os

print('Process (%s) start...' % os.getpid())
# Only works on Unix/Linux/Mac:
pid = os.fork()
if pid == 0:
    print('I am child process (%s) and my parent is %s.' % (os.getpid(), os.getppid()))  #os.getpid()是子进程的id, os.getppid()是父进程的id
else:
    print('I (%s) just created a child process (%s).' % (os.getpid(), pid))

