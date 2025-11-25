
## 1️ GamaSafe Strategy SOP (Business#1 – NIFTY Weekly)

This is the logic you’ll encode in `strategy/` and `risk_engine/`.

###  Instrument & Style

* **Underlying:** NIFTY index only (for v1.0)
* **Style:** Non-directional **Short Strangle** + **Hedges**
* **Expiry:** Nearest **weekly** expiry (Thursday)
* **Entry Day:** **Wednesday 11:00 AM IST**
  (or Tuesday if holiday / special case)

---

###  Entry Rules

1. **Market Regime Filter**

   * Avoid entry if:

     * IVP (NIFTY) > 80 and major event (Budget, Election, RBI policy) **same week**
     * Gap up/down > 1.5% on entry day
   * Otherwise → system allowed.

2. **Time Filter**

   * Only between **10:45–11:15 AM**.
   * If missed → no new trade for the week.

3. **Strike Selection (Short Legs)**

   * Use option chain to find ~**12–15 Delta** on both sides:

     * Short **OTM Call**: CE with Delta ≈ +0.15
     * Short **OTM Put**: PE with Delta ≈ –0.15
   * If exact is not available, pick **slightly safer (further OTM)**, not closer.

4. **Hedge Selection**

   * For each short leg, buy a deep OTM hedge:

     * CE hedge: 400–600 points above short CE
     * PE hedge: 400–600 points below short PE
     * OR approx premium **₹8–₹15**
   * Always hedge at entry. No naked legs.

5. **Position Size**

   * Define risk per week (e.g., **0.5–1% of capital max loss**).
   * Calculate number of lots so that worst-case loss (short–long spread width) fits within this.
   * Keep simple for v1: **fixed lots per week** (e.g., 2–4) and scale later.

---

###  Risk & Adjustment Logic

6. **Profit Booking Rule (40% Rule)**

   * Track combined premium of each short leg at entry:

     * Example:

       * Short CE: sold at ₹40
       * Short PE: sold at ₹45
   * When one side’s premium **decays by 40–50%**:

     * Example: ₹40 → ₹24
     * **Buy back that leg**, book profit.
     * Immediately **sell a new leg** on same side to re-balance strangle:

       * Choose new strike again at 12–15 Delta.

7. **Gamma / Directional Risk Rule (Red Zone)**

   * Define **inner “danger range”** near short strike:

     * When spot comes within **0.5 × expected move** of a short leg → yellow.
     * When spot crosses that boundary and IV rising → red.
   * In red zone:

     * Shift opposite leg closer (take more credit).
     * Optionally convert to **ratio hedge** or **spread** e.g., roll vertical.

8. **Hard Stop-Loss Rule (Per Side)**

   * If any short leg’s premium **doubles from entry**:

     * Example: Sold at ₹40 → now ₹80
     * **Mandatory action**:

       * Close that side
       * Either:

         * Rebuild new strangle further away, OR
         * Reduce size and keep only safer side

9. **Time-Based Exit**

   * Exit **all legs**:

     * On **Thursday by 3:10–3:20 PM** OR
     * When combined remaining premium < 10–15% of entry credit
   * No overnight carry after expiry.

---

###  P&L & Risk Constraints

10. **Per-Week Risk**

* Max allowed **realized loss** for the week: e.g., –₹25K (you choose).
* If hit:

  * Stop all new entries for week.
  * Maintain discipline.

11. **Target**

* Weekly target e.g. **₹20K–₹40K** realized.
* But process > target. Never force trade to meet number.

This SOP is what your modules will implement.

---

## 2️ Module-Level Blueprint (File-by-File Responsibilities)

###  `data_engine/`

**`fetcher.py`**

* Functions:

  * `get_spot(symbol: str) -> float`
  * `get_option_chain(symbol: str, expiry: str) -> pd.DataFrame`
  * `get_historical_iv(symbol: str) -> pd.DataFrame` (optional v2)
* Source:

  * KiteConnect APIs (or saved CSV during dev mode)

**`greeks.py`**

* Calculate Greeks if API doesn’t give:

  * `compute_greeks(option_df, spot, r, iv, dte) -> pd.DataFrame`
* Attach columns: `delta`, `gamma`, `vega`, `theta`.

**`oi.py`**

* Functions:

  * `get_oi_summary(option_chain) -> dict`

    * Highest OI CE/PE
    * Change in OI
    * Put/Call OI ratio
  * Mark TMJ / TMG zones for your language.

**`iv_atr.py`**

* `get_iv_metrics(option_chain) -> dict`:

  * Current ATM IV
  * IV percentile (IVP)
* `get_atr(symbol, lookback=14) -> float`
  (Using historical spot data)

---

###  `strategy/`

**`config.yaml`**

* Parameters:

  * entry_time_window
  * target_delta_range
  * hedge_distance_points
  * max_weekly_loss
  * lot_size
  * expiry_day
  * etc.

**`strike_selector.py`**

* Input:

  * option chain, config
* Output:

  * `{ "short_call": strike, "short_put": strike }` at ~12–15 delta.

Functions:

* `select_short_strikes(option_chain, config) -> dict`
* `select_hedge_strikes(option_chain, short_strikes, config) -> dict`

**`hedge_engine.py`**

* Verifies hedge distance & cost.
* `validate_hedges(short_legs, hedge_legs, config)`

**`adjustment_engine.py`**

* Inputs:

  * current positions
  * live prices
  * config
