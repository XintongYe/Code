# coding=utf-8
from tkinter import *
from random import *
import threading
from tkinter.messagebox import showinfo
from tkinter.messagebox import askquestion
import threading
from time import sleep


class BrickGame(object):
    
    start = True;
   
    isDown = True;
    isPause = False;
    
    window = None;
  
    frame1 = None;
    frame2 = None;

   
    btnStart = None;

   
    canvas = None;
    canvas1 = None;

   
    title = "Tetris";
   
    width = 450;
    height = 670;

   
    rows = 20;
    cols = 10;

    
    downThread = None;

    
    brick = [
        [
            [
                [0, 1, 1],
                [1, 1, 0],
                [0, 0, 0]
            ],
            [
                [1, 0, 0],
                [1, 1, 0],
                [0, 1, 0]
            ],
            [
                [0, 1, 1],
                [1, 1, 0],
                [0, 0, 0]
            ],
            [
                [1, 0, 0],
                [1, 1, 0],
                [0, 1, 0]
            ]
        ],
        [
            [
                [1, 1, 1],
                [1, 0, 0],
                [0, 0, 0]
            ],
            [
                [0, 1, 1],
                [0, 0, 1],
                [0, 0, 1]
            ],
            [
                [0, 0, 0],
                [0, 0, 1],
                [1, 1, 1]
            ],
            [
                [1, 0, 0],
                [1, 0, 0],
                [1, 1, 0]
            ]
        ],
        [
            [
                [1, 1, 1],
                [0, 0, 1],
                [0, 0, 0]
            ],
            [
                [0, 0, 1],
                [0, 0, 1],
                [0, 1, 1]
            ],
            [
                [0, 0, 0],
                [1, 0, 0],
                [1, 1, 1]
            ],
            [
                [1, 1, 0],
                [1, 0, 0],
                [1, 0, 0]
            ]
        ],
        [
            [
                [0, 0, 0],
                [0, 1, 1],
                [0, 1, 1]
            ],
            [
                [0, 0, 0],
                [0, 1, 1],
                [0, 1, 1]
            ],
            [
                [0, 0, 0],
                [0, 1, 1],
                [0, 1, 1]
            ],
            [
                [0, 0, 0],
                [0, 1, 1],
                [0, 1, 1]
            ]
        ],
        [
            [
                [1, 1, 1],
                [0, 1, 0],
                [0, 0, 0]
            ],
            [
                [0, 0, 1],
                [0, 1, 1],
                [0, 0, 1]
            ],
            [
                [0, 0, 0],
                [0, 1, 0],
                [1, 1, 1]
            ],
            [
                [1, 0, 0],
                [1, 1, 0],
                [1, 0, 0]
            ]
        ],
        [
            [
                [0, 1, 0],
                [0, 1, 0],
                [0, 1, 0]

            ],
            [
                [0, 0, 0],
                [1, 1, 1],
                [0, 0, 0]

            ],
            [
                [0, 1, 0],
                [0, 1, 0],
                [0, 1, 0]
            ],
            [
                [0, 0, 0],
                [1, 1, 1],
                [0, 0, 0]
            ]
        ],
        [
            [
                [1, 1, 0],
                [0, 1, 1],
                [0, 0, 0]
            ],
            [
                [0, 0, 1],
                [0, 1, 1],
                [0, 1, 0]
            ],
            [
                [0, 0, 0],
                [1, 1, 0],
                [0, 1, 1]
            ],
            [
                [0, 1, 0],
                [1, 1, 0],
                [1, 0, 0]
            ]
        ]

    ];

    
    curBrick = None;
   
    arr = None;
    arr1 = None;
   
    shape = -1;
  
    curRow = -10;
    curCol = -10;

   
    back = list();
   
    gridBack = list();
    preBack = list();

   
    def init(self):

        for i in range(0, self.rows):
            self.back.insert(i, list());
            self.gridBack.insert(i, list());

        for i in range(0, self.rows):

            for j in range(0, self.cols):
                self.back[i].insert(j, 0);
                self.gridBack[i].insert(j, self.canvas.create_rectangle(30 * j, 30 * i, 30 * (j + 1), 30 * (i + 1),
                                                                        fill="black"));

        for i in range(0, 3):
            self.preBack.insert(i, list());

        for i in range(0, 3):

            for j in range(0, 3):
                self.preBack[i].insert(j, self.canvas1.create_rectangle(30 * j, 30 * i, 30 * (j + 1), 30 * (i + 1),
                                                                        fill="black"));

              

    def drawRect(self):
        for i in range(0, self.rows):

            for j in range(0, self.cols):

                if self.back[i][j] == 1:

                    self.canvas.itemconfig(self.gridBack[i][j], fill="blue", outline="white");

                elif self.back[i][j] == 0:

                    self.canvas.itemconfig(self.gridBack[i][j], fill="black", outline="white");

                   
        for i in range(0, len(self.arr1)):

            for j in range(0, len(self.arr1[i])):

                if self.arr1[i][j] == 0:

                    self.canvas1.itemconfig(self.preBack[i][j], fill="black", outline="white");

                elif self.arr1[i][j] == 1:

                    self.canvas1.itemconfig(self.preBack[i][j], fill="orange", outline="white");

                    
        if self.curRow != -10 and self.curCol != -10:

            for i in range(0, len(self.arr)):

                for j in range(0, len(self.arr[i])):

                    if self.arr[i][j] == 1:
                        self.canvas.itemconfig(self.gridBack[self.curRow + i][self.curCol + j], fill="blue",
                                               outline="white");

                     
        if self.isDown:

            for i in range(0, 3):

                for j in range(0, 3):

                    if self.arr[i][j] != 0:
                        self.back[self.curRow + i][self.curCol + j] = self.arr[i][j];

                      
            self.removeRow();

            
            self.isDead();

            
            self.getCurBrick();

           

    def removeRow(self):
        count = 0
        for i in range(0, self.rows):

            tag1 = True;
            for j in range(0, self.cols):

                if self.back[i][j] == 0:
                    tag1 = False;
                    break;

            if tag1 == True:

                
                count = count + 1
                for m in range(i - 1, 0, -1):

                    for n in range(0, self.cols):
                        self.back[m + 1][n] = self.back[m][n];

        scoreValue = eval(self.scoreLabel2['text'])
        scoreValue += 5 * count * (count + 3)
        self.scoreLabel2.config(text=str(scoreValue))

    
    def getCurBrick(self):

        self.curBrick = randint(0, len(self.brick) - 1);
        self.shape = 0;
       
        self.arr = self.brick[self.curBrick][self.shape];
        self.arr1 = self.arr;

        self.curRow = 0;
        self.curCol = 1;

        
        self.isDown = False;

      

    def onKeyboardEvent(self, event):
        print(event.keycode)
        
        if self.start == False:
            return;

        if self.isPause == True:
            return;

        
        tempCurCol = self.curCol;
        tempCurRow = self.curRow;
        tempShape = self.shape;
        tempArr = self.arr;
        direction = -1;

        if event.keycode == 37 or event.keycode == 8124162:

            
            self.curCol -= 1;
            direction = 1;
        elif event.keycode == 38 or event.keycode == 97:
           
            self.shape += 1;
            direction = 2;

            if self.shape >= 4:
                self.shape = 0;
            self.arr = self.brick[self.curBrick][self.shape];
        elif event.keycode == 39 or event.keycode == 8189699:

            direction = 3;
            
            self.curCol += 1;
        elif event.keycode == 40 or event.keycode == 8255233:

            direction = 4;
          
            self.curRow += 1;

        if self.isEdge(direction) == False:
            self.curCol = tempCurCol;
            self.curRow = tempCurRow;
            self.shape = tempShape;
            self.arr = tempArr;

        self.drawRect();

        return True;

       

    def isEdge(self, direction):

        tag = True;

        
        if direction == 1:

            for i in range(0, 3):

                for j in range(0, 3):

                    if self.arr[j][i] != 0 and (
                            self.curCol + i < 0 or self.back[self.curRow + j][self.curCol + i] != 0):
                        tag = False;
                        break;
                       
        elif direction == 3:

            for i in range(0, 3):

                for j in range(0, 3):

                    if self.arr[j][i] != 0 and (
                            self.curCol + i >= self.cols or self.back[self.curRow + j][self.curCol + i] != 0):
                        tag = False;
                        break;
                      
        elif direction == 4:

            for i in range(0, 3):

                for j in range(0, 3):

                    if self.arr[i][j] != 0 and (
                            self.curRow + i >= self.rows or self.back[self.curRow + i][self.curCol + j] != 0):
                        tag = False;
                        self.isDown = True;
                        break;
                      
        elif direction == 2:

            if self.curCol < 0:
                self.curCol = 0;

            if self.curCol + 2 >= self.cols:
                self.curCol = self.cols - 3;

            if self.curRow + 2 >= self.rows:
                self.curRow = self.curRow - 3;

        return tag;

      

    def brickDown(self):

        while True:

            if self.start == False:
                print("exit thread");
                break;
            if self.isPause == False:
                tempRow = self.curRow;
                self.curRow += 1;

                if self.isEdge(4) == False:
                    self.curRow = tempRow;

                self.drawRect();

              
                sleep(1);

               

    def clickStart(self):

        self.start = True;

        for i in range(0, self.rows):

            for j in range(0, self.cols):
                self.back[i][j] = 0;
                self.canvas.itemconfig(self.gridBack[i][j], fill="black", outline="white");

        for i in range(0, len(self.arr)):

            for j in range(0, len(self.arr[i])):
                self.canvas1.itemconfig(self.preBack[i][j], fill="black", outline="white");

        self.getCurBrick();
        self.drawRect();

        self.downThread = threading.Thread(target=self.brickDown, args=());
        self.downThread.start();

    def clickPause(self):
        self.isPause = not self.isPause
        print(self.isPause)
        if not self.isPause:
            self.btnPause["text"] = "PAUSE"
        else:
            self.btnPause["text"] = "RESTORE"

    def clickReStart(self):
        ackRestart = askquestion("RESTART?")
        if ackRestart == 'yes':
            self.clickStart()
        else:
            return

    def clickQuit(self):
        ackQuit = askquestion("ARE YOU SURE TO QUIT?")
        if ackQuit == 'yes':
            self.window.destroy()
            exit()

   
    def isDead(self):

        for j in range(0, len(self.back[0])):

            if self.back[0][j] != 0:
                showinfo("Game Over！");
                self.start = False;
                break;

              

    def __init__(self):

        self.window = Tk();
        self.window.title(self.title);
        self.window.minsize(self.width, self.height);
        self.window.maxsize(self.width, self.height);

        self.frame1 = Frame(self.window, width=300, height=600, bg="black");
        self.frame1.place(x=20, y=30);

        self.scoreLabel1 = Label(self.window, text="Score:", font=(30))
        self.scoreLabel1.place(x=340, y=60)
        self.scoreLabel2 = Label(self.window, text="0", fg='red', font=(30))
        self.scoreLabel2.place(x=410, y=60)

        self.frame2 = Frame(self.window, width=90, height=90, bg="black");
        self.frame2.place(x=340, y=120);

        self.canvas = Canvas(self.frame1, width=300, height=600, bg="black");
        self.canvas1 = Canvas(self.frame2, width=90, height=90, bg="black");

        self.btnStart = Button(self.window, text="Start", command=self.clickStart);
        self.btnStart.place(x=340, y=400, width=80, height=25);

        self.btnPause = Button(self.window, text="Pause", command=self.clickPause);
        self.btnPause.place(x=340, y=450, width=80, height=25);

        self.btnReStart = Button(self.window, text="Restart", command=self.clickReStart);
        self.btnReStart.place(x=340, y=500, width=80, height=25);

        self.btnQuit = Button(self.window, text="Quit", command=self.clickQuit);
        self.btnQuit.place(x=340, y=550, width=80, height=25);

        self.init();

       
        self.getCurBrick();

      

        self.drawRect();

        self.canvas.pack();

        self.canvas1.pack();

        
        self.window.bind("<KeyPress>", self.onKeyboardEvent);

       
        self.downThread = threading.Thread(target=self.brickDown, args=());
        self.downThread.start();

        self.window.mainloop();

        self.start = False;

    pass;


if __name__ == '__main__':
    brickGame = BrickGame();
