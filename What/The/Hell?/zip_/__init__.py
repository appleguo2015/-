import os
os.mkdir('boom')
for i in range(1000):
    with open('boom/%d.txt'% i, 'w') as f:
        f.write('哈' * 100000)