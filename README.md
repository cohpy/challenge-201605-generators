# The May 2016 COhPy challenge

The challenge for May is to write a program that uses a generator. It can do
anything (some examples you could choose are below). Write tests for your
code to make sure it works as you expect.

Then, as a bonus, recreate the program without using a generator. Use the tests
you wrote for the generator version to ensure that your new version works the same.
Compare the two and see if a generator is worth-while. Does it make the code
easier to understand, more useful, more general, etc.? Write tests for your code
to make sure that it works as you expect.

Pick one to start, and then see if you can do more.

## Simpler ##

1. Write a generator function that implements the [Python range
   function](https://docs.python.org/3/library/functions.html#func-range)
   (without using range()).

2. Write a generator function that generates prime numbers via the [Sieve of Eratosthenes](https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes).

3. Write a generator function that given a string, generates all [permutations](https://en.wikipedia.org/wiki/Permutation) of that string.

4. Write a generator function that generates all [Pythagorean Triples](https://en.wikipedia.org/wiki/Pythagorean_triple) starting with (3,4,5).


## More involved ##

1. Write a generator the generates coordinates of a [two-dimensional random walk](https://en.wikipedia.org/wiki/Random_walk) and plot N steps
or have it run live and continuously. As a bonus, have it return coordinates and a color and display the painting generated. Is it possible to
use separate generators for X and Y (think Etch-A-Sketch) and color (i.e. create a generators that use generators)? Also, instead of a random
walk, create a generator that uses some other algorithm to return X and Y coordinates.

2. Given an input text (say [Mary Shelley's Frankenstein](http://www.gutenberg.org/cache/epub/84/pg84.txt)), write a generator that starts with
a random word and then follows with a word that follows a randomly picked instance of that word, continuously. Make some poetry and see what fun
phrases are emitted. Share them!

 For example, let's say I have the text:

 "Python is cool and fun. I want to learn to program Python for fun times. I love ice cream and program for a living."

 The generator will start with a given random word, for example "and". The next time called it will return with either "fun" or "program".
 If it then returns "fun", it will next return either "I" or "times", etc.

 As a bonus, use a large number of works by the same author, and respect punctuation. The first word returned will always be the first word of
 a sentence, and when a chosen word ends a sentence, it will return that punctuation.

3. Write a generator that generates noise (randomly generated), and then tones. A tone is just a [Sine wave](https://en.wikipedia.org/wiki/Sine_wave) at a specific frequency.
Output the sound to the speaker via [SimpleAudio](http://simpleaudio.readthedocs.io/en/latest/) using samples of specific duration, or
[PyAudio](https://people.csail.mit.edu/hubert/pyaudio/) using callbacks in real-time.

 Expand your program to generate [harmonics](https://en.wikipedia.org/wiki/Harmonic) at different amplitudes (sound is additive, so you can add
 the results of multiple generators). Finally expand your program to generate notes, perhaps by simply increasing or decreasing amplitude (using a generator again),
 or by developing a full [ADSR](https://en.wikipedia.org/wiki/Synthesizer#Attack_Decay_Sustain_Release_.28ADSR.29_envelope) amplitude generator.

 Record your creation and save to a wave file.

