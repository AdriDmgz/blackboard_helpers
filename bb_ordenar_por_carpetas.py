import os

supported_formats = ['cs','zip','rar','7z','pdf','doc','docx']

def check_supported_format(filename):
	supported = False
	for format in supported_formats:
		if "."+format in filename:
			supported = True
			break
	return supported

files = os.listdir(".")
for f in files:
    if check_supported_format(f):
        try:
            ini_nombre_alumno = f.index('_')
            fin_nombre_alumno = f.index('_',ini_nombre_alumno+1)
            ini_nombre_script = fin_nombre_alumno+29
        except:
            None
        else:        
            nombre_alumno = f[ini_nombre_alumno+1:fin_nombre_alumno]
            nombre_script = f[ini_nombre_script:]
            print(nombre_alumno)
            print(nombre_script)
            try:
                os.mkdir("./"+nombre_alumno)
            except:
                None            
            os.rename("./"+f,"./"+nombre_alumno+"/"+nombre_script)
