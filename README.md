# My Portfolio

The following is a description of each project

# Ash1.0

Ash1.0 is an AI created for Pokémon Champions but can be optimized to run on any turn-based games.

**How does it work?**

1. Ash1.0 simulates battles using 5 possible move choices: the first through fourth moves and a swap.
2. Ash will simulate a 5 round battle x times for each move choice (x varies on the difficulty of the opponent).
3. The move with the highest average score will be the move chose.

**Difficulties of creating and algorithm that suits Pokémon Champions**

> A simple min-max algorithm cannot work. A move like sheer cold will cause a 1 hit-ko, which will result in it having the maximum first round score to start the battle, but sheer cold has a 20% accuracy. So, the average score will likely be lower than those of weaker and more accurate moves.

> Because Pokémon Champions is a 2 v 2 battling game, a move may have multiple targets, therefore an extra step must be taken to figure out which target returns the highest score.

> To truly optimize the trainer's move, Ash1.0 must take into consideration the move and targets selected during its first run. To put it briefly; Ash 1.0 will run twice, once for the first opponent Pokémon and once for the second opponent Pokémon. To truly find the best score, the algorithm must be aware of the move it chose for the first opponent Pokémon in order to truly chose the best move for the second opponent Pokémon.


**Pros of Ash1.0**

> Using a simulation length of 5 rounds allows Ash1.0 to incorporate status changing moves as well as moves that don't do damage until later in the battle. This allows for more creative and dynamic battles with trainers.

> Ash1.0 incorporates damage, statuses, field conditions, and every other change made during actual gameplay to ensure that the move chosen is perfect for the current status of the battle.

> Ash1.0 is very easily configurable, changes in difficulty can be done by changing the number of simulations per move or the duration of each simulated battle. Each change will result in a unique move selection.

**Cons of Ash1.0**

> Ash1.0 does not cheat. This means that Ash1.0 will not be aware of the player's pre-selected moves in the current round and must figure out the best average strategy without this knowledge. This can be seen as a pro or con. Allowing the option for Ash1.0 to cheat can create very dynamic gameplay where the user must try to truly outsmart the AI, but it can also cause frustration.
