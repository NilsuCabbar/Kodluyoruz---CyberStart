Python 3.13.0 (tags/v3.13.0:60403a5, Oct  7 2024, 09:38:07) [MSC v.1941 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import math
... 
... def euclideanDistance(point1, point2):
...     return math.sqrt((point2[0] - point1[0])**2 + (point2[1] - point1[1])**2)
... 
... x1 = float(input("1. noktanın x koordinatını girin: "))
... y1 = float(input("1. noktanın y koordinatını girin: "))
... x2 = float(input("2. noktanın x koordinatını girin: "))
... y2 = float(input("2. noktanın y koordinatını girin: "))
... 
... point1 = (x1, y1)
... point2 = (x2, y2)
... 
... distance = euclideanDistance(point1, point2)
... 
