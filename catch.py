from telethon import events , TelegramClient
from asyncio import sleep as zzz
from random import randint
from re import match


api_id = 21453458
api_hash = '565cac9ed11ff64ca7e2626f7b1b18b2'
bot = TelegramClient('session' , api_id , api_hash)
chat = 572621020

list = ["Braixen","Delphox","Absol","Cloyster","Sandile","Krokorok","Krookodile","Ferroseed","Ferrothorn","Houndour","Houndoom","Vaporeon","Zoroark","Keldeo","Totodile","Croconaw","Feraligatr","Electrode","Mankey","Primeape","Annihilape","Torracat","Incineroar","Popplio","Brionne","Primarina","Toxapex","Shellder","Weedle","Kakuna","Swablu","Scraggy","Wimpod","Rhyperior","Rhydon","Shelmet","Accelgor","Vullaby","Mandibuzz","Litwick","Lampent","Chandelure","Toxticity","Helioptile","Heliolist","Rungerigus","Cofagrigus","Phantump","Trevenant","Kommo-o","Jangmo-o","Fennekin","Eevee","Buizel","Floatzel","Munchlax","Monferno","Ursaring","Prinplup","Glalie","Mamoswine","Abomasnow","Arceus","Arceus","Scorbunny","Raboot","Grookey","Dottler","Consvisquire","Corvknight","Rookidee","Mudsdale","Wishiwashi","Boldore","Gigalith","Gurdurr","Flareon","Espeon","Glaceon","Leafeon","Umbreon","Sirfetch'd","Articuno","Arcanine","Zorua","Growlithe","Porygon","Staravia","Jolteon","Sneasler","Sneasel","Basculin","Ursaluna","Samurott","Voltorb","Raichu","Rufflet","Piplup","Infernape","Starly","Litten","Empoleon","Eiscue","Crustle","Dwebble","Decidueye","Quilava","Typhlosion","Shinx","Luxio","Luxray" "Sneasler","Sneasel","Cyndaquil","Sylveon","Basculegion","Chimchar", "Zapdos", "Moltres", "Mewtwo", "Mew", "Raikou", "Entei", "Suicune", "Lugia", "Ho-Oh", "Celebi", "Regirock", "Regice", "Registeel", "Latias", "Latios", "Kyogre", "Groudon", "Rayquaza", "Jirachi", "Deoxys", "Uxie", "Mesprit", "Azelf", "Dialga", "Palkia", "Heatran", "Regigigas", "Giratina", "Cresselia", "Darkrai", "Shaymin", "Arceus", "Victini", "Cobalion", "Terrakion", "Virizion", "Golurk", "Golett", "Tornadus", "Thundurus", "Reshiram", "Zekrom", "Landorus", "Kyurem", "Keldeo", "Meloetta", "Genesect", "Xerneas", "Yveltal", "Zygarde", "Diancie", "Hoopa", "Volcanion", "Type: Null", "Silvally", "Tapu Koko", "Tapu Lele", "Tapu Bulu", "Tapu Fini", "Cosmog", "Cosmoem", "Solgaleo", "Lunala", "Nihilego", "Buzzwole", "Pheromosa", "Xurkitree", "Celesteela", "Kartana", "Guzzlord", "Necrozma", "Magearna", "Marshadow", "Zeraora", "Meltan", "Melmetal", "Zacian", "Zamazenta", "Eternatus", "Kubfu", "Urshifu", "Regieleki", "Regidrago", "Glastrier", "Spectrier", "Calyrex", "Abra", "Kadabra", "Alakazam", "Sharpedo", "Machop", "Machoke", "Machamp", "Geodude", "Graveler", "Golem", "Gastly", "Haunter", "Gengar", "Dratini", "Dragonair", "Dragonite", "Larvitar", "Pupitar", "Tyranitar", "Bagon", "Shelgon", "Salamence", "Beldum", "Metang", "Metagross", "Gible", "Gabite", "Garchomp", "Ralts", "Kirlia", "Gardevoir", "Gallade", "Magikarp", "Gyarados", "Charmander", "Charmeleon", "Charizard", "Squirtle", "Wartortle", "Blastoise", "Bulbasaur", "Ivysaur", "Venusaur", "Treecko", "Grovyle", "Sceptile", "Wishiwashi", "Torchic", "Combusken", "Blaziken", "Mudkip", "Marshtomp", "Swampert", "Aron", "Lairon", "Aggron", "Slowpoke", "Slowbro", "Slowking", "Scyther", "Scizor", "Porygon", "Porygon2", "Porygon-Z", "Deino", "Zweilous", "Hydreigon", "Axew", "Fraxure", "Haxorus", "Goomy", "Sliggoo", "Goodra", "Dreepy", "Drakloak", "Dragapult", "Froakie", "Frogadier", "Greninja", "Flabébé", "Floette", "Florges", "Buneary", "Lopunny", "Riolu", "Lucario", "Slaking", "Slakoth", "Vigoroth", "Mienfoo", "Mienshao", "Zorua", "Zoroark", "Larvesta", "Volcarona", "Noibat", "Noivern", "Jangmo-o", "Hakamo-o", "Kommo-o", "Togepi", "Togetic", "Togekiss", "Mareep", "Flaaffy", "Ampharos", "Staryu", "Starmie", "Staraptor", "Braviary", "Bisharp", "Kingambit", "Tinkatink", "Tinkatuff", "Tinkaton", "Fletchling", "Fletchinder", "Talonflame", "Pawniard", "Bisharp", "Darumaka", "Darmanitan", "Litleo", "Pyroar", "Goomy", "Sliggoo", "Goodra", "Noibat", "Noivern", "Litten", "Torracat", "Incineroar", "Popplio", "Brionne", "Primarina", "Crabrawler", "Crabominable", "Rockruff", "Lycanroc", "Cosmog", "Cosmoem", "Solgaleo", "Lunala", "Nihilego", "Buzzwole", "Pheromosa", "Xurkitree", "Celesteela", "Kartana", "Guzzlord", "Poipole", "Naganadel", "Stakataka", "Blacephalon", "Zeraora", "Meltan", "Melmetal", "Grookey", "Thwackey", "Rillaboom", "Scorbunny", "Raboot", "Cinderace", "Sobble", "Drizzile", "Inteleon", "Cramorant", "Arrokuda", "Barraskewda", "Duraludon", "Dreepy", "Drakloak", "Dragapult", "Zacian", "Zamazenta", "Eternatus", "Kubfu", "Urshifu", "Zarude", "Regieleki", "Glastrier", "Spectrier", "Calyrex", "Venusaur", "Charizard", "Blastoise", "Beedrill", "Pidgeot", "Alakazam", "Slowbro", "Gengar", "Kangaskhan", "Pinsir", "Gyarados", "Aerodactyl", "Mewtwo", "Ampharos", "Steelix", "Scizor", "Heracross", "Houndoom", "Tyranitar", "Sceptile", "Blaziken", "Swampert", "Gardevoir", "Sableye", "Mawile", "Aggron", "Medicham", "Manectric", "Sharpedo", "Camerupt", "Altaria", "Banette", "Absol", "Glalie", "Salamence", "Metagross", "Latias", "Latios", "Rayquaza", "Lopunny", "Garchomp", "Lucario", "Abomasnow", "Gallade", "Audino", "Eternatus", "Zacian", "Shaymin", "Dialga", "Palkia", "Mewtwo", "Arceus", "Zamazenta", "Glastrier", "Calyrex", "Kyurem", "Lunala", "Necrozma", "Rayquaza", "Cosmoem", "Yveltal", "Kyogre", "Xerneas", "Cosmog", "Groudon", "Giratina", "Zeraora", "Marshadow", "Buzzwole", "Solgaleo", "Zyagrde", "Regigigas", "Ho-oh", "Lugia", "Deoxys", "Reshiram", "Zekrom", "Victini", "Cobalion", "Virizion", "Terrakion", "Keldeo", "Meloetta", "Pheromosa", "Magearna", "Tapu Koko", "Tapu Lele", "Tapu Fini", "Tapu Bulu", "Kartana", "Urshifu", "Regieleki", "Spectrier", "Venusaur", "Beedrill", "Kangaskhan", "Aerodactyl", "Ampharos", "Scizor", "Houndoom", "Blaziken", "Swampert", "Salamence", "Garchomp", "Charmander", "Charizard", "Froakie", "Primarina", "Drakloak", "Gabite", "Gabite", "Goomy", "Golett", "Alakazam", "Golisopod", "Slakoth","✨"]

