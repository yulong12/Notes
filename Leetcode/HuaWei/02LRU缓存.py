
# 请你设计并实现一个满足  LRU (最近最少使用) 缓存 约束的数据结构。
# 实现 LRUCache 类：

#     LRUCache(int capacity) 以 正整数 作为容量 capacity 初始化 LRU 缓存
#     int get(int key) 如果关键字 key 存在于缓存中，则返回关键字的值，否则返回 -1 。
#     void put(int key, int value) 如果关键字 key 已经存在，则变更其数据值 value ；如果不存在，则向缓存中插入该组 key-value 。如果插入操作导致关键字数量超过 capacity ，则应该 逐出 最久未使用的关键字。

# 函数 get 和 put 必须以 O(1) 的平均时间复杂度运行。


def partition(arr, low, high):  
    i = low - 1  # 最小元素索引  
    pivot = arr[high]  # 基准  
  
    for j in range(low, high):  
        if arr[j] <= pivot:  
            i += 1  
            arr[i], arr[j] = arr[j], arr[i]  # 交换元素  
  
    arr[i + 1], arr[high] = arr[high], arr[i + 1]  # 把基准放到中间  
    return i + 1  
  
def quicksort_inplace(arr, low=0, high=None):  
    if high is None:  
        high = len(arr) - 1  
      
    if low < high:  
        pi = partition(arr, low, high)  # 获取分区索引  
        quicksort_inplace(arr, low, pi - 1)  # 排序左半部分  
        quicksort_inplace(arr, pi + 1, high)  # 排序右半部分  
  
# 示例使用  
if __name__ == "__main__":  
    sample_array = [3, 6, 8, 10, 1, 2, 1]  
    print("原始数组:", sample_array)  
    quicksort_inplace(sample_array)  
    print("排序后数组:", sample_array)