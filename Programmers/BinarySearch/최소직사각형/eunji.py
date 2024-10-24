def solution(sizes):
  
    max_w = 0
    max_h = 0

    for i in range(len(sizes)):
        x, y = map(int, sizes[i])
        w = max(x, y)
        h = min(x, y)

        max_w = max(max_w, w)
        max_h = max(max_h, h)


    answer = max_w*max_h

    return answer