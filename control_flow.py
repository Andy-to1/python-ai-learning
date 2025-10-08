 	# 示例代码（学员自定义）
nums = list(map(int, input("输入数字列表: ").split()))
total = 0
for num in nums:
    if num % 2 == 0:
        total += num
print(f"偶数和: {total}")
