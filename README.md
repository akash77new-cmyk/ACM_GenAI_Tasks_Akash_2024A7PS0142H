# ACM_GenAI_Tasks_Akash_2024A7PS0142H
This repository contains solutions to both the GenAI tasks  

Task1 -- Akash's 7 Persona Chatbot -- README  
Following files of this repository are related to this task:  
1)frontend.py (contains frontend code of chatbot)  
2)backend.py (contains backend code of chatbot)  
3)chatbot_requirements.txt (contains all the required libraries to be installed)  
4)chatbot_working1.png (image related to chatbot's working, final product!)  
5)chatbot_working2.png (same purpose as above)  

** Short Overview **  

A fun and interactive chatbot built using Streamlit, Langchain and Langgraph. It features 7 unique personas, each with its own personality and style of replying.
Integration of Google Gemini API key is implemented. I have used Streamlit to create a frontend UI for a better user experience.  

** Personas included in my chatbot **  

0. Default: Helpful AI with neutral responses.
1. Shakespeare Bot 🪶: Replies in old classic English, dramatic and poetic.
2. Emoji Bot 😂: Replies mostly in expressive emojis.
3. Roast Bot 💀: Humorous and sarcastic roasting responses.
4. Einstein Bot 🧠: Extremely intelligent and analytical responses.
5. GenZ Bot 😎: Uses GenZ slang in every response.
6. Motivational Bot 💪: Uplifting and encouraging responses.
7. Crying Bot 😢: Takes everything negatively, always on the verge of crying.

Each persona has its own **emoji avatar** that appears next to its messages in the chat.  

The chatbot maintains conversation history during the session and allows users to switch personas using a dropdown menu in the Streamlit UI.
Thus, this chatbot has memory factor implemented within it.  
  
  
**User Manual -- Must Read**  

Prerequisites  

* Python 3.10+ installed on your system  
* A Google account to create a Gemini API key  
* A code editor to run the python script, VsCode is recommended  

*How to run my chatbot*  

Step1 -- Download/copy my frontend and backend codes.  
Download/copy python codes of frontend.py and backend.py in your machine. Make sure both the files are in same folder.
Open that folder in VsCode.  
  
  
  
Step2 -- Download required python libraries  
You need to download following python libraries:  
streamlit  
langchain  
langchain-core  
langgraph  
langchain-openai  
langchain-google-genai  
python-dotenv  

In your terminal, just type pip install library_name to install particular library, eg pip install langchain
In case your machine has none of the above libraries already installed, just type pip install -r chatbot_requirements.txt
(make sure chatbot_requirements.txt is also in the same folder that of frontend.py and backend.py)
to download all the above libraries.
If by chance you are still getting wavy green lines under any library name, just install that library in the same way mentioned above.
  
  
  
Step3 -- Creating google gemini API key  
In order to interact with my chatbot, you need to have a google gemini API key, here is how to create one:  

Method1:  
Go to https://aistudio.google.com/apikey  
Click on +Create API Key, it will generate a long string of random characters which will be your gemini API key.  
Copy that string in your system  

Method2: (If method1 doesn't work)  
If you are having any difficulties, just type Google AI Studio in your browser.  
Go to first link, click on Get API key (mostly on the bottom left corner)  
Click on +Create API Key  
Again, you will get a long string of random characters as your google gemini API key, copy that string in your system.  
  
  
  
Step4 -- Integrating gemini API key, creating .env file  
This is a very crucial step, as the chatbot won't function without API Integration  
In VsCode, open the folder in which you have both the python files, frontend.py and backend.py.  
Create a file named .env inside the same folder, and type,  

GOOGLE_API_KEY=paste_your_API_key_here  

Make sure there are no spaces, no double quotes, and the format is exactly like above specified.  
Eg. If your created gemini API key is abcd1234, your .env file should contain  
GOOGLE_API_KEY=abcd1234  
  
  
  
Step 5 -- How to run the chatbot (one liner)  
Once your folder has frontend.py, backend.py and above .env file as well, and all the required libraries are installed.  
Just open up your terminal in vs code and write:  

python -m streamlit run frontend.py  

Press enter key, and it will redirect you to chatbot (streamlit UI) in your Default browser.  
I have attached some images as well, make sure you get the exact same streamlit UI  
  
  
  
** Some Important Notes **  

Avatars: Each persona has an emoji avatar displayed next to its messages.  
Persona Switching: You can change the persona at any time using the dropdown.  
Do not share your .env file publicly — it contains your private API key.  
The chatbot maintains message history/memory only during the current session.  

Enjoy chatting with Akash's 7 Persona Chatbot and explore all its personalities!
