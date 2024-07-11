import discord
from discord.ext import commands
import random
import os

GUILD_ID = 1249397298618957999
STAFF_EMERGENCY_VC_ID = 1250140892497444929
SPECIAL_ROLE_ID = 1253431093936390368
TEXT_CHANNEL_ID = 1250140892497444929
OPEN_TICKET_CHANNEL_ID = 1250149651550568478
RULES_CONFIRMED_ROLE_ID = 1253459018228432897

intents = discord.Intents.default()
intents.message_content = True
intents.members = True
intents.voice_states = True
bot = commands.Bot(command_prefix='!', intents=intents)

user_data = {}
current_lyric = None 

@bot.event
async def on_ready():
    print(f'Bot is ready. Logged in as {bot.user}')


@bot.event
async def on_voice_state_update(member, before, after):
    if before.channel != after.channel and after.channel and after.channel.id == STAFF_EMERGENCY_VC_ID:
        guild = bot.get_guild(GUILD_ID)
        role = guild.get_role(SPECIAL_ROLE_ID)
        if role:
            text_channel = guild.get_channel(TEXT_CHANNEL_ID)
            if text_channel:
                await text_channel.send(f'{role.mention} {member.name} has commenced a Staff Emergency Meeting! Join in <#1250140892497444929>.')

@bot.command()
async def send_rules(ctx):
    description = """
### __**1. Discord TOS (13+)**__
  •  https://discord.com/terms 
  •  https://discord.com/guidelines
  •  Make sure you comply with Discords TOS. This includes only ages 13+ allowed as well as no 'alt' accounts allowed.
### __**2. Respect Regular Members**__
  •  Stay respectful to all members in the server. We want this server to be a comfortable space for everybody.
  •  Do not discriminate against someone or harass them.
  •  This rule extends to DMs.
### __**3. Respect Teya**__
  •  Any disrespect towards Teya is not allowed.
  •  This includes rude comments, speculating on her personal life, sexualisation of her, constant bothering or harassing her.
  • Do not share Teya's messages outside of the server and/or on other social media platforms.
  • Do not attempt to ping Teya.
### __**4. Respect Moderators Judgement**__
 • This server aims to be a space to pursue firm values such as love, empathy, peace, safety and inclusion.
 • Do not question the Team's punishments as those are for the server's wellbeing.
### __**5. No NSFW**__
  •  Content flagged as NSFW (stands for Not Safe For Work) includes graphic violence, nudity, pornography, and other types of profanity or disturbing media. Posting NSFW content in the server will result in an immediate ban.
### __**6. No Drama**__
  •  Please don't start unnecessary and rude arguments with other members and staff. 
### __**7. No Spam**__
 • We have channels designed specifically for bot and emote/sticker/GIF spamming, hence refrain from spamming in the main channels.
### __**8. No Leaks**__
    • Leaking unreleased music is very disrespectful towards artists, regardless of their popularity.
    • Sharing or discussing leaks in the server will result in a timeout for an indefinite period of time.
### __**9. No Mini Modding**__

If you see someone breaking the rules, ping the mods. Don't try to do the mods jobs.

The Moderation Team consists of:

<@&1249463157433307217> 
Kat <@1154767280585048175> , she/they
Fiya <@429245257662595084> , they/she
Gioia <@754425993917104231> , she/her

<@&1249471651792294059> 
Milà <@816607757276020746> , she/her
Ashley <@992128363474997279> , she/her
Star <@920312727870783528> , they/fae

If you notice mini modding taking place in the server, please report it to a team member.
### __**10. No Impersonating**__
 • Impersonating fellow server members, celebrities, bots, the Moderation Team or Teya herself; with the intention of misleading and manipulating others, is prohibited.
 • Although Teya is part of the server and is well recognizable, do not impersonate her. Be your authentic self.
 • Punishment is decided based on the severity of the situation.
### __**11. No Sensitive/Confidential Information**__
 • Sharing confidential information is strictly prohibited. As well as leaks, do not post sensitive information about fellow server members, people you know in real life, celebrities, companies or Teya (mp3 audio files etc.).
 • Punishment is decided based on the severity of the situation.
### __**12. Open Ticket/Ping Team**__
 • The Moderation Team is here to listen to your concerns and help you find the best solution.

 • If you notice a server member breaking the aforementioned rules, please inform the Moderators.

**When a Moderator is online: reply to the message where a rule is being infringed, ping that staff member, mention the rule that's been broken in keywords

Example: <@754425993917104231> gif spamming

When no Moderators are online: ping <@&1253431093936390368> , explain the reason of the ping in keywords

Example: <@&1253431093936390368> NSFW content**

 • If you would prefer speaking to a Moderator in total privacy, please press the red button in <#1250149651550568478> , or contact the staff member you're closest with through Direct Messages.
### __**13. Speak English**__
 • Please refrain from speaking any language that isn't english so everyone can understand each other. Our staff will not be able to moderate in other languages.
### ↳ breaking any rules results in a warning / ban
    """

    embed = discord.Embed(
        title="( server rules ) : ❤️",
        description=description,
        color=0xFF5733
    )

    embed.set_footer(text="please confirm you ' ve read the rules via the button below <3")

    image_url = "https://your-image-url.com/teya.jpeg"  # Replace with your image URL
    embed.set_image(url=image_url)

    await ctx.send(embed=embed)
    print('Rules sent successfully')


