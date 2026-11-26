import os

LINE = "Are you exact change? My coils have been humming all day for someone who fits my slot perfectly \u2014 you just dropped in, so go ahead, press my buttons."


def main():
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
