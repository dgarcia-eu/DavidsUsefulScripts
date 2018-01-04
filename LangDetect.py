from langdetect import detect
from langdetect import lang_detect_exception

with open("file.in", "rt") as filein:
  for line in filein:
    try:
      ld = detect(line)
    except lang_detect_exception.LangDetectException:
      ld = "-"
  print(ld)
