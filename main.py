import math


def main():
    # Variance
    def variance(a):
        sum = 0
        cal = 0
        for j in range(8):
            sum = sum + a[j]
        variance = sum / 8
        for k in range(8):
            cal = (a[k] - variance) ** 2
        var = cal / 8
        return var

    # StandardDeviation

    def SD(c):
        sum = 0
        cal = 0
        for j in range(8):
            sum = sum + c[j]
        variance = sum / 8
        for k in range(8):
            cal = (c[k] - variance) ** 2
        var = cal / 8
        SD = math.sqrt(var)
        return SD

    # Average
    def average(b):
        sum = 0
        for i in range(8):
            sum = sum + b[i]
        Average = sum / 8
        return Average

    # CustomTotal
    def CT(k):
        global CT
        s = 0
        for f in range(8):
            CT = s + k[f]
        return CT

    tab = [45, 50, 68, 85, 80, 100, 24, 31]

    # n = int(input("Enter number of elements : "))
    # x = list(map(int, input(" \nEnter the numbers : ").strip().split()))[:n]
    #
    # print("\nList is : ", x)

    average(tab)

    print(" The average is:", average(tab))
    print(" The variance is:", variance(tab))
    print(" The StandardDeviation is:", SD(tab))
    print(" The StandardDeviation is:", CT(tab))


if __name__ != '__main__':
    pass
else:
    main()
