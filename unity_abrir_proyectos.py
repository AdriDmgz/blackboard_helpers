import os
import subprocess

def get_students_projects_dict():

    projects_dict = {}
    
    stundents_folders = os.listdir('.')
    for folder in stundents_folders:
        path_to_folder = './'+folder
        if os.path.isdir(path_to_folder):
            unity_projects = get_unity_projects(folder)
            projects_dict[folder] = unity_projects

    return projects_dict
            
def get_unity_projects(folder):
    
    unity_folders = []
    paths_to_check = [folder]
    while len(paths_to_check) > 0:

        path = paths_to_check[0]
        del paths_to_check[0]
        
        files = os.listdir(path)
        if "Assets" in files:           
            unity_folders.append(path)
        else:
            for f in files:
                path_to_f = path+'/'+f
                if os.path.isdir(path_to_f):
                    paths_to_check.append(path_to_f)

    return unity_folders

def open_unity_project(path):
    
    mayor_version,minor_version = get_unity_project_mayor_minor_version(path)
    unity_folder = find_best_unity_installment_path(mayor_version,minor_version)
    if unity_folder == None:
        print('No se ha encontrado una instalación de Unity',mayor_version,'para abrir el proyecto',path)
    else:
        print('Abriendo: ',path)
        cmd = [unity_folder+'/Editor/Unity.exe','-projectPath',path]
        sp = subprocess.Popen(cmd, stderr=subprocess.STDOUT, stdout=subprocess.PIPE)

def get_unity_project_mayor_minor_version(path):
    unity_version_path = path + "/ProjectSettings/ProjectVersion.txt"
    f = open(unity_version_path, "r")
    file_contents = f.readline()
    mayor_version = file_contents[17:23]   
    minor_version = file_contents[24:-3]    
    return mayor_version,minor_version
    
def find_best_unity_installment_path(project_mayor_version,project_minor_version):
    base_path = 'D:/Unity/Hub'
    unity_folders = os.listdir(base_path)
    
    max_minor_version = 0
    selected_unity_folder = None
    
    for folder in unity_folders:
    
        folder_version = folder[:6]
        folder_minor_version = int(folder[7:-2])
        print('Found Unity ',folder_version,folder_minor_version)
		
        if folder_version == project_mayor_version:
        
            if folder_minor_version == int(project_minor_version):
                selected_unity_folder = folder
                break
                
            if folder_minor_version > max_minor_version:
                selected_unity_folder = folder
                max_minor_version = folder_minor_version
                
    return base_path+'/'+selected_unity_folder
    
    
        
projects_dict = get_students_projects_dict()
lista_alumnos = list(projects_dict.keys())

opcion = ''
while opcion != 'Q':
    print()
    print('Estos son los alumnos:')
    i = 1
    for a in lista_alumnos:
        print(str(i)+'.',a)
        i += 1
    opcion = input('¿Qué proyecto quiere abrir? (Q para salir): ')
    try:
        n_alumno = int(opcion)-1
    except:
        None
    else:
        if n_alumno > len(lista_alumnos): continue
        alumno = lista_alumnos[n_alumno]
        proyectos = projects_dict[alumno]
        if len(proyectos) == 0:
            print('La carpeta no contiene proyectos')
        elif len(proyectos) == 1:
            print('Abriendo: ',proyectos[0])
            open_unity_project(proyectos[0])
        else:
            print('Estos son sus proyectos:')
            j =1
            for p in proyectos:
                print(str(j)+'.',p)
                j += 1
            opcion = input('¿Cúal de ellos quiere abrir? (Q para salir): ')
            try:
                n_proyecto = int(opcion)-1
            except:
                None
            else:
                if n_proyecto > len(proyectos): continue
                proyecto = proyectos[n_proyecto]                
                open_unity_project(proyecto)
