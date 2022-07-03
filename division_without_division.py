'''
Given two integers dividend and divisor, divide two integers without using multiplication, division, and mod operator.
'''

def divide(self, dividend: int, divisor: int) -> int:

    # Constants.
    MAX_INT = 2147483647        # 2**31 - 1
    MIN_INT = -2147483648       # -2**31
    HALF_MIN_INT = -1073741824  # MIN_INT // 2

    # Special case: overflow.
    if dividend == MIN_INT and divisor == -1:
        return MAX_INT

    # We need to convert both numbers to negatives.
    # Also, we count the number of negatives signs.
    negatives = 2
    if dividend > 0:
        negatives -= 1
        dividend = -dividend
    if divisor > 0:
        negatives -= 1
        divisor = -divisor

    quotient = 0
    # Once the divisor is bigger than the current dividend,
    # we can't fit any more copies of the divisor into it anymore */
    while divisor >= dividend:
        # We know it'll fit at least once as divivend >= divisor.
        # Note: We use a negative powerOfTwo as it's possible we might have
        # the case divide(INT_MIN, -1). */
        powerOfTwo = -1
        value = divisor
        # Check if double the current value is too big. If not, continue doubling.
        # If it is too big, stop doubling and continue with the next step */
        while value >= HALF_MIN_INT and value + value >= dividend:
            value += value;
            powerOfTwo += powerOfTwo
        # We have been able to subtract divisor another powerOfTwo times.
        quotient += powerOfTwo
        # Remove value so far so that we can continue the process with remainder.
        dividend -= value

    # If there was originally one negative sign, then
    # the quotient remains negative. Otherwise, switch
    # it to positive.
    return -quotient if negatives != 1 else quotient
  
  '''
  From this, we know that we can fit 80384 into 93706, and that 80384 must be a multiple of 157. But how many copies of 157 is this?

Well, each time we double a number we also double the amount of copies of the original number. So because we doubled 157 nine times, we must have had 2⁹ copies of 157. Indeed, 2⁹ · 157 = 80384. Yay!

But, we still have some left over—in fact we have 93706 - 80384 = 13322 left over! That's still a lot of copies of 157 we haven't counted! So what could we do about this? Well, if we work out how many times 157 fits into 13322, we could just add that to 512 to get our result.

How can we work out how many times 157 fits into 13322? Well, we just repeat the same process, adding to the result as we go, until there's nothing left for 157 to fit into.

If we do this, we'll find that 157 · 2⁶ = 10048 is the highest power that fits into 13322, leaving us with 13322 - 10048 = 3274 and a quotient so far of 2⁶ + 2⁹ = 576 (if you noticed that 10048 looks very familiar, well done. We'll be looking at this in approach 3).

We repeat this process until the dividend is less than 157.
'''
