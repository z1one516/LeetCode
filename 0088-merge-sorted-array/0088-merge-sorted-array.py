class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        index1, index2, merged_index = len(nums1)-len(nums2)-1, len(nums2)-1,len(nums1)-1


        while index1 >=0 and index2>=0:
            if nums1[index1] > nums2[index2]:
                nums1[merged_index] = nums1[index1]
                index1 -= 1
            else:
                nums1[merged_index] = nums2[index2]
                index2 -= 1
            merged_index -= 1

        # 리스트2에 남은 요소들을 리스트1로 복사
        while index2 >=0:
            nums1[merged_index]=nums2[index2]
            index2 -= 1
            merged_index -=1
        