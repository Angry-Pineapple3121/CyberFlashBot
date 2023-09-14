import discord
import random

from discord.ext import commands

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
        
        await ctx.respond(f'which chromebook is this?\n{image_link}\n\nchoices:\n1. {answers[0]}\n2. {answers[1]}\n3. {answers[2]}\n4. {answers[3]}')
        
def setup(bot):
    bot.add_cog(Quiz(bot))