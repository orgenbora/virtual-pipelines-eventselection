import argparse
import os
import ROOT
ROOT.gROOT.SetBatch(True)


def main(path, fraction, output):
    print(f"Input file: {path}")
    df = ROOT.RDataFrame("Events", path)

    count = df.Count()
    num_events = count.GetValue()
    print(f"Number of events: {num_events}")

    reduced_events = int(num_events * fraction)
    print(f"Reduce the initial dataset to {reduced_events} events")

    basename = os.path.basename(path)
    fullpath = os.path.join(output, basename)
    print(f"Write out to {fullpath}")
    df.Range(reduced_events).Snapshot("Events", fullpath)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("path", type=str,
            help="Full path to NanoAOD file such as given to TFile::Open or the RDataFrame constructor")
    parser.add_argument("fraction", type=float,
            help="Fraction of events to be kept, e.g., fraction=0.1 keeps 10% of the original file")
    parser.add_argument("output", type=str,
            help="Output directory for the reduced NanoAOD file, the basename of the input file is kept.")
    args = parser.parse_args()
    main(args.path, args.fraction, args.output)
