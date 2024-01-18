# HashBot for Discord

HashBot is a custom Discord bot designed to interact with the Pwnagotchi network auditing tool, enhancing the functionality of the DiscoHash plugin. It allows users to request and receive network hash information directly through Discord commands.

### Acknowledgments

- This bot is an extension of the work done by [@flamebarke](https://github.com/flamebarke), particularly building upon the Main DiscoHash plugin in their repository.
- The `hashbot.py` code is derived from [@flamebarke's](https://github.com/flamebarke) repository and aims to elaborate on and simplify the DiscoHash plugin's capabilities.

### Features

- **Hash Retrieval**: Users can request hashes for a specified number of access points through Discord.
- **Command Interaction**: Easy-to-use Discord commands
- **Seamless Integration**: Works alongside the Pwnagotchi's DiscoHash plugin.

### Prerequisites
1. **Pwnagotchi**
   - [DiscoHash](https://github.com/flamebarke/DiscoHash/tree/main) plugin for pwnagotchi installed and running.
  
2. **Local Computer**
   - [Python 3.6 or later.](https://www.python.org/downloads/)
      - Check your python version:
        ```bash
        python3 --version
   - `discord.py` library.
   - `python-dotenv` library for managing environment variables.

## 1. Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/SoFarSoGrant/Hashbot.git

2. **Navigate to the Repository Directory**:
   ```bash
   cd Hashbot-main

3. **Install Required Libraries** (This will install the the latest Discord.py and python-dotenv libraries.):
   ```bash
   pip3 install -r requirements.txt

## 2. Setting Up Discord Bot

1. **Turn on "Developer Mode" in your Server (this will be needed for later)**
   - Right click on your server and choose "Server Settings"
   - Go to the "Advanced" tab and toggle on the "Developer Mode" <br />
   <br />

  ![It will look like this](https://cdn.discordapp.com/attachments/1197390386130337852/1197399757681860729/Screenshot_2024-01-17_at_9.28.08_PM.png?ex=65bb206c&is=65a8ab6c&hm=ee4e41533115abfb1cdd04adc7003940bb68647f778df044b1a5a8eed5af72a9&)
<br />

2. **Create a Discord Bot**:
   - Visit the [Discord Developer Portal.](https://discord.com/developers/applications)
   - Click "New Application", give it a name (anything you want), and create your app.
      - I named mine 'wirecat' because why not.
   - Go to the "Bot" tab and click "Add Bot".

> [!WARNING]
> This next step is important, so pay attention!


3. **Get Your Bot Token**:
   - Under the "Bot" tab, find the "Token" and click "Copy" to get your bot's token. ***(Don't lose this, or you'll have to reset it and create a new one!)***
   - Paste your Token in a text editor for now.

4. **Remember Turning on Developer Mode?**
   - Go to the "Bot" tab and turn on all of the "Privileged Gateways Intents"<br />
      - These options aren't available if not in Developer Mode.

     ![Right here](https://media.discordapp.net/attachments/1197390386130337852/1197401386007146496/Screenshot_2024-01-17_at_10.44.09_PM.png?ex=65bb21f1&is=65a8acf1&hm=05b4076f13fdad4a2409fb8f51dfceebb35b6ef343872e71717c8484e6cfe9da&=&format=webp&quality=lossless&width=1440&height=476)

5. **Add Bot to Your Discord Server**:
   - Go to the "OAuth2" tab and select "URL Generator"
   - Under "Scopes", select "bot".
   - Select the the permissions for your bot.
   - **These permissions work just fine.** <br />

   
       ![Permissions for your new bot](https://cdn.discordapp.com/attachments/1197390386130337852/1197398452380913764/Screenshot_2024-01-17_at_10.22.39_PM.png?ex=65bb1f35&is=65a8aa35&hm=c74bbf0aa8e207765339c9844e7e9f0ca22b8747abd027c110f5ab92c66431fa&)

   - Copy/paste the generated URL into your address bar 
   - Select your server collecting hashes from [DiscoHash](https://github.com/flamebarke/DiscoHash/tree/main)
   - Click "Authorize"<br />
   
     
  ![You should see something like this](https://discordjs.guide/assets/bot-auth-page.e624796f.png)


### Wham, Bam, Thank you Ma'am! 

**You should now have a shiny new Bot on your server.** 🤖 


# 3. Creating the '.env' File

> [!IMPORTANT]
> This file should be created and saved in the same directory as hashbot.py

### The .env file contains sensitive information like your bot's token. Don't Share it!

***Select the dropdown based on your operating system:***

<details>
<summary><b>Windows:</b></summary>

   - Open Notepad.
   - Add your environment variables:
```
> DISCORD_TOKEN=your_discord_bot_token
> DISCORD_GUILD=your_discord_guild_id
> GUILD_CHANNEL=your_discord_channel_id
```
   - Save the file as .env (Select "All Files" as the file type and name it .env).
</details>
<details>
<summary><b>macOS/Linux:</b></summary>

   - Open Terminal.
   - Navigate to your project directory.

> [!TIP]
> type `cd ` into your terminal and drag your directory into the window to get the path.

   - Run touch .env to create a new file.
  ```
  touch .env
  ```
   - Open it with a text editor and add your environment variables.
```
> DISCORD_TOKEN=your_discord_bot_token
> DISCORD_GUILD=your_discord_guild_id
> GUILD_CHANNEL=your_discord_channel_id
```
> [!NOTE]
> If you don't see the .env file in your finder window press `⌘ + shift + .` to reveal it 
</details>

**Where to find your token & IDs**
   - **DISCORD_TOKEN** = Bot Token
      - See step 2.2 of Setting up your Discord Bot
   - **DISCORD_GUILD** = Server ID
      - Right click on your main server icon and select "Copy Server ID" at the bottom of the dropdown.
   - **GUILD_CHANNEL** = Channel ID
      - Right click on your server channel (the one you invited your bot to) and select "Copy Channel ID" at the bottom of the dropdown.

# 4. Usage: Let's Wake Up the Bot
1. **Make sure your in the project directory**
2. **Run the following in your terminal**
   ```
   python3 hashbot.py
   ```
3. **Voila**
   - If everything is set up properly, your bot should be active in your server.

![The Bot is alive!](https://cdn.discordapp.com/attachments/1197390386130337852/1197423830038224896/wirecat-online.gif?ex=65bb36d8&is=65a8c1d8&hm=0188eb432fc87e6d0823c81b679b78c03b259eb7dad4c7285cf77b99bfe54581&)


# 5. Bot Command
1. Type `/dump` into your Discord channel's messages and your bot will provide you with an hc22000 file ready for cracking
   - The default number of hashes in the file is 100
2. Add a number to the `/dump` command to specify how many of the last hashes the bot should scrape and compile.
   - ex. `/dump 5` will provide a .hc22000 file with the last 5 hashes in your channel.

# Acknowledgments
Special thanks to the Pwnagotchi project. I never would've figured this out if I didn't have you 😘
Most special thanks to @v0yager for creating DiscoHash and this Hat tip to anyone whose code was used.


### Notes:

- **Customization**: Customize the URL in the `git clone` command with your actual GitHub repository URL.
- **Additional Documentation**: If you have contributing guidelines or a license file, link them in the `README.md`. If not, you might want to create these files.
- **Functionality Details**: Add or modify any specific instructions or features related to your version of HashBot.
- **Markdown Formatting**: This is formatted in Markdown, which is standard for `README.md` files on GitHub. You can further enhance it with additional Markdown formatting as needed.

This `README.md` provides a basic structure that you can expand upon based on the specifics of your project and its deployment.
