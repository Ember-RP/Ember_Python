# Ember_Python
Ember's Python scripts


`ExpansionGenerator/GameObjectGenerator.py` is a file that seeks to generate expansion content. To work it, here are some instructions:
1. Have Python installed (obviously)
2. Take your server's GameObjectDisplayInfo.dbc -> GameObjectDisplayInfo.csv and put it into a folder with the python program.
3. Take your new content/wmos/m2s/etc in a ready-to-go patch format, but put it in your folder with GameObjectDisplayInfo.csv, and GameObjectGenerator.py. It should look like this https://i.gyazo.com/70ada5f7debfdc5aac906a22aecd4611.png
4. Start the program in python, run option 1. A new file, NewObjects.csv will be added to your folder. This file needs to be copy and pasted into your existing GameObjectDisplayInfo.csv WITHOUT any blank spaces at the end.
5. If you'd like to spawn those objects in-game, option 2 will take all object names and create an SQL file to enter them into the database. You can enter incremental database entries along with prefix and postfix names (ie: [PREFIX] MerchantTent01 [POSTFIX]). If the SQL file is not working, you may need to edit the python program in notepad to change the 1 query line.
