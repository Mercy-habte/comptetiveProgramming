class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        FizzBuzz_list = []
        
        for i in range(1, n+1):
            if i%5==0 and i%3==0:
                FizzBuzz_list.append("FizzBuzz")
            elif i%5 ==0:
                FizzBuzz_list.append("Buzz")
            elif i%3 == 0:
                FizzBuzz_list.append("Fizz")
            else:
                FizzBuzz_list.append(str(i))
        return FizzBuzz_list
