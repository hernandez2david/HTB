#AI-ASSISTED

subset_a = set((input().split()))
repeat = int(input())

flag0 = False
sub_list_b = []
for i in range(repeat):
    subset_b = set((input().split()))
    sub_list_b.append(subset_b)

result = all(subset_a.issuperset(subset) for subset in sub_list_b)

print(result)

