import dropbox
import cv2
import time
import random

startTime = time.time()

def takeSnapshot():
    number = random.randint(0,100)
    videoCaptureObject = cv2.VideoCapture(0)
    result = True
    while (result):
        ret,frame = videoCaptureObject.read()
        img_name = "img" + str(number) + ".png"
        cv2.imwrite(img_name,frame)
        startTime = time.time            
        result = False
    return(img_name)
    
    print ('snapShotTaken')
    videoCaptureObject.release()
    cv2.destroyAllWindows()
    
def uploadFiles(img_name):
    acessToken = 'iJOChwSTJ2YAAAAAAAAAAd0dRJMBHAErIhSFuDsUj0Jyv1J-y0B95SEeie7Y4NhL'
    file=img_name
    fileFrom=file
    fileTo = '/testFolder/'+(img_name)
    dbx = dropbox.Dropbox(accessToken)

    f = open(fileFrom, 'rb')
    dbx.files_upload(f.read(),fileTo,mode = dropbox.files.WriteMode.overwrite)
    print('file uploaded')
        
def main():
    while (True):
        if((time.time()-startTime>=300)):
            name = takeSnapshot()
            uploadFiles(name)

main()