import discord
from discord.ui import View, Button, Modal, TextInput
import os


## 1. Create Node Class
class Node:
  def __init__(self, value, answer="", children=[]):
    self.value = value
    self.answer = answer
    self.children = children

    #setup the Node

### 2. Create an Example Decision Tree
node24 = Node("Congrats, your partner is Greenland Dog! Greenland Dog is an arctic dog breed with thick winter hair and muscular build resistant to cold. You died of tetanus from a scar on your hand that was rummaging through the wreckage of an airplane. If the Greenland Dog, talented in tracking and hunting, were with you, you wouldn't die of tetanus." , answer='Check it')
node23 = Node("Congrats, your partner is a Siberian Husky! Siberian Husky is a breed of dog from the Arctic who can withstand the cold due to its thick winter fur and muscular build. After being rediscovered and killed by a polar bear while approaching too slowly, you need an Siberian Husky with good speed and agility.  Follow your dog's example and move quickly." , answer='Approach slowly while looking around.')
node22 = Node("Congrats, your partner is Alaska Malamute! Alaska Malamute is a breed of arctic dog with thick winter coats and muscular build that endures the cold. I would like to recommend the strong and patient Alaska Malamute to you, who died after falling into a blindfolded pit while running. Learn some patience by following the example of a dog." , answer='Run and check')
node21 = Node("Congrats, your partner is the Great Spitz! Great Spitz is an Antarctic breed with thick winter hair and a muscular build, which makes it resistant to cold. And it has a calm, elegant personality, and a strong loyalty to its owner. If you post a picture on Instagram of yourself, who wants to be an influencer under any circumstances, with the elegant Great Spitz, you will be rescued faster." , answer='Check')
node20 = Node("Congrats, your partner is an Antarctic Husky! An Antarctic Husky is resistant to the cold as a breed with thick fur and a muscular build. It is also a breed used in Antarctic expeditions, acting as a sled dog and running long distances. Continuing to walk, you eventually died of hunger, but you would have survived for about five more minutes if the Antarctic Husky were with you." , answer='First off, get out of this area')
node19 = Node("Congrats, your mate is a Jack Russell Terrier! Jack Russell Terrier is an active, tactile dog from Antarctica, mainly used as a hunting dog and used to track and hunt small animals underground. You were sadly eaten by beasts, but with Jack Russell Terrier, you will survive next! Way to go!" , answer='Go for hunt')
node18 = Node("Your dog died trying to help his parents, who couldn't swim.Do you deserve to have a dog?" , answer='2 Hours')
node17 = Node("Congratulations, your partner is Border Collie! Border Collie needs good affinity, excellent training, and consistent activities. The situation of drifting in the sea was too much stress for Border Collie to endure. If you keep Border Collie, please stick to your schedule!" , answer='Let your dog to explore the island')
node16 = Node("Congratulations, your mate is a Boston Terrier! Boston Terriers are friendly, curious, and playful. Don't take your eyes off the Boston Terriers. You will have a very low chance of meeting again!" , answer='Hold out on a lifeboat')
node15 = Node("Congratulations, your partner is Pomeranian! Pomeranian has a good affinity but is not resistant to the cold. Dress your partner with warm clothes and shoes in winter!" , answer='No')
node14 = Node("Congratulations, your partner is Spitz! Spitz is friendly and can withstand the cold with its double hair. However, he died from the cold while he was watching without his hair fully dry. If you keep Spitz, dry its hair thoroughly after a bath!" , answer='Yes')
node13 = Node("Congratulations, your mate is the Portuguese Water Dog! The Portuguese Water Dog is friendly and swims well. It's also good at hunting, so hunting fish is gum! Although everyone died of starvation because of the lack of fire, it's a relief that we're not really drifting in the sea. Yay!" , answer='Fish')
node12 = Node("Congratulations, your mate is a Labrador Retriever! Labrador Retriever is friendly and swims well. However, Labrador Retriever only has the hunting ability to catch floating objects in the water, so you unfortunately died of starvation. Fortunately, thanks to the Labrador Retriever's affinity, your friend survived. Yay!" , answer='Floating snack')
node11 = Node("Yes, you don't have to waste your energy. You can see the light in the distance" , answer='Don’t check it',children=[node22, node23])
node10 = Node("Right, it's not a good situation to take pictures.You're hungry now.Your choice?" , answer='Don’t check',children=[node19, node20])
node9 = Node("Would you hold out on a lifeboat with your parents or let your dog to explore the island?" , answer='30mins',children=[node16, node17])
node8 = Node("That's right, finding an island where you can rest is a priority rather than hunting. You managed to get to the island and start a fire. Feeling anxious, would you ask your dog to watch around?", answer='No',children=[node14, node15])
node7 = Node("Your dog succeeded in hunting.What’s in your dog’s mouth?" , answer='Yes',children=[node12, node13])
node6 = Node("While running away from a polar bear, you may have found the wreckage of an airplane." , answer='Polar bear',children=[node11, node24])
node5 = Node("As you climbed down the tree to approach the penguins,you found a space in the distance that looked perfect for taking a commemorative photo. Should we go check it out?" , answer='Penguin',children=[node10, node21])
node4 = Node("You gave a lifeboat to the one who couldn't swim. What's your relationship with the one?", answer='Parents',children=[node9, node18])
node3 = Node("While drifting, a friend whines that he is hungry.Would you let your dog hunt?", answer='Friend',children=[node7, node8])
node2 = Node("You were lucky to get stuck in a tree when you crashed on the plane. But you heard a sound under a tree. What is it?", answer='Polar regions',children=[node5, node6])
node1 = Node("You gave a lifeboat to the one who couldn't swim. What's your relationship with the one?", answer='Sea', children=[node3, node4])
root = Node('Where were you in distress?', children=[node1, node2])


