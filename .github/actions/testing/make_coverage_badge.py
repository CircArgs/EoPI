import re
import os

GITHUB_WORKSPACE = lambda p: os.path.join(os.environ["GITHUB_WORKSPACE"], p)

template = open(".github/actions/testing/badge_template.svg").read()
coverage_summary = open(GITHUB_WORKSPACE("coverage_summary")).read()
FILL = "red"
VALUE = "failing"
try:
    regex = r"(?<=^TOTAL).*?$"
    total = [
        i for i in re.findall(regex, coverage_summary, re.MULTILINE)[0].split(" ") if i
    ]
    VALUE = f"Stmts: {total[0]} | Miss: {total[1]} | Cover: {total[2]}"
    cover = int(total[2].replace("%", ""))

    if cover >= 90:
        FILL = "#1ac400"
    elif cover >= 80:
        FILL = "#d1ea00"
    elif cover >= 70:
        FILL = "#e3e000"
    elif cover >= 60:
        FILL = "#f2d600"
    elif cover >= 50:
        FILL = "#ffcc0b"
    elif cover >= 40:
        FILL = "#ffaf23"
    elif cover >= 30:
        FILL = "#ff9239"
    elif cover >= 20:
        FILL = "#ff774d"
    elif cover >= 10:
        FILL = "#fb5f5f"

except:
    pass


template = template.replace("THE_NAME", "coverage")
template = template.replace("THE_VALUE", VALUE)
template = template.replace("THE_FILL", FILL)
with open(GITHUB_WORKSPACE("coverage_badge.svg"), "w") as f:
    f.write(template)
