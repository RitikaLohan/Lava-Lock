import cv2
import hashlib
import secrets
import string

def generate_entropy_from_image(image_path):
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    resized = cv2.resize(img, (64, 64))  # Resize to standard size
    data = resized.flatten()
    hash_digest = hashlib.sha256(data.tobytes()).hexdigest()
    return hash_digest

def generate_password_from_image(image_path, length=16):
    entropy = generate_entropy_from_image(image_path)
    alphabet = string.ascii_letters + string.digits + string.punctuation
    password = ''
    for i in range(length):
        index = int(entropy[i*2:i*2+2], 16) % len(alphabet)
        password += alphabet[index]
    return password