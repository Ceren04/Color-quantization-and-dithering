import argparse
from pathlib import Path

import numpy as np
from PIL import Image


def load_rgb_image(image_path: Path) -> np.ndarray:
    # Girdi bir dosya yoludur; çıktı RGB biçiminde (yükseklik, genişlik, 3) dizisidir.
    try:
        with Image.open(image_path) as image:
            # Görseli üç kanallı RGB biçimine dönüştürür.
            with image.convert("RGB") as rgb_image:
                # uint8, her RGB kanalını 0-255 aralığında saklar.
                pixels = np.array(rgb_image, dtype=np.uint8)
    except OSError as error:
        raise ValueError(f"Görsel okunamadı: {image_path} ({error})") from error

    # RGB çıktısının beklenen yükseklik-genişlik-kanal yapısını doğrular.
    if pixels.ndim != 3 or pixels.shape[2] != 3:
        raise ValueError(f"RGB görsel için beklenmeyen matris şekli: {pixels.shape}")

    return pixels


def flatten_pixels(rgb_matrix: np.ndarray) -> np.ndarray:
    # Düzleştirmeden önce matrisin RGB biçiminde olduğunu doğrular.
    if rgb_matrix.ndim != 3 or rgb_matrix.shape[2] != 3:
        raise ValueError(
            "Düzleştirme için giriş (yükseklik, genişlik, 3) şeklinde olmalıdır."
        )

    # -1, piksel sayısını otomatik hesaplatır; her satır bir RGB pikselidir.
    return rgb_matrix.reshape(-1, 3)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Görseli RGB piksel matrisi ve düzleştirilmiş dizi olarak hazırlar."
    )
    parser.add_argument(
        "image",
        nargs="?",
        type=Path,
        default=Path("test_fotografi.jpg"),
        help="Girdi görselinin yolu (varsayılan: test_fotografi.jpg)",
    )
    args = parser.parse_args()

    print("1. Adım: Fotoğraf okunuyor...")
    try:
        matris = load_rgb_image(args.image)
    except ValueError as error:
        parser.error(str(error))

    yukseklik, genislik, _ = matris.shape
    print("2. Adım: Görsel RGB formatına dönüştürüldü.")
    print("3. Adım: NumPy RGB matrisi hazırlandı.")
    print(
        f"Orijinal fotoğraf boyutu: {yukseklik} piksel yükseklik, "
        f"{genislik} piksel genişlik"
    )
    print(f"RGB matrisinin boyutu: {matris.shape}")

    print("4. Adım: Düzleştirme (flattening) yapılıyor...")
    duz_matris = flatten_pixels(matris)

    print("\n--- İŞLEM BAŞARILI ---")
    print(f"Toplam piksel sayısı: {yukseklik * genislik}")
    print(f"Algoritma için hazırlanan düz liste boyutu: {duz_matris.shape}")
    print("İlk 10 pikselin RGB değerleri:")
    print(duz_matris[:10])


if __name__ == "__main__":
    main()
