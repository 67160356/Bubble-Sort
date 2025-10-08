class BubbleSorter:
    def __init__(self, nums):
        self.nums = nums

    def display(self):
        print(self.nums)

    def sort(self):
        n = len(self.nums)

        for i in range(n):
            swapped = False
            for j in range(0, n - i - 1):
                if self.nums[j] > self.nums[j + 1]:
                    self.nums[j], self.nums[j + 1] = self.nums[j + 1], self.nums[j]
                    swapped = True

            print(f"After round {i + 1}: {self.nums}")

            if not swapped:
                break

if __name__ == "__main__":

    nums = [64, 34, 25, 12, 22, 11, 90]
    sorter = BubbleSorter(nums)

    print("Before sorting:")
    print(f"Current data: {sorter.nums}")
    print()

    # Sort the numbers
    sorter.sort()

    print()
    print("After sorting:")
    print(f"Current data: {sorter.nums}")