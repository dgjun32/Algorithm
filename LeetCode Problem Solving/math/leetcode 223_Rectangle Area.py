# Given the coordinates of two rectilinear rectangles in a 2D plane, return the total area covered by the two rectangles.

#solution 1. 
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

#solution 2.
class Solution:
    def computeArea(self, A: int, B: int, C: int, D: int, E: int, F: int, G: int, H: int) -> int:
        each_sum = (D-B) * (C-A) + (H-F) * (G-E) # Find area covered by second rectangle
        instersect = 0 # do they some intersect?
        if A <= G and C >= E and B <= H and D >= F:
            # Yes! There is some overlap.
            width = min(C, G) - max(A,E) # Width of the overlap portion
            height = min(D, H) - max(B,F) # Height of the overlap portion
            intersect = width * height # Area of the overlap portion
        
        return each_sum - intersect
