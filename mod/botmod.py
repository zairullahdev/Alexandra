import asyncio
import wavelink
import ast
import inspect
import re
import discord
import json
import requests

def bypass(url):

    payload = {
        "url": url,
    }

    r = requests.post("https://api.bypass.vip/", data=payload)
    return r.json()

def track_end(bot):
  @bot.event
  async def on_wavelink_track_end(player: wavelink.Player, track: wavelink.Track, reason):
    ctx = player.ctx
    vc: player = ctx.voice_client

    if vc.loop:
      return await vc.play(track)

    try:
      next_song = vc.queue.get()
      await vc.play(next_song)
      await ctx.send(f"Now playing: {next_song.title}")
    except wavelink.errors.QueueEmpty:
      await ctx.send("There are no more track")
      await asyncio.sleep(180)
      await vc.disconnect()
      await ctx.send("There is no more music to play after 3min, Leaving. ( 24/7 Supported)")
