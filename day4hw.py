
web_dev = ["Asha", "Rahul", "Meena"]
data_science = ["Vikram", "Priya", "Kiran"]
ui_ux = ["Neha", "Arjun", "Sneha"]


all_participants = [web_dev, data_science, ui_ux]


web_dev.append("Rohit")


data_science.insert(1, "Anjali")


ui_ux.pop()


data_science_copy = data_science.copy()
data_science.clear()


first_two_web = web_dev[:2]
print("First two Web Dev participants:", first_two_web)


name_lengths = [len(name) for name in data_science_copy]
print("Lengths of Data Science names:", name_lengths)


asha_present = (
    "Asha" in web_dev or
    "Asha" in data_science or
    "Asha" in ui_ux
)
print("Is Asha in any workshop?", asha_present)


first_participants = (
    web_dev[0] if len(web_dev) > 0 else None,
    data_science_copy[0] if len(data_science_copy) > 0 else None,
    ui_ux[0] if len(ui_ux) > 0 else None
)

print("Tuple of first participants:", first_participants)


print("All Participants:", all_participants)
