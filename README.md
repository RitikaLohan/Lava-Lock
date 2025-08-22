#  LavaLock – Image Entropy Based Password Generator

###  Overview

**LavaLock** is a web-based secure password generator inspired by **Cloudflare’s lava lamp wall**.
Instead of relying on predictable pseudo-random generators, LavaLock extracts **entropy** (randomness) from uploaded images (such as lava lamp patterns, abstract designs, or noise) and converts it into strong, unguessable passwords using cryptographic hashing.

This project is a perfect combination of:

* **Computer Vision (OpenCV)** → Reading and processing images.
* **Cryptography (SHA-256 hashing)** → Generating secure entropy.
* **Web Development (Flask)** → Providing a simple and interactive web interface.



### ⚙️ How It Works

1. **Upload an Image**

   * The user uploads an image (simulated lava lamp, random noise, etc.) through a web interface.

2. **Extract Entropy**

   * The image is converted to grayscale and resized to a fixed **64×64** resolution.
   * All pixel intensity values are flattened into a single array.
   * This pixel data is hashed with **SHA-256**, producing a unique hexadecimal string (entropy source).

3. **Password Generation**

   * A pool of characters (`A–Z`, `a–z`, digits, and punctuation) is prepared.
   * Segments of the SHA-256 hash are mapped into this character set.
   * A **16-character password** (configurable length) is generated that is unique and highly secure.

4. **Display to User**

   * The password is returned and displayed on the web page.
   * The user can now copy and use it safely.



###  Project Structure

```
lavalock/
│── app.py          # Flask application (main web server)
│── utils.py        # Password generation logic (image entropy + hashing)
│── requirements.txt # Dependencies (Flask, OpenCV, etc.)
│
├── static/
│   └── uploads/    # Stores uploaded images
│
└── templates/
    └── index.html  # Upload form + password output
```

---

###  Technologies Used

* **Python** – Core programming language
* **OpenCV (cv2)** – Image preprocessing (resize, grayscale, flatten)
* **hashlib** – SHA-256 hashing for secure entropy
* **string + secrets** – Random password generation utilities
* **Flask** – Web framework for handling uploads and rendering results
* **HTML (Jinja2 Templates)** – Frontend form and password display



###  Running the Project

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/lavalock
   cd lavalock
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Run the Flask app:

   ```bash
   python app.py
   ```

4. Open in browser:

   ```
   http://127.0.0.1:5000/
   ```

---

###  Features

✅ Upload any image (lava lamp, random noise, abstract patterns)
✅ Convert unpredictable pixel data into entropy
✅ Generate strong, 16-character password using SHA-256
✅ Secure web-based interface with Flask
✅ Easily extendable for longer passwords



###  Why LavaLock?

* Traditional password generators rely on pseudo-random functions, which may be predictable.
* LavaLock ensures passwords are based on **real-world randomness** (image entropy), making them nearly impossible to guess.
* It is **educational** (demonstrates entropy, hashing, and cryptography) and **practical** (generates secure passwords).


