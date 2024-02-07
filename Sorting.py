from time import perf_counter_ns


class Sorting:
    def __init__(self, arr: list) -> None:
        self.array = arr

    def insertion_sort(self):
        start = perf_counter_ns()
        for index in range(1, len(self.array)):
            previous_index = index - 1

            while (
                previous_index >= 0
                and self.array[previous_index] > self.array[previous_index + 1]
            ):
                temp = self.array[previous_index]
                self.array[previous_index] = self.array[previous_index + 1]
                self.array[previous_index + 1] = temp
                # To compare with previous elements also or else it would only compare it with item are previous_index but not with elements that might be before it.
                previous_index -= 1

        return (self.array, (perf_counter_ns() - start) / 1000000)


if __name__ == "__main__":
    print(Sorting([10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]).insertion_sort())
