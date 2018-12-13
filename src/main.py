import discord
import yaml

# mainクラス
class Main(discord.Client):
    # 実行待機状態のLog
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
    
    # メッセージを監視するメソッド
    async def on_message(self, message):

        # 男性プロフィールの場合
        if (message.channel.id == self.male):

            # log
            print(message.author.name + 'に男性役職を付与')

            male_role = discord.utils.find(lambda role: role.name == '男性', message.guild.roles)
            await message.author.add_roles(male_role)

        # 女性プロフィールの場合
        if (message.channel.id == self.female):
            #log
            print(message.author.name + 'に女性役職を付与')

            female_role = discord.utils.find(lambda role: role.name == '女性', message.guild.roles)
            await message.author.add_roles(female_role)
        
        # LGBTQプロフィールの場合
        if (message.channel.id == self.LGBTQ):

            # log
            print(message.author.name + 'にLGBTQ役職を付与')

            lgbtq_role = discord.utils.find(lambda role: role.name == 'LGBTQ', message.guild.roles)
            await message.author.add_roles(lgbtq_role)

    # コンストラクタ
    def __init__(self):
        super().__init__()
        self.load_yaml()

bot = Main()

bot.run(bot.token)