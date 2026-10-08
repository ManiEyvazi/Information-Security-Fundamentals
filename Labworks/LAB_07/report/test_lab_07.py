#!/usr/bin/env python3

def xor_bytes(data: bytes, key: bytes) -> bytes:
    """XOR two byte sequences of equal length."""
    if len(data) != len(key):
        raise ValueError("Data and key must be the same length")
    return bytes(a ^ b for a, b in zip(data, key))

def hex_to_bytes(hex_str: str) -> bytes:
    return bytes.fromhex(hex_str.replace(" ", ""))

def bytes_to_hex(b: bytes) -> str:
    return " ".join(f"{x:02X}" for x in b)

def str_to_bytes(s: str, encoding='cp1251') -> bytes:
    """Convert string to bytes. CP1251 for Cyrillic text."""
    return s.encode(encoding)

def bytes_to_str(b: bytes, encoding='cp1251') -> str:
    return b.decode(encoding, errors='replace')

def main():
    print("=" * 50)
    print("ONE-TIME PAD (GAMMA) ENCRYPTION LAB")
    print("=" * 50)
    print("1. Encrypt (key + plaintext -> ciphertext)")
    print("2. Decrypt (key + ciphertext -> plaintext)")
    print("3. Recover key (plaintext + ciphertext -> key)")
    print("4. Find key for target message")
    print("5. Run example from lab")
    print("=" * 50)
   
    choice = input("Choose option (1-5): ").strip()
   
    if choice == "1":
        key_hex = input("Enter key (hex): ")
        plain_hex = input("Enter plaintext (hex): ")
        key = hex_to_bytes(key_hex)
        plain = hex_to_bytes(plain_hex)
        cipher = xor_bytes(plain, key)
        print("Ciphertext (hex):", bytes_to_hex(cipher))
   
    elif choice == "2":
        key_hex = input("Enter key (hex): ")
        cipher_hex = input("Enter ciphertext (hex): ")
        key = hex_to_bytes(key_hex)
        cipher = hex_to_bytes(cipher_hex)
        plain = xor_bytes(cipher, key)
        print("Plaintext (hex):", bytes_to_hex(plain))
        print("Plaintext (text):", bytes_to_str(plain))
   
    elif choice == "3":
        plain_hex = input("Enter plaintext (hex): ")
        cipher_hex = input("Enter ciphertext (hex): ")
        plain = hex_to_bytes(plain_hex)
        cipher = hex_to_bytes(cipher_hex)
        key = xor_bytes(cipher, plain)
        print("Recovered key (hex):", bytes_to_hex(key))
   
    elif choice == "4":
        cipher_hex = input("Enter ciphertext (hex): ")
        target = input("Enter target plaintext: ")
        cipher = hex_to_bytes(cipher_hex)
        target_bytes = str_to_bytes(target)
        if len(target_bytes) != len(cipher):
            print(f"Length mismatch: cipher={len(cipher)} bytes, target={len(target_bytes)} bytes")
            print("Adjust your target text to match ciphertext length.")
            return
        key = xor_bytes(cipher, target_bytes)
        print("Key to get target message:", bytes_to_hex(key))
   
    elif choice == "5":
        
        key_hex = "05 0C 17 7F 0E 4E 37 D2 94 10 09 2E 22 57 FF C8 0B B2 70 54"
        plain_hex = "D8 F2 E8 F0 EB E8 F6 20 2D 20 C2 FB 20 C3 E5 F0 EE E9 21 21"
       
        key = hex_to_bytes(key_hex)
        plain = hex_to_bytes(plain_hex)
       
        print("\n--- Example from Lab ---")
        print("Key:", key_hex)
        print("Plaintext (hex):", plain_hex)
        print("Plaintext (text):", bytes_to_str(plain))
       
        cipher = xor_bytes(plain, key)
        print("Ciphertext (hex):", bytes_to_hex(cipher))
       
        
        recovered_key = xor_bytes(cipher, plain)
        print("Recovered key (hex):", bytes_to_hex(recovered_key))
        print("Key match:", bytes_to_hex(recovered_key) == key_hex)
       
        
        wrong_key_hex = "05 0C 17 7F 0E 4E 37 D2 94 10 09 2E 22 55 F4 D3 07 BB BC 54"
        wrong_key = hex_to_bytes(wrong_key_hex)
        wrong_plain = xor_bytes(cipher, wrong_key)
        print("\n--- Wrong Key Decryption ---")
        print("Wrong key:", wrong_key_hex)
        print("Result (hex):", bytes_to_hex(wrong_plain))
        print("Result (text):", bytes_to_str(wrong_plain))
   
    else:
        print("Invalid choice")

if __name__ == "__main__":
    main()