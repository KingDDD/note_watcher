#!/usr/bin/env python3

import os
import sys
import threading
import subprocess

WATCH_DIR = os.path.join('/','home','d')
TARGET_DIR = os.path.join('/','home','d','workspace','notes')

def worker():
    files = os.listdir(WATCH_DIR)
    for f in files:
        if f.endswith('.py'):
            subprocess.call([
            'mv', '{}'.format(os.path.join(WATCH_DIR, f)),
            '{}'.format(os.path.join(TARGET_DIR, 'python_files',f))
            ])
        elif f.endswith('.txt'):
            subprocess.call([
            'mv', '{}'.format(os.path.join(WATCH_DIR, f)),
            '{}'.format(os.path.join(TARGET_DIR, 'note_files',f))
            ])
        elif f.endswith('.sh'):
            subprocess.call([
            'mv', '{}'.format(os.path.join(WATCH_DIR, f)),
            '{}'.format(os.path.join(TARGET_DIR, 'bash_files',f))
            ])
        elif f.endswith('.json'):
            subprocess.call([
            'mv', '{}'.format(os.path.join(WATCH_DIR, f)),
            '{}'.format(os.path.join(TARGET_DIR, 'json_files',f))
            ])
        elif f.endswith('.yaml'):
            subprocess.call([
            'mv', '{}'.format(os.path.join(WATCH_DIR, f)),
            '{}'.format(os.path.join(TARGET_DIR, 'yaml_files',f))
            ])
        else:
            pass

def watcher():
    threading.Timer(10.0, watcher).start()
    worker()

def main():
    watcher()

main()
