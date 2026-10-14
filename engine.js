(function (root) {
  "use strict";
  function round1(x) { return Math.round(x * 10) / 10; }
  function round2(x) { return Math.round(x * 100) / 100; }

  function mixPlan(capQt, pct) {
    if (!(capQt > 0) || !(pct > 0)) return { error: "the system and the target must be positive" };
    if (pct > 100) return { error: "the target cannot beat pure concentrate" };
    var conc = round1(capQt * pct / 100);
    var water = round1(capQt - conc);
    var verdict;
    if (pct < 40) verdict = "a light mix";
    else if (pct <= 60) verdict = "the sweet spot";
    else if (pct <= 70) verdict = "a heavy mix";
    else verdict = "past the sweet spot";
    return { conc: conc, water: water, verdict: verdict };
  }

  function topupPlan(volQt, curPct, targetPct) {
    if (!(volQt > 0) || !(curPct >= 0)) return { error: "the volume and the mix must be positive" };
    if (targetPct > 100) return { error: "the target cannot beat pure concentrate" };
    if (!(targetPct > curPct)) return { error: "the mix is already at or above the target" };
    var conc = round1(volQt * (targetPct - curPct) / 100);
    var verdict;
    if (conc <= 1.5) verdict = "a small top-up";
    else if (conc <= 3) verdict = "a real drain-and-fill";
    else verdict = "a flush day";
    return { conc: conc, verdict: verdict };
  }

  function costPlan(concPrice, premixPrice, qt) {
    if (!(concPrice > 0) || !(premixPrice > 0) || !(qt > 0)) return { error: "the prices and the quarts must be positive" };
    var concCost = round2(qt / 2 * concPrice / 4); // half the final mix is concentrate, 4 qt per gallon
    var premixCost = round2(qt * premixPrice / 4);
    var verdict;
    if (concCost < premixCost * 0.95) verdict = "concentrate wins";
    else if (concCost > premixCost * 1.05) verdict = "premix wins";
    else verdict = "a wash";
    return { concCost: concCost, premixCost: premixCost, verdict: verdict };
  }

  function renderMix(r, capQt, pct) {
    return "Your " + capQt + " qt system targeting " + pct + "% takes " + r.conc + " qt of concentrate and "
      + r.water + " qt of water - " + r.verdict + ".";
  }

  function renderTopup(r, volQt, curPct, targetPct) {
    return "Raising " + volQt + " qt from " + curPct + "% to " + targetPct + "% takes " + r.conc
      + " qt of concentrate - " + r.verdict + ".";
  }

  function renderCost(r, concPrice, premixPrice, qt) {
    return "For " + qt + " qt of 50% mix: $" + r.concCost + " from concentrate vs $" + r.premixCost
      + " premixed - " + r.verdict + ".";
  }

  var api = { mixPlan: mixPlan, topupPlan: topupPlan, costPlan: costPlan, renderMix: renderMix, renderTopup: renderTopup, renderCost: renderCost };
  if (typeof module !== "undefined" && module.exports) module.exports = api; else root.FreezeMath = api;
})(this);
