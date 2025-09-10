"""
Fatima Nadeem
lab4, dictionary and functions 
Sep 10, 2025
"""

print("----- Example 1: dictionary -----")
contacts = {
    "Bill" : "718-111-2222",
    "Martha": "646-000-3333",
    "Peter" : "212-000-1111"
}
print(contacts)

user1 = contacts["Martha"]
print(f"user's phone number = {user1}")

contacts["Anna"] = "646-222-3333"
print(contacts)

contacts["Peter"] = "800-000-0000"
print(contacts)

print("----- Example 2: loop through a dictionary -----")
for i in contacts:
    print(i)

for i in contacts:
    print(contacts[i])

for i in contacts:
    print(f"{i} = {contacts[i]}")

print("----- Example 3: length of a dictionary ------")
print(f"Dictionary has {len(contacts)} user(s)")

print("----- Example 4: copy a dictionary -----")
copy_contact1 = contacts.copy()
copy_contact2 = dict(contacts)
print(copy_contact1)
print(copy_contact2)

print("----- Example 5: remove a key: value pair in a dictionary -----")
print(contacts)
contacts.pop("Peter")
print(contacts)

print("----- Example 6: add a new key: value pair in a dictionary -----")
print(contacts)
contacts.update({"Lucas": "212-111-1111"})
print(contacts)

print("----- Example 7: return items, keys and values in a dictionary -----")
print(f"Return items = {contacts.items()}")
print(f"Return keys = {contacts.keys()}")
print(f"Return values = {contacts.values()}")

print("----- Example 8: dictionary application -----")
phrase = "to be or not to be"
list_phrase = phrase.split()
word_count_dict = {}
for word in list_phrase:
    if word in word_count_dict:
        word_count_dict[word] += 1 
    else:
        word_count_dict[word] = 1 

for word in word_count_dict:
    print(f"'{word}' appears {word_count_dict[word]} time(s)")

print("----- EXERCISE -----")
users = ["peterpan@yahoo.com", "annie@hotmail.com", "Carl@hotmail.com", "martha@gmail.com", "cassie@yahoo.com", "Josue@hotmail.com", "John@hotmail.com"]

email_count = {"gmail": 0, "hotmail": 0, "yahoo": 0}

for i in users:
    if "gmail" in i:
        email_count["gmail"] += 1
    elif "hotmail" in i:
        email_count["hotmail"] += 1
    elif "yahoo" in i:
        email_count["yahoo"] += 1

for g in email_count:
    print(f"{g} users = {email_count[g]}")
