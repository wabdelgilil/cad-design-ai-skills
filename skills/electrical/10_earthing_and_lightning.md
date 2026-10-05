# SKILL-EAR-01: Earthing & Lightning Protection

> **Domain:** Protective earthing, equipotential bonding, lightning protection,
> TV antenna arrestor
> **Standards:** SBC 401 Chapter 9, IEC 60364-5-54, IEC 62305
> **Evidence:** layers `L.P` (56), `E-GN-TXT` (89), `E-GN-DTL` (247),
> `E-TEXT` (10), `E-WIRE-L` (49), `tele` (14)

---

## 1. The earthing / lightning sheet

| Layer | Entities | Content |
| :--- | --- | --- |
| `L.P` | 56 | `LP Rod` ×18, `Earthing bit` ×6, spec texts |
| `E-GN-TXT` | 89 | `12.7 MM BOLT` |
| `E-GN-DTL` | 247 | the earthing detail drawing |
| `E-TEXT` | 10 | `EARTHING SYSTEM` |
| `E-WIRE-L` | 49 | the earthing-bond contractor note |

Sheet titles on layer `TEXT`: `EARTH PROTECTION SYSTEM LAYOUT` (×2) and
`LIGHTING PROTECTION SYSTEM` (×2).

---

## 2. ⭐ The device schedule (verbatim)

| Device | Block | Inserts | Text annotation |
| :--- | :--- | --- | --- |
| Lightning protection rod | `LP Rod` | **18** | `Roof lightining protection rod` |
| Earthing pit | `Earthing bit` | **6** | `Grounding earth pit` |
| Roof strip connector | — | 1 | `3x25 mm Roof copper strip connector` |
| TV antenna arrestor | — | 1 | `T.V.^Ilightning arrestor` (tab, see §5) |

> **Spelling in the original:** `lightining` (not *lightning*) and
> `Earthing bit` (not *Earthing pit*). Reproduce exactly.

### ⭐ Ratios to check a generated drawing against

```
LP rods            : 18
earthing pits      :  6      ->  3 rods per pit
copper strip       : 3 x 25 mm
bolt               : 12.7 MM (1/2 inch) BOLT
```

The 18 : 6 ratio means the roof array is fed from **6 earth pits**, i.e. the
roof is divided into roughly **3 lightning-protection zones**, each bonded to
its own pit.

---

## 3. ⭐ Material specifications

| As drawn | Interpretation |
| :--- | --- |
| `3x25 mm Roof copper strip connector` | 3 × 25 mm bare copper strip, roof level |
| `12.7 MM BOLT` | 12.7 mm (½ in) bolt — the mechanical fixings throughout |
| `NON-METALLIC CLIP MANUFACTURED FROM OUTDOOR GRADE POLYCARBONATE AND SPACED IN ACCORDANCE WITH MANUFACTURER'S RECOMMENDATION` | the conductor support on the roof run |

**The 25 mm copper strip is the primary down-conductor material for the roof
network.** It is not a cable and must not be substituted with a flexible
conductor without engineering approval.

The non-metallic clip requirement is verbatim from layer `E-GN-TXT` and must
travel with the detail: outdoor-grade polycarbonate, spaced per the
manufacturer's recommendation (i.e. **no invented spacing** — quote the
manufacturer).

---

## 4. ⭐ The contractor's earthing obligation (verbatim, layer `E-WIRE-L`)

```
It is the contractor's responsibility to coordinate with the supervising
engineer regarding the number of grounding electrodes according to the soil
resistance and to connect the grounding system with the building's rebar to
obtain a grounding resistance that ...
```

The text is truncated in the drawing (it continues off the entity). What is
unambiguously stated, and therefore binding:

1. The **number of grounding electrodes is not fixed by the drawing** — it is
   determined from **soil resistivity**.
2. The earthing system **must be bonded to the building rebar**.
3. The contractor **must coordinate with the supervising engineer** on both.
4. A target **grounding resistance** is to be achieved — the numeric target is
   in the truncated part and **must be requested**, not invented.

**Rule:** the 6 `Earthing bit` pits on the drawing are the *drawn* quantity, not
a validated count. Do not reduce or increase it without a written soil-resistivity
justification approved by the supervising engineer.

---

## 5. TV antenna arrestor

Layer `tele` carries, verbatim:

```
T.V. ANTENNA (UHF-VHF)
T.V.^Ilightning arrestor
```

> The antenna-riser note is `T.V.` + a **tab** (`^I`) + `lightning arrestor`.
> The tab is invisible in most viewers; when parsing text, treat `^I` and a
> space as equivalent so the note is still recognised.
Together with `EL-SAT-DISH` ×6. The antenna riser therefore **requires** a
lightning arrestor at the head end. This is a code-driven requirement (SBC 401
§9) and must not be omitted when the TV/MATV system is reproduced.

---

## 6. Earthing conductor routing

Layer `E-WIRE-L` also carries 31 inserts of the block `bbb` — the earthing
conductor run. Note that `bbb` is a keyboard-mash name (see SKILL-XC-01 §5);
reproduce it, never rename it.

---

## 7. Missing sheets (documented gap, not an error to fill in)

The drawing contains:
- `EARTH PROTECTION SYSTEM LAYOUT` — **earthing** ✔
- `LIGHTING PROTECTION SYSTEM` — **lightning** ✔

But **no surge protective device (SPD) schedule** and **no equipotential-bonding
detail** exist as separate sheets. If SPDs or bonding details are required, they
are **new scope** and must be raised with the supervising engineer rather than
inferred from these sheets.

---

## 8. Anti-Patterns

1. ❌ **Writing `lightning` where the drawing says `lightining`.**
2. ❌ **Writing `Earthing pit` where the block is `Earthing bit`.**
3. ❌ **Treating the 6 pits as a validated electrode count** — they are the drawn
   quantity, pending soil resistivity.
4. ❌ **Omitting the rebar bond** — it is an explicit contractor obligation.
5. ❌ **Inventing a target earth resistance** — the value is truncated in the
   drawing and must be requested.
6. ❌ **Substituting a flexible conductor for the `3x25 mm` copper strip.**
7. ❌ **Inventing a clip spacing** instead of quoting the manufacturer.
8. ❌ **Omitting the antenna arrestor** — the drawing says `T.V.^Ilightning arrestor`
   (tab after `T.V.`).
9. ❌ **Inventing an SPD schedule** that is not in the drawing.
10. ❌ **Renaming `bbb`.**
