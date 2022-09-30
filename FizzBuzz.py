class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        # ans list
        array = []

        for num in range(1,n+1):

        

            number = ""

            if (num % 3 == 0):
                # Divides by 3
                number += "Fizz"
            if (num % 5 == 0):
                # Divides by 5
                number += "Buzz"
            if (not number):
                # Not divisible by 3 or 5
                number = str(num)

            # Append the current answer str to the ans list
            array.append(number)  

        return array