images = [
    ("https://www.w24.at/assets/uploads/230904_w24_teyasalena_tv.jpg", "mischievous ladybug and bee"),
    ("https://www.keymedia.at/wp-content/uploads/2023/01/orf_keymedia_20230131111110-988x608.jpg", "crystal ball leak"),
    ("https://cdns-images.dzcdn.net/images/artist/bcf1549733a988db5dfe8198fc23b516/1900x1900-000000-80-0-0.jpg", "teya behind the scenes at eurovision"),
    ("https://ichef.bbci.co.uk/news/976/cpsprodpb/2A5C/production/_129644801_2023.05.05corinnecumming-ebu-4495_0.jpg", "teya & salena for eurovision 2023"),
]

@bot.command(name='random')
async def random_image(ctx):
    random_image = random.choice(images)

    embed = discord.Embed(
        title='image throwback ˖⁺‧₊⟡₊˚⊹ 🐞',
        description=random_image[1],
        color=0x8B0000
    )
    embed.set_image(url=random_image[0])

    await ctx.send(embed=embed)


lyrics_library = {
    "Oh my God, you're such a good writer": "Oh, it's not me, it's Edgar",
    "There's a ghost in my body and he is a lyricist": "It is Edgar Allan Poe and I think he can't resist",
    "Don't know how he possessed me, but I'm happy that he did": "'Cause this song is feeling special, and is gonna make me rich",
    "Poe, Poe, Poe, Poe, Poe, Poe, Poe": "Edgar Allan, Edgar Allan",
    "Maybe I should call a doctor or an exorcist": "Maybe someone out there knows where Shakespeare is, so I can get a taste",
    "Zero, dot, zero, zero, three": "Give me two years, and your dinner will be free",
    "Oh, mio padre, there's a ghost in my body": "Who the hell is Edgar?",
    "What a good vibe we had a good time": "Yeah feeling so right but now we say",
    "We call it life so we do not cry": "Even if you don't like why now we say",
    "No more calls, we bet it all": "Tears on display",
    "You make us wanna do things we never": "Knew we could do",
    "Today's a new day, memories are to stay": "They won't get ruined when we say",
    "Oh, my God, we should do another song!": "But we already said, 'Bye-bye-bye'",
    "She the baddest, she a savage": "She make the best cookies ever, she no average",
    "There's a saint at the North Pole and it isn't Saint Nick": "Her name is Gertrude and she's got a long list",
    "She says, 'Ho, ho, ho, merry Christmas from the Pole'": "I hope it fucking snows, don't eat the cookie dough",
    "Not a mommy, call her daddy": "Daddy, daddy",
    "You got that sweet talk and honey eyes": "They're looking down, down, down, at me",
    "I have tried to call thousand times": "Just so you would take me back",
    "I've been counting days since you left me": "Every lonely night's been a bad dream",
    "What we got was harder to find than diamonds in the ocean": "So what the fuck, you're ghostin' me now",
    "I dare you to ex me, ex me": "Don't mess with a bad bitch",
    "All your lies are drank like it's shot, my friend": "So you've been creepin', been creepin'",
    "Break my heart, I'll break your head": "bang my friends, I'll shoot you dead",
    "Making grown men cry": "But tell me how irrationally emotional am I",
    "Daddy cannot buy you love": "Trust fund baby you're not getting a hug",
    "Hollywoods calling back": "They got a role for the asshole friend",
}

