#Task Sheet One Questions

##Question 3(a):

1.Which function is responsible for getting the name from the user?
The `GetPlayerName()` function is responsible for getting the name.

2. How will you ensure that the user is asked for the name repeatedly?
I will add a `Valid` variable that is set to False until the user enters an appropriate name, this will be 
inside a `while` loop to ensure the user is asked repeatedly.

3.What additional variable will you need and what will its datatype be?
The additional variable is the `Valid` variable and it is a boolean datatype

##Pseudo-Code
	FUNCTION GetPlayerName():
		HighScore:String
		Valid:Boolean
		PlayerName:String
		OUTPUT "Do you want to add your score to the high score table? (Y or N): "
		HighScore <-- INPUT.lower()
		OUTPUT " "
		HighScore <-- HighScore[0]
		IF HighScore == "y":
			Valid <-- False
			WHILE not Valid:
				OUTPUT "Please enter your name"
				PlayerName <-- INPUT
				IF PlayerName == '':
					OUTPUT "You must enter something for your name!"
			else:
				Valid = True
				RETURN PlayerName
			END IF
		else:
			OUTPUT"Your score will not be added"
			END WHILE
	END FUNCTION

##Question 3(b)
1.Which function is responsible for adding scores to the table?
The `UpdateRecentScores()` function is responsible for adding new high scores to the table

##Question 5
1.What additional module will you need to import into the program?
The `datetime` module will need to be imported

2.Identify the four functions that will need changing
<li>
	*`DisplayRecentScores()`
	*`UpdateRecentScores()`
	*`TRecentScore()`
</li>


3.How do you convert a string in the format DD/MM/YY (e.g. 14/08/93) to a date type in Python?
You can convert from string to date type using `datetime.strftime()` 

##Additional Task - Variable Roles
1. Describe each variable in your own words:
	Fixed Value - A variable that is created which requires no calculation. It doesn't change.
	Stepper - A variable that is used to count, it increases once it goes round a loop.
	Most Recent Holder - A variable that holds the value that has been encountered most recently.
	Most Wanted Holder - A variable that holds the value that the user or programmer wants
	Gatherer - A variable that adds together all values that it has come across throughout the program
	Transformation - A variable that gets its value from calculations of other variables 
	Follower - A variable that gets its value from another older variable
	Temporary - A variable that is used as an intermediate

2. Give an example of variable from the program code for each variable role:
	Fixed Value - `NoOfSwaps`
	Stepper - `Count`
	Most Recent Holder - `Choice`
	Most Wanted Holder - `NextCard`
	Gatherer - No examples in program
	Transformation - `Higher`
	Follower - `LastCard`
	Temporary - `SwapSpace`
	
##Additional Task - Functions And Parameters
1.	Describe the difference between passing by value and passing by reference in your own words:
	Only lists and records are passed by value, all other data types are passed by reference. When you pass by value, a copy of the 
	data is passed into the function so you are not working on the original data, this is why we must return the variable at the end
	of a function so that we can update the original. When we pass by reference, you are working on the original data, when you change
	the data within a function you are changing the original so there is no need to return the variable at the end of a function.

2. For each function in the program identify the mechanism using to pass each parameter:
   GetRank Function - RankNo is passed by value
   GetSuit Function - SuitNo is passed by value
   LoadDeck Function - Deck is passed by reference
   ShuffleDeck Function - Deck is passed by reference
   DisplayCard Function - ThisCard is passed by reference
   GetCard Function - ThisCard, Deck and NoOfCardsTurnedOver are all passed by reference 
   IsNextCardHigher Function - LastCard and NextCard both passed by reference
   DisplayEndOfGameMessage Function - Score is passed by value
   DisplayCorrectGuessMessage Function - Score is passed by value 
   ResetRecentScores Function - RecentScores is passed by reference
   DisplayRecentScores Function - RecentScores is passed by reference
   UpdateRecentScores Function - RecentScores and Score are both passed by reference
   PlayGame Function - Deck and RecentScores are bother passed by reference
   
   
	

	
