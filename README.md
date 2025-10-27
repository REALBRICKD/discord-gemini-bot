# Gemini-Powered Discord Bot
This project utilizes the [discord.py](https://github.com/Rapptz/discord.py) library to host a bot either locally, or through a platform like AWS. The AI-related features are powered by Google Gemini's free API.\
A database has been integrated through [sqlite](https://github.com/sqlite/sqlite), which at present stores message history of both the bot and user, and links these interactions to user ID.\
It includes a few commands:
* /help - Displays a comprehensive list of every command that can be run by the bot, including descriptions of each command.
  Example usage of the /help command.
<img width="1384" height="708" alt="help_usage" src="https://github.com/user-attachments/assets/71144391-b4df-40af-be2d-a9a548dd6ed2" />
<br>

* /chat - Allows users to converse directly with the gemini API. Any messages and responses are saved in the database to enable continuous conversation - multiple can even take place concurrently.
  Example usage of the /chat command.
<img width="1874" height="1157" alt="chat_test" src="https://github.com/user-attachments/assets/35f7668c-815b-40c1-a16f-e8dac75a81c3" />
<br>

* /purgemessagehistory - Erases all message history of the user. Any messages and bot responses linked to their ID will be removed from the database.
<br>

* /warframefarm - uses a specially engineered prompt to search the official warframe droptables. This allows quick and accessible access to official data and information.
<br>
<img width="1879" height="725" alt="Warframefarm_Test" src="https://github.com/user-attachments/assets/4045d2f1-90d2-4c5c-a415-6886eac823f7" />
<br>

# Production and Design
The project contains a database client that performs operations regarding the bot's database. It also has a collection of cogs (think of them as commands) to load and then run when called. \
Though not as commonly done, this was a deliberate choice on my part, as it allows the bot to be easily expanded...

# Roadmap
There is ample room for expansion. Some upcoming features include (but are certainly not limited to):
* A points system to drive participation on the server the bot is hosted in
* Integrating multiple AI-powered API's such as grok and deepseek to perform other specialized commands (refer to [AI API Comparison](https://github.com/REALBRICKD/AiAPIComparison) for more details)
* An editable to-do list corresponding to a user (thank you Emi for requesting this one!)
  
# Running The Program
This program cannot be run, as it requires secure information stored in the .env file. Bots written with discord.py are linked to their owners' account tokens, which can leave accounts vulnerable if shared. If this were not the case, simply cloning the repo allows the program to be run in any IDE that supports python.

# Credits
Thank you to discord for allowing such accessible development of bots on their platform, and to my friends for testing the commands. Another massive thanks to google for allowing access to one of the top free AI APIs at the moment!
