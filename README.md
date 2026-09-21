# Slay the Spire AI

The long term goal of this project is a Slay the Spire AI. If possible,
I would like this game to be able to beat the rotational A20 record without
cheating (ideally, it literally reads the screen from a different computer
and emulates a mouse to send commands back).

## The Plan

There is a vertical aspect to this and a horrizontal aspect to it.

### The Vertical

An implementation of each piece of the Slay the Spire game.

### The Horrizontal

The implementation in its various forms:

* an API mod that sends commands to play the otherwise unmodified* game
    * the RNG fixer will be the other modification
* a headless implementation of Slay the Spire, still running on computer
* a GPU implementation of Slay the Spire
    * made such that many parallel games can run together
* Model training on the GPU implementation of Slay the Spire
* Evaluation on the headless and main game

## Stance on LLMs

Anyone looking at my recent commit history will surely see a lot of slop.
That is how I see LLMs, even recent frontier models. I'm fine with using
them for prototype purposes but honestly I'm very embarassed to commit
such low-quality code and writing.

An experiment with this project is to only let slop exist in branches tagged
as such, as a form of Code Complete's "Throwaway Prototype". All code in other
branches must be written by hand, ideally with slop branches only studied and
literally thrown away before implemented by hand in the code that makes it to
main.

## Next Action

Script that decompiles Slay the Spire.
