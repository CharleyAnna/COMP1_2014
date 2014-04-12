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
*`DisplayRecentScores()`
*`UpdateRecentScores()`
*`PlayGame()`
*`Main Program

3.How do you convert a string in the format DD/MM/YY (e.g. 14/08/93) to a date type in Python?
You can convert using `


