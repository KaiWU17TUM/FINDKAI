from Classifier import Classifier as CF
from ImageModule import ImageModule as IM
#import SoundModule as SM
import os

class Roboy:
    def __init__(self):
        self.im = IM()
        self.cf = CF()
        #self.sm = SM()
        self.FACES_PATH = "faces"
        self.TEMP_PATH = "temp"
        self.sm = SoundModule()
        if not os.path.exists(self.FACES_PATH):
            os.makedirs(self.FACES_PATH)
        if not os.path.exists(self.TEMP_PATH):
            os.makedirs(self.TEMP_PATH)
        print("roboy instance made!")

    def addFaceToMemmory(self,name):
        faceimage = self.im.take_photo()
        [fl,fe,fn] = self.cf.findFaces(faceimage)
        if name =="unknown":
            print("That's a shitty name!")
            return False #and not impressed
        elif len(fl)>1 :
            print("Too Many faces bro!.. give me some air!")
            return False  # and frustrated
        elif (len(fl)==1 and  fl[0]== CF.UNKNOWN and fl[0]==name):
            print("You trying to fool me mate? You are not "+name+"! get lost!")
            return False # and angry
        self.im.save(faceimage,name,self.FACES_PATH)
        self.cf.train(self.FACES_PATH)# can be optimized - Later!!
        print("Hello!, nice to meet you "+name)
        return True # and happy face

    def lookForPersonInImage(self,target_name,image):
        fe,fl,fn = self.cf.findFaces(image)
        for i,name in enumerate(fn):
            #print("found "+str(name))
            #print(name,CF.UNKNOWN,target_name, name is not CF.UNKNOWN,name == target_name, name is not CF.UNKNOWN and name == target_name)
            if name is not CF.UNKNOWN and name == target_name:
                #print("got here!")
                return  fe[i], fl[i], fn[i]
                #return  fl[i],fe[i],fn[i]  # return the found image
        return None,None,None # else you found nothing
                
            
    def listen(self):
        while(True):
            phrase = self.sm.getNextPhrase()
            if("my name is" in phrase):
                name = phrase.rsplit(' ',1)[1]
                print("name: ",name)
                self.addFaceToMemmory(name)
            if("find " in phrase):
                name = phrase.rsplit(' ',1)[1]
                x,y,z = self.lookForPersonInImage(name,self.im.take_photo())
                if(x is None):
                    print("couldn't find "+name+" sorry!")
                else:
                    print("There is "+name+"!!")
            

class SoundModule:
    def __init__(self):
        print("Sound Module Initialized");
    
    def getNextPhrase(self):
        phrase = input('I am Listening..')
        return phrase
    
        
    