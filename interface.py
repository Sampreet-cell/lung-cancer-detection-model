import tkinter as tk
from tkinter import PhotoImage, messagebox
import pickle

# Load the pickled machine learning model
with open('lung_cancer_model.pkl', 'rb') as f:
    model = pickle.load(f)

def process_data():
    # Get user inputs for each parameter
    GENDER = int(gender_var.get())
    AGE = int(age_entry.get()) 
    SMOKING = int(smoking_var.get()) 
    YELLOW_FINGERS = int(yellow_fingers_var.get())
    ANXIETY = int(anxiety_var.get())
    PEER_PRESSURE = int(peer_pressure_var.get())
    CHRONIC_DISEASE = int(chronic_disease_var.get())
    FATIGUE = int(fatigue_var.get())
    ALLERGY = int(allergy_var.get())
    WHEEZING = int(wheezing_var.get())
    ALCOHOL_CONSUMING = int(alcohol_consuming_var.get())
    COUGHING = int(coughing_var.get())
    SHORTNESS_OF_BREATH = int(shortness_of_breath_var.get())
    SWALLOWING_DIFFICULTY = int(swallowing_difficulty_var.get())
    CHEST_PAIN = int(chest_pain_var.get())
    
    # Create a data row based on the user inputs
    data = [[GENDER, AGE, SMOKING, YELLOW_FINGERS, ANXIETY, PEER_PRESSURE, CHRONIC_DISEASE, FATIGUE,
             ALLERGY, WHEEZING, ALCOHOL_CONSUMING, COUGHING, SHORTNESS_OF_BREATH, SWALLOWING_DIFFICULTY, CHEST_PAIN]]
    
    # Make predictions using the loaded model
    prediction = model.predict(data)
    if prediction == 1:
        result = "You are diagnosed with lung cancer"
    else:
        result = "You are not diagnosed with lung cancer"
    
    # Display the prediction result
    messagebox.showinfo("Prediction", f"{result}")

window = tk.Tk()
window.title("Lung Cancer Detection")
window.geometry("500x1000")
window.config(background="light blue")

# Create labels, entry fields, and other UI elements
title_label = tk.Label(window, text="Lung Cancer Detection", background="light blue", foreground="blue", font=("Helvetica", 25))
title_label.pack(pady=5)

# Gender
gender_label = tk.Label(window, text="GENDER:", background="light blue", foreground="blue")
gender_label.pack()
gender_var = tk.StringVar(window)
gender_var.set("1")  # Set default value to 1
gender_frame = tk.Frame(window, background="light blue")
gender_frame.pack()

rb_male = tk.Radiobutton(gender_frame, text="Male", variable=gender_var, value="1")
rb_male.pack(side=tk.LEFT, padx=5)
rb_male.config(background="light blue", foreground="blue", activebackground="light blue")

rb_female = tk.Radiobutton(gender_frame, text="Female", variable=gender_var, value="0")
rb_female.pack(side=tk.LEFT, padx=5)
rb_female.config(background="light blue", foreground="blue", activebackground="light blue")

# Age
age_label = tk.Label(window, text="AGE:", background="light blue", foreground="blue")
age_label.pack()
age_entry = tk.Entry(window)
age_entry.pack()

# Smoking
smoking_label = tk.Label(window, text="SMOKING:", background="light blue", foreground="blue")
smoking_label.pack()
smoking_var = tk.StringVar(window)
smoking_frame = tk.Frame(window, background="light blue")
smoking_frame.pack()
smoking_var = tk.StringVar(window)
smoking_var.set("1")

rb_smoking_no = tk.Radiobutton(smoking_frame, text="No", variable=smoking_var, value="1")
rb_smoking_no.pack(side=tk.LEFT, padx=5)
rb_smoking_no.config(background="light blue", foreground="blue", activebackground="light blue")

rb_smoking_yes = tk.Radiobutton(smoking_frame, text="Yes", variable=smoking_var, value="2")
rb_smoking_yes.pack(side=tk.LEFT, padx=5)
rb_smoking_yes.config(background="light blue", foreground="blue", activebackground="light blue")

