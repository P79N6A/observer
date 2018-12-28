from bs4 import BeautifulSoup as BS
import re

test='口碑佳作《驴得水》被许多剧迷称作"神剧"'

_info = re.search('《[^》]+》',test,flags=0).group()
print(_info)