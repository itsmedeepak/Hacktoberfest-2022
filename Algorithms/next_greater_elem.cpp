
class Solution:
    def nextLargerElement(self, arr, n):
        # code here
        s = []
        for i in range(len(arr)):
            while s and s[-1].get("value") < arr[i]:
                d = s.pop()
                arr[d.get("ind")] = arr[i]
            s.append({"value": arr[i], "ind": i})
        while s:
            d = s.pop()
            arr[d.get("ind")] = -1
        return arr
 
 
if __name__ == "__main__":
    print(Solution().nextLargerElement([6, 8, 0, 1, 3], 5))
