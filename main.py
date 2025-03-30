def get_intersection(set1, set2):
    set1.add(60) 
    return set1.intersection(set2)

if __name__ == "__main__":
    int_set_1 = {23, 45, 12, 7}
    int_set_2 = {70, 60, 12, 6, 9}
    int_set_3 = get_intersection(int_set_2, int_set_2)
    print(list(int_set_3))
