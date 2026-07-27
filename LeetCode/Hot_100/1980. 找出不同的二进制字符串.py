"""
给你一个字符串数组 nums ，该数组由 n 个 互不相同 的二进制字符串组成，且每个字符串长度都是 n 。请你找出并返回一个长度为 n 且 没有出现 在 nums 中的二进制字符串。如果存在多种答案，只需返回 任意一个 即可。

 

示例 1：

输入：nums = ["01","10"]
输出："11"
解释："11" 没有出现在 nums 中。"00" 也是正确答案。
示例 2：

输入：nums = ["00","01"]
输出："11"
解释："11" 没有出现在 nums 中。"10" 也是正确答案。
示例 3：

输入：nums = ["111","011","001"]
输出："101"
解释："101" 没有出现在 nums 中。"000"、"010"、"100"、"110" 也是正确答案。
 

提示：

n == nums.length
1 <= n <= 16
nums[i].length == n
nums[i] 为 '0' 或 '1'
nums 中的所有字符串 互不相同
"""

class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n = len(nums)
        for i in range(n+1):
            s = bin(i)[2:]
            l = len(s)
            for i in range(n-l):
                s = "0" + s
            if s not in nums:
                return s 
            
            
"""        
class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n = len(nums)
        # 预处理对应整数的哈希集合
        vals = {int(num, 2) for num in nums}
        # 寻找第一个不在哈希集合中的整数
        val = 0
        while val in vals:
            val += 1
        # 将整数转化为二进制字符串返回
        res = "{:b}".format(val)
        return '0' * (n - len(res)) + res

作者：力扣官方题解
链接：https://leetcode.cn/problems/find-unique-binary-string/solutions/951996/zhao-chu-bu-tong-de-er-jin-zhi-zi-fu-chu-0t10/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
"""