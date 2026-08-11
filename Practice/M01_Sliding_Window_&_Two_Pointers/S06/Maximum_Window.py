#Leetcode: 1652
class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        result = [0] * n
        
        # Base case: if k is 0, return all zeros
        if k == 0:
            return result
        
        # Define the initial window bounds based on the sign of k
        if k > 0:
            start = 1
            end = k
        else:
            start = n + k
            end = n - 1
            
        # Calculate the sum of the initial window
        current_window_sum = 0
        for i in range(start, end + 1):
            current_window_sum += code[i % n]
            
        # Slide the window across the array
        for i in range(n):
            result[i] = current_window_sum
            
            # Slide window forward: subtract old start, add new element after end
            current_window_sum -= code[start % n]
            start += 1
            end += 1
            current_window_sum += code[end % n]
            
        return result
