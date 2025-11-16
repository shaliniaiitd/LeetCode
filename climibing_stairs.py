# You are climbing a staircase. It takes n steps to reach the top.
#
# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

def climbStairs(self, n: int) -> int:
    count = 0
    for x in range(n + 1):
        for y in range(n + 1):
            if x + 2 * y == n:
                count = count + 1
                if x == y:
                    count = count + 1
                print(x, y, count)
    return count
