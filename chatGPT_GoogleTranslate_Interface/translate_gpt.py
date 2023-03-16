import openai
from googletrans import Translator
import datetime
from flask import Flask, request, render_template
# Set up the OpenAI API credentials and model
openai.api_key = "<Add your key here>"
model_engine = "davinci" # Or any other GPT model of your choice

# Set up the Googletrans Translator object
translator = Translator()

# Define a function to get the Malayalam translation of a given prompt
def generate_text(prompt):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        temperature=0.5,
        max_tokens=400,
#        n_top=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    return response.choices[0].text.strip()
# Example usage
# prompt = "what is chatGPT?"
app = Flask(__name__)
app.run(host='0.0.0.0', port=5000)
# Define the home page
@app.route('/')
def home():
    return render_template('home.html')

# Define the results page
@app.route('/results', methods=['POST'])
def results():
    # Get the prompt from the form data
    prompt = request.form['prompt']

    # Generate some text using ChatGPT
    output_text_file = generate_text(prompt)

    # Translate the output text to Malayalam
    translator = Translator()
    translated_text = translator.translate(output_text_file, dest='or').text

    # Write the translated text to a .txt file
#    filename = f"output_{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.txt"
#    with open(filename, "w") as f:
#        f.write(translated_text)

    # Render the results page with the translated text
    return render_template('results.html', output_text=translated_text)

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
