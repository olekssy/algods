""" Implementations of array algorithms. """


def search(arr: list[int], n: int) -> int:
    """ Finds index of an element in the array with linear search in O(N).
        Returns index if element exists, else -1. """


def bin_search(arr: list[int], n: int) -> int:
    """ Finds index of an element in the array with binary search in O(log N).
        Returns index if element exists, else -1. """


def insert(arr: list[int], n: int, i: int) -> bool:
    """ Inserts element at the index into the array if index is valid. """


def remove(arr: list[int], i: int) -> bool:
    """ Removes element at the index in the array if index is valid. """


def reverse(arr: list[int]) -> None:
    """ Reverses elements in the array inplace in O(N). """


def rotate(arr: list[int], k: int) -> None:
    """ Rotate array by k number of elements in O(N). """


def two_sum(arr: list[int], target: int) -> list[int]:
    """ Finds two numbers in the array, s.t. they sum up to target.
        O(N), O(N). """


def three_sum(arr: list[int], target: int) -> list[int]:
    """ Finds three numbers in the array, s.t. they sum up to target.
        O(N^2), O(N). """


def four_sum(arr: list[int], target: int) -> list[int]:
    """ Finds four numbers in the array, s.t. they sum up to target.
        O(N^3), O(N). """


def merge_sorted(arr1: list[int], arr2: list[int]) -> list[int]:
    """ Merge two sorted arrays in the sorted array in O(N). """


def remove_duplicates(arr: list[int]) -> None:
    """ Removes duplicated elements inplace. """


def is_palindrome(arr: list[int]) -> bool:
    """ Checks if an array is a palindrome. """
