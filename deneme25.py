import random

def create_sequence():
    # 25 elemanlı, başlangıçta sıfır olan bir dizi
    arr = [0] * 25
    current_index = random.randint(0, 24)  # Başlangıç indexini rastgele seç
    step_sequence = [3, -3, 8, -8, 10, -10, 12, -12]  # Adım sırasındaki kurallar
    step_idx = 0  # Adım sırasına başlamak için
    filled_count = 0  # Diziye eklenen sayıları saymak için
    
    while filled_count < 25:
        # Eğer mevcut index boşsa (0 ise), sayıyı ekle
        if arr[current_index] == 0:
            arr[current_index] = filled_count + 1
            filled_count += 1
        
        # Bir sonraki index'i hesapla
        current_index = (current_index + step_sequence[step_idx]) % 25
        
        # Adım sırasını güncelle
        step_idx = (step_idx + 1) % len(step_sequence)

    return arr

# Fonksiyonu çağır ve sonucu yazdır
arr = create_sequence()
print(arr)
