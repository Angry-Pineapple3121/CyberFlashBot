import datetime
import discord
import random

from discord.ext import commands
from discord.commands import Option

# Define all of our chromebook models
MODELS = {
    "DELL 3110": "https://cdn.discordapp.com/attachments/704479038970003570/1151974773837004850/IMG_3699.jpg",
    "DELL 3100": "https://cdn.discordapp.com/attachments/704479038970003570/1151974799325802536/IMG_3700.jpg",
    "HP G8 EE": "https://cdn.discordapp.com/attachments/704479038970003570/1151974982054854707/IMG_3706.jpg",
    "HP G7 EE": "https://cdn.discordapp.com/attachments/704479038970003570/1151975090444046427/IMG_3704.jpg",
    "HP G6 EE": "https://cdn.discordapp.com/attachments/704479038970003570/1151975289539268748/IMG_3703.jpg",
    "HP G5 EE": "https://cdn.discordapp.com/attachments/704479038970003570/1151975623183577148/IMG_3705.jpg",
    "HP G5 11A": "https://cdn.discordapp.com/attachments/704479038970003570/1151975775197741116/IMG_3701.jpg",
    "HP G4 EE": "https://cdn.discordapp.com/attachments/704479038970003570/1151975946111418468/IMG_3702.jpg",
}

class RoleButton(discord.ui.Button):
    def __init__(self, choice, correct_choice):
        """A button for one role. `custom_id` is needed for persistent views."""
        super().__init__(
            label=choice,
            style=discord.ButtonStyle.primary,
            custom_id=choice  # Set a unique custom_id for each button
        )

        self.user_choice = choice
        self.correct_choice = correct_choice
    
    async def callback(self, interaction: discord.Interaction):
        if self.user_choice == self.correct_choice:
            print(f'userChoice: {self.user_choice}')
            print(f'correctChoice: {self.correct_choice}')
            await interaction.response.send_message(f"Correct!", ephemeral=True)
        else:
            print(f'userChoice: {self.user_choice}')
            print(f'correctChoice: {self.correct_choice}')
            await interaction.response.send_message(f"Incorrect!", ephemeral=True)


class Quiz(commands.Cog):
    print("==> Cog Loaded: Quiz")
    def __init__(self, bot):
        self.bot = bot

    @discord.slash_command()
    async def quiz(self, ctx):
        """Quiz yourself on the different models of Chromebooks!"""

        # Select our random model
        selected_model = random.choice(list(MODELS.keys()))
        # Get the link for the selected model to display to user
        image_link = MODELS[selected_model]
        # Create a list with all the model names
        all_models = list(MODELS.keys())
        # Remove the correct answer from the list
        all_models.remove(selected_model)
        # Select three random incorrect answers
        incorrect_answers = random.sample(all_models, 3)
        # Combine correct and incorrect answers
        answers = [selected_model] + incorrect_answers
        # Shuffle the answers
        random.shuffle(answers)

        # Create the embed
        embed = discord.Embed(
            title=f"<:slash:1150933397179486339> Cyber Flash Chromebook Quiz",
            description=f'What is the **model** of the Chromebook shown below?',
            color=discord.Colour.blurple(),
        )
        # Add the time the user is taking the quiz
        now = datetime.datetime.now()
        rtime = now.strftime("%B %d, %Y, %H:%M")
        embed.set_footer(text=f"Requested by {ctx.author.display_name} » {rtime}")
        # Set the image to the image being used for the quiz
        embed.set_image(url=image_link)

        view = discord.ui.View(timeout=None)

        for answer in answers:
            view.add_item(RoleButton(answer, selected_model))
            print(f'added {answer} to view (correct answer: {selected_model})')

        await ctx.respond(embed=embed, view=view)

def setup(bot):
    bot.add_cog(Quiz(bot))
