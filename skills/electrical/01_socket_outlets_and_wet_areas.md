# SKILL-SPR-01: Small Power (Sockets) Distribution

> **Domain:** Residential small power / outlets
> **Standards:** SBC 401, IEC 60364-7-701 (wet areas), SECO
> **Evidence:** layer `Power` (803 entities), `E-POWER` (26), `WATER SUPPLY` (71),
> `Power Circuits` (82), `E_Wire Power` (120), `E-POWR-TEXT` (64)

---

## 1. The small-power symbol census (measured, whole drawing)

| Block | Inserts | Layer | Role |
| :--- | --- | --- | --- |
| `Single outlet` | **448** | `Power` | 1×13 A socket |
| `Boublex Outlet` | **79** | `Power` | 2× socket outlet (**name misspelled in the original**) |
| `Floor box 2` | 21 | `Power` | floor box, small power |
| `gfgfgfgfkgfklgkf88555` | 20 | `Power` | consultant scratch block — reproduce, do not rename |
| *(text)* `{\Ftimes|c0;W.P}` | **231** | `Power` | **water-proof outlet annotation** |
| `WAP` | 26 | `E-POWER` | wet-area power outlet |
| `HEATER` | 71 | `WATER SUPPLY` | water-heater connection (plumbing coordination) |
| `d s` | 81 | `Power Circuits` | power homerun symbol |

**Key ratios (self-check for any generated drawing):**

```
single outlets  : 448
double outlets  :  79
W.P. outlets    : 231     ->  34.0 % of all 448+79=527 outlets
floor boxes     :  21
```

The W.P. ratio is a strong fingerprint: if a generated floor does not produce
≈1/3 weather-proof outlets, the wet-area rule in §4 has been missed.

---

## 2. Circuit allocation

Small power occupies the **even** circuit numbers of each panel
(`04/ BL-DB`, `06/ BL-DB`, … `38/ BL-DB`) — see SKILL-XC-02 §3.

The homerun block for a power run is `d s` on layer `Power Circuits`
(81 inserts), and the text reference is `<even>/ <TAG>-DB`.

---

## 3. The `W.P.` annotation — exact form

```
{\Ftimes|c0;W.P}
```

This is MTEXT with an inline font override. Rendered output is:

```
W.P
```

- 231 occurrences, all on layer `Power`, immediately beside a socket block.
- The single exception is a bare `WP` (no dot) — treat the dotted form as
  canonical and the bare form as a drawing inconsistency to be reported, not
  silently propagated.

**Rule:** every socket installed in a wet location carries a `W.P` text
immediately adjacent to it, on the same layer as the socket.

---

## 4. Wet-area rule (SBC 401 §701 / IEC 60364-7-701)

| Zone | Extent | Requirement |
| :--- | :--- | :--- |
| Zone 0 | inside the bath/shower basin | SELV ≤ 12 V only |
| Zone 1 | directly above the bath/shower, up to 2.25 m | IPX4 minimum (IPX5 with jets) |
| Zone 2 | within 0.60 m of the Zone-1 boundary | IPX4 minimum |
| Outside | rest of the room | IP44 recommended |

Practically, in this project:
- Bathroom / kitchen / laundry sockets → block `WAP` on layer `E-POWER`, tagged
  `W.P`.
- Every such outlet needs a **30A, 2P, 230V, IP65** isolator (see §5).

---

## 5. ⭐ The weather-proof isolator (64 identical units)

Verbatim from layer `E-POWR-TEXT` (64 occurrences, all identical):

```
30A, 2P, 230V, IP65, (Weather Proof)
```

| Field | Value |
| :--- | --- |
| Current | 30 A |
| Poles | **2P** |
| Voltage | 230 V (phase-to-neutral of the 400 V system) |
| Ingress | **IP65** |
| Quantity on the drawing | **64** |

`2P` on a 230 V single-phase load is a deliberate full-pole disconnect, not a
system-voltage statement — the site supply is 400 V (SKILL-SEC-01 §1).

---

## 6. Water heaters (71 units)

Block `HEATER`, 71 inserts, layer `WATER SUPPLY`. The heater is a **plumbing**
element on an **electrical** sheet, so:

- Keep the symbol on layer `WATER SUPPLY` (do not move it to a power layer).
- The electrical connection is drawn separately on the power plan.
- A heater circuit is a **dedicated** circuit, not shared with general sockets.

---

## 7. ⭐ Water pumps — the consultant's own coordination note

Verbatim from layer `Power Circuits`:

```
Each water pump is fed from the apartment's own electrical load panel
in coordination with the mechanical plans.
```

Three consequences that must be honoured:

1. **Each apartment has its own load panel** — the apartment DB is the source.
2. **Pump feeders are per-apartment**, not per-building.
3. **Coordination with the mechanical plans is mandatory** — pump count, rating
   and starter type are not to be invented from the electrical sheet alone.

---

## 8. Floor boxes

Block `Floor box 2` × 21 on layer `Power`. The floor-box composition is stated on
layer `E-DATA` (see SKILL-ELV-01 §4) because a floor box is a **combined**
power + data + TV outlet:

```
FLOOR BOX   1 Doublex Power / 1 Data Outlet / 1 TV Outlet        (x20)
FLOOR BOX   2 Doublex Power / 1 Data / 1 Tele / 1 HDMI           (x1)
```

So the electrical half of a floor box is 1 or 2 `Boublex Outlet` — the power
component must be drawn on layer `Power` and the data/TV component on `E-DATA`.

---

## 9. Power wire runs

Layer `E_Wire Power` (120 entities, all `LWPOLYLINE`) carries the power circuit
routing. The homerun symbol is `d s` on `Power Circuits`. Circuit lines use the
same `pbx*` segment kit as lighting, on layer `Circuit Line`.

---

## 10. Anti-Patterns

1. ❌ **A wet-area socket without a `W.P` annotation.**
2. ❌ **A `WAP` outlet on layer `Power` instead of `E-POWER`.**
3. ❌ **An odd circuit number for a power circuit.**
4. ❌ **Sharing a heater circuit with general sockets** — heaters are dedicated.
5. ❌ **Locating a water pump on a common riser** — each apartment feeds its own.
6. ❌ **Writing `Doublex Outlet`** — the block is `Boublex Outlet`.
7. ❌ **Renaming `gfgfgfgfkgfklgkf88555`.**
8. ❌ **Dropping the `W.P` text and keeping only the block** — the drawing has
   both, 231 times.
9. ❌ **Using an IP44 spec where the project standard is IP65** for the 30A/2P
   isolators.
