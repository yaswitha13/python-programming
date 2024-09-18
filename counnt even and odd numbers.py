def count_even_odd(numbers):
    even_count = sum(num % 2 == 0 for num in numbers)
    odd_count = len(numbers) - even_count
    return even_count, odd_count
numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)
even_numbers, odd_numbers = count_even_odd(numbers)
print("Number of even numbers:", even_numbers)
print("Number of odd numbers:", odd_numbers)
