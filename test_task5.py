from collections import deque
import numpy as np
from task5_orchestration import run_median_cut


def test_task5():
  print("Mock veri ile Task 5 testi başlatılıyor...")

  # Mock renkler ve frekanslar
  mock_colors = np.random.randint(0, 32, size=(100, 3), dtype=np.uint8)
  mock_counts = np.random.randint(1, 20, size=(100,), dtype=np.uint32)

  def mock_find_split_axis(colors):
    ranges = np.ptp(colors, axis=0)
    return int(np.argmax(ranges))

  def mock_split_box(colors, freqs, axis):
    sorted_idx = np.argsort(colors[:, axis])
    c_sorted = colors[sorted_idx]
    f_sorted = freqs[sorted_idx]
    mid = len(c_sorted) // 2
    return (c_sorted[:mid], f_sorted[:mid]), (c_sorted[mid:], f_sorted[mid:])

  K_target = 16
  final_palette = run_median_cut(
      mock_colors,
      mock_counts,
      K=K_target,
      find_split_axis_fn=mock_find_split_axis,
      split_box_fn=mock_split_box,
  )

  print("Test başarıyla tamamlandı! Hata alınmadı.")
  print(f"Hedeflenen K={K_target} için oluşan palet boyutu: {final_palette.shape}")
  assert final_palette.shape == (K_target, 3)


if __name__ == "__main__":
  test_task5()