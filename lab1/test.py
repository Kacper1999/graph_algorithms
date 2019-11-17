import time
import os
from lab1.min_max_path_weight import find_result

path = "graphs\\"
files = os.listdir(path)
print(files)
ok_count = 0

for i in files:
    with open(path + i) as f:
        result = int(f.readline().split()[3])

    start_time = time.time()
    my_result = find_result(i)
    end_time = time.time()

    if result == my_result:
        ok_count += 1
        print(i + ": OK", end=' ')
    else:
        print(i + ": answer is: " + str(result) + " found: " + str(my_result), end=' ')
    print('(%f)' % (end_time - start_time))

print(str(ok_count) + "/" + str(len(files)))
