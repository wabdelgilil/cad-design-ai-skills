# SKILL-AUD-01: Public Address & Background Music

> **Domain:** Audio — ceiling/wall speakers, volume controls, amplifiers
> **Standards:** SBC 401, SBC 802 (Emergency Voice), ISO 9921
> **Evidence:** layer `Speakers` (325 entities), `Speakers` spec strings

---

## 1. The audio system as drawn

Layer **`Speakers`** — 325 entities, 159 block inserts:

| Block | Inserts | Role |
| :--- | --- | --- |
| `Ceiling Speaker` | **95** | ceiling loudspeaker |
| `Volume Control` | **50** | local room volume control (with mic) |
| `Audio Amplifire` | **10** | mixer/amplifier *(name misspelled in the original)* |
| `AMPLIFIER 2.1 CH 50 100 WATT` | 4 | 2.1-channel 100 W amplifier |
| `LINE`, `SPLINE`, `ARC` | 116 | speaker wiring and coverage geometry |

### ⭐ The 95 : 50 ratio

There are **95 ceiling speakers** and **50 volume controls**. The ratio is
**1.90 : 1** — i.e. roughly **one volume control per two speakers**.

This is the key design fingerprint of the system: zones with audio but no local
control (corridors, common areas) have speakers only; occupied rooms (majles,
bedrooms, living rooms) get a speaker **plus** a volume control.

**Self-check for a generated floor:** a volume-control count above ~60 % of the
speaker count means controls are being duplicated in non-occupied zones.

---

## 2. ⭐ Equipment specifications (verbatim, layer `Speakers`)

```
Ceiling SPEAKER 10 watt system voltag (70)v  /  75 dB
WALL SPEAKER 20 watt system voltag (70)v  /  3m HIGHT 80 dB
Sound volume control & MIC XLR-5
MIXER APMLIFIER(as needed)watt
```

> **Two traps in this block of text.** `voltag` is missing the final **e**, and
> the mixer line is misspelled **`APMLIFIER`** (not *Amplifier*) and is written
> **without spaces** around the parentheses. Byte-for-byte it is
> `MIXER APMLIFIER(as needed)watt`.

| Item | Spec |
| :--- | --- |
| Ceiling speaker | 10 W, **70 V** system, 75 dB |
| Wall speaker | 20 W, **70 V** system, 80 dB, mounted at **3 m** height |
| Volume control | includes a **MIC XLR-5** input — so every controlled zone can also host a microphone |
| Mixer/amplifier | *"as needed" watt* — the wattage is **not fixed** in the drawing |
**The system is a 70 V distributed (constant-voltage) PA system**, not a
low-impedance system. Every tap must therefore be on a **70 V line**, and the
amplifier power must be sized from the connected speaker wattage plus headroom.

The mixer line — `MIXER APMLIFIER(as needed)watt` — means the drawing **does not
fix** the amplifier size. Do not invent one; request it, or state the sizing
basis explicitly alongside the design.

---

## 3. The 2.1-channel amplifier

`AMPLIFIER 2.1 CH 50 100 WATT` (×4) — a 2.1-channel, 50/100 W unit. The
"50/100" is the standard 50 W + 100 W channel pairing. Four such units serve the
building.

---

## 4. Amplifier count vs speaker count

10 `Audio Amplifire` + 4 `AMPLIFIER 2.1 CH` = **14 amplifier positions** for
**95 speakers** → about **7 speakers per amplifier position**. Use this as a
planning check, and note that the drawing gives no zone-by-zone amplifier
assignment — that must be requested.

---

## 5. Interaction with the fire alarm system

The fire system already has **29 bells + 2 weatherproof sirens** on layer
`LIGHT` (SKILL-FA-01). The PA speakers are on layer `Speakers` and are a
**separate** system.

**Do not merge them.** If voice evacuation is required, it must be an explicit
engineer decision, because the drawing shows two independent systems with
different layers, different power and different addressing.

---

## 6. Block-name traps

| Exact name | Trap |
| :--- | --- |
| `Audio Amplifire` | *Amplifier* is misspelled |
| `AMPLIFIER 2.1 CH 50 100 WATT` | spaces matter; no punctuation |
| `Ceiling Speaker` / `Volume Control` | title case, not upper case |

---

## 7. Anti-Patterns

1. ❌ **Designing a low-impedance (8 Ω) PA.** The drawing specifies **70 V**.
2. ❌ **Writing `Audio Amplifier`** — the block is `Audio Amplifire`, and the
   spec text is `MIXER APMLIFIER(as needed)watt`.
3. ❌ **A volume control in every zone**, breaking the ~1:2 ratio.
4. ❌ **Fixing the amplifier wattage** when the drawing says *"as needed"*.
5. ❌ **Putting a wall speaker below 3 m** — the spec says `3m HIGHT`.
6. ❌ **Merging PA speakers with fire bells/sirens** into one layer.
7. ❌ **Omitting the `MIC XLR-5`** capability of the volume control when a zone is
   intended to host a microphone.
