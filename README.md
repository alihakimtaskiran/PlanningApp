# PlanningApp

This project is a Flask-based web application that uses the Spacy NLP library to process user input text and extract information about verbs, objects, dates, and times. This information is then rendered as an HTML table and returned to the client.

<img src="https://github.com/alihakimtaskiran/PlanningApp/blob/main/Ekran%20g%C3%B6r%C3%BCnt%C3%BCs%C3%BC%202023-05-17%20160949.png?raw=true">

## Installation

To run this project, you need Python 3.6 or later, Flask, Spacy, and pandas. You can install these with pip:

```bash
pip install flask spacy pandas
```

Then, download the Spacy model:

```bash
python -m spacy download en_core_web_sm
```

## Usage

You can start the application by running the script:

```bash
python app.py
```

The web application will be accessible at `http://localhost:5000`.

There are two routes:

- `/` - This route serves the main page of the web application, which should contain a form for user input.

- `/get_response` - This route is where the form should post to. It takes a `POST` request with a form field named `input` containing the text to process. It responds with a JSON object containing an HTML table that represents the processed text.

## Project Structure

Here is a brief explanation of the main components of the application:

- `app = Flask(__name__, static_folder="static")` - This line initializes the Flask application.

- `nlp = spacy.load("en_core_web_sm")` - This line loads the Spacy model for English language.

- `index()` - This function is mapped to the root (`/`) URL and serves the main page of the application.

- `get_response()` - This function is mapped to the `/get_response` URL and handles the processing of user input. It uses the `function_for_splitting` function to process the input and constructs an HTML table from the result.

- `get_verb_object_time(sentence)` - This function takes a sentence and uses Spacy to extract information about verbs, objects, dates, and times.

- `function_for_splitting(text_in)` - This function splits the input text into sentences and applies `get_verb_object_time` to each sentence.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

[MIT](https://choosealicense.com/licenses/mit/)
