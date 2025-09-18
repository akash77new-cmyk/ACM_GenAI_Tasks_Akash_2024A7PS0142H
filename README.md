```
# ACM_GenAI_Tasks_Akash_2024A7PS0142H

This repository contains solutions to both the GenAI tasks.

---

## Task 1 -- Akash's 7 Persona Chatbot

**Following files of this repository are related to this task:**

1. `frontend.py` (contains frontend code of chatbot)  
2. `backend.py` (contains backend code of chatbot)  
3. `chatbot_requirements.txt` (contains all the required libraries to be installed)  
4. `chatbot_working1.jpg` (image related to chatbot's working, final product!)  
5. `chatbot_working2.jpg` (same purpose as above)  

---

## Short Overview

A fun and interactive chatbot built using **Streamlit, Langchain and Langgraph**. It features **7 unique personas**, each with its own personality and style of replying. Integration of **Google Gemini API key** is implemented. I have used Streamlit to create a frontend UI for a better user experience.

---

## Personas included in my chatbot

- **Default**: Helpful AI with neutral responses.  
- **Shakespeare Bot 🪶**: Replies in old classic English, dramatic and poetic.  
- **Emoji Bot 😂**: Replies mostly in expressive emojis.  
- **Roast Bot 💀**: Humorous and sarcastic roasting responses.  
- **Einstein Bot 🧠**: Extremely intelligent and analytical responses.  
- **GenZ Bot 😎**: Uses GenZ slang in every response.  
- **Motivational Bot 💪**: Uplifting and encouraging responses.  
- **Crying Bot 😢**: Takes everything negatively, always on the verge of crying.  

> Each persona has its own **emoji avatar** that appears next to its messages in the chat.

The chatbot maintains **conversation history** during the session and allows users to **switch personas** using a dropdown menu in the Streamlit UI. Thus, this chatbot has **memory factor** implemented within it.

---

## User Manual -- Must Read

### Prerequisites

- Python 3.10+ installed on your system  
- A Google account to create a Gemini API key  
- A code editor to run the python script, **VsCode is recommended**  

---

### How to run my chatbot

#### Step 1 -- Download/copy my frontend and backend codes

Download/copy python codes of `frontend.py` and `backend.py` in your machine. Make sure both the files are in the same folder. Open that folder in VsCode.

#### Step 2 -- Download required python libraries

You need to download following python libraries:  

- streamlit  
- langchain  
- langchain-core  
- langgraph  
- langchain-openai  
- langchain-google-genai  
- python-dotenv  

In your terminal, just type `pip install library_name` to install a particular library, e.g., `pip install langchain`.  

In case your machine has none of the above libraries already installed, just type:

```
pip install -r chatbot_requirements.txt
```

(make sure `chatbot_requirements.txt` is also in the same folder as `frontend.py` and `backend.py`) to download all the above libraries.  

---

#### Step 3 -- Creating Google Gemini API key

**Method 1:**  
Go to [Google AI Studio API](https://aistudio.google.com/apikey)  
Click on **+Create API Key**, it will generate a long string of random characters which will be your Gemini API key.  
Copy that string in your system.

**Method 2 (if Method 1 doesn't work):**  
Type **Google AI Studio** in your browser.  
Go to the first link, click on **Get API key** (mostly on the bottom left corner)  
Click on **+Create API Key**  
Again, you will get a long string of random characters as your Gemini API key, copy that string.

---

#### Step 4 -- Integrating Gemini API key, creating `.env` file

Open the folder in which you have `frontend.py` and `backend.py`.  
Create a file named `.env` inside the same folder, and type:

```
GOOGLE_API_KEY=paste_your_API_key_here
```

Make sure there are **no spaces, no double quotes**, and the format is exactly like above.  
Example: If your created Gemini API key is `abcd1234`, your `.env` file should contain:  

```
GOOGLE_API_KEY=abcd1234
```

---

#### Step 5 -- How to run the chatbot (one liner)

Once your folder has `frontend.py`, `backend.py` and the above `.env` file, and all required libraries are installed:  

```
python -m streamlit run frontend.py
```

Press enter, and it will open the chatbot (Streamlit UI) in your default browser.  

I have attached some images as well to show the expected UI.

---

## Some Important Notes -- Must Read

- **Start delay:** After Step 5, you may face a delay (10-15 seconds) before the Streamlit chatbot UI appears.  
- **First reply delay:** Due to API integration; subsequent replies will be faster.  
- **Persona not selected:** If a persona doesn't get applied, just re-select it from the dropdown.  
- **Internet Required:** Ensure a proper internet connection.  
- **Avatars:** Each persona has an emoji avatar displayed next to its messages.  
- **Persona Switching:** You can switch personas anytime using the dropdown.  
- **Do not share your `.env` file publicly** — it contains your private API key.  
- **Memory:** The chatbot maintains message history/memory only during the current session.

Enjoy chatting with **Akash's 7 Persona Chatbot** and explore all its personalities!
```

Task2 -- Image Classifier on CIFAR-10 dataset -- README
# CIFAR-10 Image Classification Project (PyTorch)

## Overview

I have build an image classifier for the CIFAR-10 dataset using PyTorch. It demonstrates **training from scratch using a CNN (TinyVGG)** and **fine-tuning a pre-trained model (ResNet18)**. The notebook includes experiments both with and without **data augmentation** and provides a **comparative analysis** of all models.

Classes (10): airplane, automobile, bird, cat, deer, dog, frog, horse, ship, truck

## Prerequisites
1) Python 3.10 or above must be installed  
2) A code editor which can run .ipynb files (VsCode or Jupyter Notebook is preferred)

## Requirements

Required libraries include:

* torch
* torchvision
* matplotlib
* scikit-learn
* numpy
* pandas
  Just type pip install -r task2_requirements.txt on your terminal in VsCode.

## Experiments Performed

1. **TinyVGG (from scratch)**

   * Without augmentation
   * With augmentation

2. **ResNet18 (fine-tuned)**

   * Without augmentation
   * With augmentation

For each experiment, the notebook provides:

* Epoch-wise training/validation loss & accuracy
* Loss & accuracy plots
* Confusion matrix
* Final summary table comparing all experiments

## Instructions : How to run and see results

1. Open `ACM_task2.ipynb` in VsCode or Jupyter Notebook.
2. Run cells sequentially from top to bottom.
3. After all experiments finish, outputs will be saved in `outputs_fastmode/`.
4. Though I have provided all the outputs I got in this repo only.

### Outputs I got

* Confusion matrices: `tinyvgg_noaug_cm.png`, `tinyvgg_aug_cm.png`, `resnet_noaug_cm.png`, `resnet_aug_cm.png`
* Loss & accuracy plots: `tinyvgg_noaug_history.png`, `tinyvgg_aug_history.png`, `resnet_noaug_history.png`, `resnet_aug_history.png`
* Summary table: `summary_results.csv` (its screenshot from the notebook)


## Few Important Notes

* I have used 4 epochs, BATCH\_SIZE=64 (CPU-friendly, \~1.5 hours total runtime)
* The pre-trained ResNet18 model may show warnings about deprecated `pretrained=True`; these can be safely ignored.
* You can increase epochs for more accurate results, but runtime will increase (around 4 hours for 12 epochs)

## Author

Akash
