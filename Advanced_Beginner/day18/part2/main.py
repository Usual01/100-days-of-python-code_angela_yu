
# using colorgram to loop through the image to generate/ get the color codes
#import colorgram
# rgb_colors = []
# colors = colorgram.extract('image.jpg', 25)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_colors = (r, g, b)
#     rgb_colors.append(new_colors)
#print(rgb_colors)
import turtle
import random

turtle.colormode(255)

miracle = turtle.Turtle()
color_codes = [(25, 240, 228), (47, 231, 241), (25, 234, 244), (29, 245, 235),
    (13, 160, 109), (27, 212, 113), (134, 167, 191), (48, 104, 142),
    (146, 82, 57), (196, 143, 164), (145, 66, 87), (141, 178, 155), 
    (15, 34, 56), (172, 155, 53), (66, 116, 93), (191, 89, 116), (24, 171, 188),
    (201, 94, 74), (14, 37, 25), (55, 35, 19), (55, 23, 38), 
    (229, 175, 166), (180, 186, 217), (56, 156, 176), (84, 154, 113)]


miracle.setheading(225)
miracle.penup()
miracle.hideturtle()
miracle.forward(350)
miracle.setheading(0)

for m in range(1, 101):
    miracle.dot(20, random.choice(color_codes))
    miracle.forward(40)

    if m % 10 == 0:
        miracle.setheading(90)
        miracle.forward(50)
        miracle.setheading(180)
        miracle.forward(401)
        miracle.setheading(0)


dont_go = turtle.Screen()
dont_go.exitonclick()