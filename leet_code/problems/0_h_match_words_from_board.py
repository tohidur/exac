"""
Question: Word Search II

Given an m x n board of characters and a list of strings words, return all
words on the board.

Each word must be constructed from letters of sequentially adjacent cells,
where adjacent cells are horizontally or vertically neighboring.
The same letter cell may not be used more than once in a word.

Constraints:
    m == board.length
    n == board[i].length
    1 <= m, n <= 12
    board[i][j] is a lowercase English letter.
    1 <= words.length <= 3 * 104
    1 <= words[i].length <= 10
    words[i] consists of lowercase English letters.
    All the strings of words are unique.

Ex 1: 
Input: board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],
                ["i","f","l","v"]],
       words = ["oath","pea","eat","rain"]
Output: ["eat","oath"]

Ex 2:
Input: board = [["a","b"],["c","d"]], words = ["abcb"]
Output: []
"""

class Solution:
    def findWords(self, board, words):
        matched = []
        for word in words:
            is_matched = self._find_word(board, word)
            if is_matched:
                matched.append(word)
        return matched

    def _get_lp_map(self, board):
        if hasattr(self, '_lp_map'):
            return getattr(self, '_lp_map')

        lp_map = {}

        for row_idx, row in enumerate(board):
            for col_idx, letter in enumerate(row):
                if letter not in lp_map:
                    lp_map[letter] = []
                lp_map[letter].append([row_idx, col_idx])

        setattr(self, '_lp_map', lp_map)
        return lp_map

    def _find_word(self, board, word, visited_cells=None, start_pos=None, prev_pos=None):
        if not len(word):
            return False

        letter = word[0]

        if start_pos is None:
            "starting with word"
            lp_map = self._get_lp_map(board)
            lps = lp_map.get(letter)
            if lps is None:
                return False
            if len(word[1:]) == 0:
                return True
            for lp in lps:
                visited_cells = {}
                visited_cells[lp[0]] = {lp[1]: 1}
                is_match = self._find_word(board, word[1:], visited_cells=visited_cells, start_pos=lp)
                if is_match:
                    return True
            return False
        else:
            start_row, start_col = start_pos
            if prev_pos is None:
                prev_row, prev_col = None, None
            else:
                prev_row, prev_col = prev_pos

            adj_pos = [[start_row + 1, start_col],
                       [start_row, start_col + 1],
                       [start_row - 1, start_col],
                       [start_row, start_col - 1],]

            for adj_p in adj_pos:
                adj_p_row, adj_p_col = adj_p
                if visited_cells.get(adj_p_row):
                    if visited_cells[adj_p_row].get(adj_p_col):
                        continue


                if adj_p_row == -1 or adj_p_col == -1:
                    continue

                if adj_p_row == prev_row and adj_p_col == prev_col:
                    continue

                try:
                    adj_letter = board[adj_p_row][adj_p_col]
                except IndexError:
                    continue

                if adj_letter != letter:
                    continue

                if adj_p_row in visited_cells:
                    visited_cells[adj_p_row].update({adj_p_col: 1})
                else:
                    visited_cells[adj_p_row] = {adj_p_col: 1}

                remaining_word = word[1:]
                if len(remaining_word):
                    if not self._find_word(board, remaining_word,
                                           visited_cells=visited_cells,
                                           start_pos=adj_p,
                                           prev_pos=start_pos):
                        continue
                return True

            return False


if __name__ == "__main__":
    sol = Solution()
    print(sol.findWords([["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]],
                        ["oath","pea","eat","rain"]))
    print(sol.findWords([["a"]], ["a"]))
    print(sol.findWords([["a","b","c"],["a","e","d"],["a","f","g"]],
                        ["abcdefg","gfedcbaaa","eaabcdgfa","befa","dgc","ade"]))
    print(sol.findWords([["a","b","c","e"],["x","x","c","d"],["x","x","b","a"]],
                        ["abc","abcd"]))
    print(sol.findWords([["a","a"],["a","a"]], ["aaaaa"]))
