#ゲーム「ハングマン」

def hangman(word):
    wrong = 0
    stages = ["",
              "___________",
              "|          "
              "|    |     ",
              "|    O     "
              "|   /|\    ",
              "|   / \    ",
              "|          "]
    rletters = list(word)
    board = ["_"] * len(word)
    win = False
    print ("Welcome to Hangman!")
    while wrong < len (stages) + 1:
        print ("\n")
        message = "image and type a letter:"
        challenge = input (message)
        if challenge in rletters:
            num = rletters.index(challenge)
            board[num] = challenge
            rletters[num] = "$"
        else:
            wrong += 1
        print (" ".join(board))
        e = wrong + 1
        print ("\n".join(stages[0:e] ))
        if "_" not in board:
            print ("You win!")
            print (" ".join(board))
            win = True
            break
    if not win:
        print ("\n".join(stages[0:wrong+1]))
        print ("You lose! The answer is {}.".format(word))
hangman ("cat")