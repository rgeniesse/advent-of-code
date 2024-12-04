def main():
    with open("2024/day_2/input.txt", "r") as file:
        grtotal = 0
        for line in file:
            index = 0
            # Let's make a map even though this is probably a waste
            my_map = map(int, line.split())
            li = list(my_map)
            line_state = ""
            bad_report = 0

            while index < len(li) - 1:
                if (
                    abs(li[index] - li[index + 1]) >= 1
                    and abs(li[index] - li[index + 1]) <= 3
                ):
                    if li[index] > li[index + 1] and line_state == "ascend":
                        print("State change detected from ascend to decend.")
                        bad_report = 1
                        break
                    elif li[index] < li[index + 1] and line_state == "decend":
                        print("State change detected from decend to ascend.")
                        bad_report = 1
                        break
                    elif li[index] > li[index + 1]:
                        line_state = "decend"
                    elif li[index] < li[index + 1]:
                        line_state = "ascend"
                else:
                    print("Too much space or no change.")
                    bad_report = 1
                    break

                index += 1

            if bad_report != 1:
                grtotal += 1
        print(grtotal)


if __name__ == "__main__":
    main()
