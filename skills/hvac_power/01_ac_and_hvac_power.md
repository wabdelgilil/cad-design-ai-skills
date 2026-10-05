# SKILL-HVAC-01: HVAC & Air-Conditioning Power

> **Domain:** Air-conditioning, fans, pumps, elevators — electrical power side
> **Standards:** SBC 401, SBC 501 (mechanical), IEC 60364-7-702
> **Evidence:** layers `12- EQUIPMENT-HVAC` (73), `M-HVAC-REFP` (81),
> `E-SLD` (395), `ELEC-LEGEND` (76), `E-POWR-TEXT` (64)

---

## 1. ⭐ `KHW` is the HVAC breaker tag

Every feeder breaker on the SLD is tagged `KHW`:

| Tag | Rating | T.D.L |
| :--- | :--- | --- |
| `KHW 200A` | 200 A | **108.7 KVA** |
| `KHW 63A` | 63 A | 25.9 KVA |
| `KHW 63A` | 63 A | 23.0 KVA |
| `KHW 40A` | 40 A | 17.9 KVA |
| — (no KHW tag) | — | 12.0 KVA |

The tag is written as **`KHW` + space + rating** (e.g. `KHW 200A`), and the
plain rating (`200A`, `63A`, `40A`) also appears on the same SLD. Both forms
belong on the drawing; the plain form is the breaker rating, the `KHW` form is
the tagged designation.

**Rule:** an HVAC feeder that is missing its `T.D.L = x.x KVA` value and its
`KHW <rating>` tag is incomplete.

---

## 2. ⭐ AC isolator selection (verbatim legend, layer `ELEC-LEGEND`)

The consultant provides **three** distinct AC switching devices. Choosing the
wrong one is the most common error in this system.

| Legend text (copy exactly) | Rating | Use for |
| :--- | :--- | :--- |
| `32 A, 230V POWER SWITCH FOR SPLIT AC` | 32 A / 230 V | **split-type** (wall/floor) AC units |
| `40 A, 230V POWER ISOLATOR FOR CONCEALED AC ABOVE CEILING` | 40 A / 230 V | **concealed** (cassette/ducted) units, 230 V |
| `40 A, 400V POWER ISOLATOR FOR CONCEALED AC ABOVE CEILING` | 40 A / 400 V | **concealed** units, 400 V three-phase |

And the wet-area/outdoor variant (layer `E-POWR-TEXT`, ×64):

```
30A,2P, 230V,IP65,(Weather Proof)
```

### Decision table

| Unit type | Device | Poles |
| :--- | :--- | :--- |
| Split AC | `32 A, 230V POWER SWITCH FOR SPLIT AC` | per mechanical schedule |
| Concealed AC, 230 V | `40 A, 230V POWER ISOLATOR …` | — |
| Concealed AC, 400 V | `40 A, 400V POWER ISOLATOR …` | 3P |
| Outdoor / wet location | `30A,2P, 230V,IP65,(Weather Proof)` | 2P |

An isolator must be **within sight of and accessible from the unit**, and must
be a **lockable** device for roof plant.

---

## 3. AC supply conductor sizes (from the SLD feeder table)

| Breaker | Conductor (as drawn) | Conduit (as drawn) |
| :--- | :--- | :--- |
| 40 A | `(4X16)+16 mm2 CU/XLPE/PVC\PPVC CONDUIT 50 MM DIA` | 50 mm |
| 63 A | `(4X120)+70 mm2 CU/XLPE/PVC\PPVC CONDUIT 160 MM DIA` | 160 mm |
| 200 A | `2X((4X240)+1x120) mm2 CU/XLPE/PVC\PUPVC /2X160 MM` | 2 × 160 mm |
| sub-group | `(4X10)+10 mm2 CU/XLPE/PVC\PPVC CONDUIT 50 MM DIA` | 50 mm |

> **Transcription note.** The drawing writes **`mm2`**, not mm²; and it embeds
> the conduit size in the *same* string as the conductor, e.g.
> `(4X10)+10 mm2 CU/XLPE/PVC\PPVC CONDUIT 50 MM DIA`. `\P` and `\PP` are MTEXT
> line-break codes. Quote the whole string when a takeoff is compared against
> the drawing.

