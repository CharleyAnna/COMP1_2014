# Skeleton Program code for the AQA COMP1 Summer 2014 examination
# this code should be used in conjunction with the Preliminary Material
# written by the AQA Programmer Team
# developed in the Python 3.2 programming environment
# version 2 edited 06/03/2014

######test change#############

import random
import datetime

NO_OF_RECENT_SCORES = 3

class TCard():
  def __init__(self):
    self.Suit = 0
    self.Rank = 0

class TRecentScore():
  def __init__(self):
    self.Name = ''
    self.Score = 0
    self.Date = ' '

Deck = [None]
RecentScores = [None]
Choice = ''
AceRank = False

def GetRank(RankNo):
  Rank = ''
  if RankNo == 1 or RankNo == 14:
    Rank = 'Ace'
  elif RankNo == 2:
    Rank = 'Two'
  elif RankNo == 3:
    Rank = 'Three'
  elif RankNo == 4:
    Rank = 'Four'
  elif RankNo == 5:
    Rank = 'Five'
  elif RankNo == 6:
    Rank = 'Six'
  elif RankNo == 7:
    Rank = 'Seven'
  elif RankNo == 8:
    Rank = 'Eight'
  elif RankNo == 9:
    Rank = 'Nine'
  elif RankNo == 10:
    Rank = 'Ten'
  elif RankNo == 11:
    Rank = 'Jack'
  elif RankNo == 12:
    Rank = 'Queen'
  elif RankNo == 13:
    Rank = 'King'
  return Rank

def GetSuit(SuitNo):
  Suit = ''
  if SuitNo == 1:
    Suit = 'Clubs'
  elif SuitNo == 2:
    Suit = 'Diamonds'
  elif SuitNo == 3:
    Suit = 'Hearts'
  elif SuitNo == 4:
    Suit = 'Spades'
  return Suit

def DisplayMenu():
  print()
  print('MAIN MENU')
  print()
  print('1. Play game (with shuffle)')
  print('2. Play game (without shuffle)')
  print('3. Display recent scores')
  print('4. Reset recent scores')
  print('5. Options')
  print('6. Save high scores')
  print()

def GetMenuChoice():
  Valid = False
  while not Valid:
    Choice = input("Please select an option from the menu, or press q to quit: ").lower()
    if Choice == "q":
      Valid = True
    elif Choice == "quit":
      Choice = 'q'
      Valid = True
    elif Choice == "1":
      Valid = True
    elif Choice == "2":
      Valid = True
    elif Choice == "3":
      Valid = True
    elif Choice == "4":
      Valid = True
    elif Choice == "5":
      Valid = True
    elif Choice == "6":
      Valid = True
    else:
      print("That was not a valid menu choice, please try again: ")
  return Choice

def DisplayOptionsMenu():
  print()
  print('OPTIONS MENU')
  print()
  print('1. Set ace to be HIGH or LOW')
  print()

def GetOptionChoice():
  OptionChoice = input('Select an option from the menu or press Q to quit: ')
  print()
  return OptionChoice

def SetOptions(OptionChoice):
  global AceRank
  Valid = False
  while not Valid:
    if OptionChoice == "1":
      Valid = True
      SetAceHighOrLow()
    elif OptionChoice == "q" or OptionChoice == "Q":
      Valid = True
    else:
      print("That was not a valid menu choice please try again: ")
      print()
      OptionChoice = input('Select an option from the menu or press Q to quit: ')
    
      
def SetAceHighOrLow():
  global AceRank
  HighOrLow = input("Do you want the ace to be (H)igh or (L)ow: ").lower()
  HighOrLow = HighOrLow[0]
  Valid = False
  while not Valid:
    if HighOrLow == "h":
      Valid = True
      AceRank = True
    elif HighOrLow == "l":
      Valid = True
      AceRank = False
    else:
      print("That was not a valid input, please try again")
      print()
      HighOrLow= input("Do you want the ace to be (H)igh or (L)ow: ")
    print(AceRank)
    
  