# Yellow fingers
yellow_fingers_label = tk.Label(window, text="YELLOW FINGERS:", background="light blue", foreground="blue")
yellow_fingers_label.pack()
yellow_fingers_var = tk.StringVar(window)
yellow_fingers_frame = tk.Frame(window, background="light blue")
yellow_fingers_frame.pack()
yellow_fingers_var = tk.StringVar(window)
yellow_fingers_var.set("1")

rb_yellow_fingers_no = tk.Radiobutton(yellow_fingers_frame, text="No", variable=yellow_fingers_var, value="1")
rb_yellow_fingers_no.pack(side=tk.LEFT, padx=5)
rb_yellow_fingers_no.config(background="light blue", foreground="blue", activebackground="light blue")

rb_yellow_fingers_yes = tk.Radiobutton(yellow_fingers_frame, text="Yes", variable=yellow_fingers_var, value="2")
rb_yellow_fingers_yes.pack(side=tk.LEFT, padx=5)
rb_yellow_fingers_yes.config(background="light blue", foreground="blue", activebackground="light blue")

# Anxiety
anxiety_label = tk.Label(window, text="ANXIETY:", background="light blue", foreground="blue")
anxiety_label.pack()
anxiety_var = tk.StringVar(window)
anxiety_frame = tk.Frame(window, background="light blue")
anxiety_frame.pack()
anxiety_var = tk.StringVar(window)
anxiety_var.set("1")

rb_anxiety_no = tk.Radiobutton(anxiety_frame, text="No", variable=anxiety_var, value="1")
rb_anxiety_no.pack(side=tk.LEFT, padx=5)
rb_anxiety_no.config(background="light blue", foreground="blue", activebackground="light blue")

rb_anxiety_yes = tk.Radiobutton(anxiety_frame, text="Yes", variable=anxiety_var, value="2")
rb_anxiety_yes.pack(side=tk.LEFT, padx=5)
rb_anxiety_yes.config(background="light blue", foreground="blue", activebackground="light blue")

# Peer pressure
peer_pressure_label = tk.Label(window, text="PEER PRESSURE:", background="light blue", foreground="blue")
peer_pressure_label.pack()
peer_pressure_var = tk.StringVar(window)
peer_pressure_frame = tk.Frame(window, background="light blue")
peer_pressure_frame.pack()
peer_pressure_var = tk.StringVar(window)
peer_pressure_var.set("1")

rb_peer_pressure_no = tk.Radiobutton(peer_pressure_frame, text="No", variable=peer_pressure_var, value="1")
rb_peer_pressure_no.pack(side=tk.LEFT, padx=5)
rb_peer_pressure_no.config(background="light blue", foreground="blue", activebackground="light blue")

rb_peer_pressure_yes = tk.Radiobutton(peer_pressure_frame, text="Yes", variable=peer_pressure_var, value="2")
rb_peer_pressure_yes.pack(side=tk.LEFT, padx=5)
rb_peer_pressure_yes.config(background="light blue", foreground="blue", activebackground="light blue")

# Chronic disease
chronic_disease_label = tk.Label(window, text="CHRONIC DISEASE:", background="light blue", foreground="blue")
chronic_disease_label.pack()
chronic_disease_var = tk.StringVar(window)
chronic_disease_frame = tk.Frame(window, background="light blue")
chronic_disease_frame.pack()
chronic_disease_var = tk.StringVar(window)
chronic_disease_var.set("1")

rb_chronic_disease_no = tk.Radiobutton(chronic_disease_frame, text="No", variable=chronic_disease_var, value="1")
rb_chronic_disease_no.pack(side=tk.LEFT, padx=5)
rb_chronic_disease_no.config(background="light blue", foreground="blue", activebackground="light blue")

rb_chronic_disease_yes = tk.Radiobutton(chronic_disease_frame, text="Yes", variable=chronic_disease_var, value="2")
rb_chronic_disease_yes.pack(side=tk.LEFT, padx=5)
rb_chronic_disease_yes.config(background="light blue", foreground="blue", activebackground="light blue")

