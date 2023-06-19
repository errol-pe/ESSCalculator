import tkinter as tk


def get_policy_acknowledgment():
    return int(policy_acknowledgment.get())

def get_dark_web_training_completed():
    return int(dark_web_training_completed.get())

def get_profile_complete ():
    return int(profile_complete.get())

def calculate_score():
    total = 800

    # External Data Breach //
    external_data_breach_multiplier = 50
    number_of_breaches = int(breaches_entry.get())
    dark_web_training_completed = get_dark_web_training_completed()
    breach_remediation_completed = int(breach_remediation_entry.get())

    points = 0
    if number_of_breaches == 0:
        points = 0
    elif number_of_breaches == 1:
        if dark_web_training_completed == 1:
            points += 5
        if breach_remediation_completed == 1:
            points += 5
    elif number_of_breaches == 2:
        if dark_web_training_completed == 1:
            points += 10
        if breach_remediation_completed >= 1:
            points += 5
        if breach_remediation_completed == 2:
            points += 5
    elif number_of_breaches == 3:
        if dark_web_training_completed == 1:
            points += 15
        if breach_remediation_completed >= 1:
            points += 5
        if breach_remediation_completed >= 2:
            points += 5
        if breach_remediation_completed == 3:
            points += 5
    elif number_of_breaches == 4:
        if dark_web_training_completed == 1:
            points += 20
        if breach_remediation_completed >= 1:
            points += 5
        if breach_remediation_completed >= 2:
            points += 5
        if breach_remediation_completed >= 3:
            points += 5
        if breach_remediation_completed == 4:
            points += 5
    elif number_of_breaches == 5:
        if dark_web_training_completed == 1:
            points += 25
        if breach_remediation_completed >= 1:
            points += 5
        if breach_remediation_completed >= 2:
            points += 5
        if breach_remediation_completed >= 3:
            points += 5
        if breach_remediation_completed >= 4:
            points += 5
        if breach_remediation_completed == 5:
            points += 5
    else:
        if dark_web_training_completed == 1:
            points += 25
        if breach_remediation_completed >= number_of_breaches * 0.2:
            points += 5
        if breach_remediation_completed >= number_of_breaches * 0.4:
            points += 5
        if breach_remediation_completed >= number_of_breaches * 0.6:
            points += 5
        if breach_remediation_completed >= number_of_breaches * 0.8:
            points += 5
        if breach_remediation_completed == number_of_breaches:
            points += 5

    external_data_breach_scores = max(0, external_data_breach_multiplier - (number_of_breaches * (2 * 5)))
    # adding point for dark web remediation
    external_data_breach_score = external_data_breach_scores + points

    # Training Quiz //
    training_quiz_multiplier = 150
    training_score = int(training_score_entry.get())
    training_quiz_score = training_quiz_multiplier * (training_score / 100)

    # Phishing //
    phishing_multiplier = 300
    number_of_emails = int(phishing_emails_entry.get())
    phishing_fails = int(phishing_fails_entry.get())
    captured_data = int(captured_data_entry.get())
    bonus = int(bonus_entry.get())
    if number_of_emails == 0:
        phishing_score = phishing_multiplier
    else:
        phishing_score = phishing_multiplier * (
            1 - ((phishing_fails + (captured_data * 1.5) - (0.25 * bonus)) / number_of_emails)
        )

    # Policy Acknowledgment //
    policy_acknowledgment_multiplier = 40
    policy_acknowledgment = get_policy_acknowledgment()
    policy_acknowledgment_score = policy_acknowledgment * policy_acknowledgment_multiplier

    # Profile Complete //
    profile_complete_multiplier = 10
    profile_complete = get_profile_complete ()
    profile_complete_score = profile_complete * profile_complete_multiplier

    # Micro Training //
    micro_training_multiplier = 50
    number_of_micro_trainings_sent = int(micro_trainings_sent_entry.get())
    number_of_mt_watched = int(mt_watched_entry.get())
    if number_of_micro_trainings_sent == 0:
        micro_training_score = 0
    else:
        micro_training_score = micro_training_multiplier * (number_of_mt_watched / number_of_micro_trainings_sent)

    # Micro Quiz//
    micro_quiz_multiplier = 200
    average_micro_quiz_score = int(average_micro_quiz_score_entry.get())
    micro_quiz_score = micro_quiz_multiplier * (average_micro_quiz_score / 100)

    # Calculate the total score //
    total_score = (
        external_data_breach_score
        + training_quiz_score
        + phishing_score
        + policy_acknowledgment_score
        + profile_complete_score
        + micro_training_score
        + micro_quiz_score
    )

    total_score_label.config(text="Total ESS: {}".format(round(total_score)))

