As a language model, ChatGPT is trained on a large corpus of text in English language. Therefore, its performance may be limited when it comes to understanding and generating text in other languages. Some of the limitations of ChatGPT with other languages include:

Limited Vocabulary: ChatGPT may have a limited vocabulary when it comes to other languages, which may affect its ability to understand and generate text accurately.

Grammatical Differences: Different languages have different grammatical structures, and ChatGPT may not be able to capture these differences accurately.

Cultural Context: ChatGPT may not have enough knowledge about the cultural context of other languages, which may lead to incorrect interpretations or translations.

Idiomatic Expressions: Different languages have unique idiomatic expressions that may not be easily translatable, and ChatGPT may struggle to accurately translate such expressions.

This module can be used as a temporary fix for translating the output from the openAI chatGPT output to translate to any languages.

Requirements: a) Googletrans package b) opnAI package in python c) FLASK.

STEPS to follow:

step1: 

if your system do not have the following packages,

     to install Googletrans use pip3 install googletrans from your Linux/macOS terminal.

     to install openAI: pip3 install openAI from the terminal.

     to install FLASK use pip3 install flask from the terminal.
     
  step2: 
  
  Go to the openAI website and login using your account and go to the page where you can generate API key. (Simple way is to google where you can find the API key in openAI webpage)
  Generate a key and copy it and then open translate_gpt.py and add that in the space provided to add the key. you will see "Add your API key here" in the code. To open translate_gpt.p you can use your favourite text editor like vim.
  Close and save the translate_gpt.py file.
  
  step3:
  
  Setting up the environmental variables:
  
  type the following one by one in the terminal:
  
  ```
  export FLASK_APP=translate_gpt
  export FLASK_ENV=development
  flask run 
  
  ```
  
  after that you can open 
  
  http://localhost:5000 
  
  in your browser. You can use any of your favourite browser like google chrome. 
  
  You will see a promt in the home page and search button where you can type your question to chatGPT. 
  
  you will see the results in the next page it opens in your favourite language.
  
  step4: 
  to change language you will need to edit the language options in the transplate_gpt.py script. 
  
  edit the line number 44 :
  
  Line number 44 is 
  ```
  translated_text = translator.translate(output_text_file, dest='or').text
  ```
  to change langauge,  change dest=`or` to any other language listed in googletrans. For example `ml` stands for Malayalam. `or` stands for Oria and `fr` for french etc.
  
  
