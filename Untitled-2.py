
from PyQt6.QtWidgets import QWidget,QLabel,QApplication,QVBoxLayout

app=QApplication([])
w=QWidget()
layout=QVBoxLayout()
l1=QLabel()
l1.setText('1')
l2=QLabel()
l2.setText('2')
l3=QLabel()
l3.setText('3')
layout.addWidget(l1)
layout.addWidget(l2)
layout.addWidget(l3)
w.setLayout(layout)
w.show()


for i in range(layout.count()): 
    layout.itemAt(i).widget().deleteLater()

l2.setParent(None)
layout.addWidget(QLabel('7'))
layout.addWidget(l2)

app.exec()