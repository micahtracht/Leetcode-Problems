class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        '''
        So let's think about how I could solve this.

        Say I have two cars, A and B, and I want to determine
        if they'll merge in a fleet.

        Assume that P(A) > P(B)

        They merge if S(A) < S(B), but not always.

        We can calculate the time they'll take to arrive:
        T(A) = (D - P(A))/S(A)
        T(B) = (D - P(B))/S(B)

        If T(B) <= T(A), then they'll merge, assuming A starts ahead.

        Say I have three cars.
        I add the first one. 
        
        Then I add the second, and I check if it collides.
        If it does, then I know it is in that fleet.
        If it doesn't, I must have at least two.

        Not sure where to go from there. What if I sort by positions?

        That makes sense, bc it tells me how to compare them kinda

        So I have a car.
        I add it to the stack.
        If it collides, that forms a fleet.
        I can never get a fleet in front of that one if I start from behind.
        I keep adding, and see if I collide.
        If I don't, fleet count += 1.
        Else, do nothing.
        
        I need to find how to see if it'll collide.
        Well, car A starts the furthest ahead, so I can use that one

        Okay, here's the approach
        sort the cars by position (descending)
        maintain a stack
        add each car to the stack, and check if it is in a fleet
        with the top element

        If yes, pop it
        If no, add it

        return len(stack)
        '''
        sortedIndices = [i for i in range(len(position))]
        sortedIndices.sort(key=lambda i: position[i])
        sortedIndices.reverse()
        #print(sortedIndices)
        stack = []
        for i in sortedIndices:
            if not stack:
                stack.append(i)
                continue
            
            indexFleetCar = stack[-1]
            timeFleet = (target - position[indexFleetCar])/speed[indexFleetCar]
            timeCurr = (target - position[i])/speed[i]
            #print(timeCurr, timeFleet)

            if timeCurr > timeFleet:
                stack.append(i)
        
        return len(stack)
