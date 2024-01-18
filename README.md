# HashBot for Discord

HashBot is a custom Discord bot designed to interact with the Pwnagotchi network auditing tool, enhancing the functionality of the DiscoHash plugin. It allows users to request and receive network hash information directly through Discord commands.

### Acknowledgments

- This bot is an extension of the work done by [@flamebarke](https://github.com/flamebarke), particularly building upon the Main DiscoHash plugin in their repository.
- The `hashbot.py` code is derived from [@flamebarke's](https://github.com/flamebarke) repository and aims to augment the DiscoHash plugin's capabilities.

### Features

- **Hash Retrieval**: Users can request hashes for a specified number of access points through Discord.
- **Command Interaction**: Easy-to-use Discord commands to interact with Pwnagotchi.
- **Seamless Integration**: Works alongside the Pwnagotchi's DiscoHash plugin. 

## 1. Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/hashbot.git

2. **Navigate to the Repository Directory**:
   ```bash
   cd hashbot

3. **Install Required Libraries**:
   ```bash
   # This will install the the latest Discord and python-dotenv libraries.
   pip install -r requirements.txt

## 2. Setting Up Discord Bot

1. **Create a Discord Bot**:
- Visit the [Discord Developer Portal.](https://discord.com/developers/applications)
- Click "New Application", give it a name, and create your app.
- Go to the "Bot" tab and click "Add Bot".

![***This next part is important, so pay attention!***](https://media.discordapp.net/attachments/1197390386130337852/1197390426815070299/Screenshot_2024-01-17_at_9.38.16_PM.png?ex=65bb17bc&is=65a8a2bc&hm=9f0cb87b1457b32ba92850c120bbcb9529a6cd9ade602e6c3fbb0752a06a53ec&=&format=webp&quality=lossless)

2. **Get Your Bot Token**:
- Under the "Bot" tab, find the "Token" section and click "Copy" to get your bot's token. ***(Don't lose this, or you'll have to reset it and create a new one!)***
- Paste your Token in a text editor for now.

3. **Add Bot to Your Discord Server**:
- Go to the "OAuth2" tab.
- Under "Scopes", select "bot".
- Select the the permissions for your bot.
  **These permissions work just fine.**
  ![Permissions for your new bot](https://cdn.discordapp.com/attachments/1197390386130337852/1197392528073306193/Screenshot_2024-01-17_at_10.10.05_PM.png?ex=65bb19b1&is=65a8a4b1&hm=6aa08beb71be296b788b1abc1354c23ebc1b1deb666d989d8e7daf38e1c18673&)
- Use the generated URL to add the bot to your Discord server.


# <summary><b>Creating the '.env' File</b></summary>

### The .env file contains sensitive information like your bot's token. Follow these instructions based on your operating system:

### Windows:

- Open Notepad.
- Add your environment variables:
```
> DISCORD_TOKEN=your_discord_bot_token
> DISCORD_GUILD=your_discord_guild_id
> GUILD_CHANNEL=your_discord_channel_id
```


   </details>
____________________

# HashBot for Discord

HashBot is a custom Discord bot designed to interact with the Pwnagotchi network auditing tool, enhancing the functionality of the DiscoHash plugin. It allows users to request and receive network hash information directly through Discord commands.

## Acknowledgments

- This bot is an extension of the work done by @flamebarke, particularly building upon the Main DiscoHash plugin in their repository.
- The `hashbot.py` code is derived from @flamebarke's repository and aims to augment the DiscoHash plugin's capabilities.

  
## Features

- **Hash Retrieval**: Users can request hashes for a specified number of access points.
- **Command Interaction**: Interact with the bot using simple Discord commands.
- **Seamless Integration**: Designed to work with Pwnagotchi's custom plugin system.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine or server for development and testing purposes.

### Prerequisites

- Python 3.6 or later
- `discord.py` library
- `python-dotenv` library for environment variable management

### Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/hashbot.git

### Navigate to the Repository Directory:

cd hashbot

### Install Required Libraries:

pip install -r requirements.txt

## Setting Up Discord Bot

### Create a Discord Bot:
- Visit the Discord Developer Portal.
- Click "New Application", give it a name, and create your app.
- Go to the "Bot" tab and click "Add Bot".


### Set Up .env File:
Create a .env file in the root directory.
Add your Discord Bot Token, Guild ID, and Channel ID:

DISCORD_TOKEN=your_discord_bot_token
DISCORD_GUILD=your_discord_guild_id
GUILD_CHANNEL=your_discord_channel_id


## Usage
To run the bot, use the following command in the root directory of hashbot.py and the .env file:

python3 hashbot.py


Bot Commands
/dump [NUMBER]: Retrieves the specified number of hashes from Pwnagotchi and sends them in a text file.

# Acknowledgments
Special thanks to the Pwnagotchi project. I never would've figured this out if I didn't have you 😘
Most special thanks to @v0yager for creating DiscoHash and this Hat tip to anyone whose code was used.


### Notes:

- **Customization**: Customize the URL in the `git clone` command with your actual GitHub repository URL.
- **Additional Documentation**: If you have contributing guidelines or a license file, link them in the `README.md`. If not, you might want to create these files.
- **Functionality Details**: Add or modify any specific instructions or features related to your version of HashBot.
- **Markdown Formatting**: This is formatted in Markdown, which is standard for `README.md` files on GitHub. You can further enhance it with additional Markdown formatting as needed.

This `README.md` provides a basic structure that you can expand upon based on the specifics of your project and its deployment.
