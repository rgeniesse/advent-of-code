def main():
    with open("2024/day_1/input.txt", "r") as file:
        total_distance = 0
        list_1 = []
        list_2 = []
        for line in file:
            numbers = line.split()
            list_1.append(numbers[0])
            list_2.append(numbers[1])
        list_1.sort()
        list_2.sort()

        i = 0
        while i < len(list_1):
            difference = abs(int(list_1[i]) - int(list_2[i]))
            i += 1
            total_distance = difference + total_distance

        print(f"The total distance is: {total_distance}")

        sim_score = 0
        for element_1 in list_1:
            similarity_mul = 0
            for element_2 in list_2:
                if element_1 == element_2:
                    similarity_mul += 1
            current_sim_score = int(element_1) * int(similarity_mul)
            sim_score += current_sim_score
        print(f"The similarity score is: {sim_score}")


if __name__ == "__main__":
    main()
