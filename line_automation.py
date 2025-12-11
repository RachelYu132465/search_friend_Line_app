"""
Automate adding LINE friends from phone numbers listed in a text file.

The script expects that the LINE desktop app is already installed and logged in
on the machine where it is executed. It uses `pyautogui` for UI automation,
locating UI elements via reference images and simulating clicks/typing.
"""
import argparse
import os
import platform
import subprocess
import time
from pathlib import Path
from typing import Iterable, List

import pyautogui


def load_phone_numbers(path: Path) -> List[str]:
    """Load phone numbers from a UTF-8 text file, skipping blank lines."""
    if not path.exists():
        raise FileNotFoundError(f"Phone number list not found: {path}")

    numbers: List[str] = []
    for raw_line in path.read_text(encoding="utf-8").splitlines():
        number = raw_line.strip()
        if number:
            numbers.append(number)
    if not numbers:
        raise ValueError("No phone numbers found in the provided file.")
    return numbers


def open_or_focus_line_app(executable: str | None = None) -> None:
    """Attempt to open the LINE app or bring its window into focus."""
    if executable:
        subprocess.Popen([executable], start_new_session=True)
    elif platform.system() == "Darwin":
        subprocess.Popen(["open", "-a", "LINE"])
    elif platform.system() == "Windows":
        os.startfile("LINE")  # type: ignore[attr-defined]
    else:
        subprocess.Popen(["line"])

    # Give the app a moment to open or surface its window.
    time.sleep(2)

    windows = pyautogui.getWindowsWithTitle("LINE")
    if windows:
        windows[0].activate()
        return
    raise RuntimeError("Could not find a LINE window to focus.")


def _locate_and_click(image_path: Path, description: str) -> None:
    if not image_path.exists():
        raise FileNotFoundError(
            f"Expected image for '{description}' is missing: {image_path}"
        )

    location = pyautogui.locateCenterOnScreen(
        str(image_path), confidence=0.8, grayscale=True
    )
    if location is None:
        raise RuntimeError(
            f"Could not locate the '{description}' button. "
            "Ensure the LINE window is visible and the screenshot matches the UI."
        )
    pyautogui.click(location)


def navigate_to_phone_search(assets_dir: Path) -> None:
    """Navigate to the LINE friend search by phone number view."""
    search_friend_image = assets_dir / "search_friend_button.png"
    phone_tab_image = assets_dir / "phone_tab.png"

    _locate_and_click(search_friend_image, "Search Friends")
    time.sleep(0.5)
    _locate_and_click(phone_tab_image, "Phone number search tab")
    time.sleep(0.5)


def add_numbers_via_search(numbers: Iterable[str]) -> None:
    """Type each phone number into the search field and submit it."""
    for number in numbers:
        pyautogui.hotkey("ctrl", "a")
        pyautogui.typewrite(number)
        pyautogui.press("enter")
        time.sleep(0.8)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Search LINE friends by phone numbers listed in a text file",
    )
    parser.add_argument(
        "--numbers",
        type=Path,
        default=Path("phone_numbers.txt"),
        help="Path to a UTF-8 text file containing one phone number per line.",
    )
    parser.add_argument(
        "--assets",
        type=Path,
        default=Path("assets"),
        help="Directory containing reference screenshots for the UI buttons.",
    )
    parser.add_argument(
        "--line-executable",
        type=str,
        default=None,
        help=(
            "Optional path to the LINE executable. If omitted, the script will "
            "try common defaults based on the host platform."
        ),
    )
    args = parser.parse_args()

    numbers = load_phone_numbers(args.numbers)
    open_or_focus_line_app(args.line_executable)
    navigate_to_phone_search(args.assets)
    add_numbers_via_search(numbers)


if __name__ == "__main__":
    main()
