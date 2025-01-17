heros = ["spider man", "thor", "hulk", "iron man", "captain america"]
print(f"1. Length of the list. Ans = {len(heros)}")
print(f"2. Add 'black panther' at the end of this list")
heros.append("black panther")
print(heros)
print(
    f"3. You realize that you need to add 'black panther' after 'hulk',so remove it from the list first and then add it after 'hulk'"
)
heros.remove("black panther")
heros.insert(2, "black panther")
print(heros)
print(
    "4. Now you don't like thor and hulk because they get angry easily :) So you want to remove thor and hulk from list and replace them with doctor strange (because he is cool). Do that with one line of code."
)
heros[1:3] = ["doctor strange"]
print(heros)
print("5. Sort the heros list in alphabetical order")
heros.sort()
print(heros)
