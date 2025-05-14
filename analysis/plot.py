import os
import re
import matplotlib.pyplot as plt

KEY_METRICS = [
    "simInsts",
    "simOps",
    "system.cpu.numCycles",
    "simSeconds",
    "hostSeconds",
    "system.cpu.ipc",
    "system.cpu.cpi",
    "system.mem_ctrl.readReqs",
    "system.mem_ctrl.writeReqs",
    "system.mem_ctrl.avgRdBWSys",
    "system.mem_ctrl.avgWrBWSys"
]

OUTDIRS = [
    "nbody_100_out",
    "nbody_200_out",
    "nbody_400_out",
    "nbody_800_out",
    "nbody_1600_out",
    "nbody_3200_out"
]

INPUT_SIZES = [100, 200, 400, 800, 1600, 3200]

def parse_three_stats_dumps(stats_file):
    """
    read 'stats.txt' file which has three dumps
    returns list [setup_lines, execution_lines, teardown_lines],
    where each element is a list of lines for that region.
    """
    with open(stats_file, 'r') as f:
        lines = f.readlines()

    regions = []
    capturing = False
    current_block = []

    for line in lines:
        if "Begin Simulation Statistics" in line:
            capturing = True
            current_block = []
        elif "End Simulation Statistics" in line:
            capturing = False
            regions.append(current_block)
        elif capturing:
            current_block.append(line)

    return regions


def extract_key_metrics_from_lines(lines):
    """
    parse key metrics, returns a dict { metric_name: float_value }.
    """
    results = {}
    pattern = re.compile(r'^(\S+)\s+([\d.eE+\-NaN]+)\s+.*')

    for line in lines:
        match = pattern.match(line.strip())
        if match:
            key = match.group(1)
            val_str = match.group(2)
            if key in KEY_METRICS:
                # parse as float
                try:
                    results[key] = float(val_str)
                except ValueError:
                    results[key] = float('nan') if val_str == 'nan' else val_str
    return results


def main():
    data = {}

    # parse
    for outdir in OUTDIRS:
        stats_path = os.path.join(outdir, "stats.txt")
        if not os.path.isfile(stats_path):
            print(f"[ERROR] {stats_path} not found, skipping.")
            continue

        regions = parse_three_stats_dumps(stats_path)
        if len(regions) != 3:
            print(f"[ERROR] {stats_path} has {len(regions)} dumps")
            continue

        # only want execution tims
        execution_lines = regions[1]
        metrics = extract_key_metrics_from_lines(execution_lines)
        data[outdir] = metrics


    x_values = INPUT_SIZES

    for metric in KEY_METRICS:
        y_values = []
        valid_x = []

        for i, outdir in enumerate(OUTDIRS):
            if outdir in data and metric in data[outdir]:
                val = data[outdir][metric]
                y_values.append(val)
                valid_x.append(x_values[i])
            else:
                print(f"[WARNING] missing {metric} for {outdir}")


        if not y_values:
            continue

       #linear plot
        plt.figure(figsize=(6, 4))
        plt.plot(valid_x, y_values, marker='o', linestyle='--', color='b')
        plt.title(f"{metric} vs. Input Size (Linear Scale)")
        plt.xlabel("Input Size (# of elements)")
        plt.ylabel(metric)

        xtick_labels = []
        for val in valid_x:
            if val >= 1_000_000:
                xtick_labels.append(f"{val//1_000_000}M")
            elif val >= 1_000:
                xtick_labels.append(f"{val//1_000}k")
            else:
                xtick_labels.append(str(val))
        plt.xticks(valid_x, xtick_labels)

        plt.tight_layout()
        out_plot_linear = f"{metric}_linear.png"
        plt.savefig(out_plot_linear)
        plt.close()
        print(f"Saved plot: {out_plot_linear}")

        # log log plot
        plt.figure(figsize=(6, 4))
        plt.plot(valid_x, y_values, marker='o', linestyle='--', color='r')
        plt.title(f"{metric} vs. Input Size (Log-Log Scale)")
        plt.xlabel("Input Size (# of elements)")
        plt.ylabel(metric)
        plt.xscale('log')
        plt.yscale('log')

        plt.xticks(valid_x, xtick_labels, rotation=0)

        plt.tight_layout()
        out_plot_loglog = f"{metric}_loglog.png"
        plt.savefig(out_plot_loglog)
        plt.close()
        print(f"saved plot: {out_plot_loglog}")

    print("done")


if __name__ == "__main__":
    main()
