# coding: UTF-8  

import os
import zipfile   

def zip_dir(dirname, zipfilename):
    filelist = []
    if os.path.isfile(dirname):
        filelist.append(dirname)
    else :
        for dirpath, dirnames, filenames in os.walk(dirname):  # @UnusedVariable
            for name in filenames:
                filelist.append(os.path.join(dirpath, name))
         
    zf = zipfile.ZipFile(zipfilename, "w", zipfile.ZIP_DEFLATED)
    for tar in filelist:
        arcname = tar[len(dirname):]
        zf.write(tar, arcname)
    zf.close()
    
if __name__ == "__main__":
    zip_dir("./web/", "./web.zip")
