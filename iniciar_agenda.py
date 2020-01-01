#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Written By Ismael Heredia in the year 2020

import os
from shutil import copyfile
from subprocess import call
from threading import Thread
import time

def start_navigator():
    time.sleep(5)
    call([ruta_chrome,url])

puerto = "8000"
directorio_agenda = os.getcwd()
directorio_chrome = "C:\\Program Files (x86)\\Google\\Chrome\\Application"
ruta_chrome = directorio_chrome + "\\" + "chrome.exe"
url = "http://localhost:" + puerto

print("[!] Iniciando Agenda ...\n")

print("[+] Creando backup de la base de datos ...")

ruta_db = directorio_agenda + "/" + "db.sqlite3"
ruta_backup = directorio_agenda + "/" + "db_backup.sqlite3"

if os.path.exists(ruta_db):
    if os.path.isfile(ruta_backup):
	    os.remove(ruta_backup)
    if copyfile(ruta_db,ruta_backup):
	    print("[+] Backup realizado correctamente")
    else:
	    print("[-] Error haciendo backup")

print("[+] Iniciando timer para cargar navegador despues de iniciar servidor ...")

thread_navigator = Thread(target=start_navigator)
thread_navigator.start()

print("[+] Iniciando servidor ...")

call(["python","manage.py","runserver",puerto])
