def filtering_values_for_election(lst):
    a, b = len(lst), len(lst) + 1

    while len(lst) < b:
        avg = sum(lst) / len(lst)

        st_dv = (sum([(value - avg)**2 for value in lst]) / len(lst))**0.5

        filtered = list(filter(lambda x: avg - 2.5 *
                               st_dv <= x <= avg + 2.5 * st_dv, lst))

        if filtered == lst:
            break
        else:
            lst = filtered

        avg = sum(lst) / len(lst)
        s = (sum([(value - avg)**2 for value in lst]) / len(lst))**0.5

    return [avg, s], [avg - 2.5 * st_dv, avg + 2.5 * st_dv]


lists = [35, 34, 37, 32, 33, 36, 38, 32, 35, 35, 36, 34, 35, 100, 85, 70]
print(filtering_values_for_election(lists))
