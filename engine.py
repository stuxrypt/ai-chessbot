import chess as ch
import random as rd
# create a class for the engine
class Engine:
    def __init__(self, board, maxDepth, color):
        self.board=board
        self.maxDepth=maxDepth
        self.color=color

    def getBestmove(self):
        return self.engine(None, 1)

    def evalFunct(self):
        compt = 0
        for i in range(64):
            compt+self.squareResPoints(ch.SQAURES[i])
        compt+=self.mateOpp()+self.opening()+rd.random()




    def opening(self):
        if (self.board.fullmove_number<10):
                if (self.board.turn==self.color):
                    return 1/30 * self.board.legal_moves.count()
                else:
                    return -1/30 * self.board.legal_moves.count()
        else:
            return 0     

    def mateOpp(self):
        if (self.board.legal_moves.count()==0):
            if (self.board.turn == self.color):
                return -6969
            else:
                return 6969
        else:
            return 0
    # Takes a square as input and returns system value
    def squareResPoints(self, square):
        pieceValue=0
        if (self.board.piece_type_at(square) == ch.PAWN):
            pieceValue =1
        if (self.board.piece_type_at(square) == ch.ROOK):
            pieceValue =5.1
        if (self.board.piece_type_at(square) == ch.KNIGHT):
            pieceValue =3.33
        if (self.board.piece_type_at(square) == ch.BISHOP):
            pieceValue =3.2
        if (self.board.piece_type_at(square) == ch.QUEEN):
            pieceValue =8.8

    def engine(self, candidate, depth):
        if (depth == self.maxDepth or self.board.legal_moves.count()==0):
            return self.evalFunct()
        else:
            #get a list of legal moves in the position
            movelist = list(self.board.legal_moves)

            #initialise candidate thing
            newCandidate=None

            if (deph % 2 != 0):
                newCandidate=float("-inf")
            else:
                newCandidate=float("inf")

            for i in movelist:
                #Play "i"
                self.board.push(i)

                #get the value of the move "i"
                value = self.engine(newCandidate, depth+1)

            # Basic minmax algo
            # if maximizing (engine turn)
            if(value > newCandidate and deph % 2 != 0):
                newCandidate = value
                if (deph ==1):
                    move =i
            # if minimizing (human turn)
            elif(value < newCandidate and deph % 2 == 0):
                newCandidate = value


            # Alpha-beta pruning
            # if previous move was engine move
            if(candidate != None and value < candidate and deph % 2 == 0):
                self.board.pop()
                break


            # if previous move was human move
            elif(candidate != None and value > candidate and deph % 2 != 0):
                self.board.pop()
                break

                 #Undo move
                self.board.pop()

        if (depth>1):
            # return value of node in the tree
            return newCandidate
        else:
            return move


