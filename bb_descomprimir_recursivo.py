import os
import subprocess

def uncompress_all():

    unity_folders = []
    paths_to_check = ["."]
    while len(paths_to_check) > 0:

        path = paths_to_check[0]
        del paths_to_check[0]
        
        files = os.listdir(path)
        for f in files:
            path_to_f = path+'/'+f
            if os.path.isdir(path_to_f):
                paths_to_check.append(path_to_f)
            else:
                if '.7z' in f or '.zip' in f or '.rar' in f:
                    print('Uncompressing',path_to_f)
                    file_name = f[:f.rfind('.')]
                    dest_path = path+'/'+file_name
                    os.mkdir(dest_path)
                    
                    cmd = ['7z','x',path_to_f,'-o'+dest_path]
                    sp = subprocess.Popen(cmd, stderr=subprocess.STDOUT, stdout=subprocess.PIPE)

uncompress_all()
