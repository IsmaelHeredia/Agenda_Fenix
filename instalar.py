#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Written By Ismael Heredia in the year 2018

from subprocess import call

print("[+] Instalando ...")

call(["python","manage.py","makemigrations"])
call(["python","manage.py","migrate"])

print("\n[+] Instalación terminada")