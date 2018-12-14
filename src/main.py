import discord
import yaml
import os

# main class
class Main(discord.Client):
    # ready Log
    async def on_ready(self):
        print('activate')
    
    # load yaml method
    def load_yaml(self):
        f = open(os.path.dirname(os.path.abspath('__file__')) +'/data/data.yml', 'r')
        data = yaml.load(f)
        f.close()

        self.token = data['token']
        self.male = data['male_profile']
        self.female = data['female_profile']
        self.LGBTQ = data['LGBTQ_profile']
    
    async def on_message(self, message):

        # male prof
        if (message.channel.id == self.male):

            # log
            print(message.author.name + ' add_male')

            male_role = discord.utils.find(lambda role: role.name == '男性', message.guild.roles)
            await message.author.add_roles(male_role)

        #  female prof
        if (message.channel.id == self.female):
            #log
            print(message.author.name + ' add_female')

            female_role = discord.utils.find(lambda role: role.name == '女性', message.guild.roles)
            await message.author.add_roles(female_role)
        
        # LGBTQ prof
        if (message.channel.id == self.LGBTQ):

            # log
            print(message.author.name + ' add_lgbtq')

            lgbtq_role = discord.utils.find(lambda role: role.name == 'LGBTQ', message.guild.roles)
            await message.author.add_roles(lgbtq_role)

    # constructor
    def __init__(self):
        super().__init__()
        self.load_yaml()

bot = Main()

bot.run(bot.token)