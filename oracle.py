import json, math

def jsnum(x):
    return int(x) if isinstance(x, float) and x == int(x) else x
def fmt(x): return str(jsnum(x))
def round1(x): return jsnum(math.floor(x * 10 + 0.5) / 10)
def round2(x): return jsnum(math.floor(x * 100 + 0.5) / 100)

def mix_plan(capQt, pct):
    if not (capQt > 0) or not (pct > 0):
        return {"error": "the system and the target must be positive"}
    if pct > 100:
        return {"error": "the target cannot beat pure concentrate"}
    conc = round1(capQt * pct / 100)
    water = round1(capQt - conc)
    if pct < 40: verdict = "a light mix"
    elif pct <= 60: verdict = "the sweet spot"
    elif pct <= 70: verdict = "a heavy mix"
    else: verdict = "past the sweet spot"
    return {"conc": conc, "water": water, "verdict": verdict}

def topup_plan(volQt, curPct, targetPct):
    if not (volQt > 0) or not (curPct >= 0):
        return {"error": "the volume and the mix must be positive"}
    if targetPct > 100:
        return {"error": "the target cannot beat pure concentrate"}
    if not (targetPct > curPct):
        return {"error": "the mix is already at or above the target"}
    conc = round1(volQt * (targetPct - curPct) / 100)
    if conc <= 1.5: verdict = "a small top-up"
    elif conc <= 3: verdict = "a real drain-and-fill"
    else: verdict = "a flush day"
    return {"conc": conc, "verdict": verdict}

def cost_plan(concPrice, premixPrice, qt):
    if not (concPrice > 0) or not (premixPrice > 0) or not (qt > 0):
        return {"error": "the prices and the quarts must be positive"}
    concCost = round2(qt / 2 * concPrice / 4)
    premixCost = round2(qt * premixPrice / 4)
    if concCost < premixCost * 0.95: verdict = "concentrate wins"
    elif concCost > premixCost * 1.05: verdict = "premix wins"
    else: verdict = "a wash"
    return {"concCost": concCost, "premixCost": premixCost, "verdict": verdict}

def render_mix(r, capQt, pct):
    return ("Your " + fmt(capQt) + " qt system targeting " + fmt(pct) + "% takes " + fmt(r["conc"])
            + " qt of concentrate and " + fmt(r["water"]) + " qt of water - " + r["verdict"] + ".")

def render_topup(r, volQt, curPct, targetPct):
    return ("Raising " + fmt(volQt) + " qt from " + fmt(curPct) + "% to " + fmt(targetPct) + "% takes "
            + fmt(r["conc"]) + " qt of concentrate - " + r["verdict"] + ".")

def render_cost(r, concPrice, premixPrice, qt):
    return ("For " + fmt(qt) + " qt of 50% mix: $" + fmt(r["concCost"]) + " from concentrate vs $"
            + fmt(r["premixCost"]) + " premixed - " + r["verdict"] + ".")

cases = []
def add(fn, f, rf, args):
    r = f(*args)
    c = {"fn": fn, "args": args, "result": r}
    if "error" not in r: c["render"] = rf(r, *args)
    cases.append(c)

for a in [[10,50],[8,50],[12,60],[6,40],[10,35],[14,55],[9,65],[10,80],[0,50],[10,0],[10,110]]:
    add("mixPlan", mix_plan, render_mix, a)
for a in [[8,35,50],[10,40,60],[6,45,55],[12,30,50],[8,50,60],[10,35,45],[5,40,60],[9,38,52],[8,50,50],[8,50,40]]:
    add("topupPlan", topup_plan, render_topup, a)
for a in [[22,14,10],[18,14,10],[20,16,8],[26,11,10],[20,10.5,10],[30,20,6],[22,14,5],[16,10,8],[0,14,10],[22,14,0]]:
    add("costPlan", cost_plan, render_cost, a)
json.dump(cases, open("expected.json", "w"), separators=(",", ":"))
print(len(cases), "cases")
