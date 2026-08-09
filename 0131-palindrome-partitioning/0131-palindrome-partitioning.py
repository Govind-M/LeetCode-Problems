class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []

        def isPallindrome(rem):
            return rem == rem[::-1]

        def backtrack(path, remaining):

            if not len(remaining):
                result.append(path[:])


            for i in range(1, len(remaining) + 1):
                choice = remaining[:i]

                if not isPallindrome(choice):
                    continue

                path.append(choice)
                backtrack(path, remaining[i:])
                path.pop()

            
        backtrack([],s)
        return result

    
    