# Fatigue
fatigue_label = tk.Label(window, text="FATIGUE:", background="light blue", foreground="blue")
fatigue_label.pack()
fatigue_var = tk.StringVar(window)
fatigue_frame = tk.Frame(window, background="light blue")
fatigue_frame.pack()
fatigue_var = tk.StringVar(window)
fatigue_var.set("1")

rb_fatigue_no = tk.Radiobutton(fatigue_frame, text="No", variable=fatigue_var, value="1")
rb_fatigue_no.pack(side=tk.LEFT, padx=5)
rb_fatigue_no.config(background="light blue", foreground="blue", activebackground="light blue")

rb_fatigue_yes = tk.Radiobutton(fatigue_frame, text="Yes", variable=fatigue_var, value="2")
rb_fatigue_yes.pack(side=tk.LEFT, padx=5)
rb_fatigue_yes.config(background="light blue", foreground="blue", activebackground="light blue")

# Allergy
allergy_label = tk.Label(window, text="ALLERGY:", background="light blue", foreground="blue")
allergy_label.pack()
allergy_var = tk.StringVar(window)
allergy_frame = tk.Frame(window, background="light blue")
allergy_frame.pack()
allergy_var = tk.StringVar(window)
allergy_var.set("1")

rb_allergy_no = tk.Radiobutton(allergy_frame, text="No", variable=allergy_var, value="1")
rb_allergy_no.pack(side=tk.LEFT, padx=5)
rb_allergy_no.config(background="light blue", foreground="blue", activebackground="light blue")

rb_allergy_yes = tk.Radiobutton(allergy_frame, text="Yes", variable=allergy_var, value="2")
rb_allergy_yes.pack(side=tk.LEFT, padx=5)
rb_allergy_yes.config(background="light blue", foreground="blue", activebackground="light blue")

# Wheezing
wheezing_label = tk.Label(window, text="WHEEZING:", background="light blue", foreground="blue")
wheezing_label.pack()
wheezing_var = tk.StringVar(window)
wheezing_frame = tk.Frame(window, background="light blue")
wheezing_frame.pack()
wheezing_var = tk.StringVar(window)
wheezing_var.set("1")

rb_wheezing_no = tk.Radiobutton(wheezing_frame, text="No", variable=wheezing_var, value="1")
rb_wheezing_no.pack(side=tk.LEFT, padx=5)
rb_wheezing_no.config(background="light blue", foreground="blue", activebackground="light blue")

rb_wheezing_yes = tk.Radiobutton(wheezing_frame, text="Yes", variable=wheezing_var, value="2")
rb_wheezing_yes.pack(side=tk.LEFT, padx=5)
rb_wheezing_yes.config(background="light blue", foreground="blue", activebackground="light blue")

# Alcohol
alcohol_label = tk.Label(window, text="ALCOHOL:", background="light blue", foreground="blue")
alcohol_label.pack()
alcohol_consuming_var = tk.StringVar(window)
alcohol_frame = tk.Frame(window, background="light blue")
alcohol_frame.pack()
alcohol_consuming_var = tk.StringVar(window)
alcohol_consuming_var.set("1")

rb_alcohol_no = tk.Radiobutton(alcohol_frame, text="No", variable=alcohol_consuming_var, value="1")
rb_alcohol_no.pack(side=tk.LEFT, padx=5)
rb_alcohol_no.config(background="light blue", foreground="blue", activebackground="light blue")

rb_alcohol_yes = tk.Radiobutton(alcohol_frame, text="Yes", variable=alcohol_consuming_var, value="2")
rb_alcohol_yes.pack(side=tk.LEFT, padx=5)
rb_alcohol_yes.config(background="light blue", foreground="blue", activebackground="light blue")

# Coughing
coughing_label = tk.Label(window, text="COUGHING:", background="light blue", foreground="blue")
coughing_label.pack()
coughing_var = tk.StringVar(window)
coughing_frame = tk.Frame(window, background="light blue")
coughing_frame.pack()
coughing_var = tk.StringVar(window)
coughing_var.set("1")

