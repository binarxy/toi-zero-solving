nums = []

for i in range(1,4):
    nums.append(int(input().strip()))
    print(f'Input number {i} stored.')

choice = int(input().strip())

if choice==1:
    print(f"Original order: {nums[0]} {nums[1]} {nums[2]}")
elif choice==2:
    nums.sort(reverse=True)
    print(f"Decending order: {nums[0]} {nums[1]} {nums[2]}")
elif choice==3:
    nums.sort()
    print(f"Ascending order: {nums[0]} {nums[1]} {nums[2]}")
elif choice==0:
    pass
