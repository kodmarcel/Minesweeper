from GameEngine import GameEngine




game=GameEngine(10,10,10)


def showField():
    field=game.GetShownField()
    j=0
    for i in range(game.width,game.size,game.width):
        print(field[j:i])
        j=i
        
    
