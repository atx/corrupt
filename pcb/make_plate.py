#! /usr/bin/env python3

import argparse
import collections
import pcbnew


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input", required=True)
    parser.add_argument("-o", "--output", required=True)
    parser.add_argument("--back", action="store_true")
    parser.add_argument("--step", default=14.1, type=float)
    args = parser.parse_args()

    def pt(x, y):
        scale = pcbnew.IU_PER_MM
        return pcbnew.wxPoint(round(x*scale), round(y*scale))

    print("Loading board from '{}'".format(args.input))
    pcb = pcbnew.LoadBoard(args.input)

    print("Constructing switch holes")
    for module in pcb.GetModules():
        fpname = str(module.GetFPID().GetLibItemName())
        if not args.back and fpname.startswith("SW_Cherry"):
            center = module.GetCenter() + pt(2.54, -5.08)
            total_size = 14.1
            straight_size = 13.0
            skip_size = total_size - straight_size
            width = int(0.1*pcbnew.IU_PER_MM)
            segments = [
                # Top
                ((-straight_size/2, -total_size/2), (straight_size/2, -total_size/2)),
                # Bottom
                ((-straight_size/2, total_size/2), (straight_size/2, total_size/2)),
                # Left
                ((-total_size/2, -straight_size/2), (-total_size/2, straight_size/2)),
                # Right
                ((total_size/2, -straight_size/2), (total_size/2, straight_size/2)),
            ]
            for (s_x, s_y), (e_x, e_y) in segments:
                ds = pcbnew.DRAWSEGMENT(pcb)
                pcb.Add(ds)
                ds.SetStart(center + pt(s_x, s_y))
                ds.SetEnd(center + pt(e_x, e_y))
                ds.SetLayer(pcbnew.Edge_Cuts)
                ds.SetWidth(width)
            corners = [
                # Left-Top
                (-straight_size/2, -straight_size/2, 90*2),
                # Right-Top
                (straight_size/2, -straight_size/2, 90),
                # Right-Bottom
                (straight_size/2, straight_size/2, 0),
                # Left-Bottom
                (-straight_size/2, straight_size/2, 90*3),
            ]
            for c_x, c_y, rot in corners:
                ds = pcbnew.DRAWSEGMENT(pcb)
                pcb.Add(ds)
                ds.SetShape(pcbnew.S_ARC)
                ds.SetCenter(center + pt(c_x, c_y))
                ds.SetArcStart(center + pt(c_x + skip_size/2, c_y))
                ds.SetAngle(90 * 10)
                ds.Rotate(ds.GetCenter(), rot*10)
                ds.SetLayer(pcbnew.Edge_Cuts)
                ds.SetWidth(width)
                pass
            pcb.Delete(module)
        elif fpname.startswith("Mount"):
            pad = module.FindPadByName("")
            #pad.SetSize(pad.GetDrillSize())
        else:
            pcb.Delete(module)

    print("Deleting all tracks, zones and text")
    for track in pcb.GetTracks():
        pcb.Delete(track)
    while pcb.GetAreaCount():
        pcb.Delete(pcb.GetArea(0))
    for drawing in pcb.GetDrawings():
        if not isinstance(drawing, pcbnew.TEXTE_PCB):
            continue
        text = drawing.GetText()
        if text[:3] in {"COL", "ROW"}:
            pcb.Delete(drawing)

    print("Saving to '{}'".format(args.output))
    pcbnew.SaveBoard(args.output, pcb)
    print("Done")

