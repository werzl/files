# Uncle Bob - Clean AI: Agentic Discipline, Episode 2

## Intro
Uncle Bob paints the picture of early software developers writing assembly, punching holes in cards.

Compilers moved us up a level of abstraction, then compilers of compilers, source generators - now we only need to understand source code.

**He's making the point because he proposes we may no longer need to look at the source code, only understand architectural decisions and high-level outcomes (testing).**


## Hunt the Wumpus
Talking through a README MD document describing the Hunt the Wumpus game (text-based adventure game).

He asks **is this the source code?**
- Does this answer every question? - No there are ambiguities

He used Claude to **generate Gherkin (test syntax) from the README**. Shows one of the features. The Scenarios aren't complete / not very accurate.
- He told Claude he'd like it to support English & Spanish, so it abstracted out the commands so they could be implemented in Spanish/English.
- He asks Claude to compare the compressed sizes of the README with the features - The features contain more information than the README.
  - Features had a low compression ratio - which implies that the Gherkin lang is inefficient
- 