def LoadDeck(Deck):
  global AceRank
  CurrentFile = open('deck.txt', 'r')
  Count = 1
  while True:
    LineFromFile = CurrentFile.readline()
    if not LineFromFile:
      CurrentFile.close()
      break
    Deck[Count].Suit = int(LineFromFile)
    LineFromFile = CurrentFile.readline()
    Deck[Count].Rank = int(LineFromFile)
    if AceRank == True and Deck[Count].Rank == 1:
        Deck[Count].Rank = 14
    Count = Count + 1
 
def ShuffleDeck(Deck):
  SwapSpace = TCard()
  NoOfSwaps = 1000
  for NoOfSwapsMadeSoFar in range(1, NoOfSwaps + 1):
    Position1 = random.randint(1, 52)
    Position2 = random.randint(1, 52)
    SwapSpace.Rank = Deck[Position1].Rank
    SwapSpace.Suit = Deck[Position1].Suit
    Deck[Position1].Rank = Deck[Position2].Rank
    Deck[Position1].Suit = Deck[Position2].Suit
    Deck[Position2].Rank = SwapSpace.Rank
    Deck[Position2].Suit = SwapSpace.Suit

def DisplayCard(ThisCard):
  print()
  print('Card is the', GetRank(ThisCard.Rank), 'of', GetSuit(ThisCard.Suit))
  print()

def GetCard(ThisCard, Deck, NoOfCardsTurnedOver):
  ThisCard.Rank = Deck[1].Rank
  ThisCard.Suit = Deck[1].Suit
  for Count in range(1, 52 - NoOfCardsTurnedOver):
    Deck[Count].Rank = Deck[Count + 1].Rank
    Deck[Count].Suit = Deck[Count + 1].Suit
  Deck[52 - NoOfCardsTurnedOver].Suit = 0
  Deck[52 - NoOfCardsTurnedOver].Rank = 0

def IsNextCardHigher(LastCard, NextCard):
  Higher = False
  if NextCard.Rank > LastCard.Rank:
    Higher = True
  return Higher

def GetPlayerName():
  HighScore = input("Do you want to add your score to the high score table? (Y or N): ").lower()
  HighScore = HighScore[0]
  print()
  if HighScore == "y":
    Valid = False
    while not Valid:
      PlayerName = input('Please enter your name: ')
      if PlayerName == '':
        print("You must enter something for your name!")
      else:
        Valid = True
        return PlayerName
  else:
    print("Your score will not be added")
  
def GetChoiceFromUser():
  Valid = False
  while not Valid:
    Choice = input('Do you think the next card will be higher than the last card (enter Y or N)? ').lower()
    if Choice == "y":
      Valid = True
      Choice = "y"
    elif Choice == "n":
      Valid = True
      Choice = "n"
    elif Choice == "yes":
      Valid = True
      Choice = "y"
    elif Choice == "no":
      Valid = True
      Choice = "y"
    else:
      ("That was not a valid input, please try again")
  return Choice

def DisplayEndOfGameMessage(Score):
  print()
  print('GAME OVER!')
  print('Your score was', Score)
  if Score == 51:
    print('WOW! You completed a perfect game.')
  print()

def DisplayCorrectGuessMessage(Score):
  print()
  print('Well done! You guessed correctly.')
  print('Your score is now ', Score, '.', sep='')
  print()

def ResetRecentScores(RecentScores):
  for Count in range(1, NO_OF_RECENT_SCORES + 1):
    RecentScores[Count].Name = ''
    RecentScores[Count].Score = 0

def BubbleSortScores(RecentScores):
    list_length = len(RecentScores)
    swap_made = True
    while swap_made:
        swap_made = False
        list_length = list_length-1
        for count in range (1,list_length):
            if RecentScores[count].Score < RecentScores[count+1].Score:
                temp = RecentScores[count]
                RecentScores[count] = RecentScores[count+1]
                RecentScores[count+1] = temp
                swap_made = True
    return RecentScores


def DisplayRecentScores(RecentScores):
  print()
  print('Recent Scores: ')
  print()
  print("{0:<10} {1:<10} {2:<10}".format("Name", "Date" ,"Score"))
  print()
  for Count in range(1, NO_OF_RECENT_SCORES + 1):
    print("{0:<10} {1:<10} {2:<10}".format(RecentScores[Count].Name, RecentScores[Count].Date, RecentScores[Count].Score))
  print()
  print('Press the Enter key to return to the main menu')
  input()
  print()

