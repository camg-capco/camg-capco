Specification Heading
=====================
Tags: regression
              |word  |Vowel Count|
              |------|-----------|
              |Gauge |3          |
              |Mingle|2          |
              |Snap  |1          |
              |GoCD  |1          |
              |Rhythm|0          |

This is an executable specification file. This file follows markdown syntax.
Every heading in this file denotes a scenario. Every bulleted point denotes a step.

To execute this specification, run
	gauge specs

* Vowels in English language are "aeiou".

Vowel counts in single word
---------------------------

tags: single word

* The word <word> has <Vowel Count> vowels.