#!/usr/bin/python

import sys
import re

"""
Read the ToolsOfTheTrade Markdown file (readme.md) and alpha-sort the
contents - currently markdown "Header 3" and table rows.
This is a terrible 5-minute hack for this particular readme.md
But it does work.
"""

file_object = open("./readme.md")
lines = file_object.readlines()
header_line_numbers = []

i = 0
for i, line in enumerate(lines):
    if re.match("#", line):
        header_line_numbers.append(i)

# sort the contents of the tables within each header 3
j = 0
while j < len(header_line_numbers):
    if re.match("### ", lines[header_line_numbers[j]]):  # for header 3 blocks
        t_fst_row = header_line_numbers[j] + 4  # first row is 4 after header
        t_lst_row = header_line_numbers[j + 1] - 1  # last row is 2 before next header
        lines[t_fst_row:t_lst_row] = sorted(lines[t_fst_row:t_lst_row])
    j += 1

for line in lines:
    sys.stdout.write(line)
