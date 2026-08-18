import discord
from discord.ext import commands
import random
import string
from datetime import datetime
import asyncio
import os  # ← TREBUIE SĂ FIE ASTA!
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

# =====================================================
# CONFIGURARE CANAL DESTINAȚIE
# =====================================================

TARGET_CHANNEL_ID = 1464391763996315718  # AICI PUI ID-UL CANALULUI

# =====================================================
# ORDER TYPES ȘI PRICES (DIN POZE)
# =====================================================

ORDER_PRICES = {
    "King Frank Method": "10€",
    "BOT LOBBY method": "15€",
    "Brawl Pass & Pro Pass method": "15€",
    "Infinite Winstreak method": "10€",
    "Creator ICON": "50€",
    "Brawl Stars Cheat (Monthly)": "10€",
    "Brawl Stars Cheat (Lifetime)": "20€",
    "Matcherino method": "35€",
    "Rare Pin": "100€",
    "Free Gems method": "15€",
    "Creator Spray": "50€",
    "Cheap Brawl Pass": "4€",
    "Cheap Brawl Pass Plus": "7€",
    "Pro Ranked": "20€",
    "Unban Acc method": "15€",
    "Age Verification method": "15€",
    "Steal Acc method": "15€",
    "Free Rewards": "10€",
    "Activity Rewards": "10€",
    "Events": "10€",
    "Free Cheat": "10€",
    "Ranked Boost": "30€",
    "Win Streak": "20€",
    "Prestige Carry": "40€",
    "Free Brawl Pass": "10€",
    "Matcherino Pins": "35€",
    "Unmute Chat": "10€",
    "Buy Account": "30€",
    "Pro Pass": "15€",
    "Brawl Pass": "4€",
}

# =====================================================
# LISTE SEPARATE PENTRU COMENZI
# =====================================================

ORDER_TYPES = list(ORDER_PRICES.keys())
PRICES = list(ORDER_PRICES.values())

# =====================================================
# 100 REVIEW-URI PENTRU PRODUSE
# =====================================================

PRODUCT_REVIEWS = [
    "Got free gems, works perfectly",
    "Free gems method is legit, got 5k",
    "Best free gems service, fast delivery",
    "Free gems worked, got gems in 2 hours",
    "Got all creator sprays, amazing",
    "Creator spray method works perfectly",
    "All creator sprays unlocked, great service",
    "Got every creator spray in the game",
    "Got Brawl Pass for half price, great deal",
    "Cheap Brawl Pass works perfectly, got it fast",
    "Best cheap Brawl Pass method",
    "Brawl Pass for cheap, 100% legit",
    "Pro rank method got me to Masters",
    "Best pro rank method, worked in 2 days",
    "Got pro rank fast, great method",
    "Reached pro rank using this method",
    "Got my account unbanned in 1 day",
    "Unban method works perfectly, got account back",
    "Best unban service, got my account fast",
    "Account unbanned, great service",
    "Got my chat unmuted, works great",
    "Unmute method works perfectly, can chat now",
    "Best unmute service, got chat back fast",
    "Got my chat back, great service",
    "Got a stacked account using this method",
    "Best method for accounts, works great",
    "Got an amazing account using this method",
    "Account method is legit, got a good account",
    "Bought an account, got it in 1 hour",
    "Best place to buy accounts, very fast",
    "Bought a stacked account, everything works",
    "Account buying service is amazing",
    "Ranked boost got me to Legendary",
    "Best ranked service, fast and reliable",
    "Got to Masters rank, great service",
    "Ranked boost works perfectly",
    "Got 100 win streak, amazing service",
    "Win streak method works perfectly",
    "Best win streak service, got 50 wins",
    "Infinite win streak, works great",
    "Prestige carry got me to Prestige 3",
    "Best prestige service, fast and reliable",
    "Got Prestige 3 in 1 day, great service",
    "Prestige boost works perfectly",
    "Free cheat works perfectly, got gems",
    "Best free cheat method, got free rewards",
    "Free cheat is legit, works great",
    "Matcherino codes worked, got free gems",
    "Best Matcherino method, got rewards fast",
    "Matcherino service is legit, works great",
    "Got free Brawl Pass, works perfectly",
    "Free Brawl Pass method is legit",
    "Best free Brawl Pass service",
    "Infinite winstreak method works, got 50 wins",
    "Best infinite winstreak service",
    "Got infinite winstreak",
    "Got creator icon, works perfectly",
    "Creator icon method is legit, got it fast",
    "Best creator icon service",
    "Free rewards are amazing, got gems",
    "Got free gems and pass from drops",
    "Activities give great rewards",
    "Events are amazing, got free stuff",
    "Got all ranked rewards",
    "Ranked carry was super fast",
    "Best ranked boosting service",
    "Win streak boost is legit",
    "Got 200 win streak, highly recommend",
    "Prestige carry is amazing",
    "Got Prestige 2 in 1 day",
    "Free gems method is the best",
    "Creator spray service is great",
    "Cheap Brawl Pass saved me money",
    "Pro rank method is 100% legit",
    "Unban service restored my account",
    "Unmute chat service works fast",
    "Account method got me a stacked acc",
    "Best place to buy accounts",
    "Ranked boost is the best service",
    "Win streak method works every time",
    "Prestige boost is reliable and fast",
    "Free cheat service is amazing",
    "Matcherino codes are the best",
    "Free Brawl Pass is legit",
    "Infinite winstreak method works perfectly",
    "Creator icon service is great",
    "Best service for free rewards",
    "Ranked boost got me to Legendary fast",
    "Win streak service is incredible",
    "Prestige carry is the best",
    "Free gems method works every time",
    "Creator spray service is reliable",
    "Cheap Brawl Pass is a great deal",
    "Pro rank method got me to Masters fast",
    "Unban service is 100% legit",
    "Unmute chat service works perfectly",
    "Account method is amazing",
    "Buy accs service is the best",
    "Ranked service is fast and reliable",
    "Win streak boost is amazing",
    "Prestige service is great",
]

