import spacy
import pandas as pd

# Load the English language model
nlp = spacy.load("en_core_web_sm")



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

# Test the function


def function_for_splitting(text_in):
    out=[]
    for sentence in text_in.split("."):
        try:
            out.append(get_verb_object_time(sentence+".")[0])
        except:
            pass
    return out
        
#function_for_splitting("I will go the store at 5 pm. Then, I will study till late night. tomorrow, I will wake up to see it at 2 am to 3 am")


def create_table_from_output(text):
    # Call the function and get the activities
    activities = function_for_splitting(text)
    
    # Create a pandas DataFrame
    df = pd.DataFrame(activities, columns=["Verb", "Object", "Date", "Time"])
    
    return df

text = "I played football yesterday. I will have dinner at 7pm."
df = create_table_from_output(text)
html=df.to_html()
