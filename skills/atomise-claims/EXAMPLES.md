# Examples: Atomise Claims into Atomic Statements

## Example 1: Splitting a compound cited sentence

### Before (without this skill)

```
Blinking is a physiological process influenced by both cognitive load and fatigue, and it is widely
used as a marker of drowsiness \citep{a2020,b2021}.
```

Treated as one claim with two citations covering everything.

### After (with this skill applied)

```
[c1] (sent 1) "Blinking is a physiological process." | type: factual | cites: a2020,b2021
[c2] (sent 1) "Blinking is influenced by cognitive load." | type: factual | cites: a2020,b2021
[c3] (sent 1) "Blinking is influenced by fatigue." | type: factual | cites: a2020,b2021
[c4] (sent 1) "Blinking is widely used as a marker of drowsiness." | type: factual | cites: a2020,b2021
```

### Why it's better

Each claim can now be checked against the specific paper that supports it; the audit can find that
`a2020` supports c1/c4 but not c2/c3, which the bundled form hides.

---

## Example 2: Preserving hedges and resolving references

### Before (without this skill)

```
This pooling biases the threshold upward and reduces recall, which proves the method is superior.
```

### After (with this skill applied)

```
[c1] "Pooling blink-free and blink-heavy epochs may bias the threshold upward." | type: numeric/causal
[c2] "Pooling reduces recall." | type: numeric  (FLAG: check against results — direction unverified)
[c3] "The pooling result proves the method is superior." | type: framing  (FLAG: overclaim, "proves")
```

### Why it's better

The pronoun "this"/"which" is resolved, the causal claim is kept at its real (hedged) strength, and the
overclaim ("proves ... superior") is isolated as framing to be softened or removed downstream.
