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
        
projects_dict = get_students_projects_dict()
alumns_list = list(projects_dict.keys())
for alumn in alumns_list:
	projects = projects_dict[alumn]
	for p in projects:
		manifest_path = p + '/packages/manifest.json'
		
		print('Fixing packages for project:',p)
		manifest_file = open(manifest_path,'r')
		manifest_lines = manifest_file.readlines()
		
		for line in manifest_lines:
			if 'com.unity' in line:
				if 'modules' not in line:
					print('Removing',line[:-1],'line from manifest')
					manifest_lines.remove(line)
					
		new_manifest = ''.join(manifest_lines)
		manifest_file.close()
		
		manifest_file = open(manifest_path,'w+')
		manifest_file.write(new_manifest)
		manifest_file.close()
			
		
			
