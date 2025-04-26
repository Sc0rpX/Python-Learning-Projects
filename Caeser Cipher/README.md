# 🔐 Caesar Cipher - Encode and Decode Messages in Python

This project is a simple implementation of the **Caesar Cipher**, one of the earliest and easiest encryption techniques. You can **encode** or **decode** messages by shifting letters in the alphabet by a certain number.

## 🧠 How It Works

- You type in your message and a shift number.
- The program shifts each letter forward (encode) or backward (decode) by the given number.
- Non-alphabet characters (e.g., spaces, punctuation) stay unchanged.

## 🛠️ Features

- Encode or decode messages
- Customizable shift amount
- Keeps punctuation and spacing unchanged
- Repeats until you choose to exit

## 🧾 Example

```
Type 'encode' to encrypt, type 'decode' to decrypt:
> encode
Type your message:
> hello world!
Type the shift number:
> 3
The encoded text is: khoor zruog!
```

## 📎 Notes

- Shift values beyond 26 wrap around the alphabet automatically.
- Only lowercase letters are considered in this version.

---

Have fun encrypting your secret messages! 🕵️‍♂️📜
