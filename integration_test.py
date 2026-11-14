from pathlib import Path
from gorev1 import load_rgb_image, flatten_pixels
from task2_quantization import quantize_and_histogram

matris = load_rgb_image(Path("test.jpg"))     # klasöre bir fotoğraf koy
pixels = flatten_pixels(matris)
colors, counts = quantize_and_histogram(pixels)

print("Piksel sayısı:", len(pixels))
print("15-bit sonrası benzersiz renk:", len(colors))
print("Toplam kontrolü:", counts.sum() == len(pixels))