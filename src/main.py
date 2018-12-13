import discord
import yaml

# mainクラス
class Main(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))
    
    # yamlをloadするメソッド
    def load_yaml(self):
        f = open('./../data/data.yml', 'r')
        data = yaml.load(f)
        f.close()

        self.token = data['token']
        self.male = data['male_profile']
        self.female = data['female_profile']
        self.LGBTQ = data['LGBTQ_profile']
    
    async def on_message(self, message):
        if (message.channel.id == self.male):
            print(message.author.name + 'に男性役職を付与')
            male = discord.Role('@男性')
            await message.author.add_roles(male)

        if (message.channel.id == self.female):
            print(message.author.name + 'に女性役職を付与')

    # コンストラクタ
    def __init__(self):
        super().__init__()
        self.load_yaml()

bot = Main()

bot.run(bot.token)