# =====================================================
# 200 REVIEW-URI GENERALE
# =====================================================

GENERAL_REVIEWS = [
    "Amazing service, highly recommend",
    "Fast and reliable, 10/10",
    "Great service, will order again",
    "Very professional and fast",
    "Best service I've ever used",
    "Super fast delivery, very happy",
    "Trusted service, 100% legit",
    "Excellent work, very satisfied",
    "Great communication and fast service",
    "Very reliable and trustworthy",
    "Perfect service, nothing to complain",
    "Great value for money",
    "Super fast and professional",
    "Highly recommend to everyone",
    "Amazing experience, thank you",
    "Very efficient and quick",
    "Top quality service",
    "Very responsive and helpful",
    "Professional and courteous",
    "Absolutely flawless service",
    "Exceeded all my expectations",
    "Definitely coming back for more",
    "One of the best services I've used",
    "Incredibly fast and efficient",
    "Very impressed with the quality",
    "Outstanding work",
    "Fantastic service from start to finish",
    "Couldn't ask for better service",
    "Superb quality and speed",
    "Excellent communication throughout",
    "Highly skilled and efficient",
    "Great attention to detail",
    "Amazing results, very happy",
    "Very pleased with everything",
    "Exceptional quality service",
    "Very smooth process",
    "Awesome service, highly recommend",
    "Really good service, will use again",
    "Excellent job, very professional",
    "Great communication and service",
    "Very helpful and friendly service",
    "Top quality, very impressed",
    "Great experience, will use again",
    "Very reliable and fast",
    "Awesome job, very happy",
    "Super friendly and helpful",
    "Great quality, fast delivery",
    "Very impressed with the service",
    "Excellent value for money",
    "Great team, very professional",
    "Very satisfied, will come back",
    "Great job, very thorough",
    "Very efficient and professional",
    "Excellent experience, very happy",
    "Top service, highly recommend",
    "Very good work, very fast",
    "Great service, friendly team",
    "Amazing quality, very satisfied",
    "Very professional, great experience",
    "Great value, fast delivery",
    "Very happy with everything",
    "Great service, very reliable",
    "Very pleased with the results",
    "Excellent work, highly skilled",
    "Amazing service, very fast",
    "Very professional and helpful",
    "Great experience, very satisfied",
    "Top quality, amazing service",
    "Very reliable, great work",
    "Excellent, highly recommend",
    "Amazing job, very happy",
    "Great service, very professional",
    "Very fast and high quality",
    "Excellent value, great service",
    "Very happy with everything",
    "Awesome experience, thank you",
    "Great work, very impressed",
    "Very professional and efficient",
    "Excellent service, very satisfied",
    "Amazing quality and speed",
    "Great team, amazing results",
    "Very reliable and fast",
    "Excellent quality, great service",
    "Very impressed with the work",
    "Amazing experience, will come back",
    "Great service, very trustworthy",
    "Very professional, great results",
    "Excellent, amazing service",
    "Very happy, highly recommend",
    "Great value and quality",
    "Amazing service, fast delivery",
    "Very professional and courteous",
    "Excellent work, very satisfied",
    "Great service, very friendly",
    "Very reliable, highly recommend",
    "Amazing results, great team",
    "Very fast and professional",
    "Excellent service, very happy",
    "Great quality, amazing work",
    "Very satisfied, will use again",
    "Awesome service, highly recommend",
    "Very professional, excellent work",
    "Great experience, very fast",
    "Very happy with the quality",
    "Amazing service, great value",
    "Very reliable and efficient",
    "Excellent results, great service",
    "Very professional and skilled",
    "Great work, very trustworthy",
    "Amazing service, very satisfied",
    "Very fast and reliable",
    "Excellent quality, great value",
    "Very happy, amazing service",
    "Great team, very professional",
    "Very good service, highly recommended",
    "Excellent, very impressed",
    "Amazing work, great service",
    "Very professional and fast",
    "Great experience, excellent results",
    "Very satisfied with everything",
    "Awesome, highly recommend",
    "Best service ever, highly recommend",
    "Everything was perfect, thank you",
    "Fast and trustworthy, great job",
    "Very professional and reliable",
    "Amazing work, will use again",
    "Great service, excellent results",
    "Super happy with everything",
    "Very fast service, highly recommend",
    "Professional and quick, great job",
    "Trusted service, amazing results",
    "Great communication and fast delivery",
    "Very reliable, great experience",
    "Excellent service, will use again",
    "Super fast and reliable, great",
    "Very happy with the results",
    "Amazing quality, great prices",
    "Very professional service, recommend",
    "Great work, fast delivery",
    "Trusted and reliable, 10/10",
    "Excellent experience, very satisfied",
    "Super service, amazing quality",
    "Very responsive and professional",
    "Great team, fast results",
    "Amazing work, very happy",
    "Very satisfied, will come back",
    "Great value, amazing service",
    "Professional and efficient, great job",
    "Awesome service, highly recommend",
    "Very reliable, great results",
    "Excellent work, very impressed",
    "Super fast and professional",
    "Great communication, fast service",
    "Very trustworthy, great experience",
    "Amazing results, thank you",
    "Very good work, highly recommend",
    "Fast and reliable, best service",
    "Great experience, will use again",
    "Very professional and fast",
    "Excellent service, amazing results",
    "Super reliable, great team",
    "Very happy with everything",
    "Great work, very satisfied",
    "Awesome experience, recommend",
    "Very fast and reliable service",
    "Great quality, fast delivery",
    "Very impressed with the work",
    "Amazing service, will come back",
    "Very professional, excellent results",
    "Great value for the price",
    "Super fast and trustworthy",
    "Very happy with the outcome",
    "Excellent work, great service",
    "Very reliable and trustworthy",
    "Great service, no complaints",
    "Amazing team, great results",
    "Very fast and professional",
    "Excellent quality, great service",
    "Very satisfied, will recommend",
    "Great experience, highly recommend",
    "Very reliable, amazing work",
    "Super fast, great communication",
    "Very professional, good prices",
    "Amazing results, will use again",
    "Great service, fast delivery",
    "Very happy, thank you",
]

