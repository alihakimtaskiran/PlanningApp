from flask import Flask, render_template, request, jsonify
import spacy
import pandas as pd

app = Flask(__name__, static_folder="static")

nlp = spacy.load("en_core_web_sm")

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/get_response', methods=['POST'])
def get_response():
    user_input = request.form['input']
    
    # Process the user's input and generate an HTML table
    activities = function_for_splitting(user_input)
    df = pd.DataFrame(activities, columns=["Verb", "Object", "Date", "Time"])
    table_html = df.to_html()

    response = {'table': table_html}
    return jsonify(response)

def get_verb_object_time(sentence):
    # Process the sentence
    doc = nlp(sentence)

    # Find all dates and times
    dates = [ent.text for ent in doc.ents if ent.label_ == "DATE"]
    times = [ent.text for ent in doc.ents if ent.label_ == "TIME"]

    # Find verbs and their objects
    activities = []
    for token in doc:
        if token.pos_ == "VERB":
            verb = token.text
            dobj = None
            iobj = None
            for child in token.children:
                if child.dep_ == "dobj":  # dobj stands for 'direct object'
                    dobj = child.text
                elif child.dep_ == "iobj":  # iobj stands for 'indirect object'
                    iobj = child.text

            # If there's no direct or indirect object, set it to None
            obj = dobj or iobj or None
            
            # If there's no date, set it to None
            date = dates.pop(0) if dates else None
            
            # If there's no time, set it to None
            time = times.pop(0) if times else None
            
            # Append the activity
            activities.append((verb, obj, date, time))

    return activities

def function_for_splitting(text_in):
    out=[]
    for sentence in text_in.split("."):
        try:
            out.append(get_verb_object_time(sentence+".")[0])
        except:
            pass
    return out

if __name__ == '__main__':
    app.run(debug=True)
