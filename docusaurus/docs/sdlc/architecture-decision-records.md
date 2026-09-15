# ADR's (Architecture Decision Records)
ADR's are intended to prove/disprove assumptions that the 3 Amigo's make during the inception of a new feature or `epic`on the backlog. 

They guide the implementation, and get all developers/QA/product/tech leads to agree on a soltion.

They usually focus on specific key details where there is uncertainty around the best approach to take for a given feature.

It's an agile alternative to massive architectural designs which over-prescribe solutions, but they may not fly with leadership/arch governance teams if you must get your feature past a change advisory board.

## Template
```markdown
# Title


## Status
**status**: proposed/accepted/rejected/deprecated/superseded
**author(s)**: Jim, Bob


## Context
Describe the issue / question / decision that needs to be made.


## Options
Usually there are multiple approaches to solve a problem, list them all here with advantages/disadvantages and link to POC code.

### Option 1
Description

#### Advantages
- list

#### Disadvantages
- list


## Decision
"The team chose Option 1 because..."
"Option x didn't work because of x"


## Next Steps / Consequences (Optional)
What comes next, is further work required to finalise a POC or the chosen option?
```
