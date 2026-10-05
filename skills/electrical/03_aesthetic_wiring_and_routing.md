# SKILL-LGT-03: Aesthetic Electrical Wiring & Circuit Routing

> **Domain:** CAD Electrical Drafting & Circuit Looping  
> **Level:** Professional / Consultant Standards (SBC 401, CIBSE)  
> **Automation Target:** AutoCAD 2027 via ActiveX COM (Python `win32com.client`)

---

## 1. Engineering Philosophy & Objectives

In electrical shop drawings and consultant schematics, wire lines (`E-LITE-CIRC` / `Lighting Circuits`) are not merely schematic "point-to-point connections". They are architectural representations of conduit paths that must convey order, rhythm, and clarity.

This skill governs:
1. **Elimination of Diagonal Spiderwebs:** Strictly prohibiting arbitrary diagonal lines slashing across rooms.
2. **Orthogonal & Concentric Looping:** Constructing rectangular or curved loop lines that parallel architectural walls and cove boundaries.
3. **Wall-Conduit Following:** Guiding switch feeder wires along wall perimeters with clean $90^\circ$ turns or smooth filleted corners.
4. **Homerun Precision:** Terminating branch circuits with standard arrow pointers (`tyfg`) carrying panel board designation and circuit number (`01/ AT4-DB`).

---

## 2. Fundamental Design Principles (Code & Standards)

### 2.1 Branch Circuit Protection & Grouping (SBC 401)
- Maximum connected load per $10\text{A}$ lighting branch circuit: $\le 1200\text{ VA}$ (typically $10\text{--}15$ LED luminaires).
- Color-Coding Conventions on Plans:
  - **Red / Cyan Polylines:** Switched load circuit 1 (General downlights).
  - **Magenta / Violet Polylines:** Switched load circuit 2 (Cove, sconces, or fan).
  - **Green Polylines with Arrow:** Homerun path to distribution board (`CIRCUIT HOMERUNS POINTER`).

### 2.2 Aesthetic Drafting Standards (Consultant Practice)
- Wires connecting ceiling spots within a room should form a **closed rectangular loop or clean continuous U-shape**.
- Wires leading from a wall switch to ceiling spots must run perpendicular to the wall, then turn neatly into the luminaire array.

---

## 3. Reference Consultant Induction (Heuristics from Real Plans)

From detailed analysis of the original consultant CAD drawing (`Standard Project...ELE.dwg`):

### 3.1 The Downlight Closed Rectangular Loop
In the Master Bedroom:
- The red wiring polyline connects the 5 spots along an **orthogonal perimeter rectangle**:
  1. Starts at Top-Left Spot ($X_{\text{left}}, Y_{\text{top}}$).
  2. Runs vertically down to Bottom-Left Spot ($X_{\text{left}}, Y_{\text{bottom}}$).
  3. Runs horizontally across to Bottom-Mid Spot ($X_{\text{center}}, Y_{\text{bottom}}$).
  4. Continues horizontally across to Bottom-Right Spot ($X_{\text{right}}, Y_{\text{bottom}}$).
  5. Runs vertically up to Top-Right Spot ($X_{\text{right}}, Y_{\text{top}}$).
- **Zero diagonal shortcuts:** The lines strictly follow the axes of the room, running parallel to the blue cove light box!

### 3.2 Junction Box & Feeder Distribution
- An octagonal **Junction Box / Pull Box** (colored orange) is located at the corridor/entrance intersection:
  - Feeder enters the junction box from the panel homerun.
  - From the junction box, a vertical run climbs into the bathroom.
  - Another branch feeds down into the entrance switch.
  - A third branch feeds directly into the bedroom ceiling array.

### 3.3 Bedside 2-Way Interconnection Wire (The Purple Line)
- The switch line connecting the bedroom entrance switch to the two bedside 2-way switches is drawn as an elegant, wall-hugging run:
  - From Entrance Switch: Climbs along the West wall up to the headboard level.
  - Connects to Left Bedside Switch.
  - Extends horizontally behind the headboard to Right Bedside Switch.

---

## 4. CAD Entities, Blocks & Attributes

| Wire / Circuit Type | AutoCAD Entity Type | Layer Name | Color / Linetype |
| :--- | :--- | :--- | :--- |
| Primary Lighting Loop | `AcDbPolyline` (LightWeight) | `Lighting Circuits` | Color: `Red` (1) |
| Secondary / Fan Loop | `AcDbPolyline` (LightWeight) | `Lighting Circuits` | Color: `Magenta` (6) |
| Homerun Pointer Line | `AcDbLine` + `AcDbBlockReference` (`tyfg`) | `CIRCUIT HOMERUNS POINTER` | Color: `Green` (3) |
| Circuit Text Annotation | `AcDbMText` / `AcDbText` | `CIRCUIT HOMERUNS POINTER` | Text: `"01/ AT4-DB"` |
| Pull / Junction Box | `AcDbBlockReference` (`Junction_Box`) | `Lighting-Fixtures` | Color: `Orange` / ByBlock |

---

## 5. Algorithmic Routing Implementation (Python ActiveX)

```python
def draw_orthogonal_bedroom_loop(acad_model, spots):
    """
    Connects the 5 bedroom spots in an orthogonal aesthetic ring.
    spots: dict with keys 'top_left', 'top_right', 'bottom_left', 'bottom_mid', 'bottom_right'
    """
    import win32com.client
    
    tl = spots['top_left']
    tr = spots['top_right']
    bl = spots['bottom_left']
    bm = spots['bottom_mid']
    br = spots['bottom_right']
    
    # Path: Top-Left -> Bottom-Left -> Bottom-Mid -> Bottom-Right -> Top-Right
    coords = [
        tl['x'], tl['y'],
        bl['x'], bl['y'],
        bm['x'], bm['y'],
        br['x'], br['y'],
        tr['x'], tr['y']
    ]
    
    # Create 2D lightweight polyline
    variant_pts = win32com.client.VARIANT(win32com.client.pythoncom.VT_ARRAY | win32com.client.pythoncom.VT_R8, coords)
    pline = acad_model.AddLightWeightPolyline(variant_pts)
    pline.Layer = "Lighting Circuits"
    pline.Color = 1 # Red
    return pline
```

---

## 6. Anti-Patterns & Prohibitions (Zero Tolerance)

1. ❌ **Spiderweb Diagonals:** Drawing straight lines from a corner switch directly across the center of the bed or diagonal across the room.
2. ❌ **Crossing Open Wall Openings:** Running wires floating across door openings without following the lintel or floor conduit path.
3. ❌ **Unlabeled Homeruns:** Arrow lines without the destination distribution board code (e.g. arrow without `"01/ AT4-DB"`).
4. ❌ **Wire Intersecting Block Text:** Routing wire polylines directly through the center of room label texts or fixture attribute text.
