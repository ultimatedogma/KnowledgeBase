from pathlib import Path
from typing import List, Union

def get_markdown_files_recursive(
    path: Union[str, Path]
) -> List[Path]:
    """
    Recursively collect all .md files under `path`, ignoring any
    file or folder whose name starts with '.' at any level.

    Args:
        path: root directory (str or Path) to start searching from

    Returns:
        List of Path objects pointing to all .md files found
    """
    path = Path(path)
    md_files: List[Path] = []

    for entry in path.iterdir():
        # skip hidden files/folders
        if entry.name.startswith('.'):
            continue

        if entry.is_dir():
            # recurse into non-hidden directories
            md_files.extend(get_markdown_files_recursive(entry))
        elif entry.is_file() and entry.suffix.lower() == '.md':
            md_files.append(entry)

    return md_files


def write_content_md(
    md_paths: List[Path],
    output_filename: str = "content.md"
) -> None:
    """
    Write a markdown file (output_filename) in base_dir that contains
    a bullet list of all md_paths, each rendered as a relative link.

    Args:
        md_paths: list of Path objects pointing to .md files
        output_filename: name of the markdown file to write
    """
    
    out_file = output_filename

    # sort for predictability
    md_paths_sorted = sorted(md_paths)

    with open(out_file, "w", encoding="utf-8") as f:
        f.write("# Table of Contents\n\n")
        for md in md_paths_sorted:
            # compute the path relative to base_dir
            rel = md.as_posix()
            # use the relative path as both link text and target
            f.write(f"- [{rel.replace('.md', '')}]({rel})\n")




def main():
    md_files = get_markdown_files_recursive("./")
    write_content_md(md_files, output_filename="content.md")


if __name__ == "__main__":
    main()

    

