# Успешная посылка 115879720
import sys
from typing import List


def min_count_transport(nums: List[int], limit: int) -> int:
    """Функция для подсчета минимального количества платофрм для перевозки."""
    nums.sort()
    left = 0
    right = len(nums) - 1
    min_count = 0
    while left <= right:
        if nums[left] + nums[right] <= limit:
            left += 1
        right -= 1
        min_count += 1
    return min_count


if __name__ == '__main__':
    input_nums = list(map(int, sys.stdin.readline().rstrip().split()))
    input_limit = int(sys.stdin.readline().rstrip())
    result = min_count_transport(input_nums, input_limit)
    print(result)
