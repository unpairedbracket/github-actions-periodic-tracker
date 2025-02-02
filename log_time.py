from datetime import datetime

now = datetime.now()

with open('the_time.txt', 'w') as f:
    f.write(f"{now}\n")