# =====================================================
# COMBINĂ REVIEW-URILE
# =====================================================

ALL_REVIEWS = PRODUCT_REVIEWS + GENERAL_REVIEWS
random.shuffle(ALL_REVIEWS)

# =====================================================
# RATING-URI: 50 cu 3/5, 150 cu 4/5, 200 cu 5/5
# =====================================================

RATINGS = ["3/5"] * 50 + ["4/5"] * 150 + ["5/5"] * 200
random.shuffle(RATINGS)

# =====================================================
# DOAR "Anonymous Customer"
# =====================================================

REVIEW_NAMES = ["Anonymous Customer"]

# =====================================================
# COMENZI - CU ORDER TYPE ȘI PRICE DIN POZE
# =====================================================

@bot.command()
async def review(ctx, rating: str = None, order: str = None, price: str = None, *, message: str = None):
    target_channel = bot.get_channel(TARGET_CHANNEL_ID)
    
    if target_channel is None:
        await ctx.send("❌ Canalul destinație nu a fost găsit! Verifică ID-ul.")
        return
    
    if rating is None:
        rating = random.choice(RATINGS)
    
    if order is None:
        order = random.choice(ORDER_TYPES)
        price = ORDER_PRICES[order]
    
    if price is None:
        price = random.choice(PRICES)
    
    if message is None:
        message = random.choice(ALL_REVIEWS)
    
    # Stele pentru rating
    if rating == "5/5" or rating == "5":
        stars = "⭐⭐⭐⭐⭐"
    elif rating == "4/5" or rating == "4":
        stars = "⭐⭐⭐⭐☆"
    elif rating == "3/5" or rating == "3":
        stars = "⭐⭐⭐☆☆"
    else:
        stars = "⭐⭐⭐⭐⭐"
    
    embed = discord.Embed(
        title="📝 NEW REVIEW - Brawl Services",
        description=f"**Customer**\nAnonymous Customer 🦷",
        color=discord.Color.gold()
    )
    
    embed.add_field(
        name="📦 Order Type",
        value=order,
        inline=False
    )
    
    embed.add_field(
        name="⭐ Rating",
        value=f"{stars}\n**{rating}**",
        inline=False
    )
    
    embed.add_field(
        name="💰 Price",
        value=price,
        inline=False
    )
    
    embed.add_field(
        name="💬 Review",
        value=f"> {message}",
        inline=False
    )
    
    embed.set_footer(text="✅ Verified Review | Brawl Services")
    embed.timestamp = datetime.now()
    
    await target_channel.send(embed=embed)
    await ctx.send(f"✅ Review trimis în {target_channel.mention}!")

