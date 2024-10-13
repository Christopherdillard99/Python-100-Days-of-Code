# Day 21: Snake Game - Part 2:

## Topics covered today:
1. Continuing Object-Oriented Programming and **introducing slicing to simplify code in for loops**:
- for example, think piano_keys = ["a","b","c","d","e","f","g"]
- now what if we just want keys c, d, and e? piano_keys[2:5]
- and why is this 2-5 and not 2-4? well because it is a range that checks for all items between these markers and list start at position 0 in Python
- now, what if we just want to get everything from the left or right of an item in the list? print(piano_keys[2:]) will print keys c-g (it would exclude the item in the position you specify)
- print(piano_keys[:5]) will print keys a-e
- you can specify a third number after a colon to specify the increment like how print(piano_keys[2:5:2]) will return ['c', 'e'] in the console
- now let's say you want every second item from the entire list: print(piano_keys[::2]) <-- this yields ['a', 'c', 'e', 'g']
- but, what if you want to print the list starting from the end? print(piano_keys[::-1])
2. Adding a scoreboard, setting the location at certain cordinates, and not printing ontop of itself (replace previous instance)
3. Detecing collision with walls and collision with the snake own tail
- incorporate slicing in the following code snippet so that we only use the for loop on segments after the head to check for distance from the head, like so:

``` python
for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()
```
4. Also, just learning that I could've just been entering code blocks in my README files by wrapping the code in backticks ``` this whole time... will def be doing this from now on :) oooh and you can specify the code language right after the three backticks

## Snake Game: Part 2 (completed snake game with new segments added after each scored point):
![Start of the game](https://github.com/user-attachments/assets/64a6acc0-6876-4615-a81e-66ca3d8f22fb)

## Just for fun: changing the colors of each new segment to a random color from a list:
![Change segment colors for fun](https://github.com/user-attachments/assets/41307150-5bec-4f9f-abf6-c4b4e49d0b82)

P.S. to do this I had to import the random module in the snake.py file and set a CONSTANT at the top like COLORS = ("green", "yellow", "brown", "white") 
Then, I modified the add_segment() function to look like this: 
``` python
def add_segment(self, position): 
        new_segment = Turtle("square")
        new_segment.color(random.choice(COLORS))
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)
```



