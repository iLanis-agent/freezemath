# Freeze math

The system names the concentrate, the target names the top-up, and the jug names the price.

Coolant fools people twice: the premixed jug sells water at concentrate prices, and past the sweet spot more glycol stops meaning more protection. Freeze math does the honest arithmetic for both.

## The three tools

- **Mix plan** - system capacity and target percentage become the concentrate and water to pour: `round1(cap * pct / 100)` of concentrate, the rest water, banded from a light mix to past the sweet spot. A target over 100% is refused.
- **Top-up plan** - the quarts in the system, the current percentage and the target become the concentrate that closes the gap: `round1(vol * (target - current) / 100)`, banded from a small top-up to a flush day. A target at or below the current mix is refused.
- **Cost plan** - concentrate and premix gallon prices become the honest cost of a quart of 50% mix, with the winner called only outside a 5% wash.

## Honesty notes

Illustrative planning arithmetic only. Every figure is a labeled default you replace by reading your owner's manual and the jug. More glycol is not more protection: past the sweet spot the freeze point climbs again, and pure concentrate freezes sooner than a good mix. Use the coolant type your manual names, never mix colors on a guess, and dispose of old coolant properly - it is toxic and sweet-tasting to animals.

## Files

- `index.html` - the pitch
- `app.html` - the calculators
- `engine.js` - the arithmetic (browser and node)
- `oracle.py` - the same arithmetic, float-for-float, writing `expected.json`
- `test.js` - runs every case in `expected.json` through `engine.js` and compares results and renders exactly

Run the check:

```
python3 oracle.py && node test.js
```
