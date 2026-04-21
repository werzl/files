# Uncle Bob - Clean AI: Agentic Discipline, Episode 1

## Intro
Uncle Bob - "I'm not an expert in this, because no one is an expert in this yet".

Using Claude Code CLI.

Bob makes a big deal out of showing us how long Claude takes when he asks it to follow the TDD laws, comparing it to the 80's/90's with the long compile times.

## Testing Disciplines
`make a class named Stack, write no tests` - Bug prone


`make a class named Stack and follow the three laws of TDD` - Full TDD
- Claude assumes the `Stack` exercise for implementing a stack data structure
- Claude happily runs the TDD cycle (GREEN, RED, GREEN)
- Takes Claude longer, uses more tokens and burns more of Claude's short term memory vs just `make a class named Stack, write no tests`
- Took >3 mins


`create a class named Stack that implements a stack of integers. Write all the tests first, then implement`
- Took 43 seconds


## Prompting Observations
- Bob runs a super vague prompt `examine this code and improve as necessary`
- Prompts got higher level
- Worried less about the code and more about architecture / design structure
- Emphasis on code recedes into the background