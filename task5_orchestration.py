from collections import deque
import numpy as np


def run_median_cut(colors, counts, K, find_split_axis_fn, split_box_fn):
  """Task 5: Kutu Orkestrasyonu ve Nihai Palet Hesaplama (Median Cut).

  Parametreler:
  - colors: Task 2'den gelen 5-bit benzersiz renkler matrisi (M, 3)
  - counts: Task 2'den gelen piksel frekans ağırlıkları (M,)
  - K: Hedeflenen renk sayısı (örn. 256)
  - find_split_axis_fn: Task 3'ün eksen bulma fonksiyonu (find_split_axis)
  - split_box_fn: Task 4'ün kutu bölme fonksiyonu
  """
  # Başlangıçta tüm renkler ve frekansları tek bir kutu olarak kuyruğa eklenir
  boxes = deque([(colors, counts)])

  # Kutu sayısı K'ya ulaşana kadar döngüyü sürdür
  while len(boxes) < K:
    current_colors, current_freqs = boxes.popleft()

    # Eğer kutuda bölünecek 1 veya 0 renk kaldıysa bölemeyiz, geri ekle
    if len(current_colors) <= 1:
      boxes.append((current_colors, current_freqs))
      if all(len(c) <= 1 for c, _ in boxes):
        break
      continue

    # 1. Görev 3'ü çağır: En geniş ekseni bul (0: R, 1: G, 2: B)
    axis = find_split_axis_fn(current_colors)

    # 2. Görev 4'ü çağır: Kutuyu o eksenden medyan noktasından ikiye böl
    left_box, right_box = split_box_fn(current_colors, current_freqs, axis)

    # Oluşan iki alt kutuyu kuyruğa ekle
    boxes.append(left_box)
    boxes.append(right_box)

  # 3. Nihai Palet Hesaplama: Her kutunun frekans ağırlıklı RGB ortalamasını al
  palette = []
  for box_colors, box_freqs in boxes:
    if len(box_colors) == 0:
      palette.append([0, 0, 0])
    else:
      # Frekans ağırlıklı ortalama (numpy average)
      weighted_avg = np.average(box_colors, axis=0, weights=box_freqs)
      palette.append(np.round(weighted_avg))

  return np.array(palette, dtype=np.uint8)