# Create a Tkinter window
window = tk.Tk()
window.title("ESS Calculator")

# Create input labels and entry fields
external_breaches_label = tk.Label(window, text="1. External Breaches", padx=25, pady=25, font=('', 12))
breaches_label = tk.Label(window, text="Number of Breaches:")
breaches_entry = tk.Entry(window)
dark_web_training_label = tk.Label(window, text="Dark Web Training Completed:")

# dark web training radio yes or no

dw_training_frame = tk.Frame(window)
dw_training_frame.grid(row=2, column=2, sticky="w")


dark_web_training_completed = tk.IntVar(value=0)
dw_training_yes_radio = tk.Radiobutton(dw_training_frame, text="Yes", variable=dark_web_training_completed, value=1)
dw_training_yes_radio.grid(row=0, column=0)
dw_training_no_radio = tk.Radiobutton(dw_training_frame, text="No", variable=dark_web_training_completed, value=0)
dw_training_no_radio.grid(row=0, column=1)


breach_remediation_label = tk.Label(window, text="Remediated Breaches:")
breach_remediation_entry = tk.Entry(window)

training_quiz_label = tk.Label(window, text="2. Training Quiz", padx=25, pady=25, font=('', 12))
training_score_label = tk.Label(window, text="Training Score:")
training_score_entry = tk.Entry(window)

phishing_label = tk.Label(window, text="3. Phishing", padx=25, pady=25, font=('', 12))
phishing_emails_label = tk.Label(window, text="Number of Phishing Emails:")
phishing_emails_entry = tk.Entry(window)
phishing_fails_label = tk.Label(window, text="Number of Phishing Fails:")
phishing_fails_entry = tk.Entry(window)
captured_data_label = tk.Label(window, text="Number of Data Captured:")
captured_data_entry = tk.Entry(window)
bonus_label = tk.Label(window, text="Bonus - Phishing Emails Identified:")
bonus_entry = tk.Entry(window)

policy_title_label = tk.Label(window, text="4. Policy Acknowledgment", padx=25, pady=25, font=('', 12))
policy_acknowledgment_label = tk.Label(window, text="Policy Acknowledgment:")

# policy acknowledgment radio yes or no

policy_acknowledgment_frame = tk.Frame(window)
policy_acknowledgment_frame.grid(row=10, column=2, sticky="w")

policy_acknowledgment = tk.IntVar(value=0)
policy_yes_radio = tk.Radiobutton(policy_acknowledgment_frame, text="Yes", variable=policy_acknowledgment, value=1)
policy_yes_radio.grid(row=0, column=0)
policy_no_radio = tk.Radiobutton(policy_acknowledgment_frame, text="No", variable=policy_acknowledgment, value=0)
policy_no_radio.grid(row=0, column=1)

profile_title_label = tk.Label(window, text="5. Profile Complete", padx=25, pady=25, font=('', 12))
profile_complete_label = tk.Label(window, text="Profile Complete:")

# profile complete radio yes or no

profile_complete_frame = tk.Frame(window)
profile_complete_frame.grid(row=12, column=2, sticky="w")


