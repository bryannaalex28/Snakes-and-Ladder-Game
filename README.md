# Snakes-Ladder
CIS 1051 - Final Project

Video Walk Through: 

Overview:
Hello welcome to the Snakes and Ladders Game! This is my digital version of the classic board that was created using Python and Pygame. This game features an exicting interactive board game where two players can take turns rolling dice, climbing ladders and avoiding snakes.

Key Features:
This game includes the basic features from the orinigal came such as:
  - Dice Rolling: Players roll a dice to determine how many tiles to move.
  - Snakes: If a player hits the snake head is slides the snake tail
  - Ladders: If a player lands on the bottom of the ladder, they move to the top of        the ladder.
Also my own features like:
  - Special Tiles: Players will encounter special tiles such as extra rolls, reverse       snakes, and teleportation to spice up the game!
  - Player Movement: The game will visually show each player's movement accross the        board.
  - Animations/Sound Effects: Players experience dice animations, snake hisses, and other sound effects that enhance the gameplay experiene.

Installation/Running the Game:
To run this game, you will need to have Python and Pygame installed on your stystem. Once you've installed those, run the main.py file in your terminal. The game will window will pop up and you can start playing.

Controls:
- Press SPACE to roll the dice
- Press ESC key to quit the game

Game Features:
- Ladders: Players who land on the ladder tiles move up to a higher tile
- Snakes: Players who land on snake tiles slide down to a lower tile. Also a snake hiss will play.
- Special Tiles:
    - Extra Roll: Players get another dice roll when landing on these tiles
    - Reverse Snakes: Players move backwards when lading on these tiles.
    - Teleport: Players can teleport to different positions on the board (forward or         backwards).
- Player Stats: The game tracks each player's position on the board and the current player's turn is displayed at the bottom left of the screen.

Difficulties:
Developing this game was no joke and it took a lot of work and effort. First challenged I face was hadling the player's turns, dice rolls, and board updates I had to make sure that the game continued to run smoothly without any unexpected bahivors during a player trnasition. Also doing the animations took a bit work. This was the hardest part for me. Everytime I got one animation to work, something else would go wrong in the game. Synchronizing the dice roll animation with the actual movement of the players took some trial and error. I leard to use delays to make the animations more smooth. I also had trouble getting the sound effects to trigger properly when certain eents happened. After debugging and figuring out how to use Pygame's sound system, I was able to successfully integrate the audios smoothly.

Lessons Learned:
There was a lot of lesson learned during this experience but the main ones I would say are...
- I was able to understand and learn how to use Pygame, specifically in how to handle player movemnt, animations, and events.
- By using classes for the Player and Board, I learned how to mange game state more effectivley and keep the code readable.
- I also learned how important it is to keep players engaged to a simple game by adding speacil tiles, animations and sound effects.
- Learning how to debugg sound integration, event handling, and ensuring smooth player transitions helped me imporve my problem-solving skills.

Conclusion:
When I first took this class I had very little knowledge of coding and was scared that I wasn't going to do well. One thing this class and project has taught me is coding is all about mistakes and getting comfortable with making them. It's when there is error you learn how to imporve your coding skills. This project specifically was a journey. If you were to tell me in the beginning of the year that I was going to create a virtual board game, I would've laughed. But after completing this project I feel more confident in my abilities and it was a fun and valuable elarning experience. I enjoyed tailoring the visuals and animations the most and slowly seeing my game come to life. I hope you enjoy playing the game as much as  Ienjoyed building it!

Acknowledgements:
- Pygame for providng the framework to build the game
- Perplexity/OpenAI for assiting with coding questions and debugging during developemnt.


