import re
import os

GITHUB_WORKSPACE= lambda p: os.path.join(os.environ['GITHUB_WORKSPACE'], p)

template=open('./badge_template.svg').read()
coverage_summary=open(GITHUB_WORKSPACE('coverage_summary')).read()
regex = r"(?<=^TOTAL).*?$"
VALUE=' | '.join([i for i in re.findall(regex, coverage_summary, re.MULTILINE)[0].split(' ') if i])
template=template.replace('THE_NAME', 'COV')
template=template.replace('THE_VALUE', VALUE)
with open(GITHUB_WORKSPACE('coverage_badge.svg'), 'w') as f:
    f.write(template)