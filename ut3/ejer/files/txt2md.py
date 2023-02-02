# *******************
# DE TEXTO A MARKDOWN
# *******************
import filecmp
from pathlib import Path


def run(text_path: Path) -> bool:
    md_path = "data/txt2md/outline.md"
    with open(text_path, "r") as file_input:
        with open(md_path, "w") as file_output:
            for line in file_input:
                tabs_count = line.count("\t") + 1
                hashtag = "#" * tabs_count
                lines = line.strip()

                file_output.write((f"{hashtag} {lines}\n"))

    return filecmp.cmp(md_path, "data/txt2md/.expected", shallow=False)


if __name__ == "__main__":
    run("data/txt2md/outline.txt")