rb_coughing_no = tk.Radiobutton(coughing_frame, text="No", variable=coughing_var, value="1")
rb_coughing_no.pack(side=tk.LEFT, padx=5)
rb_coughing_no.config(background="light blue", foreground="blue", activebackground="light blue")

rb_coughing_yes = tk.Radiobutton(coughing_frame, text="Yes", variable=coughing_var, value="2")
rb_coughing_yes.pack(side=tk.LEFT, padx=5)
rb_coughing_yes.config(background="light blue", foreground="blue", activebackground="light blue")

# Shortness of breath
shortness_of_breath_label = tk.Label(window, text="SHORTNESS OF BREATH:", background="light blue", foreground="blue")
shortness_of_breath_label.pack()
shortness_of_breath_var = tk.StringVar(window)
shortness_of_breath_frame = tk.Frame(window, background="light blue")
shortness_of_breath_frame.pack()
shortness_of_breath_var = tk.StringVar(window)
shortness_of_breath_var.set("1")

rb_shortness_of_breath_no = tk.Radiobutton(shortness_of_breath_frame, text="No", variable=shortness_of_breath_var, value="1")
rb_shortness_of_breath_no.pack(side=tk.LEFT, padx=5)
rb_shortness_of_breath_no.config(background="light blue", foreground="blue", activebackground="light blue")

rb_shortness_of_breath_yes = tk.Radiobutton(shortness_of_breath_frame, text="Yes", variable=shortness_of_breath_var, value="2")
rb_shortness_of_breath_yes.pack(side=tk.LEFT, padx=5)
rb_shortness_of_breath_yes.config(background="light blue", foreground="blue", activebackground="light blue")

# Swallowing difficulty
swallowing_difficulty_label = tk.Label(window, text="SWALLOWING DIFFICULTY:", background="light blue", foreground="blue")
swallowing_difficulty_label.pack()
swallowing_difficulty_var = tk.StringVar(window)
swallowing_difficulty_frame = tk.Frame(window, background="light blue")
swallowing_difficulty_frame.pack()
swallowing_difficulty_var = tk.StringVar(window)
swallowing_difficulty_var.set("1")

rb_swallowing_difficulty_no = tk.Radiobutton(swallowing_difficulty_frame, text="No", variable=swallowing_difficulty_var, value="1")
rb_swallowing_difficulty_no.pack(side=tk.LEFT, padx=5)
rb_swallowing_difficulty_no.config(background="light blue", foreground="blue", activebackground="light blue")

rb_swallowing_difficulty_yes = tk.Radiobutton(swallowing_difficulty_frame, text="Yes", variable=swallowing_difficulty_var, value="2")
rb_swallowing_difficulty_yes.pack(side=tk.LEFT, padx=5)
rb_swallowing_difficulty_yes.config(background="light blue", foreground="blue", activebackground="light blue")

# Chest pain
chest_pain_label = tk.Label(window, text="CHEST PAIN:", background="light blue", foreground="blue")
chest_pain_label.pack()
chest_pain_var = tk.StringVar(window)
chest_pain_frame = tk.Frame(window, background="light blue")
chest_pain_frame.pack()
chest_pain_var = tk.StringVar(window)
chest_pain_var.set("1")

rb_chest_pain_no = tk.Radiobutton(chest_pain_frame, text="No", variable=chest_pain_var, value="1")
rb_chest_pain_no.pack(side=tk.LEFT, padx=5)
rb_chest_pain_no.config(background="light blue", foreground="blue", activebackground="light blue")

rb_chest_pain_yes = tk.Radiobutton(chest_pain_frame, text="Yes", variable=chest_pain_var, value="2")
rb_chest_pain_yes.pack(side=tk.LEFT, padx=5)
rb_chest_pain_yes.config(background="light blue", foreground="blue", activebackground="light blue")

# Process Button
process_button = tk.Button(window, text="Process", command=process_data)
process_button.pack(pady=10)
process_button.config(background="light blue", foreground="blue", activebackground="dark blue", activeforeground="white")

window.mainloop()