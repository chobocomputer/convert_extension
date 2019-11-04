import os, datetime, time

from PIL import Image



################## make direc #########################################
def makedirec():
    global naljja, naldirec
    
    naljja = datetime.datetime.now()
    naldirec = naljja.strftime('%Y%m%d_%H%M%S')
    os.makedirs(naldirec)
#######################################################################



################## nameoji_png     ####################################
def nameoji_png():
        original_image = Image.open(filename)

        file_front_name, file_back_name = os.path.splitext(filename)
                       
        original_image.save(os.path.join(naldirec, file_front_name + '.png'))

        original_image.close()   
#######################################################################



################## exist file #########################################
def exist_file():
    if (filename.lower().endswith('.gif') or filename.lower().endswith('.jpg') or filename.lower().endswith('.bmp') or filename.lower().endswith('.pcx')):
        return True
    

#######################################################################

   


################## main       #########################################

naljja = 0
naldirec = 0
makedirec()

for filename in os.listdir('.'):
    if exist_file():    
        nameoji_png()

#######################################################################
