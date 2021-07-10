"""
Necesita estar creada la carpeta media en ./

Hay que añadir un asterisco al inicio de un remote path si quieres descargar una carpeta de forma recursiva.
"""

import os
import pysftp
from getpass import getpass
from stat import S_ISDIR, S_ISREG

cnopts = pysftp.CnOpts()
cnopts.hostkeys = None

myHostname = "estadodelmce.es"
myUsername = "root"
myPassword =  getpass('Clave: ')
myPort = 1917


def get_r_portable(sftp, remotedir, localdir, preserve_mtime=False):
    for entry in sftp.listdir(remotedir):
        remotepath = remotedir + "/" + entry
        localpath = os.path.join(localdir, entry)
        mode = sftp.stat(remotepath).st_mode
        if S_ISDIR(mode):
            try:
                os.mkdir(localpath,mode=777)
            except OSError:     
                pass
            get_r_portable(sftp, remotepath, localpath, preserve_mtime)
        elif S_ISREG(mode):
            sftp.get(remotepath, localpath, preserve_mtime=preserve_mtime)


with pysftp.Connection(host=myHostname, username=myUsername, password=myPassword, port=myPort, cnopts=cnopts ) as sftp:
    print("Conexión dabuti")

    remoteFilePaths = [
        '/home/manel/estadodelmce/db.sqlite3',
        '*/home/manel/estadodelmce/media',
    ]

    for remoteFilePath in remoteFilePaths:
        resourceName = str(remoteFilePath.split('/')[-1])

        if not remoteFilePath.startswith('*'): # File
            localFilePath = './' + resourceName
            sftp.get(remoteFilePath, localFilePath)
        else: # Folder
            localFilePath = './' + resourceName + '/'
            remoteFilePath = remoteFilePath[1:]
            get_r_portable(sftp, remoteFilePath, localFilePath, preserve_mtime=False)