import pygame

class Square:
    """
    Class that represents a square of the board, that may have a piece on it.
    """
    def __init__(self, x, y, color):
        """
        Constructor of the class.
        """
        self.x = x
        self.y = y
        self.color = color
        self.piece = None

    def set_piece(self, piece):
        """
        Method that sets the piece that is on the square.
        """
        self.piece = piece


    def get_piece(self):
        """
        Method that returns the piece that is on the square (if any).
        """
        return self.piece


    def draw_square(self, screen, square_size):
        """
        Method that draws on the screen the board square (and its piece if any)
        """
        pygame.draw.rect(screen, self.color, [(square_size * self.y) + 40, (square_size * self.x) + 50, square_size, square_size])

        if self.piece is not None:
            screen.blit(self.piece, ((square_size * self.y) + 40, (square_size * self.x) + 50))