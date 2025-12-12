#Можако 4 вариант 
print("start code ...")
import json
with open("dump.json","r",encoding="utf-8") as file:
    data=json.load(file)
    skills=[]
    for item in data:
        if item.get("model")=="data.skill":
            skills.append({
            "code":item["fields"]["code"],
            "title":item["fields"]["title"]
        })
user_str=input("Введите номер квалификации: ").strip()

found=[]
for skill in skills:
    if user_str == skill["code"]:
        found.append(skill)
if found:
    print("=" * 20 + "Найдено" + "=" * 20)
    for skill in found:
        print(f'{skill["code"]} >> Специальность "{skill["title"]}"')
else:
            print("=" * 20 + "Не найдено" + "=" * 20)
print("... end code")