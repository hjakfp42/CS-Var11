from math import ceil, log2

bitsPerChar = ceil(log2(300 + 10))
bytesPerID = ceil(bitsPerChar * 404 / 8)
totalKB = bytesPerID * 3072 // 1024

print(totalKB)
# Ответ: 1365
