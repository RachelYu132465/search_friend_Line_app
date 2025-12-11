# LINE Friend Search Automation

This project automates searching for LINE friends by phone number using the LINE desktop app. It reads phone numbers from a text file and drives the desktop UI via `pyautogui`.

## Requirements
- Python 3.10+
- Desktop environment with the LINE application already installed and logged in
- `pyautogui` and its dependencies (see `requirements.txt`)
- Reference screenshots in an `assets/` directory:
  - `search_friend_button.png`: the button that opens "Search Friends"
  - `phone_tab.png`: the tab or button for "Phone number" search

## Usage
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Create a `phone_numbers.txt` file with one phone number per line (UTF-8 encoded).
3. Capture the UI screenshots above and place them in `assets/`.
4. Run the automation:
   ```bash
   python line_automation.py --numbers phone_numbers.txt --assets assets/
   ```
   - Add `--line-executable /path/to/LINE` if the executable isn't discoverable automatically.

## Notes
- Keep the LINE window visible on the primary monitor to improve screenshot matching reliability.
- The script selects all text in the search box before typing each number, then presses Enter to submit the search.
- Delays (`time.sleep`) are kept short for responsiveness; adjust them if your machine needs more time between actions.