* Outputs:

  * suggestions:

    * close leg x
    * open leg y
    * shift hedge
* Core:

  * Implements **40% profit rule**
  * Implements **premium doubling SL**
  * Implements **gamma/red-zone behavior**

**`exit_rules.py`**

* `should_exit_all(positions, time, pnl, config) -> bool`
* `should_reduce_size(...)`

---

###  `risk_engine/`

**`delta_monitor.py`**

* `calculate_net_delta(positions, option_chain) -> float`
* Show whether book is +- small / large delta.

**`gamma_monitor.py`**

* `calculate_net_gamma(positions, option_chain)`
* Detect “gamma risk zone” when:

  * Spot approaches short leg
  * Gamma rises sharply

**`breakeven.py`**

* Compute:

  * BE low, BE high from:

    * credit received
    * structure
* `compute_breakevens(positions, net_credit, spot) -> (low, high)`

**`risk_limits.py`**

* Check:

  * weekly loss breached?
  * max per trade risk?
* `check_weekly_risk(pnl_history, config) -> status`

---

###  `dashboard/` (Streamlit)

**`main.py`**

* Layout:

  1. Sidebar:

     * Config summary
     * Capital & risk limits
     * Toggle: Live/Simulation
  2. Tabs:

     * **Overview**
     * **Positions**
     * **OI & IV**
     * **Risk & Greeks**
     * **P&L / History**

* Calls:

  * from `data_engine` to fetch current state
  * from `strategy` to suggest entries & adjustments
  * from `risk_engine` to compute exposure

**`charts.py`**

* Helper functions:

  * Price vs BE lines
  * OI bar charts
  * IV trend
  * Delta/Gamma line charts

**`tables.py`**

* Nicely formatted:

  * Option chain table
  * Current positions
  * Adjustment suggestions

**`alerts.py`**

* Logic to display colored banners:

  * GREEN: Safe theta zone
  * YELLOW: Spot near short strikes
  * RED: Gamma risk / SL zone / weekly loss hit

---

###  `utils/`

**`config_loader.py`**

* Load `config.yaml` once and cache.

**`datetime_tools.py`**

* Helpers:

  * `is_within_time_window(now, start, end)`
  * `get_next_expiry()`

**`helpers.py`**

* Common small utilities:

  * rounding, formatting, logging wrappers.

---

###  `logs/`

* `trade_logs.csv` – each real trade decision (entry/adjust/exit)
* `pnl_logs.csv` – daily / per-session P&L
* `system_logs.log` – debug + errors

---

## 3️ Dashboard Layout (Streamlit – Screen Design)

Think of one main page with 4 sections.

###  Section 1 – Top Bar (Summary)

* NIFTY Spot, % change
* Current IV, IVP
* ATR (14), expected move
* Weekly realized P&L
* Status pill: **SAFE / WATCH / DANGER**

###  Section 2 – Current Position Block

* Table of:

  * Short legs (strike, type, qty, entry, LTP, P&L)
  * Hedge legs
* Net:

  * Net credit
  * BE low / BE high
  * Days to expiry

Visual:

* Small plot: Spot vs BE vs short strikes.

###  Section 3 – Risk & Greeks

* Net Delta
* Net Gamma
* Per-side Delta (CE vs PE)
* Risk Messages:

  * “Delta neutral” / “Call heavy” / “Put heavy”
  * “Gamma rising near CE side” etc.

###  Section 4 – OI + IV

* OI bar graph by strikes (CE & PE)
* Highlight max OI + shift from morning
* IV graph vs time (for ATM)

###  Section 5 – GamaSafe Suggestions

* Bulleted recommendations:

  * “Book 40% profit on PUT leg at 22800PE”
  * “Shift CALL leg from 24000CE to 24100CE”
  * “Weekly loss limit hit – no new entries.”
* Each suggestion is backed by functions in `adjustment_engine.py` and `risk_limits.py`.

---

## 4️ 1–2 Week Execution Roadmap

Here’s a practical build order you can follow.

###  **Day 1–2**

* Set up repo (already done 🎉)
* Add folder structure (empty py files)
* Implement **`config.yaml`**
* Implement **`data_engine/fetcher.py`** with dummy/test data (CSV or mock JSON)

###  **Day 3–4**

* Implement:

  * `greeks.py` (or plug in delta/gamma from API)
  * `iv_atr.py` basic version (even static ATR initially)
  * `oi.py` basic OI summary

* Start `strategy/strike_selector.py`

  * Hard-code 12–15 delta selection logic using chain.

###  **Day 5–6**

* Implement:

  * `risk_engine/breakeven.py`
  * `risk_engine/delta_monitor.py`
* Wire up simple **Streamlit `main.py`**:

  * Show spot, option chain, selected strikes, BE.

Now you already have **working GamaSafe Lite**.

###  **Day 7–9**

* Add:

  * `strategy/adjustment_engine.py` (40% rule + SL rule)
  * `risk_engine/gamma_monitor.py`
* Show:

  * Suggestion text box in dashboard
  * Color-coded alerts

###  **Day 10–14**

* Add:

  * Logging (`logs/`)
  * Simple P&L tracker
  * OI charts + IV charts
  * “Simulation mode” (read saved EOD chain instead of live)

By end of 2 weeks, you’ll have:

* Full SOP encoded
* Live-ish dashboard
* Risk + BE calculations
* Suggestion engine
* Logs & structure to automate further

---


