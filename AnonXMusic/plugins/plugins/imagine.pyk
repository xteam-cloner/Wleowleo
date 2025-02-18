from pyrogram import filters
from pyrogram.types import  Message
from pyrogram.types import InputMediaPhoto
from AnonXMusic import app
from MukeshAPI import api
from pyrogram.enums import ChatAction,ParseMode
#from config import BOT_USERNAME

@app.on_message(filters.command("imagine"))
async def imagine_(bot, message: Message):
    if message.reply_to_message:
        text = message.reply_to_message.text
    else:

        text =message.text.split(None, 1)[1]
    app=await message.reply_text( "`Please wait...,\n\nGenerating prompt .. ...`")
    try:
        await bot.send_chat_action(message.chat.id, ChatAction.UPLOAD_PHOTO)
        x=api.ai_image(text)
        with open("xteam.jpg", 'wb') as f:
            f.write(x)
        caption = f"""
    💘sᴜᴄᴇssғᴜʟʟʏ ɢᴇɴᴇʀᴀᴛᴇᴅ : {text}
    ✨ɢᴇɴᴇʀᴀᴛᴇᴅ ʙʏ : 
    🥀ʀᴇǫᴜᴇsᴛᴇᴅ ʙʏ : {message.from_user.mention}
    """
        await app.delete()
        await message.reply_photo("xteam.jpg",caption=caption,quote=True)
    except Exception as e:
        await app.edit_text(f"error {e}")
    
import requests
from pyrogram import filters
from pyrogram.enums import ChatAction
from AnonXMusic import app

# Getimg API key (replace with your actual key)
GETIMG_API_KEY = "key-ICLT6PNtwcDA5PKI7DmuKMXrueoKcDybWuHrXX1o9V8eszHCAOabBpvq2d7ZWewTa5A50ntiXEkDcMo1ewE5exp6LxuOAAr"
GETIMG_API_URL = "https://api.getimg.ai/v1/essential-v2/text-to-image"

# Function to generate an image using Getimg API
def generate_image(prompt):
    curl --request GET \
     --url https://api.getimg.ai/v1/models \
     --header 'accept: application/json'

    # Request payload to send to Getimg API
response = [
  {
    "id": "stable-diffusion-v1-5",
    "name": "Stable Diffusion v1.5",
    "family": "stable-diffusion",
    "pipelines": [
      "text-to-image",
      "image-to-image",
      "controlnet"
    ],
    "base_resolution": {
      "width": 512,
      "height": 512
    },
    "price": 0.00045,
    "created_at": "2023-05-23T18:51:22.297Z"
  },
  {
    "id": "realistic-vision-v1-3",
    "name": "Realistic Vision v1.3",
    "family": "stable-diffusion",
    "pipelines": [
      "text-to-image",
      "image-to-image",
      "controlnet"
    ],
    "base_resolution": {
      "width": 512,
      "height": 512
    },
    "price": 0.00045,
    "created_at": "2023-05-23T18:51:22.297Z"
  }
    ]

    # Make the API request
    response = requests.post(GETIMG_API_URL, json=data, headers=headers)

    if response.status_code == 200:
        # Extract image URL from the response
        image_url = response.json().get("image_url")
        return image_url
    else:
        return None

# Command handler to generate an image
@app.on_message(filters.command("aigen"))
async def generate_image_handler(client, message):
    chat_id = message.chat.id
    await app.send_chat_action(chat_id, ChatAction.TYPING)

    # Get the prompt from the user input
    if len(message.command) > 1:
        prompt = " ".join(message.command[1:])
    else:
        await message.reply_text("Usage: /generate_image <your prompt>")
        return

    try:
        # Call the function to generate the image via Getimg API
        image_url = generate_image(prompt)

        if image_url:
            # Send the generated image URL back to the user
            await message.reply_photo(photo=image_url, caption=f"Generated image for prompt: {prompt}")
        else:
            await message.reply_text("Sorry, I couldn't generate the image. Please try again later.")
    except Exception as e:
        await message.reply_text(f"Error: {str(e)}. Please try again later.")
