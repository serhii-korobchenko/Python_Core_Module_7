from dataclasses import replace
import os
from pathlib import Path
import re
import shutil
import sys

#SET_UPS######################################################3

### Set up data containers
set_files_images = set()
set_files_documents = set()
set_files_audio = set()
set_files_video = set()
set_files_archives = set()
set_fam_extension = set()
set_unfam_extension = set()

### Set_up for normilize function
CYRILLIC_SYMBOLS = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяєіїґ"
TRANSLATION = ("a", "b", "v", "g", "d", "e", "e", "j", "z", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u",
               "f", "h", "ts", "ch", "sh", "sch", "", "y", "", "e", "yu", "ya", "je", "i", "ji", "g")

TRANS = {}

# Create dict trans with help of zip()
for c, l in zip(CYRILLIC_SYMBOLS, TRANSLATION):
    TRANS[ord(c)] = l
    TRANS[ord(c.upper())] = l.upper()

#DEF#################################################

def search_function (path, k_space, report):   
    """ Function scan intendent folder at all levels of nestiness and find files and 
    folders with defined extensions.

    First parametr (path) - reveal carrent processing folder
    Second parametr (k_space) - regulate emty space for diferenciation levels of nestiness """

    k_space += 1
    space = " " * 3 * k_space
    
    if len(os.listdir(path)) == 0: # base case
        # Delete empty folders
        #Path.rmdir(path)
        return 
    else:
        for i in path.iterdir():
            
            on_print = '{:<0} {:<100} {:<10}'.format(space, i.name, 'Folder' if i.is_dir() else 'File')
            
            report.write(on_print + '\n')
            
            if i.is_dir() and i != 'images' and i != 'documents' and i != 'audio' and i != 'video' and i != 'archives' :
                ### All our activities with folders

                path = Path.joinpath(path, i)
                search_function (path, k_space, report) # recursive case
                
                # Delete empty folders or rename it
                if len(os.listdir(i)) == 0: 
                    Path.rmdir(i)
                
                else:
                    #rename_folder ----> path = i
                    rename_func (i)

            else:
                ### All our activities with files + archives
                #rename_files ----> path = i
                i = rename_func (i)
                                               
                ### Files GRID
                
                # images
                if i.suffix == '.jpeg' or i.suffix == '.png' or i.suffix == '.jpg' or i.suffix == '.svg':
                    
                    #add file in images list
                    set_files_images.add(os.path.basename(i))
                    
                    # add sufix to familiar list
                    set_fam_extension.add(i.suffix)
                    process_pictures (i)

                # video
                elif i.suffix == '.avi' or i.suffix == '.mp4' or i.suffix == '.mov' or i.suffix == '.mkv':
                    
                    #add file in video list
                    set_files_video.add(os.path.basename(i))
                   
                    # add sufix to familiar list
                    set_fam_extension.add(i.suffix)
                    
                    process_video (i)
                
                # documents
                elif i.suffix == '.doc' or i.suffix == '.docx' or i.suffix == '.txt' or i.suffix == '.pdf' or i.suffix == '.xlsx' or i.suffix == '.pptx':
                    
                    #add file in video list
                    set_files_documents.add(os.path.basename(i))
                   
                    # add sufix to familiar list
                    set_fam_extension.add(i.suffix)
                    
                    process_documents (i)
                
                # audio
                elif i.suffix == '.mp3' or i.suffix == '.ogg' or i.suffix == '.wav' or i.suffix == '.amr':
                    
                    #add file in video list
                    set_files_audio.add(os.path.basename(i))
                  
                    # add sufix to familiar list
                    set_fam_extension.add(i.suffix)
                    
                    process_audio (i)
                
                # archives
                elif i.suffix == '.zip' or i.suffix == '.gz' or i.suffix == '.tar':
                    
                    #add file in video list
                    set_files_archives.add(os.path.basename(i))
                  
                    # add sufix to familiar list
                    set_fam_extension.add(i.suffix)
                    
                    process_archives (i)
                else:
                    set_unfam_extension.add(i.suffix)

                continue                              

    k_space -= 1
    
    return k_space, set_files_images, set_files_documents, set_files_audio, set_files_video, set_files_archives, report

def namestr(obj, namespace):
    """ Function return name of veriable in string"""
    
    return [name for name in namespace if namespace[name] is obj]

def set_prep_for_write (set_x):
    """ Function write list of categories in report file"""

    with open('report.txt', 'a') as report:
        
        report.write(f'{namestr(set_x, globals())}: \n') 
        for item in set_x:
           report.write(str(item) + '\n') 
        report.write('\n\n')
    return namestr(set_x, globals())

