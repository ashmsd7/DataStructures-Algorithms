class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        if len(s) > 12:
            return []

        res = []

        def backtrack(index, path):
            if index == len(s):
                if len(path) == 4:
                    res.append('.'.join(path))
                return

            if len(path) == 4:
                return

            for i in range(1, 4):
                string = s[index:index+i]
                if index + i > len(s):
                    break

                if int(string) > 255:
                    continue

                if len(string) > 1 and string[0] == '0':
                    continue

                path.append(string)
                backtrack(index+i, path)
                path.pop()

        backtrack(0, [])
        return res