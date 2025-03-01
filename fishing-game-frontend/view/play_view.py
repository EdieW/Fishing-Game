import discord

class View(discord.ui.View):
    def __init__(self, session):
        super().__init__()
        self.add_item(ReturnButton(session))


class ReturnButton(discord.ui.Button):
    def __init__(self, session):
        super().__init__(label="", style=discord.ButtonStyle.grey, custom_id="")
        self.session = session

    async def callback(self, interaction: discord.Interaction):
        # 这里可以添加返回的逻辑
        pass