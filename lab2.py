# Function to create a list from a string of comma-separated values
def create_list(csv_string):
    # TODO: Convert the string into a list of values, remove leading/trailing spaces
    return (csv_string.split(', '))

# Function to concatenate two lists without using +
def concatenate_lists(lst1, lst2):
    # TODO: Implement concatenation using loops
    lst3 = []
    for i in lst1:
        lst3.append(i)
    for i in lst2:
        lst3.append(i)
    return lst3


# Function to multiply each element in a list by a scalar without using *
def scalar_multiply(lst, scalar):
    # TODO: Implement multiplication using loops
      total = []
      for i in lst:
        multnum = 0
        multiple = 0
        while multiple < scalar:
          multnum += i
          multiple += 1
        total+=[multnum]
      return(total)

assert create_list("apple, banana, cherry") == ["apple", "banana", "cherry"]
assert concatenate_lists([1, 2], [3, 4]) == [1, 2, 3, 4]
assert scalar_multiply([2, 3], 2) == [4, 6]
#################################################################################
'''
In the cell below, for instance, you'll find a stubbed out function named is_perfect, which should return True if the number passed to it is a "perfect" number, and False otherwise.

A perfect number is a postive integer whose value is equal to the sum of its proper divisors (i.e., its factors excluding the number itself). 6 is the first perfect number, as its divisors 1, 2, and 3 add up to 6.

Fill in your own implementation of the function below:
'''
def is_perfect(n):
    if n <= 0:
        return False
    sum = 0
    for i in range(1, n // 2 + 1):
        if n % i == 0:
            sum += i
    return sum == n
    
#################################################################################
'''
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Complete the following function, which finds the sum of all the multiples of 3 or 5 below the argument n.
'''
def multiples_of_3_and_5(n):
    sum = 0
    round = 1
    while round < n:
      if round % 3 == 0:
        sum += round
      elif round % 5 == 0:
        sum += round
      round += 1
    return sum 
# (3 points)


#################################################################################
'''
Exercise 3: Integer Right Triangles
Given a perimeter of 60, we can find two right triangles with integral length sides: [(10, 24, 26), (15, 20, 25)]. Complete the following function, which takes an integer p and returns the number of unique integer right triangles with perimeter p.

Note that your solution should take care to limit the number of triangles it tests --- your function must complete in under 3 seconds for all values of p used in the tests to earn credit.
'''

def integer_right_triangles(p):
    count = 0
    for a in range(1,p):
      for b in range(a,p):
        c = p - a - b
        if (a**2 + b**2 == c**2 and a + b + c == p):
          count += 1
    return count
    

#################################################################################
def test1():
    tc = unittest.TestCase()
    for n in (6, 28, 496):
        tc.assertTrue(is_perfect(n), '{} should be perfect'.format(n))
    for n in (1, 2, 3, 4, 5, 10, 20):
        tc.assertFalse(is_perfect(n), '{} should not be perfect'.format(n))
    for n in range(30, 450):
        tc.assertFalse(is_perfect(n), '{} should not be perfect'.format(n))

#################################################################################
# EXERCISE 2
#################################################################################

# implement this function
def multiples_of_3_and_5(n):
  multiples = []
  for x in range(n):
    if (x % 3 == 0 or x % 5 == 0):
      multiples.append(x)
  sum = 0
  for x in multiples:
    sum += x
  return sum

# (3 points)
def test2():
    tc = unittest.TestCase()
    tc.assertEqual(multiples_of_3_and_5(10), 23)
    tc.assertEqual(multiples_of_3_and_5(500), 57918)
    tc.assertEqual(multiples_of_3_and_5(1000), 233168)

#################################################################################
# EXERCISE 3
#################################################################################
def integer_right_triangles(p):
    count = 0
    for a in range(1,p):
      for b in range(a,p):
        c = p - a - b
        if (a*a + b*b == c*c and a + b + c == p):
          count += 1
    return count

def test3():
    tc = unittest.TestCase()
    tc.assertEqual(integer_right_triangles(60), 2)
    tc.assertEqual(integer_right_triangles(100), 0)
    tc.assertEqual(integer_right_triangles(180), 3)
    
def main():
    test1()
    test2()
    test3()

if __name__ == '__main__':
    main()
