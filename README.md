# Slay the Spire AI

The long term goal of this project is a Slay the Spire AI. If possible,
I would like this game to be able to beat the rotational A20 record without
cheating (ideally, it literally reads the screen from a different computer
and emulates a mouse to send commands back).

## The Plan

There is a vertical aspect to this and a horrizontal aspect to it.

### The Vertical

An implementation of each piece of the Slay the Spire game:

* beginning option from Neow
* the first battle with a starter deck
* each card for each character
* each encounter
* shop
* elites
* bosses
* relics
* map
* correct interaction between all of the above

### The Horrizontal

The implementation in its various forms:

* an API mod that sends commands to play the otherwise unmodified* game
    * *the RNG fixer will be the other modification
    * this provides our source of truth for our vertical
* serialization of each action in the game
    * e.g the ability to play back a game
* a headless implementation of Slay the Spire, still running on computer
* a GPU implementation of Slay the Spire
    * made such that many parallel games can run together
* Model training on the GPU implementation of Slay the Spire
* Evaluation on the headless and main game

## Decompiling Slay the Spire

Slay the Spire 1 is written in Java. Go to where it is installed (on Steam
right-click the game, manage -> browse local files), find desktop-1.0.jar,
decompile it with [CFR](https://www.benf.org/other/cfr/), then run:

```
cd /path/to/SlayTheSpire
java -jar /path/to/cfr/jar desktop-1.0.jar --outputdir /this/repo/decompiled
```

## Stance on LLMs

Anyone looking at my recent commit history will surely see a lot of slop.
"Slop" is how I see LLMs, even recent frontier models. I'm fine with using
them for prototype purposes but honestly I'm very embarassed to commit
such low-quality code and writing as much as I already have.

An experiment with this project is to only let slop exist in branches tagged
as such, as a form of Code Complete's "Throwaway Prototype". All code in other
branches must be written by hand, ideally with slop branches only studied and
literally thrown away before implemented by hand in the code that makes it to
main.

## Next Action

Script that decompiles Slay the Spire (done manually via instructions above thus far).
