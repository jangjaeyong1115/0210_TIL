for tc in range(int(input())):
    a = list(map(str,input()))
    b = []
    aeiou = ['a','e','i','o','u']
    for alphabet in a:
        if alphabet in aeiou:
            continue
        else:
            b.append(alphabet)
    print('#{} {}'.format(tc+1,''.join(b)))