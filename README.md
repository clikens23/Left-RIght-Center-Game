# Left-Right-Center-Game

This is a game of Left, Right, Center, and Dot.

To play the game, you are prompted to place a bet. This is a betting game so you either win or lose. When prompted for a bet, you are to enter a number greater than 0. If less than 0 or not a number, you are prompted again and told the number needs to be greater than 0. After getting a number, you are told that each person bets that amount. For example, if a bet is $10, everybody bets $10. The next step is to enter the number of players. You need at least 3 players to play the game and I created a MAX_PLAYERS value of 8. So you can play between 3 and 8 players. You can always change the MAX_PLAYERS to whatever you want the max number of players to be. If you want to play with 100 players, so be it. If input a value less than 3 and greater than 8, you will be prompted again.

After getting the number of people, you are prompted to get names of each player. the def names() function comes into play. The number of people playing gets passed into the def get_names. For example if passed 3, you will get 3 names. You will loop through each name and strip off excess whitespace and capitalize each first character. For example, if passed in lebron james, will output Lebron James. For each loop, you will be adding it to a players list by appending each name. For each player, you will be adding 3 chips. For example, Lebron James will have 3 chips.

After creating a list of players with 3 chips to start with for each player, a “all names have been entered, let's play” will show. Now it's time to play the game. Players list will be passed in the run_game() function. A list of chips with a L for left, R for right, C for center and 🔴for dot. We will do a while True loop and iterate though each player. If a player has more than 0 chips do the following, if not, then print “player [name] has no chips left”. For the following, the player will roll their chips depending on how many they have. If the player has 3 chips, that player will roll 3 chips, if 2 chips, roll 2 chips etc. Then a rolls list is created to append what the player rolled. Next depending on how many chips that player rolled, the player will roll random chips. If a player rolled a L, the player to the left will be given a chip. We do this players(players.index(player) to find the current player in the players lists. Then add a (-1) so  players(players.index(player) - 1) gives us the player before the current player. Then we add the % len(players) we get players[(players.index(player) - 1) % len(players)]. The reason to add the (%) modulo operator is to wrap around within the bounds of the players list. For example if the player list is what is below and we perform the function below it.

players = [Charlie, Henry, Amy, Tom, Nick]
players[(players.index(player) - 1) % len(players)]
For example, if the current player is Henry,  (players.index(player) -1 will be
1 - 1 = 0.
I got 1 because indexing in python starts at 0 so Charlies will be 0 and Henry will be 1. len(players) will be 5.
1 % 5 = 0

0 is valid and gives us Charlie's position. So using the players[(players.index(player) - 1) % len(players)] gives us charlies. If a player rolled a “R” for right, the following will occur. players[(players.index(player) + 1) % len(players)]. This is the same as left but just adding +1 instead of -1. If a player rolled a “C” for center, player chips would be -= 0. If player rolled a 🔴chip, player would gain a chip. For each roll, the player would still lose a chip with the player[“chips”] -= 1. If not for this, there would be an infinite loop. For each roll for L, R, C, and , 🔴would append to a rolls list. This way we can later print the rolls list and see what the player rolled. So if a player has 3 chips and rolls a CRL. This is how it the functions would work:

Total chips: 3
For each loop so 3 loops total

L
    Player to the left would gain a chip
    Then -1 chip from player[“chips” -= 1]
R
	Player to the right would gain a chip
	Then -1 chip from player[“chips” -= 1]
C
	Player would lose 0 chips
	Then -1 chip from player[“chips” -= 1]
	Still would lose a chip


After the rolls or roll, print would say player names rolled CRL for example by the join(rolls). This takes all the items in the rolls list and joins them in one string. For each turn, the player's name and how many chips they have will be displayed.

For the winner, the remaining_players list will iterate through each player in the players list with the if statement checking to see if the player chips are greater than 0. If it is, then it will be added to the list. If the len(remaining_list) == 1 so only has 1 player in the list, then we have the last player. The last player needs to roll a ”🔴” to win the game. If the player does roll a “🔴” then the player wins the game. If not, then the game will continue until the last player rolls a “🔴”. Once the last player rolls a wins the game, they will be told, “congrats you won”, and you won this amount of money. Winner_money is the money bet * how many players are in the game. This is how you play Left, Right, Center Game. Enjoy the game.

