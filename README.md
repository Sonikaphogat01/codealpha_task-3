# 🧠 MNIST Digit Recognition using Pygame & TensorFlow

An interactive digit recognition app built with **Pygame**, **OpenCV**, and **TensorFlow**. Draw digits on the screen and let a trained MNIST model recognize them in real-time.

---

## ✨ Features

- ✍️ Draw digits using your mouse
- 🔍 Real-time recognition using a trained CNN model
- 🧠 Built on the classic MNIST dataset
- 🖼️ Canvas reset with keyboard key ('n')
- 💡 Simple and intuitive UI

---

## 🛠️ Tech Stack

- Python
- Pygame
- TensorFlow / Keras
- OpenCV
- NumPy

---

 🚀 Getting Started
 
🔧 Setup Virtual Environment (Optional but recommended)

```bash
python -m venv tf-env
source tf-env/bin/activate  # On Windows: tf-env\Scripts\activate
```

📦 Install Dependencies

```bash
pip install -r requirements.txt
```

If `requirements.txt` is not available, install manually:

```bash
pip install pygame tensorflow opencv-python numpy
```

 💾 Download Trained Model

Make sure `mnist_model.h5` (your trained CNN model) is in the same directory as `app.py`.

If you don't have it yet, you can train your own on the MNIST dataset or download a pretrained one.

---

▶️ Run the App

```bash
python app.py
```

* Use your mouse to draw a digit
* Release the mouse to trigger prediction
* Press **`n`** to clear the screen and start again

---

 📁 Project Structure

```
📦 mnist-digit-recognition
├── app.py                
├── mnist_model.h5        
├── README.md             
├── requirements.txt      

---

 📊 Model Info

* Input: 28x28 grayscale images
* Architecture: Simple CNN with Conv2D, MaxPooling, Flatten, Dense
* Trained On: MNIST dataset (60,000 training / 10,000 testing)

---

🤝 Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you'd like to change or add.


 📃 License

This project is open-source under the [MIT License](LICENSE).

---

 🙋‍♀️ Author

Developed by **Sonika Phogat**
2nd-year AI & ML student, Guru Jambheshwar University
📫  | ✉️ sonikaphogat08@gmail.com


