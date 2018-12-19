# Beepo

A basic morse code trainer intended for experimentation.

Features:

* Memorise morse code by progressive learning similar to Koch method
* Adjustable parameters
* Timing

Non-Features:

* Full text playback - this is already well-catered for in other projects
* In general, no reproduction of features already implemented in other projects


# Install

Recommended: Setup a virtualenv

```
virtualenv .venv
. ./.venv/bin/activate
```

Install requirements:

```
pip install -r requirements.txt
```

# Run

```
python test.py
```

# Why

A primitive method of training morse code recognition (copying) is to send
training phrases at very slow speed (making both tones and pauses longer), allowing the student to spend more time decoding
each letter. The speed is then gradually increased up to the desired performance.

The Farnsworth method varies this by using the full speed for characters, only
increasing the spacing between characters and words. The spacing is then reduced up to
the desired speed. This avoids the "tone" of characters changing as the morse code
speeds up.

A further improvement on this is the Koch method, where training code is sent at
full speed, but starting out with only two letters, and increasing the number of
different letters used as the student's performance becomes good with the smaller
number of letters.

Many amateur CW aficionados regard the Koch method as the best method, as the
other methods all involve learning things at the wrong speed first, which may
not engage the same type of cognition as decoding at full speed - it is said that
at very slow speeds, the student may be listening for every single dit and dah,
and then consciously decode the sequence of dits and dahs into the character;
at full speed, one cannot "consciously think" that fast, and rather, a morse
character becomes a single entity that is directly translated to a character.

Why then this project?

Simply: The Koch method doesn't work for me personally.

This may have several reasons. I may have some congential or developmental
problems with auditory processing; I may have some attention deficit problem; or
my problem may be that I do my listening on my morning and evening work commute
on busy trains.

Whatever the reason, as I started learning to copy random sequences of M (--)
and K (-.-), everything was fine. I was quickly able to distinguish M and K.
However, once I moved on to R (.-.) I found out that my brain had categorised
Morse into "dah-dah" for M and "a bunch of tones" for K and distinguishing
between K and R was impossible.

I tortured myself for a while with morse training apps both for PC and for
mobile (Android) but I was not happy with any of them.

That's why I started this project: To create a morse trainer that will work for
me and let me become proficient in recognizing and copying all morse characters
so that I can then move on to copy phrases.

# License

Acknowledgements for public domain licensed source material:

* `setup.py` template: https://github.com/kennethreitz/setup.py
* Sound files used / derived from: https://commons.wikimedia.org/wiki/Category:Audio_files_of_Morse_code_-_alphabet

This project is also released into the public domain with no reservations.

Where public domain does not apply, the MIT license as reproduced in the `LICENSE` file shall apply.