def normalize (name):
    """ Function normalize names files and folders"""
    
    p = name.translate(TRANS)
    result = re.sub(r'[^a-zA-Z0-9\.]', '_', p)
    return result

def rename_func (path):

    path_file_item = Path (path)
    path_folder_item = path_file_item.parent.absolute()
    old_name = os.path.basename(path_file_item)               
    new_name = normalize (old_name)
    new_name_path = Path.joinpath(path_folder_item, new_name)

    if new_name != old_name:
        os.rename(path_file_item, new_name_path, src_dir_fd=None, dst_dir_fd=None)
    
    path = new_name_path
    return path

def process_pictures (path):
    """ Function process pictures category"""
    
    #print ('In Path >>>>', path)
    # Make dir if it does not exist yet
    path_base = Path.joinpath(Path(sys.argv[1]), 'images')

    isExist = os.path.exists(path_base) # Check whether the specified path exists or not

    if not isExist:
        os.makedirs(path_base)  # Create a new directory because it does not exist 
        #print("Images directory has been created!")

    file_name = os.path.basename(path)
    
    dest_pass = Path.joinpath(path_base, file_name)
    #print ('Dest path>>>>', dest_pass)
    
    shutil.move(path, dest_pass)
        
def process_video (path):
    """ Function process video category"""
        
    # Make dir if it does not exist yet
    path_base = Path.joinpath(Path(sys.argv[1]), 'video')
    
    isExist = os.path.exists(path_base) # Check whether the specified path exists or not

    if not isExist:
        os.makedirs(path_base)  # Create a new directory because it does not exist 
        #print("Video directory has been created!")

    file_name = os.path.basename(path)
    
    dest_pass = Path.joinpath(path_base, file_name)
    #print ('Dest path>>>>', dest_pass)
    
    shutil.move(path, dest_pass)

def process_documents (path):
    """ Function process documents category"""
    
    # Make dir if it does not exist yet
    path_base = Path.joinpath(Path(sys.argv[1]), 'documents')
    
    isExist = os.path.exists(path_base) # Check whether the specified path exists or not

    if not isExist:
        os.makedirs(path_base)  # Create a new directory because it does not exist 
        #print("Documents directory has been created!")

    file_name = os.path.basename(path)
    
    dest_pass = Path.joinpath(path_base, file_name)
    #print ('Dest path>>>>', dest_pass)
    
    shutil.move(path, dest_pass)

def process_audio (path):
    """ Function process music category"""
    
    # Make dir if it does not exist yet
    path_base = Path.joinpath(Path(sys.argv[1]), 'audio')
    
    isExist = os.path.exists(path_base) # Check whether the specified path exists or not

    if not isExist:
        os.makedirs(path_base)  # Create a new directory because it does not exist 
        #print("Audio directory has been created!")

    file_name = os.path.basename(path)
    
    dest_pass = Path.joinpath(path_base, file_name)
    #print ('Dest path>>>>', dest_pass)
    
    shutil.move(path, dest_pass)

def process_archives (path):
    """ Function process archives category"""
    
    # Make dir if it does not exist yet
    path_base = Path.joinpath(Path(sys.argv[1]), 'archives')
    
    isExist = os.path.exists(path_base) # Check whether the specified path exists or not

    if not isExist:
        os.makedirs(path_base)  # Create a new directory because it does not exist 
        #print("Archives directory has been created!")

    file_name = os.path.basename(path)
    
    dest_pass = Path.joinpath(path_base, file_name)
    #print ('Dest path>>>>', dest_pass)
    
    shutil.move(path, dest_pass)
    shutil.unpack_archive(dest_pass, path_base)
    os.remove(dest_pass)

#MAIN_BODY########################################

def start():


    print('LOG:')
    #print(f'Target folder is: {p}.')
            
    with open('report.txt', 'w') as report:
                    
        if sys.argv[1]:
            p = Path(sys.argv[1])
            print(f'Target folder is: {p}.')
                    
            report.write('File structure processing:' + '\n\n')
            search_function (p, 0, report)
            report.write('\n\n\n')

    print (f'You could read report file (report.txt) in your current directory')
    set_prep_for_write (set_files_images)
    set_prep_for_write (set_files_documents)
    set_prep_for_write (set_files_audio)
    set_prep_for_write (set_files_video)
    set_prep_for_write (set_files_archives)
    set_prep_for_write (set_fam_extension)
    set_prep_for_write (set_unfam_extension)

   

if __name__ == '__main__':
    start()
    
    



# python D:\PYTHON\Python_Core_Module_7\Home_Works\clean_folder\clean_folder\clean.py D:\TEST\Garbage
# Clean-folder D:\TEST\Garbage