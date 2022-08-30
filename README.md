# README


Welcome to KlashOfKlans a fun reinvention of a beloved game ClashOfClans.

The town structure consists of a map as below:

```
**************************************************************
*K>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . *
*. C C . . H H . . . . . H H . . . . . . . . . . . . . . . . *
*. . . . . H H . . . . . H H . . . . . . . . . . . . . . . . *
*. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . *
*. . . . . . . . . . . . W W W W W . . . . . . . . . . . . . *
*. . . . . . . . . . . . W T T T W . . . . . . . . H H . . . *
*. . . . . . . . . . . . W T T T W . . . . . . . . H H . . . *
*. . . . . . . . . . . . W T T T W . . . . . . . . . . . . . *
*. . . . . . . . . . . . W T T T W . . . . . . . . . . . . . *
*. . . . . . . . . . . . W W W W W . . . . . . . . . . . . . *
*. . . . . . . . . . . . . . . . . . . . H H . . . C C . . . *
*. . . . . . . . . . . . . . . . . . . . H H . . . . . . . . *
*. . . . . . . . H H . . . . . . . . . . . . . . . . . . . . *
*. . . . . . . . H H . . . . . . . . . . . . . . . . . . . . *
**************************************************************
```

The color of the buildings indicate the health of the buildings. Same works for the King and Barbarians.

## Village:

Press '1', '2','3' => to get respective spawning points.

Town hall is represented as below:
```
T T T
T T T
T T T
T T T
```

There are 5 huts as represented below:
```
H H
H H
```

There are walls areound the town hall to protect it:
```
W
```

The cannons are represented as below:
```
C C
```

They have a range of the cannon is a square area of 2 spaces around the cannon. 

### Wizard Tower:
There should be at least two wizard towers in your village. The Wizard Tower can attack aerial troops.

## King:

The king's current sword direction is shown by an angular bracket. The tile affected by the king's sword is the one right in front of the angular bracket.

Eg: ```K>```  the right tile is affected

## Archer Queen:

The Archer Queen will attack a distant AoE location (e a 5x5 area whose center is 8 tiles away from the queen’s location in the last-moved direction of the queen) with a volley of arrows. This location should be specified relative to the location of the queen, any building present in that location would be damaged by the queen’s arrows.

<b> The Archer Queen’s Eagle Arrow: </b> In this attack, the Archer Queen launches a volley of arrows high into the air attacking at a greater range
and AoE. The arrows reach the ground 1 second after being shot, dealing damage to all buildings in the AoE. The damage dealt by this attack is the same as the Queen’s original attack, but the tiles being attacked are different. The Queen now attacks a 9x9 tile area at a distance of 16 tiles from the queen. The direction and distance calculations are done similarly to the queen’s original attack.

## Archers:

Archers can attack OVER walls and buildings. I.e. They can attack anything in their range regardless of whether their path to the target is blocked or not. he archers move similarly to barbarians, they will find the nearest non-wall building and move to attack it. In case a wall appears in their path to the building, they are required to destroy the wall and proceed.

## Balloon:

The Balloon will be an aerial troop, i.e. walls and buildings do not affect its movement and certain defensive buildings can’t attack it. Balloons attack differently from Barbarians, instead of targeting any non-wall building, Balloons will prioritize attacking defensive buildings (Cannons and Wizard Towers). Once all defensive buildings are destroyed, Balloons will then move destroying other non-wall buildings (choosing to attack the nearest one, similar to barbarians). Balloons can fly over walls and other buildings, i.e. once they select a building to attack, they can move to said building without caring about the presence of walls or other buildings in their path.

## Barbarians: 

The barbarians move on their own towards the nearest building. The health of the Barbarians is depicted by its color.

## Spells:

On the activation of the spell, it will show what spell has activated. Press enter to acquire the powerup and continue the game.

### Rage Spell:

Press 'r' for activating the rage spell.

### Heal Spell:

Press 'h' for activating the heal spell.


<b> Note: </b> Press 'p' to pause and enter to resume the game.

## Replays:

You can replay any game by providing the corresponding game id. The whole game can be viewed from the beginning.

## Levels:

○ Level 1: 2 cannons and 2 wizard towers
<br>
○ Level 2: 3 cannons and 3 wizard towers
<br>
○ Level 3: 4 cannons and 4 wizard towers
