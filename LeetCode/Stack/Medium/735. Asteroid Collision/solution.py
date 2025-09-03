class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stck = []
        for a in asteroids:
            while stck and a<0 and stck[-1]>0:
                if stck[-1]<-a:
                    stck.pop()
                    continue
                elif stck[-1] == -a:
                    stck.pop()
                break
            else:
                stck.append(a)

        return stck


        """
        Question:
        asteroids: List[int]: size of asteroid and sign indicating direction
        return : List[int]: remaining asteroids after any collisions

        Solution:
        Use a stack to push and if stck[-1]*asteroid is negative pop instead

        """