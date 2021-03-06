"""
            b                              b
   +----------------+             +----------------+
   |                |             |                |
   |                |             |                | a
 c |                |           c |                |
   |                | a           |                |    f
   +----------->    |             |                | <----+
            d       |             |                |      | e
                    |             |                       |
                                  +-----------------------
                                               d
Draw a line of length a. Then draw further lines of lengths b, c, etc. How does the a-line get crossed? From the left by the d-line or from the right by the f-line, see the above picture. I just encoded the criteria for actually crossing it.

Two details:

In both cases, d needs to be at least b. In the first case to cross the a-line directly, and in the second case to get behind it so that the f-line can cross it. So I factored out d >= b.
The "special case" of the e-line stabbing the a-line from below is covered because in that case, the f-line "crosses" it (note that even if there is no actual f-line, my code uses f = 0 and thus still finds that "crossing").
"""
class Solution(object):
    def isSelfCrossing(self, x):
        """
        :type x: List[int]
        :rtype: bool
        """
        b = c = d = e = 0
        for a in x:
            if d >= b > 0 and (a >= c or a >= c-e >= 0 and f >= d-b):
               return True
            b, c, d, e, f = a, b, c, d, e
        return False