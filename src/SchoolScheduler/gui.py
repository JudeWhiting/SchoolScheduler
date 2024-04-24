import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton

def button_clicked():
    print("Button clicked!")

# Create a new application instance
app = QApplication(sys.argv)

# Create a new QWidget (window)
window = QWidget()

# Set the window title
window.setWindowTitle('Button Example')

# Set the window size
window.setGeometry(100, 100, 300, 200)

# Create a QPushButton
button = QPushButton('Click Me', window)

# Move the button to a specific location
button.move(100, 80)

# Connect the button's clicked signal to a function
button.clicked.connect(button_clicked)

# Show the window
window.show()

# Start the application event loop
sys.exit(app.exec_())
