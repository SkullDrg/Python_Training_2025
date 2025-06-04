#This program conducts an investigation on a crime scene, asking the user for details 
# about the crime and providing a summary of the findings.

Questions = {
    1: ("Did you called the victim?", "Yes", "No"),
    2: ("Have you been on the crime scene?", "Yes", "No"),
    3: ("Do you live near the victim?", "Yes", "No"),
    4: ("Did you owe the victim?", "Yes", "No"),
    5: ("Have you ever worked with the victim?", "Yes", "No"),
}

def interrogation(prompt_dict):
    yes = 0
    no = 0
    for q_id, (question, _, _) in prompt_dict.items():
        while True:
            answer = input(f"{question} (yes/no): ").strip().lower()
            if answer == "yes":
                yes += 1
                break
            elif answer == "no":
                no += 1
                break
            else:
                print("Please, answer with just yes or no.")
    return yes

yes_count = interrogation(Questions)

if yes_count == 2:
    Investigation_Result = "You are a suspect."
elif 3 <= yes_count <= 4:
    Investigation_Result = "You are an accomplice."
elif yes_count == 5:
    Investigation_Result = "You are the killer."
else:
    Investigation_Result = "You are innocent."

print(Investigation_Result)