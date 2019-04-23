import json


def generate_domain():
    with open("action_info.json", 'r', encoding='utf-8') as json_file:
        _action = json.load(json_file)
    with open("slot_info.json", 'r', encoding='utf-8') as json_file:
        _slot = json.load(json_file)
    with open("user_info.json", 'r', encoding='utf-8') as json_file:
        _intent = json.load(json_file)

    with open("../Config/_domain.yml", mode='w', encoding='utf-8') as domain_file:
        domain_file.writelines("actions:" + "\n")
        for action in _action:
            domain_file.writelines("- " + action["Ename"] + "\n")
        domain_file.writelines("intents:" + "\n")
        for intent in _intent:
            domain_file.writelines("- " + intent["Ename"] + "\n")
        domain_file.writelines("slots:" + "\n")
        for slot in _slot:
            domain_file.writelines("  " + slot["Ename"] + ":\n")
            domain_file.writelines("    type: text" + "\n")
        domain_file.writelines("templates:" + "\n")
        for temp in _action:
            domain_file.writelines("  " + temp["Ename"] + ":\n")
            if "\n" in temp["Description"]:
                for reply in temp["Description"].split("\n"):
                    domain_file.writelines("  - text: "+reply+"\n")
            else:
                domain_file.writelines("  - text: "+temp["Description"]+"\n")
        domain_file.close()


def generate_story():
    with open("story.json", 'r', encoding='utf-8') as json_file:
        _story = json.load(json_file)
    with open("../Config/_stroy.yml", mode='w', encoding='utf-8') as story_file:
        story_file.write(_story)
        story_file.close()


generate_domain()
generate_story()
print("-"*5+"done"+"-"*5)
