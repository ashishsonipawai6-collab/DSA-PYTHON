class Solution(object):
    def checkInclusion(self, s1, s2):
        if len(s1) > len(s2):
            return False

        freq = [0] * 26
        window_freq = [0] * 26

        window_size = len(s1)

        # First window
        for i in range(window_size):
            freq[ord(s1[i]) - ord('a')] += 1
            window_freq[ord(s2[i]) - ord('a')] += 1

        if freq == window_freq:
            return True

        # Sliding window
        for right in range(window_size, len(s2)):
            
            # Add new character
            window_freq[ord(s2[right]) - ord('a')] += 1

            # Remove old character
            window_freq[ord(s2[right - window_size]) - ord('a')] -= 1

            if freq == window_freq:
                return True

        return False

        