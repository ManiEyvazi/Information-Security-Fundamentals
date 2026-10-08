#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def xor_bytes(a: bytes, b: bytes) -> bytes:
    """Побитовый XOR двух последовательностей байт одинаковой длины."""
    return bytes(x ^ y for x, y in zip(a, b))

def to_hex(data: bytes) -> str:
    return ' '.join(f'{b:02X}' for b in data)

def text_to_bytes(text: str) -> bytes:
 
    return text.encode('cp1251')

def bytes_to_text(data: bytes) -> str:
    return data.decode('cp1251', errors='replace')

def main():
    # Исходные данные из методички
    P1_text = "НаВашисходящийот1204"
    P2_text = "ВСеверныйфилиалБанка"

    # Ключ длиной 20 байт
    key_hex = "05 0C 17 7F 0E 4E 37 D2 94 10 09 2E 22 57 FF C8 0B B2 70 54"
    K = bytes(int(x, 16) for x in key_hex.split())

    # Преобразуем тексты в байты
    P1 = text_to_bytes(P1_text)
    P2 = text_to_bytes(P2_text)

    print("=== Исходные данные ===")
    print(f"P1 = {P1_text}")
    print(f"P2 = {P2_text}")
    print(f"K  = {to_hex(K)}")
    print(f"Длина K = {len(K)} байт")
    print(f"Длина P1 = {len(P1)} байт")
    print(f"Длина P2 = {len(P2)} байт")
    print()

    # --- Шифрование ---
    C1 = xor_bytes(P1, K)
    C2 = xor_bytes(P2, K)

    print("=== Шифротексты ===")
    print(f"C1 = {to_hex(C1)}")
    print(f"C2 = {to_hex(C2)}")
    print()

    # --- Проверка: дешифрование ключом ---
    P1_dec = xor_bytes(C1, K)
    P2_dec = xor_bytes(C2, K)

    print("=== Дешифрование ключом (проверка) ===")
    print(f"P1' = {bytes_to_text(P1_dec)}")
    print(f"P2' = {bytes_to_text(P2_dec)}")
    print()

    # --- Атака без ключа ---
    # Если известен P1, то P2 = (C1 xor C2) xor P1
    X = xor_bytes(C1, C2)  # = P1 xor P2
    print("=== C1 xor C2 = P1 xor P2 ===")
    print(f"X = {to_hex(X)}")
    print()

    # Восстановим P2, зная P1
    P2_recovered = xor_bytes(X, P1)
    print("=== Восстановление P2 при известном P1 (без ключа) ===")
    print(f"P2 (восстановленный) = {bytes_to_text(P2_recovered)}")
    print()

    # Восстановим P1, зная P2
    P1_recovered = xor_bytes(X, P2)
    print("=== Восстановление P1 при известном P2 (без ключа) ===")
    print(f"P1 (восстановленный) = {bytes_to_text(P1_recovered)}")
    print()

    # --- Демонстрация пошагового восстановления ---
    print("=== Пошаговое восстановление P2 по шаблону P1 ===")
    # Допустим, шаблон P1 = "НаВашисходящийот1204"
    # Восстановим P2 посимвольно, используя известные символы P1
    known_P1 = "НаВашисходящийот1204"
    known_bytes = text_to_bytes(known_P1)
    # Восстанавливаем P2 там, где известен P1
    partial = bytearray(len(P2))
    for i in range(min(len(known_bytes), len(X))):
        partial[i] = X[i] ^ known_bytes[i]
    print(f"Частично восстановленный P2: {bytes_to_text(bytes(partial))}")

if __name__ == "__main__":
    main()