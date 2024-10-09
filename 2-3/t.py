q = int(input())

last_hash = 0
err = 0
is_error = False

for i in range(q):
    block = int(input())
    current_hash = block % 256
    r = (block // 256) % 256
    m = block // 256 ** 2
    new_hash = (37 * (m + r + last_hash)) % 256
    if new_hash != current_hash or new_hash >= 100:
        if is_error is False:
            err = i
            is_error = True
    last_hash = current_hash

if is_error is False:
    print(-1)
else:
    print(err)