# ## 3. Create GuessOptionsView Class
class GuessOptionView(View):
  def __init__(self, node):
    # GuessOptionView는 UI 엘리멘트, 그래서 ,node를 통해서 표시할 데이터를 전달해줘야함
    super().__init__()
    for child in node.children:
      self.add_item(GuessButton(child))

      #setup the GuessOptionsView

  async def handleButtonPress(self, interaction, node):
    if(node.children == []):
      await interaction.response.send_message(content=f'OK ...{node.value}', view=WrongView(node))
    else:
      await interaction.response.send_message(content=node.value, view=GuessOptionView(node))
    #what should happen when a button is pressed?


## 4. Create GuessButton 
class GuessButton(Button):
  def __init__(self, node):
    super().__init__(label=node.answer)
    self.node = node
    # 노드 안 콘텐츠 저장
    #setup the GuessButton

  async def callback(self, interaction):
    await self.view.handleButtonPress(interaction, self.node)
    #what happens when this button is pressed


# ## 5. Create WrongView
class WrongView(View):
    def __init__(self, node):
        super().__init__()
        self.node = node

    @discord.ui.button(label="Check your soulmate's look")
    async def buttonCallback(self, interaction, button):
        if self.node.value.startswith("Congratulations, your mate is a Labrador Retriever!"):
            embed = discord.Embed(title="Your Best buddy",
                                  description="I'm sure you found your soulmate",
                                  color=0xffccfd)
            embed.set_image(url="https://cdn.royalcanin-weshare-online.io/hz9p43oBRYZmsWpcq7ap/v1/bp-lot-1-labrador-couleur-outdoor")
            embed.add_field(name="Congratulations, your mate is a Labrador Retriever!",
                            value="Labrador Retriever is friendly and swims well. However, Labrador Retriever only has the hunting ability to catch floating objects in the water, so you unfortunately died of starvation. Fortunately, thanks to the Labrador Retriever's affinity, your friend survived. Yay!",
                            inline=True)
            await interaction.response.send_message(embed=embed)

        elif self.node.value.startswith("Congratulations, your mate is the Portuguese Water Dog!"):
            embed=discord.Embed(title="Your Best buddy", 
                                description="I sure you found your soulmate",
                                color=0xffccfd)
            embed.set_thumbnail(url="https://www.akc.org/wp-content/uploads/2017/11/Portuguese-Water-Dog-standing-in-profile-outdoors.jpg")
            embed.add_field(name="Congratulations, your mate is the Portuguese Water Dog!",  
                            value="The Portuguese Water Dog is friendly and swims well. It's also good at hunting, so hunting fish is gum! Although everyone died of starvation because of the lack of fire, it's a relief that we're not really drifting in the sea. Yay!", 
                            inline=True)
            await interaction.response.send_message(embed=embed)

        elif self.node.value.startswith("Congratulations, your partner is Spitz!"):
            embed=discord.Embed(title="Your Best buddy",
                                description="I sure you found your soulmate", 
                                color=0xffccfd)
            embed.set_thumbnail(url="https://dogtime.com/wp-content/uploads/sites/12/2023/10/GettyImages-1489388446-e1698507707274.jpg")
            embed.add_field(name="Congratulations, your partner is Spitz!", 
                            value="Spitz is friendly and can withstand the cold with its double hair. However, he died from the cold while he was watching without his hair fully dry. If you keep Spitz, dry its hair thoroughly after a bath!", 
                            inline=True)
            await interaction.response.send_message(embed=embed)

        elif self.node.value.startswith("Congratulations, your partner is Pomeranian!"):
            embed=discord.Embed(title="Your Best buddy", 
                                description="I'm sure you found your soulmate", 
                                color=0xffccfd)
            embed.set_thumbnail(url="https://cdn05.zipify.com/Tay4vjJlvXwCeCDgi4W_jeHurww=/fit-in/3840x0/504040786400472a9712f5c9d992cfa2/pot013-blog-hero-horizontal.jpeg")
            embed.add_field(name="Congratulations, your partner is Pomeranian!", 
                            value="Pomeranian has a good affinity but is not resistant to the cold. Dress your partner with warm clothes and shoes in winter!", 
                            inline=True)
            await interaction.response.send_message(embed=embed)

        elif self.node.value.startswith("Congratulations, your mate is a Boston Terrier!"):
            embed=discord.Embed(title="Your Best buddy", 
                            description="I'm sure you found your soulmate", 
                            color=0xffccfd) 
            embed.set_thumbnail(url="https://www.dutch.com/cdn/shop/articles/shutterstock_741404581.jpg?v=1697091249")
            embed.add_field(name="Congratulations, your mate is a Boston Terrier!", 
                        value="Boston Terriers are friendly, curious, and playful. Don't take your eyes off the Boston Terriers. You will have a very low chance of meeting again!", 
                        inline=True)
            await interaction.response.send_message(embed=embed)
      
        elif self.node.value.startswith("Congratulations, your partner is Border Collie!"):
            embed=discord.Embed(title="Your Best buddy", 
                          description="I'm sure you found your soulmate", 
                          color=0xffccfd) 
            embed.set_thumbnail(url="https://www.bellaandduke.com/wp-content/uploads/2023/01/Border-collie-owners-dog-breed-guide-1.png")
            embed.add_field(name="Congratulations, your partner is Border Collie!", 
                      value="Border Collie needs good affinity, excellent training, and consistent activities. The situation of drifting in the sea was too much stress for Border Collie to endure. If you keep Border Collie, please stick to your schedule!", 
                      inline=True)
            await interaction.response.send_message(embed=embed)

        elif self.node.value.startswith("Congrats, your mate is a Jack Russell Terrier!"):
            embed=discord.Embed(title="Your Best buddy", 
                      description="I'm sure you found your soulmate", 
                      color=0xffccfd) 
            embed.set_thumbnail(url="https://cdn.britannica.com/00/234900-050-0BEFCBC6/Parson-Jack-Russell-Terrier-dog-broken-coat.jpg")
            embed.add_field(name="Congrats, your mate is a Jack Russell Terrier!", 
                  value="Jack Russell Terrier is an active, tactile dog from Antarctica, mainly used as a hunting dog and used to track and hunt small animals underground. You were sadly eaten by beasts, but with Jack Russell Terrier, you will survive next! Way to go!", 
                  inline=True)
            await interaction.response.send_message(embed=embed)

        elif self.node.value.startswith("Congrats, your partner is an Antarctic Husky!"):
            embed=discord.Embed(title="Your Best buddy", 
                  
                                description="I'm sure you found your soulmate", 
                  
                                color=0xffccfd) 
            embed.set_thumbnail(url="https://collections.museumsvictoria.com.au/content/media/47/270897-large.jpg")
            embed.add_field(name="Congrats, your partner is an Antarctic Husky!", 
              
                            value="An Antarctic Husky is resistant to the cold as a breed with thick fur and a muscular build. It is also a breed used in Antarctic expeditions, acting as a sled dog and running long distances. Continuing to walk, you eventually died of hunger, but you would have survived for about five more minutes if the Antarctic Husky were with you.", 
              
                            inline=True)
            await interaction.response.send_message(embed=embed)
          
        elif self.node.value.startswith("Congrats, your partner is the Great Spitz!"):
            embed=discord.Embed(title="Your Best buddy", 

                            description="I'm sure you found your soulmate", 

                            color=0xffccfd) 
            embed.set_thumbnail(url="https://b3117286.smushcdn.com/3117286/wp-content/uploads/2019/10/shutterstock_281445887-1-scaled.jpg?lossy=1&strip=1&webp=1")
            embed.add_field(name="Congrats, your partner is the Great Spitz!", 

                        value="Great Spitz is an Antarctic breed with thick winter hair and a muscular build, which makes it resistant to cold. And it has a calm, elegant personality, and a strong loyalty to its owner. If you post a picture on Instagram of yourself, who wants to be an influencer under any circumstances, with the elegant Great Spitz, you will be rescued faster.", 

                        inline=True)
            await interaction.response.send_message(embed=embed)

      
        elif self.node.value.startswith("Congrats, your partner is Alaska Malamute!"):
            embed=discord.Embed(title="Your Best buddy", 

                            description="I'm sure you found your soulmate", 

                            color=0xffccfd) 
            embed.set_thumbnail(url="https://www.thesprucepets.com/thmb/D1jaz5CGkt-fiA02SrzYDzBl5gY=/3000x0/filters:no_upscale():strip_icc()/ProfileofAdultAlaskanMalamute-fe7ca34e39694917993f5257ed62c6c9.jpg")
            embed.add_field(name="Congrats, your partner is Alaska Malamute!", 

                        value="Alaska Malamute is a breed of arctic dog with thick winter coats and muscular build that endures the cold. I would like to recommend the strong and patient Alaska Malamute to you, who died after falling into a blindfolded pit while running. Learn some patience by following the example of a dog.", 

                        inline=True)
            await interaction.response.send_message(embed=embed)

        elif self.node.value.startswith("Congrats, your partner is a Siberian Husky!"):
            embed=discord.Embed(title="Your Best buddy", 

                        description="I'm sure you found your soulmate", 

                        color=0xffccfd) 
            embed.set_thumbnail(url="https://cdn.britannica.com/84/232784-050-1769B477/Siberian-Husky-dog.jpg")
            embed.add_field(name="Congrats, your partner is a Siberian Husky!", 

                    value="Siberian Husky is a breed of dog from the Arctic who can withstand the cold due to its thick winter fur and muscular build. After being rediscovered and killed by a polar bear while approaching too slowly, you need an Siberian Husky with good speed and agility.  Follow your dog's example and move quickly.", 

                    inline=True)
            await interaction.response.send_message(embed=embed)

        elif self.node.value.startswith("Congrats, your partner is Greenland Dog!"):
            embed=discord.Embed(title="Your Best buddy", 

                    description="I'm sure you found your soulmate", 

                    color=0xffccfd) 
            embed.set_thumbnail(url="https://www.hundeo.com/wp-content/uploads/2019/09/Gro%CC%88nlandhund.jpg")
            embed.add_field(name="Congrats, your partner is Greenland Dog!", 

                value="Greenland Dog is an arctic dog breed with thick winter hair and muscular build resistant to cold. You died of tetanus from a scar on your hand that was rummaging through the wreckage of an airplane. If the Greenland Dog, talented in tracking and hunting, were with you, you wouldn't die of tetanus.", 

                inline=True)
            await interaction.response.send_message(embed=embed)



## 7. Run the Discord Bot
intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
  print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith('I want my soulmate'):
    await message.channel.send(content=root.value, view=GuessOptionView(root))


token = os.getenv("DISCORD_BOT_SECRET")
client.run(token)
