import tkinter as tk
# Create an empty window
root = tk.Tk()
root.geometry("720x720")
# Set the title of the frame

# varible----------------------------------------------------------------------
robot=tk.PhotoImage(file="C:\\Users\\student\\Desktop\\vantheav-game\\images\\player.png")
star=tk.PhotoImage(file="C:\\Users\\student\\Desktop\\vantheav-game\\images\\poin.png")
well=tk.PhotoImage(file="C:\\Users\\student\\Desktop\\vantheav-game\\images\\well.png")
boom=tk.PhotoImage(file="C:\\Users\\student\\Desktop\\vantheav-game\\images\\bomb.png")

canvas = tk.Canvas(root)
# well--------------------------------------------------------------------------
game=[
[2,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0],
[1,1,1,1,1,1,1,3,0,3,1,1,1,1,1,1,1,0],
[0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,1,0],
[0,4,1,1,1,1,1,1,3,0,1,1,1,0,3,1,4,0],
[0,0,0,0,1,0,1,0,1,0,1,0,1,0,0,0,1,0],
[0,1,1,1,1,0,3,0,1,0,1,1,1,1,1,0,1,0],
[0,1,0,1,1,0,0,0,1,0,1,0,0,1,0,0,1,0],
[3,1,0,4,1,1,1,1,1,0,4,1,1,1,3,0,1,0],
[0,0,0,0,0,1,0,0,1,0,1,0,1,0,1,0,1,0],
[1,1,0,3,1,1,1,1,1,0,1,1,1,0,1,1,1,0],
[1,1,0,1,0,0,0,0,1,0,1,0,0,0,1,0,0,0],
[1,1,0,1,1,1,1,1,4,1,1,1,3,0,1,1,1,0],
[1,1,0,0,0,1,0,1,0,1,1,1,1,0,0,0,1,0],
[1,1,1,1,0,3,0,1,0,1,0,0,1,0,1,1,1,0],
[0,0,0,1,0,0,0,1,0,1,1,1,1,0,1,0,0,0],
[3,1,1,1,0,1,0,1,0,0,0,0,0,0,1,1,1,0],
[0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,3],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,]
]
# drew---------------------------------------------------------------------------------
def arrayOfGame():
    for num in range(len(game)):
        for i in range (len(game[num])):
            if game[num][i]==0:
                canvas.create_image(23+(40*i),20+(40*num),image=well)
            elif game[num][i]==2:
                canvas.create_image(20+(40*i),13+(40*num),image=robot)
            elif game[num][i]==3:
                canvas.create_image(20+(40*i),15+(40*num),image=star)
            elif game[num][i]==4:
                canvas.create_image(20+(40*i),20+(40*num),image=boom)
                

# move ---------------------------------------------------------------------

def PosirionPacman(game):
    for i in range(len(game)):
        for n in range(len(game[i])):
            if game[i][n] ==2:
                postion=[i,n]
    return postion
def moveRight( event):
    position=PosirionPacman(game)
    row=position[0]
    column=position[1]
    if game[row][column+1]!= 0:
        game[row][column]=1
        game[row][column+1]=2
    canvas.delete("all")
    arrayOfGame()

def moveLeft( event):
    position=PosirionPacman(game)
    row=position[0]
    column=position[1]
    if game[row][column-1]!= 0:
        game[row][column]=1
        game[row][column-1]=2
    canvas.delete("all")
    arrayOfGame()
def moveUp( event):
    position=PosirionPacman(game)
    row=position[0]
    column=position[1]
    if game[row-1][column]!= 0:
        game[row][column]=1
        game[row-1][column]=2
    canvas.delete("all")
    arrayOfGame()
def moveDown( event):
    position=PosirionPacman(game)
    row=position[0]
    column=position[1]
    if game[row+1][column]!= 0:
        game[row][column]=1
        game[row+1][column]=2
    canvas.delete("all")
    arrayOfGame()

        

root.bind("<Left>", moveLeft) #LEFT CLICK
root.bind("<Right>", moveRight)  #RIGHT CLICK
root.bind("<Up>", moveUp) #Up CLICK
root.bind("<Down>", moveDown)  #Down CLICK
arrayOfGame()
canvas.pack(expand=True, fill='both')
root.mainloop()