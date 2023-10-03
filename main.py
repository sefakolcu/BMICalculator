import tkinter as tk

window_width = 250
window_height = 275
widget_width = window_width / 2
widget_height = window_height / 2
localFont = ("Arial", 10, "italic")
bmiIndex = 0


def on_button_click():
    label_explanation.config(text="Calculating...")
    bmi_calculator()


window = tk.Tk()
window.minsize(window_width, window_height)

label_topic = tk.Label(text="BMI Calculator", font= localFont)
label_topic.pack(side="top")
label_heading_one = tk.Label(text="Lütfen kilonuzu girin (kg)", font= localFont)
label_heading_two = tk.Label(text="Lütfen boyunuzu girin (cm)", font= localFont)
label_explanation = tk.Label(text="", font=localFont)
label_explanation_two = tk.Label(text="", font=localFont)
weight_entry = tk.Entry(width=15)
lenght_entry = tk.Entry(width=15)
calculate_button = tk.Button(text="Calculate", command=on_button_click)


def widget_placing():
    label_heading_one.place(x=widget_width - 70, y=widget_height - 110)
    label_heading_two.place(x=widget_width - 75, y=widget_height - 50)
    weight_entry.place(x=widget_width - 42, y=widget_height - 80)
    lenght_entry.place(x=widget_width - 42, y=widget_height - 20)
    calculate_button.place(x=widget_width - 25, y=widget_height + 10)
    label_explanation.place(x=widget_width - 115, y=widget_height + 40)
    label_explanation_two.place(x=widget_width - 30, y=widget_height + 70)


widget_placing()


def explanation_to_user():

    global localText

    if bmiIndex > 0:
        label_explanation.config(text=f"Senin BMI indexin: {bmiIndex}")
        if bmiIndex < 18.5:
            label_explanation_two.config(text="Zayıfsın")
        elif 18.5 < bmiIndex < 24.5:
            label_explanation_two.config(text="Normalsin")
        elif 25.0 < bmiIndex < 29.9:
            label_explanation_two.config(text="Kilolusun")
        elif 30.0 < bmiIndex < 34.9:
            label_explanation_two.config(text="Obez Tip 1")
        elif 35.0 < bmiIndex < 100:
            label_explanation_two.config(text="Obez Tip 2")
def bmi_calculator():

    global bmiIndex

    user_weight = weight_entry.get()
    user_lenght = lenght_entry.get()

    if user_weight == "":
        label_explanation.config(text="Kilo değeri boş bırakılamaz")
    else:
        if user_lenght == "":
            label_explanation.config(text="Boy değeri boş bırakılamaz")
        else:
            if user_weight.isnumeric():
                translated_weight = int(user_weight)
                if user_lenght.isnumeric():
                    translated_lenght = int(user_lenght)
                    if translated_lenght > 0:
                        retranslated_lenght = float(translated_lenght / 100)
                        d_retranslated_lenght = retranslated_lenght * retranslated_lenght
                        bmiIndex = translated_weight / d_retranslated_lenght

                        explanation_to_user()
                else:
                    label_explanation.config(text="Boy değeri mutlaka rakam olmalıdır")
            else:
                label_explanation.config(text="Kilo değeri mutlaka rakam olmalıdır")


window.mainloop()
