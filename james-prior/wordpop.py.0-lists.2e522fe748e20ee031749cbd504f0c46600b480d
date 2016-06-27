import collections

TEXT_BOUNDARY = '***'


def convert_file_to_line_list(f):
    file_lines = []
    for line in f:
        file_lines.append(line)
    return file_lines


def strip_header(lines):
    pass_on = False
    stripped_lines = []
    for line in lines:
        if pass_on and line != '\n':
            stripped_lines.append(line.strip())
        elif line.startswith(TEXT_BOUNDARY):
            pass_on = True
    return stripped_lines


def strip_footer(lines):
    pass_on = True
    stripped_lines = []
    for line in lines:
        if pass_on:
            if line.startswith(TEXT_BOUNDARY):
                pass_on = False
            else:
                stripped_lines.append(line.strip())
    return stripped_lines


def strip_all(lines):
    return strip_footer(strip_header(lines))


def lines_to_word_array(lines):
    words = []
    for line in lines:
        words.extend(line.split())
    return map(lambda x:x.lower(), words)


def parse(f):
    return lines_to_word_array(strip_all(convert_file_to_line_list(f)))

vocabulary_size = 50000


def build_dataset(words):
  count = []
  count.extend(collections.Counter(words).most_common(vocabulary_size - 1))
  return count