async def send_hunt():
    while hunt:
        try:
            await bot.send_message(chat, "/hunt")
            await zzz(randint(17, 20))
        except:
            await zzz(2)
        await zzz(randint(1190, 1200))
        if hunt:
            await bot.send_message(chat, "/go")
            await zzz(1)
            await bot.send_message(chat, "/go")
       
@bot.on(events.NewMessage(outgoing=True,pattern='/go'))
async def begin(event):
    global hunt
    hunt = True
    x = await bot.send_message(chat , "/hunt")
    try:  
     async with bot.conversation('@Hexamonbot') as conv:
       await conv.get_response(x.id)
    except:
       await zzz(2,3)
       await bot.send_message(chat , "/hunt")
    for i in range(5,5000):
      await zzz(randint(5000, 5020))
      await bot.send_message(chat , "/hunt")

@bot.on(events.NewMessage(chats=chat,incoming=True))
async def hunt(event):
    if hunt == True:
     text = event.message.text
     hun = True
     message = await bot.get_messages(chat, ids=event.message.id)
  
     if ("TM" in text):
        print(event.message.text)
        await zzz(randint(2,3))
        x = await bot.send_message(chat , "/hunt")
        try:  
         async with bot.conversation('@Hexamonbot') as conv:
           await conv.get_response(x.id)
        except:
           await zzz(2,3)
           await bot.send_message(chat , "/hunt")
     elif any(item in text for item in list):
        await message.click(text="Battle")
        await message.click(text="Battle")
        await message.click(text="Battle")
        await message.click(text="Battle")
        await message.click(text="Battle")
        await message.click(text="Battle")
        await message.click(text="Battle")
        await message.click(text="Battle")
        await message.click(text="Battle")
     elif("A wild" in text or "An expert" in text):
      if hun == False:
       pass
      else:
       await zzz(randint(2,3))
       x = await bot.send_message(chat , "/hunt")
       try:  
        async with bot.conversation('@Hexamonbot') as conv:
          await conv.get_response(x.id)
       except:
          await zzz(2,3)
          await bot.send_message(chat , "/hunt")
          

