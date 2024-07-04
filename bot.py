import discord
from discord.ext import commands
import random
from discord.ui import Button, View

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

# Bot ready event
@bot.event
async def on_ready():
    print(f'Bot is ready. Logged in as {bot.user}')

class RulesView(View):
    @discord.ui.button(label="confirm 🐞", style=discord.ButtonStyle.secondary)
    async def confirm_button_callback(self, interaction: discord.Interaction, button: Button):
        # Assign role to the user
        guild = interaction.guild
        role = guild.get_role(RULES_CONFIRMED_ROLE_ID)
        if role:
            await interaction.user.add_roles(role)
            await interaction.response.send_message("thank you for confirming! you now have full access to the server <3", ephemeral=True)
        else:
            await interaction.response.send_message("something went wrong. please open a ticket.", ephemeral=True)

    @discord.ui.button(label="open a ticket ✮⋆˙", style=discord.ButtonStyle.danger)
    async def decline_button_callback(self, interaction: discord.Interaction, button: Button):
        # Create an actionable link that users can click to open a ticket
        open_ticket_link = f"https://discord.com/channels/{GUILD_ID}/{OPEN_TICKET_CHANNEL_ID}"
        await interaction.response.send_message(
            f"open a ticket in <#{OPEN_TICKET_CHANNEL_ID}> channel: [Click here to open a ticket]({open_ticket_link})",
            ephemeral=True
        )

@bot.event
async def on_voice_state_update(member, before, after):
    if before.channel != after.channel and after.channel and after.channel.id == STAFF_EMERGENCY_VC_ID:
        guild = bot.get_guild(GUILD_ID)
        role = guild.get_role(SPECIAL_ROLE_ID)
        if role:
            text_channel = guild.get_channel(TEXT_CHANNEL_ID)
            if text_channel:
                await text_channel.send(f'{role.mention} {member.name} has commenced a Staff Emergency Meeting! Join in <#1250140892497444929>.')

# Command to send server rules
@bot.command()
async def send_rules(ctx):
    print('send_rules command received')

    description = """
### __**1. Discord TOS (13+)**__
  •  https://discord.com/terms 
  •  https://discord.com/guidelines
  •  Make sure you comply with Discords TOS. This includes only ages 13+ allowed as well as no 'alt' accounts allowed.
### __**2. Respect Regular Members**__
  •  Stay respectful to all members in the server. We want this server to be a comfortable space for everybody.
  •  Do not discriminate against someone or harrass them.
  •  This rule extends to DMs.
### __**3. Respect Teya**__
  •  Any disrespect towards Teya is not allowed.
  •  This includes rude comments, speculating on her personal life, sexualisation of her, constant bothering or harrasing her.
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
        title="( server  rules ) : ❤️",
        description=description,
        color=0xFF5733
    )

    embed.set_footer(text="please  confirm  you ' ve  read  the  rules  via  the  button below <3")

    # Adding an image from a local file
    file_path = "C:/Projects/Discord/teya.jpeg"  # Update the path to your image file
    try:
        file = discord.File(file_path, filename="teya.jpeg")
        embed.set_image(url="attachment://teya.jpeg")
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        await ctx.send("Failed to send rules due to missing image file.")
        return

    view = RulesView()
    await ctx.send(file=file, embed=embed, view=view)
    print('Rules sent successfully')

# Array of tuples containing image URLs and captions
images = [
    ("C:/Projects/Discord/IMG_6845.jpeg", "grandma  teya"),
    ("C:/Projects/Discord/IMG_6847.jpeg", "teya  &  salena  for  the  bye  bye  bye  music  video"),
    ("C:/Projects/Discord/IMG_6855.jpeg", "mischievous  ladybug  and  bee"),
    ("C:/Projects/Discord/IMG_6846.jpeg", "ladybug  teya"),
    ("C:/Projects/Discord/IMG_6854.jpeg", "teya  and  salena  🩷"),
    ("C:/Projects/Discord/70490BD3-F194-4C17-934D-E5DA732E0F2C_v0_h.jpg", "crystal  ball  leak"),
    ("C:/Projects/Discord/22827-Teya&Salena_IMG_9007.jpg", "bug  duo"),
    ("C:/Projects/Discord/1900x1900-000000-80-0-0.jpg", "teya  behind  the  scenes  at  eurovision"),
    ("C:/Projects/Discord/_129644801_2023.05.05corinnecumming-ebu-4495_0.jpg", "teya  &  salena  for  eurovision  2023"),
    # Add more images as needed
]

@bot.command(name='random')
async def random_image(ctx):
    print('random command received')

    random_image = random.choice(images)

    embed = discord.Embed(
        title='image  throwback  ˖⁺‧₊⟡₊˚⊹ 🐞',
        description=random_image[1],
        color=0x8B0000
    )

    try:
        file = discord.File(random_image[0], filename="random_image.jpeg")
        embed.set_image(url="attachment://random_image.jpeg")
    except FileNotFoundError:
        print(f"File not found: {random_image[0]}")
        await ctx.send("Failed to send random image due to missing file.")
        return

    # Send the embedded message
    try:
        await ctx.send(file=file, embed=embed)
    except Exception as e:
        print(f'Error sending message: {e}')

# Replace 'your_bot_token' with your actual bot token
bot.run('MTI0MDc1ODI0MjAwNzU4MDc4NA.GY5h1R.FyOjUMxNzZZSeq4zJuIsbweRFzOd8ttZPqOqBg')
