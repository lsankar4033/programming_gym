import re

# NOTE generator-version of str.split used for performance reasons
def _itersplit(s, sep=None):
    exp = re.compile(r'\s+' if sep is None else re.escape(sep))
    pos = 0
    while True:
        m = exp.search(s, pos)
        if not m:
            if pos < len(s) or sep is not None:
                yield s[pos:]
            break
        if pos < m.start() or sep is not None:
            yield s[pos:m.start()]
        pos = m.end()

# Returns true if s has a '.' that doesn't occur at the end of the file
def _is_filename(s):
    dot_idx = s.find(".")
    return dot_idx != -1 and dot_idx != len(s) - 1

def _compute_path_length(subdir_lengths, filename):
    return sum(subdir_lengths) + len(subdir_lengths) + len(filename)

class Solution(object):

    # Solution template requires camel case, but I just use underscore case everywhere else...
    def lengthLongestPath(self, input):
        max_length = 0
        cur_subdir_lengths = []
        last_depth = 0
        last_length = 0
        for line in _itersplit(input, "\n"):
            line_without_tabs = line.lstrip("\t")
            length = len(line_without_tabs)
            depth = len(line) - length # counts # of leading tabs
            assert depth <= last_depth + 1, "String has multiple depth increases at line {}".format(line)

            if depth == last_depth + 1:
                cur_subdir_lengths.append(last_length)

            elif depth < last_depth:
                num_dirs_to_pop = last_depth - depth
                for _ in range(num_dirs_to_pop):
                    cur_subdir_lengths.pop()

            if _is_filename(line_without_tabs):
                path_length = _compute_path_length(cur_subdir_lengths, line_without_tabs)
                if path_length > max_length:
                    max_length = path_length

            last_length = length
            last_depth = depth

        return max_length
