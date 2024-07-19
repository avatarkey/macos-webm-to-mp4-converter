import sys
import os
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget
from PyQt6.QtCore import Qt, QThread, pyqtSignal
import subprocess

class ConversionThread(QThread):
    update_signal = pyqtSignal(str)

    def __init__(self, input_file):
        QThread.__init__(self)
        self.input_file = input_file

    def run(self):
        output_file = os.path.splitext(self.input_file)[0] + '.mp4'
        ffmpeg_cmd = [
            'ffmpeg',
            '-i', self.input_file,
            '-c:v', 'libx264',
            '-crf', '23',
            '-c:a', 'aac',
            '-q:a', '100',
            output_file
        ]
        
        try:
            subprocess.run(ffmpeg_cmd, check=True, capture_output=True, text=True)
            self.update_signal.emit(f"Successfully converted {self.input_file}")
        except subprocess.CalledProcessError as e:
            self.update_signal.emit(f"Error converting {self.input_file}: {e}")

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("WEBM to MP4 Converter")
        self.setGeometry(100, 100, 300, 200)
        self.setAcceptDrops(True)

        layout = QVBoxLayout()
        self.label = QLabel("Drag and drop .webm files here")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.label)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):
        files = [u.toLocalFile() for u in event.mimeData().urls()]
        for file_path in files:
            if file_path.lower().endswith('.webm'):
                self.convert_file(file_path)
            else:
                self.label.setText(f"Unsupported file: {file_path}")

    def convert_file(self, file_path):
        self.thread = ConversionThread(file_path)
        self.thread.update_signal.connect(self.update_label)
        self.thread.start()

    def update_label(self, message):
        self.label.setText(message)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
