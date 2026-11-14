import numpy as np
from task2_quantization import quantize_and_histogram, to_8bit

# Test 1: elle hazırlanmış küçük örnek
px = np.array([[255, 255, 255],
               [0, 0, 0],
               [7, 7, 7],      # 7>>3 = 0, yani (0,0,0) ile aynı kutu
               [8, 0, 0],      # 8>>3 = 1
               [255, 255, 255]], dtype=np.uint8)
colors, counts = quantize_and_histogram(px)
print(colors)   # [[0 0 0] [1 0 0] [31 31 31]]
print(counts)   # [2 1 2]
assert counts.sum() == len(px)

# Test 2: brief'teki mock veri
mock = np.random.randint(0, 256, (50, 3))
colors, counts = quantize_and_histogram(mock)
assert counts.sum() == 50
assert colors.min() >= 0 and colors.max() <= 31

# Test 3: yanlış şekil hata vermeli
try:
    quantize_and_histogram(np.zeros((10, 4)))
    print("HATA: exception bekleniyordu")
except ValueError:
    print("Şekil kontrolü çalışıyor")

print("Tüm testler geçti")