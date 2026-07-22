print("=== Bài 1 ===")

def draw_rectangle(width, height=None, c='*'):
    if height is None:
        height = width
    for i in range(height):
        print(c * width)
    print()

draw_rectangle(4, 3)
draw_rectangle(5)
draw_rectangle(3, 2, '#')

print("=== Bài 2 ===")

def stats(numbers):
    min_num = min(numbers)
    max_num = max(numbers)
    avg = sum(numbers) / len(numbers)
    return min_num, max_num, avg

numbers = [5, 2, 8, 1, 9, 3]
min_val, max_val, avg_val = stats(numbers)
print(min_val)
print(max_val)
print(avg_val)

print("=== Bài 3 ===")

def is_prime(n):
    if n < 0:
        raise ValueError("n phai la so khong am")
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

for i in range(11):
    print(i, is_prime(i))

try:
    is_prime(-5)
except ValueError as e:
    print(e)

print("=== Bài 4 ===")

count = 0

def greet(name):
    global count
    count = count + 1
    print("Xin chao", name)

greet("An")
greet("Binh")
greet("Cuong")
print(count)

print("=== Bài 5 ===")

def cal_fare(km):
    if km <= 0:
        return 0
    if km <= 1:
        return 15000
    if km <= 20:
        return 15000 + (km - 1) * 13000
    return 15000 + 19 * 13000 + (km - 20) * 11000

def main():
    while True:
        km = float(input("Nhap so km: "))
        tien = cal_fare(km)
        print("So tien:", tien)
        tiep = input("Tiep tuc? (y/n): ")
        if tiep != 'y':
            break

main()

print("=== Bài 6 ===")

import random

nums = [random.randint(1, 100) for _ in range(10)]
print(nums)

binh_phuong = list(map(lambda x: x ** 2, nums))
print(binh_phuong)

don_vi = list(map(lambda x: x % 10, nums))
print(don_vi)

print("=== Bài 7 ===")

nums2 = [random.randint(-50, 50) for _ in range(15)]
print(nums2)

so_duong = list(filter(lambda x: x > 0, nums2))
print(so_duong)

chia_het = list(filter(lambda x: x % 2 == 0 and x % 3 == 0, nums2))
print(chia_het)

print("=== Bài 8 ===")

words = ["python", "java", "c", "javascript", "go"]
print(words)

dai_nhat = max(words, key=lambda w: len(w))
ngan_nhat = min(words, key=lambda w: len(w))
print(dai_nhat)
print(ngan_nhat)

so_list = [15, 42, 78, 93, 26]
print(so_list)

so_max_don_vi = max(so_list, key=lambda x: x % 10)
print(so_max_don_vi)
