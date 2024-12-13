import pygame

end=0

def check_win(board):
    global end
    global text
    for player in ['X','O']:
        for i in range(3):
            if(
                board[i][0]["value"]==player and 
                board[i][1]["value"]==player and 
                board[i][2]["value"]==player
            ):
                end=1

        for i in range(3):
            if(
                board[0][i]["value"]==player and 
                board[1][i]["value"]==player and 
                board[2][i]["value"]==player
            ):
                end=1

        if(
            board[0][0]["value"]==player and
            board[1][1]["value"]==player and
            board[2][2]["value"]==player
        ):
            end=1
        
        elif(
            board[0][2]["value"]==player and
            board[1][1]["value"]==player and
            board[2][0]["value"]==player
        ):
            end=1
        
        if end:
            text=font.render(f"Winner: {player}",True,"black")
            return
    
    count=0
    for i in range(3):
        for j in range(3):
            if(board[i][j]["value"]!=''):
                count+=1
    if count==9:
        text=font.render(f"Tie",True,"black")
        end=1

def reset_board(board):
    for i in board:
        for cell in i:
            cell["value"]=''

board=[]

pygame.init()
screen=pygame.display.set_mode((1280,720))
clock=pygame.time.Clock()
running=True

width=screen.get_width()
height=screen.get_height()

cell_size=120

for i in range(3):
    row=[]
    for j in range(3):
        value=''
        pos=(
            (cell_size*i)+(width/2)-(cell_size+cell_size/2),
            (cell_size*j)+(height/2)-(cell_size+cell_size/2)
        )
        rect={
            "rect":pygame.Rect(pos[0],pos[1],100,100),
            "color":"white",
            "border-color":"black",
            "pos":pos,
            "value":value,
            "text-color":"white"
        }
        row.append(rect)
    board.append(row)

font=pygame.font.Font('freesansbold.ttf',32)

xo_font_size=100
xo_font=pygame.font.SysFont('Time New Roman',xo_font_size)

turn='X'
text=font.render(f"Current Turn: {turn}",True,"black")

retry_text=font.render("Retry",True,"black")
t_width,t_height=retry_text.get_size()
block_surface=pygame.Surface((1.5*t_width,1.5*t_height),pygame.SRCALPHA)
b_width,b_height=block_surface.get_size()
retry_button=None

while running:
    screen.fill("grey")

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        if event.type==pygame.MOUSEBUTTONDOWN:
            x,y=pygame.mouse.get_pos()
            if(retry_button and retry_button.collidepoint(x,y)):
                retry_button=None
                end=0
                reset_board(board)
            elif (not end):
                for i in board:
                    for cell in i:
                        if(cell["rect"].collidepoint(x,y)):
                            if(cell["value"]==''):
                                cell["value"]=turn
                                if(turn=='X'):
                                    cell["text-color"]="blue"
                                    turn='O'
                                else:
                                    cell["text-color"]="red"
                                    turn='X'
                                text=font.render(f"Current Turn: {turn}",True,"black")
                                check_win(board)

    for i in board:
        for cell in i:
            pygame.draw.rect(screen,cell["color"],cell["rect"])
            pygame.draw.rect(screen,cell["border-color"],cell["rect"],1)
            cell_text=xo_font.render(cell["value"],True,cell["text-color"])
            text_rect=cell_text.get_rect()
            screen.blit(
                cell_text,
                (
                    cell["pos"][0]+((cell_size-20)/2)-text_rect.width/2,
                    cell["pos"][1]+((cell_size-20)/2)-text_rect.height/2
                )
            )

    if(end):
        pygame.draw.rect(block_surface,"white",block_surface.get_rect(),border_radius=10)
        pygame.draw.rect(block_surface,"black",block_surface.get_rect(),1,10)
        block_surface.blit(retry_text,(b_width/2-t_width/2,b_height/2-t_height/2))
        retry_button=screen.blit(block_surface,(width/2-b_width/2,height/2+1.8*cell_size))
        
    screen.blit(text,(0,height-40))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()