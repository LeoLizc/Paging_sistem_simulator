from typing import *
import pygame

class ColumnTable():

    colSize = 50
    rowSize = 40

    def __init__(self, pos: Tuple = (0,0), numCol: int = 5, color:str = 'black', headers: Iterable[Iterable]= None, font: pygame.font.Font = None) -> None:
        numCol += 1
        self.x = pos[0]
        self.y = pos[1]
        self.columns: List[List[str]] = [['DL', 'L/E', 'P', 'M', 'DF', 'SI', 'SO']] + [['']*7 for i in range(numCol-1)]
        self.color = color
        self.size = (self.colSize*len(self.columns), self.rowSize*len(self.columns[0]))

        if len(headers)!=numCol-1:
            raise ValueError("The number of headers does not match the number of columns")

        print(numCol, len(self.columns))
        for j, header in enumerate(headers, 1):
            if header:
                if len(header)>7:
                    raise ValueError(f'The number of header {i} must match the number of rows')
                for i in range(len(header)):
                    self.columns[j][i] = str(header[i])
        if font:
            self.font = font
        else:
            self.font = pygame.font.SysFont('arial', 20)

    def render(self, screen):
        # Render the table
        for i in range(len(self.columns)):
            for j in range(len(self.columns[i])):
                pygame.draw.rect(screen, self.color, (self.x + i*(self.colSize-1), self.y + j*self.rowSize, self.colSize, self.rowSize), 2)
                # Render the text
                text = self.font.render(self.columns[i][j], True, self.color)
                text_rect = text.get_rect(center=(self.x + i*(self.colSize-1) + self.colSize//2, self.y + j*self.rowSize + self.rowSize//2))
                screen.blit(text, text_rect)
        pass
    
    def update(self, screen):
        self.render(screen)
        pass

    def checkForInput(self, position: Tuple) -> bool:
        # Check if the position is in the table
        if self.x<=position[0]<=self.x+self.colSize*len(self.columns) and self.y<=position[1]<=self.y+self.rowSize*len(self.columns[0]):
            # Check if the position is in the table
            # col = (position[0]-self.x)//self.colSize
            # row = (position[1]-self.y)//self.rowSize
            return True
        return False

    def drag(self, offeset:Tuple, limits:Tuple = (0,0)) -> None:
        new_x, new_y = self.x + offeset[0], self.y + offeset[1]
        # check if the new position is in the screen
        # print(new_x, new_y)
        if limits[0]!=0 and new_x<limits[0]:
            if new_x<=5 and new_x>=limits[0]-self.size[0]-5:
                self.x = new_x
        else:
            self.x, = new_x,

        if limits[1]!=0 and new_y<limits[1]:
            if new_y<=5 and new_y>=limits[1]-self.size[1]-5:
                self.y = new_y
        else:
            self.y = new_y
        pass

    def set_columna(self, columna: int, content: Iterable):
        if len(content)!=5:
            raise ValueError("The number of content does not match the number of rows")
        for i in range(len(content)):
            self.columns[columna+1][i+2] = str(content[i])
        pass


class RowTable():

    colSize = 45
    rowSize = 35

    def __init__(self, pos: Tuple = (0,0), numRow: int = 5, color:str = 'black', headers: List = None, font: pygame.font.Font= None, render_size: Tuple[float]= (None, None), numCol: int = 5, header_color = None) -> None:
        numRow += 1
        self.x = pos[0]
        self.y = pos[1]
        if headers:
            if len(headers)!=numCol:
                raise ValueError("The number of headers does not match the number of columns")
            self.rows: List[List[str]] = [headers] + [['']*numCol for i in range(numRow-1)]
        else:
            self.rows: List[List[str]] = [['']*numCol for i in range(numRow)]
        self.color = color
        self.size = (self.colSize*len(self.rows[0]), self.rowSize*len(self.rows))

        self.header_color = header_color
        
        if font:
            self.font = font
        else:
            self.font = pygame.font.SysFont('arial', 20)
        
        self.render_size = render_size
        self.absolute_pos = (self.x, self.y)

    def render(self, screen):


        offset = self.absolute_pos[1] - self.y
        start_row = max(offset//self.rowSize + 1, 1)
        if self.render_size[1]:
            end_row = min(start_row + (self.render_size[1]//self.rowSize + (self.render_size[1]%self.rowSize>0)) -1, len(self.rows))
        else:
            end_row = len(self.rows)

        # Render the table
        for i in range(start_row, end_row):
            # Draw every row
            for j in range(len(self.rows[i])):
                pygame.draw.rect(screen, self.color, (self.x + j*self.colSize, self.y + i*self.rowSize, self.colSize, self.rowSize), 2)
                # Render the text
                text = self.font.render(str(self.rows[i][j]), True, self.color)
                text_rect = text.get_rect(center=(self.x + j*self.colSize + self.colSize//2, self.y + i*self.rowSize + self.rowSize//2))
                screen.blit(text, text_rect)

        # fill the header
        if self.header_color: pygame.draw.rect(screen, self.header_color, (self.absolute_pos[0], self.absolute_pos[1], self.size[0], self.rowSize))
        # # render the headers
        for i in range(len(self.rows[1])):

            pygame.draw.rect(screen, self.color, (self.absolute_pos[0] + i*self.colSize, self.absolute_pos[1], self.colSize, self.rowSize), 2)

            # Render the text
            text = self.font.render(self.rows[0][i], True, self.color)
            text_rect = text.get_rect(center=(self.absolute_pos[0] + i*self.colSize + self.colSize//2, self.absolute_pos[1] + self.rowSize//2))
            screen.blit(text, text_rect)
        #drawinf edges

        if self.render_size[1]: 
            for i in range(len(self.rows[0])):
                pygame.draw.rect(screen, self.color, (self.absolute_pos[0] + i*self.colSize, self.absolute_pos[1], self.colSize, self.render_size[1]), 2)
                
    def drag(self, offeset:Tuple) -> None:
        new_x, new_y = self.x + offeset[0], self.y + offeset[1]
        # check if the new position is in the screen
        # print(new_x, new_y)
        if self.render_size[0] and self.size[0]<self.render_size[0]:
            if new_x<=5 and new_x>=self.render_size[0]-self.size[0]-5:
                self.x = new_x
        else:
            self.x, = new_x,

        if self.render_size[1] and self.size[1]>self.render_size[1]:
            # print('a')
            if new_y<=self.absolute_pos[1]+5 and new_y>=self.absolute_pos[1]+self.render_size[1]-self.size[1]-5:
                # print('b')
                self.y = new_y
        else:
            if new_y>=self.absolute_pos[1] and new_y<= self.absolute_pos[1] + self.render_size[1] - self.size[1]:
                self.y = new_y
        pass

    def checkForInput(self, position: Tuple) -> bool:
        # Check if the position is in the table
        if self.absolute_pos[0]<=position[0]<=self.absolute_pos[0]+self.size[0] and self.absolute_pos[1]<=position[1]<=self.absolute_pos[1]+self.render_size[1]:
            # Check if the position is in the table
            # col = (position[0]-self.x)//self.colSize
            # row = (position[1]-self.y)//self.rowSize
            return True
        return False

    def update(self, screen):
        self.render(screen)
        pass