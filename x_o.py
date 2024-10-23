from PyQt5.QtWidgets import *                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            
class mywin(QWidget):                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            
    def __init__(self):                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        
        super().__init__()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          
        self.tablitsa=QGridLayout()  
        self.h_lay=QHBoxLayout()
        self.v_main=QVBoxLayout()
        self.count=0

        self.btn1=QPushButton("",clicked=lambda:self.Btn(self.btn1))
        self.btn2=QPushButton("",clicked=lambda:self.Btn(self.btn2))
        self.btn3=QPushButton("",clicked=lambda:self.Btn(self.btn3))
        self.btn4=QPushButton("",clicked=lambda:self.Btn(self.btn4))
        self.btn5=QPushButton("",clicked=lambda:self.Btn(self.btn5))
        self.btn6=QPushButton("",clicked=lambda:self.Btn(self.btn6))
        self.btn7=QPushButton("",clicked=lambda:self.Btn(self.btn7))
        self.btn8=QPushButton("",clicked=lambda:self.Btn(self.btn8))
        self.btn9=QPushButton("",clicked=lambda:self.Btn(self.btn9))

        self.btn_start=QPushButton("Start",clicked=self.start)
        self.btn_exit=QPushButton("Exit",clicked=exit)
        self.btn_finish=QPushButton("Finish",clicked=self.finish)
        self.btn_finish.hide()

        self.h_lay.addWidget(self.btn_start)
        self.h_lay.addWidget(self.btn_finish)
        self.h_lay.addWidget(self.btn_exit)
        


        self.lst = [self.btn1,self.btn2,self.btn3,self.btn4,self.btn5,
                    self.btn6,self.btn7,self.btn8,self.btn9]

        index=0
        for i in range(3):                                                                                                                                                                                                                                                                                                                                                                      
            for j in range(3):                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           
                self.lst[index].setFixedSize(50,50)
                self.lst[index].setStyleSheet("font-size:20px")
                self.tablitsa.addWidget(self.lst[index],i,j)
                index+=1                              
        self.v_main.addLayout(self.tablitsa)   
        self.v_main.addLayout(self.h_lay)                                                                                                                                                                                                                                                                                                                                                                                                                                                                        
        self.setLayout(self.v_main) 
        self.finish()
    def start(self):
        self.btn_start.hide()
        self.btn_finish.show()
        for i in self.lst:
            i.setText("")
            i.setEnabled(True)
    def finish(self):
        self.btn_start.show()
        self.btn_finish.hide()
        for i in self.lst:
            i.setEnabled(False)
    def Btn(self,btn):
        if btn==self.btn1:
            if self.count%2==0:
                self.btn1.setText("X")
                self.btn1.setEnabled(False)
                self.count+=1
            else:
                self.btn1.setText("O")
                self.btn1.setEnabled(False)
                self.count+=1
        elif btn==self.btn2:
            if self.count%2==0:
                self.btn2.setText("X")
                self.btn2.setEnabled(False)
                self.count+=1
            else:
                self.btn2.setText("O")
                self.btn2.setEnabled(False)
                self.count+=1
        elif btn==self.btn3:
            if self.count%2==0:
                self.btn3.setText("X")
                self.btn3.setEnabled(False)
                self.count+=1
            else:
                self.btn3.setText("O")
                self.btn3.setEnabled(False)
                self.count+=1
        elif btn==self.btn4:
            if self.count%2==0:
                self.btn4.setText("X")
                self.btn4.setEnabled(False)
                self.count+=1
            else:
                self.btn4.setText("O")
                self.btn4.setEnabled(False)
                self.count+=1
        elif btn==self.btn5:
            if self.count%2==0:
                self.btn5.setText("X")
                self.btn5.setEnabled(False)
                self.count+=1
            else:
                self.btn5.setText("O")
                self.btn5.setEnabled(False)
                self.count+=1
        elif btn==self.btn6:
            if self.count%2==0:
                self.btn6.setText("X")
                self.btn6.setEnabled(False)
                self.count+=1
            else:
                self.btn6.setText("O")
                self.btn6.setEnabled(False)
                self.count+=1
        elif btn==self.btn7:
            if self.count%2==0:
                self.btn7.setText("X")
                self.btn7.setEnabled(False)
                self.count+=1
            else:
                self.btn7.setText("O")
                self.btn7.setEnabled(False)
                self.count+=1
        elif btn==self.btn8:
            if self.count%2==0:
                self.btn8.setText("X")
                self.btn8.setEnabled(False)
                self.count+=1
            else:
                self.btn8.setText("O")
                self.btn8.setEnabled(False)
                self.count+=1
        else:
            if self.count%2==0:
                self.btn9.setText("X")
                self.btn9.setEnabled(False)
                self.count+=1
            else:
                self.btn9.setText("O")
                self.btn9.setEnabled(False)
                self.count+=1
        self.check()
    def check(self):
        if (self.btn1.text()=="X"and self.btn2.text()=="X"and self.btn3.text()=="X")or(self.btn1.text()=="O"and self.btn2.text()=="O"and self.btn3.text()=="O"):
            msg=QMessageBox()
            msg.setText(f"{self.btn1.text()} Yutdi congrats!!!")
            msg.setIcon(QMessageBox.Information)
            msg.exec_()
            self.finish()
        elif (self.btn4.text()=="X"and self.btn5.text()=="X"and self.btn6.text()=="X")or(self.btn4.text()=="O"and self.btn5.text()=="O"and self.btn6.text()=="O"):
            msg=QMessageBox()
            msg.setText(f"{self.btn4.text()} Yutdi congrats!!!")
            msg.setIcon(QMessageBox.Information)
            msg.exec_()
            self.finish()
        elif (self.btn7.text()=="X"and self.btn8.text()=="X"and self.btn9.text()=="X")or(self.btn7.text()=="O"and self.btn8.text()=="O"and self.btn9.text()=="O"):
            msg=QMessageBox()
            msg.setText(f"{self.btn8.text()} Yutdi congrats!!!")
            msg.setIcon(QMessageBox.Information)
            msg.exec_()
            self.finish()
        elif (self.btn1.text()=="X"and self.btn4.text()=="X"and self.btn7.text()=="X")or(self.btn1.text()=="O"and self.btn4.text()=="O"and self.btn7.text()=="O"):
            msg=QMessageBox()
            msg.setText(f"{self.btn1.text()} Yutdi congrats!!!")
            msg.setIcon(QMessageBox.Information)
            msg.exec_()
            self.finish()
        elif (self.btn2.text()=="X"and self.btn5.text()=="X"and self.btn8.text()=="X")or(self.btn2.text()=="O"and self.btn5.text()=="O"and self.btn8.text()=="O"):
            msg=QMessageBox()
            msg.setText(f"{self.btn5.text()} Yutdi congrats!!!")
            msg.setIcon(QMessageBox.Information)
            msg.exec_()
            self.finish()
        elif (self.btn3.text()=="X"and self.btn6.text()=="X"and self.btn9.text()=="X")or(self.btn3.text()=="O"and self.btn6.text()=="O"and self.btn9.text()=="O"):
            msg=QMessageBox()
            msg.setText(f"{self.btn6.text()} Yutdi congrats!!!")
            msg.setIcon(QMessageBox.Information)
            msg.exec_()
            self.finish()
        elif (self.btn1.text()=="X"and self.btn5.text()=="X"and self.btn9.text()=="X")or(self.btn1.text()=="O"and self.btn5.text()=="O"and self.btn9.text()=="O"):
            msg=QMessageBox()
            msg.setText(f"{self.btn1.text()} Yutdi congrats!!!")
            msg.setIcon(QMessageBox.Information)
            msg.exec_()
            self.finish()
        elif (self.btn3.text()=="X"and self.btn5.text()=="X"and self.btn7.text()=="X")or(self.btn3.text()=="O"and self.btn5.text()=="O"and self.btn7.text()=="O"):
            msg=QMessageBox()
            msg.setText(f"{self.btn7.text()} Yutdi congrats!!!")
            msg.setIcon(QMessageBox.Information)
            msg.exec_()
            self.finish()
        
        
    

app=QApplication([])                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              
win=mywin()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        
win.show()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          
app.exec_()                                                                                                                                                                                                                                                                                                     