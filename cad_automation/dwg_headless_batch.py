"""
Headless AutoCAD & DXF Automation Template
Demonstrates headless / silent processing of architectural and MEP drawings
using ezdxf and AutoCAD accoreconsole.

Dependencies:
    pip install ezdxf
"""
import sys
import os
import ezdxf

def inspect_dxf_layers(dxf_path: str):
    """Parses a DXF file without GUI and extracts all layer names and entity counts."""
    if not os.path.exists(dxf_path):
        print(f"Error: File not found {dxf_path}")
        return
        
    doc = ezdxf.readfile(dxf_path)
    msp = doc.modelspace()
    
    print(f"DXF Version: {doc.dxfversion}")
    print(f"Total Modelspace Entities: {len(msp)}")
    
    layers = {}
    for entity in msp:
        layer = entity.dxf.layer
        layers[layer] = layers.get(layer, 0) + 1
        
    print(f"\nUnique Layers ({len(layers)}):")
    for l_name, count in sorted(layers.items()):
        print(f"  - {l_name:<30}: {count} entities")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        inspect_dxf_layers(sys.argv[1])
    else:
        print("Usage: python dwg_headless_batch.py <path_to_dxf_file>")
