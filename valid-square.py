class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        l1 = abs((p1[0]-p2[0])**2) + abs((p1[1]-p2[1])**2)
        l2 = abs((p2[0]-p3[0])**2) + abs((p2[1]-p3[1])**2)
        l3 = abs((p3[0]-p4[0])**2) + abs((p3[1]-p4[1])**2)
        l4 = abs((p1[0]-p4[0])**2) + abs((p1[1]-p4[1])**2)

        diag1 = abs((p1[0]-p3[0])**2) + abs((p1[1]-p3[1])**2)
        diag2 = abs((p2[0]-p4[0])**2) + abs((p2[1]-p4[1])**2)
        #print(l1, l2, l3 , l4, diag1)
        side = {l1,l2,l3,l4,diag1,diag2}
        sides = []
        for i in side:
            sides.append(i)
        print(sides)
        if len(sides) == 2:
            if (sides[0] > sides[1]) and (sides[0] == 2*sides[1]):
                return True
            elif  (sides[1] > sides[0]) and (sides[1] == 2*sides[0]):
                return True
            else:
                return False
        
        else:
            return False
