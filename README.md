# Color Quantization and Dithering

INF605 final project, Group 1.

We implement, in Python, the color quantization method of

- P. Heckbert, *Color Image Quantization for Frame Buffer Display*, Computer Graphics 16(3), 1982 (median cut), and
- R. W. Floyd and L. Steinberg, *An Adaptive Algorithm for Spatial Grayscale*, 1976 (error diffusion dithering).

The goal is to show a 24-bit photo with only K colors (for example 256) while keeping it as close as possible to the original.

## Pipeline

| Phase | Step | Status |
|---|---|---|
| A | Read the image, 15-bit pre-quantization and color histogram | Done |
| B | Median cut palette selection | Done |
| C | Map every pixel to its nearest palette color | In progress (a temporary stand-in is used until then) |
| D | Floyd–Steinberg dithering | In progress |
| E | Experiments, quality metrics, comparison with Pillow | In progress |

```
image -> [Task 1] pixels (N, 3) -> [Task 2] colors (M, 3) + counts (M,)
      -> [Task 5] loop { [Task 3] split axis -> [Task 4] two boxes } -> palette (K, 3)
      -> [Phase C] nearest color -> [Phase D] dithering -> quantized image
```

## Team

| Member | Phases A and B | Phases C to E |
|---|---|---|
| Gizem Bayram | Task 1: image reading and flattening | Nearest color mapping (Phase C) |
| Salih Enes Akdere | Task 2: 15-bit quantization and histogram | Floyd–Steinberg dithering (Phase D) |
| Ceren Tayran | Task 3: bounding box and split axis | Integration tests, effect of K, step-by-step visualization |
| Elif Hilal Kırer | Task 4: radix list sort and weighted median split | Experiments and Pillow comparison |
| Fatma Hepsen Çakır | Task 5: box orchestration and final palette | Quality and speed metrics, end-to-end pipeline |

## Repository

| File | Content | Author |
|---|---|---|
| `INF605_Group1_Median_Cut.ipynb` | Main notebook: all tasks in one place, plus the integration tests, the effect of K and the step-by-step view of median cut in RGB space | All members |
| `gorev1.py` | Task 1: `load_rgb_image`, `flatten_pixels` | Gizem Bayram |
| `task2_quantization.py`, `test_task2.py` | Task 2: `quantize_and_histogram`, `to_8bit` | Salih Enes Akdere |
| `INF605_Task3.ipynb` | Task 3: `bounding_box`, `axis_ranges`, `find_split_axis`, with tests and a 3D plot | Ceren Tayran |
| `task4_split.py`, `test_task4.py` | Task 4: `split_box` | Elif Hilal Kırer |
| `task5_orchestration.py`, `test_task5.py` | Task 5: `run_median_cut` | Fatma Hepsen Çakır |
| `integration_test.py` | First check that Tasks 1 and 2 work together | Salih Enes Akdere |
| `kodim23.png` | Test image (see below) | |

## How to run

```bash
pip install -r requirements.txt
jupyter notebook INF605_Group1_Median_Cut.ipynb
```

In Jupyter, choose **Kernel → Restart Kernel and Run All Cells**. The notebook runs from top to bottom in a few seconds.

The tests of the single tasks can also be run on their own from this folder:

```bash
python test_task2.py
python test_task4.py
python test_task5.py
```

## Test image

`kodim23.png` (two parrots, 768 × 512, 24-bit) comes from the Kodak Lossless True Color Image Suite, a standard test set released by Eastman Kodak for unrestricted use: [r0k.us/graphics/kodak](https://r0k.us/graphics/kodak/). It is kept as PNG because PNG is lossless; a JPEG would already have changed the colors.

## Library use

The method is written by us. Libraries provide only general tools: NumPy for arrays, Pillow for reading images, Matplotlib for plots. Library versions of color quantization, such as Pillow's `Image.quantize`, are used only to compare results.