Pattern: four current-carrying conductors plus a neutral, with the neutral equal
to the phase size up to 16 mm² and reduced to 70 mm² at 120 mm². Do not
substitute a generic current-capacity table; use the consultant's pairings
unless the engineer approves a change.

---

## 4. Inline fans — `AXI-F-IL1`

| Property | Value |
| :--- | --- |
| Block | `AXI-F-IL1` |
| Inserts | **73** |
| Layer | **`12- EQUIPMENT-HVAC`** (all 73) |
| Role | HVAC inline / duct fan |

### ⭐ Critical correction to the previous skill library

Earlier skill files classified `AXI-F-IL1` as a **bathroom exhaust fan over the
toilet**. That is **wrong**, and the evidence is unambiguous:

1. **All 73 inserts sit on `12- EQUIPMENT-HVAC`** — an HVAC equipment layer, not
   a lighting or small-power layer.
2. In the first-floor lighting plan the same block appears in **regular
   triplets** at a constant pitch, e.g.
   `(242.276, 9.769)`, `(242.373, 6.348)`, `(248.130, 9.601)` — a mechanical
   array, not a per-toilet symbol.
3. A separate block `Fan Outlet` **is declared** in the 938-block table but has
   **zero inserts** on the lighting plan.

**Rules:**
- `AXI-F-IL1` goes on `12- EQUIPMENT-HVAC`, scale `1.0`, and **never** on a
  lighting layer.
- A **bathroom** exhaust fan symbol is still **UNRESOLVED**: the candidates are
  `AXI-F-IL1` and `Fan Outlet`. This needs a visual check on the original
  drawing before any bathroom fan is drawn. Do not guess.

---

## 5. Mechanical reference layer

Layer `M-HVAC-REFP` (81 inserts) holds the block `G$C7580D14A` — the mechanical
equipment reference geometry. It is an `$`-prefixed AutoCAD fingerprint block;
reproduce it, never rename it.

Coordination rule: the electrical HVAC sheet **references** the mechanical
layout on `M-HVAC-REFP`; it does not re-draw the equipment. Any change to
`G$C7580D14A` must be mirrored on the mechanical sheet by the mechanical
consultant.

---

## 6. Elevators

The SLD carries a feeder tagged:

```
ELEVATOR-P
```

(4 occurrences). Elevator feeders are dedicated and must not be grouped with
HVAC feeders. The `-P` suffix is the only designation given — no rating is
stated on the drawing, so **the rating must come from the lift supplier /
mechanical schedule**, not from this sheet.

---

## 7. Water pumps (electrical side)

The consultant's note (layer `Power Circuits`):

```
Each water pump is fed from the apartment's own electrical load panel
in coordination with the mechanical plans.
```

- Pump feeders originate at the **apartment load panel**.
- Starter type, rating and count come from the **mechanical plans**.
- Do not invent a soft-starter/VFD arrangement; ask.

---

## 8. Ventilation set

Layer `Speakers` is audio. Mechanical ventilation is on `12- EQUIPMENT-HVAC`
and `M-HVAC-REFP`. There is **no** dedicated exhaust-fan layer in this drawing —
which is itself a finding: the drawing does not separate supply and extract air
electrically. Any new ventilation circuit must be tagged explicitly and its
layer agreed with the supervising engineer.

---

## 9. Anti-Patterns

1. ❌ **`AXI-F-IL1` on a lighting layer.** It belongs to `12- EQUIPMENT-HVAC`.
2. ❌ **Using the 32 A split-AC switch for a concealed unit** — concealed units
   get the 40 A isolator.
3. ❌ **Using the 400 V 40 A isolator for a 230 V unit.**
4. ❌ **An HVAC feeder with no `T.D.L = x.x KVA`.**
5. ❌ **Guessing a bathroom exhaust-fan symbol** while `AXI-F-IL1` vs
   `Fan Outlet` is unresolved.
6. ❌ **Renaming `G$C7580D14A`.**
7. ❌ **Grouping `ELEVATOR-P` with a `KHW` feeder.**
8. ❌ **Deriving the elevator rating from this drawing.**
9. ❌ **Sizing an AC circuit from a generic table** instead of the
   consultant pairings `(4X16)+16 mm2` / `(4X120)+70 mm2` / `(4X10)+10 mm2`.
