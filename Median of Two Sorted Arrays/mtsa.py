def merge_sort(sorted_l1, sorted_l2):
    merged_list = []
    i, j = 0, 0
    while i < len(sorted_l1) and j < len(sorted_l2):
        if sorted_l1[i] < sorted_l2[j]:
            merged_list.append(sorted_l1[i])
            i += 1
        else:
            merged_list.append(sorted_l2[j])
            j += 1
    while i < len(sorted_l1):
        merged_list.append(sorted_l1[i])
        i += 1
    while j < len(sorted_l2):
        merged_list.append(sorted_l2[j])
        j += 1
    return merged_list

def median(sorted_list):
    size = len(sorted_list)
    if size % 2 == 0:
        median = (sorted_list[size // 2 - 1] + sorted_list[size // 2]) / 2
    else:
        median = sorted_list[size // 2]
    return median

def main():
    l1 = list(map(int, input("List 1: ").split()))
    l2 = list(map(int, input("List 2: ").split()))
    merged_list = merge_sort(l1, l2)
    m = median(merged_list)
    print(f"Merged List: {merged_list}")
    print(f"Median: {m}")

if __name__ == "__main__":
    main()
