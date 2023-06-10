"""paint , for drawing shapes.
exercises
1. add a color
2. complete circle
3. complete rectangle
4. cimplete triangle
5. add width parameter
""
from turtle import*

for freegames import vector

  def line(start, end):
      "draw line from start to end."
         up()
         goto(start.x, start.y)
           down()
         goto(end.x, end.y)

  
  def sqare(start, end):
       "draw square from start to end."
         up()
              goto(start.x, start.y)
              down()
                begin_fill()
                 for count in range(4);
                forward(end.x - stard.y)
                 left(90)
                  end_fill()

   def circle(start, end):
       "draw circle from start to end."
                 pass #TOOO

   def rectangle(start, end):
       "draw rectangle from start to end."
                 pass #TOOO

   def triangle(start, end):
       "draw triangle from start to end."
                 pass #TOOO

   def tap(x,y):
       "store starting point or draw shape."
       start = state['start']
       if start is none:
           state['state'] = vector(x, y)
           else:
               shape = state['shape']
               end = vector(x, y)
               shape(start, end) state['start'] 
                 none def store(key, value):
                   "store value in state at key."
                   state[key] = value
                   state = {'start': none, 'shape': line}
                   setup(420, 420, 370, 0)
                   onscreenclick(tap)
                    listen()
                   onkey(undo, 'u')
                     
                     onkey(lambda: color('black'), 'K')
                     onkey(lambda: color('white'), 'W')
                     onkey(lambda: color('green'), 'G')
                     onkey(lambda: color('blue'), 'B')
                     onkey(lambda: color('red'), 'R')

                     onkey(lambda: store('shape', line), 'l' )
                     onkey(lambda: store('shape', sqare), 's')
                     onkey(lambda: store('shape', circle), 'c')
                     onkey(lambda: store('shape', rectangle), 'r')
                     onkey(lambda: store('shape', traingle), 't')
                     done()
                     """