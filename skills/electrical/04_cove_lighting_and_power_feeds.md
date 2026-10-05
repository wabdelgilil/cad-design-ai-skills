# SKILL-LGT-04: Cove Lighting & Power Feed Engineering

> **Domain:** Indirect & Concealed Lighting Design  
> **Level:** Professional / Consultant Standards (SBC 401, IESNA)  
> **Automation Target:** AutoCAD 2027 via ActiveX COM (Python `win32com.client`)

---

## 1. Engineering Philosophy & Objectives

Perimeter cove lighting (بيت النور / Concealed LED Strips) provides indirect, diffuse ambient illumination that defines architectural volume and softens ceiling contrasts.

In professional drafting, a cove light is not just a freeform decorative rectangle; it requires:
1. **Precise Interior Setback:** Uniform geometric offset from all four finished wall faces ($30\text{--}40\text{ cm}$).
2. **Power Feed Point / Driver Box:** A designated junction/driver box where 230V AC mains connects to the DC LED driver ($24\text{V DC}$).
3. **Dedicated Switched Control:** A designated switch gang to toggle the cove independently from downlights.

---

## 2. Fundamental Design Principles (Code & Standards)

### 2.1 Uniform Offset Rule
- **Standard Setback:** $35\text{ cm} \pm 5\text{ cm}$ from the finished interior wall plaster.
- **Corner Closure:** The cove boundary must be a **closed continuous polyline** (`Closed = True`) with uniform lineweight ($0.30\text{--}0.35\text{ mm}$) to render prominently in CAD prints.

### 2.2 LED Driver Sizing & Placement Rule
- Commercial LED strip typical rating: $9.6\text{ W/m}$ to $14.4\text{ W/m}$.
- Maximum run per single feed point without voltage drop: $\le 5.0\text{ m}$ (for longer runs, a closed loop or secondary feed is required).
- **Feed Box (Driver Junction Box):** Must be placed in an accessible corner of the cove or near the room entrance conduit drop.

---

## 3. Reference Consultant Induction (Heuristics from Real Plans)

From analysis of original consultant drawings (`Standard Project...ELE.dwg`):

### 3.1 Geometric Characteristics in CAD
- **Layer:** Dedicated layer `E-LITE-COVE` or colored Blue (`Color = 5` or `140`).
- **Entity:** `AcDbPolyline` (LightWeight, closed).
- **Global Width / Lineweight:** Plotted with medium thickness to immediately distinguish ceiling drywall offsets from architectural structural walls.

### 3.2 Power Feed & Control Line
- The cove does not sit disconnected in the ceiling.
- A secondary wire line (e.g. Magenta polyline) connects from the entrance 3-gang switch (Gang 2) to the corner power feed box of the cove.
- This represents the switch leg feeding the driver in the ceiling plenum.

---

## 4. CAD Entities, Blocks & Attributes

| Feature | AutoCAD Entity | Layer Name | Color / Lineweight |
| :--- | :--- | :--- | :--- |
| Cove Perimeter Polyline | `AcDbPolyline` (Closed) | `E-LITE-COVE` | Blue (Color: 5), Lineweight: $0.35\text{ mm}$ |
| Cove Power Feed Box | `AcDbBlockReference` (`Junction_Box`) | `Lighting-Fixtures` | Orange / ByBlock |
| Switched Driver Leg | `AcDbPolyline` | `Lighting Circuits` | Magenta (Color: 6) |

---

## 5. Algorithmic Formulation for Auto-Cove Generation

```python
def generate_cove_polyline(acad_model, room_box, setback=0.35):
    """
    Constructs a closed, uniform rectangular cove polyline.
    room_box: (xmin, ymin, xmax, ymax) of finished wall faces.
    """
    import win32com.client
    
    xmin, ymin, xmax, ymax = room_box
    c_xmin = xmin + setback
    c_ymin = ymin + setback
    c_xmax = xmax - setback
    c_ymax = ymax - setback
    
    coords = [
        c_xmin, c_ymin,
        c_xmax, c_ymin,
        c_xmax, c_ymax,
        c_xmin, c_ymax
    ]
    
    variant_pts = win32com.client.VARIANT(win32com.client.pythoncom.VT_ARRAY | win32com.client.pythoncom.VT_R8, coords)
    cove = acad_model.AddLightWeightPolyline(variant_pts)
    cove.Closed = True
    cove.Layer = "E-LITE-COVE"
    cove.Color = 5 # Blue
    cove.Lineweight = 35 # 0.35 mm
    return cove
```

---

## 6. Anti-Patterns & Prohibitions (Zero Tolerance)

1. ❌ **Floating / Disconnected Cove:** Drawing a blue rectangle with no power feed wire connecting it to the room switch.
2. ❌ **Uneven Wall Setbacks:** $20\text{ cm}$ on the North wall and $60\text{ cm}$ on the East wall without an architectural stepped ceiling reason.
3. ❌ **Open Polyline Ends:** Forgetting `Closed = True`, resulting in a disconnected visual gap at the start/end vertex.
