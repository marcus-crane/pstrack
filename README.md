# PSTrack

## hwwwhat is this?

Stop watching so much King of the Hill and/or Full Metal Jacket, it's bad for your speech.

I got annoyed that the Play Store updates can be kinda rubbish. Often an update will be available but I'll have to manually kick it off.

Yup, I have update notifications check and yessir/maam, I do indeed have auto updates enabled so *shrug* it /should/ work, right?

Anyway, this is a small script that I'll just run as a cron job and get my own homebaked update notifications using either Pushover or Pushbullet when I get around to adding that next.

Oh, the other thing is that maybe I might plug this into a Discord bot to automate update announcements for some app/game-specific servers that I'm in. That'd be kinda cool, huh?

## Where's the manual?

Here's the manual:

You'll need Python 3 and the requests module. You can pick it up with `pip(3) install requests` depending on your setup.

If you're on macOS and you install it using `brew` chances are that Python 3 will be symlinked to `python3` and `pip3` hence the `(3)` bit.

To run it, just do a simple little `python(3) track.py` and it'll either tell you to check again later or inform you of what was updated.

It's not super useful at the moment without notifications unless you're just curious or love CLI stuff.

## How do I setup the uhh, the config, what I'm trying to ask is "How do I configure this thing"

Ah, gotcha. You'll need to move `apps.example.json` to `apps.json` and populate it with your own data.

The keys are the name of the apps you want to keep track of. The objects within said keys contain the version number and the Play Store string.

Personally, when adding a new app, I just set the currentVersion to `1.0.0.0` and regardless of if it's actually higher or lower, it'll overwrite it to be correct anyway.

As for finding the Play Store ID, you can do that by going to the respective app page in the Play Store eg; [Kings Knight](https://play.google.com/store/apps/details?id=com.square_enix.android_googleplay.KingsKnightww) and copying the segment after `details?id=`. Don't include `&hl=en` if it's there or any other parameters that come afterward.

In the case of Kings Knight, the segment is just `com.square_enix.android_googleplay.KingsKnightww`

## Something something python something beginner

Yes, that's right, I haven't written much Python yet so feel free to make a pull request and teach me some stuff 🤠

I know `requirements.txt` and `setup.py` are a thing but beats me if I should be using them
