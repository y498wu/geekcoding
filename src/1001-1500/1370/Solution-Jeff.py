
# @lc app=leetcode id=1370 lang=python3

# @lc code=start


class Solution:
    def sortString(self, s: str) -> str:
        def sort(m, r):
            m1 = {}
            for k in m:
                if m[k] != 0:
                    r += k
                    m1 = dict({k: m[k]-1}, **m1)
            return m1, r

        _m = {}
        for c in s:
            _m[c] = _m[c]+1 if _m.keys().__contains__(c) else 1

        result = ''
        m = _m
        while len(m) > 0:
            m, result = sort(m, result)

        return result


if __name__ == '__main__':
    print(Solution().sortString('aaaabbbbcccc'))

# @lc code=end