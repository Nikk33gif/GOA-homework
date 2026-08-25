#2) სიის შექმნა და სიგრძე (len)
#შექმენით სია favorite_games, სადაც ჩაწერთ თქვენი 3 საყვარელი თამაშის/ჰობის დასახელებას.
#len() ფუნქციის გამოყენებით დაბეჭდეთ, სულ რამდენი ელემენტია თქვენს სიაში (მაგალითად: "ჩემს სიაშია 3 ელემენტი").
print(len("favorite_games"))

 #ახალი ელემენტის დამატება ბოლოში (append)
#append() მეთოდის გამოყენებით ჩაამატეთ სიაში კიდევ 1 ახალი თამაში.
#დაბეჭდეთ განახლებული სია.

favorite_games = ["Minecraft", "GTA V", "FIFA 24"]

favorite_games.append("Fortnite")

print(favorite_games)


favorite_games = ["GTA", "FIFA", "Fortnite", "Roblox"]

favorite_games.insert(0, "Minecraft")

print(favorite_games)

#5)ელემენტის ამოშლა (pop)
#.pop() მეთოდის გამოყენებით ამოშალეთ სიის ბოლო ელემენტი და შეინახეთ ის ცვლადში removed_game.
#დაბეჭდეთ შეტყობინება: "წაშლილი ელემენტია: [აქ ჩასვით removed_game]".
#საბოლოოდ დაბეჭდეთ თქვენი საბოლოო სია.

favorite_games = ["Minecraft", "GTA", "FIFA", "Fortnite", "Roblox"]

removed_game = favorite_games.pop("Roblox")

print("წაშლილი ელემენტია:", removed_game)
print(favorite_games)

fruits = ["apple", 93, "bannana", 23, "mango", True, 15, False, 3.1, "Hello World!"]
res = []

for item in fruits:
    if type(item) == int:
        res.append(item)

print(res)