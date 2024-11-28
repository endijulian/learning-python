import numpy
from scipy import stats


### Mean ### Mengambil nilai rata-rata
# speed =  [99,86,87,88,111,86,103,87,94,78,77,85,86]

# x = numpy.mean(speed)
# print(x)


### Median ### Mengambil nilai tengah
# speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]
# x = numpy.median(speed)

# speed = [99,86,87,88,86,103,87,94,78,77,85,86]
# x = numpy.median(speed)
# print(x)


### Mode ### Mengambil nilai yang paling banyak
speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]
x = stats.mode(speed)
print(x)
