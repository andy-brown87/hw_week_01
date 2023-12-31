users = {

"Jonathan": {
    "twitter": "jonnyt",
    "lottery_numbers": [6, 12, 49, 33, 45, 20],
    "home_town": "Stirling",
    "pets": [
    {
      "name": "fluffy",
      "species": "cat"
    },
    {
      "name": "fido",
      "species": "dog"
    },
    {
      "name": "spike",
      "species": "dog"
    }
  ]
  },
"Erik": {
    "twitter": "eriksf",
    "lottery_numbers": [18, 34, 8, 11, 24],
    "home_town": "Linlithgow",
    "pets": [
    {
      "name": "nemo",
      "species": "fish"
    },
    {
      "name": "kevin",
      "species": "fish"
    },
    {
      "name": "spike",
      "species": "dog"
    },
    {
      "name": "rupert",
      "species": "parrot"
    }
  ]
  },
"Avril": {
    "twitter": "bridgpally",
    "lottery_numbers": [12, 14, 33, 38, 9, 25],
    "home_town": "Dunbar",
    "pets": [
      {
        "name": "monty",
        "species": "snake"
      }
    ]
  }
}

# 1. Get Jonathan's Twitter handle (i.e. the string `"jonnyt"`)

print(Jonathon["twitter"])

# 2. Get Erik's hometown

print(Eric["home_town"])

# 3. Get the list of Erik's lottery numbers

print(Eric["lottery_numbers"])

# 4. Get the species of Avril's pet Monty

print(Avril["pets"]["species"])

# 5. Get the smallest of Erik's lottery numbers

print(sort.Eric["lottery_numbers"][0:1])

# 6. Return an list of Avril's lottery numbers that are even

for num in Avril["lottery_numbers"]:
 
    # checking condition
    if num % 2 == 0:
        print(num, end=" ")

# 7. Erik is one lottery number short! Add the number `7` to be included in his 
# lottery numbers

Erik.append({"lottery_numbers": [-1]"7"})

print(Eric)

# 8. Change Erik's hometown to Edinburgh

Erik[1]["hometown"] = "Edinburgh"
print(Eric)

# 9. Add a pet dog to Erik called "fluffy"

Erik.append({
      "name": "fluffy",
      "species": "dog"
    })

# 10. Add another person to the users dictionary

users.append( "Andy": {
    "twitter": "andy_zero",
    "lottery_numbers": [10, 13, 34, 37, 3, 27],
    "home_town": "South Queensferry",
    "pets": [
      {
        "name": "solo",
        "species": "fish"
      }
    ]
  })