@bot.command()
async def reviewrandom(ctx):
    target_channel = bot.get_channel(TARGET_CHANNEL_ID)
    
    if target_channel is None:
        await ctx.send("❌ Canalul destinație nu a fost găsit! Verifică ID-ul.")
        return
    
    rating = random.choice(RATINGS)
    order = random.choice(ORDER_TYPES)
    price = ORDER_PRICES[order]
    message = random.choice(ALL_REVIEWS)
    
    if rating == "5/5" or rating == "5":
        stars = "⭐⭐⭐⭐⭐"
    elif rating == "4/5" or rating == "4":
        stars = "⭐⭐⭐⭐☆"
    elif rating == "3/5" or rating == "3":
        stars = "⭐⭐⭐☆☆"
    else:
        stars = "⭐⭐⭐⭐⭐"
    
    embed = discord.Embed(
        title="📝 NEW REVIEW - Brawl Services",
        description=f"**Customer**\nAnonymous Customer 🦷",
        color=discord.Color.gold()
    )
    
    embed.add_field(
        name="📦 Order Type",
        value=order,
        inline=False
    )
    
    embed.add_field(
        name="⭐ Rating",
        value=f"{stars}\n**{rating}**",
        inline=False
    )
    
    embed.add_field(
        name="💰 Price",
        value=price,
        inline=False
    )
    
    embed.add_field(
        name="💬 Review",
        value=f"> {message}",
        inline=False
    )
    
    embed.set_footer(text="✅ Verified Review | Brawl Services")
    embed.timestamp = datetime.now()
    
    await target_channel.send(embed=embed)
    await ctx.send(f"✅ Review random trimis în {target_channel.mention}!")

