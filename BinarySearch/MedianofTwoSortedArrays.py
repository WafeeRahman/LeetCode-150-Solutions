#Given two sorted arrays we need to find the median of the two sorted arrays
#To do this, we need to find both the middle partitions of a and b, where the partitions of both lists fit the median
#Where the longer list[rightPart] >= shortlist mid[point] and shorterlist[rightPart] >= longerList[midPart] 
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        total = len(nums1) + len(nums2)
        half = total // 2
        A = nums1
        B = nums2

        if len(A) > len(B):
            A,B = B, A
        #Set A to the shorter list
        l = 0
        r = len(A)-1
        
        #Continously Compare the Middle partition until we reach the correct middle partition
        while True:
            mid1 = (l+r) // 2
            mid2 = half - mid1 - 2
            print(mid1, mid2, half)

            #Compare Middle Values
            Aleft = A[mid1] if mid1 >= 0 else float("-infinity")
            Aright = A[mid1+1] if mid1+1 < len(A) else float("infinity")
            Bleft = B[mid2] if mid2 >= 0 else float("-infinity")
            Bright = B[mid2+1] if mid2+1 < len(B) else float("infinity")

            print(Aleft, Aright, Bleft, Bright)
            
            #If we find the correct partition, return the correct value depending on even length and odd length
            if Aleft <= Bright and Bleft <= Aright:
                if total % 2 == 0:
                    return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
                return min(Aright, Bright)
            #OTWS set the boundaries, we want smaller values if the shorter list mid is greater than the longer list right
            if Aleft > Bright:
                r = mid1-1
            else:
                l = mid1+1
            
        return -1


        