@bot.event
async def on_message(message):
    global current_lyric

    if current_lyric and message.content.lower() == current_lyric[1].lower():
        embed = discord.Embed(
            title="🎉 Correct! 🎉",
            description="You got it right! You earned 10 coins.",
            color=discord.Color.green()
        )
        await message.channel.send(embed=embed)
        add_coins(message.author, 10)
        current_lyric = None

    await bot.process_commands(message)  

@bot.command(name='play')
async def play_lyrics(ctx):
    global current_lyric
    current_lyric = random.choice(list(lyrics_library.items()))
    
    embed = discord.Embed(
        title="🎶 Finish the Lyric 🎶",
        description=f"Finish the lyric: **{current_lyric[0]}**",
        color=discord.Color.blue()
    )
    
    await ctx.send(embed=embed)

@bot.command(name='answer')
async def reveal_answer(ctx):
    global current_lyric
    if current_lyric:
        embed = discord.Embed(
            title="🔍 Reveal Answer 🔍",
            description=f"The correct lyric was: **{current_lyric[1]}**",
            color=0xFF5733
        )
        current_lyric = None
    else:
        embed = discord.Embed(
            title="❌ No Active Challenge ❌",
            description="There is no active lyric challenge.",
            color=0xFF5733
        )
    
    await ctx.send(embed=embed)

def add_coins(user, amount):
    if user.id not in user_data:
        user_data[user.id] = {'coins': 0, 'inventory': []}
    user_data[user.id]['coins'] += amount

def subtract_coins(user, amount):
    if user.id in user_data and user_data[user.id]['coins'] >= amount:
        user_data[user.id]['coins'] -= amount
        return True
    return False

def get_coins(user):
    return user_data.get(user.id, {}).get('coins', 0)

def add_item_to_inventory(user, item):
    if user.id not in user_data:
        user_data[user.id] = {'coins': 0, 'inventory': []}
    user_data[user.id]['inventory'].append(item)

def get_inventory(user):
    return user_data.get(user.id, {}).get('inventory', [])

@bot.command(name='coins')
async def coins(ctx):
    coins = get_coins(ctx.author)
    await ctx.send(f'You have {coins} coins.')


shop_items = {
    'badge1': 50,
    'badge2': 100,
}

@bot.command(name='buy')
async def buy(ctx, item):
    if item in shop_items:
        if subtract_coins(ctx.author, shop_items[item]):
            add_item_to_inventory(ctx.author, item)
            await ctx.send(f'You have purchased {item}!')
        else:
            await ctx.send('You do not have enough coins.')
    else:
        await ctx.send('Item not found.')


@bot.command(name='inventory')
async def inventory(ctx):
    inventory = get_inventory(ctx.author)
    if inventory:
        await ctx.send(f'Your inventory: {", ".join(inventory)}')
    else:
        await ctx.send('Your inventory is empty.')




## TEYA LINKS

@bot.command()
async def send_links(ctx):
    description = """
**Spotify**
https://open.spotify.com/artist/3o9SkahUjtGQ6U9IU0BjhI?si=76Z_4LP4QZOfXtipavpJCQ

**Instagram**
https://www.instagram.com/whothehellisteya?igsh=MWpqdDd1cHBpN2t4aA==

**YouTube**
https://youtube.com/@whothehellisteya?si=kOPTjx79JfNi_5z7

**TikTok**
https://www.tiktok.com/@whothehellisteya?_t=8npUPK1EKpM&_r=1

**Twitter/X**
https://x.com/wthisteya?t=4BQxV-V9reBW60GOSg55Og&s=09
    """

    embed = discord.Embed(
        title="( TEYA's Socials ) : ❤️",
        description=description,
        color=0xFF5733
    )

    await ctx.send(embed=embed)
    print('Links sent successfully')

bot.run(os.getenv('DISCORD_TOKEN'))
