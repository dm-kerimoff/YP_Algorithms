def sift_down(heap, idx):
    left = 2 * idx
    right = 2 * idx + 1

    # нет дочерних узлов
    if len(heap) - 1 < left:
        return idx

    # right <= heap.size проверяет, что есть оба дочерних узла
    if right <= (len(heap) - 1) and heap[left] < heap[right]:
        idx_largest = right
    else:
        idx_largest = left

    if heap[idx] < heap[idx_largest]:
        heap[idx], heap[idx_largest] = heap[idx_largest], heap[idx]
        return sift_down(heap, idx_largest)
    else:
        return idx