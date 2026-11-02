class Solution:
    def compress(self, chars: List[str]) -> int:
        if len(chars) ==1:
            return 1
        left = 0
        right = 0
        write = 0
        while right < len(chars):
            while right < len(chars) and chars[right] == chars[left]:
                right +=1
            # now chars[right] != chars[left]
            count = right - left
            chars[write] = chars[left]
            write +=1
            if count > 1:
                for digit in str(count):
                    chars[write] = str(digit)
                    write +=1
            left = right


        return write