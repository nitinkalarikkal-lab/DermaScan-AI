# Dermascan AI - Ultimate Viva Prep Guide (AI Focus)

## 🤖 Deep Learning (Skin Detection)

**Q: Explain the exact "AI Model" used.**
A: We used a **CNN (Convolutional Neural Network)** based on the **MobileNetV2** architecture. It is a "State-of-the-Art" model designed by Google for mobile devices. It uses "Depthwise Separable Convolutions" which makes it much faster than older models like VGG16.

**Q: What is "Transfer Learning" and why did you use it?**
A: Transfer Learning is like giving a student a head-start. Instead of training the model from scratch (which takes weeks and millions of images), we took a model already trained on 1.4 million images (**ImageNet**). It already knows how to see shapes, edges, and colors. We only "fine-tuned" the last layers to recognize specific skin diseases.

**Q: How does the model "see" an image?**
A: It converts the image into a matrix of numbers (Pixels). We resize it to **224x224** pixels. Then we **Normalize** the values (divide by 255) so the numbers are between 0 and 1. This helps the AI learn faster and more stably.

**Q: What are the layers you added on top of MobileNet?**
A: 
1.  **Global Average Pooling:** To simplify the complex features.
2.  **Dropout:** To prevent "Overfitting" (when the AI just memorizes the data instead of learning).
3.  **Dense Layer:** To combine features.
4.  **Softmax Layer:** The final output that gives the probability (e.g., 90% Cellulitis, 5% Impetigo).

**Q: What is the Optimizer and Loss Function?**
A: 
- **Optimizer:** **Adam** (it adjusts the "learning rate" automatically).
- **Loss Function:** **Categorical Crossentropy** (standard for multi-class problems).

---

## 💬 Natural Language Processing (The Chatbot)

**Q: How does the "Health Chatbot" work?**
A: The chatbot is powered by **Gemini AI** (using the `google-generativeai` SDK). It uses a Large Language Model (LLM) to understand natural language queries from the patient.

**Q: Is the chatbot diagnosing the user?**
A: No. The chatbot is a "Decision Support Tool." We give it a **System Prompt** telling it to act as a medical assistant but always remind the user that it is an AI and they should consult the doctor (who is also available in our app).

---

## 🛠️ Data & Training

**Q: How did you improve the limited data you had?**
A: We used **Data Augmentation**. We randomly flipped, rotated, and zoomed into the training images. This prevents the model from being confused if a patient takes a photo from a different angle or lighting.

**Q: How do you know the model is good?**
A: We check **Validation Accuracy** and **Loss**. If the accuracy is high on "new" images (that the model hasn't seen during training), we know it can generalize well to real patients.

---

## � Dataset vs. Database & Libraries

**Q: Did you use a "Dataset" or a "Database" for the AI?**
A: Both! 
- The **Dataset** (like "Dermnet") is the collection of thousands of images we used to **train** the AI. 
- The **Database** (MySQL) is used by the Django app to **store** patient info, appointments, and doctor details.

**Q: Did you use "Open Source" tools like TensorFlow?**
A: Yes! We used **TensorFlow** (and Keras), which are the most famous open-source libraries for Deep Learning (created by Google). We also used **OpenCV** (Open Source Computer Vision) or standard Python `PIL` for image handling.

**Q: Did you use "Labeled" or "Unlabeled" data?**
A: We used **Labeled Data**. This is called **Supervised Learning**.

**Q: What is the difference between Labeled and Unlabeled data?**
A:
- **Labeled Data:** Every image has a folder name or "tag" telling the AI what it is (e.g., "This is an image of Cellulitis"). The AI learns by checking its answer against this label.
- **Unlabeled Data:** Just raw images with no names. The AI would have to guess the patterns itself (Unsupervised Learning). Our project needs 100% Labeled data to be accurate.

---

## �🚀 Architectural Integration

**Q: How is the `.h5` model used in Django?**
A: We use the `TensorFlow` library inside our `views.py`. When a user uploads a photo, the server:
1.  Saves the image to the `media/` folder.
2.  Loads the `.h5` model once.
3.  Preprocesses the image using `numpy`.
4.  Runs `model.predict()` and gets the result.
5.  Sends the result to the HTML template.

**Q: Is your AI "Real-Time"?**
A: Yes, because the inference (prediction) happens in less than 1 second due to the efficiency of MobileNetV2.
