import sys
import cv2
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QPushButton, QVBoxLayout, QWidget, QSlider



class VideoPlayer(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Video Player")
        self.video_label = QLabel()
        self.start_button = QPushButton("Start")                    #tart Button to start the video
        self.stop_button = QPushButton("Stop")                      #stop button to stop the video
        self.threshold_slider = QSlider(Qt.Horizontal)              #Place the horizontal slider
        self.threshold_slider.setMinimum(0)                         #slider grayscale minimum value 0
        self.threshold_slider.setMaximum(255)                       #slider gray scale maximum value is 255
        self.threshold_slider.setValue(127)                         #slider default value is 127
        self.start_button.clicked.connect(self.start_video)         #click to start the video capture
        self.stop_button.clicked.connect(self.stop_video)           #click to stop the video capture
        self.video_capture = cv2.VideoCapture(0)                    #open the camera device
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_frame)
        self.is_playing = False
        self.init_ui()

    def init_ui(self):                                              #Video player userinterface
        central_widget = QWidget()                                  #create widgets inside the window
        layout = QVBoxLayout()                                      #align the widgets horizontally
        layout.addWidget(self.video_label)                          #add videolabel                    
        layout.addWidget(self.start_button)                         #add start button
        layout.addWidget(self.stop_button)                          #add stop button
        layout.addWidget(self.threshold_slider)                     #add threshold slider
        central_widget.setLayout(layout)                            #set the layout to the widget
        self.setCentralWidget(central_widget)
        self.update_frame()
        self.show()                                                 #open interative window to display figures

    
    def start_video(self):
        if not self.is_playing:
            self.timer.start(30)
            self.is_playing = True

    def stop_video(self):
        if self.is_playing:
            self.timer.stop()
            self.is_playing = False

    def update_frame(self):
        ret, frame = self.video_capture.read()
        if ret:
            gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)        #converts color space to grayscale
            threshold_value = self.threshold_slider.value()
            _, binary_frame = cv2.threshold(gray_frame, threshold_value, 255, cv2.THRESH_BINARY)    #Thresh binary checks the next threshold value is either 0 / 255
            image = QImage(binary_frame, binary_frame.shape[1], binary_frame.shape[0], QImage.Format_Grayscale8)
            pixmap = QPixmap.fromImage(image)
            self.video_label.setPixmap(pixmap)

    def closeEvent(self, event):
        self.video_capture.release()                                    # close the video file
        event.accept()  



if __name__ == '__main__':
    app = QApplication(sys.argv)
    player = VideoPlayer()
    sys.exit(app.exec_())