@bot.on(events.NewMessage(chats=chat,incoming=True))
async def hunt(event):
   print(event.message.text)
   if event.message.text[:13] == "Battle begins":
        message = await bot.get_messages(chat, ids=event.message.id)
        await zzz(15)
        await message.click(text = "Poke Balls")
        await message.click(text = "Poke Balls")
        await message.click(text = "Poke Balls")      
        await message.click(text = "Poke Balls")
        await message.click(text = "Poke Balls")
        await message.click(text = "Poke Balls")  

@bot.on(events.MessageEdited(chats=chat))
async def cacther(event):
   message = await bot.get_messages(chat, ids=event.message.id)
   await message.click(text = "Poke Balls")
   await message.click(text = "Poke Balls")
   await message.click(text = "Poke Balls") 
   await message.click(text = "Poke Balls")
   await message.click(text = "Poke Balls")
   await message.click(text = "Poke Balls") 
   await message.click(text = "Poke Balls")
   await message.click(text = "Poke Balls")
   await message.click(text = "Poke Balls") 
   if event.message.text[:4] == "Wild":
    
    
    await zzz(1)
    await message.click(text = "Regular")
    await message.click(text = "Regular")
    await message.click(text = "Regular")
    await message.click(text = "Regular")
    await message.click(text = "Regular")
    await message.click(text = "Regular")
    await message.click(text = "Regular")
    await message.click(text = "Regular")
    await message.click(text = "Regular")
    await message.click(text = "Regular")
    await message.click(text = "Regular")
    await message.click(text = "Regular")
    await message.click(text = "Regular")
    await message.click(text = "Regular")
    await message.click(text = "Regular")
    await message.click(text = "Regular")
    await message.click(text = "Regular")
    await message.click(text = "Regular")
    await message.click(text = "Regular")
    await message.click(text = "Regular")
    await message.click(text = "Regular")
    

   if any(keyword in event.message.text for keyword in ['fled', 'fainted', 'caught']):
      await zzz(randint(2,3))
      x = await bot.send_message(chat , "/hunt")
      try:  
       async with bot.conversation('@Hexamonbot') as conv:
         await conv.get_response(x.id)
      except:
         await zzz(2,3)
         await bot.send_message(chat , "/hunt")



@bot.on(events.NewMessage(outgoing=True,pattern='/stop'))
async def stop(event):
    global hunt
    hunt = False


bot.start()
bot.run_until_disconnected()