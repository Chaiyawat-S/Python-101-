Python 3.11.2 (tags/v3.11.2:878ead1, Feb  7 2023, 16:38:35) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import turtle
>>> m=turtle.Pen()
>>> m.shape("turtle")
>>> m.speed(0)
>>> m.color("blue")
>>> for i in range(500):
...     m.forward(i*1)
...     m.left(90)
... 
...     
>>> for i in range(25):
...     m.up()
...     m.goto(300,300-(i*25))
...     m.stamp()
...     m.goto(-300,300-(i*25))
...     m.stamp()
... 
...     
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
61
62
63
64
65
66
