# Works in current directory. Arguments - "prefix", preamble file.

import sys
import re
import os
from itertools import groupby

def part_file(flist, expression):
  """ Split by regex for lists. """
  # Kind of magic. See docs for itertools package. # Python is quite a bit strange when it's coming to generalizations.
  # Looks like it works exactly like split().
  grouped = groupby(flist, lambda x: bool(expression.match(x)))
  return [list(group) for k, group in grouped]

# Informal variables section.
prefix = sys.argv[1]
preamble = sys.argv[2]
# See standard regular expressions syntax.
clones_regex = re.compile(re.escape(prefix) + r"_\d+\.tex")
ending = re.compile(r"\s*"+re.escape("\end{document}"))
problem = re.compile(r'\s*\\problem')

files = []
# Recursively list all files in directory.
for (dirpath, dirnames, filenames) in os.walk(os.getcwd()):
  files.extend(filenames)
  break

# All files matching rules for clones naming. S_1_1_ddd.tex. Magic comes while trying to avoid lexicographic sorting.
# It could be probably during selection. In Haskell I would just redefine Ord instance for type CloneName. But it's still asymptotically correct.
clones = [int(i[6:][:-4]) for i in list(filter(clones_regex.search, files))]
clones = ['%s_%d.tex' % (prefix, i) for i in sorted(clones)]

# Is usually used to trim preamble for further usage.
parted_head = part_file(open(preamble,'r'), ending)
# Text before "\end{document}"
content = parted_head[0]

# Extract prototype problems to content.
for clone in clones:
  clone_data = part_file(open(clone, 'r').readlines(), ending)[0]

  # Add header.
  content.append('\problem{%s}\n' % clone.split('.')[0])
  # There is data before "\problem". So body of the first problem is inside parted_clone[2].
  # Fails if there is no problem. And it must fail in order to notify authors.
  content.extend(part_file(clone_data, problem)[2])

# Take back "\end{document}"
content.extend(parted_head[1])
# Take back everything after "\end{document}" if present.
try: content.extend(parted_head[2])
except IndexError: pass

# Finally write file.
with open('%s_autogen.tex' % prefix, 'w') as output:
  for string in content:
    output.write("%s" % string)