# =====================================================
# HELP
# =====================================================

@bot.command()
async def helpreview(ctx):
    embed = discord.Embed(
        title="🤖 Brawl Services - Review Bot",
        description="Generate fake reviews with Order Type and Price!",
        color=discord.Color.blue()
    )
    
    embed.add_field(
        name="!review [rating] [order] [price] [message]",
        value='Example: `!review "5/5" "King Frank Method" "10€" "Great service!"`',
        inline=False
    )
    
    embed.add_field(
        name="!reviewrandom",
        value="Generate a random review with random order and price",
        inline=False
    )
    
    embed.add_field(
        name="!helpreview",
        value="Show this help message",
        inline=False
    )
    
    embed.set_footer(text="Brawl Services - Fake Reviews")
    
    await ctx.send(embed=embed)

# =====================================================
# AUTO REVIEW
# =====================================================

async def auto_review():
    await bot.wait_until_ready()
    
    while not bot.is_closed():
        try:
            wait_time = random.randint(3600, 18000)
            await asyncio.sleep(wait_time)
            
            target_channel = bot.get_channel(TARGET_CHANNEL_ID)
            if target_channel is None:
                print(f"❌ Canalul destinație nu a fost găsit!")
                continue
            
            rating = random.choice(RATINGS)
            order = random.choice(ORDER_TYPES)
            price = ORDER_PRICES[order]
            message = random.choice(ALL_REVIEWS)
            
            if rating == "5/5" or rating == "5":
                stars = "⭐⭐⭐⭐⭐"
            elif rating == "4/5" or rating == "4":
                stars = "⭐⭐⭐⭐☆"
            elif rating == "3/5" or rating == "3":
                stars = "⭐⭐⭐☆☆"
            else:
                stars = "⭐⭐⭐⭐⭐"
            
            embed = discord.Embed(
                title="📝 NEW REVIEW - Brawl Services",
                description=f"**Customer**\nAnonymous Customer 🦷",
                color=discord.Color.gold()
            )
            
            embed.add_field(
                name="📦 Order Type",
                value=order,
                inline=False
            )
            
            embed.add_field(
                name="⭐ Rating",
                value=f"{stars}\n**{rating}**",
                inline=False
            )
            
            embed.add_field(
                name="💰 Price",
                value=price,
                inline=False
            )
            
            embed.add_field(
                name="💬 Review",
                value=f"> {message}",
                inline=False
            )
            
            embed.set_footer(text="✅ Verified Review | Brawl Services")
            embed.timestamp = datetime.now()
            
            await target_channel.send(embed=embed)
            print(f"✅ Review automat trimis!")
            
        except Exception as e:
            print(f"❌ Eroare: {e}")
            await asyncio.sleep(60)

# =====================================================
# START
# =====================================================

# =====================================================
# START
# =====================================================

@bot.event
async def on_ready():
    print(f'✅ Bot connected as {bot.user}')
    print(f'🚀 Started successfully!')
    print(f'📝 Commands: !review, !reviewrandom, !helpreview')
    print(f'📚 Loaded {len(ALL_REVIEWS)} reviews')
    print(f'📦 {len(ORDER_TYPES)} products available')
    
    target_channel = bot.get_channel(TARGET_CHANNEL_ID)
    if target_channel:
        print(f'📌 Reviews will be sent to: #{target_channel.name}')
    else:
        print(f'❌ CANALUL DESTINAȚIE NU A FOST GĂSIT!')
    
    bot.loop.create_task(auto_review())

# =====================================================
# RULEAZĂ CU TOKEN DIN VARIABILĂ DE MEDIU
# =====================================================

bot.run(os.getenv('DISCORD_TOKEN'))  # ← ASTA E CORECT!
