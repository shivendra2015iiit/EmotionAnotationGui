import cv2
import os
import sys
import re
from tkinter import filedialog
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtWidgets import QMainWindow,QApplication,QDialog,QFileDialog
from PyQt5 import QtMultimedia,QtCore
from ui_main import Ui_MainWindow


class EmotionAnnotationUi:
    def __init__(self):
        self.videolist = []  # save the list of unwatched videos
        self.watched = []    # Save the list of watched videos
        self.emotion = 0    # store the numerical value of emotion
        self.saved = 0      # Flag to check video anotation is saved or not before pressing next
        self.image=None
        self.cap = None
        self.timer=None

        self.main_win = QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.main_win)
        self.ui.currentfolder=None
        self.ui.currentvideo=None
        self.ui.folderpath.setText("No Folder Selected")
        self.ui.emotion.setText("None")
        self.ui.Videoname.setText("None")
        self.ui.folder.clicked.connect(self.selectfolder)
        self.ui.save.clicked.connect(self.saveclicked)

        self.ui.replay.clicked.connect(self.replayclicked)
        self.ui.next.clicked.connect(self.nextclicked)

        self.ui.angry.clicked.connect(self.angryclicked)
        self.ui.happy.clicked.connect(self.happyclicked)
        self.ui.sad.clicked.connect(self.sadclicked)
        self.ui.surprise.clicked.connect(self.surpriseclicked)
        self.ui.disgust.clicked.connect(self.disgustclicked)
        self.ui.fear.clicked.connect(self.fearclicked)
        self.ui.noemotion.clicked.connect(self.noemotionclicked)
        self.ui.uncertain.clicked.connect(self.uncertainclicked)

    def selectfolder(self):

        file_path = None
        file_path = QFileDialog.getExistingDirectory(None, 'Select Video Folder', os.getcwd())
        #file_path = filedialog.askopenfilename()
        if (file_path!=None):
            self.currentfolder =file_path
            self.videolist = [f for f in os.listdir(self.currentfolder) if re.match(r'.*\.mkv', f)]
            self.ui.folderpath.setText(self.currentfolder)
            if(self.videolist!=[]):
                self.currentvideo = self.videolist.pop()
                self.ui.Videoname.setText(self.currentvideo)
            else:
                pass

        else:
            pass

        #select the folder #set the path on display folderpath.setText


#made a folder inside same folderpath with annotation and mark the
#current emotion
#1  Happy
#2  Sad
#3  Surprise
#4  Disgust
#5  Fear
#6  Angry
#7  Uncertain
#8  Noemotion
# Load the player with next emotion
    def saveclicked(self):
        if(self.emotion!=0):
            if not os.path.exists(self.currentfolder+"/annotation/"):
                os.makedirs(self.currentfolder+"/annotation/")
            file= open(self.currentfolder+"/annotation/"+self.currentvideo+".txt",'w+')
            file.write(str(self.emotion))
            file.close()
            self.saved=1
        else:
            self.saved=0
            self.ui.emotion.setText("Select Anotation")
        self.ui.emotion.setText("Select Anotation")
        self.emotion=0

    def replayclicked(self):
        self.saved = 0
        self.cap=cv2.VideoCapture(self.currentfolder+"/"+self.currentvideo)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT,381)
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH,571)

            # cv2.imshow('window-name',frame)
            # cv2.imwrite("frame%d.jpg" % count, frame)
        self.timer=QTimer()
        self.timer.timeout.connect(self.update_frame)
        self.timer.start(40)


        self.update_frame

        #play the first video
    def update_frame(self):
        ret,frame = self.cap.read()
        if frame is not None:
            self.image = frame
            self.display_image(self.image,1)
        else:
            pass

    def display_image(self,img,window=1):
        qformat=QImage.Format_RGB888
        outimage = QImage(img,img.shape[1],img.shape[0],img.strides[0],qformat)
        outimage = outimage.rgbSwapped()
        self.ui.videoplayer.setPixmap(QPixmap.fromImage(outimage))
        self.ui.videoplayer.setScaledContents(True)

#Go to the next video
    def nextclicked(self):
        if (self.saved==0):
            self.ui.emotion.setText("UnSaved Data")
        else:

            self.watched.append(self.currentvideo)
            if(len(self.videolist)!=0):
                self.currentvideo=self.videolist.pop()
                self.ui.Videoname.setText(self.currentvideo)
                self.timer.stop()
                self.replayclicked()
            else:
                self.ui.Videoname.setText("All Done!!! ")





    def angryclicked(self):
        self.emotion=6
        self.ui.emotion.setText("Angry")

    def happyclicked(self):
        self.emotion=1
        self.ui.emotion.setText("happy")

    def sadclicked(self):
        self.emotion=2
        self.ui.emotion.setText("sad")

    def surpriseclicked(self):
        self.emotion=3
        self.ui.emotion.setText("surprise")

    def disgustclicked(self):
        self.emotion=4
        self.ui.emotion.setText("disgust")

    def fearclicked(self):
        self.emotion=5
        self.ui.emotion.setText("fear")

    def noemotionclicked(self):
        self.emotion=8
        self.ui.emotion.setText("NoEmotion")

    def uncertainclicked(self):
        self.emotion=7
        self.ui.emotion.setText("Uncertain")


    def show(self):
        self.main_win.show()

    def setTitle(self,s):
        self.main_win.setWindowTitle(s)





# root = tk.Tk()
# root.withdraw()
#
# file_path = filedialog.askopenfilename()


if __name__=='__main__':

    app= QApplication(sys.argv)
    window = EmotionAnnotationUi()
    window.setTitle("EmotionAnnotation")
    window.show()
    sys.exit(app.exec_())