def UpdateRecentScores(RecentScores, Score):
  today = datetime.date.today()
  Date = today.strftime("%d/%m/%y")
  PlayerName = GetPlayerName()
  FoundSpace = False
  Count = 1
  while (not FoundSpace) and (Count <= NO_OF_RECENT_SCORES):
    if RecentScores[Count].Name == '':
      FoundSpace = True
    else:
      Count = Count + 1
  if not FoundSpace:
    for Count in range(1, NO_OF_RECENT_SCORES):
      RecentScores[Count].Name = RecentScores[Count + 1].Name
      RecentScores[Count].Score = RecentScores[Count + 1].Score
    Count = NO_OF_RECENT_SCORES
  RecentScores[Count].Name = PlayerName
  RecentScores[Count].Score = Score
  RecentScores[Count].Date = Date

def SaveScores(RecentScores):
  with open ("save_scores.txt", mode = "w", encoding = "utf-8") as my_file:
    for count in range(1,len(RecentScores)):
      save_score = ("{0} {1} {2}\n".format(RecentScores[count].Name, RecentScores[count].Date, RecentScores[count].Score))
      my_file.write(save_score)
  print()
  print("Scores saved")

def LoadScores():
  global RecentScores
  List = []
  with open("save_scores.txt", mode = "r") as my_file:
    for line in my_file:
      List.append(line)
  counter = 1
  for count in range (0, len(List), 3):
    RecentScores[counter].Name = List[count].rstrip("\n")
    RecentScores[counter].Date = List[count+1].rstrip("\n")
    RecentScores[counter].Score = List[count+1].rstrip("\n")
    counter += 1
        
        
def PlayGame(Deck, RecentScores):
  LastCard = TCard()
  NextCard = TCard()
  GameOver = False
  GetCard(LastCard, Deck, 0)
  DisplayCard(LastCard)
  NoOfCardsTurnedOver = 1
  while (NoOfCardsTurnedOver < 52) and (not GameOver):
    GetCard(NextCard, Deck, NoOfCardsTurnedOver)
    Choice = ''
    while (Choice != 'y') and (Choice != 'n'):
      Choice = GetChoiceFromUser()
    DisplayCard(NextCard)
    NoOfCardsTurnedOver = NoOfCardsTurnedOver + 1
    Higher = IsNextCardHigher(LastCard, NextCard)
    if (Higher and Choice == 'y') or (not Higher and Choice == 'n'):
      DisplayCorrectGuessMessage(NoOfCardsTurnedOver - 1)
      LastCard.Rank = NextCard.Rank
      LastCard.Suit = NextCard.Suit
    else:
      GameOver = True
  if GameOver:
    DisplayEndOfGameMessage(NoOfCardsTurnedOver - 2)
    UpdateRecentScores(RecentScores, NoOfCardsTurnedOver - 2)
  else:
    DisplayEndOfGameMessage(51)
    UpdateRecentScores(RecentScores, 51)


if __name__ == '__main__':
  for Count in range(1, 53):
    Deck.append(TCard())
  for Count in range(1, NO_OF_RECENT_SCORES + 1):
    RecentScores.append(TRecentScore())
  Choice = None
  while Choice != 'q':
    LoadScores()
    DisplayMenu()
    Choice = GetMenuChoice()
    if Choice == '1':
      LoadDeck(Deck)
      ShuffleDeck(Deck)
      PlayGame(Deck, RecentScores)
    elif Choice == '2':
      LoadDeck(Deck)
      PlayGame(Deck, RecentScores)
    elif Choice == '3':
      RecentScores = BubbleSortScores(RecentScores)
      DisplayRecentScores(RecentScores)
    elif Choice == '4':
      ResetRecentScores(RecentScores)
    elif Choice == "5":
      DisplayOptionsMenu()
      OptionChoice = GetOptionChoice()
      SetOptions(OptionChoice)
    elif Choice == "6":
      SaveScores(RecentScores)
