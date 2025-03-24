import os

with open('the_time.txt') as f:
    t = f.read()

html = f"""<!DOCTYPE html>
<html>
<body>

<h1>Most recent commit</h1>
<p>{t}</p>

</body>
</html>
"""

os.makedirs('./static', exist_ok=True)
with open('static/index.html', 'w') as f:
    f.write(html)

