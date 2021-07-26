import re
from model.file import File
from model.regex import Regex 

patterns = {
    "30NAMA": "(.+?)_S(\d{2,})E(\d{2,})_.*?(\d{3,})p_.*?_30nama.[mkv|mp4]"
}

for filename in File().ls():
    result = Regex().search(patterns["30NAMA"], filename)
    if result is False:
        continue
    File().move_series(filename, result[0], result[1], result[3])