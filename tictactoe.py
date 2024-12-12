import pygame

# class TicTacToe():
#     def __init__(self):
#         self.board=[]
#         for i in range(3):
#             self.board.append(['','',''])
        
# class Button():
#     def __init__(self,pos,width,height,color):
#         self.color=color
#         self.Rect=pygame.Rect(pos[0],pos[1],width,height)
#     def draw(self):
#         pygame.draw.rect(screen,self.color,self.Rect)

board=[]

pygame.init()
screen=pygame.display.set_mode((1280,720))
clock=pygame.time.Clock()
running=True

width=screen.get_width()
height=screen.get_height()

cell_size=120

font=pygame.font.Font('freesansbold.ttf',32)

turn='X'
text=font.render(f"Current Turn: {turn}",True,"black")

while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        if event.type==pygame.MOUSEBUTTONDOWN:
            pass
    screen.fill("grey")

    mouse=pygame.mouse.get_pos()

    board=[]
    for i in range(3):
        row=[]
        for j in range(3):
            pos=(
                (cell_size*i)+(width/2)-(cell_size+cell_size/2),
                (cell_size*j)+(height/2)-(cell_size+cell_size/2)
            )
            row.append(pos)
            pygame.draw.rect(screen,"white",[pos[0],pos[1],100,100])
        board.append(row)

    screen.blit(text,(0,height-40))

    pygame.display.update()
    clock.tick(60)

print(board)

pygame.quit()