profile_complete = tk.IntVar(value=0)
profile_yes_radio = tk.Radiobutton(profile_complete_frame, text="Yes", variable=profile_complete, value=1)
profile_yes_radio.grid(row=0, column=0)
profile_no_radio = tk.Radiobutton(profile_complete_frame, text="No", variable=profile_complete, value=0)
profile_no_radio.grid(row=0, column=1)

micro_trainings_label = tk.Label(window, text="6. Micro Training", padx=25, pady=25, font=('', 12))
micro_trainings_sent_label = tk.Label(window, text="Number of Micro Trainings Sent:")
micro_trainings_sent_entry = tk.Entry(window)
mt_watched_label = tk.Label(window, text="Number of Micro Trainings Watched:")
mt_watched_entry = tk.Entry(window)

micro_quiz_label = tk.Label(window, text="7. Micro Quiz", padx=25, pady=25, font=('', 12))
average_micro_quiz_score_label = tk.Label(window, text="Average Micro Quiz Score:")
average_micro_quiz_score_entry = tk.Entry(window)

calculate_button = tk.Button(window, text="Calculate ESS", command=calculate_score)
total_score_label = tk.Label(window, text="Total ESS:", font=('', 15))

# Grid layout
external_breaches_label.grid(row=1, column=0, sticky="w", rowspan=3)
breaches_label.grid(row=1, column=1, sticky="e")
breaches_entry.grid(row=1, column=2, sticky="w")

dark_web_training_label.grid(row=2, column=1, sticky="e")
# dw training radio layout
#dw_training_yes_radio.grid(row=2, column=2, sticky="w")
#dw_training_no_radio.grid(row=3, column=2, sticky="w")

breach_remediation_label.grid(row=4, column=1, sticky="e")
breach_remediation_entry.grid(row=4, column=2, sticky="w")

training_quiz_label.grid(row=5, column=0, sticky="w")
training_score_label.grid(row=5, column=1, sticky="e")
training_score_entry.grid(row=5, column=2, sticky="w")

phishing_label.grid(row=6, column=0, sticky="w", rowspan=3)
phishing_emails_label.grid(row=6, column=1, sticky="e")
phishing_emails_entry.grid(row=6, column=2, sticky="w")
phishing_fails_label.grid(row=7, column=1, sticky="e")
phishing_fails_entry.grid(row=7, column=2, sticky="w")
captured_data_label.grid(row=8, column=1, sticky="e")
captured_data_entry.grid(row=8, column=2, sticky="w")
bonus_label.grid(row=9, column=1, sticky="e")
bonus_entry.grid(row=9, column=2, sticky="w")

policy_title_label.grid(row=10, column=0, sticky="w")
policy_acknowledgment_label.grid(row=10, column=1, sticky="e")
# policy radio layout


#policy_yes_radio.grid(row=10, column=2, sticky="w")
#policy_no_radio.grid(row=10, column=3, sticky="w")

profile_title_label.grid(row=12, column=0, sticky="w")
profile_complete_label.grid(row=12, column=1, sticky="e")

# profile radio layout
#profile_yes_radio.grid(row=12, column=2, sticky="w")
#profile_no_radio.grid(row=13, column=2, sticky="w")

micro_trainings_label.grid(row=14, column=0, sticky="w", rowspan=2)
micro_trainings_sent_label.grid(row=14, column=1, sticky="e")
micro_trainings_sent_entry.grid(row=14, column=2, sticky="w")
mt_watched_label.grid(row=15, column=1, sticky="e")
mt_watched_entry.grid(row=15, column=2, sticky="w")

micro_quiz_label.grid(row=16, column=0, sticky="w")
average_micro_quiz_score_label.grid(row=16, column=1, sticky="e")
average_micro_quiz_score_entry.grid(row=16, column=2, sticky="w")

calculate_button.grid(row=17, column=0, columnspan=3)
total_score_label.grid(row=18, column=0, columnspan=3)


window.mainloop()
