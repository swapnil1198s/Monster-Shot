![game2](https://github.com/swapnil1198s/Monster-Shot/assets/46658528/8c36417d-2fca-431a-b752-ff99b8877be2)
# Monster-Shot
A simple 2D shooter game

Program versions: 
  macOS Monterey 12.6.3
  pygame 2.1.3 
  (SDL 2.0.22, Python 3.8.3)
  
Game demo:
https://user-images.githubusercontent.com/46658528/222571784-ca9f11c5-ab3c-478c-bfb8-014718223a28.mov

Motivation:
  I chose to make a monster shooting game because it is fun and allows me to use the concepts discussed in CPSC 6160 without complicating the project too much. This game was built in a way that could be expanded upon in the future.
  I think the pace of the game makes it exciting and the random nature of spawning will keep you on your toes. 
  
Reasoning:
  I chose to structure the game in line with the MVC architecture. The game loop controlls the flow of the game, the classes are models of object behavior, and the view is simply the pygame surface. 
  This approach fits well with the abstraction of the game and it's constituent objects. This object oriented design makes it possible to reuse methods and keep object data organized.
  
Image of classes:

![IMG_7284](https://user-images.githubusercontent.com/46658528/222577047-c6e359c1-666e-4b16-ad92-e3984ddc74e4.jpeg)

Future work:

The game engine can be enhanced by allowing more than one attempt plus more user control. More physics elements can be added to increase the dynamic nature of the game. Another good enhancement would be incorporating more user events to allow for more actionable inputs. The current game entirely functions using mouse motion and click. 
Many new feature can be added such as: show hit points upon collision, show remaining ammo, and also different ammo modes.

Generalization: This game engine can be adopted for free runner games as it already has the motion and collision aspects. The monsters spawn on timmer events so we have an infinite supply of enemies.
