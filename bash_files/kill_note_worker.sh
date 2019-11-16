#!/usr/bin/env bash

ps axf | grep note_worker.py | grep -v grep | awk '{print "kill -9 " $1}' | sh

