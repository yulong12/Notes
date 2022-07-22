# -*- coding: utf-8 -*-

"""
1.取前K个元素构建小顶堆，堆顶是目前最大的数
2.依次向后遍历，如果元素小于堆顶元素，pass，如果大于堆顶元素，替换，调整堆
3.遍历结束，倒序弹出堆顶
"""


def shif(lists, low, high):
    tmp = lists[low]
    i = low
    j = i * 2 + 1
    while j <= high:
        if j + 1 <= high and lists[j+1] < lists[j]:
            j += 1
        if tmp > lists[j]:
            lists[i] = lists[j]
            i = j
            j = i * 2 + 1
        else:
            break
    print(lists)
    lists[i] = tmp


def top_k(lists, k):
    heap = lists[: k]
    # 建堆
    for i in range(k // 2 - 1, -1, -1):
        shif(heap, i, k-1)
    for i in range(k, len(lists)):
        if lists[i] > heap[0]:
            heap[0] = lists[i]
            shif(heap, 0, k-1)

    # 重新排序
    # for i in range(k-1, -1, -1):
    #     heap[0], heap[i] = heap[i], heap[0]
    #     shif(heap, 0, i-1)
    return heap


li = [0, 8, 6, 2, 4, 9, 1, 4, 6]
print(top_k(li, 3))