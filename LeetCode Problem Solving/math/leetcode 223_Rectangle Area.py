# Given the coordinates of two rectilinear rectangles in a 2D plane, return the total area covered by the two rectangles.
class Solution:
    def computeArea(self, A: int, B: int, C: int, D: int, E: int, F: int, G: int, H: int) -> int:
        x = [A,C,E,G]
        y = [D,H,B,F]
        x.sort()
        y.sort()
        each_sum = (C-A)*(D-B) + (G-E)*(H-F)
        #no intersection
        if x==[A,C,E,G] or x==[E,G,A,C] or y==[B,D,F,H] or y==[F,H,B,D]:
            return each_sum
        #intersection
        else:
            intersect = (x[2]-x[1]) * (y[2]-y[1])
            return each_sum - intersect
